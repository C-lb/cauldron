# cauldron — design (approved 2026-07-29, not yet built)

> **Superseded on naming.** Built as `cauldron`, renamed to `potions`, then renamed again
> to **`cauldron`** on 2026-07-30. This document is kept verbatim as provenance, including
> the decision table below that rejects "potion" — that reasoning was overruled, not
> retracted, and has since been overtaken entirely. Everything else here still describes
> the built skill. Live paths are `~/.claude/skills/cauldron/`.

A Claude Code skill holding a curated library of brand colour palettes. At the start of
any new project or brand/visual work, Claude picks one outright, prints an item-get ASCII
banner, and explains the colour theory behind the choice.

## Status

Design approved through the ASCII-art section. **Nothing implemented yet.** One open
question left (below), then write the spec + implementation plan.

## Open question

Should the vial's `≈` fill in the item-get art render in the picked palette's accent
colour, so the potion handed over is literally the colour you got? (Leaning yes.)

## Decisions locked

| Decision | Choice | Why |
|---|---|---|
| Name | `cauldron` | Dye genuinely was boiled from foraged plants in a vat, so the cauldron *is* the source of colour. Keeps the skill (the library) distinct from the potion (the item the art hands you). |
| Rejected names | `dyers-hollow`, `woadwalker`, `bramblewick`, `forage`, `potion` | "hollow" felt far-fetched; "forage" is a bare common verb and would false-trigger on unrelated gathering requests; "potion" collides with the item in the art. |
| Purpose | Brand/visual palettes, **not** a semantic-colour system | Caleb stocks the hexes; the skill supplies the pick + the rationale. |
| Selection | Claude picks **one** outright, applies it, explains it | No 2-3 candidate menu. Push back to change it. |
| Storage | JSON index + per-palette markdown deep-dives | Claude scans only the index to pick, then reads one theory file. Cheapest on context. |
| Palette names | Fantasy names + a descriptive one-liner subtitle | e.g. "Ember Hollow — a warm editorial burn over cold ash". |
| Art | Every pick, no exceptions | It's the point. |
| Item in art | Potion vial, **not** a berry | A flask has a recognisable silhouette in ASCII; a berry reads as noise. Berries also imply *found*, and dye is *brewed*. |
| Seed data | Empty library + `SCHEMA.md` + one worked example (`ember-hollow`) | Nothing curated by Claude that Caleb would have to delete. |

## Layout

```
~/.claude/skills/cauldron/
  SKILL.md                     trigger + selection procedure + the art
  references/palettes.json     machine-readable index (Claude scans this to pick)
  references/SCHEMA.md         field docs + how to add a palette
  references/theory/<slug>.md  long-form rationale (read only after picking)
```

## Palette entry schema

```json
{
  "slug": "ember-hollow",
  "name": "Ember Hollow",
  "tagline": "a warm editorial burn over cold ash",
  "kind": "ui",
  "mood": ["warm", "editorial", "premium"],
  "fits": ["portfolio", "hospitality", "long-form reading"],
  "avoid": ["fintech", "medical", "high-density dashboards"],
  "colors": {
    "accent": "#C2410C",
    "accent_ink": "#FFF7ED",
    "neutrals": ["#0A0A0A", "#171717", "..."],
    "semantic": { "success": "...", "warning": "...", "danger": "...", "info": "..." }
  },
  "theory": "ember-hollow.md",
  "contrast_notes": "accent on neutral-0 = 7.1:1 (AAA)"
}
```

`kind: "ui"` entries are anti-vibecode-shaped (one accent + neutral ramp).
`kind: "data"` entries are categorical sets for charts. Claude filters on `kind` by what
it's building.

## Behaviour

At the start of any new project or brand/visual work:

1. Read `palettes.json` only.
2. Match the brief against `mood` / `fits` / `avoid`.
3. Pick one. Read that palette's theory file.
4. Print the item-get banner with the palette name, tagline, and ANSI truecolor swatches
   (real hexes rendering as actual colour in the terminal, not labels).
5. Report the CSS custom-property block ready to paste, plus a short why: which harmony
   it uses (analogous, split-complement, etc.), what the accent does perceptually, why
   the neutrals lean warm or cool.

## Relationship to anti-vibecode

`cauldron` chooses **which** colours. `anti-vibecode` governs **how they're applied**
(flat buttons, no gradients, semantic use only). No overlap. SKILL.md must state this
explicitly so the two skills don't argue.

## ASCII art

Banner (gandalf-style: figure left, wordmark right). Wordmark is pyfiglet `small` font,
`CAULDRON`:

```
                .-.
                |≈|        ___   _  _   _ _    ___  ___  ___  _  _
               (___)      / __| /_\| | | | |  |   \| _ \/ _ \| \| |
              \  |  /    | (__ / _ \ |_| | |__| |) |   / (_) | .` |
               \ | /      \___/_/ \_\___/|____|___/|_|_\\___/|_|\_|
                (o o)
                 \_/
                 /|\
                /   \
```

Per-pick item-get (the one seen most):

```
                .-.
                |≈|
               (___)
              \  |  /
               \ | /
                (o o)      You obtained  ·  E M B E R   H O L L O W
                 \_/          "a warm editorial burn over cold ash"
                 /|\
                /   \      ███ ███ ███ ███ ███
                           accent  ink  900  500  100
```

## Next session

1. Answer the open question above.
2. Write spec + implementation plan together (single combined review).
3. Build via subagent-driven execution.
4. Caleb supplies the real palette hexes once the schema is in place.

### Gotcha

`figlet` and `toilet` are not installed and `pip install pyfiglet` is blocked by PEP 668
on this machine. Use a venv:
`python3 -m venv v && ./v/bin/pip install pyfiglet`
