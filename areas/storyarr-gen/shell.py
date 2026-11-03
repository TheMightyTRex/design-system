"""Shared shell for the Storyarr area boards: rail, header rows, phone menu, Display dialog, helpers.

Each board module calls page(...) which writes areas/storyarr-<slug>.src.html. Run
`python3 areas/storyarr-gen/make.py` to write every board, then tools/build.py to expand icons.
Icons are written as {{i:name}}; ic() returns that token so it can sit inside f-strings.
"""
import pathlib

AREAS = pathlib.Path(__file__).resolve().parent.parent


def ic(name, size="i"):
    return "{{" + size + ":" + name + "}}"


def logo(px=32):
    # Storyarr's own mark (apps/web/public/assets/storyarr.svg): an open book with three sound bars.
    return (
        f'<svg viewBox="0 0 64 64" width="{px}" height="{px}" aria-hidden="true" focusable="false">'
        '<rect width="64" height="64" fill="#c2552c"/>'
        '<path d="M8 26c8-3 16-3 23 1v26c-7-4-15-4-23-1z" fill="#fff"/>'
        '<path d="M56 26c-8-3-16-3-23 1v26c7-4 15-4 23-1z" fill="#fff"/>'
        '<rect x="25" y="13" width="4" height="10" fill="#fff"/><rect x="30" y="7" width="4" height="16" fill="#fff"/>'
        '<rect x="35" y="11" width="4" height="12" fill="#fff"/></svg>'
    )


# Main menu (rail).
RAIL = [
    ("library", "Library", "book-open", "storyarr-my-library.html"),
    ("discover", "Discover", "compass", "storyarr-discover.html"),
    ("activity", "Activity", "activity", "storyarr-activity.html"),
    ("settings", "Settings", "settings", "storyarr-settings-general.html"),
]

# 1st level per main menu item: (id, name, icon, href, count, count meaning).
FIRST = {
    "library": [
        ("my-library", "My library", "book-open", "storyarr-my-library.html", None, None),
        ("following", "Following", "bookmark", "storyarr-following.html", None, None),
        ("review", "Library review", "list-checks", "storyarr-library-review.html", "12", " to review"),
    ],
    "discover": [
        ("for-you", "For you", "sparkles", "storyarr-discover.html", None, None),
        ("series", "Your series", "library", "storyarr-discover.html", None, None),
        ("browse", "Browse", "layout-grid", "storyarr-discover.html#browse", None, None),
        ("calendar", "Calendar", "calendar-days", "storyarr-calendar.html", None, None),
        ("collections", "Collections", "layers", "storyarr-discover.html", None, None),
        ("awards", "Awards", "award", "storyarr-discover.html", None, None),
        ("yours", "Your lists", "list", "storyarr-discover.html", None, None),
    ],
    "activity": [
        ("queue", "Queue", "list-ordered", "storyarr-activity.html", "4", " in progress"),
        ("wanted", "Wanted", "clock", "storyarr-activity.html#wanted", "9", " wanted"),
        ("history", "History", "history", "storyarr-activity.html#history", None, None),
    ],
    "settings": [
        ("general", "General", "sliders-horizontal", "storyarr-settings-general.html", None, None),
        ("accounts", "Accounts", "user-round", "storyarr-settings-accounts.html", None, None),
        ("sources", "Sources", "book-marked", "storyarr-settings-sources.html", None, None),
        ("library", "Library", "library", "storyarr-settings-library.html", None, None),
        ("downloads", "Downloads", "download", "storyarr-settings-downloads.html", None, None),
        ("system", "System", "scroll-text", "storyarr-settings-system.html", None, None),
    ],
}
SECTION_NAME = {"library": "Library", "discover": "Discover", "activity": "Activity", "settings": "Settings"}


def menu_tabs(items, current, label, compact=False):
    """items: (id, name, icon, href[, count, meaning])"""
    out = [f'<nav class="menu-tabs{" is-compact" if compact else ""}" aria-label="{label}">']
    for it in items:
        iid, name, icon, href = it[:4]
        count = it[4] if len(it) > 4 else None
        meaning = it[5] if len(it) > 5 else ""
        cur = ' aria-current="page"' if iid == current else ""
        c = f' <span class="count">{count}<span class="visually-hidden">{meaning}</span></span>' if count else ""
        out.append(f'<a href="{href}"{cur}>{ic(icon)}<span class="menu-tabs__label">{name}</span>{c}</a>')
    out.append("</nav>")
    return "".join(out)


def rail(current):
    links = []
    for rid, name, icon, href in RAIL:
        cur = ' aria-current="page"' if rid == current else ""
        extra = ""
        if rid == "library":
            extra = '<span class="count" style="position:absolute;top:4px;right:8px">12<span class="visually-hidden"> library items to review</span></span>'
        links.append(f'<a href="{href}"{cur}>{ic(icon, "i-lg")}{name}{extra}</a>')
    return (
        '<nav class="rail" aria-label="Main menu">'
        f'<div class="rail__logo"><a href="storyarr-my-library.html" aria-label="Storyarr, My library" style="min-height:0;padding:0">{logo(36)}</a></div>'
        + "".join(links)
        + '<div class="rail__end"><span class="avatar" aria-hidden="true">A</span><span class="visually-hidden">Signed in as Alex</span>'
        f'<button class="icon-btn icon-btn--bare" type="button" aria-label="Sign out">{ic("log-out")}</button>'
        '<button class="btn btn--quiet btn--compact" type="button" data-opens="panel-release-notes" style="font-size:var(--text-xs);padding:0 4px">v1.10.0</button></div>'
        "</nav>"
    )


def phone_menu(section, current):
    parts = []
    for rid, name, icon, href in RAIL:
        items = FIRST[rid]
        is_cur = rid == section
        lis = "".join(
            f'<li><a href="{it[3]}"{" aria-current=\"page\"" if (is_cur and it[0] == current) else ""}>{ic(it[2])}{it[1]}</a></li>'
            for it in items
        )
        parts.append(
            f'<div class="phone-menu__section"{" data-current" if is_cur else ""}>'
            f'<button type="button" aria-expanded="{"true" if is_cur else "false"}" aria-controls="pm-{rid}">{ic(icon, "i-lg")}{name}{ic("chevron-right phone-menu__chevron")}</button>'
            f'<ul id="pm-{rid}"{"" if is_cur else " hidden"}>{lis}</ul></div>'
        )
    return (
        '<div class="side-panel-layer" id="phone-menu" hidden><div class="side-panel-backdrop"></div>'
        '<nav class="phone-menu" aria-label="Main menu">'
        f'<div class="panel-header"><span class="panel-header__brand">{logo(24)}Storyarr</span>'
        f'<button class="icon-btn" type="button" data-closes aria-label="Close menu">{ic("x")}</button></div>'
        '<form class="phone-menu__search" role="search" onsubmit="return false"><input class="input" type="search" aria-label="Search books, authors or narrators" placeholder="Search books, authors or narrators"></form>'
        f'<div class="phone-menu__sections">{"".join(parts)}</div>'
        f'<div class="phone-menu__foot"><span style="display:flex;gap:8px;align-items:center"><span class="avatar" aria-hidden="true">A</span><span>Alex<br><span class="small muted">Administrator</span></span></span><button class="btn" type="button">{ic("log-out")}Sign out</button></div>'
        "</nav></div>"
    )


DISPLAY_DIALOG = f"""
<dialog class="dialog" id="display-dialog" aria-labelledby="display-h">
  <div class="panel-header"><h2 class="panel-header__title" id="display-h">Display and accessibility</h2><button class="icon-btn" type="button" data-closes aria-label="Close Display and accessibility">{ic("x")}</button></div>
  <div class="dialog__body">
    <p class="small muted">Saved in this browser. Changes apply at once.</p>
    <fieldset><legend class="field__label">Theme</legend><div class="segmented"><label><input type="radio" name="d-theme" value="light" data-display="theme" checked><span>Light</span></label><label><input type="radio" name="d-theme" value="dark" data-display="theme"><span>Dark</span></label></div></fieldset>
    <fieldset><legend class="field__label">Text size</legend><div class="segmented"><label><input type="radio" name="d-text" value="100" data-display="text" checked><span>100%</span></label><label><input type="radio" name="d-text" value="125" data-display="text"><span>125%</span></label><label><input type="radio" name="d-text" value="150" data-display="text"><span>150%</span></label><label><input type="radio" name="d-text" value="175" data-display="text"><span>175%</span></label></div></fieldset>
    <div>
      <label class="switch"><span>High contrast</span><input type="checkbox" role="switch" data-display="contrast"></label>
      <label class="switch"><span>Reduce motion</span><input type="checkbox" role="switch" data-display="motion"></label>
      <label class="switch"><span>Underline links</span><input type="checkbox" role="switch" data-display="underline"></label>
      <label class="switch"><span>Wider text spacing</span><input type="checkbox" role="switch" data-display="spacing"></label>
    </div>
  </div>
  <div class="dialog__foot"><button class="btn btn--primary" type="button" data-closes>Done</button><button class="btn btn--quiet" type="button">Reset to defaults</button></div>
</dialog>"""

RELEASE_PANEL = None  # filled below (needs panel())


def panel(pid, title, body, foot="", wide=False, head_extra=""):
    return (
        f'<div class="side-panel-layer" id="{pid}" hidden><div class="side-panel-backdrop"></div>'
        f'<aside class="side-panel{" side-panel--wide" if wide else ""}" role="dialog" aria-modal="true" aria-labelledby="{pid}-h">'
        f'<div class="panel-header"><h2 class="panel-header__title" id="{pid}-h">{title}</h2>'
        f'<span style="display:flex;gap:4px">{head_extra}<button class="icon-btn" type="button" data-closes aria-label="Close {strip_tags(title)}">{ic("x")}</button></span></div>'
        f'<div class="side-panel__body">{body}</div>'
        + (f'<div class="side-panel__foot">{foot}</div>' if foot else "")
        + "</aside></div>"
    )


def dialog(did, title, body, foot):
    return (
        f'<dialog class="dialog" id="{did}" aria-labelledby="{did}-h">'
        f'<div class="panel-header"><h2 class="panel-header__title" id="{did}-h">{title}</h2><button class="icon-btn" type="button" data-closes aria-label="Close">{ic("x")}</button></div>'
        f'<div class="dialog__body">{body}</div><div class="dialog__foot">{foot}</div></dialog>'
    )


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


RELEASE_PANEL = panel(
    "panel-release-notes",
    "Release notes",
    f"""<p class="small muted">Version 1.10.0, 28 October 2026 · current version</p>
<details class="disclosure" open><summary>Added</summary><div class="disclosure__body"><p><strong>Narrator pages</strong>: open a narrator from any book to find every book they read in your library.</p><p><strong>Slide-outs</strong>: book summaries, requests and connections open beside the list.</p></div></details>
<details class="disclosure"><summary>Changed</summary><div class="disclosure__body"><p><strong>Settings</strong>: every section saves the same way, with a save bar that stays in view.</p></div></details>
<details class="disclosure"><summary>Fixed</summary><div class="disclosure__body"><p><strong>Notifications</strong>: deleting a channel now asks first.</p></div></details>
<details class="disclosure"><summary>Database changes</summary><div class="disclosure__body"><p>Adds a narrator table. A backup is made before the upgrade; restore it from Settings, System, Upgrades.</p></div></details>""",
)

# Covers ---------------------------------------------------------------------------------------
PAL = [
    ("#323a77", "#af4e24"), ("#135c2e", "#154a96"), ("#6b4500", "#9b1c14"), ("#3d1f5c", "#0e6e6e"),
    ("#1d3b53", "#6a8a1f"), ("#5a1e3a", "#c0712a"), ("#20344f", "#7a2f6b"), ("#0f4c45", "#a8781a"),
    ("#4a2f1b", "#2f5f8a"), ("#2b2b52", "#b03a48"), ("#174a2a", "#8a4a1a"), ("#3a3a3a", "#6b5bc2"),
]


def cover(title, n=0, badge=None, width=None, audio=False):
    a, b = PAL[n % len(PAL)]
    w = f"width:{width}px;" if width else ""
    badge_html = f'<span class="cover__badge chip" data-tone="{badge[0]}">{badge[1]}</span>' if badge else ""
    if audio:
        inner = f'<span aria-hidden="true" style="display:grid;place-items:center;width:100%;aspect-ratio:1;background:linear-gradient(160deg,{a},{b});color:#fff;padding:4px">{title}</span>'
        return f'<div class="cover" style="{w}">{inner}{badge_html}</div>'
    return f'<div class="cover" style="{w}background:linear-gradient(160deg,{a},{b});color:#fff;padding:4px"><span aria-hidden="true">{title}</span>{badge_html}</div>'


def thumb(title, n=0, w=48):
    a, b = PAL[n % len(PAL)]
    return f'<div class="cover" aria-hidden="true" style="width:{w}px;background:linear-gradient(160deg,{a},{b})"></div>'


def mcard(title, meta, n=0, opens="panel-book", badge=None, href=None, audio=False):
    target = f'<a href="{href}">{title}</a>' if href else f'<button type="button" data-opens="{opens}">{title}</button>'
    return f'<li class="media-card">{cover(title, n, badge, audio=audio)}<span class="media-card__title">{target}</span><span class="media-card__meta">{meta}</span></li>'


def menu(mid, label, items, button_text=None, icon=None, align_start=False, button_class="btn", aria_label=None):
    """items: list of (text, icon or None, role) or 'hr' or ('label', text)."""
    btn_inner = (ic(icon) if icon else "") + (button_text or "")
    if button_text:
        btn_inner += ic("chevron-down")
    al = f' aria-label="{aria_label}"' if aria_label else ""
    out = [
        f'<div class="menu-wrap"><button class="{button_class}" type="button" aria-haspopup="menu" aria-controls="{mid}"{al}>{btn_inner}</button>',
        f'<div class="menu" id="{mid}" role="menu" aria-label="{label}"{" data-align=\"start\"" if align_start else ""}>',
    ]
    for it in items:
        if it == "hr":
            out.append("<hr>")
        elif it[0] == "label":
            out.append(f'<div class="menu__label">{it[1]}</div>')
        else:
            text, icn, role = (list(it) + [None, "menuitem"])[:3]
            role = role or "menuitem"
            extra = ""
            if role == "menuitemradio" or role == "menuitemcheckbox":
                checked = text.startswith("*")
                text = text.lstrip("*")
                extra = f' aria-checked="{"true" if checked else "false"}"'
            attrs = ""
            if "|" in text:
                text, attrs = text.split("|", 1)
                attrs = " " + attrs
            out.append(f'<button type="button" role="{role}"{extra}{attrs}>{ic(icn) if icn else ""}{text}</button>')
    out.append("</div></div>")
    return "".join(out)


def sort_menu(mid, current, options):
    return menu(mid, "Sort", [("label", "Sort by")] + [(("*" if o == current else "") + o, None, "menuitemradio") for o in options] + ["hr", ("Reverse order", "arrow-up-down")], f"Sort: {current}", "arrow-up-down")


def what_changed(points):
    ps = "".join(f"<p>{p}</p>" for p in points)
    return (
        f'<div class="notice" role="note" data-board>{ic("info")}<div class="notice__body">'
        f'<span class="notice__title">What changed and why</span>{ps}</div></div>'
    )


def phone_section(frames, intro):
    """frames: list of (query, caption, height)."""
    figs = "".join(
        f'<figure style="margin:0;display:grid;gap:8px;align-content:start"><div data-phone="{q}" data-title="Phone preview: {c}" data-height="{h}" style="width:392px;height:{h + 2}px;border:1px solid var(--color-border);background:var(--color-bg)"></div><figcaption class="small muted" style="max-width:390px">{c}</figcaption></figure>'
        for q, c, h in frames
    )
    return (
        '<section data-board aria-labelledby="phone-h" style="display:grid;gap:var(--space-3);padding-top:var(--space-6);border-top:2px solid var(--color-text)">'
        f'<h2 id="phone-h">On a phone (390px wide)</h2><p class="muted">{intro}</p>'
        f'<div style="display:flex;flex-wrap:wrap;gap:var(--space-6)">{figs}</div></section>'
    )


def board_divider(title, note):
    """Marks a part of the board that shows another tab or state of the same page."""
    return (
        f'<div data-board style="padding-top:var(--space-6);border-top:2px solid var(--color-text);display:grid;gap:var(--space-1)">'
        f'<p class="small muted">Board: another tab or state of this page</p><h2>{title}</h2><p class="muted small">{note}</p></div>'
    )


def page(slug, title, section, first_current, body, row2=None, panels="", dialogs="", search_value="", tab_title=None):
    """row2: (aria label, items, current) or None."""
    # Toolbar chips must be able to shrink on phones so they scroll sideways (missing item 3).
    body = body.replace('class="filter-chips" role="group"', 'class="filter-chips" style="max-width:100%;min-width:0" role="group"')
    first = FIRST.get(section, [])
    row1 = menu_tabs(first, first_current, SECTION_NAME.get(section, "Section")) if first else ""
    row2_html = ""
    if row2:
        row2_html = f'<div class="site-header__tabs">{menu_tabs(row2[1], row2[2], row2[0])}</div>'
    sv = f' value="{search_value}"' if search_value else ""
    html = f"""<!doctype html>
<html lang="en-GB" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tab_title or title} · Storyarr</title>
<link rel="stylesheet" href="../tokens.css">
<link rel="stylesheet" href="../components.css">
<style>
  /* Board only. Icon sizes are listed in the README but missing from components.css
     (storyarr-missing-components.md, item 1). */
  svg.i {{ width: var(--icon-md); height: var(--icon-md); }}
  svg.i-lg {{ width: var(--icon-lg); height: var(--icon-lg); }}
  svg.i-xl {{ width: 32px; height: 32px; }}
  /* The library's display rules (.rows, .media-grid, .notice) override the hidden attribute (item 2). */
  [hidden] {{ display: none !important; }}
</style>
</head>
<body>
<!--ICONS-->
<a class="skip-link" href="#main">Skip to main content</a>
{rail(section)}
<div class="with-rail">
<header class="site-header">
  <div class="site-header__bar">
    <span class="phone-menu-button"><button class="icon-btn" type="button" data-opens="phone-menu" aria-controls="phone-menu" aria-expanded="false" aria-label="Menu">{ic("menu", "i-lg")}</button></span>
    <a class="site-header__brand" href="storyarr-my-library.html">{logo(28)}Storyarr</a>
    {row1}
    <form class="site-header__search search-field" role="search" onsubmit="return false"><input class="input" type="search" aria-label="Search books, authors or narrators" placeholder="Search books, authors or narrators"{sv}><button class="visually-hidden">Search</button></form>
    <div class="site-header__actions"><button class="icon-btn" type="button" data-dialog="display-dialog">{ic("sun", "i-lg")}<span class="label">Display</span></button></div>
  </div>
  {row2_html}
</header>
<main class="page" id="main" style="grid-template-columns:minmax(0,1fr)">
{body}
</main>
<footer class="site-footer"><span>Storyarr 1.10.0</span><button class="btn btn--quiet btn--compact" type="button" data-opens="panel-release-notes">Release notes</button><a href="index-storyarr.html" data-board>All Storyarr boards</a></footer>
</div>
{phone_menu(section, first_current)}
{panels}
{RELEASE_PANEL}
{dialogs}
{DISPLAY_DIALOG}
<script src="../components.js"></script>
<script src="storyarr-board.js"></script>
</body>
</html>
"""
    (AREAS / f"storyarr-{slug}.src.html").write_text(html)
    return f"storyarr-{slug}.src.html"
