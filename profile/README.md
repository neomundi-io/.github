## 🌐 Choose your language

**[🇬🇧 English](README.md)** · **[🇫🇷 Lire la version française](README.fr.md)**

---

# NeoMundi

## Fundamental measurement layer for AI behavior

**A common measurement layer from which multiple uses can derive and around which heterogeneous AI infrastructures can articulate.**

NeoMundi measures behavioral variability, stability and regime changes in AI systems at runtime.

Its signals can support multiple uses — observation, drift detection, audit, governance, orchestration and control — while being consumed by independent infrastructures that retain their own architecture, function and decision authority.

**One fundamental measurement layer. Multiple uses. Multiple infrastructures.**

**Your system. Your decisions. Our signal.**

---

[**Reference Framework**](https://zenodo.org/records/21821522) · [**Executive Brief**](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf) · [**AI Observatory**](https://github.com/neomundi-io/neomundi-ai-observatory) · **Launchers & Use Cases** · [**Interoperability**](https://github.com/neomundi-io/runtime-interoperability-contract) · [**Sandbox**](https://controltower.neomundi.io/welcome)

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

NeoMundi has now produced and analyzed **more than 200,000 observations** across measurement campaigns, barometers, mappings, experiments and field pilots.

These experiments span multiple models, providers, protocols and execution configurations and contribute to the study of stability, behavioral variability, regime changes and signal actionability.

### Initial FLAG signal validation campaigns

The initial campaigns used specifically to evaluate the precision of the `FLAG` signal represented a cumulative corpus of **10,160 generations**.

| Campaign | Scope | Generations analyzed |
|---|---:|---:|
| Mapping v1 — 2026-04-26 | 5 LLM providers | 3,904 |
| TruthfulQA cohort v2 — 2026-05-17 | 8 anonymized LLM providers | 6,256 |
| **Total** | | **10,160** |

When a `FLAG` was triggered, a problematic output was confirmed in approximately **76% of cases** across this corpus.

| Campaign | FLAGs triggered | Confirmed problematic outputs | Observed precision |
|---|---:|---:|---:|
| Mapping v1 — 2026-04-26 | 437 | 331 | 75.7% |
| TruthfulQA cohort v2 — 2026-05-17 | ≈ 394 | ≈ 301 | ≈ 76.4% |
| **Cumulative total** | **≈ 831** | **≈ 632** | **≈ 76%** |

### How to read these results

NeoMundi does not claim to detect every error.

The instrument currently prioritizes signal precision over exhaustive coverage:

> it is better to flag fewer outputs usefully than to overwhelm teams with false positives.

These results constitute an initial experimental and operational validation.

They must be interpreted within their limitations, including dependence on the corpus, providers tested, selected thresholds and confirmation protocols.

Consolidation continues through longitudinal measurement campaigns, methodological audits, experimental articulations and field pilots.

---

## Use cases

A single measurement layer can support multiple use cases without imposing the infrastructure that consumes it.

| Use case | What NeoMundi signals can provide | Natural mode |
|---|---|---|
| **Autonomous agents** | Observe certain drifts and feed escalation, retry or rerouting mechanisms | OBS · GOV |
| **Compliance and audit** | Produce timestamped traces, document signals and support supervision | OBS · GOV |
| **Fine-tuning and evaluation** | Compare behavioral differences across models, prompts, datasets or versions | OBS |
| **SLA and AI infrastructure** | Detect certain behavioral degradations and document incidents | OBS · GOV |
| **Sensitive workflows** | Strengthen supervision when an incorrect output would be difficult to recover from | GOV |

**These uses derive from the same measurement layer. NeoMundi does not impose the infrastructure that consumes it.**

Launchers, orchestrators, governance systems, evidence infrastructures and business applications can consume NeoMundi signals while retaining their own function and decision authority.

---

## Integration and interoperability

NeoMundi is designed to articulate with existing LLM applications, agents, orchestrators, governance layers and business systems.

### Integration principles

- progressive integration starting with a single API call;
- **BYOK** approach depending on mode and configuration;
- no storage of prompts or responses;
- configurable thresholds and policies according to context;
- separation between measurement authority and decision authority;
- exports and auditable traces depending on integration level;
- ability to articulate signals with external infrastructures;
- dedicated deployments or controlled environments according to requirements.

### LLM provider integration

NeoMundi can be integrated with supported LLM providers through its runtime interfaces.

The integration guide explains how to connect an existing provider account, configure a model, manage API keys and transmit requests through ControlTowerAI.

➡️ [Read the LLM Provider Integration Guide](https://github.com/neomundi-io/controltowerai-docs/blob/main/providers.md)

### Interoperability

NeoMundi aims to make its signals usable by independent systems without imposing a specific architecture, policy or governance mechanism.

The Runtime Interoperability Contract documents the minimal principles required to transmit and interpret these signals across independent layers.

➡️ [Runtime Interoperability Contract](https://github.com/neomundi-io/runtime-interoperability-contract)

---

## Privacy and operational sovereignty

NeoMundi follows a data-minimization principle.

Prompts and responses are not stored.

Depending on the integration mode, only information required for measurement, traceability or associated policy operation may be retained.

NeoMundi also uses a **self-hosted semantic judge** for certain analyses.

This component runs on infrastructure controlled by NeoMundi in order to limit dependence on external services for this function.

This architecture serves three objectives:

- **privacy**: limit data exposure;
- **resilience**: reduce certain external dependencies;
- **operational sovereignty**: retain control over analysis and processing.

---

## Product status

NeoMundi is evolving progressively in order to clearly distinguish what is available today, what can be explored through supported pilots and what still belongs to the industrialization roadmap.

| Status | Meaning |
|---|---|
| **Available now** | Public sandbox, initial measurement surfaces, runtime signals and methodological documentation |
| **Supported pilot** | Progressive integration, calibration, supervision, exports and policies adapted to the operational context |
| **Product roadmap** | Extended metrics, stronger interoperability, advanced runtime orchestration and dedicated deployments |

This progression makes it possible to begin with measurement and progressively articulate the uses and levels of governance required by the operational context.

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

NeoMundi produces signals to observe certain variations, instabilities, drifts or behavioral transitions.

These signals support decision-making. They do not replace business context, human supervision or specialized verification mechanisms when these are required.

### What is the difference between OBS and GOV?

**OBS** enables observation, documentation and improvement after generation or through continuous supervision.

**GOV** enters the runtime chain when an incorrect output would be difficult to recover from.

OBS is generally the natural starting point.

GOV increases the level of control when the context requires it.

### What data is stored?

NeoMundi is designed according to a data-minimization principle.

Prompts and responses are not stored.

Depending on the selected mode, only metrics, signals, technical events, required identifiers, timestamps and reporting artifacts may be retained.

### Does NeoMundi work with my LLM?

OBS is designed to be compatible with systems capable of sending the expected observation artifacts.

GOV follows a progressive integration approach depending on providers, workflows and levels of criticality.

### How is NeoMundi different from LangSmith, Portkey or Helicone?

These tools primarily focus on application observability: logs, tracing, costs, workflows and performance.

NeoMundi adds a complementary layer focused on behavioral measurement and governance: stability, variation, runtime signals, interpretation, auditability and supervision policies.

### Does NeoMundi cover certain EU AI Act and GDPR requirements?

NeoMundi does not replace a complete compliance process, legal analysis or regulatory certification.

However, ControlTower covers several technical capabilities that are directly useful for EU AI Act and GDPR compliance efforts:

* continuous monitoring of AI-system behaviour;
* control of the risk associated with generated responses;
* operational traceability;
* auditability;
* actionable signals supporting human oversight;
* evidence useful for incident documentation;
* a privacy-first architecture based on data minimisation and the absence of prompt and response storage.

The legal relevance depends on the system concerned, its intended use, its level of risk and the organisation’s role.

➡️ [Consult the detailed mapping of NeoMundi capabilities for the EU AI Act and GDPR](https://github.com/neomundi-io/ai-act-rgpd/blob/main/README_EN.md)

##  Ecosystem & Infrastructure Support

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

 Resources

* [NeoMundi Sandbox](https://controltower.neomundi.io/welcome)
* [NeoMundi Website](https://neomundi.io)
* [Executive Brief — FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_FR.pdf)
* [Executive Brief — EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)
* [AI Observability & Behavioral Metrology — FR / EN](https://zenodo.org/records/21250268)
* [Theoretical Framework (Law E) — FR](https://doi.org/10.5281/zenodo.19385052)

---

## Contact

Do you operate AI systems in production, autonomous agents or sensitive workflows?

**Measure what can be recovered. Control what cannot.**

contact@neomundi.io
