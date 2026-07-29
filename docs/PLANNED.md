# Planned work

Parked 2026-07-30. Items 1 (live hex preview) and 2 (colour wheel) shipped later the same
day; what remains is below. Current state of the demo is described in the README.

Shipped notes, for whoever touches these next:
- The hex input lives in the "Your colours" card under the hero. It accepts commas or
  newlines, optional `#`, optional `Name #hex` pairs, flags bad tokens by name, refuses
  more than 6 (Neat's limit), builds a `custom` kit that feeds everything on the page, and
  persists to the URL hash (`#kit=Name:hex,...`). "Copy palette entry" emits a
  `palettes.json` object with `contrast_notes` measured, near-isoluminant pairs flagged.
- The wheel went OKLCH (hue = angle, chroma = radius, rim drawn via an OKLCH→sRGB
  conversion so ring and dots share angles). It ships beside the ranked lightness scale,
  which carries the adjacent-pair ratios and marks anything under 1.5:1 in danger red.

---

## Compact kit view

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

**Note:** Comfortable stays the default. The Pantone format is the point of the chips, and
compact is for when the shelf gets long. Since the sections merged into one Kits card, the
"drop the selector" part needs rethinking against the current layout: the dropdown already
previews every kit's mix, so Compact may only need to render the shelf as strips without
touching the selector.

---

## Rebuild reminder

`docs/demo.html` inlines a compiled copy of Neat. If the page is regenerated, the bundle
has to be rebuilt from the `C-lb/neat` fork and re-inlined, and the watermark patch
(`_licensed` defaulting to true in `lib/src/NeatGradient.ts`) reapplied. See
`docs/THIRD-PARTY.md` for attribution obligations, which apply to any rebuild.
