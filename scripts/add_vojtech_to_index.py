import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

index_path = Path("index.html")
content = index_path.read_text(encoding="utf-8")

# 1. Update summary card
old_summary = """    <section class="summary-card">
      <div>
        <strong>9 Isolated Assessment Portals Active</strong>
        <p>Students can only see their own assigned suite and cannot navigate back to other companies or this master hub.</p>
      </div>
      <div style="font-size: 0.85rem; color: #475569;">
        Total: <strong>737+ Modules</strong> | <strong>7,370+ Diagnostic Items</strong>
      </div>
    </section>"""

new_summary = """    <section class="summary-card">
      <div>
        <strong>10 Corporate Assessment Portals & Executive Decks Active</strong>
        <p>Students can only access their assigned suite or interactive deck without cross-company navigation.</p>
      </div>
      <div style="font-size: 0.85rem; color: #475569;">
        Total: <strong>750+ Modules & Deck Slides</strong> | <strong>7,500+ Diagnostic Items</strong>
      </div>
    </section>"""

content_norm = content.replace("\r\n", "\n")
old_summary_norm = old_summary.replace("\r\n", "\n")
new_summary_norm = new_summary.replace("\r\n", "\n")

if old_summary_norm in content_norm:
    content_norm = content_norm.replace(old_summary_norm, new_summary_norm)
    print("Summary card updated.")
else:
    print("Warning: old summary card not matched.")

# 2. Add Vojtech card right after article 9 (Jiří Lorenčík)
article_9_closing = """        <div class="card-actions">
          <a href="bidfood-engineering-jiri/index.html" class="suite-launch-btn" style="background: #0f766e;">Launch Jiří Portal →</a>
          <button class="btn-copy-link" onclick="copySuiteLink('bidfood-engineering-jiri/index.html', 'Jiří Lorenčík')">📋 Copy Link</button>
        </div>
      </article>"""

vojtech_card = """        <div class="card-actions">
          <a href="bidfood-engineering-jiri/index.html" class="suite-launch-btn" style="background: #0f766e;">Launch Jiří Portal →</a>
          <button class="btn-copy-link" onclick="copySuiteLink('bidfood-engineering-jiri/index.html', 'Jiří Lorenčík')">📋 Copy Link</button>
        </div>
      </article>

      <!-- 10: AL INVEST Břidličná - Vojtěch Berger (Packaging Quality & Football) -->
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

article_9_norm = article_9_closing.replace("\r\n", "\n")
vojtech_card_norm = vojtech_card.replace("\r\n", "\n")

if article_9_norm in content_norm:
    content_norm = content_norm.replace(article_9_norm, vojtech_card_norm, 1)
    print("Vojtěch Berger card inserted cleanly.")
else:
    print("Error: Could not locate Article 9 closing block.")

index_path.write_text(content_norm, encoding="utf-8")
print("index.html written successfully.")
