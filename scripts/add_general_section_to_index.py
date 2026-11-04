import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

index_path = Path("index.html")
content = index_path.read_text(encoding="utf-8")

# Check if already present
if "Czech-English False Friends Hub" in content:
    print("False Friends Hub already in index.html.")
    sys.exit(0)

# 1. Update summary card
old_summary = """    <section class="summary-card">
      <div>
        <strong>10 Corporate Assessment Portals & Executive Decks Active</strong>
        <p>Students can only access their assigned suite or interactive deck without cross-company navigation.</p>
      </div>
      <div style="font-size: 0.85rem; color: #475569;">
        Total: <strong>750+ Modules & Deck Slides</strong> | <strong>7,500+ Diagnostic Items</strong>
      </div>
    </section>

    <div class="suites-grid">"""

new_sections = """    <section class="summary-card">
      <div>
        <strong>Corporate English Assessment Ecosystem & General Teacher Hub</strong>
        <p>General lesson tools are available across all students; corporate testing sandboxes remain strictly isolated.</p>
      </div>
      <div style="font-size: 0.85rem; color: #475569;">
        Total: <strong>785+ Modules & Deck Slides</strong> | <strong>7,525+ Diagnostic Items</strong>
      </div>
    </section>

    <!-- SECTION 1: GENERAL INSTRUCTOR TOOLKIT & UNIVERSAL LESSONS -->
    <div style="margin-bottom: 36px;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
        <div>
          <h2 style="font-size: 1.45rem; font-weight: 800; color: #1e293b;">📚 General Lesson Toolkit & Cross-Course Resources</h2>
          <p style="font-size: 0.9rem; color: #64748b;">Universal teaching decks, diagnostics, and interactive modules not tied to any single company or student.</p>
        </div>
        <span style="font-size: 0.8rem; font-weight: 700; color: #4f46e5; background: #e0e7ff; padding: 4px 12px; border-radius: 9999px;">General Lesson Mode</span>
      </div>

      <div class="suites-grid" style="grid-template-columns: repeat(auto-fit, minmax(min(100%, 360px), 1fr));">
        <!-- Card G1: Czech-English False Friends Hub -->
        <article class="suite-card" style="border: 2px solid #818cf8;">
          <div class="suite-top-bar" style="background: #4f46e5;"></div>
          <div>
            <span class="suite-badge" style="background: #e0e7ff; color: #3730a3;">🎭 False Friends Mastery | Falešní Přátelé</span>
            <h2 class="suite-title">Czech-English False Friends Hub</h2>
            <div class="suite-company">Universal Lesson Tool | 36-Word Encyclopedia + 25-Question Quiz</div>
            <p class="suite-desc">
              Comprehensive tutorial and diagnostic quiz on deceptive cognates — Czech words that sound like English words but have completely different meanings (<em>kontrolovat</em> vs <em>control</em>, <em>aktuálně</em> vs <em>actually</em>, <em>reklamace</em> vs <em>reclamation</em>, <em>sympatický</em> vs <em>sympathetic</em>).
            </p>
            <div class="tier-pills">
              <span class="tier-pill pill-a2" style="background: #e0e7ff; color: #3730a3;">36 Word Pairs</span>
              <span class="tier-pill pill-b1" style="background: #d1fae5; color: #065f46;">25-Item Interactive Quiz</span>
              <span class="tier-pill pill-b2" style="background: #fef3c7; color: #92400e;">Instant Feedback</span>
              <span class="tier-pill pill-sp" style="background: #ede9fe; color: #5b21b6;">Printable Cheat Sheet</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="false-friends/index.html" class="suite-launch-btn" style="background: #4f46e5;">Launch False Friends Hub →</a>
            <button class="btn-copy-link" onclick="copySuiteLink('false-friends/index.html', 'False Friends Hub')">📋 Copy Link</button>
          </div>
        </article>

        <!-- Card G2: Executive Interactive Lesson Deck -->
        <article class="suite-card">
          <div class="suite-top-bar" style="background: #0284c7;"></div>
          <div>
            <span class="suite-badge" style="background: #e0f2fe; color: #0369a1;">🗣️ Spoken Fluency & Grammar Deck</span>
            <h2 class="suite-title">International Sales & Trade Deck</h2>
            <div class="suite-company">Universal Lesson Tool | 15 Interactive Slides</div>
            <p class="suite-desc">
              Universal 50/50 diagnostic lesson presentation covering spoken fluency audits, overseas negotiation scenarios, 15 diagnostic grammar items, and real-time error-spotting drills.
            </p>
            <div class="tier-pills">
              <span class="tier-pill pill-a2">15 Interactive Slides</span>
              <span class="tier-pill pill-b1">Spoken Diagnostic</span>
              <span class="tier-pill pill-b2">Tenses & Conditionals</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="Interactive_Lesson_Slides.html" class="suite-launch-btn" style="background: #0284c7;">Launch Lesson Deck →</a>
            <button class="btn-copy-link" onclick="copySuiteLink('Interactive_Lesson_Slides.html', 'Lesson Slides Deck')">📋 Copy Link</button>
          </div>
        </article>
      </div>
    </div>

    <!-- SECTION 2: COMPANY & CLIENT-SPECIFIC ASSESSMENTS -->
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">
      <div>
        <h2 style="font-size: 1.45rem; font-weight: 800; color: #1e293b;">🏢 Client & Company-Specific Testing Portals</h2>
        <p style="font-size: 0.9rem; color: #64748b;">Isolated assessment environments with dedicated storage prefixes for corporate students.</p>
      </div>
      <span style="font-size: 0.8rem; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 4px 12px; border-radius: 9999px;">10 Sandboxes Active</span>
    </div>

    <div class="suites-grid">"""

content_norm = content.replace("\r\n", "\n")
old_summary_norm = old_summary.replace("\r\n", "\n")
new_sections_norm = new_sections.replace("\r\n", "\n")

if old_summary_norm in content_norm:
    content_norm = content_norm.replace(old_summary_norm, new_sections_norm, 1)
    print("General section added before suites grid.")
else:
    print("Error: Could not find old summary and suites-grid marker.")

index_path.write_text(content_norm, encoding="utf-8")
print("index.html updated successfully.")
