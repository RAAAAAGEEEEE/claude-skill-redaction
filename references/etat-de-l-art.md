# État de l'art : détection des textes d'IA et écriture « humaine »

Revu le **2026-09-28**. Chaque ligne porte une source primaire, sa date et
une étiquette :

- **ESTABLISHED** : texte officiel (loi, documentation d'un moteur ou d'un
  fournisseur sur son propre produit, ouvrage de référence) ;
- **SUPPORTED** : étude indépendante avec données (« prépublication » =
  arXiv, pas encore relue par un comité) ;
- **CLAIMED** : vendeur, blog, praticien, liste d'observations.

Un CLAIMED ne fonde jamais une règle dure du skill.

## Verdict

1. **Écrire pour le lecteur est la seule stratégie durable.** Les
   lecteurs entraînés repèrent les textes de modèle au vocabulaire, à la
   structure et au manque d'originalité, et restent fiables après
   paraphrase et « humanisation » (SUPPORTED). Ce sont des défauts de
   qualité avant d'être des signatures.
2. **Les détecteurs automatiques ne prouvent rien seuls.** Faux positifs
   documentés (non-natifs, textes légèrement retouchés), contournement
   facile par des outils d'humanisation, résultats très variables selon
   l'outil (SUPPORTED). OpenAI a retiré son propre détecteur pour
   manque de précision (ESTABLISHED).
3. **Ce que les détecteurs mesurent** : surtout le style des modèles
   entraînés à suivre des consignes, pas une propriété invariante du
   texte généré (SUPPORTED, prépublication). Retirer les tics améliore le
   texte ; cela ne garantit rien face à un détecteur, et ce n'est pas le
   but.
4. **Google ne pénalise pas l'IA, il pénalise le peu d'effort** : contenu
   IA admis s'il apporte de la valeur ; note la plus basse pour un
   contenu copié, paraphrasé ou généré sans originalité (ESTABLISHED).
5. **Transparence** : depuis le 2026-08-02, l'AI Act impose de signaler
   un texte généré publié pour informer le public sur une question
   d'intérêt public, sauf relecture humaine ou contrôle éditorial avec
   responsabilité éditoriale (ESTABLISHED).
6. **Coquilles volontaires** : aucune source ne mesure leur effet ; c'est
   une préférence de l'utilisateur, encadrée dans
   [humanisation.md](humanisation.md).
7. **Français** : aucune étude indépendante trouvée sur les tics propres
   aux modèles en français ; les listes françaises du skill sont CLAIMED.
   Les seules mesures sur la détection en français trouvées viennent de
   vendeurs de détecteurs.

## Textes officiels (ESTABLISHED)

| Affirmation | Source (date) |
|---|---|
| Contenu produit avec l'IA admis s'il apporte de la valeur ; en générer beaucoup sans valeur relève du *scaled content abuse* ; soigner exactitude et qualité | [Google, contenu IA](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) (maj 2025-12-10) |
| « Who, How, Why » : auteur évident, explication de l'usage de l'automatisation là où le lecteur se le demanderait ; aucun nombre de mots préféré | [Google, helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) (maj 2025-12-10) |
| Note la plus basse quand presque tout le contenu principal est copié, paraphrasé ou généré avec peu d'effort, d'originalité et de valeur ajoutée ; l'usage de l'IA seul ne détermine pas la note | [Consignes des évaluateurs](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf) (version du 2025-09-11) |
| Fiche d'établissement : pas de lien, pas de promotion ni de prix dans la description ; contenus avec fautes d'orthographe refusés | [Google Business Profile, consignes](https://support.google.com/business/answer/3038177?hl=fr) (consulté le 2026-09-28) |
| Article 50(4) : le déployeur signale un texte généré ou manipulé publié pour informer le public sur des questions d'intérêt public, sauf relecture humaine ou contrôle éditorial avec une personne qui porte la responsabilité éditoriale ; applicable depuis le 2026-08-02 | [Règlement (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) ; [lignes directrices de la Commission](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations) (consulté le 2026-09-28) |
| Article 50(2) : les fournisseurs marquent les sorties de leurs systèmes génératifs dans un format lisible par machine ; un code de bonnes pratiques sert de moyen de conformité | idem |
| OpenAI retire son classifieur de textes le 2023-07-20 pour « low rate of accuracy » (26 % de textes d'IA reconnus, 9 % de textes humains accusés à tort, chiffres de son annonce de janvier 2023) | [OpenAI](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/) (note du 2023-07-20) |
| SynthID Text : filigrane posé à l'échantillonnage, déployé dans Gemini puis publié en source ouverte ; il porte sur la génération, pas sur le style | [Dathathri et al., Nature](https://www.nature.com/articles/s41586-024-08025-4) (2024-10) |
| Prospection B2B par e-mail : sans consentement préalable si le message a un lien avec la fonction du destinataire ; expéditeur identifié ; opposition simple dans chaque message | [CNIL](https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique) (maj 2026-06-10) |

## Études indépendantes (SUPPORTED)

| Affirmation | Source (date) |
|---|---|
| Des annotateurs qui utilisent souvent des LLM pour écrire détectent les articles générés (GPT-4o, Claude 3.5 Sonnet, o1-Pro) : le vote majoritaire de cinq d'entre eux se trompe sur 1 article sur 300. Indices : vocabulaire (53 % des explications), structure des phrases, originalité, ton, conclusions formatées. Robustes à la paraphrase et à l'humanisation. Meilleurs que les détecteurs, sauf Pangram | [Russell, Karpinska, Iyyer, ACL 2025](https://aclanthology.org/2025.acl-long.267/) |
| Modèles ajustés aux consignes, en anglais : propositions participiales 2 à 5 fois plus fréquentes que chez les humains (GPT-4o : 5,3 fois), nominalisations 1,5 à 2 fois, passif sans agent environ deux fois moins ; style dense et nominal ; écarts plus grands que pour les modèles de base | [Reinhart et al., PNAS 122](https://www.pnas.org/doi/10.1073/pnas.2422455122) (2025) ; [arXiv 2410.16107](https://arxiv.org/abs/2410.16107) |
| Excès de « mots de style » après l'arrivée des LLM dans 15 millions de résumés PubMed : au moins 13,5 % des résumés de 2024 passés par un LLM | [Kobak et al., Science Advances 11](https://www.science.org/doi/10.1126/sciadv.adt3813) (2025-07-04) |
| Six expériences, 4 600 participants : les gens ne distinguent pas les autoprésentations générées ; leurs indices (première personne, contractions, sujets familiaux) sont trompeurs et exploitables | [Jakesch et al., PNAS 120](https://www.pnas.org/doi/10.1073/pnas.2208839120) (2023) |
| Sept détecteurs classent plus de la moitié des essais TOEFL de non-natifs comme générés, contre une précision quasi parfaite sur des essais d'élèves américains ; en cause, la faible variété lexicale | [Liang et al., Patterns](https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7) (2023) |
| RAID, plus de 6 millions de textes : les détecteurs perdent pied face aux attaques adverses, aux stratégies d'échantillonnage et aux modèles non vus | [Dugan et al., ACL 2024](https://aclanthology.org/2024.acl-long.674/) |
| Trois détecteurs commerciaux et un ouvert : seul Pangram tient un plafond de 0,5 % de faux positifs sans perdre en précision | [Jabarian et Imas, NBER w34223](https://www.nber.org/papers/w34223) (2025) |
| Résumés récents non modifiés accusés à tort dans 9 à 15 % des cas ; retouches légères conformes aux règles signalées dans 38 à 80 % des cas ; après un outil d'humanisation, détection sous 4 % | [Karr et al., arXiv 2608.11256](https://arxiv.org/abs/2608.11256) (2026-08, prépublication) |
| GPTZero et Pangram classent comme humains les textes de modèles de base et comme IA ceux des versions ajustées aux consignes : les détecteurs suivent les artefacts de cet ajustement | [Xu et al., arXiv 2605.19516](https://arxiv.org/abs/2605.19516) (2026-05, prépublication) |

## Vendeurs et praticiens (CLAIMED)

| Affirmation | Source (date) | Remarque |
|---|---|---|
| 26 motifs d'écriture IA, classés du plus fort au plus faible ; les tics de structure durent plus que les mots | [blader/humanizer v3.1.0](https://github.com/blader/humanizer) (2026-09-28) | Base de [anti-ia.md](anti-ia.md). Le README dit que passer les détecteurs n'est pas un objectif |
| Catalogue de signes d'écriture IA ; ce sont des indices, pas des preuves ; détecteurs à taux d'erreur non négligeables | [Wikipédia, Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (consulté le 2026-09-28) | Guide communautaire |
| Pangram 4 : AUROC 0,9916, 0,0041 % de faux positifs | [Pangram Labs, arXiv 2607.27183](https://arxiv.org/abs/2607.27183) (2026-07-29) | Rapport du vendeur sur son produit |
| Étude sur 11 000 textes français : le détecteur de l'éditeur arrive premier | [Lucide.ai](https://lucide.ai/meilleur-detecteur-ia-comparatif) (2026-07) | Conflit d'intérêts : l'éditeur se classe lui-même |
| Liste française de tournures de remplissage, de vocabulaire gonflé et de faux contrastes | Prompts éditoriaux d'un site d'actualité, v2.1.0 (2026-09-28) | Même auteur ; base des sections G et des listes françaises |

## Ce qui n'a pas été trouvé

- Aucune étude mesurant l'effet de fautes de frappe volontaires sur des
  lecteurs, des détecteurs ou le classement Google.
- Aucune étude indépendante sur les tics de style des LLM en français
  (équivalent de Kobak ou Reinhart).
- Aucune documentation d'un moteur qui dirait qu'il déclasse un texte
  parce qu'il « sonne IA » indépendamment de sa valeur.

À revoir à chaque mise à jour du skill : ces absences sont datées du
2026-09-28.
