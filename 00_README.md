# Creative Technologist — Take-Home Assignment

**Dashverse / Frameo**
Submitted by **Manish Das**

---

## What's in this folder

| # | File | Assignment part |
|---|---|---|
| 01 | `01_Production_Spec.pdf` | **Part 1** — production spec of the reference ad |
| 02 | [`Four Atoms` — watch the video](https://drive.google.com/file/d/12d0oep34td6RuWrTstSrxOsyWaN9Id_C/view) | **Part 2** — the video, made for an invented brand |
| 02 | `02_Video/deviation_notes.md` | Part 2 — what I changed from my own spec, and why |
| 03 | `03_SOP.pdf` | **Part 3** — handoff instructions |
| 03 | `workflow/ad-cloner.md` | Part 3 §3 — the workflow file the process runs on |
| 03 | `workflow/prompt_sheet.md` | Part 3 §4 — all prompts, copy-pasteable |
| — | `05_screen_recording.mp4` | Optional — one unedited run of the workflow |

**Start with `01_Production_Spec.pdf`, then watch the video, then read `03_SOP.pdf`.**

---

## Reference ad analysed in Part 1

Chicnutrix "Glow Advanced" — 45.6 s · 9:16 vertical · 17 shots
Public link: **[PASTE URL]**

---

## How the video in Part 2 was made

A pipeline that takes a competitor ad as input and rebuilds it for a different
brand with a consistent AI-generated presenter. Reference is analysed into a
hook / mid / CTA structure, the script is rewritten and normalised, an avatar is
locked to a reference sheet, the script is chunked into beats of ≤10 s, and each
beat is generated as talking-head video and assembled in Premiere Pro through an
MCP connection.

Image and video generation: **Higgsfield MCP**. Timeline assembly: **Premiere MCP**.
Orchestration: **Claude**, driven by `workflow/ad-cloner.md`.

Full detail in `03_SOP.pdf`.

---

## A note on Part 2 and the invented brand

The workflow is built to rebuild a competitor's *structure* — pacing, shot
rhythm, hook mechanics — not its identity. The video submitted for Part 2 uses
an invented brand, an invented product name and a generated presenter. No
element of the reference brand's identity appears in it: not the name, not the
logo, not the packaging, and not the original presenter's likeness.
