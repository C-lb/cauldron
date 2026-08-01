# Amber Tideline

> a sunset burning down into near-black tide

Five named swatches: Licorice, Delft Blue, Taupe Gray, Persian Orange, Earth Yellow. A
literal sunset-over-water gradient: near-black tide, a dusk-blue horizon, a grey haze band,
then two warm swatches burning up to the brightest orange-yellow. Cinematic rather than
structural — this kit paints a moment, it doesn't build a UI.

## Harmony

The hues sweep 353° → 231° → 273° → 20° → 33°, which is not a clean rotation in one
direction — it's a photograph, not a colour wheel exercise. Licorice and Persian Orange are
both warm (near-complementary to Delft Blue's cool 231°), while Taupe Gray sits between them
at low saturation, doing the job real haze does: desaturating whatever's behind it. That's
the "atmosphere" read — a warm sky and a cool sea with a grey scrim where they meet, rather
than a designed hue progression.

Saturation confirms which swatches are doing the work: Earth Yellow (81%) and Persian Orange
(41%) are the only genuinely chromatic members. Delft Blue (23%) and Taupe Gray (9%) are
closer to tinted greys than colours, and Licorice (5%) is functionally black with a whisper
of warmth in it — consistent with a photographed dusk sky rather than a picked hue.

## What Earth Yellow does perceptually

It's the brightest and most saturated swatch by a wide margin and clears AAA body against
the anchor (10.05:1) — the only member of the kit that can carry real text weight on
Licorice. Used as more than a small hot spot it stops reading as a sun and starts reading as
a warning colour, since high-saturation orange-yellow is exactly where alert UI lives. Ration
it the way you'd ration an actual sunset: a rim, a highlight, a call-to-action, not a field.

Persian Orange is close behind it in role but not in weight — 6.76:1 against the anchor,
solidly AA body, and closer in lightness to Earth Yellow than to anything else in the kit
(they're a near-isoluminant pair, see below). Together they're the "warm half" of the
gradient; individually, Persian Orange is the one safe to use at larger area since it's less
intense.

## The mid-band, and the problem with it

Delft Blue measures 1.63:1 against Licorice — it fails as body text on the anchor and is
barely distinguishable from it as a fill. That's true to the source photograph (a dusk sky
just above the horizon is barely lighter than the water below it) but it means Delft Blue
functions as a *second dark*, not a mid-tone, wherever it sits next to Licorice. Don't expect
it to read as blue at small sizes against the anchor; it reads as "slightly warmer black."

Persian Orange and Earth Yellow sit 1.49:1 apart — just under this kit's own isoluminance
line. They read as one continuous warm glow rather than two distinct steps, which is
correct for a sunset and wrong for anything that needs to distinguish "orange thing" from
"yellow thing" without a label.

Taupe Gray is the kit's actual mid-tone: 4.05:1 against Licorice (large text / UI only), and
the only swatch positioned to separate the warm half from the cool half without collapsing
into either.

## The anchor

Licorice is near-black (5% saturation) and holds the full contrast range: AAA against Earth
Yellow, AA against Persian Orange, large-text-only against Taupe Gray, and a near-fail
against Delft Blue. It's the only swatch that can serve as a full-bleed ground or hold
long-form text — everything else in the kit is either too light or, in Delft Blue's case,
too close to the anchor's own depth to contrast against it.

## Where it breaks

**Fintech, medical, dense data tables.** This is mood lighting, not a system. There's no
semantic register (nothing reads as "success" or "error") and half the kit is built around
being *atmospheric* rather than *legible*.

**High-density dashboards.** Delft Blue and Taupe Gray are both weak against the anchor,
and Persian Orange/Earth Yellow are too close together to serve as independent status
colours. A dashboard built from this kit would need to import colours it doesn't have.

## Applying it

Surface Licorice, or let a real photograph stand in for it. Earth Yellow is the sun — a
small hot accent, never a field. Persian Orange is the warm mid-ground for larger shapes
that need to read as "glowing" without competing with Earth Yellow. Taupe Gray is the
transition tone: haze, dividers, secondary text on light surfaces. Delft Blue works best as
texture near the anchor — a barely-lighter band, a subtle shape — not as a swatch expected to
pop.

Body text: on Licorice, Earth Yellow clears AAA and Persian Orange clears AA; Taupe Gray is
large-text/UI only and Delft Blue does not clear at all. This kit has no light surface among
its five swatches — bring in an off-white if the design needs body copy on a pale ground.
