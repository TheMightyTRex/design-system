"""Expand {{i:name}}, {{i-lg:name}} and {{i-xl:name extra-class}} into SVG icons, and <!--ICONS--> into
the sprite, for every *.src.html given (or all of them). Run: python3 tools/build.py [files]."""
import re, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
sprite = (root / "icons.svg").read_text()
have = set(re.findall(r'id="i-([\w-]+)"', sprite))
def icon(m):
    size, rest = m.group(1), m.group(2).split()
    name, extra = rest[0], " ".join(rest[1:])
    cls = {"i": "i", "i-lg": "i i-lg", "i-xl": "i i-xl"}[size] + (" " + extra if extra else "")
    return f'<svg class="{cls}" aria-hidden="true" focusable="false"><use href="#i-{name}"/></svg>'
files = [pathlib.Path(f).resolve() for f in sys.argv[1:]] or list(root.rglob("*.src.html"))
for f in files:
    out = re.sub(r"\{\{(i|i-lg|i-xl):([^}]+)\}\}", icon, f.read_text())
    missing = sorted(set(re.findall(r'href="#i-([\w-]+)"', out)) - have)
    out = out.replace("<!--ICONS-->", sprite)
    target = f.with_name(f.name.replace(".src.html", ".html"))
    target.write_text(out)
    print(target.relative_to(root), "missing icons: " + ", ".join(missing) if missing else "")
