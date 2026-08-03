# Satsuma Letterpress

satsuma ink and cornflower on warm paper

## The harmony

A split-complementary built around orange. Satsuma (#B54B0C, ~25° hue) is the single
accent; cornflower-cobalt (#3160C9, ~220°) sits nearly opposite and enters only as the
info/link semantic — meaning, not decoration — which is what makes the pairing read as
playful without breaking the one-accent rule. The neutral ramp is not grey: every step
carries the same warm ochre cast (roughly 40–45° hue at low saturation), so the canvas
reads as paper rather than as a screen. That warmth is the quiet half of the trick the
loud half (the orange) gets credit for.

## Why the accent works

Orange is the highest-energy hue the eye tolerates at text-adjacent sizes without
vibrating. Deepened to #B54B0C it keeps the satsuma character but drops enough luminance
to hold 4.94:1 on the paper canvas and 4.98:1 under its own warm-white ink — a true AA
button fill, not a poster colour. Against the warm neutrals it reads as saturation
contrast more than hue contrast, which is why one accent is enough: everything else on
the page is the same temperature, just quieter.

The cornflower counterweight works because it is the coolest thing on an otherwise
uniformly warm page. Reserve it for links, info states, and the occasional selected
control and it lands like punctuation. Promote it to a second accent and the page splits
into two competing temperatures — the exact failure the one-accent rule exists to stop.

## The neutrals

Eleven steps from #FAF7F0 paper to a #100F0C near-black that is warm charcoal, not blue
black. The ramp holds hue while walking luminance, so dark mode built from the 800–0 end
stays in the same family as light mode built from 50–200 — one material photographed in
two lights, which is what a dual-mode app wants. Ink on paper is 16.85:1; supporting text
at 700 is 9.65:1.

## Failure modes

- **Warning vs accent.** The ochre warning (#8A6200) sits near the accent in hue at a
  1.04:1 luminance ratio. Warning UI must carry an icon or a label; orange colour alone
  cannot distinguish "warning" from "brand" here.
- **The accent on dark.** 3.63:1 on the near-black end — chrome and large text only. Use
  the lifted satsuma #E8834A for dark-canvas emphasis and swap the whole semantic set for
  the dark-tuned one in `contrast_notes`; the light set collapses on #100F0C.
- **Beige drift.** On cheap panels the 100/200 steps can read yellow-green. Keep large
  fields at 50/100 and use 200 only for wells and pressed states.
- **Don't cool the shadows.** Grey or blue-tinted shadows on this canvas look like dirt.
  Shadow colour should stay near #191612 at low opacity.
