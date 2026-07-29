#!/usr/bin/env python3
"""Render cauldron's ASCII art with ANSI truecolor swatches.

The art is the point of the skill, so it lives here rather than being pasted into
SKILL.md — one copy, no drift.

Usage:
    brew.py --banner            the wordmark banner
    brew.py <slug>              the item-get for one palette
    brew.py --check <slug>      measured contrast ratios for contrast_notes
    brew.py --list              slugs on the shelf
    brew.py --help              this message

Colour degrades on its own: set NO_COLOR, or a TERM of "dumb", and the swatches
print as blocks with their hexes underneath rather than emitting escapes that
would show as garbage. Stdlib only.
"""

import json
import os
import sys
from pathlib import Path

PALETTES = Path(__file__).resolve().parent.parent / "references" / "palettes.json"

RESET = "\x1b[0m"
INDENT = " " * 27


def color_enabled():
    # An unset TERM is normal in hook-spawned and non-interactive shells, and those
    # still render escapes fine. Only refuse when something actually says not to.
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("TERM") == "dumb":
        return False
    return True


def rgb(hex_str):
    h = hex_str.lstrip("#")
    if len(h) == 3:  # #abc shorthand
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"bad hex: {hex_str!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def fg(hex_str, text):
    if not color_enabled():
        return text
    r, g, b = rgb(hex_str)
    return f"\x1b[38;2;{r};{g};{b}m{text}{RESET}"


# --- contrast -------------------------------------------------------------

def _linear(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_str):
    r, g, b = (_linear(c) for c in rgb(hex_str))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def rating(ratio):
    if ratio >= 7:
        return "AAA body"
    if ratio >= 4.5:
        return "AA body"
    if ratio >= 3:
        return "large text / UI only"
    return "FAILS"


# --- data -----------------------------------------------------------------

def load():
    try:
        with open(PALETTES) as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"cauldron: no shelf at {PALETTES}")
    except json.JSONDecodeError as e:
        # This file is hand-edited, so a stray comma is the likeliest failure.
        sys.exit(f"cauldron: {PALETTES.name} is not valid JSON — {e}")


def find(slug):
    for p in load():
        if p["slug"] == slug:
            return p
    sys.exit(f"cauldron: no palette '{slug}'. Try --list.")


def step(neutrals, want):
    """Nearest available neutral step.

    SCHEMA.md only requires 0/100/500/900, so anything asking for 50 or 700 has
    to cope with them being absent rather than raising KeyError at render time.
    """
    if want in neutrals:
        return want, neutrals[want]

    # Only numbered steps can be reasoned about by distance. A palette may carry
    # extra named keys, and those must be skipped rather than crash int().
    numeric = {k: v for k, v in neutrals.items() if k.isdigit()}
    if not numeric:
        sys.exit("cauldron: palette neutrals have no numbered steps.")
    w = int(want)

    # Step 0 is the dark extreme, not a point on the 50-900 light-to-dark run.
    # Substituting by raw distance would hand back 50 — the lightest surface
    # standing in for the darkest — so it resolves to the darkest step instead.
    if w == 0:
        k = max(numeric, key=int)
        return k, numeric[k]

    # Otherwise nearest, with 0 excluded so near-black can't stand in for a ramp
    # step. Ties break away from mid-ramp: a substitute that overshoots keeps the
    # contrast it was chosen for, one that lands at 500 quietly loses it.
    cands = [k for k in numeric if k != "0"] or list(numeric)
    k = min(cands, key=lambda x: (abs(int(x) - w), -int(x) if w >= 500 else int(x)))
    return k, numeric[k]


def swatches(palette):
    """Named swatches of a kind:kit palette, as (name, hex) pairs."""
    sw = palette["colors"].get("swatches", [])
    if not sw:
        sys.exit(f"cauldron: '{palette['slug']}' is kind:kit with no swatches.")
    return [(s["name"], s["hex"]) for s in sw]


def samples(palette):
    """The (label, hex) pairs the art shows, per palette kind."""
    c = palette["colors"]
    n = c.get("neutrals", {})
    if palette.get("kind") == "kit":
        # Kit names are far too long to sit under a swatch block without
        # blowing the row past 80 columns, so the row is numbered and the
        # names go in a legend underneath.
        return [(str(i + 1), h) for i, (_, h) in enumerate(swatches(palette)[:6])]
    if palette.get("kind") == "data":
        cats = c.get("categorical", [])
        if not cats:
            sys.exit(f"cauldron: '{palette['slug']}' is kind:data with no categorical colours.")
        return [(str(i + 1), h) for i, h in enumerate(cats[:5])]
    return [
        ("accent", c["accent"]),
        ("ink", c["accent_ink"]),
        *[(k, v) for k, v in (step(n, s) for s in ("900", "500", "100"))],
    ]


# --- art ------------------------------------------------------------------

BANNER = r"""                .-.
                |{fill}|         ___   _  _   _ _    ___  ___  ___  _  _
               (___)       / __| /_\| | | | |  |   \| _ \/ _ \| \| |
              \  |  /     | (__ / _ \ |_| | |__| |) |   / (_) | .` |
               \ | /       \___/_/ \_\___/|____|___/|_|_\\___/|_|\_|
                (o o)
                 \_/
                 /|\
                /   \
"""


def banner():
    # Nothing picked yet, so the vial holds the same glyph unlit.
    print(BANNER.format(fill="≈"))


def swatch_rows(palette):
    """Swatch block row plus aligned labels.

    Colour mode uses 6-wide blocks so the widest label ("accent") sits exactly
    under its own block; narrower blocks push the label row out of column.

    Without colour the blocks carry no information, so the hexes go underneath
    on their own row. Columns stay 8 wide there — enough for "#C2410C" — which
    keeps the whole row inside 80 columns so it can't soft-wrap into the figure.
    """
    picks = samples(palette)
    if color_enabled():
        blocks = "".join(fg(h, "██████") + " " for _, h in picks).rstrip()
        labels = "".join(lab.center(6) + " " for lab, _ in picks).rstrip()
        return [blocks, labels]
    return [
        "".join("███".center(7) + " " for _ in picks).rstrip(),
        "".join(lab.center(7) + " " for lab, _ in picks).rstrip(),
        "".join(h.center(7) + " " for _, h in picks).rstrip(),
    ]


def item_get(palette):
    fill_hex = palette["colors"].get("accent") or samples(palette)[0][1]
    fill = fg(fill_hex, "≈")
    # Letter-spaced for the trophy feel, with a wider gap holding words apart.
    spaced = "   ".join(" ".join(w) for w in palette["name"].upper().split())
    sw = swatch_rows(palette)
    lines = [
        "                .-.",
        f"                |{fill}|",
        "               (___)",
        "              \\  |  /",
        "               \\ | /",
        f"                (o o)      You obtained  ·  {spaced}",
        f'                 \\_/          "{palette["tagline"]}"',
        "                 /|\\",
        f"                /   \\      {sw[0]}",
    ]
    lines += [INDENT + extra for extra in sw[1:]]
    if palette.get("kind") == "kit":
        lines.append("")
        named = swatches(palette)
        width = max(len(n) for n, _ in named)
        for i, (nm, h) in enumerate(named, 1):
            marker = f"{i}" if i <= 6 else " "
            lines.append(f"{INDENT}{marker:>2}  {fg(h, '██')}  {nm:<{width}}  {h}")
        if len(named) > 6:
            # Never let a truncated row read as the whole kit.
            lines.append(f"{INDENT}     ({len(named) - 6} more not shown in the row above)")
    print("\n".join(lines))
    print()


# --- check ----------------------------------------------------------------

def check(palette):
    c = palette["colors"]
    n = c.get("neutrals", {})
    print(f"{palette['name']} — measured contrast\n")

    if palette.get("kind") == "kit":
        named = swatches(palette)
        dark = min(named, key=lambda s: luminance(s[1]))
        light = max(named, key=lambda s: luminance(s[1]))
        for nm, h in named:
            if nm != dark[0]:
                r = contrast(h, dark[1])
                print(f"  {nm + ' on ' + dark[0]:<34} {r:5.2f}:1   {rating(r)}")
        print(f"\n  lightest: {light[0]} ({light[1]})   darkest: {dark[0]} ({dark[1]})")

        # A kit lives or dies on whether its members are tellable apart. Two
        # swatches at the same lightness read as one colour in greyscale, to
        # many colour-blind viewers, and to anyone glancing at a small chip.
        print("\n  separation between neighbours")
        weak = []
        for (an, ah), (bn, bh) in zip(named, named[1:]):
            r = contrast(ah, bh)
            if r < 1.5:
                weak.append((an, bn))
            print(f"    {an + ' / ' + bn:<34} {r:5.2f}:1"
                  f"{'' if r >= 1.5 else '   <- near-isoluminant'}")
        if weak:
            print(f"\n  {len(weak)} neighbouring pair(s) under 1.5:1. Separate those by role,")
            print("  position or shape — colour alone will not carry the distinction.")
        print()
        return

    if palette.get("kind") == "data":
        # Categorical sets aren't text, so what matters is that every series
        # stays visible against both the light and the dark surface.
        light_k, light = step(n, "50")
        dark_k, dark = step(n, "0")
        pairs = []
        for i, h in enumerate(c.get("categorical", [])):
            pairs.append((f"series {i + 1} on neutral-{light_k}", h, light))
            pairs.append((f"series {i + 1} on neutral-{dark_k}", h, dark))
    else:
        l_k, light = step(n, "50")
        d_k, dark = step(n, "0")
        body_k, body = step(n, "700")
        inv_k, inv = step(n, "100")
        pairs = [
            (f"accent on neutral-{l_k}", c["accent"], light),
            ("accent_ink on accent", c["accent_ink"], c["accent"]),
            (f"accent on neutral-{d_k}", c["accent"], dark),
            (f"neutral-{body_k} on neutral-{l_k}", body, light),
            (f"neutral-{inv_k} on neutral-{d_k}", inv, dark),
        ]

    for label, a, b in pairs:
        r = contrast(a, b)
        print(f"  {label:<28} {r:5.2f}:1   {rating(r)}")
    print("\nPaste the relevant lines into contrast_notes.")


# --- cli ------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__.strip())
        return
    if args[0] == "--banner":
        return banner()
    if args[0] == "--list":
        for p in load():
            print(f"{p['slug']:<20} {p.get('kind', '?'):<5} {p['tagline']}")
        return
    if args[0] == "--check":
        if len(args) < 2:
            sys.exit("cauldron: --check needs a slug.")
        return check(find(args[1]))
    if args[0].startswith("-"):
        sys.exit(f"cauldron: unknown option '{args[0]}'. Try --help.")
    item_get(find(args[0]))


if __name__ == "__main__":
    main()
