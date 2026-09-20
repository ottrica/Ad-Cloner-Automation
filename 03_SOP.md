# SOP — Producing the Next Video in This Format

**Audience:** an operator on the client's team who is smart but is *not* an AI-video expert.
**Goal:** you can produce a complete, on-format video without messaging anyone.
**Workflow file attached:** `workflow/ad-cloner.md` (the end-to-end runbook Claude executes) and `workflow/prompt_sheet.md` (all prompts, copy-pasteable).

---

## 1. Format overview

This format is a **45–60 second vertical talking-head ad** for a consumer product. One presenter — an AI-generated character we call the *avatar* — speaks to camera for the entire video from a single fixed medium shot in a single room. Over her voice, short inserts cut in: close-ups of the problem, the product, the ritual of using it, and a before/after. She is the only person who ever appears.

Every correct video in this format has the same three-part spine:

- **Hook — 8 to 10 seconds.** One unbroken shot of the avatar. No cuts inside it. This is where the video either keeps the viewer or loses them.
- **Mid-section — the bulk of the runtime.** Broken into *beats* of **no more than 10 seconds each**, alternating avatar shots with inserts.
- **CTA — 3 to 4 seconds.** A product/logo card. The avatar does not appear.

A video is **correct** when: the avatar's face is recognisably the same person in every shot she appears in; the room, wardrobe and lighting never change within a video; captions are on every frame; and the hook and CTA fall inside their time windows. A rough-looking video that holds all of these is correct. A beautiful one where the face drifts between shots is not.

<!--FLOWCHART-->

---

## 2. Before you start: inputs checklist

Do not begin until every box is ticked. Missing item 3 or 4 will cost you the most rework.

**Creative inputs**
- [ ] **Reference ad** — the competitor video you are rebuilding against, downloaded as MP4. Sourced from the Ad Intelligence tool (Meta Ad Library, Foreplay, or equivalent): search the competitor, filter to videos running longest, download one.
- [ ] **Script** — either (a) the reference script with product name and ingredients swapped, or (b) a new script you wrote that follows the reference's beat flow. Decide which before you start.
- [ ] **Product images** — clean pack shot on transparent or plain background, minimum 1000 px on the long edge. Needed for the CTA card.
- [ ] **Brand assets** — logo (PNG, transparent), brand colours (hex codes), and the approved tagline.
- [ ] **Claim clearances** — written confirmation of any efficacy or time-bound claim in the script ("in 6 weeks"). Do not generate a video around an uncleared claim.

**Character inputs**
- [ ] **Avatar reference set** — either the locked reference sheet from a previous video (preferred — reuse guarantees consistency), or nothing, if you are creating a new avatar in Step 2.

**Tools and access**
- [ ] **Claude** with the workflow file `workflow/ad-cloner.md` loaded
- [ ] **Higgsfield MCP** connected — handles all image and video generation. Confirm credits are available before starting; a mid-run credit failure loses the generation.
- [ ] **GPT-Image** access — used for avatar reference generation
- [ ] **Adobe Premiere Pro** with the **Premiere MCP** connected, and a project open
- [ ] **SFX + BGM repo** installed — our curated Premiere library of transitions, whooshes and beds for this format

---

## 3. Step-by-step run instructions

### Stage A — Analyse the reference (≈10 min)

1. **Load the reference MP4** into the workflow and run the analysis step. It returns: total runtime, every scene-cut timestamp, and the shot list split into hook / mid / CTA.
2. **Read the B-roll report.** It tells you how many inserts the reference uses and where each one falls. You will rebuild against these positions, so check the numbers look sane before continuing — if it reports 2 shots in a 45-second ad, the cut detection failed; re-run it.
3. **Confirm the three-part split.** Hook should land at 8–10 s and CTA at 3–4 s. If the reference doesn't split that way, it is a poor fit for this format — pick a different reference.

### Stage B — Script (≈15 min)

4. **Choose your script mode:**
   - **Clone mode** — the workflow takes the reference script and replaces only the product name and ingredient names. Fastest, and the beat timing is guaranteed to fit.
   - **Manual lead mode** — you supply your own opening, and the workflow fits it to the reference's flow. Use this when the client wants a different angle.
5. **Run Hinglish normalisation.** If the script mixes Hindi and English, this step rewrites Hindi words from Roman letters into Devanagari (`kiya` → `किया`). **Do not skip this.** Voice generation mispronounces Romanised Hindi; Devanagari fixes the phonetics.
6. **Read the normalised script aloud against a timer.** Hook must land in 8–10 seconds at natural speaking pace. If it runs long, cut words now — not after you have generated video.

### Stage C — Avatar (≈20 min)

7. **Generate or import the avatar.**
   - *Generate:* the workflow reads the age and gender of the presenter in the reference and returns 2–3 avatar prompt variants. Generate each with GPT-Image and pick one.
   - *Import:* supply your own character images instead. **Always prefer this if a previous video in the series exists** — reusing the locked reference set is the single most reliable way to keep the face consistent.
8. **Build the reference sheet.** Save 3–4 images of your chosen avatar: front, three-quarter left, three-quarter right, and one at the framing you'll shoot. This sheet is the ground truth for every quality check that follows. Save it to the project folder.
9. **Run the gender/grammar QC.** If the script is in Hindi or Hinglish, the workflow checks that verb gender agrees with the avatar's gender — `करा था` for a male presenter, `करी थी` for a female one. Mismatched gender agreement is the most common error in Hindi scripts and is immediately obvious to a native speaker.

### Stage D — Chunk the script (≈10 min)

10. **Split the script into generation chunks.** The workflow does this automatically under three hard rules:
    - **Hook** = one chunk, 8–10 s, never subdivided.
    - **CTA** = handled separately in Stage G, not chunked here.
    - **Mid-section** = beats of **maximum 10 seconds**. A question and its answer must stay in the same chunk. Never end a chunk mid-sentence.
11. **Eyeball the chunk list.** If any beat exceeds 10 s or ends on a comma, fix it by hand before generating. Fixing it here costs a minute; fixing it after generation costs a full regeneration.

### Stage E — Generate and place the A-roll (≈45 min, mostly waiting)

12. **Generate every mid-section beat** as an end-to-end talking-head video via Higgsfield MCP, using the avatar reference sheet plus motion direction pulled from the reference video's analysis. All A-roll is talking head — one framing, one room.
13. **Quality-check each clip as it lands** against the checks in Section 5. Reject and regenerate before moving on. Do not batch the checking to the end.
14. **Push the approved A-roll to Premiere.** The Premiere MCP lays the clips onto the timeline in script order. You should now have a complete, gap-free spoken track with no inserts yet.

### Stage F — Rebuild the hook (≈20 min)

15. **Generate the hook separately, with motion.** The hook is not a static talking head — in most references it carries a distinct camera angle or a physical action (a turn, a gesture, a reach for the product) that is doing the stopping. The workflow extracts that motion from the reference analysis and writes a motion prompt to recreate it with *your* finalised avatar.
16. **Generate 2–3 hook variants and pick the strongest.** This is the highest-leverage 10 seconds in the video; it is worth the extra generations.
17. **Place the hook at the head of the timeline** via the Premiere MCP.

### Stage G — CTA (≈10 min)

18. **Supply the product image.** The workflow applies a standardised CTA system prompt that composites your product into the locked CTA layout.
19. **Place it at the tail of the timeline, trimmed to 3–4 seconds.** Not 2, not 6.

### Stage H — B-roll and finish (≈45 min, manual)

20. **Generate the inserts** the reference used, at the positions the analysis reported.
21. **Place them on the timeline — this step is manual.** Generated B-roll frequently runs longer than the gap it needs to fill. Trim each insert to fit; do not stretch the A-roll to accommodate it. **This is editor's work and is expected to need hands.**
22. **Add SFX from the repo.** Transitions on every cut into and out of a B-roll insert. Keep it light.
23. **Add BGM from the repo.** Pick one bed for the whole video. Duck it under the voice. You may also import your own track if nothing in the repo fits.
24. **Add captions to every frame.** Sound-off is the default viewing condition; a video without captions is not finished.
25. **Export** — H.264, 9:16, 1080×1920, 30 fps.

---

## 4. Prompt templates

Copy-pasteable versions of all of these are in `workflow/prompt_sheet.md`.

> **How to read these:** `[SQUARE BRACKETS]` = you change this for every video. **Bold text** = locked, never edit — this is what keeps the character and style consistent.

### 4.1 Avatar reference generation

```
A [AGE RANGE, e.g. 24-28] year old [GENDER] [ETHNICITY] person,
[HAIR DESCRIPTION], [WARDROBE: single saturated colour, no pattern],
**photographed at eye level, medium shot from the waist up,
soft warm directional key light from frame left,
plain warm beige textured wall background with a soft plant-frond shadow,
natural skin texture with visible pores, no retouching,
shallow depth of field, 9:16 vertical, photorealistic, shot on 35mm**
```
*Locked because:* the framing, light direction, wall and shadow are the continuity anchors. Change any of them and cutbacks stop matching.

### 4.2 A-roll beat (talking head)

```
Reference image: [ATTACH AVATAR REFERENCE SHEET]
The character speaks this line to camera: "[SCRIPT LINE FOR THIS BEAT]"
Expression: [NEUTRAL / CONCERNED / REASSURING / AMUSED]
**Same character as reference image, identical face, identical hair,
identical wardrobe. Static camera, eye level, medium shot waist up.
Warm beige wall with plant shadow, unchanged. Soft key from frame left.
Natural conversational hand gestures. No camera movement. No zoom.
No cuts. Single continuous take.**
```
*Locked because:* "no camera movement, no cuts" is what lets six separately generated clips read as one conversation.

### 4.3 Hook (motion)

```
Reference image: [ATTACH AVATAR REFERENCE SHEET]
The character [MOTION EXTRACTED FROM REFERENCE — e.g. "turns from
three-quarter to face camera and raises the product into frame"]
while saying: "[HOOK LINE, 8-10 SECONDS]"
**Same character as reference image, identical face, hair and wardrobe.
Same warm beige room, same plant shadow, same soft key from frame left.
One continuous take, no cuts. Motion completes within the first
3 seconds, then settles to a stable medium shot.**
```
*Locked because:* the motion must resolve early — a hook still moving at second 7 has no stable frame to cut out of.

### 4.4 B-roll insert

```
[SUBJECT: e.g. "extreme close-up of skin texture on a cheek,
visible pigmentation"]
**Macro detail shot, no face visible above the nose, warm natural light
matching a beige interior, shallow depth of field, photorealistic,
natural unretouched skin, 9:16 vertical. No text, no logos, no hands
unless specified.**
```
*Locked because:* inserts must colour-match the A-roll room or the cut announces itself. Keeping faces out avoids a second, inconsistent face entering the video.

### 4.5 CTA card

```
Product image: [ATTACH PRODUCT PNG]
Brand logo: [ATTACH LOGO PNG]
Tagline: "[TAGLINE]"
**Product centred on a plain warm cream background, soft even studio
light, subtle contact shadow beneath the product, logo lockup centred
above or below the product, generous margins, no clutter, no people,
9:16 vertical.**
```

---

## 5. Quality checks

Run the check for a stage **before** moving to the next one. Every check below is something you can verify by looking — no expertise required.

### After avatar generation
- [ ] **Open the reference sheet images side by side.** If you would not say these are photos of the same person on different days, regenerate.
- [ ] Hands visible? Count the fingers. Five per hand, or regenerate.
- [ ] Eyes both pointing the same direction.

### After each A-roll clip
- [ ] **Pause on the first frame and the last frame. Put each next to the reference sheet. If the face doesn't match, reject and regenerate** — do not tell yourself it will be fine at speed. It will not.
- [ ] **Wall and shadow in the same position** as in the previous approved clip.
- [ ] **Same wardrobe** — check the neckline and any jewellery specifically; these drift first.
- [ ] Mouth movement matches the words; no mouth still moving after the line ends.
- [ ] Camera has not drifted, zoomed or wobbled.
- [ ] No extra limb, no hand passing through the body.

### After the hook
- [ ] Time it. **8 to 10 seconds. Outside that range, regenerate.**
- [ ] The motion finishes in the first 3 seconds and the frame is stable after it.
- [ ] Same face as the reference sheet — check this again even though you checked the A-roll.

### After B-roll generation
- [ ] **Does the light come from the same side as in the A-roll?** If the A-roll is lit from the left and the insert is lit from the right, reject.
- [ ] Warm tone matches — hold it next to an A-roll frame. A cool-toned insert breaks the room.
- [ ] No unintended faces, text, logos or watermarks.

### After the CTA card
- [ ] Product is the correct product, right way up, label readable.
- [ ] Logo is the supplied file, not a regenerated imitation. **A regenerated logo is always wrong — replace it with the real PNG.**
- [ ] Card duration is 3–4 seconds.

### Before export
- [ ] **Scrub the whole video at normal speed with sound off.** Does it make sense from captions alone? If not, fix the captions.
- [ ] **Scrub it again watching only the face.** Any shot where she becomes a different person, replace that shot.
- [ ] No beat longer than 10 seconds.
- [ ] Audio has no gaps or overlaps between beats.
- [ ] BGM sits under the voice, never over it.
- [ ] Total runtime inside the target for the placement.

---

## 6. Stopping and resuming

You can stop after any stage. Before you walk away, save these — this is the whole list:

**Always save**
- The **Premiere project file** (`.prproj`) — save, don't just leave it open
- The **avatar reference sheet** images, in the project folder, named `avatar_ref_01.png` onwards
- The **seed or generation ID** of every approved clip, in a plain text file next to the project. *Without seeds you cannot reproduce a look, and a re-generation will give you a different face.*
- The **normalised script** with the chunk splits marked
- The **analysis output** from Stage A (the shot list and B-roll timings)

**Folder layout to save into**
```
project_name/
├── project_name.prproj
├── script_normalised.md
├── analysis_output.md
├── seeds.txt
├── avatar_ref/
├── approved_clips/
└── rejected/          ← keep these; useful when comparing drift
```

**To resume:**
1. Open the `.prproj`. The timeline holds everything already placed.
2. Open `seeds.txt` and `script_normalised.md` side by side — together they tell you the last chunk that was approved.
3. Restart at the **first chunk with no approved clip**. Do not regenerate approved clips; their seeds are locked and a regeneration will drift the face.
4. Before generating anything new, re-open the avatar reference sheet. Every new clip is checked against that sheet, not against the last clip you made.

---

## 7. When to call for help

Stop and escalate. Do not push through any of these.

| Situation | Why you must escalate |
|---|---|
| **The client wants a different character.** | The avatar is a locked setting the whole series inherits. A new character means a new reference sheet and a re-run of every A-roll clip — it is a new build, not an edit. |
| **The face will not stay consistent after 3 regeneration attempts.** | Something upstream is wrong — usually a weak reference sheet. More attempts will not fix it and will burn credits. |
| **The script contains a health, efficacy or time-bound claim that isn't on the cleared list.** | Regulatory risk. Never generate around an uncleared claim, even as a draft. |
| **The client asks to change the hook length, the CTA length, or the 10-second beat rule.** | These define the format. Changing them is a format decision, not a production one. |
| **The reference ad doesn't split into hook / mid / CTA.** | It's the wrong reference for this system. Choosing a replacement is a creative call. |
| **Higgsfield or the Premiere MCP disconnects mid-run, or credits run out.** | Save the project and the seeds immediately, then escalate. Do not start re-generating to "catch up" — you will lose the seeds that keep the face consistent. |
| **The client supplies a real person's likeness to use as the avatar.** | Rights and consent issue. Always escalate. |
| **The brand logo only exists as a low-res image.** | A regenerated or upscaled logo is never acceptable on a CTA card. We need the vector from the client. |
