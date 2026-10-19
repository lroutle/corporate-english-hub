import json
from pathlib import Path

suites = ['tatra-engineering', 'tatra-sales-engineering', 'teva-engineering', 'tapi-chemistry', 'teva-it']
for s in suites:
    p = Path(s) / 'schema' / 'test_schema.json'
    with open(p, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    
    # Update level enum if needed
    if 'C2' not in sc['properties']['level']['enum']:
        sc['properties']['level']['enum'].append('C2')
    
    # Update pattern if needed
    pat = sc['properties']['test_id']['pattern']
    if '(A2|B1|B2|SP)' in pat:
        sc['properties']['test_id']['pattern'] = pat.replace('(A2|B1|B2|SP)', '(A2|B1|B2|C2|SP)')
    elif '(A2|B1|B2|C2|SP)' not in pat:
        sc['properties']['test_id']['pattern'] = pat.replace('(A2|B1|B2', '(A2|B1|B2|C2')
        
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=2, ensure_ascii=False)
    print(f"Updated {p}")
