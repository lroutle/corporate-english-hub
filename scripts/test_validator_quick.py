import sys, json
from pathlib import Path
from collections import Counter
import jsonschema

sys.path.insert(0, "scripts")

def validate_suite_modules(suite_dir, gen_func):
    schema_path = Path(suite_dir) / "schema" / "test_schema.json"
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)

    modules = gen_func()
    v = jsonschema.Draft7Validator(schema)
    errors = 0

    for tid, m in modules.items():
        for err in v.iter_errors(m):
            print(f"[{tid}] Schema error: {err.message}")
            errors += 1
        
        qs = m["questions"]
        if len(qs) != 10:
            print(f"[{tid}] Question count error: {len(qs)}")
            errors += 1
        
        keys = [q["correct_key"] for q in qs]
        counts = Counter(keys)
        if max(counts.values()) > 5:
            print(f"[{tid}] Bias error: {counts}")
            errors += 1
        
        for q in qs:
            k = q["correct_key"]
            exp = q["explanations"]
            if "correct" not in exp:
                print(f"[{q['id']}] Missing correct exp")
                errors += 1
            for ok in ["A", "B", "C", "D"]:
                if ok != k and f"wrong_{ok}" not in exp:
                    print(f"[{q['id']}] Missing wrong_{ok}")
                    errors += 1

    print(f"[{suite_dir}] Validated {len(modules)} modules: {errors} errors found.")
    return errors == 0

if __name__ == "__main__":
    from generators.tatra_eng import generate_tatra_eng_modules
    from generators.tatra_sales import generate_tatra_sales_modules
    from generators.tapi_eng import generate_tapi_eng_modules
    from generators.tapi_chem import generate_tapi_chem_modules
    from generators.teva_it import generate_teva_it_modules

    ok1 = validate_suite_modules("tatra-engineering", generate_tatra_eng_modules)
    ok2 = validate_suite_modules("tatra-sales-engineering", generate_tatra_sales_modules)
    ok3 = validate_suite_modules("tapi-engineering", generate_tapi_eng_modules)
    ok4 = validate_suite_modules("tapi-chemistry", generate_tapi_chem_modules)
    ok5 = validate_suite_modules("teva-it", generate_teva_it_modules)

    all_passed = ok1 and ok2 and ok3 and ok4 and ok5
    print("\n" + "=" * 50)
    print("ALL 5 SUITES (400 MODULES) VALIDATED:", all_passed)
    print("=" * 50)
