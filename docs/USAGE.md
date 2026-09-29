# Utilisation

## Dans Claude Code

Le skill se charge seul pour une demande de rédaction en français. On peut
aussi le nommer : « avec le skill redaction, … ».

| Demande | Ce que fait Claude |
|---|---|
| « Rédige un article de 1 000 mots sur … » | Brief (2 questions au plus), matériau sourcé, brouillon, vérificateur, relecture par un sous-agent Opus, version finale |
| « Réécris ce texte, il fait trop IA » | Réécriture avec les motifs de `references/anti-ia.md`, sans ajouter ni retirer de fait |
| « Relis ce mail » | Constats P0/P1/P2 cités, verdict ; pas de réécriture sauf demande |
| « Version humanisée de cet article » | Réécriture puis une ou deux coquilles (article de 800 mots ou plus), listées en sortie |
| « Écris la page d'accueil » | Structure par le skill `copywriting` si c'est une page de vente ; langue, faits et relecture par `redaction` |

### Ce que vous recevez

1. Le texte final dans un bloc à copier.
2. Au plus cinq lignes : corrections de la relecture, points
   `[[à confirmer : …]]` restants, coquilles insérées en mode humanisé.

### Demandes qui ne le chargent pas (voulu)

- Réponse de Claude dans la conversation, message de commit, commentaire
  de code.
- Texte en anglais : utiliser [blader/humanizer](https://github.com/blader/humanizer).
- Tweet ou fil X : `redaction-tweets-viraux` mène, `redaction` peut être
  chargé en complément pour la langue.

## Rejouer les cas d'évaluation

Les 6 cas de `evals/evals.json` se rejouent dans une session Claude Code :
copier le champ `prompt` (et le fichier `input_file` s'il y en a un), puis
comparer la sortie à `expected_output` et aux `assertions`. Mode d'emploi :
[../evals/README.md](../evals/README.md).

## Le vérificateur en ligne de commande

```bash
python scripts/verifier.py texte.md
python scripts/verifier.py texte.md --json
python scripts/verifier.py - < texte.txt
```

Chaque constat donne la priorité, la règle, la ligne, un extrait et la
correction attendue :

- **P0** : bloquant (cadratin, résidu de chatbot, placeholder, texte
  désaccentué) ; code de sortie 1.
- **P1** : à corriger avant publication (formules d'IA, espace manquante
  avant `: ; ! ?`, point à confirmer).
- **P2** : à examiner (vocabulaire gonflé, guillemets, ordinaux, rythme).

Le vérificateur ignore les blocs de code, le code en ligne et les URLs.

## Dans un pipeline

Le code de sortie permet de bloquer une publication :

```bash
python scripts/verifier.py article.md || echo "P0 trouvé, publication bloquée"
```

Voir aussi : [CONFIGURATION.md](CONFIGURATION.md), [LIMITATIONS.md](LIMITATIONS.md).
