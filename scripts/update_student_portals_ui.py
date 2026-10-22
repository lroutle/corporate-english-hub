"""
Update UI of Bidfood student portals to highlight their new specialized interest units:
- Libor: Darts & Football
- Lucie: Motorbikes
- Jiří: AI News & Automotive Car Topics
Preserves all localStorage prefixes and test runners 100% intact!
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent

# 1. Update Libor Barvenčík
libor_html_path = ROOT / "bidfood-purchasing-libor" / "index.html"
libor_html = libor_html_path.read_text(encoding="utf-8")

libor_html = libor_html.replace(
    '<button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Advanced</button>\n      </div>',
    '<button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Advanced</button>\n        <button class="filter-chip" data-filter-type="level" data-filter-val="specialized">🎯 Darts & Football (Specialized)</button>\n      </div>'
)

libor_html = libor_html.replace(
    'if (currentLevelFilter !== \'all\' && m.level !== currentLevelFilter) return false;',
    '''if (currentLevelFilter !== 'all') {
          if (currentLevelFilter === 'specialized' && m.category !== 'specialized') return false;
          if (currentLevelFilter !== 'specialized' && m.level !== currentLevelFilter) return false;
        }'''
)

libor_html = libor_html.replace(
    '<div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div></div>',
    '<div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div></div>\n        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-sp-modules">0</div><div class="hero-stat-label">Darts & Football</div></div>'
)

libor_html = libor_html.replace(
    "document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;",
    "document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;\n      document.getElementById('stat-sp-modules').textContent = allModules.filter(m => m.category === 'specialized').length;"
)

libor_html = libor_html.replace(
    "covering cold-chain logistics, international supplier communication, and GxP food industry standards.",
    "covering cold-chain logistics, international supplier communication, plus dedicated specialized modules on Professional Darts (PDC) and Football match analysis."
)

libor_html_path.write_text(libor_html, encoding="utf-8")
print("[OK] Updated Libor portal UI")


# 2. Update Lucie Rončková
lucie_html_path = ROOT / "bidfood-purchasing-lucie" / "index.html"
lucie_html = lucie_html_path.read_text(encoding="utf-8")

lucie_html = lucie_html.replace(
    '<button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Advanced</button>\n      </div>',
    '<button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Advanced</button>\n        <button class="filter-chip" data-filter-type="level" data-filter-val="specialized">🏍️ Motorbikes & Riding (Specialized)</button>\n      </div>'
)

lucie_html = lucie_html.replace(
    'if (currentLevelFilter !== \'all\' && m.level !== currentLevelFilter) return false;',
    '''if (currentLevelFilter !== 'all') {
          if (currentLevelFilter === 'specialized' && m.category !== 'specialized') return false;
          if (currentLevelFilter !== 'specialized' && m.level !== currentLevelFilter) return false;
        }'''
)

lucie_html = lucie_html.replace(
    '<div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div></div>',
    '<div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div></div>\n        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-sp-modules">0</div><div class="hero-stat-label">Motorbikes</div></div>'
)

lucie_html = lucie_html.replace(
    "document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;",
    "document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;\n      document.getElementById('stat-sp-modules').textContent = allModules.filter(m => m.category === 'specialized').length;"
)

lucie_html = lucie_html.replace(
    "covering cold-chain logistics, international supplier communication, and GxP food industry standards.",
    "covering cold-chain logistics, international supplier communication, plus dedicated specialized modules on Motorcycle Mechanics, Riding Dynamics, and Touring Gear."
)

lucie_html_path.write_text(lucie_html, encoding="utf-8")
print("[OK] Updated Lucie portal UI")


# 3. Update Jiří Lorenčík
jiri_html_path = ROOT / "bidfood-engineering-jiri" / "index.html"
jiri_html = jiri_html_path.read_text(encoding="utf-8")

jiri_html = jiri_html.replace(
    '<button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Advanced</button>\n      </div>',
    '<button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Advanced</button>\n        <button class="filter-chip" data-filter-type="level" data-filter-val="specialized">🤖 AI News & Car Topics (Specialized)</button>\n      </div>'
)

jiri_html = jiri_html.replace(
    'if (currentLevelFilter !== \'all\' && m.level !== currentLevelFilter) return false;',
    '''if (currentLevelFilter !== 'all') {
          if (currentLevelFilter === 'specialized' && m.category !== 'specialized') return false;
          if (currentLevelFilter !== 'specialized' && m.level !== currentLevelFilter) return false;
        }'''
)

jiri_html = jiri_html.replace(
    '<div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div></div>',
    '<div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div></div>\n        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-sp-modules">0</div><div class="hero-stat-label">AI & Car Tech</div></div>'
)

jiri_html = jiri_html.replace(
    "document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;",
    "document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;\n      document.getElementById('stat-sp-modules').textContent = allModules.filter(m => m.category === 'specialized').length;"
)

jiri_html = jiri_html.replace(
    "covering cold-chain logistics, international supplier communication, and GxP food industry standards.",
    "covering food plant engineering and ammonia refrigeration, plus dedicated specialized modules on Artificial Intelligence & Industrial Machine Learning, Turbocharging, and Automotive Engineering."
)

jiri_html_path.write_text(jiri_html, encoding="utf-8")
print("[OK] Updated Jiří portal UI")


# 4. Update Master Assessor Portal (index.html) cards to reflect the new specialized topics
index_master_path = ROOT / "index.html"
master_html = index_master_path.read_text(encoding="utf-8")

# Update Libor card
master_html = master_html.replace(
    'Dedicated environment for <strong>Libor Barvenčík</strong>. Wholesale meat/seafood sourcing, supplier price negotiation, Incoterms 2020, cold-chain logistics, and IFS quality claims.',
    'Dedicated environment for <strong>Libor Barvenčík</strong>. Wholesale meat/seafood sourcing, supplier negotiation, Incoterms 2020, plus personalized specialized units on <strong>Professional Darts (PDC)</strong> and <strong>Football Match Tactics</strong>.'
)
master_html = master_html.replace(
    '<span class="tier-pill pill-c1">C1 Advanced (20)</span>\n          </div>\n        </div>\n        <div class="card-actions">\n          <a href="bidfood-purchasing-libor/index.html"',
    '<span class="tier-pill pill-c1">C1 Advanced (20)</span>\n            <span class="tier-pill pill-sp">🎯 Darts & Football (4)</span>\n          </div>\n        </div>\n        <div class="card-actions">\n          <a href="bidfood-purchasing-libor/index.html"'
)

# Update Lucie card
master_html = master_html.replace(
    'Dedicated environment for <strong>Lucie Rončková</strong>. Wholesale food procurement, supplier rebates, dairy/perishables importing, freight scheduling, and shelf-life compliance.',
    'Dedicated environment for <strong>Lucie Rončková</strong>. Wholesale food procurement, supplier rebates, dairy/perishables importing, plus personalized specialized units on <strong>Motorbike Mechanics, Riding Dynamics & Touring</strong>.'
)
master_html = master_html.replace(
    '<span class="tier-pill pill-c1">C1 Advanced (20)</span>\n          </div>\n        </div>\n        <div class="card-actions">\n          <a href="bidfood-purchasing-lucie/index.html"',
    '<span class="tier-pill pill-c1">C1 Advanced (20)</span>\n            <span class="tier-pill pill-sp">🏍️ Motorbikes (4)</span>\n          </div>\n        </div>\n        <div class="card-actions">\n          <a href="bidfood-purchasing-lucie/index.html"'
)

# Update Jiří card
master_html = master_html.replace(
    'Dedicated environment for <strong>Ing. Jiří Lorenčík</strong>. Industrial ammonia refrigeration, blast freezing tunnels, automated packaging lines, CIP sanitation, and steam utilities.',
    'Dedicated environment for <strong>Ing. Jiří Lorenčík</strong>. Industrial ammonia refrigeration, blast freezing tunnels, CIP sanitation, plus personalized specialized units on <strong>AI in Manufacturing, LLMs & Automotive Engineering</strong>.'
)
master_html = master_html.replace(
    '<span class="tier-pill pill-c1">C1 Advanced (20)</span>\n          </div>\n        </div>\n        <div class="card-actions">\n          <a href="bidfood-engineering-jiri/index.html"',
    '<span class="tier-pill pill-c1">C1 Advanced (20)</span>\n            <span class="tier-pill pill-sp">🤖 AI & Car Topics (4)</span>\n          </div>\n        </div>\n        <div class="card-actions">\n          <a href="bidfood-engineering-jiri/index.html"'
)

# Update total count
master_html = master_html.replace(
    'Total: <strong>725+ Modules</strong> | <strong>7,250+ Diagnostic Items</strong>',
    'Total: <strong>737+ Modules</strong> | <strong>7,370+ Diagnostic Items</strong>'
)

index_master_path.write_text(master_html, encoding="utf-8")
print("[OK] Updated Master Assessor Portal index.html")
