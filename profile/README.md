# NeoMundi. The AI thermometer.

**Continuous AI stability measurement.**

Early detection of generative risk, without access to content.

Post-hoc or runtime, depending on criticality.

We provide the signal. You decide what to do with it.

*Deployable in front of any LLM stack, agent or orchestrator.*

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

|              | **OBS** (Observatory)         | **GOV** (Governance)             |
|--------------|-------------------------------|----------------------------------|
| Purpose      | Continuous monitoring         | Active runtime control           |
| Timing       | Continuous post-hoc stream    | During generation                |
| Privacy      | No content, metrics only      | Transient content, no retention, no logs |
| Integration  | LLM calls NeoMundi (post-stream) | NeoMundi calls LLM (BYOK runtime) |
| Best for     | Most AI systems               | Critical workflows               |

> **OBS action model.** NeoMundi emits a continuous stability signal, usable by downstream agents or orchestration layers. Block, regenerate, or escalate: the decision stays with the client.

**Decision criterion: if a bad output reaches a user, is it recoverable?**

- **Recoverable** (alert, downstream moderation, correction in the next cycle): OBS is enough.
- **Unrecoverable** (medical advice, legal counsel delivered directly to end users, fiduciary financial decisions, critical infrastructure, EU AI Act Art. 14): GOV is required.

OBS is the natural entry point for most AI systems. GOV kicks in when runtime control becomes critical.

---

## Detected instabilities

- internal contradictions
- loss of coherence
- topical drift
- progressive instability
- hallucination patterns

> NeoMundi doesn't say whether a response is true.
> NeoMundi measures whether it stays stable.

---

## Validated on real systems

- **5 LLM providers** tested (cartography v1-2026-04-26)
- **3,904 generations** analyzed (TruthfulQA)
- When NeoMundi flags, it's right **≈76% of the time** (15% current recall)
- Early detection, before visible failure

The instrument keeps refining. Truth module live on May 27, 2026.

📂 [Metrics, dataset, methodology](https://github.com/neomundi-io/llm-cartography)

---

## Use cases

| Domain | Benefit | Mode |
|---|---|---|
| 🟣 **Agents** | Detect drift, stop, retry, reroute | **OBS** · GOV runtime |
| 🟢 **Compliance** | Timestamped audit trail, every generation scored | **OBS** · GOV runtime |
| 🟡 **Fine-tuning** | Quantify deltas between model versions | **OBS** · GOV runtime |
| 🔵 **SLA / Infra** | Behavioral supervision, generation quality measured | **OBS** · GOV runtime |

> Your decision, our signal.

---

## Every generation returns

- **Stability score** (0 → 1)
- **Decision** (PASS / FLAG)
- **Drift signal** (ΔG, timestamped)
- **Structured telemetry** (analytics, fine-tuning, compliance)
- **Audit-ready traces** (PDF export per session)

→ [Sample audit report (PDF)](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## Integration

Two modes, two endpoints. Choose based on the criterion above.

### OBS mode, post-hoc, metrics-only

**No content transmitted. No provider key.** Your metrics in, your score out.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "sess_xxx",
    "metrics": { ... }
  }'
```

### GOV mode, runtime, control during generation

**Bring Your Own Key. Full privacy.** Your provider key stays under your control. NeoMundi measures the generation's stability signal without ever reading or storing your prompts or responses.

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

The instrument is served by the ControlTower platform. API key prefix: `ct_live_*`.

→ [Quickstart](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/QUICKSTART)
→ **[100 free requests to test both modes](https://controltower.neomundi.io/pricing)**

---

## Two privacy postures, both maximal

|                              | **OBS**                       | **GOV**                                |
|------------------------------|-------------------------------|----------------------------------------|
| Content (prompts, responses) | Never transmitted             | Transient, no logs, no retention       |
| Provider key                 | Never transmitted             | BYOK, under your control               |
| Storage                      | Metrics + score only          | Metrics + score only                   |

Both modes are designed to pass DPO, CISO, or Compliance review without compromise.

---

## Roadmap

The infrastructure is active. It's scaling to production.

- **May 27, 2026**: Truth module (factual verification beyond coherence)
- Self-service platform in production
- Configurable thresholds, operator dashboard

Pilot operators get priority on every update.

---

## FAQ

**OBS or GOV?**
OBS = continuous monitoring, no access to content, metrics only. GOV = control during generation, BYOK, transient content with no retention. OBS is the entry point for most cases. GOV kicks in when a bad output reaching a user isn't recoverable.

**What is the stability score?**
It measures the internal coherence of an LLM response in real time, not its truthfulness. NeoMundi detects the drift that precedes the error.

**What data do you store?**
No content, neither in OBS nor in GOV. Only governance metrics are recorded: score, decision, timestamp. Your provider key (in GOV) stays under your control.

**Does it work with my LLM?**
OBS: any LLM, including local or unlisted ones (you compute the metrics, we receive them). GOV: OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere, auto-detected from your key.

**How does this differ from LangSmith, Portkey, Helicone?**
These tools observe and log after the fact. NeoMundi measures and signals during generation. We don't replace your observability stack, we add the missing measurement layer.

**EU AI Act compliant?**
NeoMundi produces a complete audit trail per session (score, decision, timestamp, PDF export) that supports traceability and auditability requirements. Application deadline: August 2026.

---

## Repositories

NeoMundi's GitHub ecosystem:

- **[llm-cartography](https://github.com/neomundi-io/llm-cartography)**: public scientific instrument, cartography v1, dataset, versioned methodology.
- **controltower-quickstart** *(coming soon)*: integration examples, OBS vs GOV demo, clickable Colab notebook.

---

## Documentation

- 📄 [Executive Brief — EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)
- 🔬 [Cadre théorique (Loi E) — FR](https://doi.org/10.5281/zenodo.19385052)

---

> *Measure AI behavior continuously. If you run AI in production, you need a signal. Observe what's recoverable. Control what isn't.*

📧 contact@neomundi.io
