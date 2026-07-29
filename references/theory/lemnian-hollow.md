# Lemnian Hollow

> a cool sweep from mint to mauve over gunmetal

Five named swatches: Fairy Dust, Cool Steel, Lavender Grey, Dusty Mauve, Gunmetal. One
bright mint, three clustered mid-tones, one near-black anchor. Atmospheric rather than
structural — this is a kit for setting a mood, not for building hierarchy.

## Harmony

A long cool arc. The hues march 161° → 191° → 230° → 309°, roughly 148° of travel from
green-cyan through blue and into magenta. That's well past analogous (which stays inside
about 60°) without ever reaching a true complementary pair, so it reads as a *journey*
rather than a contrast: each step is a near-neighbour of the last, but the two ends have
visibly parted company.

Gunmetal sits at 150°, which is Fairy Dust's own hue drained to 11% saturation and 21%
value. That's the structural key to the whole kit. The anchor isn't a foreign neutral
imported to sit under the colours; it's the brightest member with the life taken out of it.
That shared origin is why the dark reads as *belonging* rather than as a black rectangle
someone dropped in behind.

Saturation tells you the hierarchy: 40% for Fairy Dust, then 26 / 19 / 22 for the middle,
then 11. Only one swatch is really chromatic. The rest are tinted greys.

## What Fairy Dust does perceptually

It is the only voice in the kit that carries. At 91% value and 40% saturation over a set
whose other members sit near 65%, it has roughly a 2.5:1 luminance jump on its nearest
neighbour, and it's the single swatch that clears AAA against the anchor (8.53:1).

So despite there being no `accent` field in a kit, Fairy Dust is functionally the accent,
and it should be rationed like one. Used across large fields it turns the palette into mint
wallpaper and the arc collapses, because nothing else is bright enough to answer it.

It is also close to useless on white: 1.45:1. Fairy Dust is a dark-surface colour. On a
light background it's a decorative fill at best, never text and never a thin line.

## The mid-tones, and the problem with them

Cool Steel, Lavender Grey and Dusty Mauve are near-isoluminant. Measured:

- Cool Steel / Lavender Grey — 1.19:1
- Lavender Grey / Dusty Mauve — 1.14:1
- Cool Steel / Dusty Mauve — 1.35:1

For context, 1.0:1 is *identical brightness*. These three differ almost entirely in hue,
barely at all in lightness.

Aesthetically that's the appeal. It's what makes the sweep feel like a gradient of mood
rather than a set of discrete options, and it's why the palette photographs as atmosphere.
Desaturated neighbours at matched lightness are exactly how overcast light behaves, which
is where the whole thing gets its stillness.

Functionally it's a live hazard. Three colours at the same lightness:

- collapse into one grey in greyscale printing or a screenshot run through a filter;
- are hard to separate for deuteranopic and protanopic viewers, since the blue-to-magenta
  span is where red-green deficiency does the most damage and there's no lightness cue left
  to fall back on;
- lose their distinction at small sizes, where the eye judges by lightness before hue.

None of this makes them wrong. It makes them **unable to carry meaning by themselves**. If
Cool Steel means one thing and Dusty Mauve means another, that distinction has to be
reinforced by position, label, icon or shape. Colour alone will not survive the trip.

## The anchor

Gunmetal at 12.34:1 against white and near-black in absolute terms is doing all of the
structural work. It's the only member with the contrast range to hold text, rules, or a
full-bleed background.

Build on it. The kit's natural configuration is Gunmetal as the surface, Fairy Dust as the
one thing that speaks, and the three mid-tones as texture across it — where "texture" means
illustration fills, chart bands with labels, gradient stops, map regions. Reverse it onto a
white surface and the palette loses its anchor and most of its contrast at once, because
the four remaining swatches are all mid-light.

## Where it breaks

**Dense data tables and status UI.** This is the isoluminance problem cashed out. A table
that distinguishes rows or states by Cool Steel versus Lavender Grey has, for a meaningful
share of readers, no distinction at all. Status colour also demands the semantic register
(green means good, red means stop) and there is nothing here that reads as either.

**Anything needing hierarchy from colour alone.** The kit has exactly two levels of
emphasis — Fairy Dust, and everything else. If the design needs four ranks, this palette
cannot supply them without inventing swatches, and inventing swatches is how a kit stops
being a kit.

## Applying it

Surface Gunmetal. Accent Fairy Dust, sparingly. Mid-tones for fills and atmosphere, never
as the sole carrier of a distinction.

Body text on Gunmetal: Fairy Dust clears AAA, everything else is large-text-and-chrome only
(Cool Steel 4.49:1 misses AA body by a whisker, Lavender Grey 3.77:1 and Dusty Mauve 3.32:1
by more). If you need long-form body copy in this palette, bring in an off-white — the kit
does not contain one, and that omission is real rather than an oversight to paper over.
