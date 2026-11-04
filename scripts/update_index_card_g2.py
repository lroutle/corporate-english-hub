import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

index_path = Path("index.html")
content = index_path.read_text(encoding="utf-8")

old_card = """        <!-- Card G2: English Oddities & Humour Hub -->
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

new_card = """        <!-- Card G2: English Oddities & Humour Hub -->
        <article class="suite-card" style="border: 2px solid #a78bfa;">
          <div class="suite-top-bar" style="background: #8b5cf6;"></div>
          <div>
            <span class="suite-badge" style="background: #ede9fe; color: #6d28d9;">🤪 English Oddities & Humour Hub</span>
            <h2 class="suite-title">English Oddities & British Subtext</h2>
            <div class="suite-company">Universal Lesson Tool | 6 Pure English Humour Units</div>
            <p class="suite-desc">
              Pure English linguistic eye-openers: British Subtext Decoder (What Brits say vs mean), The 9 Sounds of 'OUGH' & Spelling Chaos, Eggcorns & Malapropisms ("Nip it in the butt"), Contronyms (words that mean their opposite), Phrasal Verb madness, and Ambiguous Headlines.
            </p>
            <div class="tier-pills">
              <span class="tier-pill pill-a2" style="background: #ede9fe; color: #6d28d9;">14 Subtext Decoders</span>
              <span class="tier-pill pill-b1" style="background: #fef3c7; color: #92400e;">9 'OUGH' Sounds</span>
              <span class="tier-pill pill-b2" style="background: #ccfbf1; color: #115e59;">12 Contronyms</span>
              <span class="tier-pill pill-sp" style="background: #fee2e2; color: #991b1b;">12 Crazy Headlines</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="funny-english/index.html" class="suite-launch-btn" style="background: #8b5cf6;">Launch Oddities Hub →</a>
            <button class="btn-copy-link" onclick="copySuiteLink('funny-english/index.html', 'English Oddities Hub')">📋 Copy Link</button>
          </div>
        </article>"""

content_norm = content.replace("\r\n", "\n")
old_card_norm = old_card.replace("\r\n", "\n")
new_card_norm = new_card.replace("\r\n", "\n")

if old_card_norm in content_norm:
    content_norm = content_norm.replace(old_card_norm, new_card_norm, 1)
    print("Updated Card G2 in index.html to Pure English description.")
else:
    print("Error: Could not locate Card G2 in index.html.")

index_path.write_text(content_norm, encoding="utf-8")
