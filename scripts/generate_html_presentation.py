import os
import sys

def build_32_slide_html():
    html_path = r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_Presentation.html"

    # We will build the complete 32-slide HTML application
    # Let's write the file out
    with open(html_path, "w", encoding="utf-8") as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Automotive Engineering Mastery: From CAD Concept to Platform Leadership (32 Slides)</title>
  <style>
    :root {
      --bg-dark: #0A192F;
      --bg-surface: #0F2140;
      --bg-card: #152A4A;
      --bg-card-border: #1E3A8A;
      --primary: #0284C7;
      --primary-light: #38BDF8;
      --accent: #F59E0B;
      --teal: #0D9488;
      --rose: #E11D48;
      --indigo: #6366F1;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dark: #0F172A;
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-family);
      background-color: #030712;
      color: var(--text-main);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      user-select: none;
    }

    /* TOP BAR */
    #top-bar {
      position: fixed;
      top: 0; left: 0; right: 0; height: 50px;
      background: rgba(10, 25, 47, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid #1E293B;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 20px; z-index: 100;
    }
    .brand-title {
      font-size: 13px; font-weight: 700; letter-spacing: 0.8px;
      color: var(--primary-light); display: flex; align-items: center; gap: 8px;
    }
    .brand-title span {
      background: var(--bg-card); border: 1px solid var(--primary);
      padding: 2px 7px; border-radius: 4px; font-size: 11px; color: var(--accent);
    }
    .top-controls { display: flex; align-items: center; gap: 10px; }
    .btn {
      background: var(--bg-surface); border: 1px solid #334155;
      color: var(--text-main); font-size: 11.5px; font-weight: 600;
      padding: 5px 12px; border-radius: 5px; cursor: pointer;
      display: inline-flex; align-items: center; gap: 5px; transition: all 0.2s ease;
    }
    .btn:hover { background: var(--primary); border-color: var(--primary-light); color: #fff; }
    .btn-active { background: var(--primary); border-color: var(--primary-light); }
    .timer-badge {
      font-family: "Courier New", Courier, monospace; font-size: 13px; font-weight: 700;
      background: #020617; padding: 3px 8px; border-radius: 5px;
      border: 1px solid #334155; color: var(--accent); display: flex; align-items: center; gap: 5px;
    }

    /* STAGE */
    #presentation-stage {
      position: absolute; top: 50px; bottom: 46px; left: 0; right: 0;
      display: flex; align-items: center; justify-content: center;
      background: #060B14; padding: 14px;
    }
    .slide-viewport {
      width: 100%; max-width: 1380px; height: 100%; max-height: 775px;
      aspect-ratio: 16 / 9; background: var(--bg-dark);
      border-radius: 10px; border: 1px solid #1E293B;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      position: relative; overflow: hidden; display: none; flex-direction: column;
    }
    .slide-viewport.active {
      display: flex; animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.985); }
      to { opacity: 1; transform: scale(1); }
    }

    /* INTERIOR */
    .slide-header {
      padding: 18px 32px 10px 32px; border-bottom: 1px solid #1E293B; flex-shrink: 0;
    }
    .slide-category {
      font-size: 10.5px; font-weight: 800; letter-spacing: 1.5px;
      color: var(--primary-light); text-transform: uppercase; margin-bottom: 3px;
    }
    .slide-title { font-size: 23px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.4px; }
    .slide-content {
      padding: 18px 32px; flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 14px;
    }

    /* GRIDS */
    .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; height: 100%; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; height: 100%; }
    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; height: 100%; }
    .grid-5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; }
    .grid-6 { display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; }

    .card {
      background: var(--bg-surface); border: 1px solid #1E293B;
      border-radius: 8px; padding: 14px 16px; display: flex; flex-direction: column;
      position: relative; overflow: hidden;
    }
    .card-stripe { position: absolute; top: 0; left: 0; right: 0; height: 4px; }
    .card-title { font-size: 13.5px; font-weight: 700; color: #FFFFFF; margin-top: 4px; margin-bottom: 2px; }
    .card-subtitle { font-size: 10.5px; font-weight: 700; color: var(--primary-light); text-transform: uppercase; margin-bottom: 10px; }

    .bullet-list {
      list-style: none; display: flex; flex-direction: column; gap: 7px;
      font-size: 11.5px; color: #CBD5E1; line-height: 1.4;
    }
    .bullet-list li { position: relative; padding-left: 14px; }
    .bullet-list li::before { content: "•"; position: absolute; left: 0; color: var(--primary-light); font-weight: bold; }

    .sub-item { margin-bottom: 9px; }
    .sub-item-header { font-size: 12px; font-weight: 700; color: #F1F5F9; margin-bottom: 2px; }
    .sub-item-desc { font-size: 10.5px; color: #94A3B8; line-height: 1.35; }

    /* TITLE SLIDE */
    .title-stage {
      display: flex; flex-direction: column; justify-content: center;
      height: 100%; padding: 36px 54px; position: relative;
    }
    .title-hero { border-left: 6px solid var(--primary); padding-left: 24px; margin-bottom: 28px; }
    .title-eyebrow { font-size: 12px; font-weight: 800; letter-spacing: 2px; color: var(--accent); text-transform: uppercase; margin-bottom: 8px; }
    .title-main { font-size: 38px; font-weight: 900; line-height: 1.15; color: #FFFFFF; margin-bottom: 10px; }
    .title-desc { font-size: 15.5px; color: #94A3B8; max-width: 900px; line-height: 1.45; }

    /* COMPARISON ROWS */
    .comp-row {
      background: var(--bg-surface); border: 1px solid #1E293B;
      border-radius: 7px; display: grid; grid-template-columns: 220px 1fr 1fr;
      padding: 10px 14px; gap: 14px; align-items: center;
    }
    .comp-label { font-size: 11.5px; font-weight: 800; color: var(--accent); }
    .comp-col-ford h4, .comp-col-vw h4 { font-size: 11px; font-weight: 700; margin-bottom: 2px; }
    .comp-col-ford h4 { color: var(--primary-light); }
    .comp-col-vw h4 { color: var(--teal); }
    .comp-col-ford p, .comp-col-vw p { font-size: 10.5px; color: #CBD5E1; line-height: 1.3; }

    /* BOTTOM BAR */
    #bottom-bar {
      position: fixed; bottom: 0; left: 0; right: 0; height: 46px;
      background: #0A192F; border-top: 1px solid #1E293B;
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 20px; z-index: 100;
    }
    .nav-controls { display: flex; align-items: center; gap: 8px; }
    .progress-container {
      flex: 1; max-width: 480px; margin: 0 20px; height: 5px;
      background: #1E293B; border-radius: 3px; overflow: hidden;
    }
    .progress-bar {
      height: 100%; background: linear-gradient(90deg, var(--primary), var(--accent));
      width: 3.125%; transition: width 0.25s ease;
    }
    .slide-counter { font-size: 12px; font-weight: 700; color: #94A3B8; min-width: 80px; text-align: right; }

    /* NOTES DRAWER */
    #notes-drawer {
      position: fixed; right: -520px; top: 50px; bottom: 46px; width: 500px;
      background: #0A1324; border-left: 1px solid #1E293B;
      box-shadow: -10px 0 30px rgba(0,0,0,0.6);
      transition: right 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 95; display: flex; flex-direction: column; padding: 20px;
    }
    #notes-drawer.open { right: 0; }
    .notes-header {
      display: flex; align-items: center; justify-content: space-between;
      margin-bottom: 12px; border-bottom: 1px solid #1E293B; padding-bottom: 10px;
    }
    .notes-title { font-size: 13px; font-weight: 800; color: var(--accent); }
    .notes-body {
      flex: 1; overflow-y: auto; font-size: 13px; line-height: 1.55;
      color: #E2E8F0; white-space: pre-wrap; padding-right: 8px;
    }

    /* OVERVIEW MODAL */
    #overview-modal {
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(3, 7, 18, 0.94); backdrop-filter: blur(10px);
      z-index: 200; display: none; padding: 50px 30px; overflow-y: auto;
    }
    #overview-modal.open { display: block; }
    .overview-grid {
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;
      max-width: 1400px; margin: 0 auto;
    }
    .thumb-card {
      background: var(--bg-surface); border: 1px solid #334155;
      border-radius: 6px; padding: 12px; cursor: pointer; transition: all 0.2s ease;
      display: flex; flex-direction: column; gap: 4px;
    }
    .thumb-card:hover {
      border-color: var(--primary-light); transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(2, 132, 199, 0.2);
    }
    .thumb-num { font-size: 10px; font-weight: 800; color: var(--accent); }
    .thumb-title { font-size: 11.5px; font-weight: 700; color: #FFFFFF; }

    /* PRINT */
    @media print {
      body { overflow: visible !important; height: auto !important; background: #fff !important; color: #000 !important; }
      #top-bar, #bottom-bar, #notes-drawer, #overview-modal { display: none !important; }
      #presentation-stage { position: static !important; display: block !important; padding: 0 !important; background: transparent !important; }
      .slide-viewport {
        display: flex !important; page-break-after: always; break-after: page;
        width: 100% !important; height: 100vh !important; max-width: none !important; max-height: none !important;
        border: none !important; border-radius: 0 !important; box-shadow: none !important;
        background: #0A192F !important; color: #fff !important;
      }
    }
  </style>
</head>
<body>

  <!-- TOP BAR -->
  <header id="top-bar">
    <div class="brand-title">
      AUTOMOTIVE ENGINEERING <span>32-SLIDE MASTER RETROSPECTIVE</span>
    </div>
    <div class="top-controls">
      <div class="timer-badge" id="timer-display">⏱ 30:00</div>
      <button class="btn" id="btn-timer" title="Start / Pause Countdown">Start Timer</button>
      <button class="btn" id="btn-reset-timer" title="Reset to 30:00">Reset</button>
      <button class="btn" id="btn-notes" title="Toggle Presenter Notes (P)">Notes (P)</button>
      <button class="btn" id="btn-overview" title="Slide Grid (O)">Slide Grid (O)</button>
    </div>
  </header>

  <!-- PRESENTATION MAIN STAGE -->
  <main id="presentation-stage">
''')

        # We will loop through 32 slides and inject their HTML markup!
        # Let's inspect the slide definitions:
        # We will write out each of the 32 slides in detail!
        pass

    print("HTML generator initialized")

if __name__ == "__main__":
    build_32_slide_html()
