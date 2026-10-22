"""
Generator for all 80 Tapi IT modules (20 A2, 20 B1, 20 B2, 20 C1).
Overhauls repetitive questions, guarantees 0 duplicate prompts, and generates rich enterprise IT/cybersecurity content.
"""

import sys
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from curriculum_catalog import get_tapi_it_curriculum
from generators.common import make_q, build_test_module, KEY_PATTERN
from generators.diverse_question_engine import generate_module_questions

EXISTING_TESTS_DIR = ROOT / "tapi-it" / "data" / "tests"

def generate_tapi_it_modules():
    curriculum = get_tapi_it_curriculum()
    all_modules = {}

    for mod in curriculum:
        tid = mod["test_id"]
        disk_file = EXISTING_TESTS_DIR / f"{tid}.json"
        
        needs_regeneration = True
        
        if disk_file.exists():
            try:
                with open(disk_file, "r", encoding="utf-8") as f:
                    test_data = json.load(f)
                qs = test_data.get("questions", [])
                prompts = [q["prompt"] for q in qs]
                prompt_counts = Counter(prompts)
                if len(qs) == 10 and max(prompt_counts.values()) == 1:
                    needs_regeneration = False
                    test_data["title"] = mod["title"]
                    test_data["workplace_track"] = mod["workplace_track"]
                    test_data["level"] = mod["level"]
                    test_data["category"] = mod["category"]
                    all_modules[tid] = test_data
            except Exception:
                needs_regeneration = True

        if needs_regeneration:
            questions = generate_module_questions(mod, "tapi_it")
            test_obj = build_test_module(
                test_id=tid,
                title=mod["title"],
                level=mod["level"],
                category=mod["category"],
                track=mod["workplace_track"],
                est_time=mod["estimated_time_minutes"],
                description=mod["description"],
                objectives=[
                    f"Master professional {mod['grammar_focus']} in corporate IT and cloud systems",
                    f"Eliminate common Czech interference errors in {mod['title'].lower()}",
                    "Demonstrate precision in ITIL documentation, cybersecurity policies, and incident reports"
                ],
                questions=questions
            )
            all_modules[tid] = test_obj

    return all_modules

if __name__ == "__main__":
    mods = generate_tapi_it_modules()
    print(f"Generated {len(mods)} Tapi IT modules.")
