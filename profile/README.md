## 🌐 Choose your language

[**🇬🇧 English**](https://github.com/neomundi-io/.github/blob/main/profile/README.md) ·
[**🇫🇷 Français**](https://github.com/neomundi-io/.github/blob/main/profile/README.fr.md)

---

# NeoMundi

## Measure AI behavior at runtime. Keep control of what happens next.

NeoMundi provides an independent runtime measurement layer for AI systems.
It turns an observed execution into a structured, timestamped and comparable
measurement signal that can be consumed by existing audit, observability,
governance, insurance and decision systems.

NeoMundi provides the measurement. Your systems retain their infrastructure,
rules and decision authority.

> **Your system. Your decisions. Our measurement signal.**

### Start measuring

1. **Create your account and NeoMundi API key**  
   [Open the NeoMundi platform →](https://controlotower.neomundi.io/welcome)

2. **Connect your system to the measurement API**  
   [Follow the Runtime Measurement Quickstart →](https://github.com/neomundi-io/neomundi-runtime-measurement/blob/main/QUICKSTART.md)

3. **Use the signal in your own infrastructure**  
   [Read the interoperability contract →](https://github.com/neomundi-io/neomundi-measurement-interoperability)

**One measurement API · Existing infrastructure preserved · Machine-readable output**

**Privacy by design · NeoMundi and provider keys remain separate**

---

## Two products, one measurement primitive

### Product 01 — Runtime Measurement Layer

[**Explore the Runtime Measurement Layer →**](https://github.com/neomundi-io/neomundi-runtime-measurement)

The technical foundation of the NeoMundi ecosystem. It produces structured
runtime measurements with explicit semantics, provenance, traceability,
versioning and integration boundaries.

Use it when you want to connect an existing AI system directly to the NeoMundi
measurement signal.

### Product 02 — AI Periscope

[**Explore AI Periscope →**](https://github.com/neomundi-io/neomundi-ai-periscope)

AI Periscope uses the same measurement primitive to build reproducible
measurement campaigns, baselines, comparisons, datasets, manifests and
decision-ready reports.

Use it when you want to evaluate or compare models, prompts, configurations or
business workflows under documented conditions.

---

## How the ecosystem fits together

~~~text
AI System or Evaluation Campaign
                │
                ▼
NeoMundi Runtime Measurement Layer
                │
                ▼
Structured Measurement Signal
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
 Metric Contract   Metrology Validation
        │       │        │
        └───────┼────────┘
                ▼
   Interoperable Measurement Contract
                │
                ▼
Customer Systems · AI Periscope · Observatory · Use Cases
~~~

**Measurement ≠ Interpretation ≠ Policy ≠ Execution**

NeoMundi measures. The consuming system interprets, governs and acts.

---

## Core documentation

### Measure

[**Runtime Measurement Layer**](https://github.com/neomundi-io/neomundi-runtime-measurement)  
API integration, measurement signals, traceability, versioning and consumer
boundaries. This is the technical entry point and the centre of the ecosystem.

### Define

[**Metric Contract & Measurement Reference**](https://github.com/neomundi-io/neomundi-metric-contract)  
Definitions, scope, limits and admissible interpretation of NeoMundi
measurement signals.

### Validate

[**Metrology Validation**](https://github.com/neomundi-io/neomundi-metrology-validation)  
Calibration, reproducibility, controls, sensitivity, limitations and the
evidence supporting measurement claims.

[**G-score Reproducibility Study**](https://github.com/neomundi-io/G-score-reproducibility-study)  
An exploratory study of conditional G-score reproducibility across 33,600
observations, 12 AI models, 7 campaigns and 4 prompts. Its results are an
initial characterization, not definitive scientific validation.

### Transport

[**Measurement Interoperability**](https://github.com/neomundi-io/neomundi-measurement-interoperability)  
Public, versioned JSON contract for exchanging measurement records between
independent systems while preserving provenance, integrity and responsibility
boundaries.

[**Live interoperability demonstrator →**](https://interop.neomundi.org/)

---

## Products, pilots and public observation

### Products

[**NeoMundi Products**](https://github.com/neomundi-io/NeoMundi-Products)  
Product catalogue and navigation hub. Detailed technical documentation remains
in each canonical repository.

[**AI Periscope**](https://github.com/neomundi-io/neomundi-ai-periscope)  
Reproducible measurement campaigns, baselines, comparisons and reports.

### Pilots and evidence

[**NeoMundi Use Cases**](https://github.com/neomundi-io/neomundi-use-cases)  
Documented pilots and interoperability experiments showing how independent
systems consume NeoMundi measurements while retaining their own architecture
and decision authority.

A pilot demonstrates an articulation under documented conditions. It is not a
universal certification.

### Observatory

[**NeoMundi AI Observatory**](https://github.com/neomundi-io/neomundi-ai-observatory)  
Public longitudinal observation of AI system behavior under repeated and
documented conditions.

[**Research Observatory →**](https://neomundi.org/en/home) ·
[**AI Weather →**](https://weather.controltowerai.io)

The Observatory produces observations. Metrology Validation qualifies the
measurement.

---

## What the signal can support

The same measurement primitive can contribute to:

- runtime observation and longitudinal monitoring;
- behavioral comparison and drift detection;
- audit and evidence records;
- diagnosis and decision support;
- external governance and control mechanisms;
- insurance and risk assessment;
- model, prompt and workflow evaluation.

These applications remain responsible for their own thresholds, policies,
decisions and actions.

A NeoMundi measurement does not, by itself, prove truth, safety, compliance or
admissibility.

---

## Measurement principles

- **Contextual:** a measurement describes an observation under declared
  conditions at a specific point in time.
- **Traceable:** identifiers, timestamps, versions and provenance connect the
  signal to the observation that produced it.
- **Comparable:** explicit schema, metric and normalization versions preserve
  interpretability over time.
- **Interoperable:** structured records can be exchanged with independent
  infrastructures.
- **Non-decisional:** the consuming system retains interpretation, policy and
  execution authority.
- **Data-minimizing:** integrations should exchange only the elements required
  for measurement and traceability.

---

## Repository map

The repositories below do not all have the same status. Canonical repositories
define the current public architecture; specialized and experimental
repositories document narrower work; legacy repositories preserve earlier
stages of the framework.

### Canonical entry points

- [Runtime Measurement Layer](https://github.com/neomundi-io/neomundi-runtime-measurement)
- [Metric Contract](https://github.com/neomundi-io/neomundi-metric-contract)
- [Metrology Validation](https://github.com/neomundi-io/neomundi-metrology-validation)
- [Measurement Interoperability](https://github.com/neomundi-io/neomundi-measurement-interoperability)
- [AI Periscope](https://github.com/neomundi-io/neomundi-ai-periscope)
- [AI Observatory](https://github.com/neomundi-io/neomundi-ai-observatory)
- [Products](https://github.com/neomundi-io/NeoMundi-Products)
- [Use Cases](https://github.com/neomundi-io/neomundi-use-cases)

### Specialized measurement and research

- [Informational Metrics](https://github.com/neomundi-io/informational-metrics)
- [Energy Stability Index](https://github.com/neomundi-io/energy-stability-index)
- [Validity & Grounding](https://github.com/neomundi-io/validity-and-grounding)
- [G-score Reproducibility Study](https://github.com/neomundi-io/G-score-reproducibility-study)
- [Signal Adaptation Framework](https://github.com/neomundi-io/neomundi-signal-adaptation-framework)

These repositories document specialized or experimental work. They should not
be interpreted as autonomous decision engines or as universally validated
product capabilities.

### Governance and data protection

- [Data Protection](https://github.com/neomundi-io/neomundi-io-data-protection)
- [EU AI Act & GDPR mapping](https://github.com/neomundi-io/ai-act-rgpd)

These resources may support governance and compliance work. They do not replace
legal analysis, a complete compliance process or regulatory certification.

### Earlier framework repositories

- [Runtime Telemetry Signals](https://github.com/neomundi-io/runtime-telemetry-signals)
- [Interpretation Contract](https://github.com/neomundi-io/interpretation-contract)
- [Boundary Tension Contract](https://github.com/neomundi-io/Boundary_Tension_contract)
- [Runtime Interoperability Contract](https://github.com/neomundi-io/runtime-interoperability-contract)
- [NeoMundi OBS](https://github.com/neomundi-io/neomundi-obs)
- [NeoMundi GOV](https://github.com/neomundi-io/neomundi-gov)

These repositories preserve earlier or specialized formulations. The canonical
sources for current integration, semantics and interoperability are the Runtime
Measurement Layer, Metric Contract and Measurement Interoperability repositories.

---

## Learn more

- [NeoMundi website](https://neomundi.io)
- [Executive Brief](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)
- [Reference Framework](https://zenodo.org/records/21821522)
- [Provider integration guide](https://github.com/neomundi-io/controltowerai-docs/blob/main/providers.md)

---

## Contact

Do you operate AI systems in production, autonomous agents or sensitive
workflows?

**Measure AI behavior. Build on the signal.**

[contact@neomundi.io](mailto:contact@neomundi.io)

