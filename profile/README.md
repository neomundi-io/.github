# Neomundi - Real-Time AI Stability Control

🇫🇷 [Lire en français](https://github.com/neomundi-io/.github/blob/main/profile/README.fr.md)

---

Your AI is not auditable. Now it is and in 10 minutes.

✅ **Every response is measured in real time.**

⚠️ **You see drift before it becomes an incident.**

🛑 **You can block unstable responses before they are sent.**

📄 **You have proof: PDF export of all your logs.**

**Not a firewall. Not a guardrail. A real-time decision layer.**

**One API call. No infrastructure changes.**

---
## See it in action

> Real request. Real scoring. Real decision.

<p align="center">
  <img src="./assets/stability_score.gif" alt="Neomundi Stability Score Demo" width="800">
</p>

**Input** → scored in real time
**Drift detected** → flagged before output
**Decision** → ALLOW / FLAG / BLOCK

[→ Try it live — No installation. No API key required.](https://neomundi-io.github.io/neomundi-sandbox/)
---

## What Neomundi Detects

Neomundi detects when your AI starts to drift:

- Internal contradictions
- Loss of precision
- Topic deviation
- Global incoherence

These signals do not look for truth. They measure coherence — in real time.
Drift is visible before it becomes an error.

---

## Results & Validation

Based on public benchmarks (TruthfulQA, HaluEval, MMLU, LegalBench) and internal stress tests.

2,360 responses analyzed. 6 datasets. One question: does the stability score detect what it claims to detect?

- **91% true positives**
- **Strong correlation between stability drop and hallucination**
- **Zero over-detection on edge cases**

In practice: Neomundi detects drift before it reaches your users.

---

## Integration

Up and running in 10 minutes. Without touching your infrastructure.

**Bring your key**
You use your own provider API key — OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. It transits in your request and stays under your control.

**One redirection point**
You redirect your LLM calls through `api.neomundi.io`. No SDK to install, no code changes, no migration.

**Security**
Neomundi does not know your provider keys. Your prompts are not read or stored. Only governance metrics are recorded — stability score, decision, timestamp.

**Compatibility**
Automatic provider detection from your key:

`OpenAI · Anthropic · Google · Mistral · DeepSeek · xAI · Cohere`

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

Response: real-time stability score · ALLOW / FLAG decision · PDF export on demand.

---

## Pilot Program

We are selecting early adopter partners in sectors where LLM reliability is not optional: LegalTech, regulated industries, multi-LLM publishers.

In exchange for documenting your use case: **preferential conditions for life for the first partners.**

[→ contact@neomundi.io](mailto:contact@neomundi.io)

---

## FAQ

**What is the stability score?**
It measures the internal coherence of an LLM response in real time — not its truthfulness. Neomundi does not fact-check. It detects the drift that precedes the error.

**What data do you store?**
Your prompts are not read or stored. Your provider API key stays under your control. Only governance metrics are recorded: score, decision, timestamp. Nothing else.

**Does it work with my LLM?**
Yes — automatic detection from your key: OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. If your provider is not listed, contact us.

**What is the difference with LangSmith, Portkey or Helicone?**
These tools observe and log. Neomundi measures and intervenes during generation — before the unstable response reaches your user. We do not replace your observability stack, we add the governance layer that is missing.

**Is it compliant with the EU AI Act?**
Neomundi contributes to the traceability and auditability requirements of the EU AI Act — complete audit trail per session: score, decision, timestamp, PDF export. The enforcement deadline is August 2026.

**What is GOV mode?**
OBS mode scores and traces every response without intervening. GOV is the execution mode: unstable responses are blocked before delivery. Pilot partners get priority access.

---

## Roadmap — 30 days

- Full GOV mode — blocking unstable responses before delivery
- Extended detection: drift, error, rupture in real time
- Platform interface — logs, configurable thresholds, full export

Current pilot partners get priority access.

---

## Documentation

- Executive Brief — [link coming]
- Technical White Paper — [link coming]
- Scientific Foundation (Zenodo) — [link coming]

---

*Stability is no longer assumed. It is measured.*
