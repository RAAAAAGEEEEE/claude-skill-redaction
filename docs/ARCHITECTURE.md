# Architecture

## Principe : divulgation progressive

Claude lit `SKILL.md` à chaque déclenchement : il reste court (procédure,
règles dures, articulation avec les autres skills). Les références ne sont
lues qu'à l'étape qui en a besoin.

```
redaction/
├── SKILL.md                    procédure, règles dures, modes
├── references/
│   ├── formats.md              étape 1 et 3 : attentes par format, Google
│   ├── anti-ia.md              étape 3 et 4 : 26 motifs + 6 tics français
│   ├── typographie-style.md    étape 3 et 4 : typographie et style
│   ├── relecture.md            étape 4 : grille et prompt du relecteur
│   ├── humanisation.md         étape 5 : mode humanisé et coquilles
│   └── etat-de-l-art.md        registre daté des preuves
├── scripts/verifier.py         contrôle mécanique, hors ligne
├── tests/                      tests du vérificateur et fixtures
└── docs/                       documentation humaine
```

## Déroulé

1. **Brief** : Claude complète la demande par le projet, pose au plus
   deux questions, charge le format.
2. **Matériau** : faits et sources ; le reste devient `[[à confirmer]]`.
3. **Brouillon** : écrit par la session courante.
4. **Relecture** : `verifier.py` d'abord (formes), puis un sous-agent
   `model: "opus"` qui n'a pas écrit le texte (fond). Il ne réécrit pas :
   il cite et rend un verdict.
5. **Version finale** : corrections appliquées une fois, seconde relecture
   au plus ; coquilles en dernier si le mode humanisé est demandé.

## Pourquoi un vérificateur en plus du prompt

Une consigne de prompt ne se vérifie pas toute seule : un modèle remet le
cadratin ou laisse un `[Ville]` malgré l'interdiction. Le vérificateur
transforme les règles dures en contrôle qui échoue (code de sortie 1).

## Liens avec d'autres skills

| Skill | Relation |
|---|---|
| `copywriting` | Structure des pages de conversion |
| `redaction-tweets-viraux` | Ton et structure des tweets |
| `three-pass-writing` | Pipeline de copie produit ancré dans le dépôt |
| `seo-geo-optimizer` | Choix des formats et des preuves à publier |
| `SEO` | Actifs citables et outreach |
| blader/humanizer | Source des motifs, version anglaise |

Voir aussi : [USAGE.md](USAGE.md), [LIMITATIONS.md](LIMITATIONS.md).
