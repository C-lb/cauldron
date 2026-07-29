# Palette schema — and how to add one

`palettes.json` is the shelf. It is a JSON array of palette objects. Claude scans this file
(and only this file) to make a pick, so every field here exists to help it choose well or
to keep it from choosing badly. Nothing else belongs in it — long-form reasoning lives in
`theory/<slug>.md` and is read only after a pick is made.

## Adding a palette, short version

1. Append an object to the array in `palettes.json` following the fields below.
2. Write `theory/<slug>.md` using `theory/ember-hollow.md` as the template.
3. Run `python3 ~/.claude/skills/potions/scripts/brew.py <slug>` to see it render, and
   `… /brew.py --check <slug>` to get measured contrast ratios.
4. Paste the measured numbers into `contrast_notes`. Don't estimate them.

## Fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `slug` | string | yes | kebab-case, unique, matches the theory filename |
| `name` | string | yes | the fantasy name, e.g. `Ember Hollow` |
| `tagline` | string | yes | one descriptive line, lowercase, no full stop |
| `kind` | `"ui"` \| `"data"` | yes | see below |
| `mood` | string[] | yes | 2–5 adjectives; how it *feels* |
| `fits` | string[] | yes | project types it suits |
| `avoid` | string[] | yes | project types it does not suit — a hard exclusion |
| `colors` | object | yes | see below |
| `theory` | string | yes | filename inside `theory/` |
| `contrast_notes` | string | yes | measured ratios, from `--check` |

### `kind`

`"ui"` — anti-vibecode-shaped: exactly one accent over a neutral ramp, plus semantics.
`"data"` — a categorical set for charts, where the colours must be distinguishable from
each other rather than subordinate to one accent.

These are filtered on, not blended. Claude picks `kind` by what's being built, so a
chart-colour set never gets proposed as a brand accent.

### `colors` for `kind: "ui"`

```json
"colors": {
  "accent": "#C2410C",
  "accent_ink": "#FFF7ED",
  "neutrals": {
    "0": "#0A0A0B", "50": "#F7F8F9", "100": "#EDEEF0", "200": "#DCDEE2",
    "300": "#BFC3C9", "400": "#9AA0A8", "500": "#71777F", "600": "#565C64",
    "700": "#3D4248", "800": "#26292E", "900": "#15171A"
  },
  "semantic": {
    "info": "#2563EB", "success": "#15803D",
    "warning": "#B45309", "danger": "#B91C1C"
  }
}
```

`accent` — the single accent. One, never two. `anti-vibecode` enforces that downstream;
this schema just refuses to store a second one.

`accent_ink` — what text/glyphs sit in when placed *on* the accent. It exists as its own
field because picking it by eye is where accessible palettes usually break: a white that
looks right on a warm accent is often tinted, not `#FFFFFF`.

`neutrals` — an object keyed by step, not an array. The steps are named because both the
generated CSS custom properties and the swatch row in the item-get art refer to them by
name (`900`, `500`, `100`). An array would force positional lookups that silently shift
the moment someone inserts a step. `0` is the extreme (near-black for dark-first ramps),
`50`–`900` run light to dark. Not every step is required, but `0`, `100`, `500` and `900`
are, since the art samples them. When a tool asks for a step you haven't defined it
substitutes the nearest one, never `0` — so a sparse ramp still renders, but `--check`
will name the step it actually measured. Define `50` and `700` too if you care about those
numbers being exact.

`semantic` — blue/green/yellow/red carrying meaning only, per house rules. Stored per
palette rather than globally because a warm palette needs warmer-tuned semantics to avoid
its success-green reading as a second accent.

### `colors` for `kind: "data"`

```json
"colors": {
  "categorical": ["#...", "#...", "..."],
  "neutrals": { "...": "..." }
}
```

`categorical` is ordered by assignment priority — first series gets the first colour.
Order them so the first 3 are maximally separable, since most charts never get past three.

### `mood`, `fits`, `avoid`

These are the whole selection surface, so write them for a reader who has only the brief
and this file.

`avoid` is the strongest signal and works as a hard exclusion, not a penalty. Put a project
type here when the palette would be actively wrong — not merely suboptimal. Overstuffing
`avoid` makes a palette unpickable; leaving it empty makes it get picked for things it
ruins. A palette that fits everything fits nothing, so if `avoid` is empty, the palette is
probably too generic to earn a slot.

### `contrast_notes`

Free text, but it must contain real measured ratios and name what was measured against
what. `python3 ~/.claude/skills/potions/scripts/brew.py --check <slug>` prints them. The point is that a future reader can
tell whether the accent is safe for body text or only for large text and UI chrome — that
distinction is the difference between a palette that ships and one that gets rewritten.
