import os
import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image

def build_all():
    # 1. First, extract slide data and speaker notes
    print("Extracting slide data and speaker notes...")

    # Load speaker notes from generate_automotive_presentation.py
    notes_dict = {}
    with open(r"C:\tmp\00-Mycat\scripts\generate_automotive_presentation.py", "r", encoding="utf-8") as f:
        pptx_code = f.read()

    parts = pptx_code.split("set_speaker_notes(s")
    for part in parts[1:]:
        slide_idx_str = part.split(",", 1)[0].strip()
        try:
            slide_idx = int(slide_idx_str)
            note_content = part.split('"""', 2)[1].strip()
            notes_dict[slide_idx] = note_content
        except Exception:
            pass

    # Extract slides_data from test_slide_data.py
    with open(r"C:\tmp\00-Mycat\scripts\test_slide_data.py", "r", encoding="utf-8") as f:
        ts_code = f.read()

    # We can evaluate the slides_data list from the code
    start_token = "slides_data = ["
    start_pos = ts_code.find(start_token)
    end_token = "print(f\"Total defined slides:"
    end_pos = ts_code.find(end_token)
    list_str = ts_code[start_pos + len("slides_data = "):end_pos].strip()
    # remove trailing closing bracket if needed
    if list_str.endswith("]"):
        pass
    else:
        # find last ']'
        last_bracket = list_str.rfind("]")
        list_str = list_str[:last_bracket+1]

    slides_data = eval(list_str)
    print(f"Loaded {len(slides_data)} slides from test_slide_data.")

    # 2. Build 4 NotebookLM Markdown Chunks and Guide
    build_notebooklm_chunks(slides_data, notes_dict)

    # 3. Build Google Sheets / Excel Master Workbook
    build_excel_master_workbook(slides_data, notes_dict)


def build_notebooklm_chunks(slides_data, notes_dict):
    chunks_dir = r"C:\tmp\00-Mycat\Engineering\NotebookLM_Chunks"
    os.makedirs(chunks_dir, exist_ok=True)

    chunk_defs = [
        {
            "id": "Chunk_1",
            "filename": "01_Chunk_1_Horizons_and_CAD_Evolution_Slides_01_08.md",
            "title": "Part 1: Executive Horizons & Four Decades of CAD Design Evolution",
            "range": (1, 8),
            "summary": "Covers the executive introduction, four career horizons (CAD Designer, Project Engineer, Project Manager, Engineering Manager), and the complete 40-year evolution of automotive CAD from 1970s manual drafting boards to modern parametric solids and digital mockup (DMU).",
            "prompt": "Act as an executive automotive engineering advisor. Using this source material, generate a crisp, highly structured 8-slide presentation deck covering the progression from CAD drafting to engineering leadership, highlighting the technical differences between 2D drafting and 3D parametric solids, DMU clash detection, and kinematic packaging."
        },
        {
            "id": "Chunk_2",
            "filename": "02_Chunk_2_Vehicle_Platforms_Portfolio_Slides_09_15.md",
            "title": "Part 2: Landmark Vehicle Platforms Portfolio (Ford & Volkswagen)",
            "range": (9, 15),
            "summary": "Deep dive into 12 iconic global vehicle programs across Ford (BE91 Fiesta, BE146 Ka, C195 Ikon, C170 Focus Mk1, CD132 Mondeo Mk3, EUCD multi-brand, B2E Fiesta Mk6, B2XX EcoSport) and Volkswagen (MQB-27 A0, MQB-37 A1/A2, MEB EV Skateboard, T7 Multivan), detailing packaging innovations, multi-link kinematics, boron steel pressings, and EV skateboards.",
            "prompt": "Act as a Chief Technical Officer in vehicle architecture. Using this source, generate a high-impact 7-slide presentation deck analyzing the platform engineering and packaging breakthroughs across Ford and Volkswagen, contrasting transverse ICE modular matrices (MQB) with dedicated electric skateboards (MEB), and detailing the C170 Control Blade suspension and C195 emerging market adaptations."
        },
        {
            "id": "Chunk_3",
            "filename": "03_Chunk_3_Design_to_Manufacture_Flowchart_Slides_16_22.md",
            "title": "Part 3: End-to-End Design-to-Manufacture Flowchart & Upstream Engineering",
            "range": (16, 22),
            "summary": "Exhaustive coverage of the 12-stage vehicle development lifecycle from styling concept through Ford FDJ / VW DKM Design Freeze to hard tooling tryout, alongside in-depth disciplines: 3D Hardpoint Packaging, DFM/DFA stamping & injection moulding feasibility, DFMEA (Ford Handbook v4.2, P-Diagrams, Severity >= 8 rule), and 2D GD&T detailing (ASME Y14.5 & VW RPS datum target pin systems).",
            "prompt": "Act as an Engineering Director and Quality Fellow. Using this source, generate an authoritative 7-slide technical slide deck that walks through the 12-stage automotive design-to-manufacture lifecycle, detailing upstream virtual engineering, critical design freeze gateway criteria (Ford FDJ / VW DKM), DFMEA P-diagram linkages, and ASME Y14.5 vs VW RPS datum locating principles."
        },
        {
            "id": "Chunk_4",
            "filename": "04_Chunk_4_Validation_Crash_APQP_and_Leadership_Slides_23_32.md",
            "title": "Part 4: Virtual Validation, Crashworthiness, APQP Launch, Case Studies & Leadership",
            "range": (23, 32),
            "summary": "Covers downstream engineering disciplines: 1D/3D VSA tolerance stackups, structural FEA rigidity & modal decoupling, LS-DYNA crashworthiness (1500 MPa hot-stamped boron 22MnB5 & MEB EV battery cell protection), APQP & PPAP PSW sign-offs, 3 technical case studies (C170 Multi-Link, EUCD multi-brand safety, MQB vs MEB), multi-million-pound tooling governance, and executive conclusions.",
            "prompt": "Act as a VP of Global Vehicle Engineering. Using this source, generate a 10-slide executive presentation deck on advanced virtual crash simulation, APQP launch governance (Cpk >= 1.67, Gage R&R < 10%), multimillion-pound tooling capital asset risk management, and the architectural comparison between ICE platforms and dedicated EV skateboards."
        }
    ]

    for chunk in chunk_defs:
        filepath = os.path.join(chunks_dir, chunk["filename"])
        start_slide, end_slide = chunk["range"]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# NotebookLM Modular Source Deck: {chunk['title']}\n")
            f.write(f"## Slide Deck Chunk Coverage: Slides {start_slide:02d} to {end_slide:02d} | 30-Minute Master Presentation Suite\n\n")
            f.write("> [!IMPORTANT]\n")
            f.write(f"> **Chunk Scope**: {chunk['summary']}\n")
            f.write(">\n")
            f.write(f"> **Recommended NotebookLM Slide Generation Prompt**:\n")
            f.write(f'> *"{chunk["prompt"]}"*\n\n')
            f.write("---\n\n")

            for s in slides_data:
                s_num = s["num"]
                if not (start_slide <= s_num <= end_slide):
                    continue

                f.write(f"### Slide {s_num:02d}: [{s['time']}] {s['title']}\n")
                f.write(f"**Category:** {s['cat']}\n\n")

                # Format content based on slide type
                stype = s.get("type", "")
                if stype == "cards_3":
                    for col_key in ["col1", "col2", "col3"]:
                        if col_key in s:
                            col_title, items = s[col_key]
                            f.write(f"#### {col_title}\n")
                            for item_h, item_d in items:
                                f.write(f"* **{item_h}:** {item_d}\n")
                            f.write("\n")
                elif stype == "cards_2":
                    for col_key in ["col1", "col2"]:
                        if col_key in s:
                            col_info = s[col_key]
                            col_title = col_info[0]
                            col_sub = col_info[1]
                            items = col_info[2]
                            f.write(f"#### {col_title} ({col_sub})\n")
                            for item_h, item_d in items:
                                f.write(f"* **{item_h}:** {item_d}\n")
                            f.write("\n")
                elif stype == "comp_table":
                    f.write("| Feature / Attribute | Conventional / Manual Approach | Advanced / Modern Automotive Approach |\n")
                    f.write("| :--- | :--- | :--- |\n")
                    for row in s.get("rows", []):
                        f.write(f"| **{row[0]}** | **{row[1]}:** {row[2]} | **{row[3]}:** {row[4]} |\n")
                    f.write("\n")
                elif stype == "title":
                    f.write("Executive Opening Slide establishing 25+ years bridging CAD geometry with multi-billion-pound global vehicle architectures across Ford and Volkswagen.\n\n")
                elif stype == "horizons":
                    f.write("Overview of the four progressive career horizons:\n")
                    f.write("1. **CAD Designer (Horizon 1):** Master sections, parametric CAD (CATIA/NX), packaging sweeps, 2D ASME Y14.5 / RPS drafting.\n")
                    f.write("2. **Project Engineer (Horizon 2):** BIW & closures subsystems, DFMEA chairing (Ford v4.2), virtual FEA rigidity & crash.\n")
                    f.write("3. **Project Manager (Horizon 3):** OEM Gateway governance (GPDS / PEP), multimillion-pound tooling procurement, prototype fleet delivery.\n")
                    f.write("4. **Engineering Manager (Horizon 4):** APQP & PSW sign-off, EV architectural migration (MEB), engineering talent leadership.\n\n")
                elif stype == "timeline":
                    f.write("Four Decades of Automotive CAD Evolution:\n")
                    f.write("* **1970s Mylar Board Era:** Manual orthogonal drafting on high-stability polyester film, beam compasses, physical chalk lofting floors.\n")
                    f.write("* **1980s 2D/3D Wireframe Era:** Green CRT vectors, Computervision & Ford PDGS, wireframe edges without surface enclosures.\n")
                    f.write("* **2000s 3D Parametric Solids Era:** Associative solids in CATIA V5 & NX, feature trees, full-vehicle Digital Mockup (DMU) clash analysis.\n")
                    f.write("* **2020s Generative AI Era:** Topology optimization, algorithmically grown load paths, surrogate neural-network crash simulation in milliseconds.\n\n")
                elif stype.startswith("flowchart"):
                    f.write("End-to-end 12-stage vehicle industrialization cycle detailing the transition from virtual geometry through the Design Freeze Gateway (Ford FDJ / VW DKM) to physical tooling build, Cpk qualification, and Job 1 volume production.\n\n")
                elif stype == "takeaways":
                    f.write("Four Tenets of World-Class Automotive Engineering:\n")
                    f.write("1. **Geometry is Destiny:** CAD models must reflect true manufacturing reality—draft angles, flange access, and springback.\n")
                    f.write("2. **Design Freeze is the Point of No Return:** Engineering discipline at FDJ / DKM protects millions in tooling capital.\n")
                    f.write("3. **Simulate Virtuality, Respect Physics:** CAE accelerates cycle times, but physical testing and statistical Cpk validate safety.\n")
                    f.write("4. **Holistic Systems Thinking:** True engineering leadership unites design, manufacturing, quality, and program timing.\n\n")
                elif stype == "qa":
                    f.write("Collaborative Technical Q&A session covering platform packaging, crash structures, DFMEA, GD&T, and engineering leadership.\n\n")

                # Add Spoken Speaker Notes
                f.write("#### Spoken Speaker Transcript (1.5 - 2.0 Minutes Spoken Delivery):\n")
                f.write("```text\n")
                f.write(notes_dict.get(s_num, "Spoken script for this slide."))
                f.write("\n```\n\n")
                f.write("---\n\n")

            # Add deep discussion hooks for NotebookLM audio podcast
            f.write("### Targeted Discussion Hooks for NotebookLM Deep Dive Audio Overview\n\n")
            f.write("When generating the Deep Dive Audio Podcast in NotebookLM for this chunk, the two AI co-hosts should focus on:\n")
            if chunk["id"] == "Chunk_1":
                f.write("1. The tangible human reality of transitioning from physical drawing boards, mylar ink erasers, and chalk lofting to CRT monitors and parametric 3D models.\n")
                f.write("2. How parametric modeling (CATIA/NX) eliminated the catastrophic risk of 2D drawing mismatches on high-volume body pressings.\n")
                f.write("3. The career trajectory from detailed CAD geometry creator to managing multimillion-pound vehicle architecture budgets and cross-functional teams.\n")
            elif chunk["id"] == "Chunk_2":
                f.write("1. The brilliant engineering economy of Ford BE146 (Ka) sharing the BE91 (Fiesta) underbody pressings while executing radical 'New Edge' styling curves.\n")
                f.write("2. Why the Ford C170 Focus Control Blade rear suspension transformed the automotive industry and humiliated rival torsion-beam competitors.\n")
                f.write("3. How Volkswagen's MQB standardized the engine mounting angle (12° backwards) and pedal-to-axle dimension, creating billions in tooling reusability.\n")
                f.write("4. The monumental structural packaging shift from MQB ICE underbody tunnels to MEB dedicated flat skateboard battery enclosures.\n")
            elif chunk["id"] == "Chunk_3":
                f.write("1. Why the Design Freeze Gateway (Ford FDJ / VW DKM) is the absolute financial 'Point of No Return' in automotive engineering.\n")
                f.write("2. How the Ford DFMEA Handbook v4.2 enforces Severity >= 8 mandatory redesign to eliminate safety and compliance risks before cutting steel.\n")
                f.write("3. The vital operational difference between ASME Y14.5 GD&T and Volkswagen RPS (Reference Point System) datum pin coordination in high-speed framing cells.\n")
            elif chunk["id"] == "Chunk_4":
                f.write("1. The metallurgy of hot-stamped boron steel (22MnB5) achieving 1500 MPa tensile strength to survive high-speed side pole intrusion.\n")
                f.write("2. How APQP gateways prevent premature production ramp-up by requiring Gage R&R < 10% and initial capability Cpk >= 1.67.\n")
                f.write("3. Managing multimillion-pound stamping die and injection mould capital risk across global Tier-1 toolmaker supply chains.\n")

        print(f"Successfully generated: {filepath}")

    # Write Master Guide
    guide_path = os.path.join(chunks_dir, "NotebookLM_MultiChunk_Master_Guide.md")
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write("""# NotebookLM Multi-Chunk Master Guide: Executive Automotive Engineering

## Overview & Solution to NotebookLM Page/Slide Limits

NotebookLM is an extraordinary generative AI research engine powered by Gemini 1.5 Pro. However, when users ask NotebookLM to generate a slide deck from a massive 32-slide compendium all at once, NotebookLM's slide creator tool can hit output limits (typically generating only 6 to 8 slides, heavily summarizing or omitting technical nuance).

To guarantee **100% full-depth technical coverage** of your 25-year career across 12 vehicle programs, CAD evolution, and the 12-stage Design-to-Manufacture lifecycle, your presentation has been divided into **4 dedicated, bite-sized source decks**:

| Chunk File | Slides Covered | Core Engineering Focus | Word Count |
| :--- | :--- | :--- | :--- |
| **`01_Chunk_1_Horizons_and_CAD_Evolution_Slides_01_08.md`** | Slides 01 – 08 | 4 Career Horizons & 40-Year CAD Progression (Mylar to AI) | ~2,800 words |
| **`02_Chunk_2_Vehicle_Platforms_Portfolio_Slides_09_15.md`** | Slides 09 – 15 | 12 Vehicle Programs: Ford BE91/146/C195/C170/EUCD & VW MQB/MEB/T7 | ~2,900 words |
| **`03_Chunk_3_Design_to_Manufacture_Flowchart_Slides_16_22.md`** | Slides 16 – 22 | 12-Stage Flowchart, FDJ/DKM Design Freeze, DFMEA & RPS GD&T | ~3,100 words |
| **`04_Chunk_4_Validation_Crash_APQP_and_Leadership_Slides_23_32.md`** | Slides 23 – 32 | FEA, 1500 MPa Boron Crash, APQP Cpk, 3 Case Studies & Leadership | ~3,400 words |

---

## Step-by-Step Instructions: Starting Your New NotebookLM Workbook

### 1. Create a New Notebook in NotebookLM
1. Open [notebooklm.google.com](https://notebooklm.google.com).
2. Click **"+ New Notebook"**.
3. Name your notebook: **`Automotive Engineering Executive Master Profile`**.

### 2. Ingest the 4 Chunks as Independent Sources
1. In the left-hand **Sources** panel, click **"Add Source" -> "Upload File"** (or paste text).
2. Upload all 4 chunk markdown files from:
   `C:\\tmp\\00-Mycat\\Engineering\\NotebookLM_Chunks\\`
3. NotebookLM will parse each source with Gemini 1.5 Pro's 1-million-token window, indexing all 32 slides, engineering terms, and speaker transcripts.

### 3. Generate Individual Chunk Slide Decks
Select **one source at a time** in the left sidebar and paste the recommended prompt in the chat box:

* **For Chunk 1 (Slides 01-08):**
  > *"Generate an executive 8-slide presentation deck covering the progression from manual drafting boards to modern 3D parametric CAD, detailing the four career horizons, 3-2-1 locating principles, and DMU packaging sweeps."*

* **For Chunk 2 (Slides 09-15):**
  > *"Generate a 7-slide architectural slide deck analyzing the 12 landmark Ford and VW vehicle programs, focusing on the C170 Control Blade multi-link rear suspension, the C195 emerging market boot packaging, and the MQB ICE vs. MEB EV skateboard architecture."*

* **For Chunk 3 (Slides 16-22):**
  > *"Generate a 7-slide technical slide deck walking through the 12-stage automotive design-to-manufacture lifecycle, explaining the Ford FDJ / VW DKM Design Freeze gateway, the Ford v4.2 DFMEA Severity >= 8 rule, and ASME Y14.5 vs VW RPS datum schemes."*

* **For Chunk 4 (Slides 23-32):**
  > *"Generate a 10-slide executive presentation deck on advanced virtual crash simulation (hot-stamped boron 22MnB5), APQP production launch capability (Cpk >= 1.67), multimillion-pound tooling risk management, and the four tenets of world-class automotive engineering."*

### 4. Generate the 2-Host "Deep Dive" Audio Podcast
1. Check **all 4 sources** so NotebookLM sees your complete career.
2. In the right-hand **Notebook Guide** panel, click **"Generate"** under **Deep Dive Audio Overview**.
3. NotebookLM will generate a lifelike, engaging **15 to 20 minute conversation between two AI hosts** discussing your journey from junior CAD Designer drawing master sections on BE91 to Engineering Manager directing global vehicle programs and EV platform migrations.
""")
    print(f"Generated NotebookLM master guide: {guide_path}")


def build_excel_master_workbook(slides_data, notes_dict):
    out_path = r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_Master_GoogleSheets_Workbook.xlsx"
    print(f"Building Master Google Sheets Workbook at: {out_path}...")

    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    # Styles
    f_title = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
    f_sub = Font(name="Calibri", size=11, italic=True, color="E2E8F0")
    f_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    f_body = Font(name="Calibri", size=10, color="0F172A")
    f_body_bold = Font(name="Calibri", size=10, bold=True, color="0F172A")
    f_code = Font(name="Consolas", size=9.5, color="0369A1")

    fill_navy = PatternFill("solid", fgColor="0A192F")
    fill_slate = PatternFill("solid", fgColor="1E293B")
    fill_blue = PatternFill("solid", fgColor="0284C7")
    fill_teal = PatternFill("solid", fgColor="0D9488")
    fill_amber = PatternFill("solid", fgColor="D97706")
    fill_zebra = PatternFill("solid", fgColor="F8FAFC")
    fill_white = PatternFill("solid", fgColor="FFFFFF")

    thin_border_side = Side(style="thin", color="CBD5E1")
    border_all = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_top_left = Alignment(horizontal="left", vertical="top", wrap_text=True)

    # Assets dir
    assets_dir = r"C:\tmp\00-Mycat\Engineering\assets"

    # ==========================================
    # TAB 1: 00_Executive_Dashboard
    # ==========================================
    ws0 = wb.create_sheet(title="00_Executive_Dashboard")
    ws0.views.sheetView[0].showGridLines = True

    # Title Banner
    ws0.merge_cells("A1:K1")
    ws0["A1"] = "AUTOMOTIVE ENGINEERING MASTER REPOSITORY & CONTENT MATRIX"
    ws0["A1"].font = f_title
    ws0["A1"].fill = fill_navy
    ws0["A1"].alignment = align_center
    ws0.row_dimensions[1].height = 40

    ws0.merge_cells("A2:K2")
    ws0["A2"] = "25+ Years Experience Across 12 Vehicle Programs (Ford & VW), CAD Evolution, 12-Stage Lifecycle & APQP Governance"
    ws0["A2"].font = f_sub
    ws0["A2"].fill = fill_slate
    ws0["A2"].alignment = align_center
    ws0.row_dimensions[2].height = 24

    # KPI Summary Cards
    kpis = [
        ("GLOBAL PLATFORMS", "12 Programs", "Ford & VW Portfolios", fill_blue),
        ("CAREER HORIZONS", "4 Eras", "CAD to Engineering Mgr", fill_teal),
        ("PRESENTATION DECK", "32 Slides", "30:00 Target Timing", fill_amber),
        ("LIFECYCLE STAGES", "12 Stages", "Virtual Concept to Job 1", fill_slate),
        ("NOTEBOOKLM SOURCE", "4 Chunks", "Modular Sub-Decks", fill_navy),
    ]

    col_idx = 1
    for kpi_title, kpi_val, kpi_sub, kpi_fill in kpis:
        c_letter1 = get_column_letter(col_idx)
        c_letter2 = get_column_letter(col_idx + 1)
        ws0.merge_cells(f"{c_letter1}4:{c_letter2}4")
        ws0.merge_cells(f"{c_letter1}5:{c_letter2}5")
        ws0.merge_cells(f"{c_letter1}6:{c_letter2}6")

        ws0[f"{c_letter1}4"] = kpi_title
        ws0[f"{c_letter1}4"].font = Font(name="Calibri", size=9, bold=True, color="CBD5E1")
        ws0[f"{c_letter1}4"].fill = kpi_fill
        ws0[f"{c_letter1}4"].alignment = align_center

        ws0[f"{c_letter1}5"] = kpi_val
        ws0[f"{c_letter1}5"].font = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
        ws0[f"{c_letter1}5"].fill = kpi_fill
        ws0[f"{c_letter1}5"].alignment = align_center

        ws0[f"{c_letter1}6"] = kpi_sub
        ws0[f"{c_letter1}6"].font = Font(name="Calibri", size=8.5, italic=True, color="E2E8F0")
        ws0[f"{c_letter1}6"].fill = kpi_fill
        ws0[f"{c_letter1}6"].alignment = align_center

        col_idx += 2

    ws0.row_dimensions[4].height = 20
    ws0.row_dimensions[5].height = 30
    ws0.row_dimensions[6].height = 20

    # Career Progression Table
    ws0.cell(row=8, column=1, value="CAREER HORIZONS ARCHITECTURE").font = Font(name="Calibri", size=12, bold=True, color="0A192F")
    horizons_headers = ["Horizon", "Role Title", "Core Technical Domain", "Primary Tools", "Key Leadership Accountability"]
    for c_i, h in enumerate(horizons_headers, 1):
        cell = ws0.cell(row=9, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_slate
        cell.alignment = align_center
        cell.border = border_all
    ws0.row_dimensions[9].height = 24

    horizons_data = [
        ("Horizon 1", "CAD Designer", "Geometry Creation, Surfacing & Drafting", "CATIA V4/V5, NX, ASME Y14.5", "Parametric design intent, master sections, kinematics, 2D release"),
        ("Horizon 2", "Project Engineer", "Cross-Functional Subsystems & Virtual CAE", "DFMEA (Ford v4.2), Nastran, LS-DYNA", "Subsystem integration (BIW/Closures), P-Diagrams, crash pulses"),
        ("Horizon 3", "Project Manager", "OEM Gateways, Tooling Capital & Timing", "Ford GPDS, VW PEP, Hard Tooling Dies", "Gateways (FDJ/DKM), multi-million-pound die procurement, prototype fleets"),
        ("Horizon 4", "Engineering Manager", "APQP Governance, Strategy & Mentorship", "DVP&R, PPAP/PSW, Resource Planning", "Technical sign-off, EV architectural migration (MEB), engineering team leadership")
    ]
    for r_i, row_vals in enumerate(horizons_data, 10):
        for c_i, val in enumerate(row_vals, 1):
            cell = ws0.cell(row=r_i, column=c_i, value=val)
            cell.font = f_body
            cell.alignment = align_left if c_i > 2 else align_center
            cell.fill = fill_zebra if r_i % 2 == 0 else fill_white
            cell.border = border_all
        ws0.row_dimensions[r_i].height = 24

    # Embed Flowchart Graphic on Dashboard
    flow_img_path = os.path.join(assets_dir, "automotive_flowchart_diagram.jpg")
    if os.path.exists(flow_img_path):
        img_dash = Image(flow_img_path)
        img_dash.width = 620
        img_dash.height = 348
        ws0.add_image(img_dash, "A16")
        ws0.cell(row=15, column=1, value="12-STAGE DESIGN-TO-MANUFACTURE ARCHITECTURE OVERVIEW").font = Font(name="Calibri", size=12, bold=True, color="0A192F")

    # Set Column Widths for Dashboard
    dash_widths = [14, 22, 34, 32, 42, 12, 12, 12, 12, 12, 12]
    for i, w in enumerate(dash_widths, 1):
        ws0.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 2: 01_Slide_Deck_Roster
    # ==========================================
    ws1 = wb.create_sheet(title="01_Slide_Deck_Roster")
    ws1.views.sheetView[0].showGridLines = True

    roster_headers = [
        "Slide #", "Time Slot", "Slide Title", "Category / Section", "Visual Layout",
        "Key Engineering Objective", "Core Slide Bullets & Content", "Spoken Delivery Transcript (Speaker Notes)",
        "NotebookLM Chunk", "Status"
    ]
    for c_i, h in enumerate(roster_headers, 1):
        cell = ws1.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_navy
        cell.alignment = align_center
        cell.border = border_all
    ws1.row_dimensions[1].height = 28

    for s_i, s in enumerate(slides_data, 2):
        s_num = s["num"]
        time_slot = s["time"]
        title = s["title"]
        cat = s["cat"]
        stype = s.get("type", "Standard")

        # Map to chunk
        if 1 <= s_num <= 8:
            chunk_name = "Chunk 1: Horizons & CAD Evolution"
        elif 9 <= s_num <= 15:
            chunk_name = "Chunk 2: Vehicle Platforms"
        elif 16 <= s_num <= 22:
            chunk_name = "Chunk 3: Flowchart & Upstream DFM"
        else:
            chunk_name = "Chunk 4: Validation, Crash & APQP"

        # Summarize bullets
        bullets_text = ""
        if stype == "cards_3":
            for col_k in ["col1", "col2", "col3"]:
                if col_k in s:
                    bullets_text += f"[{s[col_k][0]}]: " + "; ".join([f"{h}: {d}" for h, d in s[col_k][1]]) + "\n"
        elif stype == "cards_2":
            for col_k in ["col1", "col2"]:
                if col_k in s:
                    bullets_text += f"[{s[col_k][0]} ({s[col_k][1]})]: " + "; ".join([f"{h}: {d}" for h, d in s[col_k][2]]) + "\n"
        elif stype == "comp_table":
            bullets_text = "Comparative Table: " + "; ".join([f"{r[0]} ({r[1]} vs {r[3]})" for r in s.get("rows", [])])
        else:
            bullets_text = title

        obj_text = f"Deliver master engineering insights on {title} within {time_slot}."
        spoken_script = notes_dict.get(s_num, "Spoken script.")

        row_vals = [
            f"Slide {s_num:02d}", time_slot, title, cat, stype,
            obj_text, bullets_text.strip(), spoken_script.strip(), chunk_name, "POLISHED"
        ]

        for c_i, val in enumerate(row_vals, 1):
            cell = ws1.cell(row=s_i, column=c_i, value=val)
            cell.font = f_body
            cell.fill = fill_zebra if s_i % 2 == 0 else fill_white
            cell.border = border_all
            if c_i in [1, 2, 5, 9, 10]:
                cell.alignment = align_center
            else:
                cell.alignment = align_top_left

        ws1.row_dimensions[s_i].height = 70

    roster_widths = [10, 14, 28, 26, 16, 28, 45, 60, 24, 12]
    for i, w in enumerate(roster_widths, 1):
        ws1.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 3: 02_Vehicle_Platforms
    # ==========================================
    ws2 = wb.create_sheet(title="02_Vehicle_Platforms")
    ws2.views.sheetView[0].showGridLines = True

    vp_headers = [
        "Code", "OEM", "Vehicle Model", "Segment", "Production Years", "Architecture Type",
        "BIW Steel Composition", "Packaging Innovation", "Chassis / Dynamic Setup",
        "Safety / Crash Targets", "Assembly Plants", "Engineering Role & Scope"
    ]
    for c_i, h in enumerate(vp_headers, 1):
        cell = ws2.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_slate
        cell.alignment = align_center
        cell.border = border_all
    ws2.row_dimensions[1].height = 28

    platforms_data = [
        ("BE91", "Ford", "Fiesta (Mk4)", "B-Segment Hatchback", "1995 - 2002", "Transverse FWD Unibody", "Mild steel, high-strength low-alloy (HSLA), tailored welded blanks", "Coil blank nesting >80% utilization; consolidated inner pressings", "MacPherson strut front, twist-beam rear axle", "ECE R94 frontal crash compliance, progressive rail folding triggers", "Dagenham, Cologne, Valencia", "CAD Designer: Master sections, door inner stampings, packaging sweeps"),
        ("BE146", "Ford", "Ka", "Sub-B City Car", "1996 - 2008", "Shared BE91 Underbody", "HSLA structural members, shared floorpan pressings with BE91", "Short front overhang packaging; radical 'New Edge' styling curves", "Tuned front geometry for urban turning circle agility", "Euro NCAP 3-star occupant protection, consolidated bumper beams", "Valencia (Spain)", "CAD Designer: Under-hood packaging, cooling pack envelopes, Class-A/B offsets"),
        ("C195", "Ford", "Ikon", "B-Segment 3-Box Saloon", "1999 - 2011", "Extended B-Platform Saloon", "Reinforced HSLA rear parcel shelf, D-pillar gussets & floorpan", "Spacious 3-box notchback boot packaging for emerging markets", "Heavy-duty rough-road suspension, increased ground clearance (+25 mm)", "Monsoon and dust intrusion sealing (double-lip weatherstripping)", "Chennai (India), South Africa", "Project Engineer: Body structure reinforcement, dust/water sealing, tooling reviews"),
        ("C170", "Ford", "Focus (Mk1)", "C-Segment Compact", "1998 - 2004", "All-New Global C-Car", "High-strength dual-phase steels (DP600), laser-welded blanks", "Zero cabin boot intrusion with full multi-link rear suspension", "Control Blade multi-link rear suspension with passive toe compliance", "Euro NCAP 4-star benchmark, ultra-stiff passenger safety cell", "Saarlouis, Valencia, Wayne (USA)", "Project Engineer: Control Blade packaging, subframe isolation bushings, FEA rigidity"),
        ("CD132", "Ford", "Mondeo (Mk3)", "D-Segment Executive", "2000 - 2007", "Global CD Platform", "Ultra-high-strength boron steel nodes, laser-brazed roof skin seams", "Laser-brazed roof joints eliminating plastic ditch mouldings", "Isolated front & rear subframes, multi-link rear suspension", "Euro NCAP 4-star, dual front crash sensors, rigid passenger cell", "Genk (Belgium)", "Project Engineer: Subsystem integration, laser roof brazing DFM, DFMEA chair"),
        ("EUCD", "Ford / Volvo / JLR", "Mondeo / S-MAX / Galaxy / V70", "C/D Multi-Brand Platform", "2006 - 2015", "Shared Multi-Brand Global", "Press-hardened boron steel (22MnB5), DP800 structural reinforcements", "Harmonized architecture sharing across Ford, Volvo, Land Rover", "Modular front/rear subframes accommodating transverse AWD/FWD", "Euro NCAP 5-star, deformable pedestrian subframes, Volvo safety cell", "Genk, Ghent, Torslanda", "Project Manager: Multi-brand engineering alignment, crash sled testing, prototype fleet"),
        ("B2E", "Ford", "Fiesta (Mk6)", "Global B-Car Platform", "2008 - 2017", "Global B Architecture", ">55% high-strength and ultra-high-strength boron steel in BIW", "Kinetic Design packaging; lightweight unibody saving 40 kg vs predecessor", "Optimized twist-beam rear axle with custom bush kinematics", "Euro NCAP 5-star, hot-formed boron B-pillars, roof crush compliance", "Cologne, Valencia, Cuautitlan, Nanjing", "Project Manager: Tooling capital commitment, gateway reviews (FDJ), APQP launch"),
        ("B2XX", "Ford", "EcoSport", "Compact SUV / Crossover", "2012 - 2022", "Raised B2E Architecture", "High-strength steel reinforced D-pillars, rear quarter & sills", "Raised ground clearance (>200 mm), side-hinged spare wheel tailgate", "Reinforced damper mountings for rough-road impact loads", "Full frontal offset crash and rear luggage impact containment (ECE R17)", "Camaçari, Chennai, Craiova", "Project Manager: D-pillar hinge structural reinforcement, latch slam durability"),
        ("MQB-27", "Volkswagen", "Polo / T-Cross (A0)", "Subcompact Modular Matrix", "2017 - Present", "Modularer Querbaukasten A0", ">30% hot-stamped boron steel passenger cell, tailored rolled blanks", "Standardized front pedal-to-axle distance with flexible wheelbase", "Modular front subframe with standardized transverse engine tilt (12°)", "Euro NCAP 5-star, IIHS small overlap crash compliance", "Pamplona, Uitenhage, Shanghai", "Engineering Manager: APQP governance, RPS datum targeting, PSW sign-off"),
        ("MQB-37", "Volkswagen", "Golf 7/8 / Passat (A1/A2)", "Core C/D Modular Matrix", "2012 - Present", "Modularer Querbaukasten Core", "Hot-formed ultra-high-strength steel passenger safety cage (1500 MPa)", "Standardized electrical topology, unified HVAC packaging, modular seats", "MacPherson front, modular 4-link rear (torsion beam on low power)", "Euro NCAP 5-star benchmark, automated emergency braking integration", "Wolfsburg, Zwickau, Puebla, Changchun", "Engineering Manager: Departmental resource strategy, tooling tryout (TT), Cpk"),
        ("MEB", "Volkswagen", "ID.3 / ID.4 / ID.Buzz", "Dedicated EV Skateboard", "2019 - Present", "Modularer E-Antriebs-Baukasten", "Extruded aluminium battery sill cage, AHSS upper cabin structure", "Underbody battery structural shear plate (+25% torsional rigidity)", "Low center-of-gravity, multi-link rear axle packaging e-motor", "Euro NCAP 5-star, zero side-pole battery cell intrusion, high-voltage cutoff", "Zwickau, Emden, Chattanooga, Anting", "Engineering Manager: EV architectural migration, battery sill crash CAE, DVP&R"),
        ("T7 Multivan", "Volkswagen", "Multivan T7", "Commercial MPV / Van", "2021 - Present", "MQB Commercial Adaptation", "Hot-formed boron A/B pillars, modular flat load floor pressings", "Modular floor tracking system, versatile 7-seater packaging, plug-in hybrid", "MQB car-like front MacPherson strut, semi-trailing rear suspension", "Euro NCAP 5-star, seat track pull strength compliance (ECE R14)", "Hannover (Germany)", "Engineering Manager: APQP launch governance, modular seat anchorage verification")
    ]

    for r_i, r_data in enumerate(platforms_data, 2):
        for c_i, val in enumerate(r_data, 1):
            cell = ws2.cell(row=r_i, column=c_i, value=val)
            cell.font = f_body
            cell.fill = fill_zebra if r_i % 2 == 0 else fill_white
            cell.border = border_all
            if c_i in [1, 2, 4, 5]:
                cell.alignment = align_center
            else:
                cell.alignment = align_top_left
        ws2.row_dimensions[r_i].height = 42

    vp_widths = [10, 12, 18, 22, 16, 24, 30, 34, 30, 30, 24, 34]
    for i, w in enumerate(vp_widths, 1):
        ws2.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 4: 03_Design_to_Mfg_12Stages
    # ==========================================
    ws3 = wb.create_sheet(title="03_Design_to_Mfg_12Stages")
    ws3.views.sheetView[0].showGridLines = True

    stages_headers = [
        "Stage #", "Lifecycle Phase", "Stage Name", "Core Engineering Deliverables",
        "Primary Software Tools", "Ford Milestone (GPDS)", "VW Milestone (PEP)",
        "Quality Tool / Gate Criteria", "Lead Time / Duration", "Capital Investment Level"
    ]
    for c_i, h in enumerate(stages_headers, 1):
        cell = ws3.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_navy
        cell.alignment = align_center
        cell.border = border_all
    ws3.row_dimensions[1].height = 28

    stages_data = [
        ("Stage 01", "Upstream Virtual", "Market Study & Vehicle Hardpoints", "Voice of Customer, target curb weight, wheelbase, ground clearance, SAE J826 H-point", "CATIA / NX, RAMSIS", "Kick-Off (KO)", "Produkt-Meilenstein (PM)", "Product Charter, Target Cost BOM", "3 - 6 Months", "Low (< £1M)"),
        ("Stage 02", "Upstream Virtual", "3D Styling Surfaces & Master Sections", "Class-A scan release, Class-B structural inners, pillar master cross-sections", "Alias, ICEM Surf, CATIA V5", "Strategic Intent (SI)", "Produkt-Festlegung (PF)", "Surface feasibility sign-off", "4 - 8 Months", "Low (< £2M)"),
        ("Stage 03", "Upstream Virtual", "Packaging & Kinematic Clearances", "Suspension jounce/rebound sweeps (+100/-80mm), door arcs, tire chain clearances", "CATIA DMU Kinematics, NX", "Strategic Conf. (SC)", "Konzeptevaluation (KE)", "Zero static/dynamic clashes in DMU", "3 - 6 Months", "Low (< £3M)"),
        ("Stage 04", "Upstream Virtual", "Design for Manufacture (DFM/DFA)", "Stamping FLD strain analysis, injection moulding draft/rib-sink, weld gun access", "AutoForm, Moldflow, Robcad", "Surface Freeze (SF)", "Datenkontrollmodell (DKM)", "Stamping draw depth & draft sign-off", "3 - 5 Months", "Medium (£5M - £10M)"),
        ("Stage 05", "Upstream Virtual", "DFMEA & Robustness Linkages", "P-Diagram boundary, Severity >= 8 mandatory redesign, Critical Characteristics (∇ CC)", "Ford FMEA Portal, ReliaSoft", "Final Eng. Release", "Konzeptfreeze", "DFMEA closure, Special Chars on CAD", "2 - 4 Months", "Engineering Headcount"),
        ("Stage 06", "Upstream Virtual", "2D Detailing & GD&T Architecture", "ASME Y14.5 / ISO 1101 drawings, 3-2-1 datums, VW RPS coordinate target pads", "CATIA Drafting, NX Drafting", "Final Data Judgement (FDJ)", "Datenkontrollmodell (DKM)", "Datum Reference Frames (DRFs) locked", "2 - 4 Months", "Engineering Headcount"),
        ("Stage 07", "Upstream Virtual", "Virtual CAE (FEA, NVH & Crash)", "Torsional stiffness (18-28 kNm/°), modal frequencies (>38Hz), LS-DYNA crash pulses", "Nastran, Abaqus, LS-DYNA", "Virtual Prototypes (VP)", "Vorserie-Freigabe", "Euro NCAP 5-star virtual compliance", "4 - 8 Months", "High (£10M CAE/HPC)"),
        ("GATEWAY", "GATEWAY FREEZE", "★ DESIGN FREEZE GATEWAY ★", "Complete geometric lock; absolute Point of No Return for tooling release", "CAD / PDM PLM Lock", "FDJ Complete", "DKM Complete", "Executive Gate Review Sign-off", "MILESTONE", "★ CAPITAL RELEASE ★"),
        ("Stage 08", "Downstream Physical", "Hard Tooling Procurement & Build", "CNC milling of cast iron stamping dies, EDM injection moulds, robotic framing bucks", "WorkNC, Tebis, Delcam CAM", "Tooling Kick-Off (TKO)", "Werkzeug-Freigabe", "Die layout approval, steel procurement", "9 - 14 Months", "Extremely High (£50M - £200M)"),
        ("Stage 09", "Downstream Physical", "Tooling Tryout (TT / Vorserie)", "First off-tool parts, 100% CMM balloon dimensional inspection, stamping FLD verification", "GOM ATOS Laser, PolyWorks", "Verification Prototypes", "Vorserien-Fahrzeuge (VFF)", "100% off-tool dimensional report", "3 - 5 Months", "High (Prototypes)"),
        ("Stage 10", "Downstream Physical", "Process Capability Studies", "PFMEA, Control Plans, Gage R&R < 10%, Statistical Process Control (Cpk >= 1.67)", "Minitab, Q-DAS, SPC Data", "Pilot Production (PP)", "Pilotserie (PVS)", "Capability study sign-off (Cpk >= 1.67)", "3 - 4 Months", "Medium (Launch Audits)"),
        ("Stage 11", "Downstream Physical", "PPAP 18 Elements & PSW Sign-Off", "18 PPAP elements, lab test certs, DVP&R completion, signed Part Submission Warrant", "Ford APQP, VW Beon Portal", "Mass Production 1 (MP1)", "Nullserie (0-Serie)", "Signed PSW warrant by Engineering Mgr", "1 - 2 Months", "Legal / Compliance"),
        ("Stage 12", "Downstream Physical", "Job 1 / SOP Volume Mass Production", "Line takt time ramp-up (60s cycle), safe launch containment, statistical quality SPC", "SAP MES, SCADA, Plant SPC", "Job 1 / OK to Ship", "Start of Production (SOP)", "Customer delivery release, final audits", "Ongoing (5-7 yr lifecycle)", "Full Operating Budget")
    ]

    for r_i, r_vals in enumerate(stages_data, 2):
        is_gate = r_vals[0] == "GATEWAY"
        for c_i, val in enumerate(r_vals, 1):
            cell = ws3.cell(row=r_i, column=c_i, value=val)
            cell.font = Font(name="Calibri", size=10, bold=is_gate, color="FFFFFF" if is_gate else "0F172A")
            cell.fill = fill_amber if is_gate else (fill_zebra if r_i % 2 == 0 else fill_white)
            cell.border = border_all
            if c_i in [1, 2, 6, 7, 9, 10]:
                cell.alignment = align_center
            else:
                cell.alignment = align_top_left
        ws3.row_dimensions[r_i].height = 36 if not is_gate else 28

    stages_widths = [12, 18, 30, 42, 26, 20, 20, 32, 20, 22]
    for i, w in enumerate(stages_widths, 1):
        ws3.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 5: 04_CAD_Evolution_Matrix
    # ==========================================
    ws4 = wb.create_sheet(title="04_CAD_Evolution_Matrix")
    ws4.views.sheetView[0].showGridLines = True

    cad_headers = [
        "CAD Era", "Decade", "Dominant CAD Systems", "Geometric Modeling Method",
        "Drawing & Data Release", "Clash & Interference Detection", "Stamping & CNC Tooling Linkage",
        "Cycle Time & Productivity Impact", "Key Engineering Milestone"
    ]
    for c_i, h in enumerate(cad_headers, 1):
        cell = ws4.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_teal
        cell.alignment = align_center
        cell.border = border_all
    ws4.row_dimensions[1].height = 28

    cad_data = [
        ("1. Manual Drafting Boards", "1960s - 1970s", "Drafting tables, parallel motions, ink pens, mylar film", "Manual orthographic 2D projections; hand lofting curves with spline weights", "Physical paper blueprints; microfiche archives; manual change stamps", "Manual visual overlay; physical wooden / clay packaging bucks", "Wooden pattern makers; manual copy-milling tracer machines (Keller)", "Months per engineering iteration; high risk of view mismatch errors", "1963 Ivan Sutherland's Sketchpad at MIT; PRONTO at GE"),
        ("2. Early 2D/3D Wireframe", "1980s - 1990s", "Computervision CADDS, Ford PDGS, IBM CADAM, early AutoCAD", "2D digital lines and 3D wireframe vectors on green phosphor CRT monitors", "2D electronic CAD plots; magnetic tapes; initial IGES neutral files", "Manual 3D wireframe rotation; still reliant on physical prototype bucks", "Early 3-axis CNC toolpaths directly from 3D surface splines", "30-40% reduction in drafting drawing time; wireframe ambiguities remained", "Ford PDGS platform; GM DAC-1; Bezier curves at Renault (UNISURF)"),
        ("3. 3D Parametric Solids & DMU", "2000s - 2010s", "CATIA V4/V5, Siemens NX (Unigraphics), PTC Pro/ENGINEER, C3P", "Feature-based parametric solid modeling with CSG trees and B-Rep surfaces", "Single-source associative 3D solid models; live 2D drawing projections", "Automated batch Digital Mockup (DMU) clash detection across complete car", "Direct 5-axis high-speed CNC die milling from Class-A/B CAD surfaces", "60-70% cycle time reduction; complete elimination of wooden styling bucks", "Ford C3P digital vehicle initiative; VW MQB virtual DMU platform integration"),
        ("4. Generative AI & Cloud Simulation", "2020s - Present", "CATIA 3DEXPERIENCE, NX Generative Design, Altair OptiStruct, AI CAD", "Cloud-native collaborative geometry, algorithmic generative topology synthesis", "Model-Based Definition (MBD / 3D GD&T); instant cloud PDM synchronization", "Real-time AI clash clearance prediction and dynamic multi-body kinematics", "Additive manufacturing tooling inserts with conformal cooling channels", "10x faster generative design loops; 20-30% structural mass reduction", "Surrogate neural-network crash modeling predicting LS-DYNA pulses in milliseconds")
    ]

    for r_i, r_vals in enumerate(cad_data, 2):
        for c_i, val in enumerate(r_vals, 1):
            cell = ws4.cell(row=r_i, column=c_i, value=val)
            cell.font = f_body
            cell.fill = fill_zebra if r_i % 2 == 0 else fill_white
            cell.border = border_all
            if c_i in [1, 2]:
                cell.alignment = align_center
            else:
                cell.alignment = align_top_left
        ws4.row_dimensions[r_i].height = 45

    # Embed CAD graphic
    cad_img_path = os.path.join(assets_dir, "cad_design_evolution.jpg")
    if os.path.exists(cad_img_path):
        img_cad = Image(cad_img_path)
        img_cad.width = 600
        img_cad.height = 338
        ws4.add_image(img_cad, "A8")
        ws4.cell(row=7, column=1, value="CHRONOLOGICAL CAD EVOLUTION ILLUSTRATION").font = Font(name="Calibri", size=12, bold=True, color="0A192F")

    cad_widths = [24, 16, 28, 34, 30, 32, 32, 32, 34]
    for i, w in enumerate(cad_widths, 1):
        ws4.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 6: 05_DFMEA_P_Diagram_Register
    # ==========================================
    ws5 = wb.create_sheet(title="05_DFMEA_P_Diagram_Register")
    ws5.views.sheetView[0].showGridLines = True

    dfmea_headers = [
        "System / Subsystem", "Component", "Function", "Potential Failure Mode",
        "Potential Effect of Failure", "S", "Class (∇)", "Potential Cause / Mechanism",
        "O", "Current Prevention Control", "Current Detection Control", "D",
        "RPN", "Recommended Action", "New S", "New O", "New D", "New RPN", "Action Status"
    ]
    for c_i, h in enumerate(dfmea_headers, 1):
        cell = ws5.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_amber
        cell.alignment = align_center
        cell.border = border_all
    ws5.row_dimensions[1].height = 28

    dfmea_data = [
        ("BIW / Side Structure", "B-Pillar Outer & Reinforcement", "Transfer side impact loads into roof rail and sill; prevent cabin intrusion", "Excessive B-pillar deformation & tearing during Euro NCAP side pole impact", "Severe occupant torso / pelvic injury; breach of survival cell", 9, "∇ CC", "Insufficient material ductility in transition zone between 1500 MPa boron and ductile base", 4, "Tailored tempering die technology creating soft zone (>600 MPa, 15% elongation) at lower pillar", "LS-DYNA dynamic side pole simulation with calibrated fracture criteria", 3, "=F2*I2*L2", "Enforce 22MnB5 hot-stamping with tailored cooling die zones; 100% CMM & ultrasonic weld inspection", 9, 2, 2, "=O2*P2*Q2", "CLOSED"),
        ("Chassis / Rear Suspension", "Control Blade Trailing Arm", "React longitudinal braking & road bump loads; maintain passive toe compliance", "Fatigue cracking at trailing blade to hub bracket weld joint", "Loss of wheel location; unstable high-speed vehicle handling under heavy braking", 8, "∇ CC", "Stress concentration peak from sharp stamping radius combined with cyclic road load inputs", 5, "FEA fatigue optimization (Miner's Rule); minimum stamping radius >= 3.0t", "Multi-axis servo-hydraulic road simulator rig test (150,000 miles equivalent)", 4, "=F3*I3*L3", "Increase blade thickness from 2.5 mm to 2.8 mm in high-stress zone; add shot-peening to weld toe", 8, 2, 2, "=O3*P3*Q3", "CLOSED"),
        ("BIW / Front Structure", "Front Longitudinal Rail Crash Box", "Absorb kinetic energy in frontal impact via progressive axial folding", "Asymmetric rail buckling /Euler column collapse without progressive accordion folding", "High deceleration spike (>40g) transmitted to cabin; excessive dummy chest injury", 9, "∇ CC", "Forming thinning during stamping draw exceeding 20% at trigger indentations", 4, "AutoForm stamping simulation verifying blank draw; double-flanged trigger beads in CAD", "High-speed servo-hydraulic impact sled test at 56 km/h", 3, "=F4*I4*L4", "Redesign trigger geometry with generous 4.0 mm fillets; specify DP600 dual-phase steel with tight yield spread", 9, 2, 2, "=O4*P4*Q4", "CLOSED"),
        ("EV Architecture / Underbody", "Battery Tray Extruded Aluminium Sill", "Isolate high-voltage battery modules from lateral side-pole collision intrusion", "Rupture of outer sill extrusion chambers allowing battery module deformation", "Battery cell puncture, thermal runaway fire hazard, passenger compartment burn", 10, "∇ CC", "Extrusion web thickness insufficient to absorb 50 kJ kinetic energy during 32 km/h side pole", 4, "Multi-cell 6000-series aluminium extrusion design with internal triangular ribs", "LS-DYNA detailed crash CAE with battery cell crush failure models", 2, "=F5*I5*L5", "Add internal high-strength steel intrusion beam within center aluminium chamber; 100% laser weld inspection", 10, 1, 2, "=O5*P5*Q5", "CLOSED"),
        ("Closures / Side Doors", "Door Hinge & Check Arm Assembly", "Support door mass over 100k cycles; maintain 30-40% weatherstrip seal compression", "Door sag exceeding 2.5 mm after 50,000 durability slam cycles", "Wind noise hiss at highway speed; water leak; increased customer closing effort", 6, "SC", "Elongation of bronze hinge pin bushing under cyclic gravity load and slam fatigue", 6, "Select oil-impregnated sintered bronze bushing; reinforce door inner hinge backing plate (2.0 mm)", "Rig durability slam test (100,000 cycles at -30°C to +80°C)", 3, "=F6*I6*L6", "Upgrade to PTFE-lined stainless steel composite bushing; add structural embossment on A-pillar mounting", 6, 2, 2, "=O6*P6*Q6", "CLOSED"),
        ("Closures / Tailgate", "External Spare Wheel Tailgate Carrier", "Secure 25 kg spare wheel assembly under severe rough-road vertical acceleration", "Fatigue fracture of D-pillar inner reinforcement bracket", "Tailgate latch rattles, misalignment, potential spare wheel detachment on rough terrain", 8, "∇ CC", "High dynamic pitch moment from cantilevered spare tire mass on severe off-road washboard roads", 5, "Add high-strength steel gusset bracket transferring loads directly into rear roof header & quarter panel", "Accelerated shaker table durability test (3-axis road profile simulation)", 3, "=F7*I7*L7", "Enforce 2.5 mm HSLA inner doubler plate; specify structural adhesive bonding along entire D-pillar seam", 8, 2, 2, "=O7*P7*Q7", "CLOSED")
    ]

    for r_i, r_vals in enumerate(dfmea_data, 2):
        for c_i, val in enumerate(r_vals, 1):
            cell = ws5.cell(row=r_i, column=c_i, value=val)
            cell.font = f_body
            cell.fill = fill_zebra if r_i % 2 == 0 else fill_white
            cell.border = border_all
            if c_i in [6, 7, 9, 12, 13, 15, 16, 17, 18, 19]:
                cell.alignment = align_center
                if c_i in [13, 18]:
                    cell.font = f_body_bold
            else:
                cell.alignment = align_top_left
        ws5.row_dimensions[r_i].height = 48

    dfmea_widths = [18, 22, 28, 30, 30, 8, 10, 30, 8, 30, 30, 8, 10, 32, 8, 8, 8, 10, 14]
    for i, w in enumerate(dfmea_widths, 1):
        ws5.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 7: 06_GDT_Metrology_RPS
    # ==========================================
    ws6 = wb.create_sheet(title="06_GDT_Metrology_RPS")
    ws6.views.sheetView[0].showGridLines = True

    gdt_headers = [
        "Subsystem / Feature", "Component Name", "Standard", "Primary Datum A (3 Pts)",
        "Secondary Datum B (2 Pts)", "Tertiary Datum C (1 Pt)", "VW RPS Target Codes",
        "Geometric Control", "Tolerance Value", "Inspection Method", "Gage R&R Target", "Capability Target (Cpk)"
    ]
    for c_i, h in enumerate(gdt_headers, 1):
        cell = ws6.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_slate
        cell.alignment = align_center
        cell.border = border_all
    ws6.row_dimensions[1].height = 28

    gdt_data = [
        ("BIW / Side Aperture", "Side Body Outer Stamping", "VW RPS 01.01", "3 Surface Pads on Rocker & B-Pillar", "Round Hole in A-Pillar (4-way pin)", "Slotted Hole in C-Pillar (2-way pin)", "RPS-F01, F02, F03 / RPS-H01, H02", "Profile of Surface (|∩|)", "1.0 mm to DRF [A|B|C]", "Optical Laser Scan / CMM", "Gage R&R < 10%", "Cpk >= 1.67"),
        ("Chassis / Subframe", "Front Engine Cradle Subframe", "ASME Y14.5M", "3 Machined Bushing Mounting Faces", "Front Left Locating Hole (4-way)", "Front Right Slotted Hole (2-way)", "DRF [A|B|C] (Chassis Master)", "True Position (⨁)", "0.5 mm at MMC to [A|B|C]", "Coordinate Measuring Machine", "Gage R&R < 10%", "Cpk >= 2.00"),
        ("Closures / Front Hood", "Engine Hood Outer Skin", "ISO 1101", "3 Hem Flange Support Contacts", "Hinge Pivot Axis Left Pin", "Striker Latch Catch Pin", "RPS-F11, F12, F13 / RPS-H11", "Profile of Surface (|∩|)", "0.7 mm to DRF [A|B|C]", "In-Line Laser Gap/Flush Gage", "Gage R&R < 10%", "Cpk >= 1.67"),
        ("Closures / Side Door", "Front Door Inner Pressing", "VW RPS 01.01", "3 Pads on Inner Structural Flange", "Upper Hinge Master Hole (4-way)", "Lower Hinge Slotted Hole (2-way)", "RPS-F21, F22, F23 / RPS-H21, H22", "True Position (⨁)", "0.8 mm at MMC to [A|B|C]", "Checking Fixture with Dial Gages", "Gage R&R < 15%", "Cpk >= 1.67"),
        ("Exterior / Fascia", "Front Bumper Fascia", "ASME Y14.5M", "4 Body Mounting Clips / Flange Plane", "Center Grille Guide Pin (4-way)", "Right Headlamp Guide Slot (2-way)", "DRF [A|B|C] (Plastic Assembly)", "Profile of Surface (|∩|)", "1.5 mm to DRF [A|B|C]", "Optical CMM (GOM ATOS Scan)", "Gage R&R < 10%", "Cpk >= 1.50"),
        ("EV Battery / Enclosure", "Battery Housing Lower Tray", "VW RPS 01.01", "4 Machined Underbody Attachment Bosses", "Front Left Alignment Dowel Hole", "Rear Right Slotted Dowel Hole", "RPS-F31 to F34 / RPS-H31, H32", "Flatness (⏥) & Profile (|∩|)", "Flatness 1.0 mm; Profile 1.2 mm", "Automated Laser Tracker CMM", "Gage R&R < 10%", "Cpk >= 1.67")
    ]

    for r_i, r_vals in enumerate(gdt_data, 2):
        for c_i, val in enumerate(r_vals, 1):
            cell = ws6.cell(row=r_i, column=c_i, value=val)
            cell.font = f_body
            cell.fill = fill_zebra if r_i % 2 == 0 else fill_white
            cell.border = border_all
            if c_i in [3, 7, 8, 9, 11, 12]:
                cell.alignment = align_center
            else:
                cell.alignment = align_top_left
        ws6.row_dimensions[r_i].height = 36

    # Embed GD&T Graphic
    gdt_img_path = os.path.join(assets_dir, "dimensional_gdt_metrology.jpg")
    if os.path.exists(gdt_img_path):
        img_gdt = Image(gdt_img_path)
        img_gdt.width = 600
        img_gdt.height = 338
        ws6.add_image(img_gdt, "A10")
        ws6.cell(row=9, column=1, value="METROLOGY & GD&T DATUM TARGETING ILLUSTRATION").font = Font(name="Calibri", size=12, bold=True, color="0A192F")

    gdt_widths = [20, 24, 14, 28, 26, 26, 24, 20, 18, 24, 16, 16]
    for i, w in enumerate(gdt_widths, 1):
        ws6.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 8: 07_Crash_Safety_BIW
    # ==========================================
    ws7 = wb.create_sheet(title="07_Crash_Safety_BIW")
    ws7.views.sheetView[0].showGridLines = True

    crash_headers = [
        "Crash Mode", "Impact Speed / Setup", "Standard / Agency", "Primary Load Path Subsystem",
        "Material Grade", "Tensile Strength (Rm)", "Energy Absorption Mode", "Intrusion Target",
        "CAE Solver", "Key Safety Outcome"
    ]
    for c_i, h in enumerate(crash_headers, 1):
        cell = ws7.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_blue
        cell.alignment = align_center
        cell.border = border_all
    ws7.row_dimensions[1].height = 28

    crash_data = [
        ("Frontal Offset Deformable", "64 km/h (40 mph) 40% Offset", "Euro NCAP / UNECE R94", "Front rail crash box, subframe shear, shotgun upper rail", "DP600 Dual Phase & HSLA 350", "600 - 800 MPa", "Axial progressive folding (accordion plastic hinges)", "A-pillar displacement < 30 mm", "LS-DYNA Explicit", "Intact passenger cell; steering wheel intrusion < 15 mm"),
        ("Frontal Full Width Rigid", "50 km/h (31 mph) 100% Rigid", "Euro NCAP / US FMVSS 208", "Upper and lower rail system, front subframe crossmember", "Dual-phase DP600 & mild steel deep-draw", "400 - 600 MPa", "Controlled front crush pulse (<35g occupant deceleration)", "Firewall intrusion < 20 mm", "LS-DYNA Explicit", "Restraint system timing; low thoracic rib deflection"),
        ("Side Mobile Deformable", "60 km/h (37 mph) MDB 1400 kg", "Euro NCAP / US FMVSS 214", "B-pillar hot-stamping, rocker sill, door anti-intrusion beams", "Hot-stamped boron steel (22MnB5)", "1500 MPa", "High-strength anti-intrusion ring, load transfer to roof/floor", "B-pillar intrusion velocity < 8 m/s", "LS-DYNA Explicit", "Zero survival cell breach; pelvic & chest load containment"),
        ("Side Pole Impact", "32 km/h (20 mph) 75° Oblique", "Euro NCAP / US FMVSS 214", "Center B-pillar, cross-car floor members, seat cross-members", "Hot-stamped boron 22MnB5 & DP1000", "1500 MPa", "Local plastic bending with high yield resistance to penetration", "B-pillar intrusion < 120 mm to seat H-point", "LS-DYNA Explicit", "Curtain airbag deployment; head protection from pole strike"),
        ("EV Lateral Battery Pole", "32 km/h (20 mph) 75° Oblique", "Euro NCAP / Global EV Regs", "Extruded aluminium battery sill, cross-car battery bulkheads", "6000-series Al extrusion & UHSS floor", "250 - 320 MPa (Al) / 1000 MPa", "Multi-cell progressive crush of aluminium extrusion chambers", "Zero deformation of battery modules (<5 mm)", "LS-DYNA Explicit", "Zero cell puncture, no thermal runaway, automatic HV pyrofuse cutoff"),
        ("Rear Moving Barrier", "80 km/h (50 mph) 70% Offset", "US FMVSS 301 / ECE R34", "Rear longitudinal side rails, rear bumper beam, spare wheel floor", "Dual Phase DP600 & HSLA 380", "600 - 800 MPa", "Progressive axial crumple of rear rails protecting fuel tank / battery", "Fuel tank zero leak; battery tray undamaged", "LS-DYNA Explicit", "Fuel system integrity; high-voltage isolation maintained")
    ]

    for r_i, r_vals in enumerate(crash_data, 2):
        for c_i, val in enumerate(r_vals, 1):
            cell = ws7.cell(row=r_i, column=c_i, value=val)
            cell.font = f_body
            cell.fill = fill_zebra if r_i % 2 == 0 else fill_white
            cell.border = border_all
            if c_i in [1, 3, 6, 8, 9]:
                cell.alignment = align_center
            else:
                cell.alignment = align_top_left
        ws7.row_dimensions[r_i].height = 36

    # Embed Crash Graphic
    crash_img_path = os.path.join(assets_dir, "biw_crash_safety.jpg")
    if os.path.exists(crash_img_path):
        img_crash = Image(crash_img_path)
        img_crash.width = 600
        img_crash.height = 338
        ws7.add_image(img_crash, "A10")
        ws7.cell(row=9, column=1, value="BIW CRASH SAFETY LOAD PATHS & BORON STEEL ILLUSTRATION").font = Font(name="Calibri", size=12, bold=True, color="0A192F")

    crash_widths = [22, 22, 20, 32, 26, 18, 30, 24, 18, 32]
    for i, w in enumerate(crash_widths, 1):
        ws7.column_dimensions[get_column_letter(i)].width = w


    # ==========================================
    # TAB 9: 08_NotebookLM_Chunk_Plan
    # ==========================================
    ws8 = wb.create_sheet(title="08_NotebookLM_Chunk_Plan")
    ws8.views.sheetView[0].showGridLines = True

    chunk_headers = [
        "Chunk ID", "Chunk Title", "Source File Name", "Slide Range", "Slide Count",
        "Core Engineering Scope", "Word Count", "NotebookLM Slide Generation Prompt",
        "Audio Podcast Discussion Focus", "Status"
    ]
    for c_i, h in enumerate(chunk_headers, 1):
        cell = ws8.cell(row=1, column=c_i, value=h)
        cell.font = f_header
        cell.fill = fill_navy
        cell.alignment = align_center
        cell.border = border_all
    ws8.row_dimensions[1].height = 28

    chunk_table_data = [
        ("Chunk 1", "Executive Horizons & 40-Year CAD Evolution", "01_Chunk_1_Horizons_and_CAD_Evolution_Slides_01_08.md", "Slides 01 – 08", 8, "4 Career Horizons (Designer to Eng Mgr) and CAD Evolution (Mylar to Generative AI)", "~2,800 words", "Generate an executive 8-slide presentation deck covering the progression from manual drafting boards to modern 3D parametric CAD, detailing four career horizons, 3-2-1 locating principles, and DMU packaging sweeps.", "Human transition from manual drawing boards to 3D parametric solids; eliminating high-volume sheet metal errors; career growth from geometry creator to engineering leader.", "READY TO INGEST"),
        ("Chunk 2", "12 Landmark Vehicle Programs Portfolio", "02_Chunk_2_Vehicle_Platforms_Portfolio_Slides_09_15.md", "Slides 09 – 15", 7, "12 Ford and VW Vehicle Programs, Packaging Innovations, Kinematics & Modular Toolkits", "~2,900 words", "Generate a 7-slide architectural slide deck analyzing the 12 landmark Ford and VW vehicle programs, focusing on C170 Control Blade suspension, C195 emerging market boot packaging, and MQB ICE vs MEB EV skateboard architecture.", "Ford BE146 Ka sharing BE91 underbody pressings; C170 Focus multi-link suspension triumph; VW MQB standardized engine angle (12°) and pedal-to-axle; MEB dedicated electric skateboard.", "READY TO INGEST"),
        ("Chunk 3", "12-Stage Flowchart & Upstream Engineering", "03_Chunk_3_Design_to_Manufacture_Flowchart_Slides_16_22.md", "Slides 16 – 22", 7, "12-Stage Lifecycle, Design Freeze Gateways (FDJ/DKM), DFM/DFA, DFMEA & GD&T Datums", "~3,100 words", "Generate a 7-slide technical slide deck walking through the 12-stage automotive design-to-manufacture lifecycle, explaining Ford FDJ / VW DKM Design Freeze, Ford v4.2 DFMEA Severity >= 8 rule, and ASME Y14.5 vs VW RPS datum schemes.", "Financial Point of No Return at Design Freeze; Ford DFMEA v4.2 Severity >= 8 mandatory redesign rule; ASME Y14.5 vs VW RPS datum locating pins in robotic welding cells.", "READY TO INGEST"),
        ("Chunk 4", "Virtual Validation, Crash, APQP & Leadership", "04_Chunk_4_Validation_Crash_APQP_and_Leadership_Slides_23_32.md", "Slides 23 – 32", 10, "FEA Rigidity, 1500 MPa Boron Crash, APQP Cpk, 3 Case Studies, Tooling Capital & Synthesis", "~3,400 words", "Generate a 10-slide executive presentation deck on advanced virtual crash simulation (hot-stamped boron 22MnB5), APQP production launch capability (Cpk >= 1.67), multimillion-pound tooling risk management, and the four tenets of world-class automotive engineering.", "Hot-stamped boron steel (22MnB5) achieving 1500 MPa to stop side pole intrusion; APQP Gage R&R < 10% and Cpk >= 1.67; multimillion-pound die tooling risk management.", "READY TO INGEST")
    ]

    for r_i, r_vals in enumerate(chunk_table_data, 2):
        for c_i, val in enumerate(r_vals, 1):
            cell = ws8.cell(row=r_i, column=c_i, value=val)
            cell.font = f_body
            cell.fill = fill_zebra if r_i % 2 == 0 else fill_white
            cell.border = border_all
            if c_i in [1, 4, 5, 7, 10]:
                cell.alignment = align_center
            else:
                cell.alignment = align_top_left
        ws8.row_dimensions[r_i].height = 55

    chunk_widths = [12, 28, 36, 16, 12, 34, 14, 40, 40, 18]
    for i, w in enumerate(chunk_widths, 1):
        ws8.column_dimensions[get_column_letter(i)].width = w

    # Save Master Workbook
    wb.save(out_path)
    print(f"Master Google Sheets Workbook successfully saved: {out_path}")

if __name__ == "__main__":
    build_all()
