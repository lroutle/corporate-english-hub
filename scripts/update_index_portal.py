from pathlib import Path

index_path = Path("index.html")
content = index_path.read_text(encoding="utf-8")

# 1. Update summary card
old_summary = """    <section class="summary-card">
      <div>
        <strong>6 Isolated Assessment Portals Active</strong>
        <p>Students can only see their own assigned suite and cannot navigate back to other companies or this master hub.</p>
      </div>
      <div style="font-size: 0.85rem; color: #475569;">
        Total: <strong>485 Modules</strong> | <strong>4,850 Diagnostic Items</strong>
      </div>
    </section>"""

new_summary = """    <section class="summary-card">
      <div>
        <strong>9 Isolated Assessment Portals Active</strong>
        <p>Students can only see their own assigned suite and cannot navigate back to other companies or this master hub.</p>
      </div>
      <div style="font-size: 0.85rem; color: #475569;">
        Total: <strong>725+ Modules</strong> | <strong>7,250+ Diagnostic Items</strong>
      </div>
    </section>"""

if old_summary in content:
    content = content.replace(old_summary, new_summary)
    print("Summary card updated.")
else:
    # Try normalizing CRLF
    content_norm = content.replace("\r\n", "\n")
    if old_summary in content_norm:
        content = content_norm.replace(old_summary, new_summary)
        print("Summary card updated (CRLF normalized).")
    else:
        print("Warning: old summary not matched exactly.")

# 2. Add Bidfood cards
bidfood_cards = """
      <!-- 7: Bidfood Purchasing - Libor Barvenčík -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #1e40af;"></div>
        <div>
          <span class="suite-badge" style="background: #dbeafe; color: #1e3a8a;">🥩 Cold-Chain Purchasing | Libor Barvenčík</span>
          <h2 class="suite-title">Bidfood Purchasing — Libor</h2>
          <div class="suite-company">Bidfood Czech Republic | Commercial Procurement | Libor Barvenčík</div>
          <p class="suite-desc">
            Dedicated environment for <strong>Libor Barvenčík</strong>. Wholesale meat/seafood sourcing, supplier price negotiation, Incoterms 2020, cold-chain logistics, and IFS quality claims.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">A2 Foundation (20)</span>
            <span class="tier-pill pill-b1">B1 Core (20)</span>
            <span class="tier-pill pill-b2">B2 Advanced (20)</span>
            <span class="tier-pill pill-c1">C1 Advanced (20)</span>
          </div>
        </div>
        <div class="card-actions">
          <a href="bidfood-purchasing-libor/index.html" class="suite-launch-btn" style="background: #1e40af;">Launch Libor Portal →</a>
          <button class="btn-copy-link" onclick="copySuiteLink('bidfood-purchasing-libor/index.html', 'Libor Barvenčík')">📋 Copy Link</button>
        </div>
      </article>

      <!-- 8: Bidfood Purchasing - Lucie Rončková -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #2563eb;"></div>
        <div>
          <span class="suite-badge" style="background: #dbeafe; color: #1e3a8a;">🧀 Wholesale Procurement | Lucie Rončková</span>
          <h2 class="suite-title">Bidfood Purchasing — Lucie</h2>
          <div class="suite-company">Bidfood Czech Republic | Commercial Procurement | Lucie Rončková</div>
          <p class="suite-desc">
            Dedicated environment for <strong>Lucie Rončková</strong>. Wholesale food procurement, supplier rebates, dairy/perishables importing, freight scheduling, and shelf-life compliance.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">A2 Foundation (20)</span>
            <span class="tier-pill pill-b1">B1 Core (20)</span>
            <span class="tier-pill pill-b2">B2 Advanced (20)</span>
            <span class="tier-pill pill-c1">C1 Advanced (20)</span>
          </div>
        </div>
        <div class="card-actions">
          <a href="bidfood-purchasing-lucie/index.html" class="suite-launch-btn" style="background: #2563eb;">Launch Lucie Portal →</a>
          <button class="btn-copy-link" onclick="copySuiteLink('bidfood-purchasing-lucie/index.html', 'Lucie Rončková')">📋 Copy Link</button>
        </div>
      </article>

      <!-- 9: Bidfood Process Engineering - Jiří Lorenčík -->
      <article class="suite-card">
        <div class="suite-top-bar" style="background: #0f766e;"></div>
        <div>
          <span class="suite-badge" style="background: #ccfbf1; color: #115e59;">❄️ Process Engineering | Ing. Jiří Lorenčík</span>
          <h2 class="suite-title">Bidfood Engineering — Jiří</h2>
          <div class="suite-company">Bidfood Czech Republic | Process Engineering & Utilities | Ing. Jiří Lorenčík</div>
          <p class="suite-desc">
            Dedicated environment for <strong>Ing. Jiří Lorenčík</strong>. Industrial ammonia refrigeration, blast freezing tunnels, automated packaging lines, CIP sanitation, and steam utilities.
          </p>
          <div class="tier-pills">
            <span class="tier-pill pill-a2">A2 Foundation (20)</span>
            <span class="tier-pill pill-b1">B1 Core (20)</span>
            <span class="tier-pill pill-b2">B2 Advanced (20)</span>
            <span class="tier-pill pill-c1">C1 Advanced (20)</span>
          </div>
        </div>
        <div class="card-actions">
          <a href="bidfood-engineering-jiri/index.html" class="suite-launch-btn" style="background: #0f766e;">Launch Jiří Portal →</a>
          <button class="btn-copy-link" onclick="copySuiteLink('bidfood-engineering-jiri/index.html', 'Jiří Lorenčík')">📋 Copy Link</button>
        </div>
      </article>
"""

# Insert before </div>\n  </div>\n\n  <div id="toast"
target_marker = '      </article>\n    </div>\n  </div>'
if target_marker in content:
    content = content.replace(target_marker, '      </article>' + bidfood_cards + '    </div>\n  </div>')
    print("Bidfood cards inserted successfully.")
else:
    # Try with CRLF
    target_marker_crlf = '      </article>\r\n    </div>\r\n  </div>'
    if target_marker_crlf in content:
        content = content.replace(target_marker_crlf, '      </article>' + bidfood_cards.replace('\n', '\r\n') + '    </div>\r\n  </div>')
        print("Bidfood cards inserted successfully (CRLF).")
    else:
        print("Error: Could not locate closing suite grid marker in index.html")

index_path.write_text(content, encoding="utf-8")
print("index.html updated successfully!")
