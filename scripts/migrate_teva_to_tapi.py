#!/usr/bin/env python3
"""
Migration script: Convert TEVA Engineering suite to TAPI Engineering and remove all Teva references.
"""

import os
import sys
import re
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def migrate_tapi_engineering_files():
    suite_dir = ROOT / "tapi-engineering"
    print(f"Migrating files in {suite_dir}...")
    
    # 1. Rename test JSON files
    tests_dir = suite_dir / "data" / "tests"
    for test_file in list(tests_dir.glob("TEV-ENG-*.json")):
        new_name = test_file.name.replace("TEV-ENG-", "TAPI-ENG-")
        new_path = tests_dir / new_name
        test_file.rename(new_path)
    print("  [OK] Renamed test JSON files to TAPI-ENG-*.json")
    
    # 2. Update content inside all test JSON files
    for test_file in tests_dir.glob("*.json"):
        text = test_file.read_text(encoding="utf-8")
        text = text.replace("TEV-ENG-", "TAPI-ENG-")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("Teva Pharmaceuticals", "TAPI")
        text = text.replace("Teva Engineering", "Tapi Engineering")
        text = text.replace("TEVA ENG", "TAPI ENG")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        test_file.write_text(text, encoding="utf-8")
    print("  [OK] Cleaned and updated all test JSON files")

    # 3. Update schema
    schema_file = suite_dir / "schema" / "test_schema.json"
    if schema_file.exists():
        text = schema_file.read_text(encoding="utf-8")
        text = text.replace("TEV-ENG", "TAPI-ENG")
        text = text.replace("Teva Engineering", "Tapi Engineering")
        schema_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated test_schema.json")

    # 4. Update index.html
    index_file = suite_dir / "index.html"
    if index_file.exists():
        text = index_file.read_text(encoding="utf-8")
        text = text.replace("Teva Engineering", "Tapi Engineering")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("TEVA ENG", "TAPI ENG")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        text = text.replace("teva_eng_test_", "tapi_eng_test_")
        index_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated tapi-engineering/index.html")

    # 5. Update engine/app.js
    app_file = suite_dir / "engine" / "app.js"
    if app_file.exists():
        text = app_file.read_text(encoding="utf-8")
        text = text.replace("Teva Engineering", "Tapi Engineering")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("TEVA ENG", "TAPI ENG")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        text = text.replace("teva_eng_test_", "tapi_eng_test_")
        app_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated engine/app.js")

    # 6. Update CURRICULUM_ROADMAP.md
    roadmap_file = suite_dir / "CURRICULUM_ROADMAP.md"
    if roadmap_file.exists():
        text = roadmap_file.read_text(encoding="utf-8")
        text = text.replace("TEV-ENG", "TAPI-ENG")
        text = text.replace("Teva Engineering", "Tapi Engineering")
        text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
        text = text.replace("Teva", "Tapi")
        text = text.replace("TEVA", "TAPI")
        roadmap_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated CURRICULUM_ROADMAP.md")

    # 7. Update scripts/validate_tests.py inside suite
    val_file = suite_dir / "scripts" / "validate_tests.py"
    if val_file.exists():
        text = val_file.read_text(encoding="utf-8")
        text = text.replace("Teva Engineering", "Tapi Engineering")
        text = text.replace("teva-engineering", "tapi-engineering")
        val_file.write_text(text, encoding="utf-8")
        print("  [OK] Updated suite validate_tests.py")

def update_curriculum_catalog():
    p = ROOT / "scripts" / "curriculum_catalog.py"
    print(f"Updating {p}...")
    text = p.read_text(encoding="utf-8")
    
    text = text.replace("def get_teva_eng_curriculum():", "def get_tapi_eng_curriculum():")
    text = text.replace("f\"TEV-ENG-", "f\"TAPI-ENG-")
    text = text.replace("TEV-ENG-", "TAPI-ENG-")
    text = text.replace("\"teva-engineering\": get_teva_eng_curriculum,", "\"tapi-engineering\": get_tapi_eng_curriculum,\n    \"teva-engineering\": get_tapi_eng_curriculum,")
    
    # Also add backward alias
    if "get_teva_eng_curriculum = get_tapi_eng_curriculum" not in text:
        text += "\n# Backward compatibility alias\nget_teva_eng_curriculum = get_tapi_eng_curriculum\n"
        
    p.write_text(text, encoding="utf-8")
    print("  [OK] Updated curriculum_catalog.py")

def update_generators():
    old_gen = ROOT / "scripts" / "generators" / "teva_eng.py"
    new_gen = ROOT / "scripts" / "generators" / "tapi_eng.py"
    
    text = old_gen.read_text(encoding="utf-8")
    if "Forwarding wrapper" in text:
        return
    text = text.replace("Teva Engineering", "Tapi Engineering")
    text = text.replace("TEVA PHARMACEUTICALS", "TAPI")
    text = text.replace("Teva", "Tapi")
    text = text.replace("TEVA", "TAPI")
    text = text.replace("teva-engineering", "tapi-engineering")
    text = text.replace("TEV-ENG", "TAPI-ENG")
    text = text.replace("generate_teva_eng_modules", "generate_tapi_eng_modules")
    text = text.replace("get_teva_eng_curriculum", "get_tapi_eng_curriculum")
    text = text.replace("A2_TEVA_SCENARIOS", "A2_TAPI_SCENARIOS")
    
    new_gen.write_text(text, encoding="utf-8")
    print("  [OK] Created scripts/generators/tapi_eng.py")
    
    # Make teva_eng.py import and forward
    old_gen.write_text("""# Forwarding wrapper for backward compatibility
from generators.tapi_eng import generate_tapi_eng_modules as generate_teva_eng_modules
from generators.tapi_eng import *
""", encoding="utf-8")
    print("  [OK] Updated teva_eng.py as wrapper")

def update_master_index():
    p = ROOT / "index.html"
    print(f"Updating Master Hub {p}...")
    text = p.read_text(encoding="utf-8")
    
    # Update Card 3
    old_card_snippet = """<!-- 3: Teva Engineering -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #0050aa;"></div>
        <div>
          <span class="suite-badge" style="background: #e0f2fe; color: #0369a1;">💊 Pharma Facilities & Automation</span>
          <h2 class="suite-title">Teva Engineering</h2>
          <div class="suite-company">TEVA PHARMACEUTICALS | Plant Facilities & Validation</div>"""
          
    new_card_snippet = """<!-- 3: Tapi Engineering -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #0050aa;"></div>
        <div>
          <span class="suite-badge" style="background: #e0f2fe; color: #0369a1;">⚙️ API Facilities & Automation</span>
          <h2 class="suite-title">Tapi Engineering</h2>
          <div class="suite-company">TAPI | Plant Facilities & Validation</div>"""
          
    text = text.replace(old_card_snippet, new_card_snippet)
    text = text.replace(
        '<a href="teva-engineering/index.html" class="suite-launch-btn" style="background: #0050aa;">Launch Portal →</a>',
        '<a href="tapi-engineering/index.html" class="suite-launch-btn" style="background: #0050aa;">Launch Tapi Engineering Portal →</a>'
    )
    text = text.replace(
        "copySuiteLink('teva-engineering/index.html', 'Teva Engineering')",
        "copySuiteLink('tapi-engineering/index.html', 'Tapi Engineering')"
    )
    
    p.write_text(text, encoding="utf-8")
    print("  [OK] Updated Master Hub index.html")

def update_deploy_and_packaging_scripts():
    # deploy_400_modules.py
    dep_file = ROOT / "scripts" / "deploy_400_modules.py"
    text = dep_file.read_text(encoding="utf-8")
    text = text.replace("from generators.teva_eng import generate_teva_eng_modules", "from generators.tapi_eng import generate_tapi_eng_modules")
    text = text.replace('"teva-engineering": generate_teva_eng_modules', '"tapi-engineering": generate_tapi_eng_modules')
    dep_file.write_text(text, encoding="utf-8")
    print("  [OK] Updated scripts/deploy_400_modules.py")
    
    # package_for_distribution.py
    pkg_file = ROOT / "scripts" / "package_for_distribution.py"
    text = pkg_file.read_text(encoding="utf-8")
    text = text.replace('("teva-engineering", "Teva_Engineering_Suite")', '("tapi-engineering", "Tapi_Engineering_Suite")')
    text = text.replace('3. Teva Engineering (Cleanroom HVAC, SCADA/PLC, tablet presses, CSV)', '3. Tapi Engineering (Cleanroom HVAC, SCADA/PLC, tablet presses, CSV)')
    pkg_file.write_text(text, encoding="utf-8")
    print("  [OK] Updated scripts/package_for_distribution.py")

def update_firebase_config():
    p = ROOT / "firebase.json"
    with open(p, "r", encoding="utf-8") as f:
        conf = json.load(f)
    
    # Add redirect from teva-engineering to tapi-engineering
    redirects = conf.get("hosting", {}).get("redirects", [])
    # Check if exists
    has_redirect = any(r.get("source") == "/teva-engineering/:path*" for r in redirects)
    if not has_redirect:
        redirects.append({
            "source": "/teva-engineering/:path*",
            "destination": "/tapi-engineering/:path*",
            "type": 301
        })
        redirects.append({
            "source": "/teva-engineering",
            "destination": "/tapi-engineering/",
            "type": 301
        })
    conf["hosting"]["redirects"] = redirects
    
    with open(p, "w", encoding="utf-8") as f:
        json.dump(conf, f, indent=2)
    print("  [OK] Updated firebase.json with 301 redirect")

def rebuild_and_validate():
    print("\nRebuilding manifests and registries for tapi-engineering...")
    from curriculum_catalog import get_tapi_eng_curriculum
    from generators.tapi_eng import generate_tapi_eng_modules
    
    suite_dir = ROOT / "tapi-engineering"
    curriculum = get_tapi_eng_curriculum()
    modules = generate_tapi_eng_modules()
    
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
    import subprocess
    val_script = suite_dir / "scripts" / "validate_tests.py"
    res = subprocess.run([sys.executable, str(val_script)], capture_output=True, text=True)
    print(res.stdout.strip())
    if res.returncode != 0:
        print("ERROR:", res.stderr.strip())
        sys.exit(1)
    print("  [OK] Validation passed 100%!")

def main():
    print("=" * 60)
    print("STARTING MIGRATION: TEVA ENGINEERING -> TAPI ENGINEERING")
    print("=" * 60)
    
    migrate_tapi_engineering_files()
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
