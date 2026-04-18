# Neomundi. The AI thermometer.

🇫🇷 [Lire en français](https://github.com/neomundi-io/.github/blob/main/profile/README.fr.md)

### Real-time validation of decision stability, as it happens.
### We provide the signal.
### You decide what to do with it.

---

| 🟣 Agents | 🟢 Compliance | 🟡 Fine-tuning | 🔵 SLA / Infra |
|-----------|---------------|----------------|----------------|
| **Stop. Retry. Reroute.** | **Trace & prove.** | **Measure drift.** | **Prove continuity.** |
| Live stability signal, injected directly into agent decision loops. | Timestamped audit trail. Every generation scored, every drift flagged. | Quantify behavioral deviations across model versions. | Behavioral monitoring beyond latency. Quality of generation, measured. |

### Each signal directly drives decisions.

- The stability signal is the foundation of AI governance.
- Due diligence · fine-tuning data quality · compliance audit · SLA proof.

> ### The signal makes decisions actionable, in real time.

---

## Every AI decision becomes measurable, traceable, and governable.

Each generation produces:
- Stability score (0 → 1)
- Decision (ALLOW / FLAG / BLOCK)
- Drift signal (timestamped)

Advanced outputs:

- Full audit trace (exportable)
- Execution metrics (cost, stability, drift)
- Cryptographic proof (hash)
- Structured datasets (analytics, fine-tuning, compliance)

> Real request. Real scoring. Real signal.

---

## See it in action

<p align="center">
  <img src="https://raw.githubusercontent.com/neomundi-io/.github/main/profile/stability_score.gif" alt="Neomundi Stability Score Demo" width="800">
</p>

[→ Try it live: No installation. No API key required.](https://neomundi-io.github.io/neomundi-sandbox/)

[→ Sample audit report PDF](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## One-line integration.
Replace your existing LLM call with Neomundi. Your service keeps running exactly as before — every response is now scored in real time.

```python
# Before
response = openai.chat.completions.create(...)

# After
result = score_prompt(user_prompt)  # Neomundi calls OpenAI for you
```

That's it.

---

## Measurement approach

Neomundi computes a real-time stability score (G) from a multivariate signal capturing semantic coherence, consistency, and structural stability during generation.

This measurement is grounded in a dynamic stability framework inspired by Lyapunov principles, where variations (ΔG) reflect deviations from stable regimes.

The system continuously evaluates and updates this signal at runtime, enabling immediate detection of drift and instability.

---

## Neomundi detects instability before it becomes visible:

- Internal contradictions
- Loss of precision
- Thematic drift
- Structural inconsistency

> Drift appears before failure. We measure it in real time.

These signals do not seek truth. They measure coherence in real time. Drift is visible before it becomes an error.

---

## Validated on real systems

7,888 executions · 15 datasets

- 95.7% within governance thresholds
- 336 instabilities detected before delivery
- Average cost: €0.003 per execution

One undetected hallucination costs more than €0.003.

---

## Deploy in minutes

- No infrastructure change
- No data exposure
- No model dependency
- A single API call

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

---

## Pilot Program

First pilots now open.

We select partners for whom AI reliability is critical.
- Legal
- Compliance
- Multi-agent systems

You get:
- Direct access
- Preferential terms
- Co-built use case

→ [contact@neomundi.io](mailto:contact@neomundi.io)

---

## FAQ

**What is the stability score?**
It measures the internal coherence of an LLM response in real time — not its truthfulness. Neomundi does not fact-check. It detects the drift that precedes failure.

**What data do you store?**
Your prompts are neither read nor stored. Your provider API key stays under your control. Only governance metrics are recorded: score, decision, timestamp. Nothing else.

**Does it work with my LLM?**
Yes — automatic detection from your key: OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. If your provider is not listed, contact us.

**What's the difference from LangSmith, Portkey, or Helicone?**
Those tools observe and log. Neomundi measures and intervenes during generation — before the unstable response reaches your user. We don't replace your observability stack, we add the missing governance layer.

**Is it EU AI Act compliant?**
Neomundi contributes to the EU AI Act's traceability and auditability requirements by producing a full audit trail per session: score, decision, timestamp, PDF export. Enforcement deadline: August 2026.

---

## Roadmap: The infrastructure is live. It's scaling.

Within 60 days:
- Configurable thresholds per client
- Pilot operator dashboard

Current pilot operators are prioritized on every update.

---

## Open Science · Reproducible · Auditable

Auditability built in by design. Not a black box.

---

## Early Access

The signal is running. Data is accumulating.
Limited spots for teams operating AI in production.

You get:
- Direct access to the runtime signal
- A co-built use case on your system
- Preferential terms

We get:
- Real data
- Real constraints
- Real validation

We select. We don't recruit.

---

## Documentation

- Executive Brief: [NeoMundi Executive Brief EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Executive_Brief_FR.pdf)

---

### Measuring AI behavior in real time.
#### If you operate AI in production, you need a signal.
#### Act before instability reaches your users.

contact@neomundi.io

At the speed of generation. Built to last.
