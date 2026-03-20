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
      "latency_ms": 800,
      "cost_usd": 0.003,
      "semantic_risk": 0.1
    },
    "mode": "OBS"
  }'
```

Response → `{ "decision": "ALLOW", "stability_score": 0.76 }`

No SDK. No config file. One endpoint. → [Request API key](mailto:contact@neomundi.io)

---

## Live Sandbox

Test Law-E in real time via the [live sandbox](https://neomundi-tech.github.io/neomundi-sandbox/)

---

## What it catches

Neomundi monitors AI responses in real time, during generation, and detects:

- Hallucination spikes — before output is sent
- Cost drift — unbounded token loops
- Response degradation — quality decay over sessions
- Semantic instability — risk signals within context

---

## Why it matters

| Without Law E™ | With Law E™ |
|---|---|
| Audited after failure | Flagged before output |
| Cost spikes undetected | Drift caught in real time |
| Reliability assumed | Reliability measured |

---

## Example Use Case

**AI-assisted legal response platform**

A law firm deploys an LLM to pre-draft client responses. Every output is measured by Law E™ before delivery.

- Unstable outputs (hallucination risk > threshold) are flagged before the lawyer sees them
- Each response carries a stability score — traceable, auditable, defensible
- Liability doesn't disappear — it gets measured and assigned

---

## Documentation

- [Executive Brief](https://github.com/neomundi-tech/neomundi-sandbox/blob/main/docs/LawE_Executive_Brief_vF.pdf)
- [Technical White Paper](https://github.com/neomundi-tech/neomundi-sandbox/blob/main/docs/LawE_Technical_WhitePaper_vF.pdf)
- [Scientific Foundation](https://zenodo.org/records/19031860)

---

## Status

| Mode | Status | Signal |
|---|---|---|
| OBS | 🟢 Live | 79.5% instability detection (TruthfulQA) |
| GOV | 🟡 In development | Early pilot onboarding open |

---

*Reliability is no longer assumed. It is continuously evaluated.*
