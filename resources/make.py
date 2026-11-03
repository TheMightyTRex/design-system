"""Write the Design resources and tools pages: resources/<page>.src.html from the bodies in resources/content/,
with the gallery's header, Display slide-out and footer around each one. Then run tools/build.py to add the
icons. Run: python3 resources/make.py && python3 tools/build.py"""
import html, pathlib, re

here = pathlib.Path(__file__).resolve().parent
gallery = (here.parent / "gallery.src.html").read_text()

# (file, tab name, icon, page title)
PAGES = [
    ("index", "Overview", "house", "Design resources and tools"),
    ("tools", "Tools", "wrench", "Tools in this repository"),
    ("outside-tools", "Outside tools", "globe", "Outside tools for accessibility and testing"),
    ("make-a-change", "Make a change", "file-pen", "Make a change"),
    ("get-feedback", "Get feedback", "send", "Get feedback"),
]

# Shared parts are copied from the gallery, so they stay the same as it.
logo = re.search(r'<svg class="g-logo".*?</svg>', gallery).group(0)
display = re.search(r'<div class="side-panel-layer" id="g-panel-display" hidden>.*?</aside>\s*</div>', gallery, re.S).group(0)
footer = re.findall(r'^<footer class="site-footer">.*</footer>$', gallery, re.M)[-1]

MAIN = [
    ("../gallery.html", "layout-grid", "Components"),
    ("../areas/index-storyarr.html", "book-open", "Storyarr boards"),
    ("../areas/index-starboard.html", "server", "Starboard boards"),
    ("https://github.com/TheMightyTRex/design-system/tree/main/docs", "file-text", "Guides"),
    ("index.html", "wrench", "Resources"),
]


def page(file, tab, title):
    body = (here / "content" / f"{file}.html").read_text().strip()
    # Every command gets the library's copy button.
    body = re.sub(r'<code class="code-block">(.*?)</code>', lambda m: (
        f'<div class="command"><code class="code-block">{m.group(1)}</code><button class="copy-btn" type="button" '
        f'data-copy="{html.escape(html.unescape(m.group(1)))}" aria-label="Copy command">{{{{i:copy}}}}</button></div>'), body, flags=re.S)
    main_tabs = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if name == "Resources" else ""}>{{{{i:{icon}}}}}'
        f'<span class="menu-tabs__label">{name}</span></a>' for href, icon, name in MAIN)
    sub_tabs = "".join(
        f'<a href="{f}.html"{" aria-current=\"page\"" if f == file else ""}>{{{{i:{icon}}}}}'
        f'<span class="menu-tabs__label">{name}</span></a>' for f, name, icon, _ in PAGES)
    phone_sub = "".join(
        f'<li><a href="{f}.html"{" aria-current=\"page\"" if f == file else ""}>{name}</a></li>' for f, name, _, _ in PAGES)
    phone_main = "".join(
        f'<div class="phone-menu__section"><a href="{href}">{{{{i-lg:{icon}}}}}{name}</a></div>'
        for href, icon, name in MAIN if name != "Resources")
    return f"""<!doctype html>
<html lang="en-GB" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · TRex Design System</title>
<!-- Made by resources/make.py from resources/content/{file}.html: change that file, not this one. -->
<link rel="stylesheet" href="../tokens.css">
<link rel="stylesheet" href="../components.css">
<style>
  /* Resources pages only; not part of the library. */
  svg.i {{ width: var(--icon-md); height: var(--icon-md); }}
  svg.i-lg {{ width: var(--icon-lg); height: var(--icon-lg); }}
  .g-logo {{ flex: none; }}
  .r-page {{ max-width: 1000px; }}
  .r-page .prose {{ max-width: 80ch; }}
  .r-page .prose h2 {{ scroll-margin-top: calc(var(--header-h) + var(--tabs-h) + var(--space-4)); }}
  .r-page .cards {{ list-style: none; padding: 0; }}
  .r-page .code-block {{ white-space: pre-wrap; overflow-wrap: anywhere; }}
  .r-page li > .command, .r-page .command + .command {{ margin-top: var(--space-2); }}
  .r-next {{ display: flex; flex-wrap: wrap; gap: var(--space-3); padding-top: var(--space-6); border-top: 1px solid var(--color-divider); }}
</style>
</head>
<body>
<!--ICONS-->
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header site-header--no-rail">
  <div class="site-header__bar">
    <button class="icon-btn phone-menu-button" type="button" data-opens="r-site-menu" aria-controls="r-site-menu" aria-expanded="false">{{{{i-lg:menu}}}}<span class="visually-hidden">Menu</span></button>
    <a class="site-header__brand" href="../gallery.html">{logo.replace('<svg class="g-logo"', '<svg class="g-logo" width="28" height="28"', 1)}<span>TRex Design System</span></a>
    <nav class="menu-tabs" aria-label="Main">{main_tabs}</nav>
    <div class="site-header__actions"><button class="icon-btn" type="button" data-opens="g-panel-display" aria-haspopup="dialog" aria-expanded="false">{{{{i-lg:sun}}}}<span class="label">Display</span></button></div>
  </div>
  <div class="site-header__tabs"><nav class="menu-tabs" aria-label="Resources">{sub_tabs}</nav></div>
</header>
<div class="side-panel-layer" id="r-site-menu" hidden>
  <div class="side-panel-backdrop"></div>
  <nav class="phone-menu" aria-label="Menu">
    <div class="panel-header"><span class="panel-header__brand">{logo.replace('<svg class="g-logo"', '<svg class="g-logo" width="24" height="24"', 1)}TRex Design System</span><button class="icon-btn" type="button" data-closes aria-label="Close menu">{{{{i:x}}}}</button></div>
    <div class="phone-menu__sections">
      {phone_main}
      <div class="phone-menu__section" data-current><button type="button" aria-expanded="true" aria-controls="r-sm-1">{{{{i-lg:wrench}}}}Resources{{{{i:chevron-right phone-menu__chevron}}}}</button>
        <ul id="r-sm-1">{phone_sub}</ul></div>
    </div>
  </nav>
</div>
<main class="page r-page" id="main" tabindex="-1">
{body}
</main>
{footer}
{display}
<script src="../components.js"></script>
<script>
  // Main menu: icons only when the names do not fit (.is-compact), as in the gallery and the apps.
  const bar = document.querySelector(".site-header__bar");
  const mainTabs = bar.querySelector(".menu-tabs");
  function fit() {{
    mainTabs.classList.remove("is-compact");
    if (bar.scrollWidth > bar.clientWidth || mainTabs.scrollWidth > mainTabs.clientWidth) mainTabs.classList.add("is-compact");
  }}
  addEventListener("resize", fit);
  fit();
</script>
</body>
</html>
"""


for file, tab, icon, title in PAGES:
    (here / f"{file}.src.html").write_text(page(file, tab, title))
    print(f"resources/{file}.src.html")
