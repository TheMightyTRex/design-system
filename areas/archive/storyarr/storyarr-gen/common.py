"""Sample data and pieces used on several Storyarr boards. All names and titles are invented."""
from shell import ic, cover, panel, menu

# (title, author, series or None, narrator or None, format, colour index)
BOOKS = [
    ("The Glass Harbour", "Mara Ellison", "The Glass Harbour, book 1", "Sam Oduya", "Audiobook and ebook", 0),
    ("Lanterns Under Ice", "Mara Ellison", "The Glass Harbour, book 2", "Sam Oduya", "Audiobook", 1),
    ("Salt Roads", "Jonah Okafor", None, "Clara Penhallow", "Audiobook", 2),
    ("The Cartographer's Daughter", "Ines Valdré", None, None, "Ebook", 3),
    ("Night Ferry", "Theo Marchetti", "Harbour Lights, book 1", "Sam Oduya", "Audiobook", 4),
    ("A Small Weather", "Priya Castellane", None, "Ravi Lindqvist", "Audiobook and ebook", 5),
    ("The Orchard Clock", "Hollis Brant", None, None, "Ebook", 6),
    ("Bright Fathoms", "Ines Valdré", "Deepwater, book 1", "Clara Penhallow", "Audiobook", 7),
    ("The Ninth Lantern", "Rowan Ashby", "The Lantern Wars, book 1", "Ravi Lindqvist", "Audiobook", 8),
    ("Paper Kingdoms", "Lena Ostrova", None, None, "Ebook", 9),
    ("Hollow Pines", "Hollis Brant", None, "Sam Oduya", "Audiobook", 10),
    ("The Quiet Engine", "Dara Whitlock", None, None, "Ebook", 11),
    ("What the River Kept", "Priya Castellane", None, "Clara Penhallow", "Audiobook and ebook", 1),
    ("Ember and Ash Road", "Rowan Ashby", "The Lantern Wars, book 2", "Ravi Lindqvist", "Audiobook", 3),
    ("The Long Recess", "Dara Whitlock", None, None, "Ebook", 5),
    ("Moth Season", "Lena Ostrova", None, "Sam Oduya", "Audiobook", 7),
    ("Starling House Rules", "Felix Amari", None, None, "Ebook", 9),
    ("The Tidewright", "Mara Ellison", "The Glass Harbour, book 3", "Sam Oduya", "Audiobook", 2),
]


def book_panel(pid="panel-book", title="The Glass Harbour", n=0, status=("success", "In library · Audiobook and ebook"),
               foot=None, extra_body="", author="Mara Ellison", series="The Glass Harbour, book 1", narrator="Sam Oduya",
               blurb="A harbour town keeps its secrets in glass. When the lighthouse keeper vanishes, his niece finds the lamp still lit and a map that should not exist."):
    foot = foot or (
        '<a class="btn btn--primary" href="storyarr-book.html">Open book page</a>'
        f'<button class="btn" type="button">{ic("list-plus")}Add to list</button>'
        + menu(pid + "-more", "More actions for " + title,
               [("Follow " + author, "bookmark"), ("Open in Hardcover (opens in a new tab)", "external-link"),
                ("Open in Goodreads (opens in a new tab)", "external-link")],
               button_class="icon-btn", icon="ellipsis", aria_label="More actions for " + title)
    )
    body = f"""<div class="side-panel__lead">{cover(title, n)}<div style="display:grid;gap:8px;align-content:start"><h3 style="font-size:var(--text-lg)">{title}</h3><span class="chip" data-tone="{status[0]}">{status[1]}</span><span class="small muted">Read by {narrator} · 11 hr 42 min</span></div></div>
<dl class="facts"><dt>Author</dt><dd><a href="storyarr-author.html">{author}</a></dd>{f'<dt>Series</dt><dd><a href="storyarr-series.html">{series}</a></dd>' if series else ""}<dt>Narrated by</dt><dd><a href="storyarr-narrator.html">{narrator}</a></dd><dt>Published</dt><dd>21 September 2026</dd><dt>Length</dt><dd>11 hr 42 min · 412 pages</dd>{"<dt>In library</dt><dd>Fiction audiobooks, Fiction ebooks</dd>" if status[0] == "success" else ""}</dl>
<p>{blurb}</p>
{extra_body}"""
    return panel(pid, "Summary", body, foot)
