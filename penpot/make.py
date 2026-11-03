"""Write the Penpot files from the library, so Penpot always matches it:

  penpot/plugin.js    plugin.src.js with the library's colours, sizes, type and icons written in
  penpot/tokens.json  every token, for Penpot's Tokens panel (Import), one set per theme plus Core

Run: python3 penpot/make.py   (after any change to tokens.css or icons.svg)"""
import json, pathlib, re

here = pathlib.Path(__file__).resolve().parent
root = here.parent
css = (root / "tokens.css").read_text()


def block(selector):
    """The custom properties inside one selector's block, in order."""
    m = re.search(r"^" + re.escape(selector) + r"\s*\{(.*?)\n\s*\}", css, re.S | re.M)
    body = re.sub(r"/\*.*?\*/", "", m.group(1), flags=re.S)
    return dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body))


light = block(":root")
dark = block(':root[data-theme="dark"]')
contrast = block(":root.pref-contrast")
contrast_dark = block(":root.pref-contrast.is-dark")

# The cascade, as in a browser: each theme is Light with the later blocks on top.
THEMES = {
    "Light": {**light},
    "Dark": {**light, **dark},
    "High contrast": {**light, **contrast},
    "High contrast dark": {**light, **dark, **contrast, **contrast_dark},
}


def resolve(value, props, depth=0):
    """A CSS colour as (hex, opacity), or None when it is not a plain colour."""
    value = value.strip()
    if depth > 8:
        return None
    m = re.fullmatch(r"var\((--[\w-]+)\)", value)
    if m:
        return resolve(props.get(m.group(1), ""), props, depth + 1)
    if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return value.lower(), 1
    if re.fullmatch(r"#[0-9a-fA-F]{3}", value):
        return "#" + "".join(c * 2 for c in value[1:]).lower(), 1
    m = re.fullmatch(r"rgb\(\s*(\d+)\s+(\d+)\s+(\d+)\s*(?:/\s*([\d.]+))?\s*\)", value)
    if m:
        r, g, b = (int(x) for x in m.groups()[:3])
        return f"#{r:02x}{g:02x}{b:02x}", float(m.group(4) or 1)
    m = re.fullmatch(r"color-mix\(in srgb,\s*(.+?)\s+([\d.]+)%,\s*transparent\)", value)
    if m:
        base = resolve(m.group(1), props, depth + 1)
        return (base[0], round(base[1] * float(m.group(2)) / 100, 3)) if base else None
    return None


COLOUR = re.compile(r"--(color|status|chart|series)-")
themes = {}
for name, props in THEMES.items():
    themes[name] = {}
    for key, value in props.items():
        if COLOUR.match(key):
            c = resolve(value, props)
            if c:
                themes[name][key[2:]] = {"hex": c[0], "opacity": c[1]}

px = lambda v: round(float(re.search(r"([\d.]+)rem", v).group(1)) * 16) if "rem" in v else int(re.search(r"(\d+)px", v).group(1))
core = {
    "space": {k[2:]: px(v) for k, v in light.items() if k.startswith("--space-")},
    "text": {k[2:]: px(v) for k, v in light.items() if re.match(r"--text-(xs|sm|md|lg|xl|2xl)$", k)},
    "weight": {k[2:]: int(v) for k, v in light.items() if k.startswith("--weight-")},
    "size": {k[2:]: px(v) for k, v in light.items()
             if re.match(r"--(control-h|control-h-compact|icon-(sm|md|lg)|header-h|tabs-h|rail-w|panel-w|dialog-w|focus-w|status-edge-w)$", k)},
}

sprite = (root / "icons.svg").read_text()
icons = {m.group(1): m.group(2) for m in re.finditer(r'<symbol id="i-([\w-]+)"[^>]*>(.*?)</symbol>', sprite, re.S)}
used = (root / "tools" / "icons.txt").read_text().split()
icons = {k: icons[k] for k in dict.fromkeys(used) if k in icons}

data = {"font": "Atkinson Hyperlegible Next", "themes": themes, "core": core, "icons": icons}
src = (here / "plugin.src.js").read_text()
assert "/*DATA*/null" in src
# The type-checking lines are for editors only. Penpot runs plugins in SES, which refuses any code that
# contains the text of an import expression or an HTML comment, even inside a comment.
src = "\n".join(line for line in src.splitlines() if not line.startswith(("/// <reference", "/** @typedef {import(")))
code = ("// Made by penpot/make.py from plugin.src.js, tokens.css and icons.svg: change those, not this file.\n"
        + src.replace("/*DATA*/null", json.dumps(data, separators=(",", ":"))) + "\n")
for refused in ("import(", "<!--", "-->"):
    assert refused not in code, f"plugin.js contains {refused!r}, which Penpot's sandbox refuses"
# A build number and a new address for each build, so no browser can keep running an old plugin.js.
import hashlib
stamp = hashlib.sha256(code.encode()).hexdigest()[:10]
assert '"/*BUILD*/"' in code
code = code.replace('"/*BUILD*/"', f'"{stamp}"')
(here / "plugin.js").write_text(code)
manifest = json.loads((here / "manifest.json").read_text())
manifest["code"] = f"plugin.js?v={stamp}"
(here / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

# Tokens for Penpot's Tokens panel: Core, then one colour set per theme, and a theme for each.
def tok(value, kind):
    return {"$value": value, "$type": kind}

tokens = {"Core": {
    "space": {k.replace("space-", ""): tok(f"{v}", "spacing") for k, v in core["space"].items()},
    "font-size": {k.replace("text-", ""): tok(f"{v}", "fontSizes") for k, v in core["text"].items()},
    "font-weight": {k.replace("weight-", ""): tok(str(v), "fontWeights") for k, v in core["weight"].items()},
    "size": {k: tok(f"{v}", "sizing") for k, v in core["size"].items()},
    "radius": {"none": tok("0", "borderRadius")},
}}
for name, colours in themes.items():
    tokens[name] = {}
    for key, c in colours.items():
        group, _, rest = key.partition("-")
        value = c["hex"] if c["opacity"] == 1 else f"rgba({int(c['hex'][1:3], 16)}, {int(c['hex'][3:5], 16)}, {int(c['hex'][5:7], 16)}, {c['opacity']})"
        tokens[name].setdefault(group, {})[rest] = tok(value, "color")
tokens["$themes"] = [{"name": n, "group": "Theme", "selectedTokenSets": {"Core": "enabled", n: "enabled"}} for n in themes]
tokens["$metadata"] = {"tokenSetOrder": ["Core", *themes]}
(here / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")

print("penpot/manifest.json: plugin.js?v=" + stamp)
print("penpot/plugin.js:", ", ".join(f"{n} {len(c)} colours" for n, c in themes.items()), f"| {len(icons)} icons")
print("penpot/tokens.json:", len(tokens) - 2, "sets")
