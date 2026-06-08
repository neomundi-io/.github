## 🌐 Choisissez votre langue

**[🇫🇷 Français](README.fr.md)** · **[🇬🇧 Read the English version](README.md)**

---

# NeoMundi

## Instrument de diagnostic et de pilotage en temps réel des comportements IA

**Réduire le risque. Améliorer la maîtrise opérationnelle.**

NeoMundi fournit une couche de mesure comportementale pour les systèmes d’IA générative et les agents autonomes.

L’instrument produit des signaux exploitables pour observer les dérives, documenter les incidents, déclencher une supervision renforcée et soutenir des politiques de gouvernance adaptées au niveau de criticité.

**Votre décision, notre signal.**

[Accéder au sandbox](https://controltower.neomundi.io/welcome) · [Découvrir NeoMundi](https://neomundi.io)

---

## Ce que fait NeoMundi en 30 secondes

NeoMundi permet de :

- observer les variations de stabilité et les ruptures de régime pendant ou après une génération ;
- produire des signaux runtime structurés, horodatés et auditables ;
- détecter certaines sorties nécessitant une attention renforcée ;
- soutenir des actions telles qu’une alerte, une revue humaine, une régénération ou un reroutage ;
- conserver l’autorité de décision du côté de l’opérateur, de son système ou de sa couche de règles.

NeoMundi ne prétend pas déterminer seul si une réponse est vraie.

L’objectif est plus opérationnel :

> rendre le comportement génératif observable, interprétable, interopérable, traçable et gouvernable.

---

## Pourquoi c’est important

Les systèmes d’IA générative sont de plus en plus intégrés à des workflows réels : agents autonomes, assistance métier, conformité, support, infrastructure, santé, juridique ou finance.

Or une réponse peut être fluide, plausible et pourtant instable, insuffisamment fondée ou inadaptée au contexte.

La difficulté n’est donc pas uniquement de produire un score.

La difficulté est de produire un signal :

- lisible par une machine ;
- compréhensible par un humain ;
- exploitable par une couche d’orchestration ;
- documentable après exécution ;
- utilisable sans transférer automatiquement l’autorité de décision à l’instrument.

Un signal isolé n’est pas une infrastructure.

Un signal spécifié, contextualisé et interopérable peut devenir une brique de gouvernance.

---

## OBS d’abord. GOV lorsque vous êtes prêt.

NeoMundi propose deux modes d’intégration selon le niveau de criticité du système.

|                      | OBS — Snapshot privacy-first                        | GOV — Gouvernance temps réel                                 |
| -------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| **Principe**         | Votre système appelle NeoMundi après une génération | NeoMundi appelle le LLM pendant l’exécution                  |
| **Objectif**         | Observer, comparer et documenter                    | Superviser et gouverner en temps réel                        |
| **Moment**           | Après génération                                    | Pendant la génération                                        |
| **Données traitées** | Snapshot limité aux données nécessaires à l’analyse | Flux traité de manière transitoire                           |
| **Signaux**          | État de stabilité, alertes, traces auditables       | État de stabilité, `ΔG`, alertes et décisions de gouvernance |
| **Rétention**        | Aucun stockage des prompts ni des réponses          | Aucun stockage des prompts ni des réponses                   |
| **Usage naturel**    | La majorité des systèmes IA                         | Workflows critiques ou difficilement rattrapables            |

### Le bon critère de décision

> Si une mauvaise sortie atteint l’utilisateur, est-elle rattrapable ?

**Si oui**, OBS constitue généralement le point d’entrée naturel.

Votre système envoie un snapshot à NeoMundi afin d’observer les comportements, détecter certaines dérives et conserver une trace exploitable.

**Si non**, GOV devient pertinent.

NeoMundi intervient dans la boucle d’exécution, appelle le LLM, suit l’évolution du signal en temps réel et permet d’appliquer une politique de supervision renforcée.

Dans les deux cas, NeoMundi fournit le signal.

Votre système, votre couche de règles ou l’opérateur responsable conserve l’autorité de décision.


---

## Ce que NeoMundi observe

NeoMundi produit des signaux permettant d’observer certains comportements pendant ou après la génération :

- variations de stabilité ;
- pertes de cohérence ;
- dérives progressives ;
- ruptures de régime ;
- schémas compatibles avec certaines sorties problématiques ;
- variations informationnelles entre générations, modèles, prompts ou versions.

Ces signaux ne constituent pas des preuves absolues.

Ils servent à rendre les générations IA plus observables, interprétables, traçables et gouvernables.

### Familles de signaux et d’artefacts

Selon le mode d’intégration et le niveau de maturité du déploiement, NeoMundi peut produire :

- **état de stabilité de gouvernance** : état normalisé associé à une génération ou à une fenêtre d’exécution ;
- **variation runtime de stabilité** : évolution du signal entre plusieurs fenêtres d’observation ;
- **FLAG** : signal conservateur indiquant qu’une sortie mérite une attention renforcée ;
- **métriques informationnelles** : mesures complémentaires liées à la structure informationnelle des générations ;
- **décisions de gouvernance** : états tels que `ALLOW`, `FLAG`, `BLOCK` ou équivalents selon la politique du client ;
- **télémétrie structurée** : événements, timestamps, identifiants techniques et signaux associés ;
- **traces auditables** : exports, rapports et artefacts de reporting selon le niveau d’intégration.

> Un signal observe.  
> Une décision oriente l’action.  
> L’interprétation reste contextuelle.

---

## Premiers résultats expérimentaux

NeoMundi a été testé sur plusieurs campagnes contrôlées portant sur des services d’IA générative accessibles par API.

### Corpus cumulé

| Campagne | Périmètre | Générations analysées |
|---|---:|---:|
| Cartographie v1 — 2026-04-26 | 5 providers LLM | 3 904 |
| Cohorte TruthfulQA v2 — 2026-05-17 | 8 providers LLM anonymisés | 6 256 |
| **Total** |  | **10 160** |

### Précision observée du signal FLAG

Lorsqu’un `FLAG` a été déclenché, une sortie problématique a été confirmée dans environ **76 %** des cas sur le corpus cumulé.

| Campagne | FLAG déclenchés | Sorties problématiques confirmées | Précision observée |
|---|---:|---:|---:|
| Cartographie v1 — 2026-04-26 | 437 | 331 | 75,7 % |
| Cohorte TruthfulQA v2 — 2026-05-17 | ≈ 394 | ≈ 301 | ≈ 76,4 % |
| **Total cumulé** | **≈ 831** | **≈ 632** | **≈ 76 %** |

### Lecture correcte de ces résultats

NeoMundi ne prétend pas détecter toutes les erreurs.

L’instrument privilégie aujourd’hui la précision du signal sur la couverture exhaustive :

> mieux vaut signaler moins, mais signaler utilement, que saturer les équipes avec des faux positifs.

Ces résultats constituent une première validation opérationnelle.

Ils doivent être lus avec leurs limites : dépendance au corpus, aux providers testés, aux seuils retenus et au protocole de confirmation humaine ou instrumentale.

La consolidation se poursuit à travers les campagnes d’observation, les audits méthodologiques et les pilotes terrain.

---

## Cas d’usage

| Usage | Ce que NeoMundi apporte | Mode naturel |
|---|---|---|
| **Agents autonomes** | Observer les dérives, déclencher une escalade, une relance ou un reroutage selon la politique retenue | OBS · GOV |
| **Conformité et audit** | Produire des traces horodatées, documenter les signaux et soutenir la supervision | OBS · GOV |
| **Fine-tuning et évaluation** | Comparer les écarts comportementaux entre modèles, prompts, datasets ou versions | OBS |
| **SLA et infrastructure IA** | Détecter certaines dégradations comportementales et documenter les incidents | OBS · GOV |
| **Workflows sensibles** | Renforcer la supervision lorsqu’une sortie erronée serait difficilement rattrapable | GOV |

NeoMundi ne remplace pas votre stack d’observabilité.

NeoMundi ajoute une couche complémentaire de mesure et de gouvernance comportementale.

---

## Intégration et confidentialité

NeoMundi est conçu pour s’intégrer progressivement à des applications LLM, agents, orchestrateurs ou systèmes métier.

### Principes d’intégration

- un appel API pour démarrer ;
- approche **BYOK** selon le mode et la configuration ;
- aucun stockage des prompts ni des réponses ;
- seuils configurables selon les politiques du client ;
- conservation de l’autorité de décision par l’opérateur ;
- exports et traces auditables selon le niveau d’intégration ;
- déploiement dédié ou environnement contrôlé selon les besoins.

### Souveraineté opérationnelle

NeoMundi utilise un **juge sémantique auto-hébergé** pour analyser certaines réponses générées par les IA.

Ce juge fonctionne sur une infrastructure maîtrisée par NeoMundi, sans dépendre d’un service externe pour cette fonction critique.

Cette architecture vise trois objectifs :

* **confidentialité** : limiter l’exposition des données sensibles ;
* **résilience** : réduire la dépendance à des services externes ;
* **souveraineté opérationnelle** : garder la maîtrise de l’analyse et du traitement.


---

## État du produit

NeoMundi évolue par étapes afin de distinguer clairement ce qui est démontrable aujourd’hui, ce qui est proposé dans le cadre des pilotes et ce qui relève de la trajectoire d’industrialisation.

| Statut | Signification |
|---|---|
| **Disponible maintenant** | Sandbox public, premières surfaces d’observation, démonstration des signaux et documentation méthodologique |
| **Pilote accompagné** | Intégration progressive, calibration, supervision, exports et politiques adaptées au contexte client |
| **Trajectoire produit** | Extension des métriques, orchestration runtime avancée, déploiements dédiés et industrialisation des politiques de gouvernance |

Cette progression permet de commencer par l’observation, puis d’augmenter le niveau de contrôle lorsque le contexte métier le justifie.

---

## Du thermomètre au spectromètre

NeoMundi évolue d’un signal de stabilité vers une couche de mesure multidimensionnelle des comportements IA pendant leur exécution.

L’objectif n’est pas de multiplier les scores.

L’objectif est de construire une infrastructure capable de :

1. mesurer ;
2. interpréter ;
3. transmettre ;
4. décider selon une politique explicite ;
5. tracer ce qui s’est produit.

Le cadre public NeoMundi documente progressivement les signaux, contrats et frontières méthodologiques nécessaires à cette infrastructure.

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

### NeoMundi couvre-t-il certaines exigences de l’EU AI Act ?

NeoMundi ne remplace pas une démarche complète de conformité.

L’instrument peut contribuer à certaines pratiques de gouvernance : journalisation, traçabilité, supervision, documentation, suivi de signaux et auditabilité.

La pertinence juridique dépend du système concerné, de son niveau de risque et du cadre d’utilisation.

---

## Ressources

- [Sandbox NeoMundi](https://controltower.neomundi.io/welcome)
- [Site NeoMundi](https://neomundi.io)
- [Executive Brief — FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_FR.pdf)
- [Cadre théorique (Loi E) — FR](https://doi.org/10.5281/zenodo.19385052)

---

## Contact

Vous opérez des systèmes IA en production, des agents autonomes ou des workflows sensibles ?

**Mesurez ce qui est récupérable. Contrôlez ce qui ne l’est pas.**

[contact@neomundi.io](mailto:contact@neomundi.io)
