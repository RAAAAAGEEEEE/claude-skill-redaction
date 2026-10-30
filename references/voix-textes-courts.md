# Voix et textes courts (réponses, commentaires, posts brefs)

Chargé à l'étape 3 et 4 quand le texte est court (moins de 40 mots) et doit
sonner comme une personne précise : réponse à un message, commentaire,
post bref. Pour les textes longs, les autres références suffisent.

Statut des affirmations : ce qui suit est une méthode de travail et des
observations sur un corpus unique (CLAIMED). Aucune étude indépendante
ne la valide en français au 2026-10-30.

## Principe : le code décide, le prompt ne fait qu'écrire

Une interdiction écrite dans un prompt s'oublie ; un contrôle qui rejette
ne s'oublie pas. Trois déplacements :

1. **Les interdictions passent du prompt à un linter.** Le prompt ne
   contient plus de liste de tics à éviter (elle les rend plus présents) ;
   le linter rejette le candidat et on en régénère un.
2. **Les consignes de forme sont chiffrées par le code**, calculées sur le
   message auquel on répond : longueur en mots (fourchette), langue,
   tutoiement ou vouvoiement, registre, casse de la première lettre,
   points d'exclamation, de suspension, emoji. « Sois bref » devient
   « entre 9 et 17 mots ».
3. **La permission de poser une question est tirée par le code** (hachage
   déterministe de l'identifiant du message, taux proche de celui du
   corpus de la personne), pas décidée par le modèle. Sans permission, une
   question dans le candidat est un rejet.

## Exemples : 5 à 8, proches et variés

- Un corpus de textes de la personne, classés par provenance : **principal**
  (écrits et choisis à la main), **or** (marqués comme réussis), **machine**
  (écrits par un modèle, jamais injectés comme exemples, seulement
  utilisés pour calibrer la détection).
- Sélection par pertinence moins redondance (MMR) : on veut des exemples
  proches du message (même langue, même longueur) mais différents entre
  eux. Un léger tirage pseudo-aléatoire fixé par l'identifiant évite de
  resservir toujours les mêmes.
- Les exemples donnent le registre, pas les sujets : ne jamais en
  recopier une phrase (le linter rejette la copie d'un exemple).

## Fiche de faits

Tout chiffre ou fait sur le produit vient d'une fiche unique, où chaque
entrée porte sa valeur et sa preuve (fichier et ligne du code source, ou
URL datée). Dans le doute, le fait n'y entre pas. Une liste `ne_pas_dire`
(expressions régulières) rejette les affirmations fausses ou non
vérifiées ; un chiffre absent du message et de la fiche est rejeté.
Jamais d'anecdote personnelle inventée : le linter rejette « j'ai
testé », « chez moi », « ça m'est arrivé » et équivalents.

## Le linter commun

Deux niveaux : **bloquant** (rejet immédiat) et **faible** (rejet à
partir de deux). Familles de règles :

| Famille | Exemples |
|---|---|
| Typographie | cadratin, invisibles, markdown, entités HTML, lien, hashtag, mention |
| Tics d'IA | amorces et félicitations, connecteurs creux, morale finale, balancement « pas seulement, mais », gérondif de conclusion, apposition, formules d'assistant, prescriptif, triades |
| Questions | plusieurs, non permise, générique, ton d'entretien, hors-sol (sans détail précis du message) |
| Structure | réaction puis relance, plus long que le message, plus de deux phrases |
| Copie | quatre-grammes du message (deux ou plus : bloquant), paraphrase proche, exemple recopié |
| Faits | fait faux selon la fiche, chiffre inconnu, média non vu, expérience inventée |
| Variété | même début que les textes récents du même compte |

### Calibrer les seuils sur le corpus

Un linter trop dur rejette les vrais textes. Mesurer avant de figer :

- **Faux positifs** : taux de rejet sur les textes humains (principal et
  or). Cible : 0.
- **Détection** : taux de rejet sur les textes machine et sur les anciennes
  réponses du système. Cible : le plus haut possible sans toucher la ligne
  précédente.
- Les seuils numériques (longueur maximale, taux de questions) se lisent
  dans le corpus, pas dans l'intuition. Ils sont écrits dans un fichier de
  calibrage versionné, regénéré par un script.

Mesure faite sur le corpus d'origine de cette méthode : 0 rejet sur 15
textes humains, 144 sur 156 textes machine, 4 sur 5 anciennes réponses.
Ces chiffres valent pour ce corpus ; les refaire sur le vôtre.

## Chaîne de rédaction

1. Rédacteur (Sonnet 5.5, effort high) : propose 4 candidats avec les
   consignes chiffrées, les exemples et la fiche de faits.
2. Linter : écarte les candidats rejetés. S'ils le sont tous, une seule
   régénération, puis abandon (mieux vaut ne rien envoyer).
3. Juge de ressemblance (Opus 5.5, effort medium) : compare les candidats
   restants à cinq vrais textes de la personne et choisit, ou refuse.
4. Contrôle mécanique propre au projet (marque, lien, longueur).

Toujours l'identifiant complet du modèle, jamais un alias nu.

## Banc à l'aveugle

Pour savoir si la voix tient, ne pas se fier à sa propre lecture.

- **Jeu** : 30 textes mélangés, 15 vrais (corpus) contre 15 générés sur
  des messages réels récents.
- **Juges** : deux modèles distincts devinent « humain » ou « IA » pour
  chaque texte, dans deux ordres différents (pour neutraliser le biais de
  position). Rapporter la précision de chaque juge. Une précision proche de
  50 % veut dire que le juge ne distingue pas ; elle ne prouve pas que le
  texte passera auprès d'un lecteur humain.
- **Banc pour la personne elle-même** : 10 paires numérotées et
  mélangées (un vrai, un généré), les réponses dans un fichier séparé.
  C'est son verdict qui compte.
- **Budget** : plafonner le nombre d'appels et vérifier le plafond
  d'abonnement avant de lancer.

### Limites connues de la méthode

- Le corpus n'est pas entièrement écrit à la main : d'où les classes de
  provenance. Un exemple « machine » injecté ferait boucler le système.
- Posts contre réponses : les vrais textes du corpus sont des posts, les
  textes générés sont des réponses. Le genre est un facteur de confusion
  que les juges peuvent exploiter ; à signaler avec le résultat.
- n = 30 : un écart de quelques points n'est pas significatif.
- Les juges sont des modèles : ils repèrent des formes d'IA, pas le sens.

Voir aussi : [anti-ia.md](anti-ia.md), [relecture.md](relecture.md),
[../docs/LIMITATIONS.md](../docs/LIMITATIONS.md).
