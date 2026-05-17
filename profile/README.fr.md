# NeoMundi. Le thermomètre de l’IA.

Observabilité de gouvernance runtime pour les systèmes d’IA générative.

Détection précoce de signaux d’instabilité générative, sans accès au contenu.

OBS pour l’observabilité de gouvernance.
GOV pour l’orchestration runtime lorsque l’intervention devient critique.

Nous fournissons le signal. Vous décidez quoi en faire.

Déployable au-dessus des stacks LLM, agents et couches d’orchestration.

<sub>EN · [Read in English](./README.md)</sub>

---

## Pourquoi c'est important

Les systèmes d’IA dérivent avant que les problèmes deviennent visibles.

NeoMundi produit des signaux d’observabilité de gouvernance permettant de détecter précocement :

- dérives comportementales,
- incohérences,
- pertes de stabilité,
- schémas associés aux hallucinations.

En mode OBS, sans accès au contenu.

---

## Deux modes de déploiement

ControlTower™ : une tour de contrôle pour la gouvernance des systèmes d’IA générative.  
Observabilité continue en OBS. Orchestration runtime en GOV lorsque l’intervention devient critique.

|                  | **OBS** (Observabilité)                          | **GOV** (Gouvernance)                          |
|------------------|--------------------------------------------------|------------------------------------------------|
| Finalité         | Observabilité de gouvernance                     | Orchestration de gouvernance runtime           |
| Moment           | Post-exécution / observabilité continue          | Pendant la génération                          |
| Confidentialité  | Aucun contenu, métriques uniquement              | Contenu transitoire, sans rétention ni log     |
| Intégration      | Le LLM appelle NeoMundi (post-stream)            | NeoMundi appelle le LLM (BYOK runtime)         |
| Adapté à         | La majorité des systèmes IA                      | Workflows critiques                            |

> **Modèle d'action en OBS.** NeoMundi produit des signaux d’observabilité de gouvernance exploitables par les agents en aval ou les couches d’orchestration. Bloquer, régénérer ou faire remonter : la décision reste au client.

**Critère de décision : si une mauvaise sortie atteint l'utilisateur, est-elle rattrapable ?**

- **Rattrapable** (alerte, modération en aval, correction au cycle suivant) : OBS suffit.
- **Non rattrapable** (conseil médical, conseil juridique livré directement, décisions financières fiduciaires, infrastructure critique, art. 14 du règlement IA européen) : GOV devient nécessaire.

OBS est le point d’entrée naturel pour la majorité des systèmes IA.  
GOV intervient lorsque la gouvernance runtime et l’orchestration temps réel deviennent critiques.

---

## Signaux d’instabilité observables

NeoMundi produit des signaux d’observabilité de gouvernance associés notamment à :

- contradictions internes,
- pertes de cohérence,
- dérives thématiques,
- instabilités progressives,
- schémas associés aux hallucinations.

> NeoMundi ne détermine pas si une réponse est vraie.
> NeoMundi produit des signaux permettant d’observer si elle reste comportementalement stable.

---

## Validé sur des systèmes réels

Les évaluations actuelles ont été réalisées principalement en mode GOV, dans des configurations runtime contrôlées.

- **5 fournisseurs LLM** testés (cartographie v1-2026-04-26)
- **3 904 générations** analysées (TruthfulQA)
- Lorsque NeoMundi FLAG, le signal est confirmé dans **≈76 % des cas** (recall actuel ≈15 %)
- Mise en évidence précoce de signaux d’instabilité avant que les problèmes deviennent visibles

L’instrument s’affine progressivement.

Module de validation factuelle prévu le 27 mai 2026.

📂 [Métriques, dataset, méthodologie](https://github.com/neomundi-io/llm-cartography)

---

## Cas d'usage

| Domaine | Bénéfice | Mode |
|---|---|---|
| 🟣 **Agents** | Observer les dérives, rerouter, escalader ou relancer selon la politique runtime | **OBS** · GOV runtime |
| 🟢 **Conformité** | Piste d’audit horodatée, signaux de gouvernance associés aux générations | **OBS** · GOV runtime |
| 🟡 **Fine-tuning** | Observer les écarts comportementaux entre versions de modèles | **OBS** · GOV runtime |
| 🔵 **SLA / Infra** | Observabilité comportementale et supervision runtime des générations | **OBS** · GOV runtime |

> Votre décision, notre signal.

---

## Artefacts et signaux produits

Selon le mode OBS ou GOV, NeoMundi peut produire notamment :

- **État de stabilité gouvernance** (normalisé de 0 → 1)
- **Décision de gouvernance** (PASS / FLAG)
- **Signaux de variation runtime** (ΔG, horodatés)
- **Télémétrie structurée** (analytique, conformité, supervision runtime)
- **Traces auditables** (exports et reporting par session)

→ [Exemple de rapport d'audit PDF](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## Intégration

Deux modes, deux endpoints.  
Le choix dépend du niveau de criticité et du besoin de gouvernance runtime.

### Mode OBS · post-exécution · metrics-only

**Aucun contenu transmis. Aucune clé fournisseur.**  
Vos métriques en entrée, vos signaux de gouvernance en sortie.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "sess_xxx",
    "metrics": { ... }
  }'
```

### Mode GOV · runtime · orchestration pendant la génération

**Bring Your Own Key. Full privacy.**  
Votre clé fournisseur reste sous votre contrôle.

NeoMundi traite le flux générationnel en runtime afin de produire des signaux de gouvernance et d’orchestration, sans rétention ni journalisation des prompts ou réponses.

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

L’instrument est servi par la plateforme ControlTower™.  
Préfixe des clés API : `ct_live_*`.


→ [Démarrage rapide](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/QUICKSTART)
→ **[100 requêtes gratuites pour tester les deux modes](https://controltower.neomundi.io/pricing)**

---

## Deux postures de confidentialité, adaptées aux deux modes

|                              | **OBS**                                  | **GOV**                                       |
|------------------------------|------------------------------------------|-----------------------------------------------|
| Contenu (prompts, réponses)  | Jamais transmis                          | Flux transitoire, sans journalisation ni rétention |
| Clé fournisseur              | Jamais transmise                         | BYOK                                           |
| Stockage                     | Métriques et artefacts de gouvernance uniquement | Métriques et artefacts de gouvernance uniquement |

Les deux modes sont conçus selon une approche privacy-by-design compatible avec les exigences DPO, RSSI et compliance modernes.

---

## Roadmap

L’infrastructure est active. Elle poursuit son industrialisation.

- **27 mai 2026** : Couche de validation factuelle expérimentale
- Plateforme self-service en production
- Seuils configurables et dashboard opérateurs
- Structuration progressive de la télémétrie runtime (OBS / GOV)

Les opérateurs pilotes restent prioritaires sur les évolutions de la plateforme.

---

## FAQ

**OBS ou GOV ?**  
OBS = observabilité de gouvernance post-exécution, sans transmission de contenu, métriques uniquement.  
GOV = orchestration runtime pendant la génération, BYOK, flux transitoire sans journalisation ni rétention.

OBS est le point d’entrée naturel pour la majorité des systèmes IA.  
GOV intervient lorsqu’un mauvais output atteignant un utilisateur devient non rattrapable.

---

**Qu'est-ce que l’état de stabilité gouvernance ?**  
Il représente un état normalisé de stabilité comportementale observé pendant ou après une génération LLM.  
NeoMundi ne mesure pas la vérité d’une réponse, mais produit des signaux permettant d’observer certaines variations et instabilités comportementales.

---

**Quelles données stockez-vous ?**  
OBS : aucun contenu transmis.  
GOV : flux transitoire traité en runtime, sans journalisation ni rétention des prompts ou réponses.

Seules les métriques et artefacts de gouvernance sont conservés : état de stabilité, décision, horodatage et reporting associé.

Votre clé fournisseur (mode GOV) reste sous votre contrôle.

---

**Fonctionne-t-il avec mon LLM ?**  
OBS : tout LLM, y compris local ou non listé (vous produisez les métriques, NeoMundi reçoit les artefacts associés).  
GOV : OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere, avec détection automatique via votre clé fournisseur.

---

**Quelle différence avec LangSmith, Portkey ou Helicone ?**  
Ces outils observent et journalisent principalement les workflows et exécutions applicatives.  
NeoMundi ajoute une couche complémentaire d’observabilité et de gouvernance runtime orientée signaux comportementaux et télémétrie gouvernance.

Nous ne remplaçons pas votre stack d’observabilité ; nous ajoutons une couche de gouvernance runtime.

---

**Conforme à l’EU AI Act ?**  
NeoMundi produit des artefacts de gouvernance exploitables pour la traçabilité, l’auditabilité et le reporting runtime : état de stabilité, décisions de gouvernance, horodatage et exports associés.

Ces éléments peuvent contribuer aux exigences de supervision et de traçabilité prévues par l’EU AI Act (application progressive à partir d’août 2026).

---

## Documentation

- 📄 [Executive Brief — FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_FR.pdf)
- 🔬 [Cadre théorique (Loi E) — FR](https://doi.org/10.5281/zenodo.19385052)

---

> *Mesurer le comportement de l'IA en continu. Si vous opérez de l'IA en production, vous avez besoin d'un signal. Observez ce qui est récupérable. Contrôlez ce qui ne l'est pas.*

📧 contact@neomundi.io
