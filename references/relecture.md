# Relecture

Grille de la passe de relecture. Elle sert au sous-agent relecteur et à
toute relecture faite sans lui.

## Pourquoi une passe séparée

Un modèle qui relit son propre texte le défend ; un relecteur qui ne l'a
pas écrit le coupe. La règle du skill : toute rédaction publiée ou
envoyée passe par une rédaction, une relecture distincte par un modèle
plus fort, et une réécriture seulement si la relecture a trouvé quelque
chose. Aucun texte n'est « trop court » pour y échapper : un objet
d'e-mail de huit mots part à des milliers de destinataires.

## Lancer le relecteur

Sous-agent, `model: "opus"`, avec dans le prompt :

1. le brief (format, lecteur, but, contraintes) ;
2. le texte **mot pour mot**, jamais résumé ;
3. le matériau factuel et ses sources ;
4. les chemins absolus de ce fichier, de [anti-ia.md](anti-ia.md), de
   [typographie-style.md](typographie-style.md) et de la section utile de
   [formats.md](formats.md) ;
5. la sortie de `scripts/verifier.py` si elle a tourné ;
6. la consigne : « Tu relis un texte que tu n'as pas écrit. Tu ne le
   réécris pas. Tu rends des constats cités mot pour mot et un verdict. »

Dans un script (hors session interactive), passer au CLI l'identifiant
complet du modèle, jamais l'alias nu : l'alias peut pointer vers une
génération antérieure sans avertissement.

## Ordre de contrôle

Les premiers contrôles tuent un texte ; les derniers le polissent. Ne pas
passer la relecture sur le rythme tant qu'une affirmation invérifiable
reste au premier paragraphe.

### 1. Vérité (P0)

- Chaque affirmation factuelle remonte au brief, à un document fourni ou
  à une source citée.
- Chaque chiffre a une source ; « plus rapide », « la plupart »,
  « nombreux » sont des affirmations aussi.
- Noms de personnes, d'entreprises, de produits écrits comme ils
  s'écrivent.
- Citations exactes, mot pour mot, attribuées.
- Aucune fonction présentée comme disponible si elle est prévue ou en
  test.
- Une affirmation *probablement* vraie est un P0.

### 2. Risque (P0)

- Promesse juridique, médicale, financière, de santé ou d'emploi :
  signaler, ne pas lisser.
- Garantie de résultat (« vous obtiendrez »), comparaison nommée avec un
  concurrent sans preuve.
- Données personnelles au-delà de ce que la personne a publié.
- Tiret cadratin hors citation verbatim ; résidu de chatbot ;
  placeholder oublié (`[Ville]`, `{{nom}}`, `TODO`).
- Texte désaccentué.

### 3. Lecteur (P1)

- Le texte parle au lecteur du brief, pas à un acheteur générique.
- La première ligne tient les trois premières secondes ; si elle pouvait
  ouvrir n'importe quel autre texte, elle échoue.
- L'objection réelle du lecteur trouve une réponse.
- Jargon expliqué ou remplacé par le mot du lecteur.

### 4. Structure (P1)

- L'idée principale arrive avant que le lecteur décide de continuer.
- Structure du format respectée ([formats.md](formats.md)), ou écart
  justifié.
- Une seule action demandée, concrète.
- Longueur dans la cible ; au-delà, couper.
- Un paragraphe = une idée ; pas de paragraphe de transition seul.

### 5. Voix et tics (P1 ou P2)

- Motifs 1 à 5 de [anti-ia.md](anti-ia.md) : P1 à chaque occurrence.
- Autres motifs : P2, P1 s'ils s'accumulent.
- Registre stable (tutoiement ou vouvoiement), conforme à l'échantillon.

### 6. Typographie (P2, P1 si systématique)

- Espaces avant `: ; ! ?`, guillemets « », nombres, majuscules des
  titres : [typographie-style.md](typographie-style.md).

### 7. Métier (P2)

- Verbes forts ; adverbes supprimés quand le verbe suffit.
- Pas de mot ou de tournure répétés à quelques lignes, sauf effet voulu.
- Concret plutôt qu'abstrait.
- La dernière ligne conclut sur un fait ou une action.

## Format de sortie du relecteur

```
P0 : « <passage cité> » → <pourquoi> → <correction exigée>
P1 : « <passage cité> » → <pourquoi> → <correction exigée>
P2 : « <passage cité> » → <pourquoi> → <correction suggérée>
VERDICT : PUBLIER | RÉÉCRIRE | REPRENDRE LE BRIEF : <une ligne>
```

- `PUBLIER` : aucun P0, aucun P1. Les P2 sont listés, l'utilisateur décide.
- `RÉÉCRIRE` : P0 ou P1 corrigeables. C'est l'issue normale.
- `REPRENDRE LE BRIEF` : l'angle, le lecteur ou le brief sont faux ;
  aucune réécriture ne sauvera le texte. Dire ce qui doit changer.

Un constat sans passage cité n'est pas utilisable : l'ancrer ou le
retirer.

## Étalonnage

- **Inflation** : fabriquer des P1 pour paraître rigoureux. Cela brûle une
  réécriture pour rien.
- **Complaisance** : laisser passer un texte parce qu'il se lit bien. Un
  texte fluide est exactement celui qui fait passer un chiffre inventé.

Un texte bien écrit avec un chiffre inventé : `RÉÉCRIRE`, et ce chiffre
est un P0. Un texte terne mais exact et bien visé peut être `PUBLIER`,
avec des P2.

## Réécriture

Appliquer les constats et rien d'autre. Une phrase non signalée reste,
même si on l'aurait écrite autrement. Un constat inapplicable sans
inventer (la correction exige une preuve absente) : laisser le
`[[à confirmer]]` et le signaler.
