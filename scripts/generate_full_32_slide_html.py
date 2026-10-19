import os
import json

def build_complete_html():
    out_path = r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_Presentation_Clean.html"

    # We will read speaker notes from the PPTX generator or write out the complete script dictionary!
    # Let's import speaker notes from PPTX generator script:
    notes_dict = {}
    with open(r"C:\tmp\00-Mycat\scripts\generate_automotive_presentation.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # We can extract the notes easily by splitting on set_speaker_notes
    parts = content.split("set_speaker_notes(s")
    for part in parts[1:]:
        slide_idx_str = part.split(",", 1)[0].strip()
        try:
            slide_idx = int(slide_idx_str)
            note_content = part.split('"""', 2)[1].strip()
            notes_dict[slide_idx] = note_content
        except Exception as e:
            pass

    print(f"Extracted speaker notes for {len(notes_dict)} slides.")

    # Now let's write out the full HTML template
    # We will build each slide's interior HTML
    with open(out_path, "w", encoding="utf-8") as f:
        # Write Head & CSS
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
      --primary: #0284C7;
      --primary-light: #38BDF8;
      --accent: #F59E0B;
      --teal: #0D9488;
      --rose: #E11D48;
      --indigo: #6366F1;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-family); background-color: #030712; color: var(--text-main);
      overflow: hidden; height: 100vh; width: 100vw; user-select: none;
    }
    #top-bar {
      position: fixed; top: 0; left: 0; right: 0; height: 48px;
      background: rgba(10, 25, 47, 0.95); backdrop-filter: blur(8px);
      border-bottom: 1px solid #1E293B; display: flex; align-items: center; justify-content: space-between;
      padding: 0 20px; z-index: 100;
    }
    .brand-title {
      font-size: 13px; font-weight: 700; letter-spacing: 0.8px; color: var(--primary-light);
      display: flex; align-items: center; gap: 8px;
    }
    .brand-title span {
      background: var(--bg-card); border: 1px solid var(--primary); padding: 2px 7px;
      border-radius: 4px; font-size: 10.5px; color: var(--accent);
    }
    .top-controls { display: flex; align-items: center; gap: 10px; }
    .btn {
      background: var(--bg-surface); border: 1px solid #334155; color: var(--text-main);
      font-size: 11.5px; font-weight: 600; padding: 5px 12px; border-radius: 5px;
      cursor: pointer; display: inline-flex; align-items: center; gap: 5px; transition: all 0.2s ease;
    }
    .btn:hover { background: var(--primary); border-color: var(--primary-light); color: #fff; }
    .btn-active { background: var(--primary); border-color: var(--primary-light); }
    .timer-badge {
      font-family: "Courier New", Courier, monospace; font-size: 13px; font-weight: 700;
      background: #020617; padding: 3px 8px; border-radius: 5px; border: 1px solid #334155;
      color: var(--accent); display: flex; align-items: center; gap: 5px;
    }
    #presentation-stage {
      position: absolute; top: 48px; bottom: 44px; left: 0; right: 0;
      display: flex; align-items: center; justify-content: center; background: #060B14; padding: 12px;
    }
    .slide-viewport {
      width: 100%; max-width: 1380px; height: 100%; max-height: 775px;
      aspect-ratio: 16 / 9; background: var(--bg-dark); border-radius: 10px;
      border: 1px solid #1E293B; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      position: relative; overflow: hidden; display: none; flex-direction: column;
    }
    .slide-viewport.active { display: flex; animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1); }
    @keyframes fadeIn { from { opacity: 0; transform: scale(0.985); } to { opacity: 1; transform: scale(1); } }
    .slide-header { padding: 16px 30px 10px 30px; border-bottom: 1px solid #1E293B; flex-shrink: 0; }
    .slide-category { font-size: 10px; font-weight: 800; letter-spacing: 1.5px; color: var(--primary-light); text-transform: uppercase; margin-bottom: 2px; }
    .slide-title { font-size: 22px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.4px; }
    .slide-content { padding: 16px 30px; flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; }
    .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; height: 100%; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; height: 100%; }
    .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; height: 100%; }
    .grid-6 { display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px; }
    .grid-5 { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
    .card {
      background: var(--bg-surface); border: 1px solid #1E293B; border-radius: 7px;
      padding: 12px 14px; display: flex; flex-direction: column; position: relative; overflow: hidden;
    }
    .card-stripe { position: absolute; top: 0; left: 0; right: 0; height: 4px; }
    .card-title { font-size: 13px; font-weight: 700; color: #FFFFFF; margin-top: 3px; margin-bottom: 2px; }
    .card-subtitle { font-size: 10px; font-weight: 700; color: var(--primary-light); text-transform: uppercase; margin-bottom: 8px; }
    .bullet-list { list-style: none; display: flex; flex-direction: column; gap: 6px; font-size: 11px; color: #CBD5E1; line-height: 1.35; }
    .bullet-list li { position: relative; padding-left: 13px; }
    .bullet-list li::before { content: "•"; position: absolute; left: 0; color: var(--primary-light); font-weight: bold; }
    .sub-item { margin-bottom: 8px; }
    .sub-item-header { font-size: 11.5px; font-weight: 700; color: #F1F5F9; margin-bottom: 1px; }
    .sub-item-desc { font-size: 10px; color: #94A3B8; line-height: 1.3; }
    .title-stage { display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 32px 48px; position: relative; }
    .title-hero { border-left: 6px solid var(--primary); padding-left: 20px; margin-bottom: 24px; }
    .title-eyebrow { font-size: 11px; font-weight: 800; letter-spacing: 2px; color: var(--accent); text-transform: uppercase; margin-bottom: 6px; }
    .title-main { font-size: 36px; font-weight: 900; line-height: 1.15; color: #FFFFFF; margin-bottom: 8px; }
    .title-desc { font-size: 14.5px; color: #94A3B8; max-width: 900px; line-height: 1.4; }
    .comp-row {
      background: var(--bg-surface); border: 1px solid #1E293B; border-radius: 6px;
      display: grid; grid-template-columns: 200px 1fr 1fr; padding: 9px 12px; gap: 12px; align-items: center;
    }
    .comp-label { font-size: 11px; font-weight: 800; color: var(--accent); }
    .comp-col-ford h4, .comp-col-vw h4 { font-size: 10.5px; font-weight: 700; margin-bottom: 1px; }
    .comp-col-ford h4 { color: var(--primary-light); }
    .comp-col-vw h4 { color: var(--teal); }
    .comp-col-ford p, .comp-col-vw p { font-size: 10px; color: #CBD5E1; line-height: 1.25; }
    #bottom-bar {
      position: fixed; bottom: 0; left: 0; right: 0; height: 44px;
      background: #0A192F; border-top: 1px solid #1E293B;
      display: flex; align-items: center; justify-content: space-between; padding: 0 20px; z-index: 100;
    }
    .nav-controls { display: flex; align-items: center; gap: 8px; }
    .progress-container { flex: 1; max-width: 480px; margin: 0 20px; height: 5px; background: #1E293B; border-radius: 3px; overflow: hidden; }
    .progress-bar { height: 100%; background: linear-gradient(90deg, var(--primary), var(--accent)); width: 3.125%; transition: width 0.25s ease; }
    .slide-counter { font-size: 11.5px; font-weight: 700; color: #94A3B8; min-width: 80px; text-align: right; }
    #notes-drawer {
      position: fixed; right: -520px; top: 48px; bottom: 44px; width: 500px;
      background: #0A1324; border-left: 1px solid #1E293B; box-shadow: -10px 0 30px rgba(0,0,0,0.6);
      transition: right 0.25s cubic-bezier(0.16, 1, 0.3, 1); z-index: 95; display: flex; flex-direction: column; padding: 18px;
    }
    #notes-drawer.open { right: 0; }
    .notes-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px solid #1E293B; padding-bottom: 8px; }
    .notes-title { font-size: 12px; font-weight: 800; color: var(--accent); }
    .notes-body { flex: 1; overflow-y: auto; font-size: 12.5px; line-height: 1.5; color: #E2E8F0; white-space: pre-wrap; padding-right: 6px; }
    #overview-modal {
      position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(3, 7, 18, 0.94);
      backdrop-filter: blur(10px); z-index: 200; display: none; padding: 40px 24px; overflow-y: auto;
    }
    #overview-modal.open { display: block; }
    .overview-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; max-width: 1400px; margin: 0 auto; }
    .thumb-card {
      background: var(--bg-surface); border: 1px solid #334155; border-radius: 5px;
      padding: 10px; cursor: pointer; transition: all 0.2s ease; display: flex; flex-direction: column; gap: 3px;
    }
    .thumb-card:hover { border-color: var(--primary-light); transform: translateY(-2px); box-shadow: 0 8px 20px rgba(2, 132, 199, 0.2); }
    .thumb-num { font-size: 9.5px; font-weight: 800; color: var(--accent); }
    .thumb-title { font-size: 11px; font-weight: 700; color: #FFFFFF; }
    @media print {
      @page { size: landscape; margin: 0; }
      body { overflow: visible !important; height: auto !important; background: #fff !important; color: #000 !important; }
      #top-bar, #bottom-bar, #notes-drawer, #overview-modal { display: none !important; }
      #presentation-stage { position: static !important; display: block !important; padding: 0 !important; background: transparent !important; }
      .slide-viewport {
        display: flex !important; page-break-after: always; break-after: page;
        width: 100vw !important; height: 100vh !important; max-width: none !important; max-height: none !important;
        border: none !important; border-radius: 0 !important; box-shadow: none !important;
        background: #0A192F !important; color: #fff !important;
      }
    }
  </style>
</head>
<body>
  <header id="top-bar">
    <div class="brand-title">AUTOMOTIVE ENGINEERING <span>32-SLIDE MASTER RETROSPECTIVE</span></div>
    <div class="top-controls">
      <div class="timer-badge" id="timer-display">⏱ 30:00</div>
      <button class="btn" id="btn-timer">Start Timer</button>
      <button class="btn" id="btn-reset-timer">Reset</button>
      <button class="btn" id="btn-notes">Notes (P)</button>
      <button class="btn" id="btn-overview">Slide Grid (O)</button>
    </div>
  </header>
  <main id="presentation-stage">
''')

        # SLIDE DEFINITIONS & MARKUP GENERATION
        # We will generate all 32 slides!
        # Slide 1:
        f.write('''
    <!-- SLIDE 1 -->
    <section class="slide-viewport active" id="slide-1" data-title="Executive Introduction" data-time="00:00 - 01:00">
      <div class="title-stage">
        <div class="title-hero">
          <div class="title-eyebrow">AUTOMOTIVE ENGINEERING MASTERY • 32-SLIDE RETROSPECTIVE</div>
          <h1 class="title-main">From CAD Concept to Platform Leadership</h1>
          <p class="title-desc">A 30-Minute Journey Across 12 Landmark Ford & VW Platforms, CAD Evolution & End-to-End Design-to-Manufacture Architecture.</p>
        </div>
        <div class="grid-4" style="height: 130px; flex-shrink: 0;">
          <div class="card" style="border-top: 4px solid var(--primary);">
            <div class="card-subtitle" style="color: var(--primary);">HORIZON 1</div>
            <div class="card-title">CAD DESIGNER</div>
            <p style="font-size: 10.5px; color: #94A3B8;">Parametric 3D CAD, master sections, packaging & GD&T.</p>
          </div>
          <div class="card" style="border-top: 4px solid var(--teal);">
            <div class="card-subtitle" style="color: var(--teal);">HORIZON 2</div>
            <div class="card-title">PROJECT ENGINEER</div>
            <p style="font-size: 10.5px; color: #94A3B8;">Subsystems, DFMEA chairing, FEA & crash CAE.</p>
          </div>
          <div class="card" style="border-top: 4px solid var(--accent);">
            <div class="card-subtitle" style="color: var(--accent);">HORIZON 3</div>
            <div class="card-title">PROJECT MANAGER</div>
            <p style="font-size: 10.5px; color: #94A3B8;">OEM Gateways (GPDS / PEP), tooling capital & prototype fleet.</p>
          </div>
          <div class="card" style="border-top: 4px solid var(--indigo);">
            <div class="card-subtitle" style="color: var(--indigo);">HORIZON 4</div>
            <div class="card-title">ENGINEERING MANAGER</div>
            <p style="font-size: 10.5px; color: #94A3B8;">APQP governance, PSW sign-off, EV migration & team leadership.</p>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 2:
        f.write('''
    <!-- SLIDE 2 -->
    <section class="slide-viewport" id="slide-2" data-title="Four Horizons of Responsibility" data-time="01:00 - 02:00">
      <div class="slide-header">
        <div class="slide-category">CAREER EVOLUTION & SCOPE OF LEADERSHIP • SLIDE 2 / 32</div>
        <h2 class="slide-title">The Four Horizons of Automotive Responsibility</h2>
      </div>
      <div class="slide-content">
        <div class="grid-4">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-subtitle">HORIZON 1</div>
            <div class="card-title">CAD DESIGNER</div>
            <p style="font-size: 10.5px; color: #94A3B8; margin-bottom: 8px;">The Geometry Foundation</p>
            <ul class="bullet-list">
              <li>Parametric solid & surface modeling (CATIA / NX).</li>
              <li>Translating Class-A scans to Class-B structural pressings.</li>
              <li>Kinematic sweeps: suspension jounce & door swing.</li>
              <li>2D drafting compliant with ASME Y14.5 / ISO 1101.</li>
              <li>Datum target definitions (3-2-1 / RPS).</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-subtitle">HORIZON 2</div>
            <div class="card-title">PROJECT ENGINEER</div>
            <p style="font-size: 10.5px; color: #94A3B8; margin-bottom: 8px;">Technical Systems Integration</p>
            <ul class="bullet-list">
              <li>Cross-functional subsystem ownership (BIW & Closures).</li>
              <li>Chairing DFMEAs using P-Diagrams (Ford v4.2).</li>
              <li>Cascading Special Characteristics (∇ CC / SC).</li>
              <li>Coordinating FEA rigidity & LS-DYNA crash solvers.</li>
              <li>Leading DFM/DFA directly with tooling vendors.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-subtitle">HORIZON 3</div>
            <div class="card-title">PROJECT MANAGER</div>
            <p style="font-size: 10.5px; color: #94A3B8; margin-bottom: 8px;">Timing & Capital Execution</p>
            <ul class="bullet-list">
              <li>Gateway execution (Ford GPDS & VW PEP).</li>
              <li>Multi-million-pound hard tooling commitments.</li>
              <li>Managing prototype builds (Mules, VP, TT, PP).</li>
              <li>Root-cause issue containment using 8D & A3 reports.</li>
              <li>Supplier technical delivery & contract governance.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--indigo);"></div>
            <div class="card-subtitle">HORIZON 4</div>
            <div class="card-title">ENGINEERING MANAGER</div>
            <p style="font-size: 10.5px; color: #94A3B8; margin-bottom: 8px;">Strategy, APQP & People</p>
            <ul class="bullet-list">
              <li>Multi-platform resource allocation & engineering budget.</li>
              <li>Technical sign-off on DVP&R and PPAP Warrants (PSW).</li>
              <li>Transitioning teams from ICE to MEB EV architecture.</li>
              <li>Adopting generative AI & accelerated CAE workflows.</li>
              <li>Mentoring junior designers into systems architects.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 3:
        f.write('''
    <!-- SLIDE 3 -->
    <section class="slide-viewport" id="slide-3" data-title="Horizon 1: CAD Designer" data-time="02:00 - 03:00">
      <div class="slide-header">
        <div class="slide-category">GEOMETRY CREATION, PARAMETRICS & 2D RELEASE • SLIDE 3 / 32</div>
        <h2 class="slide-title">Horizon 1 Deep-Dive: The CAD Designer Era</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">PARAMETRIC 3D SOLID & SURFACING</div>
            <div class="card-subtitle">Foundational Geometry</div>
            <div class="sub-item"><div class="sub-item-header">Parametric Feature Trees</div><div class="sub-item-desc">Building associative models in CATIA V4/V5 & NX capturing robust design intent.</div></div>
            <div class="sub-item"><div class="sub-item-header">Class-A to Class-B Offsets</div><div class="sub-item-desc">Translating studio clay scans into structural inner pressings with draft angles.</div></div>
            <div class="sub-item"><div class="sub-item-header">Master Section Development</div><div class="sub-item-desc">Cutting parametric cross-sections across A/B pillars and sills for spot-weld flange access.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">PACKAGING & KINEMATICS</div>
            <div class="card-subtitle">Space Claims & Envelopes</div>
            <div class="sub-item"><div class="sub-item-header">Kinematic Clearance Sweeps</div><div class="sub-item-desc">Dynamic sweeps of wheel jounce/rebound (+100/-80 mm), steering lock & snow chains.</div></div>
            <div class="sub-item"><div class="sub-item-header">SAE J826 H-Point Manikin</div><div class="sub-item-desc">Positioning 95th percentile male / 5th percentile female to establish SgRP & heel coordinates.</div></div>
            <div class="sub-item"><div class="sub-item-header">Vision Envelopes (SAE J941)</div><div class="sub-item-desc">Mapping driver eye ellipses to ensure regulatory direct and mirror field-of-view.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">2D DETAILING & GD&T RELEASE</div>
            <div class="card-subtitle">The Manufacturing Contract</div>
            <div class="sub-item"><div class="sub-item-header">ASME Y14.5 & ISO 1101</div><div class="sub-item-desc">Creating unambiguous manufacturing drawings with Datum Reference Frames (DRFs).</div></div>
            <div class="sub-item"><div class="sub-item-header">3-2-1 Locating Principle</div><div class="sub-item-desc">Constraining all 6 spatial degrees of freedom with primary, secondary, and tertiary datums.</div></div>
            <div class="sub-item"><div class="sub-item-header">Volkswagen RPS System</div><div class="sub-item-desc">Integrating standardized coordinate hole/pad target conventions across stamping assemblies.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 4:
        f.write('''
    <!-- SLIDE 4 -->
    <section class="slide-viewport" id="slide-4" data-title="Horizon 2: Project Engineer" data-time="03:00 - 04:00">
      <div class="slide-header">
        <div class="slide-category">CROSS-FUNCTIONAL INTEGRATION, DFMEA & VIRTUAL CAE • SLIDE 4 / 32</div>
        <h2 class="slide-title">Horizon 2 Deep-Dive: The Project Engineer Era</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">SUBSYSTEM OWNERSHIP</div>
            <div class="card-subtitle">Systems Architecture</div>
            <div class="sub-item"><div class="sub-item-header">Cross-Functional Leadership</div><div class="sub-item-desc">Leading technical integration across BIW, Closures, Chassis subframes, and Exterior trim.</div></div>
            <div class="sub-item"><div class="sub-item-header">Interface Boundary Management</div><div class="sub-item-desc">Protecting physical and kinematic interfaces between Body, Closures, and Powertrain.</div></div>
            <div class="sub-item"><div class="sub-item-header">Supplier DFM Reviews</div><div class="sub-item-desc">Leading on-site feasibility reviews with Tier-1 stamping and injection mould tooling specialists.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">DFMEA & ROBUSTNESS</div>
            <div class="card-subtitle">Risk Mitigation</div>
            <div class="sub-item"><div class="sub-item-header">Parameter Diagrams (P-Diagrams)</div><div class="sub-item-desc">Mapping signal inputs, control factors, and noise factors (thermal soak, aging, tolerances).</div></div>
            <div class="sub-item"><div class="sub-item-header">Ford FMEA Handbook v4.2</div><div class="sub-item-desc">Enforcing strict Severity discipline: any failure mode with Severity >= 8 mandates redesign.</div></div>
            <div class="sub-item"><div class="sub-item-header">Special Characteristics Cascade</div><div class="sub-item-desc">Designating Critical Characteristics (∇ CC) for safety and Significant Characteristics (SC) for fit.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">VIRTUAL CAE COORDINATION</div>
            <div class="card-subtitle">Simulation Alignment</div>
            <div class="sub-item"><div class="sub-item-header">Structural Rigidity (FEA)</div><div class="sub-item-desc">Aligning BIW torsional stiffness (18-28 kNm/°) and bending stiffness with vehicle dynamicists.</div></div>
            <div class="sub-item"><div class="sub-item-header">Dynamic Modal Decoupling</div><div class="sub-item-desc">Tuning body natural frequencies (>38-42 Hz) to decouple from engine idle boom (25-30 Hz).</div></div>
            <div class="sub-item"><div class="sub-item-header">Crashworthiness (LS-DYNA)</div><div class="sub-item-desc">Interpreting explicit dynamic crash pulses, progressive rail folding, and survival cell integrity.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 5:
        f.write('''
    <!-- SLIDE 5 -->
    <section class="slide-viewport" id="slide-5" data-title="Horizons 3 & 4: PM & Eng Manager" data-time="04:00 - 05:00">
      <div class="slide-header">
        <div class="slide-category">PROGRAM GATEWAYS, TOOLING CAPITAL & APQP • SLIDE 5 / 32</div>
        <h2 class="slide-title">Horizons 3 & 4: Project & Engineering Management</h2>
      </div>
      <div class="slide-content">
        <div class="grid-2">
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">HORIZON 3: PROJECT MANAGER</div>
            <div class="card-subtitle">Timing, Tooling Capital & Execution</div>
            <ul class="bullet-list">
              <li><b>OEM Gateway Governance:</b> Guiding vehicle programs through Ford GPDS (FDJ, VP, TT, PP, MP1) and VW PEP (DKM, VFF, PVS, SOP) gateways.</li>
              <li><b>Tooling Capital Commitment:</b> Managing multimillion-pound hard tooling commitments; approving die construction at design freeze.</li>
              <li><b>Prototype Fleet Delivery:</b> Orchestrating mule vehicles, Verification Prototypes (VP), crash test sleds, and extreme-weather test fleets.</li>
              <li><b>Root-Cause Problem Solving:</b> Leading rapid issue containment and root-cause resolution using 8D methodologies and A3 reports.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--indigo);"></div>
            <div class="card-title">HORIZON 4: ENGINEERING MANAGER</div>
            <div class="card-subtitle">Strategy, Organizational Quality & Mentorship</div>
            <ul class="bullet-list">
              <li><b>Platform Resource Strategy:</b> Allocating departmental engineering headcount and budgets across concurrent global vehicle architectures.</li>
              <li><b>APQP & PSW Legal Sign-off:</b> Technical authority signing off on Design Verification Plans & Reports (DVP&R) and Part Submission Warrants (PSW).</li>
              <li><b>Architectural Migration to EV:</b> Steering engineering teams through the paradigm shift from ICE platforms to dedicated MEB electric skateboards.</li>
              <li><b>Talent Mentorship & AI Tools:</b> Cultivating holistic engineering capability and driving adoption of generative AI topology optimization and surrogate CAE.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 6:
        f.write('''
    <!-- SLIDE 6 -->
    <section class="slide-viewport" id="slide-6" data-title="CAD Evolution Timeline" data-time="05:00 - 06:00">
      <div class="slide-header">
        <div class="slide-category">DIGITAL DESIGN REVOLUTION • SLIDE 6 / 32</div>
        <h2 class="slide-title">The CAD Design Evolution: 1960s Drawing Boards to Generative AI</h2>
      </div>
      <div class="slide-content">
        <div class="grid-5" style="height: 220px;">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-subtitle">PRE-1970s</div>
            <div class="card-title">MANUAL DRAFTING</div>
            <p style="font-size: 10px; color: #94A3B8;">Mylar drawing boards, lead splines, manual orthographic projections, full-scale wooden styling bucks.</p>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-subtitle">1970s-1980s</div>
            <div class="card-title">2D CAD & WIREFRAME</div>
            <p style="font-size: 10px; color: #94A3B8;">Computervision, PDGS (Ford), DAC, UNISURF, AutoCAD. Digital 2D vectors replacing hand drafting.</p>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-subtitle">1990s</div>
            <div class="card-title">PARAMETRIC 3D SOLIDS</div>
            <p style="font-size: 10px; color: #94A3B8;">Pro/ENGINEER, CATIA V4/V5, I-DEAS, NX. Associative solid modeling, feature trees, automatic drawing updates.</p>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-subtitle">2000s</div>
            <div class="card-title">DIGITAL MOCKUP (DMU)</div>
            <p style="font-size: 10px; color: #94A3B8;">Complete digital vehicle assembly, automated clash detection, kinematic sweeps, ergonomic H-point integration.</p>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-subtitle">2020s+</div>
            <div class="card-title">GENERATIVE AI & CAE</div>
            <p style="font-size: 10px; color: #94A3B8;">Algorithmic topology optimization, surrogate neural network crash models, text-to-CAD and automated DFMEA.</p>
          </div>
        </div>
        <div class="card" style="flex: 1; border-left: 6px solid var(--primary);">
          <div class="card-title" style="color: var(--primary-light);">THE ARCHITECTURAL SHIFT: FROM GEOMETRIC STORAGE TO INTELLIGENT SYNTHESIS</div>
          <ul class="bullet-list" style="margin-top: 8px;">
            <li><b>Manual Drawing Boards to 2D CAD (1960-1980s):</b> Drawing lines in vector space eliminated physical paper degradation, but CAD remained purely descriptive. Tolerances were still manually calculated via pencil and paper.</li>
            <li><b>The Parametric Revolution (1990s):</b> Feature trees established parent-child logic. Changing a draft angle or bend radius automatically updated downstream ribs, mounting bosses, and 2D drawing projections.</li>
            <li><b>Digital Mockup & AI Co-Pilot (2000s-Present):</b> The entire vehicle exists as a dynamic simulation. Today, generative AI and topology optimization convert functional boundary loads directly into organic, mass-optimized structural geometry.</li>
          </ul>
        </div>
      </div>
    </section>
''')

        # Slide 7:
        f.write('''
    <!-- SLIDE 7 -->
    <section class="slide-viewport" id="slide-7" data-title="2D Drafting vs 3D Parametrics" data-time="06:00 - 07:00">
      <div class="slide-header">
        <div class="slide-category">PARADIGM SHIFT • SLIDE 7 / 32</div>
        <h2 class="slide-title">The CAD Paradigm Shift: 2D Drafting Tables to 3D Parametric Solids</h2>
      </div>
      <div class="slide-content">
        <div class="comp-row">
          <div class="comp-label">GEOMETRIC DEFINITION</div>
          <div class="comp-col-ford"><h4>MANUAL 2D DRAFTING / EARLY 2D CAD</h4><p>Independent 2D projections (plan, elevation, section). High risk of dimensional discrepancies between views when changes occurred.</p></div>
          <div class="comp-col-vw"><h4>3D PARAMETRIC SOLIDS (CATIA / NX)</h4><p>Single unified 3D solid model. 2D drawing views are live associative projections that automatically update when model changes.</p></div>
        </div>
        <div class="comp-row">
          <div class="comp-label">DESIGN INTENT & MODIFICATIONS</div>
          <div class="comp-col-ford"><h4>MANUAL 2D DRAFTING / EARLY 2D CAD</h4><p>No history or parametric constraints. Altering a wall thickness required manually erasing and redrawing every affected view.</p></div>
          <div class="comp-col-vw"><h4>3D PARAMETRIC SOLIDS (CATIA / NX)</h4><p>Explicit feature history tree (sketches, extrusions, fillets, drafts). Modifying a base parameter propagates instantly through child features.</p></div>
        </div>
        <div class="comp-row">
          <div class="comp-label">INTERFERENCE & PACKAGING</div>
          <div class="comp-col-ford"><h4>MANUAL 2D DRAFTING / EARLY 2D CAD</h4><p>Interference detected manually or discovered physically during prototype build bucks, costing weeks and thousands of pounds.</p></div>
          <div class="comp-col-vw"><h4>3D PARAMETRIC SOLIDS (CATIA / NX)</h4><p>Automated digital interference and clash detection across complete vehicle assemblies with live clearance measurements.</p></div>
        </div>
        <div class="comp-row">
          <div class="comp-label">MASS & KINEMATIC SIMULATION</div>
          <div class="comp-col-ford"><h4>MANUAL 2D DRAFTING / EARLY 2D CAD</h4><p>Mass and center-of-gravity estimated by hand calculation. Kinematics checked via physical cardboard overlays.</p></div>
          <div class="comp-col-vw"><h4>3D PARAMETRIC SOLIDS (CATIA / NX)</h4><p>Instantaneous calculation of mass, volume, and moments of inertia. Dynamic 3D simulation of suspension sweeps and closure arcs.</p></div>
        </div>
      </div>
    </section>
''')

        # Slide 8:
        f.write('''
    <!-- SLIDE 8 -->
    <section class="slide-viewport" id="slide-8" data-title="Digital Mockup (DMU) Revolution" data-time="07:00 - 08:00">
      <div class="slide-header">
        <div class="slide-category">VIRTUAL VEHICLE ASSEMBLY • SLIDE 8 / 32</div>
        <h2 class="slide-title">The Digital Mockup (DMU) & Packaging Revolution</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">VIRTUAL VEHICLE ASSEMBLY</div>
            <div class="card-subtitle">Digital Mockup Coordination</div>
            <div class="sub-item"><div class="sub-item-header">Unified Global Coordinates</div><div class="sub-item-desc">Every component loaded into absolute vehicle zero space (X=front wheel center, Y=centerline, Z=rocker).</div></div>
            <div class="sub-item"><div class="sub-item-header">Automated Nightly Clash Scans</div><div class="sub-item-desc">Batch collision algorithms scanning thousands of assemblies overnight to report hard, soft, and clearance clashing.</div></div>
            <div class="sub-item"><div class="sub-item-header">Elimination of Wooden Bucks</div><div class="sub-item-desc">Completely replacing expensive physical styling and packaging bucks with real-time digital DMU reviews.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">OCCUPANT ERGONOMICS & VISION</div>
            <div class="card-subtitle">Digital Manikins</div>
            <div class="sub-item"><div class="sub-item-header">Digital SAE J826 H-Point</div><div class="sub-item-desc">Virtual manikins representing 95th percentile male and 5th percentile female seated in digital CAD interiors.</div></div>
            <div class="sub-item"><div class="sub-item-header">Field-of-View Mapping (SAE J941)</div><div class="sub-item-desc">Projecting driver eye ellipses to verify regulatory forward sightlines through windshields and mirror blind spots.</div></div>
            <div class="sub-item"><div class="sub-item-header">Reach & Ingress Envelopes</div><div class="sub-item-desc">Evaluating steering wheel reach, pedal clearances, and head clearance during door ingress/egress.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">DYNAMIC KINEMATICS</div>
            <div class="card-subtitle">Clearance Sweeps</div>
            <div class="sub-item"><div class="sub-item-header">Suspension Travel Sweeps</div><div class="sub-item-desc">Dynamic multi-body sweeps verifying tire clearance across full jounce (+100 mm), rebound (-80 mm), and lock.</div></div>
            <div class="sub-item"><div class="sub-item-header">Closure Hinge & Latch Arcs</div><div class="sub-item-desc">Simulating door swing kinematics, check-arm detents, and latch catch engagement arcs in 3D virtual space.</div></div>
            <div class="sub-item"><div class="sub-item-header">Flexible Line Routing</div><div class="sub-item-desc">Simulating dynamic flex lines for brake hoses and wiring harnesses under continuous steering articulation.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 9:
        f.write('''
    <!-- SLIDE 9 -->
    <section class="slide-viewport" id="slide-9" data-title="Modern CAE & AI Frontier" data-time="08:00 - 09:00">
      <div class="slide-header">
        <div class="slide-category">SIMULATION & MACHINE LEARNING • SLIDE 9 / 32</div>
        <h2 class="slide-title">The Modern CAE & AI Frontier: Topology Optimization to Generative Design</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--text-muted);"></div>
            <div class="card-title">MANUAL PART OPTIMIZATION</div>
            <div class="card-subtitle">The Historical Engineering Loop</div>
            <div class="sub-item"><div class="sub-item-header">Step 1: Baseline FEA</div><div class="sub-item-desc">Apply static loads and identify low-stress material zones in CAD.</div></div>
            <div class="sub-item"><div class="sub-item-header">Step 2: Manual CAD Removal</div><div class="sub-item-desc">Engineer manually cuts holes and fillets out of solid model in CAD.</div></div>
            <div class="sub-item"><div class="sub-item-header">Step 3: Remesh & Rerun</div><div class="sub-item-desc">Rerun FEA to check stiffness targets; repeated iteratively over weeks.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">GENERATIVE TOPOLOGY OPTIMIZATION</div>
            <div class="card-subtitle">Algorithmic Load-Path Synthesis</div>
            <div class="sub-item"><div class="sub-item-header">Boundary Conditions Only</div><div class="sub-item-desc">Define packaging design space, keep-out clearance zones, and multi-axis loads.</div></div>
            <div class="sub-item"><div class="sub-item-header">Algorithmic Material Growth</div><div class="sub-item-desc">Solver automatically removes non-contributing material, synthesizing organic load paths.</div></div>
            <div class="sub-item"><div class="sub-item-header">Mass & Stiffness Optimized</div><div class="sub-item-desc">Delivers 20-30% mass reduction with 10x faster turnaround than manual remodeling.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">SURROGATE CRASH & TEXT-TO-CAD</div>
            <div class="card-subtitle">Machine Learning in Automotive</div>
            <div class="sub-item"><div class="sub-item-header">Surrogate Crash Models</div><div class="sub-item-desc">Deep neural networks trained on historical LS-DYNA runs predicting crash pulses in milliseconds.</div></div>
            <div class="sub-item"><div class="sub-item-header">Text/Picture-to-CAD</div><div class="sub-item-desc">Emerging AI models converting descriptive requirements into parameterized 3D geometry.</div></div>
            <div class="sub-item"><div class="sub-item-header">Automated DFMEA Synthesis</div><div class="sub-item-desc">Ingesting warranty databases to automatically populate failure modes and controls.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 10:
        f.write('''
    <!-- SLIDE 10 -->
    <section class="slide-viewport" id="slide-10" data-title="Ford Small Car: BE91 & BE146" data-time="09:00 - 10:00">
      <div class="slide-header">
        <div class="slide-category">FORD PLATFORM HERITAGE • SLIDE 10 / 32</div>
        <h2 class="slide-title">Ford European Small Car Foundations: BE91 (Fiesta) & BE146 (Ka)</h2>
      </div>
      <div class="slide-content">
        <div class="grid-2">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">BE91 • FORD FIESTA (MK4)</div>
            <div class="card-subtitle">B-Segment High-Volume Hatchback</div>
            <ul class="bullet-list">
              <li><b>Aggressive Sheet Metal Consolidation:</b> Consolidating stamped inner structural panels to reduce overall piece count and assembly robot welds.</li>
              <li><b>Stamping Blank Nesting Optimization:</b> Optimizing coil blank profiles to achieve >80% material utilization, minimizing scrap on high-speed press lines.</li>
              <li><b>Front Crash Box Integration:</b> Integrating progressive deformation trigger indentations directly into the front longitudinal side rails.</li>
              <li><b>High-Volume Manufacturing Efficiency:</b> Engineered for 60-second takt times across multiple European assembly plants (Dagenham, Cologne, Valencia).</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">BE146 • FORD KA</div>
            <div class="card-subtitle">Sub-B Segment Iconic City Car</div>
            <ul class="bullet-list">
              <li><b>Shared Platform Architecture:</b> Re-engineered the proven BE91 underbody floorpan while wrapping it in revolutionary 'New Edge' styling curves.</li>
              <li><b>Tight Under-Hood Packaging:</b> Inventive packaging of cooling packs, steering columns, and suspension strut towers within a shortened front overhang.</li>
              <li><b>Consolidated Bumper Substructures:</b> Pioneered integrated front and rear protective bumper structures, lowering low-speed repair costs.</li>
              <li><b>Urban Agility & Mass Reduction:</b> Delivered agile urban handling while meeting European crash safety standards at minimum vehicle curb weight.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 11:
        f.write('''
    <!-- SLIDE 11 -->
    <section class="slide-viewport" id="slide-11" data-title="Ford Emerging & Dynamics: C195 & C170" data-time="10:00 - 11:00">
      <div class="slide-header">
        <div class="slide-category">FORD PLATFORM HERITAGE • SLIDE 11 / 32</div>
        <h2 class="slide-title">Ford Emerging Markets & Dynamics: C195 (Ikon) & C170 (Focus Mk1)</h2>
      </div>
      <div class="slide-content">
        <div class="grid-2">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">C195 • FORD IKON</div>
            <div class="card-subtitle">Emerging Market 3-Box Saloon</div>
            <ul class="bullet-list">
              <li><b>Rugged Saloon Packaging:</b> Engineered a distinctive 3-box notchback boot on the B-car platform tailored for emerging markets (India, South Africa, S. America).</li>
              <li><b>Structural Boot Reinforcement:</b> Heavily reinforced rear parcel shelf, D-pillar gussets, and luggage floor to withstand severe road vibration and heavy payloads.</li>
              <li><b>Rough-Road Chassis Upgrades:</b> Strengthened suspension subframe attachment hardpoints and increased ground clearance for punishing terrain.</li>
              <li><b>Dust & Monsoon Sealing:</b> Engineered enhanced double-lip door and boot weatherstripping to prevent severe dust ingress and monsoon water intrusion.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">C170 • FORD FOCUS (MK1)</div>
            <div class="card-subtitle">Benchmark Global Compact Platform</div>
            <ul class="bullet-list">
              <li><b>Control Blade Multi-Link Rear Suspension:</b> Pioneered the revolutionary multi-link rear suspension decoupled into trailing control blade and lateral links.</li>
              <li><b>Zero Cabin Luggage Intrusion:</b> Packaged full multi-link kinematics within an ultra-low-profile subframe, maximizing square boot volume.</li>
              <li><b>Torsional Rigidity Leadership:</b> High-stiffness Body-in-White isolating suspension bushing loads from passenger cabin resonance.</li>
              <li><b>Redefining Compact Car Dynamics:</b> Set the global automotive benchmark for ride comfort, steering precision, and passive rear-wheel toe compliance.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 12:
        f.write('''
    <!-- SLIDE 12 -->
    <section class="slide-viewport" id="slide-12" data-title="Ford D-Segment: CD132 & EUCD" data-time="11:00 - 12:00">
      <div class="slide-header">
        <div class="slide-category">FORD PLATFORM HERITAGE • SLIDE 12 / 32</div>
        <h2 class="slide-title">Ford Global D-Segment: CD132 (Mondeo Mk3) & EUCD Joint Platform</h2>
      </div>
      <div class="slide-content">
        <div class="grid-2">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">CD132 • FORD MONDEO (MK3)</div>
            <div class="card-subtitle">D-Segment Executive Saloon & Estate</div>
            <ul class="bullet-list">
              <li><b>Pioneering Boron Steel Nodes:</b> Early introduction of ultra-high-strength boron steel in structural B-pillars and rocker nodes for side impact safety.</li>
              <li><b>Laser-Brazed Roof Seams:</b> Pioneered automated laser brazing on the roof ditch, replacing black rubber mouldings with an aerodynamic seamless joint.</li>
              <li><b>Dual-Subframe NVH Isolation:</b> Engineered fully isolated front and rear chassis subframes with hydraulic bushings to eliminate road harshness.</li>
              <li><b>Deep-Draw Side Aperture Stampings:</b> Overcoming extreme draw depths and thinning limits on single-piece side outer body stampings.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">EUCD • JOINT MULTI-BRAND ARCHITECTURE</div>
            <div class="card-subtitle">Shared Across Ford, Volvo & Land Rover</div>
            <ul class="bullet-list">
              <li><b>Multi-OEM Architectural Harmonization:</b> Joint platform engineering uniting Mondeo Mk4, S-MAX, Galaxy, Volvo S80/V70/XC60, and Freelander 2.</li>
              <li><b>World-Class Safety Cage Integration:</b> Harmonizing Volvo's legendary passenger cell crash standards with Ford's high-speed volume manufacturing lines.</li>
              <li><b>Deformable Crash Subframe:</b> Engineered lower subframe deformation kinematics to absorb kinetic energy and meet strict pedestrian impact criteria.</li>
              <li><b>Transverse Powertrain Flexibility:</b> Accommodated 4-, 5-, and 6-cylinder transverse engines, dual-clutch transmissions, and AWD drivelines.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 13:
        f.write('''
    <!-- SLIDE 13 -->
    <section class="slide-viewport" id="slide-13" data-title="Ford Global B-Car & SUV: B2E & B2XX" data-time="12:00 - 13:00">
      <div class="slide-header">
        <div class="slide-category">FORD PLATFORM HERITAGE • SLIDE 13 / 32</div>
        <h2 class="slide-title">Ford Global B-Car & SUV: B2E (Fiesta Mk6) & B2XX (EcoSport)</h2>
      </div>
      <div class="slide-content">
        <div class="grid-2">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">B2E • GLOBAL FIESTA (MK6)</div>
            <div class="card-subtitle">Global High-Volume B-Segment</div>
            <ul class="bullet-list">
              <li><b>Global Manufacturing Footprint:</b> Engineered for synchronized manufacturing across Europe, Asia, South America, and North America.</li>
              <li><b>Hot-Stamped Boron Safety Cell:</b> Extensive hot-formed boron steel A-pillars, B-pillars, and rocker reinforcements achieving top safety ratings.</li>
              <li><b>Hydroformed Front Subframe:</b> Hydroformed tubular front suspension subframe maximizing structural stiffness while cutting mass.</li>
              <li><b>Electric Power Steering Packaging:</b> Pioneered early column-drive EPAS integration with optimized driver feedback.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">B2XX • FORD ECOSPORT</div>
            <div class="card-subtitle">Compact Crossover / SUV Architecture</div>
            <ul class="bullet-list">
              <li><b>High Ground Clearance Packaging:</b> Raised ride height to >200 mm ground clearance, requiring revised suspension geometry and drive shaft angles.</li>
              <li><b>Side-Hinged Tailgate Engineering:</b> Designed a unique side-hinged rear door carrying a full-size external spare wheel (>25 kg payload).</li>
              <li><b>Severe D-Pillar Structural Reinforcement:</b> Engineered heavy structural reinforcement brackets and forged hinges to eliminate door sag over rough terrain.</li>
              <li><b>Dynamic Latch Fatigue & Sealing:</b> Multi-axis proving ground fatigue analysis to prevent latch rattle and water ingress under severe torsional racking.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 14:
        f.write('''
    <!-- SLIDE 14 -->
    <section class="slide-viewport" id="slide-14" data-title="VW Modular: MQB-27 & MQB-37" data-time="13:00 - 14:00">
      <div class="slide-header">
        <div class="slide-category">VOLKSWAGEN MODULAR MATRIX • SLIDE 14 / 32</div>
        <h2 class="slide-title">Volkswagen Modular Transverse Matrix: MQB-27 (A0) & MQB-37 (A1/A2)</h2>
      </div>
      <div class="slide-content">
        <div class="grid-2">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">MQB-27 (MQB A0)</div>
            <div class="card-subtitle">Subcompact Modular Platform (Polo / T-Cross)</div>
            <ul class="bullet-list">
              <li><b>Democratizing High-Tech Safety:</b> Integrated over 30% hot-formed boron steel into entry-level subcompacts, achieving 5-star Euro NCAP ratings.</li>
              <li><b>RPS Datum System Standardization:</b> Full integration of Volkswagen's Referenzpunkt-System datum targets across multi-brand stamping plants.</li>
              <li><b>Modular Cross-Car Beam:</b> Shared lightweight dashboard cross-car structure accommodating modular steering and HVAC units.</li>
              <li><b>High Commonality Across Group:</b> Shared underbody components across VW Polo, T-Cross, SEAT Ibiza/Arona, and Škoda Fabia.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">MQB-37 (MQB A1/A2)</div>
            <div class="card-subtitle">Core Global Platform (Golf / Tiguan / Passat)</div>
            <ul class="bullet-list">
              <li><b>The 'Fixed' Dimension:</b> Standardized uniform distance from pedal box to front wheel centerline across all vehicle lines.</li>
              <li><b>Standardized 12° Engine Inclination:</b> Uniform engine tilt angles and exhaust routing allowed identical subframes across petrol, diesel, and hybrid.</li>
              <li><b>Infinite Variable Dimensions:</b> Complete flexibility in wheelbase, track width, overhangs, and seating heights on identical framing bucks.</li>
              <li><b>Industrial Efficiency Benchmark:</b> Reduced engineering hours by >30% while delivering unprecedented group manufacturing profitability.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 15:
        f.write('''
    <!-- SLIDE 15 -->
    <section class="slide-viewport" id="slide-15" data-title="VW Electrification & Commercial: MEB & T7" data-time="14:00 - 15:00">
      <div class="slide-header">
        <div class="slide-category">VOLKSWAGEN EV & COMMERCIAL • SLIDE 15 / 32</div>
        <h2 class="slide-title">Volkswagen Electrification & Commercial: MEB Platform & T7 Multivan</h2>
      </div>
      <div class="slide-content">
        <div class="grid-2">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">MEB • ELECTRIC SKATEBOARD PLATFORM</div>
            <div class="card-subtitle">Dedicated BEV Matrix (ID.3 / ID.4 / ID. Buzz)</div>
            <ul class="bullet-list">
              <li><b>Structural Battery Pack Enclosure:</b> The high-voltage battery housing functions as an active underbody shear plate, increasing torsional stiffness past 30,000 Nm/°.</li>
              <li><b>Multi-Cell Aluminium Crash Sills:</b> Massive extruded rocker sections engineered to absorb side pole impact before battery module intrusion.</li>
              <li><b>Absence of Front ICE Load Path:</b> Front crumple zones redesigned with progressive rail accordion folding without reliance on engine block deceleration.</li>
              <li><b>Flat Floor Interior Packaging:</b> Relocated HVAC unit forward into cowl area, creating D-segment interior cabin volume within a C-segment exterior footprint.</li>
            </ul>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">T7 MULTIVAN • MODULAR MPV</div>
            <div class="card-subtitle">Commercial Vehicle Migration to MQB</div>
            <ul class="bullet-list">
              <li><b>Migrating Van onto MQB Architecture:</b> Migrated Volkswagen's iconic commercial line onto passenger-car MQB foundations with car-like ride and handling.</li>
              <li><b>Modular Floor Rail System:</b> Engineered flat floor rail tracks tested to extreme dynamic seatbelt pull loads (ECE R14) for sliding, removable seats.</li>
              <li><b>Dual A-Pillar Structural Design:</b> Engineered dual A-pillar packaging with front quarter glass to maximize forward vision while ensuring roof crush strength.</li>
              <li><b>Plug-In Hybrid Packaging:</b> Integrated high-voltage hybrid battery beneath the flat floor without encroaching on passenger cabin volume.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 16: Master Design to Manufacture Flowchart
        f.write('''
    <!-- SLIDE 16 -->
    <section class="slide-viewport" id="slide-16" data-title="Master Design-to-Manufacture Flowchart" data-time="15:00 - 16:30">
      <div class="slide-header">
        <div class="slide-category">MASTER PROCESS FLOWCHART • SLIDE 16 / 32</div>
        <h2 class="slide-title">Master Design-to-Manufacture Flowchart: Complete Automotive Lifecycle</h2>
      </div>
      <div class="slide-content">
        <div class="grid-6" style="height: 180px;">
          <div class="card"><div class="card-stripe" style="background: var(--primary);"></div><div class="card-title">01. CONCEPT</div><p style="font-size: 9.5px; color: #94A3B8;">Voice of Customer, BOM targets, segment specs.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--primary);"></div><div class="card-title">02. PACKAGING</div><p style="font-size: 9.5px; color: #94A3B8;">Hardpoints, H-point, ground clearance, eye ellipse.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--primary);"></div><div class="card-title">03. 3D SURFACING</div><p style="font-size: 9.5px; color: #94A3B8;">Class-A to Class-B/C pressings & Master Sections.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--primary);"></div><div class="card-title">04. DFM / DFA</div><p style="font-size: 9.5px; color: #94A3B8;">Stamping FLD, draft angles, rib sink ratios, gun access.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--primary);"></div><div class="card-title">05. DFMEA</div><p style="font-size: 9.5px; color: #94A3B8;">P-Diagrams, Ford v4.2, Special Chars (∇ CC).</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--primary);"></div><div class="card-title">06. 2D & GD&T</div><p style="font-size: 9.5px; color: #94A3B8;">ASME Y14.5, 3-2-1 datums, VW RPS targeting, Profile.</p></div>
        </div>
        <div class="card" style="background: #0B1930; border: 1px solid var(--accent); padding: 8px 14px; text-align: center;">
          <span style="font-size: 11px; font-weight: 800; color: var(--accent); letter-spacing: 1px;">★ MAJOR GATEWAY: DESIGN FREEZE / TOOLING KICK-OFF (FORD FDJ ↔ VW DKM) — CAPITAL RELEASE ★</span>
        </div>
        <div class="grid-6" style="height: 180px;">
          <div class="card"><div class="card-stripe" style="background: var(--teal);"></div><div class="card-title">07. VIRTUAL CAE</div><p style="font-size: 9.5px; color: #94A3B8;">Torsional FEA, NVH modal decoupling, LS-DYNA crash.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--teal);"></div><div class="card-title">08. HARD TOOLING</div><p style="font-size: 9.5px; color: #94A3B8;">Cutting stamping dies, injection moulds, assembly bucks.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--teal);"></div><div class="card-title">09. TOOLING TRYOUT</div><p style="font-size: 9.5px; color: #94A3B8;">First stamped parts (TT/VFF), 100% CMM balloon checks.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--indigo);"></div><div class="card-title">10. CAPABILITY</div><p style="font-size: 9.5px; color: #94A3B8;">PFMEA, Control Plans, Gage R&R (<10%), Cpk >= 1.67.</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--indigo);"></div><div class="card-title">11. PPAP & PSW</div><p style="font-size: 9.5px; color: #94A3B8;">18 PPAP elements, DVP&R tests, signed Warrant (PSW).</p></div>
          <div class="card"><div class="card-stripe" style="background: var(--indigo);"></div><div class="card-title">12. MASS SOP</div><p style="font-size: 9.5px; color: #94A3B8;">Job 1 launch, takt-time ramp, launch containment.</p></div>
        </div>
      </div>
    </section>
''')

        # Slide 17: Flowchart Upstream
        f.write('''
    <!-- SLIDE 17 -->
    <section class="slide-viewport" id="slide-17" data-title="Flowchart: Upstream Engineering" data-time="16:30 - 17:30">
      <div class="slide-header">
        <div class="slide-category">DESIGN-TO-MANUFACTURE FLOWCHART • SLIDE 17 / 32</div>
        <h2 class="slide-title">Design-to-Manufacture: Upstream Virtual Engineering</h2>
      </div>
      <div class="slide-content">
        <div class="grid-4" style="height: 340px;">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">1. PACKAGING & HARDPOINTS</div>
            <div class="sub-item"><div class="sub-item-header">Vehicle Coordinates</div><div class="sub-item-desc">Wheelbase, track, ground clearance, cowl point, and firewall plane.</div></div>
            <div class="sub-item"><div class="sub-item-header">Ergonomic H-Point</div><div class="sub-item-desc">SAE J826 manikin coordinates establishing seating reference point and eye ellipse.</div></div>
            <div class="sub-item"><div class="sub-item-header">Clearance Envelopes</div><div class="sub-item-desc">Kinematic wheel jounce sweeps and closure swing arcs.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">2. SURFACING & DFM/DFA</div>
            <div class="sub-item"><div class="sub-item-header">Class-B Offsets</div><div class="sub-item-desc">Offsetting clay scan Class-A surfaces to structural inner pressings.</div></div>
            <div class="sub-item"><div class="sub-item-header">Stamping Feasibility</div><div class="sub-item-desc">Evaluating Formability Limit Diagrams (FLD), bend radii, and springback.</div></div>
            <div class="sub-item"><div class="sub-item-header">Assembly Ergonomics</div><div class="sub-item-desc">Ensuring robotic spot-weld flange width (>=16 mm) and poka-yoke features.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">3. DFMEA & SPECIAL CHARS</div>
            <div class="sub-item"><div class="sub-item-header">Parameter Diagrams</div><div class="sub-item-desc">Mapping signal inputs, control factors, and noise factors (Ford v4.2).</div></div>
            <div class="sub-item"><div class="sub-item-header">Severity Discipline</div><div class="sub-item-desc">Enforcing mandatory redesign for failure modes with Severity >= 8.</div></div>
            <div class="sub-item"><div class="sub-item-header">Special Chars (∇)</div><div class="sub-item-desc">Cascading Critical Characteristics (∇ CC) to 2D drawings and control plans.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">4. GD&T & VIRTUAL CAE</div>
            <div class="sub-item"><div class="sub-item-header">ASME & RPS Schemes</div><div class="sub-item-desc">Establishing 3-2-1 / RPS datums and Profile of a Surface tolerances.</div></div>
            <div class="sub-item"><div class="sub-item-header">FEA Rigidity & NVH</div><div class="sub-item-desc">Targeting 18-28 kNm/° torsional stiffness and modal decoupling (>38 Hz).</div></div>
            <div class="sub-item"><div class="sub-item-header">Crash (LS-DYNA)</div><div class="sub-item-desc">Simulating frontal progressive rail collapse and side boron intrusion.</div></div>
          </div>
        </div>
        <div class="card" style="background: #0B1930; border-left: 6px solid var(--accent); padding: 12px 18px;">
          <div style="font-size: 11px; font-weight: 800; color: var(--accent); margin-bottom: 2px;">CRITICAL GATEWAY DELIVERABLES AT DESIGN FREEZE (FDJ / DKM):</div>
          <div style="font-size: 11px; color: #E2E8F0;">✓ 100% CAD Surface Maturity &nbsp;•&nbsp; ✓ DFM Tooling Feasibility Sign-Off &nbsp;•&nbsp; ✓ DFMEA Signed with ∇ CC Identified &nbsp;•&nbsp; ✓ Virtual CAE Rigidity & Crash Confirmed</div>
        </div>
      </div>
    </section>
''')

        # Slide 18: Flowchart Downstream
        f.write('''
    <!-- SLIDE 18 -->
    <section class="slide-viewport" id="slide-18" data-title="Flowchart: Downstream Industrialization" data-time="17:30 - 18:30">
      <div class="slide-header">
        <div class="slide-category">DESIGN-TO-MANUFACTURE FLOWCHART • SLIDE 18 / 32</div>
        <h2 class="slide-title">Design-to-Manufacture: Downstream Physical Industrialization</h2>
      </div>
      <div class="slide-content">
        <div class="grid-4" style="height: 340px;">
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">1. TOOLING PROCURE & BUILD</div>
            <div class="sub-item"><div class="sub-item-header">Hard Tooling Machining</div><div class="sub-item-desc">CNC milling and EDM finishing of transfer stamping dies and injection moulds.</div></div>
            <div class="sub-item"><div class="sub-item-header">Welding Buck Fabrication</div><div class="sub-item-desc">Building robotic Body-in-White framing fixtures and geometric clamping nests.</div></div>
            <div class="sub-item"><div class="sub-item-header">Supplier Tooling Audits</div><div class="sub-item-desc">Conducting on-site progress reviews with Tier-1 die makers across Europe and Asia.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">2. TOOLING TRYOUT (TT / VFF)</div>
            <div class="sub-item"><div class="sub-item-header">First Off-Tool Parts</div><div class="sub-item-desc">Pressing first physical stampings from production dies to detect metal springback.</div></div>
            <div class="sub-item"><div class="sub-item-header">100% CMM Inspection</div><div class="sub-item-desc">Probing every dimension against GD&T drawings on Coordinate Measuring Machines.</div></div>
            <div class="sub-item"><div class="sub-item-header">Die Recut & Compensation</div><div class="sub-item-desc">Recutting die surfaces in CAM to compensate for elastic recovery in boron steels.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">3. PROCESS CAPABILITY (CPK)</div>
            <div class="sub-item"><div class="sub-item-header">Measurement Systems (MSA)</div><div class="sub-item-desc">Gage R&R studies proving measurement variance is <10% for critical characteristics.</div></div>
            <div class="sub-item"><div class="sub-item-header">Process Capability Cpk</div><div class="sub-item-desc">Mandated Cpk >= 1.67 (5-sigma quality) for all Critical Characteristics (∇ CC).</div></div>
            <div class="sub-item"><div class="sub-item-header">PFMEA & Control Plans</div><div class="sub-item-desc">Synchronizing shop-floor operator instructions and poka-yoke inspection stations.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">4. PPAP & JOB 1 / SOP</div>
            <div class="sub-item"><div class="sub-item-header">PPAP 18 Deliverables</div><div class="sub-item-desc">Compiling dimensional layouts, DVP&R test records, and material lab certs.</div></div>
            <div class="sub-item"><div class="sub-item-header">Part Submission Warrant</div><div class="sub-item-desc">Executive technical signature on PSW legally certifying production readiness.</div></div>
            <div class="sub-item"><div class="sub-item-header">Serial SOP Launch</div><div class="sub-item-desc">Line ramp-up at takt time with zero defects under launch containment protocols.</div></div>
          </div>
        </div>
        <div class="card" style="background: #0B1930; border-left: 6px solid var(--teal); padding: 12px 18px;">
          <div style="font-size: 11px; font-weight: 800; color: var(--teal); margin-bottom: 2px;">THE LEGAL SUMMIT OF APQP: PART SUBMISSION WARRANT (PSW) SIGN-OFF:</div>
          <div style="font-size: 11px; color: #E2E8F0;">✓ Full 18 PPAP Elements Verified &nbsp;•&nbsp; ✓ Cpk >= 1.67 Confirmed on ∇ CC &nbsp;•&nbsp; ✓ Gage R&R < 10% &nbsp;•&nbsp; ✓ Run-at-Rate Demonstrated at Full Line Speed</div>
        </div>
      </div>
    </section>
''')

        # Slides 19 to 26 (Processes 1 to 8)
        # Process 1: Initial 3D Design
        f.write('''
    <!-- SLIDE 19 -->
    <section class="slide-viewport" id="slide-19" data-title="Process 1: Initial 3D Design" data-time="18:30 - 19:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 1 OF 8 • PACKAGING & GEOMETRY ARCHITECTURE • SLIDE 19 / 32</div>
        <h2 class="slide-title">Process 1: Initial 3D Design & Hardpoint Packaging</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">HARDPOINTS & ARCHITECTURE</div>
            <div class="card-subtitle">Foundational Coordinates</div>
            <div class="sub-item"><div class="sub-item-header">Vehicle Coordinates</div><div class="sub-item-desc">Establishing absolute zero origins, front/rear wheel centers, cowl point, and ground clearance angles.</div></div>
            <div class="sub-item"><div class="sub-item-header">SAE J826 H-Point</div><div class="sub-item-desc">Positioning 95th percentile male / 5th percentile female manikins to define SgRP and heel point.</div></div>
            <div class="sub-item"><div class="sub-item-header">Vision & Glazing (SAE J941)</div><div class="sub-item-desc">Mapping driver eye ellipse to guarantee regulatory forward and mirror visibility angles.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">SURFACE FEASIBILITY (CLASS A TO B/C)</div>
            <div class="card-subtitle">Class-A to B/C Translation</div>
            <div class="sub-item"><div class="sub-item-header">Engineering Offsets</div><div class="sub-item-desc">Translating styling clay scans into Class-B structural pressings and Class-C non-visible brackets.</div></div>
            <div class="sub-item"><div class="sub-item-header">Flanging & Radii Feasibility</div><div class="sub-item-desc">Modifying razor-sharp studio styling creases (<0.5 mm) to manufacturable stamping radii (>1.5 mm).</div></div>
            <div class="sub-item"><div class="sub-item-header">Parametric Master Sections</div><div class="sub-item-desc">Cutting 2D cross-sections across pillars, sills, and headers to secure spot-weld flange access.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">KINEMATIC DYNAMIC ENVELOPES</div>
            <div class="card-subtitle">Dynamic Clearance Sweeps</div>
            <div class="sub-item"><div class="sub-item-header">Suspension Sweeps</div><div class="sub-item-desc">3D swept volumes across full jounce (+100 mm), rebound (-80 mm), and steering lock angles.</div></div>
            <div class="sub-item"><div class="sub-item-header">Closure Kinematics</div><div class="sub-item-desc">Door and tailgate swing arcs with inclined hinge axes for gravity-assisted closure.</div></div>
            <div class="sub-item"><div class="sub-item-header">Weatherstrip Sealing</div><div class="sub-item-desc">Verifying continuous 30-40% seal compression around door apertures to stop wind hiss.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 20: DFM / DFA
        f.write('''
    <!-- SLIDE 20 -->
    <section class="slide-viewport" id="slide-20" data-title="Process 2: DFM & DFA" data-time="19:30 - 20:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 2 OF 8 • MANUFACTURING & ASSEMBLY FEASIBILITY • SLIDE 20 / 32</div>
        <h2 class="slide-title">Process 2: Design for Manufacture (DFM) & Assembly (DFA)</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">SHEET METAL STAMPING DFM</div>
            <div class="card-subtitle">Cold Stamping & Boron Pressing</div>
            <div class="sub-item"><div class="sub-item-header">Formability Limit (FLD)</div><div class="sub-item-desc">Assessing major vs. minor principal strain to eliminate tearing and wrinkling in die draws.</div></div>
            <div class="sub-item"><div class="sub-item-header">Minimum Punch Radii</div><div class="sub-item-desc">Enforcing punch radii >= 1.5t for mild steel, and >= 2.5-3.0t for advanced high-strength steels.</div></div>
            <div class="sub-item"><div class="sub-item-header">Springback Compensation</div><div class="sub-item-desc">Reverse-compensating tooling surfaces in CAD/CAM to counteract elastic recovery in AHSS.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">INJECTION MOULDING DFM</div>
            <div class="card-subtitle">Polymers & Interior Trim</div>
            <div class="sub-item"><div class="sub-item-header">Nominal Wall Uniformity</div><div class="sub-item-desc">Maintaining uniform 2.5-3.0 mm walls to prevent differential cooling warpage.</div></div>
            <div class="sub-item"><div class="sub-item-header">Rib-to-Wall Ratios</div><div class="sub-item-desc">Limiting rib base thickness to 50-60% of adjacent wall (trib <= 0.6t) to eliminate sink marks.</div></div>
            <div class="sub-item"><div class="sub-item-header">Draft Angle Standards</div><div class="sub-item-desc">0.5°-1.0° on polished tools; minimum 1.5° per 0.025 mm texture grain depth.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">DESIGN FOR ASSEMBLY (DFA)</div>
            <div class="card-subtitle">Ergonomics & Automation</div>
            <div class="sub-item"><div class="sub-item-header">Spot-Weld Flange Access</div><div class="sub-item-desc">Ensuring minimum 16-18 mm flange width for 16 mm robotic weld gun electrode tips.</div></div>
            <div class="sub-item"><div class="sub-item-header">Mistake-Proofing (Poka-Yoke)</div><div class="sub-item-desc">Asymmetrical locating pins preventing components from being installed inverted.</div></div>
            <div class="sub-item"><div class="sub-item-header">Nutrunner Radial Clearance</div><div class="sub-item-desc">Minimum 35 mm clearance around bolt axes for automated multi-spindle nutrunners.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 21: DFMEA
        f.write('''
    <!-- SLIDE 21 -->
    <section class="slide-viewport" id="slide-21" data-title="Process 3: DFMEA & Robustness" data-time="20:30 - 21:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 3 OF 8 • RISK MITIGATION & QUALITY ROBUSTNESS • SLIDE 21 / 32</div>
        <h2 class="slide-title">Process 3: DFMEA & Robustness Linkages</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">PARAMETER DIAGRAM (P-DIAGRAM)</div>
            <div class="card-subtitle">Mapping System Robustness</div>
            <div class="sub-item"><div class="sub-item-header">Signal Input</div><div class="sub-item-desc">Driver command or system trigger (e.g., 40 N pull force on exterior door handle).</div></div>
            <div class="sub-item"><div class="sub-item-header">Control Factors</div><div class="sub-item-desc">Design parameters: return spring rate, cable stiffness, pivot ratio, alloy temper.</div></div>
            <div class="sub-item"><div class="sub-item-header">Noise Factors</div><div class="sub-item-desc">Piece-to-piece tolerances, thermal extremes (-40°C to +85°C), ice buildup, grease aging.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--rose);"></div>
            <div class="card-title">THE FORD SEVERITY RULE</div>
            <div class="card-subtitle">Ford FMEA Handbook v4.2</div>
            <div class="sub-item"><div class="sub-item-header">Severity (S 1-10)</div><div class="sub-item-desc">Ratings 9-10 indicate regulatory safety non-compliance. S >= 8 mandates redesign regardless of RPN.</div></div>
            <div class="sub-item"><div class="sub-item-header">Occurrence (O 1-10)</div><div class="sub-item-desc">Assesses failure mechanism probability based on design maturity and historical warranty.</div></div>
            <div class="sub-item"><div class="sub-item-header">Detection (D 1-10)</div><div class="sub-item-desc">Evaluates capability of DVP&R virtual simulations and physical rig tests to catch defects prior to freeze.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">SPECIAL CHARACTERISTICS CASCADE</div>
            <div class="card-subtitle">Critical & Significant Features</div>
            <div class="sub-item"><div class="sub-item-header">Critical Characteristics (∇ CC)</div><div class="sub-item-desc">Features affecting safety or regulatory compliance. Mandates ∇ symbol on CAD, drawings, and Control Plans.</div></div>
            <div class="sub-item"><div class="sub-item-header">Significant Characteristics (SC)</div><div class="sub-item-desc">Key features driving customer satisfaction, fit, flush, and major assembly interfaces.</div></div>
            <div class="sub-item"><div class="sub-item-header">PFMEA & Control Plan Link</div><div class="sub-item-desc">Every ∇ CC cascades directly to Process FMEA, poka-yoke gauging, and Cpk >= 1.67 statistical controls.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 22: GD&T
        f.write('''
    <!-- SLIDE 22 -->
    <section class="slide-viewport" id="slide-22" data-title="Process 4: 2D Detailing & GD&T" data-time="21:30 - 22:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 4 OF 8 • GEOMETRIC TOLERANCING ARCHITECTURE • SLIDE 22 / 32</div>
        <h2 class="slide-title">Process 4: 2D Detailing & GD&T Architecture</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">3-2-1 LOCATING PRINCIPLE</div>
            <div class="card-subtitle">Datum Reference Frames (DRF)</div>
            <div class="sub-item"><div class="sub-item-header">Full 6-DOF Constraint</div><div class="sub-item-desc">Completely eliminating 3 translations (Tx, Ty, Tz) and 3 rotations (Rx, Ry, Rz).</div></div>
            <div class="sub-item"><div class="sub-item-header">Primary Datum A (3 Points)</div><div class="sub-item-desc">Establishes the fundamental spatial plane; constrains pitch, roll, and perpendicular translation.</div></div>
            <div class="sub-item"><div class="sub-item-header">Secondary B & Tertiary C</div><div class="sub-item-desc">Datum B (2 points) constrains yaw and in-plane shift; Datum C (1 point) locks final stop.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">VOLKSWAGEN RPS SYSTEM</div>
            <div class="card-subtitle">Referenzpunkt-System</div>
            <div class="sub-item"><div class="sub-item-header">Group-Wide Datum Standard</div><div class="sub-item-desc">Standardized coordinate datum targeting system applied across MQB, MEB, and commercial vehicles.</div></div>
            <div class="sub-item"><div class="sub-item-header">RPS Pads (RPS-F) & Holes (RPS-H)</div><div class="sub-item-desc">Precision-milled local pads on stamped panels functioning as repeatable CMM contact targets.</div></div>
            <div class="sub-item"><div class="sub-item-header">End-to-End Continuity</div><div class="sub-item-desc">The same RPS datums defined in CAD are machined into stamping dies and robotic welding bucks.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">GEOMETRIC CONTROLS IN BIW</div>
            <div class="card-subtitle">Profile & Bonus Tolerances</div>
            <div class="sub-item"><div class="sub-item-header">Profile of a Surface (|∩|)</div><div class="sub-item-desc">The universal geometric control for complex 3D stamped sheet metal and Class-A exterior skins.</div></div>
            <div class="sub-item"><div class="sub-item-header">True Position (⨁)</div><div class="sub-item-desc">Locating fastener clearance holes, suspension subframe attachment points, and hinge pins.</div></div>
            <div class="sub-item"><div class="sub-item-header">Maximum Material Condition (MMC)</div><div class="sub-item-desc">Utilizing bonus tolerances on clearance holes as hole size departs from minimum MMC boundary.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 23: Tolerance Studies
        f.write('''
    <!-- SLIDE 23 -->
    <section class="slide-viewport" id="slide-23" data-title="Process 5: Tolerance Studies & VSA" data-time="22:30 - 23:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 5 OF 8 • DIMENSIONAL ENGINEERING & VARIATION SIMULATION • SLIDE 23 / 32</div>
        <h2 class="slide-title">Process 5: 1D Tolerance Stacks & 3D Variation Analysis</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">1D TOLERANCE METHODS</div>
            <div class="card-subtitle">Worst-Case vs. Statistical RSS</div>
            <div class="sub-item"><div class="sub-item-header">Worst-Case Arithmetic (Twc)</div><div class="sub-item-desc">Twc = Σ |ti|. Assumes all parts simultaneously reach extreme dimensional limits. Overly conservative for mass production.</div></div>
            <div class="sub-item"><div class="sub-item-header">Root Sum of Squares (Trss)</div><div class="sub-item-desc">Trss = √(Σ ti²). Gaussian statistical model assuming independent normal distributions; ideal for high-volume lines (>200k/yr).</div></div>
            <div class="sub-item"><div class="sub-item-header">Bender's Factor Correction</div><div class="sub-item-desc">Applying 1.3-1.5x multiplier to RSS to account for mean tooling wear and process drift over production lifetime.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">3D MONTE CARLO VSA</div>
            <div class="card-subtitle">Multi-Body Kinematic Variation</div>
            <div class="sub-item"><div class="sub-item-header">Kinematic Simulation</div><div class="sub-item-desc">Running 5,000-10,000 virtual vehicle builds in VisVSA / 3DCS, modeling 6-DOF part variation and assembly sequences.</div></div>
            <div class="sub-item"><div class="sub-item-header">Exterior Gap & Flush</div><div class="sub-item-desc">Predicting hood-to-fender (3.5 ± 0.8 mm), door-to-door (4.0 ± 0.7 mm), and headlamp-to-bumper fitment.</div></div>
            <div class="sub-item"><div class="sub-item-header">Pareto Contribution Analysis</div><div class="sub-item-desc">Identifying the 'vital few' variables driving >70% of variation to target tooling investment precisely where it matters.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">THERMAL EXPANSION DYNAMICS</div>
            <div class="card-subtitle">Multi-Material Modeling</div>
            <div class="sub-item"><div class="sub-item-header">Thermal Range (ΔT)</div><div class="sub-item-desc">Modeling structural expansion across -40°C arctic soak to +85°C high-ambient desert solar loading.</div></div>
            <div class="sub-item"><div class="sub-item-header">Material Mismatch (ΔL)</div><div class="sub-item-desc">Calculating expansion differentials between aluminium closures (α ≈ 23x10⁻⁶/K), steel BIW (α ≈ 12x10⁻⁶/K), and composites.</div></div>
            <div class="sub-item"><div class="sub-item-header">Weatherstrip Load Retention</div><div class="sub-item-desc">Verifying door seal compression remains within 30-40% across thermal extremes to prevent water leaks and wind hiss.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 24: FEA
        f.write('''
    <!-- SLIDE 24 -->
    <section class="slide-viewport" id="slide-24" data-title="Process 6: FEA Rigidity & NVH" data-time="23:30 - 24:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 6 OF 8 • STRUCTURAL SIMULATION & ACOUSTICS • SLIDE 24 / 32</div>
        <h2 class="slide-title">Process 6: Finite Element Analysis (FEA) — Rigidity & NVH</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">STATIC RIGIDITY TARGETS</div>
            <div class="card-subtitle">Handling & Deflection</div>
            <div class="sub-item"><div class="sub-item-header">Torsional Rigidity (kNm/°)</div><div class="sub-item-desc">Targeting 18-28 kNm/° on ICE platforms; >30 kNm/° on MEB skateboard EV architectures.</div></div>
            <div class="sub-item"><div class="sub-item-header">Bending Stiffness (N/mm)</div><div class="sub-item-desc">Vertical rocker deflection control ensuring door latch alignment and preventing body sag under load.</div></div>
            <div class="sub-item"><div class="sub-item-header">Local Mount Stiffness</div><div class="sub-item-desc">Ensuring >10,000 N/mm at strut towers and subframe mounting nodes to deliver crisp steering feedback.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">DYNAMIC NVH & MODAL FREQUENCIES</div>
            <div class="card-subtitle">Acoustic Decoupling</div>
            <div class="sub-item"><div class="sub-item-header">First Torsion Mode (>38-42 Hz)</div><div class="sub-item-desc">Decoupling BIW resonant torsion from engine 4-cylinder idle firing excitation (25-30 Hz at 750-900 RPM).</div></div>
            <div class="sub-item"><div class="sub-item-header">First Bending Mode (>42-46 Hz)</div><div class="sub-item-desc">Decoupling vehicle body bending modes from suspension wheel-hop inputs (12-15 Hz).</div></div>
            <div class="sub-item"><div class="sub-item-header">Acoustic Boom Prevention</div><div class="sub-item-desc">Preventing low-frequency cabin resonance that causes passenger ear pressure and fatigue.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">FATIGUE & DURABILITY LIFE</div>
            <div class="card-subtitle">Road Load Simulation</div>
            <div class="sub-item"><div class="sub-item-header">Road Load Data (WFT)</div><div class="sub-item-desc">Multi-axis load time histories from Belgian cobblestones, pothole strikes, and curb impacts.</div></div>
            <div class="sub-item"><div class="sub-item-header">Miner's Cumulative Damage</div><div class="sub-item-desc">Σ (ni / Ni) <= 1.0. Stress-life (S-N) and strain-life (ε-N) durability analysis across 150,000+ miles.</div></div>
            <div class="sub-item"><div class="sub-item-header">Spot-Weld & Adhesive Fatigue</div><div class="sub-item-desc">Evaluating nugget shear stresses; implementing continuous weld-bonding adhesive to cut stress peaks by 40%.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 25: Crash & EV Safety
        f.write('''
    <!-- SLIDE 25 -->
    <section class="slide-viewport" id="slide-25" data-title="Process 7: Crashworthiness & EV" data-time="24:30 - 25:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 7 OF 8 • NON-LINEAR CRASH SIMULATION & SAFETY • SLIDE 25 / 32</div>
        <h2 class="slide-title">Process 7: Structural Crashworthiness & EV Safety</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">FRONTAL CRASH LOAD PATHS</div>
            <div class="card-subtitle">Euro NCAP 40% Offset & Full Width</div>
            <div class="sub-item"><div class="sub-item-header">Three Decoupled Paths</div><div class="sub-item-desc">Upper shotgun rail (25% energy), main longitudinal rail (55%), lower subframe extension (20%).</div></div>
            <div class="sub-item"><div class="sub-item-header">Progressive Rail Collapse</div><div class="sub-item-desc">Hexagonal high-strength steel crash boxes with stamped trigger indentations creating uniform accordion crush.</div></div>
            <div class="sub-item"><div class="sub-item-header">Engine Block Kinematics</div><div class="sub-item-desc">Directing ICE block downward beneath passenger floorpan to prevent firewall penetration.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--rose);"></div>
            <div class="card-title">BORON SAFETY CELL (22MnB5)</div>
            <div class="card-subtitle">Hot-Stamped Side Impact Safety</div>
            <div class="sub-item"><div class="sub-item-header">Ultra-High-Strength Boron</div><div class="sub-item-desc">Hot-stamped at 900°C and quenched to martensitic microstructure with Rm > 1500 MPa.</div></div>
            <div class="sub-item"><div class="sub-item-header">Tailored Tempering B-Pillar</div><div class="sub-item-desc">1500 MPa martensite at upper B-pillar prevents head strike; 600-800 MPa ductile base creates controlled plastic hinge.</div></div>
            <div class="sub-item"><div class="sub-item-header">Boron Cross-Car Beams</div><div class="sub-item-desc">High-strength floor cross-members transferring side barrier impact across the underbody tunnel.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">MEB EV BATTERY PROTECTION</div>
            <div class="card-subtitle">The Skateboard Safety Architecture</div>
            <div class="sub-item"><div class="sub-item-header">Multi-Cell Aluminium Sills</div><div class="sub-item-desc">Massive extruded rocker sections engineered to absorb side pole impact before battery module intrusion.</div></div>
            <div class="sub-item"><div class="sub-item-header">Structural Battery Housing</div><div class="sub-item-desc">Heavy aluminium baseplate and internal web frame acting as an impenetrable survival cell.</div></div>
            <div class="sub-item"><div class="sub-item-header">Pyrofuse High-Voltage Disconnect</div><div class="sub-item-desc">Automatic pyrotechnic disconnect isolating 400V/800V battery pack within 2 milliseconds of impact.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 26: APQP & Launch
        f.write('''
    <!-- SLIDE 26 -->
    <section class="slide-viewport" id="slide-26" data-title="Process 8: APQP & Launch" data-time="25:30 - 26:30">
      <div class="slide-header">
        <div class="slide-category">PROCESS 8 OF 8 • LAUNCH GOVERNANCE & STATISTICAL QUALITY • SLIDE 26 / 32</div>
        <h2 class="slide-title">Process 8: APQP & Production Launch Governance</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">APQP 5-PHASE LIFECYCLE</div>
            <div class="card-subtitle">Systematic Quality Framework</div>
            <div class="sub-item"><div class="sub-item-header">Phase 1: Concept & Planning</div><div class="sub-item-desc">Translating Voice of Customer into target vehicle specifications and initial BOM.</div></div>
            <div class="sub-item"><div class="sub-item-header">Phase 2: Product Design</div><div class="sub-item-desc">CAD release, DFM/DFA, DFMEA, GD&T drawings, and DVP&R virtual verification.</div></div>
            <div class="sub-item"><div class="sub-item-header">Phase 3: Process Design</div><div class="sub-item-desc">Stamping die cutting, injection mould build, PFMEA, Control Plans, and packaging.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">OEM GATEWAY SYNCHRONIZATION</div>
            <div class="card-subtitle">Ford GPDS vs. Volkswagen PEP</div>
            <div class="sub-item"><div class="sub-item-header">Concept Freeze</div><div class="sub-item-desc">Ford Concept Approval (CA) ↔ VW Projektvereinbarung / Konzeptfreigabe.</div></div>
            <div class="sub-item"><div class="sub-item-header">Design Freeze (Hard Tooling)</div><div class="sub-item-desc">Ford Final Data Judgement (FDJ) ↔ VW Datenkontrollmodell (DKM). Hard tooling released.</div></div>
            <div class="sub-item"><div class="sub-item-header">Tooling Tryout (TT)</div><div class="sub-item-desc">First parts stamped from production dies ↔ VW Vorserie (VFF). Dimensional checks.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">PPAP 18 ELEMENTS & CAPABILITY</div>
            <div class="card-subtitle">The Manufacturing Contract</div>
            <div class="sub-item"><div class="sub-item-header">Measurement Systems (MSA)</div><div class="sub-item-desc">Gage R&R < 10% mandatory for Critical Characteristics; 10-30% conditionally acceptable.</div></div>
            <div class="sub-item"><div class="sub-item-header">Process Capability (Cpk)</div><div class="sub-item-desc">Mandated Cpk >= 1.67 (5-sigma quality) for Critical Characteristics (∇ CC); Cpk >= 1.33 for standard.</div></div>
            <div class="sub-item"><div class="sub-item-header">Part Submission Warrant (PSW)</div><div class="sub-item-desc">The formal signed executive declaration certifying production readiness at rate with zero defects.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 27: Case Study 1
        f.write('''
    <!-- SLIDE 27 -->
    <section class="slide-viewport" id="slide-27" data-title="Case Study 1: Ford C170 Focus" data-time="26:30 - 27:15">
      <div class="slide-header">
        <div class="slide-category">TECHNICAL CASE STUDY 1 • CHASSIS PACKAGING & DYNAMICS • SLIDE 27 / 32</div>
        <h2 class="slide-title">Technical Case Study 1: The Multi-Link Packaging Triumph of Ford C170 Focus</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">THE COMPACT CLASS CONUNDRUM</div>
            <div class="card-subtitle">The Twist-Beam Barrier</div>
            <div class="sub-item"><div class="sub-item-header">Twist-Beam Compromise</div><div class="sub-item-desc">Compact C-segment cars universally used cheap twist-beam rear axles, compromising ride quality and cornering stability.</div></div>
            <div class="sub-item"><div class="sub-item-header">The Multi-Link Barrier</div><div class="sub-item-desc">Traditional multi-link independent rear suspensions were considered too costly and intruded severely into boot luggage space.</div></div>
            <div class="sub-item"><div class="sub-item-header">Ford Dynamic Challenge</div><div class="sub-item-desc">Ford leadership demanded class-leading vehicle dynamics ('fun-to-drive') without compromising family luggage utility.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">THE CONTROL BLADE SOLUTION</div>
            <div class="card-subtitle">Decoupled Kinematics</div>
            <div class="sub-item"><div class="sub-item-header">Decoupled Kinematics</div><div class="sub-item-desc">Longitudinal trailing arm (the flat stamped 'Control Blade') decoupled from short lateral camber/toe links.</div></div>
            <div class="sub-item"><div class="sub-item-header">Braking Compliance</div><div class="sub-item-desc">The thin vertical blade absorbed road longitudinal impact and braking torque while flexing laterally without binding.</div></div>
            <div class="sub-item"><div class="sub-item-header">Passive Rear-Wheel Steer</div><div class="sub-item-desc">Under lateral cornering forces, the elastomeric bushings induced passive toe-in, stabilizing the rear axle at speed.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">ARCHITECTURAL IMPACT</div>
            <div class="card-subtitle">Industry Benchmark</div>
            <div class="sub-item"><div class="sub-item-header">Zero Boot Intrusion</div><div class="sub-item-desc">Packaged entire multi-link assembly within a compact subframe beneath the floor, preserving an immense square boot.</div></div>
            <div class="sub-item"><div class="sub-item-header">Class Benchmark for 20 Years</div><div class="sub-item-desc">The Control Blade architecture set the industry standard, copied by competitors across Europe and Asia.</div></div>
            <div class="sub-item"><div class="sub-item-header">Proof of Packaging Mastery</div><div class="sub-item-desc">Demonstrated that innovative geometric packaging delivers premium dynamics within high-volume cost constraints.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 28: Case Study 2
        f.write('''
    <!-- SLIDE 28 -->
    <section class="slide-viewport" id="slide-28" data-title="Case Study 2: Ford EUCD Safety" data-time="27:15 - 28:00">
      <div class="slide-header">
        <div class="slide-category">TECHNICAL CASE STUDY 2 • MULTI-BRAND PLATFORM HARMONIZATION • SLIDE 28 / 32</div>
        <h2 class="slide-title">Technical Case Study 2: Structural Safety Harmonization of Ford EUCD</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">THE MULTI-OEM CHALLENGE</div>
            <div class="card-subtitle">Three Global Brands</div>
            <div class="sub-item"><div class="sub-item-header">Three Distinct Brands</div><div class="sub-item-desc">Developing a single shared platform for Ford (Mondeo/S-MAX), Volvo (S80/V70/XC60), and Land Rover (Freelander 2).</div></div>
            <div class="sub-item"><div class="sub-item-header">Conflicting Philosophies</div><div class="sub-item-desc">Reconciling Volvo's unyielding passenger cell safety expectations with Ford's high-speed assembly line takt times.</div></div>
            <div class="sub-item"><div class="sub-item-header">Diverse Body Styles</div><div class="sub-item-desc">Accommodating saloons, estates, 7-seat MPVs, and all-wheel-drive SUVs across divergent curb weights.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">THE STRUCTURAL SOLUTION</div>
            <div class="card-subtitle">Modular Safety Cage</div>
            <div class="sub-item"><div class="sub-item-header">Multi-Tier Front Crash Rails</div><div class="sub-item-desc">Three decoupled front load paths absorbing energy at 64 km/h offset impacts while controlling deceleration pulses.</div></div>
            <div class="sub-item"><div class="sub-item-header">Deformable Crash Subframe</div><div class="sub-item-desc">Lower front subframe engineered to shear away and tilt the engine downward beneath the floor in severe impacts.</div></div>
            <div class="sub-item"><div class="sub-item-header">Hot-Stamped Boron Safety Cell</div><div class="sub-item-desc">Extensive hot-formed boron steel B-pillars and floor cross-members linking left and right rocker sills.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">MANUFACTURING & MARKET SUCCESS</div>
            <div class="card-subtitle">Cross-Brand Synergy</div>
            <div class="sub-item"><div class="sub-item-header">5-Star Euro NCAP Across Lines</div><div class="sub-item-desc">Every derivative vehicle on EUCD achieved 5-star Euro NCAP ratings, setting new executive segment safety benchmarks.</div></div>
            <div class="sub-item"><div class="sub-item-header">>60% Underbody Commonality</div><div class="sub-item-desc">Shared over 60% of structural underbody pressings, unlocking massive global tooling and purchasing economies.</div></div>
            <div class="sub-item"><div class="sub-item-header">Proof of Cross-OEM Synergy</div><div class="sub-item-desc">Demonstrated that divergent engineering cultures can unite to produce world-class architectures.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 29: Case Study 3
        f.write('''
    <!-- SLIDE 29 -->
    <section class="slide-viewport" id="slide-29" data-title="Case Study 3: MQB ICE vs MEB EV" data-time="28:00 - 28:45">
      <div class="slide-header">
        <div class="slide-category">TECHNICAL CASE STUDY 3 • ARCHITECTURAL COMPARISON • SLIDE 29 / 32</div>
        <h2 class="slide-title">Technical Case Study 3: The Skateboard Revolution — MQB ICE vs. MEB EV</h2>
      </div>
      <div class="slide-content">
        <div class="comp-row">
          <div class="comp-label">CRASH ENERGY MANAGEMENT</div>
          <div class="comp-col-ford"><h4>CONVENTIONAL ICE ARCHITECTURE (MQB-37)</h4><p>Heavy engine block acts as rigid mass in frontal crash; front rails fold around engine while directing it downward beneath passenger floorpan.</p></div>
          <div class="comp-col-vw"><h4>DEDICATED EV SKATEBOARD (MEB PLATFORM)</h4><p>No rigid engine block allows longer progressive front rail crush; but high-voltage battery demands zero side-pole intrusion via extruded aluminium sills.</p></div>
        </div>
        <div class="comp-row">
          <div class="comp-label">TORSIONAL RIGIDITY CONTRIBUTION</div>
          <div class="comp-col-ford"><h4>CONVENTIONAL ICE ARCHITECTURE (MQB-37)</h4><p>Rigidity achieved via central floor exhaust tunnel, boxed rocker sills, and rear parcel shelf structure (typical: 20,000 - 24,000 Nm/°).</p></div>
          <div class="comp-col-vw"><h4>DEDICATED EV SKATEBOARD (MEB PLATFORM)</h4><p>Aluminium battery housing acts as massive underbody structural shear plate, increasing torsional rigidity past 30,000 Nm/° (+25% over ICE).</p></div>
        </div>
        <div class="comp-row">
          <div class="comp-label">CABIN SPACE & PACKAGING</div>
          <div class="comp-col-ford"><h4>CONVENTIONAL ICE ARCHITECTURE (MQB-37)</h4><p>High dash cowl and central floor tunnel dividing passenger footwells; engine and cooling pack dictate front axle position.</p></div>
          <div class="comp-col-vw"><h4>DEDICATED EV SKATEBOARD (MEB PLATFORM)</h4><p>Completely flat cabin floor with zero exhaust tunnel; HVAC relocated forward into bulkhead; D-segment interior space in C-segment footprint.</p></div>
        </div>
      </div>
    </section>
''')

        # Slide 30: Leadership & Capital
        f.write('''
    <!-- SLIDE 30 -->
    <section class="slide-viewport" id="slide-30" data-title="Engineering Leadership & Capital" data-time="28:45 - 29:15">
      <div class="slide-header">
        <div class="slide-category">EXECUTIVE MANAGEMENT & INNOVATION • SLIDE 30 / 32</div>
        <h2 class="slide-title">Engineering Leadership & Capital Asset Governance</h2>
      </div>
      <div class="slide-content">
        <div class="grid-3">
          <div class="card">
            <div class="card-stripe" style="background: var(--primary);"></div>
            <div class="card-title">TOOLING ASSET GOVERNANCE</div>
            <div class="card-subtitle">Capital Risk Management</div>
            <div class="sub-item"><div class="sub-item-header">Managing 'Point of No Return'</div><div class="sub-item-desc">Rigorous technical reviews prior to Tooling Kick-Off (FDJ/DKM) preventing catastrophic late tooling rework.</div></div>
            <div class="sub-item"><div class="sub-item-header">High-Stakes Stamping Dies</div><div class="sub-item-desc">A single transfer die set for a side aperture outer costs $4M-$6M; requires zero tolerance for geometric errors.</div></div>
            <div class="sub-item"><div class="sub-item-header">Supplier Run-at-Rate Audits</div><div class="sub-item-desc">Leading on-site audits at supplier press shops to verify cycle takt time and dimensional stability.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">PEOPLE & TEAM LEADERSHIP</div>
            <div class="card-subtitle">Organizational Capability</div>
            <div class="sub-item"><div class="sub-item-header">Cross-Functional Harmony</div><div class="sub-item-desc">Uniting styling designers, body engineers, CAE simulation specialists, and assembly plant directors.</div></div>
            <div class="sub-item"><div class="sub-item-header">Mentoring Future Leaders</div><div class="sub-item-desc">Transforming junior CAD operators into holistic systems engineers who understand cost, tooling, and physics.</div></div>
            <div class="sub-item"><div class="sub-item-header">Codifying Lessons Learned</div><div class="sub-item-desc">Ensuring manufacturing launch defects and warranty feedback are written into future platform design guidelines.</div></div>
          </div>
          <div class="card">
            <div class="card-stripe" style="background: var(--accent);"></div>
            <div class="card-title">STRATEGIC SCALABILITY</div>
            <div class="card-subtitle">The Digital Future</div>
            <div class="sub-item"><div class="sub-item-header">Cross-Brand Architecture</div><div class="sub-item-desc">Leveraging modular toolkits to maximize commonality across volume, commercial, and premium brands.</div></div>
            <div class="sub-item"><div class="sub-item-header">Bridging CAD to Serial SOP</div><div class="sub-item-desc">Maintaining relentless technical rigor from initial 3D sketch all the way to legal PSW signature.</div></div>
            <div class="sub-item"><div class="sub-item-header">Embracing Digital Disruption</div><div class="sub-item-desc">Leading engineering organizations into the future of electrified skateboards and generative AI CAE.</div></div>
          </div>
        </div>
      </div>
    </section>
''')

        # Slide 31: Core Takeaways
        f.write('''
    <!-- SLIDE 31 -->
    <section class="slide-viewport" id="slide-31" data-title="Core Takeaways" data-time="29:15 - 29:45">
      <div class="slide-header">
        <div class="slide-category">SYNTHESIS & EXECUTIVE REFLECTION • SLIDE 31 / 32</div>
        <h2 class="slide-title">Core Takeaways: Four Tenets of World-Class Automotive Engineering</h2>
      </div>
      <div class="slide-content">
        <div class="card" style="border-left: 6px solid var(--primary); margin-bottom: 8px;">
          <div class="card-title" style="color: var(--primary);">1. MASTER THE MICRO TO DELIVER THE MACRO</div>
          <p style="font-size: 11.5px; color: #CBD5E1; line-height: 1.4;">Vehicle platform success is decided at the micrometer level. Datum schemes (GD&T / RPS), punch bend radii, and 1D/3D tolerance stackups dictate whether a multi-billion-pound architecture launches smoothly or suffers costly factory rework.</p>
        </div>
        <div class="card" style="border-left: 6px solid var(--teal); margin-bottom: 8px;">
          <div class="card-title" style="color: var(--teal);">2. UPSTREAM PREVENTION BEATS DOWNSTREAM CRISIS</div>
          <p style="font-size: 11.5px; color: #CBD5E1; line-height: 1.4;">Robust DFMEAs, Parameter Diagrams, and early DFM/DFA eliminate failures at the CAD cursor. Catching an error in virtual CAD costs 1x; fixing it in hard tooling costs 10x; fixing it at pilot production costs 100x.</p>
        </div>
        <div class="card" style="border-left: 6px solid var(--accent); margin-bottom: 8px;">
          <div class="card-title" style="color: var(--accent);">3. MODULAR SCALABILITY DEFINES OEM SURVIVAL</div>
          <p style="font-size: 11.5px; color: #CBD5E1; line-height: 1.4;">The evolution from dedicated platforms (C170) to modular matrix ecosystems (MQB) and dedicated electric skateboards (MEB) proves the power of standardizing hidden manufacturing interfaces while preserving brand distinctiveness.</p>
        </div>
        <div class="card" style="border-left: 6px solid var(--indigo);">
          <div class="card-title" style="color: var(--indigo);">4. AUTHENTIC LEADERSHIP IS GROUNDED IN FIRST PRINCIPLES</div>
          <p style="font-size: 11.5px; color: #CBD5E1; line-height: 1.4;">The most effective engineering leaders are those who have personally held the CAD pencil, calculated tolerance stacks, chaired DFMEA reviews, and signed off on crash test sleds. Technical empathy drives organizational excellence.</p>
        </div>
      </div>
    </section>
''')

        # Slide 32: Q&A
        f.write('''
    <!-- SLIDE 32 -->
    <section class="slide-viewport" id="slide-32" data-title="Questions & Discussion" data-time="29:45 - 30:00+">
      <div class="title-stage">
        <div class="title-hero">
          <div class="title-eyebrow">COLLABORATIVE EXCHANGE & DISCUSSION • SLIDE 32 / 32</div>
          <h1 class="title-main">Questions & Technical Discussion</h1>
          <p class="title-desc">Deep-dive exploration of vehicle architectures, process execution, and engineering leadership.</p>
        </div>
        <div class="grid-3" style="height: 160px; flex-shrink: 0;">
          <div class="card" style="border-top: 4px solid var(--primary);">
            <div class="card-subtitle" style="color: var(--primary);">TOPIC 1</div>
            <div class="card-title">CRASH & EV INTEGRATION</div>
            <p style="font-size: 10px; color: #94A3B8;">Transitioning structural crash teams from traditional ICE front rails to high-voltage MEB skateboard battery protection.</p>
          </div>
          <div class="card" style="border-top: 4px solid var(--teal);">
            <div class="card-subtitle" style="color: var(--teal);">TOPIC 2</div>
            <div class="card-title">DIMENSIONAL QUALITY</div>
            <p style="font-size: 10px; color: #94A3B8;">Overcoming real-world challenges when migrating from 1D tolerance stacks to 3D Monte Carlo variation simulation (VSA).</p>
          </div>
          <div class="card" style="border-top: 4px solid var(--accent);">
            <div class="card-subtitle" style="color: var(--accent);">TOPIC 3</div>
            <div class="card-title">APQP & GATEWAY SPEED</div>
            <p style="font-size: 10px; color: #94A3B8;">Accelerating automotive development timing without compromising Cpk >= 1.67 capability and PSW sign-off.</p>
          </div>
        </div>
      </div>
    </section>
''')

        # Write Bottom Bar, Drawers, and Scripts
        f.write('''
  </main>
  <footer id="bottom-bar">
    <div class="nav-controls">
      <button class="btn" id="btn-prev">◀ Prev</button>
      <button class="btn" id="btn-next">Next ▶</button>
    </div>
    <div class="progress-container">
      <div class="progress-bar" id="progress-bar"></div>
    </div>
    <div class="slide-counter" id="slide-counter">Slide 1 / 32</div>
  </footer>

  <aside id="notes-drawer">
    <div class="notes-header">
      <div class="notes-title" id="notes-header-title">PRESENTER SCRIPT • SLIDE 1</div>
      <button class="btn" id="btn-close-notes" style="padding: 2px 7px; font-size: 10px;">✕ Close</button>
    </div>
    <div class="notes-body" id="notes-body-text"></div>
  </aside>

  <div id="overview-modal">
    <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1400px; margin: 0 auto 20px auto;">
      <h3 style="font-size: 18px; font-weight: 800; color: #fff;">Slide Grid Overview (32 Slides)</h3>
      <button class="btn" id="btn-close-overview">✕ Close (Esc)</button>
    </div>
    <div class="overview-grid" id="overview-grid-container"></div>
  </div>

  <script>
    const speakerNotes = ''' + json.dumps(notes_dict) + ''';
    let currentSlide = 1;
    const totalSlides = 32;
    let timerSeconds = 30 * 60;
    let timerInterval = null;
    let isTimerRunning = false;

    const slides = document.querySelectorAll('.slide-viewport');
    const slideCounter = document.getElementById('slide-counter');
    const progressBar = document.getElementById('progress-bar');
    const notesDrawer = document.getElementById('notes-drawer');
    const notesHeaderText = document.getElementById('notes-header-title');
    const notesBodyText = document.getElementById('notes-body-text');
    const timerDisplay = document.getElementById('timer-display');
    const btnTimer = document.getElementById('btn-timer');
    const btnResetTimer = document.getElementById('btn-reset-timer');
    const overviewModal = document.getElementById('overview-modal');
    const overviewGrid = document.getElementById('overview-grid-container');

    function updateSlide(index) {
      if (index < 1 || index > totalSlides) return;
      currentSlide = index;
      slides.forEach((slide, idx) => {
        if (idx + 1 === currentSlide) slide.classList.add('active');
        else slide.classList.remove('active');
      });
      slideCounter.textContent = `Slide ${currentSlide} / ${totalSlides}`;
      progressBar.style.width = `${(currentSlide / totalSlides) * 100}%`;

      const currentSlideElem = document.getElementById(`slide-${currentSlide}`);
      const title = currentSlideElem ? currentSlideElem.getAttribute('data-title') : '';
      const timing = currentSlideElem ? currentSlideElem.getAttribute('data-time') : '';
      notesHeaderText.textContent = `SLIDE ${currentSlide}: ${title.toUpperCase()} (${timing})`;
      notesBodyText.textContent = speakerNotes[currentSlide] || "No speaker notes for this slide.";
    }

    function nextSlide() { if (currentSlide < totalSlides) updateSlide(currentSlide + 1); }
    function prevSlide() { if (currentSlide > 1) updateSlide(currentSlide - 1); }
    function toggleNotes() {
      notesDrawer.classList.toggle('open');
      document.getElementById('btn-notes').classList.toggle('btn-active');
    }
    function toggleOverview() {
      overviewModal.classList.toggle('open');
      document.getElementById('btn-overview').classList.toggle('btn-active');
    }

    function formatTime(sec) {
      const m = Math.floor(sec / 60).toString().padStart(2, '0');
      const s = (sec % 60).toString().padStart(2, '0');
      return `⏱ ${m}:${s}`;
    }

    function startTimer() {
      if (isTimerRunning) {
        clearInterval(timerInterval);
        isTimerRunning = false;
        btnTimer.textContent = 'Resume Timer';
        btnTimer.classList.remove('btn-active');
      } else {
        isTimerRunning = true;
        btnTimer.textContent = 'Pause Timer';
        btnTimer.classList.add('btn-active');
        timerInterval = setInterval(() => {
          if (timerSeconds > 0) {
            timerSeconds--;
            timerDisplay.textContent = formatTime(timerSeconds);
          } else {
            clearInterval(timerInterval);
            isTimerRunning = false;
            timerDisplay.textContent = "⏱ 00:00 (Time's Up)";
            timerDisplay.style.color = "var(--rose)";
          }
        }, 1000);
      }
    }

    function resetTimer() {
      clearInterval(timerInterval);
      isTimerRunning = false;
      timerSeconds = 30 * 60;
      timerDisplay.textContent = formatTime(timerSeconds);
      timerDisplay.style.color = "var(--accent)";
      btnTimer.textContent = 'Start Timer';
      btnTimer.classList.remove('btn-active');
    }

    function buildOverviewGrid() {
      overviewGrid.innerHTML = '';
      slides.forEach((slide, idx) => {
        const slideNum = idx + 1;
        const title = slide.getAttribute('data-title') || `Slide ${slideNum}`;
        const timing = slide.getAttribute('data-time') || '';
        const card = document.createElement('div');
        card.className = 'thumb-card';
        card.innerHTML = `<div class="thumb-num">SLIDE ${slideNum} • ${timing}</div><div class="thumb-title">${title}</div>`;
        card.addEventListener('click', () => { updateSlide(slideNum); toggleOverview(); });
        overviewGrid.appendChild(card);
      });
    }

    document.getElementById('btn-next').addEventListener('click', nextSlide);
    document.getElementById('btn-prev').addEventListener('click', prevSlide);
    document.getElementById('btn-notes').addEventListener('click', toggleNotes);
    document.getElementById('btn-close-notes').addEventListener('click', toggleNotes);
    document.getElementById('btn-overview').addEventListener('click', toggleOverview);
    document.getElementById('btn-close-overview').addEventListener('click', toggleOverview);
    btnTimer.addEventListener('click', startTimer);
    btnResetTimer.addEventListener('click', resetTimer);

    document.addEventListener('keydown', (e) => {
      if (overviewModal.classList.contains('open')) {
        if (e.key === 'Escape') toggleOverview();
        return;
      }
      if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === 'PageDown') {
        e.preventDefault(); nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault(); prevSlide();
      } else if (e.key === 'Home') {
        e.preventDefault(); updateSlide(1);
      } else if (e.key === 'End') {
        e.preventDefault(); updateSlide(totalSlides);
      } else if (e.key === 'p' || e.key === 'P') {
        e.preventDefault(); toggleNotes();
      } else if (e.key === 'o' || e.key === 'O' || e.key === 'Escape') {
        e.preventDefault(); toggleOverview();
      }
    });

    buildOverviewGrid();
    updateSlide(1);
  </script>
</body>
</html>
''')
    print(f"Successfully generated 32-slide HTML presentation: {out_path}")

if __name__ == "__main__":
    build_complete_html()
