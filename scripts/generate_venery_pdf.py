import os
from pathlib import Path
from playwright.sync_api import sync_playwright

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Absurd Collective Nouns: Medieval Terms of Venery Quiz — Master Answer Key</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 10mm 12mm 10mm 12mm;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #1e293b;
      background: #ffffff;
      font-size: 8.5pt;
      line-height: 1.3;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }

    .page {
      width: 100%;
      min-height: 275mm;
      max-height: 277mm;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      page-break-after: always;
      break-after: page;
      position: relative;
    }
    .page:last-child {
      page-break-after: avoid;
      break-after: avoid;
    }

    /* Header */
    .header-bar {
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%);
      color: #ffffff;
      padding: 10px 14px;
      border-radius: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      border-left: 5px solid #f59e0b;
    }
    .header-title {
      font-size: 13pt;
      font-weight: 800;
      letter-spacing: -0.3px;
    }
    .header-subtitle {
      font-size: 8.2pt;
      color: #cbd5e1;
      margin-top: 2px;
    }
    .header-badge {
      background: rgba(245, 158, 11, 0.2);
      border: 1px solid #f59e0b;
      color: #fef3c7;
      font-size: 7.2pt;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      white-space: nowrap;
    }

    /* Intro Card */
    .intro-box {
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 4px solid #d97706;
      border-radius: 5px;
      padding: 6px 10px;
      margin-bottom: 8px;
      font-size: 8pt;
      color: #78350f;
      line-height: 1.35;
    }
    .intro-box strong {
      color: #92400e;
    }

    /* Reference Pills Grid */
    .summary-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      margin-bottom: 8px;
    }
    .summary-col {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 5px 7px;
    }
    .summary-col-title {
      font-size: 7.2pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 4px;
      color: #334155;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .summary-item {
      font-size: 7.4pt;
      color: #475569;
      line-height: 1.3;
    }
    .summary-item strong {
      color: #0f172a;
    }

    /* Questions Grid */
    .q-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
      flex: 1;
    }

    .q-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      padding: 6px 8px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .q-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3px;
    }
    .q-number-pill {
      font-size: 6.8pt;
      font-weight: 800;
      background: #fef3c7;
      color: #92400e;
      padding: 1px 6px;
      border-radius: 9999px;
      text-transform: uppercase;
    }
    .q-term-badge {
      font-size: 7pt;
      font-weight: 800;
      background: #ecfdf5;
      color: #047857;
      border: 1px solid #a7f3d0;
      padding: 1px 6px;
      border-radius: 4px;
    }
    .q-prompt {
      font-size: 7.9pt;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.25;
      margin-bottom: 4px;
    }
    .options-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3px;
      margin-bottom: 4px;
    }
    .opt-box {
      font-size: 7.2pt;
      padding: 2px 5px;
      border-radius: 3px;
      border: 1px solid #e2e8f0;
      background: #f8fafc;
      color: #64748b;
    }
    .opt-box.is-correct {
      background: #dcfce7;
      border-color: #22c55e;
      color: #15803d;
      font-weight: 800;
    }
    .q-lore {
      background: #f8fafc;
      border-left: 3px solid #10b981;
      padding: 3px 6px;
      border-radius: 0 3px 3px 0;
      font-size: 7.2pt;
      color: #334155;
      line-height: 1.25;
    }
    .q-lore strong {
      color: #065f46;
    }

    /* Rank Card */
    .rank-card {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      padding: 6px 10px;
      margin-top: 6px;
    }
    .rank-title {
      font-size: 7.6pt;
      font-weight: 800;
      color: #1e293b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
    }
    .rank-tiers {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
    }
    .rank-tier-box {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 3px 6px;
      font-size: 7pt;
    }
    .rank-tier-box strong {
      display: block;
      color: #0f172a;
      margin-bottom: 1px;
    }

    /* Footer */
    .footer-bar {
      border-top: 1px solid #e2e8f0;
      padding-top: 4px;
      margin-top: 6px;
      display: flex;
      justify-content: space-between;
      font-size: 6.8pt;
      color: #94a3b8;
    }
  </style>
</head>
<body>

  <!-- ==================== PAGE 1: QUESTIONS 1 - 8 ==================== -->
  <div class="page">
    <div>
      <div class="header-bar">
        <div>
          <div class="header-title">🏹 Absurd Collective Nouns: Medieval "Terms of Venery"</div>
          <div class="header-subtitle">Official 16-Question Master Quiz &amp; Historical Etymology Key • Dame Juliana Berners (1486)</div>
        </div>
        <div class="header-badge">Master Answer Key</div>
      </div>

      <div class="intro-box">
        <strong>The Venery Tradition:</strong> In 1486, Dame Juliana Berners printed <em>The Book of Saint Albans</em>, introducing aristocratic hunting ("venery") group nouns. Designed as witty courtly tests of gentlemanly education, these poetic terms characterized animals by sound, behavior, temperament, or medieval superstition. Today, many remain fully accepted English idioms.
      </div>

      <div class="summary-grid">
        <div class="summary-col">
          <div class="summary-col-title">🐦 Aerial &amp; Birds</div>
          <div class="summary-item">• Crows: <strong>A Murder</strong></div>
          <div class="summary-item">• Owls: <strong>A Parliament</strong></div>
          <div class="summary-item">• Ravens: <strong>An Unkindness</strong></div>
          <div class="summary-item">• Flamingos: <strong>A Flamboyance</strong></div>
        </div>
        <div class="summary-col">
          <div class="summary-col-title">🦁 Heavy Beasts</div>
          <div class="summary-item">• Rhinos: <strong>A Crash</strong></div>
          <div class="summary-item">• Hippos: <strong>A Bloat</strong></div>
          <div class="summary-item">• Hyenas: <strong>A Cackle</strong></div>
          <div class="summary-item">• Lions: <strong>A Pride</strong></div>
        </div>
        <div class="summary-col">
          <div class="summary-col-title">🐒 Witty &amp; Social</div>
          <div class="summary-item">• Ferrets: <strong>A Business</strong></div>
          <div class="summary-item">• Lemurs: <strong>A Conspiracy</strong></div>
          <div class="summary-item">• Apes: <strong>A Shrewdness</strong></div>
          <div class="summary-item">• Pandas: <strong>An Embarrassment</strong></div>
        </div>
        <div class="summary-col">
          <div class="summary-col-title">🦔 Curiosities</div>
          <div class="summary-item">• Porcupines: <strong>A Prickle</strong></div>
          <div class="summary-item">• Giraffes: <strong>A Tower</strong></div>
          <div class="summary-item">• Peacocks: <strong>An Ostentation</strong></div>
          <div class="summary-item">• Wombats: <strong>A Wisdom</strong></div>
        </div>
      </div>
    </div>

    <!-- Questions 1 - 8 Grid -->
    <div class="q-grid">
      
      <!-- Q1 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q1 • 🐦 Crows</span>
            <span class="q-term-badge">A Murder of Crows</span>
          </div>
          <div class="q-prompt">In 15th-century hunting lore, what is the official collective noun for crows?</div>
          <div class="options-row">
            <div class="opt-box">A) cartel</div>
            <div class="opt-box is-correct">✓ B) murder</div>
            <div class="opt-box">C) gossip</div>
            <div class="opt-box">D) conspiracy</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Originating in <em>The Book of Saint Albans</em>, scavengers were linked to battlefields and portents of death in medieval folklore.
        </div>
      </div>

      <!-- Q2 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q2 • 🦉 Owls</span>
            <span class="q-term-badge">A Parliament of Owls</span>
          </div>
          <div class="q-prompt">If you stumble upon a midnight gathering of owls in woodland, you see a...</div>
          <div class="options-row">
            <div class="opt-box is-correct">✓ A) parliament</div>
            <div class="opt-box">B) council</div>
            <div class="opt-box">C) senate</div>
            <div class="opt-box">D) synod</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Inspired by C.S. Lewis and medieval myth viewing owls as solemn, wise lawmakers debating grave matters under moonlight.
        </div>
      </div>

      <!-- Q3 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q3 • 🦅 Ravens</span>
            <span class="q-term-badge">An Unkindness of Ravens</span>
          </div>
          <div class="q-prompt">What is the classic collective term for ravens, dating back to 1486?</div>
          <div class="options-row">
            <div class="opt-box">A) treachery</div>
            <div class="opt-box is-correct">✓ B) unkindness</div>
            <div class="opt-box">C) malice</div>
            <div class="opt-box">D) darkness</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Peasant myth alleged ravens were unnatural parents who evicted fledglings prematurely to scavenge alone.
        </div>
      </div>

      <!-- Q4 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q4 • 🦩 Flamingos</span>
            <span class="q-term-badge">A Flamboyance of Flamingos</span>
          </div>
          <div class="q-prompt">When hundreds of pink flamingos wade together, English officially calls them a...</div>
          <div class="options-row">
            <div class="opt-box">A) carnival</div>
            <div class="opt-box is-correct">✓ B) flamboyance</div>
            <div class="opt-box">C) masquerade</div>
            <div class="opt-box">D) dazzle</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> From French <em>flamboyant</em> (flaming/vibrant), describing their iridescent pink plumes and synchronous courtship dances.
        </div>
      </div>

      <!-- Q5 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q5 • 🦏 Rhinoceroses</span>
            <span class="q-term-badge">A Crash of Rhinos</span>
          </div>
          <div class="q-prompt">A heavy-armored group of rhinoceroses running together is termed a...</div>
          <div class="options-row">
            <div class="opt-box">A) smash</div>
            <div class="opt-box is-correct">✓ B) crash</div>
            <div class="opt-box">C) thunder</div>
            <div class="opt-box">D) battering</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Near-blind, 2-tonne rhinos gallop at 50 km/h, literally crashing headlong through brush and savanna woodland without stopping.
        </div>
      </div>

      <!-- Q6 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q6 • 🦛 Hippopotamuses</span>
            <span class="q-term-badge">A Bloat of Hippos</span>
          </div>
          <div class="q-prompt">A herd of hippopotamuses wallowing in a riverbank is poetically known as a...</div>
          <div class="options-row">
            <div class="opt-box is-correct">✓ A) bloat</div>
            <div class="opt-box">B) bulk</div>
            <div class="opt-box">C) basin</div>
            <div class="opt-box">D) barrel</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Directly depicts their rotund, barrel-like bloated silhouettes basking in murky African river waters.
        </div>
      </div>

      <!-- Q7 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q7 • 🐕 Hyenas</span>
            <span class="q-term-badge">A Cackle of Hyenas</span>
          </div>
          <div class="q-prompt">A pack of spotted hyenas prowling the savanna is officially called a...</div>
          <div class="options-row">
            <div class="opt-box">A) giggle</div>
            <div class="opt-box is-correct">✓ B) cackle</div>
            <div class="opt-box">C) sneer</div>
            <div class="opt-box">D) scoff</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Coined after their shrill, maniacal high-pitched vocalizations echoing across plains during communal feeding bouts.
        </div>
      </div>

      <!-- Q8 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q8 • 🐼 Pandas</span>
            <span class="q-term-badge">An Embarrassment of Pandas</span>
          </div>
          <div class="q-prompt">What endearing collective noun describes a group of giant pandas?</div>
          <div class="options-row">
            <div class="opt-box">A) tumble</div>
            <div class="opt-box is-correct">✓ B) embarrassment</div>
            <div class="opt-box">C) nap</div>
            <div class="opt-box">D) bamboozle</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Celebrates their notoriously clumsy somersaults, playful bumbling nature, and awkward physical antics.
        </div>
      </div>

    </div>

    <div class="footer-bar">
      <span>English Oddities &amp; Humour Series • Corporate English Hub</span>
      <span>Page 1 of 2 (Questions 1–8)</span>
      <span>Bidfood Executive English Training</span>
    </div>
  </div>

  <!-- ==================== PAGE 2: QUESTIONS 9 - 16 & RANKING ==================== -->
  <div class="page">
    <div>
      <div class="header-bar">
        <div>
          <div class="header-title">🏹 Absurd Collective Nouns: Medieval "Terms of Venery"</div>
          <div class="header-subtitle">Official 16-Question Master Quiz &amp; Historical Etymology Key (Continued)</div>
        </div>
        <div class="header-badge">Master Answer Key</div>
      </div>
    </div>

    <!-- Questions 9 - 16 Grid -->
    <div class="q-grid">

      <!-- Q9 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q9 • 🦡 Ferrets</span>
            <span class="q-term-badge">A Business of Ferrets</span>
          </div>
          <div class="q-prompt">If you keep multiple pet ferrets together in an enclosure, you own a...</div>
          <div class="options-row">
            <div class="opt-box">A) mischief</div>
            <div class="opt-box is-correct">✓ B) business</div>
            <div class="opt-box">C) hustle</div>
            <div class="opt-box">D) scramble</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Originates from Middle English <em>besynes</em> ("restless busyness"), portraying their relentless darting and scurrying.
        </div>
      </div>

      <!-- Q10 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q10 • 🐒 Lemurs</span>
            <span class="q-term-badge">A Conspiracy of Lemurs</span>
          </div>
          <div class="q-prompt">A troop of ring-tailed lemurs huddled together in Madagascar is a...</div>
          <div class="options-row">
            <div class="opt-box is-correct">✓ A) conspiracy</div>
            <div class="opt-box">B) syndicate</div>
            <div class="opt-box">C) secret</div>
            <div class="opt-box">D) whisper</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Their wide luminous tapetum eyes and secretive jungle circle huddles evoked cloaked conspirators hatching midnight treason.
        </div>
      </div>

      <!-- Q11 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q11 • 🦔 Porcupines</span>
            <span class="q-term-badge">A Prickle of Porcupines</span>
          </div>
          <div class="q-prompt">What is the unmistakably descriptive group name for porcupines?</div>
          <div class="options-row">
            <div class="opt-box">A) needle</div>
            <div class="opt-box is-correct">✓ B) prickle</div>
            <div class="opt-box">C) barb</div>
            <div class="opt-box">D) quill</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> An onomatopoeic visual gem directly invoking their bristling coat of 30,000 defensive barbed quills when startled.
        </div>
      </div>

      <!-- Q12 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q12 • 🦒 Giraffes</span>
            <span class="q-term-badge">A Tower of Giraffes</span>
          </div>
          <div class="q-prompt">What architectural term describes a tall group of giraffes walking?</div>
          <div class="options-row">
            <div class="opt-box">A) steeple</div>
            <div class="opt-box is-correct">✓ B) tower</div>
            <div class="opt-box">C) monument</div>
            <div class="opt-box">D) column</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Standing up to 5.8m tall, a migrating family silhouettes against the flat grassland horizon like walking watchtowers.
        </div>
      </div>

      <!-- Q13 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q13 • 🦚 Peacocks</span>
            <span class="q-term-badge">An Ostentation of Peacocks</span>
          </div>
          <div class="q-prompt">When male peacocks strut displaying their iridescent train, they form an...</div>
          <div class="options-row">
            <div class="opt-box">A) extravagance</div>
            <div class="opt-box is-correct">✓ B) ostentation</div>
            <div class="opt-box">C) arrogance</div>
            <div class="opt-box">D) elegance</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> From Latin <em>ostentare</em> ("to flaunt/show off"), mocking the peacock's shameless vanity and pompous display.
        </div>
      </div>

      <!-- Q14 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q14 • 🦍 Apes</span>
            <span class="q-term-badge">A Shrewdness of Apes</span>
          </div>
          <div class="q-prompt">Medieval hunters in 1486 granted a group of apes which cunning collective noun?</div>
          <div class="options-row">
            <div class="opt-box">A) cunning</div>
            <div class="opt-box is-correct">✓ B) shrewdness</div>
            <div class="opt-box">C) wisdom</div>
            <div class="opt-box">D) mischief</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> In 15th-century English, 'shrewd' meant playfully mischievous or calculatingly cunning, praising their quick wits.
        </div>
      </div>

      <!-- Q15 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q15 • 🦁 Lions</span>
            <span class="q-term-badge">A Pride of Lions</span>
          </div>
          <div class="q-prompt">Which venery term became completely mainstream in everyday modern English?</div>
          <div class="options-row">
            <div class="opt-box">A) reign</div>
            <div class="opt-box is-correct">✓ B) pride</div>
            <div class="opt-box">C) majesty</div>
            <div class="opt-box">D) dominion</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Medieval heraldry crowned the lion king of beasts; their regal bearing and family loyalty cemented "pride" into standard speech.
        </div>
      </div>

      <!-- Q16 -->
      <div class="q-card">
        <div>
          <div class="q-header">
            <span class="q-number-pill">Q16 • 🐻 Wombats</span>
            <span class="q-term-badge">A Wisdom of Wombats</span>
          </div>
          <div class="q-prompt">What philosophical collective noun is reserved for Australia's wombats?</div>
          <div class="options-row">
            <div class="opt-box">A) ponder</div>
            <div class="opt-box is-correct">✓ B) wisdom</div>
            <div class="opt-box">C) contemplation</div>
            <div class="opt-box">D) trundle</div>
          </div>
        </div>
        <div class="q-lore">
          <strong>Lore:</strong> Despite their slow, stocky waddle, observers bestowed this dignified title honoring their ancient, unbothered stoicism.
        </div>
      </div>

    </div>

    <!-- Official Medieval Ranking Table -->
    <div class="rank-card">
      <div class="rank-title">
        <span>🏆 Official Medieval Venery Ranking System</span>
        <span>Based on 16 Diagnostic Items</span>
      </div>
      <div class="rank-tiers">
        <div class="rank-tier-box" style="border-left: 3px solid #d97706;">
          <strong>👑 15–16 Correct</strong>
          <span>Grandmaster of the Royal Hunt (Dame Juliana's Chosen Scholar)</span>
        </div>
        <div class="rank-tier-box" style="border-left: 3px solid #0284c7;">
          <strong>🏹 12–14 Correct</strong>
          <span>Chief Falconer of the English Realm (Courtly Lore Expert)</span>
        </div>
        <div class="rank-tier-box" style="border-left: 3px solid #16a34a;">
          <strong>🐎 8–11 Correct</strong>
          <span>Knowledgeable Forest Squire (Competent Field Navigator)</span>
        </div>
        <div class="rank-tier-box" style="border-left: 3px solid #64748b;">
          <strong>🦆 0–7 Correct</strong>
          <span>Confused Peasant Wandering in Sherwood Forest</span>
        </div>
      </div>
    </div>

    <div class="footer-bar">
      <span>English Oddities &amp; Humour Series • Corporate English Hub</span>
      <span>Page 2 of 2 (Questions 9–16 &amp; Scores)</span>
      <span>Bidfood Executive English Training</span>
    </div>
  </div>

</body>
</html>
"""

def generate():
    root_dir = Path("C:/tmp/00-Mycat")
    html_path = root_dir / "terms_of_venery_quiz_answers_printable.html"
    pdf_path = root_dir / "Terms_of_Venery_Quiz_Answers.pdf"
    
    html_path.write_text(HTML_CONTENT, encoding="utf-8")
    print(f"Wrote HTML to {html_path}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.as_uri())
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        browser.close()
    
    print(f"Generated PDF at {pdf_path} (Size: {pdf_path.stat().st_size} bytes)")
    
    # Also copy to funny-english directory
    funny_dir = root_dir / "funny-english"
    if funny_dir.exists():
        import shutil
        shutil.copy(pdf_path, funny_dir / "Terms_of_Venery_Quiz_Answers.pdf")
        shutil.copy(html_path, funny_dir / "terms_of_venery_quiz_answers_printable.html")
        print(f"Copied to {funny_dir}")

if __name__ == "__main__":
    generate()
