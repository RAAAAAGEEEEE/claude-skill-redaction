"""Tests hors ligne de evals/evals.json : structure, fixtures et vérificateur.

Ils ne mesurent pas le comportement de Claude (aucune évaluation
automatique n'existe pour cela). Ils garantissent que les cas sont bien
formés, que les sorties de référence passent le vérificateur et que les
sorties fautives déclenchent les règles attendues.
"""
import io
import json
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EVALS_DIR = os.path.join(ROOT, "evals")
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import verifier  # noqa: E402

ORDER = {"P0": 0, "P1": 1, "P2": 2}


def load():
    with io.open(os.path.join(EVALS_DIR, "evals.json"), encoding="utf-8") as fh:
        return json.load(fh)


def read(rel):
    with io.open(os.path.normpath(os.path.join(EVALS_DIR, rel)), encoding="utf-8") as fh:
        return fh.read()


class Structure(unittest.TestCase):
    def test_at_least_three_realistic_cases(self):
        self.assertGreaterEqual(len(load()["evals"]), 3)

    def test_each_case_is_complete_and_ids_are_unique(self):
        ids = set()
        for case in load()["evals"]:
            self.assertNotIn(case["id"], ids)
            ids.add(case["id"])
            for key in ("prompt", "expected_output", "assertions", "should_trigger"):
                self.assertIn(key, case, case["id"])
            self.assertTrue(case["prompt"].strip())
            self.assertGreaterEqual(len(case["assertions"]), 2, case["id"])
            for a in case["assertions"]:
                self.assertIn(a["kind"], ("humain", "verifier"), case["id"])

    def test_referenced_files_exist(self):
        for case in load()["evals"]:
            for key in ("input_file", "reference_output"):
                if key in case:
                    self.assertTrue(os.path.isfile(os.path.join(EVALS_DIR, case[key])), case[key])
            if "flawed_output" in case:
                path = os.path.normpath(os.path.join(EVALS_DIR, case["flawed_output"]["file"]))
                self.assertTrue(os.path.isfile(path), path)

    def test_no_real_email_address_in_evals(self):
        pattern = re.compile(r"[\w.+-]+@(?!example\.)[\w-]+\.[a-z]{2,}", re.I)
        for name in os.listdir(EVALS_DIR):
            if os.path.isfile(os.path.join(EVALS_DIR, name)):
                self.assertIsNone(pattern.search(read(name)), name)
        for name in os.listdir(os.path.join(EVALS_DIR, "fixtures")):
            self.assertIsNone(pattern.search(read(os.path.join("fixtures", name))), name)


class ReferenceOutputs(unittest.TestCase):
    def test_reference_outputs_pass_the_verifier(self):
        for case in load()["evals"]:
            if "reference_output" not in case:
                continue
            findings = verifier.verify(read(case["reference_output"]))
            checks = [a for a in case["assertions"] if a["kind"] == "verifier"]
            self.assertTrue(checks, case["id"])
            for check in checks:
                limit = ORDER[check["max_priority_allowed"]]
                allowed = set(check["allowed_rules"])
                for f in findings:
                    if f.rule in allowed:
                        continue
                    self.assertGreater(
                        ORDER[f.priority], limit,
                        "%s : %s %s" % (case["id"], f.priority, f.rule),
                    )

    def test_reference_outputs_have_no_p0(self):
        for case in load()["evals"]:
            if "reference_output" in case:
                findings = verifier.verify(read(case["reference_output"]))
                self.assertFalse([f for f in findings if f.priority == "P0"], case["id"])


class FlawedOutputs(unittest.TestCase):
    def test_flawed_outputs_trigger_expected_rules(self):
        for case in load()["evals"]:
            flawed = case.get("flawed_output")
            if not flawed:
                continue
            found = {f.rule for f in verifier.verify(read(flawed["file"]))}
            for rule in flawed["expected_rules"]:
                self.assertIn(rule, found, "%s : %s" % (case["id"], rule))


if __name__ == "__main__":
    unittest.main()
