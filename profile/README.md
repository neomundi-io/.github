# NeoMundi. The AI thermometer.

Runtime governance observability for generative AI systems.

Early detection of generative instability signals, without access to content.

OBS for governance observability.
GOV for runtime orchestration when intervention becomes critical.

We provide the signal. You decide what to do with it.

Deployable across LLM stacks, agents, and orchestration layers.

<sub>FR · [Lire en français](./README.fr.md)</sub>

---

## Why It Matters

AI systems drift before problems become visible.

NeoMundi produces governance observability signals designed to surface early signs of:

- behavioral drift,
- inconsistencies,
- stability loss,
- patterns associated with hallucinations.

In OBS mode, without access to content.

---

## Two Deployment Modes

ControlTower™ is a control tower for generative AI governance.

Continuous observability in OBS mode. Runtime orchestration in GOV mode when intervention becomes critical.

|                  | **OBS** (Observability)                     | **GOV** (Governance)                          |
|------------------|---------------------------------------------|-----------------------------------------------|
| Purpose          | Governance observability                    | Runtime governance orchestration              |
| Timing           | Post-execution / continuous observability   | During generation                             |
| Privacy          | No content, metrics only                    | Transient content, no retention or logging    |
| Integration      | The LLM calls NeoMundi (post-stream)        | NeoMundi calls the LLM (runtime BYOK)         |
| Best suited for  | Most AI systems                             | Critical workflows                            |

> **OBS operating model.** NeoMundi produces governance observability signals usable by downstream agents and orchestration layers. Blocking, regenerating, escalating or rerouting remains under client control.

**Decision criterion: if a bad output reaches the user, is it recoverable?**

- **Recoverable** (alerts, downstream moderation, next-cycle correction): OBS is sufficient.
- **Non-recoverable** (medical advice, directly delivered legal advice, fiduciary financial decisions, critical infrastructure, Article 14 of the EU AI Act): GOV becomes necessary.

OBS is the natural entry point for most AI systems.

GOV is intended for situations where runtime governance and real-time orchestration become critical.

### Related Repositories

- OBS observability layer:
  https://github.com/neomundi-io/neomundi-obs

- GOV orchestration layer:
  https://github.com/neomundi-io/neomundi-gov

---

## Observable Instability Signals

NeoMundi produces governance observability signals associated with:

- internal contradictions,
- coherence loss,
- thematic drift,
- progressive instability,
- patterns associated with hallucinations.

NeoMundi does not determine whether a response is true.

NeoMundi produces signals designed to observe whether a response remains behaviorally stable.

---

## Validated on Real Systems

Current evaluations have been conducted primarily in GOV mode, within controlled runtime configurations.

- 5 LLM providers tested (cartography v1-2026-04-26)
- 3,904 generations analyzed (TruthfulQA)
- When NeoMundi FLAGs, the signal is confirmed in ≈76% of cases (current recall ≈15%)
- Early surfacing of instability signals before problems become visible

The instrument continues to evolve progressively.

Experimental factual validation layer planned for May 27, 2026.

📂 [Metrics, dataset, methodology](https://github.com/neomundi-io/llm-cartography)

---

## Use Cases

| Domain | Benefit | Mode |
|---|---|---|
| 🟣 **Agents** | Observe drift, reroute, escalate or regenerate according to runtime policy | **OBS** · GOV runtime |
| 🟢 **Compliance** | Timestamped audit trail and governance signals associated with generations | **OBS** · GOV runtime |
| 🟡 **Fine-tuning** | Observe behavioral differences between model versions | **OBS** · GOV runtime |
| 🔵 **SLA / Infra** | Behavioral observability and runtime supervision of generations | **OBS** · GOV runtime |

> Your decision, our signal.

---

## Produced Artifacts and Signals

Depending on OBS or GOV mode, NeoMundi may produce:

- Governance stability state (normalized from 0 → 1)
- Governance decision (PASS / FLAG)
- Runtime variation signals (ΔG, timestamped)
- Structured telemetry (analytics, compliance, runtime supervision)
- Auditable traces (session exports and reporting)

→ [Sample audit report (PDF)](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## Integration

Two modes, two endpoints.

The choice depends on the required level of criticality and runtime governance.

### OBS Mode · post-execution · metrics-only

No content transmitted. No provider key required.

Your metrics in, your governance signals out.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "sess_xxx",
    "metrics": { ... }
  }'
```

### GOV Mode · runtime · orchestration during generation

Bring Your Own Key. Full privacy.

Your provider key remains under your control.

NeoMundi processes the generative runtime stream in order to produce governance and orchestration signals, without retention or logging of prompts or responses.

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

The instrument is served through the ControlTower™ platform.

API key prefix: `ct_live_*`

→ [Quickstart](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/QUICKSTART)
→ **[100 free requests to test both modes](https://controltower.neomundi.io/pricing)**

---

## Two Privacy Models Adapted to Both Modes

|                              | **OBS**                                         | **GOV**                                              |
|------------------------------|-------------------------------------------------|------------------------------------------------------|
| Content (prompts, responses) | Never transmitted                               | Transient runtime flow, without logging or retention |
| Provider key                 | Never transmitted                               | BYOK                                                 |
| Storage                      | Governance metrics and artifacts only           | Governance metrics and artifacts only                |

Both modes are designed according to a privacy-by-design approach compatible with modern DPO, CISO, and compliance requirements.

---

## Roadmap

The infrastructure is active and continuing its industrialization process.

- May 27, 2026: Experimental factual validation layer
- Self-service platform in production
- Configurable thresholds and operator dashboard
- Progressive structuring of runtime telemetry (OBS / GOV)

Pilot operators remain prioritized for upcoming platform evolutions.

---

## FAQ

### OBS or GOV?

OBS = post-execution governance observability, without content transmission, metrics only.

GOV = runtime orchestration during generation, BYOK, transient runtime flow without logging or retention.

OBS is the natural entry point for most AI systems.

GOV is intended for situations where a bad output reaching a user becomes non-recoverable.

---

### What is the governance stability state?

It represents a normalized state of behavioral stability observed during or after an LLM generation.

NeoMundi does not measure whether a response is true. It produces signals designed to observe certain behavioral variations and instabilities.

---

### What data do you store?

OBS: no content transmitted.

GOV: transient runtime flow processed without logging or retention of prompts or responses.

Only governance metrics and artifacts are retained:
stability state, governance decision, timestamps, and associated reporting artifacts.

Your provider key (GOV mode) remains under your control.

---

### Does it work with my LLM?

OBS: any LLM, including local or unlisted models (you produce the metrics, NeoMundi receives the associated artifacts).

GOV: OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere, with automatic detection through your provider key.

---

### How is this different from LangSmith, Portkey, or Helicone?

These tools primarily observe and log workflows and application executions.

NeoMundi adds a complementary runtime governance and observability layer focused on behavioral signals and governance telemetry.

We do not replace your observability stack; we add a runtime governance layer.

---

### Is it compliant with the EU AI Act?

NeoMundi produces governance artifacts usable for traceability, auditability, and runtime reporting:
stability states, governance decisions, timestamps, and associated exports.

These artifacts may contribute to supervision and traceability requirements introduced by the EU AI Act (progressive enforcement beginning in August 2026).

---

## Documentation

- 📄 [Executive Brief — EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)
- 🔬 [Theoretical framework (Law E) — EN](https://doi.org/10.5281/zenodo.19385052)

---

> *Measure AI behavior continuously. If you run AI in production, you need a signal. Observe what's recoverable. Control what isn't.*

📧 contact@neomundi.io
