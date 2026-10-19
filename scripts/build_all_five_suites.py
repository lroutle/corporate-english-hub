#!/usr/bin/env python3
"""
Master Builder for 5 Independent English Testing Suites:
1. Tatra Engineering (tatra-engineering)
2. Tatra Sales and Engineering (tatra-sales-engineering)
3. Teva Engineering (teva-engineering)
4. Tapi Chemistry (tapi-chemistry)
5. Teva IT (teva-it)

Includes the new lower CEFR Tier (A2 - Pre-Intermediate Foundation) for learners who struggle with B1.
All test answer keys are strictly balanced across A, B, C, D (no position bias).
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Suite Configurations
SUITES = {
    "tatra-engineering": {
        "name": "Tatra Engineering",
        "company": "TATRA TRUCKS a.s.",
        "division": "Vehicle R&D, Chassis & Heavy Manufacturing",
        "id_prefix": "TTR-ENG",
        "color_primary": "#c51230",
        "color_dark": "#1e293b",
        "color_accent": "#ef4444",
        "badge_icon": "🚛⚙️",
        "brand_text": "TATRA ENG",
        "storage_prefix": "tatra_eng",
        "prompt_context": "automotive manufacturing engineers, suspension designers, and chassis assembly technicians at Tatra Trucks (Kopřivnice)"
    },
    "tatra-sales-engineering": {
        "name": "Tatra Sales and Engineering",
        "company": "TATRA TRUCKS a.s.",
        "division": "International Defense, Commercial Sales & Tender Engineering",
        "id_prefix": "TTR-SALES",
        "color_primary": "#990011",
        "color_dark": "#0f172a",
        "color_accent": "#d97706",
        "badge_icon": "🚛🤝",
        "brand_text": "TATRA SALES",
        "storage_prefix": "tatra_sales",
        "prompt_context": "technical sales representatives, international defense tender negotiators, and export logistics managers at Tatra Trucks"
    },
    "teva-engineering": {
        "name": "Teva Engineering",
        "company": "TEVA PHARMACEUTICALS",
        "division": "Pharmaceutical Facilities, Automation & Validation Engineering",
        "id_prefix": "TEV-ENG",
        "color_primary": "#0050aa",
        "color_dark": "#003876",
        "color_accent": "#00a3e0",
        "badge_icon": "💊⚙️",
        "brand_text": "TEVA ENG",
        "storage_prefix": "teva_eng",
        "prompt_context": "pharmaceutical process engineers, cleanroom HVAC specialists, SCADA automation engineers, and Computerized System Validation (CSV) leads at Teva Pharmaceuticals"
    },
    "tapi-chemistry": {
        "name": "Tapi Chemistry",
        "company": "TAPI (Teva Active Pharmaceutical Ingredients)",
        "division": "Chemical Synthesis, Analytical QC & API Batch Manufacturing",
        "id_prefix": "TAPI-CHEM",
        "color_primary": "#059669",
        "color_dark": "#064e3b",
        "color_accent": "#10b981",
        "badge_icon": "🧪⚗️",
        "brand_text": "TAPI CHEM",
        "storage_prefix": "tapi_chem",
        "prompt_context": "organic synthesis chemists, analytical QC scientists, reaction scale-up engineers, and API batch operators at TAPI"
    },
    "teva-it": {
        "name": "Teva IT",
        "company": "TEVA PHARMACEUTICALS",
        "division": "Global IT Infrastructure, Software Engineering & Cybersecurity",
        "id_prefix": "TEV-IT",
        "color_primary": "#4338ca",
        "color_dark": "#1e1b4b",
        "color_accent": "#0284c7",
        "badge_icon": "💻☁️",
        "brand_text": "TEVA IT",
        "storage_prefix": "teva_it",
        "prompt_context": "cloud architects, DevOps specialists, software engineers, and cybersecurity incident responders at Teva Global IT"
    }
}

def generate_schema(suite_key, conf):
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": f"{conf['name']} Test Schema",
        "type": "object",
        "required": [
            "test_id", "title", "level", "category", "workplace_track",
            "estimated_time_minutes", "description", "questions"
        ],
        "properties": {
            "test_id": {
                "type": "string",
                "pattern": f"^{conf['id_prefix']}-(A2|B1|B2|C2|SP)-\\d{{3}}$"
            },
            "title": { "type": "string", "minLength": 5 },
            "level": { "type": "string", "enum": ["A2", "B1", "B2", "C2", "B1/B2"] },
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
                        "explanations": {
                            "type": "object",
                            "required": ["correct"],
                            "additionalProperties": { "type": "string" }
                        },
                        "cz_learning_point": { "type": "string", "minLength": 10 },
                        "workplace_track": { "type": "string" }
                    }
                }
            }
        }
    }

def generate_css(conf):
    return f"""/* {conf['name']} Custom Industrial Design System */
:root {{
  --primary: {conf['color_primary']};
  --primary-dark: {conf['color_dark']};
  --primary-accent: {conf['color_accent']};
  --navy-dark: #0f172a;
  --navy-slate: #1e293b;
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #64748b;
  --bg-main: #f8fafc;
  --bg-card: #ffffff;
  --border-subtle: #e2e8f0;
  --border-strong: #cbd5e1;
  --success-bg: #ecfdf5;
  --success-border: #10b981;
  --success-text: #065f46;
  --danger-bg: #fef2f2;
  --danger-border: #ef4444;
  --danger-text: #991b1b;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: var(--font-sans); background: var(--bg-main); color: var(--text-primary); line-height: 1.6; min-height: 100vh; display: flex; flex-direction: column; }}

.suite-header {{ background: linear-gradient(135deg, var(--navy-dark) 0%, var(--primary-dark) 60%, var(--primary) 100%); color: #fff; border-bottom: 4px solid var(--primary-accent); padding: 16px 24px; box-shadow: var(--shadow-md); position: sticky; top: 0; z-index: 50; }}
.header-container {{ max-width: 1100px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }}
.brand-wrapper {{ display: flex; align-items: center; gap: 14px; text-decoration: none; color: inherit; }}
.brand-logo-badge {{ background: linear-gradient(135deg, var(--primary), var(--primary-accent)); color: #fff; font-weight: 900; font-size: 1.1rem; letter-spacing: 1px; padding: 6px 14px; border-radius: var(--radius-sm); }}
.brand-titles h1 {{ font-size: 1.15rem; font-weight: 700; }}
.brand-titles p {{ font-size: 0.8rem; color: #94a3b8; }}

.main-layout {{ max-width: 1100px; margin: 28px auto; padding: 0 20px; flex: 1; width: 100%; }}
.nav-breadcrumbs {{ display: flex; align-items: center; gap: 8px; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 20px; }}
.nav-breadcrumbs a {{ color: var(--primary); text-decoration: none; font-weight: 600; }}

.test-meta-card {{ background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 24px 28px; margin-bottom: 24px; box-shadow: var(--shadow-sm); position: relative; overflow: hidden; }}
.test-meta-card::before {{ content: ""; position: absolute; top: 0; left: 0; bottom: 0; width: 6px; background-color: var(--primary); }}
.test-badge-row {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; align-items: center; }}
.badge {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase; padding: 4px 10px; border-radius: 9999px; display: inline-flex; }}
.badge-level-a2 {{ background: #fef08a; color: #854d0e; }}
.badge-level-b1 {{ background: #dbeafe; color: #1e40af; }}
.badge-level-b2 {{ background: #e0e7ff; color: #3730a3; }}
.badge-level-c2 {{ background: #fae8ff; color: #86198f; border: 1px solid #f0abfc; }}
.badge-specialized {{ background: #fef3c7; color: #92400e; }}
.badge-track {{ background: #f1f5f9; color: #334155; border: 1px solid var(--border-subtle); }}

.test-title {{ font-size: 1.5rem; font-weight: 800; color: var(--navy-dark); line-height: 1.3; margin-bottom: 8px; }}
.test-description {{ color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 16px; }}
.test-meta-stats {{ display: flex; flex-wrap: wrap; gap: 20px; padding-top: 14px; border-top: 1px solid var(--border-subtle); font-size: 0.85rem; color: var(--text-muted); }}

.toolbar-card {{ background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 14px 20px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; }}
.view-toggle-group {{ display: flex; background: #f1f5f9; padding: 3px; border-radius: var(--radius-sm); }}
.view-btn {{ background: none; border: none; padding: 6px 14px; font-size: 0.82rem; font-weight: 600; color: var(--text-muted); cursor: pointer; border-radius: 4px; }}
.view-btn.active {{ background: #fff; color: var(--primary); box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}

.progress-summary-box {{ display: flex; align-items: center; gap: 14px; flex: 1; max-width: 400px; margin: 0 16px; }}
.progress-bar-outer {{ flex: 1; height: 10px; background-color: #e2e8f0; border-radius: 9999px; overflow: hidden; }}
.progress-bar-fill {{ height: 100%; background: linear-gradient(90deg, var(--primary), var(--primary-accent)); width: 0%; transition: width 0.3s; }}
.progress-text {{ font-size: 0.82rem; font-weight: 600; color: #334155; white-space: nowrap; }}

.btn {{ display: inline-flex; align-items: center; gap: 6px; font-family: inherit; font-size: 0.85rem; font-weight: 600; padding: 8px 16px; border-radius: var(--radius-sm); border: 1px solid transparent; cursor: pointer; transition: all 0.2s; text-decoration: none; }}
.btn-primary {{ background-color: var(--primary); color: #fff; }}
.btn-primary:hover {{ opacity: 0.9; }}
.btn-secondary {{ background: #fff; border-color: var(--border-strong); color: #334155; }}
.btn-export {{ background: #0284c7; color: #fff; }}
.btn-reset {{ color: #dc2626; border-color: #fecaca; background: #fff; }}

.question-nav-strip {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }}
.nav-dot {{ width: 38px; height: 38px; border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: center; font-size: 0.85rem; font-weight: 700; background: #fff; border: 1px solid var(--border-subtle); color: var(--text-secondary); cursor: pointer; }}
.nav-dot.current {{ border-color: var(--primary); outline: 2px solid var(--primary); font-weight: 900; }}
.nav-dot.answered-correct {{ background: #10b981; color: #fff; border-color: #10b981; }}
.nav-dot.answered-wrong {{ background: #ef4444; color: #fff; border-color: #ef4444; }}

.question-card {{ background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 28px; margin-bottom: 24px; box-shadow: var(--shadow-sm); }}
.question-card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; font-size: 0.8rem; color: var(--text-muted); border-bottom: 1px solid var(--border-subtle); padding-bottom: 10px; }}
.question-track-tag {{ background: #f1f5f9; padding: 2px 8px; border-radius: 4px; font-weight: 600; color: var(--navy-slate); }}
.question-prompt {{ font-size: 1.15rem; font-weight: 600; color: var(--navy-dark); line-height: 1.5; margin-bottom: 22px; }}
.blank-slot {{ display: inline-block; min-width: 80px; border-bottom: 2px solid var(--primary); padding: 0 4px; color: var(--primary); font-weight: 700; }}

.options-list {{ display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px; }}
.option-btn {{ display: flex; align-items: flex-start; gap: 14px; width: 100%; text-align: left; background: #fff; border: 2px solid var(--border-subtle); border-radius: var(--radius-md); padding: 14px 18px; font-family: inherit; font-size: 1rem; color: var(--navy-dark); cursor: pointer; transition: all 0.2s; }}
.option-btn:hover:not(:disabled) {{ border-color: var(--primary-accent); background: #f8fafc; }}
.option-letter {{ display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: #f1f5f9; color: #334155; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; }}
.option-text {{ flex: 1; padding-top: 2px; }}

.option-btn.selected-correct {{ background-color: var(--success-bg) !important; border-color: var(--success-border) !important; color: var(--success-text) !important; }}
.option-btn.selected-correct .option-letter {{ background: var(--success-border); color: #fff; }}
.option-btn.selected-wrong {{ background-color: var(--danger-bg) !important; border-color: var(--danger-border) !important; color: var(--danger-text) !important; }}
.option-btn.selected-wrong .option-letter {{ background: var(--danger-border); color: #fff; }}
.option-btn.is-revealed-correct {{ background-color: #f0fdf4 !important; border-color: #86efac !important; border-style: dashed !important; }}

.guidance-box {{ margin-top: 20px; border-radius: var(--radius-md); padding: 20px 22px; animation: fadeIn 0.3s ease-in-out; }}
@keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}
.guidance-wrong {{ background: #fff1f2; border: 1px solid #fecdd3; border-left: 5px solid #e11d48; }}
.guidance-correct {{ background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #16a34a; }}
.guidance-header {{ display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 1.05rem; margin-bottom: 14px; }}
.guidance-wrong .guidance-header {{ color: #9f1239; }}
.guidance-correct .guidance-header {{ color: #166534; }}
.guidance-section {{ margin-bottom: 12px; font-size: 0.92rem; line-height: 1.55; }}
.guidance-section strong {{ display: inline-block; font-weight: 700; margin-right: 6px; }}
.cz-note-card {{ background: #fffbeb; border: 1px solid #fef3c7; border-radius: var(--radius-sm); padding: 10px 14px; margin-top: 10px; color: #92400e; font-size: 0.88rem; display: flex; gap: 10px; align-items: flex-start; }}
.corp-example-card {{ background: #f8fafc; border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); padding: 10px 14px; margin-top: 8px; color: var(--navy-slate); font-size: 0.88rem; }}

.step-nav-footer {{ display: flex; justify-content: space-between; align-items: center; margin-top: 24px; padding-top: 18px; border-top: 1px solid var(--border-subtle); }}

.results-modal-backdrop {{ position: fixed; inset: 0; background-color: rgba(15, 23, 42, 0.65); backdrop-filter: blur(4px); display: flex; align-items: center; justify-content: center; padding: 20px; z-index: 100; }}
.results-modal-content {{ background: #ffffff; border-radius: var(--radius-lg); max-width: 650px; width: 100%; max-height: 90vh; overflow-y: auto; box-shadow: var(--shadow-lg); padding: 32px; position: relative; }}
.results-score-circle {{ width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, var(--navy-dark), var(--primary)); color: #ffffff; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0 auto 16px auto; }}
.results-score-circle .score-num {{ font-size: 2.2rem; font-weight: 800; line-height: 1; }}
.results-score-circle .score-label {{ font-size: 0.72rem; color: #cbd5e1; text-transform: uppercase; }}
.results-breakdown {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 24px; }}
.results-stat-box {{ background: #f8fafc; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 12px; text-align: center; }}
.modal-actions {{ display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }}

.toast-notice {{ position: fixed; bottom: 24px; right: 24px; background: var(--navy-dark); color: #fff; padding: 12px 20px; border-radius: var(--radius-md); font-size: 0.9rem; z-index: 120; }}
.suite-footer {{ background: #fff; border-top: 1px solid var(--border-subtle); padding: 24px 20px; text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: 40px; }}
"""

def generate_app_js(suite_key, conf):
    return f"""/**
 * {conf['name']} Interactive English Testing Engine
 * Self-contained vanilla JS testing engine for {conf['company']} ({conf['division']}).
 */

class SuiteTestEngine {{
  constructor(options = {{}}) {{
    this.containerId = options.containerId || 'test-app-root';
    this.storagePrefix = '{conf['storage_prefix']}_test_';
    this.testData = null;
    this.userAnswers = {{}};
    this.firstTryAnswers = {{}};
    this.currentQuestionIndex = 0;
    this.viewMode = 'step';
  }}

  init(testData) {{
    this.testData = testData;
    this.userAnswers = {{}};
    this.firstTryAnswers = {{}};
    this.currentQuestionIndex = 0;
    window.currentSuiteEngine = this;
    this.loadSavedState();
    this.render();
  }}

  loadSavedState() {{
    if (!this.testData || !this.testData.test_id) return;
    try {{
      const saved = localStorage.getItem(`${{this.storagePrefix}}${{this.testData.test_id}}`);
      if (saved) {{
        const parsed = JSON.parse(saved);
        if (parsed.userAnswers) this.userAnswers = parsed.userAnswers;
        if (parsed.firstTryAnswers) this.firstTryAnswers = parsed.firstTryAnswers;
      }}
    }} catch (e) {{}}
  }}

  saveState() {{
    if (!this.testData || !this.testData.test_id) return;
    try {{
      localStorage.setItem(`${{this.storagePrefix}}${{this.testData.test_id}}`, JSON.stringify({{
        userAnswers: this.userAnswers,
        firstTryAnswers: this.firstTryAnswers,
        updatedAt: new Date().toISOString()
      }}));
    }} catch (e) {{}}
  }}

  resetTest() {{
    if (confirm('Reset all answers for this test module?')) {{
      this.userAnswers = {{}};
      this.firstTryAnswers = {{}};
      this.currentQuestionIndex = 0;
      if (this.testData && this.testData.test_id) {{
        localStorage.removeItem(`${{this.storagePrefix}}${{this.testData.test_id}}`);
      }}
      this.render();
      this.showToast('Test progress has been reset.');
    }}
  }}

  setViewMode(mode) {{
    if (this.viewMode === mode) return;
    this.viewMode = mode;
    this.render();
  }}

  handleAnswerSelect(questionIndex, selectedKey) {{
    const question = this.testData.questions[questionIndex];
    const qid = question.id;
    const isCorrect = (selectedKey === question.correct_key);

    if (this.firstTryAnswers[qid] === undefined) {{
      this.firstTryAnswers[qid] = isCorrect;
    }}

    const prevAttempts = (this.userAnswers[qid] && this.userAnswers[qid].attemptCount) || 0;
    this.userAnswers[qid] = {{
      selectedKey: selectedKey,
      isCorrect: isCorrect,
      attemptCount: prevAttempts + 1
    }};

    this.saveState();
    this.render();

    if (this.isTestCompleted()) {{
      const totalQ = this.testData.questions.length;
      const answeredCount = Object.keys(this.userAnswers).length;
      if (answeredCount === totalQ && questionIndex === totalQ - 1) {{
        setTimeout(() => this.openResultsModal(), 600);
      }}
    }}
  }}

  isTestCompleted() {{
    if (!this.testData || !this.testData.questions) return false;
    return Object.keys(this.userAnswers).length === this.testData.questions.length;
  }}

  calculateScore() {{
    if (!this.testData || !this.testData.questions) return {{ score: 0, total: 0, percent: 0 }};
    const total = this.testData.questions.length;
    let correctCount = 0;
    this.testData.questions.forEach(q => {{
      if (this.firstTryAnswers[q.id] === true) correctCount += 1;
    }});
    const percent = total > 0 ? Math.round((correctCount / total) * 100) : 0;
    return {{ score: correctCount, total, percent }};
  }}

  getMissedQuestions() {{
    if (!this.testData || !this.testData.questions) return [];
    return this.testData.questions.filter(q => {{
      const state = this.userAnswers[q.id];
      return state && !this.firstTryAnswers[q.id];
    }});
  }}

  render() {{
    const root = document.getElementById(this.containerId);
    if (!root) return;
    if (!this.testData) {{
      root.innerHTML = `<div class="question-card"><p>Loading test module...</p></div>`;
      return;
    }}

    const {{ score, total, percent }} = this.calculateScore();
    const answeredCount = Object.keys(this.userAnswers).length;

    let html = `
      <nav class="nav-breadcrumbs">
        <a href="index.html">← ${{this.escapeHtml('{conf['name']}')}} Portal</a>
        <span>/</span>
        <span>${{this.escapeHtml(this.testData.level)}}</span>
        <span>/</span>
        <span>${{this.escapeHtml(this.testData.test_id)}}</span>
      </nav>

      <header class="test-meta-card">
        <div class="test-badge-row">
          <span class="badge badge-level-${{this.testData.level.toLowerCase().replace('/', '-')}}">${{this.escapeHtml(this.testData.level)}}</span>
          <span class="badge badge-track">${{this.escapeHtml(this.testData.workplace_track)}}</span>
          <span class="badge badge-specialized">${{this.escapeHtml(this.testData.category.toUpperCase())}}</span>
        </div>
        <h1 class="test-title">${{this.escapeHtml(this.testData.title)}}</h1>
        <p class="test-description">${{this.escapeHtml(this.testData.description)}}</p>
        <div class="test-meta-stats">
          <div>⏱ <strong>${{this.testData.estimated_time_minutes || 15}} min</strong></div>
          <div>📋 <strong>${{this.testData.questions.length}} Questions</strong></div>
          <div>🎯 Score: <strong>${{score}}/${{total}} (${{percent}}%)</strong></div>
        </div>
      </header>

      <div class="toolbar-card">
        <div class="view-toggle-group">
          <button class="view-btn ${{this.viewMode === 'step' ? 'active' : ''}}" id="btn-view-step">Step-by-Step</button>
          <button class="view-btn ${{this.viewMode === 'list' ? 'active' : ''}}" id="btn-view-list">List View</button>
        </div>

        <div class="progress-summary-box">
          <div class="progress-bar-outer">
            <div class="progress-bar-fill" style="width: ${{(answeredCount / total) * 100}}%"></div>
          </div>
          <span class="progress-text">${{answeredCount}} / ${{total}} answered</span>
        </div>

        <div>
          <button class="btn btn-secondary" id="btn-open-results">📊 Results</button>
          <button class="btn btn-export" id="btn-export-notebooklm">📓 NotebookLM Export</button>
          <button class="btn btn-reset" id="btn-reset-test">↺ Reset</button>
        </div>
      </div>

      <nav class="question-nav-strip">
        ${{this.testData.questions.map((q, idx) => {{
          const ans = this.userAnswers[q.id];
          let statusClass = '';
          if (ans) {{
            statusClass = this.firstTryAnswers[q.id] ? 'answered-correct' : 'answered-wrong';
          }}
          if (this.viewMode === 'step' && idx === this.currentQuestionIndex) {{
            statusClass += ' current';
          }}
          return `<button class="nav-dot ${{statusClass}}" data-q-idx="${{idx}}">${{idx + 1}}</button>`;
        }}).join('')}}
      </nav>

      <main class="test-content-area">
        ${{this.viewMode === 'step' 
          ? this.renderSingleQuestion(this.currentQuestionIndex) 
          : this.testData.questions.map((_, idx) => this.renderSingleQuestion(idx)).join('')}}
      </main>
    `;

    root.innerHTML = html;
    this.attachEventListeners();
  }}

  renderSingleQuestion(index) {{
    const q = this.testData.questions[index];
    if (!q) return '';

    const ansState = this.userAnswers[q.id];
    const isAnswered = Boolean(ansState);
    const selectedKey = ansState ? ansState.selectedKey : null;
    const isCorrect = ansState ? ansState.isCorrect : false;

    const formattedPrompt = this.escapeHtml(q.prompt).replace(/_{{3,}}/g, '<span class="blank-slot">_______</span>');

    let optionsHtml = q.options.map(opt => {{
      let optClass = 'option-btn';
      let statusIndicator = '';

      if (isAnswered) {{
        if (opt.key === selectedKey) {{
          optClass += isCorrect ? ' selected-correct' : ' selected-wrong';
          statusIndicator = isCorrect ? ' ✓' : ' ✕';
        }} else if (!isCorrect && opt.key === q.correct_key) {{
          optClass += ' is-revealed-correct';
          statusIndicator = ' (Correct)';
        }}
      }}

      return `
        <button class="${{optClass}}" data-q-idx="${{index}}" data-opt-key="${{opt.key}}">
          <span class="option-letter">${{opt.key}}</span>
          <span class="option-text">${{this.escapeHtml(opt.text)}}${{statusIndicator}}</span>
        </button>
      `;
    }}).join('');

    let guidanceHtml = '';
    if (isAnswered) {{
      if (isCorrect) {{
        guidanceHtml = `
          <div class="guidance-box guidance-correct">
            <div class="guidance-header">✓ Correct Answer! (Option ${{q.correct_key}})</div>
            <div class="guidance-section"><strong>Technical Rationale:</strong> ${{this.escapeHtml(q.explanations.correct)}}</div>
            <div class="cz-note-card">
              <span>💡</span>
              <div><strong>Czech Contrastive Insight:</strong> ${{this.escapeHtml(q.cz_learning_point)}}</div>
            </div>
          </div>
        `;
      }} else {{
        const wrongExp = q.explanations[`wrong_${{selectedKey}}`] || 'This choice does not fit the required grammar aspect or register.';
        guidanceHtml = `
          <div class="guidance-box guidance-wrong">
            <div class="guidance-header">✕ Incorrect Selection (Option ${{selectedKey}})</div>
            <div class="guidance-section"><strong>Why Option ${{selectedKey}} is wrong:</strong> ${{this.escapeHtml(wrongExp)}}</div>
            <div class="guidance-section"><strong>Correct Solution (${{q.correct_key}}):</strong> ${{this.escapeHtml(q.explanations.correct)}}</div>
            <div class="cz-note-card">
              <span>⚠️</span>
              <div><strong>Czech Interference / Contrastive Note:</strong> ${{this.escapeHtml(q.cz_learning_point)}}</div>
            </div>
            <div class="corp-example-card">
              <strong>Workplace Application:</strong> Crucial for accurate reporting in ${{this.escapeHtml(q.workplace_track)}}.
            </div>
          </div>
        `;
      }}
    }}

    let stepNavHtml = '';
    if (this.viewMode === 'step') {{
      const isFirst = index === 0;
      const isLast = index === this.testData.questions.length - 1;
      stepNavHtml = `
        <footer class="step-nav-footer">
          <button class="btn btn-secondary" id="btn-prev-q" ${{isFirst ? 'disabled style="opacity:0.5;cursor:not-allowed;"' : ''}}>← Previous</button>
          <span>Question ${{index + 1}} of ${{this.testData.questions.length}}</span>
          ${{isLast ? '<button class="btn btn-primary" id="btn-finish-test">Complete Test →</button>' : '<button class="btn btn-primary" id="btn-next-q">Next →</button>'}}
        </footer>
      `;
    }}

    return `
      <article class="question-card" id="q-card-${{index}}">
        <header class="question-card-header">
          <span>Question ${{index + 1}} of ${{this.testData.questions.length}} (${{q.id}})</span>
          <span class="question-track-tag">${{this.escapeHtml(q.workplace_track)}}</span>
        </header>
        <div class="question-prompt">${{formattedPrompt}}</div>
        <div class="options-list">${{optionsHtml}}</div>
        ${{guidanceHtml}}
        ${{stepNavHtml}}
      </article>
    `;
  }}

  attachEventListeners() {{
    const btnStep = document.getElementById('btn-view-step');
    if (btnStep) btnStep.onclick = () => this.setViewMode('step');
    const btnList = document.getElementById('btn-view-list');
    if (btnList) btnList.onclick = () => this.setViewMode('list');
    const btnReset = document.getElementById('btn-reset-test');
    if (btnReset) btnReset.onclick = () => this.resetTest();
    const btnResults = document.getElementById('btn-open-results');
    if (btnResults) btnResults.onclick = () => this.openResultsModal();
    const btnExport = document.getElementById('btn-export-notebooklm');
    if (btnExport) btnExport.onclick = () => this.exportNotebookLM();

    document.querySelectorAll('.nav-dot').forEach(btn => {{
      btn.onclick = (e) => this.goToQuestion(parseInt(e.currentTarget.getAttribute('data-q-idx'), 10));
    }});

    document.querySelectorAll('.option-btn').forEach(btn => {{
      btn.onclick = (e) => {{
        const qIdx = parseInt(e.currentTarget.getAttribute('data-q-idx'), 10);
        const optKey = e.currentTarget.getAttribute('data-opt-key');
        this.handleAnswerSelect(qIdx, optKey);
      }};
    }});

    const btnPrev = document.getElementById('btn-prev-q');
    if (btnPrev) btnPrev.onclick = () => {{ if (this.currentQuestionIndex > 0) {{ this.currentQuestionIndex--; this.render(); window.scrollTo({{ top: 120, behavior: 'smooth' }}); }} }};
    const btnNext = document.getElementById('btn-next-q');
    if (btnNext) btnNext.onclick = () => {{ if (this.currentQuestionIndex < this.testData.questions.length - 1) {{ this.currentQuestionIndex++; this.render(); window.scrollTo({{ top: 120, behavior: 'smooth' }}); }} }};
    const btnFinish = document.getElementById('btn-finish-test');
    if (btnFinish) btnFinish.onclick = () => this.openResultsModal();
  }}

  goToQuestion(idx) {{
    if (idx < 0 || idx >= this.testData.questions.length) return;
    this.currentQuestionIndex = idx;
    if (this.viewMode === 'step') {{
      this.render();
      window.scrollTo({{ top: 120, behavior: 'smooth' }});
    }} else {{
      const card = document.getElementById(`q-card-${{idx}}`);
      if (card) card.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
  }}

  openResultsModal() {{
    const {{ score, total, percent }} = this.calculateScore();
    const missed = this.getMissedQuestions();

    let rating = 'Need More Practice';
    let ratingColor = '#ef4444';
    if (percent >= 90) {{ rating = 'Mastery / Certified'; ratingColor = '#10b981'; }}
    else if (percent >= 75) {{ rating = 'Strong Proficiency'; ratingColor = '{conf['color_primary']}'; }}
    else if (percent >= 60) {{ rating = 'Satisfactory Baseline'; ratingColor = '#f59e0b'; }}

    const modalHtml = `
      <div class="results-modal-backdrop" id="results-modal">
        <div class="results-modal-content">
          <div style="text-align: center; margin-bottom: 24px;">
            <div class="results-score-circle">
              <span class="score-num">${{percent}}%</span>
              <span class="score-label">First-Try</span>
            </div>
            <h2 style="color: ${{ratingColor}}; margin-bottom: 6px;">${{rating}}</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">
              Module: <strong>${{this.escapeHtml(this.testData.title)}}</strong> (${{this.escapeHtml(this.testData.test_id)}})
            </p>
          </div>

          <div class="results-breakdown">
            <div class="results-stat-box"><div style="font-size:1.3rem; font-weight:700; color:#10b981;">${{score}}</div><div>Correct First-Try</div></div>
            <div class="results-stat-box"><div style="font-size:1.3rem; font-weight:700; color:#ef4444;">${{total - score}}</div><div>Review Needed</div></div>
            <div class="results-stat-box"><div style="font-size:1.3rem; font-weight:700;">${{total}}</div><div>Total Items</div></div>
          </div>

          ${{missed.length > 0 ? `
            <div style="background:#fff1f2; border:1px solid #fecdd3; border-radius:var(--radius-md); padding:16px; margin-bottom:20px;">
              <h3 style="color:#9f1239; font-size:0.95rem; margin-bottom:8px;">Recommended Focus Areas:</h3>
              <ul style="padding-left:20px; font-size:0.88rem; color:#4c0519;">
                ${{missed.map(m => `<li><strong>${{m.id}}:</strong> ${{this.escapeHtml(m.cz_learning_point)}}</li>`).join('')}}
              </ul>
            </div>
          ` : '<div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:var(--radius-md); padding:16px; margin-bottom:20px; text-align:center; color:#065f46;">🎉 Outstanding! 100% first-try accuracy.</div>'}}

          <div class="modal-actions">
            <button class="btn btn-export" id="modal-btn-export">📓 Generate NotebookLM Study Guide</button>
            <button class="btn btn-secondary" id="modal-btn-close">Close</button>
          </div>
        </div>
      </div>
    `;

    const existing = document.getElementById('results-modal');
    if (existing) existing.remove();
    document.body.insertAdjacentHTML('beforeend', modalHtml);

    document.getElementById('modal-btn-close').onclick = () => document.getElementById('results-modal').remove();
    document.getElementById('modal-btn-export').onclick = () => this.exportNotebookLM();
  }}

  generateNotebookLMMarkdown() {{
    const {{ score, total, percent }} = this.calculateScore();
    const missed = this.getMissedQuestions();
    const dateStr = new Date().toLocaleDateString('en-US', {{ year: 'numeric', month: 'long', day: 'numeric' }});

    let md = `# ${{this.testData.title}} - Study Digest\\n`;
    md += `**Program:** {conf['name']} ({conf['company']}) | **Module:** ${{this.testData.test_id}} | **Level:** ${{this.testData.level}} | **Date:** ${{dateStr}}\\n`;
    md += `**Track:** ${{this.testData.workplace_track}} | **First-Try Score:** ${{score}}/${{total}} (${{percent}}%)\\n\\n---\\n\\n`;

    md += `## Executive Diagnostic Summary\\n`;
    md += `This customized study digest is generated for {conf['prompt_context']}.\\n`;
    md += `It isolates contrastive grammar interference (Czenglish) and specific technical vocabulary gaps recorded during the assessment.\\n\\n`;

    if (missed.length > 0) {{
      md += `### Items Requiring Reinforcement (${{missed.length}} items):\\n\\n`;
      missed.forEach((q, idx) => {{
        const userState = this.userAnswers[q.id];
        const chosenKey = userState ? userState.selectedKey : 'None';
        const chosenOpt = q.options.find(o => o.key === chosenKey);
        const correctOpt = q.options.find(o => o.key === q.correct_key);

        md += `#### ${{idx + 1}}. ${{q.id}} (${{q.workplace_track}})\\n`;
        md += `* **Prompt:** "${{q.prompt}}"\\n`;
        md += `* **Selected Choice:** [${{chosenKey}}] "${{chosenOpt ? chosenOpt.text : 'N/A'}}" *(Incorrect)*\\n`;
        md += `* **Correct Option:** [${{q.correct_key}}] "${{correctOpt ? correctOpt.text : ''}}"\\n`;
        md += `* **Why the chosen option is wrong:** ${{q.explanations['wrong_' + chosenKey] || 'Grammatical mismatch.'}}\\n`;
        md += `* **Correct Rationale:** ${{q.explanations.correct}}\\n`;
        md += `* **Czech Contrastive Linguistic Note:** ${{q.cz_learning_point}}\\n\\n`;
      }});
    }}

    md += `## Complete Question Bank\\n\\n`;
    this.testData.questions.forEach((q, idx) => {{
      md += `### ${{idx + 1}}. [${{q.id}}] ${{q.prompt}}\\n`;
      q.options.forEach(opt => {{
        const isCorrect = (opt.key === q.correct_key);
        md += `  * ${{opt.key}}) ${{opt.text}}${{isCorrect ? ' **[CORRECT]**' : ''}}\\n`;
      }});
      md += `\\n* **Explanation:** ${{q.explanations.correct}}\\n`;
      md += `* **Czech Note:** ${{q.cz_learning_point}}\\n\\n`;
    }});

    md += `---\\n\\n## Recommended NotebookLM Audio Overview Prompt\\n`;
    md += `> *"Act as two senior professional trainers debriefing Czech professionals from {conf['company']} on the module '${{this.testData.title}}'. Focus on the contrastive linguistic mistakes made by Czech native speakers, explain why these errors occur, and model how to express these concepts with precision in authentic workplace scenarios."*\\n`;

    return md;
  }}

  exportNotebookLM() {{
    const mdContent = this.generateNotebookLMMarkdown();
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(mdContent).then(() => this.showToast('Copied Study Digest to clipboard!')).catch(() => {{}});
    }}
    const blob = new Blob([mdContent], {{ type: 'text/markdown;charset=utf-8;' }});
    const url = URL.createObjectURL(blob);
    const downloadLink = document.createElement('a');
    downloadLink.href = url;
    downloadLink.download = `${{this.testData.test_id}}_Study_Digest.md`;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
    URL.revokeObjectURL(url);
    this.showToast('Downloaded Study Digest (.md) for NotebookLM!');
  }}

  showToast(msg) {{
    const existing = document.querySelector('.toast-notice');
    if (existing) existing.remove();
    const toast = document.createElement('div');
    toast.className = 'toast-notice';
    toast.innerHTML = `<span>📋</span> <span>${{this.escapeHtml(msg)}}</span>`;
    document.body.appendChild(toast);
    setTimeout(() => {{ if (toast && toast.parentNode) toast.remove(); }}, 3500);
  }}

  escapeHtml(str) {{
    if (typeof str !== 'string') return '';
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
  }}
}}

window.SuiteTestEngine = SuiteTestEngine;
"""

def generate_runner_html(suite_key, conf):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{conf['name']} | Interactive English Test Runner</title>
  <link rel="stylesheet" href="engine/styles.css">
</head>
<body>
  <header class="suite-header">
    <div class="header-container">
      <a href="index.html" class="brand-wrapper">
        <span class="brand-logo-badge">{conf['brand_text']}</span>
        <div class="brand-titles">
          <h1>{conf['name']} Testing Suite</h1>
          <p>{conf['company']} | {conf['division']}</p>
        </div>
      </a>
      <div>
        <a href="index.html" class="btn btn-secondary">← Suite Portal</a>
      </div>
    </div>
  </header>

  <div class="main-layout" id="test-app-root"></div>

  <footer class="suite-footer">
    <p><strong>{conf['company']}</strong> | {conf['name']} English Assessment Suite (Levels A2, B1, B2 & Specialized)</p>
    <p style="margin-top:6px; font-size:0.8rem; color:#94a3b8;">Standalone Testing Environment with Contrastive Czech-English Diagnostics</p>
  </footer>

  <script src="engine/app.js"></script>
  <script src="data/tests_registry.js"></script>
  <script>
    async function startRunner() {{
      const urlParams = new URLSearchParams(window.location.search);
      const testId = urlParams.get('test') || '{conf['id_prefix']}-A2-001';
      const engine = new SuiteTestEngine({{ containerId: 'test-app-root' }});

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
              <a href="test_runner.html?test=${conf['id_prefix']}-A2-001" class="btn btn-primary">Load A2 Pilot Test</a>
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

def generate_index_html(suite_key, conf):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{conf['name']} | Interactive English Assessment Hub</title>
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
    .hero-stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 14px; margin-top: 24px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.15); }}
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

    .modules-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 20px; margin-bottom: 40px; }}
    .module-card {{ background: #ffffff; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 22px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: var(--shadow-sm); transition: all 0.2s; }}
    .module-card:hover {{ border-color: var(--primary); box-shadow: var(--shadow-md); transform: translateY(-2px); }}
    .module-id {{ font-family: monospace; font-weight: 800; font-size: 0.82rem; color: var(--primary-dark); background: #f1f5f9; padding: 2px 6px; border-radius: 4px; }}
    .module-card h3 {{ font-size: 1.1rem; font-weight: 700; color: var(--navy-dark); margin: 8px 0; }}
    .module-card p {{ font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 12px; }}
    .module-grammar-tag {{ font-size: 0.76rem; color: #0284c7; background: #f0f9ff; border: 1px solid #bae6fd; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 14px; font-weight: 600; }}
    .card-footer {{ display: flex; justify-content: space-between; align-items: center; padding-top: 14px; border-top: 1px solid var(--border-subtle); }}

    .tier-a2-highlight {{ background: #fefce8; border: 1px solid #fef08a; padding: 12px 18px; border-radius: var(--radius-md); margin-bottom: 20px; font-size: 0.88rem; color: #854d0e; display: flex; gap: 12px; align-items: center; }}
  </style>
</head>
<body>
  <header class="suite-header">
    <div class="header-container">
      <div class="brand-wrapper">
        <span class="brand-logo-badge">{conf['brand_text']}</span>
        <div class="brand-titles">
          <h1>{conf['name']} Assessment Hub</h1>
          <p>{conf['company']} | {conf['division']}</p>
        </div>
      </div>
      <div>
        <a href="../index.html" class="btn btn-secondary">⊞ Master Corporate Hub</a>
      </div>
    </div>
  </header>

  <div class="main-layout">
    <section class="hero-banner">
      <h1>{conf['name']} English Assessment Suite</h1>
      <p>
        Tailored technical and workplace language modules for Czech professionals in {conf['division']}. Featuring the newly integrated <strong>A2 Pre-Intermediate Foundation Tier</strong>, instant Czech contrastive guidance, and Google NotebookLM export.
      </p>
      <div class="hero-stats-grid">
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-total-modules">0</div><div class="hero-stat-label">Total Modules</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-a2-modules">0</div><div class="hero-stat-label">A2 Foundation Tier</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-b1-b2-modules">0</div><div class="hero-stat-label">B1 & B2 Core</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-c2-modules">0</div><div class="hero-stat-label">C2 Mastery Tier</div></div>
        <div class="hero-stat-card"><div class="hero-stat-number" id="stat-user-completed">0</div><div class="hero-stat-label">Completed by You</div></div>
      </div>
    </section>

    <div class="tier-a2-highlight">
      <span style="font-size: 1.4rem;">💡</span>
      <div>
        <strong>New A2 Pre-Intermediate Foundation Tier:</strong> For learners finding B1 challenging, our A2 modules focus on clear tool identification, routine shift reports, simple past events, and basic workplace questions with minimal cognitive load.
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
        <button class="filter-chip" data-filter-type="level" data-filter-val="C2">Tier 3: C2 Mastery</button>
        <button class="filter-chip" data-filter-type="level" data-filter-val="specialized">Specialized Units</button>
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
    <p><strong>{conf['company']}</strong> | {conf['name']} | Standalone Modular Testing Architecture</p>
  </footer>

  <script src="data/manifest.js"></script>
  <script>
    let allModules = [];
    let currentLevelFilter = 'all';
    let currentTrackFilter = 'all';
    let searchQuery = '';
    const storagePrefix = '{conf['storage_prefix']}_test_';

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
      document.getElementById('stat-c2-modules').textContent = allModules.filter(m => m.level === 'C2').length;

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
        if (currentLevelFilter !== 'all') {{
          if (currentLevelFilter === 'specialized' && m.category !== 'specialized') return false;
          if (currentLevelFilter !== 'specialized' && m.level !== currentLevelFilter) return false;
        }}
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

def generate_validator_py(suite_key, conf):
    return f"""#!/usr/bin/env python3
\"\"\"
Validator for {conf['name']} test modules.
Verifies Draft-7 schema and checks for answer key distribution bias (no all-A).
\"\"\"

import sys
import json
from pathlib import Path
from collections import Counter

try:
    import jsonschema
except ImportError:
    jsonschema = None

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema" / "test_schema.json"
TESTS_DIR = Path(__file__).resolve().parent.parent / "data" / "tests"

def validate_file(p, schema):
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    errs = []
    if jsonschema:
        v = jsonschema.Draft7Validator(schema)
        for e in v.iter_errors(data):
            errs.append(f"Schema violation: {{e.message}}")
    
    questions = data.get("questions", [])
    if len(questions) < 8 or len(questions) > 12:
        errs.append(f"Expected 8-12 questions, got {{len(questions)}}")

    keys = []
    for q in questions:
        k = q.get("correct_key")
        keys.append(k)
        opt_keys = [o.get("key") for o in q.get("options", [])]
        if k not in opt_keys:
            errs.append(f"[{{q.get('id')}}] correct_key '{{k}}' not in options: {{opt_keys}}")
        for ok in opt_keys:
            if ok != k and f"wrong_{{ok}}" not in q.get("explanations", {{}}):
                errs.append(f"[{{q.get('id')}}] Missing explanation for distractor 'wrong_{{ok}}'")

    # Anti-bias check: no key represents > 50%
    counts = Counter(keys)
    if len(questions) >= 8 and max(counts.values()) > (len(questions) * 0.5):
        errs.append(f"Key distribution bias detected: {{dict(counts)}}")

    return errs

def main():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f)
    files = sorted(list(TESTS_DIR.glob("*.json"))) if TESTS_DIR.exists() else []
    print(f"Validating {{len(files)}} {conf['name']} test file(s)...")
    passed = 0
    for f in files:
        errs = validate_file(f, schema)
        if not errs:
            print(f"  [PASS] {{f.name}}")
            passed += 1
        else:
            print(f"  [FAIL] {{f.name}}: {{errs}}")
    print(f"Summary: {{passed}}/{{len(files)}} Passed.")
    if passed < len(files): sys.exit(1)

if __name__ == "__main__":
    main()
"""

print("Writing builder script...")
