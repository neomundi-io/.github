# NeoMundi. Le thermomètre de l'IA.

**Mesure continue de la stabilité des IA.** Détection précoce du risque génératif, sans accès au contenu.
Post-hoc ou en temps réel, selon la criticité.

Nous fournissons le signal. Vous décidez quoi en faire.

*Déployable au-dessus de n'importe quelle stack LLM.*

<sub>EN · [Read in English](./README.md)</sub>

---

## Pourquoi c'est important

Les systèmes d'IA dérivent avant d'échouer.

NeoMundi mesure en continu, avant que la défaillance soit visible :

- dérive
- incohérence
- effondrement
- schémas d'hallucination

En mode OBS, sans accès au contenu.

---

## Deux modes de déploiement

ControlTower™ : une tour de contrôle pour la génération d'IA. Observation continue, intervention uniquement si nécessaire.

|                  | **OBS** (Observatoire)        | **GOV** (Gouvernance)              |
|------------------|-------------------------------|------------------------------------|
| Finalité         | Surveillance continue         | Contrôle actif en temps réel       |
| Moment           | Après la génération           | Pendant la génération              |
| Confidentialité  | Aucun contenu, métriques uniquement | Contenu transitoire, sans rétention ni log |
| Intégration      | Le LLM appelle NeoMundi (post-stream)           | NeoMundi appelle le LLM (BYOK runtime)        |
| Adapté à         | La majorité des systèmes IA   | Workflows critiques                |

> **Modèle d'action en OBS.** NeoMundi émet un signal de stabilité continu, exploitable par les agents en aval ou les couches d'orchestration. Bloquer, régénérer ou faire remonter : la décision reste au client.

**Critère de décision : si une mauvaise sortie atteint l'utilisateur, est-elle rattrapable ?**

- **Rattrapable** (alerte, modération en aval, correction au cycle suivant) : OBS suffit.
- **Non rattrapable** (conseil médical, conseil juridique livré directement, décisions financières fiduciaires, infrastructure critique, art. 14 du règlement IA européen) : GOV est requis.

OBS est le point d'entrée naturel pour la majorité des systèmes IA. GOV intervient lorsque le contrôle temps réel devient critique.

---

## Ce que NeoMundi détecte

- contradictions internes
- perte de cohérence
- dérive thématique
- instabilité progressive
- schémas d'hallucination

> NeoMundi ne dit pas si une réponse est vraie.
> NeoMundi mesure si elle reste stable.

---

## Mesure et détection

NeoMundi calcule un score de stabilité (G) à partir d'un signal multivarié capturant la cohérence sémantique, la consistance et la stabilité structurelle pendant la génération.

L'instrument évalue et met à jour le signal en continu, permettant la détection immédiate de la dérive et de l'instabilité.

NeoMundi capte l'instabilité avant qu'elle ne devienne visible :

- Contradictions internes
- Perte de précision
- Dérive thématique
- Incohérence structurelle

La dérive apparaît avant la défaillance. Nous la mesurons en temps réel. NeoMundi ne dit pas si c'est vrai. NeoMundi dit si c'est cohérent.


---

## Validé sur des systèmes réels

Cartographie v1-2026-04-26 — 3 904 mesures TruthfulQA × 5 services génératifs.

NeoMundi n'attrape pas encore tout (≈15 % de recall), **mais quand il flag, il a raison ≈76 % du temps**. Un signal fiable pour gouverner.

L'instrument s'affine. Module Vérité actif le 27 mai 2026.

📂 Métriques complètes, dataset et méthodologie : [llm-cartography](https://github.com/neomundi-io/llm-cartography).

---

## Cas d'usage

| 🟣 Agents | 🟢 Conformité | 🟡 Fine-tuning | 🔵 SLA / Infra |
|---|---|---|---|
| Stopper. Relancer. Rerouter. | Tracer & prouver. | Mesurer la dérive. | Prouver la continuité. |
| Signal de stabilité en direct, injecté dans les boucles de décision des agents. | Piste d'audit horodatée. Chaque génération scorée, chaque dérive signalée. | Quantifier les écarts comportementaux entre versions de modèles. | Supervision comportementale au-delà de la latence. Qualité de génération, mesurée. |
| **Mode : OBS** | **Mode : OBS** *(GOV si blocage temps réel exigé)* | **Mode : OBS** | **Mode : OBS** |

> Votre décision, notre signal.

---

## Chaque génération produit

**Sorties standard**

- Score de stabilité (0 → 1)
- Décision (PASS / FLAG)
- Signal de dérive (horodaté)

**Sorties avancées**

- Jeux de données structurés (analytique, fine-tuning, conformité)
- Signal réel. Scoring réel. Résultat réel.

→ [Exemple de rapport d'audit PDF](#)

---

## Intégration

Deux modes, deux endpoints. Choix selon le critère de tri ci-dessus.

### Mode OBS — post-hoc, metrics-only

Aucun contenu transmis. Aucune clé fournisseur. Vos métriques in, votre score out.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "sess_xxx",
    "metrics": { ... }
  }'
```

### Mode GOV — runtime, contrôle pendant

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

→ [Guide d'intégration complet](#)
→ **[100 requêtes gratuites pour tester les deux modes](https://controltower.neomundi.io/pricing)**

---

## Deux postures de privacy, les deux maximales

| | **OBS** | **GOV** |
|---|---|---|
| Contenu (prompts, réponses) | Jamais transmis | Transitoire, sans log, sans rétention |
| Clé fournisseur | Jamais transmise | BYOK, sous votre contrôle |
| Stockage | Métriques + score uniquement | Aucun contenu stocké |
| Hébergement | UE | UE |

Les deux modes sont conçus pour passer une revue DPO, RSSI ou Compliance sans concession.

---

## Roadmap

L'infrastructure est active. Elle s'industrialise.

- **27 mai 2026** : Module Vérité actif (vérification factuelle au-delà de la cohérence) + Plateforme self-service en production (seuils configurables par client, dashboard opérateurs).

Les opérateurs pilotes actuels sont prioritaires sur chaque mise à jour.

---

## FAQ

**Quelle différence entre OBS et GOV ?**
OBS mesure post-hoc, en metrics-only : aucun contenu, aucune clé fournisseur ne transitent. C'est la porte d'entrée, adaptée à la majorité des cas d'usage. GOV mesure en runtime, en enrichissant le signal thermodynamique d'une couche sémantique : le flux transite par notre couche le temps strict de la mesure. À utiliser quand un mauvais output qui atteint un utilisateur n'est pas récupérable.

**Qu'est-ce que le score de stabilité ?**
Il mesure la cohérence interne d'une réponse LLM en temps réel — pas sa véracité. NeoMundi ne vérifie pas les faits, il détecte la dérive qui précède l'erreur.

**Quelles données stockez-vous ?**
En OBS : aucune donnée de contenu, ni en transit ni en stockage. Seules les métriques de gouvernance sont enregistrées (score, décision, horodatage).
En GOV : vos prompts ne sont ni lus ni stockés. Votre clé API fournisseur reste sous votre contrôle. Seules les métriques de gouvernance sont enregistrées.

**Fonctionne-t-il avec mon LLM ?**
En OBS : oui, n'importe quel modèle, y compris locaux ou non listés (vous calculez les métriques en local et nous les transmettez).
En GOV : OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere — détection automatique depuis votre clé. Si votre fournisseur n'est pas listé, contactez-nous.

**Quelle est la différence avec LangSmith, Portkey ou Helicone ?**
Ces outils observent et journalisent. NeoMundi mesure et signale — avant que la réponse instable n'atteigne votre utilisateur (GOV) ou pour permettre à vos agents d'agir avant livraison (OBS). Nous ne remplaçons pas votre stack d'observabilité, nous y ajoutons la couche de mesure manquante.

**Est-ce conforme à l'EU AI Act ?**
NeoMundi contribue aux exigences de traçabilité et d'auditabilité de l'EU AI Act en produisant une piste d'audit complète par session : score, décision, horodatage, export PDF. L'échéance d'application est août 2026.

---

## Repos

L'écosystème GitHub de NeoMundi :

- **[llm-cartography](https://github.com/neomundi-io/llm-cartography)** — instrument scientifique public. Cartographie v1, dataset, méthodologie versionnée.
- **controltower-quickstart** *(à venir)* — exemples d'intégration, démo OBS vs GOV, notebook Colab cliquable.

---

## Documentation

- 📑 **Executive Brief (FR)** — vue synthétique pour décideurs → [NeoMundi_Executive_Brief_FR.pdf](#)
- 📐 **Méthodologie complète** — spec scientifique versionnée → [llm-cartography](https://github.com/neomundi-io/llm-cartography)
- 📂 **Dataset de référence v1-2026-04-26** — DOI Zenodo → [10.5281/zenodo.19762753](https://doi.org/10.5281/zenodo.19762753)
- 🔬 **Cadre théorique (loi E)** — DOI Zenodo → [10.5281/zenodo.19385052](https://doi.org/10.5281/zenodo.19385052)

---

> *Mesurer le comportement de l'IA en continu. Si vous opérez de l'IA en production, vous avez besoin d'un signal. Observez ce qui est récupérable. Contrôlez ce qui ne l'est pas.*

📧 contact@neomundi.io
