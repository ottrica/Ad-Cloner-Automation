# Prompt Sheet — copy-pasteable

`[SQUARE BRACKETS]` = change for every video.
Everything **not** in brackets is locked — do not edit, it is what keeps the character
and the room consistent across separately generated clips.

---

## 1. Avatar reference generation  (GPT-Image)

```text
A [AGE RANGE] year old [GENDER] [ETHNICITY] person, [HAIR DESCRIPTION],
wearing [WARDROBE - single saturated colour, no pattern],
photographed at eye level, medium shot from the waist up,
soft warm directional key light from frame left,
plain warm beige textured wall background with a soft plant-frond shadow,
natural skin texture with visible pores, no retouching,
shallow depth of field, 9:16 vertical, photorealistic, shot on 35mm
```

Generate 4 images: front, three-quarter left, three-quarter right, and one at
final framing. These become the reference sheet.

---

## 2. A-roll beat  (Higgsfield)

```text
Reference image: [ATTACH AVATAR REFERENCE SHEET]

The character speaks this line to camera: "[SCRIPT LINE FOR THIS BEAT]"
Expression: [NEUTRAL / CONCERNED / REASSURING / AMUSED]

Same character as reference image, identical face, identical hair,
identical wardrobe. Static camera, eye level, medium shot waist up.
Warm beige wall with plant shadow, unchanged. Soft key from frame left.
Natural conversational hand gestures. No camera movement. No zoom.
No cuts. Single continuous take.
```

---

## 3. Hook  (Higgsfield — motion)

```text
Reference image: [ATTACH AVATAR REFERENCE SHEET]

The character [MOTION EXTRACTED FROM REFERENCE ANALYSIS]
while saying: "[HOOK LINE - must time to 8-10 seconds]"

Same character as reference image, identical face, hair and wardrobe.
Same warm beige room, same plant shadow, same soft key from frame left.
One continuous take, no cuts. Motion completes within the first
3 seconds, then settles to a stable medium shot.
```

Generate 2-3 variants. Pick the strongest.

---

## 4. B-roll insert  (Higgsfield)

```text
[SUBJECT - e.g. "extreme close-up of skin texture on a cheek,
visible pigmentation"]

Macro detail shot, no face visible above the nose, warm natural light
matching a beige interior, shallow depth of field, photorealistic,
natural unretouched skin, 9:16 vertical. No text, no logos, no hands
unless specified.
```

---

## 5. CTA card  (Higgsfield — standardised system prompt)

```text
Product image: [ATTACH PRODUCT PNG]
Brand logo: [ATTACH LOGO PNG]
Tagline: "[TAGLINE]"

Product centred on a plain warm cream background, soft even studio
light, subtle contact shadow beneath the product, logo lockup centred
above or below the product, generous margins, no clutter, no people,
9:16 vertical.
```

Trim to 3-4 seconds on the timeline. Replace any generated logo with the real PNG.

---

## 6. Hinglish normalisation instruction

```text
Rewrite every Romanised Hindi word in this script into Devanagari.
Leave English words in Latin script. Do not translate. Do not change
word order, meaning, or sentence length — this is a script-level
transliteration only, to fix TTS phonetics.

Then verify Hindi verb gender agreement against the avatar's gender:
  female avatar -> करी थी / की थी
  male avatar   -> करा था / किया था
Flag any mismatch.

Script:
[PASTE SCRIPT]
```

---

## 7. Chunking instruction

```text
Split this script into generation chunks under these hard rules:
1. The hook is ONE chunk, 8-10 seconds at natural speaking pace,
   never subdivided.
2. Every other beat is at most 10.0 seconds.
3. No chunk ends mid-sentence.
4. A question and its answer stay in the same chunk.
5. Exclude the CTA — it is a generated card, not a spoken beat.

Return a table: chunk number, text, estimated duration.

Script:
[PASTE NORMALISED SCRIPT]
```
