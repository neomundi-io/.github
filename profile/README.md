## 🌐 Choose your language

**[🇬🇧 English](README.md)** · **[🇫🇷 Lire la version française](README.fr.md)**

---

# NeoMundi

## From AI observability to behavioral metrology
** Real-time measurement of AI behavior for governance and operational control.**

**Reduce risk. Improve operational control.**

NeoMundi provides an observability and behavioral metrology layer for generative AI systems and autonomous agents.

The instrument produces actionable signals to observe drift, detect regime changes, document incidents, trigger enhanced supervision, and support governance decisions adapted to the level of criticality.

**Your decision, our signal.**

[Access the sandbox](https://controltower.neomundi.io/welcome)

---

## What NeoMundi does in 30 seconds

NeoMundi enables you to:

- observe stability variations and regime shifts during or after a generation;
- produce structured, timestamped and auditable runtime signals;
- detect certain outputs requiring enhanced attention;
- support actions such as an alert, human review, regeneration or rerouting;
- keep decision-making authority with the operator, their system or their policy layer.

NeoMundi does not claim to determine on its own whether an answer is true.

The objective is more operational:

> make generative behavior observable, interpretable, interoperable, traceable and governable.

---

## Why it matters

Generative AI systems are increasingly integrated into real-world workflows: autonomous agents, business assistance, compliance, support, infrastructure, healthcare, legal services and finance.

Yet an answer can be fluent and plausible while still being unstable, insufficiently grounded or inappropriate for the context.

The challenge is therefore not merely to produce a score.

The challenge is to produce a signal that is:

- readable by a machine;
- understandable by a human;
- usable by an orchestration layer;
- documentable after execution;
- actionable without automatically transferring decision-making authority to the instrument.

An isolated signal is not an infrastructure.

A specified, contextualized and interoperable signal can become a building block for governance.

---

## OBS first. GOV when you are ready.

NeoMundi offers two integration modes depending on the system's level of criticality.

|                    | OBS — Privacy-first snapshot                               | GOV — Real-time governance                                  |
| ------------------ | ---------------------------------------------------------- | ----------------------------------------------------------- |
| **Principle**      | Your system calls NeoMundi after a generation              | NeoMundi calls the LLM during execution                     |
| **Objective**      | Observe, compare and document                               | Supervise and govern in real time                           |
| **Timing**         | After generation                                            | During generation                                           |
| **Data processed** | Snapshot limited to the data required for analysis          | Stream processed transiently                                |
| **Signals**        | Stability state, alerts and auditable traces                | Stability state, `ΔG`, alerts and governance decisions      |
| **Retention**      | No storage of prompts or responses                          | No storage of prompts or responses                          |
| **Natural fit**    | Most AI systems                                             | Critical or difficult-to-recover workflows                  |

### The right decision criterion

> If a poor output reaches the user, can it be recovered from?

**If yes**, OBS is generally the natural starting point.

Your system sends a snapshot to NeoMundi to observe behavior, detect certain drifts and retain an actionable trace.

**If no**, GOV becomes relevant.

NeoMundi enters the execution loop, calls the LLM, tracks the evolution of the signal in real time and enables an enhanced supervision policy.

In both cases, NeoMundi provides the signal.

Your system, your policy layer or the responsible operator retains decision-making authority.

---

## What NeoMundi observes

NeoMundi produces signals to observe certain behaviors during or after generation:

- stability variations;
- losses of coherence;
- progressive drift;
- regime shifts;
- patterns compatible with certain problematic outputs;
- informational variations across generations, models, prompts or versions.

These signals are not absolute proof.

They make AI generations more observable, interpretable, traceable and governable.

### Families of signals and artifacts

Depending on the integration mode and the maturity level of the deployment, NeoMundi can produce:

- **governance stability state**: a normalized state associated with a generation or execution window;
- **runtime stability variation**: evolution of the signal across several observation windows;
- **FLAG**: a conservative signal indicating that an output requires enhanced attention;
- **informational metrics**: complementary measurements related to the informational structure of generations;
- **governance decisions**: states such as `ALLOW`, `FLAG`, `BLOCK` or equivalents according to the client's policy;
- **structured telemetry**: events, timestamps, technical identifiers and associated signals;
- **auditable traces**: exports, reports and reporting artifacts depending on the level of integration.

> A signal observes.  
> A decision guides action.  
> Interpretation remains contextual.

---

## Initial experimental results

NeoMundi has been tested through several controlled campaigns covering generative AI services accessible through APIs.

### Cumulative corpus

| Campaign | Scope | Generations analyzed |
|---|---:|---:|
| Mapping v1 — 2026-04-26 | 5 LLM providers | 3,904 |
| TruthfulQA cohort v2 — 2026-05-17 | 8 anonymized LLM providers | 6,256 |
| **Total** |  | **10,160** |

### Observed precision of the FLAG signal

When a `FLAG` was triggered, a problematic output was confirmed in approximately **76%** of cases across the cumulative corpus.

| Campaign | FLAGs triggered | Confirmed problematic outputs | Observed precision |
|---|---:|---:|---:|
| Mapping v1 — 2026-04-26 | 437 | 331 | 75.7% |
| TruthfulQA cohort v2 — 2026-05-17 | ≈ 394 | ≈ 301 | ≈ 76.4% |
| **Cumulative total** | **≈ 831** | **≈ 632** | **≈ 76%** |

### How to read these results correctly

NeoMundi does not claim to detect every error.

The instrument currently prioritizes signal precision over exhaustive coverage:

> it is better to flag fewer outputs usefully than to overwhelm teams with false positives.

These results constitute an initial operational validation.

They must be read with their limitations: dependence on the corpus, the providers tested, the selected thresholds and the human or instrumental confirmation protocol.

Consolidation continues through observation campaigns, methodological audits and field pilots.

---

## Use cases

| Use case | What NeoMundi provides | Natural mode |
|---|---|---|
| **Autonomous agents** | Observe drift and trigger escalation, retry or rerouting according to the selected policy | OBS · GOV |
| **Compliance and audit** | Produce timestamped traces, document signals and support supervision | OBS · GOV |
| **Fine-tuning and evaluation** | Compare behavioral differences across models, prompts, datasets or versions | OBS |
| **SLA and AI infrastructure** | Detect certain behavioral degradations and document incidents | OBS · GOV |
| **Sensitive workflows** | Strengthen supervision when an incorrect output would be difficult to recover from | GOV |

NeoMundi does not replace your observability stack.

NeoMundi adds a complementary behavioral measurement and governance layer.

---

## Integration and privacy

NeoMundi is designed to integrate progressively with LLM applications, agents, orchestrators and business systems.

### Integration principles

- one API call to get started;
- a **BYOK** approach depending on the mode and configuration;
- no storage of prompts or responses;
- configurable thresholds according to client policies;
- decision-making authority retained by the operator;
- exports and auditable traces depending on the level of integration;
- dedicated deployment or controlled environment according to requirements.

### LLM provider integration

NeoMundi can be integrated with supported LLM providers through a governed runtime API.

Use the provider integration guide to connect your existing provider account, configure your model, manage API keys securely and start streaming governed requests through ControlTowerAI.

➡️ [Read the LLM Provider Integration Guide](https://github.com/neomundi-io/controltowerai-docs/blob/main/providers.md)

### Operational sovereignty

NeoMundi uses a **self-hosted semantic judge** to analyze certain AI-generated responses.

This judge runs on infrastructure controlled by NeoMundi, without depending on an external service for this critical function.

This architecture serves three objectives:

- **privacy**: limit the exposure of sensitive data;
- **resilience**: reduce dependence on external services;
- **operational sovereignty**: retain control over analysis and processing.

---

## Product status

NeoMundi is evolving in stages to clearly distinguish what can be demonstrated today, what is offered through pilot programs and what belongs to the industrialization roadmap.

| Status | Meaning |
|---|---|
| **Available now** | Public sandbox, initial observation surfaces, signal demonstrations and methodological documentation |
| **Supported pilot** | Progressive integration, calibration, supervision, exports and policies adapted to the client's context |
| **Product roadmap** | Extended metrics, advanced runtime orchestration, dedicated deployments and industrialized governance policies |

This progression makes it possible to start with observation and increase the level of control when the business context requires it.

---

## From thermometer to spectrometer

NeoMundi is evolving from a stability signal into a multidimensional measurement layer for AI behavior during execution.

The objective is not to multiply scores.

The objective is to build an infrastructure capable of:

1. measuring;
2. interpreting;
3. transmitting;
4. deciding according to an explicit policy;
5. tracing what occurred.

The public NeoMundi framework progressively documents the signals, contracts and methodological boundaries required for this infrastructure.

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
* [Executive Brief — FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/NeoMundi_Executive_Brief_2026_FR.pdf)
* [Executive Brief — EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/NeoMundi_Executive_Brief_2026_EN.pdf)
* [Theoretical Framework (Law E) — FR](https://doi.org/10.5281/zenodo.19385052)

---

## Contact

Do you operate AI systems in production, autonomous agents or sensitive workflows?

**Measure what can be recovered. Control what cannot.**

contact@neomundi.io
