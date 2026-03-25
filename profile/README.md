# Runtime AI Risk Control
**by Neomundi**

> 🇫🇷 [Lire en français](README.fr.md)

---

Your AI makes mistakes. That is not the real problem. The real problem is when you find out.

The response has already been sent. The client has already read it. At that point, it is too late.

Neomundi sits between your application and your AI. Every response is analyzed while it is being generated.

- Every response is traced
- Every response is auditable
- A score tells you when the risk of error is rising

You stop discovering problems after the fact. They are detected while the response is still being written. The system triggers an alert (OBS mode) or makes a decision (GOV mode).

---

## Not a firewall. Not a guardrail.

Firewalls block indiscriminately. Guardrails constrain after the fact. Neomundi does something different: it measures risk continuously, alerts you, and makes a decision at the right moment.

No infrastructure changes. One API call. Immediate visibility.

**G-score: 0 = low risk · 1 = high risk**

> [Test it live in the sandbox](https://simulator.neomundi.io)

---

## EU AI Act — built in, not bolted on

Become compliant in 10 minutes. Without changing your architecture.

Once Neomundi is connected, every response receives a confidence score and becomes auditable.

- You know which responses are risky
- You are alerted in real time if a response becomes dangerous
- You download your audit report in one click with hallucinations detected, flagged responses, full history

No more days spent auditing after the fact.

- **OBS mode**: continuous monitoring, no constraints on your responses
- **GOV mode**: your policies enforced in real time

You do not prepare for compliance. You deploy it.

---

## What it catches

Neomundi monitors AI responses during generation and detects:

- **Hallucination spikes**: before the output is sent
- **Cost drift**: from unbounded token loops
- **Response degradation**: quality decay over sessions
- **Semantic instability**: weak signals that accumulate and make the response increasingly unreliable

---

## Why it matters

| Without Neomundi | With Neomundi |
|---|---|
| Problem discovered after the fact | Problem detected before output |
| Cost drift undetected | Drift caught in real time |
| Reliability assumed | Reliability measured |

---

## Use case — law firm

A law firm deploys an LLM to pre-draft client responses. Every response is scored before it reaches the lawyer.

- Unstable responses are flagged before anyone reads them
- Every response carries a stability score and become traceable, auditable, defensible
- Liability does not disappear. It gets measured and assigned.
- Less stress: risk is managed, visible, and under control
- For the client, a premium service: proof of compliance and information quality

---

## Documentation

- [Executive Brief](#)
- [Technical White Paper](#)
- [Scientific Foundation](#)

---

## Status

| Mode | Status | Signal |
|---|---|---|
| OBS | 🟢 Live | Early pilot onboarding open |
| GOV | 🟡 Coming | 79.5% instability detection (TruthfulQA) |

---

## FAQ

**How fast can I integrate Neomundi?**
In minutes. One API call between your app and your LLM. No SDK, no architecture change.

**What do I get immediately?**
Instant visibility on every AI response: risk level, decision signal, and audit trace.

**Does it impact performance?**
No. Start in OBS mode: zero enforcement, full transparency.

**What happens when I activate GOV mode?**
Neomundi enforces your policies in real time, blocking or allowing responses based on your risk thresholds.

**Why is this useful for my business?**
You reduce AI response risk, become auditable, and move toward compliance without slowing down your product.

**Do you store my data?**
No sensitive data is stored. Only aggregated metrics are used for reporting and optimization.

**What is the next step?**
Test the sandbox in 30 seconds. If it fits your use case, contact us to activate production access.

---

The risk of your AI responses is no longer a black box. It is traced, explainable, and scored in real time.
