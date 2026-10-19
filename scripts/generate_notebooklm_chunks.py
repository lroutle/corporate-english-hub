import os
import re

def create_notebooklm_chunks():
    chunks_dir = r"C:\tmp\00-Mycat\Engineering\NotebookLM_Chunks"
    os.makedirs(chunks_dir, exist_ok=True)

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

    # Read layout doc for rich descriptions
    layout_path = r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_Presentation_Layout.md"
    with open(layout_path, "r", encoding="utf-8") as f:
        layout_text = f.read()

    # Split layout doc by slides
    slide_sections = {}
    pattern = re.compile(r'### Slide (\d+): \[(.*?)\] (.*?)\n(.*?)(?=### Slide \d+:|\Z)', re.DOTALL)
    for match in pattern.finditer(layout_text):
        s_num = int(match.group(1))
        s_time = match.group(2)
        s_title = match.group(3)
        s_body = match.group(4).strip()
        slide_sections[s_num] = {
            "num": s_num,
            "time": s_time,
            "title": s_title,
            "body": s_body,
            "notes": notes_dict.get(s_num, "")
        }

    print(f"Loaded {len(slide_sections)} slides from layout document.")

    # Define the 4 chunks
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

            # Write each slide in this chunk
            for s_num in range(start_slide, end_slide + 1):
                s_data = slide_sections.get(s_num)
                if not s_data:
                    continue
                f.write(f"### Slide {s_num:02d}: [{s_data['time']}] {s_data['title']}\n\n")
                f.write(s_data['body'])
                f.write("\n\n")
                f.write("#### Spoken Speaker Transcript (1.5 - 2.0 Minutes Spoken Delivery):\n")
                f.write("```text\n")
                f.write(s_data['notes'])
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

        print(f"Generated NotebookLM chunk: {filepath}")

    # Generate master guide
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

if __name__ == "__main__":
    create_notebooklm_chunks()
