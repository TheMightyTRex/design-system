"""Write the Design resources and tools pages: resources/<page>.src.html from the bodies in resources/content/,
with the site's header, menus, Display slide-out and footer (tools/sitepage.py) around each one. Then run
tools/build.py to add the icons. Run: python3 resources/make.py && python3 tools/build.py"""
import html, pathlib, re, sys

here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "tools"))
import sitepage  # noqa: E402

# (file, page title); the tab names and icons are in tools/sitepage.py.
PAGES = [
    ("index", "Design resources and tools"),
    ("tools", "Tools in this repository"),
    ("outside-tools", "Outside tools for accessibility and testing"),
    ("make-a-change", "Make a change"),
    ("get-feedback", "Get feedback"),
]

CSS = """
  /* Resources pages only. */
  .r-page { max-width: 1000px; }
  .r-page .prose { max-width: 80ch; }
  .r-page .cards { list-style: none; padding: 0; }
  .r-page .code-block { white-space: pre-wrap; overflow-wrap: anywhere; }
  .r-page li > .command, .r-page .command + .command { margin-top: var(--space-2); }
  .r-next { display: flex; flex-wrap: wrap; gap: var(--space-3); padding-top: var(--space-6); border-top: 1px solid var(--color-divider); }
"""


def body_of(file):
    body = (here / "content" / f"{file}.html").read_text().strip()
    # Every command gets the library's copy button.
    body = re.sub(r'<code class="code-block">(.*?)</code>', lambda m: (
        f'<div class="command"><code class="code-block">{m.group(1)}</code><button class="copy-btn" type="button" '
        f'data-copy="{html.escape(html.unescape(m.group(1)))}" aria-label="Copy command">{{{{i:copy}}}}</button></div>'), body, flags=re.S)
    return f'<div class="page r-page">\n{body}\n</div>'


for file, title in PAGES:
    out = sitepage.page(root="../", main="resources", current=f"resources/{file}.html", title=title,
                        body=body_of(file), css=CSS, note=f"Made by resources/make.py from resources/content/{file}.html")
    (here / f"{file}.src.html").write_text(out)
    print(f"resources/{file}.src.html")
