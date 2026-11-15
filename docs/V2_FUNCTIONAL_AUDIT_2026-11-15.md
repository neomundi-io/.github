# NeoMundi — functional audit of the product base

**Date:** 2026-11-15 · **Scope:** what the platform does *today*, with the evidence for each claim.

This document is the measurement. [`PRODUCT_ARCHITECTURE.md`](PRODUCT_ARCHITECTURE.md) is what we
build on top of it. Where the two disagree, this one wins.

> **Reading rule.** Every row marked 🟢 has a named proof: a file and line, a contract, a commit, a
> workflow run, or a command executed against production. Rows marked 🟡 are implemented but not
> reachable by a user in the current wiring. Rows marked 🔴 do not exist. **A README is never used
> as evidence here.**

---

## 1. Real inventory — what exists, at which revision

| Component | Repo | Visibility | Head at audit | Deployed / published |
|---|---|---|---|---|
| Measurement API (`govern`) | `Backend_plateforme_v2` | private | `11a2bf8` | **revision `03e2b344`**, image index `sha256:cc1f6eb7…`, started 2026-11-15T12:26:31Z, `restarts=0` |
| Portal API | same repo, `portal/` | private | `11a2bf8` | revision `fc5fadd9` |
| Control Tower V2 (frontend) | `Frontend_plateforme_v2` | private | **`40dac840`** | revision `40dac840` — **repo head == deployed container** |
| Python SDK | `neomundi-python-sdk` | public | `9d4db574` | **PyPI `2.1.0`**, wheel 63 605 B `bcaeeb76…`, uploaded 2026-11-15T14:06:56Z |
| Measurement MCP + plugin | `neomundi-measurement-mcp` | public | `f5f37138` | `0.2.0` live-tested; `0.3.0-rc.1` prepared |
| Evidence gateway | `neomundi-evidence-gateway` | public | `9a0c15d6` | 278 files; CI 4/4 |
| Evidence verifier | — | public | — | **PyPI `neomundi-evidence-verify` 0.1.0**, `requires_python >=3.11` |
| Evidence engine | `neomundi-evidence` / `-public` | **private** | `6c5bb4c5` | not installable by `pip` — 12 CLI programs |
| Station | `neomundi-station-public` / `neomundi-station` | public / private | `8f5745b9` | — |
| Measurement docs | `neomundi-runtime-measurement` | public | `0873c8a3` | — |
| Org profile | `.github` | public | `79ea1c6` | `profile/README.md` only — **no `docs/` before this PR** |

**Deployed-revision method.** Read on the host, read-only:
`docker inspect <container> --format '{{.Image}}'` then the image's OCI label
`org.opencontainers.image.revision`. The Docker tag proves nothing; the compose file pins `govern`
by **index** digest (`application/vnd.oci.image.index.v1+json`, confirmed via
`docker buildx imagetools inspect`).

🔴 **`main` of the backend is not the production lineage.** Measured 2026-11-15: production carries
**47 commits absent from `main`**, and `main` is not a descendant. Deploying `main` would remove
COHERE-019/024, API-020, API-017, `MODERATION_TIMEOUT` and API-012 — verified by content count, not
by ancestry. Any backend fix must be delivered as a candidate branch on the production revision.

### Published wire contracts — the only machine-readable description of the API

`/openapi.json` and `/docs` return **404** in production. The two schemas served by
`GET /v1/contracts/<name>` (public, unauthenticated, unmetered) are therefore the whole published
surface:

| Contract | SHA-256 | State |
|---|---|---|
| `govern-rest-1.0.json` | `46b0579f1d413ca75616d01eed1bef0dc317ff5e507dbcabc1dd146b7faab59c` | served; identical to the backend repo bytes |
| `govern-sse-1.0.json` | `358fc2ec1869471896d08c8e2cc0855b15def6433340a0506dae180733c7fefe` | unchanged since before 2026-11-15 |

🟢 Both byte-match the pinned public mirror: `scripts/check_live_wire_schemas.py` →
`BYTE_MATCH` / `PASS` on both documents. The SDK re-measures both digests on every test run from
`API_CONTRACT["wire_contracts"]`.

---

## 2. Capability matrix — INSTALL → TRACE → MEASURE → VERIFY → ACT

### INSTALL — 🟢 real

| Capability | State | Evidence |
|---|---|---|
| `pip install --upgrade neomundi` → 2.1.0 | 🟢 | executed in a fresh venv from a neutral directory: `Successfully installed … neomundi-2.1.0`; `importlib.metadata.version('neomundi') == '2.1.0'` |
| `trace`, `verify`, `verify_audit_certificate`, `govern`, `stream` on the client | 🟢 | asserted on the installed wheel, plus the release workflow's own smoke test |
| `py.typed` (PEP 561) | 🟢 | present in the installed package |
| Single runtime dependency (`httpx`) | 🟢 | `pyproject.toml`; install pulled only httpx + its transitive deps |
| No host assumed — `base_url` mandatory | 🟢 | `client.py::_validate_base_url` raises `ConfigurationError` |
| Key format checked locally before any call | 🟢 | `KEY_PREFIXES = ("ct_live_", "ct_test_", "ct_trial_")` |
| MCP / agent integration | 🟢 code, 🟡 release | MCP `0.2.0` live-tested; `0.3.0-rc.1` adds contract validation, not yet re-qualified |

### TRACE — 🟡 partial, and the limit is structural

| Capability | State | Evidence |
|---|---|---|
| Trace-only route on the API | 🔴 **does not exist** | all eight deployed routers read route by route (`app/main.py::_include_routers`); none accepts an interaction without measuring it |
| `client.trace()` context manager | 🟢 | `src/neomundi/trace.py`; latency measured with `time.monotonic()` around the caller's own block |
| Caller-side correlation id | 🟢 | `TraceRecord.client_trace_id`, paired with the server's `request_id` |
| Server retains that id | 🔴 | `metadata` is accepted by `GovernRequest` and **never read** by the route; the persisted object is the response plus `_audit_context` lengths |
| `audit.trace_id` usable as a key | 🔴 | `f"trace-{request_id[:8]}"` — 8 hex chars, not unique by construction |
| Observation acknowledged | 🟢 | body `request_id` + `X-Request-ID` header (⚠ **different values**: the header identifies the HTTP request, the body the observation) |
| Observation **recorded** | 🟢 since 2026-11-15 | `log_persisted` / `log_write` now on REST as on SSE. Verified by one authorised production call: `log_persisted: true`, `log_write: "inserted"` |
| Retrieval of that observation | 🟢 | `GET /v1/govern/{request_id}` → HTTP 200, same `request_id`. On replay `log_persisted` is `null` — a replay states no persistence verdict |
| SDK interprets the REST pair | 🟡 **by choice** | `TraceRecord.registered` stays `None` on REST; the pair lands in `unknown_fields` and is readable via `result.get("log_persisted")`. Typing it is a feature decision, not a doc fix |
| Streaming events | 🟢 | SSE `done` integrity verified: length, bytes and SHA-256 recomputed; `chunk` assembly checked against `done.response_text` |
| Data available for a trace list | 🟡 **6 fields** | `portal/schemas/usage.py::GovernLogItem` = `request_id`, `decision`, `g_score`, `confidence`, `mode`, `timestamp`. No signals, no `delta_g`, no `evaluators`, no `log_persisted` |

### MEASURE — 🟢 real, with named limits

| Capability | State | Evidence |
|---|---|---|
| Five signals | 🟢 | `stability_score`, `coherence_score`, `semantic_risk`, `factual_hallucination_score`, `semantic_instability_score` |
| Where they run | 🟢 | three of five on models hosted on the service's own machine; factuality and semantic instability call **one** subcontractor; hosting in Switzerland |
| `measured` vs `not_measured` never collapsed | 🟢 | `measured_signals` / `unmeasured_signals` with a reason per signal; a withheld aggregate is `null`, never `0.0` |
| Per-signal provenance | 🟢 | `evaluators` block with `prompt_template_hash`, `inference_config_hash`, `config_fingerprint` |
| `g_score`, `g_final`, `v_score`, `delta_g` | 🟢 exposed | ⚠ `delta_g` compares with the **previous request of the same account**, whatever the question; it is **not** a drift measure |
| Token count provenance | 🟢 | REST declares `token_count_source: "caller_declared"` as a **`const` of a required field** — the server counts nothing on that route. ⚠ `token_count_scope` is also `caller_declared`, which names no scope |
| SSE token counting | 🟢 | `provider_usage` / `chunk_count_fallback`; on the fallback path the unit is **`chunks`**, not tokens |
| Measurement version served | 🟢 `3.5.0` | ⚠ the SDK declares `verified_measurement_versions = ("3.3.0", "3.3.1")`. `3.5.0` is **deliberately not** declared verified — the warning a consumer sees is correct |
| Time series / history | 🟡 | `GET /v1/usage/logs` (portal) lists observations; the rich per-observation payload needs `GET /v1/govern/{id}` or `/dashboard` on the measurement service |
| Signal qualification | 🔴 planned | not audited, not available |

### VERIFY — 🟢 for emission authenticity, 🔴 for the observation↔archive link

Three different questions wear the same verb. The platform answers two of them.

| Question | Surface | Auth | Metered | State |
|---|---|---|---|---|
| Did this platform emit this record, unaltered? | `GET /v1/rgc/verify/{request_id}` — canonical hash recomputed from the source log **and** JWS Ed25519 verified | **none** | no | 🟢 probed in production |
| Does the digest printed on a Tier-03 certificate match the stored observation? | `GET /v1/audit/verify/{audit_trail_id}` | **none** | no | 🟢 probed |
| Is this Evidence archive intact? | `neomundi-evidence verify` (PyPI `neomundi-evidence-verify` 0.1.0) | — | — | 🟢 |
| **Is the AI answer true?** | — | — | — | 🔴 **nothing here answers this** |

- `valid` is **tri-state** and never folded: `true` / `false` / `null`. A **404** on `rgc/verify`
  means "no RGC contract was emitted", **not** "invalid signature". `audit/verify` **without
  `?sha256=`** returns `valid: null` — nothing was verified, because no digest is stored at issue
  time.
- Emitting an RGC contract is a separate, **TIER_03-only** call: `POST /v1/rgc/contracts/{id}`.
- The gateway exposes **2 of the engine's 12 entry points** (`verify`, `attestation`) —
  `contracts/gateway-request-v1.json::operation.enum`. Exit codes `0/1/2` come from the engine
  untranslated; **`3` = engine unavailable, `4` = request refused**, both meaning *no verification
  took place*. `verification_performed` is a required response field.
- 🟡 **The conformance corpus is not in the PyPI wheel.** `pip install` verifies *your* archives;
  replaying the published corpus needs a `git clone` of the gateway.
- 🔴 **No attested link between an observation and an Evidence archive.** Nothing in a `/v1/govern`
  response names an archive, and no archive carries a NeoMundi `request_id`.
  🟢 **But correlation is possible today at zero cost:** the gateway request contract has a
  `request_id` field that is *caller-supplied and echoed verbatim* — "the gateway never generates
  one". Passing the observation's `request_id` correlates the two by convention. **Convention is
  not attestation**, and the document must keep saying so.

### ACT — 🟡 export and attest yes, react no

| Capability | State | Evidence |
|---|---|---|
| Export one observation as PDF / JSON / CSV | 🟢 | `GET /v1/exports/{request_id}.{pdf,json,csv}`; the PDF is localised FR/EN and carries `X-Audit-Trail-Id` |
| Publicly verifiable audit certificate | 🟢 | `audit_trail_id` is `uuid5(NAMESPACE_URL, "neomundi-audit/{request_id}")` — deterministic from the observation, distinguishable from it |
| Emit a signed RGC contract | 🟢 TIER_03 | `POST /v1/rgc/contracts/{id}`; public key at `GET /v1/rgc/jwks` (`neomundi-rgc-2026-01`, Ed25519) |
| Monthly report | 🟢 | `GET /v1/reports`, `GET /v1/reports/snapshot` |
| Account audit trail | 🟢 | `GET /v1/reports/audit-trail` (portal) and `/{account_id}/audit-trail` (admin) |
| Bulk / structured export | 🟢 | portal `/structured-export`, `/zip`, `/export-data` |
| Event stream, activity feed | 🟢 | portal `/events/stream`, `/activity-feed` |
| Thresholds, alerting, SLA engine | 🔴 | **by design** the SDK embeds no threshold and derives no verdict; nothing in the API raises an alert |
| Drift detection | 🔴 | `delta_g` is explicitly not a drift measure |
| EU AI Act pack | 🔴 planned | the *inputs* exist (provenance, signed contracts, retrievable observations); the pack does not |

---

## 3. V2 visualization inventory — `Frontend_plateforme_v2` @ `40dac840`

`neomundi-control-tower` **4.1.0** · React 18.3 · **recharts 2.12.7** · zustand · react-router 6 ·
i18next (FR/EN) · Playwright + vitest.

**Charts actually present** — only three source files import recharts
(code search, `repo:neomundi-io/Frontend_plateforme_v2`):

| File | Lines | Chart |
|---|---|---|
| `src/features/governance/GovernanceDashboard.tsx` | 1038 | `AreaChart` + `Area` + `ReferenceLine` + `CartesianGrid` + `ResponsiveContainer` |
| `src/features/dashboard/DashboardPaid.tsx` | 576 | `BarChart` + `Bar` + `Tooltip` |
| `src/pages/ApiKeyDetailPage.tsx` | 473 | `BarChart` + `Bar` + `Tooltip` |

**Screens:** 8 pages under `src/pages/` (`ReportsPage`, `DocumentationPage`, `GettingStartedPage`,
`ApiKeyDetailPage`, `FaqPage`, `ContactPage`, `TermsPage`, `ErrorPage`) and 13 feature areas
(`dashboard` ×3 tiers, `governance`, `usage`, `api-keys`, `billing`, `invoices`, `admin` ×9 pages,
`affiliate`, `auth`, `newsletter`, `pricing`, `profile`, `settings` ×3).

**The measurement console already exists.** `GovernStreamPanel.tsx` (570 lines) drives a complete
single-interaction journey:

| Step | Call |
|---|---|
| post-call measurement | `POST /v1/govern` |
| live generation | `POST /v1/govern/stream`, consuming `chunk`, `governance_check`, `coherence_check`, `hallucination_check`, `error`, `done` |
| per-observation detail | `GET /v1/govern/{request_id}/dashboard` (`loadDash`) |
| export | `GET /v1/exports/{request_id}.{pdf,json,csv}` |
| signed contract | `POST /v1/rgc/contracts/{request_id}` |

### 🔴 The one rupture that explains everything else: two authentication domains

`GovernanceDashboard.tsx:219-222`, in the code itself:

> *"No on-mount governance-dashboard fetch: `GET /v1/govern/{id}/dashboard` lives on govern
> (X-API-Key auth), and the dashboard mount doesn't hold the user's API key. The GovernanceCard
> populates from the panel's `loadDash` after a live test (the user just entered the key there)."*

And `GovernStreamPanel.tsx:173-175`: *"The portal exposes no `/v1/govern` route, so this MUST…"*.

The browser session authenticates against the **portal**; every rich measurement read requires
**`X-API-Key`** on the **measurement service**. Consequences, all observed:

1. the observation list is limited to the portal's 6 fields;
2. there is **no per-observation detail screen** — no such page exists in `src/pages/`;
3. the governance dashboard is empty until the user pastes an API key into the panel;
4. TRACE and MEASURE history cannot be charted for an account without that key.

### Component → data → endpoint matrix

| Component | Data expected | Data available | Endpoint | State | Work left |
|---|---|---|---|---|---|
| `GovernStreamPanel` | live events + final envelope | all of it | `POST /v1/govern`, `POST /v1/govern/stream` (govern, `X-API-Key`) | 🟢 **works** | none |
| `GovernanceDashboard` card | full per-observation payload | all of it, **only after** a live test | `GET /v1/govern/{id}/dashboard` | 🟡 wired, not auto-loaded | resolve the key question |
| `GovernanceDashboard` G curve (`AreaChart`) | G time series per account | 🔴 no endpoint returns a signal series | — | 🟡 chart exists, series does not | add a series endpoint **or** widen `/v1/usage/logs` |
| Export buttons (PDF/JSON/CSV) | `request_id` + API key | yes | `GET /v1/exports/{id}.{pdf,json,csv}` | 🟢 **works** | none |
| RGC contract button | `request_id` + TIER_03 | yes | `POST /v1/rgc/contracts/{id}` | 🟢 **works** | none |
| `UsagePage` table | observation list | 6 fields | `GET /v1/usage/logs` (portal) | 🟢 works, shallow | enrich the schema or link to a detail view |
| `DashboardPaid` / `ApiKeyDetailPage` `BarChart` | consumption per day/key | yes | `GET /v1/usage/summary`, `/{key_id}/stats` | 🟢 **works** | none |
| `ReportsPage` | monthly report + audit trail | yes | `GET /v1/reports`, `/v1/reports/snapshot`, `/v1/reports/audit-trail` | 🟢 works | none |
| `ChecksConfigPage` | per-account check config | yes | `GET`/`PUT /v1/checks/config` | 🟢 works | none |
| ESI weights (β) | 4 coefficients | yes | `GET`/`PUT /v1/esi/coefficients` | 🟢 works, TIER_02+ | none |
| Evidence verdict panel | gateway verdict | 🔴 no screen exists | gateway CLI/JSON | 🔴 **absent** | new component |
| Observation detail page | full payload + provenance | available on the API | `GET /v1/govern/{id}` | 🔴 **absent** | new page (data already exists) |
| Timeline / execution explorer | ordered events per observation | SSE events are live-only, not replayable | — | 🔴 **absent** | needs event persistence |

---

## 4. Continuity of a single interaction

| Identifier | Produced by | Survives where | Limit |
|---|---|---|---|
| `client_trace_id` | caller (SDK) | **caller side only** | dropped by the route |
| `request_id` (body) | API | response, `governance_logs`, exports, RGC, dashboard | **the only reliable correlation key** |
| `X-Request-ID` (header) | middleware | that HTTP response | ⚠ **not** the observation id |
| `audit.trace_id` | API | response | derived, truncated, not unique |
| `audit_trail_id` | exports | PDF + public verify route | `uuid5` of the `request_id` — deterministic |
| Evidence `request_id` | **caller** | gateway response, echoed | correlation by convention, **not attested** |

**Works with no development:** install → trace → measure → retrieve → export → RGC emit → public
verify. Verified end to end today, one real call.
**Needs wiring only:** observation detail screen; passing `request_id` into the gateway.
**Needs light adaptation:** enrich `/v1/usage/logs`; resolve the two auth domains.
**Genuinely new:** signal time-series endpoint, replayable event timeline, Evidence verdict UI,
thresholds/SLA/alerting, EU AI Act pack.

---

## 5. Prioritised integration backlog

| # | Item | Why | Size |
|---|---|---|---|
| 1 | Resolve the two auth domains for measurement reads | unblocks items 2–4 and the whole account-level story | design + small backend |
| 2 | Observation detail screen | the data already exists on `GET /v1/govern/{id}` | front only |
| 3 | Signal time-series endpoint | the `AreaChart` is built and waiting | small backend |
| 4 | Enrich `/v1/usage/logs` with signals and `log_persisted` | removes most detail round-trips | small backend |
| 5 | Pass the observation `request_id` into the Evidence gateway | continuity by convention, zero cost | integration |
| 6 | Evidence verdict panel | makes VERIFY visible | front + gateway call |
| 7 | Attested observation↔archive link | the real gap behind VERIFY | design decision |
| 8 | Thresholds / SLA / alerting | required before any SLA claim | new product work |

---

## 6. Shortest commercial demonstration

Five minutes, one API key, no new code. What the user sees, screen by screen:

1. **INSTALL** — terminal: `pip install --upgrade neomundi` → `neomundi-2.1.0`.
2. **TRACE + MEASURE** — Control Tower → governance panel, paste the key, send a prompt. Text
   streams in; `governance_check`, `coherence_check`, `hallucination_check` events arrive during
   generation; `done` closes with integrity recomputed.
3. **Detail** — the governance card fills from `loadDash`: decision, G, the five signals with
   `measured`/`not_measured` per signal, evaluator fingerprints, measurement version.
4. **VERIFY** — "Contrat RGC" button → signed contract; then, **in a private window without any
   key**, open `GET /v1/rgc/verify/{request_id}` → `valid: true`, `payload_hash_match`,
   `signature_valid`, `key_id`.
5. **ACT** — export the PDF certificate; open `GET /v1/audit/verify/{audit_trail_id}` with the
   printed digest → verified, **without a key**.

Say out loud at step 5: this proves *emission and integrity*, **not** that the AI answer was true.

---

## 7. Commercial-readiness verdict

| Use case | Verdict |
|---|---|
| **AUDIT** — understand, reconstitute, verify | 🟢 **sellable today.** Retrievable observation, per-signal provenance, PDF/JSON/CSV export, two key-free public verification routes. Limits to state: no replayable event timeline, no observation detail screen yet. |
| **SLA** — monitor, qualify deviations | 🔴 **not sellable.** No threshold engine, no alerting, no drift measure (`delta_g` is not one), no signal time series. The raw material exists; the product does not. |
| **EU AI Act** — feed a conformity file | 🟡 **prepare, do not promise.** Provenance, signed contracts and retrievable observations are real inputs; no pack, no mapping to the text, no article-level coverage claim. |

**Overall: the base is real, the roof is not built.** Four of the five verbs are demonstrable today
on a single interaction, end to end, with public verification. The two things to never claim before
they exist: **ACT as a reaction capability**, and **"verified" as a statement about the truth of an
AI answer**.

🔴 One contract question stays open for an owner, not for an engineer: `MEASUREMENT_WIRE_CONTRACTS.md`
says *"do not regenerate published 1.0 in place"*, and the 2026-11-15 change added two optional
properties to the published REST `1.0`. It was applied under the reading that the sentence governs
*constraints* (none changed, `required` identical, and the SSE `1.0` already carried those two
properties). If the stricter reading is intended, that change needed `neomundi.govern.rest/1.1`.
