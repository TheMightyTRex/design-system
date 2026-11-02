from shell import AREAS, ic, logo

BOARDS = [
    ("Library", [
        ("my-library", "My library", "Every book opens the same Summary slide-out on all four tabs; one toolbar per tab; Author, Series, then Narrated by in the facts."),
        ("following", "Following", "Tabs in header row 2, hero dropped; Follow an author and Follow settings open slide-outs; no drawer inside the detail."),
        ("library-review", "Library review", "Item review moves from a deeply nested modal to a wide slide-out with Previous and Next; problem chips on the toolbar."),
    ]),
    ("Item pages", [
        ("book", "Book page", "Two main actions and a More menu; tabs in row 2, including a visible Details and matching; copies, editions, releases and matching in slide-outs."),
        ("author", "Author page", "Shared item header and progress bar; back link returns where you came from; books open the Summary slide-out."),
        ("series", "Series page", "Selection side column becomes a sticky selection bar; Request opens a slide-out; Requests tab moves to Activity."),
        ("narrator", "Narrator page (new)", "Every book in your library read by one narrator, plus Find more by this narrator."),
    ]),
    ("Discover and search", [
        ("discover", "Discover: For you and Browse", "Visible h1, one shelf header, Customise Discover as a slide-out; Browse on the section toolbar with Clear all."),
        ("calendar", "Calendar", "Month is a real table; day details in the shared slide-out; one toolbar with month controls; list view on phones."),
        ("search", "Search results", "One search box (the header); Where to search menu and Books, Authors, Series chips; results open the Summary slide-out."),
    ]),
    ("Activity", [
        ("activity", "Activity: Queue, Wanted, History", "Heading says Activity; one row per request; request details with the recovery timeline in a slide-out; bulk approve on Wanted."),
    ]),
    ("Settings", [
        ("settings-general", "Settings: General", "Display renamed from General; one save bar; notification channels edit in a slide-out and deleting one now asks first."),
        ("settings-accounts", "Settings: Accounts", "No third tab level; people and roles edit in slide-outs; sign-in providers move to Sign-in."),
        ("settings-sources", "Settings: Sources", "Reading accounts as cards with list rows; connecting and list details in slide-outs; one home for the Hardcover token."),
        ("settings-library", "Settings: Library", "One way to add and edit servers, access and folders (slide-outs); File naming's save bar becomes the model."),
        ("settings-downloads", "Settings: Downloads", "Clients only in Download clients, edited in a slide-out; reserve and recovery move to Preferences; blocklist with Undo."),
        ("settings-system", "Settings: System", "Logs on the toolbar with entries in a slide-out; main upgrade setting first; restore is a dialog."),
    ]),
    ("Wizards", [
        ("onboarding", "Onboarding", "Shared wizard: one question per step, Continue saves, Keep the defaults and finish, connection as a dialog."),
        ("upgrade", "Upgrade wizard", "Same wizard as setup; one step per new setting; Remind me later is a quiet button."),
    ]),
]


def build():
    groups = []
    for g, items in BOARDS:
        cards = "".join(
            f'<li class="card"><h3 class="card__title"><a href="storyarr-{slug}.html">{name}</a></h3><p class="small">{summary}</p>'
            '</li>'
            for slug, name, summary in items)
        groups.append(f'<section aria-labelledby="g-{g[:4]}" style="display:grid;gap:var(--space-3)"><h2 id="g-{g[:4]}">{g}</h2><ul class="cards">{cards}</ul></section>')
    html = f"""<!doctype html>
<html lang="en-GB" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Storyarr area boards · Shared components</title>
<link rel="stylesheet" href="../tokens.css">
<link rel="stylesheet" href="../components.css">
<style>svg.i {{ width: var(--icon-md); height: var(--icon-md); }}</style>
</head>
<body>
<!--ICONS-->
<a class="skip-link" href="#main">Skip to main content</a>
<main class="page" id="main">
<div class="page-head"><div class="page-head__text"><h1>Storyarr area boards</h1><p class="page-head__summary">19 boards, 2 November 2026 · built only from the shared component library · read with audit-storyarr.md</p></div>
<div class="actions"><a class="btn" href="../gallery.html">{ic("layout-grid")}Component gallery</a></div></div>
<div class="notice" role="note">{ic("info")}<div class="notice__body"><span class="notice__title">How to read the boards</span>
<p>Each board is a full desktop page with the rail, header row 1 and, where the page has tabs, header row 2. It starts with \"What changed and why\" and ends with a 390px phone preview of the part whose layout changes. Slide-outs and dialogs work: select a book, a row or an Edit button. Parts marked \"Board: another tab or state of this page\" show other tabs on the same board.</p>
<p>Components the boards needed but the library lacks are listed in storyarr-missing-components.md. The boards are generated by storyarr-gen/make.py, then tools/build.py.</p></div></div>
{"".join(groups)}
</main>
</body>
</html>
"""
    (AREAS / "index-storyarr.src.html").write_text(html)
    return ["index-storyarr.src.html"]
