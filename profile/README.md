# Law-E — Runtime AI Risk & Stability Monitoring

AI systems fail silently.
Neomundi measures instability before it happens.

---

## Quickstart

### API Example

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "raw_metrics": {
      "token_count": 150,
      "latency_ms": 200,
      "cost_usd": 0.02,
      "semantic_risk": 0.1
    },
    "mode": "OBS"
  }'
Example response
{
  "decision": "ALLOW",
  "stability_score": 0.76
}
Payload format
{
  "raw_metrics": {
    "token_count": number,
    "latency_ms": number,
    "cost_usd": number,
    "semantic_risk": number
  },
  "mode": "OBS"
}
What it means

```

## Live Sandbox

Test Law-E in real time via the [live sandbox](https://neomundi-tech.github.io/neomundi-sandbox/)

To request API access, [contact us](mailto:contact@neomundi.io)


---

## What it catches

Neomundi monitors AI responses in real time, during generation, and detects:

- Hallucination spikes — before output is sent  
- Cost drift — unbounded token loops  
- Response degradation — quality decay over sessions  
- Semantic instability — risk signals within context

---

## Why it matters

|       Without Law E™    |          With Law E™        |
|           ---           |             ---             |
| Audited after failure   | Flagged before output       |
| Cost spikes undetected  | Drift caught in real time   |
| Reliability assumed     | Reliability measured        |


---
## Architecture

LLM / AI System  
↓  
Raw Metrics  
↓  
Normalizer  
↓  
Aggregation  
↓  
Stability Score  
↓  
Decision Layer (ALLOW / FLAG / MODULATE)

---
## Example Use Case

AI-assisted legal response platform

A law firm deploys an LLM to pre-draft client responses. Every output is measured by Law E™ before delivery.
→
Unstable outputs (hallucination risk > threshold) are flagged before the lawyer sees them
→
Each response carries a stability score — traceable, auditable, defensible
→
Liability doesn't disappear — it gets measured and assigned

---

## Documentation

- [Executive Brief](https://github.com/neomundi-tech/neomundi-sandbox/blob/main/docs/LawE_Executive_Brief_vF.pdf)
  
- [Technical White Paper](https://github.com/neomundi-tech/neomundi-sandbox/blob/main/docs/LawE_Technical_WhitePaper_vF.pdf)
  
- [Scientific Foundation](https://zenodo.org/records/19031860)

---

## Status

OBS mode: live
GOV mode: in development
Early results: ~79% instability signals detected (TruthfulQA)
Early pilot onboarding in progress

--- 

## Vision

We expose a runtime stability metric currently being normalized toward invariance.
Law-E explores a unifying stability framework across:
LLMs
AI agents
infrastructure
future AI-native systems

---

Reliability is no longer assumed.
It is continuously evaluated.
