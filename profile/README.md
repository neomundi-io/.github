# NeoMundi. The AI thermometer.

**Continuous AI stability measurement.**
Post-hoc or runtime, depending on criticality.

We provide the signal. You decide what to do with it.

*Deployable in front of any LLM stack.*

<sub>FR · [Lire en français](./README.fr.md)</sub>

---

## Why it matters

AI systems drift before they fail.

NeoMundi measures continuously, before failure becomes visible:

- drift
- inconsistency
- collapse
- hallucination patterns

In OBS mode, without access to content.

---

## Two deployment modes

ControlTower™: a control tower for AI generation. Continuous observation, intervention only when necessary.

|              | **OBS** (Observatory)     | **GOV** (Governance)         |
|--------------|---------------------------|------------------------------|
| Purpose      | Continuous monitoring     | Active runtime control       |
| Timing       | After generation          | During generation            |
| Privacy      | Metrics only              | Transient content, EU only   |
| Integration  | Minimal friction          | Deeper integration           |
| Best for     | Most AI systems           | Critical workflows           |

> **OBS action model.** NeoMundi emits a continuous stability signal, usable by downstream agents or orchestration layers. Block, regenerate, or escalate: the decision stays with the client.

**Decision criterion: if a bad output reaches a user, is it recoverable?**

- **Recoverable** (alert, downstream moderation, correction in the next cycle): OBS is enough.
- **Unrecoverable** (medical advice, legal counsel delivered directly to end users, fiduciary financial decisions, critical infrastructure, EU AI Act Art. 14): GOV is required.

OBS is the natural entry point for most AI systems. GOV kicks in when runtime control becomes critical.

---

## What NeoMundi detects

- internal contradictions
- loss of coherence
- topical drift
- progressive instability
- hallucination patterns

> NeoMundi doesn't say whether a response is true.
> NeoMundi measures whether it stays stable.

---

## Measurement and detection

NeoMundi computes a stability score (G) from a multivariate signal capturing semantic coherence, consistency, and structural stability during generation.

The instrument evaluates and updates the signal continuously, enabling immediate detection of drift and instability.

NeoMundi catches instability before it becomes visible:

- Internal contradictions
- Loss of precision
- Topical drift
- Structural incoherence

Drift appears before failure. We measure it in real time. NeoMundi doesn't say whether it's true. It says whether it's coherent.

---

## Validated on real systems

Cartography v1-2026-04-26 — 3,904 measurements on TruthfulQA × 5 generative services.

NeoMundi doesn't catch everything yet (~15% recall), **but when it flags, it's right ~76% of the time**. A reliable signal for governance.

The instrument is sharpening. Truth Module live on May 27, 2026.

📂 Full metrics, dataset, and methodology: [llm-cartography](https://github.com/neomundi-io/llm-cartography).

---

## Use cases

| 🟣 Agents | 🟢 Compliance | 🟡 Fine-tuning | 🔵 SLA / Infra |
|---|---|---|---|
| Stop. Retry. Reroute. | Trace & prove. | Measure drift. | Prove continuity. |
| Live stability signal injected into agent decision loops. | Timestamped audit trail. Every generation scored, every drift flagged. | Quantify behavioral gaps between model versions. | Behavioral supervision beyond latency. Generation quality, measured. |
| **Mode: OBS** | **Mode: OBS** *(GOV if real-time blocking is required)* | **Mode: OBS** | **Mode: OBS** |

> Your decision, our signal.

---

## What each generation produces

**Standard outputs**

- Stability score (0 → 1)
- Decision (PASS / FLAG)
- Drift signal (timestamped)

**Advanced outputs**

- Structured datasets (analytics, fine-tuning, compliance)
- Real signal. Real scoring. Real result.

→ [Sample audit report (PDF)](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## Integration

Two modes, two endpoints. Pick yours using the decision criterion above.

### OBS Mode — post-hoc, metrics-only

No content transmitted. No provider key. Your metrics in, your score out.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "sess_xxx",
    "metrics": { ... }
  }'
```

### GOV Mode — runtime, control during

**Bring Your Own Key. Full privacy.** Your provider key stays under your control. NeoMundi measures the stability signal of generation without ever reading or storing the content of your prompts or responses.

```bash
curl -X POST https://api.neomundi.io/v1/govern/stream \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Your prompt here",
    "model": "gpt-4o",
    "provider_api_key": "sk-xxx"
  }'
```

The instrument runs on the ControlTower platform. API key prefix: `ct_live_*`.

→ [Full integration guide](#)
→ **[100 free requests to test both modes](https://controltower.neomundi.io/pricing)**

---

## Two privacy postures, both maximal

| | **OBS** | **GOV** |
|---|---|---|
| Content (prompts, responses) | Never transmitted | Transient, no log, no retention |
| Provider key | Never transmitted | BYOK, under your control |
| Storage | Metrics + score only | No content stored |
| Hosting | EU | EU |

Both modes are designed to pass DPO, CISO, or Compliance review without compromise.

---

## Roadmap

The infrastructure is live. It's scaling.

- **May 27, 2026**: Truth Module live (factual verification beyond coherence) + self-service platform in production (client-configurable thresholds, operator dashboard).

Current pilot operators have priority on every update.

---

## FAQ

**What's the difference between OBS and GOV?**
OBS measures post-hoc, metrics-only: no content, no provider key transits. It's the entry point, suited to most use cases. GOV measures at runtime, enriching the thermodynamic signal with a semantic layer: the stream transits through our layer for the strict duration of measurement. Use it when a bad output reaching a user is unrecoverable.

**What is the stability score?**
It measures the internal coherence of an LLM response in real time — not its truthfulness. NeoMundi doesn't verify facts; it detects the drift that precedes the error.

**What data do you store?**
In OBS: no content data, neither in transit nor at rest. Only governance metrics are recorded (score, decision, timestamp).
In GOV: your prompts are neither read nor stored. Your provider API key stays under your control. Only governance metrics are recorded.

**Does it work with my LLM?**
In OBS: yes, any model, including local or unlisted ones (you compute metrics locally and transmit them to us).
In GOV: OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere — automatic detection from your key. If your provider isn't listed, contact us.

**How is this different from LangSmith, Portkey, or Helicone?**
Those tools observe and log. NeoMundi measures and signals — before an unstable response reaches your user (GOV) or to let your agents act before delivery (OBS). We don't replace your observability stack; we add the missing measurement layer to it.

**Is it EU AI Act compliant?**
NeoMundi contributes to the traceability and auditability requirements of the EU AI Act by producing a complete per-session audit trail: score, decision, timestamp, PDF export. Enforcement date is August 2026.

---

## Repositories

NeoMundi's GitHub ecosystem:

- **[llm-cartography](https://github.com/neomundi-io/llm-cartography)** — public scientific instrument. v1 cartography, dataset, versioned methodology.
- **controltower-quickstart** *(coming soon)* — integration examples, OBS vs GOV demo, one-click Colab notebook.

---

## Documentation

- 📑 **Executive Brief (FR)** — synthetic view for decision-makers → [NeoMundi_Executive_Brief_FR.pdf](#)
- 📐 **Full methodology** — versioned scientific spec → [llm-cartography](https://github.com/neomundi-io/llm-cartography)
- 📂 **Reference dataset v1-2026-04-26** — DOI Zenodo → [10.5281/zenodo.19762753](https://doi.org/10.5281/zenodo.19762753)
- 🔬 **Theoretical framework (Law E)** — DOI Zenodo → [10.5281/zenodo.19385052](https://doi.org/10.5281/zenodo.19385052)

---

> *Measure AI behavior continuously. If you operate AI in production, you need a signal. Observe what's recoverable. Control what isn't.*

📧 contact@neomundi.io
