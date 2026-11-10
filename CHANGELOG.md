# Changelog

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versions selon [SemVer](https://semver.org/lang/fr/).

## [1.3.0] - 2026-11-10

### Ajouté
- `SKILL.md` : section « Retours de terrain » (accents, cadratin, chaîne en trois temps, faits, affirmations de rang), avec dates.

## [1.2.0] - 2026-10-30

### Ajouté
- `references/voix-textes-courts.md` : méthode pour les textes courts qui
  doivent sonner comme une personne (exemples classés par provenance et
  choisis par pertinence moins redondance, consignes de forme chiffrées par
  le code, permission de question décidée par le code, fiche de faits avec
  preuves, linter commun avec seuils calibrés sur un corpus, chaîne
  rédacteur, linter, juge de ressemblance, banc à l'aveugle avec deux juges
  et un banc pour la personne).
- `SKILL.md` : section « Textes courts qui doivent sonner comme une
  personne » qui renvoie à cette référence.

### Modifié
- Versions mises à jour dans `SKILL.md`, `README.md`, `CONTRIBUTING.md`,
  `docs/INSTALLATION.md`, `evals/evals.json`.
- `docs/ARCHITECTURE.md`, `docs/LIMITATIONS.md`, `docs/USAGE.md`,
  `README.md` : référence, limites de la méthode (genre posts contre
  réponses, corpus pas entièrement écrit à la main, n = 30).

### Cause
- Les réponses brèves produites avec un prompt chargé d'interdictions
  restaient reconnaissables (questions parachutées, amorces, reformulation
  du message). Les interdictions n'étaient pas appliquées, seulement
  demandées : elles deviennent un contrôle qui rejette.

## [1.1.0] - 2026-09-29

### Ajouté
- `evals/` : 6 cas d'évaluation fictifs (`evals.json`, fixtures,
  `README.md`) et `tests/test_evals.py` (7 tests).
- Front-matter portable de `SKILL.md` : `license`, `compatibility`,
  `metadata` (auteur, version, dépôt), `allowed-tools`.

### Modifié
- Publication : toute référence à des projets ou à une infrastructure
  privés est retirée de la documentation (exemples et sources neutres).
  L'historique git antérieur n'est pas réécrit.
- `LICENSE` : nom complet du titulaire du droit d'auteur.

## [1.0.2] - 2026-09-28

### Modifié
- `references/humanisation.md` : les formes de coquille sont au nombre de trois
  (accent oublié, lettres inversées, consonne double simplifiée), sur des mots courants de six lettres ou
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
