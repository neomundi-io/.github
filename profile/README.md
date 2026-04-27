<a id="english-version"></a>

# NeoMundi. The AI thermometer.

[🇫🇷 Lire en français](README.fr.md)

---

**Real-time validation of decision stability, as it happens.**

We provide the signal.
You decide what to do with it.

📄 Methodology · DOI [10.5281/zenodo.19762753](https://doi.org/10.5281/zenodo.19762753) · Repo [llm-cartography](https://github.com/neomundi-io/llm-cartography)

---

## The runtime stability signal.
### Powering AI governance, fine-tuning, compliance and due diligence.

| 🟣 Agents | 🟢 Compliance | 🟡 Fine-tuning | 🔵 SLA / Infra |
|-----------|---------------|----------------|----------------|
| **Stop. Retry. Reroute.** | **Trace & prove.** | **Measure drift.** | **Prove continuity.** |
| Live stability signal, injected directly into agent decision loops. | Timestamped audit trail. Every generation scored, every drift flagged. | Quantify behavioral deviations across model versions. | Behavioral monitoring beyond latency. Quality of generation, measured. |

> **Your decision, our signal.**

---

## Measurement and detection

NeoMundi computes a real-time stability score (G) from a multivariate signal capturing semantic coherence, consistency and structural stability during generation.

This measurement is grounded in a dynamic stability framework inspired by Lyapunov principles, where variations (ΔG) reflect deviations from stable regimes.

The instrument continuously evaluates and updates this signal at runtime, enabling immediate detection of drift and instability.

**NeoMundi detects instability before it becomes visible:**

- Internal contradictions
- Loss of precision
- Thematic drift
- Structural inconsistency

> *Drift appears before failure. We measure it in real time.*
>
> *NeoMundi doesn't say if it's true. It says if it's coherent.*

### Validated on real systems

**Cartography v1-2026-04-26 — 3,904 measurements on TruthfulQA × 5 generative services.**

NeoMundi doesn't catch everything yet (~15% recall), **but when it flags, it's right ~76% of the time**. A reliable signal you can already act on.

The instrument is being refined. **Truth Module live on May 27, 2026.**

📊 Full metrics, dataset and methodology: [llm-cartography](https://github.com/neomundi-io/llm-cartography).

---

## Each generation produces

**Standard outputs:**
- Stability score (0 → 1)
- Decision (PASS / FLAG)
- Drift signal (timestamped)

**Advanced outputs:**
- Full audit trace (exportable)
- Execution metrics (cost, stability, drift)
- Cryptographic proof (hash)
- Structured datasets (analytics, fine-tuning, compliance)

> *Real signal. Real scoring. Real outcome.*

---

## See it in action

→ [Try it live](https://neomundi-io.github.io/neomundi-sandbox/): no installation, no API key.
→ [Sample audit report PDF](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## One-line integration

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

The instrument is served by the ControlTower platform. API key prefix: `ct_live_*`.

→ [Full integration guide](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/QUICKSTART)

---

## Roadmap

The infrastructure is live. It's scaling.

- **May 27, 2026**: Truth Module live (factual verification beyond coherence)
- **May–June 2026**: Self-service platform in production
- **Q3 2026**: Configurable thresholds per client, operator dashboard

Current pilot operators are prioritized on every update.

---

## FAQ

**What is the stability score?**
It measures the internal coherence of an LLM response in real time — not its truthfulness. NeoMundi does not fact-check. It detects the drift that precedes failure.

**What data do you store?**
Your prompts are neither read nor stored. Your provider API key stays under your control. Only governance metrics are recorded: score, decision, timestamp. Nothing else.

**Does it work with my LLM?**
Yes — automatic detection from your key: OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. If your provider is not listed, contact us.

**What's the difference from LangSmith, Portkey, or Helicone?**
Those tools observe and log. NeoMundi measures and signals during generation — before the unstable response reaches your user. We don't replace your observability stack, we add the missing measurement layer.

**Is it EU AI Act compliant?**
NeoMundi contributes to the EU AI Act's traceability and auditability requirements by producing a full audit trail per session: score, decision, timestamp, PDF export. Enforcement deadline: August 2026.

---

## Open Science · Reproducible · Auditable

Auditability built in by design. Not a black box.

- 📄 Full versioned methodology: [llm-cartography](https://github.com/neomundi-io/llm-cartography)
- 🔬 Reference dataset: [DOI 10.5281/zenodo.19762753](https://doi.org/10.5281/zenodo.19762753)
- 📐 Theoretical framework (law E): [DOI 10.5281/zenodo.19385052](https://doi.org/10.5281/zenodo.19385052)

---

> *Measuring AI behavior in real time.*
> *If you operate AI in production, you need a signal.*
> *Act before instability reaches your users.*

`contact@neomundi.io`

---

NeoMundi Recherche, French not-for-profit association (loi 1901), Vannes (France).
Commercial activities: Louis M Sàrl, Morges (Switzerland).

*At the speed of generation. Built to last.*
