#!/usr/bin/env python3
"""
Packaging Script for Google Drive Distribution
Creates clean standalone ZIP archives for:
1. The entire multi-suite ecosystem (Master Hub + all 5 corporate suites)
2. Each individual department suite (Tatra Eng, Tatra Sales, Teva Eng, Tapi Chem, Teva IT)
Includes 1-click launchers and clear instructions for students/employees.
"""

import os
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT / "dist"

SUITES = [
    ("tatra-engineering", "Tatra_Engineering_Suite"),
    ("tatra-sales-engineering", "Tatra_Sales_Engineering_Suite"),
    ("tapi-engineering", "Tapi_Engineering_Suite"),
    ("tapi-chemistry", "Tapi_Chemistry_Suite"),
    ("teva-it", "Teva_IT_Suite")
]

STUDENT_README = """========================================================================
   INTERACTIVE WORKPLACE ENGLISH TESTING SUITE - OFFLINE EDITION
========================================================================

Welcome to your corporate interactive English assessment environment.
This suite works 100% offline with NO installation, NO account, and NO server required.

************************************************************************
CRITICAL STEP BEFORE OPENING:
************************************************************************
If you downloaded this file as a ZIP archive:
1. You MUST first RIGHT-CLICK the ZIP file and select:
   -> "Extract All..." (or "Extrahovat vše..." in Czech Windows).
2. Choose a folder and click "Extract".
3. NEVER double-click index.html directly from inside the ZIP!
   (Opening inside the ZIP prevents stylesheets and question data from loading).
4. Do NOT attempt to run inside Google Drive preview (download first).
************************************************************************

HOW TO LAUNCH:
------------------------------------------------------------------------
Option A (Recommended):
  Double-click "Launch_Suite.bat"
  (This will automatically open the suite in Google Chrome or Microsoft Edge)

Option B:
  Double-click "index.html" directly in the extracted folder.

MOBILE PHONES:
------------------------------------------------------------------------
All testing modules are fully mobile responsive! For the best experience on
mobile phones, open index.html using Google Chrome or Apple Safari.

FEATURES:
------------------------------------------------------------------------
- Instant answer feedback with Czech-English contrastive explanations.
- Automatic score calculation and review of missed items.
- "NotebookLM Export" button: Generates an AI audio study digest and Markdown summary.
- Progress saved automatically in your browser.

Enjoy your learning!
"""

MASTER_README = """========================================================================
   MASTER CORPORATE ENGLISH ASSESSMENT ECOSYSTEM - OFFLINE EDITION
========================================================================

Contains all 5 independent corporate assessment suites:
1. Tatra Engineering (Automotive chassis R&D, assembly lines, powertrain)
2. Tatra Sales and Engineering (Defense bids, STANAG, Incoterms, international sales)
3. Tapi Engineering (Cleanroom HVAC, SCADA/PLC, tablet presses, CSV)
4. Tapi Chemistry (Active Pharmaceutical Ingredients, synthesis, HPLC/GC)
5. Teva IT (Cloud infrastructure, DevOps, Zero Trust cybersecurity, SAP/LIMS)

************************************************************************
CRITICAL STEP BEFORE OPENING:
************************************************************************
If you downloaded this as a ZIP archive:
1. RIGHT-CLICK the ZIP and select "Extract All..." ("Extrahovat vše...").
2. Do NOT open index.html from inside the compressed preview window!
3. Do NOT click index.html inside the Google Drive web interface (download first).
************************************************************************

HOW TO LAUNCH:
------------------------------------------------------------------------
Option A (Recommended):
  Double-click "Launch_Master_Hub.bat"
  (Opens the Executive Hub uniting all 5 corporate suites)

Option B:
  Double-click "index.html" directly in the extracted folder.

Option C (Local Web Server):
  Double-click "Start_Local_Server.bat" to run a local HTTP server on port 8088.
"""

def create_zip_archive(source_dir, output_zip_path, extra_files=None):
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                # Skip pycache or dist
                if "__pycache__" in file_path.parts or "dist" in file_path.parts:
                    continue
                arcname = file_path.relative_to(source_dir)
                zipf.write(file_path, arcname)
        if extra_files:
            for arcname, content in extra_files.items():
                zipf.writestr(arcname, content)

def package_all():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    print("Packaging testing suites for Google Drive distribution...\n")

    # 1. Package individual suites
    for suite_slug, archive_name in SUITES:
        suite_path = ROOT / suite_slug
        zip_dest = DIST_DIR / f"{archive_name}.zip"
        print(f"Creating {zip_dest.name}...")
        create_zip_archive(
            suite_path,
            zip_dest,
            extra_files={
                "INSTRUCTIONS_FOR_STUDENTS.txt": STUDENT_README,
                "PLEASE_READ_BEFORE_OPENING.txt": STUDENT_README
            }
        )
        print(f"  [OK] Created {zip_dest.name} ({zip_dest.stat().st_size / 1024:.1f} KB)")

    # 2. Package Master Ecosystem (Master Hub + all 5 suites)
    master_zip_dest = DIST_DIR / "Corporate_English_Testing_Suites_ALL.zip"
    print(f"\nCreating Master Ecosystem: {master_zip_dest.name}...")

    with zipfile.ZipFile(master_zip_dest, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add root index.html and launchers
        zipf.write(ROOT / "index.html", "index.html")
        if (ROOT / "Launch_Master_Hub.bat").exists():
            zipf.write(ROOT / "Launch_Master_Hub.bat", "Launch_Master_Hub.bat")
        if (ROOT / "Start_Local_Server.bat").exists():
            zipf.write(ROOT / "Start_Local_Server.bat", "Start_Local_Server.bat")
        zipf.writestr("INSTRUCTIONS_FOR_STUDENTS.txt", MASTER_README)
        zipf.writestr("PLEASE_READ_BEFORE_OPENING.txt", MASTER_README)

        # Add all 5 suites
        for suite_slug, _ in SUITES:
            suite_path = ROOT / suite_slug
            for root, dirs, files in os.walk(suite_path):
                for file in files:
                    file_path = Path(root) / file
                    if "__pycache__" in file_path.parts:
                        continue
                    arcname = Path(suite_slug) / file_path.relative_to(suite_path)
                    zipf.write(file_path, arcname)

    print(f"  [OK] Created {master_zip_dest.name} ({master_zip_dest.stat().st_size / 1024:.1f} KB)")
    print(f"\nAll archives successfully generated in: {DIST_DIR}")

if __name__ == "__main__":
    package_all()
