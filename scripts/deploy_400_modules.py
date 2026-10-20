#!/usr/bin/env python3
"""
Master Deployer for 400 Modules Across 5 Corporate Suites.
Deploys:
- 80 modules per suite (20 A2, 20 B1, 20 B2, 20 C2) x 5 suites = 400 JSON files
- data/curriculum_manifest.json in each suite
- data/manifest.js in each suite (offline execution)
- data/tests_registry.js in each suite (zero-server execution)
- Validates all 400 files
- Rebuilds distribution ZIP packages
"""

import sys
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generators.tatra_eng import generate_tatra_eng_modules
from generators.tatra_sales import generate_tatra_sales_modules
from generators.tapi_eng import generate_tapi_eng_modules
from generators.tapi_chem import generate_tapi_chem_modules
from generators.tapi_it import generate_tapi_it_modules
from curriculum_catalog import ALL_CURRICULA

SUITE_GENERATORS = {
    "tatra-engineering": generate_tatra_eng_modules,
    "tatra-sales-engineering": generate_tatra_sales_modules,
    "tapi-engineering": generate_tapi_eng_modules,
    "tapi-chemistry": generate_tapi_chem_modules,
    "tapi-it": generate_tapi_it_modules
}

def deploy_suite(suite_name, gen_func):
    suite_dir = ROOT / suite_name
    tests_dir = suite_dir / "data" / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n--- Deploying {suite_name} (80 modules) ---")
    modules = gen_func()
    curriculum = ALL_CURRICULA[suite_name]()

    # 1. Write each test JSON file
    for tid, test_obj in modules.items():
        t_path = tests_dir / f"{tid}.json"
        with open(t_path, "w", encoding="utf-8") as f:
            json.dump(test_obj, f, indent=2, ensure_ascii=False)

    print(f"  [OK] Wrote {len(modules)} test JSON files to {tests_dir}")

    # 2. Write curriculum_manifest.json
    manifest_path = suite_dir / "data" / "curriculum_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Wrote {len(curriculum)} entries to curriculum_manifest.json")

    # 3. Write manifest.js for offline portal loading
    manifest_js_path = suite_dir / "data" / "manifest.js"
    with open(manifest_js_path, "w", encoding="utf-8") as f:
        f.write("window.CURRICULUM_MANIFEST = " + json.dumps(curriculum, indent=2, ensure_ascii=False) + ";\n")
    print(f"  [OK] Wrote manifest.js")

    # 4. Write tests_registry.js for offline runner loading
    reg_js_path = suite_dir / "data" / "tests_registry.js"
    with open(reg_js_path, "w", encoding="utf-8") as f:
        f.write("window.TEST_REGISTRY = window.TEST_REGISTRY || {};\n")
        f.write("Object.assign(window.TEST_REGISTRY, " + json.dumps(modules, indent=2, ensure_ascii=False) + ");\n")
    print(f"  [OK] Wrote tests_registry.js ({len(modules)} tests bundled)")

def main():
    print("=" * 60)
    print("STARTING MASTER DEPLOYMENT OF 400 INTERACTIVE MODULES")
    print("=" * 60)

    for s_name, g_func in SUITE_GENERATORS.items():
        deploy_suite(s_name, g_func)

    print("\n" + "=" * 60)
    print("RUNNING DISK VALIDATORS ACROSS ALL 5 SUITES...")
    print("=" * 60)

    all_passed = True
    for s_name in SUITE_GENERATORS.keys():
        validator_script = ROOT / s_name / "scripts" / "validate_tests.py"
        res = subprocess.run([sys.executable, str(validator_script)], capture_output=True, text=True)
        print(f"\n[{s_name}]")
        print(res.stdout.strip())
        if res.returncode != 0:
            print("FAILED:", res.stderr.strip())
            all_passed = False

    if not all_passed:
        print("\nERROR: One or more suites failed validation.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("ALL 400 TEST MODULES (80 PER SUITE) VALIDATED SUCCESSFULLY!")
    print("REPACKAGING DISTRIBUTION ZIPS...")
    print("=" * 60)

    pkg_script = ROOT / "scripts" / "package_for_distribution.py"
    subprocess.run([sys.executable, str(pkg_script)], check=True)
    print("\nMASTER DEPLOYMENT COMPLETE!")

if __name__ == "__main__":
    main()
