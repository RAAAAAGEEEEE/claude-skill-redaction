# Changelog

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versions selon [SemVer](https://semver.org/lang/fr/).

## [1.0.2] - 2026-09-28

### Modifié
- `references/humanisation.md` : les formes de coquille sont celles du
  module de coquilles d'un site d'actualité (accent oublié, lettres inversées,
  consonne double simplifiée), sur des mots courants de six lettres ou
  plus ; l'accent oublié n'est plus exclu. Le vérificateur le signale en
  P1, ce qui est attendu puisque la coquille est listée.

## [1.0.1] - 2026-09-28

### Modifié
- `references/anti-ia.md`, G3 : une question-titre sur une page de vente
  est permise quand `copywriting` la propose (une seule, pas une série),
  pour lever la contradiction entre les deux skills.

## [1.0.0] - 2026-09-28

Première version.

### Ajouté
- `SKILL.md` : procédure brief, matériau, brouillon, relecture séparée,
  version finale ; six règles dures (rien d'inventé, pas de cadratin,
  relecture séparée, français accentué, rien ne part, humaniser n'est pas
  dissimuler) ; articulation avec `copywriting`, `redaction-tweets-viraux`,
  `three-pass-writing`, `seo-geo-optimizer` et `SEO`.
- `references/anti-ia.md` : les 26 motifs de blader/humanizer v3.1.0
  adaptés au français, plus six tics propres au français (section G).
- `references/typographie-style.md` : espaces, guillemets, tirets,
  majuscules, nombres, abréviations, listes, style.
- `references/formats.md` : article, page, e-mail, post, documentation,
  fiche Google, description produit ; attentes de Google sourcées.
- `references/relecture.md` : grille P0/P1/P2 et prompt du relecteur.
- `references/humanisation.md` : mode humanisé et règle des coquilles.
- `references/etat-de-l-art.md` : registre daté (2026-09-28) sur la
  détection des textes d'IA, 9 lignes ESTABLISHED, 9 SUPPORTED,
  5 CLAIMED.
- `scripts/verifier.py` : contrôle mécanique hors ligne ; 21 tests.
- Documentation selon le standard GitHub du mainteneur ; notice MIT de
  blader/humanizer dans `THIRD_PARTY_NOTICES.md`.
