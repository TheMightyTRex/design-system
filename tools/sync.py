#!/usr/bin/env python3
"""Copies the shared library into the apps that carry a copy, so they always use the same components.

This repository is the source. Change tokens.css, components.css, components.js or icons.svg here, check
the gallery (four themes, 175% text) and run tools/contrast.py, then run:  python3 tools/sync.py
Add --check to list what would change without writing anything (it exits with 1 when a copy differs).
It writes (folders set in tools/paths.py):
  Starboard    STARBOARD_WEB/css/tokens.css (font path ../fonts/), css/components.css, js/components.js,
               (the core only, with each part in css/parts/ and js/parts/, once the app has a js/parts folder:
               tools/parts.py), icons/sprite.svg (library icons plus Starboard's own), css/palettes.css and
               palettes.json (palettes/, for the own style's colours); and, next to the web folder,
               lib/terminal-frame.sh, the copy in run-first.sh, starboard/qr.py (from terminal/) and
               tools/verbose-check.py, the Plain English check (warns only)
  Stallboard   STALLBOARD_DS/tokens.css, components.css, components.js and fonts/ (the store's assets/ds folder)
  Plug-ins     PLUGINS_DIR/tv-station/ds-tokens.css (the tokens, for the schedule grid pages) and
               PLUGINS_DIR/outside-services/ds.css (tokens and components) with font.woff2, for the status page.
               A plug-in whose copy changes needs a patch version bump and a changelog line in the plug-ins repository.
It does not commit. A file the library no longer has (RETIRED) is listed as "retired" while an app still has a
copy, for the app to remove with git rm; sync.py never deletes anything. Commit in each repo, then rebuild and test each app.
Storyarr (retired on 11 November 2026) is no longer synced.
"""
import pathlib
import re
import sys

import parts
from paths import path

HERE = pathlib.Path(__file__).resolve().parent.parent
STARBOARD = path("STARBOARD_WEB")
STALLBOARD = path("STALLBOARD_DS")
PLUGINS = path("PLUGINS_DIR")
CHECK = "--check" in sys.argv
DIFFERS = []  # every copy that differs or is absent, for the exit code of --check


def write(path, text, new=False):
    """new: a file an app copy may not have yet (another branch); --check lists it as absent, not differs."""
    old = path.read_text() if path.exists() else None
    if old == text:
        print("same   ", path)
    elif CHECK and new and old is None:
        print("absent ", path)
        DIFFERS.append(path)
    elif CHECK:
        print("differs", path)
        DIFFERS.append(path)
    else:
        path.write_text(text)
        print("updated", path)


tokens = (HERE / "tokens.css").read_text()
components = (HERE / "components.css").read_text()
behaviour = (HERE / "components.js").read_text()
# No longer in the library: ux-notes.js, the UX notes tester, replaced by Snaglist (DEV-05, 13 November 2026:
# github.com/TheMightyTRex/snaglist, which each app copies in itself).
RETIRED = {"Starboard": ["js/ux-notes.js"]}
icons = dict(re.findall(r'<symbol id="i-([^"]+)"[^>]*>(.*?)</symbol>', (HERE / "icons.svg").read_text(), re.S))
note = "\n * Copied by tools/sync.py from github.com/TheMightyTRex/design-system: change it there, not here."

if STARBOARD.exists():
    write(STARBOARD / "css/tokens.css", tokens.replace('url("fonts/', 'url("../fonts/'))
    # Parts (DASH-507): an app with a js/parts folder loads the core on every page and a part only where it is used.
    # Until the app has that folder it gets the whole files, as before, so its pages never lose a component.
    if (STARBOARD / "js/parts").is_dir():
        core_css, parts_css = parts.css(components)
        core_js, parts_js = parts.js(behaviour)
        write(STARBOARD / "css/components.css", core_css)
        write(STARBOARD / "js/components.js", core_js)
        if not CHECK:
            (STARBOARD / "css/parts").mkdir(exist_ok=True)
        for name in parts_js:
            write(STARBOARD / "css/parts" / f"{name}.css", parts_css[name], new=True)
            write(STARBOARD / "js/parts" / f"{name}.js", parts_js[name], new=True)
        for name in parts.css_only(components):  # styles with no script: a page loads the file and nothing else
            write(STARBOARD / "css/parts" / f"{name}.css", parts_css[name], new=True)
    else:
        write(STARBOARD / "css/components.css", components)
        write(STARBOARD / "js/components.js", behaviour)
    # The palettes, for the own style's colours (owner, 13 November 2026): loaded only when one is chosen.
    write(STARBOARD / "css/palettes.css", (HERE / "palettes/app-palettes.css").read_text(), new=True)
    write(STARBOARD / "palettes.json", (HERE / "palettes/palettes.json").read_text(), new=True)
    # The brand logos of the places for backups (Simple Icons, CC0): one small file, loaded only where a page uses them.
    write(STARBOARD / "icons/services.svg", (HERE / "service-logos.svg").read_text(), new=True)
    sprite = STARBOARD / "icons/sprite.svg"
    own = dict(re.findall(r'<symbol id="i-([^"]+)"[^>]*>(.*?)</symbol>', sprite.read_text(), re.S)) if sprite.exists() else {}
    merged = {**own, **icons}
    write(sprite, "\n".join(['<svg xmlns="http://www.w3.org/2000/svg">'] + [
        f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round">{merged[k]}</symbol>' for k in sorted(merged)] + ["</svg>"]) + "\n")
    # The terminal frame and QR encoder (terminal/): the installer reads lib/terminal-frame.sh, the Run first script
    # carries a copy between its "terminal-frame" lines (it arrives on its own through curl), and the terminal
    # set-up's feedback draws its QR code with starboard/qr.py.
    app = STARBOARD.parent
    frame = (HERE / "terminal/terminal-frame.sh").read_text()
    write(app / "lib/terminal-frame.sh", frame)
    write(app / "starboard/qr.py", (HERE / "terminal/qr.py").read_text())
    # The Plain English check (26 November 2026): warns about the lines a pull request adds, never fails (tools/verbose-check.py ci).
    write(app / "tools/verbose-check.py", (HERE / "tools/verbose-check.py").read_text(), new=True)
    first = app / "run-first.sh"
    if first.exists():
        text = first.read_text()
        a = text.index("\n", text.index("# terminal-frame: start")) + 1
        b = text.index("# terminal-frame: end")
        write(first, text[:a] + frame + text[b:])

# Stallboard, the store (STALLBOARD_DS is its assets/ds folder): byte-for-byte copies, and the font beside them.
if STALLBOARD.exists():
    write(STALLBOARD / "tokens.css", tokens)
    write(STALLBOARD / "components.css", components)
    write(STALLBOARD / "components.js", behaviour)
    for name in ("atkinson-hyperlegible-next.woff2", "LICENSE-OFL.txt"):
        font = HERE / "fonts" / name
        target = STALLBOARD / "fonts" / name
        same = target.exists() and target.read_bytes() == font.read_bytes()
        if same:
            print("same   ", target)
        elif CHECK:
            print("differs", target)
            DIFFERS.append(target)
        else:
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(font.read_bytes())
            print("updated", target)

# The two plug-ins that carry their own pinned copy (the other plug-ins are drawn by Starboard itself). The header
# names no commit, so --check can tell a real difference from a new commit that changed nothing here.
PLUGIN_HEAD = ("/* The TRex Design System's {what}, copied by tools/sync.py (github.com/TheMightyTRex/design-system).\n"
               "   Do not change this copy: change the design system and run sync.py again. */\n")
if PLUGINS.exists():
    plugin_font = 'url("font.woff2")'
    t = tokens.replace('url("fonts/atkinson-hyperlegible-next.woff2")', plugin_font)
    if (PLUGINS / "tv-station").is_dir():
        write(PLUGINS / "tv-station/ds-tokens.css", PLUGIN_HEAD.format(what="tokens.css") + t)
    if (PLUGINS / "outside-services").is_dir():
        write(PLUGINS / "outside-services/ds.css", PLUGIN_HEAD.format(what="tokens.css and components.css") + t + "\n" + components)
        font = HERE / "fonts/atkinson-hyperlegible-next.woff2"
        target = PLUGINS / "outside-services/font.woff2"
        if target.exists() and target.read_bytes() == font.read_bytes():
            print("same   ", target)
        elif CHECK:
            print("differs", target)
            DIFFERS.append(target)
        else:
            target.write_bytes(font.read_bytes())
            print("updated", target)

for name, folder in (("Starboard", STARBOARD), ("Stallboard", STALLBOARD), ("the plug-ins", PLUGINS)):
    for old in RETIRED.get(name, []) if folder.exists() else []:
        if (folder / old).exists():
            print("retired", folder / old, "(no longer in the library: remove it from the app with git rm)")
    if not folder.exists():
        print("missing", name, folder, "(set it in tools/paths.local.json)")
if CHECK and DIFFERS:
    print(f"{len(DIFFERS)} copies differ: run python3 tools/sync.py")
    sys.exit(1)
