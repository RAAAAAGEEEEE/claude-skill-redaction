# Limites

- **Pas d'évaluation du comportement du modèle.** Les 28 tests couvrent
  le vérificateur et la cohérence des cas de `evals/`. Rien ne mesure
  automatiquement si Claude choisit ce skill au bon moment ni si ses
  textes sont meilleurs ; les 6 cas de [evals/](../evals/README.md) se
  rejouent à la main.
- **Listes françaises non mesurées.** Au 2026-09-28, aucune étude
  indépendante ne mesure les tics des modèles en français ; les listes
  sont des observations (CLAIMED). Les études citées portent sur
  l'anglais.
- **Le vérificateur voit des formes, pas le sens.** Il ne repère ni un
  fait inventé, ni un triplet reformulé, ni un contraste sans formule
  figée. Il produit des faux positifs (citation verbatim) et des faux
  négatifs.
- **Contrôle d'accents approximatif** : seuil global et liste de racines ;
  un texte court ou très technique peut passer.
- **Pas « indétectable ».** Retirer les tics ne garantit rien face à un
  détecteur ; les détecteurs eux-mêmes se trompent dans les deux sens
  (voir [references/etat-de-l-art.md](../references/etat-de-l-art.md)).
- **Coquilles volontaires** : préférence du propriétaire du skill, sans
  effet mesuré. Elles peuvent coûter en crédibilité ; elles sont donc
  interdites dans les zones sensibles et toujours listées.
- **Relecture par Opus** : suppose un abonnement ou un accès qui permet
  de lancer un sous-agent sur ce modèle. Sinon, relecture par la même
  session, moins fiable, et signalée.
- **Typographie** : conventions de France par défaut ; public québécois
  à préciser dans le brief.
- **Date** : l'état de l'art est daté du 2026-09-28 et vieillit vite
  (lois, consignes de Google, études).

Voir aussi : [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
