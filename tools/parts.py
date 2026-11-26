#!/usr/bin/env python3
"""Makes the light form of the library from the one source: the core, and a file for each part.

components.css and components.js hold every component, and the gallery, the boards and the help centre load them
whole. Some components are large and few pages use them (the log viewer, the combobox, the schedule picker). Those
are marked in the source as parts, from "part: name" to "/part". An app that counts every byte (Starboard,
lightweight first, DASH-507) loads the core on every page and a part only on the pages that use it:

    css/components.css              the core (components.css without the parts)
    css/parts/<name>.css            one part's styles, in @layer shared
    js/components.js                the core (components.js without the parts)
    js/parts/<name>.js              one part's behaviour: load it after the core, and after the parts it needs

tools/sync.py writes those from this module. Run this file to check the source: python3 tools/parts.py
(it lists each part with its size, and fails if a part reaches for something the core does not hand it).
docs/LIBRARY.md, Parts, has the rules for marking one.
"""
import gzip
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
OPEN = re.compile(r"^\s*/\* part: ([a-z-]+)(?:; (.*?))? \*/\s*$")
CLOSE = re.compile(r"^\s*/\* /part \*/\s*$")
LINE = re.compile(r"\s*// part\s*$")


def _cut(text, name_of_file):
    """The source without its parts, and each part's lines with what its opening line says about it."""
    core, parts, now = [], {}, None
    for n, line in enumerate(text.split("\n"), 1):
        opened = OPEN.match(line)
        if opened:
            if now:
                raise ValueError(f"{name_of_file}:{n}: part {opened.group(1)} starts inside part {now}")
            now = opened.group(1)
            if now in parts:  # marked again: its next piece goes on the end of the same part (styles that sit apart in the file)
                continue
            said = dict(bit.split(": ", 1) for bit in (opened.group(2) or "").split("; ") if bit)
            parts[now] = {"lines": [], **{k: [x.strip() for x in v.replace(" first", "").split(",")] for k, v in said.items()},
                          "first": " first" in said.get("setup", "")}
        elif CLOSE.match(line):
            if not now:
                raise ValueError(f"{name_of_file}:{n}: /part with no part open")
            now = None
        elif now:
            parts[now]["lines"].append(line)
        elif not LINE.search(line):
            core.append(line)
    if now:
        raise ValueError(f"{name_of_file}: part {now} is never closed")
    return "\n".join(core), parts


def css(text):
    """(core, {name: file text}) from components.css."""
    core, parts = _cut(text, "components.css")
    core = re.sub(r"\n{3,}", "\n\n", core)
    return core, {name: f"/* {name}: a part of the shared components. Load it after components.css, on the pages that use it.\n"
                        " * Made by tools/parts.py from components.css in github.com/TheMightyTRex/design-system: change it there, not here. */\n"
                        "@layer shared {\n" + "\n".join(p["lines"]).rstrip() + "\n}\n" for name, p in parts.items()}


def js(text):
    """(core, {name: file text}) from components.js. A part gets the core's helpers from SharedComponents.kit, what it
    needs from other parts off SharedComponents, and gives back what it exports and its set-up."""
    core, parts = _cut(text, "components.js")
    core = re.sub(r"\n{3,}", "\n\n", core)
    kit = re.search(r"kit: \{ ([^}]+) \}", core)
    if not kit:
        raise ValueError("components.js: SharedComponents.kit is missing")
    out = {}
    for name, p in parts.items():
        needs = []
        for other in p.get("needs", []):
            if other not in parts:
                raise ValueError(f"components.js: part {name} needs {other}, which is not a part")
            needs += parts[other].get("exports", [])
        head = [f"/* {name}: a part of the shared components. Load it after components.js"
                + (f" and parts/{'.js, parts/'.join(p['needs'])}.js" if p.get("needs") else "") + ", on the pages that use it.",
                " * Made by tools/parts.py from components.js in github.com/TheMightyTRex/design-system: change it there, not here. */",
                "(() => {", "  const S = window.SharedComponents;", f"  const {{ {kit.group(1)} }} = S.kit;"]
        if needs:
            head.append(f"  const {{ {', '.join(needs)} }} = S;")
        tail = []
        if p.get("exports"):
            tail.append(f"  Object.assign(S, {{ {', '.join(p['exports'])} }});")
        for run in p.get("setup", []):
            tail.append(f"  S.addSetup({run}{', true' if p['first'] else ''});")
        out[name] = "\n".join(head + [""] + p["lines"] + [""] + tail + ["})();", ""])
    return core, out


def _names(text):
    """Names declared at the top of the library's one function (two spaces in)."""
    return {a or b for a, b in re.findall(r"^  (?:async )?function (\w+)|^  (?:const|let) (\w+)", text, re.M)}


def check():
    """Every part must stand on the kit, its own names and what it says it needs; the core must not use a part."""
    source = (HERE / "components.js").read_text()
    core, parts = _cut(source, "components.js")
    core_css, parts_css = css((HERE / "components.css").read_text())
    kit = set(re.search(r"kit: \{ ([^}]+) \}", core).group(1).split(", "))
    every = _names(source)
    problems = []
    bare = lambda code: re.sub(r"/\*.*?\*/|//[^\n]*", "", code, flags=re.S)
    for name, p in parts.items():
        code = "\n".join(p["lines"])
        own = _names(code)
        given = kit | own | {x for other in p.get("needs", []) for x in parts[other].get("exports", [])}
        for word in sorted(every - given):
            if re.search(rf"(?<![\w.$]){re.escape(word)}\b(?!\s*:)", bare(code)) and not re.search(rf"\b(?:const|let|function)\s+{word}\b|[(,]\s*{word}\s*[,)=]", code):
                problems.append(f"part {name} uses {word}, which the kit does not hand it")
        for word in p.get("exports", []) + p.get("setup", []):
            if word not in own:
                problems.append(f"part {name} says it has {word}, and does not")
        if name not in parts_css:
            problems.append(f"part {name} has no styles marked in components.css")
    moved = {x for p in parts.values() for x in _names("\n".join(p["lines"]))}
    for word in sorted(moved):
        if re.search(rf"(?<![\w.$]){re.escape(word)}\b", bare(core)):
            problems.append(f"the core uses {word}, which is in a part")
    # A part with styles and no behaviour is a styles-only part (components no page of the app loads today).
    for text, what in ((core_css, "core styles"), *((t, f"part {n} styles") for n, t in parts_css.items())):
        if text.count("{") != text.count("}"):
            problems.append(f"{what}: the braces do not match")
    size = lambda t: len(gzip.compress(t.encode(), 9))
    whole = size((HERE / "components.css").read_text()) + size(source)
    core_js, parts_js = js(source)
    print(f"whole  {whole:>7,} bytes compressed (components.css and components.js)")
    print(f"core   {size(core_css) + size(core_js):>7,}")
    for name in parts:
        print(f"  {name:<16} {size(parts_css.get(name, '')) + size(parts_js[name]):>6,}")
    for name in parts_css:
        if name not in parts:
            print(f"  {name:<16} {size(parts_css[name]):>6,}  (styles only)")
    for line in problems:
        print("PROBLEM", line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(check())
