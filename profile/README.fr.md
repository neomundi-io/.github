EN · [Read in English](./README.md)

# NeoMundi. Le thermomètre de l’IA.

**Observabilité en temps réel et signaux de gouvernance pour les systèmes d’IA générative.**

NeoMundi est une couche de signal en temps réel déployable au-dessus des stacks LLM, des agents et des systèmes d’orchestration.

Elle aide les équipes IA à mesurer l’instabilité, la dérive et les signaux pertinents pour la gouvernance avant d’appliquer leurs politiques.

> **Un appel API. BYOK. Protection des données par conception. Aucun stockage des contenus.**

**Llama auto-hébergé est disponible pour certaines fonctions de gouvernance.**
Une voie d’inférence souveraine pour renforcer la confidentialité, la résilience et la maîtrise opérationnelle.

Nous fournissons le signal.
**Votre système, votre politique ou l’opérateur responsable conserve l’autorité de décision.**

OBS d’abord. GOV lorsque vous êtes prêt.

*Appelez l’instrument. Observez la dérive. Configurez vos seuils. Gouvernez en temps réel.*

---

## Cadre NeoMundi de gouvernance en temps réel

NeoMundi évolue **du thermomètre vers le spectromètre** : d’un signal de stabilité en temps réel vers une couche de mesure multidimensionnelle du comportement des systèmes d’IA pendant leur exécution.

> **Le cadre inclut désormais une voie d’inférence Llama auto-hébergée pour certaines fonctions de gouvernance.**

Cette évolution renforce trois exigences fondamentales de la gouvernance industrielle de l’IA :

* **confidentialité**, en réduisant l’exposition inutile des données sensibles ;
* **résilience**, en limitant la dépendance aux services d’inférence externes ;
* **souveraineté opérationnelle**, en permettant à certaines fonctions de gouvernance de s’exécuter sur une infrastructure maîtrisée par NeoMundi.

Un signal de gouvernance en temps réel doit répondre à trois exigences minimales :

> **être observable, interprétable et interopérable.**

Le cadre NeoMundi de gouvernance en temps réel organise ces exigences à travers plusieurs dépôts méthodologiques publics consacrés à l’observabilité, aux métriques informationnelles, à l’interprétation, à l’interopérabilité et à la gouvernance en temps réel des systèmes d’IA.

> **Mesurer. Interpréter. Transmettre. Décider. Tracer.**


---

## Cadre NeoMundi de gouvernance en temps réel

NeoMundi évolue du thermomètre vers le spectromètre : d’un signal de stabilité en temps réel vers une couche de mesure multidimensionnelle du comportement des systèmes d’IA pendant leur exécution.

Le cadre inclut désormais une voie d’inférence Llama auto-hébergée pour certaines fonctions de gouvernance.

Cette évolution renforce trois exigences fondamentales de la gouvernance industrielle de l’IA :

- **confidentialité**, en réduisant l’exposition inutile des données sensibles ;
- **résilience**, en limitant la dépendance aux services d’inférence externes ;
- **souveraineté opérationnelle**, en permettant à certaines fonctions de gouvernance de s’exécuter sur une infrastructure maîtrisée par NeoMundi.

Un signal de gouvernance en temps réel doit répondre à trois exigences minimales : il doit être observable, interprétable et interopérable.

Le cadre NeoMundi de gouvernance en temps réel organise ces exigences à travers plusieurs dépôts méthodologiques publics consacrés à l’observabilité, aux métriques informationnelles, à l’interprétation, à l’interopérabilité et à la gouvernance en temps réel des systèmes d’IA.

Ensemble, ces dépôts constituent les fondations minimales d’une infrastructure industrialisable de gouvernance de l’IA : mesurer, interpréter, transmettre, décider, tracer.

---

### Dépôts principaux - Core repositories

- [`neomundi-signal-adaptation-framework`](https://github.com/neomundi-io/neomundi-signal-adaptation-framework)  
  Couche SAL : point d’entrée architectural pour adapter des sources hétérogènes vers un état canonique mesurable par NeoMundi.

- [`runtime-telemetry-signals`](https://github.com/neomundi-io/runtime-telemetry-signals)  
  Définitions publiques des signaux de télémétrie runtime, incluant G, ΔG et les états de gouvernance.

- [`informational-metrics`](https://github.com/neomundi-io/informational-metrics)  
  Notes méthodologiques publiques sur la volumétrie, la densité volumétrique, l’énergie informationnelle et la densité informationnelle.

- [`energy-stability-index`](https://github.com/neomundi-io/energy-stability-index)  
  Documentation conceptuelle de l’Energy Stability Index comme indicateur composite de gouvernance.

- [`validity-and-grounding`](https://github.com/neomundi-io/validity-and-grounding)  
  Documentation méthodologique publique sur la validité, l’ancrage, la détection d’hallucination et les limites des signaux liés à la preuve.

- [`runtime-interoperability-contract`](https://github.com/neomundi-io/runtime-interoperability-contract)  
  Sémantique minimale d’interopérabilité entre les couches de mesure, d’orchestration et d’ancrage de preuve.

- [`neomundi-io-data-protection`](https://github.com/neomundi-io/neomundi-io-data-protection)  
  Documentation publique de l’architecture privacy NeoMundi : minimisation des données, BYOK, absence de stockage des contenus, modes de traitement OBS/GOV et notes de préparation DPA.

- [`interpretation-contract`](https://github.com/neomundi-io/interpretation-contract)  
  Frontières méthodologiques pour l’interprétation des signaux, des métriques et des décisions de gouvernance.

- [`neomundi-obs`](https://github.com/neomundi-io/neomundi-obs)  
  Couche OBS : observabilité post-hoc, sans orchestration runtime.

- [`neomundi-gov`](https://github.com/neomundi-io/neomundi-gov)  
  Couche GOV : gouvernance runtime et orchestration pendant la génération.

- [`Boundary Tension contract`](https://github.com/neomundi-io/Boundary_Tension_contract)  
  Dépôt de recherche conceptuelle consacré aux signaux de tension aux frontières dans les systèmes IA runtime.

L'objectif n'est pas d'établir une vérité absolue.

L'objectif est de rendre le comportement de génération de l'IA observable, interprétable, interopérable, auditable et gouvernable en temps réel.

---

## Pourquoi c’est important

Un signal de gouvernance n’a de valeur que s’il peut être compris, transmis, interprété et utilisé par un système réel.

La difficulté n’est pas seulement de produire un score.  
La difficulté est de produire un signal exploitable dans une infrastructure de gouvernance : lisible par une machine, interprétable par un humain, traçable par un audit, et actionnable par une couche d’orchestration.

NeoMundi construit ses signaux selon cette exigence industrielle :

- observabilité : le signal décrit une surface mesurable ;
- interprétabilité : le signal déclare ce qu’il signifie et ce qu’il ne signifie pas ;
- interopérabilité : le signal peut circuler entre couches indépendantes ;
- gouvernabilité : le signal peut soutenir une décision sans s’y substituer ;
- auditabilité : le signal peut être documenté, horodaté et relu après exécution.

Un signal isolé n’est pas une infrastructure.  
Un signal spécifié, contextualisé et interopérable peut devenir une brique de gouvernance.

C’est le rôle du NeoMundi Runtime Governance Framework : rendre les comportements génératifs observables, interprétables et gouvernables avant que les dérives ne deviennent invisibles, irréversibles ou coûteuses.

---

## Deux modes de déploiement

ControlTower™ agit comme une tour de contrôle pour la gouvernance des systèmes d’IA générative.

OBS fournit une observabilité de gouvernance après génération.  
GOV fournit une orchestration runtime lorsque l’intervention pendant l’exécution devient critique.

|                  | **OBS** (Observabilité)                          | **GOV** (Gouvernance)                          |
|------------------|--------------------------------------------------|------------------------------------------------|
| Finalité         | Observabilité de gouvernance                     | Orchestration de gouvernance runtime           |
| Moment           | Post-exécution / observabilité continue          | Pendant la génération                          |
| Confidentialité  | Aucun contenu, métriques uniquement              | Contenu transitoire, sans rétention ni log     |
| Intégration      | Le système appelle ControlTower après génération | ControlTower appelle le LLM en runtime (BYOK)  |
| Adapté à         | La majorité des systèmes IA                      | Workflows critiques                            |

> **Modèle d’action en OBS.** ControlTower produit des signaux d’observabilité de gouvernance exploitables par les agents en aval ou les couches d’orchestration. Bloquer, régénérer ou faire remonter : la décision reste au client.

**Critère de décision : si une mauvaise sortie atteint l’utilisateur, est-elle rattrapable ?**

- **Rattrapable** : alerte, modération en aval, correction au cycle suivant → OBS suffit.
- **Non rattrapable** : conseil médical, conseil juridique livré directement, décision financière fiduciaire, infrastructure critique, supervision humaine renforcée → GOV devient nécessaire.

OBS est le point d’entrée naturel pour la majorité des systèmes IA.  
GOV intervient lorsque la gouvernance runtime et l’orchestration temps réel deviennent critiques.

---

## Cas d’usage

Ces usages peuvent mobiliser des niveaux différents de profondeur : signal simple, métriques avancées, auditabilité renforcée ou reporting de conformité.

| Usage | Ce que NeoMundi apporte | Mode naturel |
|---|---|---|
| 🟣 **Agents** | Signaux runtime pour observer les dérives, rerouter, escalader ou relancer selon la politique d’orchestration | **OBS** · GOV runtime |
| 🟡 **Fine-tuning** | Métriques informationnelles pour comparer les écarts comportementaux entre versions de modèles, prompts ou datasets | **OBS** |
| 🟢 **Conformité** | Piste d’audit horodatée, décisions de gouvernance, rapports et traçabilité des générations | **OBS** · GOV runtime |
| 🔵 **SLA / Infra** | Supervision comportementale des générations, détection de dégradation et documentation des incidents runtime | **OBS** · GOV runtime |

> Votre décision, notre signal.

---

## Types de signaux observables

NeoMundi ne détermine pas seul si une réponse est vraie.

Il produit des signaux runtime permettant d’observer des variations de stabilité, des pertes de cohérence, des dérives progressives, des ruptures de régime ou des schémas compatibles avec des hallucinations.

Ces signaux ne sont pas des preuves absolues.  
Ils rendent les générations IA plus observables, interprétables, traçables et gouvernables.

---

## Validé sur des systèmes réels

La surface publique documente les concepts, les signaux et les contrats méthodologiques.
Les évaluations actuelles ont été réalisées principalement en mode GOV, dans des configurations runtime contrôlées.

- **5 fournisseurs LLM** testés (cartographie v1-2026-04-26)
- **3 904 générations** analysées (TruthfulQA)
- Lorsque NeoMundi FLAG, le signal est confirmé dans **≈76 % des cas** (recall actuel ≈15 %)
- Mise en évidence précoce de signaux d’instabilité avant que les problèmes deviennent visibles

La validation opérationnelle se poursuit à travers des audits indépendants, des pilotes terrain et des analyses contrôlées.

📂 [Métriques, dataset, méthodologie](https://github.com/neomundi-io/llm-cartography)



---

## Artefacts et signaux produits

Selon le mode OBS ou GOV, NeoMundi peut produire plusieurs familles d’artefacts d’observabilité et de gouvernance.

Ces artefacts ne constituent pas des vérités absolues.  
Ils servent à rendre les générations IA observables, interprétables, traçables et gouvernables.

NeoMundi peut notamment produire :

- **État de stabilité de gouvernance** : signal normalisé associé à une génération ou un segment d’exécution.
- **Variation runtime de stabilité** : ΔG, variation observée entre plusieurs fenêtres d’exécution.
- **Métriques informationnelles** : volumétrie, densité volumétrique, énergie informationnelle, densité informationnelle.
- **Indice composite** : ESI, lecture synthétique multidimensionnelle de gouvernance.
- **Décisions de gouvernance** : ALLOW, FLAG, BLOCK ou états équivalents selon la politique appliquée.
- **Télémétrie structurée** : événements, timestamps, identifiants de requête, signaux associés.
- **Traces auditables** : exports, rapports, journaux et artefacts de reporting selon le mode et le niveau d’intégration.

> Un signal observe.  
> Une décision oriente l’action.  
> L’interprétation reste contextuelle.

---

## Intégration

Ajoutez une couche de signal runtime à vos agents, applications LLM ou systèmes d’orchestration en quelques minutes.

Un appel API permet à votre système de recevoir des signaux exploitables pour observer, décider, relancer, rerouter, escalader ou documenter une génération IA.

Selon le niveau de criticité, vous pouvez commencer avec OBS, tester GOV, puis configurer progressivement vos seuils, vos politiques d’action et vos exports depuis ControlTower™.

### Ce que l’intégration apporte

- **OBS** : observabilité post-hoc, métriques uniquement, sans contenu transmis.
- **GOV** : orchestration runtime pendant la génération, avec clé provider côté client, BYOK.
- **Signaux runtime** : stabilité, variation, régime, décision de gouvernance.
- **Auditabilité** : timestamps, traces, exports, rapports.
- **Interopérabilité** : signaux exploitables par agents, orchestrateurs et couches de contrôle.
- **Déploiement souverain possible** : installation dédiée, image Docker, environnement contrôlé selon les besoins

- [Quickstart API & Sandbox NeoMundi](https://github.com/neomundi-io/neomundi-sandbox)  
  Documentation de démarrage, exemples d’intégration et accès aux ressources de test.

---

## FAQ

**OBS ou GOV ?**  

OBS est le mode d’observabilité post-exécution : ControlTower™ reçoit des métriques ou artefacts d’observation, sans transmission de contenu sémantique complet.

GOV est le mode de gouvernance runtime : ControlTower™ intervient pendant la génération, avec clé fournisseur côté client, traitement transitoire du flux, sans journalisation ni rétention des prompts ou réponses.

OBS est le point d’entrée naturel pour la majorité des systèmes IA.  
GOV devient pertinent lorsqu’un mauvais output atteignant l’utilisateur serait difficilement rattrapable.

---

**Qu’est-ce que l’état de stabilité de gouvernance ?**  

Il s’agit d’un état normalisé associé à la stabilité comportementale observée pendant ou après une génération IA.

NeoMundi ne prétend pas déterminer seul si une réponse est vraie.  
NeoMundi produit des signaux permettant d’observer certaines variations, instabilités, dérives ou transitions comportementales.

---

**Quelles données sont stockées ?**  

En mode OBS : aucun contenu sémantique complet n’est transmis.

En mode GOV : le flux est traité de manière transitoire pendant l’exécution, sans journalisation ni rétention des prompts ou réponses.

Seuls les métriques, signaux et artefacts de gouvernance peuvent être conservés : état de stabilité, décision, horodatage, identifiants techniques et reporting associé.

La clé fournisseur utilisée en mode GOV reste sous le contrôle du client.

---

**Fonctionne-t-il avec mon LLM ?**  

OBS peut être utilisé avec tout système IA capable de transmettre des métriques ou artefacts d’observation à ControlTower™.

GOV est conçu pour fonctionner avec des providers LLM compatibles via une logique BYOK, selon les intégrations disponibles.

---

**Quelle différence avec LangSmith, Portkey ou Helicone ?**  

Ces outils sont principalement centrés sur l’observabilité applicative, le tracing, les logs, les coûts, les workflows et les performances.

NeoMundi ajoute une couche complémentaire de gouvernance runtime orientée signaux : stabilité, variation, densité informationnelle, décisions de gouvernance et auditabilité.

NeoMundi ne remplace pas votre stack d’observabilité.  
NeoMundi ajoute une couche de mesure et de gouvernance comportementale.

---

**NeoMundi couvre-t-il certaines exigences de l’EU AI Act by design ?**

NeoMundi ne remplace pas une démarche complète de conformité.

En revanche, ControlTower™ contribue by design à certaines exigences de gouvernance IA : contrôle runtime, journalisation, traçabilité, supervision et auditabilité.

Les artefacts produits, signaux de stabilité, décisions de gouvernance, horodatages, identifiants techniques, exports et rapports, peuvent soutenir la documentation, le suivi et la maîtrise des risques des systèmes IA.


---

## Documentation

- 📄 [Executive Brief — FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_FR.pdf)
- 🔬 [Cadre théorique (Loi E) — FR](https://doi.org/10.5281/zenodo.19385052)

---

*Mesurer le comportement de l’IA en continu.  
Si vous opérez de l’IA en production, vous avez besoin d’un signal.  
Observez ce qui est récupérable. Contrôlez ce qui ne l’est pas.*

contact@neomundi.io
