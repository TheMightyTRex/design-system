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

# name: (label, what it suits, light colours, dark colours[, surfaces]). Teal is the colour before Mica.
# Surfaces (owner, 20 November 2026: "allow background changes"): a palette may also tint the page, the cards and
# the lines in Light and Dark, as the Hallmark themes do (Dusk, Rose, Amber and Lime are after Nutlope/hallmark, MIT).
# High contrast keeps pure white or black whatever the palette. Text, status colours and chart series never change.
DUSK_SURFACES = {
    "light": {"color-bg": "#eff0f6", "color-header": "#eff0f6", "color-surface": "#f8f8fc", "color-surface-sunken": "#e5e7f0",
              "color-border": "#6c6f80", "color-divider": "#7e8196"},
    "dark": {"color-bg": "#0e1017", "color-header": "#0e1017", "color-surface": "#151820", "color-surface-raised": "#1c202b",
             "color-surface-sunken": "#0a0c11", "color-panel-header": "#1c202b", "color-text-muted": "#c3c8d8",
             "color-border": "#8d93a8", "color-divider": "#6b7186"},
}
ROSE_SURFACES = {
    "light": {"color-bg": "#f8f5ed", "color-header": "#f8f5ed", "color-surface": "#fdfbf6", "color-surface-sunken": "#efe9dc",
              "color-text": "#17224f"},
    "dark": {"color-bg": "#191315", "color-header": "#191315", "color-surface": "#21191c", "color-surface-raised": "#2a2024",
             "color-surface-sunken": "#120d0f", "color-panel-header": "#2a2024", "color-text-muted": "#d4c6cb",
             "color-border": "#a08f95", "color-divider": "#7a6a70"},
}
AMBER_SURFACES = {
    "light": {"color-bg": "#f4f2ee", "color-header": "#f4f2ee", "color-surface": "#fbfaf7", "color-surface-sunken": "#e9e6df",
              "color-border": "#706c66", "color-divider": "#83807a"},
    "dark": {"color-bg": "#0d1013", "color-header": "#0d1013", "color-surface": "#14181c", "color-surface-raised": "#1b2025",
             "color-surface-sunken": "#090b0d", "color-panel-header": "#1b2025", "color-text-muted": "#c4c8cc",
             "color-border": "#8e959c", "color-divider": "#6b7279"},
}
LIME_SURFACES = {
    "light": {"color-bg": "#f1f4f2", "color-header": "#f1f4f2", "color-surface": "#f9fbfa", "color-surface-sunken": "#e5eae7",
              "color-border": "#6a716d", "color-divider": "#7d8580"},
    "dark": {"color-bg": "#04090c", "color-header": "#04090c", "color-surface": "#0b1317", "color-surface-raised": "#111b20",
             "color-surface-sunken": "#020507", "color-panel-header": "#111b20", "color-text-muted": "#bfcbd0",
             "color-border": "#86969d", "color-divider": "#62737a"},
}
PALETTES = {
    "teal": ("Teal", "The colour before Mica: calm and clear",
             dict(accent="#0b5f5a", count="#af4e24", tile="#0b5f5a", star="#af4e24"),
             dict(accent="#5ed3c6", count="#c0401a", tile="#5ed3c6", star="#ffb38a")),
    "dusk": ("Dusk", "Periwinkle on blue slate: quiet evenings, reading",
             dict(accent="#4753ab", count="#a61e4d", tile="#2e368b", star="#c2410c"),
             dict(accent="#acbcff", count="#b8336a", tile="#c7d2fe", star="#fdba74"), DUSK_SURFACES),
    "lime": ("Lime", "Lime on blue-black: sharp and technical",
             dict(accent="#3a5700", count="#a61e4d", tile="#2e4e00", star="#c2410c"),
             dict(accent="#bcf053", count="#b8336a", tile="#d9f99d", star="#fdba74"), LIME_SURFACES),
    "rose": ("Rose", "Fluorescent pink on warm paper: playful, media",
             dict(accent="#a62a65", count="#1d4ed8", tile="#880046", star="#c2410c"),
             dict(accent="#ff99c0", count="#2563eb", tile="#ff99c0", star="#93c5fd"), ROSE_SURFACES),
    "amber": ("Amber", "Amber on graphite: signals, servers, night",
              dict(accent="#874e00", count="#1d4ed8", tile="#693200", star="#1e40af"),
              dict(accent="#f7b83d", count="#2563eb", tile="#fde68a", star="#93c5fd"), AMBER_SURFACES),
    "graphite": ("Graphite", "Neutral and technical: servers, admin, documents",
                 dict(accent="#3d4f6b", count="#b4461b", tile="#1f2937", star="#c2410c"),
                 dict(accent="#b9c6da", count="#b4461b", tile="#e5e7eb", star="#fdba74")),
}
# Palettes saved before 20 November 2026, for an app to move people on: the nearest new one.
RENAMED = {"indigo": "dusk", "plum": "rose", "ember": "amber", "forest": "lime"}


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


def accent_set(mode, c, surfaces=None):
    """The accent colours for one theme (light, dark, contrast, contrast-dark), with the palette's own surfaces in
    Light and Dark."""
    base = "dark" if mode in ("dark", "contrast-dark") else "light"
    own = (surfaces or {}).get(base, {}) if not mode.startswith("contrast") else {}
    if mode.startswith("contrast"):
        a = stronger(c["accent"], HC_BG[base])
        soft = mix(a, HC_BG[base], 0.85 if base == "light" else 0.78)
        return {"color-accent": a, "color-accent-soft": soft, "color-control-active": soft,
                "color-accent-text": "#ffffff" if base == "light" else "#000000",
                "color-logo-tile": a, "color-logo-star": "#000000" if base == "light" else "#ffffff"}
    bg = own.get("color-bg", NEUTRALS[base]["color-bg"])
    soft = mix(c["accent"], "#ffffff", 0.88) if base == "light" else mix(c["accent"], bg, 0.78)
    return {**own, "color-accent": c["accent"], "color-accent-soft": soft, "color-control-active": soft,
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


for name, (label, suits, light, dark, *more) in PALETTES.items():
    surfaces = more[0] if more else None
    acc = {m: accent_set(m, light if m in ("light", "contrast") else dark, surfaces) for m in ("light", "dark", "contrast", "contrast-dark")}
    data[name] = {"label": label, "suits": suits, "light": {**NEUTRALS["light"], **acc["light"], "color-focus": _LIGHT["color-focus"]},
                  "dark": {**NEUTRALS["dark"], **acc["dark"]}, "accent": acc}
    (OUT / f"{name}.css").write_text("\n".join([
        f"/* {label} accent for the TRex Design System. {suits}.",
        "   Load after tokens.css and before components.css. Written by tools/palettes.py: edit that, not this. */",
        *rules(":root", data[name]), ""]))
(OUT / "palettes.json").write_text(json.dumps({k: {x: v[x] for x in ("label", "suits", "light", "dark", "accent")} for k, v in data.items()}, indent=2) + "\n")
(OUT / "renamed.json").write_text(json.dumps(RENAMED, indent=2) + "\n")

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
  <header><h2 id="palettes-h">Accent colours</h2><p class="muted">Six colours. Teal and Graphite are accents over Mica's neutral greys; Dusk, Lime, Rose and Amber also tint the page and cards in Light and Dark, after the Hallmark themes. Load <code>tokens.css</code>, then one palette file, then <code>components.css</code>. The accent changes links, the main button, the chosen item, the count and the logo in every theme. High contrast keeps pure white or black; focus, status colours and chart series never change. Blue, the default, is <code>tokens.css</code> itself; Teal is the colour before Mica.</p></header>
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
