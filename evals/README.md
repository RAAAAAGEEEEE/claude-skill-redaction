# Évaluations

`evals.json` décrit 6 cas fictifs : noms, commerces, dates et chiffres sont
inventés pour l'exercice. Chaque cas donne un `prompt`, la sortie attendue
en une phrase et des assertions.

| Champ | Sens |
|---|---|
| `should_trigger` | `false` : le skill ne doit pas s'appliquer (texte anglais) |
| `input_file` | Texte à joindre au prompt, dans `fixtures/` |
| `reference_output` | Exemple de bonne sortie ; le vérificateur ne doit rien y trouver de bloquant |
| `flawed_output` | Exemple de mauvaise sortie ; le vérificateur doit y déclencher les règles listées |
| `assertions[].kind` | `verifier` : contrôlé par `scripts/verifier.py` ; `humain` : jugé à la lecture |

## Ce qui est automatique

```bash
python -m unittest tests.test_evals
```

Ces tests vérifient que les cas sont bien formés, que les sorties de
référence passent le vérificateur et que les sorties fautives déclenchent
les règles attendues. Ils ne lancent pas Claude.

## Rejouer un cas à la main

1. Ouvrir une session Claude Code avec le skill installé.
2. Coller le `prompt` (joindre `input_file` s'il existe).
3. Sauvegarder la sortie dans un fichier et lancer
   `python scripts/verifier.py sortie.md`.
4. Cocher chaque assertion `humain` contre la sortie.

Un cas échoue si une seule assertion échoue. Aucun score n'est publié :
ces cas n'ont pas été rejoués en série sur plusieurs modèles.

Voir aussi : [../docs/USAGE.md](../docs/USAGE.md), [../CONTRIBUTING.md](../CONTRIBUTING.md).
