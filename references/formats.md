# Formats : ce qu'attendent les lecteurs et Google

Revu le 2026-09-28. Étiquettes : voir [etat-de-l-art.md](etat-de-l-art.md).
Ce fichier dit **comment écrire** un format. **Quoi publier** (quel format
pour quelle intention, avec quelle preuve) relève de `seo-geo-optimizer`,
fichier `references/content-formats.md`.

## Ce qui vaut pour tous les formats

Google (ESTABLISHED, [helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content),
maj 2025-12-10 ; [contenu IA](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content),
maj 2025-12-10) :

- le contenu apporte une information, une analyse ou une expérience
  originale, pas un résumé de ce qui existe ;
- les sources sont claires, l'auteur identifiable, la méthode de
  production explicable (« Who, How, Why ») ; une mention d'automatisation
  est utile là où un lecteur se demanderait « comment ce texte a-t-il été
  fait ? » ;
- aucun nombre de mots préféré ; ne pas changer la date d'une page sans
  changement réel ;
- le contenu produit avec l'IA est admis s'il apporte de la valeur ; en
  produire en masse sans valeur relève du *scaled content abuse*.

Consignes des évaluateurs de Google, version du 2025-09-11 (ESTABLISHED,
[PDF](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf)) :
note la plus basse pour un contenu principal copié, paraphrasé ou généré
avec peu d'effort, d'originalité et de valeur ajoutée ; l'usage de l'IA
seul ne détermine pas la note.

Conséquence pour ce skill : **la valeur vient du matériau** (fait vérifié,
expérience, donnée, exemple précis) apporté par l'utilisateur ou la recherche.
Sans matériau, dire qu'il manque plutôt que délayer.

## Article, billet, guide

**Lecteur** : cherche une réponse ou une information précise, lit le
début, survole le reste.

- **Titre** informatif : il dit ce qui se passe ou ce qu'on apprend. Pas
  de question, pas de jeu de mots forcé, pas de deux-points
  systématique.
- **Chapô** d'une ou deux phrases : ce que le lecteur apprend. Aucun
  chiffre qui ne soit repris et sourcé dans le corps.
- **Ouvrir sur le fait le plus utile** (pyramide inversée), pas sur un
  contexte général.
- **Intertitres** qui nomment le contenu de la section, seulement si le
  texte est assez long pour en avoir besoin.
- **Sources** nommées et liées dans le texte ; distinguer annonce,
  démonstration et test indépendant.
- **Dates** de publication et de mise à jour visibles, identiques au
  balisage (ESTABLISHED, Google, [dates](https://developers.google.com/search/docs/appearance/publication-dates)).
- **Auteur** : signature et page auteur si le site en a.
- **Fin** : sur un fait, une limite, ou l'étape suivante pour le lecteur ;
  jamais un résumé ni une morale.
- **Test, comparatif, classement** : critères du *reviews system* de Google
  (expérience propre, mesures, avantages et inconvénients tirés de sa
  propre recherche, ce qui distingue le produit). Sans test réel, on
  n'écrit pas un test. Détail : `seo-geo-optimizer`.

## Page de site, landing

**Lecteur** : décide en quelques secondes si la page le concerne.

- Structure de conversion : skill `copywriting` (hero, preuve, objections,
  appel à l'action). Ce skill y ajoute la langue, les faits et la
  relecture.
- **Une promesse** par page, dans les mots du client.
- **Preuve réelle** : chiffre sourcé, client nommé avec accord, avis
  existant cité mot pour mot. Jamais de témoignage, de note ou de logo
  inventé (règle dure 1).
- **Un seul appel à l'action**, concret : ce qu'on fait et ce qui se
  passe ensuite.
- **Textes d'interface** (boutons, libellés, messages d'erreur) : exacts,
  courts, cohérents d'une page à l'autre ; ne pas les « humaniser ».
- **Mentions légales, CGV, politique de confidentialité** : ne pas
  réécrire le fond ; signaler ce qui paraît faux.
- **Site d'un client ou d'un commerçant** : le texte porte le nom d'un
  tiers ; aucune affirmation sur son activité (ancienneté, gamme,
  diagnostic gratuit…) sans source. C'est là que les premiers jets
  inventent le plus volontiers.

## E-mail

**Prospection (B2B)** :

- Objet court et précis, sans faux « Re: » ni fausse familiarité.
- Première ligne : pourquoi cette personne, avec un fait vérifiable sur
  elle ou son entreprise. Si la personnalisation n'est pas réelle, ne pas
  la simuler.
- Une question ou une action, une seule, qui appelle une réponse.
- Cadre légal en France (ESTABLISHED, [CNIL](https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique),
  maj 2026-06-10) : sans consentement préalable si le message est en lien
  avec la fonction du destinataire ; expéditeur identifié ; moyen simple
  et gratuit de s'opposer dans chaque message.

**Client, support** : la réponse ou la décision d'abord ; puis ce que le
client doit faire ; pas de réexplication du problème qu'il a lui-même
décrit ([anti-ia.md](anti-ia.md), 26).

**Transactionnel** (confirmation, facture, rappel) : données exactes,
aucune fantaisie, aucune coquille, même en mode humanisé.

## Post (LinkedIn, Bluesky, Facebook, X)

- **X** : ton et structure de `redaction-tweets-viraux` (direct, frontal,
  question finale permise, trois mots-dièse au plus). Ce skill garde la
  main sur les faits, la langue et le cadratin.
- **LinkedIn** : première ligne qui porte le fait ou l'enjeu concret ;
  paragraphes courts mais pas une phrase par ligne en cascade (c'est le
  motif 2) ; pas de liste d'émojis ; un lien ou une action.
- Partout : pas de promesse chiffrée sans source, pas de « thread 🧵 »,
  deux ou trois mots-dièse au plus et hors des phrases.

## Documentation, README, note technique

**Lecteur** : veut faire une tâche et vérifier qu'il l'a bien faite.

- Commencer par ce que fait l'outil et pour qui, puis le démarrage.
- Impératif pour les étapes (« Installez », « Lancez »), une action par
  étape, le résultat attendu après chaque commande.
- Commandes copiables telles quelles et **réellement exécutées** ; chemins
  exacts ; versions et dates explicites (« au 2026-09-28 », jamais
  « actuellement »).
- Aucun ton marketing, aucune promesse chiffrée sans source.
- Dépôt GitHub de l'utilisateur : appliquer
  `~/.claude/standards/GITHUB_DOCUMENTATION_STANDARD.md`.

## Fiche Google (Business Profile), description produit

- **Fiche Google** : description centrée sur les services, les produits,
  l'histoire de l'établissement ; aucun lien, pas de promotion ni de prix ;
  les consignes refusent aussi les fautes d'orthographe (ESTABLISHED,
  [consignes Google](https://support.google.com/business/answer/3038177?hl=fr),
  consulté le 2026-09-28). Donc **jamais de coquille** sur une fiche. Le
  reste (API, validation) : `seo-geo-optimizer`,
  `references/google-business-profile.md`.
- **Description produit** : à partir des caractéristiques vérifiées ;
  jamais recopiée du fabricant (*thin affiliation*, spam policies de
  Google) ; au moins une information que la fiche du fabricant n'a pas
  (usage, comparaison, limite).

## Longueurs

Aucune longueur n'est récompensée en soi (Google, ESTABLISHED). Prendre
la longueur du brief ; sans consigne, la plus courte qui répond
complètement. Couper vaut mieux que compresser.
