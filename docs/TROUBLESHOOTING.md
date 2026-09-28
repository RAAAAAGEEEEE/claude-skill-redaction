# Dépannage

## Le skill ne se charge pas

- Vérifier que le dossier s'appelle `redaction` et contient `SKILL.md` à
  sa racine : `ls ~/.claude/skills/redaction/SKILL.md`.
- Ouvrir une nouvelle session Claude Code : la liste des skills se lit au
  démarrage.
- Nommer le skill dans la demande : « avec le skill redaction, … ».
- Demande en anglais : le skill vise le français ; c'est voulu.

## Un autre skill se charge à la place

`copywriting` (pages de vente) ou `redaction-tweets-viraux` (tweets)
peuvent passer devant. Demander d'appliquer aussi `redaction` pour la
langue et la relecture. Voir la table d'articulation dans
[SKILL.md](../SKILL.md).

## `python` introuvable

Sous Windows, essayer `py scripts/verifier.py …`. Sans Python, le skill
fonctionne sans le contrôle mécanique, et Claude doit le signaler.

## Le vérificateur signale un faux positif

- Cadratin dans une **citation verbatim** : le garder, le justifier en
  une ligne.
- Heure `12:30`, ratio `16:9` : ignorés. Autre format technique : le
  mettre entre accents graves (code en ligne), que le vérificateur ignore.
- Le vérificateur appliqué aux fichiers de `references/` y trouve des
  dizaines de constats : normal, ces fichiers citent les tics qu'ils
  décrivent. Il sert pour la prose produite, pas pour le skill.

## `UnicodeDecodeError`, code de sortie 2

Le fichier n'est pas en UTF-8. Le réenregistrer en UTF-8.

## Les tests échouent

Lancer depuis la racine du skill :
`python -m unittest discover -s tests -v`, puis lire le test en échec.
Une modification des listes de `verifier.py` peut faire réagir la
fixture `tests/fixtures/propre.md`, qui ne doit produire aucun constat.

Voir aussi : [INSTALLATION.md](INSTALLATION.md).
