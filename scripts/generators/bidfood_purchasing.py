"""
Generator for all 80 Bidfood Purchasing modules (20 A2, 20 B1, 20 B2, 20 C1).
Dedicated to Libor Barvenčík and Lucie Rončková.
Covers cold-chain wholesale food procurement, supplier negotiations, Incoterms, and quality specs.
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from curriculum_catalog import get_bidfood_purchasing_curriculum
from generators.common import make_q, build_test_module, KEY_PATTERN
from generators.diverse_question_engine import generate_module_questions

def generate_bidfood_purchasing_modules():
    curriculum = get_bidfood_purchasing_curriculum()
    all_modules = {}

    for mod in curriculum:
        tid = mod["test_id"]
        questions = generate_module_questions(mod, "bidfood_pur")
        test_obj = build_test_module(
            test_id=tid,
            title=mod["title"],
            level=mod["level"],
            category=mod["category"],
            track=mod["workplace_track"],
            est_time=mod["estimated_time_minutes"],
            description=mod["description"],
            objectives=[
                f"Master professional {mod['grammar_focus']} in wholesale food procurement",
                f"Eliminate common Czech interference errors in {mod['title'].lower()}",
                "Demonstrate precision in international commercial negotiations and food safety documentation"
            ],
            questions=questions
        )
        all_modules[tid] = test_obj

    return all_modules

if __name__ == "__main__":
    mods = generate_bidfood_purchasing_modules()
    print(f"Generated {len(mods)} Bidfood Purchasing modules.")
