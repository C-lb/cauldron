# Silver Gelatin

> black and white photography, only tone

A palette with no hue at all. Every neutral step is true grayscale — R, G and B equal at
every stop — and the accent is not a colour choice but a weight choice: the darkest ink
available, used the way a darkroom print uses pure black. The name comes from the
silver-halide photographic process that produces black-and-white prints: no colour dye
layer, just density of exposed silver. That's the whole design principle transplanted to a
UI palette.

## No hue to reason about

Every other `kind: "ui"` entry on this shelf earns its theory file by explaining a hue
relationship: how the accent sits against the ramp, why the neutrals lean warm or cold to
flatter it. Silver Gelatin has none of that, because there's no hue anywhere in `colors`
except `semantic`. `accent` (`#121212`) and every neutral step are pure achromatic grays.
This is not an oversight — it's the entire pitch. A palette that cannot look "off-brand"
because it never chose a brand hue in the first place.

That constrains what the palette can do for you. It can't create warmth, energy, or a
sense of place the way Ember Hollow or Paprika Bazaar can — there's no pigment to carry
that. What it buys instead is total legibility of structure: every visual distinction on
screen is a distinction in *lightness*, which is the one channel every viewer perceives,
colour-blind or not, in daylight or dim light, on a calibrated monitor or a cheap one.

## Why the accent is near-black, not pure black

`#121212` rather than `#000000`. Pure black on a bright screen produces visible halation
around text — the eye's local contrast adaptation makes `#000000` glyphs on `#FAFAFA`
slightly buzz at small sizes, an effect print designers have known about for a century
(hence "rich black" in ink, never pure black). Lifting the accent one step off true black
removes the buzz without giving up any meaningful contrast: `18.73:1` ink-on-accent is so
far past AAA (7:1) that the half-step cost is free.

`accent_ink` is `#FFFFFF`, not an off-white. Unlike Ember Hollow, where the accent has a
hue for a cool white to clash against, there's no hue here for pure white to fight. It
reads clean because there's nothing chromatic underneath it to argue with.

## The ramp is deliberately boring

Ten neutral steps, spaced by roughly even blocks of luminance rather than clustered at
either end. That's a different choice from Ember Hollow, whose ramp bunches tightly at the
light steps because that palette needs fine surface separation in a light UI. Silver
Gelatin spaces more evenly because its job is different: it's often the *only* source of
visual hierarchy on screen, so every step has to read as a distinct, nameable tone rather
than existing to flatter a light canvas specifically. `500` (`#808080`) sits at almost
exactly the geometric middle, which is the point — this is a palette organized around a
value scale, the way a photographer thinks in stops, not around a canvas direction.

## Where it breaks

**It cannot carry state on its own.** With zero chroma in the base palette, `info` /
`success` / `warning` / `danger` are the only colour anywhere in the system, and they will
look conspicuous by contrast — which is correct, that's what a semantic colour is for, but
it means those four hues do all the "something happened" signaling. If a product needs more
than four simultaneous state colours, or needs colour for anything beyond info/success/
warning/danger, this palette will not stretch to cover it.

**Playful or lifestyle brands.** A palette with no chroma reads as serious by default —
technical, editorial, archival. Forcing warmth or playfulness out of it means fighting the
premise; reach for a `kind: "kit"` with named warm swatches instead.

**Anything that needs to look alive.** Grayscale-only UIs can read as unfinished or as a
placeholder state to users who associate "no colour yet" with "not done." That's a real
perception risk for consumer-facing marketing, less so for tools whose users already expect
a utilitarian surface (dashboards, documentation, admin).

## Applying it

Treat `accent` as ink, not paint — it's for text, primary buttons, and the one interactive
element per view that needs to dominate, exactly like Ember Hollow's accent, just without a
hue. Everything else is neutral steps chosen by how much visual weight a region should
carry, not by what it "is." Body text on the light canvas: `700` on `50` (`9.93:1`, AAA).
The accent itself measures `1.12:1` against `neutral-0` and fails outright there — this
palette does not attempt a dark-canvas mode; use `neutral-100` or `accent_ink` for anything
that needs to read on a dark surface instead.
