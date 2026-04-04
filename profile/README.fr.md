# Neomundi rend le comportement de vos IA mesurable, gouvernable et prouvable en temps réel.

🇬🇧 [Read in English](https://github.com/neomundi-io/.github/blob/main/profile/README.md)

---

## Pas du monitoring. Pas des garde-fous.
Une couche de décision pendant la génération — pas après.

---

## Neomundi mesure la stabilité de chaque réponse à l'inférence, détecte les dérives avant l'envoi et peut déclencher une décision en temps réel.

---

## Chaque mesure génère une trace exploitable, apportant une preuve documentée de gouvernance, alignée avec les exigences de traçabilité et de diligence de l'EU AI Act.


---
## Voir en action

> Requête réelle. Score réel. Décision réelle.

<p align="center">
  <img src="https://raw.githubusercontent.com/neomundi-io/.github/main/profile/stability_score.gif" alt="Neomundi Stability Score Demo" width="800">
</p>

**Input** → scoré en temps réel

**Dérive détectée** → signalée avant envoi

**Décision** → ALLOW / FLAG / BLOCK

[→ Tester en direct — Aucune installation. Aucune clef requise.](https://neomundi-io.github.io/neomundi-sandbox/)
---

## Ce que Neomundi détecte

Neomundi détecte quand votre IA commence à dériver :

- Contradictions internes
- Perte de précision
- Sortie du sujet
- Incohérence globale

Ces signaux ne cherchent pas la vérité. Ils mesurent la cohérence en temps réel. La dérive est visible avant qu'elle ne devienne une erreur.

---

## Résultats & Validation

2 360 réponses analysées · 6 datasets publics (TruthfulQA, HaluEval, MMLU, LegalBench)

- 79,5% de détection des réponses instables avant livraison
- 91% de précision : moins de 9% de fausses alarmes
- Corrélation forte entre baisse de stabilité et hallucination
- Zéro sur-détection sur les cas limites

*Graphe et dataset complets à venir.*

---

## Ce que Neomundi est et n'est pas

|  | Firewall | Guardrail | Prompt engineering | **Neomundi** |
|--|--|--|--|--|
| Agit pendant la génération | ❌ | ❌ | ❌ | ✅ |
| Mesure la stabilité en temps réel | ❌ | ❌ | ❌ | ✅ |
| Produit une preuve auditable | ❌ | ❌ | ❌ | ✅ |
| Souverain : données sur votre stack | ⚠️ | ⚠️ | ✅ | ✅ |
| Sans changement d'infrastructure | ❌ | ⚠️ | ✅ | ✅ |

> Neomundi crée une nouvelle catégorie : la gouvernance IA en temps réel.

---

## Intégration

Opérationnel en 10 minutes. Sans toucher à votre infrastructure.

**Bring your key** : vous utilisez votre propre clé API provider : OpenAI · Anthropic · Google · Mistral · DeepSeek · xAI · Cohere. Elle transite dans votre requête et reste sous votre contrôle.

**Un seul point de redirection** : vous redirigez vos appels LLM via : api.neomundi.io. Aucun SDK à installer, aucun changement de code, aucune migration.

**Sécurité** : Neomundi ne connaît pas vos clés provider. Vos prompts ne sont pas lus ni stockés. Seules les métriques de gouvernance sont enregistrées : score, décision, horodatage.

```bash
curl -X POST https://api.neomundi.io/v1/govern/stream \
  -H "X-API-Key: ct_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Votre prompt ici",
    "model": "gpt-4o",
    "provider_api_key": "sk-xxx"
  }'
```

Réponse : score de stabilité en temps réel · décision ALLOW / FLAG / BLOCK · export PDF — *Real-time audit of AI behavior at runtime*

---

## Confidentialité & Privacy by Design

Neomundi ne lit pas vos prompts. Neomundi ne stocke pas vos réponses.

Seules les métriques de gouvernance sont enregistrées : score de stabilité, décision, horodatage, hash SHA-256 de la requête.

**Votre clé provider** (OpenAI, Anthropic, Mistral…) transite dans votre requête et reste sous votre contrôle. Elle n'est jamais persistée côté Neomundi.

**Ce qui est enregistré :** score · décision · régime · coût · horodatage  
**Ce qui n'est jamais enregistré :** prompt · réponse · clé provider · données personnelles

---

## Programme pilote

Nous sélectionnons des partenaires early adopters dans les secteurs où la fiabilité des LLMs n'est pas une option : LegalTech · secteurs réglementés · éditeurs multi-LLM.

En échange de la documentation de votre cas d'usage : **conditions préférentielles à vie pour les premiers partenaires.**

→ [contact@neomundi.io](mailto:contact@neomundi.io)

---

## FAQ

**C'est quoi le score de stabilité ?**
Il mesure la cohérence interne d'une réponse LLM en temps réel, pas sa véracité. Neomundi ne fait pas de fact-checking. Il détecte la dérive qui précède l'erreur.

**Vous stockez quoi sur mes données ?**
Vos prompts ne sont pas lus ni stockés. Votre clé API provider reste sous votre contrôle. Seules les métriques de gouvernance sont enregistrées : score, décision, horodatage. Rien d'autre.

**Ça marche avec mon LLM ?**
Oui — détection automatique depuis votre clé : OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. Si votre provider n'est pas listé, contactez-nous.

**Quelle différence avec LangSmith, Portkey ou Helicone ?**
Ces outils observent et logguent. Neomundi mesure et intervient pendant la génération avant que la réponse instable atteigne votre utilisateur. Nous ne remplaçons pas votre stack d'observabilité, nous ajoutons la couche de gouvernance qui manque.

**C'est conforme EU AI Act ?**
Neomundi contribue aux exigences de traçabilité et d'auditabilité de l'EU AI Act en livrant une piste d'audit complète par session : score, décision, horodatage, export PDF. L'échéance d'application est août 2026.

**C'est quoi le mode GOV ?**
Le mode OBS score et trace chaque réponse sans intervenir. GOV est le mode d'exécution : les réponses instables sont bloquées avant diffusion. Les pilotes y ont accès en priorité.

---

## Roadmap : 30 jours
- Mode GOV complet : moins de tokens pour une meilleure réponse. Le système sait quand s'arrêter, dès que l'information utile est délivrée
- Auto-reduce : régénération automatique déclenchée via webhook sur l'API client dès que le seuil de stabilité est atteint
- Détection étendue : dérive, erreur, rupture en temps réel
- Interface plateforme : logs, seuils configurables, export complet

*Les pilotes en cours ont accès en priorité.*

---

## Documentation

- Executive Brief : [NeoMundi Executive Brief FR](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Executive_Brief_FR.pdf)
- Technical White Paper : *[lien à venir]*
- Fondation scientifique (Zenodo) : [Thermodynamic Governance of AI Systems](https://doi.org/10.5281/zenodo.19385052)

---

*La stabilité n'est plus supposée. Elle est mesurée.*
