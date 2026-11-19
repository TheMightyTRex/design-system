#!/usr/bin/env python3
"""Checks the contrast of every token pair the components draw, for every accent colour, in Light, Dark, High
contrast and High contrast dark (WCAG 2.2 AA: 4.5:1 for text, 3:1 for the parts of controls, card edges and rules,
the glass layers at their worst case (black or white right behind them) and the page wash,
hover edges, the current-item bar and the focus ring). Fails on any pair that falls short.

The themes come from tokens.css and the accents from palettes/palettes.json (written by tools/palettes.py); Blue,
the default, is tokens.css itself. Colours made with color-mix(), such as the hover fill, are worked out over each
background they can sit on, as the browser does. Disabled controls are left out: WCAG 2.2 does not ask for contrast
on them, and every disabled control also says so in words or with the not-allowed pointer. The focus ring sits 2px
outside the control (outline-offset), so it is checked against the surfaces round it, not the control's own fill;
a count badge's number is checked against the badge, which carries no meaning of its own.

Run: python3 tools/check_accents.py [--report accent-report.txt]   (exit code 1 if any pair fails)
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = (ROOT / "tokens.css").read_text()


def block(start):
    i = CSS.index(start)
    j = CSS.index("{", i)
    depth, k = 1, j + 1
    while depth:
        depth += {"{": 1, "}": -1}.get(CSS[k], 0)
        k += 1
    return dict((n, v.split("/*")[0].strip()) for n, v in re.findall(r"--([\w-]+):\s*([^;]+);", CSS[j + 1:k - 1]))


root = dict((n, v.split("/*")[0].strip()) for n, v in re.findall(r"--([\w-]+):\s*([^;]+);", CSS.split("color-scheme: light;")[0]))
dark = {**root, **block(':root[data-theme="dark"] {')}
hc = {**root, **block(":root.pref-contrast {")}
hcd = {**dark, **hc, **block(':root.pref-contrast[data-theme="dark"],')}
THEMES = {"light": ("Light", root), "dark": ("Dark", dark), "contrast": ("High contrast", hc), "contrast-dark": ("High contrast dark", hcd)}

ACCENTS = {"blue": ("Blue (default)", {})}
for name, p in json.loads((ROOT / "palettes" / "palettes.json").read_text()).items():
    ACCENTS[name] = (p["label"], {m: {k.removeprefix("--"): v for k, v in p["accent"][m].items()} for m in THEMES})


def rgb(h):
    return [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]


def hexa(c):
    return "#" + "".join(f"{round(max(0, min(1, x)) * 255):02x}" for x in c)


def lum(h):
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in rgb(h)]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def mixhex(a, b, share_b):
    return hexa([x * (1 - share_b) + y * share_b for x, y in zip(rgb(a), rgb(b))])


def resolve(t, name, over=None, seen=()):
    """A token's colour as #rrggbb; `over` is the background a see-through colour sits on."""
    v = t[name].strip()
    m = re.fullmatch(r"var\(--([\w-]+)(?:,\s*(.+))?\)", v)
    if m:
        if m.group(1) in t and m.group(1) not in seen:
            return resolve(t, m.group(1), over, seen + (name,))
        return resolve({**t, "_": m.group(2)}, "_", over) if m.group(2) else None
    m = re.fullmatch(r"color-mix\(in srgb,\s*var\(--([\w-]+)\)\s*(\d+)%,\s*transparent\)", v)
    if m:
        top, share = resolve(t, m.group(1), over), int(m.group(2)) / 100
        base = over or resolve(t, "color-surface")
        return hexa([a * share + b * (1 - share) for a, b in zip(rgb(top), rgb(base))])
    return v.lower() if re.fullmatch(r"#[0-9a-fA-F]{6}", v) else None


SURFACES = ["color-bg", "color-header", "color-surface", "color-surface-raised", "color-surface-sunken",
            "color-panel-header", "color-slide-header"]
TONES = ["success", "info", "neutral", "warning", "danger", "muted"]


def pairs(glass=True):
    """(foreground, background, ratio needed, what it is). A background "hover:X" is the hover fill over X; "glass:X"
    is the glass layer X with black (light themes) or white (dark themes) right behind it, its worst case; "tint" is
    the page wash at its strongest, and "glass-hover:X" the hover fill on that worst-case glass."""
    out = []
    if glass:
        for layer in ("color-header", "color-surface-raised"):
            out += [("color-text", f"glass:{layer}", 4.5, "text on glass"), ("color-text-muted", f"glass:{layer}", 4.5, "secondary text on glass"),
                    ("color-accent", f"glass:{layer}", 4.5, "links on glass"), ("color-text", f"glass-hover:{layer}", 4.5, "a hovered menu item on glass"),
                    ("color-border", f"glass:{layer}", 3, "buttons and fields on glass"), ("color-focus", f"glass:{layer}", 3, "the focus ring on glass"),
                    ("color-hover-edge", f"glass-hover:{layer}", 3, "the hover edge on glass")]
        out += [("color-text", "tint", 4.5, "text on the page wash"), ("color-text-muted", "tint", 4.5, "secondary text on the page wash"),
                ("color-accent", "tint", 4.5, "links on the page wash"), ("color-divider", "tint", 3, "card edges on the page wash"),
                ("color-border", "tint", 3, "fields and buttons on the page wash"), ("color-focus", "tint", 3, "the focus ring on the page wash")]
    for bg in SURFACES + ["color-accent-soft", "color-control-active"] + [f"hover:{s}" for s in SURFACES]:
        out += [("color-text", bg, 4.5, "text"), ("color-text-muted", bg, 4.5, "secondary text"),
                ("color-accent", bg, 4.5, "links and quiet buttons")]
    for bg in SURFACES:
        out += [("color-border", bg, 3, "edges of fields and buttons"), ("color-focus", bg, 3, "the focus ring"),
                ("color-accent", bg, 3, "the current-item bar"), ("color-hover-edge", bg, 3, "the hover edge on menus"),
                ("color-hover-edge", f"hover:{bg}", 3, "the hover edge against its own fill")]
    for bg in ["color-bg", "color-surface"]:
        out.append(("color-divider", bg, 3, "card edges and rules"))
    out += [("color-accent", "color-control-active", 3, "the current-item bar on its fill"),
            ("color-accent-text", "color-accent", 4.5, "words on main buttons"),
            ("color-count-text", "color-count", 4.5, "the number on a count badge"),
            ("color-logo-tile", "color-header", 3, "the logo"),
            ("color-text", "status-danger-bg", 4.5, "words on an error message"),
            ("color-text-muted", "status-danger-bg", 4.5, "detail on an error message"),
            ("color-surface-raised", "status-danger-fg", 4.5, "words on a red main button")]
    for tone in TONES:
        out += [(f"status-{tone}-fg", f"status-{tone}-bg", 4.5, f"{tone} chips and messages")]
        for bg in ["color-bg", "color-surface", "color-surface-raised"]:
            out.append((f"status-{tone}-fg", bg, 4.5, f"{tone} words and edges on a card"))
    for n in (1, 2):
        out += [(f"chart-{n}", "color-surface", 3, "chart lines"), (f"chart-{n}", "color-surface-raised", 3, "chart lines")]
    for n in range(1, 8):
        out += [(f"series-{n}", "color-surface", 3, "chart series"), (f"series-{n}", "color-surface-raised", 3, "chart series")]
    return out


def main():
    report = []
    fails = 0
    summary = []
    for key, (label, acc) in ACCENTS.items():
        for mode, (theme, base) in THEMES.items():
            t = {**base, **acc.get(mode, {})}
            worst_text, worst_ui, bad = 99, 99, []
            dark_theme = mode in ("dark", "contrast-dark")
            behind = "#ffffff" if dark_theme else "#000000"
            alpha = int(t.get("glass-alpha", "100%").rstrip("%")) / 100

            def glass_of(layer):
                return mixhex(resolve(t, layer), behind, 1 - alpha)

            for fg, bg, need, what in pairs(glass=not mode.startswith("contrast")):
                over = None
                if bg.startswith("glass:"):
                    b = glass_of(bg[6:])
                elif bg.startswith("glass-hover:"):
                    over = glass_of(bg[12:])
                    b = resolve(t, "color-hover", over)
                elif bg == "tint":
                    b = mixhex(resolve(t, "color-bg"), resolve(t, "color-accent"), int(t.get("page-tint", "0%").rstrip("%")) / 100)
                elif bg.startswith("hover:"):
                    over = resolve(t, bg[6:])
                    b = resolve(t, "color-hover", over)
                else:
                    b = resolve(t, bg)
                f = resolve(t, fg, b if fg == "color-hover" else None)
                if not (f and b):
                    continue
                f = f if not f.startswith("#") or len(f) == 7 else f
                r = ratio(f, b)
                if need >= 4.5:
                    worst_text = min(worst_text, r)
                else:
                    worst_ui = min(worst_ui, r)
                if r < need:
                    bad.append(f"    FAIL {fg} on {bg} {f} on {b}: {r:.2f}:1, needs {need:g}:1 ({what})")
            fails += len(bad)
            summary.append(f"{label:16} {theme:19} lowest text {worst_text:5.2f}:1  lowest UI part {worst_ui:5.2f}:1  "
                           f"{'pass' if not bad else str(len(bad)) + ' failing'}")
            report += [summary[-1], *bad]
    text = "\n".join(["Contrast of every token pair, for every accent and theme (WCAG 2.2 AA: 4.5:1 text, 3:1 UI parts)",
                      f"{len(pairs())} pairs each in Light and Dark (glass and the page wash included), {len(pairs(False))} in High contrast", "", *report, "", f"{fails} failures"])
    if "--report" in sys.argv:
        (ROOT / sys.argv[sys.argv.index("--report") + 1]).write_text(text + "\n")
    print(text)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
