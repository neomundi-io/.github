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

---

## Ressources NeoMundi

### 1. Connecter la couche de mesure

[**Interface universelle de mesure**](https://github.com/neomundi-io/neomundi-measurement-interoperability/tree/main)  
Connectez les signaux de mesure NeoMundi à votre infrastructure grâce à un contrat d’interopérabilité signé, versionné et vérifiable indépendamment.

---

### 2. Essayer en pratique

[**Cas d’usage**](https://github.com/neomundi-io/neomundi-use-cases)  
Pilotes documentés, expérimentations orientées production et intégrations opérationnelles utilisant les signaux de mesure NeoMundi.

[**Launchers**](https://github.com/neomundi-io/neomundi-launchers)  
Implémentations de référence permettant de déployer des workflows opérationnels concrets autour des signaux de mesure NeoMundi.

[**Sandbox**](https://controltower.neomundi.io/welcome)  
Accédez à l’environnement de mesure NeoMundi et testez directement la couche de mesure runtime.

---

### 3. Métrologie, méthodologie et preuves

[**Metric Contract & Measurement Reference**](https://github.com/neomundi-io/neomundi-metric-contract)  
Définitions sémantiques, frontières de mesure, reproductibilité, traçabilité et portabilité des signaux de mesure runtime NeoMundi.

[**Metrology Validation**](https://github.com/neomundi-io/neomundi-metrology-validation)  
Validation expérimentale, calibration, reproductibilité et cadre de preuve associés aux signaux de mesure NeoMundi.

[**Observatoire IA**](https://github.com/neomundi-io/neomundi-ai-observatory)  
Observations publiques, baromètres, cartographies et analyses longitudinales du comportement des IA en runtime.

---

### 4. Comprendre NeoMundi

[**Executive Brief**](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)  
Présentation synthétique du positionnement de NeoMundi, de sa couche de mesure et de son modèle opérationnel.

[**Reference Framework**](https://zenodo.org/records/21821522)  
Architecture fondatrice et cadre conceptuel de la métrologie runtime NeoMundi.

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

NeoMundi a désormais produit et analysé **plus de 200 000 observations** à travers ses campagnes longitudinales de mesure, baromètres, cartographies, expérimentations contrôlées et pilotes terrain.

Le programme d’observation actuel couvre **12 systèmes d’IA**, répartis entre différents providers, modèles, protocoles et configurations d’exécution.

Ces travaux contribuent notamment à étudier :

- la stabilité et la variabilité comportementales ;
- les changements de régime et les dérives longitudinales ;
- la reproductibilité des signaux de mesure ;
- l’actionnabilité des signaux et scores produits ;
- leur interopérabilité avec des infrastructures d’IA hétérogènes.

➡️ [Observatoire IA NeoMundi](https://github.com/neomundi-io/neomundi-ai-observatory/blob/main/README.fr.md)  
➡️ [Observatoire de recherche NeoMundi](https://neomundi.org/)

### Consolidation du cadre de mesure

Le programme expérimental NeoMundi ne repose pas sur un seul axe de validation.

En complément de l’observation longitudinale, des travaux dédiés à la **reproductibilité** et à l’**actionnabilité** contribuent progressivement à consolider le cadre de mesure.

L’objectif est d’établir si les signaux produits sont non seulement observables, mais également :

1. reproductibles dans des conditions comparables ;
2. sensibles à des changements comportementaux significatifs ;
3. interprétables dans des limites méthodologiques explicites ;
4. exploitables par des opérateurs, des couches de gouvernance et des infrastructures indépendantes.

Ces travaux contribuent à la validation progressive des signaux, métriques et scores dérivés produits par NeoMundi.

### Corpus initial de validation du signal FLAG

Les premières campagnes contrôlées utilisées spécifiquement pour évaluer la précision du signal `FLAG` représentaient un corpus cumulé de **10 160 générations**.

| Campagne | Périmètre | Générations analysées |
|---|---:|---:|
| Cartographie v1 — 2026-04-26 | 5 providers LLM | 3 904 |
| Cohorte TruthfulQA v2 — 2026-05-17 | 8 providers LLM anonymisés | 6 256 |
| **Total** | | **10 160** |

Lorsqu’un `FLAG` a été déclenché, une sortie problématique a été confirmée dans environ **76 % des cas** sur ce corpus de validation.

| Campagne | FLAG déclenchés | Sorties problématiques confirmées | Précision observée |
|---|---:|---:|---:|
| Cartographie v1 — 2026-04-26 | 437 | 331 | 75,7 % |
| Cohorte TruthfulQA v2 — 2026-05-17 | ≈ 394 | ≈ 301 | ≈ 76,4 % |
| **Total cumulé** | **≈ 831** | **≈ 632** | **≈ 76 %** |

### Comment lire ces résultats

NeoMundi ne prétend pas détecter toutes les erreurs.

L’instrument privilégie aujourd’hui la précision du signal sur une couverture exhaustive :

> mieux vaut signaler moins, mais signaler utilement, que saturer les opérateurs avec des faux positifs.

Les résultats du `FLAG` constituent un premier axe de validation au sein d’un programme métrologique plus large.

Ils doivent être interprétés dans leurs limites méthodologiques, notamment leur dépendance au corpus, aux providers, aux seuils et aux protocoles de confirmation utilisés.

La validation est progressivement renforcée par **l’observation longitudinale, les études de reproductibilité, les travaux sur l’actionnabilité, les audits méthodologiques, les articulations indépendantes et les pilotes terrain**.

---

## Cas d’usage

Une même couche de mesure peut alimenter de multiples usages sans imposer l’infrastructure qui les exploite.

| Usage | Ce que les signaux NeoMundi rendent possible | Mode de mesure |
|---|---|---|
| **Agents autonomes** | Détecter certaines variations ou dérives afin qu’un orchestrateur puisse déclencher une escalade, une relance ou un reroutage | OBS · GOV |
| **Conformité et audit** | Produire des mesures horodatées et des traces exploitables pour documenter le comportement d’un système | OBS · GOV |
| **Évaluation et comparaison** | Comparer les comportements entre modèles, prompts, datasets, versions ou configurations | OBS |
| **Infrastructure IA et SLA** | Identifier certaines dégradations comportementales et documenter leur évolution dans le temps | OBS · GOV |
| **Workflows sensibles** | Fournir des signaux runtime pouvant alimenter une supervision renforcée ou une politique externe de contrôle | GOV |
| **Monitoring longitudinal** | Mesurer l’évolution d’un système dans le temps et identifier des changements de régime ou de profil comportemental | OBS |
| **Recherche et métrologie** | Produire des observations comparables pour étudier stabilité, variabilité, reproductibilité et transitions comportementales | OBS |

**Ces usages dérivent d’une même couche de mesure.**

NeoMundi n’impose ni l’application, ni l’orchestrateur, ni la politique qui exploite ses signaux.

Des launchers, agents, systèmes de gouvernance, infrastructures de preuve, outils d’audit ou applications métier peuvent consommer les signaux NeoMundi tout en conservant leur propre architecture, leur fonction et leur autorité décisionnelle.

> **Une mesure fondamentale. Plusieurs usages. Plusieurs infrastructures.**

---

## Intégration et interopérabilité

NeoMundi est conçu comme une couche indépendante pouvant s’articuler avec des applications LLM, agents, orchestrateurs, plateformes d’observabilité, systèmes de gouvernance et infrastructures métier existantes.

### Principes d’intégration

- intégration progressive via API ;
- compatibilité avec plusieurs modèles, providers et architectures ;
- approche **BYOK** lorsque le mode d’intégration le permet ;
- minimisation des données transmises ;
- aucun stockage des prompts ni des réponses ;
- production de signaux et artefacts structurés ;
- séparation entre **autorité de mesure** et **autorité de décision** ;
- possibilité pour des infrastructures externes de consommer et interpréter les signaux ;
- déploiements contrôlés ou dédiés selon les besoins.

NeoMundi n’a pas vocation à remplacer les infrastructures existantes.

La couche de mesure peut au contraire être utilisée par des systèmes indépendants qui conservent leurs propres fonctions de logging, orchestration, gouvernance, preuve ou contrôle.

### Intégration des providers LLM

Les interfaces runtime NeoMundi permettent d’articuler la mesure avec les providers et modèles pris en charge.

Le guide d’intégration documente la connexion aux providers, la configuration des modèles et la gestion des clés nécessaires aux modes d’intégration concernés.

➡️ [LLM Provider Integration Guide](https://github.com/neomundi-io/controltowerai-docs/blob/main/providers.md)

### Interopérabilité

L’interopérabilité constitue un principe central de l’architecture NeoMundi.

L’objectif est qu’un signal de mesure puisse être produit par une couche, transmis à une autre, interprété dans un cadre explicite puis utilisé par une infrastructure indépendante — sans transfert implicite d’autorité entre ces différentes fonctions.

Le **Runtime Interoperability Contract** documente la sémantique minimale permettant cette articulation entre couches indépendantes.

➡️ [Contrat d’interopérabilité runtime](https://github.com/neomundi-io/runtime-interoperability-contract/blob/main/README_FR.md)

---

## Confidentialité et souveraineté opérationnelle

NeoMundi applique un principe de minimisation des données traitées.

Les prompts et réponses ne sont pas stockés.

Selon le mode d’intégration, seules les informations nécessaires à la mesure, à la traçabilité et à la production des artefacts associés peuvent être conservées.

NeoMundi utilise également un **juge sémantique auto-hébergé** pour certaines analyses.

Ce composant fonctionne sur une infrastructure maîtrisée par NeoMundi afin de limiter la dépendance à des services externes pour cette fonction de mesure.

Cette architecture poursuit trois objectifs :

- **confidentialité** : limiter l’exposition des données ;
- **résilience** : réduire les dépendances externes critiques ;
- **souveraineté opérationnelle** : conserver la maîtrise de la chaîne de mesure et de traitement.

---

## État du produit

NeoMundi distingue clairement la couche de mesure disponible aujourd’hui, les intégrations expérimentées avec des partenaires et les éléments encore en cours d’industrialisation.

| Statut | Signification |
|---|---|
| **Disponible maintenant** | API et surfaces de mesure, signaux runtime, sandbox, documentation méthodologique et premières interfaces d’intégration |
| **Pilotes et articulations** | Intégration avec des agents, orchestrateurs, infrastructures de gouvernance, systèmes de preuve et applications indépendantes |
| **Industrialisation** | Extension du domaine de mesure, consolidation des métriques, interopérabilité standardisée, performances et options de déploiement |

La trajectoire consiste à renforcer progressivement **la mesure elle-même et sa capacité à être consommée par des infrastructures hétérogènes**, plutôt qu’à centraliser les usages dans NeoMundi.

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

NeoMundi mesure certains aspects du comportement des systèmes d’IA : stabilité, variabilité, dérive, changements de régime et autres signaux associés.

Ces mesures peuvent contribuer à identifier des sorties nécessitant une attention renforcée, mais elles ne constituent pas à elles seules une preuve de vérité, d’erreur ou de conformité.

L’interprétation reste contextuelle et peut être complétée par des mécanismes spécialisés de vérification, des règles métier ou une supervision humaine.

### Quelle différence entre OBS et GOV ?

**OBS** mesure le comportement d’un système après génération ou à travers des observations successives.

Il constitue généralement le mode d’intégration le plus simple et le point d’entrée naturel pour la majorité des systèmes.

**GOV** permet d’effectuer certaines mesures pendant l’exécution lorsque le contexte nécessite une supervision plus rapprochée.

Dans les deux cas, NeoMundi produit la mesure et les signaux associés.

L’application, l’orchestrateur, la politique externe ou l’opérateur conserve l’autorité de décision.

### Quelles données sont stockées ?

NeoMundi applique un principe de minimisation des données.

Les prompts et réponses ne sont pas stockés.

Selon le mode d’intégration, seuls les métriques, signaux, événements techniques, identifiants nécessaires, timestamps et artefacts requis pour la mesure, la traçabilité ou l’audit peuvent être conservés.

### NeoMundi fonctionne-t-il avec mon LLM ou mon infrastructure ?

NeoMundi est conçu pour être indépendant d’un modèle ou d’un provider particulier.

La couche de mesure peut s’articuler progressivement avec différents modèles, providers, agents, orchestrateurs et infrastructures d’IA.

**OBS** peut être utilisé lorsqu’un système est capable de transmettre les artefacts nécessaires à la mesure.

**GOV** nécessite une intégration runtime plus profonde et dépend des providers, architectures et workflows concernés.

L’objectif est que des infrastructures hétérogènes puissent consommer les signaux NeoMundi tout en conservant leur propre architecture et leur fonction.

### Quelle différence avec LangSmith, Portkey, Helicone ou d’autres plateformes d’observabilité ?

Ces plateformes couvrent principalement des fonctions d’observabilité applicative telles que les logs, traces, coûts, latences, workflows ou performances opérationnelles.

NeoMundi se concentre sur un domaine complémentaire : **la mesure du comportement des systèmes d’IA**.

La couche NeoMundi vise notamment à rendre mesurables et comparables :

- la stabilité comportementale ;
- la variabilité ;
- certaines dérives ;
- les changements de régime ;
- certains signaux de cohérence ;
- des métriques informationnelles ;
- leur évolution dans le temps.

NeoMundi n’a donc pas vocation à remplacer une stack d’observabilité.

Ses signaux peuvent au contraire être consommés par des plateformes d’observabilité, des orchestrateurs, des systèmes de gouvernance ou d’autres infrastructures indépendantes.

### NeoMundi est-il un système de gouvernance ?

NeoMundi fournit une **couche de mesure pouvant alimenter des mécanismes de gouvernance**, mais la mesure et la décision restent deux fonctions distinctes.

Un signal NeoMundi peut par exemple être utilisé par un système externe pour :

- déclencher une alerte ;
- demander une revue humaine ;
- relancer une génération ;
- rerouter une requête ;
- appliquer une politique de contrôle.

La décision finale appartient au système, à la politique ou à l’opérateur qui consomme le signal.

### NeoMundi couvre-t-il certaines exigences de l’EU AI Act et du RGPD ?

NeoMundi ne remplace ni une démarche complète de conformité, ni une analyse juridique, ni une certification réglementaire.

La couche de mesure et les outils associés peuvent néanmoins fournir plusieurs capacités techniques utiles à des démarches de conformité, notamment :

- suivi du comportement des systèmes d’IA dans le temps ;
- traçabilité des observations et signaux ;
- documentation de certaines variations ou incidents ;
- production d’artefacts auditables ;
- signaux exploitables pour la supervision humaine ;
- minimisation des données traitées ;
- absence de stockage des prompts et réponses dans les modes concernés.

La pertinence réglementaire dépend du système, de son usage, de son niveau de risque et du rôle de l’organisation qui le déploie.

➡️ [Consulter le mapping détaillé des capacités NeoMundi pour l’AI Act et le RGPD](https://github.com/neomundi-io/ai-act-rgpd)

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

## Contact

Vous opérez des systèmes IA en production, des agents autonomes ou des workflows sensibles ?

**Mesurez le comportement des IA. Construisez sur le signal.**

[contact@neomundi.io](mailto:contact@neomundi.io)
