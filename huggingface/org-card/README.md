---
title: README
emoji: 📐
colorFrom: indigo
colorTo: yellow
sdk: static
pinned: false
short_description: Independent, signed runtime measurement of AI behavior
---

# NeoMundi measures. You decide.

**NeoMundi enriches existing observability with independent, signed and verifiable behavioral
measurement.**

**Keep your models, tools and infrastructure. Add an independent measurement layer.** NeoMundi
complements the stack you already run — it does not replace it. You attach the measurement where
your framework already has a hook, and the observation carries the latency and the token count
*that host actually observed*. A count the provider never published is reported as absent, never
as zero.

Our object of study is the **produced execution** — the response a system actually returned, under
conditions we recorded. Not the internals of a model, and not the truth of its content.

**We are not** a language model, a certification body, a compliance guarantee, or a leaderboard.
We publish no composite score and no model ranking.

This Hugging Face profile is the **scientific entry point**: experimental material, reproducible
verifications and corpus status. Technical documentation lives on
[GitHub](https://github.com/neomundi-io), which remains the source of truth.

## Integrate with your existing AI stack

One measurement API. **Seven integrations**, each published on PyPI under Apache-2.0. You do not
write a measurement call per call site.

| Your stack | Package | Maturity | Evidence |
|---|---|---|---|
| **LangChain** | [`langchain-neomundi`](https://pypi.org/project/langchain-neomundi/) | beta | **E2** |
| **Langfuse** | [`langfuse-neomundi`](https://pypi.org/project/langfuse-neomundi/) | beta | **E2** |
| **LiteLLM** | [`litellm-neomundi`](https://pypi.org/project/litellm-neomundi/) | beta | **E2** |
| **Microsoft Agent Framework** | [`agent-framework-neomundi`](https://pypi.org/project/agent-framework-neomundi/) | beta | **E2** |
| **MLflow** | [`mlflow-neomundi`](https://pypi.org/project/mlflow-neomundi/) | beta | **E2** |
| **OpenAI Agents SDK** | [`openai-agents-neomundi`](https://pypi.org/project/openai-agents-neomundi/) | beta | **E2** |
| **OpenTelemetry** | [`otel-neomundi`](https://pypi.org/project/otel-neomundi/) | beta | **E2** |

```sh
pip install langchain-neomundi
```

**The evidence level is computed, not claimed.** An integration advertising **E2** carries a proof
under `evidence/` that CI opens and reads, and whose numbers must agree with what it asserts —
otherwise the pull request does not land. The scale runs E0 (nothing probative) to E3
(independently reproduced by a third party).

🔴 **Every submitted observation is a billed measurement.** There is no trace-only route. Read the
cost section of your integration before pointing it at a busy application.

[Integration library](https://github.com/neomundi-io/neomundi-integrations) ·
[catalogue](https://github.com/neomundi-io/neomundi-integrations/blob/main/CATALOG.md) ·
[candidate hosts](https://github.com/neomundi-io/neomundi-integrations#future-integrations--roadmap)

Or call the instrument directly from Python:

```sh
pip install neomundi
```

`neomundi` **2.2.0** (PyPI, 2026-11-26, Apache-2.0) declares `measurement_version` **3.5.0**
verified on REST, and makes `token_count` and `latency_ms` optional — a metric your host never
published is **named as absent** rather than substituted with a zero the server would read as the
most favourable value. REST and SSE both passed live qualification on 2026-11-26.
[Python SDK](https://github.com/neomundi-io/neomundi-python-sdk)

## Reproduce a verification

No account, no API key, no network, no cost. Python standard library only — Python 3.11+.

```sh
pip install neomundi-evidence-verify
git clone --depth 1 https://github.com/neomundi-io/neomundi-evidence-gateway
cd neomundi-evidence-gateway

# what can this install actually do, and what does each absence cost?
neomundi-evidence doctor

# a valid archive from the public conformance corpus
neomundi-evidence verify verifier/conformance/fixtures/A-valid/A-05-archive-valid/archive.zip

# the same command on a tampered archive
neomundi-evidence verify verifier/conformance/fixtures/D-tampered/D-10-archive-member-tampered/archive.zip
```

Observed with verifier **0.2.0**, conformance corpus **1.3.0**, protocol `evidence-protocol/1`
revision `1.0.0-rc.1`:

```
# valid archive
BILAN : 17 PASS, 0 FAIL, 4 NOT TESTED          exit code 0

# tampered archive
BILAN : 16 PASS, 1 FAIL, 4 NOT TESTED          exit code 1
Ce dossier ne doit pas etre presente comme verifie.
```

**Read the exit code, not the absence of red text.** `0` means *no control failed* — and that
includes controls that **could not be performed**. `NOT TESTED` is not success.

The `NOT TESTED` lines are deliberate. They name what no local check can establish: the
fingerprints of replayed inputs, export completeness, ledger chaining, and the archive's origin
and timestamp. Adding `--strict` turns an unmet **required** guarantee into exit code `2` — and on
this valid archive it does exactly that, returning `2` for the fingerprints of replayed inputs,
because the public fixture ships no input corpus to check them against. No verdict line changes;
only the code. A signature establishes commitment and custody, not fact.

Two optional extras buy two specific controls — `[attestations]` for Ed25519/JWS signatures,
`[timestamps]` for reading an OpenTimestamps proof tree. Without them the tool reports
`NOT TESTED`, never `PASS`. The verifier reports in French.

[Verifier guide](https://github.com/neomundi-io/neomundi-evidence-gateway/blob/main/verifier/README.md) ·
[verification limits](https://github.com/neomundi-io/neomundi-evidence-gateway/blob/main/references/LIMITS.md) ·
[`neomundi-evidence-verify` on PyPI](https://pypi.org/project/neomundi-evidence-verify/)

## Measure → Observe → Verify

Three distinct functions, one chain.

| Stage | Function | Source |
|---|---|---|
| **Measure** | Produce observations and measurements of an execution, with status, evaluator coverage and provenance. REST and SSE. | [neomundi-runtime-measurement](https://github.com/neomundi-io/neomundi-runtime-measurement) |
| **Observe** | Run experimental protocols: controlled campaigns, retained conditions, append-only hash-chained records, exportable results. | [neomundi-station-public](https://github.com/neomundi-io/neomundi-station-public) |
| **Verify** | Check archive integrity, trace artifacts, verify Ed25519 attestations — and report what cannot be established. | [neomundi-evidence-gateway](https://github.com/neomundi-io/neomundi-evidence-gateway) |

The [Python SDK](https://github.com/neomundi-io/neomundi-python-sdk), the
[integration library](https://github.com/neomundi-io/neomundi-integrations) and the
[MCP server](https://github.com/neomundi-io/neomundi-measurement-mcp) are access interfaces to the
instrument, not additional stages. The Evidence **engine** is private; the **verifier** and the
**gateway** are public, and the gateway forwards engine submissions without verifying them itself.

## What a measurement contains

| Field | Records |
|---|---|
| Signals | Measurements computed on the execution. Semantics in the [metric contract](https://github.com/neomundi-io/neomundi-metric-contract). |
| Status | `measured`, `degraded` or `not_measured`. |
| Evaluator coverage | Which evaluators ran, which did not, and why — see [what evaluators can and cannot establish](https://github.com/neomundi-io/neomundi-metric-contract/blob/main/EVALUATORS.md). |
| Provenance | Operator, model requested, whether the operator attested the model actually served, and `measurement_version`. |

An unavailable signal is reported as unavailable. It is never replaced by zero, and interpretation
stays with the consuming system.

## Reference corpora

Frozen as `20261105T1200_GEL_CORPUS_GATE0` (5 November 2026) at `measurement_version` **3.3.1** —
the version of the instrument at freeze time, not the current one.

| | MED | GROUNDED-S1 |
|---|---|---|
| Regime | `live`, seven named operators | `synthetic`, no operator |
| Records | 844 | 151 |
| Observations | 209 | 30 |
| Measurements | 208, all `measured` | 15 `measured`, 8 `degraded`, 7 `not_measured` |
| Content published | No — derived archive only | Yes |

Operators measured in MED: `anthropic`, `cohere`, `deepseek`, `google`, `infomaniak`, `moonshot`,
`openai`. Two of the seven returned `requested_only` — the operator did not state which model
actually served the request, so only the requested model is established.

**Not yet hosted here.** GROUNDED-S1 is packaged as a Hub dataset — 151 ledger records, projected
to remove three fields that made a private source conversion deducible — and held back pending a
licence decision. MED's content is not redistributable at all. Publishing a corpus depends on
redistribution rights and a licence, decided per corpus. We do not publish placeholder datasets,
and **no dataset is publicly available from this profile today.**

## Repositories

Source is public and inspectable on GitHub.

| Repository | What it is | Licence |
|---|---|---|
| [neomundi-python-sdk](https://github.com/neomundi-io/neomundi-python-sdk) | Python client, REST and SSE · `neomundi` 2.2.0 | Apache-2.0 |
| [neomundi-integrations](https://github.com/neomundi-io/neomundi-integrations) | Seven framework integrations, each with a computed evidence level | Apache-2.0 |
| [neomundi-evidence-gateway](https://github.com/neomundi-io/neomundi-evidence-gateway) | Public verifier and gateway for execution evidence packages | Apache-2.0 |
| [neomundi-ai-observatory](https://github.com/neomundi-io/neomundi-ai-observatory) | Open entry point for the AI Observatory | Apache-2.0 |
| [neomundi-runtime-measurement](https://github.com/neomundi-io/neomundi-runtime-measurement) | Measurement signals, REST/SSE and interoperability contracts | not granted |
| [neomundi-station-public](https://github.com/neomundi-io/neomundi-station-public) | Record contracts for the append-only hash-chained ledger · [station.neomundi.org](https://station.neomundi.org) | not granted |
| [neomundi-measurement-mcp](https://github.com/neomundi-io/neomundi-measurement-mcp) | MCP server and desktop plugin · source 0.3.0-rc.1, last live-qualified 0.2.0 | see repository |
| [neomundi-use-cases](https://github.com/neomundi-io/neomundi-use-cases) | Documented pilots with protocols, results and limitations | not granted |
| [neomundi-metrology-validation](https://github.com/neomundi-io/neomundi-metrology-validation) | Methodological consolidation and reproducibility framework | not granted |

Contracts: [metric contract](https://github.com/neomundi-io/neomundi-metric-contract) ·
[measurement interoperability (RGC)](https://github.com/neomundi-io/neomundi-measurement-interoperability) ·
[interpretation contract](https://github.com/neomundi-io/interpretation-contract)

**Reuse terms differ per repository, and the list above says which.** The SDK, the integration
library, the Evidence gateway and the AI Observatory are Apache-2.0. The repositories marked *not
granted* carry no `LICENSE` file: they are published to be read, run and audited, but
redistribution and derivative use are not licensed. Ask before reusing:
[contact@neomundi.io](mailto:contact@neomundi.io). The **hosted Runtime Measurement API remains
proprietary and commercially metered** — an open-source SDK does not include free hosted API
access. See the SDK's
[licensing boundaries](https://github.com/neomundi-io/neomundi-python-sdk/blob/main/LICENSE_NOTICE.md).

## Research

**Research question.** How can runtime signals help observe, compare and govern generative systems
across real-world contexts?

Current work: runtime stability, factual validity, semantic risk, behavioral drift, cost and
efficiency, professional use cases, red-team cases, and instrument qualification. The goal is not
to rank models. It is to qualify a measurement instrument through open, inspectable and repeatable
experiments.

[AI Observatory](https://github.com/neomundi-io/neomundi-ai-observatory) ·
[metrology validation](https://github.com/neomundi-io/neomundi-metrology-validation) ·
[use cases and pilots](https://github.com/neomundi-io/neomundi-use-cases) ·
[product architecture](https://github.com/neomundi-io/.github/blob/main/docs/PRODUCT_ARCHITECTURE.md)

We collaborate on bounded, documented pilots. [contact@neomundi.io](mailto:contact@neomundi.io)

## Limitations

These are properties of the instrument, not disclaimers appended to it.

- **A measurement is not a verdict on content.** It describes properties of a produced text. It
  does not establish that an answer is correct, medically sound, or legally compliant.
- **No ranking.** No composite score, no ordering of models or providers.
- **End-to-end qualification is partial.** The frozen Q-2 chain followed one authorized real
  execution through Measure → Observe → Verify, with an Ed25519 signature verified independently
  against the published trust reference. The technical chain passed; the overall verdict remains
  `PARTIAL` on specific scientific and provenance guarantees. Q-2 is a preserved private reference,
  not a downloadable sample.
- **Provenance has a ceiling.** `requested_only` means the served model was never attested by the
  operator.
- **Campaign identity is instrument-verifiable, not third-party reproducible.** The recomputation
  recipe is unpublished. An external evaluation on 6 November 2026, holding the frozen data,
  concluded *not established* for one campaign. Treat campaign hashes as verifiable with the
  instrument and not without it.
- **Tamper detection is scoped.** 10/10 on the named falsification suite; other suites differ.
- **Interface maturity differs.** REST, SSE, SDK, integrations and MCP are not at the same
  qualification level — see
  [integration status](https://github.com/neomundi-io/neomundi-runtime-measurement#integration-status)
  and each integration's own limitations.
- **Thresholds, alerting and drift are not products.** The measurement layer supplies raw material;
  it embeds no threshold and derives no verdict.
- **Programme support is not endorsement.** NeoMundi participates in the
  [OVHcloud Startup Program](https://startup.ovhcloud.com/) and
  [NVIDIA Inception](https://www.nvidia.com/en-us/startups/), with
  [Infomaniak](https://www.infomaniak.com/) as infrastructure partner. None of these implies
  certification or endorsement of results.

## Links

[github.com/neomundi-io](https://github.com/neomundi-io) — source of truth ·
[neomundi.io](https://neomundi.io) — platform ·
[live demo](https://neomundi.io/demo/) ·
[neomundi.org](https://neomundi.org) — research ·
[station.neomundi.org](https://station.neomundi.org) — live Station ·
[data protection](https://github.com/neomundi-io/neomundi-io-data-protection) ·
[contact@neomundi.io](mailto:contact@neomundi.io)

---

<sub>This card is generated from `huggingface/org-card/README.md` in
[`neomundi-io/.github`](https://github.com/neomundi-io/.github) and synchronised to the Hub by
GitHub Actions. Edit it there, not here.</sub>
