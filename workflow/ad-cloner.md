# Ad Cloner — End-to-End Workflow Runbook

> This is the workflow file referenced by `03_SOP.md` §3. It is executed by Claude with the
> Higgsfield MCP (image + video generation) and the Premiere MCP (timeline assembly) connected.
> Every video generation and image generation in this workflow bills to Higgsfield.

## Pipeline

```
[1] Competitor discovery      Ad Intelligence tool -> shortlist -> select reference MP4
         |
[2] Video analysis            cut detection -> shot list -> hook / mid / CTA split
         |                    B-roll count + timestamps + motion description
         |
[3] Script rewrite            mode A: clone + swap product/ingredients
         |                    mode B: manual lead, fitted to reference beat flow
         |
[4] Hinglish normalisation    Roman Hindi -> Devanagari (phonetics fix)
         |
[5] Avatar                    age/gender from [2] -> 2-3 prompt variants -> GPT-Image
         |                    OR import existing avatar
         |                    -> gender/grammar QC for Hindi verb agreement
         |
[6] Chunking                  hook = 1 chunk (8-10s, atomic)
         |                    CTA = standardised system prompt, handled at [9]
         |                    mid  = beats, max 10s, sentence- and Q&A-safe
         |
[7] A-roll generation         Higgsfield: talking-head video per beat
         |                    -> Premiere MCP: place sequentially on timeline
         |
[8] Hook rebuild              motion prompt from [2] + finalised avatar
         |                    -> Premiere MCP: place at head
         |
[9] CTA                       product image + standardised CTA system prompt
         |                    -> Premiere MCP: place at tail, 3-4s
         |
[10] B-roll                   regenerate inserts at positions from [2]
         |                    -> Premiere MCP: place, MANUAL trim by editor
         |
[11] Finish                   SFX from repo -> BGM from repo -> captions -> export
```

## Stage contracts

### [2] Video analysis — output schema
```yaml
runtime_s: float
fps: int
resolution: [w, h]
cuts: [float]              # scene-cut timestamps
sections:
  hook:  {in: 0.0, out: float}     # target 8-10s
  mid:   {in: float, out: float}
  cta:   {in: float, out: float}   # target 3-4s
shots:
  - {n: int, in: float, out: float, dur: float,
     type: a_roll|b_roll|cg|product|cta,
     framing: str, content: str, caption: str}
broll:
  count: int
  positions: [{in: float, out: float, subject: str}]
hook_motion: str           # feeds stage [8]
```

### [4] Hinglish normalisation — rule
Romanised Hindi tokens are rewritten to Devanagari; English tokens are left alone.
Rationale: TTS and lip-sync mispronounce Romanised Hindi (`kiya` reads as English).
```
"maine ye 6 hafte kiya"  ->  "मैंने ये 6 हफ़्ते किया"
"my skin barrier"        ->  "my skin barrier"      (unchanged)
```

### [5] Avatar — gender/grammar QC
If script language is Hindi or Hinglish, verb gender must agree with avatar gender.
```
avatar.gender == female  ->  करी थी / की थी      (करा था is an error)
avatar.gender == male    ->  करा था / किया था    (करी थी is an error)
```
Fails the stage and returns to [4] on mismatch.

### [6] Chunking — hard rules
1. Hook is one chunk. Never subdivided. Target 8-10s at natural pace.
2. Mid-section beat duration <= 10.0s.
3. A chunk never ends mid-sentence.
4. A question and its answer never split across chunks.
5. CTA is excluded — it is a generated card, not a spoken beat.

### [7] / [8] A-roll and hook — locked prompt segments
The **bold/locked** blocks in `prompt_sheet.md` are emitted verbatim on every generation.
They carry: framing, eye level, key-light direction, wall + plant shadow, wardrobe,
"no camera movement", "single continuous take". These are what make independently
generated clips cut together as one scene.

### [10] B-roll — known manual step
Generated inserts routinely overrun their slot. The editor trims each insert to the
gap; the A-roll is never stretched to fit. This is the one stage that is not automated
and is expected to need hands.

## Tooling

| Stage | Tool |
|---|---|
| 1 | Ad Intelligence tool (Meta Ad Library / Foreplay) |
| 2 | Claude — analysis from the MP4 |
| 3, 4, 6 | Claude |
| 5 | GPT-Image (avatar stills) |
| 7, 8, 9, 10 | **Higgsfield MCP** — all image and video generation |
| 7, 8, 9, 10 | **Premiere MCP** — timeline placement |
| 11 | Premiere Pro + in-house SFX/BGM repo |

## Credits
All image and video generation is performed through the **Higgsfield MCP**.
