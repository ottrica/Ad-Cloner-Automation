#!/usr/bin/env python3
"""Build the single master submission PDF.

Everything the grader needs is inside one file:
  cover -> Part 1 -> Part 2 -> Part 3 -> Appendix A/B (workflow files, verbatim)

The raw .md workflow files are additionally embedded as PDF file attachments,
so the operator can extract and use them without retyping out of a page.
"""
import pathlib, subprocess, markdown
from pypdf import PdfReader, PdfWriter

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
OUT = ROOT / "Creative_Technologist_Assignment.pdf"

# Documents in reading order. (source file, section label, appendix?)
SECTIONS = [
    ("01_Production_Spec.md", "Part 1 — Production Spec", False),
    ("02_Video_Notes.md",     "Part 2 — The Video",       False),
    ("03_SOP.md",             "Part 3 — Handoff SOP",     False),
]
APPENDICES = [
    ("workflow/ad-cloner.md",   "Appendix A — Workflow File: ad-cloner.md"),
    ("workflow/prompt_sheet.md", "Appendix B — Prompt Sheet: prompt_sheet.md"),
]
ATTACH = ["workflow/ad-cloner.md", "workflow/prompt_sheet.md",
          "01_Production_Spec.md", "03_SOP.md"]

CSS = """
@page { size: A4; margin: 18mm 16mm 16mm; }
@page :first { margin-top: 0; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", "Noto Sans", Arial, sans-serif;
       font-size: 10pt; line-height: 1.47; color: #1c1c1e; margin: 0; }

/* cover */
.cover { height: 247mm; display: flex; flex-direction: column;
         justify-content: center; page-break-after: always; }
.cover .kicker { font-size: 9.5pt; letter-spacing: 2.4pt; text-transform: uppercase;
                 color: #777; margin-bottom: 12pt; }
.cover h1 { font-size: 34pt; line-height: 1.08; letter-spacing: -1pt;
            margin: 0 0 14pt; border: 0; }
.cover .sub { font-size: 12pt; color: #444; line-height: 1.6; }
.cover .rule { border-top: 2px solid #1c1c1e; margin: 22pt 0; }
.cover .meta { font-size: 9.5pt; color: #555; line-height: 1.8; }

/* section dividers */
.divider { page-break-before: always; padding-top: 58mm; page-break-after: always; }
.divider .num { font-size: 9.5pt; letter-spacing: 2.4pt; text-transform: uppercase;
                color: #777; }
.divider h1 { font-size: 27pt; margin: 8pt 0 0; border: 0; letter-spacing: -.6pt; }
.divider .blurb { font-size: 10.5pt; color: #555; margin-top: 12pt;
                  max-width: 105mm; line-height: 1.6; }

h1 { font-size: 20pt; margin: 0 0 4pt; letter-spacing: -.4pt; line-height: 1.2; }
h1 + p { color: #555; margin-top: 0; }
h2 { font-size: 13.5pt; margin: 15pt 0 6pt; padding-bottom: 4pt;
     border-bottom: 1.5px solid #1c1c1e; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 13pt 0 5pt; page-break-after: avoid; }
h4 { font-size: 10pt; margin: 11pt 0 4pt; page-break-after: avoid; }
p, li { orphans: 2; widows: 2; }
strong { color: #000; }
hr { border: 0; border-top: 1px solid #ddd; margin: 11pt 0; }
table { border-collapse: collapse; width: 100%; margin: 9pt 0;
        font-size: 8.4pt; }
th { background: #f2f2f4; text-align: left; font-weight: 600;
     border-bottom: 1.5px solid #1c1c1e; }
th, td { padding: 4.5pt 6pt; vertical-align: top; border-bottom: 1px solid #e3e3e6; }
tr { page-break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.5pt;
       background: #f2f2f4; padding: 1pt 3pt; border-radius: 2px; }
pre { background: #f7f7f9; border: 1px solid #e3e3e6; border-left: 3px solid #1c1c1e;
      padding: 8pt 10pt; border-radius: 3px; font-size: 8pt; line-height: 1.45;
      white-space: pre-wrap; page-break-inside: avoid; margin: 8pt 0; }
pre code { background: none; padding: 0; font-size: inherit; }
blockquote { border-left: 3px solid #c8c8cc; margin: 9pt 0; padding: 2pt 0 2pt 11pt;
             color: #444; font-size: 9.2pt; }
ul, ol { padding-left: 17pt; margin: 6pt 0; }
li { margin: 2pt 0; }
a { color: #1c1c1e; }
.note { background: #f7f7f9; border-left: 3px solid #1c1c1e; padding: 9pt 11pt;
        font-size: 9.2pt; margin: 10pt 0; }
"""

COVER = """
<div class="cover">
  <div class="kicker">Take-Home Assignment</div>
  <h1>Creative<br>Technologist</h1>
  <div class="sub">Dashverse / Frameo</div>
  <div class="rule"></div>
  <div class="meta">
    <strong>Submitted by</strong> [YOUR NAME]<br>
    <strong>Date</strong> [DATE]<br>
    <strong>Reference ad</strong> Chicnutrix &ldquo;Glow Advanced&rdquo; &middot;
      45.6&nbsp;s &middot; 9:16 &middot; 17 shots<br>
    <strong>Stack</strong> Claude &middot; Higgsfield MCP &middot; GPT-Image &middot;
      Premiere Pro + Premiere MCP
  </div>
</div>

<h1>Contents</h1>
<p>This document contains the complete submission. Everything referenced below is
inside this file &mdash; nothing depends on an external link resolving.</p>

<table>
<tr><th>Section</th><th>What it covers</th></tr>
<tr><td><strong>Part 1</strong> &mdash; Production Spec</td>
    <td>Teardown of the reference ad: format, camera reasoning, full shot-by-shot
        table with real timecodes, locked elements, and three questions for the
        client.</td></tr>
<tr><td><strong>Part 2</strong> &mdash; The Video</td>
    <td>The 20&ndash;30&nbsp;second video made for an invented brand, how it maps
        to the spec, declared deviations, and how character consistency was
        held.</td></tr>
<tr><td><strong>Part 3</strong> &mdash; Handoff SOP</td>
    <td>Instructions detailed enough for a non-expert to produce the next video
        in this format without asking me anything. Seven sections.</td></tr>
<tr><td><strong>Appendix A</strong> &mdash; <code>ad-cloner.md</code></td>
    <td>The workflow file the process actually runs on, reproduced verbatim.</td></tr>
<tr><td><strong>Appendix B</strong> &mdash; <code>prompt_sheet.md</code></td>
    <td>Every prompt as a fill-in-the-blank template, reproduced verbatim.</td></tr>
</table>

<div class="note">
<strong>The workflow files are attached to this PDF, not just printed in it.</strong>
Both <code>.md</code> files are embedded as file attachments, so the prompts can be
extracted and used directly rather than retyped. Open the attachments pane in your
PDF reader &mdash; the paperclip icon in Acrobat, or
<em>View &rarr; Navigation Panels &rarr; Attachments</em>. They are also supplied as
loose files alongside this PDF in the submission folder.
</div>

<h2>How the video was made, in one paragraph</h2>
<p>A competitor ad is selected through an ad-intelligence tool and analysed into a
three-part structure &mdash; hook, mid-section, CTA &mdash; with every cut, B-roll
position and camera motion recorded. The script is rewritten for the new brand and,
if it mixes Hindi and English, normalised into Devanagari so voice generation
pronounces it correctly. An avatar is generated from the reference&rsquo;s age and
gender read, then locked to a reference sheet. The script is chunked into beats of
no more than ten seconds each, every beat is generated as talking-head video through
the Higgsfield MCP, and the clips are placed on a Premiere Pro timeline through the
Premiere MCP. The hook is rebuilt separately with motion, the CTA card is composited
from the product image, B-roll is generated and trimmed by hand, and SFX and music
come from an in-house Premiere library. Full detail in Part 3.</p>
"""

DIVIDER = """
<div class="divider">
  <div class="num">{num}</div>
  <h1>{title}</h1>
  <div class="blurb">{blurb}</div>
</div>
"""

BLURBS = {
    "Part 1 — Production Spec":
        "Turning &ldquo;we want this, but for us&rdquo; into a written plan another "
        "team could execute without ever seeing the original.",
    "Part 2 — The Video":
        "The proof. Same format, same camera language, invented brand.",
    "Part 3 — Handoff SOP":
        "Making myself unnecessary &mdash; the method as a system someone else runs.",
    "Appendix A — Workflow File: ad-cloner.md":
        "The runbook the pipeline executes, verbatim. Also attached to this PDF as a file.",
    "Appendix B — Prompt Sheet: prompt_sheet.md":
        "Every prompt, copy-pasteable. Also attached to this PDF as a file.",
}

MD_EXT = ["tables", "fenced_code", "sane_lists"]


def to_html(md_text: str) -> str:
    md_text = md_text.replace("- [ ] ", "- ☐ ").replace("- [x] ", "- ☑ ")
    return markdown.markdown(md_text, extensions=MD_EXT)


def divider(idx: str, title: str) -> str:
    return DIVIDER.format(num=idx, title=title, blurb=BLURBS[title])


def main() -> None:
    parts = [COVER]

    for n, (src, label, _) in enumerate(SECTIONS, 1):
        parts.append(divider(f"Part {n} of 3", label))
        parts.append(to_html((ROOT / src).read_text(encoding="utf-8")))

    for letter, (src, label) in zip("AB", APPENDICES):
        parts.append(divider(f"Appendix {letter}", label))
        raw = (ROOT / src).read_text(encoding="utf-8")
        # verbatim, so the reader sees exactly what the file contains
        parts.append("<pre><code>" +
                     raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") +
                     "</code></pre>")

    html = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
            f'<title>Creative Technologist — Take-Home Assignment</title>'
            f'<style>{CSS}</style></head><body>{"".join(parts)}</body></html>')

    tmp_html = ROOT / "_master.html"
    tmp_html.write_text(html, encoding="utf-8")
    raw_pdf = ROOT / "_master_raw.pdf"
    subprocess.run([
        CHROME, "--headless", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={raw_pdf}", tmp_html.as_uri(),
    ], check=True, capture_output=True)

    # embed the raw source files as real PDF attachments
    writer = PdfWriter(clone_from=str(raw_pdf))
    for rel in ATTACH:
        path = ROOT / rel
        writer.add_attachment(path.name, path.read_bytes())
    writer.add_metadata({
        "/Title": "Creative Technologist — Take-Home Assignment",
        "/Subject": "Dashverse / Frameo — Parts 1-3 with workflow files attached",
    })
    with open(OUT, "wb") as fh:
        writer.write(fh)

    tmp_html.unlink(); raw_pdf.unlink()
    print(f"{OUT.name}: {len(PdfReader(str(OUT)).pages)} pages, "
          f"{OUT.stat().st_size // 1024} KB, {len(ATTACH)} files attached")


if __name__ == "__main__":
    main()
