## 🌐 Choose your language

[**🇬🇧 English**](https://github.com/neomundi-io/.github/blob/main/profile/README.md) · [**🇫🇷 Lire la version française**](https://github.com/neomundi-io/.github/blob/main/profile/README.fr.md)

---

# NeoMundi

## Fundamental measurement layer for AI behavior

**A common measurement layer from which multiple uses can derive and around which heterogeneous AI infrastructures can articulate.**

NeoMundi measures behavioral variability, stability and regime changes in AI systems at runtime.

Its signals can support multiple uses — observation, drift detection, audit, governance, orchestration and control — while being consumed by independent infrastructures that retain their own architecture, function and decision authority.

**One fundamental measurement layer. Multiple uses. Multiple infrastructures.**

**Your system. Your decisions. Our signal.**

---

## NeoMundi Resources

[**Reference Framework**](https://zenodo.org/records/21821522)
Foundational architecture and conceptual framework for NeoMundi runtime metrology.

[**Metric Contract & Measurement Reference**](https://github.com/neomundi-io/neomundi-metric-contract)
Semantic definitions, measurement boundaries, reproducibility, traceability and portability of NeoMundi runtime measurement signals.

[**Metrology Validation**](https://github.com/neomundi-io/neomundi-metrology-validation)
Experimental validation, calibration, reproducibility and evidence framework for NeoMundi measurement signals.

[**Measurement Interoperability**](https://github.com/neomundi-io/neomundi-measurement-interoperability/tree/main)
Signed, versioned and independently verifiable interoperability for transporting NeoMundi runtime measurement signals across independent infrastructures.

[**Executive Brief**](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)
Concise overview of NeoMundi’s positioning, measurement layer and operational model.

[**AI Observatory**](https://github.com/neomundi-io/neomundi-ai-observatory)
Public observations, barometers, mappings and longitudinal analysis of AI behavior at runtime.

[**Launchers**](https://github.com/neomundi-io/neomundi-launchers)
Reference implementations for deploying concrete operational workflows around NeoMundi measurement signals.

[**Use Cases**](https://github.com/neomundi-io/neomundi-use-cases)
Documented pilots, experimental articulations and operational integrations using NeoMundi measurement signals.

[**Sandbox**](https://controltower.neomundi.io/welcome)
Access the NeoMundi measurement environment and test the runtime measurement layer.


---

## What NeoMundi does in 30 seconds

NeoMundi provides a **fundamental measurement layer for AI behavior at runtime**.

It can be used to:

- measure stability, behavioral variability and regime changes;
- produce structured, timestamped and auditable runtime signals;
- detect certain situations requiring enhanced attention;
- support supervision, audit, orchestration and governance use cases;
- transmit these signals to independent infrastructures through interoperable interfaces.

**One fundamental measurement layer. Multiple uses. Multiple infrastructures.**

NeoMundi provides the signal.  
The operator, its system or its policy layer retains decision authority.

---

## Why it matters

Generative AI systems are increasingly integrated into real-world workflows: autonomous agents, business assistance, infrastructure, compliance, support, healthcare, legal services and finance.

An output can be fluent and plausible while still displaying instability, drift, a regime change or insufficient grounding.

The challenge is therefore not merely to produce more logs or scores.

It is to produce an **operational measurement** that is:

- machine-readable;
- interpretable by humans;
- transmissible to third-party infrastructures;
- traceable over time;
- usable to trigger actions according to an explicit policy.

> An isolated signal is data.  
> A measured, contextualized and interoperable signal can become a building block for decision-making.

---

## OBS first. GOV when the context requires it.

NeoMundi provides two integration modes depending on system criticality and when measurement needs to occur.

| | **OBS — Privacy-first snapshot** | **GOV — Real-time governance** |
|---|---|---|
| **Principle** | Your system calls NeoMundi after a generation | NeoMundi enters the execution loop |
| **Objective** | Observe, compare and document | Supervise and govern in real time |
| **Timing** | After generation | During generation |
| **Data processed** | Snapshot limited to the data required for analysis | Stream processed transiently |
| **Signals** | Stability state, alerts and auditable traces | Stability state, `ΔG`, alerts and governance signals |
| **Retention** | No storage of prompts or responses | No storage of prompts or responses |
| **Natural fit** | Most AI systems | Critical or difficult-to-recover workflows |

### The right decision criterion

> If a poor output reaches the user, can it be recovered from?

**If yes**, OBS is generally the natural starting point.

Your system sends a snapshot to NeoMundi to measure certain behaviors, detect variations and retain an actionable trace.

**If no**, GOV becomes relevant.

NeoMundi enters the execution loop, tracks signal evolution in real time and enables a supervision policy to react during execution.

---

## Measurement signals and artifacts

Depending on the integration mode, NeoMundi can produce signals and artifacts including:

- **behavioral stability**: a normalized state associated with a generation or execution window;
- **stability variation**: evolution of the signal across observation windows;
- **regime changes**: observable transitions in system behavior;
- **coherence signals**: indications related to the evolution of coherence during execution;
- **informational metrics**: complementary measurements related to the informational structure and density of generations;
- **FLAG**: a conservative signal indicating that an output requires enhanced attention;
- **structured telemetry**: events, timestamps, technical identifiers and associated signals;
- **auditable traces**: exports, reports and artifacts documenting what occurred.

These signals do not, in isolation, constitute absolute proof of truth, error or compliance.

They must be interpreted in context and according to the policy of the system consuming them.

---

## Experimental validation

NeoMundi has now produced and analyzed **more than 200,000 observations** across longitudinal measurement campaigns, barometers, mappings, controlled experiments and field pilots.

The current observational program covers **12 AI systems** across heterogeneous providers, models, protocols and execution configurations.

These experiments contribute to the study of:

- behavioral stability and variability;
- regime changes and longitudinal drift;
- reproducibility of measurement signals;
- actionability of the signals and scores produced;
- interoperability across heterogeneous AI infrastructures.

➡️ [NeoMundi AI Observatory](https://github.com/neomundi-io/neomundi-ai-observatory)  
➡️ [NeoMundi Research Observatory](https://neomundi.org/en/home)

### Consolidating the measurement framework

NeoMundi's experimental program does not rely on a single validation axis.

In addition to longitudinal observation, dedicated work on **reproducibility** and **actionability** is being used to progressively consolidate the measurement framework.

The objective is to establish whether the signals produced are not only observable, but also:

1. repeatable under comparable conditions;
2. sensitive to meaningful behavioral changes;
3. interpretable within explicit methodological boundaries;
4. usable by operators, governance layers and independent infrastructures.

This work contributes to the progressive validation of NeoMundi's signals, metrics and derived scores.

### Initial FLAG signal validation corpus

Earlier controlled campaigns used specifically to evaluate the precision of the `FLAG` signal represented a cumulative corpus of **10,160 generations**.

| Campaign | Scope | Generations analyzed |
|---|---:|---:|
| Mapping v1 — 2026-04-26 | 5 LLM providers | 3,904 |
| TruthfulQA cohort v2 — 2026-05-17 | 8 anonymized LLM providers | 6,256 |
| **Total** | | **10,160** |

When a `FLAG` was triggered, a problematic output was confirmed in approximately **76% of cases** across this validation corpus.

| Campaign | FLAGs triggered | Confirmed problematic outputs | Observed precision |
|---|---:|---:|---:|
| Mapping v1 — 2026-04-26 | 437 | 331 | 75.7% |
| TruthfulQA cohort v2 — 2026-05-17 | ≈ 394 | ≈ 301 | ≈ 76.4% |
| **Cumulative total** | **≈ 831** | **≈ 632** | **≈ 76%** |

### How to read these results

NeoMundi does not claim to detect every error.

The instrument currently prioritizes signal precision over exhaustive coverage:

> it is better to flag fewer outputs usefully than to overwhelm operators with false positives.

The `FLAG` results represent one early validation axis within a broader metrological program.

They must be interpreted within their methodological limits, including dependence on the corpus, providers, thresholds and confirmation protocols used.

Validation is progressively strengthened through **longitudinal observation, reproducibility studies, actionability studies, methodological audits, independent articulations and field pilots**.

---

## Use cases

A single measurement layer can support multiple use cases without imposing the infrastructure that consumes it.

| Use case | What NeoMundi signals can enable | Measurement mode |
|---|---|---|
| **Autonomous agents** | Detect certain variations or drifts so that an orchestrator can trigger escalation, retry or rerouting mechanisms | OBS · GOV |
| **Compliance and audit** | Produce timestamped measurements and actionable traces to document system behavior | OBS · GOV |
| **Evaluation and comparison** | Compare behavioral differences across models, prompts, datasets, versions or configurations | OBS |
| **AI infrastructure and SLA** | Identify certain behavioral degradations and document their evolution over time | OBS · GOV |
| **Sensitive workflows** | Provide runtime signals that can feed enhanced supervision or an external control policy | GOV |
| **Longitudinal monitoring** | Measure how a system evolves over time and identify regime changes or behavioral profile shifts | OBS |
| **Research and metrology** | Produce comparable observations to study stability, variability, reproducibility and behavioral transitions | OBS |

**These uses derive from the same measurement layer.**

NeoMundi does not impose the application, orchestrator or policy that consumes its signals.

Launchers, agents, governance systems, evidence infrastructures, audit tools and business applications can consume NeoMundi signals while retaining their own architecture, function and decision authority.

> **One fundamental measurement layer. Multiple uses. Multiple infrastructures.**

---

## Integration and interoperability

NeoMundi is designed as an independent layer that can articulate with existing LLM applications, agents, orchestrators, observability platforms, governance systems and business infrastructures.

### Integration principles

- progressive integration through APIs;
- compatibility with multiple models, providers and architectures;
- **BYOK** approach where supported by the integration mode;
- minimization of transmitted data;
- no storage of prompts or responses;
- production of structured signals and artifacts;
- separation between **measurement authority** and **decision authority**;
- ability for external infrastructures to consume and interpret signals;
- controlled or dedicated deployments according to requirements.

NeoMundi is not intended to replace existing infrastructures.

Instead, the measurement layer can be consumed by independent systems that retain their own logging, orchestration, governance, evidence or control functions.

### LLM provider integration

NeoMundi runtime interfaces enable the measurement layer to articulate with supported LLM providers and models.

The integration guide documents provider connectivity, model configuration and API key management for the relevant integration modes.

➡️ [LLM Provider Integration Guide](https://github.com/neomundi-io/controltowerai-docs/blob/main/providers.md)

### Interoperability

Interoperability is a core principle of the NeoMundi architecture.

The objective is for a measurement signal to be produced by one layer, transmitted to another, interpreted within an explicit framework and then consumed by an independent infrastructure — without implicitly transferring authority between these different functions.

The **Runtime Interoperability Contract** documents the minimal semantics required for this articulation between independent layers.

➡️ [Runtime Interoperability Contract](https://github.com/neomundi-io/runtime-interoperability-contract)

---

## Privacy and operational sovereignty

NeoMundi follows a data-minimization principle.

Prompts and responses are not stored.

Depending on the integration mode, only the information required for measurement, traceability and the production of associated artifacts may be retained.

NeoMundi also uses a **self-hosted semantic judge** for certain analyses.

This component runs on infrastructure controlled by NeoMundi in order to limit dependence on external services for this measurement function.

This architecture serves three objectives:

- **privacy**: limit data exposure;
- **resilience**: reduce critical external dependencies;
- **operational sovereignty**: retain control over the measurement and processing chain.

---

## Product status

NeoMundi clearly distinguishes between the measurement layer available today, integrations being experimented with alongside partners, and components still undergoing industrialization.

| Status | Meaning |
|---|---|
| **Available now** | Measurement APIs and surfaces, runtime signals, sandbox, methodological documentation and initial integration interfaces |
| **Pilots and articulations** | Integration with agents, orchestrators, governance infrastructures, evidence systems and independent applications |
| **Industrialization** | Extension of the measurement domain, consolidation of metrics, standardized interoperability, performance improvements and deployment options |

The trajectory is to progressively strengthen **the measurement itself and its ability to be consumed by heterogeneous infrastructures**, rather than centralizing downstream use cases within NeoMundi.

---

## Main repositories — Core repositories

NeoMundi is progressively publishing the methodological foundations of its approach.

Each repository documents a specific function: measuring AI behavior, checking certain responses, interpreting signals correctly, transmitting results, protecting data or deploying the OBS and GOV modes.

### Measure AI behavior

- [`neomundi-signal-adaptation-framework`](https://github.com/neomundi-io/neomundi-signal-adaptation-framework/blob/main/README_EN.md)  
  Explains how to transform different data sources into a common format so that they can be compared and measured.

- [`runtime-telemetry-signals`](https://github.com/neomundi-io/runtime-telemetry-signals)  
  Documents the signals used to monitor AI behavior during operation, including its stability level and how this signal evolves over time.

- [`informational-metrics`](https://github.com/neomundi-io/informational-metrics)  
  Presents the metrics used to analyze the quantity, structure and informational density of generated responses.

- [`energy-stability-index`](https://github.com/neomundi-io/energy-stability-index)  
  Documents a composite index designed to summarize several dimensions of stability. This index is part of NeoMundi's development roadmap.

### Check certain responses

- [`validity-and-grounding`](https://github.com/neomundi-io/validity-and-grounding)  
  Documents the self-hosted semantic judge used to identify certain hallucination risks, as well as the validity module used to check a response against reference information or documents.

### Understand what the signals mean

- [`interpretation-contract`](https://github.com/neomundi-io/interpretation-contract)  
  Clarifies what NeoMundi signals allow you to conclude, what they do not prove on their own and which decisions remain the responsibility of the client or operator.

- [`Boundary Tension contract`](https://github.com/neomundi-io/Boundary_Tension_contract)  
  Explores situations where the boundary of responsibility must be clearly defined: between an AI that generates a response, a signal that raises an alert and a human or system that decides to act.

### Transmit results to other systems

- [`runtime-interoperability-contract`](https://github.com/neomundi-io/runtime-interoperability-contract)  
  Defines a common format for transmitting NeoMundi signals between measurement tools, agents, client applications and supervision systems.

### Protect data

- [`neomundi-io-data-protection`](https://github.com/neomundi-io/neomundi-io-data-protection)  
  Documents the data protection principles: minimization of processed information, BYOK, no storage of prompts or responses, and preparation of contractual frameworks.

### Observe, then govern

- [`neomundi-obs`](https://github.com/neomundi-io/neomundi-obs)  
  Presents OBS mode: your system calls NeoMundi after a generation and sends a snapshot limited to the data required for analysis. This privacy-first mode makes it possible to observe and document AI behavior without placing NeoMundi in the execution loop.

- [`neomundi-gov`](https://github.com/neomundi-io/neomundi-gov)  
  Presents GOV mode: NeoMundi calls the LLM during execution, analyzes the stream in real time and tracks the evolution of the `ΔG` signal in particular. Prompts and responses are processed transiently, without retention.

---

The objective is not to establish absolute truth from a single score.

The objective is to make AI behavior easier to measure, check, understand, transmit, document and govern.

---

## FAQ

### Does NeoMundi determine whether an answer is true or false?

No.

NeoMundi measures certain aspects of AI system behavior, including stability, variability, drift, regime changes and related signals.

These measurements can help identify outputs requiring enhanced attention, but they do not constitute, on their own, proof of truth, error or compliance.

Interpretation remains contextual and may be complemented by specialized verification mechanisms, business rules or human supervision.

### What is the difference between OBS and GOV?

**OBS** measures system behavior after generation or across successive observations.

It is generally the simplest integration mode and the natural starting point for most systems.

**GOV** enables certain measurements to be performed during execution when the context requires closer supervision.

In both cases, NeoMundi produces the measurement and associated signals.

The application, orchestrator, external policy layer or operator retains decision authority.

### What data is stored?

NeoMundi follows a data-minimization principle.

Prompts and responses are not stored.

Depending on the integration mode, only metrics, signals, technical events, required identifiers, timestamps and artifacts necessary for measurement, traceability or audit may be retained.

### Does NeoMundi work with my LLM or infrastructure?

NeoMundi is designed to be independent of any specific model or provider.

The measurement layer can progressively articulate with different models, providers, agents, orchestrators and AI infrastructures.

**OBS** can be used when a system is able to transmit the artifacts required for measurement.

**GOV** requires deeper runtime integration and depends on the providers, architectures and workflows involved.

The objective is to enable heterogeneous infrastructures to consume NeoMundi signals while retaining their own architecture and function.

### How is NeoMundi different from LangSmith, Portkey, Helicone or other observability platforms?

These platforms primarily cover application observability functions such as logs, traces, costs, latency, workflows and operational performance.

NeoMundi focuses on a complementary domain: **the measurement of AI system behavior**.

The NeoMundi layer aims in particular to make the following measurable and comparable:

- behavioral stability;
- variability;
- certain forms of drift;
- regime changes;
- certain coherence signals;
- informational metrics;
- their evolution over time.

NeoMundi is therefore not intended to replace an observability stack.

Its signals can instead be consumed by observability platforms, orchestrators, governance systems or other independent infrastructures.

### Is NeoMundi a governance system?

NeoMundi provides a **measurement layer that can feed governance mechanisms**, but measurement and decision-making remain distinct functions.

A NeoMundi signal can, for example, be used by an external system to:

- trigger an alert;
- request human review;
- regenerate an output;
- reroute a request;
- apply a control policy.

The final decision remains with the system, policy or operator consuming the signal.

### Does NeoMundi address certain EU AI Act and GDPR requirements?

NeoMundi does not replace a complete compliance process, legal analysis or regulatory certification.

The measurement layer and associated tools can nevertheless provide several technical capabilities that may support compliance efforts, including:

- monitoring AI system behavior over time;
- traceability of observations and signals;
- documentation of certain variations or incidents;
- production of auditable artifacts;
- actionable signals supporting human oversight;
- minimization of processed data;
- absence of prompt and response storage in the relevant modes.

Regulatory relevance depends on the system concerned, its intended use, its level of risk and the role of the organization deploying it.

➡️ [View the detailed mapping of NeoMundi capabilities for the EU AI Act and GDPR](https://github.com/neomundi-io/ai-act-rgpd)

---

## Ecosystem & Infrastructure Support

NeoMundi develops its work through an open ecosystem of technical, research, governance and infrastructure contributors.

### NVIDIA Inception Program

NeoMundi is a member of the NVIDIA Inception program.

<img src="https://raw.githubusercontent.com/neomundi-io/neomundi-sandbox/main/nvidia-inception-program-badge-rgb-for-screen.png"
     alt="NeoMundi is a member of the NVIDIA Inception program"
     width="180">

© 2025 NVIDIA, the NVIDIA logo, and NVIDIA Inception are trademarks and/or registered trademarks of NVIDIA Corporation in the U.S. and other countries.

### Infrastructure support

The NeoMundi AI Observatory is supported by sovereign infrastructure partners, including Infomaniak.

<img src="https://raw.githubusercontent.com/neomundi-io/neomundi-ai-observatory/main/logos/ecosystem/logo_infomaniak.png"
     alt="Infomaniak"
     width="150">

These relationships support the development and operation of independent AI measurement, auditability and runtime governance capabilities. They do not imply endorsement of NeoMundi’s research findings, measurements or interpretations by the organisations named above.

---

## Contact

Do you operate AI systems in production, autonomous agents or sensitive workflows?

**Measure AI behavior. Build on the signal.**

[contact@neomundi.io](mailto:contact@neomundi.io)
