#!/usr/bin/env python3
"""The design system's help centre: builds an app's Markdown help into web pages, one for each article, with
search, a collapsible menu of every article on the left, On this page following the article on the right, and the
same Display and accessibility settings as the apps. Pages use this repository's tokens.css, components.css,
components.js, fonts and icons. Layout and rules: docs/LIBRARY.md, Help centre. 7 November 2026.

Each app keeps a help-centre.json at its root (see docs/LIBRARY.md), then from the app's folder:

    python3 <design-system>/tools/help_centre/build.py [--config help-centre.json] [--out _site]

Needs Python-Markdown and pymdown-extensions (pip install markdown==3.7 pymdown-extensions==10.9), or run\ntools/help_centre/build.sh, which uses a Python container. Pages go in <out>/help/<the same path>.html,
README.md becoming index.html; links between articles point at the pages, and links to other files in the app's
repository point at GitHub.
"""
import fnmatch
import argparse
import html
import json
import pathlib
import re
import shutil

import markdown

DS = pathlib.Path(__file__).resolve().parent.parent.parent  # this design system
HERE = pathlib.Path(__file__).resolve().parent
# Set from the app's help-centre.json by configure().
ROOT = HELP = None
FOOTER_NOTE = BANNER = ""
BANNER_COUNT = 0
FAVICON = None
BANNER_LABEL = "Advertisement"
STRIP = []
SPONSORED = []
NAME = TITLE = REPO = BLOB = SITE = LOGO = STOP = EXAMPLE = ""
LEAVE_OUT = []
SECTIONS = {}
FRONT_DOOR = True


def configure(config_path):
    """Reads help-centre.json: name, repo, site, and optionally help_dir, branch, leave_out, sections, logo_file,
    footer_starts (text that begins a footer on every page, left out of search), search_example and front_door."""
    global ROOT, HELP, NAME, TITLE, REPO, BLOB, SITE, LOGO, STOP, EXAMPLE, LEAVE_OUT, SECTIONS, FRONT_DOOR
    global FOOTER_NOTE, BANNER, BANNER_LABEL, BANNER_COUNT, STRIP, SPONSORED, FAVICON
    cfg_file = pathlib.Path(config_path).resolve()
    cfg = json.loads(cfg_file.read_text(encoding="utf-8"))
    ROOT = cfg_file.parent
    HELP = ROOT / cfg.get("help_dir", "docs/help")
    NAME = cfg["name"]
    TITLE = cfg.get("title", f"{NAME} help centre")
    REPO = cfg["repo"].rstrip("/")
    BLOB = f"{REPO}/blob/{cfg.get('branch', 'main')}/"
    SITE = cfg["site"].rstrip("/") + "/"
    LEAVE_OUT = cfg.get("leave_out", ["HOW-THIS-HELP-IS-WRITTEN.md"])
    SECTIONS = cfg.get("sections", {"guides": "Guides", "topics": "Topics", "basics": "Basics"})
    STOP = cfg.get("footer_starts", "")
    EXAMPLE = cfg.get("search_example", "Type what you want to do.")
    FRONT_DOOR = cfg.get("front_door", True)
    # footer_note: Markdown shown in every page's footer (a notice the app wants on every page).
    # banner: {"label", "markdown"}, shown at the top of every page as a labelled region that can be hidden.
    # strip_between: two markers; anything between them in an article is left out (it is in the footer instead).
    md = lambda text: markdown.markdown(text, output_format="html") if text else ""
    FOOTER_NOTE = md(cfg.get("footer_note", ""))
    # banners: a list of {"label", "markdown"}; one shows on each page and the next page shows the next one, so
    # nothing moves while it is read. "banner" (one only) still works.
    raw = cfg.get("banners") or ([cfg["banner"]] if cfg.get("banner") else [])
    BANNER_LABEL = (raw[0].get("label") if raw else None) or "Advertisement"

    def one(b):
        out = md(b.get("markdown", ""))
        # The banner is the same on every page: its own pages' links go to the full address, and links to other sites
        # are marked as paid (rel="sponsored"), as an advertisement's links should be.
        out = re.sub(r'href="(?![a-z][a-z0-9+.-]*:|#|/)([^"]+)"', lambda m: f'href="{SITE}{m.group(1)}"', out)
        return re.sub(r'<a href="(https?://(?!themightytrex\.github\.io)[^"]+)"', r'<a href="\1" rel="sponsored noopener"', out)
    BANNER = "".join(f'<div class="help-banner__item" data-banner="{i}"><span class="help-banner__label">'
                     f'{html.escape(b.get("label") or BANNER_LABEL)}</span>{one(b)}</div>' for i, b in enumerate(raw[:6]))
    BANNER_COUNT = min(len(raw), 6)
    STRIP = cfg.get("strip_between", [])
    FAVICON = ROOT / cfg["favicon_file"] if cfg.get("favicon_file") else None  # the browser tab's icon
    SPONSORED = cfg.get("sponsored_links", [])  # text in an address that marks an affiliate link, such as "a_aid="
    logo = (ROOT / cfg["logo_file"]).read_text(encoding="utf-8") if cfg.get("logo_file") else ""
    logo = re.sub(r"<\?xml[^>]*>|<!--.*?-->|<title[^>]*>.*?</title>", "", logo, flags=re.S).strip()
    logo = re.sub(r'\s(role|aria-labelledby|aria-label)="[^"]*"', "", logo)  # the link names it
    LOGO = re.sub(r"<svg\b", '<svg class="help-logo" width="28" height="28" aria-hidden="true" focusable="false"', logo, count=1) if logo else ""


def left_out(md):
    rel = md.relative_to(HELP).as_posix()
    return any(fnmatch.fnmatch(rel, pat) for pat in LEAVE_OUT)


def slug(value, separator="-"):
    """Heading ids as GitHub makes them, so links written for GitHub (#before-you-begin) still work."""
    value = re.sub(r"<[^>]+>", "", value).strip().lower()
    value = re.sub(r"[^\w\- ]", "", value)
    return value.replace(" ", separator)


def page_path(md):
    """docs/help/topics/x.md -> topics/x.html; README.md -> index.html."""
    rel = md.relative_to(HELP)
    return rel.with_name("index.html") if rel.name == "README.md" else rel.with_suffix(".html")


def fix_links(body, md):
    """Article links go to their pages; other repository files to GitHub; everything else is left alone."""
    here = md.parent

    def fix(m):
        attr, url = m.group(1), html.unescape(m.group(2))
        if re.match(r"^[a-z][a-z0-9+.-]*:|^#|^//", url, re.I):
            return m.group(0)
        path, _, anchor = url.partition("#")
        target = (here / path).resolve()
        try:
            rel_help = target.relative_to(HELP)
        except ValueError:
            try:
                return f'{attr}="{html.escape(BLOB + str(target.relative_to(ROOT)))}{"#" + anchor if anchor else ""}"'
            except ValueError:
                return m.group(0)
        if target.suffix == ".md" and left_out(target):
            return f'{attr}="{html.escape(BLOB + str(target.relative_to(ROOT)))}{"#" + anchor if anchor else ""}"'
        if target.suffix == ".md":
            new = page_path(target)
            back = pathlib.Path(*[".."] * len(md.relative_to(HELP).parent.parts)) if md.relative_to(HELP).parent.parts else pathlib.Path(".")
            out = (back / new).as_posix()
        else:
            out = path  # an image or another file copied next to the pages
        return f'{attr}="{html.escape(out)}{"#" + anchor if anchor else ""}"'

    # Only real tags: code samples are escaped (&lt;script src="..."&gt;), so their addresses stay as written.
    return re.sub(r"<[a-zA-Z][^<>]*>", lambda t: re.sub(r'\b(href|src)="([^"]*)"', fix, t.group(0)), body)


def crumbs_and_body(text):
    """The first line of an article is its trail, "[Help centre](../README.md) · Apps · how-to": that becomes the
    breadcrumbs. Returns (trail parts, kind, the rest)."""
    lines = text.splitlines()
    first = lines[0] if lines else ""
    if first.startswith("[Help centre]"):
        parts = [p.strip() for p in first.split("·")]
        kind = parts[-1] if len(parts) > 2 and parts[-1] in ("how-to", "reference", "troubleshooting", "concept", "guide") else ""
        middle = parts[1:-1] if kind else parts[1:]
        return middle, kind, "\n".join(lines[1:])
    return [], "", text


def plain(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


TEMPLATE = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {site_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/css/tokens.css">
<link rel="stylesheet" href="{root}assets/css/components.css">
<link rel="stylesheet" href="{root}assets/css/help.css">
<script>{prefs_js}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header site-header--no-rail">
  <div class="site-header__bar help-bar">
    <button class="icon-btn help-menu-btn" type="button" aria-expanded="false" aria-controls="help-nav">{icon_menu}<span class="label">Menu</span></button>
    <a class="site-header__brand" href="{root}index.html" aria-label="{site_title} home">{logo}<span aria-hidden="true">{site_title}</span></a>
    <button class="icon-btn help-search-btn" type="button" aria-expanded="false" aria-controls="help-search">{icon_search}<span class="label">Search</span></button>
    <form class="help-search" id="help-search" role="search" action="{root}search.html">
      <label class="visually-hidden" for="help-q">Search the help</label>
      <input class="input" type="search" id="help-q" name="q" placeholder="Search the help" autocomplete="off" value="{query}">
      <button class="btn" type="submit">Search</button>
    </form>
    <button class="icon-btn" type="button" data-opens="help-display" aria-haspopup="dialog" aria-expanded="false">{icon_display}<span class="label">Display</span></button>
  </div>
</header>
{banner}
<div class="help-layout{layout_class}">
<nav class="help-nav" id="help-nav" aria-label="Help centre">
  <button class="btn btn--quiet help-nav__hide" type="button" aria-expanded="true" aria-controls="help-nav-groups">{icon_hide}<span>Hide the menu</span></button>
  <div id="help-nav-groups" class="help-nav__groups">
{nav}
  </div>
</nav>
<button class="btn btn--quiet help-nav__show" type="button" aria-expanded="false" aria-controls="help-nav-groups" hidden>{icon_show}<span>Show the menu</span></button>
<main id="main" tabindex="-1" class="help-page">
{crumbs}
{toc_inline}
<article class="prose">
{kind}{body}
</article>
{edit}
</main>
{toc}
</div>
<footer class="site-footer help-footer">
  {footer_note}
  <p><a href="{root}index.html">Help centre</a> · <a href="{repo}">{name} on GitHub</a> · <a href="{repo}/issues">Report a problem with this help</a></p>
</footer>
<div class="side-panel-layer" id="help-display" hidden>
  <div class="side-panel-backdrop"></div>
  <aside class="side-panel" role="dialog" aria-modal="true" aria-labelledby="help-display-h">
    <div class="panel-header"><h2 class="panel-header__title" id="help-display-h">Display and accessibility</h2><button class="icon-btn" type="button" data-closes aria-label="Close display and accessibility">{icon_x}</button></div>
    <form class="side-panel__body form-stack" id="help-display-form">
      <fieldset><legend>Theme</legend><div class="segmented"><label><input type="radio" name="theme" value="system"><span>Match device</span></label><label><input type="radio" name="theme" value="light"><span>Light</span></label><label><input type="radio" name="theme" value="dark"><span>Dark</span></label></div></fieldset>
      <fieldset><legend>Text size</legend><div class="segmented"><label><input type="radio" name="text" value="100"><span>100%</span></label><label><input type="radio" name="text" value="125"><span>125%</span></label><label><input type="radio" name="text" value="150"><span>150%</span></label><label><input type="radio" name="text" value="175"><span>175%</span></label></div></fieldset>
      <fieldset><legend>Reduce motion</legend><div class="segmented"><label><input type="radio" name="motion" value="device"><span>Match device</span></label><label><input type="radio" name="motion" value="on"><span>On</span></label><label><input type="radio" name="motion" value="off"><span>Off</span></label></div></fieldset>
      <label class="switch" for="help-pref-contrast"><span>High contrast</span><input type="checkbox" role="switch" id="help-pref-contrast" name="contrast"></label>
      <label class="switch" for="help-pref-underline"><span>Underline links</span><input type="checkbox" role="switch" id="help-pref-underline" name="underline"></label>
      <label class="switch" for="help-pref-spacing"><span>Wider text spacing</span><input type="checkbox" role="switch" id="help-pref-spacing" name="spacing"></label>
      <p class="small muted">Choices apply at once and are kept in this browser.</p>
    </form>
    <div class="side-panel__foot"><button class="btn btn--primary" type="button" data-closes>Done</button><button class="btn" type="button" id="help-display-reset">Reset</button></div>
  </aside>
</div>
<div id="help-announcer" class="visually-hidden" aria-live="polite"></div>
<script>window.SharedComponentsSprite = "{root}assets/icons/sprite.svg";</script>
<script src="{root}assets/components.js"></script>
<script src="{root}assets/help.js"></script>
</body>
</html>
"""

# Display and accessibility: the same choices and classes as the app (web/js/common.js), applied before the page
# draws so it never flashes. Kept in this browser only.
PREFS_JS = ("try{var p=JSON.parse(localStorage.getItem('help-display')||'{}'),r=document.documentElement;"
            "if(p.theme&&p.theme!=='system')r.dataset.theme=p.theme;if(p.text&&p.text!=='100')r.classList.add('pref-text-'+p.text);"
            "if(p.contrast)r.classList.add('pref-contrast');if(p.motion==='on')r.classList.add('pref-motion');"
            "if(p.motion==='off')r.classList.add('pref-motion-off');if(p.underline)r.classList.add('pref-underline');"
            "if(p.spacing)r.classList.add('pref-spacing');if(localStorage.getItem('help-nav')==='hidden')r.classList.add('help-nav-hidden');"
            "if(localStorage.getItem('help-banner')==='hidden')r.classList.add('help-banner-hidden');"
            "__ROTATE__}catch(e){}")
# With two or more banners, which one this page shows (the next in turn, counted in this browser).
ROTATE_JS = ("var b=Number(localStorage.getItem('help-banner-next'))||0;localStorage.setItem('help-banner-next',(b+1)%__BC__);"
             "r.dataset.banner=b%__BC__")


def icon(name, root, size=20):
    return (f'<svg class="i{" i-lg" if size >= 20 else ""}" width="{size}" height="{size}" aria-hidden="true" focusable="false">'
            f'<use href="{root}assets/icons/sprite.svg#i-{name}"/></svg>')


def nav_groups():
    """The left menu, from the help centre home's own lists: each heading with links becomes a group."""
    groups, current = [], None
    for line in (HELP / "README.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#{2,3} (.+)", line)
        if m:
            current = {"title": re.split(r":", m.group(1))[0].strip(), "items": []}
            groups.append(current)
            continue
        m = re.match(r"^- \[([^\]]+)\]\(([^)#]+\.md)\)", line)
        if m and current is not None:
            current["items"].append((m.group(1), page_path(HELP / m.group(2)).as_posix()))
    return [g for g in groups if g["items"]]


def nav_html(groups, here, root):
    out = []
    for n, g in enumerate(groups):
        has = any(url == here for _, url in g["items"])
        items = "".join(f'<li><a href="{root}{url}"{" aria-current=\"page\"" if url == here else ""}>{html.escape(t)}</a></li>'
                        for t, url in g["items"])
        out.append(f'<div class="help-nav__group"><h2 class="help-nav__heading"><button type="button" aria-expanded="{"true" if has else "false"}" '
                   f'aria-controls="help-nav-{n}">{html.escape(g["title"])}</button></h2>'
                   f'<ul id="help-nav-{n}"{"" if has else " hidden"}>{items}</ul></div>')
    return "\n".join(out)


def toc_html(body):
    """The article's sections, for On this page: (the menu that follows the article, the one inside it on phones)."""
    heads = [(i, plain(t)) for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)]
    if len(heads) < 2:
        return "", ""
    links = "".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in heads)
    side = f'<nav class="help-toc" aria-labelledby="help-toc-h"><h2 class="help-toc__heading" id="help-toc-h">On this page</h2><ul>{links}</ul></nav>'
    inline = f'<details class="disclosure help-toc-inline"><summary>On this page</summary><div class="disclosure__body"><ul>{links}</ul></div></details>'
    return side, inline


def page(title, body, root, *, description="", crumbs="", kind="", edit="", canonical="", query="", nav="", toc=("", "")):
    return TEMPLATE.format(site_title=html.escape(TITLE), title=html.escape(title), description=html.escape(description[:200]), canonical=canonical,
                           root=root, logo=LOGO, crumbs=crumbs, kind=kind, body=body, edit=edit, repo=REPO, query=query,
                           prefs_js=PREFS_JS.replace("__ROTATE__", ROTATE_JS.replace("__BC__", str(BANNER_COUNT)) if BANNER_COUNT > 1 else ""), name=html.escape(NAME),
                           footer_note=f'<div class="help-footer__note">{FOOTER_NOTE}</div>' if FOOTER_NOTE else "",
                           banner=(f'<aside class="help-banner" id="help-banner" aria-label="{html.escape(BANNER_LABEL)}">'
                                   f'<div class="help-banner__body" data-count="{BANNER_COUNT}">{BANNER}</div>'
                                   f'<button class="icon-btn help-banner__hide" type="button" aria-label="Hide this {html.escape(BANNER_LABEL.lower())}">'
                                   f'{icon("x", root)}</button></aside>') if BANNER else "", nav=nav, toc=toc[0], toc_inline=toc[1],
                           layout_class="" if toc[0] else " help-layout--no-toc",
                           icon_menu=icon("menu", root), icon_search=icon("search", root), icon_display=icon("sun", root), icon_x=icon("x", root),
                           icon_hide=icon("chevron-left", root, 18), icon_show=icon("chevron-right", root, 18))


def build(out):
    site = out / "help"
    if site.exists():
        shutil.rmtree(site)
    (site / "assets" / "css").mkdir(parents=True)
    (site / "assets" / "icons").mkdir()
    for name in ("tokens.css", "components.css"):
        shutil.copy(DS / name, site / "assets" / "css" / name)
    (site / "assets" / "css" / "fonts").mkdir()
    for f in (DS / "fonts").iterdir():  # tokens.css looks for its fonts beside it
        shutil.copy(f, site / "assets" / "css" / "fonts" / f.name)
    shutil.copy(HERE / "help.css", site / "assets" / "css" / "help.css")
    shutil.copy(HERE / "help.js", site / "assets" / "help.js")
    if FAVICON and FAVICON.exists():  # else the logo itself
        shutil.copy(FAVICON, site / "assets" / "favicon.svg")
    else:
        (site / "assets" / "favicon.svg").write_text(re.sub(r'\sclass="help-logo"[^>]*?focusable="false"', ' xmlns="http://www.w3.org/2000/svg"', LOGO, count=1), encoding="utf-8")
    shutil.copy(DS / "components.js", site / "assets" / "components.js")
    shutil.copy(DS / "icons.svg", site / "assets" / "icons" / "sprite.svg")
    groups = nav_groups()
    if (HELP / "images").is_dir():
        shutil.copytree(HELP / "images", site / "images")

    index = []
    pages = sorted(p for p in HELP.rglob("*.md") if not left_out(p))
    for md in pages:
        rel_out = page_path(md)
        depth = len(rel_out.parent.parts)
        root = "../" * depth
        text = md.read_text(encoding="utf-8")
        if len(STRIP) == 2:
            text = re.sub(re.escape(STRIP[0]) + r".*?" + re.escape(STRIP[1]), "", text, flags=re.S)
        trail, kind, rest = crumbs_and_body(text)
        # superfences: code samples inside numbered steps stay code (fenced_code misses them, and their HTML ran).
        conv = markdown.Markdown(extensions=["tables", "sane_lists", "toc", "pymdownx.superfences"],
                                 extension_configs={"toc": {"slugify": slug}}, output_format="html")
        body = fix_links(conv.convert(rest), md)
        # Callouts written GitHub's way ("> [!TIP]" and the rest) become the library's notices, so they look the same
        # on GitHub and here: TIP and NOTE are information, IMPORTANT success-coloured, WARNING and CAUTION warnings.
        tones = {"NOTE": ("info", "info"), "TIP": ("info", "info"), "IMPORTANT": ("success", "circle-check"),
                 "WARNING": ("warning", "triangle-alert"), "CAUTION": ("danger", "circle-alert")}
        def callout(m):
            tone, ic = tones[m.group(1)]
            inner = re.sub(r"^\s*<p>\s*", "<p>", m.group(2).strip(), count=1)
            return (f'<div class="notice help-callout" data-tone="{tone}">{icon(ic, root)}'
                    f'<div class="notice__body">{inner}</div></div>')
        body = re.sub(r"<blockquote>\s*<p>\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)</blockquote>",
                      lambda m: callout(m) if m.group(1) in tones else m.group(0), body, flags=re.S)
        # A wide table scrolls sideways on its own: as a labelled region the keyboard can reach and scroll
        # (WCAG 2.1.1), named after the section it is in.
        def wrap_table(m, _n=[0]):
            before = body[:m.start()]
            head = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", before, re.S)
            name = plain(head[-1]) if head else title_guess
            return (f'<div class="help-table" role="region" tabindex="0" aria-label="Table: {html.escape(name)}">'
                    f"{m.group(0)}</div>")
        title_guess = plain((re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S) or [None, ""])[1]) or "table"
        body = re.sub(r"<table>.*?</table>", wrap_table, body, flags=re.S)
        # Affiliate links are marked as paid links (rel="sponsored") and open in a new tab, which they say.
        for mark in SPONSORED:
            body = re.sub(r'<a href="([^"]*' + re.escape(html.escape(mark)) + r'[^"]*)">(.*?)</a>',
                          r'<a href="\1" rel="sponsored noopener" target="_blank">\2<span class="visually-hidden"> (opens in a new tab)</span></a>',
                          body, flags=re.S)
        # Mermaid flowcharts (the guides' steps) are drawn in the browser, as GitHub draws them.
        body, charts = re.subn(r'(?:<div class="highlight">)?<pre[^>]*><code class="language-mermaid">(.*?)</code></pre>(?:</div>)?',
                               r'<pre class="mermaid">\1</pre>', body, flags=re.S)
        if charts:
            body += ('\n<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs";'
                     'mermaid.initialize({startOnLoad: true, theme: matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "default"});</script>')
        title_m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        title = plain(title_m.group(1)) if title_m else TITLE
        first_p = re.search(r"<p>(.*?)</p>", body, re.S)
        description = plain(first_p.group(1)) if first_p else ""
        section = SECTIONS.get(rel_out.parts[0], "") if len(rel_out.parts) > 1 else ""
        items = [f'<li><a href="{root}index.html">Help centre</a></li>']
        if section:
            items.append(f"<li>{html.escape(section)}</li>")
        items += [f"<li>{html.escape(t)}</li>" for t in trail if t and t != section]
        items.append(f'<li aria-current="page">{html.escape(title)}</li>')
        crumbs = f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>' if rel_out.name != "index.html" or depth else ""
        kind_html = f'<p class="prose__kind">{html.escape(kind.capitalize())}</p>\n' if kind else ""
        edit = (f'<p class="help-source small muted"><a href="{BLOB}{md.relative_to(ROOT).as_posix()}">'
                f"This page on GitHub</a>, where the help is written.</p>")
        target = site / rel_out
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page(title, body, root, description=description, crumbs=crumbs, kind=kind_html, edit=edit,
                               canonical=SITE + rel_out.as_posix(), nav=nav_html(groups, rel_out.as_posix(), root),
                               toc=toc_html(body) if rel_out.name != "index.html" else ("", "")), encoding="utf-8")
        headings = [plain(h) for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body, re.S)]
        words = plain(re.sub(r"<h1[^>]*>.*?</h1>", "", body, flags=re.S))
        if STOP:
            words = words.split(STOP)[0]  # a footer on every page
        index.append({"url": rel_out.as_posix(), "title": title, "section": section or (trail[0] if trail else ""),
                      "kind": kind, "summary": description[:220], "headings": headings, "text": words[:6000]})

    (site / "search-index.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    search_body = ('<h1>Search the help</h1>\n'
                   '<p id="help-results-count" class="muted" role="status" aria-live="polite">' + html.escape(EXAMPLE) + '</p>\n'
                   '<ol id="help-results" class="help-results"></ol>\n'
                   '<noscript><p>Search needs JavaScript. Every article is listed on the <a href="index.html">help centre '
                   'home</a>.</p></noscript>')
    (site / "search.html").write_text(page("Search the help", search_body, "", description=f"Search the {TITLE}.",
                                           canonical=SITE + "search.html", nav=nav_html(groups, "search.html", "")), encoding="utf-8")
    if FRONT_DOOR:  # the site's own front door goes to the help centre, when the site is only the help
        (out / "index.html").write_text(f'<!doctype html><meta charset="utf-8"><title>{html.escape(TITLE)}</title>'
                                        '<meta http-equiv="refresh" content="0; url=help/index.html">'
                                        f'<a href="help/index.html">{html.escape(TITLE)}</a>\n', encoding="utf-8")
    (out / ".nojekyll").write_text("")
    return len(pages)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--config", default="help-centre.json", help="the app's settings, at the app's root")
    ap.add_argument("--out", default="_site")
    a = ap.parse_args()
    configure(a.config)
    n = build(pathlib.Path(a.out).resolve())
    print(f"{n} help pages in {a.out}/help, with search")


if __name__ == "__main__":
    main()
