"""Write the Boards pages: the landing page (index.html) and each app's boards page (index-starboard.html,
index-storyarr.html), with the site's menus (tools/sitepage.py). Storyarr's overview comes from
storyarr-gen/b_index.py, Starboard's from _starboard/_index.html.
Run: python3 areas/make_index.py, then python3 tools/build.py areas/index*.src.html"""
import pathlib, re, sys

here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "tools"))
sys.path.insert(0, str(here / "storyarr-gen"))
import sitepage  # noqa: E402


def write_all():
    import b_index
    bodies = {
        "starboard": (here / "_starboard" / "_index.html").read_text().strip(),
        "storyarr": b_index.body(),
    }
    counts = {}
    for app, body in bodies.items():
        counts[app] = len(set(re.findall(rf'href="{app}-([\w-]+)\.html"', body)))
        out = sitepage.boards_page(app, body, date="2 November 2026",
                                   note=f"Made by areas/make_index.py")
        (here / f"index-{app}.src.html").write_text(out)
    (here / "index.src.html").write_text(sitepage.boards_landing(counts))
    return ["index.src.html", "index-starboard.src.html", "index-storyarr.src.html"]


if __name__ == "__main__":
    for f in write_all():
        print("areas/" + f)
