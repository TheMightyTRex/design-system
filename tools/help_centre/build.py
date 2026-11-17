#!/usr/bin/env python3
"""The design system's help centre: builds an app's Markdown help into web pages in the help centre standard
(docs/HELP-WRITING.md, section 11; chosen by the owner on 14 November 2026, Starboard DASH-436):

- the top bar: the seven main items as quick links (Home, Get started, Use it, Plug-ins, Accessibility, Fix a
  problem, Developers), with Search and Display;
- a hub on every page: a side menu that folds (areas, then groups, then every article; .side-tree), the page you
  are on marked and its area and group open; on phones it opens from Menu;
- the front page: the latest version beside the heading, the journey with a column of cards under each stage, the
  newest item and the problem solver card;
- a page for each area with a card for each group, and a problem solver page that works with no script;
- articles flow chart first: a ```flow block (or a simple Mermaid flowchart) drawn as SVG with the same paths in
  words, and its numbered answers as cards with a grey band;
- plug-in mode (a "plugins" block): each plug-in a folding item in the side menu with the same eight pages.

Everything comes from the app's help-centre.json (docs/HELP-WRITING.md, section 11, has its shape) and from a
comment in each article, <!-- help: <area> / <group> -->. With no "areas" in help-centre.json, the side menu is the
help home's own lists, as before. From the app's folder:

    python3 <design-system>/tools/help_centre/build.py [--config help-centre.json] [--out _site] [--strict]

Needs Python-Markdown and pymdown-extensions (pip install markdown==3.7 pymdown-extensions==10.9), or run
tools/help_centre/build.sh, which uses a Python container. Pages go in <out>/help/<the same path>.html, README.md
becoming index.html; links between articles point at the pages, and links to other files in the app's repository
point at GitHub. No library is loaded in the browser: the pages use this repository's tokens.css, components.css,
components.js, fonts and icons, and help.css and help.js beside this file.
"""
import argparse
import base64
import fnmatch
import html
import json
import pathlib
import re
import shutil
import sys

import markdown

HERE = pathlib.Path(__file__).resolve().parent
DS = HERE.parent.parent  # this design system
sys.path.insert(0, str(HERE))
import flowchart  # noqa: E402

# Set from the app's help-centre.json by configure().
ROOT = HELP = None
CFG = {}
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
WARNINGS = []

# The standard: the same seven items, in this order, in every help centre (owner, 14 November 2026). An app's
# help-centre.json gives each area its groups; the names and icons stay the same everywhere.
STANDARD = [("start", "Get started", "compass"), ("use", "Use it", "play"), ("plugins", "Plug-ins", "puzzle"),
            ("a11y", "Accessibility", "eye"), ("fix", "Fix a problem", "wrench"), ("dev", "Developers", "terminal")]
# Every plug-in has the same eight pages, in this order. A page with nothing to say shows one line saying so.
PLUGIN_PAGES = [("overview", "Overview"), ("install", "Install"), ("settings", "Settings"), ("dashboard-card", "Dashboard card"),
                ("updates", "Updates"), ("accessibility", "Accessibility"), ("problems", "Problems"), ("for-developers", "For developers")]
NOTHING = {"install": "{name} has no install steps of its own: add it like every other plug-in.",
           "settings": "{name} has no settings.", "dashboard-card": "{name} has no dashboard card.",
           "updates": "{name} has nothing of its own to know about updates.",
           "accessibility": "{name} has no accessibility notes of its own.", "problems": "There are no known problems with {name}.",
           "for-developers": "{name} has no notes for developers."}
MARKER = re.compile(r"<!--\s*help:\s*([\w-]+)\s*/\s*([\w-]+)\s*-->")
# Words that mark a page as not written yet (DASH-426). --strict stops on any of them in the Markdown a page is built
# from, outside code, and in the settings' own words; a help centre may give its own list as "placeholders".
PLACEHOLDERS = [r"still to be written", r"\bto be written\b", r"\bTODO\b", r"\bTBD\b", r"\bTBC\b", r"lorem ipsum"]


def configure(config_path):
    """Reads help-centre.json: name, repo, site, and optionally help_dir, branch, leave_out, sections, logo_file,
    footer_starts (text that begins a footer on every page, left out of search), search_example, front_door, and the
    standard's areas, home, version_from or version, journey, featured, solver and plugins."""
    global ROOT, HELP, NAME, TITLE, REPO, BLOB, SITE, LOGO, STOP, EXAMPLE, LEAVE_OUT, SECTIONS, FRONT_DOOR, CFG
    global FOOTER_NOTE, NOTICE_LABEL, BANNER, BANNER_LABEL, BANNER_COUNT, STRIP, SPONSORED, FAVICON, COUNTER
    cfg_file = pathlib.Path(config_path).resolve()
    cfg = json.loads(cfg_file.read_text(encoding="utf-8"))
    CFG = cfg
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
    md = lambda text: markdown.markdown(text, output_format="html") if text else ""
    # The footer notice (DASH-436 follow-up): the footer shows one link, its first bold sentence (or "footer_link"),
    # which opens a slide-out with the whole notice; the footer itself stays like the apps' footers.
    note = (cfg.get("footer_note") or "").strip()
    first = re.match(r"\*\*(.+?)\*\*\s*", note)
    NOTICE_LABEL = cfg.get("footer_link") or (first.group(1).strip() if first else "")
    FOOTER_NOTE = md(note[first.end():] if first and not cfg.get("footer_link") else note)
    # Visitor counting is off unless a help centre names its GoatCounter address: no cookies and no personal data,
    # and the footer says so on every page.
    gc = cfg.get("goatcounter", "")
    if gc and not re.fullmatch(r"https://[a-z0-9-]+\.goatcounter\.com/count", gc):
        raise SystemExit(f"goatcounter must look like https://<code>.goatcounter.com/count, not {gc!r}")
    COUNTER = (f'<script data-goatcounter="{gc}" async src="https://gc.zgo.at/count.js"></script>\n') if gc else ""
    if gc:
        NOTICE_LABEL = NOTICE_LABEL or "Visit counting"
        FOOTER_NOTE += md("This help centre counts visits with [GoatCounter](https://www.goatcounter.com), "
                          "which uses no cookies and keeps no personal data.")
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
    FAVICON = ROOT / cfg["favicon_file"] if cfg.get("favicon_file") else None
    SPONSORED = cfg.get("sponsored_links", [])
    logo = (ROOT / cfg["logo_file"]).read_text(encoding="utf-8") if cfg.get("logo_file") else ""
    logo = re.sub(r"<\?xml[^>]*>|<!--.*?-->|<title[^>]*>.*?</title>", "", logo, flags=re.S).strip()
    logo = re.sub(r'\s(role|aria-labelledby|aria-label)="[^"]*"', "", logo)  # the link names it
    LOGO = re.sub(r"<svg\b", '<svg class="help-logo" width="28" height="28" aria-hidden="true" focusable="false"', logo, count=1) if logo else ""


def warn(text):
    WARNINGS.append(text)


def check_written(text, where):
    """Warns when the words still say a page is to be written (PLACEHOLDERS), so --strict stops on it."""
    words = re.sub(r"^```.*?^```[ \t]*$", "", text, flags=re.S | re.M)
    words = re.sub(r"`[^`\n]*`|<!--.*?-->", "", words, flags=re.S)
    for pat in CFG.get("placeholders", PLACEHOLDERS):
        m = re.search(pat, words, flags=re.I if pat.islower() else 0)
        if m:
            warn(f"{where}: still a placeholder ({m.group(0)!r})")
            return


# ---- Markdown to a page ---------------------------------------------------------------------------------------

def left_out(md):
    try:
        rel = md.relative_to(HELP).as_posix()
    except ValueError:
        return False
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


def up(out_rel):
    """From a page to the help centre's root: "" or "../" for each folder."""
    return "../" * len(pathlib.PurePosixPath(out_rel).parent.parts)


OUTSIDE = {}  # Markdown files outside the help folder that are pages too (plug-in overviews): path -> page


def fix_links(body, md, out_rel):
    """Article links go to their pages; other repository files to GitHub; everything else is left alone."""
    here = md.parent
    back = up(out_rel)

    def fix(m):
        attr, url = m.group(1), html.unescape(m.group(2))
        if re.match(r"^[a-z][a-z0-9+.-]*:|^#|^//", url, re.I):
            return m.group(0)
        path, _, anchor = url.partition("#")
        tail = "#" + anchor if anchor else ""
        target = (here / path).resolve()
        if target in OUTSIDE:
            return f'{attr}="{html.escape(back + OUTSIDE[target])}{tail}"'
        try:
            target.relative_to(HELP)
        except ValueError:
            try:
                return f'{attr}="{html.escape(BLOB + target.relative_to(ROOT).as_posix())}{tail}"'
            except ValueError:
                return m.group(0)
        if target.suffix == ".md" and left_out(target):
            return f'{attr}="{html.escape(BLOB + target.relative_to(ROOT).as_posix())}{tail}"'
        if target.suffix == ".md":
            return f'{attr}="{html.escape(back + page_path(target).as_posix())}{tail}"'
        if md.is_relative_to(HELP):
            return f'{attr}="{html.escape(path)}{tail}"'  # an image or another file copied next to the pages
        return f'{attr}="{html.escape(BLOB + target.relative_to(ROOT).as_posix())}{tail}"'

    # Only real tags: code samples are escaped (&lt;script src="..."&gt;), so their addresses stay as written.
    return re.sub(r"<[a-zA-Z][^<>]*>", lambda t: re.sub(r'\b(href|src)="([^"]*)"', fix, t.group(0)), body)


def crumbs_and_body(text):
    """The first line of an article is its trail, "[Help centre](../README.md) · Apps · how-to". Returns (trail
    parts, kind, the rest)."""
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


def icon(name, root, size=20, cls=""):
    return (f'<svg class="i{" i-lg" if size >= 20 else ""}{" " + cls if cls else ""}" width="{size}" height="{size}" aria-hidden="true" '
            f'focusable="false"><use href="{root}assets/icons/sprite.svg#i-{name}"/></svg>')


def md_title(md):
    m = re.search(r"^# (.+)$", md.read_text(encoding="utf-8"), re.M)
    return plain(markdown.markdown(m.group(1))) if m else md.stem.replace("-", " ").capitalize()


def convert(text, md, out_rel, root):
    """Markdown to the article's HTML: links, callouts, tables, paid links, flow charts and answer cards."""
    if len(STRIP) == 2:
        text = re.sub(re.escape(STRIP[0]) + r".*?" + re.escape(STRIP[1]), "", text, flags=re.S)
    flows = []

    def keep_flow(m):
        flows.append(m.group(1))
        return f"\n\nHELPFLOWCHART{len(flows) - 1}\n\n"
    text = re.sub(r"^```flow[ \t]*\n(.*?)^```[ \t]*$", keep_flow, text, flags=re.S | re.M)
    conv = markdown.Markdown(extensions=["tables", "sane_lists", "toc", "pymdownx.superfences"],
                             extension_configs={"toc": {"slugify": slug}}, output_format="html")
    body = fix_links(conv.convert(text), md, out_rel)
    body = re.sub(r"<pre(?![^>]*tabindex)", '<pre tabindex="0"', body)
    tones = {"NOTE": ("info", "info"), "TIP": ("info", "info"), "IMPORTANT": ("success", "circle-check"),
             "WARNING": ("warning", "triangle-alert"), "CAUTION": ("danger", "circle-alert")}

    def callout(m):
        tone, ic = tones[m.group(1)]
        inner = re.sub(r"^\s*<p>\s*", "<p>", m.group(2).strip(), count=1)
        return f'<div class="notice help-callout" data-tone="{tone}">{icon(ic, root)}<div class="notice__body">{inner}</div></div>'
    body = re.sub(r"<blockquote>\s*<p>\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)</blockquote>",
                  lambda m: callout(m) if m.group(1) in tones else m.group(0), body, flags=re.S)
    title_guess = plain((re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S) or [None, ""])[1]) or "table"

    def wrap_table(m):
        head = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body[:m.start()], re.S)
        name = plain(head[-1]) if head else title_guess
        return f'<div class="help-table" role="region" tabindex="0" aria-label="Table: {html.escape(name)}">{m.group(0)}</div>'
    body = re.sub(r"<table>.*?</table>", wrap_table, body, flags=re.S)
    for mark in SPONSORED:
        body = re.sub(r'<a href="([^"]*' + re.escape(html.escape(mark)) + r'[^"]*)">(.*?)</a>',
                      r'<a href="\1" rel="sponsored noopener" target="_blank">\2<span class="visually-hidden"> (opens in a new tab)</span></a>',
                      body, flags=re.S)
    h2s = [(i, plain(t)) for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)]
    answers = {}

    def describe(n):
        k = n["kind"]
        if k == "answer":
            hid = n.get("heading")
            label = f'{n["number"]}. {html.escape(n["text"])}'
            return f'<a href="#{hid}">{label}</a>' if hid else label
        if k == "link":
            path, _, anchor = n["href"].partition("#")
            target = (md.parent / path).resolve()
            if target in OUTSIDE:
                href = up(out_rel) + OUTSIDE[target]
            elif target.is_relative_to(HELP):
                href = up(out_rel) + page_path(target).as_posix()
            else:
                href = BLOB + target.relative_to(ROOT).as_posix()
            return f'<a href="{html.escape(href)}{"#" + anchor if anchor else ""}">{html.escape(n["text"])}</a>'
        if k == "q":
            return f"<strong>{html.escape(n['text'])}</strong>"
        if k == "start":
            return f"<strong>Start:</strong> {html.escape(n['text'])}"
        return html.escape(n["text"])

    def link_title(target):
        path = (md.parent / target.partition("#")[0]).resolve()
        if not path.exists():
            raise flowchart.FlowError(f"the chart links to {target}, which does not exist")
        return md_title(path)

    def place(chart):
        """Finds each numbered answer's section: #its-id, else the heading that starts with its number."""
        for node in chart["nodes"].values():
            if node["kind"] != "answer":
                continue
            hid = node["anchor"] if any(i == node["anchor"] for i, _ in h2s) else ""
            if node["anchor"] and not hid:
                warn(f"{md.relative_to(ROOT)}: answer {node['number']} names #{node['anchor']}, which is not a section heading")
            if not hid:
                hid = next((i for i, t in h2s if re.match(rf"^{re.escape(node['number'])}[.:]\s", t)), "")
            if not hid:
                hid = next((i for i, t in h2s if t.lower() == node["text"].lower()), "")
            if not hid:
                warn(f"{md.relative_to(ROOT)}: answer {node['number']} of the chart has no section (a heading starting "
                     f"\"{node['number']}. \", or #its-id on the chart's line)")
            node["heading"] = hid
            if hid:
                answers[hid] = node["number"]

    for n, src in enumerate(flows):
        try:
            chart = flowchart.parse_flow(src, md.name)
            place(chart)
            out = flowchart.render(chart, f"flow-{n + 1}", describe, link_title, chart["title"])
        except flowchart.FlowError as e:
            raise SystemExit(f"Flow chart in {md.relative_to(ROOT)}: {e}")
        body = body.replace(f"<p>HELPFLOWCHART{n}</p>", out)
    # Simple Mermaid flowcharts are drawn the same way, with no library; anything else stays as its code.
    count = [len(flows)]

    def mermaid(m):
        chart = flowchart.parse_mermaid(html.unescape(re.sub(r"<[^>]+>", "", m.group(1))))
        if not chart:
            warn(f"{md.relative_to(ROOT)}: a Mermaid chart the builder cannot draw is shown as its code; write it as a flow block")
            return m.group(0)
        count[0] += 1
        return flowchart.render(chart, f"flow-{count[0]}", describe)
    body = re.sub(r'(?:<div class="highlight">)?<pre[^>]*><code class="language-mermaid">(.*?)</code></pre>(?:</div>)?', mermaid, body, flags=re.S)
    # Each numbered answer's section becomes an answer card: the number and heading on a grey band.
    if answers:
        heads = list(re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S))
        stops = [m.start() for m in heads] + [len(body)]
        for i in reversed(range(len(heads))):
            m = heads[i]
            if m.group(1) not in answers:
                continue
            num = answers[m.group(1)]
            inner = re.sub(rf"^\s*{re.escape(num)}[.:]\s*", "", m.group(2))
            end = stops[i + 1]
            card = (f'<section class="answer-card" aria-labelledby="{m.group(1)}"><div class="answer-card__band">'
                    f'<h2 id="{m.group(1)}"><span class="answer-card__n">{html.escape(num)}</span> {inner}</h2></div>'
                    f'<div class="answer-card__body">{body[m.end():end]}</div></section>')
            body = body[:m.start()] + card + body[end:]
    return body


# ---- The site's structure ------------------------------------------------------------------------------------

def readme_order():
    """Where each article is listed on the help home, so the side menu keeps the same order."""
    order = {}
    readme = HELP / "README.md"
    if readme.exists():
        for n, target in enumerate(re.findall(r"\]\(([^)#\s]+\.md)\)", readme.read_text(encoding="utf-8"))):
            order.setdefault((HELP / target).resolve(), n)
    return order


def legacy_tree():
    """No areas in help-centre.json: the help home's own lists, one folding item for each heading."""
    areas, current = [], None
    for line in (HELP / "README.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#{2,3} (.+)", line)
        if m:
            current = {"key": slug(m.group(1)), "label": re.split(r":", m.group(1))[0].strip(), "icon": "",
                       "groups": [{"key": "", "label": "", "pages": []}]}
            areas.append(current)
            continue
        m = re.match(r"^- \[([^\]]+)\]\(([^)#]+\.md)\)", line)
        if m and current is not None:
            current["groups"][0]["pages"].append({"title": m.group(1), "url": page_path(HELP / m.group(2)).as_posix()})
    return [a for a in areas if a["groups"][0]["pages"]]


def standard_areas():
    by_key = {a["key"]: a for a in CFG.get("areas", [])}
    unknown = set(by_key) - {k for k, _, _ in STANDARD}
    if unknown:
        raise SystemExit(f"help-centre.json: areas must be the standard's ({', '.join(k for k, _, _ in STANDARD)}), not {', '.join(sorted(unknown))}")
    out = []
    for key, label, ic in STANDARD:
        a = by_key.get(key, {})
        out.append({"key": key, "label": a.get("label", label), "icon": a.get("icon", ic), "intro": a.get("intro", ""), "link_card": a.get("link_card"),
                    "none": a.get("none", f"There is nothing under {a.get('label', label)} yet."),
                    "groups": [{"key": g["key"], "label": g["label"], "intro": g.get("intro", ""), "pages": []} for g in a.get("groups", [])]})
    return out


def plugin_list():
    """The plug-ins, from help-centre.json's "plugins" and the collection's catalogue."""
    pc = CFG.get("plugins")
    if not pc:
        return []
    cat = {}
    if pc.get("catalogue"):
        data = json.loads((ROOT / pc["catalogue"]).read_text(encoding="utf-8"))
        cat = {p["id"]: p for p in (data.get("plugins", data) if isinstance(data, dict) else data)}
    groups, seen = [], set()
    for g in pc["groups"]:
        items = []
        for pid in g["ids"]:
            seen.add(pid)
            info = {**cat.get(pid, {}), **pc.get("details", {}).get(pid, {})}
            if not info.get("name"):
                raise SystemExit(f"help-centre.json: plug-in {pid} is not in the catalogue and has no name")
            status = info.get("status") or (["Published", "success"] if info.get("published") else ["Not published yet", "muted"])
            items.append({"id": pid, "name": info["name"], "summary": info.get("description", ""), "version": info.get("version", ""),
                          "api": info.get("starboard_api", ""), "status": status, "icon": info.get("icon", ""), "group": g["label"],
                          "logo": info.get("logo", ""), "logo_ext": ""})
        groups.append({"label": g["label"], "key": slug(g["label"]), "plugins": items})
    missing = sorted(set(cat) - seen)
    if missing:
        warn(f"plug-ins in the catalogue but in no group: {', '.join(missing)}")
    return groups


def plugin_icon(p, root, compact=True):
    cls = "app-icon" + (" app-icon--compact" if compact else "")
    if p.get("logo_ext"):  # its own logo, a rounded tile (API 1.14 logo), from the catalogue; the name is beside it
        return f'<span class="{cls} has-image"><img src="{root}assets/logos/{p["id"]}.{p["logo_ext"]}" alt="" width="40" height="40"></span>'
    if p["icon"]:
        return f'<span class="{cls}" aria-hidden="true">{icon(p["icon"], root, 18)}</span>'
    initials = "".join(w[0] for w in re.findall(r"[A-Za-z0-9]+", p["name"])[:2]).upper()
    return f'<span class="{cls}" aria-hidden="true">{html.escape(initials)}</span>'


# ---- Shared parts of every page ------------------------------------------------------------------------------

def side_tree(tree, plugins, here, root, current_area="", current_group=""):
    """The side menu. here: the page's own address; current_area and current_group: what is open."""
    chev = icon("chevron-right", root, 16, "side-tree__chev")
    out = [f'<a class="side-tree__home" href="{root}index.html"{" aria-current=\"page\"" if here == "index.html" else ""}>'
           f'<span class="side-tree__tile">{icon("house", root, 18)}</span>Home</a>']

    def link(url, title):
        return f'<li><a href="{root}{url}"{" aria-current=\"page\"" if url == here else ""}>{html.escape(title)}</a></li>'

    def area_html(a):
        is_open = a["key"] == current_area
        tile = f'<span class="side-tree__tile">{icon(a["icon"], root, 18)}</span>' if a["icon"] else ""
        parts = [f'<details class="side-tree__area"{" open" if is_open else ""}><summary>{tile}{html.escape(a["label"])}{chev}</summary>']
        extra = [link(u, t) for u, t in a.get("first", [])]
        if extra:
            parts.append(f"<ul>{''.join(extra)}</ul>")
        for g in a["groups"]:
            if not g["pages"]:
                continue
            if not g["label"]:
                parts.append(f"<ul>{''.join(link(p['url'], p['title']) for p in g['pages'])}</ul>")
                continue
            g_open = is_open and g["key"] == current_group
            n = len(g["pages"])
            parts.append(f'<details class="side-tree__group"{" open" if g_open else ""}><summary>{g.get("lead", "")}{html.escape(g["label"])}'
                         f'<span class="side-tree__count"><span class="visually-hidden">, </span>{n}'
                         f'<span class="visually-hidden"> {"page" if n == 1 else "pages"}</span></span>{chev}</summary>'
                         f"<ul>{''.join(link(p['url'], p['title']) for p in g['pages'])}</ul></details>")
        parts.append("</details>")
        return "".join(parts)

    for a in tree:
        if a["key"] == "plugins" and plugins:
            if any(g["pages"] for g in a["groups"]):  # the area's own articles (adding, looking after) come first
                out.append(area_html(a))
            for pg in plugins:
                out.append(area_html({"key": "plugins:" + pg["key"], "label": pg["label"], "icon": "puzzle", "groups": [
                    {"key": p["id"], "label": p["name"], "lead": plugin_icon(p, root),
                     "pages": [{"url": f"plugins/{p['id']}/{'index' if k == 'overview' else k}.html", "title": t} for k, t in PLUGIN_PAGES]}
                    for p in pg["plugins"]]}))
            continue
        if a["key"] == "dev" and CFG.get("areas"):
            out.append('<p class="side-tree__label">For builders</p>')
        out.append(area_html(a))
    return f'<nav class="side-tree" aria-label="Help menu">{"".join(out)}</nav>'


def top_links(root, current):
    if not CFG.get("areas"):
        return ""
    labels = {a["key"]: a.get("label") for a in CFG.get("areas", [])}
    items = [("index.html", "Home", "home")] + [(f"areas/{k}.html", labels.get(k) or label, k) for k, label, _ in STANDARD]
    lis = "".join(f'<li><a href="{root}{u}"{" aria-current=\"page\"" if k == current else ""}>{html.escape(label)}</a></li>'
                  for u, label, k in items)
    return f'<nav class="top-links" aria-label="Main help areas"><ul>{lis}</ul></nav>'


def crumbs_html(items):
    lis = "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' if u else f"<li>{html.escape(t)}</li>" for t, u in items[:-1])
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{lis}<li aria-current="page">{html.escape(items[-1][0])}</li></ol></nav>'


def toc_html(body):
    """The article's sections, for On this page (beside the article; inside it on phones)."""
    heads = [(i, plain(t)) for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)]
    if len(heads) < 2:
        return "", ""
    links = "".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in heads)
    side = f'<nav class="help-toc" aria-labelledby="help-toc-h"><h2 class="help-toc__heading" id="help-toc-h">On this page</h2><ul>{links}</ul></nav>'
    inline = f'<details class="disclosure help-toc-inline"><summary>On this page</summary><div class="disclosure__body"><ul>{links}</ul></div></details>'
    return side, inline


MAKER_MARK = ('<svg class="maker-mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><rect x="1" y="1" width="30" height="30" '
              'fill="var(--color-logo-tile)"/><path fill="var(--color-bg)" d="M17 6.5h7.5q2.5 0 2.5 2.2V11h-4v.8h2.6v1.6H21v2.2l2.6 1.5-.6 1-2-1.1V20q0 '
              '2.2-2.4 2.9l.9 3.8h1.6V28h-4.3l-.9-4.4h-1.6l-.8 3.1h1.4V28h-4.1l1-4.9q-3.6-1-8.7.3 3.4-3.6 8.2-5.2 3.3-1.3 3.9-4.6V8.4q0-1.9 1.4-1.9Z"/>'
              '<circle cx="20" cy="8.6" r="1" fill="var(--color-logo-star)"/></svg>')


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
{counter}</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header site-header--no-rail">
  <div class="site-header__bar help-bar">
    <a class="site-header__brand" href="{root}index.html">{logo}<span>{site_title}</span></a>
    {top_links}
    <div class="help-bar__tools">
      <button class="icon-btn help-menu-btn" type="button" aria-expanded="false" aria-controls="help-side">{icon_menu}<span class="label">Menu</span></button>
      <a class="icon-btn help-search-btn" href="{root}search.html">{icon_search}<span class="label">Search</span></a>
      <button class="icon-btn" type="button" data-opens="help-display" aria-haspopup="dialog" aria-expanded="false">{icon_display}<span class="label">Display</span></button>
    </div>
  </div>
</header>
{banner}
<div class="help-hub">
<div class="help-side" id="help-side" data-side-scroll>
  <form class="help-search" id="help-search" role="search" aria-label="Search the help" action="{root}search.html">
    <label class="visually-hidden" for="help-side-q">Search the help</label>
    <input class="input" type="search" id="help-side-q" name="q" placeholder="Search the help" autocomplete="off">
  </form>
  {side}
</div>
<main id="main" tabindex="-1" class="help-main{main_class}">
{band}
<div class="help-article{layout_class}">
<div class="help-article__body">
{crumbs}
{toc_inline}
{content}
{edit}
</div>
{toc}
</div>
</main>
</div>
<footer class="site-footer help-footer">
  <div class="site-footer__app">
    <span class="site-footer__brand">{logo}{name} help</span>
    <nav aria-label="{name} help"><ul class="site-footer__links">
      <li><a href="{root}index.html">Help centre</a></li>
      <li><a href="{repo}" target="_blank" rel="noopener noreferrer">GitHub repository<span class="visually-hidden"> (opens in a new tab)</span></a></li>
      <li><a href="{repo}/issues" target="_blank" rel="noopener noreferrer">Report a problem with this help<span class="visually-hidden"> (opens in a new tab)</span></a></li>
      {notice_link}
    </ul></nav>
  </div>
  <a class="site-footer__maker" href="https://github.com/TheMightyTRex" rel="me noopener noreferrer" target="_blank">{maker_mark}TheMightyTRexUK<span class="visually-hidden">, on GitHub (opens in a new tab)</span>{icon_external}</a>
</footer>
{notice_panel}<div class="side-panel-layer" id="help-display" hidden>
  <div class="side-panel-backdrop"></div>
  <aside class="side-panel" role="dialog" aria-modal="true" aria-labelledby="help-display-h">
    <div class="panel-header"><h2 class="panel-header__title" id="help-display-h">Display and accessibility</h2><button class="icon-btn" type="button" data-closes aria-label="Close display and accessibility">{icon_x}</button></div>
    <form class="side-panel__body form-stack" id="help-display-form">
      <fieldset><legend>Theme</legend><div class="segmented"><label><input type="radio" name="theme" value="system"><span>Match device</span></label><label><input type="radio" name="theme" value="light"><span>Light</span></label><label><input type="radio" name="theme" value="dark"><span>Dark</span></label></div></fieldset>
      <fieldset><legend>Text size</legend><div class="segmented"><label><input type="radio" name="text" value="100"><span>100%</span></label><label><input type="radio" name="text" value="125"><span>125%</span></label><label><input type="radio" name="text" value="150"><span>150%</span></label><label><input type="radio" name="text" value="175"><span>175%</span></label></div></fieldset>
      <fieldset><legend>Reduce motion</legend><div class="segmented"><label><input type="radio" name="motion" value="device"><span>Match device</span></label><label><input type="radio" name="motion" value="on"><span>Active</span></label><label><input type="radio" name="motion" value="off"><span>Inactive</span></label></div></fieldset>
      <label class="switch" for="help-pref-contrast"><span>High contrast</span><input type="checkbox" role="switch" id="help-pref-contrast" name="contrast"></label>
      <label class="switch" for="help-pref-underline"><span>Underline links</span><input type="checkbox" role="switch" id="help-pref-underline" name="underline"></label>
      <label class="switch" for="help-pref-spacing"><span>Wider text spacing</span><input type="checkbox" role="switch" id="help-pref-spacing" name="spacing"></label>
      <p class="small muted">Choices apply at once and are kept in this browser.</p>
    </form>
    <div class="side-panel__foot"><button class="btn btn--primary" type="button" data-closes>Close</button><button class="btn" type="button" id="help-display-reset">Reset to defaults</button></div>
  </aside>
</div>
<div id="help-announcer" class="visually-hidden" aria-live="polite"></div>
<script>window.SharedComponentsSprite = "{root}assets/icons/sprite.svg";</script>
<script src="{root}assets/components.js"></script>
<script src="{root}assets/help.js"></script>
</body>
</html>
"""

# Display and accessibility: the same choices and classes as the app, applied before the page draws so it never
# flashes. Kept in this browser only. "js" lets the phone menu fold away only when script can open it again.
PREFS_JS = ("document.documentElement.classList.add('js');"
            "try{var p=JSON.parse(localStorage.getItem('help-display')||'{}'),r=document.documentElement;"
            "if(p.theme&&p.theme!=='system')r.dataset.theme=p.theme;if(p.text&&p.text!=='100')r.classList.add('pref-text-'+p.text);"
            "if(p.contrast)r.classList.add('pref-contrast');if(p.motion==='on')r.classList.add('pref-motion');"
            "if(p.motion==='off')r.classList.add('pref-motion-off');if(p.underline)r.classList.add('pref-underline');"
            "if(p.spacing)r.classList.add('pref-spacing');"
            "if(localStorage.getItem('help-banner')==='hidden')r.classList.add('help-banner-hidden');"
            "__ROTATE__}catch(e){}")
ROTATE_JS = ("var b=Number(localStorage.getItem('help-banner-next'))||0;localStorage.setItem('help-banner-next',(b+1)%__BC__);"
             "r.dataset.banner=b%__BC__")


class Site:
    def __init__(self, tree, plugins):
        self.tree, self.plugins = tree, plugins

    def page(self, out_rel, title, content, *, description="", crumbs="", edit="", area="", group="",
             toc=("", ""), band="", main_class=""):
        root = up(out_rel)
        return TEMPLATE.format(
            site_title=html.escape(TITLE), title=html.escape(title), description=html.escape(description[:200]),
            canonical=SITE + out_rel, root=root, logo=LOGO, crumbs=crumbs, content=content, edit=edit, repo=REPO,
            name=html.escape(NAME), band=band, main_class=main_class, counter=COUNTER,
            prefs_js=PREFS_JS.replace("__ROTATE__", ROTATE_JS.replace("__BC__", str(BANNER_COUNT)) if BANNER_COUNT > 1 else ""),
            notice_link=(f'<li><button class="site-footer__link-btn" type="button" data-opens="help-notice" aria-haspopup="dialog" '
                         f'aria-expanded="false">{html.escape(NOTICE_LABEL)}</button></li>') if NOTICE_LABEL else "",
            notice_panel=(f'<div class="side-panel-layer" id="help-notice" hidden><div class="side-panel-backdrop"></div>'
                          f'<aside class="side-panel" role="dialog" aria-modal="true" aria-labelledby="help-notice-h">'
                          f'<div class="panel-header"><h2 class="panel-header__title" id="help-notice-h">{html.escape(NOTICE_LABEL)}</h2>'
                          f'<button class="icon-btn" type="button" data-closes aria-label="Close">{icon("x", root)}</button></div>'
                          f'<div class="side-panel__body help-notice">{FOOTER_NOTE}</div>'
                          f'<div class="side-panel__foot"><button class="btn btn--primary" type="button" data-closes>Close</button></div>'
                          f'</aside></div>') if NOTICE_LABEL else "",
            maker_mark=MAKER_MARK, icon_external=icon("external-link", root, 16),
            banner=(f'<aside class="help-banner" id="help-banner" aria-label="{html.escape(BANNER_LABEL)}">'
                    f'<div class="help-banner__body" data-count="{BANNER_COUNT}">{BANNER}</div>'
                    f'<button class="icon-btn help-banner__hide" type="button" aria-label="Hide this {html.escape(BANNER_LABEL.lower())}">'
                    f'{icon("x", root)}</button></aside>') if BANNER else "",
            side=side_tree(self.tree, self.plugins, out_rel, root, area, group),
            top_links=top_links(root, "home" if out_rel == "index.html" else area.split(":")[0] if area else ""),
            toc=toc[0], toc_inline=toc[1], layout_class="" if toc[0] else " help-article--no-toc",
            icon_menu=icon("menu", root), icon_search=icon("search", root), icon_display=icon("sun", root), icon_x=icon("x", root))


def version():
    """The latest version, never typed by hand: "version_from" names a changelog (the first released version in
    it, not Unreleased) or a file that holds only the version."""
    if CFG.get("version"):
        return CFG["version"]
    src = CFG.get("version_from")
    if not src:
        return ""
    text = (ROOT / src).read_text(encoding="utf-8")
    if src.endswith(".md"):
        m = re.search(r"^##\s*\[?v?(\d+\.\d+\.\d+)\]?", text, re.M)
        if not m:
            raise SystemExit(f"help-centre.json: no version found in {src}")
        return m.group(1)
    return text.strip().splitlines()[0].strip()


def resolve(to, root):
    """A link in help-centre.json: an article (x.md, from the help folder), a page (solver.html, areas/fix.html) or
    an address."""
    if re.match(r"^[a-z]+:", to):
        return to
    path, _, anchor = to.partition("#")
    tail = "#" + anchor if anchor else ""
    if path.endswith(".md"):
        target = (HELP / path).resolve()
        if not target.exists():
            raise SystemExit(f"help-centre.json: {to} does not exist in {HELP.relative_to(ROOT)}")
        if target in OUTSIDE:
            return root + OUTSIDE[target] + tail
        return root + page_path(target).as_posix() + tail
    return root + path + tail


# ---- The pages -----------------------------------------------------------------------------------------------

def journey_html(cfg, root, uid="journey"):
    stages = cfg["stages"]
    out = []
    for i, s in enumerate(stages, 1):
        cards = "".join(f'<li><a class="stage-card{" is-lead" if j == 0 else ""}" href="{html.escape(resolve(c["to"], root))}">'
                        f'<b>{html.escape(c["title"])}</b><span>{html.escape(c.get("line", ""))}</span></a></li>'
                        for j, c in enumerate(s.get("cards", [])))
        out.append(f'<li class="journey__stage" data-tone="{s.get("tone", "step")}"><div class="journey__marker" aria-hidden="true">'
                   f'<span class="journey__dot">{icon(s.get("icon", "circle"), root, 28)}</span><span class="journey__n">{i}</span></div>'
                   f'<h3 class="journey__label">{i} · {html.escape(s["label"])}</h3><ul class="journey__cards">{cards}</ul></li>')
    intro = cfg.get("intro", "Follow the path, or go straight to any stage.")
    return (f'<section class="journey" aria-labelledby="{uid}-h"><h2 id="{uid}-h">{html.escape(cfg["title"])}</h2>'
            f'<p>{html.escape(intro)}</p><ol class="journey__stages" style="--stages: {len(stages)}">{"".join(out)}</ol></section>')


def featured_html(f, root):
    pic = ""
    if f.get("flow"):
        chart = flowchart.parse_flow(f["flow"], "help-centre.json featured")
        pic = flowchart.render(chart, "feature-flow", lambda n: html.escape(n["text"]))
    elif f.get("image"):
        pic = f'<img src="{root}{html.escape(f["image"])}" alt="{html.escape(f.get("alt", ""))}">'
    pic_html = f'<div class="feature-card__pic">{pic}</div>' if pic else ""
    return (f'<section class="feature-card" aria-labelledby="feature-h"><div class="feature-card__text">'
            f'<span class="chip" data-tone="info">{html.escape(f.get("chip", "New"))}</span><h2 id="feature-h">{html.escape(f["title"])}</h2>'
            f'<p>{html.escape(f.get("text", ""))}</p><a class="btn btn--primary" href="{html.escape(resolve(f["to"], root))}">'
            f'{html.escape(f.get("button", "Read how it works"))}</a></div>{pic_html}</section>')


def solver_card(s, root):
    return (f'<section class="solver-card" aria-labelledby="solver-card-h"><span class="side-tree__tile solver-card__tile">'
            f'{icon("wrench", root, 28)}</span><div><h2 id="solver-card-h">{html.escape(s.get("card_title", "Something not working?"))}</h2>'
            f'<p>{html.escape(s.get("card_text", "The problem solver asks up to four questions and takes you to the right fix."))}</p></div>'
            f'<a class="btn btn--primary" href="{root}solver.html">{html.escape(s.get("button", "Start the problem solver"))}</a></section>')


def link_card(c, root, key):
    """An area's link card (help-centre.json, an area's "link_card"): one card at the top of the area's page that leads
    somewhere else, such as another help centre, in the problem solver card's shape."""
    to = c["to"] if c["to"].startswith(("https://", "http://")) else root + c["to"]
    return (f'<section class="solver-card" aria-labelledby="link-card-{key}"><span class="side-tree__tile solver-card__tile">'
            f'{icon(c.get("icon", "puzzle"), root, 28)}</span><div><h2 id="link-card-{key}">{html.escape(c["title"])}</h2>'
            f'<p>{html.escape(c["text"])}</p></div><a class="btn btn--primary" href="{html.escape(to)}">{html.escape(c["button"])}</a></section>')


def plugin_cards(group, root, level=3):
    cards = []
    for p in group["plugins"]:
        base = f"{root}plugins/{p['id']}/"
        cards.append(f'<li><article class="card has-band plugin-card"><div class="card-band">{plugin_icon(p, root)}'
                     f'<h{level} class="card-band__title"><a href="{base}index.html">{html.escape(p["name"])}</a></h{level}>'
                     f'<span class="card-band__side"><span class="chip" data-tone="{p["status"][1]}">{html.escape(p["status"][0])}</span></span></div>'
                     f'<p>{html.escape(p["summary"])}</p><ul class="plugin-card__links" aria-label="{html.escape(p["name"])} pages">'
                     f'<li><a href="{base}install.html">Install</a></li><li><a href="{base}settings.html">Settings</a></li>'
                     f'<li><a href="{base}problems.html">Problems</a></li></ul></article></li>')
    return f'<ul class="plugin-cards">{"".join(cards)}</ul>'


def solver_tree(node, root, depth=1):
    if depth > 4:
        raise SystemExit("help-centre.json: the problem solver asks at most four questions on any path")
    h = f"h{min(depth + 1, 6)}"
    items = []
    for a in node["answers"]:
        if "next" in a:
            items.append(f'<li><span class="solver__choice">{html.escape(a["label"])}</span>{solver_tree(a["next"], root, depth + 1)}</li>')
        else:
            items.append(f'<li><a href="{html.escape(resolve(a["to"], root))}">{html.escape(a["label"])}</a></li>')
    return f'<div class="solver__node"><{h} class="solver__question">{html.escape(node["question"])}</{h}><ul class="solver__answers">{"".join(items)}</ul></div>'


def build(out):
    site = out / "help"
    if site.exists():
        shutil.rmtree(site)
    (site / "assets" / "css" / "fonts").mkdir(parents=True)
    (site / "assets" / "icons").mkdir()
    for name in ("tokens.css", "components.css"):
        shutil.copy(DS / name, site / "assets" / "css" / name)
    for f in (DS / "fonts").iterdir():  # tokens.css looks for its fonts beside it
        shutil.copy(f, site / "assets" / "css" / "fonts" / f.name)
    shutil.copy(HERE / "help.css", site / "assets" / "css" / "help.css")
    shutil.copy(HERE / "help.js", site / "assets" / "help.js")
    if FAVICON and FAVICON.exists():
        shutil.copy(FAVICON, site / "assets" / "favicon.svg")
    else:
        (site / "assets" / "favicon.svg").write_text(re.sub(r'\sclass="help-logo"[^>]*?focusable="false"', ' xmlns="http://www.w3.org/2000/svg"', LOGO, count=1), encoding="utf-8")
    shutil.copy(DS / "components.js", site / "assets" / "components.js")
    shutil.copy(DS / "icons.svg", site / "assets" / "icons" / "sprite.svg")
    if (HELP / "images").is_dir():
        shutil.copytree(HELP / "images", site / "images")

    standard = bool(CFG.get("areas"))
    plugins = plugin_list() if standard else []
    pc = CFG.get("plugins", {})
    # Each plug-in's logo from the catalogue (a data address), written once as a file the pages share.
    for g in plugins:
        for p in g["plugins"]:
            m = re.match(r"data:image/(svg\+xml|png);base64,([A-Za-z0-9+/=\s]+)$", p["logo"] or "")
            if m:
                p["logo_ext"] = "svg" if m.group(1).startswith("svg") else "png"
                (site / "assets" / "logos").mkdir(exist_ok=True)
                (site / "assets" / "logos" / f"{p['id']}.{p['logo_ext']}").write_bytes(base64.b64decode(m.group(2)))
    # Plug-in overviews may live outside the help folder (each plug-in's README): they are pages too.
    for g in plugins:
        for p in g["plugins"]:
            src = ROOT / pc.get("overview", "{id}/README.md").format(id=p["id"])
            if src.exists():
                OUTSIDE[src.resolve()] = f"plugins/{p['id']}/index.html"
    pages = sorted(p for p in HELP.rglob("*.md") if not left_out(p))
    if standard and pc:
        # A plug-in's own pages are built with it, not as articles.
        pages_root = (ROOT / pc.get("pages", "help/plugins/{id}/{page}.md").split("{id}")[0]).resolve()
        pages = [p for p in pages if not p.resolve().is_relative_to(pages_root)]
    order = readme_order()
    articles = []  # (md, out_rel, text, area, group)
    tree = standard_areas() if standard else legacy_tree()
    by_area = {a["key"]: a for a in tree}
    for md in pages:
        rel_out = page_path(md).as_posix()
        text = md.read_text(encoding="utf-8")
        check_written(text, str(md.relative_to(ROOT)))
        area = group = ""
        if standard and rel_out != "index.html":
            m = MARKER.search(text)
            if not m:
                warn(f"{md.relative_to(ROOT)}: no <!-- help: <area> / <group> --> line, so it is under Use it, Other")
                area, group = "use", "other"
            else:
                area, group = m.group(1), m.group(2)
            a = by_area.get(area)
            if not a:
                raise SystemExit(f"{md.relative_to(ROOT)}: area {area} is not one of the standard's")
            g = next((x for x in a["groups"] if x["key"] == group), None)
            if not g:
                if group != "other":
                    warn(f"{md.relative_to(ROOT)}: group {group} is not in help-centre.json under {area}, so it is under Other")
                g = next((x for x in a["groups"] if x["key"] == "other"), None)
                if not g:
                    g = {"key": "other", "label": "Other", "intro": "", "pages": []}
                    a["groups"].append(g)
                group = "other"
            g["pages"].append({"title": md_title(md), "url": rel_out, "order": order.get(md.resolve(), 10_000)})
        articles.append((md, rel_out, text, area, group))
    if standard:
        for a in tree:
            for g in a["groups"]:
                g["pages"].sort(key=lambda p: (p["order"], p["title"].lower()))
            a["first"] = [(f"areas/{a['key']}.html", "Overview")]
            if a["key"] == "fix" and CFG.get("solver"):
                a["first"].append(("solver.html", CFG["solver"].get("title", "Problem solver")))
    S = Site(tree, plugins)
    labels = {a["key"]: a["label"] for a in tree}
    group_labels = {(a["key"], g["key"]): g["label"] for a in tree for g in a["groups"]}
    index = []

    def write(rel, text):
        target = site / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    for md, rel_out, text, area, group in articles:
        if standard and rel_out == "index.html":
            continue  # the front page is built from help-centre.json below
        root = up(rel_out)
        trail, kind, rest = crumbs_and_body(text)
        body = convert(rest, md, rel_out, root)
        title_m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        title = plain(title_m.group(1)) if title_m else TITLE
        first_p = re.search(r"<p>(.*?)</p>", body, re.S)
        description = plain(first_p.group(1)) if first_p else ""
        if standard:
            g_label = group_labels.get((area, group), "Other")
            crumbs = crumbs_html([("Help centre", f"{root}index.html"), (labels[area], f"{root}areas/{area}.html"), (g_label, ""), (title, "")])
            section = f"{labels[area]} · {g_label}"
        else:
            section = SECTIONS.get(pathlib.PurePosixPath(rel_out).parts[0], "") if "/" in rel_out else ""
            items = [("Help centre", f"{root}index.html")] + ([(section, "")] if section else [])
            items += [(t, "") for t in trail if t and t != section] + [(title, "")]
            crumbs = crumbs_html(items) if rel_out != "index.html" else ""
        kind_html = f'<p class="prose__kind">{html.escape(kind.capitalize())}</p>\n' if kind else ""
        edit = (f'<p class="help-source small muted"><a href="{BLOB}{md.relative_to(ROOT).as_posix()}">'
                f"This page on GitHub</a>, where the help is written.</p>")
        write(rel_out, S.page(rel_out, title, f'<article class="prose">\n{kind_html}{body}\n</article>', description=description,
                              crumbs=crumbs, edit=edit, area=area, group=group,
                              toc=toc_html(body) if rel_out != "index.html" else ("", "")))
        headings = [plain(h) for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body, re.S)]
        words = plain(re.sub(r"<h1[^>]*>.*?</h1>", "", body, flags=re.S))
        if STOP:
            words = words.split(STOP)[0]
        index.append({"url": rel_out, "title": title, "section": section or (trail[0] if trail else ""),
                      "kind": kind, "summary": description[:220], "headings": headings, "text": words[:6000]})

    count = len(index)
    if standard:
        # The plug-ins' own pages: the same eight for every one, in the same order.
        for g in plugins:
            for p in g["plugins"]:
                for key, label in PLUGIN_PAGES:
                    rel_out = f"plugins/{p['id']}/{'index' if key == 'overview' else key}.html"
                    root = up(rel_out)
                    pattern = pc.get("overview", "{id}/README.md") if key == "overview" else pc.get("pages", "help/plugins/{id}/{page}.md")
                    src = ROOT / pattern.format(id=p["id"], page=key)
                    if src.exists():
                        check_written(src.read_text(encoding="utf-8"), str(src.relative_to(ROOT)))
                        _, _, text = crumbs_and_body(src.read_text(encoding="utf-8"))
                        text = re.sub(r"^# .*\n", "", text, count=1, flags=re.M)
                        body = convert(text, src, rel_out, root)
                        edit = (f'<p class="help-source small muted"><a href="{BLOB}{src.relative_to(ROOT).as_posix()}">'
                                f"This page on GitHub</a>, where the help is written.</p>")
                    elif key == "overview":
                        raise SystemExit(f"plug-in {p['id']}: no overview at {src.relative_to(ROOT)}")
                    else:
                        body = f"<p>{html.escape(pc.get('nothing', {}).get(key, NOTHING[key]).format(name=p['name']))}</p>"
                        edit = ""
                    body = f'<h1><span class="visually-hidden">{html.escape(p["name"])}: </span>{label}</h1>\n{body}'
                    sub = " · ".join(x for x in (f"Version {p['version']}" if p["version"] else "", f"plug-in API {p['api']}" if p["api"] else "") if x)
                    sub_html = f'<p class="plugin-band__sub">{html.escape(sub)}</p>' if sub else ""
                    band = (f'<div class="plugin-band">{plugin_icon(p, root, compact=False)}<div><p class="plugin-band__name">{html.escape(p["name"])}</p>'
                            f'{sub_html}</div><div class="plugin-band__side">'
                            f'<span class="chip" data-tone="{p["status"][1]}">{html.escape(p["status"][0])}</span>'
                            f'<a class="btn btn--primary" href="{root}plugins/{p["id"]}/install.html">How to add it</a></div></div>')
                    crumbs = crumbs_html([("Help centre", f"{root}index.html"), (labels["plugins"], f"{root}areas/plugins.html"),
                                          (g["label"], ""), (p["name"], f"{root}plugins/{p['id']}/index.html" if key != "overview" else ""), (label, "")])
                    write(rel_out, S.page(rel_out, f"{label} · {p['name']}", f'<article class="prose">\n{body}\n</article>',
                                          description=p["summary"], crumbs=crumbs, edit=edit, area="plugins:" + g["key"], group=p["id"],
                                          toc=toc_html(body), band=band, main_class=" help-main--band"))
                    index.append({"url": rel_out, "title": f"{p['name']}: {label}", "section": f"{labels['plugins']} · {g['label']}",
                                  "kind": "", "summary": p["summary"][:220],
                                  "headings": [plain(h) for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body, re.S)],
                                  "text": plain(body)[:6000]})
                    count += 1
        # The front page: the latest version beside the heading, the journey, the newest item, the problem solver.
        home = CFG.get("home", {})
        v = version()
        badge = ""
        if v:
            link = CFG.get("version_link") or BLOB + CFG.get("version_from", "CHANGELOG.md")
            badge = (f'<a class="version-badge" href="{html.escape(link)}"><span class="chip" data-tone="success">Latest version</span>'
                     f'<b>{html.escape(v)}</b><span class="visually-hidden"> (release notes)</span></a>')
        parts = [f'<div class="help-landing__head"><h1>{html.escape(home.get("title", f"Welcome to {NAME} help"))}</h1>{badge}</div>']
        if home.get("intro"):
            parts.append(f'<p class="help-landing__intro">{html.escape(home["intro"])}</p>')
        if CFG.get("journey"):
            parts.append(journey_html(CFG["journey"], ""))
        if CFG.get("featured"):
            parts.append(featured_html(CFG["featured"], ""))
        if CFG.get("solver"):
            parts.append(solver_card(CFG["solver"], ""))
        for g in plugins:
            parts.append(f'<section class="help-landing__group" aria-labelledby="pg-{g["key"]}"><h2 id="pg-{g["key"]}">{html.escape(g["label"])}</h2>{plugin_cards(g, "")}</section>')
        write("index.html", S.page("index.html", home.get("title", TITLE), f'<div class="help-landing">{"".join(parts)}</div>',
                                   description=home.get("intro", f"Help for {NAME}."), main_class=" help-main--landing"))
        # A page for each area: a card for each group, with every article in it.
        for a in tree:
            rel_out = f"areas/{a['key']}.html"
            root = "../"
            cards = []
            if a["key"] == "plugins" and plugins:
                for g in plugins:
                    cards.append(f'<section class="help-landing__group" aria-labelledby="pg-{g["key"]}"><h2 id="pg-{g["key"]}">{html.escape(g["label"])}</h2>{plugin_cards(g, root)}</section>')
            groups = [g for g in a["groups"] if g["pages"]]
            if groups:
                items = []
                for g in groups:
                    links = "".join(f'<li><a href="{root}{p["url"]}">{html.escape(p["title"])}</a></li>' for p in g["pages"])
                    intro = f'<p>{html.escape(g["intro"])}</p>' if g["intro"] else ""
                    items.append(f'<li><section class="card help-group-card" aria-labelledby="g-{g["key"]}"><h2 id="g-{g["key"]}">'
                                 f'{html.escape(g["label"])}</h2>{intro}<ul>{links}</ul></section></li>')
                cards.append(f'<ul class="help-group-cards">{"".join(items)}</ul>')
            if a["key"] == "fix" and CFG.get("solver"):
                cards.insert(0, solver_card(CFG["solver"], root))
            if a.get("link_card"):
                cards.insert(0, link_card(a["link_card"], root, a["key"]))
            if not cards:
                check_written(a["none"], f"help-centre.json, area {a['key']}")
                cards.append(f'<p>{html.escape(a["none"])}</p>')
            intro = f'<p class="help-landing__intro">{html.escape(a["intro"])}</p>' if a["intro"] else ""
            write(rel_out, S.page(rel_out, a["label"], f'<div class="help-landing"><h1>{html.escape(a["label"])}</h1>{intro}{"".join(cards)}</div>',
                                  description=a["intro"] or a["label"], area=a["key"], main_class=" help-main--landing",
                                  crumbs=crumbs_html([("Help centre", f"{root}index.html"), (a["label"], "")])))
        # The problem solver: the whole tree as lists of links; components.js asks one question at a time.
        if CFG.get("solver"):
            s = CFG["solver"]
            title = s.get("title", "Problem solver")
            content = (f'<div class="help-landing"><h1>{html.escape(title)}</h1>'
                       f'<p class="help-landing__intro">{html.escape(s.get("intro", "Answer up to four questions to find the right fix."))}</p>'
                       f'<div class="solver" data-solver>{solver_tree(s["start"], "")}</div></div>')
            write("solver.html", S.page("solver.html", title, content, area="fix", main_class=" help-main--landing",
                                        description=s.get("intro", ""), crumbs=crumbs_html([("Help centre", "index.html"),
                                                                                           (labels["fix"], "areas/fix.html"), (title, "")])))
        for a in tree:
            for g in a["groups"]:
                if g["key"] == "other" and g["pages"]:
                    warn(f"{len(g['pages'])} articles under {a['label']}, Other: give each a group")

    (site / "search-index.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    search_body = ('<h1>Search the help</h1>\n'
                   '<form class="help-search help-search--page" role="search" aria-label="Search again" action="search.html"><label class="visually-hidden" for="help-q">'
                   'Search the help</label><input class="input" type="search" id="help-q" name="q" autocomplete="off"></form>\n'
                   '<p id="help-results-count" class="muted" role="status" aria-live="polite">' + html.escape(EXAMPLE) + '</p>\n'
                   '<ol id="help-results" class="help-results"></ol>\n'
                   '<noscript><p>Search needs JavaScript. Every article is listed in the menu and on the '
                   '<a href="index.html">help centre home</a>.</p></noscript>')
    write("search.html", S.page("search.html", "Search the help", f'<div class="help-landing">{search_body}</div>',
                                description=f"Search the {TITLE}.", main_class=" help-main--landing"))
    if FRONT_DOOR:  # the site's own front door goes to the help centre, when the site is only the help
        (out / "index.html").write_text(f'<!doctype html><meta charset="utf-8"><title>{html.escape(TITLE)}</title>'
                                        '<meta http-equiv="refresh" content="0; url=help/index.html">'
                                        f'<a href="help/index.html">{html.escape(TITLE)}</a>\n', encoding="utf-8")
    (out / ".nojekyll").write_text("")
    return count


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--config", default="help-centre.json", help="the app's settings, at the app's root")
    ap.add_argument("--out", default="_site")
    ap.add_argument("--strict", action="store_true", help="stop with an error when there is a warning (an article with no group)")
    a = ap.parse_args()
    configure(a.config)
    n = build(pathlib.Path(a.out).resolve())
    for w in WARNINGS:
        print("warning:", w)
    print(f"{n} help pages in {a.out}/help, with search")
    if a.strict and WARNINGS:
        sys.exit(1)


if __name__ == "__main__":
    main()
