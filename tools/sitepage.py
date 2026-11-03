"""The design system site's own pages: one header, main menu, phone menu, left menu, Display slide-out and
footer around a page's body, so every page of the site has the same menu. The logo, Display slide-out and
footer are copied from gallery.src.html, so they stay the same as the gallery's.

Used by resources/make.py, areas/storyarr-gen/b_index.py and areas/_starboard/index.py. Each writes a
.src.html file; then run tools/build.py to add the icons."""
import html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
GALLERY = (ROOT / "gallery.src.html").read_text()
LOGO = re.search(r'<svg class="g-logo".*?</svg>', GALLERY).group(0)
DISPLAY = re.search(r'<div class="side-panel-layer" id="g-panel-display" hidden>.*?</aside>\s*</div>', GALLERY, re.S).group(0)
FOOTER = re.findall(r'^<footer class="site-footer">.*</footer>$', GALLERY, re.M)[-1]

# The main menu (header row 1), the same on every page of the site. Paths are from the site's root.
MAIN = [
    ("components", "gallery.html", "layout-grid", "Components"),
    ("boards", "areas/index-storyarr.html", "monitor", "Boards"),
    ("guides", "https://github.com/TheMightyTRex/design-system/tree/main/docs", "file-text", "Guides"),
    ("resources", "resources/index.html", "wrench", "Resources"),
]

# Each main menu item's own pages (header row 2), when it has more than one.
SUB = {
    "boards": [("areas/index-storyarr.html", "book-open", "Storyarr boards"),
               ("areas/index-starboard.html", "server", "Starboard boards")],
    "resources": [("resources/index.html", "house", "Overview"),
                  ("resources/tools.html", "wrench", "Tools"),
                  ("resources/outside-tools.html", "globe", "Outside tools"),
                  ("resources/make-a-change.html", "file-pen", "Make a change"),
                  ("resources/get-feedback.html", "send", "Get feedback")],
}

CSS = """
  /* The site's own layout; not part of the library. */
  svg.i { width: var(--icon-md); height: var(--icon-md); }
  svg.i-lg { width: var(--icon-lg); height: var(--icon-lg); }
  .g-logo { flex: none; }
  .s-shell { display: grid; grid-template-columns: 240px minmax(0, 1fr); }
  .s-nav { position: sticky; top: calc(var(--header-h) + var(--tabs-h)); align-self: start; max-height: calc(100vh - var(--header-h) - var(--tabs-h)); overflow-y: auto; padding: var(--space-6) var(--space-4); border-right: 1px solid var(--color-divider); }
  .s-nav h2 { font-size: var(--text-sm); color: var(--color-text-muted); padding: 0 var(--space-3); margin-bottom: var(--space-2); }
  .s-nav ol { margin: 0; padding: 0; list-style: none; display: grid; gap: 2px; }
  .s-nav a { display: block; padding: var(--space-2) var(--space-3); color: var(--color-text); font-size: var(--text-sm); text-decoration: none; border-left: 3px solid transparent; }
  .s-nav a:hover { background: var(--color-control-active); }
  .s-nav .s-group { margin-top: var(--space-4); color: var(--color-text-muted); font-size: var(--text-xs); font-weight: 700; padding: 0 var(--space-3); }
  .s-main { min-width: 0; }
  .s-main .page h2 { scroll-margin-top: calc(var(--header-h) + var(--tabs-h) + var(--space-4)); }
  @media (max-width: 860px) {
    .s-shell { grid-template-columns: 1fr; }
    .s-nav { display: none; }
  }
"""

SCRIPT = """<script>
  // Main menu: icons only when the names do not fit (.is-compact), as in the gallery and the apps.
  const bar = document.querySelector(".site-header__bar");
  const mainTabs = bar.querySelector(".menu-tabs");
  function fit() {
    mainTabs.classList.remove("is-compact");
    if (bar.scrollWidth > bar.clientWidth || mainTabs.scrollWidth > mainTabs.clientWidth) mainTabs.classList.add("is-compact");
  }
  addEventListener("resize", fit);
  fit();
  document.querySelectorAll("#s-site-menu a").forEach((a) => a.addEventListener("click", () => document.getElementById("s-site-menu").closeLayer?.(false)));
</script>"""


def _href(root, path):
    return path if path.startswith("http") else root + path


def _current(flag):
    return ' aria-current="page"' if flag else ""


def side_from_body(body, heading):
    """The left menu from the body itself: each h2 is a group, and each link in a card or row title under it is
    an item. So the menu always lists exactly the boards the page shows."""
    groups = []
    for part in re.split(r"(?=<h2[ >])", body)[1:]:
        name = re.sub(r"<[^>]+>", "", re.match(r"<h2[^>]*>(.*?)</h2>", part, re.S).group(1)).strip()
        links = re.findall(r'class="(?:card__title|row__title)"><a href="([^"]+)">(.*?)</a>', part)
        if links:
            groups.append((name, links))
    items = "".join(
        f'<li class="s-group">{g}</li>' + "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in links)
        for g, links in groups)
    return f'<nav class="s-nav" aria-labelledby="s-nav-h"><h2 id="s-nav-h">{heading}</h2><ol>{items}</ol></nav>'


def page(*, root, main, current, title, body, side=None, css="", note=""):
    """root: the path from the page to the site's root ("../"). main: the main menu item this page is in.
    current: the page's own path from the root, to mark it in row 2. side: a left menu (side_from_body)."""
    main_tabs = "".join(
        f'<a href="{_href(root, path)}"{_current(key == main)}>{{{{i:{icon}}}}}<span class="menu-tabs__label">{name}</span></a>'
        for key, path, icon, name in MAIN)
    sub = SUB.get(main, [])
    row2 = ""
    if sub:
        tabs = "".join(
            f'<a href="{_href(root, path)}"{_current(path == current)}>{{{{i:{icon}}}}}<span class="menu-tabs__label">{name}</span></a>'
            for path, icon, name in sub)
        label = next(name for key, _, _, name in MAIN if key == main)
        row2 = f'\n  <div class="site-header__tabs"><nav class="menu-tabs" aria-label="{label}">{tabs}</nav></div>'
    phone = []
    for key, path, icon, name in MAIN:
        if SUB.get(key):
            # A main item with its own pages folds open to list them; the one this page is in starts open.
            here = key == main
            items = "".join(f'<li><a href="{_href(root, p)}"{_current(p == current)}>{n}</a></li>' for p, _, n in SUB[key])
            phone.append(
                f'<div class="phone-menu__section"{" data-current" if here else ""}><button type="button" aria-expanded="{str(here).lower()}" aria-controls="s-sm-{key}">'
                f'{{{{i-lg:{icon}}}}}{name}{{{{i:chevron-right phone-menu__chevron}}}}</button><ul id="s-sm-{key}"{"" if here else " hidden"}>{items}</ul></div>')
        else:
            phone.append(f'<div class="phone-menu__section"><a href="{_href(root, path)}"{_current(key == main)}>{{{{i-lg:{icon}}}}}{name}</a></div>')
    content = f'<main class="s-main" id="main" tabindex="-1">\n{body}\n</main>'
    if side:
        content = f'<div class="s-shell">\n{side}\n{content}\n</div>'
    return f"""<!doctype html>
<html lang="en-GB" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · TRex Design System</title>
<!-- {note or "Made by a script with tools/sitepage.py"}: change the source, not this file. -->
<link rel="stylesheet" href="{root}tokens.css">
<link rel="stylesheet" href="{root}components.css">
<style>{CSS}{css}</style>
</head>
<body>
<!--ICONS-->
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header site-header--no-rail">
  <div class="site-header__bar">
    <button class="icon-btn phone-menu-button" type="button" data-opens="s-site-menu" aria-controls="s-site-menu" aria-expanded="false">{{{{i-lg:menu}}}}<span class="visually-hidden">Menu</span></button>
    <a class="site-header__brand" href="{root}gallery.html">{LOGO.replace('<svg class="g-logo"', '<svg class="g-logo" width="28" height="28"', 1)}<span>TRex Design System</span></a>
    <nav class="menu-tabs" aria-label="Main">{main_tabs}</nav>
    <div class="site-header__actions"><button class="icon-btn" type="button" data-opens="g-panel-display" aria-haspopup="dialog" aria-expanded="false">{{{{i-lg:sun}}}}<span class="label">Display</span></button></div>
  </div>{row2}
</header>
<div class="side-panel-layer" id="s-site-menu" hidden>
  <div class="side-panel-backdrop"></div>
  <nav class="phone-menu" aria-label="Menu">
    <div class="panel-header"><span class="panel-header__brand">{LOGO.replace('<svg class="g-logo"', '<svg class="g-logo" width="24" height="24"', 1)}TRex Design System</span><button class="icon-btn" type="button" data-closes aria-label="Close menu">{{{{i:x}}}}</button></div>
    <div class="phone-menu__sections">
      {"".join(phone)}
    </div>
  </nav>
</div>
{content}
{FOOTER}
{DISPLAY}
<script src="{root}components.js"></script>
{SCRIPT}
</body>
</html>
"""
