# Contribuer

Issues et pull requests bienvenues.

## Avant d'ouvrir une pull request

1. `python -m unittest discover -s tests` passe. À la version 1.1.0,
   28 tests hors ligne passent.
2. Toute règle ajoutée à `scripts/verifier.py` a un test dans `tests/`, et
   `tests/fixtures/propre.md` ne produit toujours aucun constat.
3. Toute affirmation ajoutée dans `references/` porte une source primaire
   datée et une étiquette ESTABLISHED, SUPPORTED ou CLAIMED
   ([references/etat-de-l-art.md](references/etat-de-l-art.md)). Une
   liste d'observations sans mesure est CLAIMED et ne devient pas une
   règle dure.
4. Un nouveau motif d'écriture IA donne : ce qu'il faut surveiller, le
   problème, un exemple avant/après en français, et s'il est *faible
   seul*.
5. La documentation change **dans le même commit** que le comportement :
   `SKILL.md` si la procédure change, `docs/` si l'usage change,
   `CHANGELOG.md` dans tous les cas.
6. Aucun tiret cadratin dans les fichiers du dépôt, sauf pour le citer
   comme caractère.
7. Aucune donnée personnelle réelle dans les fixtures, les exemples et
   les cas de `evals/` (noms et chiffres fictifs, dites-le).
8. Un changement de comportement du skill ajoute ou met à jour un cas de
   `evals/evals.json` ([evals/README.md](evals/README.md)).

## Suivre l'amont

Quand [blader/humanizer](https://github.com/blader/humanizer) publie une
nouvelle version, comparer son `SKILL.md` à la version citée en tête de
`references/anti-ia.md`, reporter les changements utiles et mettre à
jour la version citée.

## Style

- Documentation et messages en français ; code et noms de variables en
  anglais.
- Python 3.10+, bibliothèque standard uniquement.
- Toute commande documentée a été exécutée.
