# Mode humanisé

Revu le 2026-09-28. Preuves : [etat-de-l-art.md](etat-de-l-art.md).

## Ce que « humain » veut dire ici

Un texte se lit comme humain quand il fait des choix pour un lecteur et un
sujet : un détail précis, un avis assumé, une phrase courte au bon endroit,
une chose laissée de côté. Les lecteurs entraînés repèrent un texte de
modèle surtout au vocabulaire, à la structure et au manque d'originalité
(SUPPORTED, Russell et al. 2025). Les détecteurs automatiques, eux,
suivent surtout le style des modèles entraînés à suivre des consignes
(SUPPORTED, Xu et al. 2026, prépublication).

D'où l'ordre de travail :

1. **Matériau d'abord** : un fait de première main, un exemple réel, une
   donnée sourcée valent plus que tout réglage de style.
2. **Retirer les tics** de [anti-ia.md](anti-ia.md), motifs 1 à 5 en
   priorité.
3. **Voix** : suivre l'échantillon s'il existe ; sinon le genre (un billet
   peut avoir un avis, une doc non). Une opinion ne s'invente pas : elle
   vient de l'utilisateur ou du brief.
4. **Rythme** : phrases de longueurs inégales, paragraphes inégaux.
5. **Coquilles** : seulement dans le cadre ci-dessous.

Ce skill ne promet jamais qu'un texte sera « indétectable » : aucune
source ne permet de le garantir, et ce n'est pas le but. Le but est un
texte qu'on a envie de lire.

## Les coquilles (option sur demande)

Option demandée par certains utilisateurs, pas une technique démontrée : aucune
étude trouvée au 2026-09-28 ne mesure l'effet de fautes volontaires sur
les lecteurs, les détecteurs ou le classement (statut : préférence de
l'utilisateur ; effet non documenté).

**Quand** : uniquement si l'utilisateur demande un texte « humanisé »
(« humanise », « version humaine », « rends-le moins IA »). Jamais par
défaut, jamais parce qu'un autre skill le suggère.

**Combien** : une ou deux coquilles ordinaires par **article long**. Ce
skill fixe « long » à 800 mots et plus (convention du skill, à ajuster si
l'utilisateur le demande). En dessous : aucune, sauf demande explicite de
l'utilisateur pour ce texte.

**Quelle forme** : une faute de frappe banale sur un mot courant d'au
moins six lettres, en minuscules, sans apostrophe ni trait d'union, du
genre qu'un correcteur laisse passer. Trois formes seulement :

- accent oublié (« developpement », « deja ») ;
- deux lettres intérieures inversées (« porblème ») ;
- consonne double simplifiée (« dévelopement », « comercial »).

Pas de faute de grammaire, d'accord ni d'homophone (« a/à », « ces/ses »,
« et/est ») : elles passent pour de l'ignorance, pas pour de la frappe.
Un accent oublié fait réagir le vérificateur (`accent-manquant`, P1) :
c'est attendu, la coquille est listée en sortie.

**Jamais dans** :

- chiffres, prix, dates, heures, unités, pourcentages, numéros ;
- noms propres (personnes, entreprises, marques, produits, lieux) ;
- citations et avis reproduits ;
- titre, chapô, intertitres, première phrase, appel à l'action ;
- mot-clé principal de la page, balises `title`, meta description, texte
  alternatif, données structurées ;
- liens, URLs, adresses e-mail, code, commandes, chemins ;
- texte juridique (mentions légales, CGV, contrat, politique de
  confidentialité) ;
- texte d'interface (boutons, libellés, messages d'erreur, formulaires) ;
- e-mail transactionnel, fiche Google (les consignes Google y refusent
  les fautes), texte signé d'un tiers sans son accord.

**Où** : dans le corps, sur un mot ordinaire, deux coquilles dans deux
paragraphes différents et éloignés.

**Traçabilité** : la sortie liste chaque coquille (mot fautif, mot
correct, paragraphe) pour que l'utilisateur puisse la retirer. Une coquille non
listée est une faute, pas un choix.

## Transparence

Humaniser le style ne retire pas une mention d'assistance par IA que le
site affiche (par exemple une mention « article assisté par IA ») ou que la
loi impose. Pour un texte publié afin d'informer le public sur une
question d'intérêt public, l'AI Act exige de signaler un texte généré,
sauf relecture humaine ou contrôle éditorial avec une personne qui en
porte la responsabilité éditoriale (ESTABLISHED, article 50(4),
applicable depuis le 2026-08-02). La relecture par l'utilisateur avant
publication est donc aussi une condition de conformité.
