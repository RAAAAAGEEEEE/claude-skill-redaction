# redaction

Skill Claude Code de rédaction généraliste en français : articles, pages,
e-mails, posts, documentation. Il fait écrire Claude pour un lecteur
précis, avec des faits vérifiés, dans un français typographiquement
correct, et sans les tics qui trahissent un texte de modèle.

## Le problème

Demandez un article à un modèle : vous obtenez un texte fluide qui ouvre
sur « Dans un monde où… », empile les « ce n'est pas X, c'est Y », glisse
un tiret cadratin par phrase, invente un « depuis plus de quinze ans » et
finit sur « En conclusion ». Chaque phrase se lit bien ; l'ensemble ne
dit rien à personne, et parfois dit faux.

## Pour qui

Les francophones qui font écrire Claude Code pour publier ou envoyer :
fondateurs solo, petites équipes, rédacteurs qui relisent des premiers
jets générés.

## Ce qu'il apporte

- Une procédure courte : brief, brouillon, **relecture par un autre
  modèle**, version finale.
- Les 26 motifs d'écriture IA de
  [blader/humanizer](https://github.com/blader/humanizer) adaptés au
  français, plus six tics propres au français.
- La typographie française (espaces, guillemets, nombres, majuscules) et
  les attentes par format, sourcées et datées.
- Une règle sans exception : aucun fait, chiffre, source ou citation
  inventé ; ce qui manque devient `[[à confirmer : …]]`.
- Un vérificateur hors ligne (`scripts/verifier.py`) qui refuse ce qu'une
  consigne ne suffit pas à empêcher : cadratins, résidus de chatbot,
  placeholders, texte désaccentué.
- Un état de l'art daté sur la détection des textes d'IA, chaque
  affirmation étiquetée ESTABLISHED, SUPPORTED ou CLAIMED.

## Statut

**Bêta, version 1.0.0** (2026-09-28). Le vérificateur est couvert par
21 tests hors ligne. Le comportement du skill dans Claude (choix du
skill, qualité des textes) n'a pas d'évaluation automatique. Voir
[docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Exemple de sortie du vérificateur

Sortie réelle sur le fichier de test `tests/fixtures/ia.md` (extrait) :

```
verifier.py 1.0.0 : P0=4 P1=8 P2=9
  P0 [cadratin] l.5 : …able partenaire de croissance — et ça change tout.
      Tiret cadratin interdit (sauf citation verbatim) : virgule, deux-points, parenthèses ou point.
  P0 [placeholder] l.7 : …notre engagement. Bienvenue à [Ville]!
      Placeholder oublié.
  P1 [formule-ia] l.5 : Ce n'est pas un simple site, c'est un véritable partenaire de cr…
      faux contraste « ce n'est pas X, c'est Y » (motif 1)
```

## Prérequis

- Claude Code (skills personnels dans `~/.claude/skills/`).
- Python 3.10 ou plus récent pour le vérificateur (bibliothèque standard
  seulement). Sans Python, le skill fonctionne ; seule la vérification
  mécanique manque.

## Démarrage

```bash
git clone https://github.com/RAAAAAGEEEEE/claude-skill-redaction ~/.claude/skills/redaction
```

Puis, dans Claude Code : « Rédige un article sur … ». Le skill se charge
seul pour toute demande de rédaction en français.

Vérifier l'installation :

```bash
cd ~/.claude/skills/redaction && python -m unittest discover -s tests
```

## Exemple minimal

```bash
python ~/.claude/skills/redaction/scripts/verifier.py mon-article.md
```

Code de sortie : 0 sans problème bloquant, 1 si un P0 est trouvé, 2 si le
fichier est illisible.

## Architecture

`SKILL.md` porte la procédure et les règles dures ; `references/` le
détail chargé à la demande (tics d'IA, typographie, formats, relecture,
mode humanisé, état de l'art) ; `scripts/verifier.py` le contrôle
mécanique. Détail : [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Configuration

Aucune variable d'environnement, aucune clé. Options du vérificateur et
réglages du mode humanisé : [docs/CONFIGURATION.md](docs/CONFIGURATION.md).

## Sécurité et confidentialité

Aucun accès réseau. Le vérificateur lit un fichier local ou l'entrée
standard. Détail : [docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md).

## Limites

- Les listes de tics français sont des observations (CLAIMED) : aucune
  étude indépendante ne les mesure en français au 2026-09-28.
- Le vérificateur repère des formes, pas le sens : il ne voit ni un fait
  inventé ni un triplet bien déguisé. La relecture reste indispensable.
- Retirer les tics ne rend pas un texte « indétectable », et ce n'est pas
  le but.

Liste complète : [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Feuille de route (non contractuelle)

- Évaluations de déclenchement (quelles demandes chargent le skill).
- Mesure des tics sur un corpus français, si une étude sérieuse paraît.

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT, voir [LICENSE](LICENSE). `references/anti-ia.md` adapte
blader/humanizer (MIT, Siqi Chen) : voir
[docs/LEGAL_AND_ATTRIBUTION.md](docs/LEGAL_AND_ATTRIBUTION.md).

## Documentation

- [SKILL.md](SKILL.md) : la procédure lue par Claude
- [docs/INSTALLATION.md](docs/INSTALLATION.md)
- [docs/USAGE.md](docs/USAGE.md)
- [docs/CONFIGURATION.md](docs/CONFIGURATION.md)
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
- [docs/LIMITATIONS.md](docs/LIMITATIONS.md)
- [docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md)
- [docs/LEGAL_AND_ATTRIBUTION.md](docs/LEGAL_AND_ATTRIBUTION.md)
- [CHANGELOG.md](CHANGELOG.md)
