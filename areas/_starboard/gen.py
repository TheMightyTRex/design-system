"""Builds the Starboard area boards (areas/starboard-<slug>.src.html) from the fragments in this folder.

Each fragment (<slug>.frag.html) has a meta line and four parts:
  <!--meta {"title": "...", "main": "apps", "sub": "apps"}-->
  <!--note-->   the "What changed and why" text (inside the notice body)
  <!--page-->   the page content (inside <main><div class="page">)
  <!--phone-->  the phone-width version of the key part
  <!--panels--> slide-outs and dialogs
Directives inside any part:
  <!--include:name-->        the shared fragment _name.html
  <!--chart {json}-->         a line chart panel with a table view (no chart component in the library yet)
Run: python3 gen.py, then python3 ../../tools/build.py ../starboard-*.src.html ../index-starboard.src.html
Board scaffolding only; nothing here is part of the library.
"""
import json, pathlib, re, html

here = pathlib.Path(__file__).resolve().parent
areas = here.parent

LOGO = ('<svg viewBox="0 0 32 32" width="{s}" height="{s}" aria-hidden="true" focusable="false">'
        '<rect x="3" y="3" width="12" height="12" fill="var(--color-logo-tile)"/>'
        '<rect x="3" y="17" width="12" height="12" fill="var(--color-logo-tile)"/>'
        '<rect x="17" y="17" width="12" height="12" fill="var(--color-logo-tile)"/>'
        '<path d="M23 3.5l1.9 4.4 4.7.4-3.6 3.1 1.1 4.6-4.1-2.5-4.1 2.5 1.1-4.6-3.6-3.1 4.7-.4Z" '
        'fill="var(--color-logo-star)"/></svg>')

MAIN = [
    ("apps", "Apps", "layout-grid", "starboard-apps.html"),
    ("search", "Search", "search", "starboard-search.html"),
    ("downloads", "Downloads", "download", "starboard-downloads.html"),
    ("upcoming", "Coming up", "calendar-days", "starboard-coming-up.html"),
    ("system", "System", "activity", "starboard-overview.html"),
    ("settings", "Settings", "settings", "starboard-settings-apps.html"),
]
SUB = {
    "apps": [
        ("apps", "Apps", "layout-grid", "starboard-apps.html", ""),
        ("services", "Other services", "server-cog", "starboard-other-services.html", ""),
    ],
    "system": [
        ("overview", "Overview", "gauge", "starboard-overview.html", ""),
        ("storage", "Storage", "hard-drive", "starboard-storage.html", ""),
        ("disks", "Disk health", "heart-pulse", "starboard-disk-health.html", "1|to check"),
        ("monitor", "Monitor", "chart-line", "starboard-monitor.html", ""),
        ("network", "Network", "network", "starboard-network.html", ""),
        ("backup", "Backup and restore", "archive", "starboard-backup.html", ""),
    ],
    "settings": [
        ("settings-apps", "Manage apps", "app-window", "starboard-settings-apps.html", ""),
        ("general", "General", "sliders-horizontal", "starboard-settings-general.html", ""),
        ("security", "Security", "shield-check", "starboard-settings-security.html", ""),
        ("about", "About and updates", "info", "starboard-settings-about.html", ""),
    ],
}


def count(c):
    if not c:
        return ""
    n, what = c.split("|")
    return f' <span class="count">{n}<span class="visually-hidden"> {what}</span></span>'


def tabs(items, current, label, phone=False):
    out = [f'<nav class="menu-tabs" aria-label="{label}">']
    for key, name, icon, href, c in items:
        cur = ' aria-current="page"' if key == current else ""
        out.append(f'<a href="{href}"{cur}>{{{{i:{icon}}}}}<span class="menu-tabs__label">{name}</span>{count(c)}</a>')
    out.append("</nav>")
    return "".join(out)


def header(main, sub):
    main_items = [(k, n, i, h, "") for k, n, i, h in MAIN]
    row1 = tabs(main_items, main, "Main menu")
    row2 = ""
    if main in SUB:
        name = dict((k, n) for k, n, _, _ in MAIN)[main]
        row2 = f'<div class="site-header__tabs">{tabs(SUB[main], sub, name)}</div>'
    return f"""<header class="site-header">
  <div class="site-header__bar">
    <a class="site-header__brand" href="starboard-apps.html" style="display:inline-flex;padding-left:var(--space-5)">{LOGO.format(s=28)}Starboard</a>
    {row1}
    <form class="site-header__search search-field" role="search" action="starboard-search.html"><input class="input" type="search" name="q" aria-label="Search films, series, music and books" placeholder="Search films, series, music, books"><button class="visually-hidden" type="submit">Search</button></form>
    <div class="site-header__actions"><button class="icon-btn" type="button" data-dialog="display-dialog">{{{{i-lg:sun}}}}<span class="label">Display</span></button></div>
  </div>
  {row2}
</header>"""


def phone_header(main, sub):
    row2 = ""
    if main in SUB:
        items = SUB[main]
        name = dict((k, n) for k, n, _, _ in MAIN)[main]
        row2 = f'<div class="site-header__tabs">{tabs(items, sub, name + " (phone)")}</div>'
    return f"""<header class="site-header" style="position:relative">
        <div class="site-header__bar" style="height:60px;padding-inline:var(--space-4);gap:var(--space-3)">
          <button class="icon-btn" type="button" data-opens="phone-menu" aria-controls="phone-menu" aria-expanded="false">{{{{i-lg:menu}}}}<span class="visually-hidden">Menu</span></button>
          <span class="panel-header__brand">{LOGO.format(s=28)}Starboard</span>
          <button class="icon-btn" type="button" style="margin-left:auto" data-dialog="display-dialog" aria-label="Display">{{{{i-lg:sun}}}}</button>
        </div>
        {row2}
      </header>"""


def auth_header():
    return f"""<header class="site-header">
  <div class="site-header__bar" style="padding-left:var(--space-5)">
    <span class="panel-header__brand">{LOGO.format(s=28)}Starboard</span>
    <div class="site-header__actions" style="margin-left:auto"><button class="icon-btn" type="button" data-dialog="display-dialog">{{{{i-lg:sun}}}}<span class="label">Display</span></button></div>
  </div>
</header>"""


def phone_menu(main, sub):
    secs = []
    for key, name, icon, href in MAIN:
        cur = key == main
        if key in SUB:
            items = "".join(
                f'<li><a href="{h}"{" aria-current=\"page\"" if k == sub else ""}>{{{{i:{ic}}}}}{n}</a></li>'
                for k, n, ic, h, _ in SUB[key])
            secs.append(
                f'<div class="phone-menu__section"{" data-current" if cur else ""}>'
                f'<button type="button" aria-expanded="{"true" if cur else "false"}" aria-controls="pm-{key}">'
                f'{{{{i-lg:{icon}}}}}{name}{{{{i:chevron-right phone-menu__chevron}}}}</button>'
                f'<ul id="pm-{key}"{"" if cur else " hidden"}>{items}</ul></div>')
        else:
            style = ("display:flex;align-items:center;gap:var(--space-3);min-height:52px;padding:0 var(--space-4);"
                     "font-weight:var(--weight-strong);text-decoration:none;"
                     + ("color:var(--color-accent)" if cur else "color:var(--color-text)"))
            secs.append(f'<div class="phone-menu__section"><a href="{href}" style="{style}"'
                        f'{" aria-current=\"page\"" if cur else ""}>{{{{i-lg:{icon}}}}}{name}</a></div>')
    return f"""<div class="side-panel-layer" id="phone-menu" hidden>
  <div class="side-panel-backdrop"></div>
  <nav class="phone-menu" aria-label="Main menu">
    <div class="panel-header"><span class="panel-header__brand">{LOGO.format(s=24)}Starboard</span><button class="icon-btn" type="button" data-closes aria-label="Close menu">{{{{i:x}}}}</button></div>
    <form class="phone-menu__search" role="search" action="starboard-search.html"><input class="input" type="search" name="q" aria-label="Search films, series, music and books" placeholder="Search films, series, music, books"></form>
    <div class="phone-menu__sections">{"".join(secs)}</div>
    <div class="phone-menu__foot"><span class="small muted">Starboard v0.2.0</span><button class="btn" type="button">{{{{i:log-out}}}}Sign out</button></div>
  </nav>
</div>"""


DISPLAY = """<dialog class="dialog" id="display-dialog" aria-labelledby="display-h">
  <div class="panel-header"><h2 class="panel-header__title" id="display-h">Display and accessibility</h2><button class="icon-btn" type="button" data-closes aria-label="Close display and accessibility">{{i:x}}</button></div>
  <div class="dialog__body">
    <fieldset><legend class="field__label">Theme</legend><div class="segmented"><label><input type="radio" name="d-theme" value="light" data-display="theme" checked><span>Light</span></label><label><input type="radio" name="d-theme" value="dark" data-display="theme"><span>Dark</span></label></div></fieldset>
    <fieldset><legend class="field__label">Text size</legend><div class="segmented"><label><input type="radio" name="d-text" value="100" data-display="text" checked><span>100%</span></label><label><input type="radio" name="d-text" value="125" data-display="text"><span>125%</span></label><label><input type="radio" name="d-text" value="150" data-display="text"><span>150%</span></label><label><input type="radio" name="d-text" value="175" data-display="text"><span>175%</span></label></div></fieldset>
    <div>
      <label class="switch"><span class="check__text"><strong>High contrast</strong></span><input type="checkbox" role="switch" data-display="contrast"></label>
      <label class="switch"><span class="check__text"><strong>Reduce motion</strong></span><input type="checkbox" role="switch" data-display="motion"></label>
      <label class="switch"><span class="check__text"><strong>Underline links</strong></span><input type="checkbox" role="switch" data-display="underline"></label>
      <label class="switch"><span class="check__text"><strong>Wider text spacing</strong></span><input type="checkbox" role="switch" data-display="spacing"></label>
    </div>
  </div>
  <div class="dialog__foot"><button class="btn btn--primary" type="button" data-closes>Done</button><button class="btn btn--quiet" type="button">Reset</button></div>
</dialog>"""


def chart(spec):
    """A line chart drawn in SVG with a table view. spec: id, title, now, series [[name, [values]]], labels,
    max, unit, desc, tone (optional words beside the value)."""
    cid, title, now = spec["id"], spec["title"], spec["now"]
    series, labels = spec["series"], spec["labels"]
    top = spec.get("max") or max(max(v) for _, v in series) * 1.2
    unit = spec.get("unit", "")
    w, h, pad_l, pad_b = 600, 170, 44, 22
    n = len(series[0][1])
    def xy(i, v):
        x = pad_l + (w - pad_l - 8) * i / (n - 1)
        y = 8 + (h - pad_b - 8) * (1 - v / top)
        return f"{x:.1f},{y:.1f}"
    grid = []
    for k in range(5):
        v = top * k / 4
        y = 8 + (h - pad_b - 8) * (1 - k / 4)
        grid.append(f'<line x1="{pad_l}" x2="{w - 8}" y1="{y:.1f}" y2="{y:.1f}" stroke="var(--color-divider)" stroke-width="1"/>'
                    f'<text x="{pad_l - 6}" y="{y + 4:.1f}" text-anchor="end" font-size="15" fill="var(--color-text-muted)">{v:g}{unit}</text>')
    step = max(1, (n - 1) // 4)
    for i in range(0, n, step):
        x = pad_l + (w - pad_l - 8) * i / (n - 1)
        anchor = "start" if i == 0 else ("end" if i + step >= n else "middle")
        grid.append(f'<text x="{x:.1f}" y="{h - 4}" text-anchor="{anchor}" font-size="15" fill="var(--color-text-muted)">{labels[i]}</text>')
    lines = []
    for si, (name, vals) in enumerate(series):
        pts = " ".join(xy(i, v) for i, v in enumerate(vals))
        dash = ' stroke-dasharray="6 4"' if si == 1 else ""
        lines.append(f'<polyline fill="none" stroke="var(--chart-{si + 1})" stroke-width="2.5"{dash} points="{pts}"/>')
        lx, ly = xy(n - 1, vals[-1]).split(",")
        lines.append(f'<circle cx="{lx}" cy="{ly}" r="4" fill="var(--chart-{si + 1})"/>')
    legend = ""
    if len(series) > 1:
        legend = '<p class="small" style="display:flex;gap:var(--space-4);flex-wrap:wrap">' + "".join(
            f'<span style="display:inline-flex;align-items:center;gap:var(--space-2)"><span aria-hidden="true" style="display:inline-block;width:20px;height:0;border-top:3px {"dashed" if i else "solid"} var(--chart-{i + 1})"></span>{nm}</span>'
            for i, (nm, _) in enumerate(series)) + "</p>"
    head_cells = "".join(f'<th scope="col">{nm}</th>' for nm, _ in series)
    rows = "".join(
        f'<tr><th scope="row" class="numeric">{labels[i]}</th>' + "".join(f'<td class="numeric">{vals[i]:g}{unit}</td>' for _, vals in series) + "</tr>"
        for i in range(0, n, step))
    tone = spec.get("tone")
    tone_html = f' <span class="chip" data-tone="{tone[0]}">{tone[1]}</span>' if tone else ""
    return f"""<section class="panel" aria-labelledby="{cid}-h">
  <div class="panel__head"><h3 id="{cid}-h">{title}</h3><span class="numeric">{now}{tone_html}</span></div>
  <svg viewBox="0 0 {w} {h}" role="img" aria-labelledby="{cid}-h {cid}-d" style="display:block;width:100%;height:auto">{"".join(grid)}{"".join(lines)}</svg>
  <p class="visually-hidden" id="{cid}-d">{spec["desc"]}</p>
  {legend}
  <details class="disclosure"><summary>Show as a table</summary><div class="disclosure__body"><div class="table-wrap"><table class="table"><caption class="visually-hidden">{title}</caption><thead><tr><th scope="col">Time</th>{head_cells}</tr></thead><tbody>{rows}</tbody></table></div></div></details>
</section>"""


def expand(text):
    text = re.sub(r"<!--include:([\w-]+)-->", lambda m: expand((here / f"_{m.group(1)}.html").read_text()), text)
    text = re.sub(r"<!--chart (\{.*?\})-->", lambda m: chart(json.loads(m.group(1))), text, flags=re.S)
    return text


def parts(src):
    meta = json.loads(re.search(r"<!--meta (\{.*?\})-->", src, re.S).group(1))
    out = {}
    for name in ("note", "page", "phone", "panels"):
        m = re.search(rf"<!--{name}-->(.*?)(?=<!--(?:note|page|phone|panels)-->|\Z)", src, re.S)
        out[name] = expand(m.group(1).strip()) if m else ""
    return meta, out


def board(slug, src):
    meta, p = parts(src)
    main, sub = meta.get("main", ""), meta.get("sub", "")
    auth = meta.get("auth", False)
    head = auth_header() if auth else header(main, sub)
    phone_head = "" if auth else phone_header(main, sub)
    footer = "" if auth else '<footer class="site-footer"><span>Starboard v0.2.0</span><a href="starboard-settings-about.html">About and updates</a></footer>'
    phone = ""
    if p["phone"]:
        phone = f"""<section aria-labelledby="board-phone-h" style="display:grid;gap:var(--space-4);padding:var(--space-8);border-top:2px solid var(--color-text);background:var(--color-surface-sunken)">
  <div style="display:grid;gap:var(--space-1)"><h2 id="board-phone-h">On a phone (390px)</h2><p class="small muted">{meta.get("phone_note", "The part of the page whose layout changes on phones.")}</p></div>
  <div style="width:390px;border:1px solid var(--color-border);background:var(--color-bg);overflow:hidden">
      {phone_head}
      <div style="display:grid;gap:var(--space-4);padding:var(--space-4)">
{p["phone"]}
      </div>
  </div>
</section>"""
    pm = "" if auth else phone_menu(main, sub)
    return f"""<!doctype html>
<html lang="en-GB" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta["title"]} · Starboard board</title>
<link rel="stylesheet" href="../tokens.css">
<link rel="stylesheet" href="../components.css">
<style>
  /* Board only, as in the gallery: icon sizes (no icon size class in the library yet). */
  svg.i {{ width: var(--icon-md); height: var(--icon-md); }}
  svg.i-lg {{ width: var(--icon-lg); height: var(--icon-lg); }}
  svg.i-xl {{ width: 32px; height: 32px; }}
</style>
</head>
<body>
<!--ICONS-->
<a class="skip-link" href="#main">Skip to main content</a>
<aside aria-label="About this board" style="padding:var(--space-4) var(--space-8);background:var(--color-surface-sunken);border-bottom:1px solid var(--color-divider)">
  <div class="notice" style="max-width:1100px">{{{{i:info}}}}<div class="notice__body"><span class="notice__title">What changed and why</span>
{p["note"]}
  </div><a class="btn btn--compact" href="index-starboard.html">All boards</a></div>
</aside>
{head}
<main id="main" tabindex="-1">
<div class="page"{' style="max-width:520px"' if auth else ""}>
{p["page"]}
</div>
</main>
{footer}
{phone}
{pm}
{p["panels"]}
{DISPLAY}
<script src="../components.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    for f in sorted(here.glob("*.frag.html")):
        slug = f.name.replace(".frag.html", "")
        (areas / f"starboard-{slug}.src.html").write_text(board(slug, f.read_text()))
        print("wrote", f"starboard-{slug}.src.html")
