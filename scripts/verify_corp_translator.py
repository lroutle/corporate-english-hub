import sys
from pathlib import Path

content = Path("funny-english/index.html").read_text(encoding="utf-8")
print("Size:", len(content))
print("Has tab-corporate:", 'id="tab-corporate"' in content)
print("Has tab-subtext:", 'id="tab-subtext"' in content)
print("Has CORP_PHRASES_DATA:", 'const CORP_PHRASES_DATA =' in content)
print("Has HOW_TO_SAY_DATA:", 'const HOW_TO_SAY_DATA =' in content)
print("Has SIGN_OFF_DATA:", 'const SIGN_OFF_DATA =' in content)
print("Has BOARDROOM_QUIZ_DATA:", 'const BOARDROOM_QUIZ_DATA =' in content)

idx_content = Path("index.html").read_text(encoding="utf-8")
print("Has Card G2 update in index.html:", 'TikTok Corporate Translator' in idx_content)
