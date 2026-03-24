## Law-E, Runtime AI Risk Control

Every AI response is a risk you own.

Law-E sits inside the flow between your application and the AI
and decides before the response is released.

Each output is scored in real time. If the risk is too high, it is flagged or blocked - in milliseconds.
> G-score: 0 = low risk · 1 = high risk

You don't guess what your AI is doing anymore.
You measure it. You control it. You can prove it.

Not monitoring. Not logging.
A real-time decision layer for AI.

---
Not a firewall. Not a guardrail.

Firewalls block. Guardrails constrain.  
Law-E measures risk and decides — in real time.

User prompt → [LLM] → ⚡ Law E™ scores in <50ms → ALLOW ✅ / FLAG 🚨
                       G-Score  |  Risk: Low  |  Drift: 0.02

---

No infrastructure changes. Instant control.

## Live Sandbox

Test Law-E in real time via the [live sandbox](https://neomundi-io.github.io/neomundi-sandbox/)

---

## EU AI Act — built in, not bolted on

Compliance is not a feature.
It is enforced at runtime.

Every response is scored, traced, and auditable — by design.

OBS mode gives you continuous monitoring out of the box.  
GOV mode enforces it in real time.

You don’t prepare for compliance.  
You deploy it.

---

## What it catches

Neomundi monitors AI responses in real time, during generation, and detects:

- Hallucination spikes - before output is sent
- Cost drift - unbounded token loops
- Response degradation - quality decay over sessions
- Semantic instability - risk signals within context

---

## Why it matters

Without Law-E, you discover failures after they happen.  
With Law-E, you stop them before they reach anyone.

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
- Each response carries a stability score - traceable, auditable, defensible
- Liability doesn't disappear - it gets measured and assigned

---

## Documentation

- **[Executive Brief](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/LawE_Executive_Brief.pdf)**
- **[Technical White Paper](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/LawE_Technical_WhitePaper.pdf)**
- **[Scientific Foundation](https://zenodo.org/records/19031860)**

---

## Status

| Mode | Status | Signal |
|---|---|---|
| OBS | 🟢 Live | Early pilot onboarding open |
| GOV | 🟡 For early pilote | 79.5% instability detection (TruthfulQA) |

---

## FAQ

**1. How fast can I integrate Neomundi?**  
In minutes. Add one API call between your app and your LLM — no SDK, no architecture change.

**2. What do I get immediately?**  
Instant visibility on every AI response: risk level, decision signal, and audit trace — in real time.

**3. Does it impact performance?**  
No. Start in OBS mode: zero enforcement, full transparency.

**4. What happens when I activate GOV mode?**  
Neomundi enforces your policies in real time — blocking or allowing responses based on your risk thresholds.

**5. Why is this useful for my business?**  
You reduce AI risk, gain auditability, and move toward compliance — without slowing down your product.

**6. Do you store my data?**  
No sensitive data is stored. Only aggregated metrics are used for reporting and optimization.

**7. What’s the next step?**  
Test the sandbox in 30 seconds.  
If it makes sense for your use case, contact us to activate production access.

---
*Reliability is no longer assumed. It is continuously evaluated.*
