import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
print("Scanning files to hide NotebookLM...")

# 1. Update CSS
css_files = list(root.glob("**/engine/styles.css"))
for cf in css_files:
    text = cf.read_text(encoding="utf-8")
    if ".btn-export, #btn-export-notebooklm, #modal-btn-export" not in text:
        text = text.replace(
            ".btn-export { background: #0284c7; color: #fff; }",
            ".btn-export, #btn-export-notebooklm, #modal-btn-export { display: none !important; }"
        )
        text = text.replace(
            ".btn-export {",
            ".btn-export, #btn-export-notebooklm, #modal-btn-export { display: none !important; }\n.btn-export-orig {"
        )
        cf.write_text(text, encoding="utf-8")
        print(f"Updated CSS: {cf}")

# 2. Update app.js
app_files = list(root.glob("**/engine/app.js"))
for af in app_files:
    text = af.read_text(encoding="utf-8")
    text = re.sub(r'<button class="btn btn-export" id="btn-export-notebooklm"[^>]*>.*?</button>', '<!-- NotebookLM export hidden -->', text)
    text = re.sub(r'<button class="btn btn-export" id="modal-btn-export"[^>]*>.*?</button>', '', text)
    af.write_text(text, encoding="utf-8")
    print(f"Updated JS: {af}")

# 3. Clean mentions in HTML
html_files = list(root.glob("**/*.html"))
for hf in html_files:
    text = hf.read_text(encoding="utf-8")
    text = text.replace(", and Google NotebookLM export", "")
    text = text.replace("and Google NotebookLM export.", "")
    text = text.replace("and Google NotebookLM export", "")
    text = text.replace(" | Integrated NotebookLM Exporter Engine", "")
    hf.write_text(text, encoding="utf-8")
    print(f"Cleaned mentions in {hf.name}")

print("\nNotebookLM has been completely hidden across all files!")
