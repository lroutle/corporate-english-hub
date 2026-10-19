#!/usr/bin/env python3
"""
Tatra Trucks Interactive English Testing Suite - Test Validator
Validates test JSON files against schema/test_schema.json and checks pedagogical integrity.
"""

import os
import sys
import json
import re
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Warning: jsonschema library not found. Run 'pip install jsonschema'.")
    jsonschema = None

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "test_schema.json"
TESTS_DIR = Path(__file__).resolve().parent.parent / "data" / "tests"

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_test_data(data, schema, filename="<input>"):
    errors = []
    
    # 1. JSON Schema validation
    if jsonschema:
        validator = jsonschema.Draft7Validator(schema)
        for err in validator.iter_errors(data):
            path = ".".join(str(p) for p in err.path)
            errors.append(f"Schema violation at '{path}': {err.message}")

    # 2. Semantic and Pedagogical Integrity checks
    test_id = data.get("test_id", "")
    questions = data.get("questions", [])

    if len(questions) < 8 or len(questions) > 12:
        errors.append(f"Expected 8-12 questions, found {len(questions)}")

    for i, q in enumerate(questions):
        qid = q.get("id", f"Q{i+1}")
        
        # ID prefix check
        if not qid.startswith(test_id):
            errors.append(f"Question ID '{qid}' does not start with test_id '{test_id}'")

        # Options keys
        options = q.get("options", [])
        opt_keys = [o.get("key") for o in options]
        correct_key = q.get("correct_key")

        if correct_key not in opt_keys:
            errors.append(f"[{qid}] correct_key '{correct_key}' not found in options: {opt_keys}")

        # Unique keys
        if len(opt_keys) != len(set(opt_keys)):
            errors.append(f"[{qid}] Duplicate option keys found: {opt_keys}")

        # Explanation coverage
        explanations = q.get("explanations", {})
        if "correct" not in explanations or not explanations["correct"].strip():
            errors.append(f"[{qid}] Missing or empty 'correct' explanation")

        for key in opt_keys:
            if key != correct_key:
                wrong_field = f"wrong_{key}"
                if wrong_field not in explanations or not explanations[wrong_field].strip():
                    errors.append(f"[{qid}] Missing or empty explanation for incorrect option '{wrong_field}'")

        # Czech learning point check
        cz_pt = q.get("cz_learning_point", "")
        if not cz_pt or len(cz_pt.strip()) < 10:
            errors.append(f"[{qid}] Missing or insufficient cz_learning_point")

    return errors

def validate_file(file_path, schema):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"Could not parse JSON in {file_path.name}: {e}"]

    return validate_test_data(data, schema, filename=file_path.name)

def main():
    schema = load_schema()
    target_files = []

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            p = Path(arg)
            if p.is_file():
                target_files.append(p)
            elif p.is_dir():
                target_files.extend(list(p.glob("*.json")))
    else:
        if TESTS_DIR.exists():
            target_files = sorted(list(TESTS_DIR.glob("*.json")))

    if not target_files:
        print(f"No test JSON files found in {TESTS_DIR}.")
        sys.exit(0)

    total = len(target_files)
    passed = 0
    failed = 0

    print(f"Validating {total} test file(s) against {SCHEMA_PATH.name}...")
    for f in target_files:
        errs = validate_file(f, schema)
        if not errs:
            print(f"  [PASS] {f.name}")
            passed += 1
        else:
            print(f"  [FAIL] {f.name} ({len(errs)} error(s)):")
            for e in errs:
                print(f"    - {e}")
            failed += 1

    print("\n" + "=" * 50)
    print(f"Validation Summary: {passed}/{total} Passed, {failed} Failed.")
    print("=" * 50)

    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
