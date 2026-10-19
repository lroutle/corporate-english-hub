import re
from pathlib import Path

for script_name in ["generate_suite_modules.py", "build_all_five_suites.py", "build_full_suites_ecosystem.py", "add_c2_tier_ecosystem.py"]:
    p = Path("scripts") / script_name
    if p.exists():
        text = p.read_text(encoding="utf-8")
        ids = re.findall(r'"test_id":\s*"([^"]+)"', text)
        print(f"{script_name}: {len(ids)} test IDs -> {set(ids)}")
