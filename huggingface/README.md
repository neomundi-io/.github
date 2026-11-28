# Hugging Face presence — how it is maintained

NeoMundi's Hugging Face organisation is [**neomundi-research**](https://huggingface.co/neomundi-research).
Its public face is an *organisation card*, which on the Hub is a public Space named `README`
with `sdk: static`.

**This directory is the single source of truth for that card.** It is edited here, validated by
CI, and published to the Hub by GitHub Actions. It is **not** edited on the Hub: the next sync
overwrites anything changed there, and the card's own footer says so.

| | |
|---|---|
| Source | [`huggingface/org-card/README.md`](org-card/README.md) |
| Target | [`spaces/neomundi-research/README`](https://huggingface.co/spaces/neomundi-research/README) |
| Rendered | <https://huggingface.co/neomundi-research> |
| Workflow | [`.github/workflows/sync-huggingface.yml`](../.github/workflows/sync-huggingface.yml) |
| Gate | [`huggingface/validate_card.py`](validate_card.py) |
| Authentication | GitHub OIDC trusted publisher — **no stored token** |

## What the mechanism does

```
push to main (huggingface/org-card/**)        workflow_dispatch
                 │                                   │
                 └───────────────┬───────────────────┘
                                 ▼
                        job: validate
              scope · Hub metadata · every link resolves
                                 │  fails → nothing is published
                                 ▼
                        job: sync      (needs: validate)
              GitHub OIDC token → 60-minute Hub token scoped to one repo
                        hf upload → verify what the Hub serves
```

The sync job never runs on a card that failed validation, because it declares `needs: validate`.

### The validation gate

`validate_card.py` refuses three classes of problem that are otherwise discovered in public:

1. **Scope.** The synced directory must contain `README.md` and nothing else. A directory sync
   publishes whatever is in the directory; a stray file lands on a public profile.
2. **Hub metadata.** The Hub parses the YAML front matter *before* accepting a commit.
   A `short_description` over **60 characters** raises `Invalid metadata in README.md` and nothing
   is uploaded — so the cap is checked here, where the failure is cheap and legible.
3. **Links.** Every external `http(s)` URL in the card must resolve. A card linking to a
   repository that has since been made private is worse than a card that omits it. `401`, `403`
   and `429` are reported as notes, not failures: the URL is reachable but gated or rate-limiting
   the probe.

Run it locally before pushing:

```sh
python huggingface/validate_card.py huggingface/org-card
# or, offline:
python huggingface/validate_card.py huggingface/org-card --no-network
```

### Authentication: a trusted publisher, not a secret

The job exchanges a short-lived GitHub OIDC token for a Hugging Face token that expires after
**60 minutes** and is **scoped to one repository**. There is no `HF_TOKEN` secret in this
repository: nothing to store, nothing to rotate, and a leaked token is useless within the hour.

| | Personal access token | Trusted publisher |
|---|---|---|
| Lifetime | until revoked | 1 hour |
| Storage | a CI secret | nothing to store |
| Rotation | manual | automatic, every run |
| If leaked | valid until revoked | at most ~1 hour, one repo |

The mechanism needs exactly two things: `permissions: id-token: write` on the job, and
`HF_OIDC_RESOURCE` naming the target. The `hf` CLI (`huggingface_hub >= 1.19.0`) detects GitHub
Actions, performs the exchange and uses the resulting token with no further configuration.

Reference: [Trusted Publishers](https://huggingface.co/docs/hub/trusted-publishers) ·
[GitHub Actions on the Hub](https://huggingface.co/docs/hub/repositories-github-actions)

## Enabling it — two steps, one of them manual

### 1. Declare the trusted publisher on the Hub

There is no API for this; it is a Hub settings page. On
<https://huggingface.co/spaces/neomundi-research/README/settings>, open **Trusted Publishers**,
add a publisher with provider **GitHub Actions**, and enter these claims — all of them must match
for the exchange to succeed:

| Claim | Value |
|---|---|
| Repository | `neomundi-io/.github` |
| Branch | `main` |
| Workflow | `sync-huggingface.yml` |

Leave **Read-only** unticked: the publisher must be able to write the card.

Pinning the branch and the workflow is deliberate. With `repository` alone, any workflow on any
branch of this repository could publish the card. The permission is fixed at creation: to change
it, delete the publisher and add it again.

Managing a repository's trusted publishers requires the **Write** role on that Hub repository.

### 2. Turn the sync on

The sync job is gated on a repository variable, so that merging the workflow does not publish
before the publisher exists:

```sh
gh variable set HF_SYNC_ENABLED --body true --repo neomundi-io/.github
```

Until that variable is `true`, every run validates the card and reports *Publishing disabled*
instead of failing. That is the expected state before step 1 is done.

## Testing it

```sh
# validation only, publishes nothing
gh workflow run sync-huggingface.yml --repo neomundi-io/.github -f validate_only=true

# full run: validate, publish, and verify what the Hub serves
gh workflow run sync-huggingface.yml --repo neomundi-io/.github
```

The last step of the sync job downloads the card the Hub actually serves and compares it byte for
byte with the commit that produced it. Publishing is not the same as being served, so the run only
succeeds once the two agree.

## Why not `huggingface/hub-sync`

[`huggingface/hub-sync`](https://github.com/huggingface/hub-sync) is the official action and it was
the first candidate. It is not used here, for two reasons that are properties of the action rather
than preferences:

1. **`hf_token` is a required input.** The action has no OIDC path, so adopting it means storing a
   permanent Hugging Face token as a repository secret — the thing a trusted publisher exists to
   remove. `hf auth token` can mint a short-lived token and feed it in, but that is the trusted
   publisher doing the work with the action wrapped around it, not the action's own mechanism.
2. **It calls `hf repos create --exist-ok` on every run.** A repo-scoped publisher token is scoped
   to one existing repository; a creation call on the namespace is a wider permission than this
   sync needs, and than the token grants.

What the action does that is worth keeping, and is reproduced here: it always excludes `.git*` and
nested `.git/` and `.github/` directories. This workflow does not need those exclusions, because
it syncs a directory that the validation gate requires to hold exactly one file.

One behaviour is deliberately **not** reproduced: `hub-sync` defaults to `delete_removed: true`,
which deletes every Hub file outside the upload set. Here the upload is a plain `hf upload` with no
`--delete`, so the Space's own `.gitattributes` and any Hub-side setting survive a sync. Only the
card is replaced.

## Scope of what is published

The card is the **only** thing this mechanism publishes, and the validation gate enforces that by
refusing any directory holding more than `README.md`.

Three Hugging Face resources exist and are **out of scope** on purpose:

| Resource | State | Why it is not synced |
|---|---|---|
| [`datasets/neomundi-research/grounded-s1`](https://huggingface.co/datasets/neomundi-research/grounded-s1) | **private** | Held pending a licence decision. It must stay private, and no automation should be able to flip that. |
| `neomundi-lab/law-e-framework` (model) | public, legacy | Lives under the `neomundi-lab` **user** account, not the organisation. Superseded content, pending an owner decision. |
| `neomundi-lab/law-e-framework` (dataset) | public, legacy | Same. |

Adding a resource to this mechanism means adding a directory, a target and a trusted publisher of
its own — never widening an existing publisher's scope.
