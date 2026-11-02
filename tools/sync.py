#!/usr/bin/env python3
"""Copies the shared library into both apps, so Storyarr and Starboard always use the same components.

This repository is the source. Change tokens.css, components.css, components.js or icons.svg here, check
the gallery (four themes, 175% text) and run tools/contrast.py, then run:  python3 tools/sync.py
Add --check to list what would change without writing anything.
It writes (folders set in tools/paths.py):
  Starboard  STARBOARD_WEB/css/tokens.css (font path ../fonts/), css/components.css, js/components.js,
             js/ux-notes.js, icons/sprite.svg (library icons plus Starboard's own)
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


def write(path, text):
    old = path.read_text() if path.exists() else None
    if old == text:
        print("same   ", path)
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
    sprite = STARBOARD / "icons/sprite.svg"
    own = dict(re.findall(r'<symbol id="i-([^"]+)"[^>]*>(.*?)</symbol>', sprite.read_text(), re.S)) if sprite.exists() else {}
    merged = {**own, **icons}
    write(sprite, "\n".join(['<svg xmlns="http://www.w3.org/2000/svg">'] + [
        f'<symbol id="i-{k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round">{merged[k]}</symbol>' for k in sorted(merged)] + ["</svg>"]) + "\n")

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
