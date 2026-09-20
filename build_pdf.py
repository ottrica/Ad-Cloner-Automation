#!/usr/bin/env python3
"""Render the submission markdown files to PDF via headless Chromium."""
import subprocess, sys, pathlib, markdown

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: A4; margin: 18mm 16mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", "Noto Sans", Arial, sans-serif;
       font-size: 10pt; line-height: 1.47; color: #1c1c1e; margin: 0; }
h1 { font-size: 21pt; margin: 0 0 4pt; letter-spacing: -.4pt; line-height: 1.2; }
h1 + p { color: #555; margin-top: 0; }
h2 { font-size: 13.5pt; margin: 15pt 0 6pt; padding-bottom: 4pt;
     border-bottom: 1.5px solid #1c1c1e; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 14pt 0 5pt; color: #000; page-break-after: avoid; }
h4 { font-size: 10pt; margin: 11pt 0 4pt; page-break-after: avoid; }
p, li { orphans: 2; widows: 2; }
strong { color: #000; }
hr { border: 0; border-top: 1px solid #ddd; margin: 11pt 0; }
table { border-collapse: collapse; width: 100%; margin: 9pt 0;
        font-size: 8.4pt; page-break-inside: auto; }
th { background: #f2f2f4; text-align: left; font-weight: 600;
     border-bottom: 1.5px solid #1c1c1e; }
th, td { padding: 4.5pt 6pt; vertical-align: top;
         border-bottom: 1px solid #e3e3e6; }
tr { page-break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.5pt;
       background: #f2f2f4; padding: 1pt 3pt; border-radius: 2px; }
pre { background: #f7f7f9; border: 1px solid #e3e3e6; border-left: 3px solid #1c1c1e;
      padding: 8pt 10pt; border-radius: 3px; font-size: 8.3pt; line-height: 1.45;
      white-space: pre-wrap; page-break-inside: avoid; margin: 8pt 0; }
pre code { background: none; padding: 0; font-size: inherit; }
blockquote { border-left: 3px solid #c8c8cc; margin: 9pt 0; padding: 2pt 0 2pt 11pt;
             color: #444; font-size: 9.2pt; }
ul, ol { padding-left: 17pt; margin: 6pt 0; }
li { margin: 2pt 0; }
li input[type=checkbox] { margin-right: 4pt; }
a { color: #1c1c1e; }
"""

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>{title}</title><style>{css}</style></head><body>{body}</body></html>"""


def render(md_path: pathlib.Path, pdf_path: pathlib.Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    # GitHub-style task list checkboxes -> real checkboxes
    text = text.replace("- [ ] ", "- ☐ ").replace("- [x] ", "- ☑ ")
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    html_path = pdf_path.with_suffix(".html")
    html_path.write_text(
        HTML.format(title=md_path.stem, css=CSS, body=body), encoding="utf-8")
    subprocess.run([
        CHROME, "--headless", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}", html_path.as_uri(),
    ], check=True, capture_output=True)
    html_path.unlink()
    print(f"  {pdf_path.name}  ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    targets = sys.argv[1:] or ["00_README.md", "01_Production_Spec.md", "03_SOP.md"]
    print("Building PDFs:")
    for name in targets:
        src = ROOT / name
        render(src, src.with_suffix(".pdf"))
