import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

index_path = Path("index.html")
content = index_path.read_text(encoding="utf-8")

if "English Oddities & British Subtext" in content:
    print("Funny English card already present in index.html.")
    sys.exit(0)

# 1. Update summary counts
old_summary_count = "Total: <strong>785+ Modules & Deck Slides</strong> | <strong>7,525+ Diagnostic Items</strong>"
new_summary_count = "Total: <strong>810+ Modules, Decks & Humour Units</strong> | <strong>7,550+ Diagnostic Items</strong>"

content_norm = content.replace("\r\n", "\n")
content_norm = content_norm.replace(old_summary_count, new_summary_count)

# 2. Add Funny English card right after False Friends Card
marker = """          <div class="card-actions">
            <a href="false-friends/index.html" class="suite-launch-btn" style="background: #4f46e5;">Launch False Friends Hub →</a>
            <button class="btn-copy-link" onclick="copySuiteLink('false-friends/index.html', 'False Friends Hub')">📋 Copy Link</button>
          </div>
        </article>"""

new_card = """          <div class="card-actions">
            <a href="false-friends/index.html" class="suite-launch-btn" style="background: #4f46e5;">Launch False Friends Hub →</a>
            <button class="btn-copy-link" onclick="copySuiteLink('false-friends/index.html', 'False Friends Hub')">📋 Copy Link</button>
          </div>
        </article>

        <!-- Card G2: English Oddities & Humour Hub -->
        <article class="suite-card" style="border: 2px solid #a78bfa;">
          <div class="suite-top-bar" style="background: #8b5cf6;"></div>
          <div>
            <span class="suite-badge" style="background: #ede9fe; color: #6d28d9;">🤪 English Oddities & Humour Hub</span>
            <h2 class="suite-title">English Oddities & British Subtext</h2>
            <div class="suite-company">Universal Lesson Tool | 6 Interactive Humour Units</div>
            <p class="suite-desc">
              Classroom icebreakers and linguistic eye-openers: British Subtext Decoder (What Brits say vs mean), Czenglish Idiom Collisions, Contronyms (words that mean their own opposite), Phrasal Verb madness, Bizarre Animal Groups, and Ambiguous Headlines.
            </p>
            <div class="tier-pills">
              <span class="tier-pill pill-a2" style="background: #ede9fe; color: #6d28d9;">14 Subtext Decoders</span>
              <span class="tier-pill pill-b1" style="background: #fef3c7; color: #92400e;">15 Czenglish Idioms</span>
              <span class="tier-pill pill-b2" style="background: #ccfbf1; color: #115e59;">12 Contronyms</span>
              <span class="tier-pill pill-sp" style="background: #fee2e2; color: #991b1b;">12 Crazy Headlines</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="funny-english/index.html" class="suite-launch-btn" style="background: #8b5cf6;">Launch Oddities Hub →</a>
            <button class="btn-copy-link" onclick="copySuiteLink('funny-english/index.html', 'English Oddities Hub')">📋 Copy Link</button>
          </div>
        </article>"""

marker_norm = marker.replace("\r\n", "\n")
new_card_norm = new_card.replace("\r\n", "\n")

if marker_norm in content_norm:
    content_norm = content_norm.replace(marker_norm, new_card_norm, 1)
    print("Funny English card added successfully to General section.")
else:
    print("Error: Could not find False Friends closing marker.")

index_path.write_text(content_norm, encoding="utf-8")
print("index.html written successfully.")
