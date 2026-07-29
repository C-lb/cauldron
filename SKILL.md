---
name: skittles
description: Picks a brand colour palette from a curated library and explains the colour theory behind the pick. Use this when a project needs a colour direction it does not have yet — starting a new app, site, brand or UI from scratch — and use it even when the user doesn't say "palette", including phrasings like "what colours should this use", "pick a scheme", "give it a look", or "how should this feel". Do NOT use it when colours are already chosen: restyling an existing UI, making a built screen feel more premium, or changing one specific colour is anti-vibecode's job, not this one.
---

# skittles

A shelf of curated brand palettes. Given a brief, pick **one** outright, hand it over with
the item-get art, and explain why it's right. No candidate menus — an argued pick the user
can reject is more useful than three options they now have to adjudicate.

The palettes are stocked by hand. This skill's job is selection and rationale, not
generation.

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

## Boundary with anti-vibecode

`skittles` chooses **which** colours. `anti-vibecode` governs **how they're applied** —
flat buttons, one accent, no gradients, semantic colours carrying meaning only.

They don't overlap and shouldn't argue. If both are active, skittles supplies the hexes
and then gets out of the way. Every `kind: "ui"` palette here is already shaped to
anti-vibecode's rules (exactly one accent over a neutral ramp), so handing one over never
puts the two skills in conflict.

## Procedure

**1. Read `references/palettes.json`. Only that file.**

It's the whole selection surface, and it's written to be sufficient on its own. Don't read
the theory files yet — there's one per palette, and reading them all to choose is the
expensive way to do this. `references/SCHEMA.md` is for *authoring* palettes; you don't
need it to pick one.

**2. Filter on `kind`, then match `mood` / `fits` / `avoid`.**

`kind: "ui"` for interfaces and brands, `kind: "data"` for chart colour sets, `kind: "kit"`
for named swatch sets with no declared accent or ramp. A categorical chart set is not a
brand accent and must never be offered as one.

A kit needs more from you than a `ui` palette does. It carries no `accent`, no neutral
ramp and no semantics, so handing one over means saying which swatch should act as the
accent, what surface to build on, and what the kit doesn't contain. Its theory file makes
that argument; don't improvise it from the hexes.

`avoid` is a hard exclusion, not a penalty. If the project type is on a palette's `avoid`
list, that palette is out however well the mood fits — those lists were written by someone
who knew exactly where the palette breaks.

**3. Pick one. Judgement, not arithmetic.**

Don't score the tags and total them up. A weighted rubric over subjective adjectives
produces confident-looking numbers that hide the actual reasoning, and it can't be argued
with. Read the tags as evidence, decide, and be ready to say why in a sentence.

**4. Read that palette's theory file — `references/theory/<theory>.md`. Just the one.**

This is where the rationale comes from. Don't paraphrase from the tags; the theory file has
the actual harmony, the perceptual reasoning, and the failure modes.

**5. Render the art.**

```bash
python3 ~/.claude/skills/skittles/scripts/brew.py <slug>
```

Absolute path on purpose — the working directory during a project kickoff is the project,
not the skill, so a relative path silently fails exactly when the skill is being used for
real. Stdlib only, no install step. It prints the item-get with the vial filled in the
palette's own accent and five true-colour swatches.

**6. Report.** Format below.

## Output

The art can't carry the information on its own — terminal output isn't guaranteed to reach
the user, and colour blocks aren't copy-pasteable. So the art is the flourish and the text
is the contract. Always give both.

After running `brew.py`, write in the reply:

- **Name and tagline**, in plain text. Not only inside the art.
- **The CSS custom properties**, ready to paste, with the values read from the palette's
  `colors` object. For a `kit`, name the variables after the swatch names
  (`--fairy-dust`) rather than inventing role names the kit doesn't claim:

```css
:root {
  --accent: …;        /* colors.accent */
  --accent-ink: …;    /* colors.accent_ink */

  --n-0: …;           /* one line per step in colors.neutrals */

  --info: …;          /* the four colors.semantic entries */
  --success: …;
  --warning: …;
  --danger: …;
}
```

  Take the hexes from `palettes.json` at the time you run, never from memory — a palette
  edited since is the likeliest way to hand over a colour that no longer exists.

- **Why**, in three or four sentences drawn from the theory file: which harmony it uses,
  what the accent does perceptually, why the neutrals lean warm or cool.
- **The contrast caveat**, from `contrast_notes` — specifically whether the accent is safe
  for body text or restricted to large text and UI chrome. This is the field most likely to
  get skipped and the one most likely to cause a rewrite later.

Then say the pick can be swapped. One sentence, no menu.

## When nothing fits

Say so. Don't invent hexes.

The premise is a hand-curated shelf; a library that quietly generates a palette when it
misses isn't curated any more, and the user loses the ability to trust that anything they
got came off the shelf. Name the closest entry, say what it gets wrong for this brief, and
point at `references/SCHEMA.md` for adding one.

## Adding palettes

`references/SCHEMA.md` documents every field and the full process. `--list` shows what's on
the shelf, `--check` prints measured contrast ratios for a new entry:

```bash
python3 ~/.claude/skills/skittles/scripts/brew.py --list
python3 ~/.claude/skills/skittles/scripts/brew.py --check <slug>
```
