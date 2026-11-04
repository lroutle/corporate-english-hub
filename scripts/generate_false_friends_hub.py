import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def build_false_friends_hub():
    out_dir = Path("false-friends")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "index.html"

    # We will write a complete, self-contained single-page application for the False Friends Hub.
    html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>Czech-English False Friends | Master Tutorial & Diagnostic Quiz</title>
  <style>
    :root {
      --primary: #4f46e5;
      --primary-dark: #3730a3;
      --primary-light: #818cf8;
      --primary-subtle: #e0e7ff;
      --accent: #0d9488;
      --accent-light: #2dd4bf;
      --dark-navy: #0f172a;
      --card-bg: #ffffff;
      --bg: #f8fafc;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --success: #10b981;
      --success-subtle: #d1fae5;
      --danger: #ef4444;
      --danger-subtle: #fee2e2;
      --warning: #f59e0b;
      --warning-subtle: #fef3c7;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
      --radius-md: 10px;
      --radius-lg: 16px;
      --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font);
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Header */
    .hub-header {
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%);
      color: #ffffff;
      padding: 32px 24px;
      box-shadow: var(--shadow-md);
      border-bottom: 4px solid var(--accent-light);
    }

    .header-inner {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .brand-group h1 {
      font-size: 2.1rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-group p {
      color: #c7d2fe;
      font-size: 1rem;
      max-width: 780px;
    }

    .header-actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      border: none;
    }

    .btn-light {
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.25);
    }
    .btn-light:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    .btn-accent {
      background: var(--accent);
      color: #ffffff;
    }
    .btn-accent:hover {
      background: #0f766e;
    }

    /* Main Container */
    .main-wrap {
      max-width: 1200px;
      margin: 28px auto;
      padding: 0 20px;
      flex: 1;
      width: 100%;
    }

    /* Navigation Tabs */
    .nav-tabs {
      display: flex;
      gap: 8px;
      border-bottom: 2px solid var(--border);
      margin-bottom: 28px;
      overflow-x: auto;
      padding-bottom: 2px;
    }

    .tab-btn {
      padding: 12px 22px;
      background: none;
      border: none;
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 3px solid transparent;
      margin-bottom: -2px;
      transition: all 0.2s;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .tab-btn:hover {
      color: var(--primary);
    }

    .tab-btn.active {
      color: var(--primary);
      border-bottom-color: var(--primary);
    }

    .tab-count {
      background: var(--primary-subtle);
      color: var(--primary-dark);
      font-size: 0.78rem;
      padding: 2px 8px;
      border-radius: 9999px;
    }

    /* Tutorial Section */
    .controls-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }

    .search-input {
      flex: 1;
      min-width: 280px;
      padding: 12px 18px;
      border: 2px solid var(--border);
      border-radius: var(--radius-md);
      font-size: 0.95rem;
      outline: none;
      font-family: inherit;
    }
    .search-input:focus {
      border-color: var(--primary);
    }

    .filter-chips {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-chip {
      background: #ffffff;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 9999px;
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .filter-chip:hover {
      border-color: var(--primary);
      color: var(--primary);
    }
    .filter-chip.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }

    /* Cards Grid */
    .cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 360px), 1fr));
      gap: 22px;
    }

    .ff-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
    }
    .ff-card:hover {
      box-shadow: var(--shadow-md);
      border-color: var(--primary-light);
      transform: translateY(-2px);
    }

    .ff-card-top {
      border-top: 4px solid var(--primary);
      position: absolute;
      top: 0; left: 0; right: 0;
    }
    .ff-card[data-cat="business"] .ff-card-top { border-top-color: #3b82f6; }
    .ff-card[data-cat="roles"] .ff-card-top { border-top-color: #8b5cf6; }
    .ff-card[data-cat="social"] .ff-card-top { border-top-color: #10b981; }
    .ff-card[data-cat="daily"] .ff-card-top { border-top-color: #f59e0b; }

    .ff-category-badge {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 8px;
    }

    .ff-cz-head {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 12px;
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .ff-cz-head span {
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-muted);
    }

    .comparison-box {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 14px;
      font-size: 0.92rem;
    }

    .comp-row {
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-bottom: 6px;
    }
    .comp-row:last-child { margin-bottom: 0; }

    .label-wrong {
      color: var(--danger);
      font-weight: 700;
      min-width: 65px;
      font-size: 0.8rem;
    }

    .label-correct {
      color: var(--success);
      font-weight: 700;
      min-width: 65px;
      font-size: 0.8rem;
    }

    .ff-examples {
      font-size: 0.88rem;
      margin-bottom: 12px;
      line-height: 1.45;
    }

    .ex-wrong {
      color: #991b1b;
      background: #fef2f2;
      padding: 6px 10px;
      border-radius: 6px;
      margin-bottom: 6px;
    }

    .ex-correct {
      color: #065f46;
      background: #f0fdf4;
      padding: 6px 10px;
      border-radius: 6px;
    }

    .ff-note {
      font-size: 0.8rem;
      color: var(--text-muted);
      border-top: 1px dashed var(--border);
      padding-top: 10px;
      font-style: italic;
    }

    /* Quiz Tab */
    .quiz-container {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 32px;
      box-shadow: var(--shadow-sm);
    }

    .quiz-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      flex-wrap: wrap;
      gap: 16px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--border);
    }

    .score-badge {
      background: var(--primary-subtle);
      color: var(--primary-dark);
      padding: 8px 18px;
      border-radius: 9999px;
      font-weight: 800;
      font-size: 1.05rem;
    }

    .quiz-item-card {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px;
      margin-bottom: 20px;
      border-left: 5px solid var(--primary);
    }

    .quiz-item-card.answered-correct {
      border-left-color: var(--success);
      background: #f0fdf4;
    }

    .quiz-item-card.answered-wrong {
      border-left-color: var(--danger);
      background: #fef2f2;
    }

    .quiz-num {
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--primary);
      margin-bottom: 6px;
    }

    .quiz-question {
      font-size: 1.08rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 16px;
      line-height: 1.5;
    }

    .quiz-options {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
    }

    .quiz-btn {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 16px;
      text-align: left;
      font-size: 0.95rem;
      cursor: pointer;
      font-family: inherit;
      color: var(--text-main);
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .quiz-btn:hover:not(:disabled) {
      border-color: var(--primary);
      background: var(--primary-subtle);
    }

    .quiz-btn.chosen-correct {
      background: var(--success) !important;
      color: #ffffff !important;
      border-color: var(--success) !important;
      font-weight: 700;
    }

    .quiz-btn.chosen-wrong {
      background: var(--danger) !important;
      color: #ffffff !important;
      border-color: var(--danger) !important;
      text-decoration: line-through;
    }

    .quiz-btn.show-correct {
      border-color: var(--success) !important;
      background: #d1fae5 !important;
      color: #065f46 !important;
      font-weight: 700;
    }

    .quiz-feedback {
      display: none;
      margin-top: 14px;
      padding: 12px 16px;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.5;
    }

    .quiz-feedback.show {
      display: block;
      animation: fadeIn 0.25s ease;
    }

    .quiz-feedback.correct-fb {
      background: #dcfce7;
      color: #14532d;
      border-left: 4px solid var(--success);
    }

    .quiz-feedback.wrong-fb {
      background: #fee2e2;
      color: #7f1d1d;
      border-left: 4px solid var(--danger);
    }

    /* Score summary banner */
    .summary-box {
      display: none;
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
      color: #ffffff;
      padding: 32px;
      border-radius: var(--radius-lg);
      text-align: center;
      margin-top: 32px;
    }

    /* Cheat Sheet Matrix */
    .table-wrap {
      overflow-x: auto;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
    }

    .ff-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.92rem;
    }

    .ff-table th {
      background: #f1f5f9;
      padding: 14px 18px;
      font-weight: 700;
      color: var(--text-main);
      border-bottom: 2px solid var(--border);
    }

    .ff-table td {
      padding: 12px 18px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }

    .ff-table tr:hover {
      background: #f8fafc;
    }

    .tag-cz { font-weight: 700; color: #1e293b; }
    .tag-trap { color: #dc2626; font-weight: 600; font-family: monospace; }
    .tag-real { color: #059669; font-weight: 700; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Print optimization */
    @media print {
      .hub-header, .nav-tabs, .controls-row, .header-actions, .quiz-btn { display: none !important; }
      body { background: #fff; color: #000; }
      .ff-card { break-inside: avoid; border: 1px solid #ccc; box-shadow: none; }
      .main-wrap { max-width: 100%; padding: 0; margin: 0; }
    }
  </style>
</head>
<body>

  <!-- Top Master Hub Header -->
  <header class="hub-header">
    <div class="header-inner">
      <div class="brand-group">
        <h1><span>🎭</span> Czech-English False Friends (Falešní Přátelé)</h1>
        <p>
          Master Reference & Diagnostic Suite: Words from Czech that sound deceptively similar to English words, but carry completely different meanings.
        </p>
      </div>
      <div class="header-actions">
        <a href="../index.html" class="btn btn-light">← Assessor Portal</a>
        <button class="btn btn-accent" onclick="window.print()">🖨️ Print Cheat Sheet</button>
      </div>
    </div>
  </header>

  <div class="main-wrap">

    <!-- Navigation Tabs -->
    <div class="nav-tabs">
      <button class="tab-btn active" onclick="switchTab('tutorial')">
        📖 Visual Tutorial & Encyclopedia <span class="tab-count" id="count-cards">36</span>
      </button>
      <button class="tab-btn" onclick="switchTab('quiz')">
        🎯 25-Question Diagnostic Quiz <span class="tab-count">25 Items</span>
      </button>
      <button class="tab-btn" onclick="switchTab('table')">
        ⚡ Rapid A–Z Matrix <span class="tab-count">Quick Reference</span>
      </button>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 1: VISUAL TUTORIAL & ENCYCLOPEDIA -->
    <!-- ============================================================== -->
    <div id="tab-tutorial">
      <div class="controls-row">
        <input type="text" id="search-input" class="search-input" placeholder="🔍 Search by Czech word, false friend, or English meaning (e.g. kontrolovat, actually, chef)...">
        
        <div class="filter-chips">
          <button class="filter-chip active" onclick="filterCategory('all', this)">All Categories</button>
          <button class="filter-chip" onclick="filterCategory('business', this)">💼 Business & Office</button>
          <button class="filter-chip" onclick="filterCategory('roles', this)">👔 Job Titles & Roles</button>
          <button class="filter-chip" onclick="filterCategory('social', this)">🗣️ Social & Character</button>
          <button class="filter-chip" onclick="filterCategory('daily', this)">🛒 Daily Life & Objects</button>
        </div>
      </div>

      <div class="cards-grid" id="cards-container">
        <!-- Injected via JavaScript -->
      </div>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 2: INTERACTIVE DIAGNOSTIC QUIZ -->
    <!-- ============================================================== -->
    <div id="tab-quiz" style="display: none;">
      <div class="quiz-container">
        <div class="quiz-header-bar">
          <div>
            <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--text-main);">Diagnostic Screening: Spot the False Friend</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem;">Select the authentic English phrasing for each scenario. Instant feedback reveals why typical Czech instincts fail.</p>
          </div>
          <div class="score-badge" id="score-display">Score: 0 / 25 (0%)</div>
        </div>

        <div id="quiz-list">
          <!-- Injected via JavaScript -->
        </div>

        <div class="summary-box" id="quiz-summary">
          <h2 style="font-size: 2rem; margin-bottom: 8px;" id="summary-title">Quiz Completed!</h2>
          <p style="font-size: 1.2rem; color: #cbd5e1; margin-bottom: 20px;" id="summary-text"></p>
          <button class="btn btn-accent" style="font-size: 1rem; padding: 12px 24px;" onclick="resetQuiz()">🔄 Retake Diagnostic Quiz</button>
        </div>
      </div>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 3: RAPID A-Z REFERENCE MATRIX -->
    <!-- ============================================================== -->
    <div id="tab-table" style="display: none;">
      <div class="table-wrap">
        <table class="ff-table">
          <thead>
            <tr>
              <th>Czech Word (What you think)</th>
              <th>Deceptive False English</th>
              <th>What that English Word ACTUALLY Means</th>
              <th>True English Translation (Say this!)</th>
            </tr>
          </thead>
          <tbody id="matrix-body">
            <!-- Injected via JavaScript -->
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <script>
    // Comprehensive Database of 36 Major Czech-English False Friends
    const FALSE_FRIENDS_DATA = [
      {
        cz: "Aktuálně / Aktuální",
        category: "business",
        trap: "Actually",
        trap_meaning: "Ve skutečnosti / vlastně (in fact, really)",
        correct: "Currently / At present / Latest / Up-to-date",
        ex_wrong: "❌ 'Actually we are developing a new prototype.' (Sounds like you are correcting a misunderstanding!)",
        ex_correct: "✓ 'Currently, we are developing a new prototype.' / 'Here is the up-to-date schedule.'",
        note: "One of the most frequent errors in Czech corporate emails. 'Actually' contradicts or clarifies; 'currently' refers to present time."
      },
      {
        cz: "Kontrolovat",
        category: "business",
        trap: "Control",
        trap_meaning: "Řídit / ovládat / mít pod nadvládou (to dominate, steer, regulate)",
        correct: "Check / Inspect / Verify / Monitor / Audit",
        ex_wrong: "❌ 'I must control your passport at the border.' (Sounds like you want to seize power over it!)",
        ex_correct: "✓ 'I must check / inspect your passport.' / 'We verified the batch dimensions.'",
        note: "In English, quality testing is 'inspection' or 'checking'. You only 'control' an air conditioner or a remote machine."
      },
      {
        cz: "Reklamace / Reklamovat",
        category: "business",
        trap: "Reclamation / Reclaim",
        trap_meaning: "Rekultivace půdy / vysoušení močálů / znovuzískání ztraceného majetku",
        correct: "Complaint / Claim / To make a formal complaint",
        ex_wrong: "❌ 'The automotive client sent a severe reclamation about the engine burrs.'",
        ex_correct: "✓ 'The automotive client submitted a severe customer complaint / warranty claim.'",
        note: "Never use 'reclamation' for customer disputes. In English, it is always a 'customer complaint' or 'quality claim'."
      },
      {
        cz: "Akce (sleva / událost)",
        category: "business",
        trap: "Action",
        trap_meaning: "Činnost / děj / právní žaloba / vojenský zásah",
        correct: "Special offer / Promotion / Sale / Event",
        ex_wrong: "❌ 'We have a big action on butter and cheese this week.'",
        ex_correct: "✓ 'We have a special promotion / discount sale on butter this week.'",
        note: "Czech uses 'akce' for sales promotions, social parties, and events. English distinguishes 'special offer/sale' from an 'event'."
      },
      {
        cz: "Evidence",
        category: "business",
        trap: "Evidence",
        trap_meaning: "Důkaz / soudní svědectví / nezvratná fakta o vině",
        correct: "Records / Tracking / Database / Register / Logs",
        ex_wrong: "❌ 'Our HR department keeps an evidence of all employee sick days.'",
        ex_correct: "✓ 'Our HR department maintains records / a register of employee sick days.'",
        note: "English 'evidence' is non-count and exclusively means proof in court or scientific verification."
      },
      {
        cz: "Realizovat",
        category: "business",
        trap: "Realize",
        trap_meaning: "Uvědomit si / pochopit v hlavě (to come to understand)",
        correct: "Implement / Carry out / Execute / Deliver / Complete",
        ex_wrong: "❌ 'We realized the plant expansion project in six months.'",
        ex_correct: "✓ 'We implemented / executed the plant expansion project in six months.'",
        note: "While 'realize dreams' exists in poetic English, in business operations use 'execute, implement, or deliver'."
      },
      {
        cz: "Eventuálně",
        category: "business",
        trap: "Eventually",
        trap_meaning: "Nakonec / po dlouhé době / časem (in the end, after delays)",
        correct: "Possibly / Alternatively / If necessary / If needed",
        ex_wrong: "❌ 'You can submit the report today, or eventually on Monday.' (Means: after years of struggle!)",
        ex_correct: "✓ 'You can submit it today, or alternatively / if necessary on Monday.'",
        note: "'Eventually' implies that something took a very long time to happen ('After 10 years, they eventually succeeded')."
      },
      {
        cz: "Konkurz",
        category: "business",
        trap: "Concourse",
        trap_meaning: "Dvorana / hala nádraží nebo letiště / otevřené prostranství",
        correct: "Bankruptcy / Insolvency (finances) OR Audition / Tender (selection)",
        ex_wrong: "❌ 'The supplier went into concourse and stopped production.'",
        ex_correct: "✓ 'The supplier declared bankruptcy / entered insolvency.'",
        note: "Czech 'konkurz' means insolvency/bankruptcy or a competitive hiring tender/audition."
      },
      {
        cz: "Faktura",
        category: "business",
        trap: "Fracture",
        trap_meaning: "Zlomenina kosti / puklina horniny",
        correct: "Invoice / Bill",
        ex_wrong: "❌ 'Please pay the fracture before the due date.'",
        ex_correct: "✓ 'Please pay the invoice / bill before the due date.'",
        note: "Faktura comes from Italian fattura, but English uses 'invoice' for business and 'bill' for utilities/restaurants."
      },
      {
        cz: "Revize (technická)",
        category: "business",
        trap: "Revision",
        trap_meaning: "Opakování učiva na zkoušku / revize textu smlouvy (proofreading)",
        correct: "Inspection / Periodic safety check / Statutory service / Audit",
        ex_wrong: "❌ 'The boiler technician is coming for an annual revision.'",
        ex_correct: "✓ 'The technician is coming for an annual safety inspection / service check.'",
        note: "In English, a 'revision' is editing a text or studying for an exam. Technical machine checks are 'inspections'."
      },
      {
        cz: "Absolvovat",
        category: "business",
        trap: "Absolve",
        trap_meaning: "Zprostit viny / odpustit hříchy (pardon, forgive guilt)",
        correct: "Complete / Graduate from / Attend / Finish",
        ex_wrong: "❌ 'I absolved the Technical University in 2018.'",
        ex_correct: "✓ 'I graduated from the Technical University in 2018.' / 'I completed the safety course.'",
        note: "In English, priests and courts 'absolve' people of crimes and sins. You 'graduate from' a university."
      },
      {
        cz: "Trafika",
        category: "business",
        trap: "Traffic",
        trap_meaning: "Silniční provoz / hustota dopravy na cestách",
        correct: "Newsstand / Newsagent's / Kiosk / Tobacconist",
        ex_wrong: "❌ 'I stopped at the traffic to buy a newspaper.'",
        ex_correct: "✓ 'I stopped at the newsstand / kiosk to buy a newspaper.'",
        note: "'Traffic' refers only to vehicle flow or digital network bandwidth."
      },
      {
        cz: "Šéf",
        category: "roles",
        trap: "Chef",
        trap_meaning: "Šéfkuchař v restauraci (professional culinary cook)",
        correct: "Boss / Manager / Supervisor / Head / Director",
        ex_wrong: "❌ 'My chef approved my holiday request yesterday.' (Unless you work in a restaurant kitchen!)",
        ex_correct: "✓ 'My boss / department manager approved my holiday request.'",
        note: "French 'chef' means chief, but English adopted it strictly for professional restaurant kitchen cooks."
      },
      {
        cz: "Brigáda / Brigádník",
        category: "roles",
        trap: "Brigade",
        trap_meaning: "Vojenská brigáda (armádní jednotka) nebo hasičský sbor (fire brigade)",
        correct: "Part-time job / Temporary job / Student gig / Temp worker",
        ex_wrong: "❌ 'During high school, I had a brigade at a local warehouse.'",
        ex_correct: "✓ 'During high school, I had a summer / temporary part-time job at a local warehouse.'",
        note: "English 'brigade' is strictly military or civil defence (Fire Brigade). Temporary student work is a 'part-time job' or 'temp gig'."
      },
      {
        cz: "Promoce",
        category: "roles",
        trap: "Promotion",
        trap_meaning: "Povýšení v zaměstnání (career step) / reklamní kampaň (marketing)",
        correct: "Graduation ceremony / University commencement",
        ex_wrong: "❌ 'My family attended my promotion last Friday.' (They think you got a higher salary at work!)",
        ex_correct: "✓ 'My family attended my university graduation ceremony.'",
        note: "In English, 'promotion' is moving up to senior manager. Finishing university is 'graduation'."
      },
      {
        cz: "Kauza",
        category: "roles",
        trap: "Cause",
        trap_meaning: "Příčina / prapůvod jevu / charitativní účel",
        correct: "Case / Affair / Scandal / Legal proceeding",
        ex_wrong: "❌ 'The media is reporting heavily on the corruption cause.'",
        ex_correct: "✓ 'The media is reporting heavily on the corruption scandal / case.'",
        note: "'Cause' is the reason why something happens (Root Cause) or a social movement ('a good cause')."
      },
      {
        cz: "Ordinace",
        category: "roles",
        trap: "Ordination",
        trap_meaning: "Vysvěcení kněze na duchovního (religious consecration)",
        correct: "Doctor's surgery / Clinic / Doctor's office / Practice",
        ex_wrong: "❌ 'I have an appointment at the doctor's ordination at 10 AM.'",
        ex_correct: "✓ 'I have an appointment at the doctor's surgery / clinic at 10 AM.'",
        note: "'Ordination' is making someone a priest. A medical workspace is a 'surgery' (UK) or 'doctor's office' (US)."
      },
      {
        cz: "Transparent (podstatné jméno)",
        category: "roles",
        trap: "Transparent",
        trap_meaning: "Průhledný / čirý (přídavné jméno)",
        correct: "Banner / Placard / Protest sign",
        ex_wrong: "❌ 'The protesters were holding large transparents in front of the ministry.'",
        ex_correct: "✓ 'The protesters were holding large banners / placards.'",
        note: "In English, 'transparent' is an adjective (transparent plastic). A cloth slogan sheet is a 'banner'."
      },
      {
        cz: "Sympatický",
        category: "social",
        trap: "Sympathetic",
        trap_meaning: "Soucitný / projevující soustrast a pochopení v neštěstí",
        correct: "Likable / Pleasant / Friendly / Charming / Nice",
        ex_wrong: "❌ 'Our new client is very sympathetic; we laughed a lot.' (Sounds like you shared a tragedy!)",
        ex_correct: "✓ 'Our new client is very likable / pleasant / friendly.'",
        note: "Being 'sympathetic' means you comfort someone whose family died. If someone is easy to like, they are 'likable'."
      },
      {
        cz: "Nervózní",
        category: "social",
        trap: "Nervous",
        trap_meaning: "Mít trému před zkouškou / být roztřesený obavami (anxious, apprehensive)",
        correct: "Irritable / Agitated / Tense / Stressed / Edgy",
        ex_wrong: "❌ 'The angry plant manager was very nervous and shouted at everyone.'",
        ex_correct: "✓ 'The plant manager was irritable / agitated / tense and stressed.'",
        note: "Czech 'nervózní' often means irritable/annoyed. English 'nervous' means shy, scared, or having stage fright before speaking."
      },
      {
        cz: "Host",
        category: "social",
        trap: "Host",
        trap_meaning: "Hostitel – ten, kdo zve ostatní k sobě domů nebo pořádá večírek",
        correct: "Guest / Visitor",
        ex_wrong: "❌ 'The host was staying in our hotel room for three nights.' (Host is the owner of the hotel!)",
        ex_correct: "✓ 'The guest / visitor was staying in our hotel room.'",
        note: "Exact opposite meanings! Czech 'host' is the invited guest; English 'host' is the person welcoming the guests."
      },
      {
        cz: "Gymnázium",
        category: "social",
        trap: "Gymnasium / Gym",
        trap_meaning: "Tělocvična / fitness centrum / posilovna",
        correct: "Grammar school / Academic high school / Preparatory school",
        ex_wrong: "❌ 'After elementary school, I studied for four years at a gymnasium.' (Sounds like you exercised for 4 years!)",
        ex_correct: "✓ 'After elementary school, I attended an academic high school / grammar school.'",
        note: "'Gym' is strictly for lifting weights and sports. The Czech academic school type is a 'grammar school' or 'academic high school'."
      },
      {
        cz: "Hazard",
        category: "social",
        trap: "Hazard",
        trap_meaning: "Nebezpečí / překážka / zdroj rizika (danger, risk factor)",
        correct: "Gambling / Reckless risk-taking / Foolhardiness",
        ex_wrong: "❌ 'He lost all his money in hazard.'",
        ex_correct: "✓ 'He lost all his money in gambling.' / 'That aggressive overtaking was pure reckless driving.'",
        note: "In English, an occupational 'hazard' is a trip hazard or chemical hazard (zdroj nebezpečí). Gambling is 'gambling'."
      },
      {
        cz: "Smoking (oděv)",
        category: "social",
        trap: "Smoking",
        trap_meaning: "Kouření cigaret / dým (inhaling tobacco)",
        correct: "Tuxedo (US) / Dinner jacket (UK) / Black tie",
        ex_wrong: "❌ 'The invitation says men must wear smoking to the gala.'",
        ex_correct: "✓ 'The invitation says men must wear a tuxedo / dinner jacket to the gala.'",
        note: "While 19th-century gentlemen wore 'smoking jackets', today's formal evening wear is a 'tuxedo' or 'dinner jacket'."
      },
      {
        cz: "Kombinéza",
        category: "social",
        trap: "Combination",
        trap_meaning: "Kombinace / sloučení / směsice několika prvků",
        correct: "Overalls / Boilersuit / Jumpsuit / Flight suit",
        ex_wrong: "❌ 'The maintenance engineer put on his combination before entering the cleanroom.'",
        ex_correct: "✓ 'The maintenance engineer put on his overalls / boilersuit.'",
        note: "One-piece protective industrial workwear is 'overalls' or 'a boilersuit'."
      },
      {
        cz: "Pasta (zubní / technická)",
        category: "daily",
        trap: "Pasta",
        trap_meaning: "Italské těstoviny (špagety, penne, makarony)",
        correct: "Toothpaste (dental) OR Paste / Compound (technical)",
        ex_wrong: "❌ 'I brushed my teeth with mint pasta this morning.'",
        ex_correct: "✓ 'I brushed my teeth with mint toothpaste this morning.'",
        note: "English 'pasta' is exclusively cooked Italian wheat noodles. Cleaning teeth uses 'toothpaste'."
      },
      {
        cz: "Preservativ",
        category: "daily",
        trap: "Preservative",
        trap_meaning: "Konzervační látka v potravinách (E-čka proti kažení jídla)",
        correct: "Condom (contraceptive)",
        ex_wrong: "❌ 'This strawberry jam contains 100% natural preservatives.' (Don't confuse this in Czech!)",
        ex_correct: "✓ In English: 'Food preservatives extend shelf life.' / For contraception: 'condom'.",
        note: "A legendary international embarrassment. English 'preservative' = food additive. Contraception = condom."
      },
      {
        cz: "Konfekce",
        category: "daily",
        trap: "Confectionery",
        trap_meaning: "Cukrovinky / bonbony / čokolády / sladkosti",
        correct: "Ready-to-wear clothing / Off-the-rack apparel",
        ex_wrong: "❌ 'She bought a winter coat in the confectionery store.' (A coat among chocolates!)",
        ex_correct: "✓ 'She bought a winter coat at a ready-to-wear clothing store.'",
        note: "'Confectionery' is candy and sweets. Factory-made apparel is 'ready-to-wear clothing'."
      },
      {
        cz: "Dres (sportovní)",
        category: "daily",
        trap: "Dress",
        trap_meaning: "Dámské šaty (one-piece woman's garment)",
        correct: "Jersey / Shirt / Kit (sports)",
        ex_wrong: "❌ 'The football players wore yellow dresses during the match.' (Picture 11 players in yellow frocks!)",
        ex_correct: "✓ 'The football players wore yellow jerseys / yellow shirts.'",
        note: "A sports shirt is a 'jersey' or 'kit'. A 'dress' is female formal/casual clothing."
      },
      {
        cz: "Masivní",
        category: "daily",
        trap: "Massive",
        trap_meaning: "Obrovský / monumentální / gigantický (enormous, colossal)",
        correct: "Solid (wood/metal) / Sturdy / Heavy-duty / Robust",
        ex_wrong: "❌ 'We bought a dining table made of massive oak.' (Sounds like it weighs 10,000 kg!)",
        ex_correct: "✓ 'We bought a dining table made of solid oak.'",
        note: "Czech 'masivní dřevo' is 'solid wood'. In English, 'massive' describes size (a massive skyscraper, massive debt)."
      },
      {
        cz: "List (papíru / stromu)",
        category: "daily",
        trap: "List",
        trap_meaning: "Seznam položek pod sebou (a roster, bulleted list)",
        correct: "Sheet (of paper) / Leaf (of a tree)",
        ex_wrong: "❌ 'Please give me a clean list to take notes.'",
        ex_correct: "✓ 'Please give me a blank sheet of paper to take notes.'",
        note: "Paper comes in 'sheets'. A 'list' is a sequence of names, numbers, or bullet points."
      },
      {
        cz: "Baterka",
        category: "daily",
        trap: "Battery",
        trap_meaning: "Elektrický článek / akumulátor (cell battery)",
        correct: "Flashlight (US) / Torch (UK)",
        ex_wrong: "❌ 'Turn on your battery, it is completely dark in the cellar.'",
        ex_correct: "✓ 'Turn on your flashlight / torch; it is completely dark.'",
        note: "A handheld light is a 'flashlight' or 'torch'. It contains batteries inside it."
      },
      {
        cz: "Afekt",
        category: "social",
        trap: "Affect",
        trap_meaning: "Ovlivnit / působit na něco (verb)",
        correct: "Fit of rage / Emotional frenzy / Violent outburst",
        ex_wrong: "❌ 'The crime was committed in an affect.'",
        ex_correct: "✓ 'The crime was committed in a fit of rage / in the heat of the moment.'",
        note: "English 'affect' is a common verb meaning to influence ('Inflation affects prices')."
      },
      {
        cz: "Paragraf (§)",
        category: "business",
        trap: "Paragraph",
        trap_meaning: "Odstavec v běžném textu (block of text)",
        correct: "Section (§) / Article / Clause",
        ex_wrong: "❌ 'According to paragraph 4 of the commercial contract, penalties apply.'",
        ex_correct: "✓ 'According to Section 4 / Article 4 of the contract, penalties apply.'",
        note: "In legal English, § is a 'Section'. A 'paragraph' is just an indented block of prose in an essay or book."
      },
      {
        cz: "Fyzický",
        category: "daily",
        trap: "Physique",
        trap_meaning: "Tělesná stavba těla / postava (muscular build)",
        correct: "Physical (bodily, tangible, material)",
        ex_wrong: "❌ 'We must do a physique inspection of the raw inventory.'",
        ex_correct: "✓ 'We must conduct a physical inspection of the raw inventory.'",
        note: "'Physique' is a noun for someone's body shape ('an athletic physique'). The adjective is 'physical'."
      },
      {
        cz: "Konzerva",
        category: "daily",
        trap: "Preserve / Conserve",
        trap_meaning: "Zavařenina / marmeláda / džem s celým ovocem",
        correct: "Can / Tin (tinned food, canned meat/tuna)",
        ex_wrong: "❌ 'Take three conserves of meat for our camping trip.'",
        ex_correct: "✓ 'Take three cans / tins of meat for our camping trip.'",
        note: "Metallic cylindrical containers of food are 'cans' (US) or 'tins' (UK). English 'conserve' is whole fruit jam."
      }
    ];

    // 25 Diagnostic Quiz Items
    const QUIZ_QUESTIONS = [
      {
        q: "1. Right now, our production department is _______ a new automated quality sensor on the converting line.",
        options: [
          { text: "A) testing / inspecting", correct: true },
          { text: "B) controlling", correct: false },
          { text: "C) reclaiming", correct: false }
        ],
        explanation: "✓ In English, checking parameters or quality is 'inspecting / testing'. 'Control' means to govern, regulate, or dominate (e.g. control the machine speed)."
      },
      {
        q: "2. The export manager clarified: '_______, our warehouse in Poland is operating at 95% capacity.'",
        options: [
          { text: "A) Actually", correct: false },
          { text: "B) Currently / At present", correct: true },
          { text: "C) Eventually", correct: false }
        ],
        explanation: "✓ Czech 'aktuálně' is 'currently' or 'at present'. 'Actually' means 've skutečnosti/vlastně' and is used to correct misunderstandings."
      },
      {
        q: "3. When the dairy customer received punctured lids, they immediately submitted a formal _______ to our sales team.",
        options: [
          { text: "A) reclamation", correct: false },
          { text: "B) customer complaint / claim", correct: true },
          { text: "C) concourse", correct: false }
        ],
        explanation: "✓ Czech 'reklamace' is never 'reclamation' in English. It is a 'customer complaint' or 'warranty/quality claim'."
      },
      {
        q: "4. In our meeting, the supervisor was very _______ and welcomed all our team's proposals with a warm smile.",
        options: [
          { text: "A) sympathetic", correct: false },
          { text: "B) likable / pleasant / friendly", correct: true },
          { text: "C) nervous", correct: false }
        ],
        explanation: "✓ Czech 'sympatický' translates to 'likable, pleasant, or friendly'. 'Sympathetic' in English means showing pity or compassion for grief/tragedy."
      },
      {
        q: "5. We can deliver the first pallet tomorrow morning, or _______ on Monday if your receiving dock is closed.",
        options: [
          { text: "A) eventually", correct: false },
          { text: "B) alternatively / if necessary", correct: true },
          { text: "C) actually", correct: false }
        ],
        explanation: "✓ Czech 'eventuálně' means 'alternatively/possibly/if needed'. 'Eventually' in English means 'in the end / after a long wait'."
      },
      {
        q: "6. Our maintenance technician put on his cleanroom _______ before entering the sterile packaging suite.",
        options: [
          { text: "A) combination", correct: false },
          { text: "B) overalls / boilersuit", correct: true },
          { text: "C) dress", correct: false }
        ],
        explanation: "✓ Protective one-piece workwear is 'overalls' or a 'boilersuit'. 'Combination' is an abstract mixture."
      },
      {
        q: "7. When entering the plant floor, the food auditor reminded everyone: 'Safety glasses and earplugs _______ be worn.'",
        options: [
          { text: "A) must", correct: true },
          { text: "B) don't have to", correct: false },
          { text: "C) shouldn't", correct: false }
        ],
        explanation: "✓ Mandatory statutory requirement in industrial safety requires 'must'."
      },
      {
        q: "8. During high school, Petr had a summer _______ at a local brewery packaging line.",
        options: [
          { text: "A) brigade", correct: false },
          { text: "B) temporary part-time job", correct: true },
          { text: "C) promotion", correct: false }
        ],
        explanation: "✓ Czech 'brigáda' is a 'temporary / part-time student job'. 'Brigade' in English is a military detachment or the Fire Brigade!"
      },
      {
        q: "9. The entire engineering team attended Jan's _______ at Brno University of Technology.",
        options: [
          { text: "A) promotion", correct: false },
          { text: "B) graduation ceremony", correct: true },
          { text: "C) ordination", correct: false }
        ],
        explanation: "✓ Czech 'promoce' is a 'university graduation ceremony'. English 'promotion' is getting a higher job rank at work."
      },
      {
        q: "10. In the second half, the football players swapped their sweat-soaked _______ for fresh ones.",
        options: [
          { text: "A) dresses", correct: false },
          { text: "B) jerseys / shirts", correct: true },
          { text: "C) combinations", correct: false }
        ],
        explanation: "✓ Czech 'sportovní dres' is a 'jersey' or 'shirt'. English 'dress' is a woman's one-piece gown!"
      },
      {
        q: "11. The executive dining table was handcrafted from _______ American walnut.",
        options: [
          { text: "A) massive", correct: false },
          { text: "B) solid", correct: true },
          { text: "C) physical", correct: false }
        ],
        explanation: "✓ Czech 'masivní dřevo' is 'solid wood'. In English, 'massive' means colossal/huge in size."
      },
      {
        q: "12. The plant manager was feeling _______ and shouted at the operators because the line stopped twice.",
        options: [
          { text: "A) nervous", correct: false },
          { text: "B) irritable / agitated / tense", correct: true },
          { text: "C) sympathetic", correct: false }
        ],
        explanation: "✓ Czech 'nervózní' often means bad-tempered, stressed, or irritable. English 'nervous' means anxious/jittery before an exam or speech."
      },
      {
        q: "13. Please write your summary on a blank _______ of paper.",
        options: [
          { text: "A) list", correct: false },
          { text: "B) sheet", correct: true },
          { text: "C) transparent", correct: false }
        ],
        explanation: "✓ A piece of paper is a 'sheet'. A 'list' is a bulleted sequence of items (e.g. a shopping list)."
      },
      {
        q: "14. We must pay the supplier's _______ before the end of the 30-day payment term.",
        options: [
          { text: "A) fracture", correct: false },
          { text: "B) invoice / bill", correct: true },
          { text: "C) evidence", correct: false }
        ],
        explanation: "✓ Czech 'faktura' is an 'invoice'. 'Fracture' is a cracked bone!"
      },
      {
        q: "15. The maintenance crew carries a high-power _______ for inspecting dark crawlspaces under the furnace.",
        options: [
          { text: "A) battery", correct: false },
          { text: "B) flashlight / torch", correct: true },
          { text: "C) hazard", correct: false }
        ],
        explanation: "✓ A handheld light source is a 'flashlight' (US) or 'torch' (UK). The 'battery' is the chemical cell inside it."
      },
      {
        q: "16. After prolonged negotiations, the foreign distributor _______ agreed to our revised price formula.",
        options: [
          { text: "A) eventually / in the end", correct: true },
          { text: "B) actually", correct: false },
          { text: "C) possibly", correct: false }
        ],
        explanation: "✓ English 'eventually' means 'in the end after a long struggle/wait'."
      },
      {
        q: "17. 'Who was that person at your reception desk?' — 'He was a visiting _______ from our German subsidiary.'",
        options: [
          { text: "A) host", correct: false },
          { text: "B) guest / visitor", correct: true },
          { text: "C) chef", correct: false }
        ],
        explanation: "✓ Exact opposites! Czech 'host' = English 'guest'. In English, the 'host' is the person who lives there and welcomes guests!"
      },
      {
        q: "18. The HR director keeps strict _______ of all overtime hours and weekend call-outs.",
        options: [
          { text: "A) evidence", correct: false },
          { text: "B) records / logs", correct: true },
          { text: "C) concourse", correct: false }
        ],
        explanation: "✓ Administrative tracking is 'records' or 'logs'. English 'evidence' is strictly legal/criminal proof."
      },
      {
        q: "19. The restaurant menu proudly highlighted that all jams were cooked without artificial _______.",
        options: [
          { text: "A) preservatives", correct: true },
          { text: "B) condoms", correct: false },
          { text: "C) pastes", correct: false }
        ],
        explanation: "✓ Food additives preventing spoilage are 'preservatives'. Contraception is 'condom'."
      },
      {
        q: "20. The electrical technician conducted the required annual safety _______ on all transformers.",
        options: [
          { text: "A) revision", correct: false },
          { text: "B) inspection / audit", correct: true },
          { text: "C) reclaim", correct: false }
        ],
        explanation: "✓ Technical safety check is an 'inspection'. 'Revision' in English is amending a document or studying for exams."
      },
      {
        q: "21. According to _______ 4.2 of the supply agreement, late deliveries incur a 1% daily penalty.",
        options: [
          { text: "A) paragraph", correct: false },
          { text: "B) Section / Article / Clause", correct: true },
          { text: "C) transparent", correct: false }
        ],
        explanation: "✓ In legal contracts, § is a 'Section', 'Article', or 'Clause'. A 'paragraph' is just an indented text block."
      },
      {
        q: "22. The hotel was booked solid because a medical conference was being _______ in the main hall.",
        options: [
          { text: "A) realized", correct: false },
          { text: "B) held / hosted / organized", correct: true },
          { text: "C) absolved", correct: false }
        ],
        explanation: "✓ Events and conferences are 'held', 'hosted', or 'organized'. English 'realize' means to understand mentally."
      },
      {
        q: "23. Before the black-tie charity dinner, the director rented a tailored _______.",
        options: [
          { text: "A) smoking", correct: false },
          { text: "B) tuxedo / dinner jacket", correct: true },
          { text: "C) confectionery", correct: false }
        ],
        explanation: "✓ Men's formal black-tie attire is a 'tuxedo' or 'dinner jacket'. 'Smoking' is smoking tobacco!"
      },
      {
        q: "24. The striker converted the penalty into the bottom left corner, but VAR _______ whether he was offside.",
        options: [
          { text: "A) checked / reviewed", correct: true },
          { text: "B) controlled", correct: false },
          { text: "C) reclaimed", correct: false }
        ],
        explanation: "✓ VAR officials 'check' or 'review' incidents. They do not 'control' them."
      },
      {
        q: "25. Because of wet leaves on the track, the commuter train suffered an unexpected _______.",
        options: [
          { text: "A) delay", correct: true },
          { text: "B) defect", correct: false },
          { text: "C) reclamation", correct: false }
        ],
        explanation: "✓ Schedule lateness is a 'delay'. A 'defect' is a physical flaw in a manufactured product."
      }
    ];

    // Rendering Engine
    function renderCards(filter = 'all', query = '') {
      const container = document.getElementById('cards-container');
      container.innerHTML = '';

      const q = query.toLowerCase().trim();
      const filtered = FALSE_FRIENDS_DATA.filter(item => {
        const matchesCat = (filter === 'all' || item.category === filter);
        const matchesQuery = !q || 
          item.cz.toLowerCase().includes(q) ||
          item.trap.toLowerCase().includes(q) ||
          item.correct.toLowerCase().includes(q) ||
          item.trap_meaning.toLowerCase().includes(q) ||
          item.note.toLowerCase().includes(q);
        return matchesCat && matchesQuery;
      });

      document.getElementById('count-cards').innerText = filtered.length;

      if (filtered.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">
            <h3>No false friends matched your search</h3>
            <p>Try searching for words like 'kontrolovat', 'actually', 'chef', 'reklamace', or 'evidence'.</p>
          </div>
        `;
        return;
      }

      filtered.forEach(item => {
        const card = document.createElement('article');
        card.className = 'ff-card';
        card.setAttribute('data-cat', item.category);

        const catNames = {
          business: '💼 Business & Office',
          roles: '👔 Job Titles & Roles',
          social: '🗣️ Social & Personality',
          daily: '🛒 Daily Life & Objects'
        };

        card.innerHTML = `
          <div class="ff-card-top"></div>
          <div>
            <div class="ff-category-badge">${catNames[item.category] || item.category}</div>
            <div class="ff-cz-head">${item.cz} <span>(Czech thought)</span></div>

            <div class="comparison-box">
              <div class="comp-row">
                <span class="label-wrong">⚠️ TRAP:</span>
                <strong style="color: var(--danger); font-family: monospace; font-size: 1rem;">${item.trap}</strong>
              </div>
              <div style="font-size: 0.82rem; color: var(--text-muted); margin-left: 73px; margin-bottom: 8px;">
                Means: <em>${item.trap_meaning}</em>
              </div>

              <div class="comp-row">
                <span class="label-correct">✓ SAY THIS:</span>
                <strong style="color: var(--success); font-size: 0.98rem;">${item.correct}</strong>
              </div>
            </div>

            <div class="ff-examples">
              <div class="ex-wrong">${item.ex_wrong}</div>
              <div class="ex-correct">${item.ex_correct}</div>
            </div>
          </div>

          <div class="ff-note">
            💡 <strong>Why?</strong> ${item.note}
          </div>
        `;
        container.appendChild(card);
      });
    }

    function renderMatrix() {
      const tbody = document.getElementById('matrix-body');
      tbody.innerHTML = '';

      FALSE_FRIENDS_DATA.forEach(item => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="tag-cz">${item.cz}</td>
          <td class="tag-trap">${item.trap}</td>
          <td style="color: #64748b;">${item.trap_meaning}</td>
          <td class="tag-real">${item.correct}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Quiz State
    let quizAnswers = new Array(QUIZ_QUESTIONS.length).fill(null);

    function renderQuiz() {
      const container = document.getElementById('quiz-list');
      container.innerHTML = '';

      QUIZ_QUESTIONS.forEach((qItem, idx) => {
        const itemCard = document.createElement('div');
        itemCard.className = 'quiz-item-card';
        itemCard.id = `quiz-card-${idx}`;

        let optionsHtml = '';
        qItem.options.forEach((opt, optIdx) => {
          optionsHtml += `
            <button class="quiz-btn" id="btn-${idx}-${optIdx}" onclick="handleQuizAnswer(${idx}, ${optIdx}, ${opt.correct})">
              ${opt.text}
            </button>
          `;
        });

        itemCard.innerHTML = `
          <div class="quiz-num">Item ${idx + 1} of 25</div>
          <div class="quiz-question">${qItem.q}</div>
          <div class="quiz-options">
            ${optionsHtml}
          </div>
          <div class="quiz-feedback" id="feedback-${idx}">
            ${qItem.explanation}
          </div>
        `;
        container.appendChild(itemCard);
      });
      updateScore();
    }

    function handleQuizAnswer(qIdx, optIdx, isCorrect) {
      if (quizAnswers[qIdx] !== null) return; // already answered
      quizAnswers[qIdx] = isCorrect;

      const card = document.getElementById(`quiz-card-${qIdx}`);
      const btn = document.getElementById(`btn-${qIdx}-${optIdx}`);
      const feedback = document.getElementById(`feedback-${qIdx}`);

      // Disable buttons for this question
      QUIZ_QUESTIONS[qIdx].options.forEach((opt, i) => {
        const b = document.getElementById(`btn-${qIdx}-${i}`);
        b.disabled = true;
        if (opt.correct) {
          b.classList.add('show-correct');
        }
      });

      if (isCorrect) {
        btn.classList.add('chosen-correct');
        card.classList.add('answered-correct');
        feedback.className = 'quiz-feedback show correct-fb';
      } else {
        btn.classList.add('chosen-wrong');
        card.classList.add('answered-wrong');
        feedback.className = 'quiz-feedback show wrong-fb';
      }

      updateScore();
    }

    function updateScore() {
      const answered = quizAnswers.filter(a => a !== null).length;
      const correct = quizAnswers.filter(a => a === true).length;
      const pct = answered === 0 ? 0 : Math.round((correct / answered) * 100);

      document.getElementById('score-display').innerText = `Score: ${correct} / 25 (${pct}%)`;

      if (answered === QUIZ_QUESTIONS.length) {
        showQuizSummary(correct);
      }
    }

    function showQuizSummary(score) {
      const sumBox = document.getElementById('quiz-summary');
      const title = document.getElementById('summary-title');
      const text = document.getElementById('summary-text');

      sumBox.style.display = 'block';

      if (score >= 23) {
        title.innerText = '🏆 Czenglish Master Detective!';
        text.innerText = `Outstanding! You scored ${score} out of 25 (92%+). You have exceptional sensitivity to false friends and speak with natural, idiomatic precision.`;
      } else if (score >= 18) {
        title.innerText = '🥈 Fluent Professional';
        text.innerText = `Well done! You scored ${score} out of 25 (${Math.round((score/25)*100)}%). A solid command of business English with only a few tricky false friends remaining to polish.`;
      } else if (score >= 12) {
        title.innerText = '🥉 False Friend Apprentice';
        text.innerText = `You scored ${score} out of 25. You have a good base, but several subtle false friends (like control vs inspect, or actually vs currently) are slipping into your English.`;
      } else {
        title.innerText = '📖 High False Friend Risk';
        text.innerText = `You scored ${score} out of 25. Many Czech literal translations are causing interference. Review the Tutorial tab to eliminate these false friend traps!`;
      }

      sumBox.scrollIntoView({ behavior: 'smooth' });
    }

    function resetQuiz() {
      quizAnswers = new Array(QUIZ_QUESTIONS.length).fill(null);
      document.getElementById('quiz-summary').style.display = 'none';
      renderQuiz();
      document.getElementById('quiz-list').scrollIntoView({ behavior: 'smooth' });
    }

    // Tabs
    function switchTab(tabId) {
      document.getElementById('tab-tutorial').style.display = tabId === 'tutorial' ? 'block' : 'none';
      document.getElementById('tab-quiz').style.display = tabId === 'quiz' ? 'block' : 'none';
      document.getElementById('tab-table').style.display = tabId === 'table' ? 'block' : 'none';

      document.querySelectorAll('.tab-btn').forEach((btn, i) => {
        const matches = (i === 0 && tabId === 'tutorial') ||
                        (i === 1 && tabId === 'quiz') ||
                        (i === 2 && tabId === 'table');
        btn.classList.toggle('active', matches);
      });
    }

    // Category Filter
    let currentCategory = 'all';
    function filterCategory(cat, btn) {
      currentCategory = cat;
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      renderCards(currentCategory, document.getElementById('search-input').value);
    }

    // Search input listener
    document.getElementById('search-input').addEventListener('input', (e) => {
      renderCards(currentCategory, e.target.value);
    });

    // Init
    renderCards();
    renderMatrix();
    renderQuiz();
  </script>
</body>
</html>"""

    out_file.write_text(html_code, encoding="utf-8")
    print(f"[OK] Generated False Friends Hub: {out_file}")

if __name__ == "__main__":
    build_false_friends_hub()
