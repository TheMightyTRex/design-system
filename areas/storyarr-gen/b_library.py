from shell import *
from common import BOOKS, book_panel

ROW2_LIBRARY = ("My library shelves", [
    ("libraries", "In my libraries", "book-copy", "storyarr-my-library.html"),
    ("authors", "Authors", "users", "storyarr-my-library.html#authors-tab"),
    ("series", "Series", "library", "storyarr-my-library.html#authors-tab"),
    ("saved", "All saved titles", "archive", "storyarr-my-library.html#saved-tab"),
], "libraries")


def chipbtn(text, count, pressed=False):
    c = f' <span class="count">{count}</span>' if count else ""
    return f'<button class="filter-chip" type="button" aria-pressed="{"true" if pressed else "false"}">{text}{c}</button>'


def view_switch(name, options, checked):
    labels = "".join(
        f'<label><input type="radio" name="{name}" data-show-view="{v}"{" checked" if v == checked else ""}><span>{ic(icon)}<span class="visually-hidden">{text}</span></span></label>'
        for v, text, icon in options
    )
    return f'<fieldset class="segmented" aria-label="View"><legend class="visually-hidden">View</legend>{labels}</fieldset>'


def my_library():
    cards = "".join(
        mcard(t, f"{a}" + (f" · {s.split(', ')[1].capitalize()}" if s else ""), n,
              badge=("info", "Audiobook") if f == "Audiobook" else None)
        for (t, a, s, r, f, n) in BOOKS[:16]
    )
    rows = "".join(
        f'<li class="row row--opens">{thumb(t, n)}<div><div class="row__title"><button type="button" data-opens="panel-book">{t}</button></div>'
        f'<div class="row__meta">{a}{" · " + s if s else ""}{" · read by " + r if r else ""}</div></div>'
        f'<div class="row__side"><span class="tag">{f}</span><span class="chip" data-tone="success">In library</span></div></li>'
        for (t, a, s, r, f, n) in BOOKS[:8]
    )
    body = f"""
{what_changed([
    "<strong>Every book opens the same Summary slide-out</strong> on all four tabs. Today In my libraries opens a panel and the other three tabs jump to the book page.",
    "<strong>One toolbar (design D) on every tab</strong>: view switch, search, format chips with counts, Library menu, sort. Manage connections and Save view moved from above the toolbar into its More menu; the sort note moved into the summary line.",
    "<strong>Summary facts</strong>: Author first, then Series, then Narrated by, which links to the new narrator page.",
    "<strong>One cover grid</strong> that follows the cover size setting, plus a List view. Add a title is a short dialog, not a form that pushes the grid down.",
])}
<div class="page-head"><div class="page-head__text"><h1>My library</h1><p class="page-head__summary">1,284 books in 2 libraries · newest first</p></div></div>
<section aria-label="Books in my libraries" style="display:grid;gap:var(--space-4)">
  <div class="toolbar">
    <div class="toolbar__row">
      {view_switch("lib-view", [("covers", "Covers", "layout-grid"), ("list", "List", "list")], "covers")}
      <div class="toolbar__search"><input class="input" type="search" aria-label="Search my library" placeholder="Title, author or narrator"></div>
      <div class="filter-chips" role="group" aria-label="Format">{chipbtn("Audiobooks", "612", True)}{chipbtn("Ebooks", "803")}</div>
      {menu("m-lib", "Library", [("*All libraries", None, "menuitemradio"), ("Fiction audiobooks", None, "menuitemradio"), ("Fiction ebooks", None, "menuitemradio")], "Library: All", "library", True)}
      <div class="toolbar__end"><span class="toolbar__count">612 books</span>
        {sort_menu("m-lib-sort", "Recently added", ["Recently added", "Title", "Author", "Series", "Published"])}
        {menu("m-lib-more", "More for My library", [("Save this view", "bookmark-plus"), ("Manage connections", "plug"), "hr", ("Refresh library", "refresh-cw")], icon="ellipsis", button_class="icon-btn", aria_label="More for My library")}
      </div>
    </div>
    <div class="applied"><span class="muted">Filtered by</span><span class="applied__item">Audiobooks<button type="button" aria-label="Remove filter: Audiobooks">{ic("x")}</button></span><button class="btn btn--quiet btn--compact" type="button">Clear all</button><span class="muted" style="margin-left:auto">Showing 612 of 1,284</span></div>
  </div>
  <ul class="media-grid" data-view="covers" aria-label="Books">{cards}</ul>
  <ul class="rows" data-view="list" hidden aria-label="Books">{rows}</ul>
  <div class="load-more"><span>Showing 16 of 612 audiobooks</span><button class="btn" type="button">Show 40 more</button></div>
</section>

{board_divider("Authors and Series tabs", "Same toolbar. The view switch adds List and detail; a group opens its author or series page, not a second grid with its own back link.")}
<section id="authors-tab" aria-label="Authors tab example" style="display:grid;gap:var(--space-4)">
  <div class="toolbar"><div class="toolbar__row">
    <fieldset class="segmented" aria-label="View"><legend class="visually-hidden">View</legend><label><input type="radio" name="a-view"><span>{ic("layout-grid")}<span class="visually-hidden">Covers</span></span></label><label><input type="radio" name="a-view" checked><span>{ic("list")}<span class="visually-hidden">List</span></span></label><label><input type="radio" name="a-view"><span>{ic("panel-right-open")}<span class="visually-hidden">List and detail</span></span></label></fieldset>
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search authors" placeholder="Author name"></div>
    <div class="filter-chips" role="group" aria-label="Show">{chipbtn("Following", "8")}{chipbtn("Not followed", "131")}</div>
    <div class="toolbar__end"><span class="toolbar__count">139 authors</span>{sort_menu("m-auth-sort", "Name", ["Name", "Books in library", "Recently added"])}</div>
  </div></div>
  <ul class="rows">
    <li class="row row--opens"><span class="avatar" aria-hidden="true">ME</span><div><div class="row__title"><a href="storyarr-author.html">Mara Ellison</a></div><div class="row__meta">3 books in library · The Glass Harbour</div></div><div class="row__side"><span class="chip" data-tone="success">Following</span></div></li>
    <li class="row row--opens"><span class="avatar" aria-hidden="true">PC</span><div><div class="row__title"><a href="storyarr-author.html">Priya Castellane</a></div><div class="row__meta">2 books in library</div></div><div class="row__side"></div></li>
    <li class="row row--opens"><span class="avatar" aria-hidden="true">RA</span><div><div class="row__title"><a href="storyarr-author.html">Rowan Ashby</a></div><div class="row__meta">2 books in library · The Lantern Wars</div></div><div class="row__side"><span class="chip" data-tone="success">Following</span></div></li>
  </ul>
</section>

{board_divider("All saved titles tab", "Same toolbar; Add a title sits at the end of it and opens a short dialog. Every tile opens the Summary slide-out.")}
<section id="saved-tab" aria-label="All saved titles example" style="display:grid;gap:var(--space-4)">
  <div class="toolbar"><div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search saved titles" placeholder="Title or author"></div>
    <div class="filter-chips" role="group" aria-label="Status">{chipbtn("In library", "1,284")}{chipbtn("Wanted", "9")}{chipbtn("Not requested", "342")}</div>
    <div class="toolbar__end"><span class="toolbar__count">1,635 titles</span><button class="btn btn--primary" type="button" data-dialog="dlg-add-title">{ic("plus")}Add a title</button></div>
  </div></div>
  <ul class="media-grid" data-size="small">
    {mcard("Paper Kingdoms", "Lena Ostrova", 9, badge=("muted", "Not requested"))}
    {mcard("The Long Recess", "Dara Whitlock", 5, badge=("", "Wanted"))}
    {mcard("Starling House Rules", "Felix Amari", 9, badge=("success", "In library"))}
    {mcard("Moth Season", "Lena Ostrova", 7, badge=("muted", "Not requested"))}
  </ul>
</section>

{phone_section([("phone=1", "Header shows the menu button, the name and Display; the shelves stay under it. Search takes its own line and the chips scroll sideways.", 760),
                ("phone=1&open=panel-book", "The Summary slide-out fills the width. Close or Back returns to the same cover.", 760)],
               "The layout changes in two places on phones: the header and the slide-out.")}
"""
    dialogs = dialog("dlg-add-title", "Add a title",
                     '<p>Add a book that is not in your libraries yet, so you can request it or follow its series.</p>'
                     '<div class="field"><label for="at-1">Title</label><input class="input" id="at-1"></div>'
                     '<div class="field"><label for="at-2">Author</label><input class="input" id="at-2"></div>'
                     '<div class="field"><label for="at-3">ISBN or Hardcover link</label><span class="hint" id="at-3h">Optional. Finds the right edition faster.</span><input class="input" id="at-3" aria-describedby="at-3h"></div>',
                     '<button class="btn btn--primary" type="button" data-closes>Add title</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    return page("my-library", "My library", "library", "my-library", body, ROW2_LIBRARY, book_panel(), dialogs)


def following():
    authors = [
        ("ME", "Mara Ellison", "3 of 4 released books in library · next 3 Mar 2027", None, True),
        ("RA", "Rowan Ashby", "2 of 5 released books in library", None, False),
        ("PC", "Priya Castellane", "2 of 2 released books in library", None, False),
        ("IV", "Ines Valdré", "2 of 6 released books in library", ("muted", "Paused"), False),
        ("TM", "Theo Marchetti", "1 of 3 released books in library · next 12 Jan 2027", None, False),
        ("HB", "Hollis Brant", "2 of 2 released books in library", None, False),
    ]
    rows = "".join(
        f'<li class="row row--opens"{" aria-current=\"true\" style=\"background:var(--color-control-active);box-shadow:inset 3px 0 0 var(--color-accent)\"" if cur else ""}>'
        f'<span class="avatar" aria-hidden="true">{ini}</span><div><div class="row__title"><a href="#shelf"{" aria-current=\"true\"" if cur else ""}>{name}</a></div><div class="row__meta">{meta}</div></div>'
        f'<div class="row__side">{f"<span class=\"chip\" data-tone=\"{chip[0]}\">{chip[1]}</span>" if chip else ""}</div></li>'
        for ini, name, meta, chip, cur in authors
    )
    shelf = "".join([
        mcard("The Glass Harbour", "Book 1 · 2024", 0, badge=("success", "In library")),
        mcard("Lanterns Under Ice", "Book 2 · 2025", 1, badge=("success", "In library")),
        mcard("The Tidewright", "Book 3 · 2026", 2, badge=("", "Wanted")),
        mcard("A Map of Small Tides", "Standalone · 2023", 5, badge=("success", "In library")),
        mcard("The Lamp Room", "Book 4 · 3 Mar 2027", 6, badge=("", "Not released")),
        mcard("Harbour Songs", "Stories · 2022", 9, badge=("muted", "Excluded · Collection")),
    ])
    body = f"""
{what_changed([
    "<strong>Authors, Series and Releases moved to header row 2</strong> with icons, like every other page. The hero and the eyebrow \"YOUR READING WORLD\" are gone; the page has one h1.",
    "<strong>One toolbar</strong> replaces the hand-built bar, the Show select and the separate sort: status chips with counts, sort, and Follow an author at the end.",
    "<strong>Follow an author opens a slide-out with a search</strong>, instead of jumping to a books search.",
    "<strong>No drawer inside the detail</strong>: a book opens the shared Summary slide-out. Follow settings open in a slide-out instead of swapping the whole page. One way to load more.",
])}
<div class="page-head"><div class="page-head__text"><h1>Following</h1><p class="page-head__summary">38 authors · 4 new books this month · next release 12 Jan 2027</p></div></div>
<div class="toolbar">
  <div class="toolbar__row">
    {view_switch("f-view", [("list", "List", "list"), ("detail", "List and detail", "panel-right-open")], "detail")}
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search followed authors" placeholder="Author name"></div>
    <div class="filter-chips" role="group" aria-label="Show">{chipbtn("Upcoming", "5")}{chipbtn("Published recently", "4")}{chipbtn("Not in library", "17")}{chipbtn("Paused", "2")}</div>
    <div class="toolbar__end"><span class="toolbar__count">38 authors</span>{sort_menu("m-f-sort", "Name", ["Name", "Next release", "Books not in library"])}<button class="btn btn--primary" type="button" data-opens="panel-follow-author">{ic("plus")}Follow an author</button></div>
  </div>
</div>
<div style="display:flex;flex-wrap:wrap;gap:var(--space-6);align-items:flex-start">
  <nav aria-label="Followed authors" style="flex:1 1 300px;min-width:0"><ul class="rows">{rows}</ul><div class="load-more"><span>Showing 6 of 38 authors</span><button class="btn" type="button">Show 20 more</button></div></nav>
  <section id="shelf" aria-labelledby="shelf-h" class="panel" data-view="detail" style="flex:3 1 520px;min-width:0">
    <div class="panel__head"><div style="display:grid;gap:4px"><h2 id="shelf-h">Mara Ellison</h2><span class="small muted">Following since 4 March 2025 · audiobooks and ebooks · new books are requested automatically</span></div>
      <div class="actions"><button class="btn btn--primary" type="button">{ic("download")}Request 1 missing book</button><button class="btn" type="button" data-opens="panel-follow-settings">{ic("sliders-horizontal")}Follow settings</button><a class="btn btn--quiet" href="storyarr-author.html">Open author page</a></div></div>
    <div class="meter"><div class="meter__label"><span>Released books in library</span><span class="numeric">3 of 4 (75%)</span></div><div class="progress" role="img" aria-label="3 of 4 released books in library"><span style="width:75%"></span></div></div>
    <div class="filter-chips" role="group" aria-label="Status">{chipbtn("In library", "3")}{chipbtn("Wanted", "1")}{chipbtn("Not released", "1")}{chipbtn("Excluded", "1")}</div>
    <ul class="media-grid" data-size="small" aria-label="Books by Mara Ellison">{shelf}</ul>
  </section>
</div>
{phone_section([("phone=1&view=list", "On phones the list shows alone; choosing an author opens the shelf as its own page with a back link.", 760),
                ("phone=1&open=panel-follow-settings", "Follow settings in the slide-out, full width, with Save follow and Cancel in a footer that stays put.", 760)],
               "List and detail becomes list, then page. The slide-outs fill the width.")}
"""
    panels = book_panel() + panel("panel-follow-author", "Follow an author",
        f"""<div class="field"><label for="fa-q">Author name</label><div class="input-group"><input class="input" id="fa-q" type="search" value="Okafor"><button class="btn" type="button">{ic("search")}Search</button></div></div>
<p class="small muted" role="status">3 authors found on Hardcover</p>
<ul class="rows">
<li class="row"><span class="avatar" aria-hidden="true">JO</span><div><div class="row__title">Jonah Okafor</div><div class="row__meta">6 books · 1 in your library</div></div><div class="row__side"><button class="btn btn--compact" type="button">{ic("bookmark")}Follow<span class="visually-hidden"> Jonah Okafor</span></button></div></li>
<li class="row"><span class="avatar" aria-hidden="true">AO</span><div><div class="row__title">Adaeze Okafor</div><div class="row__meta">2 books</div></div><div class="row__side"><button class="btn btn--compact" type="button">{ic("bookmark")}Follow<span class="visually-hidden"> Adaeze Okafor</span></button></div></li>
<li class="row"><span class="avatar" aria-hidden="true">BO</span><div><div class="row__title">Bem Okafor-Lane</div><div class="row__meta">1 book</div></div><div class="row__side"><button class="btn btn--compact" type="button">{ic("bookmark")}Follow<span class="visually-hidden"> Bem Okafor-Lane</span></button></div></li>
</ul>
<p class="small muted">Following an author asks for their new books as they come out. You choose formats next.</p>""") + panel("panel-follow-settings", "Follow settings: Mara Ellison",
        f"""<fieldset><legend class="field__label">Formats</legend>
<label class="check"><input type="checkbox" checked><span class="check__text">Audiobooks</span></label>
<label class="check"><input type="checkbox" checked><span class="check__text">Ebooks</span></label></fieldset>
<fieldset><legend class="field__label">When a new book comes out</legend><div class="option-cards">
<label class="option-card"><input type="radio" name="fs-when" checked><strong>Request it automatically</strong><small>Storyarr searches your download sources on release day.</small></label>
<label class="option-card"><input type="radio" name="fs-when"><strong>Add it to Wanted</strong><small>You choose when to search.</small></label></div></fieldset>
<fieldset><legend class="field__label">Books to exclude</legend>
<label class="check"><input type="checkbox" checked><span class="check__text">Collections and anthologies</span></label>
<label class="check"><input type="checkbox"><span class="check__text">Plays and scripts</span></label></fieldset>
<label class="check"><input type="checkbox"><span class="check__text">Pause this follow<span class="check__hint">Keeps the books you have; stops asking for new ones.</span></span></label>""",
        f'<button class="btn btn--primary" type="button">Save follow</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button><button class="btn btn--danger" type="button" data-dialog="dlg-unfollow">Stop following</button>')
    dialogs = dialog("dlg-unfollow", "Stop following Mara Ellison?",
                     "<p>Storyarr stops asking for her new books. Books already in your library stay, and requests in progress carry on.</p>",
                     '<button class="btn btn--danger btn--primary" type="button" data-closes>Stop following</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    row2 = ("Following", [("authors", "Authors", "users", "storyarr-following.html"), ("series", "Series", "library", "storyarr-following.html"), ("releases", "Releases", "calendar-clock", "storyarr-following.html")], "authors")
    return page("following", "Following", "library", "following", body, row2, panels, dialogs)


def library_review():
    def rrow(t, n, path, tags, cover_ok=True):
        lead = thumb(t, n) if cover_ok else '<div class="cover" style="width:48px" aria-hidden="true"></div>'
        tg = "".join(f'<span class="tag">{x}</span>' for x in tags)
        return (f'<li class="row row--opens">{lead}<div><div class="row__title"><button type="button" data-opens="panel-review">{t}</button></div>'
                f'<div class="row__meta"><code>{path}</code> · Fiction audiobooks</div></div><div class="row__side">{tg}</div></li>')
    body = f"""
{what_changed([
    "<strong>Item details open in a wide slide-out, not a modal</strong>, so the queue stays in view. Previous and Next in its header replace the \"Review next item after saving\" checkbox.",
    "<strong>No nesting</strong>: today the modal holds an open details block, sub-tabs, an embedded search page and an inline preview. Now Where to look is a segmented control, and results and the chosen match sit in the same slide-out.",
    "<strong>The section toolbar</strong> replaces the hand-built bar and the \"Most common problems\" links: problem chips with counts, Library menu and sort.",
    "<strong>Rows with real covers</strong> instead of a fourth card style with 9px placeholder text. \"Couldn't read fully\" becomes \"Cannot read file\". Leave unmatched and Delete stay dialogs.",
])}
<div class="page-head"><div class="page-head__text"><h1>Library review</h1><p class="page-head__summary">12 items need a decision · 4 fixed this week</p></div></div>
<div class="toolbar">
  <div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search library review" placeholder="File name, title or author"></div>
    <div class="filter-chips" role="group" aria-label="Problem">{chipbtn("No match found", "5")}{chipbtn("Low confidence", "2")}{chipbtn("Cannot read file", "3")}{chipbtn("Missing details", "2")}</div>
    {menu("m-rv-lib", "Library", [("*All libraries", None, "menuitemradio"), ("Fiction audiobooks", None, "menuitemradio"), ("Fiction ebooks", None, "menuitemradio")], "Library: All", "library", True)}
    <div class="toolbar__end"><span class="toolbar__count">12 items</span>{sort_menu("m-rv-sort", "Oldest first", ["Oldest first", "Newest first", "File name"])}</div>
  </div>
</div>
<section aria-labelledby="g1"><h2 class="group-heading" id="g1">Needs matching (7)</h2><ul class="rows">
{rrow("Lanterns Under Ice", 1, "/audiobooks/Mara Ellison/Lanterns Under Ice (2025)", ["No match found"])}
{rrow("track01-ninth-lantern.m4b", 8, "/audiobooks/Unsorted/track01-ninth-lantern.m4b", ["No match found"], False)}
{rrow("Bright Fathoms", 7, "/audiobooks/Ines Valdre/Bright Fathoms", ["Low confidence"])}
</ul></section>
<section aria-labelledby="g2"><h2 class="group-heading" id="g2">Read issues (3)</h2><ul class="rows">
{rrow("Moth Season", 7, "/audiobooks/Lena Ostrova/Moth Season/part2.mp3", ["Cannot read file"])}
{rrow("Hollow Pines", 10, "/ebooks/Hollis Brant/Hollow Pines.epub", ["Cannot read file"])}
</ul></section>
<section aria-labelledby="g3"><h2 class="group-heading" id="g3">Details (2)</h2><ul class="rows">
{rrow("The Quiet Engine", 11, "/ebooks/Dara Whitlock/The Quiet Engine.epub", ["Missing details"])}
</ul></section>
<div class="load-more"><span>Showing 6 of 12 items</span><button class="btn" type="button">Show 6 more</button></div>
{phone_section([("phone=1", "Rows keep the cover and title; problem tags wrap under the title.", 760),
                ("phone=1&open=panel-review", "The review slide-out fills the width; Previous and Next stay in its header.", 760)],
               "On phones the list and the review slide-out each take the full width.")}
"""
    head_extra = (f'<button class="icon-btn" type="button" aria-label="Previous item">{ic("chevron-left")}</button>'
                  f'<button class="icon-btn" type="button" aria-label="Next item">{ic("chevron-right")}</button>')
    review = panel("panel-review", "Review: Lanterns Under Ice", f"""
<p class="small muted">Item 1 of 12 · Needs matching</p>
<div class="notice" data-tone="warning">{ic("triangle-alert")}<div class="notice__body"><span class="notice__title">No match found</span><p>Storyarr read the folder and file tags but found no book with this title and author on Hardcover. Search again or enter the details yourself.</p></div></div>
<section aria-labelledby="rv-read-h" style="display:grid;gap:var(--space-3)"><h3 id="rv-read-h">What Storyarr read</h3>
<dl class="facts"><dt>Folder</dt><dd><code>/audiobooks/Mara Ellison/Lanterns Under Ice (2025)</code></dd><dt>Files</dt><dd>14 MP3 files · 9 hr 58 min · 512 MB</dd><dt>Title tag</dt><dd>Lanterns under ice (unabridged)</dd><dt>Author tag</dt><dd>M. Ellison</dd><dt>Narrator tag</dt><dd>Sam Oduya</dd><dt>Library</dt><dd>Fiction audiobooks</dd></dl></section>
<section aria-labelledby="rv-find-h" style="display:grid;gap:var(--space-3)"><h3 id="rv-find-h">Find the right book</h3>
<fieldset><legend class="field__label">Where to look</legend><div class="segmented"><label><input type="radio" name="rv-where" checked><span>Hardcover</span></label><label><input type="radio" name="rv-where"><span>Open Library</span></label><label><input type="radio" name="rv-where"><span>Enter details yourself</span></label></div></fieldset>
<div class="field"><label for="rv-q">Search Hardcover</label><div class="input-group"><input class="input" id="rv-q" type="search" value="Lanterns under ice Ellison"><button class="btn" type="button">{ic("search")}Search</button></div></div>
<ul class="rows" aria-label="Possible matches">
<li class="row">{thumb("Lanterns Under Ice", 1)}<div><div class="row__title">Lanterns Under Ice</div><div class="row__meta">Mara Ellison · The Glass Harbour, book 2 · 2025 · audiobook read by Sam Oduya</div></div><div class="row__side"><span class="chip" data-tone="success">Chosen</span></div></li>
<li class="row">{thumb("Lanterns", 4)}<div><div class="row__title">Lanterns</div><div class="row__meta">Mara Ellis · 2019</div></div><div class="row__side"><button class="btn btn--compact" type="button">Use this match<span class="visually-hidden">: Lanterns by Mara Ellis</span></button></div></li>
</ul>
<div class="notice" data-tone="success" role="status">{ic("circle-check")}<div class="notice__body"><span class="notice__title">Match chosen</span><p>Lanterns Under Ice by Mara Ellison. Save to move the files into place and add the book to My library.</p></div></div>
</section>""",
        f'<button class="btn btn--primary" type="button">Save and review next</button><button class="btn" type="button" data-dialog="dlg-leave">Leave unmatched</button><button class="btn btn--danger" type="button" data-dialog="dlg-delete-item">{ic("trash-2")}Delete files</button>',
        wide=True, head_extra=head_extra)
    dialogs = dialog("dlg-leave", "Leave Lanterns Under Ice unmatched?",
                     "<p>The files stay in your library under their folder name. Storyarr stops asking about them; you can match them later from the book page.</p>",
                     '<button class="btn btn--primary" type="button" data-closes>Leave unmatched</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        dialog("dlg-delete-item", "Delete the files for Lanterns Under Ice?",
               "<p>14 files (512 MB) are deleted from <code>/audiobooks/Mara Ellison/Lanterns Under Ice (2025)</code>. This cannot be undone. Your request history stays.</p>",
               '<button class="btn btn--danger btn--primary" type="button" data-closes>Delete files</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    row2 = ("Library review", [("all", "All", "circle-alert", "storyarr-library-review.html", "12", " items"),
                               ("needs-matching", "Needs matching", "puzzle", "storyarr-library-review.html", "7", " items"),
                               ("read-issue", "Read issues", "file-x", "storyarr-library-review.html", "3", " items"),
                               ("details", "Details", "file-question", "storyarr-library-review.html", "2", " items")], "all")
    return page("library-review", "Library review", "library", "review", body, row2, review, dialogs)


def build():
    return [my_library(), following(), library_review()]
