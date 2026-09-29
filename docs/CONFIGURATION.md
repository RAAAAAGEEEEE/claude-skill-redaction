# Configuration

Le skill n'a ni variable d'environnement, ni clé, ni fichier de réglages.
Il n'y a donc pas de `.env.example`.

## Options du vérificateur

| Option | Effet |
|---|---|
| `fichier` | Chemin du texte en UTF-8, ou `-` pour l'entrée standard |
| `--json` | Sortie JSON : liste d'objets `priority`, `rule`, `line`, `excerpt`, `message` |

## Réglages internes (dans `scripts/verifier.py`)

À modifier dans le code, avec un test (voir [CONTRIBUTING.md](../CONTRIBUTING.md)) :

| Réglage | Valeur | Où |
|---|---|---|
| Seuil de texte désaccentué | moins de 0,5 % de lettres accentuées, sur 300 lettres au moins | `check_accents` |
| Rythme uniforme | coefficient de variation des longueurs de phrase inférieur à 0,25, sur 8 phrases au moins | `check_rhythm` |
| Gras décoratif | plus d'un passage en gras pour 100 mots, sur 150 mots au moins | `check_rhythm` |
| Listes de formules et de vocabulaire | `CHATBOT_RESIDUE`, `PLACEHOLDERS`, `STAGING`, `INFLATED` | en tête du fichier |

## Réglages du mode humanisé

Définis dans [references/humanisation.md](../references/humanisation.md) :

| Réglage | Valeur | Statut |
|---|---|---|
| Déclenchement | demande explicite « humanise », « version humaine », « moins IA » | option du skill, à la demande de l'utilisateur |
| Coquilles par article long | 1 ou 2 | option du skill, à la demande de l'utilisateur |
| Article long | 800 mots ou plus | convention du skill |
| Zones interdites | chiffres, noms propres, citations, titres, textes juridiques et d'interface, fiche Google, e-mail transactionnel… | règle du skill |

Pour changer une valeur, modifier ce fichier de référence et le
CHANGELOG dans le même commit.

Voir aussi : [USAGE.md](USAGE.md).
