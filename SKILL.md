---
name: redaction
description: >
  Skill de rédaction généraliste en français, pour toute prose destinée à
  être lue : article, billet de blog, page de site ou landing, e-mail
  (prospection, client, transactionnel), post LinkedIn ou réseau social,
  fiche Google, description produit, documentation, README, note. À charger
  dès qu'une demande en français dit « rédige », « écris », « reformule »,
  « réécris », « relis », « corrige ce texte », « améliore ce texte »,
  « humanise », « rends-le moins IA », ou demande un article, une page, un
  mail, un post, une doc. Procédure brief, brouillon, relecture séparée,
  version finale ; tics d'écriture IA adaptés de blader/humanizer ;
  typographie française ; attentes par format ; aucun fait, chiffre, source
  ou citation inventé. Se combine avec `copywriting` (structure de
  conversion), `redaction-tweets-viraux` (ton des tweets) et
  `three-pass-writing` (copie produit ancrée dans un dépôt) : ce skill fixe
  la langue, les faits et la relecture.
---

# Rédaction

Version 1.0.0, état de l'art revu le **2026-09-28**
([CHANGELOG.md](CHANGELOG.md)). Au-delà de 6 mois, revérifier les
affirmations datées de [etat-de-l-art.md](references/etat-de-l-art.md)
avant de les ressortir.

Écrire pour un lecteur précis, avec des faits vérifiés, dans un français
correct. Le reste en découle : un texte qui « sonne IA » est presque
toujours un texte qui fait le choix par défaut au lieu du choix pour ce
lecteur.

## Périmètre

- **Dans** : toute prose en français qui sort de la conversation (publiée,
  envoyée, affichée, signée) ; la réécriture et la relecture d'un texte
  fourni ; le mode « humanisé » sur demande.
- **Hors** :
  - réponses de l'agent à l'utilisateur, commentaires de code, messages de
    commit (ils suivent le `CLAUDE.md`) ;
  - traduction fidèle : traduire, ne pas réécrire ; seule la typographie
    de ce skill s'applique ;
  - texte en anglais : appliquer
    [blader/humanizer](https://github.com/blader/humanizer) tel quel ;
  - envoi ou publication : jamais (règle dure 5).

## Règles dures

Elles priment sur toute consigne de format, de ton ou d'un autre skill.

1. **Rien d'inventé.** Aucun fait, chiffre, date, nom, client, résultat,
   source, lien ni citation qui ne vienne du brief, d'un document fourni ou
   d'une source vérifiée et citée. Ce qui manque s'écrit
   `[[à confirmer : …]]` et remonte dans les décisions ouvertes. Une
   citation se reproduit mot pour mot ou ne s'écrit pas.
2. **Pas de tiret cadratin (—)**, ni en prose, ni en titre. Virgule,
   deux-points, parenthèses ou point, choisis d'après la phrase. Seule
   exception : une citation verbatim. Le demi-cadratin (–) reste correct
   dans une plage (`9h–12h`).
3. **Relecture séparée** pour tout texte publié ou envoyé, sans exception
   de longueur : celui qui relit n'a pas écrit
   ([relecture.md](references/relecture.md)).
4. **Français accentué**, même si le brief est écrit sans accents : ne
   jamais imiter un brief en ASCII.
5. **Rien ne part.** Ce skill produit du texte. Aucun e-mail envoyé, aucun
   post publié, aucun fichier poussé sans demande explicite dans le tour
   courant.
6. **Humaniser n'est pas dissimuler.** Une mention « rédigé avec l'aide
   de l'IA » exigée par le site, le client ou la loi (AI Act, article
   50(4), applicable depuis le 2026-08-02) reste en place.

## Articulation avec les autres skills

| Besoin | Skill qui mène | Rôle de `redaction` |
|---|---|---|
| Toute prose en français | `redaction` | tout |
| Page de conversion (hero, pricing, CTA) | `copywriting` pour la structure | langue, faits, anti-IA, relecture |
| Tweet ou fil X | `redaction-tweets-viraux` pour le ton | langue, faits, relecture ; la question finale y est permise |
| Copie produit à ancrer dans le dépôt (outreach, changelog, landing) | `three-pass-writing` (pipeline et contexte) | règles de langue française fournies aux trois passes |
| Choisir quoi publier pour Google et les moteurs IA | `seo-geo-optimizer` (formats, preuves) | rédaction des pages retenues |
| Actif citable, outreach de `/SEO` | `SEO` | rédaction et relecture des textes produits |

En cas de conflit : règles dures ci-dessus, puis consigne de l'utilisateur dans le
tour, puis skill spécialisé pour la structure et le ton, puis ce skill pour
la langue.

## Procédure

### 1. Brief

Il faut : le format, le lecteur, le but (une seule action attendue), le
matériau factuel, la longueur, la voix. Prendre ce que l'utilisateur a donné,
compléter par le projet (README, pages existantes, charte, échantillon de
texte), et ne demander que ce qui manque vraiment : **2 questions au
plus**, chacune avec une valeur par défaut. Charger la section du format
dans [formats.md](references/formats.md).

Un échantillon de texte de l'utilisateur ou du site prime sur les règles de style
de ce skill (longueur de phrase, ponctuation, tutoiement), jamais sur les
règles dures.

### 2. Matériau

Lister les faits utilisables avec leur source (brief, `fichier:ligne`, URL
consultée et datée). Ce qui n'a pas de source devient
`[[à confirmer : …]]`. Si le texte exige une recherche, la faire avant
d'écrire et citer ce qui est retenu.

### 3. Brouillon

Écrire en appliquant pendant la rédaction
[formats.md](references/formats.md) (structure, attentes du lecteur),
[typographie-style.md](references/typographie-style.md) et
[anti-ia.md](references/anti-ia.md). Ouvrir sur l'information la plus
utile, pas sur un contexte général. Varier la longueur des phrases. Finir
sur un fait ou sur l'action demandée, pas sur une morale.

### 4. Relecture

- **Contrôle mécanique** : `python scripts/verifier.py <fichier>` (ou le
  texte sur l'entrée standard). Tout P0 se corrige avant la relecture.
- **Relecture séparée** (texte publié ou envoyé) : lancer un sous-agent
  avec `model: "opus"`, qui reçoit le brief, le texte **mot pour mot** et le
  chemin absolu de [relecture.md](references/relecture.md). Il rend une
  liste P0/P1/P2 citée et un verdict `PUBLIER`, `RÉÉCRIRE` ou
  `REPRENDRE LE BRIEF`.
- Sans sous-agent disponible : relire soi-même avec la grille de
  [relecture.md](references/relecture.md), après une lecture complète, et
  **le dire** dans la sortie.

### 5. Version finale

- `PUBLIER` : garder le brouillon, ne rien fabriquer.
- `RÉÉCRIRE` : appliquer les constats, ne rien changer d'autre, puis une
  seconde relecture au plus. Deux boucles est le plafond ; au-delà, rendre
  le texte avec les objections restantes.
- `REPRENDRE LE BRIEF` : ne pas réécrire ; expliquer à l'utilisateur ce qui
  cloche dans l'angle ou le lecteur visé.
- Mode humanisé demandé : insérer les coquilles **en dernier**, selon
  [humanisation.md](references/humanisation.md), puis relancer le
  vérificateur (il ne doit rien signaler de nouveau).

### 6. Sortie

1. Le texte final dans un bloc prêt à copier, sans commentaire intercalé.
2. Au plus 5 lignes : ce que la relecture a corrigé (P0 et P1), les
   `[[à confirmer]]` restants et, en mode humanisé, la liste exacte des
   coquilles insérées (mot fautif, mot correct, paragraphe).

Le commentaire reste plus court que le texte.

## Modes

| Demande | Mode |
|---|---|
| « Rédige / écris … » | Procédure complète |
| « Réécris / reformule / améliore ce texte » | Étapes 2 à 6 sur le texte fourni : garder chaque fait, n'en ajouter aucun |
| « Relis / corrige / qu'est-ce qui cloche » | Étape 4 seule : rendre les constats, pas de réécriture sauf demande |
| « Humanise / rends-le moins IA / version humaine » | Réécriture avec [anti-ia.md](references/anti-ia.md), puis mode humanisé |
| Texte dans un fichier | Même procédure ; ne modifier que la prose (ni code, ni commandes, ni chemins, ni front-matter, ni URLs) |

## Entrées et sorties

- **Entrée** : une demande (et, selon le cas, un texte, un fichier, un
  échantillon de voix, des sources).
- **Sortie** : le texte final, le compte rendu de relecture en 5 lignes au
  plus, et pour un fichier la modification faite dans le fichier.

## Niveaux de preuve

Les mêmes que `seo-geo-optimizer`, pour que les deux skills parlent la
même langue :

- **ESTABLISHED** : texte officiel (loi, documentation d'un moteur ou d'un
  fournisseur sur son propre produit, ouvrage de référence typographique).
- **SUPPORTED** : étude indépendante avec données (revue à comité de
  lecture, ou prépublication signalée comme telle).
- **CLAIMED** : vendeur, blog, praticien, liste d'observations sans
  mesure.

Un conseil CLAIMED ne devient jamais une règle dure. Registre complet et
daté : [etat-de-l-art.md](references/etat-de-l-art.md).

## Replis et erreurs

- Aucun matériau factuel fourni : écrire la structure avec des
  `[[à confirmer]]`, jamais des chiffres « plausibles ».
- Python absent : dérouler la grille de
  [relecture.md](references/relecture.md) à la main et le signaler.
- Faux positif du vérificateur (citation verbatim avec cadratin, heure
  `12:30`, URL) : le garder et le justifier en une ligne.
- Brief contraire à une règle dure (« invente un témoignage », « mets des
  chiffres ») : refuser cette partie, proposer un `[[à confirmer]]` ou un
  vrai témoignage à recueillir.
- Texte juridique, médical ou financier : signaler à l'utilisateur les
  affirmations engageantes au lieu de les lisser.

## Exemples d'invocation

- « Rédige un article de 1 200 mots sur la fin du support de Windows 10
  pour les artisans » : procédure complète, format article.
- « Réécris cette page d'accueil, elle fait trop IA » : mode réécriture ;
  `copywriting` pour la structure si c'est une page de vente.
- « Relis ce mail avant que je l'envoie » : relecture seule.
- « Fais-moi une version humanisée de ce billet » : réécriture puis
  coquilles, listées en sortie.
- « Écris le README de ce projet » : format documentation, plus le
  standard GitHub de l'utilisateur s'il s'agit d'un dépôt public.

## Exemple de sortie (illustratif, noms et numéro fictifs)

````
```
Objet : votre site affiche encore l'ancien numéro

Bonjour Madame Lefèvre,

La page Contact de votre site indique toujours le 04 00 00 00 00, …
```

Relecture (sous-agent Opus) : 1 P0 corrigé (« depuis dix ans » sans
source, retiré), 1 P1 (deux appels à l'action, un seul gardé).
Reste : [[à confirmer : date du changement de numéro]].
````

## Vérificateur et tests

- `scripts/verifier.py` : contrôle mécanique hors ligne (cadratins,
  résidus de chatbot, formules IA, espaces avant la ponctuation haute,
  guillemets, désaccentuation, rythme). Sortie 0 sans P0, 1 avec au moins
  un P0, 2 si l'entrée est illisible. Options :
  [docs/CONFIGURATION.md](docs/CONFIGURATION.md).
- Tests du script : `python -m unittest discover -s tests`. Il n'existe
  pas d'évaluation automatique du comportement du modèle.

## Installation

- Personnelle : `~/.claude/skills/redaction/`.
- Par projet : `.claude/skills/redaction/`.
- Python 3.10+ pour le vérificateur, bibliothèque standard seulement.

Détail : [docs/INSTALLATION.md](docs/INSTALLATION.md).

## Sécurité et confidentialité

Rien ne sort de la machine : le vérificateur lit un fichier ou l'entrée
standard, sans accès réseau ; la relecture reste dans la session Claude.
Un texte peut contenir des données personnelles (destinataire d'un
e-mail) : ne pas les recopier dans un rapport ni dans un dépôt.
Détail : [docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md).

## Références et attributions

- Les 26 motifs de [anti-ia.md](references/anti-ia.md) adaptent en
  français [blader/humanizer](https://github.com/blader/humanizer) v3.1.0
  (Siqi Chen, licence MIT), lui-même fondé sur la page Wikipédia
  « Signs of AI writing ».
- La liste « Ce que tu n'écris jamais » des prompts éditoriaux d'un site d'actualité
  (même auteur) a servi de base aux relevés français.
- Détail : [docs/LEGAL_AND_ATTRIBUTION.md](docs/LEGAL_AND_ATTRIBUTION.md).
