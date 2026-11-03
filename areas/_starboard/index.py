"""Write the Starboard boards index: areas/index-starboard.src.html from _index.html, with the site's header,
menus and a left menu of every board (tools/sitepage.py). Run: python3 areas/_starboard/index.py, then
python3 tools/build.py areas/index-starboard.src.html"""
import pathlib, sys

here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent / "tools"))
import sitepage  # noqa: E402

body = (here / "_index.html").read_text().strip()
html = sitepage.page(root="../", main="boards", current="areas/index-starboard.html", title="Starboard boards",
                     body=body, side=sitepage.side_from_body(body, "Starboard boards"),
                     note="Made by areas/_starboard/index.py from areas/_starboard/_index.html")
(here.parent / "index-starboard.src.html").write_text(html)
print("areas/index-starboard.src.html")
