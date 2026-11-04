import sys
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
content = (ROOT / "false-friends" / "index.html").read_text(encoding="utf-8")
cz_words = re.findall(r'cz:\s*"([^"]+)"', content)
print(f"Total existing: {len(cz_words)}")
for i, w in enumerate(cz_words, 1):
    print(f"{i:2d}. {w}")
