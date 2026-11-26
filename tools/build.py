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
def expand(text):
    """The page with its icons and the sprite filled in, and the icons the sprite lacks."""
    out = re.sub(r"\{\{(i|i-lg|i-xl):([^}]+)\}\}", icon, text)
    missing = sorted(set(re.findall(r'href="#i-([\w-]+)"', out)) - have)
    return out.replace("<!--ICONS-->", sprite), missing


# gallery.src.html is the source of the component pages: tools/site.py writes them (and gallery.html, the old address).
SKIP = {"gallery.src.html"}


def main():
    files = [pathlib.Path(f).resolve() for f in sys.argv[1:]] or [f for f in root.rglob("*.src.html") if f.name not in SKIP]
    for f in files:
        out, missing = expand(f.read_text())
        target = f.with_name(f.name.replace(".src.html", ".html"))
        target.write_text(out)
        print(target.relative_to(root), "missing icons: " + ", ".join(missing) if missing else "")


if __name__ == "__main__":
    main()
