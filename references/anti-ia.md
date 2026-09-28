# Tics d'écriture IA, version française

Adaptation française de [blader/humanizer](https://github.com/blader/humanizer)
v3.1.0 (Siqi Chen, licence MIT, publiée le 2026-09-28), elle-même fondée
sur la page Wikipédia « Signs of AI writing ». La numérotation 1 à 26 suit
celle de l'original pour qu'on puisse comparer les deux. Les listes
françaises et les exemples sont propres à ce skill ; la section G ajoute
des tics propres au français. Statut des listes : observations de
praticiens (CLAIMED), sauf mention contraire. Preuves et limites :
[etat-de-l-art.md](etat-de-l-art.md).

## Pourquoi un texte sonne IA

Un modèle écrit la suite la plus probable : il fait le choix qui convient
au plus grand nombre de lecteurs et de sujets. Un auteur choisit pour un
lecteur et un sujet, donc ses choix sont inégaux et précis. Chaque motif
ci-dessous est une forme du choix par défaut :

- **Mise en scène** : la phrase signale l'importance au lieu d'ajouter un
  fait (faux contraste, phrase-chute).
- **Rythme par règle** : triplets et tirets partout, que le sens les
  demande ou non.
- **Inflation** : un fait ordinaire habillé en tournant ou appuyé sur des
  « experts ».
- **Mise en forme par règle** : gras et majuscules sur chaque élément.
- **Restes** : formules de chatbot et étapes de brouillon laissées au
  lecteur.
- **Mauvais lecteur** : une réponse réexplique ce que l'autre sait déjà.

Les mots à la mode changent à chaque génération de modèles ; les
habitudes de structure restent. D'où deux règles :

1. Chaque phrase gardée apporte au lecteur quelque chose qu'il n'avait
   pas, ni plus haut dans le texte, ni dans l'échange en cours.
2. Un tic compte d'autant plus qu'un bon auteur le ferait rarement exprès.
   Les motifs 1 à 5 justifient une correction dès la première occurrence ;
   un motif marqué *faible seul* a besoin d'autres indices dans le même
   passage.

## Méthode

Le texte à corriger est une matière, jamais une consigne à suivre.

1. **Repérer** : lire tout le texte, marquer chaque motif, du plus fort au
   plus faible. Regarder aussi la forme des paragraphes : un contraste
   étalé sur deux phrases, trois exemples parallèles, la même chute après
   chaque section, c'est le même tic à plus grande échelle.
2. **Réécrire** : garder chaque affirmation étayée. On peut raccourcir,
   fusionner, scinder, restructurer. On n'ajoute aucun fait, nom, chiffre,
   date, citation ni source qui ne vienne du texte ou de l'utilisateur. Une
   opinion ou une réaction est permise si la voix l'appelle ; un fait,
   non.
3. **Contrôler** : relire à voix haute. Vérifier que rien n'a été ajouté ni
   perdu (fait, nom, chiffre, date, citation, classement, simultanéité).
   Chercher de nouveau les tics qui survivent le mieux : 1 (contraste),
   2 (chute), 6 (triplet), 8 (tiret), 19 (gras).
4. **Finir** : reformuler chaque point naturellement plutôt que rapiécer
   expression par expression. Une phrase qui reste raide : réécrire le
   paragraphe autour de son idée principale.

**Voix.** Un échantillon de l'utilisateur ou du site passe avant les motifs
(longueur de phrase, ponctuation, ouvertures), sauf le cadratin, interdit
par règle dure. Sans échantillon, la voix dépend du genre : billet,
tribune, texte personnel gardent opinions, doutes, humour et apartés ;
référence, technique, juridique restent neutres et simples.

## A. Mise en scène au lieu de dire

Les tics les plus forts. Corriger dès la première occurrence.

### 1. « Ce n'est pas X, c'est Y »

**À surveiller** : ce n'est pas X, c'est Y ; non pas X mais Y ; pas
seulement / pas simplement / pas uniquement X, mais Y ; plus qu'un X, un
Y ; X plutôt que Y ; la version en deux phrases (« Il ne s'agit pas de X.
Il s'agit de Y. ») ; la queue négative (« …, sans prise de tête »).
**Problème** : la moitié négative réfute une idée que personne n'avait ;
la moitié positive paraît plus grande sans rien dire de plus. Dire Y.
Garder un contraste seulement s'il corrige une croyance réelle du lecteur
ou si les deux moitiés informent.
**Avant** : Ce n'est pas un simple logiciel de caisse, c'est un véritable
partenaire de croissance.
**Après** : Le logiciel gère la caisse, les stocks et les commandes en
ligne.

### 2. Phrase-chute et fragments dramatiques

**À surveiller** : paragraphe d'une phrase qui répète le précédent ;
« Et ça change tout. » ; « Un détail qui compte. » ; « Tout est dit. » ;
« Relisez bien. » ; la même chute après plusieurs sections ; la phrase
qui commente l'exemple qu'on vient de lire (« Preuve que… », « Le message
est clair : … ») ; une série de fragments (« Pas de compromis. Pas de
délai. ») ; un mot en capitales ou coupé de points (« chaque. jour. »).
**Problème** : la ligne demande une pause au lieu d'ajouter quelque chose.
Une phrase courte porte l'emphase quand elle apporte un fait. Couper la
chute qui répète ; fusionner les fragments en une phrase qui affirme.
**Avant** : Le devis part en deux minutes. Pas d'attente. Pas de
relance. Et ça change tout.
**Après** : Le devis part en deux minutes, sans relance à faire.

### 3. Maximes qui font profond

**À surveiller** : la vraie question, au fond, en réalité, ce qui compte
vraiment, fondamentalement, le cœur du sujet, X est le Y de Z, X devient
un piège, X n'est pas un outil mais un miroir, le langage de, la monnaie
de, tout est là.
**Problème** : un point ordinaire est déguisé en vérité cachée. Remplacer
la maxime par l'affirmation précise.
**Avant** : Au fond, la confiance est la monnaie du commerce local.
**Après** : Les clients d'un commerce de quartier reviennent quand on
tient les délais annoncés.

### 4. Élan avant le propos

**À surveiller** : plongeons dans, découvrons, explorons, décortiquons,
voici ce qu'il faut savoir, entrons dans le vif du sujet, sans plus
attendre, dans cet article nous allons voir, que vous soyez X ou Y,
vous vous demandez sans doute, soyons honnêtes, franchement ?, la
réalité, c'est que.
**Problème** : on annonce le propos ou une franchise au lieu de le dire.
Supprimer l'élan, pas seulement son ton. « Franchement » au milieu d'une
phrase familière est normal ; le tic, c'est l'ouverture isolée avant une
affirmation banale.
**Avant** : Que vous soyez artisan ou commerçant, vous vous demandez sans
doute comment être visible sur Google. Plongeons dans le sujet.
**Après** : Une fiche Google complète suffit souvent à apparaître dans
les recherches locales.

### 5. Répondre à personne

**À surveiller** : il ne s'agit pas de dire que, loin de moi l'idée,
entendons-nous bien, soyons clairs, on pourrait être tenté de, une
approche évidente serait, vous pensez peut-être que… mais, certains
diront.
**Problème** : le texte répond à une objection absente ou écarte une
option que personne n'a proposée, souvent un reste de brouillon.
Supprimer la défense ; si elle contient une affirmation, l'énoncer. Garder
une objection attribuée ou traitée en entier.
**Avant** : Il ne s'agit pas de dire que le papier est mort. Mais le
devis en ligne fait gagner du temps.
**Après** : Le devis en ligne évite de ressaisir les quantités.

## B. Rythme par règle

### 6. Triplets forcés

**Problème** : les idées arrivent par trois pour sonner complet (« rapide,
fiable et intuitif » ; trois exemples parallèles ; trois faits puis une
leçon). Vérifier que chaque élément apporte une idée distincte. Sinon :
fusionner, développer le plus fort, varier la structure. Garder trois
éléments quand le sens en compte trois.
**Avant** : Notre équipe est réactive, passionnée et à l'écoute.
**Après** : L'équipe répond aux demandes de devis dans la journée.

### 7. Ouvertures répétées

**Problème** : plusieurs phrases de suite commencent par le même sujet
(« Il… Il… Il… », « Cette solution… Cette solution… »). Fusionner, changer
de sujet, commencer par l'action. Ne pas bannir le mot : une répétition
voulue pour le rythme reste permise.
**Avant** : L'atelier ouvre à 8 h. L'atelier ferme à 18 h. L'atelier
reçoit sans rendez-vous.
**Après** : L'atelier reçoit sans rendez-vous, de 8 h à 18 h.

### 8. Le tiret à tout faire

**Règle** (règle dure du skill) : aucun tiret cadratin (—) dans le texte
final, sauf citation verbatim. Pas non plus de demi-cadratin (–) ni de
trait d'union espacé (` - `) ou doublé (` -- `) utilisé comme tiret. Le
demi-cadratin reste correct dans une plage (`2024–2026`, `9h–12h`). Code,
commandes, chemins et URLs ne sont pas concernés.
**Problème** : le tiret évite de choisir le lien entre deux propositions.
Le remplacer selon le sens : virgule, deux-points, parenthèses, point, ou
une autre phrase. Jamais de remplacement mécanique.
**Avant** : La nouvelle offre — annoncée sans préavis — concerne tous les
abonnés.
**Après** : La nouvelle offre, annoncée sans préavis, concerne tous les
abonnés.

### 9. Précautions empilées

**À surveiller** : pourrait potentiellement, semble relativement, dans
une certaine mesure, il est possible que… peut-être, a priori
éventuellement.
**Problème** : une précaution après l'autre, pour réparer une exagération
plutôt que pour signaler un vrai doute. Garder celle que la source
justifie. « Peut-être » ou « souvent » seuls sont des habitudes humaines.
*Faible seul.*
**Avant** : Cette mise à jour pourrait potentiellement avoir un certain
impact sur les performances.
**Après** : Cette mise à jour peut ralentir les anciens téléphones.

### 10. Doublets figés (adaptation française)

L'original traite des adjectifs composés anglais à trait d'union, sans
équivalent en français. Le tic voisin en français est la paire de
synonymes qui double le mot sans rien ajouter.
**À surveiller** : simple et efficace, clair et précis, rapide et
efficace, simple et intuitif, fiable et sécurisé, complet et détaillé.
**Problème** : le second mot ne dit rien que le premier ne disait. Garder
le mot exact, ou remplacer la paire par le fait qui la prouve.
*Faible seul.*
**Avant** : Une interface simple et intuitive.
**Après** : L'interface tient sur un écran : trois boutons, un champ de
recherche.

### 11. Phrases sans sujet, voix passive

**Problème** : la phrase cache qui agit ou n'a pas de sujet
(« Aucune installation nécessaire. », « Résultats conservés
automatiquement. »). Rétablir le sujet et l'action quand c'est plus clair.
Une étude sur l'anglais trouve que GPT-4o emploie *moins* le passif sans
agent que les humains (SUPPORTED, Reinhart et al. 2025) : le vrai signal,
ce sont les fragments nominaux. *Faible seul.*
**Avant** : Aucune configuration requise. Sauvegarde effectuée chaque
nuit.
**Après** : Vous n'avez rien à configurer. Le service sauvegarde vos
données chaque nuit.

## C. Inflation et autorité empruntée

Le fait dessous est souvent juste. Le garder, retirer l'habillage.

### 12. Mots d'IA

**À surveiller** (liste française, CLAIMED) : crucial, essentiel,
incontournable, primordial, véritable, indéniable, témoigner de,
souligner (au figuré), mettre en lumière, mettre en exergue, s'inscrire
dans, favoriser, optimiser (hors sens technique), levier, écosystème (au
figuré), paysage (au figuré), panorama, dynamique (nom), enjeu(x), au
cœur de, pierre angulaire, fer de lance, de pointe, robuste (au figuré),
fluide, sans couture, holistique, synergie, tirer parti, exploiter
pleinement, naviguer (au figuré), plonger, riche (au figuré), méticuleux,
subtil, vibrant, tapisserie (au figuré), booster, révolutionner.
**Problème** : les modèles emploient ces mots bien plus que les gens,
surtout groupés. En anglais, l'excès de vocabulaire de style des modèles
est mesuré (SUPPORTED, Kobak et al. 2025) ; pour le français, aucune
mesure publiée trouvée au 2026-09-28. Un mot soutenu hors liste n'est pas
un tic.
**Avant** : Cette solution de pointe s'inscrit dans une démarche
holistique et témoigne de notre engagement.
**Après** : Le logiciel regroupe la facturation et le planning.

### 13. Importance gonflée

**À surveiller** : marque un tournant, ouvre la voie, redéfinit, joue un
rôle clé, s'impose comme une référence, laisse une empreinte durable,
dans un contexte en pleine évolution ; les sections « Défis et
perspectives », « Et demain ? » ; les envois (« L'avenir s'annonce
prometteur », « Une belle aventure ne fait que commencer »).
**Problème** : un détail ordinaire est présenté comme un tournant, un
héritage, une promesse. Garder le fait, lâcher la portée. Finir sur le
dernier fait concret ; si la source donne de vrais projets, les citer.
**Avant** : L'ouverture de ce second atelier marque un tournant décisif
et ouvre la voie à un avenir prometteur.
**Après** : Le second atelier, ouvert en mars à Lyon, emploie quatre
personnes.

### 14. Lien vague

**À surveiller** : associé à, en lien avec, lié à, rattaché à, en
relation avec.
**Problème** : le texte dit que deux choses sont liées sans dire
comment. Nommer la relation que donne la source ; si elle ne la donne
pas, garder la formule vague plutôt qu'inventer un rôle.
**Avant** : Il est associé à la fondation de l'entreprise.
**Après** : Il a cofondé l'entreprise en 2019.

### 15. Participe présent de commentaire

**À surveiller** : « …, soulignant », « …, marquant ainsi », « …,
témoignant de », « …, illustrant », « …, confirmant », « …, reflétant »,
« …, offrant », « …, permettant ainsi », « …, renforçant ».
**Problème** : un participe accroché en fin de phrase donne une
profondeur que le fait n'a pas. En anglais, GPT-4o emploie les
propositions participiales à 5,3 fois le taux humain (SUPPORTED, Reinhart
et al. 2025) ; le transfert au français est une hypothèse raisonnable, non
mesurée. Garder le fait, et le commentaire seulement si la source le
porte.
**Avant** : Le chiffre d'affaires a progressé de 12 %, témoignant de la
solidité du modèle.
**Après** : Le chiffre d'affaires a progressé de 12 % en 2025.

### 16. Langue de vente

**À surveiller** : niché au cœur de, écrin, incontournable, à couper le
souffle, exceptionnel, prestigieux, un large éventail de, renommé,
d'exception, idéalement situé, havre de paix.
**Problème** : le texte lit comme une brochure. Dire ce qu'est la chose.
**Avant** : Niché au cœur du Vieux-Lyon, notre établissement vous
accueille dans un écrin d'exception.
**Après** : Le restaurant est rue Saint-Jean, dans le Vieux-Lyon.

### 17. Autorité empruntée

**À surveiller** : les experts, de nombreux observateurs, selon certains
spécialistes, des études montrent, une liste de médias prestigieux,
« plus de 10 000 abonnés ».
**Problème** : un nom ou une autorité anonyme remplace ce qui a été dit.
Nommer la source et ce qu'elle a dit, avec lien, ou couper. L'absence de
citation n'est pas un tic en soi : la plupart des textes ne citent rien.
**Avant** : Les experts s'accordent à dire que le télétravail augmente
la productivité.
**Après** : Selon l'enquête de [[à confirmer : source]], …

### 18. Éviter « est » et « a »

**À surveiller** : se positionne comme, se veut, fait figure de, s'impose
comme, constitue, représente, affiche, arbore, dispose de, propose
(pour « a »), bénéficie de.
**Problème** : un verbe simple est remplacé par un verbe de parade.
Écrire « est », « a ».
**Avant** : La salle se positionne comme l'espace de réception de la
mairie et dispose de 200 places.
**Après** : La salle est l'espace de réception de la mairie ; elle a
200 places.

## D. Mise en forme par règle

### 19. Gras décoratif

**Problème** : des mots en gras sans raison ; des listes où chaque
élément porte une étiquette en gras suivie de deux-points. Retirer le
gras ; transformer la liste en phrase quand les étiquettes n'apportent
rien.
**Avant** : - **Performance** : la performance a été améliorée.
**Après** : La mise à jour accélère le chargement des pages.

### 20. Titres décoratifs

**Problème** : majuscule à chaque mot (à l'anglaise), émojis ou flèches
dans les titres et les listes, filet entre chaque section, titre
d'effet (« La décision, en un écran ») au lieu d'un titre qui nomme le
contenu. En français, seul le premier mot et les noms propres prennent
la majuscule.
**Avant** : ## Nos Engagements Pour Votre Réussite 🚀
**Après** : ## Délais et garanties

### 21. Guillemets étrangers

**Problème** : en français, “ ” ou "…" à la place des guillemets
français « ». C'est d'abord une faute typographique, et un indice faible
d'un texte généré ou traduit. *Faible seul.* Règles :
[typographie-style.md](typographie-style.md).
**Avant** : Il a parlé d'un "délai raisonnable".
**Après** : Il a parlé d'un « délai raisonnable ».

## E. Restes de conversation et de brouillon

À supprimer d'office.

### 22. Résidus de chatbot

**À surveiller** : Bien sûr !, Absolument !, Excellente question,
Vous avez tout à fait raison, J'espère que cela vous aide, N'hésitez pas
à, Souhaitez-vous que je, Voulez-vous que, Voici un / une …, En tant
qu'IA, Je peux aussi.
**Problème** : l'accueil, le compliment ou l'offre d'un chatbot restent
dans un texte qui doit tenir seul. Retirer l'emballage, garder le
contenu. (Les formules de politesse d'une lettre ou d'un e-mail existent
depuis longtemps et ne sont pas visées.)

### 23. Limites de connaissance et suppositions

**À surveiller** : à ma connaissance, selon les informations
disponibles, à la date de ma dernière mise à jour, bien que les détails
soient limités, peu d'informations publiques, il est probable que (suivi
d'un fait supposé), on peut supposer que.
**Problème** : le texte montre où s'arrêtent les données du modèle, puis
comble le vide avec une supposition. Dire ce que la source ne montre pas,
ou couper la phrase.
**Avant** : Bien que peu d'informations soient disponibles, l'entreprise
a probablement été fondée dans les années 1990.
**Après** : La date de fondation ne figure pas dans les sources
consultées.

### 24. Titre répété en première phrase

**Problème** : un intertitre suivi d'une phrase qui le redit (« ## Tarifs »
puis « Parlons tarifs. »). Supprimer la phrase.

### 25. Parler du document au lieu du sujet

**À surveiller** : ce qui a été remplacé (« ajouté pour remplacer ») ;
comment le texte a été produit (« rédigé à partir de », « tout ce qui n'a
pu être confirmé est signalé ») ; la légende d'un tableau que le lecteur
voit déjà (« le tableau ci-dessous compare »).
**Problème** : le texte se décrit au lieu de parler de son sujet. Une
version précédente ne se mentionne que dans un changelog ou un guide de
migration. Garder une source que le lecteur peut suivre et une mise en
garde qui change ce qu'il doit faire. *Faible seul* pour une seule
description de page.

## F. Le mauvais lecteur

### 26. Réexpliquer ce que le lecteur sait

Ne s'applique qu'aux réponses (e-mail en fil, commentaire, message) quand
on voit l'échange.
**À surveiller** : une réponse courte qui reformule le problème, refait
le diagnostic et aligne les preuves avant d'arriver à la décision ; la
réponse dans la dernière ligne.
**Problème** : le lecteur a déjà le contexte ; le reconstruire enterre
le propos. Ouvrir sur la décision, ne garder que l'élément qui peut
changer son accord et le lien dont il a besoin pour agir.
**Avant** : Comme vous me l'indiquiez, votre site affiche l'ancien
horaire. J'ai vérifié : la page Contact et le pied de page sont
concernés. Après analyse, je peux corriger les deux ce soir.
**Après** : Je corrige ce soir l'horaire de la page Contact et du pied de
page.

## G. Tics propres au français (ajouts de ce skill)

Issus des prompts éditoriaux d'un site d'actualité (même auteur) et de relectures de
textes générés en français. CLAIMED.

### G1. Conclusions annoncées

**À surveiller** : en conclusion, en somme, en définitive, pour
conclure, pour résumer, vous l'aurez compris, au final ; un dernier
paragraphe qui résume ce qui vient d'être dit.
**Correction** : couper ; finir sur le dernier fait ou sur l'action.

### G2. Remplissage d'ouverture

**À surveiller** : dans un monde où, à l'heure où, de nos jours, à l'ère
du numérique, il est important de noter que, il convient de souligner
que, force est de constater, il va sans dire, pas de doute.
**Correction** : commencer par le fait.

### G3. Questions rhétoriques en série

**À surveiller** : ouverture par « Vous êtes-vous déjà demandé… ? » ;
une question par paragraphe ; question posée pour y répondre aussitôt.
**Exceptions** : la question finale d'un tweet, voulue par
`redaction-tweets-viraux` ; la vraie question d'un e-mail de prospection
(elle appelle une réponse) ; **une** question-titre sur une page de vente
quand `copywriting` la propose (« Marre de relancer vos devis ? »). Une,
pas une série.

### G4. Emphase à l'anglaise

**À surveiller** : points d'exclamation en série, mots en capitales,
majuscules de titre, « WOW », émojis en tête de ligne.

### G5. Registre incohérent

**À surveiller** : tutoiement et vouvoiement mêlés ; « on » et « nous »
alternés sans raison ; passage du « vous » au « les clients » pour le
même lecteur.
**Correction** : choisir une fois, d'après le brief ou l'échantillon.

### G6. Calques de l'anglais

**À surveiller** : faire sens, adresser un problème, être en charge de,
dans le futur, supporter (pour soutenir), opportunité (pour occasion),
délivrer (pour livrer, fournir), impacter. *Faible seul* : beaucoup de
francophones les emploient ; les corriger quand le registre est soutenu
ou quand ils s'accumulent.

## Quand ne pas agir

Chaque motif décrit un choix par défaut, et une personne peut faire
chacun exprès. Laisser en place une expression surveillée dans une
citation, un titre d'œuvre, un nom propre, ou un passage qui parle de
l'expression au lieu de l'employer. Les formules de politesse d'une
lettre sont antérieures aux chatbots. Un texte écrit avant le
30 novembre 2022 n'est pas un texte d'IA. Les gens qui jugent « à
l'oreille » font à peine mieux que le hasard, et l'écriture humaine
absorbe les habitudes des modèles : plusieurs indices ensemble sont la
seule garantie.

Garder ce qui porte la voix de l'auteur, sauf si le sens en souffre :

- un détail précis et inhabituel (une vraie adresse, une citation
  étrange, « l'avocat qui avait son bureau au-dessus de mon dentiste ») ;
- des sentiments mêlés, une tension non résolue ;
- des références datées d'une époque ou d'un milieu ;
- un choix à la première personne que l'auteur sait expliquer ;
- un vrai aparté, une parenthèse, une correction en cours de phrase.
