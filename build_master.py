#!/usr/bin/env python3
"""Build the master submission PDF.

  cover -> contents -> Part 1 -> Part 2 -> Part 3 -> Appendix A/B

Video previews are rendered from real frames of the reference ad. The raw .md
workflow files are embedded as PDF file attachments so prompts can be extracted
rather than retyped.
"""
import io, pathlib, subprocess, markdown
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import shots
from style import CSS

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
OUT = ROOT / "Creative_Technologist_Assignment.pdf"

AUTHOR = "Manish Das"
VIDEO_URL = "https://drive.google.com/file/d/12d0oep34td6RuWrTstSrxOsyWaN9Id_C/view"
REF_URL = "https://www.facebook.com/ads/library/?id=1393506182719580"

SECTIONS = [
    ("01_Production_Spec.md", "Part 1 — Production Spec"),
    ("02_Video_Notes.md",     "Part 2 — The Video"),
    ("03_SOP.md",             "Part 3 — Handoff SOP"),
]
APPENDICES = [
    ("workflow/ad-cloner.md",    "Appendix A — Workflow File"),
    ("workflow/prompt_sheet.md", "Appendix B — Prompt Sheet"),
]
ATTACH = ["workflow/ad-cloner.md", "workflow/prompt_sheet.md",
          "01_Production_Spec.md", "03_SOP.md"]

BLURBS = {
    "Part 1 — Production Spec":
        "Turning &ldquo;we want this, but for us&rdquo; into a written plan another "
        "team could execute without ever seeing the original.",
    "Part 2 — The Video":
        "The proof. Same format, same camera language, invented brand.",
    "Part 3 — Handoff SOP":
        "Making myself unnecessary &mdash; the method as a system someone else runs.",
    "Appendix A — Workflow File":
        "<code>ad-cloner.md</code> &mdash; the runbook the pipeline executes, verbatim. "
        "Also attached to this PDF as a file.",
    "Appendix B — Prompt Sheet":
        "<code>prompt_sheet.md</code> &mdash; every prompt, copy-pasteable. "
        "Also attached to this PDF as a file.",
}

COVER = f"""
<div class="cover">
  <div class="kicker">Take-Home Assignment</div>
  <h1>Creative<span class="thin">Technologist</span></h1>
  <div class="sub">Dashverse / Frameo</div>
  <div class="accentbar"></div>
  <div class="meta">
    <span class="meta-k">Submitted by</span>{AUTHOR}<br>
    <span class="meta-k">Reference ad</span><a href="{REF_URL}">Chicnutrix
      &ldquo;Glow Advanced&rdquo;</a> &middot; 45.6&nbsp;s &middot; 9:16
      &middot; 17 shots<br>
    <span class="meta-k">Part 2 video</span><a href="{VIDEO_URL}">Four Atoms
      &mdash; watch on Google Drive</a><br>
    <span class="meta-k">Stack</span>Claude &middot; Higgsfield MCP &middot;
      GPT-Image &middot; Premiere Pro + Premiere MCP
  </div>
  <div class="strip"><img src="assets/filmstrip.jpg" alt=""></div>
</div>
"""

TOC_ROWS = [
    ("Part 1", "Production Spec",
     "Teardown of the reference ad: format, camera reasoning, a shot-by-shot table "
     "with measured timecodes and stills, locked elements, and three client questions."),
    ("Part 2", "The Video",
     "The video made for an invented brand, how it maps to the spec, declared "
     "deviations, and how character consistency was held."),
    ("Part 3", "Handoff SOP",
     "Instructions detailed enough for a non-expert to produce the next video in "
     "this format without asking me anything. Seven sections."),
    ("Appendix A", "ad-cloner.md",
     "The workflow file the process actually runs on, reproduced verbatim."),
    ("Appendix B", "prompt_sheet.md",
     "Every prompt as a fill-in-the-blank template, reproduced verbatim."),
]


def contents_page() -> str:
    rows = "".join(
        f'<div class="toc-row"><div class="tnum">{n}</div>'
        f'<div class="tbody"><span class="tt">{t}</span><br>'
        f'<span class="td">{d}</span></div></div>'
        for n, t, d in TOC_ROWS)
    return f"""
<h1>Contents</h1>
<p class="lede">Everything in this submission is inside this one file. The workflow
files are also embedded as attachments, and the two videos are linked and previewed
below &mdash; nothing depends on hunting for a separate folder.</p>
<div class="toc">{rows}</div>

<h2>The two videos</h2>

<div class="videocard">
  <div class="vstrip"><img src="assets/filmstrip.jpg" alt="Reference ad frames"></div>
  <div class="vmeta">
    <p class="vtitle">Reference &mdash; Chicnutrix &ldquo;Glow Advanced&rdquo;</p>
    <p class="vsub">45.6&nbsp;s &middot; 720&times;1280 &middot; 30&nbsp;fps &middot;
       17 shots &middot; analysed in Part 1</p>
    <p class="vlink">Watch: <a href="{REF_URL}">Meta Ad Library</a></p>
  </div>
</div>

<div class="videocard placeholder">
  <div class="vph">Poster frame to be added &mdash; open the link to watch</div>
  <div class="vmeta">
    <p class="vtitle">Part 2 &mdash; Four Atoms</p>
    <p class="vsub">Invented brand &middot; 9:16 &middot; shared anyone-with-link,
       no sign-in required</p>
    <p class="vlink">Watch: <a href="{VIDEO_URL}">Google Drive</a></p>
  </div>
</div>

<h2>How the video was made</h2>
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
come from an in-house Premiere library. Full detail in Part&nbsp;3.</p>

<div class="note">
<strong>The workflow files are attached to this PDF, not just printed in it.</strong>
Both <code>.md</code> files are embedded as file attachments, so the prompts can be
extracted and used directly rather than retyped. Open the attachments pane in your
PDF reader &mdash; the paperclip icon in Acrobat, or <em>View &rarr; Navigation
Panels &rarr; Attachments</em>.
</div>
"""

DIVIDER = """
<div class="divider">
  <div class="num">{num}</div>
  <h1>{title}</h1>
  <div class="rule"></div>
  <div class="blurb">{blurb}</div>
</div>
"""

MD_EXT = ["tables", "fenced_code", "sane_lists"]


def to_html(md_text: str) -> str:
    md_text = md_text.replace("- [ ] ", "- ☐ ").replace("- [x] ", "- ☑ ")
    html = markdown.markdown(md_text, extensions=MD_EXT)
    return html.replace("<!--SHOT_TABLE-->", shots.table_html())


def divider(idx: str, title: str) -> str:
    return DIVIDER.format(num=idx, title=title.split(" — ")[1],
                          blurb=BLURBS[title]).replace(
        "<h1>", f'<h1>')


def esc(raw: str) -> str:
    return raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def paginate(src: pathlib.Path, dst: pathlib.Path) -> None:
    """Stamp page numbers and a running footer on every page but the cover."""
    reader = PdfReader(str(src))
    writer = PdfWriter()
    total = len(reader.pages)
    for i, page in enumerate(reader.pages):
        if i:
            buf = io.BytesIO()
            c = canvas.Canvas(buf, pagesize=A4)
            c.setFont("Helvetica", 7)
            c.setFillColorRGB(.42, .45, .50)
            c.drawString(48, 30, f"{AUTHOR}  ·  Creative Technologist Assignment")
            c.drawRightString(A4[0] - 48, 30, f"{i + 1} / {total}")
            c.setStrokeColorRGB(.89, .89, .91)
            c.setLineWidth(.5)
            c.line(48, 40, A4[0] - 48, 40)
            c.save()
            buf.seek(0)
            page.merge_page(PdfReader(buf).pages[0])
        writer.add_page(page)
    for rel in ATTACH:
        p = ROOT / rel
        writer.add_attachment(p.name, p.read_bytes())
    writer.add_metadata({
        "/Title": "Creative Technologist — Take-Home Assignment",
        "/Author": AUTHOR,
        "/Subject": "Dashverse / Frameo — Parts 1-3 with workflow files attached",
    })
    with open(dst, "wb") as fh:
        writer.write(fh)


def main() -> None:
    parts = [COVER, contents_page()]

    for n, (src, label) in enumerate(SECTIONS, 1):
        parts.append(divider(f"Part {n} of 3", label))
        parts.append(to_html((ROOT / src).read_text(encoding="utf-8")))

    for letter, (src, label) in zip("AB", APPENDICES):
        parts.append(divider(f"Appendix {letter}", label))
        parts.append("<pre><code>" + esc((ROOT / src).read_text(encoding="utf-8"))
                     + "</code></pre>")

    html = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
            '<title>Creative Technologist — Take-Home Assignment</title>'
            f'<style>{CSS}</style></head><body>{"".join(parts)}</body></html>')

    tmp_html = ROOT / "_master.html"
    tmp_html.write_text(html, encoding="utf-8")
    raw = ROOT / "_master_raw.pdf"
    subprocess.run([
        CHROME, "--headless", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={raw}", tmp_html.as_uri(),
    ], check=True, capture_output=True)

    paginate(raw, OUT)
    tmp_html.unlink(); raw.unlink()
    print(f"{OUT.name}: {len(PdfReader(str(OUT)).pages)} pages, "
          f"{OUT.stat().st_size // 1024} KB, {len(ATTACH)} files attached")


if __name__ == "__main__":
    main()
