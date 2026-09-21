## 🌐 Choisissez votre langue

[**🇬🇧 English**](https://github.com/neomundi-io/.github/blob/main/profile/README.md) ·
[**🇫🇷 Français**](https://github.com/neomundi-io/.github/blob/main/profile/README.fr.md)

---

# NeoMundi

## Mesurez le comportement de l’IA à l’exécution. Transformez le signal en valeur opérationnelle.

NeoMundi transforme chaque exécution d’IA observée en un objet de mesure
structuré, horodaté, versionné et interopérable.

Ce même signal indépendant peut soutenir :

- **le pilotage opérationnel et la supervision** ;
- **l’observabilité et la détection de dérive** ;
- **l’audit et la traçabilité** ;
- **les éléments de preuve de conformité et la supervision humaine** ;
- **l’évaluation du risque et de l’assurabilité** ;
- **la comparaison de modèles, de prompts et de workflows** ;
- **les systèmes de gouvernance, d’orchestration et de contrôle externes** ;
- **la recherche et l’observation longitudinale**.

NeoMundi s’intègre aux produits et aux infrastructures déjà responsables de ces
fonctions. NeoMundi fournit le contexte de mesure ; le système consommateur
conserve ses règles, son interprétation et son autorité de décision.

**Intégrez une fois. Renforcez plusieurs usages en aval.**

> **Une primitive de mesure. Plusieurs applications. Plusieurs infrastructures.**
>
> **Votre système. Vos décisions. Notre signal de mesure.**

### Commencez ici

| Votre objectif | Point d’entrée |
|---|---|
| Créer un compte et une clé API | [Ouvrir la plateforme NeoMundi →](https://controlotower.neomundi.io/welcome) |
| Intégrer la mesure runtime | [Runtime Measurement Layer →](https://github.com/neomundi-io/neomundi-runtime-measurement) |
| Lancer des campagnes d’évaluation | [AI Periscope →](https://github.com/neomundi-io/neomundi-ai-periscope) |
| Comprendre la sémantique des signaux | [Metric Contract →](https://github.com/neomundi-io/neomundi-metric-contract) |
| Échanger des enregistrements de mesure | [Measurement Interoperability →](https://github.com/neomundi-io/neomundi-measurement-interoperability) |
| Examiner les preuves scientifiques | [Metrology Validation →](https://github.com/neomundi-io/neomundi-metrology-validation) |
| Explorer les pilotes et les usages opérationnels | [Cas d’usage NeoMundi →](https://github.com/neomundi-io/neomundi-use-cases) |
| Consulter la cartographie des capacités de conformité | [AI Act européen & RGPD →](https://github.com/neomundi-io/ai-act-rgpd) |
| Explorer les observations longitudinales | [Observatoire IA →](https://github.com/neomundi-io/neomundi-ai-observatory) |

---

## Architecture

~~~text
MESURER
Runtime Measurement Layer
        │
        ▼
DÉFINIR + VALIDER
Metric Contract · Metrology Validation
        │
        ▼
TRANSPORTER
Contrat d’interopérabilité versionné
        │
        ▼
APPLIQUER + OBSERVER
AI Periscope · Systèmes partenaires · Cas d’usage · Observatoire
~~~

**Mesure ≠ Interprétation ≠ Politique ≠ Exécution**

Cette séparation est le principe organisateur de l’écosystème NeoMundi.

---

## Couche produit

### Produit 01 — Runtime Measurement Layer

[**Documentation et Quickstart →**](https://github.com/neomundi-io/neomundi-runtime-measurement)

Le produit technique fondamental. Il mesure le comportement observable de l’IA
dans des conditions déclarées et produit des enregistrements structurés avec
une sémantique, une provenance, une traçabilité et des versions explicites.

### Produit 02 — AI Periscope

[**Dépôt du produit →**](https://github.com/neomundi-io/neomundi-ai-periscope)

Le produit de campagne et d’évaluation. Il organise les mesures runtime en
baselines, comparaisons, jeux de données, manifestes et rapports reproductibles
pour les modèles, les prompts, les configurations et les workflows métiers.

Les deux produits utilisent la même primitive de mesure.

---

## Couche de confiance

| Fonction | Source canonique | Rôle |
|---|---|---|
| Définir | [Metric Contract](https://github.com/neomundi-io/neomundi-metric-contract) | Signification, portée, limites et interprétation admissible des signaux |
| Valider | [Metrology Validation](https://github.com/neomundi-io/neomundi-metrology-validation) | Calibration, reproductibilité, contrôles, limites et qualification des affirmations |
| Transporter | [Measurement Interoperability](https://github.com/neomundi-io/neomundi-measurement-interoperability) | Échange JSON versionné, provenance, intégrité et limites du système consommateur |

[**Explorer le démonstrateur d’interopérabilité →**](https://interop.neomundi.org/)

L’interopérabilité publique expose l’interface de mesure. Elle n’exige pas la
publication des implémentations, formules ou mécanismes de décision propriétaires.

---

## Preuves et observation publique

### Métrologie et reproductibilité

[**Étude de reproductibilité du G-score →**](https://github.com/neomundi-io/G-score-reproducibility-study)

Une étude empirique exploratoire portant sur 33 600 observations, 12 modèles
d’IA, 7 campagnes et 4 prompts. Elle caractérise la reproductibilité
conditionnelle et les ruptures de régime observées dans les conditions documentées.

### Observatoire

[**Observatoire IA NeoMundi →**](https://github.com/neomundi-io/neomundi-ai-observatory)

L’Observatoire construit une mémoire longitudinale du comportement des systèmes
d’IA à partir d’observations répétées, horodatées et documentées.

[**Observatoire de recherche →**](https://neomundi.org/) ·
[**Météo des IA →**](https://weather.controltowerai.io)

> **L’Observatoire observe. Metrology Validation qualifie l’instrument.**

### Cas d’usage

[**Pilotes et intégrations documentés →**](https://github.com/neomundi-io/neomundi-use-cases)

Les cas d’usage montrent comment des infrastructures indépendantes peuvent
consommer le même signal de mesure pour l’audit, l’orchestration, la gouvernance,
l’assurance, le diagnostic ou la preuve, tout en conservant leurs propres
règles et leur autorité.

Un pilote documenté constitue une preuve d’articulation dans des conditions
déclarées, et non une certification universelle.

---

## Modèle de statut

NeoMundi distingue ce qui est disponible, spécialisé, expérimental et historique.

| Statut | Signification |
|---|---|
| **Disponible** | Produit, contrat, documentation ou surface d’observation publique active |
| **Spécialisé** | Métrique, étude, ressource de gouvernance ou composant de soutien plus ciblé |
| **Expérimental** | Recherche active qui ne constitue pas une capacité produit canonique |
| **Historique** | Matériau antérieur conservé pour la traçabilité, tandis que le contenu canonique est consolidé ailleurs |

Aucun signal expérimental, indice composite ou concept de recherche ne doit être
considéré comme un moteur de décision ou comme une preuve de vérité, de sécurité,
de conformité ou d’admissibilité.

---

## Carte de l’écosystème

### Disponibles et canoniques

- [Runtime Measurement Layer](https://github.com/neomundi-io/neomundi-runtime-measurement)
- [AI Periscope](https://github.com/neomundi-io/neomundi-ai-periscope)
- [Metric Contract](https://github.com/neomundi-io/neomundi-metric-contract)
- [Metrology Validation](https://github.com/neomundi-io/neomundi-metrology-validation)
- [Measurement Interoperability](https://github.com/neomundi-io/neomundi-measurement-interoperability)
- [Produits](https://github.com/neomundi-io/NeoMundi-Products)
- [Cas d’usage](https://github.com/neomundi-io/neomundi-use-cases)
- [Observatoire IA](https://github.com/neomundi-io/neomundi-ai-observatory)

### Preuves et métriques spécialisées

- [Étude de reproductibilité du G-score](https://github.com/neomundi-io/G-score-reproducibility-study)
- [Informational Metrics](https://github.com/neomundi-io/informational-metrics)
- [Energy Stability Index](https://github.com/neomundi-io/energy-stability-index)
- [Validity & Grounding](https://github.com/neomundi-io/validity-and-grounding)
- [Protection des données](https://github.com/neomundi-io/neomundi-io-data-protection)
- [Cartographie AI Act européen & RGPD](https://github.com/neomundi-io/ai-act-rgpd)

### Recherche expérimentale

- [Signal Adaptation Framework](https://github.com/neomundi-io/neomundi-signal-adaptation-framework)

Les travaux expérimentaux étendent le programme de recherche, mais ne
redéfinissent pas le contrat produit public tant qu’ils ne sont pas implémentés,
validés et versionnés.

### Références historiques et de consolidation

- [Runtime Telemetry Signals](https://github.com/neomundi-io/runtime-telemetry-signals)
- [Interpretation Contract](https://github.com/neomundi-io/interpretation-contract)
- [Boundary Tension Contract](https://github.com/neomundi-io/Boundary_Tension_contract)
- [Runtime Interoperability Contract](https://github.com/neomundi-io/runtime-interoperability-contract)
- [NeoMundi OBS](https://github.com/neomundi-io/neomundi-obs)
- [NeoMundi GOV](https://github.com/neomundi-io/neomundi-gov)

Pour la sémantique, l’intégration et l’interopérabilité actuelles, consultez les
dépôts canoniques présentés ci-dessus.

---

## Doctrine fondatrice

- Mesurer avant d’interpréter.
- Répéter avant de généraliser.
- Séparer l’observation de l’attribution causale.
- Ne jamais confondre stabilité et vérité.
- Ne jamais confondre signal et verdict.
- Séparer l’autorité de mesure de l’autorité de décision.

---

## Confidentialité et responsabilité

Les intégrations NeoMundi suivent une approche de minimisation des données et
sont conçues pour n’échanger que les éléments nécessaires à la mesure, à la
traçabilité et au mode d’intégration concerné.

L’organisation consommatrice reste responsable :

- de ses accès et clés fournisseur ;
- de ses seuils et politiques ;
- de son interprétation du signal ;
- de ses décisions et actions opérationnelles ;
- de ses obligations juridiques, réglementaires et sectorielles.

---

## Explorer NeoMundi

- [NeoMundi](https://neomundi.io/)
- [Produits](https://github.com/neomundi-io/NeoMundi-Products)
- [Observatoire de recherche](https://neomundi.org/)
- [Météo des IA](https://weather.controltowerai.io)
- [Executive Brief](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/Executive_brief_EN.pdf)
- [Cadre de référence](https://zenodo.org/records/21821522)
- [Guide d’intégration des fournisseurs](https://github.com/neomundi-io/controltowerai-docs/blob/main/providers.md)

---

## Contact

Vous concevez ou exploitez des systèmes d’IA en production ?

**Mesurez le comportement. Préservez le contexte. Construisez sur le signal.**

[contact@neomundi.io](mailto:contact@neomundi.io)
