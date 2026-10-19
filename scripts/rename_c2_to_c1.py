#!/usr/bin/env python3
"""
Comprehensive Migration Script: Rename C2 to C1 across the entire Corporate English Ecosystem.
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def update_curriculum_catalog():
    p = ROOT / "scripts" / "curriculum_catalog.py"
    print(f"Updating {p}...")
    text = p.read_text(encoding="utf-8")
    
    # Replace references
    text = text.replace("20 C2 Mastery", "20 C1 Advanced")
    text = text.replace("# C2 (001-020)", "# C1 (001-020)")
    text = text.replace("c2_topics =", "c1_topics =")
    text = text.replace("for num, title, track, grammar in c2_topics:", "for num, title, track, grammar in c1_topics:")
    
    # Replace test_ids and level
    text = re.sub(r'f"([A-Z-]+)-C2-\{num\}"', r'f"\1-C1-{num}"', text)
    text = text.replace('"level": "C2"', '"level": "C1"')
    text = text.replace("Mastery-tier forensic and executive", "Advanced-tier forensic and executive")
    text = text.replace("Mastery-tier commercial and technical", "Advanced-tier commercial and technical")
    text = text.replace("Mastery-tier pharmaceutical engineering", "Advanced-tier pharmaceutical engineering")
    text = text.replace("Mastery-tier active pharmaceutical", "Advanced-tier active pharmaceutical")
    text = text.replace("Mastery-tier pharmaceutical IT", "Advanced-tier pharmaceutical IT")
    
    p.write_text(text, encoding="utf-8")
    print("  [OK] curriculum_catalog.py updated.")

def update_generators():
    gen_dir = ROOT / "scripts" / "generators"
    for py_file in gen_dir.glob("*.py"):
        print(f"Updating generator {py_file.name}...")
        text = py_file.read_text(encoding="utf-8")
        
        text = text.replace("20 C2", "20 C1")
        text = text.replace("generate_c2_question", "generate_c1_question")
        text = text.replace("c2_scenarios", "c1_scenarios")
        text = text.replace("C2 automotive", "C1 automotive")
        text = text.replace("C2 legal", "C1 legal")
        text = text.replace("C2 regulatory", "C1 regulatory")
        text = text.replace("C2 chemical", "C1 chemical")
        text = text.replace("C2 cloud", "C1 cloud")
        text = text.replace("Mastery-tier syntax", "Advanced-tier syntax")
        text = text.replace("else: # C2", "else: # C1")
        
        py_file.write_text(text, encoding="utf-8")
        print(f"  [OK] {py_file.name} updated.")

def update_schemas():
    schema_files = list(ROOT.glob("**/schema/*schema*.json"))
    for sf in schema_files:
        print(f"Updating schema {sf}...")
        import json
        with open(sf, "r", encoding="utf-8") as f:
            sc = json.load(f)
        
        # Level enum
        if "level" in sc.get("properties", {}):
            lvl_enum = sc["properties"]["level"].get("enum", [])
            if "C1" not in lvl_enum:
                lvl_enum.append("C1")
            sc["properties"]["level"]["enum"] = lvl_enum
        
        # Test ID pattern
        if "test_id" in sc.get("properties", {}):
            pat = sc["properties"]["test_id"].get("pattern", "")
            if "(A2|B1|B2|C2|SP)" in pat:
                sc["properties"]["test_id"]["pattern"] = pat.replace("(A2|B1|B2|C2|SP)", "(A2|B1|B2|C1|C2|SP)")
            elif "(A2|B1|B2|SP)" in pat:
                sc["properties"]["test_id"]["pattern"] = pat.replace("(A2|B1|B2|SP)", "(A2|B1|B2|C1|C2|SP)")
        
        with open(sf, "w", encoding="utf-8") as f:
            json.dump(sc, f, indent=2, ensure_ascii=False)
        print(f"  [OK] Schema {sf.name} updated.")

def clean_old_c2_tests():
    print("Removing old C2 test JSON files...")
    count = 0
    for p in ROOT.glob("**/data/tests/*-C2-*.json"):
        p.unlink()
        count += 1
    print(f"  [OK] Removed {count} old C2 test JSON files.")

def update_suite_html_files():
    suite_htmls = [
        ROOT / "tatra-engineering" / "index.html",
        ROOT / "tatra-sales-engineering" / "index.html",
        ROOT / "teva-engineering" / "index.html",
        ROOT / "tapi-chemistry" / "index.html",
        ROOT / "tapi-chemistry-kosar" / "index.html",
        ROOT / "tapi-chemistry-mazur" / "index.html",
        ROOT / "teva-it" / "index.html"
    ]
    
    for sh in suite_htmls:
        if not sh.exists():
            continue
        print(f"Updating suite UI in {sh.relative_to(ROOT)}...")
        text = sh.read_text(encoding="utf-8")
        
        text = text.replace('id="stat-c2-modules">0</div><div class="hero-stat-label">C2 Mastery Tier</div>', 'id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div>')
        text = text.replace('data-filter-val="C2">Tier 3: C2 Mastery</button>', 'data-filter-val="C1">Tier 3: C1 Advanced</button>')
        text = text.replace("document.getElementById('stat-c2-modules').textContent = allModules.filter(m => m.level === 'C2').length;", "document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;")
        text = text.replace("m.level === 'C2'", "m.level === 'C1'")
        
        sh.write_text(text, encoding="utf-8")
        print(f"  [OK] {sh.name} updated.")

def update_css_badges():
    css_files = list(ROOT.glob("**/engine/styles.css"))
    for cf in css_files:
        print(f"Updating CSS badges in {cf.relative_to(ROOT)}...")
        text = cf.read_text(encoding="utf-8")
        
        if ".badge-level-c1" not in text:
            badge_rules = "\n.badge-level-c1 { background: #fae8ff; color: #86198f; }\n.badge-level-c2 { background: #fae8ff; color: #86198f; }"
            if ".badge-level-b2" in text:
                text = text.replace(
                    ".badge-level-b2 { background: #e0e7ff; color: #3730a3; }",
                    ".badge-level-b2 { background: #e0e7ff; color: #3730a3; }" + badge_rules
                )
            else:
                text += badge_rules
            cf.write_text(text, encoding="utf-8")
            print(f"  [OK] Badge CSS added to {cf.name}")

def update_master_index():
    p = ROOT / "index.html"
    print(f"Updating Master Hub {p}...")
    text = p.read_text(encoding="utf-8")
    
    # CSS pill
    text = text.replace(".pill-c2 { background: #fae8ff; color: #86198f; }", ".pill-c1 { background: #fae8ff; color: #86198f; }\n    .pill-c2 { background: #fae8ff; color: #86198f; }")
    
    # HTML pills in cards
    text = text.replace(
        '<span class="tier-pill pill-c2">C2 Mastery (20)</span>',
        '<span class="tier-pill pill-c1">C1 Advanced (20)</span>'
    )
    
    p.write_text(text, encoding="utf-8")
    print("  [OK] Master Hub index.html updated.")

def sync_tapi_variants():
    print("Syncing Tapi variants (Kosar and Mazur)...")
    source_dir = ROOT / "tapi-chemistry" / "data"
    for dest_name in ["tapi-chemistry-kosar", "tapi-chemistry-mazur"]:
        dest_dir = ROOT / dest_name / "data"
        dest_tests = dest_dir / "tests"
        
        # Clean dest tests
        if dest_tests.exists():
            shutil.rmtree(dest_tests)
        shutil.copytree(source_dir / "tests", dest_tests)
        
        # Copy manifests
        shutil.copy2(source_dir / "curriculum_manifest.json", dest_dir / "curriculum_manifest.json")
        shutil.copy2(source_dir / "manifest.js", dest_dir / "manifest.js")
        shutil.copy2(source_dir / "tests_registry.js", dest_dir / "tests_registry.js")
        print(f"  [OK] Synced 80 tests and manifests to {dest_name}")

def main():
    print("=" * 60)
    print("MIGRATING TIER 3 FROM C2 TO C1")
    print("=" * 60)
    
    update_curriculum_catalog()
    update_generators()
    update_schemas()
    clean_old_c2_tests()
    update_suite_html_files()
    update_css_badges()
    update_master_index()
    
    print("\n" + "=" * 60)
    print("REGENERATING AND DEPLOYING ALL MODULES...")
    print("=" * 60)
    deploy_script = ROOT / "scripts" / "deploy_400_modules.py"
    subprocess.run([sys.executable, str(deploy_script)], check=True)
    
    sync_tapi_variants()
    
    print("\n" + "=" * 60)
    print("ENSURING NOTEBOOKLM REMAINS HIDDEN...")
    print("=" * 60)
    hide_script = ROOT / "scripts" / "hide_notebooklm.py"
    subprocess.run([sys.executable, str(hide_script)], check=True)
    
    print("\n" + "=" * 60)
    print("C2 -> C1 MIGRATION SUCCESSFULLY COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    main()
