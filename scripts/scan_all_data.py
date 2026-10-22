import re
from pathlib import Path

p_dir = Path("scripts")
for py in p_dir.glob("*.py"):
    text = py.read_text(encoding="utf-8")
    tids = set(re.findall(r'tests\["([^"]+)"\]', text) + re.findall(r'"test_id":\s*"([^"]+)"', text))
    if tids:
        print(f"{py.name}: {len(tids)} test IDs -> {sorted(list(tids))[:5]} ...")
