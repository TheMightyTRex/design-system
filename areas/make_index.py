"""Write the Boards pages: the landing page (index.html) and Starboard's boards page (index-starboard.html), with the
site's menus (tools/sitepage.py). Starboard's overview comes from _starboard/_index.html.
Run: python3 areas/make_index.py, then python3 tools/build.py areas/index*.src.html

Storyarr was retired on 11 November 2026. Its boards, their generator and their index page are archived in
areas/archive/storyarr/ and are not rebuilt; make_index.py only counts them for the landing page."""
import pathlib, re, sys

here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "tools"))
import sitepage  # noqa: E402


def write_all():
    body = (here / "_starboard" / "_index.html").read_text().strip()
    counts = {"starboard": len(set(re.findall(r'href="starboard-([\w-]+)\.html"', body))),
              "storyarr": len(list((here / "archive" / "storyarr").glob("storyarr-*.src.html")))}
    out = sitepage.boards_page("starboard", body, date="2 November 2026", note="Made by areas/make_index.py")
    (here / "index-starboard.src.html").write_text(out)
    (here / "index.src.html").write_text(sitepage.boards_landing(counts))
    return ["index.src.html", "index-starboard.src.html"]


if __name__ == "__main__":
    for f in write_all():
        print("areas/" + f)
