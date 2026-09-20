"""Generate the workflow flowchart as an SVG.

Vector, so it stays sharp at print resolution. Tool names are set as text
labels rather than vendor logo artwork.
"""
import pathlib

INK, MUTED, HAIR, TINT = "#14161a", "#6b7280", "#e4e4e8", "#f6f6f8"
PHASES = [
    ("Analyse",            "#c2185b", "What is the reference actually doing?"),
    ("Script & character", "#7b3fa0", "Lock everything that must stay identical"),
    ("Generate",           "#0f766e", "Make the shots, one beat at a time"),
    ("Assemble",           "#b4531f", "Cut it together and ship"),
]

# (phase index, title, subtitle, tool, flag)
NODES = [
    (0, "Select the competitor ad",
        "Search the brand, filter to long-running ads, download the MP4",
        "Ad Intelligence", None),
    (0, "Analyse the video",
        "Cut detection → shot list, hook / mid / CTA split, B-roll map, hook motion",
        "Claude", None),
    (1, "Rewrite the script",
        "Clone-and-swap the product and ingredients, or write a new lead to the same beats",
        "Claude", None),
    (1, "Normalise Hinglish",
        "Romanised Hindi → Devanagari, so voice generation says it correctly",
        "Claude", None),
    (1, "Lock the avatar",
        "Age and gender read from the reference → reference sheet the whole video inherits",
        "GPT-Image", "gate"),
    (1, "Chunk into beats",
        "Hook stays whole · every other beat ≤ 10 s · never split a sentence or a Q&A",
        "Claude", None),
    (2, "Generate the A-roll",
        "One talking-head clip per beat, checked against the reference sheet",
        "Higgsfield MCP", "gate"),
    (2, "Rebuild the hook",
        "Motion prompt from the reference, performed by the locked avatar",
        "Higgsfield MCP", "gate"),
    (2, "Composite the CTA card",
        "Product image dropped into the standardised 3–4 s end card",
        "Higgsfield MCP", None),
    (2, "Generate the B-roll",
        "Inserts rebuilt at the positions the analysis reported",
        "Higgsfield MCP", None),
    (3, "Lay the timeline",
        "Clips placed in script order, hook at the head, CTA at the tail",
        "Premiere MCP", None),
    (3, "Trim the B-roll to fit",
        "Inserts overrun their slots — the editor trims by hand, A-roll is never stretched",
        "Editor", "manual"),
    (3, "Sound, captions, export",
        "SFX and BGM from the in-house repo · captions on every frame · H.264 9:16",
        "Premiere Pro", None),
]

W = 1020
PAD_TOP, NODE_H, NODE_GAP = 8, 62, 13
PHASE_HEAD, PHASE_GAP = 40, 12
SPINE_X, BOX_X = 30, 66


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build() -> str:
    out, y = [], PAD_TOP
    spine_pts, last_phase = [], None

    for pi, title, sub, tool, flag in NODES:
        if pi != last_phase:
            if last_phase is not None:
                y += PHASE_GAP
            name, colour, tag = PHASES[pi]
            out.append(
                f'<text x="{BOX_X}" y="{y + 20}" class="phname" fill="{colour}">'
                f'{esc(name.upper())}</text>'
                f'<text x="{BOX_X + 20 + len(name) * 12.7}" y="{y + 20}" class="phtag">'
                f'{esc(tag)}</text>'
                f'<line x1="{BOX_X}" y1="{y + 29}" x2="{W}" y2="{y + 29}" '
                f'stroke="{colour}" stroke-width="1.6" opacity=".35"/>')
            y += PHASE_HEAD
            last_phase = pi

        colour = PHASES[pi][1]
        cy = y + NODE_H / 2
        spine_pts.append((cy, colour))

        fill, stroke = ("#fff8f2", "#b4531f") if flag == "manual" else ("#ffffff", HAIR)
        out.append(
            f'<rect x="{BOX_X}" y="{y}" width="{W - BOX_X}" height="{NODE_H}" rx="6" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>'
            f'<rect x="{BOX_X}" y="{y}" width="4.5" height="{NODE_H}" rx="2.2" fill="{colour}"/>')

        out.append(f'<text x="{BOX_X + 20}" y="{y + 25}" class="ntitle">{esc(title)}</text>')
        out.append(f'<text x="{BOX_X + 20}" y="{y + 45}" class="nsub">{esc(sub)}</text>')

        # tool chip, right-aligned inside the node
        cw = len(tool) * 7.4 + 22
        out.append(
            f'<rect x="{W - cw - 14}" y="{y + 13}" width="{cw}" height="22" rx="11" '
            f'fill="{TINT}" stroke="{HAIR}" stroke-width="1"/>'
            f'<text x="{W - cw / 2 - 14}" y="{y + 28}" class="chip">{esc(tool)}</text>')

        if flag == "manual":
            out.append(f'<text x="{W - cw - 78}" y="{y + 28}" class="flag" '
                       f'fill="#b4531f">MANUAL</text>')
        if flag == "gate":
            out.append(f'<text x="{W - cw - 66}" y="{y + 28}" class="flag" '
                       f'fill="{MUTED}">QC GATE</text>')

        y += NODE_H + NODE_GAP

    total_h = y - NODE_GAP + 10

    # spine + numbered nodes
    spine = [f'<line x1="{SPINE_X}" y1="{spine_pts[0][0]}" x2="{SPINE_X}" '
             f'y2="{spine_pts[-1][0]}" stroke="{HAIR}" stroke-width="2.4"/>']
    for i, (cy, colour) in enumerate(spine_pts, 1):
        spine.append(
            f'<circle cx="{SPINE_X}" cy="{cy}" r="13.5" fill="#fff" '
            f'stroke="{colour}" stroke-width="2.2"/>'
            f'<text x="{SPINE_X}" y="{cy + 4.6}" class="nnum" fill="{colour}">{i}</text>')

    css = f"""
    text {{ font-family: 'DejaVu Sans', sans-serif; }}
    .phname {{ font-size: 15px; font-weight: 700; letter-spacing: 2.4px; }}
    .phtag  {{ font-size: 13.5px; fill: {MUTED}; font-style: italic; }}
    .ntitle {{ font-size: 17px; font-weight: 700; fill: {INK}; }}
    .nsub   {{ font-size: 13.5px; fill: {MUTED}; }}
    .chip   {{ font-size: 12.5px; font-weight: 700; fill: {INK};
               text-anchor: middle; letter-spacing: .3px; }}
    .nnum   {{ font-size: 14px; font-weight: 700; text-anchor: middle; }}
    .flag   {{ font-size: 10.5px; font-weight: 700; letter-spacing: 1.1px;
               text-anchor: end; }}
    """
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {total_h:.0f}" '
            f'width="{W}" height="{total_h:.0f}"><style>{css}</style>'
            f'{"".join(spine)}{"".join(out)}</svg>')


if __name__ == "__main__":
    path = pathlib.Path(__file__).parent / "assets" / "workflow_flowchart.svg"
    path.write_text(build(), encoding="utf-8")
    print(f"{path.name}: {path.stat().st_size // 1024} KB, {len(NODES)} nodes")
