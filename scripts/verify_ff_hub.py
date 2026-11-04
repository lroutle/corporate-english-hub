import sys
from pathlib import Path

content = Path("false-friends/index.html").read_text(encoding="utf-8")
print("Size:", len(content))
print("Has horror tab:", 'id="tab-horror"' in content)
print("Has 8 stories in data:", 'horror-8' in content)
print("Has 30 quiz questions in data:", '26. The project manager' in content)
print("Has renderHorrorStories function:", 'function renderHorrorStories()' in content)
print("Has 52 card count:", 'id="count-cards">52' in content)
