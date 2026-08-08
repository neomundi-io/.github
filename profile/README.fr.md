## 🌐 Choisissez votre langue

**[🇫🇷 Français](README.fr.md)** · **[🇬🇧 Read the English version](README.md)**

---

# NeoMundi

## Couche fondamentale de mesure du comportement des IA

**Une couche de mesure commune à partir de laquelle de multiples usages peuvent dériver et autour de laquelle des infrastructures hétérogènes peuvent s’articuler.**

NeoMundi mesure en temps réel la variabilité comportementale, la stabilité et les changements de régime des systèmes d’IA.

Ses signaux peuvent alimenter de multiples usages — observation, détection de dérive, audit, gouvernance, orchestration, contrôle — tout en étant consommés par des infrastructures indépendantes qui conservent leur propre architecture, leur fonction et leur autorité décisionnelle.

**Une mesure fondamentale. Plusieurs usages. Plusieurs infrastructures.**

**Votre système. Vos décisions. Notre signal.**

[**Cadre de référence**](https://zenodo.org/records/21821522) · [**Executive Brief**](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_FR.pdf) · [**Observatoire IA NeoMundi**](https://github.com/neomundi-io/neomundi-ai-observatory/blob/main/README.fr.md) · **Launchers & cas d’usage** · [**Interopérabilité**](https://github.com/neomundi-io/runtime-interoperability-contract/blob/main/README_FR.md) · [**Sandbox**](https://controltower.neomundi.io/welcome)

---

## Ce que fait NeoMundi en 30 secondes

NeoMundi fournit une **couche fondamentale de mesure du comportement des IA en cours d’exécution**.

Elle permet notamment de :

- mesurer la stabilité, la variabilité et les changements de régime ;
- produire des signaux runtime structurés, horodatés et auditables ;
- détecter certaines situations nécessitant une attention renforcée ;
- alimenter des usages de supervision, d’audit, d’orchestration ou de gouvernance ;
- transmettre ces signaux à des infrastructures indépendantes via des interfaces interopérables.

**Une mesure fondamentale. Plusieurs usages. Plusieurs infrastructures.**

NeoMundi fournit le signal.  
L’opérateur, son système ou sa couche de règles conserve l’autorité de décision.

---

## Pourquoi c’est important

Les systèmes d’IA générative sont désormais intégrés à des workflows réels : agents autonomes, assistance métier, infrastructure, conformité, support, santé, juridique ou finance.

Une réponse peut être fluide et plausible tout en présentant une instabilité, une dérive, une rupture de régime ou une insuffisance de fondement.

Le besoin n’est donc pas seulement de produire davantage de logs ou de scores.

Il est de produire une **mesure exploitable** :

- lisible par une machine ;
- interprétable par un humain ;
- transmissible à une infrastructure tierce ;
- traçable dans le temps ;
- utilisable pour déclencher une action selon une politique explicite.

> Un signal isolé est une donnée.  
> Un signal mesuré, contextualisé et interopérable peut devenir une brique de décision.

---

## OBS d’abord. GOV lorsque le contexte l’exige.

NeoMundi propose deux modes d’intégration selon le niveau de criticité du système et le moment auquel la mesure doit intervenir.

| | **OBS — Snapshot privacy-first** | **GOV — Gouvernance temps réel** |
|---|---|---|
| **Principe** | Votre système appelle NeoMundi après une génération | NeoMundi intervient dans la boucle d’exécution |
| **Objectif** | Observer, comparer et documenter | Superviser et gouverner en temps réel |
| **Moment** | Après génération | Pendant la génération |
| **Données traitées** | Snapshot limité aux données nécessaires à l’analyse | Flux traité de manière transitoire |
| **Signaux** | État de stabilité, alertes et traces auditables | État de stabilité, `ΔG`, alertes et signaux de gouvernance |
| **Rétention** | Aucun stockage des prompts ni des réponses | Aucun stockage des prompts ni des réponses |
| **Usage naturel** | La majorité des systèmes IA | Workflows critiques ou difficilement rattrapables |

### Le bon critère de décision

> Si une mauvaise sortie atteint l’utilisateur, est-elle rattrapable ?

**Si oui**, OBS constitue généralement le point d’entrée naturel.

Votre système envoie un snapshot à NeoMundi afin de mesurer certains comportements, détecter des variations et conserver une trace exploitable.

**Si non**, GOV devient pertinent.

NeoMundi intervient dans la boucle d’exécution, suit l’évolution du signal en temps réel et permet à une politique de supervision de réagir pendant l’exécution.

---

## Signaux et artefacts de mesure

Selon le mode d’intégration, NeoMundi peut produire notamment :

- **stabilité comportementale** : état normalisé associé à une génération ou à une fenêtre d’exécution ;
- **variation de stabilité** : évolution du signal entre plusieurs fenêtres d’observation ;
- **changements de régime** : transitions observables dans le comportement du système ;
- **signaux de cohérence** : indications relatives à l’évolution de la cohérence au cours de l’exécution ;
- **métriques informationnelles** : mesures complémentaires liées à la structure et à la densité informationnelles des générations ;
- **FLAG** : signal conservateur indiquant qu’une sortie nécessite une attention renforcée ;
- **télémétrie structurée** : événements, timestamps, identifiants techniques et signaux associés ;
- **traces auditables** : exports, rapports et artefacts permettant de documenter ce qui s’est produit.

Ces signaux ne constituent pas, isolément, une preuve absolue de vérité, d’erreur ou de conformité.

Ils doivent être interprétés dans leur contexte et selon la politique du système qui les consomme.

---

## Validation expérimentale

NeoMundi a désormais produit et analysé **plus de 200 000 observations** à travers ses campagnes de mesure, baromètres, cartographies, expérimentations et pilotes.

Ces travaux couvrent plusieurs modèles, providers, protocoles et configurations d’exécution et contribuent à étudier la stabilité, la variabilité comportementale, les changements de régime et l’actionnabilité des signaux produits.

### Premières campagnes de validation du signal FLAG

Les premières campagnes utilisées pour évaluer spécifiquement la précision du signal `FLAG` représentaient un corpus cumulé de **10 160 générations**.

| Campagne | Périmètre | Générations analysées |
|---|---:|---:|
| Cartographie v1 — 2026-04-26 | 5 providers LLM | 3 904 |
| Cohorte TruthfulQA v2 — 2026-05-17 | 8 providers LLM anonymisés | 6 256 |
| **Total** | | **10 160** |

Lorsqu’un `FLAG` a été déclenché, une sortie problématique a été confirmée dans environ **76 % des cas** sur ce corpus.

| Campagne | FLAG déclenchés | Sorties problématiques confirmées | Précision observée |
|---|---:|---:|---:|
| Cartographie v1 — 2026-04-26 | 437 | 331 | 75,7 % |
| Cohorte TruthfulQA v2 — 2026-05-17 | ≈ 394 | ≈ 301 | ≈ 76,4 % |
| **Total cumulé** | **≈ 831** | **≈ 632** | **≈ 76 %** |

### Lecture correcte de ces résultats

NeoMundi ne prétend pas détecter toutes les erreurs.

L’instrument privilégie aujourd’hui la précision du signal sur une couverture exhaustive :

> mieux vaut signaler moins, mais signaler utilement, que saturer les équipes avec des faux positifs.

Ces résultats constituent une première validation expérimentale et opérationnelle.

Ils doivent être interprétés avec leurs limites : dépendance au corpus, aux providers testés, aux seuils retenus et aux protocoles de confirmation utilisés.

La consolidation se poursuit à travers les campagnes longitudinales, les audits méthodologiques, les articulations expérimentales et les pilotes terrain.

---

## Cas d’usage

Une même couche de mesure peut alimenter plusieurs usages sans imposer l’infrastructure qui les exploite.

| Usage | Ce que les signaux NeoMundi peuvent apporter | Mode naturel |
|---|---|---|
| **Agents autonomes** | Observer certaines dérives et alimenter des mécanismes d’escalade, de relance ou de reroutage | OBS · GOV |
| **Conformité et audit** | Produire des traces horodatées, documenter les signaux et soutenir la supervision | OBS · GOV |
| **Fine-tuning et évaluation** | Comparer les écarts comportementaux entre modèles, prompts, datasets ou versions | OBS |
| **SLA et infrastructure IA** | Détecter certaines dégradations comportementales et documenter les incidents | OBS · GOV |
| **Workflows sensibles** | Renforcer la supervision lorsqu’une sortie erronée serait difficilement rattrapable | GOV |

**Ces usages dérivent d’une même couche de mesure. NeoMundi n’impose pas l’infrastructure qui les exploite.**

Des launchers, orchestrateurs, systèmes de gouvernance, infrastructures de preuve ou applications métier peuvent consommer les signaux NeoMundi tout en conservant leur propre fonction et leur autorité décisionnelle.

---

## Intégration et interopérabilité

NeoMundi est conçu pour s’articuler avec des applications LLM, agents, orchestrateurs, couches de gouvernance et systèmes métier existants.

### Principes d’intégration

- intégration progressive à partir d’un appel API ;
- approche **BYOK** selon le mode et la configuration ;
- aucun stockage des prompts ni des réponses ;
- seuils et politiques configurables selon le contexte ;
- séparation entre autorité de mesure et autorité de décision ;
- exports et traces auditables selon le niveau d’intégration ;
- possibilité d’articuler les signaux avec des infrastructures externes ;
- déploiements dédiés ou environnements contrôlés selon les besoins.

### Intégration des providers LLM

NeoMundi peut être intégré aux providers LLM pris en charge via ses interfaces runtime.

Le guide d’intégration explique comment connecter un compte provider existant, configurer un modèle, gérer les clés API et transmettre des requêtes à travers ControlTowerAI.

➡️ [Read the LLM Provider Integration Guide](https://github.com/neomundi-io/controltowerai-docs/blob/main/providers.md)

### Interopérabilité

NeoMundi vise à rendre ses signaux exploitables par des systèmes indépendants sans leur imposer une architecture, une politique ou un mécanisme de gouvernance particulier.

Le contrat d’interopérabilité runtime documente les principes minimaux permettant de transmettre et interpréter ces signaux entre couches indépendantes.

➡️ [Contrat d’interopérabilité runtime](https://github.com/neomundi-io/runtime-interoperability-contract/blob/main/README_FR.md)

---

## Confidentialité et souveraineté opérationnelle

NeoMundi applique un principe de minimisation des données traitées.

Les prompts et réponses ne sont pas stockés.

Selon le mode d’intégration, seules les informations nécessaires à la mesure, à la traçabilité ou au fonctionnement des politiques associées peuvent être conservées.

NeoMundi utilise également un **juge sémantique auto-hébergé** pour certaines analyses.

Ce composant fonctionne sur une infrastructure maîtrisée par NeoMundi afin de limiter la dépendance à des services externes pour cette fonction.

Cette architecture poursuit trois objectifs :

- **confidentialité** : limiter l’exposition des données ;
- **résilience** : réduire certaines dépendances externes ;
- **souveraineté opérationnelle** : conserver la maîtrise de l’analyse et du traitement.

---

## État du produit

NeoMundi évolue progressivement afin de distinguer clairement ce qui est disponible aujourd’hui, ce qui peut être expérimenté dans le cadre de pilotes et ce qui relève encore de l’industrialisation.

| Statut | Signification |
|---|---|
| **Disponible maintenant** | Sandbox public, premières surfaces de mesure, signaux runtime et documentation méthodologique |
| **Pilote accompagné** | Intégration progressive, calibration, supervision, exports et politiques adaptées au contexte |
| **Trajectoire produit** | Extension des métriques, interopérabilité renforcée, orchestration runtime avancée et déploiements dédiés |

Cette progression permet de commencer par la mesure, puis d’articuler progressivement les usages et niveaux de gouvernance nécessaires au contexte opérationnel.
---

## Dépôts principaux — Core repositories

NeoMundi publie progressivement les fondations méthodologiques de son approche.

Chaque dépôt documente une fonction précise : mesurer les comportements IA, vérifier certaines réponses, interpréter correctement les signaux, transmettre les résultats, protéger les données ou déployer les modes OBS et GOV.

### Mesurer les comportements IA

* [`neomundi-signal-adaptation-framework`](https://github.com/neomundi-io/neomundi-signal-adaptation-framework)
  Explique comment transformer différentes sources de données en un format commun afin de pouvoir les comparer et les mesurer.

* [`runtime-telemetry-signals`](https://github.com/neomundi-io/runtime-telemetry-signals)
  Documente les signaux utilisés pour suivre le comportement d’une IA pendant son fonctionnement, notamment son niveau de stabilité et l’évolution de ce signal dans le temps.

* [`informational-metrics`](https://github.com/neomundi-io/informational-metrics)
  Présente les métriques utilisées pour analyser la quantité, la structure et la densité informationnelle des réponses générées.

* [`energy-stability-index`](https://github.com/neomundi-io/energy-stability-index)
  Documente un indice composite destiné à résumer plusieurs dimensions de stabilité. Cet indice fait partie de la trajectoire d’évolution de NeoMundi.

### Vérifier certaines réponses

* [`validity-and-grounding`](https://github.com/neomundi-io/validity-and-grounding)
  Documente le juge sémantique auto-hébergé utilisé pour repérer certains risques d’hallucination, ainsi que le module de validité permettant de vérifier une réponse par rapport à des informations ou à des documents de référence.

### Comprendre ce que signifient les signaux

* [`interpretation-contract`](https://github.com/neomundi-io/interpretation-contract)
  Précise ce que les signaux produits par NeoMundi permettent de conclure, ce qu’ils ne prouvent pas à eux seuls et quelles décisions restent sous la responsabilité du client ou de l’opérateur.

* [`Boundary Tension contract`](https://github.com/neomundi-io/Boundary_Tension_contract)
  Explore les situations où la frontière de responsabilité doit être clairement définie : entre une IA qui génère une réponse, un signal qui alerte et un humain ou un système qui décide d’agir.

### Transmettre les résultats aux autres systèmes

* [`runtime-interoperability-contract`](https://github.com/neomundi-io/runtime-interoperability-contract)
  Définit un format commun pour transmettre les signaux NeoMundi entre les outils de mesure, les agents, les applications clientes et les systèmes de supervision.

### Protéger les données

* [`neomundi-io-data-protection`](https://github.com/neomundi-io/neomundi-io-data-protection)
  Documente les principes de protection des données : minimisation des informations traitées, BYOK, absence de stockage des prompts et réponses, et préparation des cadres contractuels.

### Observer puis gouverner

* [`neomundi-obs`](https://github.com/neomundi-io/neomundi-obs)
  Présente le mode OBS : votre système appelle NeoMundi après une génération et lui transmet un snapshot limité aux données nécessaires à l’analyse. Ce mode privacy-first permet d’observer et de documenter les comportements IA sans placer NeoMundi dans la boucle d’exécution.

* [`neomundi-gov`](https://github.com/neomundi-io/neomundi-gov)
  Présente le mode GOV : NeoMundi appelle le LLM pendant l’exécution, analyse le flux en temps réel et suit notamment l’évolution du signal `ΔG`. Les prompts et réponses sont traités de manière transitoire, sans rétention.

---

L’objectif n’est pas d’établir une vérité absolue à partir d’un score unique.

L’objectif est de rendre les comportements IA plus faciles à mesurer, à vérifier, à comprendre, à transmettre, à documenter et à gouverner.


---

## FAQ

### NeoMundi détermine-t-il si une réponse est vraie ou fausse ?

Non.

NeoMundi produit des signaux permettant d’observer certaines variations, instabilités, dérives ou transitions comportementales.

Ces signaux soutiennent la décision. Ils ne remplacent ni le contexte métier, ni la supervision humaine, ni les mécanismes spécialisés de vérification lorsque ceux-ci sont nécessaires.

### Quelle différence entre OBS et GOV ?

**OBS** permet d’observer, documenter et améliorer après génération ou en supervision continue.

**GOV** intervient dans la chaîne runtime lorsqu’une sortie erronée serait difficilement rattrapable.

OBS constitue généralement le point d’entrée naturel.

GOV augmente le niveau de contrôle lorsque le contexte l’exige.

### Quelles données sont stockées ?

NeoMundi est conçu selon un principe de minimisation des données.

Les prompts et réponses ne sont pas stockés.

Selon le mode retenu, seuls les métriques, signaux, événements techniques, identifiants nécessaires, timestamps et artefacts de reporting peuvent être conservés.

### NeoMundi fonctionne-t-il avec mon LLM ?

OBS est conçu pour être compatible avec des systèmes capables de transmettre les artefacts d’observation attendus.

GOV suit une logique d’intégration progressive selon les providers, workflows et niveaux de criticité.

### Quelle différence avec LangSmith, Portkey ou Helicone ?

Ces outils sont principalement centrés sur l’observabilité applicative : logs, tracing, coûts, workflows et performance.

NeoMundi ajoute une couche complémentaire orientée mesure et gouvernance comportementale : stabilité, variation, signaux runtime, interprétation, auditabilité et politiques de supervision.

### NeoMundi couvre-t-il certaines exigences de l’EU AI Act et du RGPD ?

NeoMundi ne remplace pas une démarche complète de conformité, une analyse juridique ni une certification réglementaire.

ControlTower couvre néanmoins plusieurs capacités techniques directement utiles aux démarches IA Act et RGPD :

* monitoring continu du comportement des systèmes IA ;
* contrôle du risque des réponses générées ;
* traçabilité opérationnelle ;
* auditabilité ;
* signaux exploitables pour la supervision humaine ;
* éléments de preuve utiles à la documentation des incidents ;
* architecture privacy-first fondée sur la minimisation des données et l’absence de stockage des prompts et réponses.

La pertinence juridique dépend du système concerné, de son usage, de son niveau de risque et du rôle de l’organisation.

➡️ [Consulter le mapping détaillé des capacités NeoMundi pour l’IA Act et le RGPD](https://github.com/neomundi-io/ai-act-rgpd)

---

## Écosystème & soutien d’infrastructure

NeoMundi développe ses travaux au sein d’un écosystème ouvert de contributeurs techniques, de recherche, de gouvernance et d’infrastructure.

### NVIDIA Inception Program

NeoMundi est membre du programme NVIDIA Inception.

<img src="https://raw.githubusercontent.com/neomundi-io/neomundi-sandbox/main/nvidia-inception-program-badge-rgb-for-screen.png"
  alt="NeoMundi est membre du programme NVIDIA Inception"
  width="180">

© 2025 NVIDIA, le logo NVIDIA et NVIDIA Inception sont des marques commerciales et/ou des marques déposées de NVIDIA Corporation aux États-Unis et dans d’autres pays.

### Soutien d’infrastructure

L’Observatoire IA NeoMundi est soutenu par des partenaires d’infrastructure souveraine, dont Infomaniak.

<img src="https://raw.githubusercontent.com/neomundi-io/neomundi-ai-observatory/main/logos/ecosystem/logo_infomaniak.png"
  alt="Infomaniak"
  width="150">

Ces relations soutiennent le développement et l’exploitation de capacités indépendantes de mesure des IA, d’auditabilité et de gouvernance runtime. Elles n’impliquent pas que les organisations citées ci-dessus cautionnent les résultats de recherche, les mesures ou les interprétations de NeoMundi.

---

## Ressources

* [NeoMundi Sandbox](https://controltower.neomundi.io/welcome)
* [NeoMundi Website](https://neomundi.io)
* [Executive Brief — FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/NeoMundi_Executive_Brief_2026_FR.pdf)
* [Executive Brief — EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/NeoMundi_Executive_Brief_2026_EN.pdf)
* [AI Observability & Behavioral Metrology — FR / EN](https://zenodo.org/records/21250268)
* [Theoretical Framework (Law E) — FR](https://doi.org/10.5281/zenodo.19385052)

---

## Contact

Vous opérez des systèmes IA en production, des agents autonomes ou des workflows sensibles ?

**Mesurez ce qui est récupérable. Contrôlez ce qui ne l’est pas.**

[contact@neomundi.io](mailto:contact@neomundi.io)
