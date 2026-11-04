import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
index_path = ROOT / "index.html"
content = index_path.read_text(encoding="utf-8")

old_snippet = """      <!-- 10: AL INVEST Břidličná - Vojtěch Berger (Packaging Quality & Football) -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #0284c7;"></div>
        <div>
          <span class="suite-badge" style="background: #e0f2fe; color: #0369a1;">🏭 Packaging Quality & Football | Vojtěch Berger</span>
          <h2 class="suite-title">AL INVEST — Vojtěch Berger</h2>
          <div class="suite-company">AL INVEST Břidličná, a.s. | Packaging Division | Vojtěch Berger</div>
          <p class="suite-desc">
            Executive Diagnostic & Grammar Deck for <strong>Vojtěch Berger</strong>. Aluminium food packaging quality, foil converting & pinholes, BRCGS standards, 8D problem solving, combined with <strong>World Sports & Football Analytics</strong>.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">Interactive Deck (19 Slides)</span>
            <span class="tier-pill pill-b1">18 Diagnostic Items</span>
            <span class="tier-pill pill-b2">Top 6 Czenglish Traps</span>
            <span class="tier-pill pill-sp">⚽ Football & Sports</span>
          </div>
        </div>
        <div class="card-actions">
          <a href="Vojtech_Berger_Grammar_Deck.html" class="suite-launch-btn" style="background: #0284c7;">Launch Interactive Deck →</a>
          <button class="btn-copy-link" onclick="copySuiteLink('Vojtech_Berger_Grammar_Deck.html', 'Vojtěch Berger Deck')">📋 Copy Link</button>
        </div>
      </article>"""

new_snippet = """      <!-- 10: AL INVEST Břidličná - Vojtěch Berger (Packaging Quality & Football) -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #0284c7;"></div>
        <div>
          <span class="suite-badge" style="background: #e0f2fe; color: #0369a1;">🏭 Packaging Quality & Football | Vojtěch Berger</span>
          <h2 class="suite-title">AL INVEST — Vojtěch Berger</h2>
          <div class="suite-company">AL INVEST Břidličná, a.s. | Packaging Division | Vojtěch Berger</div>
          <p class="suite-desc">
            Complete 84-module testing suite & executive grammar deck for <strong>Vojtěch Berger</strong> (Specialista kvality - divize Obaly). Aluminium food packaging quality, foil converting & pinholes, BRCGS Issue 6 & 8D CAPA, plus specialized units on <strong>World Sports & Football Analytics</strong>.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">A2 Foundation (20)</span>
            <span class="tier-pill pill-b1">B1 Core (20)</span>
            <span class="tier-pill pill-b2">B2 Advanced (20)</span>
            <span class="tier-pill pill-c1">C1 Leadership (20)</span>
            <span class="tier-pill pill-sp">⚽ Football (4)</span>
            <span class="tier-pill" style="background:#e0f2fe; color:#0369a1; border-color:#bae6fd;">🗣️ 19-Slide Deck</span>
          </div>
        </div>
        <div class="card-actions" style="display:flex; flex-wrap:wrap; gap:8px;">
          <a href="alinvest-packaging-vojtech/index.html" class="suite-launch-btn" style="background: #0284c7; flex:1; min-width:130px;">Launch Vojtěch Portal →</a>
          <a href="Vojtech_Berger_Grammar_Deck.html" class="suite-launch-btn" style="background: #0369a1; flex:1; min-width:130px;" target="_blank">Grammar Deck ↗</a>
          <button class="btn-copy-link" onclick="copySuiteLink('alinvest-packaging-vojtech/index.html', 'Vojtěch Berger Portal')">📋 Copy Link</button>
        </div>
      </article>"""

if old_snippet in content:
    content = content.replace(old_snippet, new_snippet)
    index_path.write_text(content, encoding="utf-8")
    print("[OK] Successfully updated Card 10 in index.html")
else:
    print("[ERROR] old_snippet not found in index.html")
