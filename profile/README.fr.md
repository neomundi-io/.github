# NeoMundi. Le thermomètre de l'IA.

[🇬🇧 Read in English](#english-version)

---

**Validation en temps réel de la stabilité des décisions, au moment où elles se produisent.**

Nous fournissons le signal.
Vous décidez quoi en faire.

📄 Méthodologie · DOI [10.5281/zenodo.19762753](https://doi.org/10.5281/zenodo.19762753) · Repo [llm-cartography](https://github.com/neomundi-io/llm-cartography)

---

## Le signal runtime de stabilité.
### Au service de la gouvernance, du fine-tuning, de la conformité et de la due diligence.

| 🟣 Agents | 🟢 Conformité | 🟡 Fine-tuning | 🔵 SLA / Infra |
|-----------|---------------|----------------|----------------|
| **Stopper. Relancer. Rerouter.** | **Tracer & prouver.** | **Mesurer la dérive.** | **Prouver la continuité.** |
| Signal de stabilité en direct, injecté dans les boucles de décision des agents. | Piste d'audit horodatée. Chaque génération scorée, chaque dérive signalée. | Quantifier les écarts comportementaux entre versions de modèles. | Supervision comportementale au-delà de la latence. Qualité de génération, mesurée. |

> **Votre décision, notre signal.**

---

## Mesure et détection

NeoMundi calcule un score de stabilité en temps réel (G) à partir d'un signal multivarié capturant la cohérence sémantique, la consistance et la stabilité structurelle pendant la génération.

Cette mesure s'appuie sur un cadre de stabilité dynamique inspiré des principes de Lyapunov, où les variations (ΔG) reflètent les écarts aux régimes stables.

L'instrument évalue et met à jour ce signal en continu au runtime, permettant une détection immédiate des dérives et des instabilités.

**NeoMundi détecte l'instabilité avant qu'elle ne devienne visible :**

- Contradictions internes
- Perte de précision
- Dérive thématique
- Incohérence structurelle

> *La dérive apparaît avant la défaillance. Nous la mesurons en temps réel.*
>
> *NeoMundi ne dit pas si c'est vrai. Il dit si c'est cohérent.*

### Validé sur des systèmes réels

**Cartographie v1-2026-04-26 — 3 904 mesures TruthfulQA × 5 services génératifs.**

NeoMundi n'attrape pas encore tout (≈15 % de recall), **mais quand il flag, il a raison ≈76 % du temps**. Un signal fiable sur lequel agir dès maintenant.

L'instrument s'affine. **Module Vérité actif le 27 mai 2026.**

📊 Métriques complètes, dataset et méthodologie : [llm-cartography](https://github.com/neomundi-io/llm-cartography).

---

## Chaque génération produit

**Sorties standard :**
- Score de stabilité (0 → 1)
- Décision (PASS / FLAG)
- Signal de dérive (horodaté)

**Sorties avancées :**
- Trace d'audit complète (exportable)
- Métriques d'exécution (coût, stabilité, dérive)
- Preuve cryptographique (hash)
- Jeux de données structurés (analytique, fine-tuning, conformité)

> *Signal réel. Scoring réel. Résultat réel.*

---

## Voir en action

→ [Essayer en direct](https://neomundi.io/sandbox) : sans installation, sans clé API.
→ [Exemple de rapport d'audit PDF](https://neomundi.io/sample-audit.pdf)

---

## Intégration en une ligne

**Bring Your Own Key. Full privacy.** Votre clé fournisseur reste sous votre contrôle. NeoMundi mesure le signal de stabilité de la génération sans jamais lire ni stocker le contenu de vos prompts ou réponses.

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

L'instrument est servi par la plateforme ControlTower. Préfixe de clé API : `ct_live_*`.

→ [Guide d'intégration complet](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/QUICKSTART.md)

---

## Roadmap

L'infrastructure est active. Elle s'industrialise.

- **27 mai 2026** : Module Vérité actif (vérification factuelle au-delà de la cohérence)
- **Mai-Juin 2026** : Plateforme self-service en production
- **Q3 2026** : Seuils configurables par client, dashboard opérateurs

Les opérateurs pilotes actuels sont prioritaires sur chaque mise à jour.

---

## FAQ

**Qu'est-ce que le score de stabilité ?**
Il mesure la cohérence interne d'une réponse LLM en temps réel — pas sa véracité. NeoMundi ne vérifie pas les faits. Il détecte la dérive qui précède l'erreur.

**Quelles données stockez-vous ?**
Vos prompts ne sont ni lus ni stockés. Votre clé API fournisseur reste sous votre contrôle. Seules les métriques de gouvernance sont enregistrées : score, décision, horodatage. Rien d'autre.

**Fonctionne-t-il avec mon LLM ?**
Oui — détection automatique depuis votre clé : OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. Si votre fournisseur n'est pas listé, contactez-nous.

**Quelle est la différence avec LangSmith, Portkey ou Helicone ?**
Ces outils observent et journalisent. NeoMundi mesure et signale pendant la génération — avant que la réponse instable n'atteigne votre utilisateur. Nous ne remplaçons pas votre stack d'observabilité, nous y ajoutons la couche de mesure manquante.

**Est-ce conforme à l'EU AI Act ?**
NeoMundi contribue aux exigences de traçabilité et d'auditabilité de l'EU AI Act en produisant une piste d'audit complète par session : score, décision, horodatage, export PDF. L'échéance d'application est août 2026.

---

## Open Science · Reproductible · Auditable

Auditabilité intégrée dès la conception. Pas une boîte noire.

- 📄 Méthodologie complète et versionnée : [llm-cartography](https://github.com/neomundi-io/llm-cartography)
- 🔬 Dataset de référence : [DOI 10.5281/zenodo.19762753](https://doi.org/10.5281/zenodo.19762753)
- 📐 Cadre théorique (loi E) : [DOI 10.5281/zenodo.19385052](https://doi.org/10.5281/zenodo.19385052)

---

> *Mesurer le comportement de l'IA en temps réel.*
> *Si vous opérez de l'IA en production, vous avez besoin d'un signal.*
> *Agissez avant que l'instabilité n'atteigne vos utilisateurs.*

`contact@neomundi.io`

---

NeoMundi Recherche, association loi 1901, Vannes (France).
Activités commerciales : Louis M Sàrl, Morges (Suisse).

*À la vitesse de la génération. Construit pour durer.*

---

<a id="english-version"></a>

# NeoMundi. The AI thermometer.

[🇫🇷 Lire en français](#neomundi-le-thermomètre-de-lia)

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

→ [Try it live](https://neomundi.io/sandbox): no installation, no API key.
→ [Sample audit report PDF](https://neomundi.io/sample-audit.pdf)

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

→ [Full integration guide](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/QUICKSTART.md)

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
