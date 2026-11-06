import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ff_html_path = ROOT / "false-friends" / "index.html"
root_html_path = ROOT / "false_friends.html"

content = ff_html_path.read_text(encoding="utf-8")

# 1. Remove premature push calls:
premature = """    // Merge New Pairs into Master Database
    FALSE_FRIENDS_DATA.push(...ADDITIONAL_PAIRS);

    // Merge New Questions into Quiz
    QUIZ_QUESTIONS.push(...ADDITIONAL_QUIZ);"""

if premature in content:
    content = content.replace(premature, "")
    print("[OK] Removed premature push calls.")

# 2. Add FALSE_FRIENDS_DATA.push right after FALSE_FRIENDS_DATA array:
target_ff = """        note: "Metallic cylindrical containers of food are 'cans' (US) or 'tins' (UK). English 'conserve' is whole fruit jam."
      }
    ];"""

replacement_ff = """        note: "Metallic cylindrical containers of food are 'cans' (US) or 'tins' (UK). English 'conserve' is whole fruit jam."
      }
    ];

    // Merge New Pairs into Master Database (52 Total)
    if (typeof ADDITIONAL_PAIRS !== 'undefined') {
      FALSE_FRIENDS_DATA.push(...ADDITIONAL_PAIRS);
    }"""

if target_ff in content:
    content = content.replace(target_ff, replacement_ff)
    print("[OK] Appended ADDITIONAL_PAIRS after FALSE_FRIENDS_DATA.")
else:
    print("[WARN] target_ff not found.")

# 3. Add QUIZ_QUESTIONS.push right after QUIZ_QUESTIONS array:
target_quiz = """        explanation: "✓ Schedule lateness is a 'delay'. A 'defect' is a physical flaw in a manufactured product."
      }
    ];"""

replacement_quiz = """        explanation: "✓ Schedule lateness is a 'delay'. A 'defect' is a physical flaw in a manufactured product."
      }
    ];

    // Merge New Questions into Quiz (30 Total)
    if (typeof ADDITIONAL_QUIZ !== 'undefined') {
      QUIZ_QUESTIONS.push(...ADDITIONAL_QUIZ);
    }"""

if target_quiz in content:
    content = content.replace(target_quiz, replacement_quiz)
    print("[OK] Appended ADDITIONAL_QUIZ after QUIZ_QUESTIONS.")
else:
    print("[WARN] target_quiz not found.")

# Write to both locations
ff_html_path.write_text(content, encoding="utf-8")
root_html_path.write_text(content, encoding="utf-8")
print(f"[OK] Written to {ff_html_path} and {root_html_path}")
