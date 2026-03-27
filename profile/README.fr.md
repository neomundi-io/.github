# Neomundi — Contrôle de Stabilité IA en Temps Réel

> 🇬🇧 [Read in English](README.md)

---

## ⚡ Votre IA n'est pas fausse. Elle dérive.

Neomundi ne vérifie pas si votre IA a raison.
Il mesure si votre IA est stable.

Chaque réponse reçoit un score.
Quand la stabilité chute, vous le savez — avant que la réponse soit envoyée.

**G-score : 0 = stable · 1 = instable**

> [Tester en direct →](https://neomundi-io.github.io/neomundi-sandbox/)

---

## Ce qu'est la dérive

Neomundi détecte quatre signaux en temps réel :

- **Contradiction interne** — la réponse se contredit elle-même
- **Perte de précision** — la précision se dégrade en cours de réponse
- **Dérive du sujet** — la réponse s'éloigne du fil initial
- **Incohérence de ton** — le ton ou la logique devient inconsistant

Aucun de ces signaux n'exige de connaître la vérité.
Ils mesurent uniquement la cohérence.

---

## Pourquoi la dérive est importante

Dans nos tests (TruthfulQA), les signaux d'instabilité précèdent jusqu'à 79 % des réponses incorrectes.

Neomundi ne détecte pas la vérité.
Il détecte la dérive qui la précède.

---

## Ce que vous obtenez

**Mode OBS** — chaque réponse est scorée et tracée. Rien n'est bloqué.
Vous disposez d'une piste d'audit complète : chaque réponse, chaque score, chaque horodatage.

**Mode GOV** — quand la dérive dépasse votre seuil, la réponse est signalée ou peut être interrompue.
Avant qu'elle n'atteigne personne.

---

## L'argument audit

Une réponse instable envoyée, c'est votre responsabilité.
Une réponse instable interceptée, c'est la preuve que vous contrôlez.

Neomundi transforme chaque interaction IA en un enregistrement auditable.

---

## Un seul appel API. Aucun changement d'infrastructure.

```bash
curl -X POST https://api.neomundi.io/v1/observe \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"mode": "OBS", "session_id": "abc123"}'
```

---

## Statut

| Mode | Statut |
|---|---|
| OBS | 🟢 Live — onboarding pilotes ouvert |
| GOV | 🟡 À venir |

---

## Documentation

- [Executive Brief](#)
- [Technical White Paper](#)
- [Fondation scientifique (Zenodo)](#)

---

*La stabilité n'est plus supposée. Elle est mesurée.*
