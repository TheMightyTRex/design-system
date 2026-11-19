#!/usr/bin/env python3
"""Writes the accent colours: one CSS file each in palettes/, and every one in app-palettes.css for an app that
lets people choose (Starboard's own style).

Since Mica became the default design (owner, 18 November 2026, DASH-479), a palette is an accent colour over Mica's
neutral greys: the accent, its soft tint, the words on it, the chosen item, the count and the logo, in Light and
Dark, and a stronger accent for High contrast and High contrast dark, so the chosen colour stays in every theme.
Surfaces, text, borders, focus, status colours and chart series stay the same, so meanings never change. Blue,
in tokens.css itself, is the default and needs no file. palettes.json carries each accent merged with the neutrals,
so an app can draw a swatch or a small picture from one list.

Run: python3 tools/palettes.py && python3 tools/build.py && python3 tools/check_accents.py
"""
import colorsys
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "palettes"
TOKENS_CSS = (ROOT / "tokens.css").read_text()


def _block(start):
    i = TOKENS_CSS.index(start)
    return dict(re.findall(r"--(color-[\w-]+):\s*(#[0-9a-fA-F]{6})", TOKENS_CSS[i:TOKENS_CSS.index("}", i)]))


_LIGHT = dict(re.findall(r"--(color-[\w-]+):\s*(#[0-9a-fA-F]{6})", TOKENS_CSS.split("color-scheme: light;")[0]))
NEUTRAL_KEYS = ("color-bg", "color-header", "color-surface", "color-surface-raised", "color-surface-sunken", "color-text",
                "color-text-muted", "color-border", "color-divider", "color-panel-header")
NEUTRALS = {"light": {k: _LIGHT[k] for k in NEUTRAL_KEYS},
            "dark": {k: {**_LIGHT, **_block(':root[data-theme="dark"] {')}[k] for k in NEUTRAL_KEYS}}
HC_BG = {"light": "#ffffff", "dark": "#000000"}

# name: (label, what it suits, light colours, dark colours). Teal is the colour before Mica.
PALETTES = {
    "teal": ("Teal", "The colour before Mica: calm and clear",
             dict(accent="#0b5f5a", count="#af4e24", tile="#0b5f5a", star="#af4e24"),
             dict(accent="#5ed3c6", count="#c0401a", tile="#5ed3c6", star="#ffb38a")),
    "indigo": ("Indigo", "Calm and focused: tools, dashboards, reading",
               dict(accent="#4338ca", count="#a61e4d", tile="#312e81", star="#c2410c"),
               dict(accent="#a5b4fc", count="#b8336a", tile="#c7d2fe", star="#fdba74")),
    "forest": ("Forest", "Natural and steady: libraries, gardens, health",
               dict(accent="#2f6b3a", count="#9a3412", tile="#1f4d2b", star="#c2410c"),
               dict(accent="#86d39a", count="#b4461b", tile="#bbf7d0", star="#fdba74")),
    "plum": ("Plum", "Warm and personal: media, music, journals",
             dict(accent="#7e2a8f", count="#a14400", tile="#4a1d5c", star="#c2410c"),
             dict(accent="#e2a6f0", count="#b4461b", tile="#f0d4fa", star="#fcd34d")),
    "ember": ("Ember", "Bright and lively: home, food, events",
              dict(accent="#a43e12", count="#1d4ed8", tile="#7c2d12", star="#1e40af"),
              dict(accent="#ffb38a", count="#2563eb", tile="#fed7aa", star="#93c5fd")),
    "graphite": ("Graphite", "Neutral and technical: servers, admin, documents",
                 dict(accent="#3d4f6b", count="#b4461b", tile="#1f2937", star="#c2410c"),
                 dict(accent="#b9c6da", count="#b4461b", tile="#e5e7eb", star="#fdba74")),
}


def rgb(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))


def hexa(c):
    return "#" + "".join(f"{round(max(0, min(1, x)) * 255):02x}" for x in c)


def mix(a, b, t):
    return hexa(tuple(x * (1 - t) + y * t for x, y in zip(rgb(a), rgb(b))))


def lum(h):
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in rgb(h)]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def stronger(h, bg, need=7.0):
    """The accent moved in lightness (same hue) until it has `need`:1 on the High contrast page."""
    hue, l, s = colorsys.rgb_to_hls(*rgb(h))
    step = -0.01 if lum(bg) > 0.5 else 0.01
    while ratio(hexa(colorsys.hls_to_rgb(hue, l, s)), bg) < need and 0 < l < 1:
        l += step
    return hexa(colorsys.hls_to_rgb(hue, max(0, min(1, l)), s))


def accent_set(mode, c):
    """The accent colours for one theme (light, dark, contrast, contrast-dark)."""
    base = "dark" if mode in ("dark", "contrast-dark") else "light"
    if mode.startswith("contrast"):
        a = stronger(c["accent"], HC_BG[base])
        soft = mix(a, HC_BG[base], 0.85 if base == "light" else 0.78)
        return {"color-accent": a, "color-accent-soft": soft, "color-control-active": soft,
                "color-accent-text": "#ffffff" if base == "light" else "#000000",
                "color-logo-tile": a, "color-logo-star": "#000000" if base == "light" else "#ffffff"}
    bg = NEUTRALS[base]["color-bg"]
    soft = mix(c["accent"], "#ffffff", 0.88) if base == "light" else mix(c["accent"], bg, 0.78)
    return {"color-accent": c["accent"], "color-accent-soft": soft, "color-control-active": soft,
            "color-accent-text": "#ffffff" if lum(c["accent"]) < 0.3 else "#000000",
            "color-count": c["count"], "color-count-text": "#ffffff",
            "color-logo-tile": c["tile"], "color-logo-star": c["star"]}


def rule(sel, v, indent=""):
    body = "\n".join(f"{indent}  --{k}: {h};" for k, h in v.items())
    return f"{indent}{sel} {{\n{body}\n{indent}}}"


OUT.mkdir(exist_ok=True)
for old in OUT.glob("*.css"):  # only the palettes this file still makes
    if old.stem not in PALETTES and old.name != "app-palettes.css":
        old.unlink()
data = {}
SELECTORS = {  # (theme, selector suffix); :where() keeps the light and dark rules as weak as the theme they replace
    "light": ":where(:not(.pref-contrast))",
    "dark": '[data-theme="dark"]:where(:not(.pref-contrast))',
    "contrast": '.pref-contrast:not([data-theme="dark"]):not(.is-dark)',
    "contrast-dark": '.pref-contrast:is([data-theme="dark"], .is-dark)',
}


def rules(root, d):
    # Dark only when chosen (data-theme="dark"): light is the default (owner, 18 November 2026).
    return [rule(root + SELECTORS["light"], d["accent"]["light"]),
            rule(root + SELECTORS["dark"], d["accent"]["dark"]),
            rule(root + SELECTORS["contrast"], d["accent"]["contrast"]),
            rule(root + SELECTORS["contrast-dark"], d["accent"]["contrast-dark"])]


for name, (label, suits, light, dark) in PALETTES.items():
    acc = {m: accent_set(m, light if m in ("light", "contrast") else dark) for m in ("light", "dark", "contrast", "contrast-dark")}
    data[name] = {"label": label, "suits": suits, "light": {**NEUTRALS["light"], **acc["light"], "color-focus": _LIGHT["color-focus"]},
                  "dark": {**NEUTRALS["dark"], **acc["dark"]}, "accent": acc}
    (OUT / f"{name}.css").write_text("\n".join([
        f"/* {label} accent for the TRex Design System. {suits}.",
        "   Load after tokens.css and before components.css. Written by tools/palettes.py: edit that, not this. */",
        *rules(":root", data[name]), ""]))
(OUT / "palettes.json").write_text(json.dumps({k: {x: v[x] for x in ("label", "suits", "light", "dark", "accent")} for k, v in data.items()}, indent=2) + "\n")

# Every accent in one file for an app that lets people choose (Starboard's own style): the app sets
# data-palette="forest" on <html>, and tools/sync.py copies this file in. Blue, the default, is tokens.css.
app = ["/* Every accent colour for an app where people choose one: set data-palette on <html>. Load after tokens.css.",
       "   Written by tools/palettes.py: edit that, not this. Blue, the default, needs no data-palette. */"]
for name, d in data.items():
    app += rules(f':root[data-palette="{name}"]', d)
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
  <header><h2 id="palettes-h">Accent colours</h2><p class="muted">Six accent colours over Mica's neutral greys. Load <code>tokens.css</code>, then one palette file, then <code>components.css</code>. Only the accent changes: links, the main button, the chosen item, the count and the logo, in Light, Dark and both High contrast themes. Surfaces, text, focus, status colours and chart series stay the same. Blue, the default, is <code>tokens.css</code> itself; Teal is the colour before Mica.</p></header>
  <div class="g-pals">
{cards}
  </div>
  <div class="g-notes">
    <div><h4>Use one</h4><ul><li><code>&lt;link rel="stylesheet" href="tokens.css"&gt;</code>, then <code>palettes/forest.css</code>, then <code>components.css</code>.</li><li>Pick one accent per product. An app may let people choose one (Starboard, own style): load <code>palettes/app-palettes.css</code> after <code>tokens.css</code> and set <code>data-palette</code> on <code>&lt;html&gt;</code>.</li></ul></div>
    <div><h4>Change one</h4><ul><li>Edit <code>tools/palettes.py</code>, run it, then <code>tools/build.py</code> and <code>tools/check_accents.py</code> (0 failures).</li></ul></div>
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
