# Basement Amethyst

*a violet signal in concrete and sodium light*

## The problem it was built for

An operations tool used in two hostile lighting conditions by the same person in the same
shift: an underground car park at 2am, and a forecourt in direct afternoon glare. Held
one-handed, often while holding something else. The screen is a legal record, so a
misread status is not a cosmetic failure.

That rules out most of what a palette is normally chosen for. There is no mood to set and
no brand warmth to project. What the palette has to do is keep four status colours apart
from each other and from the accent, at a glance, from a dark-adapted eye.

## The harmony

A single accent at hue 269, deep amethyst, over a cool near-neutral ramp.

The accent's hue is not a taste decision, it is a spacing decision. The four semantic
hues cluster across roughly 220 degrees of the wheel: danger at 0, warning at 39, success
at 151, info at 216. That leaves exactly one wide gap, from about 250 to 330, and the
accent belongs in it. At 269 the accent sits 48 degrees from info, its nearest neighbour,
and 91 or more from the rest.

A pure optimiser puts the accent at 292, a hot magenta, which buys another 20 degrees of
separation from info. That was rejected. Magenta reads consumer and playful, and this is
a custody record; 48 degrees is already well past the point where two hues are confused
at a glance, so the extra separation was not worth what it cost in register.

Violet earns its place a second way, which is environmental rather than perceptual. A car
park is concrete grey, sodium or LED white, painted yellow lines, and car paint in
roughly every colour a manufacturer sells. Violet at this chroma is close to absent from
that world, so the accent never camouflages against the background, and never against a
photograph of a car.

## The neutrals

Cool, and dark-first. Step 0 is the canvas at #0B0C0E, and 50 through 900 run light to
dark, so a dark-mode surface is a *higher* step than its canvas: cards at 900, raised
surfaces at 800 and 700. Elevation reads as more light, never as more shadow.

They lean very slightly blue rather than warm. A warm grey next to an amber warning
state starts to look like a dimmer version of that warning, which is exactly the
confusion this palette exists to avoid. Cool greys stay legibly *not a status*.

## What the accent is allowed to do

It is a fill. The measured ratio that matters is white on the accent at 5.02:1, because
the accent's job is the single full-width primary action, with its label sitting on top.

It is not a text colour on dark. On the near-black canvas the accent measures 3.90:1,
which is large text and UI chrome only. This is not a flaw to design around: no single
colour can be AA body on both a near-black and a near-white canvas, because the two
luminance windows do not overlap at all. Anyone who goes looking for one is looking for
something that does not exist.

## Failure modes

**The semantics are dark-tuned and do not transfer.** On the dark canvas they measure
7.19, 10.43, 10.70 and 7.05 to one. On a light canvas the same four measure between 1.7
and 2.6, which is unusable. Substitutes are listed in `contrast_notes` and must actually
be substituted, not approximated.

A dual-mode set was tried first and abandoned. Forcing one value per semantic to clear AA
on near-black and 3:1 on near-white pins it to a narrow mid-luminance band, and the only
colours in that band are desaturated: the warning lands on a muddy brown. A muddy brown
warning at 2am is worse than maintaining two values.

**Warning and danger are 39 degrees apart** at a 1.52:1 luminance ratio. That is the
weakest pair in the palette and no amount of hue tuning fixes it while keeping amber
amber and red red. They must never be the only difference between two states. Pair them
with text, an icon, or position. Any interface built on this palette that signals
something by colour alone has misused it, and the case where it will be noticed is the
one where someone is colour-blind, in the dark, in a hurry.

**Do not add a second accent.** The gap the accent occupies is the only wide one left. A
second hue lands inside a semantic's territory by definition, and the first thing to
break will be a status the user has stopped reading carefully because they have learned
to trust the colour.
