#!/usr/bin/env python3
"""Contrôle mécanique d'un texte français avant relecture.

Signale ce qu'une consigne de prompt ne suffit pas à empêcher : tiret
cadratin, résidus de chatbot, placeholders oubliés, texte désaccentué,
formules d'écriture IA, typographie française, rythme uniforme.

Usage :
    python scripts/verifier.py texte.md
    python scripts/verifier.py - < texte.txt
    python scripts/verifier.py texte.md --json

Code de sortie : 0 = aucun P0, 1 = au moins un P0, 2 = entrée illisible.
Bibliothèque standard seulement, aucun accès réseau.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from dataclasses import asdict, dataclass

VERSION = "1.0.0"

EM_DASH = "\u2014"
EN_DASH = "\u2013"


@dataclass
class Finding:
    priority: str  # P0, P1, P2
    rule: str
    line: int
    excerpt: str
    message: str


# --- Listes -------------------------------------------------------------

CHATBOT_RESIDUE = [
    r"j'esp[èe]re que (cela|ceci|ça) (vous |t')?aide",
    r"n'h[ée]sitez pas [àa] (me |nous )?(contacter|demander|poser|revenir)",
    r"\bbien s[ûu]r\s*!",
    r"\babsolument\s*!",
    r"\bexcellente question\b",
    r"\bvous avez (tout [àa] fait|parfaitement) raison\b",
    r"\ben tant qu'(ia|intelligence artificielle|assistant)\b",
    r"\bsouhaitez-vous que je\b",
    r"\bvoulez-vous que je\b",
    r"\bje peux aussi (vous )?(proposer|r[ée]diger|g[ée]n[ée]rer)\b",
    r"\bà ma connaissance\b",
    r"\b(ma|mes) derni[èe]re?s? mise[s]? [àa] jour\b",
]

PLACEHOLDERS = [
    r"\[(ville|nom|pr[ée]nom|entreprise|soci[ée]t[ée]|date|adresse|t[ée]l[ée]phone|produit|client|lien|url)\]",
    r"\{\{[^}]+\}\}",
    r"\bTODO\b",
    r"\bXXX\b",
    r"\blorem ipsum\b",
]

OPEN_ITEM = r"\[\[\s*[àa] confirmer[^\]]*\]\]"

STAGING = [  # motifs 1 à 5, G1, G2 : P1
    (r"\bce n'est pas (seulement |simplement |uniquement |juste )?[^.;:!?]{1,80}, c'est\b", "faux contraste « ce n'est pas X, c'est Y » (motif 1)"),
    (r"\bnon pas [^.;:!?]{1,60} mais\b", "faux contraste « non pas X mais Y » (motif 1)"),
    (r"\bpas (seulement|uniquement|simplement) [^.;:!?]{1,60}, mais (aussi|également|surtout)\b", "faux contraste « pas seulement X, mais Y » (motif 1)"),
    (r"\bplus qu'un[e]? [^.;:!?]{1,40}, (un|une|c'est)\b", "faux contraste « plus qu'un X, un Y » (motif 1)"),
    (r"\bil ne s'agit pas de\b", "réponse à une objection absente (motif 5)"),
    (r"\b(et )?(ça|cela) change tout\b", "phrase-chute (motif 2)"),
    (r"\btout est (dit|là)\b", "phrase-chute (motif 2)"),
    (r"\bla vraie question\b", "maxime (motif 3)"),
    (r"^\s*au fond,", "maxime (motif 3)"),
    (r"\b(plongeons|d[ée]couvrons|explorons|d[ée]cortiquons)\b", "élan avant le propos (motif 4)"),
    (r"\bvoici ce qu'il faut savoir\b", "élan avant le propos (motif 4)"),
    (r"\bentrons dans le vif du sujet\b", "élan avant le propos (motif 4)"),
    (r"\bsans plus attendre\b", "élan avant le propos (motif 4)"),
    (r"\bdans cet article,? (nous|on|je) (allons|va|vais)\b", "annonce du plan (motif 4)"),
    (r"\bque vous soyez [^.;:!?]{1,50} ou\b", "ouverture « que vous soyez X ou Y » (motif 4)"),
    (r"\bdans un monde o[ùu]\b", "remplissage d'ouverture (G2)"),
    (r"\b[àa] l'heure o[ùu]\b", "remplissage d'ouverture (G2)"),
    (r"\b[àa] l'[èe]re du num[ée]rique\b", "remplissage d'ouverture (G2)"),
    (r"\bil (est|semble) (important|essentiel|crucial|primordial) de (noter|souligner|rappeler)\b", "remplissage (G2)"),
    (r"\bil convient de (noter|souligner|rappeler)\b", "remplissage (G2)"),
    (r"\bforce est de constater\b", "remplissage (G2)"),
    (r"\bil va sans dire\b", "remplissage (G2)"),
    (r"^\s*(en conclusion|en somme|en d[ée]finitive|pour conclure|pour r[ée]sumer|vous l'aurez compris)\b", "conclusion annoncée (G1)"),
]

INFLATED = [  # motif 12, 13, 16, 18 : P2, compté
    "crucial", "cruciale", "cruciaux", "cruciales", "incontournable", "primordial", "indéniable",
    "témoigne", "témoignent", "témoignant", "mettre en lumière", "met en lumière",
    "mettent en lumière", "met en exergue", "s'inscrit dans", "s'inscrivent dans",
    "pierre angulaire", "fer de lance", "de pointe", "holistique", "synergie",
    "écosystème", "paysage numérique", "tirer parti", "exploiter pleinement",
    "sans couture", "révolutionnaire", "révolutionner", "game changer",
    "marque un tournant", "ouvre la voie", "redéfinit", "niché", "nichée",
    "écrin", "à couper le souffle", "se positionne comme", "se veut",
    "fait figure de", "véritable", "booster",
]

PARTICIPLE_RIDER = r",\s+(soulignant|marquant(?: ainsi)?|t[ée]moignant|illustrant|confirmant|refl[ée]tant|renfor[çc]ant|d[ée]montrant|permettant ainsi|offrant ainsi)\b"

# Racines qui n'existent pas sans accent en français correct (écrites avec
# [a-z] et non \w : \w engloberait la lettre accentuée suivante).
UNACCENTED_ROOTS = r"(?<![a-zà-ÿ])(apres|deja|tres|telephon[a-z]*|formalit[a-z]*|etablissement[a-z]*|societe[s]?|equipe[s]?|qualite[s]?|securite|resume|numero[s]?|interet[s]?|etre|premiere[s]?|derniere[s]?|annee[s]?|periode[s]?|reponse[s]?|creation[s]?|developpement[s]?)(?![a-zà-ÿ])"

ACCENTED = set("àâäéèêëîïôöùûüÿçœæÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇŒÆ")

EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27bf\u2b50\u2b06\u2194-\u21ff]")


# --- Préparation du texte ------------------------------------------------

def strip_code(text: str) -> list[tuple[int, str]]:
    """Renvoie (numéro de ligne, ligne) hors blocs de code, code en ligne
    et URLs, pour ne contrôler que la prose."""
    out = []
    in_fence = False
    for i, raw in enumerate(text.splitlines(), start=1):
        if raw.strip().startswith("```") or raw.strip().startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", " ", raw)
        line = re.sub(r"https?://\S+|www\.\S+|\S+@\S+\.\w+", " ", line)
        out.append((i, line))
    return out


def excerpt(line: str, start: int, end: int, width: int = 30) -> str:
    a = max(0, start - width)
    b = min(len(line), end + width)
    return ("…" if a > 0 else "") + line[a:b].strip() + ("…" if b < len(line) else "")


# --- Contrôles -----------------------------------------------------------

def check_dashes(lines):
    found = []
    for n, line in lines:
        for m in re.finditer(EM_DASH, line):
            found.append(Finding("P0", "cadratin", n, excerpt(line, m.start(), m.end()),
                                 "Tiret cadratin interdit (sauf citation verbatim) : virgule, deux-points, parenthèses ou point."))
        for m in re.finditer(r"(?<=\S) " + EN_DASH + r" (?=\S)", line):
            found.append(Finding("P1", "demi-cadratin", n, excerpt(line, m.start(), m.end()),
                                 "Demi-cadratin espacé employé comme tiret ; il ne sert qu'aux plages (2024\u20132026)."))
        for m in re.finditer(r"(?<=[a-zà-ÿA-Z,]) (-|--) (?=[a-zà-ÿA-Z])", line):
            found.append(Finding("P1", "trait-union-tiret", n, excerpt(line, m.start(), m.end()),
                                 "Trait d'union espacé ou doublé employé comme tiret."))
    return found


def check_patterns(lines, patterns, priority, rule, message):
    found = []
    for n, line in lines:
        for pat in patterns:
            for m in re.finditer(pat, line, flags=re.IGNORECASE):
                found.append(Finding(priority, rule, n, excerpt(line, m.start(), m.end()), message))
    return found


def check_staging(lines):
    found = []
    for n, line in lines:
        for pat, msg in STAGING:
            for m in re.finditer(pat, line, flags=re.IGNORECASE):
                found.append(Finding("P1", "formule-ia", n, excerpt(line, m.start(), m.end()), msg))
    return found


def check_inflated(lines):
    found = []
    for n, line in lines:
        low = line.lower()
        for word in INFLATED:
            for m in re.finditer(r"(?<![a-zà-ÿ])" + re.escape(word) + r"(?![a-zà-ÿ])", low):
                found.append(Finding("P2", "vocabulaire-gonfle", n, excerpt(line, m.start(), m.end()),
                                     f"« {word} » : vocabulaire gonflé ou verbe de parade (motifs 12, 13, 16, 18)."))
        for m in re.finditer(PARTICIPLE_RIDER, line, flags=re.IGNORECASE):
            found.append(Finding("P2", "participe-commentaire", n, excerpt(line, m.start(), m.end()),
                                 "Participe présent de commentaire en fin de phrase (motif 15)."))
    return found


def check_typography(lines):
    found = []
    for n, line in lines:
        # Espace avant la ponctuation haute (on ignore heures 12:30, ratios 16:9, :: et smileys)
        for m in re.finditer(r"(?<=[a-zà-ÿA-ZÀ-Ÿ0-9»)\]])([;!?]|:(?![\d/]))", line):
            found.append(Finding("P1", "espace-ponctuation", n, excerpt(line, m.start(), m.end()),
                                 f"Espace manquante avant « {m.group(0)} » (insécable si possible)."))
        for m in re.finditer(r"«(?=\S)|(?<=\S)»", line):
            found.append(Finding("P2", "guillemets-espaces", n, excerpt(line, m.start(), m.end()),
                                 "Espace (insécable) à l'intérieur des guillemets « »."))
        for m in re.finditer(r"[\u201c\u201d]|(?<![\w=])\"(?=[a-zà-ÿA-ZÀ-Ÿ])", line):
            found.append(Finding("P2", "guillemets-etrangers", n, excerpt(line, m.start(), m.end()),
                                 "Guillemets anglais ou droits : en français, « »."))
        for m in re.finditer(r"\.\.\.", line):
            found.append(Finding("P2", "points-suspension", n, excerpt(line, m.start(), m.end()),
                                 "Trois points : utiliser le caractère « … »."))
        for m in re.finditer(r"\b\d+(ème|eme|ère|ere|nd|nde)\b", line, flags=re.IGNORECASE):
            found.append(Finding("P2", "ordinal", n, excerpt(line, m.start(), m.end()),
                                 "Ordinal : 1er, 1re, 2e (pas 2ème, 1ère, 2nd)."))
        for m in re.finditer(r"(?<=\d)%", line):
            found.append(Finding("P2", "pourcentage", n, excerpt(line, m.start(), m.end()),
                                 "Espace insécable avant « % »."))
        for m in re.finditer(r"!!+|\?!|!\?", line):
            found.append(Finding("P1", "exclamation", n, excerpt(line, m.start(), m.end()),
                                 "Ponctuation expressive en série."))
        if line.lstrip().startswith("#"):
            title = line.lstrip("# ").strip()
            words = [w for w in re.findall(r"[A-Za-zÀ-ÿ']+", title) if len(w) > 3]
            if len(words) >= 3 and sum(w[0].isupper() for w in words[1:]) >= 2:
                found.append(Finding("P2", "titre-majuscules", n, title[:60],
                                     "Titre en majuscules à l'anglaise : seule la première lettre et les noms propres (motif 20)."))
            if EMOJI.search(title):
                found.append(Finding("P2", "titre-emoji", n, title[:60], "Émoji ou flèche dans un titre (motif 20)."))
    return found


def check_accents(text_lines):
    found = []
    prose = " ".join(l for _, l in text_lines)
    letters = [c for c in prose if c.isalpha()]
    if len(letters) >= 300:
        ratio = sum(c in ACCENTED for c in letters) / len(letters)
        if ratio < 0.005:
            found.append(Finding("P0", "desaccentue", 0, f"{ratio:.2%} de lettres accentuées",
                                 "Texte désaccentué : un français courant en compte en général plusieurs pour cent."))
    for n, line in text_lines:
        for m in re.finditer(UNACCENTED_ROOTS, line.lower()):
            found.append(Finding("P1", "accent-manquant", n, excerpt(line, m.start(), m.end()),
                                 f"« {m.group(0)} » s'écrit avec un accent."))
    return found


def split_sentences(prose: str) -> list[str]:
    parts = re.split(r"(?<=[.!?…])\s+(?=[A-ZÀ-Ÿ«])", prose)
    return [p.strip() for p in parts if len(p.split()) >= 2]


def check_rhythm(text_lines):
    found = []
    prose_lines = [(n, l) for n, l in text_lines if l.strip() and not l.lstrip().startswith(("#", "|", "-", "*", ">"))]
    prose = " ".join(l.strip() for _, l in prose_lines)
    sentences = split_sentences(prose)
    lengths = [len(s.split()) for s in sentences]
    if len(lengths) >= 8:
        mean = statistics.mean(lengths)
        cv = statistics.pstdev(lengths) / mean if mean else 0
        if cv < 0.25:
            found.append(Finding("P2", "rythme-uniforme", 0, f"{len(lengths)} phrases, {mean:.0f} mots en moyenne, variation {cv:.2f}",
                                 "Phrases de longueur presque identique : varier (CLAIMED)."))
    firsts = [s.split()[0].lower().strip("«»,;:") for s in sentences]
    for i in range(len(firsts) - 2):
        if firsts[i] == firsts[i + 1] == firsts[i + 2] and len(firsts[i]) > 1:
            found.append(Finding("P2", "ouvertures-repetees", 0, " / ".join(sentences[i:i + 3])[:90],
                                 f"Trois phrases de suite commencent par « {firsts[i]} » (motif 7)."))
            break
    words = len(prose.split())
    bold = len(re.findall(r"\*\*[^*]+\*\*", prose))
    if words >= 150 and bold / words > 0.01:
        found.append(Finding("P2", "gras-decoratif", 0, f"{bold} passages en gras pour {words} mots",
                             "Gras décoratif (motif 19)."))
    return found


def check_open_items(text_lines):
    return [Finding("P1", "a-confirmer", n, m.group(0), "Point à confirmer avant publication.")
            for n, l in text_lines for m in re.finditer(OPEN_ITEM, l, flags=re.IGNORECASE)]


def verify(text: str) -> list[Finding]:
    lines = strip_code(text)
    findings: list[Finding] = []
    findings += check_dashes(lines)
    findings += check_patterns(lines, CHATBOT_RESIDUE, "P0", "residu-chatbot",
                               "Résidu de conversation de chatbot (motifs 22, 23).")
    findings += check_patterns(lines, PLACEHOLDERS, "P0", "placeholder", "Placeholder oublié.")
    findings += check_accents(lines)
    findings += check_staging(lines)
    findings += check_open_items(lines)
    findings += check_typography(lines)
    findings += check_inflated(lines)
    findings += check_rhythm(lines)
    order = {"P0": 0, "P1": 1, "P2": 2}
    findings.sort(key=lambda f: (order[f.priority], f.line))
    return findings


def render(findings: list[Finding]) -> str:
    counts = {p: sum(f.priority == p for f in findings) for p in ("P0", "P1", "P2")}
    out = [f"verifier.py {VERSION} : P0={counts['P0']} P1={counts['P1']} P2={counts['P2']}"]
    for f in findings:
        where = f"l.{f.line}" if f.line else "texte"
        out.append(f"  {f.priority} [{f.rule}] {where} : {f.excerpt}")
        out.append(f"      {f.message}")
    return "\n".join(out)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Contrôle mécanique d'un texte français.")
    parser.add_argument("fichier", help="chemin du texte, ou - pour l'entrée standard")
    parser.add_argument("--json", action="store_true", help="sortie JSON")
    args = parser.parse_args(argv)
    try:
        if args.fichier == "-":
            text = sys.stdin.buffer.read().decode("utf-8")
        else:
            with open(args.fichier, encoding="utf-8") as fh:
                text = fh.read()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"Entrée illisible : {exc}", file=sys.stderr)
        return 2
    findings = verify(text)
    if args.json:
        sys.stdout.buffer.write(json.dumps([asdict(f) for f in findings], ensure_ascii=False, indent=2).encode("utf-8"))
        sys.stdout.buffer.write(b"\n")
    else:
        sys.stdout.buffer.write(render(findings).encode("utf-8") + b"\n")
    return 1 if any(f.priority == "P0" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
