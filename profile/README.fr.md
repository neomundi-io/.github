# Neomundi - Contrôle de Stabilité et gouvernance IA en Temps Réel
# Fini l'audit rétrospectif. Nous mesurons votre IA pendant qu'elle génère.

🇬🇧 [Read in English](https://github.com/neomundi-io/.github/blob/main/profile/README.md)

---

Votre IA n'est pas auditable. Maintenant, elle l'est en 10 minutes.

✅ **Chaque réponse est mesurée en temps réel.**

⚠️ **Vous voyez la dérive avant qu'elle devienne un incident.**

🛑 **Vous pouvez bloquer les réponses instables avant envoi.**

📄 **Vous avez une preuve : export PDF de tous vos logs.**



**Pas un firewall. Pas un garde-fou. Une couche de décision en temps réel.**

**Un seul appel API. Aucun changement d'infrastructure.**

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

Ces signaux ne cherchent pas la vérité. Ils mesurent la cohérence — en temps réel. La dérive est visible avant qu'elle ne devienne une erreur.

---

## Résultats & Validation

2 360 réponses analysées · 6 datasets publics (TruthfulQA, HaluEval, MMLU, LegalBench)

- 91% de vrais positifs
- Corrélation forte entre baisse de stabilité et hallucination
- Zéro sur-détection sur les cas limites

*Graphe et dataset complets — à venir.*

---

## Intégration

Opérationnel en 10 minutes. Sans toucher à votre infrastructure.

**Bring your key** — vous utilisez votre propre clé API provider : OpenAI · Anthropic · Google · Mistral · DeepSeek · xAI · Cohere. Elle transite dans votre requête et reste sous votre contrôle.

**Un seul point de redirection** — vous redirigez vos appels LLM via `api.neomundi.io`. Aucun SDK à installer, aucun changement de code, aucune migration.

**Sécurité** — Neomundi ne connaît pas vos clés provider. Vos prompts ne sont pas lus ni stockés. Seules les métriques de gouvernance sont enregistrées : score, décision, horodatage.

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

Réponse : score de stabilité en temps réel · décision ALLOW / FLAG / BLOCK · export PDF sur demande.

---

## Programme pilote

Nous sélectionnons des partenaires early adopters dans les secteurs où la fiabilité des LLMs n'est pas une option : LegalTech · secteurs réglementés · éditeurs multi-LLM.

En échange de la documentation de votre cas d'usage : **conditions préférentielles à vie pour les premiers partenaires.**

→ [contact@neomundi.io](mailto:contact@neomundi.io)

---

## FAQ

**C'est quoi le score de stabilité ?**
Il mesure la cohérence interne d'une réponse LLM en temps réel — pas sa véracité. Neomundi ne fait pas de fact-checking. Il détecte la dérive qui précède l'erreur.

**Vous stockez quoi sur mes données ?**
Vos prompts ne sont pas lus ni stockés. Votre clé API provider reste sous votre contrôle. Seules les métriques de gouvernance sont enregistrées : score, décision, horodatage. Rien d'autre.

**Ça marche avec mon LLM ?**
Oui — détection automatique depuis votre clé : OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. Si votre provider n'est pas listé, contactez-nous.

**Quelle différence avec LangSmith, Portkey ou Helicone ?**
Ces outils observent et logguent. Neomundi mesure et intervient pendant la génération — avant que la réponse instable atteigne votre utilisateur. Nous ne remplaçons pas votre stack d'observabilité, nous ajoutons la couche de gouvernance qui manque.

**C'est conforme EU AI Act ?**
Neomundi contribue aux exigences de traçabilité et d'auditabilité de l'EU AI Act en livrant une piste d'audit complète par session : score, décision, horodatage, export PDF. L'échéance d'application est août 2026.

**C'est quoi le mode GOV ?**
Le mode OBS score et trace chaque réponse sans intervenir. GOV est le mode d'exécution : les réponses instables sont bloquées avant diffusion. Les pilotes y ont accès en priorité.

---

## Roadmap — 30 jours

- Mode GOV complet — blocage des réponses instables avant envoi
- Détection étendue — dérive, erreur, rupture en temps réel
- Interface plateforme — logs, seuils configurables, export complet

*Les pilotes en cours ont accès en priorité.*

---

## Documentation

- Executive Brief — *[lien à venir]*
- Technical White Paper — *[lien à venir]*
- Fondation scientifique (Zenodo) — *[lien à venir]*

---

*La stabilité n'est plus supposée. Elle est mesurée.*
