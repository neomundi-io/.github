# NeoMundi. The AI thermometer.

Runtime observability and governance signals for generative AI systems.

NeoMundi is a runtime signal layer deployable above LLM stacks, agents, and orchestration systems.

It helps AI teams measure instability, drift, and governance-relevant signals before enforcing policies.

One API call. BYOK. Privacy first. No content storage.

We provide the signal.  
Your system, policy, or responsible operator keeps decision authority.

OBS first. GOV when ready.

Call the instrument. Observe the drift. Configure your thresholds. Govern in real time.

<sub>FR · [Lire en français](./README.fr.md)</sub>

---

## NeoMundi Runtime Governance Framework

NeoMundi is evolving from thermometer to spectrometer: from a runtime stability signal toward a multidimensional measurement layer for AI system behavior during execution.

A runtime governance signal must meet three minimal requirements: it must be observable, interpretable and interoperable.

The NeoMundi Runtime Governance Framework organizes these requirements across several public methodological repositories dedicated to observability, informational metrics, interpretation, interoperability and runtime governance for AI systems.

Together, these repositories form the minimal foundations of an industrializable AI governance infrastructure: measure, interpret, transmit, decide, trace.

### Main repositories - Core repositories

- [`neomundi-signal-adaptation-framework`](https://github.com/neomundi-io/neomundi-signal-adaptation-framework/blob/main/README_EN.md)  
  SAL layer: conceptual entry point of the framework, where heterogeneous sources are adapted into a canonical state measurable by NeoMundi.

- [`runtime-telemetry-signals`](https://github.com/neomundi-io/runtime-telemetry-signals)  
  Public definitions of runtime telemetry signals, including G, ΔG and governance states.

- [`informational-metrics`](https://github.com/neomundi-io/informational-metrics)  
  Public methodological notes on volumetry, volumetric density, informational energy and informational density.

- [`energy-stability-index`](https://github.com/neomundi-io/energy-stability-index)  
  Conceptual documentation of the Energy Stability Index as a composite governance indicator.

- [`validity-and-grounding`](https://github.com/neomundi-io/validity-and-grounding)  
  Public methodological documentation on validity, grounding, hallucination detection and the limits of proof-related signals.

- [`neomundi-io-data-protection`](https://github.com/neomundi-io/neomundi-io-data-protection)  
  Privacy architecture, data minimization, BYOK, no-content-storage principles and OBS/GOV processing modes for the NeoMundi runtime measurement instrument.

- [`runtime-interoperability-contract`](https://github.com/neomundi-io/runtime-interoperability-contract)  
  Minimal interoperability semantics between measurement, orchestration and proof-anchoring layers.

- [`interpretation-contract`](https://github.com/neomundi-io/interpretation-contract)  
  Methodological boundaries for interpreting signals, metrics and governance decisions.

- [`neomundi-obs`](https://github.com/neomundi-io/neomundi-obs)  
  OBS layer: post-hoc observability, without runtime orchestration.

- [`neomundi-gov`](https://github.com/neomundi-io/neomundi-gov)  
  GOV layer: runtime governance and orchestration during generation.

- [`Boundary Tension contract`](https://github.com/neomundi-io/Boundary_Tension_contract)  
  Conceptual research repository dedicated to boundary tension signals in runtime AI systems.
The objective is not to establish absolute truth.

The objective is to make AI generation behavior observable, interpretable, interoperable, auditable and governable at runtime.

---

## Why It Matters

A governance signal has value only if it can be understood, transmitted, interpreted and used by a real system.

The challenge is not just to produce a score.  
The challenge is to produce a signal that can operate inside a governance infrastructure: readable by a machine, interpretable by a human, traceable by an audit, and actionable by an orchestration layer.

NeoMundi builds its signals according to this industrial requirement:

- observability: the signal describes a measurable surface;
- interpretability: the signal declares what it means and what it does not mean;
- interoperability: the signal can circulate across independent layers;
- governability: the signal can support a decision without replacing it;
- auditability: the signal can be documented, timestamped and reviewed after execution.

An isolated signal is not an infrastructure.  
A specified, contextualized and interoperable signal can become a governance building block.

This is the role of the NeoMundi Runtime Governance Framework: making generative behaviors observable, interpretable and governable before drift becomes invisible, irreversible or costly.

---

## Two Deployment Modes

ControlTower™ acts as a control tower for the governance of generative AI systems.

OBS provides governance observability after generation.  
GOV provides runtime orchestration when intervention during execution becomes critical.

|                  | **OBS** (Observability)                          | **GOV** (Governance)                          |
|------------------|--------------------------------------------------|-----------------------------------------------|
| Purpose          | Governance observability                         | Runtime governance orchestration              |
| Moment           | Post-execution / continuous observability        | During generation                             |
| Confidentiality  | No content, metrics only                         | Transient content, with no retention or logs  |
| Integration      | The system calls ControlTower after generation   | ControlTower calls the LLM at runtime (BYOK)  |
| Best suited for  | Most AI systems                                  | Critical workflows                            |

> **OBS action model.** ControlTower produces governance observability signals that can be used by downstream agents or orchestration layers. Block, regenerate or escalate: the decision remains with the client.

**Decision criterion: if a bad output reaches the user, can it be recovered?**

- **Recoverable**: alert, downstream moderation, correction in the next cycle → OBS is enough.
- **Non-recoverable**: medical advice, legal advice delivered directly, fiduciary financial decisions, critical infrastructure, reinforced human oversight → GOV becomes necessary.

OBS is the natural entry point for most AI systems.  
GOV applies when runtime governance and real-time orchestration become critical.

---

## Use Cases

These use cases may require different levels of depth: simple signal, advanced metrics, reinforced auditability or compliance reporting.

| Use Case | What NeoMundi Provides | Natural Mode |
|---|---|---|
| 🟣 **Agents** | Runtime signals to observe drift, reroute, escalate or retry according to the orchestration policy | **OBS** · GOV runtime |
| 🟡 **Fine-tuning** | Informational metrics to compare behavioral gaps across model versions, prompts or datasets | **OBS** |
| 🟢 **Compliance** | Timestamped audit trail, governance decisions, reports and generation traceability | **OBS** · GOV runtime |
| 🔵 **SLA / Infra** | Behavioral supervision of generations, degradation detection and runtime incident documentation | **OBS** · GOV runtime |

> Your decision, our signal.

---

## Types of Observable Signals

NeoMundi does not determine on its own whether an answer is true.

It produces runtime signals that help observe stability variations, coherence losses, progressive drift, regime breaks, or patterns compatible with hallucinations.

These signals are not absolute proofs.  
They make AI generations more observable, interpretable, traceable and governable.

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

## Produced Artifacts and Signals

Depending on the OBS or GOV mode, NeoMundi can produce several families of observability and governance artifacts.

These artifacts are not absolute truths.  
They are designed to make AI generations observable, interpretable, traceable and governable.

NeoMundi can notably produce:

- **Governance stability state**: a normalized signal associated with a generation or execution segment.
- **Runtime stability variation**: ΔG, the observed variation across several execution windows.
- **Informational metrics**: volumetry, volumetric density, informational energy, informational density.
- **Composite index**: ESI, a multidimensional synthetic governance reading.
- **Governance decisions**: ALLOW, FLAG, BLOCK or equivalent states according to the applied policy.
- **Structured telemetry**: events, timestamps, request identifiers and associated signals.
- **Auditable traces**: exports, reports, logs and reporting artifacts depending on the mode and integration level.

> A signal observes.  
> A decision guides action.  
> Interpretation remains contextual.

---

## Why NeoMundi is easy to test

NeoMundi does not require teams to migrate their stack or expose their full observability pipeline.

A first test only requires:

1. One API call
2. The client’s own LLM provider key
3. OBS mode enabled
4. No prompt/output storage by NeoMundi
5. Optional configurable thresholds for GOV mode later

You can start by observing the signal, compare it with your own outputs, then decide whether to activate governance thresholds.
Call the instrument. Observe when your AI drifts. Set your thresholds. Govern in real time.

## Integration

Add a runtime signal layer to your agents, LLM applications or orchestration systems in minutes.

A single API call allows your system to receive actionable signals to observe, decide, retry, reroute, escalate or document an AI generation.

Depending on the level of criticality, you can start with OBS, test GOV, then progressively configure your thresholds, action policies and exports from ControlTower™.

### What the Integration Provides

- **OBS**: post-hoc observability, metrics only, with no content transmitted.
- **GOV**: runtime orchestration during generation, with the client-side provider key, BYOK.
- **Runtime signals**: stability, variation, regime, governance decision.
- **Auditability**: timestamps, traces, exports, reports.
- **Interoperability**: signals usable by agents, orchestrators and control layers.
- **Sovereign deployment possible**: dedicated installation, Docker image, controlled environment depending on integration needs.

- [Quickstart API & NeoMundi Sandbox](https://github.com/neomundi-io/neomundi-sandbox)  
  Getting started documentation, integration examples and access to test resources.

---

## Call the instrument. Observe the drift. Set your thresholds. Govern.

NeoMundi starts in OBS mode: it measures runtime stability without enforcing decisions.
Teams can watch drift patterns, compare signals with their own evaluations, and tune thresholds safely.

When ready, they can activate GOV mode to flag, review, or block responses according to their own governance rules.

No migration.
No content storage.
Your provider key.
Your thresholds.
Your governance.

---

## FAQ

**OBS or GOV?**  

OBS is the post-execution observability mode: ControlTower™ receives metrics or observation artifacts, without transmission of full semantic content.

GOV is the runtime governance mode: ControlTower™ intervenes during generation, with the provider key remaining on the client side, transient stream processing, and no logging or retention of prompts or responses.

OBS is the natural entry point for most AI systems.  
GOV becomes relevant when a bad output reaching the user would be difficult to recover from.

---

**What is the governance stability state?**  

It is a normalized state associated with the behavioral stability observed during or after an AI generation.

NeoMundi does not claim to determine on its own whether an answer is true.  
NeoMundi produces signals that help observe certain variations, instabilities, drifts or behavioral transitions.

---

**What data is stored?**  

In OBS mode: no full semantic content is transmitted.

In GOV mode: the stream is processed transiently during execution, with no logging or retention of prompts or responses.

Only governance metrics, signals and artifacts may be retained: stability state, decision, timestamp, technical identifiers and associated reporting.

The provider key used in GOV mode remains under the client’s control.

---

**Does it work with my LLM?**  

OBS can be used with any AI system capable of sending metrics or observation artifacts to ControlTower™.

GOV is designed to work with compatible LLM providers through a BYOK logic, depending on available integrations.

---

**How is this different from LangSmith, Portkey or Helicone?**  

These tools are mainly focused on application observability, tracing, logs, costs, workflows and performance.

NeoMundi adds a complementary runtime governance layer oriented around signals: stability, variation, informational density, governance decisions and auditability.

NeoMundi does not replace your observability stack.  
NeoMundi adds a behavioral measurement and governance layer.

---

**Does NeoMundi cover certain EU AI Act requirements by design?**

NeoMundi does not replace a complete compliance process.

However, ControlTower™ contributes by design to certain AI governance requirements: runtime control, logging, traceability, supervision and auditability.

The produced artifacts, stability signals, governance decisions, timestamps, technical identifiers, exports and reports, can support documentation, monitoring and risk management for AI systems.

---

## Documentation

- 📄 [Executive Brief — EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)
- 🔬 [Theoretical framework (Law E) — EN](https://doi.org/10.5281/zenodo.19385052)

---

*Measure AI behavior continuously.  
If you operate AI in production, you need a signal.  
Observe what can be recovered. Control what cannot.*

contact@neomundi.io
