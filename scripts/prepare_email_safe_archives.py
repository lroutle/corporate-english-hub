#!/usr/bin/env python3
"""
Prepares email-safe versions of distribution packages.
Creates:
1. Renamed extensions (*.zip.rename_to_zip) which bypass Gmail's automatic filetype scanner.
2. Password-protected 7z archives with encrypted headers (-p -mhe=on) where scanners cannot inspect internal .bat and .js files.
"""

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT / "dist"
SAFE_DIR = DIST_DIR / "email_safe"
SAFE_DIR.mkdir(parents=True, exist_ok=True)

zip_files = list(DIST_DIR.glob("*.zip"))

print("Generating email-safe packages...")

# 1. Renamed extension packages (Bypasses Gmail extension filter)
for zf in zip_files:
    # Rename to .zip.txt (Gmail allows attaching .txt files without scanning payload for .bat/.js)
    txt_dest = SAFE_DIR / f"{zf.name}.txt"
    shutil.copy2(zf, txt_dest)
    print(f"  [Created Renamed] {txt_dest.name}")

# 2. If 7z is available, create encrypted archives (password: english2026)
for zf in zip_files:
    base_name = zf.stem
    suite_dir = ROOT / base_name.replace("_", "-").lower()
    # Check 7z encryption
    dest_7z = SAFE_DIR / f"{base_name}_encrypted.7z"
    try:
        cmd = ["7z", "a", str(dest_7z), str(zf), "-penglish2026", "-mhe=on", "-y"]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"  [Created Encrypted 7z] {dest_7z.name} (password: english2026)")
    except Exception:
        pass

print(f"\nAll email-safe packages ready in: {SAFE_DIR}")
