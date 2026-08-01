# Larkspur Orchard

> cream and meadow-green pierced by one cornflower blue

Five named swatches: Ivory, Vanilla, Tea Green, Celtic Blue, Drab Dark Brown. Three pastel
steps, one saturated blue dropped in like a wildflower, one near-black olive-brown anchor.
A garden kit — light, wholesome, unhurried — with exactly one moment of intensity.

## Harmony

Ivory, Vanilla and Tea Green sit close together in hue, walking from a neutral warm white
(~62°) through a pale yellow (~50°) into a soft yellow-green (~78°) — a tight analogous run
of about 28°, all at high value and low-to-mid saturation. That's the "meadow" half of the
kit: three tones that could pass for the same flower at different times of day.

Celtic Blue breaks hard from that run. It sits at roughly 213°, a genuine complement-ish
jump of well over 130° from the green end, and it's the only swatch with real saturation
(64%, against 20–38% for the pastels). Drab Dark Brown closes the set at 71° — nearly Tea
Green's own hue, drained to 27% value and 24% saturation, the same "brightest member with
the life taken out of it" move Lemnian Hollow makes with Gunmetal. The anchor belongs to the
meadow half, not to the blue.

So the kit reads as two families sharing one card: a warm-pastel cluster with its own dark
version of itself, and a single cool intruder with no relatives. That imbalance is the
point — it's what makes Celtic Blue read as a flower against foliage rather than as a fourth
pastel.

## What Celtic Blue does perceptually

It's the only swatch here with the saturation to act as an accent, and by a wide margin —
next highest is Vanilla at 38%, and Vanilla is desaturated by being pale, not by being
muted. Celtic Blue is genuinely chromatic in a kit that's otherwise chalk and moss.

That makes it the de facto accent even though nothing in a kit is declared as one. Used
generously it stops reading as a wildflower and starts reading as a brand blue competing
with the meadow, which flattens the whole effect. One swatch used sparingly — a link, a
single illustrated bloom, a call-to-action — is what the harmony is built for.

It also measures weakest of the five against the anchor: 2.37:1 on Drab Dark Brown, which
fails body text outright and is marginal even for large text or UI chrome. Celtic Blue wants
a pale surface under it (Ivory or Vanilla), not the dark one.

## The pastel run, and the problem with it

Ivory, Vanilla and Tea Green are close to isoluminant against each other:

- Ivory / Vanilla — 1.21:1
- Vanilla / Tea Green — 1.24:1

Both are well under the 1.5:1 line this kit's own tooling flags. Visually that's the charm —
it's what makes the three read as one continuous cream-to-green wash rather than three
discrete swatches — but it means none of the three can be relied on to separate from its
neighbour without help from position, a border, or a label. A three-way legend built only
from these three will not survive greyscale, a low-quality print, or a glance from across a
room.

Tea Green and Celtic Blue are the one pastel/accent pair with real separation (3.20:1),
which is exactly why that pairing is where the kit wants to put its contrast.

## The anchor

Drab Dark Brown clears AAA body against all three pastels (11.34:1, 9.39:1, 7.58:1) and is
the only swatch dark enough to hold long-form text or a full-bleed ground. Because it shares
Tea Green's hue rather than importing a foreign neutral, dark-mode or footer treatments built
from it read as "the meadow at dusk," not as a black box dropped behind pastel art.

## Where it breaks

**Fintech, medical, anything that needs to read as serious or precise.** The palette is
unapologetically soft and organic; asking it to carry authority or urgency fights its own
harmony.

**Dense data tables and status UI.** The three pastels are near-isoluminant and this kit
has no semantic register at all — no colour here reads as "warning" or "success" without a
label doing the actual work.

**High-contrast dark UI.** Only Celtic Blue and the anchor have real chroma; everything else
goes chalky and low-energy on a dark ground, which undersells a kit built to be read on
paper-light surfaces.

## Applying it

Surface Ivory or Vanilla. Let Tea Green carry large fills — packaging backgrounds,
illustration foliage, section dividers. Spend Celtic Blue like a single flower: one accent
element per view, never a field. Reserve Drab Dark Brown for body copy and the one dark
surface the kit supports.

Body text: on the pastel surfaces, only Drab Dark Brown clears AA; on Drab Dark Brown, all
three pastels clear AAA and Celtic Blue does not clear at all. If a design needs blue body
text, this kit does not supply a safe way to set it — treat Celtic Blue as decoration and
large UI only.
