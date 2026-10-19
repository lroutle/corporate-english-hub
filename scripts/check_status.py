import json
from pathlib import Path

suites = ['tatra-engineering', 'tatra-sales-engineering', 'teva-engineering', 'tapi-chemistry', 'teva-it']
for s in suites:
    p = Path(s) / 'data' / 'curriculum_manifest.json'
    with open(p, encoding='utf-8') as f:
        m = json.load(f)
    print(f'=== {s} ===')
    for item in m:
        t_path = Path(s) / 'data' / 'tests' / f"{item['test_id']}.json"
        status = 'EXISTS' if t_path.exists() else 'MISSING'
        print(f"  [{status}] {item['test_id']} ({item['level']}): {item['title']}")
