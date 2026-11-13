#!/usr/bin/env python3
"""Writes the colour palettes: one CSS file each in palettes/, for building a new design or site.

A palette is a different colour list for the same design system. A new project loads tokens.css, then one
palette file, then components.css: every component looks and behaves the same, only the colours change
(page tints, surfaces, the accent, focus, the count and the logo, in Light and Dark). Status colours and
chart series stay the same, so meanings never change. High contrast keeps its own fixed colours, so it
stays as strong as it can be. Teal, in tokens.css itself, is the default and needs no file.

The neutrals are the default neutrals turned to the palette's hue, so lightness, and therefore contrast,
stays close to the default. It also writes the gallery's Palettes section. tools/contrast.py checks every
palette.

Run: python3 tools/palettes.py && python3 tools/build.py && python3 tools/contrast.py
"""
import colorsys
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "palettes"

# The default (Teal) neutrals, read off tokens.css.
NEUTRALS = {
    "light": {"color-bg": "#f0f5ff", "color-header": "#fcfdff", "color-surface": "#f7faff",
              "color-surface-raised": "#ffffff", "color-surface-sunken": "#e4ebf7", "color-text": "#141416",
              "color-text-muted": "#424b5b", "color-border": "#7d879a", "color-divider": "#c2cddf"},
    "dark": {"color-bg": "#101827", "color-header": "#141e2e", "color-surface": "#1c2738",
             "color-surface-raised": "#232f42", "color-surface-sunken": "#0c1220", "color-text": "#f3f4f6",
             "color-text-muted": "#a4aec1", "color-border": "#6f7b91", "color-divider": "#303c51"},
}

# name: (label, what it suits, neutral hue in degrees, neutral saturation scale, light colours, dark colours)
PALETTES = {
    "indigo": ("Indigo", "Calm and focused: tools, dashboards, reading", 235, 1.0,
               dict(accent="#4338ca", count="#a61e4d", tile="#312e81", star="#c2410c"),
               dict(accent="#a5b4fc", count="#b8336a", tile="#c7d2fe", star="#fdba74")),
    "forest": ("Forest", "Natural and steady: libraries, gardens, health", 140, 0.7,
               dict(accent="#2f6b3a", count="#9a3412", tile="#1f4d2b", star="#c2410c"),
               dict(accent="#86d39a", count="#b4461b", tile="#bbf7d0", star="#fdba74")),
    "plum": ("Plum", "Warm and personal: media, music, journals", 290, 0.8,
             dict(accent="#7e2a8f", count="#a14400", tile="#4a1d5c", star="#c2410c"),
             dict(accent="#e2a6f0", count="#b4461b", tile="#f0d4fa", star="#fcd34d")),
    "ember": ("Ember", "Bright and lively: home, food, events", 28, 0.8,
              dict(accent="#a43e12", count="#1d4ed8", tile="#7c2d12", star="#1e40af"),
              dict(accent="#ffb38a", count="#2563eb", tile="#fed7aa", star="#93c5fd")),
    "graphite": ("Graphite", "Neutral and technical: servers, admin, documents", 220, 0.15,
                 dict(accent="#1d4ed8", count="#b4461b", tile="#1f2937", star="#c2410c"),
                 dict(accent="#93c5fd", count="#b4461b", tile="#e5e7eb", star="#fdba74")),
}


def rgb(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))


def hexa(c):
    return "#" + "".join(f"{round(max(0, min(1, x)) * 255):02x}" for x in c)


def rehue(h, hue, scale):
    _, l, s = colorsys.rgb_to_hls(*rgb(h))
    return hexa(colorsys.hls_to_rgb(hue / 360, l, min(1, s * scale)))


def mix(a, b, t):
    return hexa(tuple(x * (1 - t) + y * t for x, y in zip(rgb(a), rgb(b))))


def lum(h):
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in rgb(h)]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def colours(mode, hue, scale, c):
    v = {k: (h if k == "color-surface-raised" and mode == "light" else rehue(h, hue, scale))
         for k, h in NEUTRALS[mode].items()}
    if mode == "light":
        v["color-header"] = mix(v["color-bg"], "#ffffff", 0.85)
        v["color-panel-header"] = "#ffffff"
        v["color-accent-soft"] = mix(c["accent"], "#ffffff", 0.88)
        v["color-accent-text"] = "#ffffff"
    else:
        v["color-panel-header"] = v["color-surface-raised"]
        v["color-accent-soft"] = mix(c["accent"], v["color-bg"], 0.80)
        v["color-accent-text"] = v["color-bg"] if lum(c["accent"]) > 0.3 else "#ffffff"
    v["color-accent"] = c["accent"]
    v["color-focus"] = c["accent"]
    v["color-count"] = c["count"]
    v["color-count-text"] = "#ffffff"
    v["color-logo-tile"] = c["tile"]
    v["color-logo-star"] = c["star"]
    return v


def rule(sel, v, indent=""):
    body = "\n".join(f"{indent}  --{k}: {h};" for k, h in v.items())
    return f"{indent}{sel} {{\n{body}\n{indent}}}"


OUT.mkdir(exist_ok=True)
data = {}
for name, (label, suits, hue, scale, light, dark) in PALETTES.items():
    lv, dv = colours("light", hue, scale, light), colours("dark", hue, scale, dark)
    data[name] = {"label": label, "suits": suits, "light": lv, "dark": dv}
    # :where() keeps each rule as weak as the theme it replaces, and leaves High contrast alone.
    (OUT / f"{name}.css").write_text("\n".join([
        f"/* {label} palette for the TRex Design System. {suits}.",
        "   Load after tokens.css and before components.css. Written by tools/palettes.py: edit that, not this. */",
        rule(":root:where(:not(.pref-contrast))", lv),
        "@media (prefers-color-scheme: dark) {",
        rule(':root:not([data-theme="light"]):where(:not(.pref-contrast))', dv, "  "),
        "}",
        rule(':root[data-theme="dark"]:where(:not(.pref-contrast))', dv),
        "",
    ]))
(OUT / "palettes.json").write_text(json.dumps(data, indent=2) + "\n")

# Every palette in one file for an app that lets people choose (Starboard's own style, owner, 13 November 2026:
# "add the design system colour options in the settings page"). The app sets data-palette="forest" on <html>, and
# tools/sync.py copies this file in. Each rule is :where()-weak against High contrast, so High contrast and the app's
# own styles win; Teal, the default, is tokens.css with no data-palette.
app = ["/* Every palette for an app where people choose one: set data-palette on <html>. Load after tokens.css.",
       "   Written by tools/palettes.py: edit that, not this. Teal, the default, needs no data-palette. */"]
for name, d in data.items():
    root = f':root[data-palette="{name}"]'
    app += [rule(f"{root}:where(:not(.pref-contrast))", d["light"]),
            "@media (prefers-color-scheme: dark) {",
            rule(f'{root}:not([data-theme="light"]):where(:not(.pref-contrast))', d["dark"], "  "),
            "}",
            rule(f'{root}[data-theme="dark"]:where(:not(.pref-contrast))', d["dark"])]
(OUT / "app-palettes.css").write_text("\n".join(app) + "\n")

# The gallery section: each palette as swatches and a small sample, in Light and Dark side by side. The sample
# sets the palette's colours on its own box, so the rest of the gallery keeps its own.
TOKENS = (ROOT / "tokens.css").read_text()
DARK_STATUS = dict(re.findall(r"--(status-[\w-]+):\s*(#[0-9a-fA-F]{6})",
                              TOKENS[TOKENS.index(':root[data-theme="dark"] {'):TOKENS.index("color-scheme: dark;", TOKENS.index(':root[data-theme="dark"] {'))]))


def sample(v, mode):
    v = {**v, **DARK_STATUS} if mode == "dark" else v
    style = ";".join(f"--{k}:{h}" for k, h in v.items()) + f";color-scheme:{mode}"
    sw = "".join(f'<span class="g-pal__sw" style="background:var(--{k})" title="--{k}"></span>'
                 for k in ("color-bg", "color-surface-raised", "color-text", "color-accent", "color-accent-soft",
                           "color-count", "color-logo-tile", "color-logo-star"))
    return (f'<div class="g-pal__mode" style="{style}"><div class="g-pal__bar"><span class="g-pal__logo">'
            f'<svg viewBox="0 0 32 32" width="20" height="20" aria-hidden="true" focusable="false"><rect x="1" y="1" width="30" height="30" fill="var(--color-logo-tile)"/>'
            f'<circle cx="22" cy="10" r="4" fill="var(--color-logo-star)"/></svg>Your app</span>'
            f'<span class="count">3</span></div><div class="g-pal__body"><p>{"Light" if mode == "light" else "Dark"}: '
            f'body text and <a href="#palettes">a link</a>.</p><div class="actions"><button class="btn btn--primary btn--compact" type="button" tabindex="-1">Save</button>'
            f'<button class="btn btn--compact" type="button" tabindex="-1">Cancel</button><span class="chip" data-tone="success">Ready</span></div>'
            f'<div class="g-pal__sws">{sw}</div></div></div>')

cards = "\n".join(
    f'    <div class="g-pal"><h3>{d["label"]} <code>palettes/{n}.css</code></h3><p class="small muted">{d["suits"]}.</p>'
    f'<div class="g-pal__modes">{sample(d["light"], "light")}{sample(d["dark"], "dark")}</div></div>'
    for n, d in data.items())
section = f'''<!--PALETTES-->
<section class="g-section" id="palettes" aria-labelledby="palettes-h">
  <header><h2 id="palettes-h">Palettes</h2><p class="muted">Five colour lists for building a new design or site with the same components. Load <code>tokens.css</code>, then one palette file, then <code>components.css</code>. Only colours change: page tints, surfaces, the accent, focus, the count and the logo, in Light and Dark. Status colours, chart series and High contrast stay the same. Teal, the default, is <code>tokens.css</code> itself.</p></header>
  <div class="g-pals">
{cards}
  </div>
  <div class="g-notes">
    <div><h4>Use one</h4><ul><li><code>&lt;link rel="stylesheet" href="tokens.css"&gt;</code>, then <code>palettes/forest.css</code>, then <code>components.css</code>.</li><li>Pick one palette per product. An app may let people choose one (Starboard, own style): load <code>palettes/app-palettes.css</code> after <code>tokens.css</code> and set <code>data-palette</code> on <code>&lt;html&gt;</code>.</li></ul></div>
    <div><h4>Change one</h4><ul><li>Edit <code>tools/palettes.py</code>, run it, then <code>tools/build.py</code> and <code>tools/contrast.py</code> (0 failures).</li></ul></div>
  </div>
</section>
<!--END PALETTES-->'''
gallery = ROOT / "gallery.src.html"
g = gallery.read_text()
if "<!--PALETTES-->" in g:
    g = re.sub(r"<!--PALETTES-->.*?<!--END PALETTES-->", lambda m: section, g, flags=re.S)
else:
    i = g.index('<section class="g-section" id="type"')
    g = g[:i] + section + "\n\n" + g[i:]
gallery.write_text(g)
print(len(PALETTES), "palettes written:", ", ".join(d["label"] for d in data.values()))
