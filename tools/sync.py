#!/usr/bin/env python3
"""Copies the shared library into both apps, so Storyarr and Starboard always use the same components.

This repository is the source. Change tokens.css, components.css, components.js or icons.svg here, check
the gallery (four themes, 175% text) and run tools/contrast.py, then run:  python3 tools/sync.py
Add --check to list what would change without writing anything.
It writes (folders set in tools/paths.py):
  Starboard  STARBOARD_WEB/css/tokens.css (font path ../fonts/), css/components.css, js/components.js,
             js/ux-notes.js, icons/sprite.svg (library icons plus Starboard's own), css/palettes.css and
             palettes.json (palettes/, for the own style's colours); and, next to the web folder,
             lib/terminal-frame.sh, the copy in run-first.sh and starboard/qr.py (from terminal/)
  Storyarr   STORYARR_SHARED/tokens.css (no @font-face or --font: Storyarr loads the font itself),
             components.css, ux-notes.js
It does not commit. Commit in each repo, then rebuild and test each app.
"""
import pathlib
import re
import sys

from paths import path

HERE = pathlib.Path(__file__).resolve().parent.parent
STARBOARD = path("STARBOARD_WEB")
STORYARR = path("STORYARR_SHARED")
CHECK = "--check" in sys.argv


def write(path, text, new=False):
    """new: a file an app copy may not have yet (another branch); --check lists it as absent, not differs."""
    old = path.read_text() if path.exists() else None
    if old == text:
        print("same   ", path)
    elif CHECK and new and old is None:
        print("absent ", path)
    elif CHECK:
        print("differs", path)
    else:
        path.write_text(text)
        print("updated", path)


tokens = (HERE / "tokens.css").read_text()
components = (HERE / "components.css").read_text()
behaviour = (HERE / "components.js").read_text()
notes = (HERE / "ux-notes.js").read_text()  # the UX notes tester (both apps)
icons = dict(re.findall(r'<symbol id="i-([^"]+)"[^>]*>(.*?)</symbol>', (HERE / "icons.svg").read_text(), re.S))
note = "\n * Copied by tools/sync.py from github.com/TheMightyTRex/design-system: change it there, not here."

if STARBOARD.exists():
    write(STARBOARD / "css/tokens.css", tokens.replace('url("fonts/', 'url("../fonts/'))
    write(STARBOARD / "css/components.css", components)
    write(STARBOARD / "js/components.js", behaviour)
    write(STARBOARD / "js/ux-notes.js", notes)
    # The palettes, for the own style's colours (owner, 13 November 2026): loaded only when one is chosen.
    write(STARBOARD / "css/palettes.css", (HERE / "palettes/app-palettes.css").read_text(), new=True)
    write(STARBOARD / "palettes.json", (HERE / "palettes/palettes.json").read_text(), new=True)
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
    first = app / "run-first.sh"
    if first.exists():
        text = first.read_text()
        a = text.index("\n", text.index("# terminal-frame: start")) + 1
        b = text.index("# terminal-frame: end")
        write(first, text[:a] + frame + text[b:])

if STORYARR.exists():
    t = re.sub(r"@font-face \{.*?\}\n\n", "", tokens, count=1, flags=re.S)
    t = re.sub(r"  --font: [^\n]*\n", "", t, count=1)
    t = t.replace(" * Shared design tokens for Storyarr and Starboard (version 1, 2 November 2026).",
                  " * Shared design tokens for Storyarr and Starboard (version 1, 2 November 2026)." + note +
                  "\n * Storyarr's copy leaves out the font (styles.css loads Atkinson Hyperlegible Next and sets --font).", 1)
    write(STORYARR / "tokens.css", t)
    write(STORYARR / "ux-notes.js", notes)
    write(STORYARR / "components.css", components.replace(
        " * Shared components for Storyarr and Starboard (version 1, 2 November 2026).",
        " * Shared components for Storyarr and Starboard (version 1, 2 November 2026)." + note, 1))

for name, folder in (("Starboard", STARBOARD), ("Storyarr", STORYARR)):
    if not folder.exists():
        print("missing", name, folder, "(set it in tools/paths.local.json)")
