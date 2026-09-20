"""Shot data for the reference ad, measured by scene-cut detection."""

SHOTS = [
    (1,  0.00,  6.67, "A-roll",  "MS presenter, pink dress, beige wall, white facial roller", "Full hook line delivered to camera; gestures with roller"),
    (2,  6.67,  8.10, "B-roll",  "ECU cheek, visible pigmentation", "&ldquo;a cream for pigmentation&rdquo;"),
    (3,  8.10,  9.77, "B-roll",  "ECU neck / jawline", "&ldquo;a serum for hydration&rdquo;"),
    (4,  9.77,  9.90, "A-roll",  "MS presenter", "Single-frame flash cutback &mdash; rhythmic punctuation"),
    (5,  9.90, 10.83, "B-roll",  "ECU under-eye, finger touching skin", "&ldquo;a treatment for breakouts&rdquo;"),
    (6, 10.83, 12.43, "B-roll",  "CU green clay mask, gua-sha tool", "&ldquo;a mask for dullness&rdquo;"),
    (7, 12.43, 15.77, "A-roll",  "MS presenter", "&ldquo;and somehow&hellip;&rdquo; &mdash; pace resets, turn into the pitch"),
    (8, 15.77, 18.80, "Product", "3 tubes on plinth, brand lockup", "Product reveal, name on screen"),
    (9, 18.80, 23.07, "B-roll",  "Effervescent tablet dropping into water glass", "Hero ingredient named on screen"),
    (10,23.07, 25.30, "B-roll",  "CU presenter drinking through straw", "&ldquo;antioxidant&rdquo; &mdash; shows the ritual"),
    (11,25.30, 28.90, "A-roll",  "MS presenter", "&ldquo;to slow signs of&hellip;&rdquo;"),
    (12,28.90, 33.57, "CG",      "Liposome spheres, iridescent", "Delivery-technology claim"),
    (13,33.57, 36.83, "CG",      "Bubbles inside membrane", "&ldquo;for faster absorption and impact&rdquo;"),
    (14,36.83, 39.17, "A-roll",  "MS presenter", "&ldquo;11 more skin-lovin&rsquo; ingredients&rdquo;"),
    (15,39.17, 40.83, "B-roll",  "Before/after split, same face", "&ldquo;Get visible results&rdquo;"),
    (16,40.83, 42.23, "A-roll",  "MS presenter", "&ldquo;In 6 weeks* only&rdquo;"),
    (17,42.23, 45.59, "CTA",     "Logo end card on cream", "Brand lockup + tagline"),
]

SECTION_OF = {  # which part of the three-act spine each shot belongs to
    **{n: "hook" for n in (1, 2)},
    **{n: "mid" for n in range(3, 17)},
    17: "cta",
}

TYPE_CLASS = {"A-roll": "t-a", "B-roll": "t-b", "CG": "t-cg",
              "Product": "t-p", "CTA": "t-cta"}


def table_html() -> str:
    rows = []
    for n, tin, tout, kind, framing, action in SHOTS:
        rows.append(f"""
        <tr class="shot {SECTION_OF[n]}">
          <td class="n">{n}</td>
          <td class="thumb"><img src="assets/shot_{n:02d}.jpg" alt=""></td>
          <td class="tc">{tin:05.2f}<span class="dash">&ndash;</span>{tout:05.2f}
              <span class="dur">{tout - tin:.2f}s</span></td>
          <td><span class="tag {TYPE_CLASS[kind]}">{kind}</span></td>
          <td class="frame">{framing}</td>
          <td class="act">{action}</td>
        </tr>""")
    return f"""
    <table class="shots">
      <thead><tr>
        <th>#</th><th>Frame</th><th>In &ndash; Out</th><th>Type</th>
        <th>What&rsquo;s in frame</th><th>What happens</th>
      </tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table>
    <p class="legend">
      <span class="sw hook"></span> Hook &nbsp;
      <span class="sw mid"></span> Mid-section &nbsp;
      <span class="sw cta"></span> CTA
      &nbsp;&nbsp;&middot;&nbsp;&nbsp; Timecodes measured by scene-cut detection at
      threshold&nbsp;0.25 on the source file.
    </p>"""
