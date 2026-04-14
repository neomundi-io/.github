# Neomundi. Le thermomètre de l'IA.

🇬🇧 [Read in English](https://github.com/neomundi-io/.github/blob/main/profile/README.md)

### Validation en temps réel de la stabilité des décisions au moment où elles se produisent.
### Nous fournissons le signal.
### Vous décidez quoi en faire.

---

| 🟣 Agents | 🟢 Conformité | 🟡 Fine-tuning | 🔵 SLA / Infra |
|-----------|---------------|----------------|----------------|
| **Stopper. Relancer. Rerouteur.** | **Tracer & prouver.** | **Mesurer la dérive.** | **Prouver la continuité.** |
| Signal de stabilité en direct, injecté dans les boucles de décision des agents. | Piste d'audit horodatée. Chaque génération scorée, chaque dérive signalée. | Quantifier les écarts comportementaux entre versions de modèles. | Supervision comportementale au-delà de la latence. Qualité de génération, mesurée. |

### Chaque signal pilote directement les décisions.

- Le signal de stabilité est le fondement de la gouvernance IA.
- Due diligence · qualité des données de fine-tuning · audit de conformité · preuve de SLA.

> ### Le signal rend les décisions actionnables, en temps réel.

---

## Chaque décision IA devient mesurable, traçable et gouvernable.

Chaque génération produit :
- Score de stabilité (0 → 1)
- Décision (ALLOW / FLAG / BLOCK)
- Signal de dérive (horodaté)

Sorties avancées :

- Trace d'audit complète (exportable)  
- Métriques d'exécution (coût, stabilité, dérive)  
- Preuve cryptographique (hash)  
- Jeux de données structurés (analytique, fine-tuning, conformité)

> Signal réel. Scoring réel. Résultat réel.

---

## Voir en action

<p align="center">
  <img src="https://raw.githubusercontent.com/neomundi-io/.github/main/profile/stability_score.gif" alt="Neomundi Stability Score Demo" width="800">
</p>

[→ Essayer en direct : Sans installation. Sans clé API.](https://neomundi-io.github.io/neomundi-sandbox/)

[→ Exemple de rapport d'audit PDF](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Audit_Report_2026-04.pdf)

---

## Intégration en une ligne.
Remplacez votre appel LLM existant par Neomundi. Votre service continue de tourner exactement comme avant, chaque réponse est désormais scorée en temps réel.

python

### Avant
response = openai.chat.completions.create(...)

### Après
result = score_prompt(user_prompt)  # Neomundi appelle OpenAI pour vous

C'est tout.

---

## Neomundi détecte l'instabilité avant qu'elle ne devienne visible :

- Contradictions internes
- Perte de précision
- Dérive thématique
- Incohérence structurelle

> La dérive apparaît avant la défaillance. Nous la mesurons en temps réel.

Ces signaux ne cherchent pas la vérité. Ils mesurent la cohérence en temps réel. La dérive est visible avant de devenir une erreur.

---

## Validé sur des systèmes réels

7 888 exécutions · 15 jeux de données

- 95,7 % dans les seuils de gouvernance  
- 336 instabilités détectées avant livraison  
- Coût moyen : 0,003 € par exécution  

Une hallucination non détectée coûte plus de 0,003 €.

---

## Déploiement en quelques minutes

- Aucun changement d'infrastructure
- Aucune exposition de données
- Aucune dépendance au modèle
- Un seul appel API

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

---

## Programme Pilote

Premiers pilotes ouverts

Nous sélectionnons des partenaires pour lesquels la fiabilité de l'IA est critique.
- Juridique
- Conformité
- Systèmes multi-agents

Vous obtenez :
- Accès direct
- Conditions préférentielles
- Cas d'usage co-construit

→ [contact@neomundi.io](mailto:contact@neomundi.io)

---

## FAQ

**Qu'est-ce que le score de stabilité ?**
Il mesure la cohérence interne d'une réponse LLM en temps réel — pas sa véracité. Neomundi ne vérifie pas les faits. Il détecte la dérive qui précède l'erreur.

**Quelles données stockez-vous ?**
Vos prompts ne sont ni lus ni stockés. Votre clé API fournisseur reste sous votre contrôle. Seules les métriques de gouvernance sont enregistrées : score, décision, horodatage. Rien d'autre.

**Fonctionne-t-il avec mon LLM ?**
Oui — détection automatique depuis votre clé : OpenAI, Anthropic, Google, Mistral, DeepSeek, xAI, Cohere. Si votre fournisseur n'est pas listé, contactez-nous.

**Quelle est la différence avec LangSmith, Portkey ou Helicone ?**
Ces outils observent et journalisent. Neomundi mesure et intervient pendant la génération — avant que la réponse instable n'atteigne votre utilisateur. Nous ne remplaçons pas votre stack d'observabilité, nous y ajoutons la couche de gouvernance manquante.

**Est-ce conforme à l'EU AI Act ?**
Neomundi contribue aux exigences de traçabilité et d'auditabilité de l'EU AI Act en produisant une piste d'audit complète par session : score, décision, horodatage, export PDF. L'échéance d'application est août 2026.

---

## Roadmap : L'infrastructure est active. Elle s'industrialise.

Dans 60 jours
- Seuils configurables par client
- Interface opérateurs pilotes

Les opérateurs pilotes actuels sont prioritaires sur chaque mise à jour.

---

## Open Science · Reproductible · Auditable

Auditabilité intégrée dès la conception. Pas une boîte noire.

---

## Early Access

Le signal tourne. Les données s'accumulent.
Nombre de places limité pour les équipes qui opèrent de l'IA en production.

Vous obtenez :
- Accès direct au signal runtime
- Un cas d'usage co-construit sur votre système
- Des conditions préférentielles

Nous obtenons :
- Des données réelles
- Des contraintes réelles
- Une validation réelle

Nous sélectionnons. Nous ne recrutons pas.

---

## Documentation

- Executive Brief : [NeoMundi Executive Brief EN](https://github.com/neomundi-io/neomundi-sandbox/blob/main/docs/NeoMundi_Executive_Brief_FR.pdf)

---

### Mesurer le comportement de l'IA en temps réel.
#### Si vous opérez de l'IA en production, vous avez besoin d'un signal.
#### Agissez avant que l'instabilité n'atteigne vos utilisateurs.

contact@neomundi.io

À la vitesse de la génération. Construit pour durer.

