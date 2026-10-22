import sys, json
from pathlib import Path
from collections import Counter
import jsonschema

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

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
        
        prompts = [q["prompt"] for q in qs]
        p_counts = Counter(prompts)
        if max(p_counts.values()) > 1:
            print(f"[{tid}] Duplicate prompt error: {max(p_counts.values())} identical prompts")
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

    print(f"[{suite_dir:26}] Validated {len(modules)} modules: {errors} errors found.")
    return errors == 0

if __name__ == "__main__":
    from generators.tatra_eng import generate_tatra_eng_modules
    from generators.tatra_sales import generate_tatra_sales_modules
    from generators.tapi_eng import generate_tapi_eng_modules
    from generators.tapi_chem import generate_tapi_chem_modules
    from generators.tapi_it import generate_tapi_it_modules
    from generators.bidfood_purchasing import generate_bidfood_purchasing_modules
    from generators.bidfood_engineering import generate_bidfood_engineering_modules

    ok1 = validate_suite_modules("tatra-engineering", generate_tatra_eng_modules)
    ok2 = validate_suite_modules("tatra-sales-engineering", generate_tatra_sales_modules)
    ok3 = validate_suite_modules("tapi-engineering", generate_tapi_eng_modules)
    ok4 = validate_suite_modules("tapi-chemistry", generate_tapi_chem_modules)
    ok5 = validate_suite_modules("tapi-it", generate_tapi_it_modules)
    ok6 = validate_suite_modules("bidfood-purchasing-libor", generate_bidfood_purchasing_modules)
    ok7 = validate_suite_modules("bidfood-purchasing-lucie", generate_bidfood_purchasing_modules)
    ok8 = validate_suite_modules("bidfood-engineering-jiri", generate_bidfood_engineering_modules)

    all_passed = ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8
    print("\n" + "=" * 50)
    print("ALL SUITES VALIDATED:", all_passed)
    print("=" * 50)
    if not all_passed:
        sys.exit(1)
