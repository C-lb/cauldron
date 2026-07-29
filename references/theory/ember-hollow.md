# Ember Hollow

> a warm editorial burn over cold ash

A single scorched orange doing all the work over a neutral ramp that is deliberately
colder than it is. Read as: banked embers in grey ash. The accent looks hotter than its
hex suggests, because everything around it is pulling the opposite direction.

## Harmony

Near-complementary, unevenly weighted. The accent `#C2410C` sits around 21° hue; the
neutral ramp carries a slight blue-violet undertone, roughly 220°. That's close to
opposition on the wheel, but the neutrals are held at very low chroma, so it never becomes
the orange-and-blue clash that ruins most warm/cool pairings.

The trick is the imbalance. A true complementary scheme gives two colours comparable
presence and they fight for the eye. Here one side is saturated and occupies maybe 5% of
any screen; the other is desaturated to near-grey and occupies the rest. The eye reads the
ash as neutral, not as blue — but the accent still gets the full perceptual lift of sitting
against its opposite. You get complementary contrast while appearing to use one colour.

This is why the neutrals must stay cold. Warm the ramp toward beige and the accent
collapses into it: the whole palette turns into one muddy orange-brown wash, which is the
default failure mode of every "warm editorial" palette on the internet.

## What the accent does perceptually

`#C2410C` is a burnt orange, not a signal orange. It's been darkened and desaturated off
pure orange far enough that it stops reading as *alert* and starts reading as *material* —
terracotta, rust, fired clay. That matters because orange at full chroma is a warning
colour, and the brain treats it as one. Pulling the lightness down to around 45% and the
chroma back moves it out of the warning register into the pigment register.

Consequence for use: it can be a large field. A full-bleed orange block at this value reads
as a considered surface. The same hue at `#F97316` would read as an error state at that
size.

It is also close enough to the `warning` semantic (`#B45309`) to be a problem if you're
careless. They are distinguishable side by side but not from memory. So warnings in this
palette should carry an icon and never rely on colour alone — which is house policy
anyway, but here it's load-bearing rather than a nicety.

## Why the neutrals lean cold

Three reasons, in order of weight:

1. **To make the accent hot.** Covered above. This is the main one.
2. **Long-form legibility.** The palette's primary use is reading. A cold grey at
   `#3D4248` on `#F7F8F9` produces a slightly higher perceived contrast than the same
   luminance in a warm grey, because blue-tinted text edges read as crisper. Marginal, but
   it compounds over a page of body copy.
3. **It keeps the greys honest.** Warm greys drift. Under a warm accent, a warm neutral
   starts looking like a washed-out version of the accent rather than an absence of colour,
   and the palette loses its ability to say "nothing is happening here."

The ramp is smooth in perceived lightness, not in hex arithmetic. Steps cluster more
tightly at the light end (`50`, `100`, `200` are close together) because that's where
surface separation happens in a light UI and where the eye is most sensitive to small
differences. The dark end spaces out more, since `800` and `900` are doing structural work
— backgrounds, not distinctions.

## The ink

`#FFF7ED` on the accent, not `#FFFFFF`. Pure white on a burnt orange has a faint blue cast
that reads as slightly dirty, a chromatic-aberration illusion where the eye over-corrects
for the surrounding warmth. Warming the white a few points to a bare cream cancels it. The
contrast cost is negligible (4.88:1, still AA) and the surface reads notably cleaner.

## Where it breaks

The `avoid` list is not decoration.

**Fintech and medical.** Burnt orange carries associations of heat, decay and warning.
Neither domain wants any of them near a number that represents someone's money or blood
work. There's no styling fix; the association is in the hue.

**High-density dashboards and enterprise admin.** The palette has exactly one accent and
a low-chroma ramp. That is a strength for a reading surface and a fatal limitation for a
screen that needs to distinguish nine simultaneous states. Reaching for a second accent to
cope is how this palette gets ruined — if the interface needs that, it needs a different
palette, or a `kind: "data"` set alongside.

## Applying it

The accent is punctuation, not paint. One primary action per view, the occasional rule or
marker, and links in long-form text. Everything structural is neutral. If two things on
screen are competing to be orange, one of them is wrong.

Body text on light: `700` on `50`. Body text on dark: `100` on `0` — *not* the accent,
which only clears 3.82:1 there and is reserved for headings and chrome.
