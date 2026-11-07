"""Rebuild icons.svg from Lucide (Storyarr's node_modules, set in tools/paths.py). Run with every icon name the library needs:
python3 tools/icons.py "book-open bookmark ..." (the current list is in icons.txt)."""
import re, sys, pathlib
from paths import path
src = path("LUCIDE_ICONS")
names = sys.argv[1].split()
out = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none">']
for n in names:
    p = src/f"{n}.mjs"
    if not p.exists(): print("missing", n); continue
    t = p.read_text()
    if "node: [" not in t:
        m = re.search(r"from '\./([\w-]+)\.mjs'", t)
        if not m: print("odd", n); continue
        t = (src/f"{m.group(1)}.mjs").read_text()
    node = t[t.index("node: ["):t.index("__iconData.node;")]
    parts = []
    for m in re.finditer(r'\[\s*"(\w+)",\s*\{(.*?)\}\s*\]', node, re.S):
        tag, attrs = m.group(1), m.group(2)
        kv = re.findall(r'(\w+):\s*"([^"]*)"', attrs)
        a = " ".join(f'{"stroke-width" if k=="strokeWidth" else k}="{v}"' for k, v in kv if k != "key")
        parts.append(f"<{tag} {a}/>")
    out.append(f'<symbol id="i-{n}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{"".join(parts)}</symbol>')
# The library's own icons, drawn in Lucide's style (24 grid, 2 stroke, square corners as the library). They are not in
# Lucide, so they are added after every rebuild (TheMightyTRexUK, 7 November 2026).
OWN = {
    "help": '<path d="M3 3h18v18H3z"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    "help-new-tab": '<path d="M11 3H3v18h18v-8"/><path d="M15 3h6v6"/><path d="M21 3l-5.5 5.5"/><path d="M7.59 11a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M10.5 18h.01"/>',
}
for n, shapes in OWN.items():
    out.append(f'<symbol id="i-{n}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{shapes}</symbol>')
out.append("</svg>")
(pathlib.Path(__file__).resolve().parent.parent/"icons.svg").write_text("\n".join(out))
print(len(names), "icons")
