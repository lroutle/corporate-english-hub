import sys
import json
from pathlib import Path
from collections import Counter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

suites = [
    "tatra-engineering",
    "tatra-sales-engineering",
    "tapi-engineering",
    "tapi-chemistry",
    "tapi-it",
    "tapi-chemistry-kosar",
    "tapi-chemistry-mazur",
    "bidfood-purchasing-libor",
    "bidfood-purchasing-lucie",
    "bidfood-engineering-jiri"
]

print("=== REPETITION AUDIT ACROSS SUITES ===")
total_all_mods = 0
total_all_dups = 0

for s in suites:
    p = Path(s) / "data" / "tests"
    if not p.exists():
        continue
    dup_modules = []
    total_mods = 0
    for jf in sorted(p.glob("*.json")):
        total_mods += 1
        with open(jf, encoding="utf-8") as f:
            d = json.load(f)
        qs = d.get("questions", [])
        prompts = [q["prompt"] for q in qs]
        prompt_counts = Counter(prompts)
        max_rep = max(prompt_counts.values()) if prompt_counts else 0
        if max_rep > 1:
            dup_modules.append((jf.name, max_rep, d.get("title", "")))
    
    total_all_mods += total_mods
    total_all_dups += len(dup_modules)
    status = f"{len(dup_modules)} DUPLICATES" if dup_modules else "0 DUPLICATES (PASS)"
    print(f"[{s:26}] Modules: {total_mods:2} | Status: {status}")
    for name, rep, title in dup_modules[:5]:
        print(f"   {name}: {rep} identical prompts! ({title})")

print("\n" + "=" * 50)
print(f"TOTAL AUDITED: {total_all_mods} modules | TOTAL WITH DUPLICATES: {total_all_dups}")
print("=" * 50)
