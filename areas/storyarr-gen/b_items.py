from shell import *
from common import BOOKS, book_panel
from b_library import chipbtn


def back(text="Back to My library", href="storyarr-my-library.html"):
    return f'<a class="btn btn--quiet" href="{href}" style="justify-self:start;margin-left:calc(-1 * var(--space-4))">{ic("arrow-left")}{text}</a>'


def item_header(art, h1, byline, chips, facts, actions, extra=""):
    return f"""<div style="display:flex;flex-wrap:wrap;gap:var(--space-6);align-items:flex-start">
  <div style="flex:none;width:176px">{art}</div>
  <div style="flex:1 1 360px;min-width:0;display:grid;gap:var(--space-3)">
    <div style="display:grid;gap:var(--space-1)"><h1>{h1}</h1><p class="muted">{byline}</p></div>
    <div class="actions">{chips}</div>
    {extra}
    <dl class="facts">{facts}</dl>
    <div class="actions">{actions}</div>
  </div>
</div>"""


def more_menu(mid, name, items):
    return menu(mid, f"More actions for {name}", items, icon="ellipsis", button_class="icon-btn", aria_label=f"More actions for {name}")


def tabs(label, items, current):
    return (label, items, current)


def book():
    t = "The Glass Harbour"
    facts = ('<dt>Author</dt><dd><a href="storyarr-author.html">Mara Ellison</a></dd>'
             '<dt>Series</dt><dd><a href="storyarr-series.html">The Glass Harbour, book 1</a></dd>'
             '<dt>Narrated by</dt><dd><a href="storyarr-narrator.html">Sam Oduya</a></dd>'
             '<dt>Published</dt><dd>21 September 2024 · Tidewater Press</dd>'
             '<dt>Length</dt><dd>11 hr 42 min · 412 pages</dd>')
    actions = (f'<button class="btn btn--primary" type="button" data-opens="panel-request-edition">{ic("download")}Request ebook</button>'
               f'<button class="btn" type="button" data-dialog="dlg-add-list">{ic("list-plus")}Add to list</button>'
               + more_menu("m-book-more", t, [("Follow Mara Ellison", "bookmark"), ("Open in Hardcover (opens in a new tab)", "external-link"), ("Open in Goodreads (opens in a new tab)", "external-link"), "hr", ("Delete book|data-dialog=\"dlg-delete-book\"", "trash-2")]))
    header = item_header(cover(t, 0), t, 'by <a href="storyarr-author.html">Mara Ellison</a> · read by <a href="storyarr-narrator.html">Sam Oduya</a>',
                         '<span class="chip" data-tone="success">In library · Audiobook</span><span class="chip" data-tone="muted">Not requested · Ebook</span>', facts, actions)
    sources_rows = [
        ("The.Glass.Harbour.Mara.Ellison.2024.EPUB", "MyAnonamouse", "2.1 MB", "Ebook · EPUB", "1 day", "96", None),
        ("Mara Ellison - The Glass Harbour (retail)", "Prowlarr: Bookshelf", "1.8 MB", "Ebook · AZW3", "4 days", "81", None),
        ("glass_harbour_ellison_epub_v2", "AudioBook Bay", "3.0 MB", "Ebook · EPUB", "2 weeks", "40", ("danger", "Blocked")),
    ]
    srows = "".join(
        f'<tr><td data-label="Release"><button class="btn btn--quiet btn--compact" type="button" data-opens="panel-release" style="padding:0;white-space:normal;text-align:left">{n}</button></td>'
        f'<td data-label="Source">{s}</td><td data-label="Size" class="numeric">{z}</td><td data-label="Format">{f}</td><td data-label="Age">{a}</td><td data-label="Score" class="numeric">{sc}</td>'
        f'<td data-label="Status">{f"<span class=\"chip\" data-tone=\"{ch[0]}\">{ch[1]}</span>" if ch else "<span class=\"chip\">Ready</span>"}</td></tr>'
        for n, s, z, f, a, sc, ch in sources_rows)
    body = f"""
{what_changed([
    "<strong>Two main actions</strong> (Request ebook, Add to list) and one More menu for the rest, instead of up to eight buttons with Delete beside the primary.",
    "<strong>The tabs move to header row 2</strong> with icons: Overview, Editions and files, Sources, History, plus a visible Details and matching tab for administrators (today a hidden eighth tab behind a gear). Authors and Reviews fold into Overview.",
    "<strong>Slide-outs replace modals</strong> for a library copy, requesting an edition, release details (its tabs become sections) and matching, so you can compare rows. Delete, Download anyway and Add to list stay dialogs.",
    "<strong>One filter bar on Sources</strong> (the section toolbar) instead of two stacked bars and a coverage block. No capitals in the eyebrow; facts list Author first, then Series and Narrated by.",
])}
{back()}
{header}
<section aria-labelledby="ov-h" style="display:grid;gap:var(--space-4);max-width:880px">
  <h2 id="ov-h" class="visually-hidden">Overview</h2>
  <p>A harbour town keeps its secrets in glass. When the lighthouse keeper vanishes, his niece finds the lamp still lit and a map that should not exist. The first book in The Glass Harbour series.</p>
  <div class="actions"><span class="tag">Fantasy</span><span class="tag">Mystery</span><span class="tag">Coastal</span></div>
  <div class="stats"><div class="stat"><span class="stat__value">4.2</span><span class="stat__label">Average of 1,208 ratings on Hardcover</span></div><div class="stat"><span class="stat__value">2</span><span class="stat__label">Copies in your libraries</span></div><div class="stat"><span class="stat__value">3</span><span class="stat__label">Editions known</span></div></div>
  <section class="panel" aria-labelledby="ov-author-h"><div class="panel__head"><h3 id="ov-author-h">About Mara Ellison</h3><a href="storyarr-author.html">Open author page</a></div><p>Mara Ellison writes coastal fantasy. 4 books, 3 in your library. You follow her.</p></section>
  <section aria-labelledby="ov-rev-h" style="display:grid;gap:var(--space-3)"><h3 id="ov-rev-h">Reader reviews</h3>
    <ul class="rows"><li class="row row--no-lead"><div><div class="row__title">Quietly gripping</div><div class="row__meta">5 of 5 · reader on Hardcover · 2 March 2025</div><p class="small">The lighthouse chapters are the best thing I read this year.</p></div><div class="row__side"></div></li>
    <li class="row row--no-lead"><div><div class="row__title">Slow start</div><div class="row__meta">3 of 5 · reader on Hardcover · 18 January 2025</div><details class="disclosure"><summary>Contains spoilers</summary><div class="disclosure__body"><p>The map turns out to be a copy.</p></div></details></div><div class="row__side"></div></li></ul>
  </section>
</section>

{board_divider("Editions and files tab", "Library copies are rows that open a slide-out. One editions table; Request this edition opens a slide-out beside it.")}
<section aria-labelledby="ed-h" style="display:grid;gap:var(--space-4)">
  <h2 id="ed-h" class="visually-hidden">Editions and files</h2>
  <h3>Library copies</h3>
  <ul class="rows">
    <li class="row row--opens">{thumb(t, 0)}<div><div class="row__title"><button type="button" data-opens="panel-copy">Audiobook · M4B · 11 hr 42 min</button></div><div class="row__meta">Fiction audiobooks · Audiobookshelf · added 3 October 2024</div></div><div class="row__side"><span class="chip" data-tone="success">In library</span></div></li>
    <li class="row row--opens">{thumb(t, 0)}<div><div class="row__title"><button type="button" data-opens="panel-copy">Audiobook · MP3 · 11 hr 40 min</button></div><div class="row__meta">Fiction audiobooks · duplicate copy · added 9 July 2025</div></div><div class="row__side"><span class="chip" data-tone="warning">Needs attention</span></div></li>
  </ul>
  <h3>Editions</h3>
  <div class="table-wrap" data-stack><table class="table">
    <thead><tr><th scope="col">Format</th><th scope="col">Narrator or publisher</th><th scope="col">Length</th><th scope="col">Published</th><th scope="col">Status</th><th scope="col"><span class="visually-hidden">Actions</span></th></tr></thead>
    <tbody>
      <tr><td data-label="Format">Audiobook</td><td data-label="Narrator"><a href="storyarr-narrator.html">Sam Oduya</a></td><td data-label="Length">11 hr 42 min</td><td data-label="Published">21 Sept 2024</td><td data-label="Status"><span class="chip" data-tone="success">In library</span></td><td></td></tr>
      <tr><td data-label="Format">Audiobook</td><td data-label="Narrator">Full cast</td><td data-label="Length">12 hr 5 min</td><td data-label="Published">2 Feb 2026</td><td data-label="Status"><span class="chip" data-tone="muted">Not requested</span></td><td><button class="btn btn--compact" type="button" data-opens="panel-request-edition">Request this edition<span class="visually-hidden">: full cast audiobook</span></button></td></tr>
      <tr><td data-label="Format">Ebook</td><td data-label="Publisher">Tidewater Press</td><td data-label="Length">412 pages</td><td data-label="Published">21 Sept 2024</td><td data-label="Status"><span class="chip" data-tone="muted">Not requested</span></td><td><button class="btn btn--compact" type="button" data-opens="panel-request-edition">Request this edition<span class="visually-hidden">: Tidewater Press ebook</span></button></td></tr>
    </tbody></table></div>
</section>

{board_divider("Sources tab", "One section toolbar, then the releases table. A release opens its details in a slide-out, so you can compare two releases one after the other without losing the table.")}
<section aria-labelledby="src-h" style="display:grid;gap:var(--space-4)">
  <h2 id="src-h" class="visually-hidden">Sources</h2>
  <div class="toolbar"><div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search releases" placeholder="Release name"></div>
    <div class="filter-chips" role="group" aria-label="Format">{chipbtn("Audiobooks", "6")}{chipbtn("Ebooks", "3", True)}</div>
    {menu("m-src-source", "Source", [("*All sources", None, "menuitemradio"), ("MyAnonamouse", None, "menuitemradio"), ("Prowlarr", None, "menuitemradio"), ("AudioBook Bay", None, "menuitemradio")], "Source: All", "radar", True)}
    <div class="toolbar__end"><span class="toolbar__count">3 releases · searched 4 sources 2 minutes ago</span>{sort_menu("m-src-sort", "Score", ["Score", "Size", "Age"])}<button class="btn" type="button">{ic("refresh-cw")}Search again</button></div>
  </div></div>
  <div class="table-wrap" data-stack><table class="table">
    <thead><tr><th scope="col">Release</th><th scope="col">Source</th><th scope="col">Size</th><th scope="col">Format</th><th scope="col">Age</th><th scope="col" aria-sort="descending"><button type="button">Score{ic("arrow-up-down")}</button></th><th scope="col">Status</th></tr></thead>
    <tbody>{srows}</tbody></table></div>
</section>

{board_divider("History tab", "What happened to this book, newest first. Requests in progress link to Activity.")}
<div class="table-wrap" data-stack><table class="table">
  <thead><tr><th scope="col">Date</th><th scope="col">Event</th><th scope="col">Format</th><th scope="col">By</th></tr></thead>
  <tbody><tr><td data-label="Date">3 Oct 2024</td><td data-label="Event">Imported into Fiction audiobooks</td><td data-label="Format">Audiobook</td><td data-label="By">Storyarr</td></tr>
  <tr><td data-label="Date">3 Oct 2024</td><td data-label="Event">Downloaded from MyAnonamouse with qBittorrent</td><td data-label="Format">Audiobook</td><td data-label="By">Storyarr</td></tr>
  <tr><td data-label="Date">2 Oct 2024</td><td data-label="Event">Requested</td><td data-label="Format">Audiobook</td><td data-label="By">Alex</td></tr></tbody></table></div>

{phone_section([("phone=1", "The cover sits above the title; the two main actions and the More menu wrap under the facts. The tabs stay in header row 2 and scroll sideways.", 760),
                ("phone=1&open=panel-release", "Release details fill the width. The former tabs are sections you scroll through.", 760)],
               "The header block stacks and the slide-outs fill the width.")}
"""
    panels = panel("panel-copy", "Library copy: audiobook, M4B", f"""
<span class="chip" data-tone="success">In library</span>
<dl class="facts"><dt>Library</dt><dd>Fiction audiobooks (Audiobookshelf)</dd><dt>Folder</dt><dd><code>/audiobooks/Mara Ellison/The Glass Harbour</code></dd><dt>Files</dt><dd>1 M4B file · 482 MB · 11 hr 42 min</dd><dt>Chapters</dt><dd>38</dd><dt>Matched to</dt><dd>The Glass Harbour, audiobook read by Sam Oduya</dd></dl>
<section aria-labelledby="copy-coll-h" style="display:grid;gap:var(--space-2)"><h3 id="copy-coll-h">Also in this folder</h3><p class="small muted">Nothing else. Collections list every book they hold here.</p></section>""",
        f'<button class="btn" type="button" data-opens="panel-match">{ic("puzzle")}Correct match</button><button class="btn btn--danger" type="button" data-dialog="dlg-delete-copy">{ic("trash-2")}Delete copy</button>') + \
        panel("panel-request-edition", "Request ebook", f"""
<p>The Glass Harbour, ebook from Tidewater Press, 412 pages.</p>
<fieldset><legend class="field__label">When Storyarr finds a release</legend><div class="option-cards">
<label class="option-card"><input type="radio" name="re-when" checked><strong>Download the best release</strong><small>Uses your download preferences to choose.</small></label>
<label class="option-card"><input type="radio" name="re-when"><strong>Ask me first</strong><small>The request waits in Activity until you choose a release.</small></label></div></fieldset>
<div class="field"><label for="re-lib">Library</label><select class="select" id="re-lib"><option>Fiction ebooks</option><option>Fiction audiobooks</option></select></div>""",
        '<button class="btn btn--primary" type="button">Request ebook</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        panel("panel-release", "Release details", f"""
<p><strong>The.Glass.Harbour.Mara.Ellison.2024.EPUB</strong></p>
<div class="actions"><span class="chip">Ready</span><span class="tag">Freeleech</span><span class="tag">VIP</span></div>
<section aria-labelledby="rl-sum-h" style="display:grid;gap:var(--space-2)"><h3 id="rl-sum-h">Summary</h3><dl class="facts"><dt>Source</dt><dd>MyAnonamouse</dd><dt>Size</dt><dd>2.1 MB</dd><dt>Format</dt><dd>Ebook · EPUB</dd><dt>Uploaded</dt><dd>1 November 2026</dd><dt>Seeders</dt><dd>42</dd></dl></section>
<section aria-labelledby="rl-why-h" style="display:grid;gap:var(--space-2)"><h3 id="rl-why-h">Why it scores 96</h3><ul class="rows">
<li class="row row--no-lead"><div><div class="row__title">Title and author match</div><div class="row__meta">Exact match on both</div></div><div class="row__side"><span class="numeric">+60</span></div></li>
<li class="row row--no-lead"><div><div class="row__title">Preferred format</div><div class="row__meta">EPUB is first in your ebook formats</div></div><div class="row__side"><span class="numeric">+30</span></div></li>
<li class="row row--no-lead"><div><div class="row__title">Preferred source</div><div class="row__meta">MyAnonamouse is first in your sources</div></div><div class="row__side"><span class="numeric">+6</span></div></li></ul></section>
<section aria-labelledby="rl-files-h" style="display:grid;gap:var(--space-2)"><h3 id="rl-files-h">Files</h3><p><code>The Glass Harbour - Mara Ellison.epub</code> · 2.1 MB</p></section>""",
        f'<button class="btn btn--primary" type="button">{ic("download")}Download release</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button><button class="btn btn--danger" type="button">{ic("ban")}Block release</button>') + \
        panel("panel-match", "Correct match", f"""
<p>Choose the book these files belong to. The files move to the chosen book's folder when you save.</p>
<div class="field"><label for="mt-q">Search Hardcover</label><div class="input-group"><input class="input" id="mt-q" type="search" value="The Glass Harbour"><button class="btn" type="button">{ic("search")}Search</button></div></div>
<ul class="rows"><li class="row">{thumb("x", 0)}<div><div class="row__title">The Glass Harbour</div><div class="row__meta">Mara Ellison · 2024 · current match</div></div><div class="row__side"><span class="chip" data-tone="success">Chosen</span></div></li>
<li class="row">{thumb("x", 6)}<div><div class="row__title">Glass Harbours</div><div class="row__meta">Ira Penn · 2011</div></div><div class="row__side"><button class="btn btn--compact" type="button">Use this match<span class="visually-hidden">: Glass Harbours by Ira Penn</span></button></div></li></ul>""",
        '<button class="btn btn--primary" type="button">Save match</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>', wide=True)
    dialogs = dialog("dlg-delete-book", "Delete The Glass Harbour?", "<p>Storyarr deletes 2 library copies (962 MB) and forgets the book. Requests and history for it are removed. This cannot be undone.</p><div class=\"field\"><label for=\"del-type\">Type DELETE to confirm</label><input class=\"input\" id=\"del-type\" autocomplete=\"off\"></div>",
                     '<button class="btn btn--danger btn--primary" type="button" data-closes>Delete permanently</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        dialog("dlg-delete-copy", "Delete this copy?", "<p>The M4B file (482 MB) is deleted from the disk. The other copy and the book stay in your library.</p>",
               '<button class="btn btn--danger btn--primary" type="button" data-closes>Delete copy</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        dialog("dlg-add-list", "Add to list", '<fieldset><legend class="field__label">Lists</legend><label class="check"><input type="checkbox"><span class="check__text">Read next</span></label><label class="check"><input type="checkbox" checked><span class="check__text">Holiday listening</span></label></fieldset>',
               '<button class="btn btn--primary" type="button" data-closes>Save lists</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    row2 = ("Book", [("overview", "Overview", "book-open-text", "storyarr-book.html"), ("editions", "Editions and files", "book-copy", "storyarr-book.html"),
                     ("sources", "Sources", "radar", "storyarr-book.html"), ("history", "History", "history", "storyarr-book.html"),
                     ("details", "Details and matching", "file-pen", "storyarr-book.html")], "overview")
    return page("book", t, "library", "my-library", body, row2, panels, dialogs)


def author():
    facts = ('<dt>Books</dt><dd>4 published · 1 coming 3 March 2027</dd><dt>Series</dt><dd><a href="storyarr-series.html">The Glass Harbour</a></dd>'
             '<dt>Following</dt><dd>Since 4 March 2025 · audiobooks and ebooks</dd>')
    actions = (f'<button class="btn btn--primary" type="button">{ic("download")}Request 1 missing book</button>'
               f'<button class="btn" type="button" data-opens="panel-follow-settings">{ic("sliders-horizontal")}Follow settings</button>'
               + more_menu("m-au-more", "Mara Ellison", [("Open in Hardcover (opens in a new tab)", "external-link"), ("Open in Goodreads (opens in a new tab)", "external-link")]))
    art = '<div class="cover" style="aspect-ratio:1;font-size:var(--text-2xl);font-weight:700;background:var(--color-accent-soft);color:var(--color-text)"><span aria-hidden="true">ME</span></div>'
    extra = '<div class="meter"><div class="meter__label"><span>Released books in library</span><span class="numeric">3 of 4 (75%)</span></div><div class="progress" role="img" aria-label="3 of 4 released books in library"><span style="width:75%"></span></div></div>'
    header = item_header(art, "Mara Ellison", "Author · coastal fantasy and mystery", '<span class="chip" data-tone="success">Following</span>', facts, actions, extra)
    body = f"""
{what_changed([
    "<strong>Back link returns to where you came from</strong> (today it always goes to the home page).",
    "<strong>One item header</strong> shared with the book, series and narrator pages, with one progress bar style and Follow settings as a slide-out.",
    "<strong>Books open the Summary slide-out</strong> instead of navigating away; the Books tab gets the section toolbar and groups books by series.",
    "<strong>Tabs in header row 2</strong> with icons; no capital eyebrow; the portrait is decorative, so it has no alt text repeating the heading.",
])}
{back()}
{header}
<section aria-label="Books by Mara Ellison" style="display:grid;gap:var(--space-4)">
  <div class="toolbar"><div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search books by Mara Ellison" placeholder="Title"></div>
    <div class="filter-chips" role="group" aria-label="Status">{chipbtn("In library", "3")}{chipbtn("Wanted", "1")}{chipbtn("Not released", "1")}</div>
    <div class="toolbar__end"><span class="toolbar__count">6 books</span>{sort_menu("m-au-sort", "Series order", ["Series order", "Published", "Title"])}</div>
  </div></div>
  <h2 class="group-heading"><a href="storyarr-series.html">The Glass Harbour</a> · 4 books</h2>
  <ul class="media-grid" data-size="small">
    {mcard("The Glass Harbour", "Book 1 · 2024", 0, badge=("success", "In library"))}
    {mcard("Lanterns Under Ice", "Book 2 · 2025", 1, badge=("success", "In library"))}
    {mcard("The Tidewright", "Book 3 · 2026", 2, badge=("", "Wanted"))}
    {mcard("The Lamp Room", "Book 4 · 3 Mar 2027", 6, badge=("", "Not released"))}
  </ul>
  <h2 class="group-heading">Other books · 2</h2>
  <ul class="media-grid" data-size="small">
    {mcard("A Map of Small Tides", "2023", 5, badge=("success", "In library"))}
    {mcard("Harbour Songs", "Stories · 2022", 9, badge=("muted", "Excluded · Collection"))}
  </ul>
</section>
{phone_section([("phone=1", "The portrait sits above the name; actions wrap; the toolbar stacks.", 760)], "The item header stacks on phones.")}
"""
    panels = book_panel() + panel("panel-follow-settings", "Follow settings: Mara Ellison", """<fieldset><legend class="field__label">Formats</legend>
<label class="check"><input type="checkbox" checked><span class="check__text">Audiobooks</span></label>
<label class="check"><input type="checkbox" checked><span class="check__text">Ebooks</span></label></fieldset>
<fieldset><legend class="field__label">When a new book comes out</legend><div class="option-cards">
<label class="option-card"><input type="radio" name="fs-when" checked><strong>Request it automatically</strong><small>Storyarr searches your download sources on release day.</small></label>
<label class="option-card"><input type="radio" name="fs-when"><strong>Add it to Wanted</strong><small>You choose when to search.</small></label></div></fieldset>""",
        '<button class="btn btn--primary" type="button">Save follow</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    row2 = ("Author", [("books", "Books", "book-copy", "storyarr-author.html"), ("about", "About", "info", "storyarr-author.html")], "books")
    return page("author", "Mara Ellison", "library", "my-library", body, row2, panels)


def series():
    art = (f'<div style="position:relative;height:250px">'
           f'<div style="position:absolute;left:0;top:0;width:120px">{cover("The Glass Harbour", 0)}</div>'
           f'<div style="position:absolute;left:28px;top:34px;width:120px">{cover("Lanterns Under Ice", 1)}</div>'
           f'<div style="position:absolute;left:56px;top:68px;width:120px">{cover("The Tidewright", 2)}</div></div>')
    extra = '<div class="meter"><div class="meter__label"><span>Released books in library</span><span class="numeric">2 of 3 (67%)</span></div><div class="progress" role="img" aria-label="2 of 3 released books in library"><span style="width:67%"></span></div></div>'
    facts = '<dt>Author</dt><dd><a href="storyarr-author.html">Mara Ellison</a></dd><dt>Books</dt><dd>3 published, 1 novella, 1 coming 3 March 2027</dd><dt>Narrated by</dt><dd><a href="storyarr-narrator.html">Sam Oduya</a></dd>'
    actions = (f'<button class="btn btn--primary" type="button">{ic("bookmark")}Follow series</button>'
               + more_menu("m-se-more", "The Glass Harbour", [("Open in Hardcover (opens in a new tab)", "external-link"), ("Requests for this series in Activity", "activity")]))
    header = item_header(art, "The Glass Harbour", 'Series by <a href="storyarr-author.html">Mara Ellison</a>', '<span class="chip" data-tone="muted">Not followed</span>', facts, actions, extra)

    def srow(num, t, meta, chip, n, checked=False, disabled=False):
        cid = "sel-" + t.lower().replace(" ", "-").replace("'", "")
        box = (f'<label class="check" style="padding:11px 0"><input type="checkbox" id="{cid}"{" checked" if checked else ""}{" disabled" if disabled else ""}><span class="visually-hidden">Select {t}</span></label>')
        return (f'<li class="row" style="grid-template-columns:auto auto minmax(0,1fr) auto">{box}{thumb(t, n)}'
                f'<div><div class="row__title"><button type="button" data-opens="panel-book" class="btn btn--quiet" style="padding:0;min-height:0;color:inherit;font-size:inherit">{num} · {t}</button></div><div class="row__meta">{meta}</div></div>'
                f'<div class="row__side">{chip}</div></li>')
    body = f"""
{what_changed([
    "<strong>Selection is a sticky bar</strong> (\"2 selected · Request · Add to list\") instead of a side column inside the page; Request opens a slide-out with the options.",
    "<strong>Requests tab removed</strong>: request history lives in Activity, filtered by this series (in the More menu). Tabs are Reading order, About and Lists, in header row 2.",
    "<strong>Same item header and progress bar</strong> as author and book pages; Follow series is the one main action. Book titles open the Summary slide-out.",
])}
{back()}
{header}
<section aria-labelledby="ro-h" style="display:grid;gap:var(--space-4);padding-bottom:var(--space-12)">
  <h2 id="ro-h" class="visually-hidden">Reading order</h2>
  <div class="toolbar"><div class="toolbar__row">
    <div class="filter-chips" role="group" aria-label="Status">{chipbtn("Missing", "2")}{chipbtn("Not released", "1")}</div>
    {menu("m-se-format", "Format", [("*Audiobooks and ebooks", None, "menuitemradio"), ("Audiobooks", None, "menuitemradio"), ("Ebooks", None, "menuitemradio")], "Format: Both", None, True)}
    <div class="toolbar__end"><span class="toolbar__count">5 books</span><button class="btn" type="button">{ic("square-check")}Select all missing</button></div>
  </div></div>
  <ul class="rows">
    {srow("Book 1", "The Glass Harbour", "2024 · 11 hr 42 min", '<span class="chip" data-tone="success">In library · Audiobook</span>', 0)}
    {srow("Book 2", "Lanterns Under Ice", "2025 · 9 hr 58 min", '<span class="chip" data-tone="success">In library · Audiobook</span>', 1)}
    {srow("Book 2.5", "The Keeper's Year", "Novella · 2025", '<span class="chip" data-tone="muted">Not requested</span>', 4, True)}
    {srow("Book 3", "The Tidewright", "2026", '<span class="chip">Wanted</span>', 2, True)}
    {srow("Book 4", "The Lamp Room", "3 March 2027", '<span class="chip">Not released · 3 Mar 2027</span>', 6, False, True)}
  </ul>
  <div role="region" aria-label="Selected books" style="position:sticky;bottom:var(--space-4);z-index:5;display:flex;flex-wrap:wrap;align-items:center;gap:var(--space-2) var(--space-4);padding:var(--space-3) var(--space-4);border:1px solid var(--color-border);background:var(--color-surface-raised);box-shadow:var(--shadow-raised)">
    <strong role="status">2 selected</strong>
    <div class="actions" style="margin-left:auto"><button class="btn btn--primary" type="button" data-opens="panel-series-request">{ic("download")}Request 2 books</button><button class="btn" type="button" data-dialog="dlg-add-list">{ic("list-plus")}Add to list</button><button class="btn btn--quiet" type="button">Clear selection</button></div>
  </div>
</section>
{phone_section([("phone=1&at=ro-h", "Rows keep the checkbox and the title; the selection bar stays at the foot of the window and its buttons wrap.", 760),
                ("phone=1&open=panel-series-request", "Request options in the slide-out, full width.", 760)], "The selection bar wraps on phones.")}
"""
    panels = book_panel() + panel("panel-series-request", "Request 2 books", f"""
<ul class="rows"><li class="row">{thumb("x", 4)}<div><div class="row__title">The Keeper's Year</div><div class="row__meta">Book 2.5 · novella</div></div><div class="row__side"></div></li><li class="row">{thumb("x", 2)}<div><div class="row__title">The Tidewright</div><div class="row__meta">Book 3</div></div><div class="row__side"></div></li></ul>
<fieldset><legend class="field__label">Formats</legend><label class="check"><input type="checkbox" checked><span class="check__text">Audiobooks</span></label><label class="check"><input type="checkbox"><span class="check__text">Ebooks</span></label></fieldset>
<div class="field"><label for="sr-nar">Narrator</label><span class="hint" id="sr-narh">Keeps the series in one voice when a choice exists.</span><select class="select" id="sr-nar" aria-describedby="sr-narh"><option>Prefer Sam Oduya</option><option>Any narrator</option></select></div>""",
        '<button class="btn btn--primary" type="button">Request 2 books</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    dialogs = dialog("dlg-add-list", "Add 2 books to a list", '<fieldset><legend class="field__label">Lists</legend><label class="check"><input type="checkbox"><span class="check__text">Read next</span></label><label class="check"><input type="checkbox"><span class="check__text">Holiday listening</span></label></fieldset>',
                     '<button class="btn btn--primary" type="button" data-closes>Save lists</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    row2 = ("Series", [("order", "Reading order", "list-ordered", "storyarr-series.html"), ("about", "About", "info", "storyarr-series.html"), ("lists", "Lists", "list", "storyarr-series.html")], "order")
    return page("series", "The Glass Harbour series", "library", "my-library", body, row2, panels, dialogs)


def narrator():
    art = f'<div class="cover" style="aspect-ratio:1;background:var(--color-accent-soft);color:var(--color-text)">{ic("mic", "i-xl")}</div>'
    facts = ('<dt>In your library</dt><dd>5 audiobooks · 54 hours</dd><dt>Authors</dt><dd><a href="storyarr-author.html">Mara Ellison</a>, Theo Marchetti, Hollis Brant, Lena Ostrova</dd>'
             '<dt>Series</dt><dd><a href="storyarr-series.html">The Glass Harbour</a>, Harbour Lights</dd>')
    actions = (f'<a class="btn btn--primary" href="#more">{ic("search")}Find more by this narrator</a>'
               + more_menu("m-na-more", "Sam Oduya", [("Prefer this narrator in download preferences", "sliders-horizontal"), ("Open in Hardcover (opens in a new tab)", "external-link")]))
    header = item_header(art, "Sam Oduya", "Narrator", "", facts, actions)
    lib = [b for b in BOOKS if b[3] == "Sam Oduya"]
    cards = "".join(mcard(t, a, n, badge=("success", "In library"), audio=True) for (t, a, s, r, f, n) in lib)
    more = "".join([
        mcard("The Salt Wives", "Cora Vance · 2025", 3, opens="panel-book-more", badge=("muted", "Not requested"), audio=True),
        mcard("Harbour Lights: Low Water", "Theo Marchetti · Book 2", 8, opens="panel-book-more", badge=("muted", "Not requested"), audio=True),
        mcard("A Field of Bells", "Hollis Brant · 2023", 11, opens="panel-book-more", badge=("", "Wanted"), audio=True),
        mcard("The Lamp Room", "Mara Ellison · Book 4", 6, opens="panel-book-more", badge=("", "Not released · 3 Mar 2027"), audio=True),
        mcard("Winter Tenants", "Ada Morrow · 2021", 1, opens="panel-book-more", badge=("muted", "Not requested"), audio=True),
    ])
    body = f"""
{what_changed([
    "<strong>New page.</strong> Today a narrator's name is plain text. Now every \"Narrated by\" link (Summary slide-out, book page, editions table) opens this page.",
    "<strong>All books in your library read by this narrator</strong>, with the same section toolbar and Summary slide-out as My library.",
    "<strong>Find more by this narrator</strong> searches Hardcover and Audible for audiobooks they read that you do not have, with the same status chips; Request is in each book's slide-out.",
])}
{back()}
{header}
<section aria-labelledby="lib-h" style="display:grid;gap:var(--space-4)">
  <h2 id="lib-h">In your library</h2>
  <div class="toolbar"><div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search books read by Sam Oduya" placeholder="Title or author"></div>
    {menu("m-na-lib", "Library", [("*All libraries", None, "menuitemradio"), ("Fiction audiobooks", None, "menuitemradio")], "Library: All", "library", True)}
    <div class="toolbar__end"><span class="toolbar__count">5 audiobooks</span>{sort_menu("m-na-sort", "Title", ["Title", "Author", "Published"])}</div>
  </div></div>
  <ul class="media-grid" data-size="small">{cards}</ul>
</section>
<section id="more" aria-labelledby="more-h" style="display:grid;gap:var(--space-4)">
  <div style="display:grid;gap:var(--space-1)"><h2 id="more-h">More read by Sam Oduya</h2><p class="muted">Found on Hardcover and Audible 1 minute ago. Books already in your library are left out.</p></div>
  <div class="toolbar"><div class="toolbar__row">
    <div class="filter-chips" role="group" aria-label="Status">{chipbtn("Not requested", "3")}{chipbtn("Wanted", "1")}{chipbtn("Not released", "1")}</div>
    <div class="toolbar__end"><span class="toolbar__count">5 audiobooks</span>{sort_menu("m-na-more-sort", "Newest", ["Newest", "Title", "Author"])}<button class="btn" type="button">{ic("refresh-cw")}Search again</button></div>
  </div></div>
  <ul class="media-grid" data-size="small">{more}</ul>
</section>
{phone_section([("phone=1", "The header stacks; Find more by this narrator stays the first button.", 760), ("phone=1&at=more", "Results from the search, two covers per row.", 760)], "Same responsive rules as the author page.")}
"""
    panels = book_panel() + book_panel("panel-book-more", "The Salt Wives", 3, ("muted", "Not requested"), author="Cora Vance", series=None,
        blurb="Three sisters inherit a salt works and the debts that come with it. Read by Sam Oduya, unabridged.",
        foot=f'<button class="btn btn--primary" type="button">{ic("download")}Request audiobook</button><button class="btn" type="button">{ic("list-plus")}Add to list</button><a class="btn btn--quiet" href="storyarr-book.html">Open book page</a>')
    return page("narrator", "Sam Oduya", "library", "my-library", body, None, panels)


def build():
    return [book(), author(), series(), narrator()]
