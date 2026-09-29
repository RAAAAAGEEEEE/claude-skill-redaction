# Typographie et style du français

Revu le 2026-09-28. Références (toutes ESTABLISHED en tant qu'ouvrages ou
services de référence ; elles divergent parfois entre la France et le
Québec, et la divergence est signalée) :

- *Lexique des règles typographiques en usage à l'Imprimerie nationale*,
  Imprimerie nationale (référence de la typographie française) ;
- Office québécois de la langue française, Banque de dépannage
  linguistique, [espacement avant et après les signes](https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles)
  (consulté le 2026-09-28) ;
- Bureau de la traduction du Canada, *Le guide du rédacteur*,
  [tableau des espacements](https://www.btb.termiumplus.gc.ca/redac-chap?lang=fra&lettr=chapsect6&info0=6.13)
  (consulté le 2026-09-28) ;
- Académie française, rubrique « Dire, ne pas dire » et page sur
  l'accentuation des majuscules.

Règle d'or : **un support, une convention**. Si le site ou le client a
déjà une convention (apostrophe droite, heure `9h30`), la suivre
partout plutôt que mélanger.

## Ponctuation et espaces

| Signe | Avant | Après |
|---|---|---|
| `.` `,` `…` | rien | espace |
| `:` | espace insécable (U+00A0) | espace |
| `;` `!` `?` | espace fine insécable (U+202F), ou insécable ordinaire | espace |
| `«` | espace | espace insécable |
| `»` | espace insécable | espace ou ponctuation |
| `(` `[` | espace | rien |
| `)` `]` | rien | espace ou ponctuation |
| `%` et unités | espace insécable (`15 %`, `20 kg`) | espace |

- En France, une espace précède toujours `: ; ! ?`. L'OQLF admet de ne
  rien mettre avant `; ! ?` (usage québécois) : ne l'appliquer que pour un
  public québécois.
- Quand le canal ne transporte pas les insécables (champ JSON d'un
  pipeline, SMS, certains outils d'e-mailing), une espace ordinaire est
  acceptée. **Jamais d'absence
  d'espace** (`Attention:` est faux).
- Points de suspension : un seul caractère `…`, trois points au plus,
  jamais « etc. … ».
- Point d'exclamation : un seul, rarement ; jamais `!!` ni `?!` en
  série.

## Guillemets et apostrophes

- Guillemets français « » avec espaces insécables à l'intérieur. Second
  niveau (citation dans la citation) : “ ”.
- Jamais de "guillemets droits" ni de “guillemets anglais” au premier
  niveau d'un texte français.
- La ponctuation finale se place à l'intérieur des guillemets si la
  citation est une phrase complète introduite par deux-points, à
  l'extérieur sinon.
- Apostrophe : typographique (’) ou droite ('), une seule forme par
  support. Les deux sont correctes à l'écran ; le mélange ne l'est pas.

## Tirets

- **Cadratin (—)** : interdit par règle dure du skill (c'est la marque
  typographique la plus reconnaissable d'un texte de modèle). Seule exception : une
  citation verbatim (avis client, extrait de presse).
- **Demi-cadratin (–)** : plage de valeurs sans espaces (`2024–2026`,
  `lun.–ven.`). En phrase courante, préférer « de 9 h à 12 h ».
- **Trait d'union (-)** : mots composés, inversions (« peut-on »), coupures.
  Jamais comme tiret de ponctuation, espacé ou doublé.
- Dialogue : tiret de dialogue seulement en fiction.

## Majuscules

- Titres, intertitres, boutons : majuscule au premier mot et aux noms
  propres seulement (« Délais et garanties », pas « Délais Et
  Garanties »).
- Accentuer les majuscules : État, À partir de, ÉCOLE (recommandation de
  l'Académie française et de l'Imprimerie nationale).
- Minuscule pour les jours, les mois, les langues, les adjectifs de
  nationalité (« le marché français », « les Français »).
- Sigles sans points (SNCF, TVA) ; acronymes prononcés comme un mot
  parfois en bas de casse (Unesco), selon l'usage établi.

## Nombres, dates, unités

- Séparateur de milliers : espace insécable (`12 500`) ; virgule
  décimale (`2,5`). Pas de séparateur dans les années (`2026`) ni les
  codes postaux.
- Monnaie après le nombre, espacée : `12 €`, `1 200 €`.
- Heures : `9 h 30` (Imprimerie nationale) ou `9h30` (usage courant),
  une forme par support ; `12:30` seulement dans une interface ou un
  horaire technique.
- Dates : `28 septembre 2026`, `1er octobre` ; pas de zéro initial en
  prose (`3 mars`, pas `03 mars`).
- Ordinaux : `1er`, `1re`, `2e`, `XXIe siècle` ; jamais `2ème`, `2nd`,
  `1ère`.
- En prose, écrire en lettres les petits nombres isolés (« trois
  raisons ») ; en chiffres les mesures, prix, pourcentages, statistiques
  et tout ce qui se compare.
- Un chiffre du texte doit être celui de la source : même valeur, même
  unité, même arrondi. Pas de conversion silencieuse.

## Abréviations

`M.` (pas `Mr`), `Mme`, `Mmes`, `Dr`, `n°`, `p.`, `etc.` (jamais suivi de
points de suspension), `c.-à-d.`, `p. ex.`. Première occurrence d'un sigle
peu connu : le développer.

## Orthographe et grammaire à surveiller

- Rectifications de 1990 : admises ; choisir une graphie par texte
  (« événement » ou « évènement »).
- Pièges fréquents : quel que soit / quelle que soit ; pallier un
  manque (pas « à ») ; se rappeler quelque chose (pas « de ») ; malgré
  que (à éviter) ; au jour d'aujourd'hui ; accord du participe passé
  avec « avoir » ; « leur » invariable devant un verbe ; « tout » adverbe
  devant un adjectif féminin à consonne (« toute petite »).
- Calques : voir [anti-ia.md](anti-ia.md), G6.

## Écriture inclusive

Suivre la charte du support ou du client. Par défaut : formulations
épicènes (« la clientèle », « les personnes inscrites ») et doublets
complets au besoin (« les artisans et artisanes ») ; pas de point médian
sauf demande.

## Listes

Deux formes, une par liste :

- phrases complètes : majuscule initiale et point final à chaque
  élément ;
- fragments introduits par deux-points : minuscule initiale,
  point-virgule entre les éléments, point final au dernier.

Une liste sert une vraie énumération, jamais un paragraphe découpé.

## Style

- **Une idée par phrase**, une idée par paragraphe. Paragraphes de deux à
  cinq phrases sur le web.
- **Varier la longueur** : une phrase courte après deux longues. Un texte
  où toutes les phrases font la même longueur se lit comme une notice.
- **Verbe concret, nom concret** : « pèse 55 kg » plutôt que « affiche un
  poids contenu ». Un verbe précis vaut mieux qu'un adjectif.
- **Actif** quand l'acteur compte ; le passif reste correct quand l'acteur
  est inconnu ou sans intérêt.
- **Attribuer** directement : « selon le fabricant », « d'après la fiche
  publiée par X », « X annonce ». Jamais « certains estiment ».
- **Dire le manque** : « le fabricant ne communique pas l'autonomie » est
  une information.
- **Registre** : vouvoiement par défaut pour un client ou un inconnu ;
  tutoiement si la marque ou l'échantillon le fait. Une fois choisi, ne plus en changer.
- **Jargon** : l'expliquer à la première occurrence, ou employer le mot du
  lecteur.
- **Accents** : un brief écrit sans accents ne s'imite pas. Le
  vérificateur signale un texte désaccentué.
