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

# Each app's own logo, as in the app.
STARBOARD_LOGO = ('<svg class="s-logo" viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
                  '<rect x="3" y="3" width="12" height="12" fill="var(--color-logo-tile)"/>'
                  '<rect x="3" y="17" width="12" height="12" fill="var(--color-logo-tile)"/>'
                  '<rect x="17" y="17" width="12" height="12" fill="var(--color-logo-tile)"/>'
                  '<path d="M23 3.5l1.9 4.4 4.7.4-3.6 3.1 1.1 4.6-4.1-2.5-4.1 2.5 1.1-4.6-3.6-3.1 4.7-.4Z" fill="var(--color-logo-star)"/></svg>')
STORYARR_LOGO = ('<svg class="s-logo" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
                 '<rect width="64" height="64" fill="#c2552c"/>'
                 '<path d="M8 26c8-3 16-3 23 1v26c-7-4-15-4-23-1z" fill="#fff"/>'
                 '<path d="M56 26c-8-3-16-3-23 1v26c7-4 15-4 23-1z" fill="#fff"/>'
                 '<rect x="25" y="13" width="4" height="10" fill="#fff"/><rect x="30" y="7" width="4" height="16" fill="#fff"/>'
                 '<rect x="35" y="11" width="4" height="12" fill="#fff"/></svg>')

# The two apps whose boards the site shows.
APPS = {
    "starboard": {
        "name": "Starboard", "logo": STARBOARD_LOGO, "repo": "https://github.com/TheMightyTRex/starboard",
        "about": "An accessible dashboard for a home media server: the apps it runs, downloads, storage, disk "
                 "health and backups. Plain HTML and JavaScript, using the library as it is.",
    },
    "storyarr": {
        "name": "Storyarr", "logo": STORYARR_LOGO, "repo": "https://github.com/TheMightyTRex/storyarr",
        "about": "Follow authors and series and keep your audiobook library complete. Built with React, which "
                 "wraps the library's classes in its own components.",
    },
}

# The main menu (header row 1), the same on every page of the site. Paths are from the site's root.
MAIN = [
    ("components", "gallery.html", "layout-grid", "Components"),
    ("boards", "areas/index.html", "monitor", "Boards"),
    ("guides", "https://github.com/TheMightyTRex/design-system/tree/main/docs", "file-text", "Guides"),
    ("resources", "resources/index.html", "wrench", "Resources"),
]

# Each main menu item's own pages (header row 2), when it has more than one.
SUB = {
    "boards": [("areas/index-starboard.html", STARBOARD_LOGO, "Starboard"),
               ("areas/index-storyarr.html", STORYARR_LOGO, "Storyarr")],
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
  svg.s-logo { flex: none; width: 20px; height: 20px; }
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


def _icon(icon):
    """A Lucide icon name, or an app's own logo as an SVG."""
    return icon if icon.startswith("<svg") else f"{{{{i:{icon}}}}}"


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


def page(*, root, main, current, title, body, side=None, css="", note="", script=""):
    """root: the path from the page to the site's root ("../"). main: the main menu item this page is in.
    current: the page's own path from the root, to mark it in row 2. side: a left menu (side_from_body)."""
    main_tabs = "".join(
        f'<a href="{_href(root, path)}"{_current(key == main)}>{{{{i:{icon}}}}}<span class="menu-tabs__label">{name}</span></a>'
        for key, path, icon, name in MAIN)
    sub = SUB.get(main, [])
    row2 = ""
    if sub:
        tabs = "".join(
            f'<a href="{_href(root, path)}"{_current(path == current)}>{_icon(icon)}<span class="menu-tabs__label">{name}</span></a>'
            for path, icon, name in sub)
        label = next(name for key, _, _, name in MAIN if key == main)
        row2 = f'\n  <div class="site-header__tabs"><nav class="menu-tabs" aria-label="{label}">{tabs}</nav></div>'
    phone = []
    for key, path, icon, name in MAIN:
        if SUB.get(key):
            # A main item with its own pages folds open to list them; the one this page is in starts open.
            here = key == main
            pages = [(p, n) for p, _, n in SUB[key]]
            if path not in [p for p, _ in pages]:
                pages.insert(0, (path, f"All {name.lower()}"))  # The item's own landing page, such as All boards.
            items = "".join(f'<li><a href="{_href(root, p)}"{_current(p == current)}>{n}</a></li>' for p, n in pages)
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
{script}
</body>
</html>
"""


# Boards ------------------------------------------------------------------------------------------------
# Each app's boards page works like the component gallery: an overview, the categories and boards in the left
# menu, and the chosen board shown in the page (an iframe, so each board keeps its own header, slide-outs and
# scripts). The address names the board (#my-library), so Back, links and a new tab all work.

BOARD_CSS = """
  .b-head { display: flex; gap: var(--space-4); align-items: center; }
  .b-head svg.s-logo, .b-card svg.s-logo { width: 56px; height: 56px; }
  .b-facts { display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-4); font-size: var(--text-sm); color: var(--color-text-muted); }
  .s-nav a[aria-current] { border-left-color: var(--color-accent); font-weight: 700; }
  .b-view { display: grid; grid-template-rows: auto minmax(0, 1fr); height: calc(100vh - var(--header-h) - var(--tabs-h)); }
  .b-view[hidden] { display: none; }
  .b-bar { display: flex; flex-wrap: wrap; gap: var(--space-2) var(--space-4); align-items: center; justify-content: space-between; padding: var(--space-3) var(--space-6); border-bottom: 1px solid var(--color-divider); }
  .b-bar h1 { font-size: var(--text-lg); }
  .b-bar .actions { gap: var(--space-2); }
  .b-frame { width: 100%; height: 100%; border: 0; background: var(--color-bg); }
  .b-cards { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-4); }
  .b-card { display: grid; gap: var(--space-3); align-content: start; }
  .b-card .b-head h2 { font-size: var(--text-xl); }
  @media (max-width: 860px) { .b-bar { padding: var(--space-3) var(--space-4); } }
"""

BOARD_SCRIPT = """<script>
  // Show the board the address names (#my-library) in the page, or the overview when it names none.
  const prefix = document.body.dataset.prefix;
  const overview = document.getElementById("b-overview");
  const view = document.getElementById("b-view");
  const frame = view.querySelector("iframe");
  const heading = document.getElementById("b-title");
  const own = document.getElementById("b-own");
  const navLinks = [...document.querySelectorAll(".s-nav a")];
  const baseTitle = document.title;
  const nameOf = (slug) => navLinks.find((a) => a.getAttribute("href") === "#" + slug)?.textContent;
  function show(moveFocus) {
    const slug = decodeURIComponent(location.hash.slice(1));
    const name = slug && nameOf(slug);
    for (const a of navLinks) {
      if (a.getAttribute("href") === (name ? "#" + slug : "#")) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    }
    overview.hidden = !!name;
    view.hidden = !name;
    if (!name) { document.title = baseTitle; frame.removeAttribute("src"); return; }
    const src = prefix + slug + ".html";
    if (frame.getAttribute("src") !== src) frame.setAttribute("src", src);
    frame.title = name + " board";
    heading.textContent = name;
    own.href = src;
    document.title = name + " · " + baseTitle;
    window.scrollTo(0, 0);
    if (moveFocus) heading.focus();
  }
  addEventListener("hashchange", () => show(true));
  show(false);
  // The board follows this page's Display choices, and its own links stay in step with the address.
  const syncDisplay = () => {
    const doc = frame.contentDocument;
    if (!doc) return;
    doc.documentElement.className = document.documentElement.className;
    if (document.documentElement.dataset.theme) doc.documentElement.dataset.theme = document.documentElement.dataset.theme;
    else doc.documentElement.removeAttribute("data-theme");
  };
  new MutationObserver(syncDisplay).observe(document.documentElement, { attributes: true, attributeFilter: ["class", "data-theme"] });
  frame.addEventListener("load", () => {
    const doc = frame.contentDocument;
    if (!doc) return;
    syncDisplay();
    // A link back to the boards list leaves the frame.
    doc.querySelectorAll('a[href^="index-"]').forEach((a) => (a.target = "_top"));
    // Moving to another board inside the frame updates the address and the menu.
    const file = frame.contentWindow.location.pathname.split("/").pop();
    if (file.startsWith(prefix)) {
      const slug = file.slice(prefix.length).replace(/\\.html$/, "");
      if (nameOf(slug) && location.hash !== "#" + slug) { history.replaceState(null, "", "#" + slug); show(false); }
    }
  });
</script>"""


def boards_page(app, body, *, date, note):
    """An app's boards page. body holds the overview's notice and sections, with links to <app>-<slug>.html."""
    a = APPS[app]
    prefix = f"{app}-"
    # Links to boards open them in this page.
    body = re.sub(rf'href="{prefix}([\w-]+)\.html"', r'href="#\1"', body)
    groups = []
    for part in re.split(r"(?=<h2[ >])", body)[1:]:
        name = re.sub(r"<[^>]+>", "", re.match(r"<h2[^>]*>(.*?)</h2>", part, re.S).group(1)).strip()
        links = re.findall(r'class="(?:card__title|row__title)"><a href="(#[\w-]+)">(.*?)</a>', part)
        if links:
            groups.append((name, links))
    count = sum(len(links) for _, links in groups)
    items = "".join(
        f'<li class="s-group">{g}</li>' + "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in links)
        for g, links in groups)
    side = (f'<nav class="s-nav" aria-labelledby="s-nav-h"><h2 id="s-nav-h">{a["name"]} boards</h2>'
            f'<ol><li><a href="#">Overview</a></li>{items}</ol></nav>')
    main = f"""<div class="page" id="b-overview">
<div class="page-head"><div class="b-head">{a["logo"]}<div class="page-head__text"><h1>{a["name"]} boards</h1><p class="page-head__summary">{a["about"]}</p></div></div></div>
<p class="b-facts"><span>{count} boards</span><span>{date}</span><span>Built only from the shared component library</span><a href="{a["repo"]}">{a["name"]} on GitHub</a></p>
{body}
</div>
<section class="b-view" id="b-view" aria-labelledby="b-title" hidden>
  <div class="b-bar"><h1 id="b-title" tabindex="-1">Board</h1><div class="actions"><a class="btn btn--compact" href="#">{{{{i:arrow-left}}}}All {a["name"]} boards</a><a class="btn btn--compact" id="b-own" href="#">{{{{i:external-link}}}}Open on its own</a></div></div>
  <iframe class="b-frame" title="Board"></iframe>
</section>"""
    out = page(root="../", main="boards", current=f"areas/index-{app}.html", title=f"{a['name']} boards", body=main,
               side=side, css=BOARD_CSS, note=note, script=BOARD_SCRIPT)
    return out.replace("<body>", f'<body data-prefix="{prefix}">', 1)


def boards_landing(counts):
    """The Boards landing page: both apps, each with its logo, what it is and how many boards it has."""
    cards = "".join(
        f'<li class="card b-card"><div class="b-head">{a["logo"]}<h2 class="card__title"><a href="index-{key}.html">{a["name"]}</a></h2></div>'
        f'<p>{a["about"]}</p><p class="b-facts"><span>{counts[key]} boards</span></p></li>'
        for key, a in APPS.items())
    body = f"""<div class="page" style="max-width:1100px">
<div class="page-head"><div class="page-head__text"><h1>Boards</h1><p class="page-head__summary">Every area of Starboard and Storyarr as a full page, built only from the shared component library.</p></div></div>
<ul class="b-cards">{cards}</ul>
<div class="prose">
<h2>What a board is</h2>
<p>A board is one page of an app, designed with the library before it is built. Each one starts with what changed and why, then shows the whole page at desktop width, then the part that changes on a phone.</p>
<p>Slide-outs, menus and dialogs work, so a board can be tried as well as read. Choose an app, then a category and a board in the menu.</p>
</div>
</div>"""
    return page(root="../", main="boards", current="areas/index.html", title="Boards", body=body, css=BOARD_CSS,
                note="Made by areas/make_index.py")
