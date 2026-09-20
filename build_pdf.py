#!/usr/bin/env python3
"""Render the submission markdown files to PDF via headless Chromium."""
import subprocess, sys, pathlib, markdown

import shots
from figure import FIG
from style import CSS

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>{title}</title><style>{css}</style></head><body>{body}</body></html>"""


def render(md_path: pathlib.Path, pdf_path: pathlib.Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    # GitHub-style task list checkboxes -> real checkboxes
    text = text.replace("- [ ] ", "- ☐ ").replace("- [x] ", "- ☑ ")
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    body = body.replace("<!--SHOT_TABLE-->", shots.table_html())
    body = body.replace("<!--FLOWCHART-->", FIG)
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
