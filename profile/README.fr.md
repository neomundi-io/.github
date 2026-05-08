# NeoMundi. Le thermomètre de l'IA.

**Mesure continue de la stabilité des IA.**

Détection précoce du risque génératif, sans accès au contenu.

Post-hoc ou en temps réel, selon la criticité.

Nous fournissons le signal. Vous décidez quoi en faire.

*Déployable au-dessus de toute stack LLM, agent ou orchestrateur.*

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

|                  | **OBS** (Observatoire)                | **GOV** (Gouvernance)                       |
|------------------|---------------------------------------|---------------------------------------------|
| Finalité         | Surveillance continue                 | Contrôle actif en temps réel                |
| Moment           | Flux continu, post-hoc                | Pendant la génération                       |
| Confidentialité  | Aucun contenu, métriques uniquement   | Contenu transitoire, sans rétention ni log  |
| Intégration      | Le LLM appelle NeoMundi (post-stream) | NeoMundi appelle le LLM (BYOK runtime)      |
| Adapté à         | La majorité des systèmes IA           | Workflows critiques                         |

> **Modèle d'action en OBS.** NeoMundi émet un signal de stabilité continu, exploitable par les agents en aval ou les couches d'orchestration. Bloquer, régénérer ou faire remonter : la décision reste au client.

**Critère de décision : si une mauvaise sortie atteint l'utilisateur, est-elle rattrapable ?**

- **Rattrapable** (alerte, modération en aval, correction au cycle suivant) : OBS suffit.
- **Non rattrapable** (conseil médical, conseil juridique livré directement, décisions financières fiduciaires, infrastructure critique, art. 14 du règlement IA européen) : GOV est requis.

OBS est le point d'entrée naturel pour la majorité des systèmes IA. GOV intervient lorsque le contrôle temps réel devient critique.

---

## Instabilités détectées

- contradictions internes
- perte de cohérence
- dérive thématique
- instabilité progressive
- schémas d'hallucination

> NeoMundi ne dit pas si une réponse est vraie.
> NeoMundi mesure si elle reste stable.

---

## Validé sur des systèmes réels

- **5 fournisseurs LLM** testés (cartographie v1-2026-04-26)
- **3 904 générations** analysées (TruthfulQA)
- Quand NeoMundi flag, il a raison **≈76 % du temps** (15 % de recall actuel)
- Détection précoce, avant la défaillance visible

L'instrument s'affine. Module Vérité actif le 27 mai 2026.

📂 [Métriques, dataset, méthodologie](https://github.com/neomundi-io/llm-cartography)

---

## Cas d'usage

| Domaine | Bénéfice | Mode |
|---|---|---|
| 🟣 **Agents** | Détecter la dérive, stopper, relancer, rerouter | **OBS** · GOV runtime |
| 🟢 **Conformité** | Piste d'audit horodatée, chaque génération scorée | **OBS** · GOV runtime |
| 🟡 **Fine-tuning** | Quantifier les écarts entre versions de modèles | **OBS** · GOV runtime |
| 🔵 **SLA / Infra** | Supervision comportementale, qualité de génération mesurée | **OBS** · GOV runtime |

> Votre décision, notre signal.

---

## Chaque génération retourne

- **Score de stabilité** (0 → 1)
- **Décision** (PASS / FLAG)
- **Signal de dérive** (ΔG, horodaté)
- **Télémétrie structurée** (analytique, fine-tuning, conformité)
- **Traces auditables** (export PDF par session)

→ [Exemple de rapport d'audit PDF](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## Intégration

Deux modes, deux endpoints. Choix selon le critère de tri ci-dessus.

### Mode OBS, post-hoc, metrics-only

**Aucun contenu transmis. Aucune clé fournisseur.** Vos métriques in, votre score out.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "sess_xxx",
    "metrics": { ... }
  }'
```

### Mode GOV, runtime, contrôle pendant

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

→ [Démarrage rapide](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/QUICKSTART)
→ **[100 requêtes gratuites pour tester les deux modes](https://controltower.neomundi.io/pricing)**

---

## Deux postures de privacy, les deux maximales

|                              | **OBS**                       | **GOV**                                |
|------------------------------|-------------------------------|----------------------------------------|
| Contenu (prompts, réponses)  | Jamais transmis               | Transitoire, sans log, sans rétention  |
| Clé fournisseur              | Jamais transmise              | BYOK            |
| Stockage                     | Métriques + score uniquement  | Métriques + score uniquement               |

Les deux modes sont conçus pour passer une revue DPO, RSSI ou Compliance sans concession.

---

## Roadmap

L'infrastructure est active. Elle s'industrialise.

- **27 mai 2026** : Module Vérité (vérification factuelle au-delà de la cohérence)
- Plateforme self-service en production
- Seuils configurables, dashboard opérateurs

Les opérateurs pilotes sont prioritaires sur chaque mise à jour.

---

## FAQ

**OBS ou GOV ?**
OBS = monitoring continu, sans accès au contenu, métriques uniquement. GOV = contrôle pendant la génération, BYOK, contenu transitoire sans rétention. OBS est la porte d'entrée pour la majorité des cas. GOV intervient quand un mauvais output qui atteint un utilisateur n'est pas rattrapable.

**Qu'est-ce que le score de stabilité ?**
Il mesure la cohérence interne d'une réponse LLM en temps réel, pas sa véracité. NeoMundi détecte la dérive qui précède l'erreur.

**Quelles données stockez-vous ?**
Aucun contenu, ni en OBS ni en GOV. Seules les métriques de gouvernance sont enregistrées : score, décision, horodatage. Votre clé fournisseur (en GOV) reste sous votre contrôle.

**Fonctionne-t-il avec mon LLM ?**
OBS : tout LLM, y compris local ou non listé (vous calculez les métriques, nous les recevons). GOV : OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere, détection automatique depuis votre clé.

**Quelle différence avec LangSmith, Portkey, Helicone ?**
Ces outils observent et journalisent après coup. NeoMundi mesure et signale pendant la génération. Nous ne remplaçons pas votre stack d'observabilité, nous y ajoutons la couche de mesure manquante.

**Conforme à l'EU AI Act ?**
NeoMundi produit une piste d'audit complète par session (score, décision, horodatage, export PDF) qui contribue aux exigences de traçabilité et d'auditabilité. Échéance d'application : août 2026.

---

## Repos

L'écosystème GitHub de NeoMundi :

- **[llm-cartography](https://github.com/neomundi-io/llm-cartography)** : instrument scientifique public, cartographie v1, dataset, méthodologie versionnée.
- **controltower-quickstart** *(à venir)* : exemples d'intégration, démo OBS vs GOV, notebook Colab cliquable.

---

## Documentation

- 📄 [Executive Brief — FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_FR.pdf)
- 🔬 **Cadre théorique (loi E)**, DOI Zenodo : [10.5281/zenodo.19385052](https://doi.org/10.5281/zenodo.19385052)

---

> *Mesurer le comportement de l'IA en continu. Si vous opérez de l'IA en production, vous avez besoin d'un signal. Observez ce qui est récupérable. Contrôlez ce qui ne l'est pas.*

📧 contact@neomundi.io
