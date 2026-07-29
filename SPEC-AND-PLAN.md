# cauldron — spec + implementation plan

> Renamed three times on 2026-07-30 at Caleb's call: `cauldron` → `potions` → `skittles` → back to **`cauldron`**.
> DESIGN.md's original rejection of "potion" is left standing as provenance; both renames
> override it.

Written 2026-07-29, off the approved `DESIGN.md`. Read DESIGN.md first; this file only
adds what DESIGN.md left unspecified, plus the build order.

## Open question — resolved

**Q:** Should the vial's `≈` fill render in the picked palette's accent colour?
**A:** Yes. The potion handed over is literally the colour you got. The vial glass
(`.-.`, `(___)`) stays default terminal colour so the fill reads as fill.

## New decisions (not in DESIGN.md)

### D1 — Colour delivery: bundled script, not inline text

DESIGN.md says the swatches must render as *actual colour*, not labels. That can't happen
in my reply text: a fenced code block renders ANSI escapes literally, and unfenced ASCII
art loses its alignment to markdown. So colour has to come from a process writing to the
terminal.

**Resolution:** bundle `scripts/brew.py`. It takes a palette slug, reads `palettes.json`,
and writes the item-get art to stdout with ANSI truecolor (`\x1b[38;2;R;G;Bm`). Claude
invokes it via Bash.

**Caveat, stated plainly:** Bash stdout is shown to Claude and *usually* to the user in
Claude Code, but that isn't guaranteed by the harness. So SKILL.md requires Claude to also
restate the palette name, tagline, and hex values as plain text in its reply. The art is
the flourish; the text is the contract. If the terminal swallows the art, the user still
gets everything they need.

**Degradation:** if the terminal reports no truecolor support (`NO_COLOR` set, or `TERM`
is `dumb`), `brew.py` falls back to labelled `███` blocks with hexes underneath rather
than emitting escapes that would print as garbage.

### D2 — `brew.py` owns the art, SKILL.md does not

DESIGN.md pasted the item-get template into SKILL.md. Keeping a second copy there invites
drift. SKILL.md shows the banner once (as a picture of what the skill does) and otherwise
points at the script.

### D3 — Selection is a judgement call, not a scoring function

No weighted rubric over `mood`/`fits`/`avoid`. `avoid` is a hard exclusion; everything
else is read as evidence. A rubric would produce confident-looking arithmetic over
subjective tags, which is worse than an argued pick. SKILL.md asks for the *reason* in the
output so a bad pick is visible and correctable.

### D4 — Empty-library behaviour

The shipped library holds exactly one palette (`ember-hollow`). If nothing in the library
fits the brief, Claude says so and points at `SCHEMA.md` rather than inventing hexes on
the spot — the skill's whole premise is that Caleb stocks the shelf. Inventing a palette
would silently turn a curated library into a generator.

### D5 — Trigger scope

Fires on new-project kickoff and brand/visual work needing a colour direction. Does *not*
fire when a palette already exists in the project, or when the user asks to change one
specific colour. Restyling an existing app is anti-vibecode's job, not cauldron's.

## File manifest

| Path | Purpose |
|---|---|
| `SKILL.md` | trigger, selection procedure, output contract, anti-vibecode boundary |
| `scripts/brew.py` | renders banner + item-get with ANSI truecolor; no deps beyond stdlib |
| `references/palettes.json` | the index; ships with `ember-hollow` only |
| `references/SCHEMA.md` | field docs + how Caleb adds a palette |
| `references/theory/ember-hollow.md` | worked long-form rationale, the template for future entries |

`DESIGN.md` and this file stay in the directory as provenance.

## Build order

1. `references/SCHEMA.md` — pins the field contract everything else depends on.
2. `references/palettes.json` — `ember-hollow` filled to the schema, real hexes, measured
   contrast ratios.
3. `references/theory/ember-hollow.md` — the depth a theory file is expected to have.
4. `scripts/brew.py` — render both art modes, truecolor + fallback. Verify by running it.
5. `SKILL.md` — written last, once the pieces it references exist and their shapes are known.

Each step verified before the next: schema against the JSON, JSON against the script, script
by actually executing it.

## Done means

- `python3 scripts/brew.py ember-hollow` prints the item-get with a coloured vial fill and
  five swatches, no traceback, no external packages.
- `NO_COLOR=1 python3 scripts/brew.py ember-hollow` prints the labelled fallback.
- `python3 scripts/brew.py --banner` prints the wordmark banner.
- `palettes.json` parses and validates against every field SCHEMA.md documents.
- SKILL.md is under 500 lines and carries no *data* that lives in a reference file — no
  hexes, no palette specifics, no authoring steps. The `kind` split and the `avoid`
  hard-exclusion rule do appear in both SKILL.md and SCHEMA.md, deliberately: selection
  reads only `palettes.json`, so those two rules have to be present without SCHEMA.md
  being loaded. Duplicated rules that can't drift are fine; duplicated values are not.
