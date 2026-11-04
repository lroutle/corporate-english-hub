import sys
from pathlib import Path

def generate_html_deck(output_html_path):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vojtěch Berger | Aluminium Packaging Quality & Football Grammar Deck</title>
  <style>
    :root {
      --bg-primary: #0b132b;
      --bg-card: #1c2541;
      --bg-card-hover: #222f54;
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #94a3b8;
      --primary: #0284c7;
      --primary-light: #38bdf8;
      --accent-emerald: #10b981;
      --accent-emerald-glow: rgba(16, 185, 129, 0.2);
      --accent-gold: #f59e0b;
      --accent-rose: #ef4444;
      --border-subtle: rgba(255, 255, 255, 0.12);
      --border-glow: rgba(56, 189, 248, 0.35);
      --steel: #64748b;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-primary);
      overflow: hidden;
      height: 100vh;
      display: flex;
      flex-direction: column;
      user-select: text;
    }

    /* Presentation Canvas */
    #presentation {
      flex: 1;
      position: relative;
      width: 100%;
      height: 100%;
      overflow-y: auto;
      overflow-x: hidden;
    }

    .slide {
      display: none;
      width: 100%;
      min-height: 100%;
      padding: 40px 70px 90px 70px;
      flex-direction: column;
      justify-content: flex-start;
      opacity: 0;
      transform: translateY(14px);
      transition: opacity 0.35s ease, transform 0.35s ease;
    }

    .slide.active {
      display: flex;
      opacity: 1;
      transform: translateY(0);
    }

    /* Badges & Headers */
    .badge {
      display: inline-block;
      align-self: flex-start;
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      background: rgba(56, 189, 248, 0.12);
      color: var(--primary-light);
      border: 1px solid var(--primary-light);
      margin-bottom: 14px;
    }

    .badge-emerald {
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
      border-color: var(--accent-emerald);
    }

    .badge-gold {
      background: rgba(245, 158, 11, 0.15);
      color: var(--accent-gold);
      border-color: var(--accent-gold);
    }

    .badge-rose {
      background: rgba(239, 68, 68, 0.15);
      color: var(--accent-rose);
      border-color: var(--accent-rose);
    }

    h1 {
      font-size: 2.7rem;
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 12px;
      background: linear-gradient(135deg, #ffffff 40%, var(--primary-light) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    h2 {
      font-size: 2.1rem;
      font-weight: 700;
      margin-bottom: 8px;
      color: #ffffff;
    }

    p.subtitle {
      font-size: 1.12rem;
      color: var(--text-muted);
      max-width: 950px;
      line-height: 1.5;
      margin-bottom: 24px;
    }

    /* Grids & Cards */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-top: 10px;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 20px;
      margin-top: 10px;
    }

    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 22px 24px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.35);
      position: relative;
    }

    .card.highlight {
      border-color: var(--primary-light);
      box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
    }

    .card h3 {
      font-size: 1.25rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .card ul {
      list-style: none;
      margin-top: 10px;
    }

    .card li {
      font-size: 0.98rem;
      color: var(--text-secondary);
      margin-bottom: 10px;
      line-height: 1.45;
      display: flex;
      align-items: flex-start;
    }

    .card li::before {
      content: "•";
      color: var(--primary-light);
      font-size: 1.4rem;
      line-height: 1;
      margin-right: 10px;
    }

    .formula-box {
      background: rgba(56, 189, 248, 0.08);
      border: 1px dashed var(--primary-light);
      border-radius: 8px;
      padding: 10px 14px;
      margin: 12px 0;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.9rem;
      color: #bae6fd;
      line-height: 1.4;
    }

    /* Interactive Quiz Test Box */
    .test-box {
      background: #151f38;
      border: 1px solid var(--border-subtle);
      border-left: 5px solid var(--primary-light);
      padding: 16px 20px;
      border-radius: 10px;
      margin-bottom: 16px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    }

    .test-box.emerald { border-left-color: var(--accent-emerald); }
    .test-box.gold { border-left-color: var(--accent-gold); }
    .test-box.rose { border-left-color: var(--accent-rose); }

    .test-box-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }

    .test-box strong {
      color: var(--accent-gold);
      font-size: 0.88rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .test-prompt {
      font-size: 1.05rem;
      color: #f1f5f9;
      line-height: 1.5;
      margin-bottom: 12px;
    }

    .options-grid {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    .option-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text-secondary);
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.92rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-align: left;
    }

    .option-btn:hover {
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--primary-light);
      color: #ffffff;
      transform: translateY(-1px);
    }

    .option-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: var(--accent-emerald) !important;
      color: #ffffff !important;
      font-weight: 700;
      box-shadow: 0 0 12px var(--accent-emerald-glow);
    }

    .option-btn.wrong {
      background: rgba(239, 68, 68, 0.25) !important;
      border-color: var(--accent-rose) !important;
      color: #fca5a5 !important;
      text-decoration: line-through;
    }

    .explanation-panel {
      display: none;
      margin-top: 12px;
      padding: 10px 14px;
      background: rgba(16, 185, 129, 0.08);
      border-left: 3px solid var(--accent-emerald);
      border-radius: 6px;
      font-size: 0.88rem;
      color: #a7f3d0;
      line-height: 1.45;
    }

    .explanation-panel.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Error Spotting Cards */
    .trap-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 14px 18px;
      margin-bottom: 12px;
    }

    .trap-wrong {
      color: #f87171;
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 4px;
    }

    .trap-correct {
      color: #34d399;
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 6px;
      display: none;
    }

    .trap-note {
      color: var(--text-muted);
      font-size: 0.85rem;
      font-style: italic;
      display: none;
    }

    .trap-card.revealed .trap-correct,
    .trap-card.revealed .trap-note {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    .btn-toggle-trap {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-subtle);
      color: #bae6fd;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.78rem;
      cursor: pointer;
      margin-top: 6px;
    }

    .btn-toggle-trap:hover {
      background: var(--primary);
      color: #fff;
    }

    /* Navigation Footer Bar */
    #footer-bar {
      height: 65px;
      background: rgba(11, 19, 43, 0.98);
      backdrop-filter: blur(10px);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 40px;
      z-index: 1000;
      position: relative;
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn-nav {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .btn-nav:hover {
      background: var(--primary);
      border-color: var(--primary-light);
      transform: translateY(-1px);
    }

    .slide-select {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: #ffffff;
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
    }

    .slide-select option {
      background: var(--bg-primary);
      color: #fff;
    }

    .progress-container {
      flex: 1;
      max-width: 320px;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 9999px;
      overflow: hidden;
      margin: 0 24px;
    }

    #progress-bar {
      height: 100%;
      width: 5.26%;
      background: linear-gradient(90deg, var(--primary) 0%, var(--accent-emerald) 100%);
      transition: width 0.3s ease;
    }

    #slide-counter {
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--text-muted);
      min-width: 90px;
      text-align: right;
    }

    /* Print / Responsive adjustments */
    @media (max-width: 900px) {
      .grid-2, .grid-3 { grid-template-columns: 1fr; }
      .slide { padding: 24px 20px 80px 20px; }
      h1 { font-size: 2.1rem; }
      h2 { font-size: 1.6rem; }
      #footer-bar { padding: 0 16px; }
      .progress-container { display: none; }
    }
  </style>
</head>
<body>

<div id="presentation">

  <!-- ========================================== -->
  <!-- SLIDE 1: Title Slide -->
  <!-- ========================================== -->
  <div class="slide active">
    <span class="badge">AL INVEST BŘIDLIČNÁ • DIVIZE OBALY • QUALITY ENGINEERING</span>
    <h1>Executive Technical Grammar & Diagnostic Deck</h1>
    <p class="subtitle">Tailored Language Architecture for Aluminium Food Packaging Quality Engineering & World Sports (Football Analytics)</p>
    
    <div class="grid-3" style="margin-top: 10px;">
      <div class="card highlight">
        <h3>👤 Assessed Specialist</h3>
        <p style="font-size: 1.3rem; font-weight: 800; color: #fff; margin-bottom: 6px;">Vojtěch Berger</p>
        <p style="font-size: 0.92rem; color: var(--primary-light); font-weight: 600;">Specialista kvality – divize Obaly</p>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-top: 4px;">Quality Engineer – Packaging Division</p>
        <div class="formula-box" style="margin-top: 14px;">
          AL INVEST Břidličná, a.s.<br>
          ✉️ Vojtech.Berger@alinvest.cz<br>
          📞 +420 554 222 017 | 📱 +420 720 980 043
        </div>
      </div>

      <div class="card">
        <h3>🏭 Packaging & Quality Core</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 10px;">Industrial workflows in aluminium converting:</p>
        <ul>
          <li>Foil rolling & thickness gauge tolerances (µm)</li>
          <li>Pinhole detection, surface tension & Dyne test</li>
          <li>Lamination (Alu/PE/PET) & heat-seal peel testing</li>
          <li>BRCGS Packaging & FSSC 22000 food safety</li>
          <li>8D Problem Solving, CAPA & NCR reports</li>
        </ul>
      </div>

      <div class="card">
        <h3>⚽ World Sports & Football</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 10px;">Tactical strategy, analytics & debate:</p>
        <ul>
          <li>High-intensity pressing vs low defensive blocks</li>
          <li>Champions League, Premier League & EURO analysis</li>
          <li>VAR protocols, semi-automated offside & IFAB rules</li>
          <li>Transfer market dynamics & Expected Goals (xG)</li>
          <li>High-stakes post-match argument formulation</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 2: Agenda (50/50 Dual-Domain Framework) -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-emerald">Diagnostic & Assessment Framework</span>
    <h2>Session Roadmap: The 50/50 Executive Structure</h2>
    <p class="subtitle">A structured 60-minute framework balancing professional fluency with surgical grammatical screening.</p>

    <div class="grid-2">
      <div class="card">
        <h3 style="color: var(--primary-light);">Part 1: Spoken Audit & Rapport (30 min)</h3>
        <ul>
          <li><strong>00–05m: Introduction & Background:</strong> Warm-up, professional scope at AL INVEST Břidličná, and daily responsibilities in Divize Obaly.</li>
          <li><strong>05–15m: Packaging Operations & Inspection:</strong> Walkthrough of bare vs converted foil, lacquering, lamination, and BRCGS food safety protocols.</li>
          <li><strong>15–25m: Football Passions & Tactical Debate:</strong> Favored teams, tactical formations (4-3-3 pressing vs 5-4-1 low block), and modern refereeing tech (VAR).</li>
          <li><strong>25–30m: High-Stakes Dilemma Simulation:</strong> Spontaneous resolution of an urgent snack packaging delamination complaint vs a disputed penalty.</li>
        </ul>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-emerald);">Part 2: Diagnostic & Applied Grammar (30 min)</h3>
        <ul>
          <li><strong>30–45m: The 18-Point Diagnostic Screening:</strong> Tailored interactive questions testing tenses, passives, conditionals, modals, and prepositions.</li>
          <li><strong>45–52m: Top 6 "Czenglish" Traps:</strong> Spotting and eliminating classic interference errors (<em>control vs inspect</em>, <em>reklamace</em>, <em>since/for</em>).</li>
          <li><strong>52–56m: High-Impact Deep Dives:</strong> Audit-ready Passive Voice in 8D reports and Conditionals in packaging tolerances and pitch tactics.</li>
          <li><strong>56–60m: Strength Profile & Syllabus:</strong> Synthesizing observations into a concrete personalized training trajectory for Vojtěch.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 3: Spoken Audit 1 - Packaging Quality -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge">Part 1 • Spoken Diagnostic</span>
    <h2>Spoken Audit 1: Daily Quality Operations at AL INVEST</h2>
    <p class="subtitle">Evaluating routine technical reporting, active inspection processes, and terminology precision.</p>

    <div class="grid-2">
      <div class="card">
        <h3>Prompt 1: Foil Converting & Inspection Routines</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "Could you introduce your responsibilities as a Quality Engineer in the Packaging Division? What types of aluminium packaging does AL INVEST manufacture, and what do your routine shift checks involve?"
        </p>
        <div class="formula-box">
          Target Focus: Present Simple for SOP routines • 3rd person singular '-s' • Converting terminology: bare foil, lacquering, slitting, dyne level, gauge (µm).
        </div>
      </div>

      <div class="card">
        <h3>Prompt 2: Food Contact Standards & Audit Compliance</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "How long have you been working in quality engineering at AL INVEST, and how do international standards like BRCGS Packaging or FSSC 22000 shape your daily packaging releases?"
        </p>
        <div class="formula-box">
          Target Focus: Present Perfect (since / for) vs Past Simple • Regulatory modals: must comply, shall ensure • Food migration limits & hygiene controls.
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 4: Spoken Audit 2 - Football Passion -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-gold">Part 1 • Spoken Diagnostic</span>
    <h2>Spoken Audit 2: World Football Passion & Tactical Philosophy</h2>
    <p class="subtitle">Evaluating conversational agility, comparative arguments, and passionate debate in sports.</p>

    <div class="grid-2">
      <div class="card">
        <h3>Prompt 3: Club Allegiances & International Competitions</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "Which domestic and international football clubs do you follow most passionately? What makes following them compelling, and how do you rate their current season?"
        </p>
        <div class="formula-box">
          Target Focus: Expressing preference & emotion • Comparatives & Superlatives (e.g. <em>far more disciplined than...</em>) • Frequency adverbs • European fixtures.
        </div>
      </div>

      <div class="card">
        <h3>Prompt 4: Pressing Systems vs Low Blocks</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "From a tactical standpoint, do you admire high-intensity gegenpressing (like Klopp or Guardiola) or compact, structured defensive low blocks? What makes a team's setup succeed?"
        </p>
        <div class="formula-box">
          Target Focus: Nuanced opinion phrases • 1st & 2nd Conditionals • Tactical concepts: inverted wingers, pressing triggers, transitional turnovers, Expected Goals (xG).
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 5: Spoken Audit 3 - 8D & Defect Investigation -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-rose">Part 1 • Spoken Diagnostic</span>
    <h2>Spoken Audit 3: Non-Conformance & Root Cause Analysis</h2>
    <p class="subtitle">Testing narrative past tenses, defect terminology, and formal 8D problem-solving formulations.</p>

    <div class="grid-2">
      <div class="card">
        <h3>Prompt 5: Narrative of a Defect Incident</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "Can you describe a challenging packaging defect, customer complaint, or line stoppage you investigated? What happened on the slitting or lacquering line, and how did you detect it?"
        </p>
        <div class="formula-box">
          Target Focus: Past Continuous + Past Simple (interrupted actions) • Time linkers (<em>while, suddenly, subsequently</em>) • Defects: pinholes, delamination, lacquer wrinkles.
        </div>
      </div>

      <div class="card">
        <h3>Prompt 6: Presenting 8D Containment & CAPA to Clients</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "When submitting an 8D report to a multinational food brand (e.g. Nestlé or Danone), how do you explain the containment actions and permanent corrective measures in English?"
        </p>
        <div class="formula-box">
          Target Focus: Objective Passive Voice (<em>The batch was quarantined...</em>) • Present Perfect for completed fixes (<em>We have upgraded the optical sensor...</em>) • Reassuring tone.
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 6: Spoken Audit 4 - VAR & Technological Officiating -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-emerald">Part 1 • Spoken Diagnostic</span>
    <h2>Spoken Audit 4: Technology & High-Stakes Officiating (VAR)</h2>
    <p class="subtitle">Exploring argumentative nuance, modals of deduction, and hypothetical rule reforms.</p>

    <div class="grid-2">
      <div class="card">
        <h3>Prompt 7: VAR & Semi-Automated Offside Technology</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "Do you believe VAR and semi-automated offside technology have made football fairer, or have they damaged the raw emotion and spontaneous flow of celebrating a goal?"
        </p>
        <div class="formula-box">
          Target Focus: Balancing opposing viewpoints (<em>On the one hand... whereas on the other...</em>) • Officiating terms: clear & obvious error, pitchside monitor, handball law.
        </div>
      </div>

      <div class="card">
        <h3>Prompt 8: If You Were President of IFAB...</h3>
        <p style="font-size: 1.15rem; color: #fff; line-height: 1.5; margin-bottom: 12px;">
          "If IFAB (the International Football Association Board) invited you to modify or eliminate one single rule in world football, which rule would you reform and why?"
        </p>
        <div class="formula-box">
          Target Focus: Second Conditional (<em>If I had the power, I would introduce...</em>) • Modal hedging • Innovations: orange cards (sin bins), effective game clock.
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 7: Diagnostic Grammar 1 - Tenses -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge">Diagnostic Screening • Items 1 – 3</span>
    <h2>Technical Grammar 1: Tense Differentiation</h2>
    <p class="subtitle">Test items combining packaging quality operations with football match narratives. Click an option to check.</p>

    <!-- Item 1 -->
    <div class="test-box">
      <div class="test-box-header">
        <strong>1. Routine SOP vs Active Complaint (Present Simple vs Continuous)</strong>
      </div>
      <p class="test-prompt">Right now our quality team _______ a customer complaint regarding pinholes in a coffee foil laminate, but normally we _______ standard tensile sampling every two hours.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-1')">A) investigates / are conducting</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-1')">B) is investigating / conduct</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-1')">C) investigates / conduct</button>
      </div>
      <div class="explanation-panel" id="exp-1">
        ✓ <strong>Correct!</strong> <em>Right now</em> requires Present Continuous (<em>is investigating</em>) for a temporary active task. <em>Normally</em> signals a routine standard procedure, requiring Present Simple (<em>conduct</em>).
      </div>
    </div>

    <!-- Item 2 -->
    <div class="test-box">
      <div class="test-box-header">
        <strong>2. Incident Interruption during Converting (Past Continuous + Past Simple)</strong>
      </div>
      <p class="test-prompt">While the operator _______ the web tension at 350 m/min, the optical pinhole detector suddenly _______ an emergency audio alarm.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-2')">A) was monitoring / triggered</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-2')">B) monitored / was triggering</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-2')">C) was monitoring / was triggering</button>
      </div>
      <div class="explanation-panel" id="exp-2">
        ✓ <strong>Correct!</strong> The background ongoing action uses Past Continuous (<em>was monitoring</em>), while the sudden event interrupting it uses Past Simple (<em>triggered</em>).
      </div>
    </div>

    <!-- Item 3 -->
    <div class="test-box">
      <div class="test-box-header">
        <strong>3. Professional Tenure & Career Evolution (Present Perfect vs Past Simple)</strong>
      </div>
      <p class="test-prompt">Vojtěch _______ as a quality specialist in packaging for four years now, but before joining AL INVEST he _______ automotive component testing.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-3')">A) worked / has managed</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-3')">B) has worked (or has been working) / managed</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-3')">C) is working / managed</button>
      </div>
      <div class="explanation-panel" id="exp-3">
        ✓ <strong>Correct!</strong> Unfinished time continuing to the present with <em>for four years now</em> requires Present Perfect. The completed past role before joining AL INVEST requires Past Simple (<em>managed</em>).
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 8: Diagnostic Grammar 2 - Passive Voice -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-emerald">Diagnostic Screening • Items 4 – 6</span>
    <h2>Technical Grammar 2: Passive Voice in Quality Audits & Sports</h2>
    <p class="subtitle">The passive voice provides objective, audit-ready technical reports. Click an option to test.</p>

    <!-- Item 4 -->
    <div class="test-box emerald">
      <div class="test-box-header">
        <strong>4. Laboratory Inspection & Degreasing (Present Simple Passive)</strong>
      </div>
      <p class="test-prompt">Before the bare aluminium coil is converted into food packaging, its tensile strength _______ and its surface _______ to guarantee lacquer adhesion.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-4')">A) is tested / is degreased</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-4')">B) tests / degreases</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-4')">C) are tested / is degreasing</button>
      </div>
      <div class="explanation-panel" id="exp-4">
        ✓ <strong>Correct!</strong> <em>Tensile strength is tested</em> and <em>surface is degreased</em>. In technical specifications, the passive voice places focus on the material and parameter, not the operator.
      </div>
    </div>

    <!-- Item 5 -->
    <div class="test-box emerald">
      <div class="test-box-header">
        <strong>5. Football Match Disciplinary Action (Past Passive)</strong>
      </div>
      <p class="test-prompt">Following an on-field VAR review in the 74th minute, the opposing defender _______ with a straight red card and three penalty points _______ from the club.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-5')">A) was dismissed / were deducted</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-5')">B) dismissed / deducted</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-5')">C) was dismissing / was deducted</button>
      </div>
      <div class="explanation-panel" id="exp-5">
        ✓ <strong>Correct!</strong> Singular subject (<em>the defender was dismissed</em>) + plural subject (<em>three penalty points were deducted</em>). Standard sports governance passive.
      </div>
    </div>

    <!-- Item 6 -->
    <div class="test-box emerald">
      <div class="test-box-header">
        <strong>6. Batch Quarantine & 8D Containment (Present Perfect Passive)</strong>
      </div>
      <p class="test-prompt">All suspect reels from batch #2026-B _______ in the warehouse until the micro-leakage report _______ by the accredited external laboratory.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-6')">A) have quarantined / will complete</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-6')">B) have been quarantined / has been completed</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-6')">C) are quarantined / completed</button>
      </div>
      <div class="explanation-panel" id="exp-6">
        ✓ <strong>Correct!</strong> <em>Have been quarantined</em> indicates completed containment action whose state remains active now. <em>Has been completed</em> in the time clause indicates future completion.
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 9: Diagnostic Grammar 3 - Conditionals -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-gold">Diagnostic Screening • Items 7 – 9</span>
    <h2>Technical Grammar 3: Conditionals in Quality Specs & Tactics</h2>
    <p class="subtitle">Expressing physical tolerances, production guarantees, and tactical pitch contingencies.</p>

    <!-- Item 7 -->
    <div class="test-box gold">
      <div class="test-box-header">
        <strong>7. Zero Conditional: Scientific Laws of Foil Permeability</strong>
      </div>
      <p class="test-prompt">If the thickness of the barrier aluminium layer _______ below 6.35 microns, the pinhole density _______ according to international packaging physics.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-7')">A) falls / will rise</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-7')">B) falls / rises</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-7')">C) will fall / rises</button>
      </div>
      <div class="explanation-panel" id="exp-7">
        ✓ <strong>Correct!</strong> Zero Conditional (If + Present Simple, Present Simple) expresses universal physical laws and unchanging technical facts.
      </div>
    </div>

    <!-- Item 8 -->
    <div class="test-box gold">
      <div class="test-box-header">
        <strong>8. First Conditional: Customer Claim Protocol</strong>
      </div>
      <p class="test-prompt">If the customer's incoming lab _______ delamination between the foil and the PE film, our plant _______ a replacement batch within 48 hours.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-8')">A) detects / will dispatch</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-8')">B) will detect / dispatches</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-8')">C) detects / dispatches</button>
      </div>
      <div class="explanation-panel" id="exp-8">
        ✓ <strong>Correct!</strong> First Conditional (If + Present Simple, will + verb) describes realistic contractual guarantees and future possibilities. Never put <em>will</em> in the <em>if</em>-clause!
      </div>
    </div>

    <!-- Item 9 -->
    <div class="test-box gold">
      <div class="test-box-header">
        <strong>9. Second Conditional: Hypothetical Quality Investment</strong>
      </div>
      <p class="test-prompt">If AL INVEST _______ 100% optical camera inspection on all slitting lines, we _______ customer claims by over 40%.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-9')">A) installs / would reduce</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-9')">B) installed / would reduce</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-9')">C) installed / will reduce</button>
      </div>
      <div class="explanation-panel" id="exp-9">
        ✓ <strong>Correct!</strong> Second Conditional (If + Past Simple, would + base verb) describes imaginary or hypothetical operational upgrades.
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 10: Diagnostic Grammar 4 - 3rd Conditional & Past Modals -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-rose">Diagnostic Screening • Items 10 – 12</span>
    <h2>Technical Grammar 4: 8D Root Cause & Match Retrospectives</h2>
    <p class="subtitle">Evaluating unchangeable past scenarios in quality investigations and tournament history.</p>

    <!-- Item 10 -->
    <div class="test-box rose">
      <div class="test-box-header">
        <strong>10. Third Conditional: Root Cause Prevention in Packaging</strong>
      </div>
      <p class="test-prompt">If the slitter operator _______ the dull cutting knives at the scheduled interval, the aluminium web _______ on the customer's high-speed packing line.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-10')">A) replaced / wouldn't tear</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-10')">B) had replaced / wouldn't have torn</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-10')">C) had replaced / wouldn't tear</button>
      </div>
      <div class="explanation-panel" id="exp-10">
        ✓ <strong>Correct!</strong> Third Conditional (If + had + V3, would have + V3) analyzes unchangeable past events in 8D D4 root cause retrospectives.
      </div>
    </div>

    <!-- Item 11 -->
    <div class="test-box rose">
      <div class="test-box-header">
        <strong>11. Third Conditional: Stoppage-Time Penalty Drama</strong>
      </div>
      <p class="test-prompt">If the striker _______ the penalty in stoppage time, the club _______ directly for the Champions League knockout stage.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-11')">A) had converted / would have qualified</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-11')">B) converted / would qualify</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-11')">C) had converted / qualified</button>
      </div>
      <div class="explanation-panel" id="exp-11">
        ✓ <strong>Correct!</strong> Past hypothetical situation in football history: <em>If he had converted... they would have qualified</em>.
      </div>
    </div>

    <!-- Item 12 -->
    <div class="test-box rose">
      <div class="test-box-header">
        <strong>12. Past Modals of Deduction: Investigating Defect Causes</strong>
      </div>
      <p class="test-prompt">The heat-seal lacquer failed the peel test; the drying tunnel temperature _______ below the specified curing threshold during the night shift.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-12')">A) must drop</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-12')">B) must have dropped</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-12')">C) should drop</button>
      </div>
      <div class="explanation-panel" id="exp-12">
        ✓ <strong>Correct!</strong> <em>Must have dropped</em> expresses logical deduction of near certainty about a past event based on physical evidence.
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 11: Diagnostic Grammar 5 - Modals & Regulations -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge">Diagnostic Screening • Items 13 – 15</span>
    <h2>Technical Grammar 5: Modals of Obligation & Food Safety Rules</h2>
    <p class="subtitle">Distinguishing strict legal requirements, prohibitions, and absence of obligation.</p>

    <!-- Item 13 -->
    <div class="test-box">
      <div class="test-box-header">
        <strong>13. Food Contact Legislation: EU Regulation (EC) 1935/2004</strong>
      </div>
      <p class="test-prompt">Under EU food contact law, packaging materials _______ not transfer their constituents to food in quantities that could endanger human health.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-13')">A) must / shall</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-13')">B) can</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-13')">C) might</button>
      </div>
      <div class="explanation-panel" id="exp-13">
        ✓ <strong>Correct!</strong> Strict statutory obligation requires <em>must not</em> or formal legislative <em>shall not</em>.
      </div>
    </div>

    <!-- Item 14 -->
    <div class="test-box">
      <div class="test-box-header">
        <strong>14. Football Officiating Protocol: Absence of Obligation vs Duty</strong>
      </div>
      <p class="test-prompt">The match referee _______ consult the pitchside VAR monitor for routine fouls, but he _______ review any direct red-card incident.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-14')">A) mustn't / should</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-14')">B) doesn't have to / must</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-14')">C) can't / has to</button>
      </div>
      <div class="explanation-panel" id="exp-14">
        ✓ <strong>Correct!</strong> <em>Doesn't have to</em> means there is no obligation (it is optional/unnecessary). <em>Must</em> expresses mandatory duty.
      </div>
    </div>

    <!-- Item 15 -->
    <div class="test-box">
      <div class="test-box-header">
        <strong>15. BRCGS Packaging Audit Preparation (Strict Prohibition)</strong>
      </div>
      <p class="test-prompt">Quality inspectors _______ store unapproved chemical solvent bottles near open food-contact packaging reels under any circumstances.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-15')">A) don't have to</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-15')">B) must not</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-15')">C) shouldn't</button>
      </div>
      <div class="explanation-panel" id="exp-15">
        ✓ <strong>Correct!</strong> <em>Must not</em> is mandatory prohibition. <em>Don't have to</em> only means it is not necessary!
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 12: Diagnostic Grammar 6 - Prepositions & Collocations -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-emerald">Diagnostic Screening • Items 16 – 18</span>
    <h2>Technical Grammar 6: Prepositions & Essential Collocations</h2>
    <p class="subtitle">Preposition accuracy is the primary marker of natural executive English.</p>

    <!-- Item 16 -->
    <div class="test-box emerald">
      <div class="test-box-header">
        <strong>16. Compliance & Engineering Responsibilities</strong>
      </div>
      <p class="test-prompt">As a quality specialist, Vojtěch is responsible _______ ensuring full compliance _______ BRCGS Packaging standards across all lines.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-16')">A) for / with</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-16')">B) of / to</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-16')">C) about / in</button>
      </div>
      <div class="explanation-panel" id="exp-16">
        ✓ <strong>Correct!</strong> <em>Responsible FOR</em> + noun/gerund; <em>Compliance WITH</em> (or <em>compliant with</em>).
      </div>
    </div>

    <!-- Item 17 -->
    <div class="test-box emerald">
      <div class="test-box-header">
        <strong>17. Football Match Transition & Positioning</strong>
      </div>
      <p class="test-prompt">The counter-attacking goal originated _______ a turnover _______ midfield, catching the backline completely out of position.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-17')">A) in / on</button>
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-17')">B) from / in</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-17')">C) with / at</button>
      </div>
      <div class="explanation-panel" id="exp-17">
        ✓ <strong>Correct!</strong> <em>Originate FROM</em>; <em>IN midfield</em> (compare with: <em>ON the wing / ON the pitch</em>).
      </div>
    </div>

    <!-- Item 18 -->
    <div class="test-box emerald">
      <div class="test-box-header">
        <strong>18. Customer Claim Management & Settlement</strong>
      </div>
      <p class="test-prompt">Our technical team apologized _______ the customer _______ the delayed CoAs and agreed _______ an on-site audit next Tuesday.</p>
      <div class="options-grid">
        <button class="option-btn" onclick="checkAnswer(this, true, 'exp-18')">A) to / for / on (or to)</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-18')">B) with / about / with</button>
        <button class="option-btn" onclick="checkAnswer(this, false, 'exp-18')">C) at / of / for</button>
      </div>
      <div class="explanation-panel" id="exp-18">
        ✓ <strong>Correct!</strong> <em>Apologize TO [person] FOR [issue]</em>; <em>Agree ON [a date] / Agree TO [a proposal]</em>.
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 13: Error Spotting (Czenglish Traps) -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-rose">Error-Spotting Masterclass</span>
    <h2>The Top 6 "Czenglish" Traps in Packaging & Sports</h2>
    <p class="subtitle">Spot the single critical error before the customer or auditor notices! Click the button to inspect the fix.</p>

    <div class="grid-2">
      <!-- Trap 1 -->
      <div class="trap-card" id="trap-1">
        <div class="trap-wrong">❌ "I work as a quality engineer in AL INVEST since three years."</div>
        <div class="trap-correct">✓ "I have been working as a quality engineer at AL INVEST for three years."</div>
        <div class="trap-note">Czech "pracuji od/už 3 roky" requires Present Perfect Continuous + FOR (duration) or SINCE (starting year/date).</div>
        <button class="btn-toggle-trap" onclick="toggleTrap('trap-1')">🔍 Inspect Solution & Rule</button>
      </div>

      <!-- Trap 2 -->
      <div class="trap-card" id="trap-2">
        <div class="trap-wrong">❌ "We must control each slit coil for surface defects."</div>
        <div class="trap-correct">✓ "We must inspect / check / examine each slit coil for surface defects."</div>
        <div class="trap-note">False Friend: 'Control' means to govern/regulate. Checking product quality is 'inspect, check, audit, or test'.</div>
        <button class="btn-toggle-trap" onclick="toggleTrap('trap-2')">🔍 Inspect Solution & Rule</button>
      </div>

      <!-- Trap 3 -->
      <div class="trap-card" id="trap-3">
        <div class="trap-wrong">❌ "The food client sent an urgent reclamation about pinholes."</div>
        <div class="trap-correct">✓ "The food client submitted an urgent complaint / claim regarding pinholes."</div>
        <div class="trap-note">False Friend: 'Reclamation' means land recovery or recycling. Czech 'reklamace' is a customer complaint or claim.</div>
        <button class="btn-toggle-trap" onclick="toggleTrap('trap-3')">🔍 Inspect Solution & Rule</button>
      </div>

      <!-- Trap 4 -->
      <div class="trap-card" id="trap-4">
        <div class="trap-wrong">❌ "The referee should to review the penalty incident on the monitor."</div>
        <div class="trap-correct">✓ "The referee should review the penalty incident on the monitor."</div>
        <div class="trap-note">Modal verbs (should, must, can, could, would) are always followed directly by the bare infinitive (never 'to').</div>
        <button class="btn-toggle-trap" onclick="toggleTrap('trap-4')">🔍 Inspect Solution & Rule</button>
      </div>

      <!-- Trap 5 -->
      <div class="trap-card" id="trap-5">
        <div class="trap-wrong">❌ "Our engineering team will discuss about the heat-seal issue tomorrow."</div>
        <div class="trap-correct">✓ "Our engineering team will discuss the heat-seal issue tomorrow."</div>
        <div class="trap-note">'Discuss' is a transitive verb in English — never say 'discuss about' (compare: 'talk about' vs 'discuss [topic]').</div>
        <button class="btn-toggle-trap" onclick="toggleTrap('trap-5')">🔍 Inspect Solution & Rule</button>
      </div>

      <!-- Trap 6 -->
      <div class="trap-card" id="trap-6">
        <div class="trap-wrong">❌ "If the coach will change the tactical formation, they will score."</div>
        <div class="trap-correct">✓ "If the coach changes the tactical formation, they will score."</div>
        <div class="trap-note">In 1st conditionals, the condition clause (with 'if') takes Present Simple, NEVER 'will'.</div>
        <button class="btn-toggle-trap" onclick="toggleTrap('trap-6')">🔍 Inspect Solution & Rule</button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 14: Deep Dive - Present Perfect vs Past Simple -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-gold">Targeted Technical Review</span>
    <h2>Grammar Deep Dive: Present Perfect vs Past Simple</h2>
    <p class="subtitle">The definitive golden rule for quality audit reports, plant updates, and tournament retrospectives.</p>

    <div class="grid-2">
      <div class="card" style="border-left: 5px solid var(--accent-gold);">
        <h3 style="color: var(--accent-gold);">Past Simple: Finished Time Period</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 12px;">
          Use when the time period is completely finished or tied to a specific past date/timestamp.
        </p>
        <div class="formula-box">
          yesterday, in 2024, last week, three shifts ago, during the morning audit
        </div>
        <ul style="margin-top: 14px;">
          <li>✓ <em>"We recalibrated the optical pinhole sensors on line 3 yesterday morning."</em></li>
          <li>✓ <em>"The customer submitted their audit report on May 14th."</em></li>
          <li>✓ <em>"Spain won the UEFA European Championship in July 2024."</em></li>
          <li>✓ <em>"The slitter operator stopped the web immediately when tension dropped."</em></li>
        </ul>
      </div>

      <div class="card" style="border-left: 5px solid var(--accent-emerald);">
        <h3 style="color: var(--accent-emerald);">Present Perfect: Status Up to Now</h3>
        <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 12px;">
          Use when the time is open/ongoing, or the past action directly impacts current plant operations.
        </p>
        <div class="formula-box">
          so far, already, recently, since, this week, yet, up to now
        </div>
        <ul style="margin-top: 14px;">
          <li>✓ <em>"We have already inspected 14 master coils this morning."</em></li>
          <li>✓ <em>"Have you received the laboratory CoA for the lacquering lot yet?"</em></li>
          <li>✓ <em>"AL INVEST has maintained BRCGS Packaging certification for years."</em></li>
          <li>✓ <em>"The striker has scored 12 goals so far this season."</em></li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 15: Deep Dive - Active vs Passive in 8D Reports -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-emerald">Targeted Technical Review</span>
    <h2>Grammar Deep Dive: The Passive Voice in 8D Reports</h2>
    <p class="subtitle">Transforming conversational or blame-oriented statements into objective, audit-grade documentation.</p>

    <div class="grid-2">
      <div class="card" style="border-left: 5px solid var(--accent-rose);">
        <h3 style="color: var(--accent-rose);">❌ Conversational Active (Avoid in Audits)</h3>
        <ul>
          <li><strong>"The forklift driver dropped the master coil."</strong><br><span style="color: var(--text-muted); font-size: 0.88rem;">Focuses personal blame rather than packaging integrity and containment.</span></li>
          <li><strong>"We tested the peel strength at 180°C."</strong><br><span style="color: var(--text-muted); font-size: 0.88rem;">Sounds informal and conversational rather than standard test documentation.</span></li>
          <li><strong>"Somebody forgot to clean the lacquering roller."</strong><br><span style="color: var(--text-muted); font-size: 0.88rem;">Unacceptable in formal customer-facing 8D non-conformance reports.</span></li>
          <li><strong>"The referee made a catastrophic mistake."</strong><br><span style="color: var(--text-muted); font-size: 0.88rem;">Emotional journalism rather than objective analytical commentary.</span></li>
        </ul>
      </div>

      <div class="card" style="border-left: 5px solid var(--accent-emerald);">
        <h3 style="color: var(--accent-emerald);">✓ Objective Audit Passive (Recommended)</h3>
        <ul>
          <li><strong>"The master coil was damaged during internal transport."</strong><br><span style="color: var(--accent-emerald); font-size: 0.88rem;">Focuses objectively on material status and containment requirement.</span></li>
          <li><strong>"Heat-seal peel strength was evaluated at 180°C (DIN 55529)."</strong><br><span style="color: var(--accent-emerald); font-size: 0.88rem;">Establishes institutional rigor, standard test methods, and precision.</span></li>
          <li><strong>"Inadequate roller cleaning was identified as the direct root cause."</strong><br><span style="color: var(--accent-emerald); font-size: 0.88rem;">Standard 8D D4 root cause phrasing for multinational brand auditors.</span></li>
          <li><strong>"An on-field decision was reviewed and overturned by VAR."</strong><br><span style="color: var(--accent-emerald); font-size: 0.88rem;">Calm, professional sports governance phrasing.</span></li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 16: Live Case Study 1 - Snack Foil Delamination -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-rose">Extension Bank • Live Case Study</span>
    <h2>Live Case Study 1: The Snack Packaging Delamination Crisis</h2>
    <p class="subtitle">A realistic emergency quality dispute with a multinational food packer.</p>

    <div class="card highlight" style="margin-bottom: 20px;">
      <h3 style="color: var(--primary-light);">The Quality Emergency Scenario</h3>
      <p style="font-size: 1.1rem; line-height: 1.6; color: #ffffff;">
        A tier-one potato chip packer in Poland urgently contacts AL INVEST. During high-speed vertical form-fill-seal (VFFS) packaging at 120 bags/min, the outer PET film is peeling away from the 7 µm aluminium barrier foil, causing seal failures and nitrogen flush leakage. They threaten to halt two packaging lines and claim €45,000 in downtime losses.
      </p>
    </div>

    <div class="grid-3">
      <div class="card">
        <h3 style="color: var(--primary-light);">Step 1: Immediate Containment (D3)</h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 10px;">What actions and language must Vojtěch deploy right away?</p>
        <div class="formula-box">
          • "All reels currently in transit are being quarantined."<br>
          • "Retain samples from batch #308 are being tested right now."
        </div>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-gold);">Step 2: Root Cause (D4)</h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 10px;">How do we explain the 5 Whys without admitting undue liability?</p>
        <div class="formula-box">
          • "If corona treatment had dropped, surface dyne would have fallen below 38."<br>
          • "The solvent ratio might have affected curing."
        </div>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-emerald);">Step 3: Corrective Actions (D5)</h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 10px;">How do we reassure the auditor that the fix is permanent?</p>
        <div class="formula-box">
          • "Adhesion checks have been integrated into hourly inspection sheets."<br>
          • "We will dispatch certified replacement reels tomorrow."
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 17: Live Case Study 2 - Champions League Final VAR -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-gold">Extension Bank • Live Case Study</span>
    <h2>Live Case Study 2: The 89th-Minute Champions League Final VAR</h2>
    <p class="subtitle">A high-stakes football refereeing controversy to test argumentative fluency and diplomatic hedging.</p>

    <div class="card highlight" style="margin-bottom: 20px;">
      <h3 style="color: var(--accent-gold);">The Match Incident Scenario</h3>
      <p style="font-size: 1.1rem; line-height: 1.6; color: #ffffff;">
        In the 89th minute of the UEFA Champions League Final, tied 1-1, a thunderous shot strikes a defender's outstretched arm while they are sliding to block the cross. The ball deflected off their own knee first. The referee waves play on, but the VAR calls him to the pitchside monitor. If awarded, the resulting penalty will decide the European champion.
      </p>
    </div>

    <div class="grid-3">
      <div class="card">
        <h3 style="color: var(--primary-light);">Analysis 1: Law 12 Interpretation</h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 10px;">Was the arm making the body unnaturally bigger?</p>
        <div class="formula-box">
          • "The arm was extended to support his landing."<br>
          • "Because the ball deflected off his own knee first, the contact was accidental."
        </div>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-gold);">Analysis 2: Clear & Obvious Error</h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 10px;">Did this reach the threshold for VAR intervention?</p>
        <div class="formula-box">
          • "If the on-field decision wasn't a clear mistake, VAR shouldn't have intervened."<br>
          • "Subjective handballs should remain the referee's call."
        </div>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-rose);">Analysis 3: Post-Match Fallout</h3>
        <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 10px;">How does the coach express frustration diplomatically?</p>
        <div class="formula-box">
          • "Had the penalty not been awarded, we would have forced extra time."<br>
          • "We respect the officials, but technology needs clearer boundaries."
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 18: Bilingual Domain Reference Glossary -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge">Curriculum Reference & Vocabulary</span>
    <h2>Bilingual Domain Reference: Packaging & Football Terminology</h2>
    <p class="subtitle">Key professional vocabulary for technical meetings, supplier audits, and sports debates.</p>

    <div class="grid-2">
      <div class="card">
        <h3 style="color: var(--primary-light);">🏭 Aluminium Packaging Quality (Czech → English)</h3>
        <div style="font-size: 0.92rem; line-height: 1.7; color: var(--text-secondary);">
          • <strong>Foliová válcovna / Převíjení:</strong> Aluminium rolling mill / Slitting & Rewinding<br>
          • <strong>Tloušťka fólie / Tolerance (µm):</strong> Foil gauge / Thickness tolerance<br>
          • <strong>Poréznost / Mikrodírky:</strong> Pinhole detection / Micro-porosity<br>
          • <strong>Pevnost v tahu / Tažnost:</strong> Tensile strength (Rm) / Elongation at break (A50)<br>
          • <strong>Svarová pevnost / Těsnost:</strong> Heat-seal strength / Seal integrity & peel test<br>
          • <strong>Povrchové napětí (Dyne):</strong> Surface wetting tension (Dyne level / test inks)<br>
          • <strong>Laminace / Lakování:</strong> Lamination (Alu/PE/PET) / Lacquer coating<br>
          • <strong>Reklamace zákazníka:</strong> Customer complaint / Quality claim (NCR)<br>
          • <strong>Nápravná a preventivní opatření:</strong> CAPA (Corrective & Preventive Actions)<br>
          • <strong>Protokol o neshodě (8D):</strong> 8D Problem Solving Report (Containment / Root Cause)
        </div>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-emerald);">⚽ World Sports & Football Analytics (Czech → English)</h3>
        <div style="font-size: 0.92rem; line-height: 1.7; color: var(--text-secondary);">
          • <strong>Vysoký presink / Nízký blok:</strong> High pressing / Compact low defensive block<br>
          • <strong>Přechodová fáze do útoku:</strong> Attacking transition / Counter-attacking turnover<br>
          • <strong>Obranná linie / Ofsajdová past:</strong> Backline defensive line / Offside trap<br>
          • <strong>Očekávané góly (xG):</strong> Expected Goals (xG) / Shot conversion rate<br>
          • <strong>Přezkum videa (VAR):</strong> VAR review / Clear and obvious error protocol<br>
          • <strong>Otočení skóre / Vyrovnání:</strong> Comeback victory / Equalizing goal in stoppage time<br>
          • <strong>Finanční fair play (FFP):</strong> UEFA Financial Fair Play / Squad cost ratio<br>
          • <strong>Čisté konto / Herní vytížení:</strong> Clean sheet / Squad rotation & match fitness<br>
          • <strong>Obrácená křídla / Krajní beci:</strong> Inverted wingers / Overlapping full-backs<br>
          • <strong>Zákaz přestupů / Výkupní klauzule:</strong> Transfer ban / Release buyout clause
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 19: Action Plan & Next Steps -->
  <!-- ========================================== -->
  <div class="slide">
    <span class="badge badge-emerald">Executive Trajectory</span>
    <h1>Action Plan: Tailored Syllabus for Vojtěch Berger</h1>
    <p class="subtitle">Strategic progression roadmap designed for AL INVEST Břidličná packaging quality excellence.</p>

    <div class="grid-2">
      <div class="card highlight">
        <h3 style="color: var(--primary-light);">🎯 Target Competencies</h3>
        <ul>
          <li><strong>Audit-Ready 8D Technical Reporting:</strong> Formulating impersonal passives, root cause statements, and preventative guarantees that satisfy tier-one multinational food brand auditors.</li>
          <li><strong>Conditionals for Physical Tolerances:</strong> Seamlessly deploying 1st, 2nd, and 3rd conditionals when explaining laboratory test tolerances and negotiating claim settlements.</li>
          <li><strong>Spontaneous Spoken Agility:</strong> Eliminating hesitation during unannounced supplier audits, foreign customer visits, and technical dispute conference calls.</li>
          <li><strong>Sports Debate & Rapport Mastery:</strong> Using idiomatic, high-level sports English to build effortless rapport with foreign colleagues and commercial contacts.</li>
        </ul>
      </div>

      <div class="card">
        <h3 style="color: var(--accent-emerald);">📦 Learning Methodology & Tools</h3>
        <ul>
          <li><strong>Interactive Deck Practice:</strong> Continuing to drill the interactive test items and error-spotting cards to consolidate target grammar patterns.</li>
          <li><strong>Real Packaging Case Simulations:</strong> Walking through realistic BRCGS Packaging audits, customer claims, and CoA certifications in English.</li>
          <li><strong>Football Analytics Reviews:</strong> Utilizing tactical articles and match highlights for spontaneous debate and vocabulary expansion.</li>
          <li><strong>Czenglish Eradication:</strong> 5-minute warm-up drills each session to permanently replace false friends (<em>control / inspect, claim / reclamation</em>).</li>
        </ul>
      </div>
    </div>

    <div class="card" style="margin-top: 20px; background: rgba(56, 189, 248, 0.08); border-color: var(--primary-light); padding: 16px 24px;">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div>
          <strong style="color: #ffffff; font-size: 1.05rem;">Assessed Client: Vojtěch Berger | AL INVEST Břidličná, a.s.</strong>
          <p style="color: var(--text-muted); font-size: 0.88rem;">Specialista kvality – divize Obaly | Vojtech.Berger@alinvest.cz</p>
        </div>
        <div style="text-align: right;">
          <strong style="color: var(--accent-emerald); font-size: 1.05rem;">Corporate English Architecture</strong>
          <p style="color: var(--text-muted); font-size: 0.88rem;">Instructor: Lee Routledge</p>
        </div>
      </div>
    </div>
  </div>

</div>

<!-- ========================================== -->
<!-- FOOTER NAVIGATION CONTROLS -->
<!-- ========================================== -->
<div id="footer-bar">
  <div class="nav-controls">
    <button class="btn-nav" id="prev-btn">◀ Previous</button>
    <button class="btn-nav" id="next-btn">Next ▶</button>
    <select class="slide-select" id="slide-select">
      <option value="0">1. Title: Vojtěch Berger</option>
      <option value="1">2. Session Roadmap (50/50)</option>
      <option value="2">3. Spoken Audit 1: Packaging Operations</option>
      <option value="3">4. Spoken Audit 2: Football & Tactics</option>
      <option value="4">5. Spoken Audit 3: 8D & Defect Cases</option>
      <option value="5">6. Spoken Audit 4: Technology & VAR</option>
      <option value="6">7. Diagnostic 1: Tense Differentiation</option>
      <option value="7">8. Diagnostic 2: Passive Voice</option>
      <option value="8">9. Diagnostic 3: Conditionals</option>
      <option value="9">10. Diagnostic 4: 3rd Conditionals</option>
      <option value="10">11. Diagnostic 5: Modals & Food Safety</option>
      <option value="11">12. Diagnostic 6: Prepositions</option>
      <option value="12">13. Error Spotting: Czenglish Traps</option>
      <option value="13">14. Deep Dive: Pres. Perf. vs Past</option>
      <option value="14">15. Deep Dive: Passive in 8D Reports</option>
      <option value="15">16. Case Study 1: Snack Foil Delamination</option>
      <option value="16">17. Case Study 2: Champions League VAR</option>
      <option value="17">18. Bilingual Domain Glossary</option>
      <option value="18">19. Action Plan & Next Steps</option>
    </select>
    <button class="btn-nav" id="fullscreen-btn" title="Toggle Fullscreen (F)">⛶ Fullscreen</button>
  </div>

  <div class="progress-container">
    <div id="progress-bar"></div>
  </div>

  <div id="slide-counter">Slide 01 / 19</div>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const progressBar = document.getElementById('progress-bar');
  const slideCounter = document.getElementById('slide-counter');
  const slideSelect = document.getElementById('slide-select');
  const fullscreenBtn = document.getElementById('fullscreen-btn');
  let currentSlide = 0;

  function updateSlide(index) {
    if (index < 0) index = 0;
    if (index >= slides.length) index = slides.length - 1;
    currentSlide = index;

    slides.forEach((s, i) => {
      s.classList.toggle('active', i === currentSlide);
    });

    const pct = ((currentSlide + 1) / slides.length) * 100;
    progressBar.style.width = pct + '%';
    slideCounter.innerText = `Slide ${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
    slideSelect.value = String(currentSlide);

    // Scroll presentation to top on slide change
    document.getElementById('presentation').scrollTop = 0;
  }

  prevBtn.addEventListener('click', () => {
    if (currentSlide > 0) updateSlide(currentSlide - 1);
  });

  nextBtn.addEventListener('click', () => {
    if (currentSlide < slides.length - 1) updateSlide(currentSlide + 1);
  });

  slideSelect.addEventListener('change', (e) => {
    updateSlide(parseInt(e.target.value, 10));
  });

  fullscreenBtn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen().catch(() => {});
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;

    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      if (currentSlide < slides.length - 1) updateSlide(currentSlide + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      if (currentSlide > 0) updateSlide(currentSlide - 1);
    } else if (e.key === 'Home') {
      updateSlide(0);
    } else if (e.key === 'End') {
      updateSlide(slides.length - 1);
    } else if (e.key === 'f' || e.key === 'F') {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }
  });

  // Interactive Quiz Answer Checker
  function checkAnswer(btn, isCorrect, expId) {
    const parentGrid = btn.closest('.options-grid');
    const buttons = parentGrid.querySelectorAll('.option-btn');
    
    // Disable other buttons once clicked
    buttons.forEach(b => {
      b.classList.remove('correct', 'wrong');
    });

    if (isCorrect) {
      btn.classList.add('correct');
    } else {
      btn.classList.add('wrong');
      // Highlight the correct one
      buttons.forEach(b => {
        if (b.getAttribute('onclick').includes('true')) {
          b.classList.add('correct');
        }
      });
    }

    if (expId) {
      const exp = document.getElementById(expId);
      if (exp) exp.classList.add('active');
    }
  }

  // Toggle Error Spotting Trap Card
  function toggleTrap(cardId) {
    const card = document.getElementById(cardId);
    if (card) {
      card.classList.toggle('revealed');
      const btn = card.querySelector('.btn-toggle-trap');
      if (btn) {
        btn.innerText = card.classList.contains('revealed') ? '▲ Hide Solution' : '🔍 Inspect Solution & Rule';
      }
    }
  }

  updateSlide(0);
</script>
</body>
</html>"""
    
    Path(output_html_path).write_text(html_content, encoding='utf-8')
    print(f"[OK] Generated HTML Deck: {output_html_path}")

if __name__ == "__main__":
    generate_html_deck("Vojtech_Berger_Grammar_Deck.html")
