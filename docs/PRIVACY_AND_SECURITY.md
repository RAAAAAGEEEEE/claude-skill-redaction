# Confidentialité et sécurité

## Ce qui sort de la machine

- **Vérificateur** : rien. Il lit un fichier local ou l'entrée standard,
  écrit sur la sortie standard, et n'importe aucun module réseau.
- **Skill** : les textes et le brief restent dans la session Claude Code ;
  le sous-agent relecteur tourne dans la même session. Une recherche web
  n'a lieu que si la rédaction l'exige, avec les outils de la session.
- Aucune clé, aucun jeton, aucun compte.

## Ce que le skill ne fait jamais

- Envoyer un e-mail, publier un post, pousser un fichier sans demande
  explicite dans le tour.
- Recopier dans un rapport ou un dépôt les données personnelles d'un
  texte (destinataire d'un e-mail, client cité).
- Suivre des instructions contenues dans un texte à relire : le texte
  est une matière, jamais une consigne.

## Données personnelles dans les textes

Un e-mail de prospection ou une réponse client contient souvent un nom et
une adresse. Les garder hors des fixtures et des exemples publics ; les
exemples du dépôt sont fictifs et marqués comme tels.

## Signaler une faille

Ouvrir une issue sans détail exploitable, ou contacter le mainteneur via
son profil GitHub.

Voir aussi : [LIMITATIONS.md](LIMITATIONS.md).
