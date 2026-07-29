# cauldron

A Claude Code skill. A shelf of hand-curated brand colour palettes: given a brief, Claude
picks **one** outright, hands it over with item-get ASCII art, and explains the colour
theory behind the choice.

```
                .-.
                |≈|         ___ _  _____ _____ _____ _    ___ ___
               (___)       / __| |/ /_ _|_   _|_   _| |  | __/ __|
              \  |  /      \__ \ ' < | |  | |   | | | |__| _|\__ \
               \ | /       |___/_|\_\___| |_|   |_| |____|___|___/
                (o o)
                 \_/
                 /|\
                /   \
```

Every pick prints like a game item drop, with the vial filled in the palette's own accent
colour and true-colour swatches in the terminal:

```
                .-.
                |≈|
               (___)
              \  |  /
               \ | /
                (o o)      You obtained  ·  E M B E R   H O L L O W
                 \_/          "a warm editorial burn over cold ash"
                 /|\
                /   \      ██████ ██████ ██████ ██████ ██████
                           accent  ink    900    500    100
```

## Demo

`docs/demo.html` is a single self-contained page: every kit as Pantone-format chips, then
the same colours driven through the real Neat gradient engine with its seven named presets
(Flame, Sands, Prussian, Lemon, Bloom, Forest, Bubble Gum). Open it straight from disk, no
build step and no network:

```bash
open docs/demo.html
```

Switching kit re-skins all seven presets without changing how they move. The preset values
are Neat's own, carried over unchanged; only the colours are swapped. There is also a
vision simulator (greyscale, deuteranopia, protanopia) that runs over the chips, which is
how you can see Lemnian Hollow's three mid-tones collapse into one swatch.

The page inlines a compiled copy of Neat. See [`docs/THIRD-PARTY.md`](docs/THIRD-PARTY.md)
for attribution and licence.

## Why

Ask an LLM for colours and you get a fresh invention every time, justified after the fact.
This inverts it: the palettes are stocked by hand, ahead of time, by someone who thought
about them. The skill's job is **selection and rationale**, not generation. If nothing on
the shelf fits the brief, it says so rather than inventing hexes, because a library that
quietly generates on a miss isn't a library any more.

Each palette ships with a long-form theory file covering the harmony it uses, what the
accent does perceptually, why the neutrals lean warm or cool, and where the palette breaks.
Claude reads only the one it picked.

## Install

Clone into your Claude Code skills directory:

```bash
git clone https://github.com/C-lb/cauldron.git ~/.claude/skills/cauldron
```

That's it. No dependencies. `brew.py` is Python 3 standard library only.

Note that the skill's documented commands use the absolute path
`~/.claude/skills/cauldron/scripts/brew.py`. If you install elsewhere, update the paths in
`SKILL.md` and `references/SCHEMA.md`. A relative path fails silently from a project
working directory, which is exactly when the skill runs.

## Stocking the shelf

**The shipped library contains exactly one palette**, `ember-hollow`, as a worked example.
It is meant to be replaced with your own. `references/SCHEMA.md` documents every field.

Short version:

1. Append an entry to `references/palettes.json`.
2. Write `references/theory/<slug>.md`, modelled on `theory/ember-hollow.md`.
3. Run `--check` and paste the **measured** contrast ratios into `contrast_notes`. Don't
   estimate them.

```bash
python3 ~/.claude/skills/cauldron/scripts/brew.py --list            # what's on the shelf
python3 ~/.claude/skills/cauldron/scripts/brew.py <slug>            # render the item-get
python3 ~/.claude/skills/cauldron/scripts/brew.py --check <slug>    # measured WCAG ratios
```

`--check` output:

```
Ember Hollow — measured contrast

  accent on neutral-50          4.87:1   AA body
  accent_ink on accent          4.88:1   AA body
  accent on neutral-0           3.82:1   large text / UI only
  neutral-700 on neutral-50     9.54:1   AAA body
  neutral-100 on neutral-0     17.05:1   AAA body
```

Three kinds of entry are supported:

| `kind` | shape | for |
|---|---|---|
| `ui` | one accent + neutral ramp + semantics | interfaces and brands |
| `data` | ordered categorical array | charts |
| `kit` | named swatches, no accent or ramp | swatch sets collected as-is |

Claude filters on `kind`, so a chart colour set never gets offered as a brand accent.

`kit` exists because most palettes people actually collect are five colours with names and
no declared opinion about which one is the button. Forcing those into the `ui` shape means
inventing a neutral ramp and nominating an accent, which is generation dressed up as
curation. For kits, `--check` additionally reports the contrast between neighbouring
swatches and flags any pair under 1.5:1 as near-isoluminant — colours that differ only in
hue collapse in greyscale, at small sizes, and for red-green colour-blind viewers.

## How it picks

1. Reads `references/palettes.json`, and only that file. The theory files are expensive and
   only one gets read, after the decision.
2. Filters on `kind`, then matches the brief against each palette's `mood`, `fits` and
   `avoid`. **`avoid` is a hard exclusion**, not a penalty.
3. Picks one, by judgement rather than by scoring the tags and totalling them up. A
   weighted rubric over subjective adjectives produces confident-looking numbers that hide
   the reasoning and can't be argued with.
4. Reads that palette's theory file, renders the art, and reports the CSS custom properties
   with a short explanation and the contrast caveat.

No candidate menus. An argued pick you can reject is more useful than three options you now
have to adjudicate. You can always ask for a different one.

## Colour in the terminal

The swatches are real ANSI true-colour, emitted by `brew.py`. Colour degrades on its own:
set `NO_COLOR`, or a `TERM` of `dumb`, and the swatches print as blocks with their hexes
underneath instead of emitting escapes that would show as garbage. The fallback stays
inside 80 columns so it can't soft-wrap and mangle the drawing.

Because terminal output isn't guaranteed to reach the reader, the skill also requires
Claude to restate the palette name, tagline and hex values as plain text. The art is the
flourish; the text is the contract.

## Relationship to anti-vibecode

`cauldron` chooses **which** colours. [`anti-vibecode`](https://github.com/C-lb/anti-vibecode)
governs **how they're applied**: flat buttons, one accent, no gradients, semantic colours
carrying meaning only.

They don't overlap. Every `kind: "ui"` palette here is already shaped to anti-vibecode's
rules, so handing one over never puts the two in conflict.

## Repo layout

```
SKILL.md                     trigger, selection procedure, output contract
scripts/brew.py              the art + contrast measurement, stdlib only
references/palettes.json     the shelf (Claude scans only this to pick)
references/SCHEMA.md         field docs + how to add a palette
references/theory/<slug>.md  long-form rationale, read only after picking
DESIGN.md                    original design doc, kept as provenance
SPEC-AND-PLAN.md             spec + build plan, kept as provenance
```

## Licence

MIT.
