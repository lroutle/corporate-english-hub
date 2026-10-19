#!/usr/bin/env python3
"""
Populates all missing test modules across all 5 suites:
Total: 45 modules (9 modules per suite x 5 suites)
Strictly adheres to Draft-7 schema and anti-bias key balancing.
"""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent

# Balanced key distribution pattern for 10 questions: 2 A, 3 B, 3 C, 2 D
KEY_PATTERN = ["B", "C", "A", "D", "C", "B", "D", "A", "C", "B"]

def create_q(qid, prompt, options_dict, correct_key, explanations, cz_note, track):
    options = [{"key": k, "text": options_dict[k]} for k in ["A", "B", "C", "D"]]
    return {
        "id": qid,
        "prompt": prompt,
        "options": options,
        "correct_key": correct_key,
        "explanations": explanations,
        "cz_learning_point": cz_note,
        "workplace_track": track
    }

def rebalance_existing_test(source_path, target_id, target_title=None, target_track=None):
    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["test_id"] = target_id
    if target_title: data["title"] = target_title
    if target_track: data["workplace_track"] = target_track

    # Take first 10 questions (or all if 8-12)
    questions = data.get("questions", [])[:10]
    for idx, q in enumerate(questions):
        q["id"] = f"{target_id}-Q{idx+1}"
        if target_track: q["workplace_track"] = target_track
        target_k = KEY_PATTERN[idx % len(KEY_PATTERN)]
        curr_k = q.get("correct_key")

        # Map current options
        opts_by_key = {o["key"]: o["text"] for o in q.get("options", [])}
        correct_text = opts_by_key.get(curr_k)

        # Distractor texts
        distractors = [opts_by_key[k] for k in ["A", "B", "C", "D"] if k != curr_k and k in opts_by_key]

        # Old explanations
        old_exp = q.get("explanations", {})
        correct_exp = old_exp.get("correct", "Correct answer.")
        distractor_exps = [old_exp.get(f"wrong_{k}", "Incorrect option.") for k in ["A", "B", "C", "D"] if k != curr_k]

        # Reassign so target_k gets correct_text
        new_opts = {}
        new_exp = {"correct": correct_exp}
        keys_other = [k for k in ["A", "B", "C", "D"] if k != target_k]

        new_opts[target_k] = correct_text
        for i, ok in enumerate(keys_other):
            new_opts[ok] = distractors[i % len(distractors)]
            new_exp[f"wrong_{ok}"] = distractor_exps[i % len(distractor_exps)]

        q["options"] = [{"key": k, "text": new_opts[k]} for k in ["A", "B", "C", "D"]]
        q["correct_key"] = target_k
        q["explanations"] = new_exp

    data["questions"] = questions
    return data

print("Helper functions defined.")
