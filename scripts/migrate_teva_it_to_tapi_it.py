#!/usr/bin/env python3
"""
Migration script: Convert TEVA IT suite to TAPI IT and remove all Teva references.
"""

import os
import sys
import re
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def migrate_tapi_it_files():
    suite_dir = ROOT / "tapi-it"
    print(f"Migrating files in {suite_dir}...")
    
    # 1. Rename test JSON files
    tests_dir = suite_dir / "data" / "tests"
    for test_file in list(tests_dir.glob("TEV-IT-*.json")):
        new_name = test_file.name.replace("TEV-IT-", "TAPI-IT-")
        new_path = tests_dir / new_name
        test_file.rename(new_path)
    print("  [OK] Renamed test JSON files to TAPI-IT-*.json")
    
    # 2. Update content inside all test JSON files
    for test_file in tests_dir.glob("*.json"):
        text = test_file.read_text(encoding="utf-8")
        text = text.replace("TEV-IT-", "TAPI-IT-")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("Teva Pharmaceuticals", "TAPI")
        text = text.replace("Teva IT", "Tapi IT")
        text = text.replace("TEVA IT", "TAPI IT")
        text = text.replace("Teva Global IT", "Tapi Global IT")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        test_file.write_text(text, encoding="utf-8")
    print("  [OK] Cleaned and updated all test JSON files")

    # 3. Update schema
    schema_file = suite_dir / "schema" / "test_schema.json"
    if schema_file.exists():
        text = schema_file.read_text(encoding="utf-8")
        text = text.replace("TEV-IT", "TAPI-IT")
        text = text.replace("Teva IT", "Tapi IT")
        schema_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated test_schema.json")

    # 4. Update index.html
    index_file = suite_dir / "index.html"
    if index_file.exists():
        text = index_file.read_text(encoding="utf-8")
        text = text.replace("Teva IT", "Tapi IT")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("TEVA IT", "TAPI IT")
        text = text.replace("Teva Global IT", "Tapi Global IT")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        text = text.replace("teva_it_test_", "tapi_it_test_")
        index_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated tapi-it/index.html")

    # 5. Update test_runner.html
    runner_file = suite_dir / "test_runner.html"
    if runner_file.exists():
        text = runner_file.read_text(encoding="utf-8")
        text = text.replace("Teva IT", "Tapi IT")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("TEVA IT", "TAPI IT")
        text = text.replace("TEV-IT-", "TAPI-IT-")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        runner_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated tapi-it/test_runner.html")

    # 6. Update engine/app.js
    app_file = suite_dir / "engine" / "app.js"
    if app_file.exists():
        text = app_file.read_text(encoding="utf-8")
        text = text.replace("Teva IT", "Tapi IT")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("TEVA IT", "TAPI IT")
        text = text.replace("Teva Global IT", "Tapi Global IT")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        text = text.replace("teva_it_test_", "tapi_it_test_")
        app_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated engine/app.js")

    # 7. Update styles.css, README.md, CURRICULUM_ROADMAP.md, Launch_Suite.bat
    for other_f in [suite_dir / "engine" / "styles.css", suite_dir / "README.md", suite_dir / "CURRICULUM_ROADMAP.md", suite_dir / "Launch_Suite.bat"]:
        if other_f.exists():
            text = other_f.read_text(encoding="utf-8")
            text = text.replace("TEV-IT", "TAPI-IT")
            text = text.replace("Teva IT", "Tapi IT")
            text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
            text = text.replace("Teva Global IT", "Tapi Global IT")
            text = text.replace("Teva", "Tapi")
            text = text.replace("TEVA", "TAPI")
            other_f.write_text(text, encoding="utf-8")
            print(f"  [OK] Updated {other_f.name}")

    # 8. Update scripts/validate_tests.py inside suite
    val_file = suite_dir / "scripts" / "validate_tests.py"
    if val_file.exists():
        text = val_file.read_text(encoding="utf-8")
        text = text.replace("Teva IT", "Tapi IT")
        text = text.replace("teva-it", "tapi-it")
        val_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated suite validate_tests.py")

def update_curriculum_catalog():
    p = ROOT / "scripts" / "curriculum_catalog.py"
    print(f"Updating {p}...")
    text = p.read_text(encoding="utf-8")
    
    text = text.replace("def get_teva_it_curriculum():", "def get_tapi_it_curriculum():")
    text = text.replace("f\"TEV-IT-", "f\"TAPI-IT-")
    text = text.replace("TEV-IT-", "TAPI-IT-")
    text = text.replace("\"teva-it\": get_teva_it_curriculum", "\"tapi-it\": get_tapi_it_curriculum,\n    \"teva-it\": get_tapi_it_curriculum")
    
    # Also add backward alias
    if "get_teva_it_curriculum = get_tapi_it_curriculum" not in text:
        text += "\n# Backward compatibility alias\nget_teva_it_curriculum = get_tapi_it_curriculum\n"
        
    p.write_text(text, encoding="utf-8")
    print("  [OK] Updated curriculum_catalog.py")

def update_generators():
    old_gen = ROOT / "scripts" / "generators" / "teva_it.py"
    new_gen = ROOT / "scripts" / "generators" / "tapi_it.py"
    
    text = old_gen.read_text(encoding="utf-8")
    if "Forwarding wrapper" in text:
        return
        
    text = text.replace("Teva IT", "Tapi IT")
    text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
    text = text.replace("Teva Global IT", "Tapi Global IT")
    text = text.replace("Teva", "Tapi")
    text = text.replace("TEVA", "TAPI")
    text = text.replace("teva-it", "tapi-it")
    text = text.replace("TEV-IT", "TAPI-IT")
    text = text.replace("generate_teva_it_modules", "generate_tapi_it_modules")
    text = text.replace("get_teva_it_curriculum", "get_tapi_it_curriculum")
    
    new_gen.write_text(text, encoding="utf-8")
    print("  [OK] Created scripts/generators/tapi_it.py")
    
    # Make teva_it.py import and forward
    old_gen.write_text("""# Forwarding wrapper for backward compatibility
from generators.tapi_it import generate_tapi_it_modules as generate_teva_it_modules
from generators.tapi_it import *
""", encoding="utf-8")
    print("  [OK] Updated teva_it.py as wrapper")

def update_master_index():
    p = ROOT / "index.html"
    print(f"Updating Master Hub {p}...")
    text = p.read_text(encoding="utf-8")
    
    # Update Card 6
    old_card_snippet = """<!-- 6: Teva IT -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #4338ca;"></div>
        <div>
          <span class="suite-badge" style="background: #ede9fe; color: #5b21b6;">💻 Cloud, DevOps & Security</span>
          <h2 class="suite-title">Teva IT</h2>
          <div class="suite-company">TEVA PHARMACEUTICALS | Global Digital & IT</div>"""
          
    new_card_snippet = """<!-- 6: Tapi IT -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #4338ca;"></div>
        <div>
          <span class="suite-badge" style="background: #ede9fe; color: #5b21b6;">💻 Cloud, DevOps & Security</span>
          <h2 class="suite-title">Tapi IT</h2>
          <div class="suite-company">TAPI | Global Digital & IT</div>"""
          
    text = text.replace(old_card_snippet, new_card_snippet)
    text = text.replace(
        '<a href="teva-it/index.html" class="suite-launch-btn" style="background: #4338ca;">Launch Teva IT Portal →</a>',
        '<a href="tapi-it/index.html" class="suite-launch-btn" style="background: #4338ca;">Launch Tapi IT Portal →</a>'
    )
    text = text.replace(
        "copySuiteLink('teva-it/index.html', 'Teva IT')",
        "copySuiteLink('tapi-it/index.html', 'Tapi IT')"
    )
    
    p.write_text(text, encoding="utf-8")
    print("  [OK] Updated Master Hub index.html")

def update_deploy_and_packaging_scripts():
    # deploy_400_modules.py
    dep_file = ROOT / "scripts" / "deploy_400_modules.py"
    text = dep_file.read_text(encoding="utf-8")
    text = text.replace("from generators.teva_it import generate_teva_it_modules", "from generators.tapi_it import generate_tapi_it_modules")
    text = text.replace('"teva-it": generate_teva_it_modules', '"tapi-it": generate_tapi_it_modules')
    dep_file.write_text(text, encoding="utf-8")
    print("  [OK] Updated scripts/deploy_400_modules.py")
    
    # package_for_distribution.py
    pkg_file = ROOT / "scripts" / "package_for_distribution.py"
    text = pkg_file.read_text(encoding="utf-8")
    text = text.replace('("teva-it", "Teva_IT_Suite")', '("tapi-it", "Tapi_IT_Suite")')
    text = text.replace('5. Teva IT (Cloud infrastructure, DevOps, Zero Trust cybersecurity, SAP/LIMS)', '5. Tapi IT (Cloud infrastructure, DevOps, Zero Trust cybersecurity, SAP/LIMS)')
    pkg_file.write_text(text, encoding="utf-8")
    print("  [OK] Updated scripts/package_for_distribution.py")

    # test_validator_quick.py
    val_file = ROOT / "scripts" / "test_validator_quick.py"
    text = val_file.read_text(encoding="utf-8")
    text = text.replace("from generators.teva_it import generate_teva_it_modules", "from generators.tapi_it import generate_tapi_it_modules")
    text = text.replace('validate_suite_modules("teva-it"', 'validate_suite_modules("tapi-it"')
    val_file.write_text(text, encoding="utf-8")
    print("  [OK] Updated scripts/test_validator_quick.py")

def update_firebase_config():
    p = ROOT / "firebase.json"
    with open(p, "r", encoding="utf-8") as f:
        conf = json.load(f)
    
    redirects = conf.get("hosting", {}).get("redirects", [])
    has_redirect = any(r.get("source") == "/teva-it/:path*" for r in redirects)
    if not has_redirect:
        redirects.append({
            "source": "/teva-it/:path*",
            "destination": "/tapi-it/:path*",
            "type": 301
        })
        redirects.append({
            "source": "/teva-it",
            "destination": "/tapi-it/",
            "type": 301
        })
    conf["hosting"]["redirects"] = redirects
    
    with open(p, "w", encoding="utf-8") as f:
        json.dump(conf, f, indent=2)
    print("  [OK] Updated firebase.json with 301 redirect")

def rebuild_and_validate():
    print("\nRebuilding manifests and registries for tapi-it...")
    from curriculum_catalog import get_tapi_it_curriculum
    from generators.tapi_it import generate_tapi_it_modules
    
    suite_dir = ROOT / "tapi-it"
    curriculum = get_tapi_it_curriculum()
    modules = generate_tapi_it_modules()
    
    # Write curriculum_manifest.json
    with open(suite_dir / "data" / "curriculum_manifest.json", "w", encoding="utf-8") as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
        
    # Write manifest.js
    with open(suite_dir / "data" / "manifest.js", "w", encoding="utf-8") as f:
        f.write("window.CURRICULUM_MANIFEST = " + json.dumps(curriculum, indent=2, ensure_ascii=False) + ";\n")
        
    # Write tests_registry.js
    with open(suite_dir / "data" / "tests_registry.js", "w", encoding="utf-8") as f:
        f.write("window.TEST_REGISTRY = window.TEST_REGISTRY || {};\n")
        f.write("Object.assign(window.TEST_REGISTRY, " + json.dumps(modules, indent=2, ensure_ascii=False) + ");\n")
        
    print(f"  [OK] Wrote manifest.js and tests_registry.js ({len(modules)} tests)")
    
    # Run validation
    val_script = suite_dir / "scripts" / "validate_tests.py"
    res = subprocess.run([sys.executable, str(val_script)], capture_output=True, text=True)
    print(res.stdout.strip())
    if res.returncode != 0:
        print("ERROR:", res.stderr.strip())
        sys.exit(1)
    print("  [OK] Validation passed 100%!")

def main():
    print("=" * 60)
    print("STARTING MIGRATION: TEVA IT -> TAPI IT")
    print("=" * 60)
    
    migrate_tapi_it_files()
    update_curriculum_catalog()
    update_generators()
    update_master_index()
    update_deploy_and_packaging_scripts()
    update_firebase_config()
    rebuild_and_validate()
    
    print("\n" + "=" * 60)
    print("MIGRATION COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
