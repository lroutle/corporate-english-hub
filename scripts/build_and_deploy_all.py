#!/usr/bin/env python3
"""
Master Build and Deployment Orchestrator.
- Regenerates all 5 Core Suites (eliminating duplicate prompts and deploying bespoke B1-005 & B1-016).
- Syncs Tapi Chemistry variants (Kosar & Mazur).
- Deploys 3 new Bidfood Student Sandboxes:
    1. bidfood-purchasing-libor (Libor Barvenčík)
    2. bidfood-purchasing-lucie (Lucie Rončková)
    3. bidfood-engineering-jiri (Jiří Lorenčík)
- Audits all modules across the entire ecosystem for 0 duplicate prompts.
- Validates against schema and pedagogical standards.
"""

import sys
import json
import shutil
from pathlib import Path
from collections import Counter
import jsonschema

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from generators.tatra_eng import generate_tatra_eng_modules
from generators.tatra_sales import generate_tatra_sales_modules
from generators.tapi_eng import generate_tapi_eng_modules
from generators.tapi_chem import generate_tapi_chem_modules
from generators.tapi_it import generate_tapi_it_modules
from generators.bidfood_purchasing import generate_bidfood_purchasing_modules
from generators.bidfood_engineering import generate_bidfood_engineering_modules
from curriculum_catalog import ALL_CURRICULA

CORE_SUITES = {
    "tatra-engineering": (generate_tatra_eng_modules, "tatra-engineering"),
    "tatra-sales-engineering": (generate_tatra_sales_modules, "tatra-sales-engineering"),
    "tapi-engineering": (generate_tapi_eng_modules, "tapi-engineering"),
    "tapi-chemistry": (generate_tapi_chem_modules, "tapi-chemistry"),
    "tapi-it": (generate_tapi_it_modules, "tapi-it")
}

def write_suite_data(suite_dir, curriculum, modules):
    tests_dir = suite_dir / "data" / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write individual JSON test files
    for tid, test_obj in modules.items():
        t_path = tests_dir / f"{tid}.json"
        with open(t_path, "w", encoding="utf-8") as f:
            json.dump(test_obj, f, indent=2, ensure_ascii=False)

    # 2. Write curriculum_manifest.json
    manifest_path = suite_dir / "data" / "curriculum_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)

    # 3. Write manifest.js (for offline loading)
    manifest_js_path = suite_dir / "data" / "manifest.js"
    with open(manifest_js_path, "w", encoding="utf-8") as f:
        f.write("window.CURRICULUM_MANIFEST = " + json.dumps(curriculum, indent=2, ensure_ascii=False) + ";\n")

    # 4. Write tests_registry.js (zero-server execution)
    reg_js_path = suite_dir / "data" / "tests_registry.js"
    with open(reg_js_path, "w", encoding="utf-8") as f:
        f.write("window.TEST_REGISTRY = window.TEST_REGISTRY || {};\n")
        f.write("Object.assign(window.TEST_REGISTRY, " + json.dumps(modules, indent=2, ensure_ascii=False) + ");\n")


def deploy_core_suites():
    print("=" * 60)
    print("DEPLOYING 5 CORE TESTING SUITES (400 MODULES)")
    print("=" * 60)

    for s_name, (gen_fn, curr_key) in CORE_SUITES.items():
        print(f"\n--- Processing {s_name} ---")
        suite_dir = ROOT / s_name
        modules = gen_fn()
        curriculum = ALL_CURRICULA[curr_key]()
        write_suite_data(suite_dir, curriculum, modules)
        print(f"  [OK] Successfully deployed {len(modules)} modules to {s_name}")


def sync_tapi_variants():
    print("\n" + "=" * 60)
    print("SYNCING TAPI CHEMISTRY STUDENT VARIANTS (KOŠAŘ & MAZUR)")
    print("=" * 60)

    src_dir = ROOT / "tapi-chemistry" / "data"
    for dest_name in ["tapi-chemistry-kosar", "tapi-chemistry-mazur"]:
        dest_dir = ROOT / dest_name / "data"
        dest_tests = dest_dir / "tests"
        if dest_tests.exists():
            shutil.rmtree(dest_tests)
        shutil.copytree(src_dir / "tests", dest_tests)
        shutil.copy2(src_dir / "curriculum_manifest.json", dest_dir / "curriculum_manifest.json")
        shutil.copy2(src_dir / "manifest.js", dest_dir / "manifest.js")
        shutil.copy2(src_dir / "tests_registry.js", dest_dir / "tests_registry.js")
        print(f"  [OK] Synced {len(list(dest_tests.glob('*.json')))} tests and manifests to {dest_name}")


def create_bidfood_schema(suite_dir, pattern, title):
    schema_dir = suite_dir / "schema"
    schema_dir.mkdir(parents=True, exist_ok=True)
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": title,
        "type": "object",
        "required": [
            "test_id", "title", "level", "category", "workplace_track",
            "estimated_time_minutes", "description", "questions"
        ],
        "properties": {
            "test_id": { "type": "string", "pattern": pattern },
            "title": { "type": "string", "minLength": 5 },
            "level": { "type": "string", "enum": ["A2", "B1", "B2", "C1"] },
            "category": { "type": "string", "enum": ["core", "specialized"] },
            "workplace_track": { "type": "string" },
            "estimated_time_minutes": { "type": "integer", "minimum": 8, "maximum": 30 },
            "description": { "type": "string" },
            "learning_objectives": { "type": "array", "items": { "type": "string" } },
            "questions": {
                "type": "array",
                "minItems": 8,
                "maxItems": 12,
                "items": {
                    "type": "object",
                    "required": ["id", "prompt", "options", "correct_key", "explanations", "cz_learning_point", "workplace_track"],
                    "properties": {
                        "id": { "type": "string" },
                        "prompt": { "type": "string", "minLength": 8 },
                        "options": {
                            "type": "array",
                            "minItems": 3,
                            "maxItems": 5,
                            "items": {
                                "type": "object",
                                "required": ["key", "text"],
                                "properties": {
                                    "key": { "type": "string", "enum": ["A", "B", "C", "D", "E"] },
                                    "text": { "type": "string", "minLength": 1 }
                                }
                            }
                        },
                        "correct_key": { "type": "string", "enum": ["A", "B", "C", "D", "E"] },
                        "explanations": { "type": "object", "required": ["correct"] },
                        "cz_learning_point": { "type": "string", "minLength": 10 },
                        "workplace_track": { "type": "string" }
                    }
                }
            }
        }
    }
    with open(schema_dir / "test_schema.json", "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2, ensure_ascii=False)


def create_bidfood_engine(suite_dir, default_storage_prefix, primary_color, primary_dark, primary_accent):
    engine_dir = suite_dir / "engine"
    engine_dir.mkdir(parents=True, exist_ok=True)
    
    # Read reference app.js from tatra-engineering
    ref_app_path = ROOT / "tatra-engineering" / "engine" / "app.js"
    app_js = ref_app_path.read_text(encoding="utf-8")
    app_js = app_js.replace(
        "this.storagePrefix = 'tatra_eng_test_';",
        f"this.storagePrefix = options.storagePrefix || '{default_storage_prefix}';"
    )
    with open(engine_dir / "app.js", "w", encoding="utf-8") as f:
        f.write(app_js)

    # Styles.css with domain branding
    ref_css_path = ROOT / "tapi-chemistry-kosar" / "engine" / "styles.css"
    css = ref_css_path.read_text(encoding="utf-8")
    css = css.replace("--primary: #059669;", f"--primary: {primary_color};")
    css = css.replace("--primary-dark: #064e3b;", f"--primary-dark: {primary_dark};")
    css = css.replace("--primary-accent: #10b981;", f"--primary-accent: {primary_accent};")
    with open(engine_dir / "styles.css", "w", encoding="utf-8") as f:
        f.write(css)


def generate_portal_html(portal_title, brand_badge_text, brand_badge_color, org_subtitle, student_name, hero_title, hero_desc, storage_prefix, footer_text):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>{portal_title}</title>
  <link rel="stylesheet" href="engine/styles.css">
  <style>
    .hero-banner {{
      background: linear-gradient(135deg, var(--navy-dark) 0%, var(--primary-dark) 60%, var(--primary) 100%);
      color: #ffffff;
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      margin-bottom: 28px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
      border-left: 8px solid var(--primary-accent);
    }}
    .hero-banner h1 {{ font-size: 2rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 10px; }}
    .hero-banner p {{ font-size: 1rem; color: #cbd5e1; max-width: 780px; line-height: 1.6; margin-bottom: 20px; }}
    .hero-stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 140px), 1fr)); gap: 14px; margin-top: 24px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.15); }}
    .hero-stat-card {{ background: rgba(255, 255, 255, 0.08); backdrop-filter: blur(8px); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: var(--radius-md); padding: 14px 18px; }}
    .hero-stat-number {{ font-size: 1.6rem; font-weight: 800; color: #ffffff; line-height: 1.1; }}
    .hero-stat-label {{ font-size: 0.78rem; color: #cbd5e1; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }}

    .filter-section {{ background: #ffffff; border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 22px; margin-bottom: 28px; box-shadow: var(--shadow-sm); }}
    .search-input {{ width: 100%; padding: 12px 16px; border: 2px solid var(--border-subtle); border-radius: var(--radius-md); font-size: 0.95rem; font-family: inherit; margin-bottom: 16px; }}
    .search-input:focus {{ outline: none; border-color: var(--primary); }}
    .filter-chips-row {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }}
    .filter-label {{ font-size: 0.8rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-right: 4px; min-width: 60px; }}
    .filter-chip {{ background: #f1f5f9; border: 1px solid var(--border-subtle); color: #334155; font-size: 0.82rem; font-weight: 600; padding: 6px 14px; border-radius: 9999px; cursor: pointer; }}
    .filter-chip.active {{ background: var(--primary); color: #ffffff; border-color: var(--primary); }}

    .modules-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr)); gap: 20px; margin-bottom: 40px; }}
    .module-card {{ background: #ffffff; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 22px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: var(--shadow-sm); transition: all 0.2s; }}
    .module-card:hover {{ border-color: var(--primary); box-shadow: var(--shadow-md); transform: translateY(-2px); }}
    .module-id {{ font-family: monospace; font-weight: 800; font-size: 0.82rem; color: var(--primary-dark); background: #f1f5f9; padding: 2px 6px; border-radius: 4px; }}
    .module-card h3 {{ font-size: 1.1rem; font-weight: 700; color: var(--navy-dark); margin: 8px 0; }}
    .module-card p {{ font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 12px; }}
    .module-grammar-tag {{ font-size: 0.76rem; color: #0284c7; background: #f0f9ff; border: 1px solid #bae6fd; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 14px; font-weight: 600; }}
    .card-footer {{ display: flex; justify-content: space-between; align-items: center; padding-top: 14px; border-top: 1px solid var(--border-subtle); }}

    .tier-a2-highlight {{ background: #fefce8; border: 1px solid #fef08a; padding: 12px 18px; border-radius: var(--radius-md); margin-bottom: 20px; font-size: 0.88rem; color: #854d0e; display: flex; gap: 12px; align-items: center; }}

    @media (max-width: 768px) {{
      .hero-banner {{ padding: 22px 16px; border-left-width: 5px; }}
      .hero-banner h1 {{ font-size: 1.45rem; line-height: 1.25; }}
      .hero-stats-grid {{ grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 18px; }}
      .modules-grid {{ grid-template-columns: 1fr; gap: 16px; }}
    }}
  </style>
</head>
<body>
  <header class="suite-header">
    <div class="header-container">
      <div class="brand-wrapper">
        <span class="brand-logo-badge" style="background:{brand_badge_color};">{brand_badge_text}</span>
        <div class="brand-titles">
          <h1>{portal_title}</h1>
          <p>{org_subtitle}</p>
        </div>
      </div>
      <div>
        <span style="font-size:0.85rem; background:rgba(255,255,255,0.15); padding:6px 14px; border-radius:9999px; font-weight:700;">👤 {student_name}</span>
      </div>
    </div>
  </header>

  <div class="main-layout">
    <section class="hero-banner">
      <h1>{hero_title}</h1>
      <p>{hero_desc}</p>
      <div class="hero-stats-grid">
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-total-modules">0</div><div class="hero-stat-label">Total Modules</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-a2-modules">0</div><div class="hero-stat-label">A2 Foundation Tier</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-b1-b2-modules">0</div><div class="hero-stat-label">B1 & B2 Core</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">0</div><div class="hero-stat-label">C1 Advanced Tier</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-user-completed">0</div><div class="hero-stat-label">Completed by You</div></div>
      </div>
    </section>

    <div class="tier-a2-highlight">
      <span style="font-size: 1.4rem;">💡</span>
      <div>
        <strong>A2 Pre-Intermediate Foundation Tier:</strong> Start with A2 for fast-paced terminology acquisition, routine email inquiries, delivery notes, and daily workplace operations before advancing to B1 and B2 core diagnostic modules.
      </div>
    </div>

    <section class="filter-section">
      <input type="text" id="module-search" class="search-input" placeholder="Search by topic, grammar focus, track, or module ID...">
      
      <div class="filter-chips-row">
        <span class="filter-label">Level:</span>
        <button class="filter-chip active" data-filter-type="level" data-filter-val="all">All Levels</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="A2">Tier 0: A2 Foundation</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="B1">Tier 1: B1 Operational</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="B2">Tier 2: B2 Advanced</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Advanced</button>
      </div>

      <div class="filter-chips-row" id="track-chips-container">
        <span class="filter-label">Track:</span>
        <button class="filter-chip active" data-filter-type="track" data-filter-val="all">All Tracks</button>
      </div>
    </section>

    <main>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <h2 style="font-size:1.25rem; font-weight:700;">Curriculum Modules</h2>
        <span style="font-size:0.85rem; color:var(--text-muted);" id="results-count-text">Loading modules...</span>
      </div>
      <div class="modules-grid" id="modules-grid"></div>
    </main>
  </div>

  <footer class="suite-footer">
    <p><strong>{footer_text}</strong> | Dedicated Assessment Environment with Contrastive Czech-English Diagnostics</p>
  </footer>

  <script src="data/manifest.js"></script>
  <script>
    let allModules = [];
    let currentLevelFilter = 'all';
    let currentTrackFilter = 'all';
    let searchQuery = '';
    const storagePrefix = '{storage_prefix}';

    async function initSuitePortal() {{
      try {{
        if (window.CURRICULUM_MANIFEST && Array.isArray(window.CURRICULUM_MANIFEST)) {{
          allModules = window.CURRICULUM_MANIFEST;
        }} else {{
          const resp = await fetch('data/curriculum_manifest.json');
          if (!resp.ok) throw new Error('Failed to load manifest');
          allModules = await resp.json();
        }}
        updateStats();
        populateTrackFilters();
        setupFilters();
        renderModules();
      }} catch (err) {{
        document.getElementById('modules-grid').innerHTML = '<div class="question-card"><p>Failed to load manifest.</p></div>';
      }}
    }}

    function updateStats() {{
      document.getElementById('stat-total-modules').textContent = allModules.length;
      document.getElementById('stat-a2-modules').textContent = allModules.filter(m => m.level === 'A2').length;
      document.getElementById('stat-b1-b2-modules').textContent = allModules.filter(m => m.level === 'B1' || m.level === 'B2').length;
      document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;

      let completed = 0;
      allModules.forEach(m => {{
        try {{
          const saved = localStorage.getItem(`${{storagePrefix}}${{m.test_id}}`);
          if (saved) {{
            const parsed = JSON.parse(saved);
            if (parsed.userAnswers && Object.keys(parsed.userAnswers).length > 0) completed++;
          }}
        }} catch(e) {{}}
      }});
      document.getElementById('stat-user-completed').textContent = completed;
    }}

    function populateTrackFilters() {{
      const tracks = Array.from(new Set(allModules.map(m => m.workplace_track)));
      const container = document.getElementById('track-chips-container');
      tracks.forEach(t => {{
        const btn = document.createElement('button');
        btn.className = 'filter-chip';
        btn.setAttribute('data-filter-type', 'track');
        btn.setAttribute('data-filter-val', t);
        btn.textContent = t.length > 25 ? t.substring(0, 23) + '...' : t;
        btn.title = t;
        container.appendChild(btn);
      }});
    }}

    function setupFilters() {{
      document.getElementById('module-search').addEventListener('input', (e) => {{
        searchQuery = e.target.value.toLowerCase().trim();
        renderModules();
      }});

      document.querySelectorAll('.filter-chip').forEach(chip => {{
        chip.addEventListener('click', (e) => {{
          const type = e.currentTarget.getAttribute('data-filter-type');
          const val = e.currentTarget.getAttribute('data-filter-val');
          document.querySelectorAll(`.filter-chip[data-filter-type="${{type}}"]`).forEach(c => c.classList.remove('active'));
          e.currentTarget.classList.add('active');

          if (type === 'level') currentLevelFilter = val;
          if (type === 'track') currentTrackFilter = val;
          renderModules();
        }});
      }});
    }}

    function renderModules() {{
      const grid = document.getElementById('modules-grid');
      const filtered = allModules.filter(m => {{
        if (currentLevelFilter !== 'all' && m.level !== currentLevelFilter) return false;
        if (currentTrackFilter !== 'all' && m.workplace_track !== currentTrackFilter) return false;
        if (searchQuery) {{
          const corpus = `${{m.test_id}} ${{m.title}} ${{m.description}} ${{m.grammar_focus || ''}} ${{m.workplace_track}}`.toLowerCase();
          if (!corpus.includes(searchQuery)) return false;
        }}
        return true;
      }});

      document.getElementById('results-count-text').textContent = `Showing ${{filtered.length}} of ${{allModules.length}} modules`;

      if (filtered.length === 0) {{
        grid.innerHTML = '<div class="question-card" style="grid-column: 1/-1; text-align: center;"><p>No modules matched your search.</p></div>';
        return;
      }}

      grid.innerHTML = filtered.map(m => {{
        let statusHtml = '';
        try {{
          const saved = localStorage.getItem(`${{storagePrefix}}${{m.test_id}}`);
          if (saved) {{
            const parsed = JSON.parse(saved);
            const ansCount = parsed.userAnswers ? Object.keys(parsed.userAnswers).length : 0;
            if (ansCount > 0) statusHtml = `<span style="font-size:0.75rem; background:#ecfdf5; color:#065f46; padding:3px 8px; border-radius:4px; font-weight:700;">✓ Saved (${{ansCount}})</span>`;
          }}
        }} catch(e) {{}}

        return `
          <article class="module-card">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="module-id">${{m.test_id}}</span>
                <span class="badge badge-level-${{m.level.toLowerCase().replace('/', '-')}}">${{m.level}}</span>
              </div>
              <h3>${{m.title}}</h3>
              <p>${{m.description}}</p>
              ${{m.grammar_focus ? `<div class="module-grammar-tag">🎯 ${{m.grammar_focus}}</div>` : ''}}
              <div style="font-size:0.78rem; color:#475569; font-weight:600;">🏢 ${{m.workplace_track}}</div>
            </div>
            <div class="card-footer">
              <span style="font-size:0.8rem; color:var(--text-muted);">⏱ ${{m.estimated_time_minutes || 15}} min</span>
              ${{statusHtml || '<span style="font-size:0.75rem; color:#64748b;">Ready</span>'}}
              <a href="test_runner.html?test=${{m.test_id}}" class="btn btn-primary" style="padding:6px 14px; font-size:0.8rem;">Launch →</a>
            </div>
          </article>
        `;
      }}).join('');
    }}

    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', initSuitePortal);
    }} else {{
      initSuitePortal();
    }}
  </script>
</body>
</html>
"""


def generate_test_runner_html(runner_title, brand_badge_text, brand_badge_color, header_title, org_subtitle, storage_prefix, default_test_id, footer_text):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>{runner_title}</title>
  <link rel="stylesheet" href="engine/styles.css">
</head>
<body>
  <header class="suite-header">
    <div class="header-container">
      <a href="index.html" class="brand-wrapper">
        <span class="brand-logo-badge" style="background:{brand_badge_color};">{brand_badge_text}</span>
        <div class="brand-titles">
          <h1>{header_title}</h1>
          <p>{org_subtitle}</p>
        </div>
      </a>
      <div>
        <a href="index.html" class="btn btn-secondary">← Suite Portal</a>
      </div>
    </div>
  </header>

  <div class="main-layout" id="test-app-root"></div>

  <footer class="suite-footer">
    <p><strong>{footer_text}</strong></p>
    <p style="margin-top:6px; font-size:0.8rem; color:#94a3b8;">Dedicated Testing Environment with Contrastive Czech-English Diagnostics</p>
  </footer>

  <script src="engine/app.js"></script>
  <script src="data/tests_registry.js"></script>
  <script>
    async function startRunner() {{
      const urlParams = new URLSearchParams(window.location.search);
      const testId = urlParams.get('test') || '{default_test_id}';
      const engine = new SuiteTestEngine({{ containerId: 'test-app-root', storagePrefix: '{storage_prefix}' }});

      try {{
        let testData = null;
        if (window.TEST_REGISTRY && window.TEST_REGISTRY[testId]) {{
          testData = window.TEST_REGISTRY[testId];
        }} else {{
          const resp = await fetch(`data/tests/${{testId}}.json`);
          if (!resp.ok) throw new Error(`HTTP ${{resp.status}}`);
          testData = await resp.json();
        }}
        engine.init(testData);
      }} catch (err) {{
        document.getElementById('test-app-root').innerHTML = `
          <div class="question-card" style="text-align: center; padding: 40px;">
            <h2 style="color: var(--primary); margin-bottom: 12px;">⚠️ Test Module Not Found</h2>
            <p style="color: var(--text-secondary); margin-bottom: 20px;">
              Could not load <strong>${{testId}}.json</strong>. Please ensure the test JSON file exists in <code>data/tests/</code>.
            </p>
            <div style="display:flex; justify-content:center; gap:12px;">
              <a href="test_runner.html?test={default_test_id}" class="btn btn-primary">Load A2 Pilot Test</a>
              <a href="index.html" class="btn btn-secondary">Return to Portal</a>
            </div>
          </div>
        `;
      }}
    }}

    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', startRunner);
    }} else {{
      startRunner();
    }}
  </script>
</body>
</html>
"""


def deploy_bidfood_sandboxes():
    print("\n" + "=" * 60)
    print("DEPLOYING 3 DEDICATED BIDFOOD STUDENT SANDBOXES (240 MODULES)")
    print("=" * 60)

    # 1. Generate Bidfood Purchasing modules once
    pur_modules = generate_bidfood_purchasing_modules()
    pur_curr = ALL_CURRICULA["bidfood-purchasing"]()

    # 2. Generate Bidfood Engineering modules once
    eng_modules = generate_bidfood_engineering_modules()
    eng_curr = ALL_CURRICULA["bidfood-engineering"]()

    sandboxes = [
        {
            "dir_name": "bidfood-purchasing-libor",
            "student_name": "Libor Barvenčík",
            "role": "Wholesale Purchasing & Cold-Chain Procurement",
            "portal_title": "Bidfood Purchasing Assessment Hub — Libor Barvenčík",
            "brand_badge": "BIDFOOD | LIBOR",
            "badge_color": "#1e40af",
            "storage_prefix": "bidfood_pur_libor_test_",
            "default_test": "BID-PUR-A2-001",
            "modules": pur_modules,
            "curriculum": pur_curr,
            "schema_pattern": r"^BID-PUR-(A2|B1|B2|C1|C2|SP)-\d{3}$",
            "schema_title": "Bidfood Purchasing Test Schema",
            "primary": "#1e40af",
            "dark": "#172554",
            "accent": "#3b82f6"
        },
        {
            "dir_name": "bidfood-purchasing-lucie",
            "student_name": "Lucie Rončková",
            "role": "Wholesale Purchasing & Cold-Chain Procurement",
            "portal_title": "Bidfood Purchasing Assessment Hub — Lucie Rončková",
            "brand_badge": "BIDFOOD | LUCIE",
            "badge_color": "#1e40af",
            "storage_prefix": "bidfood_pur_lucie_test_",
            "default_test": "BID-PUR-A2-001",
            "modules": pur_modules,
            "curriculum": pur_curr,
            "schema_pattern": r"^BID-PUR-(A2|B1|B2|C1|C2|SP)-\d{3}$",
            "schema_title": "Bidfood Purchasing Test Schema",
            "primary": "#1e40af",
            "dark": "#172554",
            "accent": "#3b82f6"
        },
        {
            "dir_name": "bidfood-engineering-jiri",
            "student_name": "Ing. Jiří Lorenčík",
            "role": "Plant Process Engineering & Automation",
            "portal_title": "Bidfood Process Engineering Assessment Hub — Jiří Lorenčík",
            "brand_badge": "BIDFOOD | JIŘÍ",
            "badge_color": "#0f766e",
            "storage_prefix": "bidfood_eng_jiri_test_",
            "default_test": "BID-ENG-A2-001",
            "modules": eng_modules,
            "curriculum": eng_curr,
            "schema_pattern": r"^BID-ENG-(A2|B1|B2|C1|C2|SP)-\d{3}$",
            "schema_title": "Bidfood Process Engineering Test Schema",
            "primary": "#0f766e",
            "dark": "#134e4a",
            "accent": "#14b8a6"
        }
    ]

    for sb in sandboxes:
        sb_dir = ROOT / sb["dir_name"]
        print(f"\n--- Deploying {sb['dir_name']} ({sb['student_name']}) ---")
        sb_dir.mkdir(parents=True, exist_ok=True)

        # Schema & Engine
        create_bidfood_schema(sb_dir, sb["schema_pattern"], sb["schema_title"])
        create_bidfood_engine(sb_dir, sb["storage_prefix"], sb["primary"], sb["dark"], sb["accent"])

        # Test data & manifests
        write_suite_data(sb_dir, sb["curriculum"], sb["modules"])

        # Portal index.html
        index_html = generate_portal_html(
            portal_title=sb["portal_title"],
            brand_badge_text=sb["brand_badge"],
            brand_badge_color=sb["badge_color"],
            org_subtitle=f"Bidfood Czech Republic | Assessed Professional: {sb['student_name']}",
            student_name=sb["student_name"],
            hero_title=sb["portal_title"],
            hero_desc=f"Dedicated assessment portal for {sb['student_name']} ({sb['role']}) covering cold-chain logistics, international supplier communication, and GxP food industry standards.",
            storage_prefix=sb["storage_prefix"],
            footer_text=f"Bidfood Czech Republic | {sb['portal_title']}"
        )
        with open(sb_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(index_html)

        # Test runner.html
        runner_html = generate_test_runner_html(
            runner_title=f"{sb['student_name']} | Interactive Test Runner",
            brand_badge_text=sb["brand_badge"],
            brand_badge_color=sb["badge_color"],
            header_title=sb["portal_title"],
            org_subtitle=f"Bidfood Czech Republic | Assessed Professional: {sb['student_name']}",
            storage_prefix=sb["storage_prefix"],
            default_test_id=sb["default_test"],
            footer_text=f"Bidfood Czech Republic | Assessed Professional: {sb['student_name']}"
        )
        with open(sb_dir / "test_runner.html", "w", encoding="utf-8") as f:
            f.write(runner_html)

        print(f"  [OK] Successfully deployed {len(sb['modules'])} modules & standalone portal for {sb['student_name']}")


def audit_ecosystem():
    print("\n" + "=" * 60)
    print("RUNNING ECOSYSTEM-WIDE REPETITION & QUALITY AUDIT")
    print("=" * 60)

    suites_to_audit = [
        "tatra-engineering",
        "tatra-sales-engineering",
        "tapi-engineering",
        "tapi-chemistry",
        "tapi-it",
        "tapi-chemistry-kosar",
        "tapi-chemistry-mazur",
        "bidfood-purchasing-libor",
        "bidfood-purchasing-lucie",
        "bidfood-engineering-jiri"
    ]

    total_modules_audited = 0
    total_dup_modules = 0

    for s in suites_to_audit:
        p = ROOT / s / "data" / "tests"
        if not p.exists():
            continue
        dup_mods = []
        schema_file = ROOT / s / "schema" / "test_schema.json"
        has_schema = schema_file.exists()
        if has_schema:
            schema = json.load(open(schema_file, encoding="utf-8"))
            v = jsonschema.Draft7Validator(schema)

        schema_errors = 0
        bias_errors = 0

        for jf in sorted(p.glob("*.json")):
            total_modules_audited += 1
            with open(jf, encoding="utf-8") as f:
                d = json.load(f)

            if has_schema:
                for err in v.iter_errors(d):
                    schema_errors += 1
                    print(f"[{s} - {jf.name}] Schema Error: {err.message}")

            qs = d.get("questions", [])
            prompts = [q["prompt"] for q in qs]
            c = Counter(prompts)
            max_rep = max(c.values()) if c else 0
            if max_rep > 1:
                dup_mods.append((jf.name, max_rep))

            keys = [q["correct_key"] for q in qs]
            key_counts = Counter(keys)
            if max(key_counts.values()) > 5:
                bias_errors += 1

        total_dup_modules += len(dup_mods)
        status_str = f"DUPLICATES: {len(dup_mods)}" if dup_mods else "0 DUPLICATES (PASS)"
        print(f"[{s:26}] {len(list(p.glob('*.json'))):2} modules | {status_str} | Schema Errs: {schema_errors} | Bias Errs: {bias_errors}")
        if dup_mods:
            for m_name, count in dup_mods[:3]:
                print(f"    -> {m_name}: {count} identical prompts!")

    print("\n" + "=" * 60)
    print(f"AUDIT SUMMARY: {total_modules_audited} TOTAL TEST MODULES AUDITED")
    print(f"MODULES WITH DUPLICATED PROMPTS: {total_dup_modules}")
    print("=" * 60)
    if total_dup_modules > 0:
        print("FAIL: Duplicates still detected!")
        sys.exit(1)
    else:
        print("SUCCESS: 100% OF MODULES HAVE ZERO DUPLICATE PROMPTS!")


def main():
    deploy_core_suites()
    sync_tapi_variants()
    deploy_bidfood_sandboxes()
    audit_ecosystem()

if __name__ == "__main__":
    main()
