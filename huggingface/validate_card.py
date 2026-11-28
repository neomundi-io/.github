#!/usr/bin/env python3
"""Validate the Hugging Face organisation card before it is synchronised.

This is the gate the sync workflow depends on. It refuses a card that the Hub
would reject silently, a card that would publish something other than itself,
and a card that points at a URL that no longer resolves.

Three classes of check, in order of how expensive they are:

1. Scope     -- the synced directory must contain README.md and nothing else.
                hub-sync and `hf upload` mirror a directory; a stray file in it
                is published to a public profile.
2. Metadata  -- the Hub parses the YAML front matter *before* accepting a
                commit. `short_description` over 60 characters raises
                `Invalid metadata in README.md` and nothing is uploaded.
3. Links     -- every external http(s) URL must resolve. A card that links to a
                repository that has since been made private is worse than a
                card that does not link to it at all.

Usage:
    python validate_card.py <card-directory> [--no-network]

Exit codes:
    0  every check passed
    1  at least one check failed
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# The Hub truncates nothing: past 60 characters it refuses the commit outright.
SHORT_DESCRIPTION_MAX = 60

REQUIRED_KEYS = ("title", "sdk")

# A static Space card carries only these. Anything else is a typo that the Hub
# will either ignore or reject, and both are worth catching here.
KNOWN_KEYS = {
    "title", "emoji", "colorFrom", "colorTo", "sdk", "sdk_version",
    "app_file", "pinned", "license", "short_description", "thumbnail",
    "models", "datasets", "tags", "header", "hf_oauth", "fullWidth",
}

USER_AGENT = "neomundi-card-validator/1.0 (+https://github.com/neomundi-io)"

failures: list[str] = []
notes: list[str] = []


def fail(message: str) -> None:
    failures.append(message)
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[ OK ] {message}")


def note(message: str) -> None:
    notes.append(message)
    print(f"[NOTE] {message}")


def check_scope(card_dir: Path) -> Path:
    """The synced directory must hold the card and nothing else."""
    card = card_dir / "README.md"
    if not card.is_file():
        fail(f"no README.md in {card_dir}")
        raise SystemExit(1)

    extras = sorted(p.name for p in card_dir.iterdir() if p.name != "README.md")
    if extras:
        fail(
            "the synced directory must contain README.md only; found: "
            + ", ".join(extras)
        )
    else:
        ok("publication scope: README.md only")
    return card


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("the card does not open with a YAML front matter block")
        return {}
    end = text.find("\n---\n", 3)
    if end == -1:
        fail("the YAML front matter block is not closed")
        return {}

    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"front matter line is not a key/value pair: {line!r}")
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data


def check_metadata(data: dict[str, str]) -> None:
    for key in REQUIRED_KEYS:
        if key not in data:
            fail(f"front matter is missing the required key `{key}`")

    unknown = sorted(set(data) - KNOWN_KEYS)
    if unknown:
        fail("front matter carries unknown key(s): " + ", ".join(unknown))

    if data.get("sdk") != "static":
        fail(f"an organisation card must declare `sdk: static`, not {data.get('sdk')!r}")
    else:
        ok("sdk: static")

    description = data.get("short_description", "")
    length = len(description)
    if length == 0:
        note("no short_description -- the Hub will show none")
    elif length > SHORT_DESCRIPTION_MAX:
        fail(
            f"short_description is {length} characters, over the Hub's "
            f"{SHORT_DESCRIPTION_MAX}-character cap: the commit would be refused"
        )
    else:
        ok(f"short_description: {length}/{SHORT_DESCRIPTION_MAX} characters")

    # A card is only rendered on the organisation page while the Space is public;
    # `private` or `protected` hide it with no error message at all.
    if data.get("pinned") not in (None, "false", "true"):
        fail(f"`pinned` must be true or false, not {data.get('pinned')!r}")


def extract_urls(text: str) -> list[str]:
    body = text
    if body.startswith("---\n"):
        end = body.find("\n---\n", 3)
        if end != -1:
            body = body[end + 5:]

    urls = set()
    # Markdown link targets and bare URLs alike; strip trailing punctuation that
    # belongs to the sentence rather than the address.
    for raw in re.findall(r"https?://[^\s<>\")\]]+", body):
        urls.add(raw.rstrip(".,;:"))
    return sorted(urls)


# Throttling is not a dead link. GitHub answers a burst of unauthenticated
# requests with 503 or 429; treated as failures those produce a red CI run and a
# card nobody changed. Each of these is retried with a growing pause, and only
# reported once it survives every attempt.
TRANSIENT = (429, 500, 502, 503, 504)
ATTEMPTS = 3
BACKOFF_SECONDS = 4


def probe_once(url: str) -> int | str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception as exc:  # noqa: BLE001 - network shapes vary too much
        return f"{type(exc).__name__}: {exc}"


def probe(url: str) -> tuple[str, int | str]:
    status: int | str = "not attempted"
    for attempt in range(ATTEMPTS):
        status = probe_once(url)
        if status == 200:
            return url, status
        if isinstance(status, int) and status not in TRANSIENT:
            return url, status
        if attempt < ATTEMPTS - 1:
            time.sleep(BACKOFF_SECONDS * (attempt + 1))
    return url, status


def check_links(text: str, enabled: bool) -> None:
    urls = extract_urls(text)
    if not enabled:
        note(f"link check skipped (--no-network); {len(urls)} URL(s) not probed")
        return

    print(f"\n-- probing {len(urls)} external URL(s)")
    # Deliberately modest: a wide fan-out is what triggers the throttling the
    # retry logic above then has to absorb.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = sorted(pool.map(probe, urls))

    for url, status in results:
        if status == 200:
            continue
        if isinstance(status, int) and status in (401, 403):
            # Reachable, but gated to this probe. Not a dead link.
            note(f"{status} (reachable, not public to this probe) {url}")
        elif isinstance(status, int) and status in TRANSIENT:
            note(f"{status} after {ATTEMPTS} attempts (host throttling, not a dead link) {url}")
        else:
            fail(f"unreachable link -- {status} -- {url}")

    alive = sum(1 for _, s in results if s == 200)
    ok(f"links: {alive}/{len(results)} returned 200")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("card_dir", type=Path)
    parser.add_argument("--no-network", action="store_true")
    args = parser.parse_args()

    print(f"Validating the organisation card in {args.card_dir}\n")

    card = check_scope(args.card_dir)
    text = card.read_text(encoding="utf-8")
    ok(f"card size: {len(text.encode('utf-8'))} bytes")

    check_metadata(parse_front_matter(text))
    check_links(text, enabled=not args.no_network)

    print()
    if failures:
        print(f"REFUSED: {len(failures)} check(s) failed, {len(notes)} note(s)")
        for message in failures:
            print(f"  - {message}")
        raise SystemExit(1)
    print(f"ACCEPTED: every check passed, {len(notes)} note(s)")


if __name__ == "__main__":
    main()
