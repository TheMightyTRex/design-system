from shell import *
from common import BOOKS, book_panel
from b_library import chipbtn, view_switch

REQ_FOOT = (f'<button class="btn btn--primary" type="button">{ic("download")}Request audiobook</button>'
            f'<button class="btn" type="button">{ic("list-plus")}Add to list</button><a class="btn btn--quiet" href="storyarr-book.html">Open book page</a>')


def shelf(sid, title, caption, cards):
    return f"""<section aria-labelledby="{sid}-h" style="display:grid;gap:var(--space-3)">
  <div class="panel__head"><div style="display:grid;gap:2px"><h2 id="{sid}-h">{title}</h2><p class="small muted">{caption}</p></div>
    <div class="actions"><a class="btn btn--quiet" href="#browse">View all<span class="visually-hidden">: {title}</span></a>
    {menu(sid + "-more", "More for " + title, [("Refresh shelf", "refresh-cw"), ("Download list as CSV", "download"), "hr", ("Hide from For you", "eye-off")], icon="ellipsis", button_class="icon-btn", aria_label="More for " + title)}
    <button class="icon-btn" type="button" aria-label="Previous books: {title}">{ic("chevron-left")}</button><button class="icon-btn" type="button" aria-label="Next books: {title}">{ic("chevron-right")}</button></div></div>
  <ul class="media-grid" data-size="small" style="grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:minmax(120px,1fr);overflow-x:auto;padding:4px">{cards}</ul>
</section>"""


def cards(sel, badges):
    return "".join(mcard(BOOKS[i][0], BOOKS[i][1], BOOKS[i][5], opens="panel-dbook", badge=badges[k % len(badges)]) for k, i in enumerate(sel))


def discover():
    nr = ("", "Not released")
    nq = ("muted", "Not requested")
    il = ("success", "In library")
    body = f"""
{what_changed([
    "<strong>A visible h1</strong> (\"For you\") replaces the hidden h1 and the slogan headings such as \"Stories worth celebrating\".",
    "<strong>One shelf header</strong> for every shelf: heading, caption, View all, a More menu (Refresh, Download list, Hide from For you) and 44px arrows. Today there are four header layouts and two kinds of View all.",
    "<strong>Customise Discover opens a slide-out</strong>, so the shelves stay in sight while you reorder them. It works while shelves load, instead of staying greyed out with no reason given.",
    "<strong>Browse and the other views get the section toolbar</strong>: search, chips, menus, sort and an applied row with Clear all. The Lists menu sits at the end of the toolbar, not in a row of its own.",
])}
<div class="page-head"><div class="page-head__text"><h1>For you</h1><p class="page-head__summary">6 shelves · updated today at 08:00</p></div></div>
<div class="toolbar"><div class="toolbar__row">
  <div class="filter-chips" role="group" aria-label="Format">{chipbtn("Audiobooks", "")}{chipbtn("Ebooks", "")}</div>
  <div class="toolbar__end">
    {menu("m-lists", "Lists", [("Add list|data-dialog=\"dlg-add-list\"", "plus"), "hr", ("Refresh all lists", "refresh-cw"), ("Refresh Goodreads lists", None), ("Refresh StoryGraph lists", None)], "Lists", "list")}
    <button class="btn" type="button" data-opens="panel-customise">{ic("sliders-horizontal")}Customise Discover</button>
  </div>
</div></div>
{shelf("s1", "New from authors you follow", "4 books out in the last 30 days", cards([17, 4, 8, 13, 5, 1, 12], [nq, il, nq]))}
{shelf("s2", "Continue your series", "Next books in series you have started", cards([1, 13, 7, 0, 16, 2, 9], [nq, ("", "Wanted"), nq]))}
{shelf("s3", "Coming soon", "Not released yet, from authors and series you follow", cards([10, 3, 6, 11, 14, 15, 2], [nr]))}
{shelf("s4", "From your list: Read next", "Goodreads list · 18 books · 11 in your library", cards([5, 9, 12, 0, 3, 8, 6], [il, nq]))}

{board_divider("Browse view", "Same page, Browse chosen in header row 1. Filters that today exist only in the address show as applied filters, with Clear all.")}
<section id="browse" aria-labelledby="browse-h" style="display:grid;gap:var(--space-4)">
  <div class="page-head"><div class="page-head__text"><h2 id="browse-h" style="font-size:var(--text-xl)">Browse</h2><p class="page-head__summary">Award winners and nominees from Hardcover and Goodreads</p></div></div>
  <div class="toolbar">
    <div class="toolbar__row">
      <div class="toolbar__search"><input class="input" type="search" aria-label="Search Browse" placeholder="Title or author"></div>
      <div class="filter-chips" role="group" aria-label="Show">{chipbtn("Winners", "212", True)}{chipbtn("In library", "38")}</div>
      {menu("m-br-genre", "Genre", [("*Fantasy", None, "menuitemradio"), ("Mystery", None, "menuitemradio"), ("Science fiction", None, "menuitemradio")], "Genre: Fantasy", None, True)}
      {menu("m-br-year", "Award year", [("*Any year", None, "menuitemradio"), ("2026", None, "menuitemradio"), ("2025", None, "menuitemradio")], "Award year", None, True)}
      {menu("m-br-src", "Source", [("*All sources", None, "menuitemradio"), ("Hardcover", None, "menuitemradio"), ("Goodreads", None, "menuitemradio")], "Source", None, True)}
      <div class="toolbar__end">{sort_menu("m-br-sort", "Relevance", ["Relevance", "Newest", "Title"])}</div>
    </div>
    <div class="applied"><span class="muted">Filtered by</span><span class="applied__item">Genre: Fantasy<button type="button" aria-label="Remove filter: Genre Fantasy">{ic("x")}</button></span><span class="applied__item">Winners<button type="button" aria-label="Remove filter: Winners">{ic("x")}</button></span><button class="btn btn--quiet btn--compact" type="button">Clear all</button><span class="muted" style="margin-left:auto">Showing 212 of 1,203</span></div>
  </div>
  <ul class="media-grid" data-size="small">{cards([7, 8, 13, 0, 5, 11, 2, 16], [nq, il])}</ul>
  <div class="load-more"><span>Showing 8 of 212 books</span><button class="btn" type="button">Show 40 more</button></div>
</section>
{phone_section([("phone=1", "Shelves keep their arrows; the header names stay, View all and More wrap under the heading.", 760),
                ("phone=1&open=panel-customise", "Customise Discover fills the width; Save and Cancel stay in the footer.", 760)],
               "On phones Discover views move into the menu drawer, under Discover.")}
"""
    shelves = [("New from authors you follow", True), ("Continue your series", True), ("Coming soon", True), ("From your list: Read next", True),
               ("Popular on Hardcover this week", False), ("Recently added to your library", False)]
    rows = "".join(
        f'<li class="row row--no-lead"><label class="check"><input type="checkbox"{" checked" if on else ""}><span class="check__text">{t}</span></label>'
        f'<div class="row__side"><button class="icon-btn icon-btn--bare" type="button" aria-label="Move {t} up"{" disabled" if k == 0 else ""}>{ic("arrow-up")}</button>'
        f'<button class="icon-btn icon-btn--bare" type="button" aria-label="Move {t} down"{" disabled" if k == len(shelves) - 1 else ""}>{ic("arrow-down")}</button></div></li>'
        for k, (t, on) in enumerate(shelves))
    panels = book_panel("panel-dbook", "The Tidewright", 2, ("muted", "Not requested"), foot=REQ_FOOT, series="The Glass Harbour, book 3") + panel(
        "panel-customise", "Customise Discover", f"""<p>Choose the shelves on For you and their order. Changes show behind this panel when you save.</p>
<ul class="rows" aria-label="Shelves">{rows}</ul>
<fieldset><legend class="field__label">Books per shelf</legend><div class="segmented"><label><input type="radio" name="cu-n"><span>10</span></label><label><input type="radio" name="cu-n" checked><span>20</span></label><label><input type="radio" name="cu-n"><span>40</span></label></div></fieldset>
<label class="check"><input type="checkbox" checked><span class="check__text">Hide books already in my library</span></label>""",
        '<button class="btn btn--primary" type="button">Save Discover</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button><button class="btn btn--quiet" type="button" style="margin-left:auto">Reset to defaults</button>')
    dialogs = dialog("dlg-add-list", "Add list", '<div class="field"><label for="al-url">List address</label><span class="hint" id="al-urlh">A Goodreads, StoryGraph or Hardcover list.</span><input class="input" id="al-url" aria-describedby="al-urlh"></div>',
                     '<button class="btn btn--primary" type="button" data-closes>Add list</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    return page("discover", "For you", "discover", "for-you", body, None, panels, dialogs, tab_title="Discover")


def calendar():
    rel = {3: [(0, "The Tidewright", "Mara Ellison"), (5, "A Small Weather", "Priya Castellane")], 5: [(4, "Night Ferry", "Theo Marchetti")],
           10: [(8, "Ember and Ash Road", "Rowan Ashby"), (7, "Bright Fathoms", "Ines Valdré"), (9, "Paper Kingdoms", "Lena Ostrova")],
           12: [(3, "The Orchard Clock", "Hollis Brant")], 17: [(6, "Moth Season", "Lena Ostrova"), (2, "Salt Roads", "Jonah Okafor")],
           19: [(11, "The Quiet Engine", "Dara Whitlock")], 24: [(1, "Lanterns Under Ice", "Mara Ellison"), (10, "Hollow Pines", "Hollis Brant"), (5, "Starling House Rules", "Felix Amari"), (8, "The Long Recess", "Dara Whitlock")],
           26: [(9, "What the River Kept", "Priya Castellane")]}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # November 2026 starts on a Sunday. Weeks run Monday to Sunday.
    cells = [(26 + i, False) for i in range(6)] + [(d, True) for d in range(1, 31)] + [(d, False) for d in range(1, 7)]
    trs = []
    for w in range(6):
        tds = []
        for k in range(7):
            d, inm = cells[w * 7 + k]
            content = f'<span class="numeric"{"" if inm else " style=\"color:var(--color-text-muted)\""}>{d}</span>'
            if inm and d == 2:
                content += ' <span class="chip" data-tone="info">Today</span>'
            if inm and d in rel:
                n = len(rel[d])
                first = rel[d][0][1]
                content += (f'<div class="small" style="margin-top:4px">{first}{f" and {n - 1} more" if n > 1 else ""}</div>'
                            f'<button class="btn btn--compact" type="button" data-opens="panel-day" style="margin-top:4px">{n} release{"s" if n > 1 else ""}<span class="visually-hidden"> on {days[k]} {d} November</span></button>')
            tds.append(f'<td data-label="{days[k]}" style="height:112px;width:14.28%">{content}</td>')
        trs.append(f'<tr>{"".join(tds)}</tr>')
    month = (f'<div class="table-wrap" data-view="month"><table class="table"><caption class="visually-hidden">Releases in November 2026</caption>'
             f'<thead><tr>{"".join(f"<th scope=\"col\">{d}</th>" for d in days)}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>')
    agenda = []
    for d in sorted(rel):
        k = (d + 5) % 7  # 1 Nov = Sunday (index 6)
        items = "".join(f'<li class="row row--opens">{thumb(t, n)}<div><div class="row__title"><button type="button" data-opens="panel-day">{t}</button></div><div class="row__meta">{a}</div></div><div class="row__side"><span class="chip">Not released</span></div></li>' for n, t, a in rel[d])
        agenda.append(f'<h2 class="group-heading">{days[k]} {d} November</h2><ul class="rows">{items}</ul>')
    body = f"""
{what_changed([
    "<strong>Day details use the shared slide-out</strong>: a backdrop, focus kept inside, Escape to close, and a width that no longer depends on the rail.",
    "<strong>The month is a real table</strong> with weekday column headings, so screen readers hear the week structure; each day's button names its date.",
    "<strong>One toolbar</strong>: view switch (Month, List), Genres and Show menus that look and save the same way, and the month controls at the end instead of in the heading area.",
    "<strong>List view</strong> is the default on phones, instead of a grid of bare counts.",
])}
<div class="page-head"><div class="page-head__text"><h1>Calendar</h1><p class="page-head__summary">November 2026 · 15 releases from authors and series you follow</p></div></div>
<div class="toolbar"><div class="toolbar__row">
  {view_switch("cal-view", [("month", "Month", "calendar-days"), ("list", "List", "list")], "month")}
  {menu("m-cal-genre", "Genres", [("*Fantasy", None, "menuitemcheckbox"), ("*Mystery", None, "menuitemcheckbox"), ("Romance", None, "menuitemcheckbox"), ("Science fiction", None, "menuitemcheckbox")], "Genres: 2", "tags", True)}
  {menu("m-cal-show", "Show", [("*Authors I follow", None, "menuitemcheckbox"), ("*Series I follow", None, "menuitemcheckbox"), ("Wanted books", None, "menuitemcheckbox"), ("Books in my library", None, "menuitemcheckbox")], "Show: 2", "eye", True)}
  <div class="toolbar__end">
    <button class="icon-btn" type="button" aria-label="Previous month, October 2026">{ic("chevron-left")}</button>
    <strong role="status" style="min-width:9em;text-align:center">November 2026</strong>
    <button class="icon-btn" type="button" aria-label="Next month, December 2026">{ic("chevron-right")}</button>
    <button class="btn" type="button">Today</button>
  </div>
</div></div>
{month}
<div data-view="list" hidden>{"".join(agenda)}</div>
<div class="notice">{ic("info")}<div class="notice__body"><p>4 books are due this month without a release day. <a href="#">Show books without a release day</a></p></div></div>
{phone_section([("phone=1&view=list", "List view on phones: one heading per day, rows with covers. Month view stays available in the view switch.", 760),
                ("phone=1&view=list&open=panel-day", "Day details fill the width.", 760)], "The month grid becomes a list on phones.")}
"""
    items = "".join(f'<li class="row row--opens">{thumb(t, n)}<div><div class="row__title"><a href="storyarr-book.html">{t}</a></div><div class="row__meta">{a} · audiobook and ebook</div></div><div class="row__side"><span class="chip">Not released · 3 Nov</span><button class="btn btn--compact" type="button">Request<span class="visually-hidden"> {t}</span></button></div></li>' for n, t, a in rel[3])
    panels = panel("panel-day", "Tuesday 3 November 2026", f"""<p class="small muted">2 releases · from authors you follow</p><ul class="rows">{items}</ul>
<p class="small muted">Requested books are searched for on release day at 00:05.</p>""")
    return page("calendar", "Calendar", "discover", "calendar", body, None, panels)


def search():
    nq = ("muted", "Not requested")
    il = ("success", "In library")
    body = f"""
{what_changed([
    "<strong>One search box</strong>: the header search. The second search form, the provider select and the page eyebrow \"FIND YOUR NEXT BOOK\" are gone.",
    "<strong>Where to search is a toolbar menu</strong> (Everywhere, In your catalogue, Hardcover, Open Library, Audiobook recordings), next to Books, Authors and Series chips with counts.",
    "<strong>Authors and series are searchable</strong>, so Following's \"Follow an author\" and this page find the same people.",
    "<strong>One result card</strong> with a status chip; selecting a result opens the Summary slide-out with Request and Open book page, instead of navigating away.",
])}
<div class="page-head"><div class="page-head__text"><h1>Search results</h1><p class="page-head__summary">Results for "glass harbour" · 24 books, 2 authors, 1 series</p></div></div>
<div class="toolbar"><div class="toolbar__row">
  {view_switch("s-view", [("covers", "Covers", "layout-grid"), ("list", "List", "list")], "covers")}
  <div class="filter-chips" role="group" aria-label="Show">{chipbtn("Books", "24")}{chipbtn("Authors", "2")}{chipbtn("Series", "1")}</div>
  {menu("m-s-where", "Where to search", [("*Everywhere", None, "menuitemradio"), ("In your catalogue", None, "menuitemradio"), ("Hardcover", None, "menuitemradio"), ("Open Library", None, "menuitemradio"), ("Audiobook recordings", None, "menuitemradio")], "Where: Everywhere", "globe", True)}
  <div class="toolbar__end"><span class="toolbar__count">27 results</span>{sort_menu("m-s-sort", "Relevance", ["Relevance", "Newest", "Title"])}</div>
</div></div>
<section aria-labelledby="sa-h" style="display:grid;gap:var(--space-2)"><h2 id="sa-h" class="group-heading">Authors and series</h2>
<ul class="rows">
  <li class="row row--opens"><span class="avatar" aria-hidden="true">ME</span><div><div class="row__title"><a href="storyarr-author.html">Mara Ellison</a></div><div class="row__meta">Author · 6 books · 3 in your library</div></div><div class="row__side"><span class="chip" data-tone="success">Following</span></div></li>
  <li class="row row--opens">{thumb("x", 0, 40)}<div><div class="row__title"><a href="storyarr-series.html">The Glass Harbour</a></div><div class="row__meta">Series by Mara Ellison · 4 books · 2 in your library</div></div><div class="row__side"><button class="btn btn--compact" type="button">{ic("bookmark")}Follow series</button></div></li>
  <li class="row row--opens"><span class="avatar" aria-hidden="true">GH</span><div><div class="row__title"><a href="storyarr-author.html">Greta Harbour</a></div><div class="row__meta">Author · 2 books</div></div><div class="row__side"><button class="btn btn--compact" type="button">{ic("bookmark")}Follow<span class="visually-hidden"> Greta Harbour</span></button></div></li>
</ul></section>
<section aria-labelledby="sb-h" style="display:grid;gap:var(--space-3)"><h2 id="sb-h" class="group-heading">Books</h2>
<ul class="media-grid" data-size="small">
  {mcard("The Glass Harbour", "Mara Ellison · 2024", 0, opens="panel-sbook", badge=il)}
  {mcard("Lanterns Under Ice", "Mara Ellison · 2025", 1, opens="panel-sbook", badge=il)}
  {mcard("The Tidewright", "Mara Ellison · 2026", 2, opens="panel-sbook", badge=("", "Wanted"))}
  {mcard("Harbour of Glass", "Ilse Brandt · 2019", 7, opens="panel-sbook", badge=nq)}
  {mcard("Glass Harbours", "Ira Penn · 2011", 6, opens="panel-sbook", badge=nq)}
  {mcard("The Harbour Glassmaker", "Noor Haddad · 2022", 9, opens="panel-sbook", badge=nq)}
  {mcard("The Lamp Room", "Mara Ellison · 2027", 11, opens="panel-sbook", badge=("", "Not released"))}
</ul>
<div class="load-more"><span>Showing 7 of 24 books</span><button class="btn" type="button">Show 20 more</button></div></section>
{phone_section([("phone=1", "On phones search lives in the menu drawer; the results page keeps the query in its summary line and the toolbar stacks.", 760),
                ("phone=1&open=panel-sbook", "A result opens the Summary slide-out with Request.", 760)], "The header search moves into the drawer on phones.")}
"""
    panels = book_panel("panel-sbook", "Harbour of Glass", 7, nq, foot=REQ_FOOT, author="Ilse Brandt", series=None, narrator="Clara Penhallow",
                        blurb="A glassblower's apprentice finds a letter sealed inside a float. Found on Hardcover; not in your catalogue yet.")
    return page("search", "Search results", "discover", None, body, None, panels, search_value="glass harbour")


def build():
    return [discover(), calendar(), search()]
