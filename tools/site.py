#!/usr/bin/env python3
"""Builds the design system site, one page for each part, from the sources. Run: python3 tools/site.py

  Sources                          Pages
  gallery.src.html (80 sections)   foundations/*.html, components/*.html, patterns/*.html (PARTS below)
  docs/*.md                        guides/*.html (GUIDES below), with a left menu, contents and Previous and Next
  icons.svg                        foundations/icons.html
  (all of them)                    index.html (the landing page), search.html and search-index.js
  (the old address)                gallery.html: a stub that sends each old #section address to its new page

Change this script or its sources, never the pages. The header, menus, Display slide-out and footer come from
tools/sitepage.py, which the resources pages and the boards use too, so every page has the same menu.
Run it after any change to gallery.src.html or docs/*.md, then tools/build.py for the resources and boards.
It stops with an error when a gallery section belongs to no page, so a new section is never lost."""
import html
import json
import pathlib
import re
import sys

import markdown

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402
import sitepage  # noqa: E402

# Where each page starts in the gallery: (first section, area, file, name, icon, what it holds). A page runs to the
# section before the next start. The order here is the order of the menu and of Previous and Next.
PARTS = [
    ("colour", "foundations", "colour", "Colour", "sparkles", "Role names for every colour, and how a theme changes the values."),
    ("palettes", "foundations", "accent-colours", "Accent colours", "sliders-horizontal", "The accent colours and the rules they keep in every theme."),
    ("type", "foundations", "type-space-icons", "Type, space and icons", "layout-grid", "One typeface, the size and space scales and the icon sizes."),
    ("header", "components", "shell", "Shell", "app-window", "The header and menus, the phone menu, page head, footer, Display, banners, alerts and the command palette."),
    ("buttons", "components", "actions", "Actions", "play", "Buttons and menu buttons."),
    ("fields", "components", "inputs", "Inputs", "pencil", "Fields, choices, filters, combobox, tag input, secret field, schedule and the error summary."),
    ("status", "components", "content", "Content", "file-text", "Status, tooltips, facts, charts, rows, tables, notices, toasts, callouts, disclosure and the log viewer."),
    ("cards", "components", "containers", "Panels, cards and tabs", "layout-grid", "Panels and cards, and tabs."),
    ("media", "components", "media", "Covers, media and shelves", "film", "Covers and media cards, the A to Z list, load more, cover actions, series header and shelf."),
    ("toolbar", "components", "settings-and-tools", "Settings and toolbars", "settings", "The section toolbar, settings rows, the save bar, settings patterns, the folder picker, timeline and calendar."),
    ("slide-out", "components", "slide-outs-and-dialogs", "Slide-outs and dialogs", "panel-right-open", "The slide-out and the dialog."),
    ("which", "patterns", "choosing", "Choosing", "list-checks", "Slide-out, dialog or page, and which item to use."),
    ("wizard", "patterns", "wizard", "Wizard", "list-ordered", "Every job done in steps: the pieces, and signing in to a service."),
    ("terminal", "patterns", "terminal", "Terminal", "terminal", "How a wizard appears and behaves in a terminal."),
    ("events", "patterns", "lists-and-changes", "Lists and changes", "history", "The event list, what will change, earlier and later, and recent checks."),
    ("help-article", "patterns", "help", "Help", "circle-help", "The help article, the help centre and what is new."),
    ("retiring", "patterns", "dates", "Dates", "calendar", "Retiring something, dated changes and time ago."),
]
AREAS = {
    "foundations": ("Foundations", "Colour, accent colours, type, space and icons: the values every component uses."),
    "components": ("Components", "Every component of the shared library, live, with its markup and rules."),
    "patterns": ("Patterns", "How components work together: choosing, the wizard, the terminal, help and dates."),
}

# The guides: file in docs/, page name, group.
GUIDES = [
    ("DESIGN-SYSTEM", "Design system", "Design"), ("LIBRARY", "Component library", "Design"), ("COMPONENTS", "Components by area", "Design"),
    ("WIZARD", "Wizard", "Patterns"), ("TERMINAL", "Terminal", "Patterns"),
    ("CONTENT-DESIGN", "Content design", "Words"), ("HELP-WRITING", "Help writing", "Words"), ("CHANGELOGS", "Changelogs", "Words"),
    ("ALT-TEXT", "Alt text", "Words"), ("SCREENSHOTS", "Screenshots", "Words"),
    ("ACCESSIBILITY", "Accessibility", "Accessibility and security"), ("WCAG", "WCAG 2.2 AA", "Accessibility and security"),
    ("SECURITY-CHECKS", "Security checks", "Accessibility and security"),
]
GUIDE_SLUG = {n: n.lower() for n, _, _ in GUIDES}

GALLERY = (ROOT / "gallery.src.html").read_text()
SITE_CSS = re.search(r"<style>(.*?)</style>", GALLERY, re.S).group(1)
# The page-shell rules of the old gallery are replaced by sitepage's; the demo rules stay.
SITE_CSS = re.sub(r"^\s*\.g-(shell|nav)[^\n]*\n", "", SITE_CSS, flags=re.M)
SITE_CSS = re.sub(r"@media \(max-width: 860px\) \{[^}]*(\{[^}]*\}[^}]*)*\}\s*", "", SITE_CSS)

SITE_CSS += "\n  .g-notes .g-note-h { font-size: var(--text-sm); font-weight: 700; margin-bottom: var(--space-1); }\n"

pages = []  # every page written: dicts for the search index and the stub


def sections():
    """Every gallery section in order: (id, html)."""
    out, pos = [], 0
    for m in re.finditer(r'<section class="g-section" id="([\w-]+)"', GALLERY):
        if m.start() < pos:
            continue  # inside the one before
        depth, i = 0, m.start()
        for t in re.finditer(r"<section\b|</section>", GALLERY[i:]):
            depth += 1 if t.group(0) == "<section" else -1
            if depth == 0:
                end = i + t.end()
                break
        out.append((m.group(1), GALLERY[i:end]))
        pos = end
    return out


def panels():
    """The slide-outs the demos open: id -> html."""
    tail = GALLERY[GALLERY.index("<!-- Slide-outs used by the demos -->"):GALLERY.index('<script src="components.js">')]
    out = {}
    for m in re.finditer(r'\s*<div class="side-panel-layer" id="(g-[\w-]+)" hidden>.*?</aside>\s*</div>', tail, re.S):
        out[m.group(1)] = m.group(0)
    return out


def chunks():
    """The demo script, in pieces by section: id -> code. The old gallery menu code is dropped."""
    js = GALLERY[GALLERY.index("<script>\n  // @chunk colour"):GALLERY.rindex("</script>")]
    out = {}
    for m in re.finditer(r"  // @chunk ([\w-]+)\n(.*?)(?=  // @chunk |\Z)", js, re.S):
        out[m.group(1)] = m.group(2)
    out.pop("site-menu", None)
    return out


def esc(text):
    return html.escape(text, quote=True)


def crumbs(items):
    """A trail ending at the current page: items is [(name, path or None)], paths from the site root."""
    parts = []
    for name, path in items:
        parts.append(f'<li><a href="{path}">{esc(name)}</a></li>' if path else f'<li aria-current="page">{esc(name)}</li>')
    return f'<nav class="breadcrumbs s-crumbs" aria-label="Breadcrumb"><ol>{"".join(parts)}</ol></nav>'


def pager(prev, nxt):
    """Previous and Next links: each is (name, path) or None."""
    if not prev and not nxt:
        return ""
    a = f'<a class="s-prev" href="{prev[1]}" rel="prev"><small>Previous</small><span>{esc(prev[0])}</span></a>' if prev else ""
    b = f'<a class="s-next" href="{nxt[1]}" rel="next"><small>Next</small><span>{esc(nxt[0])}</span></a>' if nxt else ""
    return f'<nav class="s-pager" aria-label="Previous and next">{a}{b}</nav>'


def left_nav(heading, siblings, current, own_title, own_links):
    """The left menu: the pages of this part, then this page's own sections."""
    pages_li = "".join(
        f'<li><a href="{p}"{" aria-current=\"page\"" if p == current else ""}>{esc(n)}</a></li>' for n, p in siblings)
    own = "".join(f'<li><a href="{h}">{esc(n)}</a></li>' for h, n in own_links)
    second = f'<h2 id="s-own-h">{esc(own_title)}</h2><ol>{own}</ol>' if own_links else ""
    return (f'<nav class="s-nav" aria-labelledby="s-nav-h"><h2 id="s-nav-h">{esc(heading)} pages</h2>'
            f'<ol class="s-nav-pages">{pages_li}</ol>{second}</nav>')


def write(rel, text, *, expand=True):
    out, missing = build.expand(text) if expand else (text, [])
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(out)
    if missing:
        print(rel, "missing icons:", ", ".join(missing))


def main():
    secs = sections()
    sec_ids = [i for i, _ in secs]
    starts = [p[0] for p in PARTS]
    for s in starts:
        if s not in sec_ids:
            sys.exit(f"tools/site.py: PARTS starts at {s}, which is not a section of gallery.src.html")
    if sec_ids[0] != starts[0]:
        sys.exit(f"tools/site.py: section {sec_ids[0]} comes before the first page; add a page that starts at it")
    # Give each section to the page it falls in.
    owner, current = {}, None
    for i, _ in secs:
        current = i if i in starts else current
        owner[i] = current
    by_start = {}
    for i, h in secs:
        by_start.setdefault(owner[i], []).append((i, h))
    panel_html, script_chunks = panels(), chunks()

    # Where every id lives, so a link to #media from another page goes to the page that has it.
    page_of = {}
    for part in PARTS:
        for i, h in by_start[part[0]]:
            page_of[i] = f"{part[1]}/{part[2]}.html"
            for m in re.finditer(r'\sid="([\w-]+)"', h):
                page_of.setdefault(m.group(1), f"{part[1]}/{part[2]}.html")

    # The header's second row for each area, and the guides' own pages.
    menu = {}
    for area in AREAS:
        menu[area] = [[f"{p[1]}/{p[2]}.html", p[4], p[3]] for p in PARTS if p[1] == area]
    (HERE / "site-menu.json").write_text(json.dumps(menu, indent=1) + "\n")
    importlib_reload()
    # Pages in reading order, for Previous and Next within an area.
    order = {a: [(p[3], f"{p[2]}.html") for p in PARTS if p[1] == a] for a in AREAS}

    for k, part in enumerate(PARTS):
        start, area, slug, name, icon, summary = part
        rel = f"{area}/{slug}.html"
        group = [p for p in PARTS if p[1] == area]
        idx = group.index(part)
        secs_here = by_start[start]
        body_secs = "\n\n".join(h for _, h in secs_here)
        # The labels in the notes under each demo (Behaviour, Classes) are headings in the source; here they are
        # labels, so no heading is skipped.
        body_secs = re.sub(r"<div><h[34]>(.*?)</h[34]>", r'<div><p class="g-note-h">\1</p>', body_secs)
        # Links to sections on other pages.
        here_ids = set(re.findall(r'\sid="([\w-]+)"', body_secs))
        def fix(m):
            target = m.group(1)
            if target in here_ids or target not in page_of:
                return m.group(0)
            dest = page_of[target]
            dest = dest.split("/", 1)[1] if dest.startswith(area + "/") else "../" + dest
            return f'href="{dest}#{target}"'
        body_secs = re.sub(r'href="#([\w-]+)"', fix, body_secs)
        used_panels = "".join(h for pid, h in panel_html.items() if f'data-opens="{pid}"' in body_secs)
        used_panels = re.sub(r'href="#([\w-]+)"', fix, used_panels)
        script = "".join(code for cid, code in script_chunks.items() if f'id="{cid}"' in body_secs)
        script = script.replace('.g-nav ol a', '.s-nav ol a')
        script = f"<script>\n{script}\n</script>" if script.strip() else ""
        links = [(f"#{i}", re.sub(r"<[^>]+>", "", re.search(r"<h2[^>]*>(.*?)</h2>", h, re.S).group(1))) for i, h in secs_here]
        sibs = [(p[3], f"{p[2]}.html") for p in group]
        nav = left_nav(AREAS[area][0], sibs, f"{slug}.html", "On this page", links)
        prev = (group[idx - 1][3], f"{group[idx - 1][2]}.html") if idx else None
        nxt = (group[idx + 1][3], f"{group[idx + 1][2]}.html") if idx + 1 < len(group) else None
        # Previous of the first page and next of the last page lead into the neighbouring area.
        if not prev and k:
            q = PARTS[k - 1]
            prev = (q[3], f"../{q[1]}/{q[2]}.html")
        if not nxt and k + 1 < len(PARTS):
            q = PARTS[k + 1]
            nxt = (q[3], f"../{q[1]}/{q[2]}.html")
        # The icons page follows the type page.
        body = (crumbs([("Home", "../index.html"), (AREAS[area][0], f"../{area}/index.html"), (name, None)]) +
                f'<div class="g-main"><div class="page-head"><div class="page-head__text"><h1>{esc(name)}</h1>'
                f'<p class="page-head__summary">{esc(summary)}</p></div></div>\n{body_secs}\n</div>' +
                pager(prev, nxt))
        text = sitepage.page(root="../", main=area, current=rel, title=name, body=body, side=nav, css=SITE_CSS,
                             note="Made by tools/site.py from gallery.src.html", script=script)
        text = text.replace("<!--ICONS-->", "<!--ICONS-->", 1)
        text = text.replace("\n</body>", f"\n{used_panels}\n</body>", 1)
        text = text.replace('<main class="s-main" id="main" tabindex="-1">', '<main class="s-main" id="main" tabindex="-1">', 1)
        write(rel, text)
        text_only = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body_secs))
        heads = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body_secs, re.S)
        pages.append({"title": name, "area": AREAS[area][0], "url": rel, "summary": summary,
                      "text": html.unescape(" ".join(re.sub(r"<[^>]+>", "", h) for h in heads)) + " " + html.unescape(text_only)[:1200]})

    foundations_extras()
    guides(page_of)
    landings(by_start)
    write_search_and_stub(page_of)
    print(len(pages), "pages")


def importlib_reload():
    """sitepage read site-menu.json when it was imported; read it again now it is written."""
    for key, items in json.loads((HERE / "site-menu.json").read_text()).items():
        sitepage.SUB[key] = [tuple(p) for p in items]


def foundations_extras():
    """The icons page: every icon in the sprite, from icons.svg."""
    names = sorted(re.findall(r'<symbol id="i-([\w-]+)"', (ROOT / "icons.svg").read_text()))
    items = "".join(f'<li>{{{{i:{n}}}}}<code>{n}</code></li>' for n in names)
    body = (f'<div class="g-main"><div class="page-head"><div class="page-head__text"><h1>Icons</h1>'
            f'<p class="page-head__summary">{len(names)} icons from Lucide, drawn at 16, 18 and 20px with a 2px stroke. Use one with '
            f'<code>&lt;use href="#i-&lt;name&gt;"&gt;</code>. Every icon sits beside words or has a name for screen readers.</p></div></div>'
            f'<section class="g-section" id="all-icons" aria-labelledby="all-icons-h"><header><h2 id="all-icons-h">All icons</h2></header>'
            f'<ul class="s-icons">{items}</ul></section></div>')
    rel = "foundations/icons.html"
    PARTS_F = [p for p in PARTS if p[1] == "foundations"]
    sibs = [(p[3], f"{p[2]}.html") for p in PARTS_F] + [("Icons", "icons.html")]
    nav = left_nav("Foundations", sibs, "icons.html", "", [])
    last = PARTS_F[-1]
    body = (crumbs([("Home", "../index.html"), ("Foundations", "../foundations/index.html"), ("Icons", None)]) + body +
            pager((last[3], f"{last[2]}.html"), ("Shell", "../components/shell.html")))
    write(rel, sitepage.page(root="../", main="foundations", current=rel, title="Icons", body=body, side=nav, css=SITE_CSS,
                             note="Made by tools/site.py from icons.svg"))
    pages.append({"title": "Icons", "area": "Foundations", "url": rel, "summary": "Every icon in the sprite.", "text": " ".join(names)})


def md_page(name):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"], extension_configs={"toc": {"toc_depth": "2"}})
    text = (ROOT / "docs" / f"{name}.md").read_text()
    out = md.convert(text)
    toc = [(t["id"], re.sub(r"<[^>]+>", "", t["name"])) for t in md.toc_tokens[0]["children"]] if md.toc_tokens and md.toc_tokens[0]["level"] == 1 else \
          [(t["id"], re.sub(r"<[^>]+>", "", t["name"])) for t in md.toc_tokens if t["level"] == 2]
    title = re.search(r"<h1[^>]*>(.*?)</h1>", out, re.S)
    title = html.unescape(re.sub(r"<[^>]+>", "", title.group(1))) if title else name
    return out, toc, title


def guides(page_of):
    names = {n for n, _, _ in GUIDES}
    pages_list = [(title, f"{n.lower()}.html", group) for n, title, group in GUIDES]
    ordered = [(t, p) for t, p, _ in pages_list]
    for k, (n, title, group) in enumerate(GUIDES):
        out, toc, h1 = md_page(n)
        # Links between guides stay on the site; links to the gallery go to the new pages.
        def link(m):
            href = m.group(1)
            mm = re.match(r"(?:https://github\.com/TheMightyTRex/design-system/(?:blob|tree)/main/)?(?:\.\./)?(?:docs/)?([A-Z-]+)\.md(#[\w-]*)?$", href)
            if mm and mm.group(1) in names:
                return f'href="{mm.group(1).lower()}.html{mm.group(2) or ""}"'
            if href in ("../gallery.html", "gallery.html"):
                return 'href="../components/index.html"'
            if re.match(r"(?:\.\./)?gallery\.html#([\w-]+)", href):
                sid = re.match(r"(?:\.\./)?gallery\.html#([\w-]+)", href).group(1)
                return f'href="../{page_of[sid]}#{sid}"' if sid in page_of else 'href="../components/index.html"'
            return m.group(0)
        out = re.sub(r'href="([^"]+)"', link, out)
        out = re.sub(r"<h1[^>]*>.*?</h1>", "", out, count=1, flags=re.S)
        out = out.replace("<pre>", '<pre tabindex="0">')
        tables = iter(range(1, 999))
        out = re.sub(r"<table>.*?</table>", lambda m: f'<div class="s-scroll" tabindex="0" role="region" aria-label="Table {next(tables)}">{m.group(0)}</div>', out, flags=re.S)
        rel = f"guides/{n.lower()}.html"
        sib_groups = ""
        for g in dict.fromkeys(g for _, _, g in GUIDES):
            lis = "".join(f'<li><a href="{p}"{" aria-current=\"page\"" if p == f"{n.lower()}.html" else ""}>{esc(t)}</a></li>'
                          for t, p, gg in pages_list if gg == g)
            sib_groups += f'<li class="s-group">{esc(g)}</li>{lis}'
        own = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc)
        nav = (f'<nav class="s-nav" aria-labelledby="s-nav-h"><h2 id="s-nav-h">Guides</h2><ol class="s-nav-pages"><li><a href="index.html">All guides</a></li>{sib_groups}</ol>'
               f'<h2 id="s-own-h">On this page</h2><ol>{own}</ol></nav>')
        prev = (ordered[k - 1][0], ordered[k - 1][1]) if k else ("All guides", "index.html")
        nxt = (ordered[k + 1][0], ordered[k + 1][1]) if k + 1 < len(ordered) else None
        src = f"https://github.com/TheMightyTRex/design-system/blob/main/docs/{n}.md"
        body = (crumbs([("Home", "../index.html"), ("Guides", "index.html"), (title, None)]) +
                f'<div class="s-doc"><div class="page-head"><div class="page-head__text"><h1>{esc(h1)}</h1>'
                f'<p class="page-head__summary">{esc(group)} guide. <a href="{src}">Edit this guide on GitHub</a>.</p></div></div>'
                f'<div class="prose">\n{out}\n</div></div>' + pager(prev, nxt))
        write(rel, sitepage.page(root="../", main="guides", current=rel, title=title, body=body, side=nav, css=SITE_CSS,
                                 note=f"Made by tools/site.py from docs/{n}.md"))
        plain = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", out)))
        pages.append({"title": title, "area": "Guides", "url": rel, "summary": f"{group} guide", "text": plain[:2500]})
    # The guides landing page.
    cards = ""
    for g in dict.fromkeys(g for _, _, g in GUIDES):
        rows = "".join(f'<li class="row row--no-lead"><div><span class="row__title"><a href="{p}">{esc(t)}</a></span></div></li>'
                       for t, p, gg in pages_list if gg == g)
        cards += f'<section class="stack-3" aria-labelledby="g-{abs(hash(g)) % 9999}"><h2 id="g-{abs(hash(g)) % 9999}">{esc(g)}</h2><ul class="rows">{rows}</ul></section>'
    body = (crumbs([("Home", "../index.html"), ("Guides", None)]) +
            f'<div class="s-landing"><div class="page-head"><div class="page-head__text"><h1>Guides</h1><p class="page-head__summary">The written rules: how to build, write and test. Each guide is one page.</p></div></div>{cards}</div>' +
            pager(None, (ordered[0][0], ordered[0][1])))
    nav = ""
    write("guides/index.html", sitepage.page(root="../", main="guides", current="guides/index.html", title="Guides", body=body,
                                             css=SITE_CSS, note="Made by tools/site.py"))
    pages.append({"title": "Guides", "area": "Guides", "url": "guides/index.html", "summary": "All the guides.", "text": " ".join(t for t, _, _ in pages_list)})


def landings(by_start):
    for area, (name, about) in AREAS.items():
        group = [p for p in PARTS if p[1] == area]
        extra = [("Icons", "icons.html", "Every icon in the sprite.")] if area == "foundations" else []
        cards = "".join(
            f'<li class="card"><h2 class="card__title"><a href="{p[2]}.html">{esc(p[3])}</a></h2><p>{esc(p[5])}</p>'
            f'<p class="small muted">{len(by_start[p[0]])} section{"s" if len(by_start[p[0]]) != 1 else ""}</p></li>' for p in group)
        cards += "".join(f'<li class="card"><h2 class="card__title"><a href="{h}">{esc(t)}</a></h2><p>{esc(s)}</p></li>' for t, h, s in extra)
        rel = f"{area}/index.html"
        body = (crumbs([("Home", "../index.html"), (name, None)]) +
                f'<div class="s-landing"><div class="page-head"><div class="page-head__text"><h1>{name}</h1><p class="page-head__summary">{esc(about)}</p></div></div>'
                f'<ul class="s-cards">{cards}</ul></div>' + pager(None, (group[0][3], f"{group[0][2]}.html")))
        write(rel, sitepage.page(root="../", main=area, current=rel, title=name, body=body, css=SITE_CSS, note="Made by tools/site.py"))
        pages.append({"title": name, "area": name, "url": rel, "summary": about, "text": " ".join(p[3] + " " + p[5] for p in group)})
    # Home.
    tiles = [("Foundations", "foundations/index.html", "Colour, accent colours, type, space and icons."),
             ("Components", "components/index.html", "Every component, live, with its markup and rules."),
             ("Patterns", "patterns/index.html", "Choosing, the wizard, the terminal, help and dates."),
             ("Guides", "guides/index.html", "Content design, help writing, accessibility, security and more, one page each."),
             ("Boards", "areas/index.html", "Whole pages of Starboard, built from the library, and an archive of the retired Storyarr's boards."),
             ("Resources", "resources/index.html", "Tools, outside tools, how to make a change and how to get feedback.")]
    cards = "".join(f'<li class="card"><h2 class="card__title"><a href="{h}">{t}</a></h2><p>{s}</p></li>' for t, h, s in tiles)
    body = (f'<div class="s-landing"><div class="page-head"><div class="page-head__text"><h1>TRex design system</h1>'
            f'<p class="page-head__summary">One design for Starboard and its plug-ins: tokens, components, behaviour and icons, with the rules for words, help and accessibility. Each part has its own page.</p></div></div>'
            f'<ul class="s-cards">{cards}</ul>'
            f'<p><a class="btn btn--primary" href="components/index.html">Open the components</a> <a class="btn" href="search.html">Search the site</a></p></div>')
    write("index.html", sitepage.page(root="", main="", current="index.html", title="Home", body=body, css=SITE_CSS,
                                      note="Made by tools/site.py").replace("\n</head>", "\n</head>", 1))
    pages.append({"title": "Home", "area": "Home", "url": "index.html", "summary": "The design system.", "text": ""})


SEARCH_SCRIPT = """<script src="search-index.js"></script>
<script>
  // Search: every word you type must appear in a page's title, headings or text. Best matches first.
  const form = document.getElementById("q-form");
  const input = document.getElementById("q");
  const out = document.getElementById("q-results");
  const count = document.getElementById("q-count");
  function run() {
    const words = input.value.toLowerCase().split(/\\s+/).filter(Boolean);
    out.replaceChildren();
    if (!words.length) { count.textContent = "Type a word to search all " + SITE_INDEX.length + " pages."; return; }
    const hits = [];
    for (const p of SITE_INDEX) {
      const title = p.title.toLowerCase(), text = (p.summary + " " + p.text).toLowerCase();
      if (!words.every((w) => title.includes(w) || text.includes(w))) continue;
      hits.push([words.reduce((s, w) => s + (title.includes(w) ? 10 : 0) + (text.includes(w) ? 1 : 0), 0), p]);
    }
    hits.sort((a, b) => b[0] - a[0]);
    for (const [, p] of hits) {
      const li = document.createElement("li");
      li.className = "row row--no-lead";
      const at = (p.summary + " " + p.text).toLowerCase().indexOf(words[0]);
      const snippet = at > 0 ? "..." + (p.summary + " " + p.text).slice(Math.max(0, at - 40), at + 100) + "..." : p.summary;
      li.innerHTML = '<div><span class="row__title"><a></a></span><div class="row__meta"></div></div>';
      li.querySelector("a").textContent = p.title + " (" + p.area + ")";
      li.querySelector("a").href = p.url;
      li.querySelector(".row__meta").textContent = snippet;
      out.append(li);
    }
    count.textContent = hits.length === 1 ? "1 page matches." : hits.length + " pages match.";
  }
  form.addEventListener("submit", (e) => { e.preventDefault(); history.replaceState(null, "", "?q=" + encodeURIComponent(input.value)); run(); });
  input.addEventListener("input", run);
  input.value = new URLSearchParams(location.search).get("q") || "";
  run();
</script>"""


def write_search_and_stub(page_of):
    index = [p for p in pages if p["url"] != "search.html"]
    (ROOT / "search-index.js").write_text("// Made by tools/site.py: the pages searched by search.html.\nconst SITE_INDEX = " + json.dumps(index, ensure_ascii=False) + ";\n")
    body = (crumbs([("Home", "index.html"), ("Search", None)]) +
            '<div class="s-landing"><div class="page-head"><div class="page-head__text"><h1>Search</h1><p class="page-head__summary">Search every page of the design system.</p></div></div>'
            '<form id="q-form" role="search" class="search-field"><label for="q">Words to find</label><input class="input" id="q" type="search" autocomplete="off"> '
            '<button class="btn btn--primary" type="submit">Search</button></form>'
            '<p id="q-count" role="status" aria-live="polite"></p><ul class="rows" id="q-results"></ul></div>')
    write("search.html", sitepage.page(root="", main="", current="search.html", title="Search", body=body, css=SITE_CSS,
                                       note="Made by tools/site.py", script=SEARCH_SCRIPT))
    # The old gallery address. Old links such as gallery.html#buttons go to the page that now has the section.
    table = {k: v for k, v in page_of.items()}
    links = "".join(f'<li><a href="{p[1]}/{p[2]}.html">{esc(p[3])}</a> ({esc(AREAS[p[1]][0])})</li>' for p in PARTS)
    stub = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Components moved · TRex Design System</title>
<!-- Made by tools/site.py: the old address of the component gallery. -->
<noscript><meta http-equiv="refresh" content="0; url=components/index.html"></noscript>
<script>
  // gallery.html#buttons opens the page that now has the Buttons section.
  const pages = {json.dumps(table)};
  const id = decodeURIComponent(location.hash.slice(1));
  location.replace(pages[id] ? pages[id] + "#" + id : "components/index.html");
</script>
</head>
<body>
<h1>The component gallery has moved</h1>
<p>Each part now has its own page. <a href="index.html">Go to the home page</a>, or choose one:</p>
<ul>{links}</ul>
</body>
</html>
"""
    (ROOT / "gallery.html").write_text(stub)


if __name__ == "__main__":
    main()
