import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
index_path = ROOT / "index.html"
content = index_path.read_text(encoding="utf-8")

old_g1 = """        <!-- Card G1: Czech-English False Friends Hub -->
        <article class="suite-card" style="border: 2px solid #818cf8;">
          <div class="suite-top-bar" style="background: #4f46e5;"></div>
          <div>
            <span class="suite-badge" style="background: #e0f2fe; color: #3730a3;">🎭 False Friends Mastery | Falešní Přátelé</span>
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
        </article>"""

new_g1 = """        <!-- Card G1: Czech-English False Friends Hub -->
        <article class="suite-card" style="border: 2px solid #818cf8;">
          <div class="suite-top-bar" style="background: #4f46e5;"></div>
          <div>
            <span class="suite-badge" style="background: #e0e7ff; color: #3730a3;">🎭 False Friends Mastery | Falešní Přátelé</span>
            <h2 class="suite-title">Czech-English False Friends Hub</h2>
            <div class="suite-company">Universal Lesson Tool | 52-Word Encyclopedia + 30-Question Quiz + 8 Horror Stories</div>
            <p class="suite-desc">
              Expanded interactive encyclopedia of deceptive cognates (<em>kontrolovat</em> vs <em>check</em>, <em>aktuálně</em> vs <em>currently</em>, <em>fabrika</em> vs <em>plant</em>, <em>penzion</em> vs <em>guesthouse</em>, <em>harmonogram</em> vs <em>schedule</em>), interactive <strong>Corporate Email Horror Stories</strong>, and 30-item diagnostic quiz.
            </p>
            <div class="tier-pills">
              <span class="tier-pill pill-a2" style="background: #e0e7ff; color: #3730a3;">52 Word Pairs</span>
              <span class="tier-pill pill-sp" style="background: #fee2e2; color: #991b1b;">😱 8 Email Horror Stories</span>
              <span class="tier-pill pill-b1" style="background: #d1fae5; color: #065f46;">30-Item Diagnostic Quiz</span>
              <span class="tier-pill pill-b2" style="background: #fef3c7; color: #92400e;">A–Z Matrix &amp; Cheat Sheet</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="false-friends/index.html" class="suite-launch-btn" style="background: #4f46e5;">Launch False Friends Hub →</a>
            <button class="btn-copy-link" onclick="copySuiteLink('false-friends/index.html', 'False Friends Hub')">📋 Copy Link</button>
          </div>
        </article>"""

# Match loosely or find start and end
idx1 = content.find("<!-- Card G1: Czech-English False Friends Hub -->")
idx2 = content.find("<!-- Card G2: English Oddities & Humour Hub -->")

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + new_g1 + "\n\n        " + content[idx2:]
    index_path.write_text(content, encoding="utf-8")
    print("[OK] Successfully updated Card G1 in index.html")
else:
    print("[ERROR] Could not find Card G1 tags in index.html")
