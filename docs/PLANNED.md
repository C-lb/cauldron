# Planned work

Parked 2026-07-30. Three features for `docs/demo.html`, in the order they're worth doing.
Nothing here is started. Current state of the demo is described in the README.

---

## 1. Live hex preview at the top of the page

**What:** an input at the very top where you paste hex codes and immediately see them as
chips, as a gradient, and in the contrast table. No editing `palettes.json` first.

**Why this is first:** it closes the loop the skill is missing. Right now stocking the
shelf means hand-editing JSON, writing a theory file, and running `--check` in a terminal.
This turns the demo into the authoring tool.

**Design**

- Accepts loose input: `#8BE8CB, #7EA2AA, #888DA7` or newline-separated, with or without
  `#`, and ideally `Fairy Dust #8BE8CB` name-and-hex pairs on each line.
- Builds an ad-hoc kit that feeds everything already on the page: chips, the Neat gradient,
  the vision simulator, the contrast table.
- Invalid tokens get flagged inline next to the input, not silently dropped. Say which
  token failed.
- Cap at 6, since that is Neat's colour limit, and say so when input exceeds it rather
  than truncating quietly.

**The high-value part:** a "Copy as palette entry" button that emits a ready-to-paste
`palettes.json` object with `contrast_notes` **already measured and filled in**, including
the near-isoluminant neighbour warnings. That is the step most likely to be skipped or
estimated by eye, and the demo already computes it.

**Open question:** persistence. Recommend encoding into the URL hash
(`#kit=8BE8CB,7EA2AA,888DA7`) so a trial palette survives reload and can be sent to someone.
No localStorage, nothing to clear.

---

## 2. Colour wheel

**What:** plot a kit's swatches on a colour wheel so the harmony is visible rather than
described.

**Why:** the theory files already argue in these terms. Lemnian Hollow's write-up talks
about a 148 degree arc from 161 to 309, and about Gunmetal sitting at 150 degrees as Fairy
Dust drained of chroma. A wheel shows both instantly. Ember Hollow's near-complementary
imbalance is the same story.

**Design**

- Canvas-drawn HSL wheel. Hue is angle, saturation is radius. Each swatch is a dot,
  connected in kit order so the sweep reads as a path.
- Label each dot with its swatch name.

**The trap to avoid:** a hue/saturation wheel throws away lightness, and lightness is the
axis this whole library cares about most. A wheel on its own would make Lemnian Hollow's
three mid-tones look nicely spread when the entire problem is that they are not. So the
wheel must ship **next to a lightness scale** showing the same swatches ranked by relative
luminance, with the near-isoluminant pairs marked. Wheel answers "what harmony is this",
lightness bar answers "will it survive".

**Open question:** whether to use HSL or a perceptual space (OKLCH). HSL is what the hex
maps to directly and is easier to explain; OKLCH would place the dots where the eye
actually sees them and would make the isoluminance visible on the wheel itself. Leaning
OKLCH for correctness, but it needs a conversion step and the axis labels get less familiar.

---

## 3. Compact kit view

**What:** a density toggle, and stop showing one kit at a time.

**Why:** the Pantone chips are tall by design (`aspect-ratio: 1/1.18` plus a label band).
Five of them fill a screen. With a real shelf of kits that becomes a very long page, and
the current design hides every kit but one behind a selector, so kits cannot be compared.

**Design**

- Toggle in the section header: Comfortable (current Pantone chips) and Compact.
- Compact renders each kit as one horizontal strip: small square swatches butted together,
  name and hex beneath in caption type, whole kit on one or two lines.
- In Compact, drop the kit selector and render **every** kit stacked, so the shelf reads as
  an index and kits can be compared against each other.
- The gradient section keeps its own kit selector regardless, since it can only drive one
  kit at a time.

**Note:** Comfortable stays the default. The Pantone format is the point of section 1, and
compact is for when the shelf gets long.

---

## Rebuild reminder

`docs/demo.html` inlines a compiled copy of Neat. If the page is regenerated, the bundle
has to be rebuilt from the `C-lb/neat` fork and re-inlined, and the watermark patch
(`_licensed` defaulting to true in `lib/src/NeatGradient.ts`) reapplied. See
`docs/THIRD-PARTY.md` for attribution obligations, which apply to any rebuild.
