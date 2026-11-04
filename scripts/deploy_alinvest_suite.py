#!/usr/bin/env python3
"""
Deploy Standalone Assessment Suite for Vojtěch Berger:
- AL INVEST Břidličná, a.s. | Divize Obaly / Packaging Division
- 84 Total Modules:
    * 20 A2 Foundation (AL-PKG-A2-001 to 020)
    * 20 B1 Operational (AL-PKG-B1-001 to 020)
    * 20 B2 Upper-Intermediate (AL-PKG-B2-001 to 020)
    * 20 C1 Leadership (AL-PKG-C1-001 to 020)
    * 4 Specialized Football & World Sports (AL-PKG-SP-001 to 004)
- Unique localStorage prefix: alinvest_pkg_vojtech_test_ (100% preservation of student results)
- Standalone Portal UI & Interactive Test Runner with direct link to Interactive Grammar Deck.
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

from curriculum_catalog import get_alinvest_packaging_curriculum
from generators.alinvest_packaging import generate_alinvest_packaging_modules
from generate_vojtech_specialized_modules import VOJTECH_SPECIALIZED_MODULES

SUITE_DIR = ROOT / "alinvest-packaging-vojtech"

def create_schema(suite_dir):
    schema_dir = suite_dir / "schema"
    schema_dir.mkdir(parents=True, exist_ok=True)
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "AL INVEST Packaging Division Test Schema",
        "type": "object",
        "required": [
            "test_id", "title", "level", "category", "workplace_track",
            "estimated_time_minutes", "description", "questions"
        ],
        "properties": {
            "test_id": { "type": "string", "pattern": "^AL-PKG-(A2|B1|B2|C1|SP)-\\d{3}$" },
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

def create_engine(suite_dir):
    engine_dir = suite_dir / "engine"
    engine_dir.mkdir(parents=True, exist_ok=True)
    
    # Read reference app.js from tatra-engineering
    ref_app_path = ROOT / "tatra-engineering" / "engine" / "app.js"
    app_js = ref_app_path.read_text(encoding="utf-8")
    app_js = app_js.replace(
        "this.storagePrefix = 'tatra_eng_test_';",
        "this.storagePrefix = options.storagePrefix || 'alinvest_pkg_vojtech_test_';"
    )
    with open(engine_dir / "app.js", "w", encoding="utf-8") as f:
        f.write(app_js)

    # Styles.css with AL INVEST aluminium branding (#0284c7)
    ref_css_path = ROOT / "tapi-chemistry-kosar" / "engine" / "styles.css"
    css = ref_css_path.read_text(encoding="utf-8")
    css = css.replace("--primary: #059669;", "--primary: #0284c7;")
    css = css.replace("--primary-dark: #064e3b;", "--primary-dark: #0c4a6e;")
    css = css.replace("--primary-accent: #10b981;", "--primary-accent: #38bdf8;")
    with open(engine_dir / "styles.css", "w", encoding="utf-8") as f:
        f.write(css)

def generate_portal_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>AL INVEST Packaging Assessment Hub — Vojtěch Berger</title>
  <link rel="stylesheet" href="engine/styles.css">
  <style>
    .hero-banner {
      background: linear-gradient(135deg, var(--navy-dark) 0%, var(--primary-dark) 60%, var(--primary) 100%);
      color: #ffffff;
      border-radius: var(--radius-lg);
      padding: 36px 32px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
      border-left: 8px solid var(--primary-accent);
    }
    .hero-banner h1 { font-size: 2rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 10px; }
    .hero-banner p { font-size: 1rem; color: #cbd5e1; max-width: 820px; line-height: 1.6; margin-bottom: 20px; }
    .hero-stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 140px), 1fr)); gap: 14px; margin-top: 24px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.15); }
    .hero-stat-card { background: rgba(255, 255, 255, 0.08); backdrop-filter: blur(8px); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: var(--radius-md); padding: 14px 18px; }
    .hero-stat-number { font-size: 1.6rem; font-weight: 800; color: #ffffff; line-height: 1.1; }
    .hero-stat-label { font-size: 0.78rem; color: #cbd5e1; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }

    /* Lesson Deck Promo Banner */
    .deck-promo-card {
      background: linear-gradient(90deg, #f0fdf4 0%, #e0f2fe 100%);
      border: 2px solid #38bdf8;
      border-radius: var(--radius-lg);
      padding: 20px 24px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      box-shadow: var(--shadow-sm);
    }
    .deck-promo-info h3 { font-size: 1.15rem; font-weight: 800; color: #0369a1; margin-bottom: 4px; }
    .deck-promo-info p { font-size: 0.9rem; color: #334155; margin: 0; }
    .deck-promo-btn {
      background: #0284c7;
      color: #ffffff;
      padding: 10px 20px;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.88rem;
      text-decoration: none;
      white-space: nowrap;
      transition: all 0.2s;
      box-shadow: 0 2px 4px rgba(2, 132, 199, 0.25);
    }
    .deck-promo-btn:hover { background: #0369a1; transform: translateY(-1px); }

    .filter-section { background: #ffffff; border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 22px; margin-bottom: 28px; box-shadow: var(--shadow-sm); }
    .search-input { width: 100%; padding: 12px 16px; border: 2px solid var(--border-subtle); border-radius: var(--radius-md); font-size: 0.95rem; font-family: inherit; margin-bottom: 16px; }
    .search-input:focus { outline: none; border-color: var(--primary); }
    .filter-chips-row { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
    .filter-label { font-size: 0.8rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-right: 4px; min-width: 60px; }
    .filter-chip { background: #f1f5f9; border: 1px solid var(--border-subtle); color: #334155; font-size: 0.82rem; font-weight: 600; padding: 6px 14px; border-radius: 9999px; cursor: pointer; }
    .filter-chip.active { background: var(--primary); color: #ffffff; border-color: var(--primary); }

    .modules-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr)); gap: 20px; margin-bottom: 40px; }
    .module-card { background: #ffffff; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 22px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: var(--shadow-sm); transition: all 0.2s; }
    .module-card:hover { border-color: var(--primary); box-shadow: var(--shadow-md); transform: translateY(-2px); }
    .module-id { font-family: monospace; font-weight: 800; font-size: 0.82rem; color: var(--primary-dark); background: #f1f5f9; padding: 2px 6px; border-radius: 4px; }
    .module-card h3 { font-size: 1.05rem; font-weight: 700; color: var(--navy-dark); margin: 8px 0; }
    .module-card p { font-size: 0.86rem; color: var(--text-secondary); margin-bottom: 12px; }
    .module-grammar-tag { font-size: 0.76rem; color: #0284c7; background: #f0f9ff; border: 1px solid #bae6fd; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 14px; font-weight: 600; }
    .card-footer { display: flex; justify-content: space-between; align-items: center; padding-top: 14px; border-top: 1px solid var(--border-subtle); }

    .tier-a2-highlight { background: #fefce8; border: 1px solid #fef08a; padding: 12px 18px; border-radius: var(--radius-md); margin-bottom: 20px; font-size: 0.88rem; color: #854d0e; display: flex; gap: 12px; align-items: center; }

    @media (max-width: 768px) {
      .hero-banner { padding: 22px 16px; border-left-width: 5px; }
      .hero-banner h1 { font-size: 1.45rem; line-height: 1.25; }
      .deck-promo-card { flex-direction: column; align-items: flex-start; }
      .hero-stats-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 18px; }
      .modules-grid { grid-template-columns: 1fr; gap: 16px; }
    }
  </style>
</head>
<body>
  <header class="suite-header">
    <div class="header-container">
      <div class="brand-wrapper">
        <span class="brand-logo-badge" style="background:#0284c7;">AL INVEST | VOJTĚCH</span>
        <div class="brand-titles">
          <h1>AL INVEST Packaging Assessment Hub — Vojtěch Berger</h1>
          <p>AL INVEST Břidličná, a.s. | Packaging Division | Assessed Professional: Vojtěch Berger</p>
        </div>
      </div>
      <div style="display:flex; align-items:center; gap:12px;">
        <a href="../index.html" class="btn btn-secondary">← Main Assessor Portal</a>
        <span style="font-size:0.85rem; background:rgba(255,255,255,0.15); padding:6px 14px; border-radius:9999px; font-weight:700;">👤 Vojtěch Berger</span>
      </div>
    </div>
  </header>

  <div class="main-layout">
    <section class="hero-banner">
      <h1>AL INVEST Břidličná | Divize Obaly — Vojtěch Berger</h1>
      <p>
        Bespoke 84-module technical English assessment suite for <strong>Vojtěch Berger</strong> (Specialista kvality - divize Obaly).
        Rigorous focus on aluminium food packaging quality (foil converting, gauge tolerances in &mu;m, pinhole detection, dyne wetting tension, lamination, BRCGS Issue 6 &amp; 8D CAPA) combined with <strong>World Sports &amp; Football Analytics</strong> (pressing structures, VAR refereeing, and expected goals models).
      </p>
      <div class="hero-stats-grid">
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-total-modules">84</div><div class="hero-stat-label">Total Modules</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-a2-modules">20</div><div class="hero-stat-label">A2 Foundation Tier</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-b1-b2-modules">40</div><div class="hero-stat-label">B1 & B2 Core Tiers</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-c1-modules">20</div><div class="hero-stat-label">C1 Advanced Tier</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-sp-modules" style="color:#38bdf8;">4</div><div class="hero-stat-label">⚽ Football Analytics</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-user-completed">0</div><div class="hero-stat-label">Completed by You</div></div>
      </div>
    </section>

    <!-- Interactive Lesson Deck Promo Banner -->
    <div class="deck-promo-card">
      <div class="deck-promo-info">
        <h3>🗣️ Interactive Spoken &amp; Grammar Presentation Deck Available</h3>
        <p>19-slide interactive lesson deck featuring 4 spoken audits, 18 live diagnostic check items, top 6 Czenglish traps, and 2 case studies.</p>
      </div>
      <a href="../Vojtech_Berger_Grammar_Deck.html" class="deck-promo-btn" target="_blank">Launch Grammar Deck ↗</a>
    </div>

    <div class="tier-a2-highlight">
      <span style="font-size:1.4rem;">💡</span>
      <div>
        <strong>A2 Foundation Tier:</strong> Start with A2 for fast-paced terminology acquisition, foil converting SOPs, slitting tools, and cleanroom PPE before advancing to B1 and B2 core diagnostic modules.
      </div>
    </div>

    <section class="filter-section">
      <input type="text" id="module-search" class="search-input" placeholder="Search by topic, grammar focus, track, or module ID...">
      
      <div class="filter-chips-row">
        <span class="filter-label">Level:</span>
        <button class="filter-chip active" data-filter-type="level" data-filter-val="all">All Levels</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="A2">Tier 0: A2 Foundation (20)</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="B1">Tier 1: B1 Operational (20)</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="B2">Tier 2: B2 Advanced (20)</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="C1">Tier 3: C1 Leadership (20)</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="specialized">⚽ Football Analytics (4)</button>
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
    <p><strong>AL INVEST Břidličná, a.s. | Packaging Division — Vojtěch Berger</strong></p>
    <p style="margin-top:6px; font-size:0.8rem; color:#94a3b8;">Dedicated Testing Environment with Contrastive Czech-English Diagnostics &amp; Local Storage Persistence</p>
  </footer>

  <script src="data/manifest.js"></script>
  <script>
    let allModules = [];
    let currentLevelFilter = 'all';
    let currentTrackFilter = 'all';
    let searchQuery = '';
    const storagePrefix = 'alinvest_pkg_vojtech_test_';

    async function initSuitePortal() {
      try {
        if (window.CURRICULUM_MANIFEST && Array.isArray(window.CURRICULUM_MANIFEST)) {
          allModules = window.CURRICULUM_MANIFEST;
        } else {
          const resp = await fetch('data/curriculum_manifest.json');
          if (!resp.ok) throw new Error('Failed to load manifest');
          allModules = await resp.json();
        }
        updateStats();
        populateTrackFilters();
        setupFilters();
        renderModules();
      } catch (err) {
        document.getElementById('modules-grid').innerHTML = '<div class="question-card"><p>Failed to load manifest.</p></div>';
      }
    }

    function updateStats() {
      document.getElementById('stat-total-modules').textContent = allModules.length;
      document.getElementById('stat-a2-modules').textContent = allModules.filter(m => m.level === 'A2').length;
      document.getElementById('stat-b1-b2-modules').textContent = allModules.filter(m => m.level === 'B1' || m.level === 'B2').length;
      document.getElementById('stat-c1-modules').textContent = allModules.filter(m => m.level === 'C1').length;
      document.getElementById('stat-sp-modules').textContent = allModules.filter(m => m.category === 'specialized').length;

      let completed = 0;
      allModules.forEach(m => {
        try {
          const saved = localStorage.getItem(`${storagePrefix}${m.test_id}`);
          if (saved) {
            const parsed = JSON.parse(saved);
            if (parsed.userAnswers && Object.keys(parsed.userAnswers).length > 0) completed++;
          }
        } catch(e) {}
      });
      document.getElementById('stat-user-completed').textContent = completed;
    }

    function populateTrackFilters() {
      const container = document.getElementById('track-chips-container');
      const tracks = [...new Set(allModules.map(m => m.workplace_track))].sort();
      tracks.forEach(track => {
        const btn = document.createElement('button');
        btn.className = 'filter-chip';
        btn.dataset.filterType = 'track';
        btn.dataset.filterVal = track;
        btn.textContent = track;
        btn.addEventListener('click', () => {
          container.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
          btn.classList.add('active');
          currentTrackFilter = track;
          renderModules();
        });
        container.appendChild(btn);
      });
    }

    function setupFilters() {
      document.querySelectorAll('[data-filter-type="level"]').forEach(chip => {
        chip.addEventListener('click', (e) => {
          document.querySelectorAll('[data-filter-type="level"]').forEach(c => c.classList.remove('active'));
          e.target.classList.add('active');
          currentLevelFilter = e.target.dataset.filterVal;
          renderModules();
        });
      });

      const trackAll = document.querySelector('#track-chips-container [data-filter-val="all"]');
      if (trackAll) {
        trackAll.addEventListener('click', () => {
          document.querySelectorAll('#track-chips-container .filter-chip').forEach(c => c.classList.remove('active'));
          trackAll.classList.add('active');
          currentTrackFilter = 'all';
          renderModules();
        });
      }

      document.getElementById('module-search').addEventListener('input', (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        renderModules();
      });
    }

    function renderModules() {
      const grid = document.getElementById('modules-grid');
      const filtered = allModules.filter(m => {
        if (currentLevelFilter !== 'all') {
          if (currentLevelFilter === 'specialized' && m.category !== 'specialized') return false;
          if (currentLevelFilter !== 'specialized' && (m.level !== currentLevelFilter || m.category === 'specialized')) return false;
        }
        if (currentTrackFilter !== 'all' && m.workplace_track !== currentTrackFilter) return false;
        if (searchQuery) {
          const corpus = `${m.test_id} ${m.title} ${m.description} ${m.grammar_focus || ''} ${m.workplace_track}`.toLowerCase();
          if (!corpus.includes(searchQuery)) return false;
        }
        return true;
      });

      document.getElementById('results-count-text').textContent = `Showing ${filtered.length} of ${allModules.length} modules`;

      if (filtered.length === 0) {
        grid.innerHTML = '<div class="question-card" style="grid-column: 1/-1; text-align: center;"><p>No modules matched your search.</p></div>';
        return;
      }

      grid.innerHTML = filtered.map(m => {
        let statusHtml = '';
        try {
          const saved = localStorage.getItem(`${storagePrefix}${m.test_id}`);
          if (saved) {
            const parsed = JSON.parse(saved);
            const ansCount = parsed.userAnswers ? Object.keys(parsed.userAnswers).length : 0;
            if (ansCount > 0) statusHtml = `<span style="font-size:0.75rem; background:#ecfdf5; color:#065f46; padding:3px 8px; border-radius:4px; font-weight:700;">✓ Saved (${ansCount})</span>`;
          }
        } catch(e) {}

        const badgeStyle = m.category === 'specialized' 
          ? 'background:#f0fdf4; color:#15803d; border:1px solid #bbf7d0;'
          : '';

        return `
          <article class="module-card">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="module-id">${m.test_id}</span>
                <span class="badge badge-level-${m.level.toLowerCase().replace('/', '-')}" style="${badgeStyle}">${m.category === 'specialized' ? '⚽ SP: ' + m.level : m.level}</span>
              </div>
              <h3>${m.title}</h3>
              <p>${m.description}</p>
              ${m.grammar_focus ? `<div class="module-grammar-tag">🎯 ${m.grammar_focus}</div>` : ''}
              <div style="font-size:0.78rem; color:#475569; font-weight:600;">🏭 ${m.workplace_track}</div>
            </div>
            <div class="card-footer">
              <span style="font-size:0.8rem; color:var(--text-muted);">⏱ ${m.estimated_time_minutes || 15} min</span>
              ${statusHtml || '<span style="font-size:0.75rem; color:#64748b;">Ready</span>'}
              <a href="test_runner.html?test=${m.test_id}" class="btn btn-primary" style="padding:6px 14px; font-size:0.8rem; background:#0284c7;">Launch →</a>
            </div>
          </article>
        `;
      }).join('');
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initSuitePortal);
    } else {
      initSuitePortal();
    }
  </script>
</body>
</html>"""

def generate_test_runner_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>Vojtěch Berger | Interactive Test Runner</title>
  <link rel="stylesheet" href="engine/styles.css">
</head>
<body>
  <header class="suite-header">
    <div class="header-container">
      <a href="index.html" class="brand-wrapper">
        <span class="brand-logo-badge" style="background:#0284c7;">AL INVEST | VOJTĚCH</span>
        <div class="brand-titles">
          <h1>AL INVEST Packaging Assessment Hub — Vojtěch Berger</h1>
          <p>AL INVEST Břidličná, a.s. | Packaging Division | Assessed Professional: Vojtěch Berger</p>
        </div>
      </a>
      <div style="display:flex; align-items:center; gap:12px;">
        <a href="index.html" class="btn btn-secondary">← Suite Portal</a>
        <a href="../Vojtech_Berger_Grammar_Deck.html" class="btn btn-secondary" target="_blank">Grammar Deck ↗</a>
      </div>
    </div>
  </header>

  <div class="main-layout" id="test-app-root"></div>

  <footer class="suite-footer">
    <p><strong>AL INVEST Břidličná, a.s. | Assessed Professional: Vojtěch Berger</strong></p>
    <p style="margin-top:6px; font-size:0.8rem; color:#94a3b8;">Dedicated Testing Environment with Contrastive Czech-English Diagnostics</p>
  </footer>

  <script src="engine/app.js"></script>
  <script src="data/tests_registry.js"></script>
  <script>
    async function startRunner() {
      const urlParams = new URLSearchParams(window.location.search);
      const testId = urlParams.get('test') || 'AL-PKG-A2-001';
      const engine = new SuiteTestEngine({ containerId: 'test-app-root', storagePrefix: 'alinvest_pkg_vojtech_test_' });

      try {
        let testData = null;
        if (window.TEST_REGISTRY && window.TEST_REGISTRY[testId]) {
          testData = window.TEST_REGISTRY[testId];
        } else {
          const resp = await fetch(`data/tests/${testId}.json`);
          if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
          testData = await resp.json();
        }
        engine.init(testData);
      } catch (err) {
        document.getElementById('test-app-root').innerHTML = `
          <div class="question-card" style="text-align: center; padding: 40px;">
            <h2 style="color: var(--primary); margin-bottom: 12px;">⚠️ Test Module Not Found</h2>
            <p style="color: var(--text-secondary); margin-bottom: 20px;">
              Could not load <strong>${testId}.json</strong>. Please ensure the test JSON file exists in <code>data/tests/</code>.
            </p>
            <div style="display:flex; justify-content:center; gap:12px;">
              <a href="test_runner.html?test=AL-PKG-A2-001" class="btn btn-primary" style="background:#0284c7;">Load A2 Pilot Test</a>
              <a href="index.html" class="btn btn-secondary">Return to Portal</a>
            </div>
          </div>
        `;
      }
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', startRunner);
    } else {
      startRunner();
    }
  </script>
</body>
</html>"""

def main():
    print("=" * 60)
    print("DEPLOYING STANDALONE ASSESSMENT SUITE FOR VOJTĚCH BERGER")
    print("=" * 60)

    # 1. Setup Directories
    tests_dir = SUITE_DIR / "data" / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)

    # 2. Generate 80 Core Modules
    print("\n1. Generating 80 Core Modules (A2, B1, B2, C1)...")
    core_modules = generate_alinvest_packaging_modules()
    print(f"   [OK] Generated {len(core_modules)} core packaging modules.")

    # 3. Add 4 Specialized Football Modules
    print("\n2. Loading 4 Specialized Football & World Sports Modules...")
    all_modules = dict(core_modules)
    for sp_mod in VOJTECH_SPECIALIZED_MODULES:
        all_modules[sp_mod["test_id"]] = sp_mod
    print(f"   [OK] Total modules to write: {len(all_modules)}")

    # 4. Write Individual Test JSONs
    print("\n3. Writing JSON files to data/tests/...")
    for tid, test_obj in all_modules.items():
        with open(tests_dir / f"{tid}.json", "w", encoding="utf-8") as f:
            json.dump(test_obj, f, indent=2, ensure_ascii=False)
    print(f"   [OK] Wrote {len(all_modules)} test files.")

    # 5. Build Curriculum Manifest (84 entries)
    print("\n4. Building curriculum manifest...")
    manifest_list = []
    # 80 core from curriculum_catalog
    for mod in get_alinvest_packaging_curriculum():
        manifest_list.append(mod)
    # 4 specialized
    for sp_mod in VOJTECH_SPECIALIZED_MODULES:
        manifest_list.append({
            "test_id": sp_mod["test_id"],
            "title": sp_mod["title"],
            "level": sp_mod["level"],
            "category": sp_mod["category"],
            "workplace_track": sp_mod["workplace_track"],
            "grammar_focus": sp_mod["grammar_focus"],
            "estimated_time_minutes": sp_mod["estimated_time_minutes"],
            "description": sp_mod["description"]
        })

    with open(SUITE_DIR / "data" / "curriculum_manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest_list, f, indent=2, ensure_ascii=False)

    with open(SUITE_DIR / "data" / "manifest.js", "w", encoding="utf-8") as f:
        f.write("window.CURRICULUM_MANIFEST = " + json.dumps(manifest_list, indent=2, ensure_ascii=False) + ";\n")

    with open(SUITE_DIR / "data" / "tests_registry.js", "w", encoding="utf-8") as f:
        f.write("window.TEST_REGISTRY = window.TEST_REGISTRY || {};\n")
        f.write("Object.assign(window.TEST_REGISTRY, " + json.dumps(all_modules, indent=2, ensure_ascii=False) + ");\n")
    print(f"   [OK] Manifests written: {len(manifest_list)} items registered.")

    # 6. Create Schema & Engine
    print("\n5. Setting up schema and engine...")
    create_schema(SUITE_DIR)
    create_engine(SUITE_DIR)
    print("   [OK] Schema and engine configured.")

    # 7. Create HTML Pages
    print("\n6. Creating index.html and test_runner.html...")
    with open(SUITE_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(generate_portal_html())
    with open(SUITE_DIR / "test_runner.html", "w", encoding="utf-8") as f:
        f.write(generate_test_runner_html())
    print("   [OK] Portals written.")

    # 8. Schema Validation & Repetition Check
    print("\n7. Validating all 84 modules against JSON schema and repetition audit...")
    schema_path = SUITE_DIR / "schema" / "test_schema.json"
    schema = json.load(open(schema_path, encoding="utf-8"))
    validator = jsonschema.Draft7Validator(schema)

    schema_errors = 0
    dup_errors = 0
    for tid, test_obj in all_modules.items():
        errs = list(validator.iter_errors(test_obj))
        if errs:
            schema_errors += 1
            print(f"   [FAIL] Schema error in {tid}: {errs[0].message}")
        
        prompts = [q["prompt"] for q in test_obj["questions"]]
        counts = Counter(prompts)
        if max(counts.values()) > 1:
            dup_errors += 1
            print(f"   [FAIL] Duplicate prompt in {tid}")

    if schema_errors == 0 and dup_errors == 0:
        print("   [PASS] ALL 84 MODULES VALIDATED WITH 0 SCHEMA ERRORS AND 0 DUPLICATE PROMPTS!")
    else:
        print(f"   [WARN] {schema_errors} schema errors, {dup_errors} duplicate errors.")

    print("\n" + "=" * 60)
    print("AL INVEST SUITE DEPLOYMENT COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
