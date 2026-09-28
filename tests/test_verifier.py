"""Tests hors ligne de scripts/verifier.py."""
import io
import json
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import verifier  # noqa: E402

FIX = os.path.join(HERE, "fixtures")
NB = "\u00a0"
FN = "\u202f"


def rules(text):
    return [(f.priority, f.rule) for f in verifier.verify(text)]


def read(name):
    with io.open(os.path.join(FIX, name), encoding="utf-8") as fh:
        return fh.read()


class CleanText(unittest.TestCase):
    def test_clean_fixture_has_no_finding(self):
        self.assertEqual(verifier.verify(read("propre.md")), [])


class HardRules(unittest.TestCase):
    def test_em_dash_is_p0(self):
        self.assertIn(("P0", "cadratin"), rules("Le devis part vite \u2014 en deux minutes."))

    def test_em_dash_inside_code_is_ignored(self):
        self.assertEqual(rules("Exemple : `a \u2014 b` dans le code."), [])

    def test_en_dash_in_range_is_allowed(self):
        self.assertEqual(rules("Ouvert de 2024\u20132026."), [])

    def test_spaced_en_dash_is_p1(self):
        self.assertIn(("P1", "demi-cadratin"), rules("La boutique \u2013 rue Haute \u2013 ouvre tôt."))

    def test_spaced_hyphen_used_as_dash(self):
        self.assertIn(("P1", "trait-union-tiret"), rules("La boutique - rue Haute - ouvre tôt."))

    def test_chatbot_residue_is_p0(self):
        self.assertIn(("P0", "residu-chatbot"), rules("Voici le texte. J'espère que cela vous aide."))

    def test_placeholder_is_p0(self):
        self.assertIn(("P0", "placeholder"), rules(f"Votre artisan à [Ville]{NB}!"))
        self.assertIn(("P0", "placeholder"), rules("Bonjour {{prenom}},"))

    def test_unaccented_text_is_p0(self):
        found = rules(read("desaccentue.md"))
        self.assertIn(("P0", "desaccentue"), found)
        self.assertIn(("P1", "accent-manquant"), found)

    def test_short_text_skips_accent_ratio(self):
        self.assertNotIn(("P0", "desaccentue"), rules("Merci."))


class AiPatterns(unittest.TestCase):
    def test_fixture_triggers_expected_rules(self):
        found = set(rules(read("ia.md")))
        for expected in [("P1", "formule-ia"), ("P2", "vocabulaire-gonfle"),
                         ("P2", "participe-commentaire"), ("P2", "titre-majuscules"),
                         ("P2", "titre-emoji")]:
            self.assertIn(expected, found)

    def test_false_contrast(self):
        self.assertIn(("P1", "formule-ia"), rules("Ce n'est pas un outil, c'est un partenaire."))

    def test_open_item_is_listed(self):
        self.assertIn(("P1", "a-confirmer"), rules("Fondée en [[à confirmer : année]]."))

    def test_repeated_openings(self):
        text = ("L'atelier ouvre tôt le matin. L'atelier ferme tard. L'atelier reçoit sans "
                "rendez-vous. Le parking est gratuit. Les vélos entrent. On paie par carte. "
                "Le café est offert aux clients du matin qui attendent leur commande. Fin.")
        self.assertIn(("P2", "ouvertures-repetees"), rules(text))

    def test_uniform_rhythm(self):
        text = " ".join(["Le magasin ouvre ses portes à neuf heures."] * 9)
        self.assertIn(("P2", "rythme-uniforme"), rules(text))


class Typography(unittest.TestCase):
    def test_missing_space_before_high_punctuation(self):
        self.assertIn(("P1", "espace-ponctuation"), rules("Attention: le magasin ferme."))
        self.assertIn(("P1", "espace-ponctuation"), rules("Vraiment?"))

    def test_time_and_url_are_not_flagged(self):
        self.assertEqual(rules(f"Rendez-vous à 12:30 sur https://exemple.fr/page?x=1 demain."), [])

    def test_quotes(self):
        self.assertIn(("P2", "guillemets-etrangers"), rules('Il parle d\'un "délai raisonnable".'))
        self.assertIn(("P2", "guillemets-etrangers"), rules("Il parle d'un “délai”."))
        self.assertIn(("P2", "guillemets-espaces"), rules("Il parle d'un «délai»."))
        self.assertEqual(rules(f"Il parle d'un «{NB}délai{NB}»."), [])

    def test_ordinals_ellipsis_percent(self):
        found = rules("Le 2ème essai... donne 15% de plus.")
        self.assertIn(("P2", "ordinal"), found)
        self.assertIn(("P2", "points-suspension"), found)
        self.assertIn(("P2", "pourcentage"), found)


class Cli(unittest.TestCase):
    def run_cli(self, *args, stdin=None):
        return subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "verifier.py"), *args],
                              input=stdin, capture_output=True)

    def test_exit_codes(self):
        self.assertEqual(self.run_cli(os.path.join(FIX, "propre.md")).returncode, 0)
        self.assertEqual(self.run_cli(os.path.join(FIX, "ia.md")).returncode, 1)
        self.assertEqual(self.run_cli(os.path.join(FIX, "absent.md")).returncode, 2)

    def test_stdin_and_json(self):
        res = self.run_cli("-", "--json", stdin="Texte \u2014 avec cadratin.".encode("utf-8"))
        self.assertEqual(res.returncode, 1)
        data = json.loads(res.stdout.decode("utf-8"))
        self.assertEqual(data[0]["rule"], "cadratin")


if __name__ == "__main__":
    unittest.main()
