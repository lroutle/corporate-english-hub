from pathlib import Path

def update_file(path_str, replacements):
    p = Path(path_str)
    content = p.read_text(encoding='utf-8')
    for old, new in replacements:
        if old not in content:
            print(f"Warning: '{old[:40]}' not found in {path_str}")
        content = content.replace(old, new)
    p.write_text(content, encoding='utf-8')
    print(f"Updated {path_str}")

# 1. Update index.html
index_replacements = [
    ("<!-- 4: Tapi Chemistry - Košař -->", "<!-- 4: Tapi Chemistry - Jan Košař -->"),
    ("🧪 API Chemistry | Ing. Košař", "🧪 API Chemistry | Jan Košař"),
    ("Tapi Chemistry — Košař", "Tapi Chemistry — Jan Košař"),
    ("Dedicated environment for <strong>Ing. Košař</strong>.", "Dedicated environment for <strong>Jan Košař</strong>."),
    ("Launch Košař Portal →", "Launch Jan Košař Portal →"),
    ("copySuiteLink('tapi-chemistry-kosar/index.html', 'Košař')", "copySuiteLink('tapi-chemistry-kosar/index.html', 'Jan Košař')"),
    ("<!-- 5: Tapi Chemistry - Mazur -->", "<!-- 5: Tapi Chemistry - Lukáš Mazur -->"),
    ("🧪 API Chemistry | Ing. Mazur", "🧪 API Chemistry | Lukáš Mazur"),
    ("Tapi Chemistry — Mazur", "Tapi Chemistry — Lukáš Mazur"),
    ("Dedicated environment for <strong>Ing. Mazur</strong>.", "Dedicated environment for <strong>Lukáš Mazur</strong>."),
    ("Launch Mazur Portal →", "Launch Lukáš Mazur Portal →"),
    ("copySuiteLink('tapi-chemistry-mazur/index.html', 'Mazur')", "copySuiteLink('tapi-chemistry-mazur/index.html', 'Lukáš Mazur')"),
]
update_file("index.html", index_replacements)

# 2. Update tapi-chemistry-kosar/index.html
kosar_index_replacements = [
    ("<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | KOŠAŘ</span>", "<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | JAN KOŠAŘ</span>"),
    ("Tapi Chemistry Assessment Hub — Ing. Košař", "Tapi Chemistry Assessment Hub — Jan Košař"),
    ("Assessed Professional: Ing. Košař", "Assessed Professional: Jan Košař"),
    ("👤 Ing. Košař", "👤 Jan Košař"),
    ("Tapi Chemistry English Assessment — Ing. Košař", "Tapi Chemistry English Assessment — Jan Košař"),
    ("Tailored technical and workplace language modules for Ing. Košař", "Tailored technical and workplace language modules for Jan Košař"),
]
update_file("tapi-chemistry-kosar/index.html", kosar_index_replacements)

# 3. Update tapi-chemistry-kosar/test_runner.html
kosar_runner_replacements = [
    ("<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | KOŠAŘ</span>", "<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | JAN KOŠAŘ</span>"),
    ("Tapi Chemistry Testing Suite — Ing. Košař", "Tapi Chemistry Testing Suite — Jan Košař"),
    ("Assessed Professional: Ing. Košař", "Assessed Professional: Jan Košař"),
    ("Tapi Chemistry Assessment Suite — Ing. Košař", "Tapi Chemistry Assessment Suite — Jan Košař"),
]
update_file("tapi-chemistry-kosar/test_runner.html", kosar_runner_replacements)

# 4. Update tapi-chemistry-mazur/index.html
mazur_index_replacements = [
    ("<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | MAZUR</span>", "<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | LUKÁŠ MAZUR</span>"),
    ("Tapi Chemistry Assessment Hub — Ing. Mazur", "Tapi Chemistry Assessment Hub — Lukáš Mazur"),
    ("Assessed Professional: Ing. Mazur", "Assessed Professional: Lukáš Mazur"),
    ("👤 Ing. Mazur", "👤 Lukáš Mazur"),
    ("Tapi Chemistry English Assessment — Ing. Mazur", "Tapi Chemistry English Assessment — Lukáš Mazur"),
    ("Tailored technical and workplace language modules for Ing. Mazur", "Tailored technical and workplace language modules for Lukáš Mazur"),
]
update_file("tapi-chemistry-mazur/index.html", mazur_index_replacements)

# 5. Update tapi-chemistry-mazur/test_runner.html
mazur_runner_replacements = [
    ("<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | MAZUR</span>", "<span class=\"brand-logo-badge\" style=\"background:#059669;\">TAPI | LUKÁŠ MAZUR</span>"),
    ("Tapi Chemistry Testing Suite — Ing. Mazur", "Tapi Chemistry Testing Suite — Lukáš Mazur"),
    ("Assessed Professional: Ing. Mazur", "Assessed Professional: Lukáš Mazur"),
    ("Tapi Chemistry Assessment Suite — Ing. Mazur", "Tapi Chemistry Assessment Suite — Lukáš Mazur"),
]
update_file("tapi-chemistry-mazur/test_runner.html", mazur_runner_replacements)
