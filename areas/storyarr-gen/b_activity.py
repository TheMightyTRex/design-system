from shell import *
from b_library import chipbtn


def req_row(t, n, byline, chips, meta, primary, more_id, progress=None, checkbox=False):
    side = primary + menu(more_id, f"More actions for {t}", [("Search again", "refresh-cw"), ("Cancel download", "circle-x"), "hr", ("Withdraw request|data-dialog=\"dlg-withdraw\"", "undo-2")],
                          icon="ellipsis", button_class="icon-btn", aria_label=f"More actions for {t}")
    prog = (f'<div class="meter" style="grid-column:2 / -1"><div class="progress" role="img" aria-label="{progress}% downloaded"><span style="width:{progress}%"></span></div></div>'
            if progress is not None else "")
    lead = thumb(t, n)
    cols = ""
    if checkbox:
        lead = f'<label class="check" style="padding:11px 0"><input type="checkbox" checked><span class="visually-hidden">Select {t}</span></label>{thumb(t, n)}'
        cols = ' style="grid-template-columns:auto auto minmax(0,1fr) auto"'
    return (f'<li class="row row--opens"{cols}>{lead}<div style="display:grid;gap:4px"><div class="row__title"><button type="button" data-opens="panel-request">{t}</button></div>'
            f'<div class="row__meta">{byline}</div><div class="actions">{chips}</div><div class="row__meta">{meta}</div></div>'
            f'<div class="row__side">{side}</div>{prog}</li>')


def activity():
    rows = "".join([
        req_row("Lanterns Under Ice", 1, "Mara Ellison · requested by Alex", '<span class="chip" data-tone="warning">Needs attention · Ebook</span><span class="chip" data-tone="success">In library · Audiobook</span>',
                "The download stalled and no other release meets your minimum score.", f'<button class="btn btn--primary btn--compact" type="button" data-opens="panel-sources">Choose a release</button>', "m-r1"),
        req_row("The Tidewright", 2, "Mara Ellison · requested automatically (following)", '<span class="chip" data-tone="info">Downloading 45% · Audiobook</span><span class="chip">Wanted · Ebook</span>',
                "MyAnonamouse · qBittorrent · 212 of 470 MB · 6 min left", f'<button class="btn btn--compact" type="button">{ic("pause")}Pause<span class="visually-hidden"> The Tidewright</span></button>', "m-r2", 45),
        req_row("Night Ferry", 4, "Theo Marchetti · requested by Robin", '<span class="chip" data-tone="info">Importing · Audiobook</span>',
                "Copying 22 files into Fiction audiobooks", "", "m-r3"),
        req_row("Ember and Ash Road", 3, "Rowan Ashby · requested by Alex", '<span class="chip">Waiting · 16:31 · Audiobook</span>',
                "No release found in 4 sources. Storyarr searches again at 16:31.", f'<button class="btn btn--compact" type="button">{ic("search")}Search now</button>', "m-r4"),
    ])
    wanted = "".join([
        req_row("Paper Kingdoms", 9, "Lena Ostrova · requested by Robin, 1 Nov", '<span class="chip">Pending · Ebook</span>', "Waiting for an administrator to approve", "", "m-w1", checkbox=True),
        req_row("Starling House Rules", 9, "Felix Amari · requested by Sam, 31 Oct", '<span class="chip">Pending · Audiobook</span>', "Waiting for an administrator to approve", "", "m-w2", checkbox=True),
    ])
    hist = [("1 Nov 2026", "The Glass Harbour", "Ebook", ("success", "In library"), "Alex"), ("31 Oct 2026", "Moth Season", "Audiobook", ("muted", "Declined"), "Sam"),
            ("30 Oct 2026", "Hollow Pines", "Ebook", ("muted", "Withdrawn"), "Robin"), ("28 Oct 2026", "The Quiet Engine", "Ebook", ("danger", "Failed"), "Alex")]
    htr = "".join(f'<tr><td data-label="Date">{d}</td><td data-label="Book"><button class="btn btn--quiet btn--compact" type="button" data-opens="panel-request" style="padding:0">{b}</button></td><td data-label="Format">{f}</td><td data-label="Outcome"><span class="chip" data-tone="{c[0]}">{c[1]}</span></td><td data-label="Requested by">{r}</td></tr>' for d, b, f, c, r in hist)
    body = f"""
{what_changed([
    "<strong>The heading says Activity</strong>, like the menu, instead of \"Requests\". Sort, Find books and Import local files leave the tab row: sort joins the toolbar and the two actions go in its More menu.",
    "<strong>One row per request</strong> with a status chip per format and a progress bar only while downloading, instead of a table with one h2 per request and mostly empty Speed and Time left columns.",
    "<strong>Request details open in a slide-out</strong> with the recovery timeline already expanded, preferences and reasons, and actions in a footer. Today the status chip is a 20px button that expands a table row two details blocks deep.",
    "<strong>Sources for a request</strong> open in a wide slide-out instead of a modal inside a table cell. Withdraw is a dialog at page level. Status words follow the content guide: \"In library\", never \"Available\".",
])}
<div class="page-head"><div class="page-head__text"><h1>Activity</h1><p class="page-head__summary">Queue · 4 requests in progress · 1 needs attention</p></div></div>
<div class="toolbar">
  <div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search the queue" placeholder="Title or author"></div>
    <div class="filter-chips" role="group" aria-label="Status">{chipbtn("Downloading", "1")}{chipbtn("Importing", "1")}{chipbtn("Needs attention", "1")}{chipbtn("Waiting", "1")}</div>
    {menu("m-a-format", "Format", [("*Audiobooks and ebooks", None, "menuitemradio"), ("Audiobooks", None, "menuitemradio"), ("Ebooks", None, "menuitemradio")], "Format: Both", None, True)}
    <div class="toolbar__end"><span class="toolbar__count">4 requests</span>{sort_menu("m-a-sort", "Newest", ["Newest", "Oldest", "Title", "Status"])}
    {menu("m-a-more", "More for Activity", [("Find books", "search"), ("Import local files", "folder-input")], icon="ellipsis", button_class="icon-btn", aria_label="More for Activity")}</div>
  </div>
</div>
<ul class="rows" aria-label="Queue">{rows}</ul>

{board_divider("Wanted tab", "Requests waiting for approval or a release. Administrators select rows and act on them together in a bar that stays in view.")}
<section id="wanted" aria-label="Wanted example" style="display:grid;gap:var(--space-4)">
  <div class="toolbar"><div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search Wanted" placeholder="Title or author"></div>
    <div class="filter-chips" role="group" aria-label="Show">{chipbtn("Pending", "2", True)}{chipbtn("Your requests", "3")}</div>
    {menu("m-w-req", "Requested by", [("*Everyone", None, "menuitemradio"), ("Alex", None, "menuitemradio"), ("Robin", None, "menuitemradio"), ("Sam", None, "menuitemradio")], "Requested by: Everyone", "users", True)}
    <div class="toolbar__end"><span class="toolbar__count">2 of 9 requests</span></div>
  </div></div>
  <ul class="rows">{wanted}</ul>
  <div role="region" aria-label="Selected requests" style="position:sticky;bottom:var(--space-4);z-index:5;display:flex;flex-wrap:wrap;align-items:center;gap:var(--space-2) var(--space-4);padding:var(--space-3) var(--space-4);border:1px solid var(--color-border);background:var(--color-surface-raised);box-shadow:var(--shadow-raised)">
    <strong role="status">2 selected</strong><div class="actions" style="margin-left:auto"><button class="btn btn--primary" type="button">{ic("check")}Approve 2 requests</button><button class="btn" type="button" data-dialog="dlg-decline">{ic("ban")}Decline 2 requests</button><button class="btn btn--quiet" type="button">Clear selection</button></div>
  </div>
</section>

{board_divider("History tab", "Finished requests are real tabular data, so they stay a table. Selecting a book opens the same request slide-out.")}
<section id="history" aria-label="History example" style="display:grid;gap:var(--space-4)">
  <div class="toolbar"><div class="toolbar__row">
    <div class="toolbar__search"><input class="input" type="search" aria-label="Search history" placeholder="Title or author"></div>
    <div class="filter-chips" role="group" aria-label="Outcome">{chipbtn("In library", "31")}{chipbtn("Declined", "2")}{chipbtn("Withdrawn", "1")}{chipbtn("Failed", "1")}</div>
    {menu("m-h-date", "Date", [("*Last 30 days", None, "menuitemradio"), ("Last 90 days", None, "menuitemradio"), ("All time", None, "menuitemradio")], "Last 30 days", "calendar-days", True)}
    <div class="toolbar__end"><span class="toolbar__count">35 requests</span></div>
  </div></div>
  <div class="table-wrap" data-stack><table class="table"><thead><tr><th scope="col" aria-sort="descending"><button type="button">Date{ic("arrow-up-down")}</button></th><th scope="col">Book</th><th scope="col">Format</th><th scope="col">Outcome</th><th scope="col">Requested by</th></tr></thead><tbody>{htr}</tbody></table></div>
</section>
{phone_section([("phone=1", "Rows stack: chips and the primary action wrap under the title; the progress bar spans the row.", 760),
                ("phone=1&open=panel-request", "Request details fill the width, with the timeline first after the status.", 760)],
               "The queue and the request slide-out on a phone.")}
"""
    tl = [("30 Oct, 14:12", "Requested by Alex", "Ebook, Fiction ebooks"),
          ("30 Oct, 14:13", "Searched 4 sources", "3 releases found; best score 88"),
          ("30 Oct, 14:13", "Sent to qBittorrent", "Lanterns.Under.Ice.EPUB from MyAnonamouse"),
          ("30 Oct, 20:40", "Download stalled at 62%", "No seeders for 6 hours"),
          ("30 Oct, 20:41", "Release blocked and searched again", "Storyarr will not try this release again"),
          ("30 Oct, 20:42", "2 releases found, both below your minimum score", "Scores 41 and 37; minimum 50"),
          ("Now", "Needs attention", "Waiting for you to choose a release or change the request")]
    tli = "".join(f'<li class="row row--no-lead"><div><div class="row__title">{w}</div><div class="row__meta">{m}</div></div><div class="row__side"><span class="small muted numeric">{t}</span></div></li>' for t, w, m in tl)
    panels = panel("panel-request", "Lanterns Under Ice, ebook", f"""
<div class="notice" data-tone="warning">{ic("triangle-alert")}<div class="notice__body"><span class="notice__title">Needs attention</span><p>The download stalled, and the other releases are below your minimum score. Choose a release, or search again later.</p></div></div>
<dl class="facts"><dt>Author</dt><dd><a href="storyarr-author.html">Mara Ellison</a></dd><dt>Series</dt><dd><a href="storyarr-series.html">The Glass Harbour, book 2</a></dd><dt>Requested by</dt><dd>Alex, 30 October 2026</dd><dt>Library</dt><dd>Fiction ebooks</dd><dt>Download client</dt><dd>qBittorrent</dd></dl>
<section aria-labelledby="tl-h" style="display:grid;gap:var(--space-2)"><h3 id="tl-h">Recovery timeline</h3><ol class="rows" style="padding:0">{tli}</ol></section>
<section aria-labelledby="pc-h" style="display:grid;gap:var(--space-2)"><h3 id="pc-h">Preferences and limits</h3><dl class="facts"><dt>Formats</dt><dd>EPUB, then AZW3</dd><dt>Minimum score</dt><dd>50</dd><dt>Sources</dt><dd>All 4 sources</dd><dt>Language</dt><dd>English</dd></dl>
<a href="storyarr-settings-downloads.html">Change download preferences</a></section>""",
        f'<button class="btn btn--primary" type="button" data-opens="panel-sources">Choose a release</button><button class="btn" type="button">{ic("refresh-cw")}Search again</button><button class="btn btn--danger" type="button" data-dialog="dlg-withdraw">Withdraw</button>', wide=True) + \
        panel("panel-sources", "Releases for Lanterns Under Ice, ebook", f"""
<p class="small muted">Searched 4 sources at 20:42. Releases below your minimum score are shown with a reason.</p>
<div class="table-wrap" data-stack><table class="table"><thead><tr><th scope="col">Release</th><th scope="col">Source</th><th scope="col">Score</th><th scope="col"><span class="visually-hidden">Action</span></th></tr></thead><tbody>
<tr><td data-label="Release">Lanterns Under Ice EPUB (fan edit)</td><td data-label="Source">AudioBook Bay</td><td data-label="Score" class="numeric">41 · below minimum</td><td><button class="btn btn--compact" type="button" data-dialog="dlg-anyway">Download anyway</button></td></tr>
<tr><td data-label="Release">lanterns_ice_ellison.azw3</td><td data-label="Source">Prowlarr</td><td data-label="Score" class="numeric">37 · below minimum</td><td><button class="btn btn--compact" type="button" data-dialog="dlg-anyway">Download anyway</button></td></tr>
<tr><td data-label="Release">Lanterns.Under.Ice.EPUB</td><td data-label="Source">MyAnonamouse</td><td data-label="Score" class="numeric">88</td><td><span class="chip" data-tone="danger">Blocked</span></td></tr>
</tbody></table></div>
<a href="storyarr-book.html">Open the book's Sources tab</a>""", wide=True)
    dialogs = dialog("dlg-withdraw", "Withdraw the request for Lanterns Under Ice?", "<p>Storyarr stops searching for the ebook. The audiobook in your library is not affected. You can request it again at any time.</p>",
                     '<button class="btn btn--danger btn--primary" type="button" data-closes>Withdraw request</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        dialog("dlg-decline", "Decline 2 requests?", '<p>Robin and Sam are told their requests were declined.</p><div class="field"><label for="dc-why">Reason (optional)</label><input class="input" id="dc-why"></div>',
               '<button class="btn btn--primary" type="button" data-closes>Decline 2 requests</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>') + \
        dialog("dlg-anyway", "Download a release below your minimum score?", "<p>This release scored 41 because it is a fan edit. Storyarr downloads it once for this request and does not change your preferences.</p>",
               '<button class="btn btn--primary" type="button" data-closes>Download anyway</button><button class="btn btn--quiet" type="button" data-closes>Cancel</button>')
    return page("activity", "Activity", "activity", "queue", body, None, panels, dialogs)


def build():
    return [activity()]
