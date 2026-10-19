#!/usr/bin/env python3
"""
Rebalance answer options across A, B, C, D in test JSON files.
Eliminates option position bias (e.g., all answers being 'A').
"""

import json
import random
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent.parent / "data" / "tests"

# Deterministic seed for reproducible balanced distribution
SEED = 42

def rebalance_question(q, target_key):
    old_correct_key = q["correct_key"]
    old_options = q["options"]
    old_explanations = q["explanations"]

    # Identify correct option and distractors
    correct_opt = None
    distractors = []
    
    for opt in old_options:
        key = opt["key"]
        text = opt["text"]
        if key == old_correct_key:
            correct_opt = {"text": text, "old_key": key}
        else:
            distractor_exp = old_explanations.get(f"wrong_{key}", "")
            distractors.append({"text": text, "old_key": key, "explanation": distractor_exp})

    if not correct_opt:
        return q

    # Build new ordered options list with correct_opt at target_key
    keys = ["A", "B", "C", "D"][:len(old_options)]
    if target_key not in keys:
        target_key = keys[0]

    distractor_keys = [k for k in keys if k != target_key]
    
    new_options = []
    new_explanations = {
        "correct": old_explanations.get("correct", "")
    }

    d_idx = 0
    for k in keys:
        if k == target_key:
            new_options.append({"key": k, "text": correct_opt["text"]})
        else:
            d = distractors[d_idx]
            new_options.append({"key": k, "text": d["text"]})
            new_explanations[f"wrong_{k}"] = d["explanation"]
            d_idx += 1

    q["options"] = new_options
    q["correct_key"] = target_key
    q["explanations"] = new_explanations
    return q

def rebalance_test_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = data.get("questions", [])
    # Cycle through balanced keys: B, C, A, D, C, A, D, B, A, C...
    cycle = ["B", "C", "A", "D", "C", "B", "D", "A", "B", "D", "C", "A"]
    
    for i, q in enumerate(questions):
        target = cycle[i % len(cycle)]
        rebalance_question(q, target)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Rebalanced {file_path.name}: keys distributed across A, B, C, D.")

def main():
    test_files = sorted(list(TESTS_DIR.glob("*.json")))
    for tf in test_files:
        rebalance_test_file(tf)
    print(f"\nSuccessfully rebalanced all {len(test_files)} test files.")

if __name__ == "__main__":
    main()
