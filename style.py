"""Stylesheet for the submission PDF."""

CSS = """
@page { size: A4; margin: 20mm 17mm 19mm; }
@page :first { margin: 0; }

:root {
  --ink:    #14161a;
  --body:   #2b2f36;
  --muted:  #6b7280;
  --hair:   #e4e4e8;
  --paper:  #ffffff;
  --tint:   #f6f6f8;
  --accent: #c2185b;
  --warm:   #b4531f;
}

* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

body {
  font-family: "Bitstream Charter", "Charter", Georgia, serif;
  font-size: 10.1pt; line-height: 1.54; color: var(--body);
  margin: 0; background: var(--paper);
}

/* ---------- display / structural type ---------- */
h1, h2, h3, h4, th, .tag, .kicker, .num, .legend, .meta-k, .lede {
  font-family: "DejaVu Sans", "Liberation Sans", Arial, sans-serif;
}

h1 { font-size: 19pt; line-height: 1.18; letter-spacing: -.45pt;
     color: var(--ink); margin: 0 0 6pt; font-weight: 700; }
h2 { font-size: 12.5pt; letter-spacing: -.1pt; color: var(--ink);
     margin: 17pt 0 8pt; padding-bottom: 5pt; font-weight: 700;
     border-bottom: 2px solid var(--ink); page-break-after: avoid; }
h3 { font-size: 10.5pt; color: var(--ink); margin: 13pt 0 5pt;
     font-weight: 700; page-break-after: avoid; }
h4 { font-size: 9.6pt; color: var(--ink); margin: 12pt 0 4pt;
     font-weight: 700; page-break-after: avoid; }

p { margin: 0 0 8pt; orphans: 2; widows: 2; }
strong { color: var(--ink); font-weight: 700; }
em { font-style: italic; }
hr { border: 0; border-top: 1px solid var(--hair); margin: 15pt 0; }
a { color: var(--accent); text-decoration: none; border-bottom: .5pt solid var(--accent); }

ul, ol { padding-left: 15pt; margin: 7pt 0; }
li { margin: 3pt 0; orphans: 2; widows: 2; }

code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.2pt;
       background: var(--tint); color: var(--ink);
       padding: 1pt 3.5pt; border-radius: 2.5px; }
pre { background: var(--tint); border: 1px solid var(--hair);
      border-left: 2.5pt solid var(--ink); padding: 9pt 11pt; border-radius: 3px;
      font-size: 7.9pt; line-height: 1.5; white-space: pre-wrap;
      page-break-inside: avoid; margin: 9pt 0; }
pre code { background: none; padding: 0; font-size: inherit; }

blockquote { border-left: 2.5pt solid var(--accent); margin: 10pt 0;
             padding: 3pt 0 3pt 12pt; color: var(--muted);
             font-size: 9.4pt; font-style: italic; }

/* ---------- cover ---------- */
.cover { height: 297mm; background: var(--ink); color: #fff;
         padding: 30mm 20mm 0; page-break-after: always;
         display: flex; flex-direction: column; }
.cover .kicker { font-size: 8.5pt; letter-spacing: 3.2pt; text-transform: uppercase;
                 color: rgba(255,255,255,.55); margin-bottom: 16pt; }
.cover h1 { font-size: 40pt; line-height: 1.02; letter-spacing: -1.6pt;
            color: #fff; margin: 0 0 12pt; }
.cover h1 .thin { font-weight: 300; color: rgba(255,255,255,.62); display: block; }
.cover .sub { font-family: "DejaVu Sans", sans-serif; font-size: 11pt;
              color: rgba(255,255,255,.75); letter-spacing: .3pt; }
.cover .accentbar { width: 46mm; height: 3pt; background: var(--accent); margin: 20pt 0; }
.cover .meta { font-size: 9.2pt; color: rgba(255,255,255,.78); line-height: 1.95; }
.cover .meta-k { display: inline-block; width: 30mm; font-size: 7.8pt;
                 letter-spacing: 1.4pt; text-transform: uppercase;
                 color: rgba(255,255,255,.42); }
.cover .meta a { color: #fff; border-bottom-color: rgba(255,255,255,.4); }
.cover .strip { margin: auto -20mm 0; display: block;
                height: 38mm; overflow: hidden; }
.cover .strip img { width: 100%; display: block; opacity: .92; margin-top: -5mm; }

/* ---------- section dividers ---------- */
.divider { page-break-before: always; page-break-after: always;
           padding-top: 88mm; }
.divider .num { font-size: 8.5pt; letter-spacing: 3.2pt; text-transform: uppercase;
                color: var(--accent); font-weight: 700; }
.divider h1 { font-size: 30pt; letter-spacing: -1pt; margin: 10pt 0 0;
              line-height: 1.08; }
.divider .rule { width: 26mm; height: 2.5pt; background: var(--ink); margin: 16pt 0; }
.divider .blurb { font-size: 11pt; color: var(--muted); max-width: 108mm;
                  line-height: 1.6; font-style: italic; }

/* ---------- lede paragraph ---------- */
.lede { font-size: 10.6pt; color: var(--ink); line-height: 1.55;
        border-left: 2.5pt solid var(--accent); padding-left: 11pt; margin: 0 0 14pt; }

/* ---------- tables ---------- */
table { border-collapse: collapse; width: 100%; margin: 10pt 0; font-size: 8.5pt;
        font-family: "DejaVu Sans", sans-serif; }
th { background: var(--ink); color: #fff; text-align: left; font-weight: 700;
     font-size: 7.6pt; letter-spacing: .6pt; text-transform: uppercase;
     padding: 5.5pt 7pt; }
td { padding: 5.5pt 7pt; vertical-align: top; border-bottom: 1px solid var(--hair); }
table.shots td { padding: 3pt 5.5pt; }
tbody tr:nth-child(even) { background: #fafafb; }
tr { page-break-inside: avoid; }

/* shot table */
table.shots { font-size: 7.5pt; }
table.shots td.n { color: var(--muted); font-weight: 700; width: 5mm;
                   text-align: right; padding-right: 2pt; }
table.shots td.thumb { width: 9.5mm; padding: 3pt 5pt 3pt 4pt; }
table.shots td.thumb img { width: 7.5mm; display: block; border-radius: 1.5px;
                           border: .5pt solid var(--hair); }
table.shots td.tc { width: 21mm; font-family: "DejaVu Sans Mono", monospace;
                    font-size: 7.2pt; color: var(--ink); white-space: nowrap; }
table.shots td.tc .dash { color: var(--muted); padding: 0 .5pt; }
table.shots td.tc .dur { display: block; color: var(--muted); font-size: 6.8pt; }
table.shots td.frame { width: 46mm; }
table.shots td.act { color: var(--body); }
table.shots tr.hook   td.n { box-shadow: inset 2.5pt 0 0 var(--accent); }
table.shots tr.mid    td.n { box-shadow: inset 2.5pt 0 0 var(--hair); }
table.shots tr.cta    td.n { box-shadow: inset 2.5pt 0 0 var(--warm); }

.tag { display: inline-block; font-size: 6.6pt; letter-spacing: .5pt;
       text-transform: uppercase; font-weight: 700; padding: 1.5pt 4pt;
       border-radius: 2px; white-space: nowrap; }
.t-a   { background: #14161a; color: #fff; }
.t-b   { background: #e8e8ec; color: #40454e; }
.t-cg  { background: #ded6ea; color: #4b3a63; }
.t-p   { background: #fbe3ec; color: #8e1246; }
.t-cta { background: #b4531f; color: #fff; }

.legend { font-size: 7.4pt; color: var(--muted); margin-top: 5pt; }
.legend .sw { display: inline-block; width: 8pt; height: 3pt; vertical-align: middle;
              margin-right: 2pt; }
.legend .sw.hook { background: var(--accent); }
.legend .sw.mid  { background: var(--hair); }
.legend .sw.cta  { background: var(--warm); }

/* ---------- callouts ---------- */
.note { background: var(--tint); border-left: 2.5pt solid var(--ink);
        padding: 10pt 12pt; font-size: 9.2pt; margin: 12pt 0;
        page-break-inside: avoid; }
.note strong:first-child { display: block; margin-bottom: 3pt; }

/* ---------- video cards ---------- */
.videocard { border: 1px solid var(--hair); border-radius: 4px; overflow: hidden;
             margin: 12pt 0 16pt; page-break-inside: avoid; }
.videocard .vstrip { display: block; width: 100%; }
.videocard .vstrip img { width: 100%; display: block; }
.videocard .vmeta { padding: 9pt 12pt; background: var(--tint); }
.videocard .vtitle { font-family: "DejaVu Sans", sans-serif; font-weight: 700;
                     font-size: 10pt; color: var(--ink); margin: 0 0 2pt; }
.videocard .vsub { font-size: 8.4pt; color: var(--muted); margin: 0 0 6pt;
                   font-family: "DejaVu Sans", sans-serif; }
.videocard .vlink { font-family: "DejaVu Sans", sans-serif; font-size: 8.6pt;
                    font-weight: 700; }
.videocard .vlink a { color: var(--accent); }
.videocard .vph.packshot { background: #fff; border-bottom: 1px solid var(--hair); text-align: center; padding: 10pt; }
.videocard .vph.packshot img { width: 30mm; }
.videocard.placeholder .vph { background: var(--tint); border-bottom: 1px solid var(--hair);
       padding: 22pt 12pt; text-align: center; color: var(--muted);
       font-family: "DejaVu Sans", sans-serif; font-size: 8.4pt; }

/* ---------- product card ---------- */
.prodcard { display: flex; gap: 14pt; align-items: flex-start;
            border: 1px solid var(--hair); border-radius: 4px; padding: 12pt;
            margin: 12pt 0 16pt; page-break-inside: avoid; background: var(--tint); }
.prodcard img { width: 34mm; flex: none; border-radius: 3px; background: #fff; }
.prodcard .pbody { font-size: 9.2pt; }
.prodcard .ptitle { font-family: "DejaVu Sans", sans-serif; font-weight: 700;
                    font-size: 10pt; color: var(--ink); margin: 0 0 2pt; }
.prodcard .psub { font-family: "DejaVu Sans", sans-serif; font-size: 8.4pt;
                  color: var(--muted); margin: 0 0 7pt; }
.prodcard .pnote { font-size: 8.2pt; color: var(--muted); font-style: italic;
                   margin: 6pt 0 0; }

/* ---------- contents ---------- */
.toc { margin: 4pt 0 0; }
.toc-row { display: flex; align-items: baseline; gap: 8pt; padding: 7pt 0;
           border-bottom: 1px solid var(--hair); page-break-inside: avoid; }
.toc-row .tnum { font-family: "DejaVu Sans", sans-serif; font-size: 7.6pt;
                 font-weight: 700; letter-spacing: 1.2pt; color: var(--accent);
                 width: 24mm; flex: none; text-transform: uppercase; }
.toc-row .tbody .tt { font-family: "DejaVu Sans", sans-serif; font-weight: 700;
                      font-size: 9.6pt; color: var(--ink); }
.toc-row .tbody .td { font-size: 9pt; color: var(--muted); }
"""
