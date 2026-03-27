# Neomundi — Runtime AI Stability Monitor

> 🇫🇷 [Lire en français](README.fr.md)

---

## ⚡ Your AI isn't wrong. It drifts.

Neomundi doesn't check whether your AI is right.
It measures whether your AI is stable.

Every response gets a score.
When stability drops, you know — before the response is sent.

**G-score: 0 = stable · 1 = unstable**

> [Test it live →](https://neomundi-io.github.io/neomundi-sandbox/)

---

## What drift looks like

Neomundi detects four signals in real time:

- **Internal contradiction** — the response contradicts itself
- **Loss of precision** — accuracy degrades mid-response
- **Topic drift** — the response departs from the original thread
- **Tone inconsistency** — tone or logic becomes inconsistent

None of these require knowing the truth.
They only require measuring coherence.

---

## Why drift matters

In our tests (TruthfulQA), instability signals precede up to 79% of incorrect responses.

Neomundi doesn't detect the truth.
It detects the drift that comes before it.

---

## What you get

**OBS mode** — every response is scored and traced. Nothing is blocked.
You have a full audit trail: every response, every score, every timestamp.

**GOV mode** — when drift crosses your threshold, the response is flagged or can be interrupted.
Before it reaches anyone.

---

## The audit argument

A drifting response that was sent is your liability.
A drifting response that was caught is your proof of control.

Neomundi turns every AI interaction into an auditable record.

---

## One API call. No infrastructure change.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"mode": "OBS", "session_id": "abc123"}'
```

---

## Status

| Mode | Status |
|---|---|
| OBS | 🟢 Live — pilot onboarding open |
| GOV | 🟡 Coming |

---

## Documentation

- [Executive Brief](#)
- [Technical White Paper](#)
- [Scientific Foundation (Zenodo)](#)

---

*Stability is not assumed. It is measured.*
