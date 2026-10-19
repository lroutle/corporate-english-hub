# Tatra Trucks Interactive English Testing Suite (120 Modules)

Production-ready, data-driven, interactive English testing and diagnostic platform built specifically for **TATRA TRUCKS a.s.** (Kopřivnice, Czech Republic), serving engineers, assembly line leaders, international defense and commercial tender negotiators, and procurement specialists.

---

## 🎯 Target Audience & Pedagogical Framework

- **Target Audience:** Czech adult automotive professionals (powertrain/chassis R&D, assembly quality inspection, global fleet sales, defense contracts, procurement).
- **Proficiency Levels:** **CEFR B1 (Intermediate)** and **CEFR B2 (Upper-Intermediate)**.
- **Pedagogical Core: Czech Contrastive Linguistics ("Czenglish" Elimination):**
  - **Tense vs. Aspect:** Correcting the pervasive Czech habit of using Present Simple with *since/for* (*"I work here since 2018"* $\rightarrow$ *"I have worked here since 2018"*).
  - **Sequence of Past Events:** Enforcing Past Perfect in incident reports (*"noticed the pressure hadn't been calibrated"* instead of simple past).
  - **Engineering False Friends:** Dismantling false cognates like *control* (kontrolovat $\rightarrow$ check/inspect), *actual* (aktuální $\rightarrow$ current), *evidence* (evidence $\rightarrow$ records), and *fabricate* (vyrábět $\rightarrow$ manufacture).
  - **Tatra Heavy Vehicle Terminology:** Mastering proprietary concepts: central backbone tube (*centrální nosná roura*), swinging half-axles (*výkyvné polonápravy*), inter-wheel/inter-axle differential locks (*uzávěrky*), air bellows (*vzduchové vaky*), and CTIS (*centrální dofukování*).

---

## 🏗️ Architecture & Component Overview

```
c:\tmp\00-Mycat\
├── schema/
│   └── test_schema.json           # Formal JSON Schema enforcing question & explanation structure
├── engine/
│   ├── app.js                     # Vanilla JS test engine (step & list views, scoring, export)
│   └── styles.css                 # Industrial Tatra Trucks branded stylesheet (CSS variables)
├── data/
│   ├── curriculum_manifest.json   # Full registry of all 120 testing modules with metadata
│   └── tests/                     # Individual test modules adhering strictly to test_schema.json
│       ├── TTR-B1-001.json        # Chassis Assembly & Inspection (Past Simple vs Past Perfect)
│       ├── TTR-B1-002.json        # Spare Parts Dispatch (Present Perfect vs Past Simple)
│       ├── TTR-B1-003.json        # Shift Handover (Present Simple vs Continuous)
│       ├── TTR-B1-005.json        # Factory Safety Directives (Modals of Obligation)
│       ├── TTR-B1-018.json        # Incoterms & Contracts (Zero & First Conditionals)
│       ├── TTR-B2-001.json        # Chassis Stress Analysis (Mixed Conditionals)
│       ├── TTR-B2-002.json        # Defense Tender Negotiations (Modals of Deduction)
│       ├── TTR-B2-004.json        # High-Stakes Contract Bargaining (Inversion for Emphasis)
│       ├── TTR-SP-001.json        # False Friends in Automotive Manufacturing
│       ├── TTR-SP-004.json        # Tatra Backbone Tube & Chassis Nomenclature
│       └── TTR-SP-016.json        # Professional Negotiation Idioms
├── scripts/
│   ├── validate_tests.py          # Automated schema validator & pedagogical integrity checker
│   ├── build_curriculum_manifest.py # Rebuilds master curriculum catalog
│   └── generate_suite_modules.py  # Content generation script for test modules
├── index.html                     # Central Testing Suite Portal & Dashboard
├── test_runner.html               # Dedicated single-test runner (loads via URL ?test=ID)
└── CURRICULUM_ROADMAP.md          # Complete 120-module syllabus roadmap
```

---

## ⚡ Features of the Interactive Engine

1. **Dual Viewing Modes:**
   - **Step-by-Step Mode:** Focus on one question at a time with keyboard/click navigation and status indicator dots.
   - **List View Mode:** Complete overview of all questions in a single scrollable document.
2. **Dynamic Wrong Answer Guidance UI:**
   When an incorrect option is chosen, the engine dynamically renders:
   - **Why this choice is wrong:** Exact explanation of grammatical aspect or syntactic mismatch.
   - **Correct Solution:** Technical rationale for the correct answer.
   - **Czech Contrastive Linguistic Note:** Explaining mother-tongue interference and why Czech native speakers make this error.
   - **Tatra Workplace Example:** Real-world context in automotive engineering, assembly, or sales.
3. **Instant First-Try Scoring & Persistence:**
   - Tracks official first-try score vs subsequent practice attempts.
   - Saves progress automatically in `localStorage`.
   - Score reset capability for clean re-attempts.
4. **NotebookLM Export Engine:**
   - One-click generation of a clean Markdown study digest formatted specifically for Google NotebookLM.
   - Automatically summarizes missed questions, grammatical rules, Czech contrastive points, and includes a prompt tailored for NotebookLM's **Audio Overview** feature (generating an AI podcast debrief of the user's test performance).

---

## 🚀 Running the Suite Locally

Start any standard HTTP server from the project directory:

```powershell
# Using Python (built-in):
python -m http.server 8088

# Open in browser:
# http://127.0.0.1:8088/index.html
```

Or open individual tests directly:
- `http://127.0.0.1:8088/test_runner.html?test=TTR-B1-001`
- `http://127.0.0.1:8088/test_runner.html?test=TTR-B2-001`
- `http://127.0.0.1:8088/test_runner.html?test=TTR-SP-004`

---

## 🧪 Validating Test Modules

Every test JSON must adhere strictly to `schema/test_schema.json`. Run the automated validator:

```powershell
python scripts\validate_tests.py
```

The script verifies:
1. JSON Schema Draft-7 conformance.
2. Question count per test (8–12 questions).
3. Valid option keys and correct key presence.
4. Explanations for all incorrect options (`wrong_A`, `wrong_B`, etc.).
5. Presence of comprehensive Czech contrastive learning notes (`cz_learning_point`).
