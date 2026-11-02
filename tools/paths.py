"""Where the apps' checkouts are, for sync.py and icons.py.

Each path comes from, in order: an environment variable, tools/paths.local.json (not committed, so your
own folders stay out of the repository), or a default that assumes the apps sit next to this repository.

  STARBOARD_WEB    Starboard's web folder        default ../starboard/web
  STORYARR_SHARED  Storyarr's shared folder      default ../storyarr/apps/web/src/shared
  LUCIDE_ICONS     Lucide's icon modules         default ../storyarr/apps/web/node_modules/lucide-react/dist/esm/icons

paths.local.json uses the same names as keys, for example {"STORYARR_SHARED": "/path/to/storyarr/apps/web/src/shared"}.
"""
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
_local = ROOT / "tools" / "paths.local.json"
_saved = json.loads(_local.read_text()) if _local.exists() else {}
_defaults = {
    "STARBOARD_WEB": ROOT.parent / "starboard/web",
    "STORYARR_SHARED": ROOT.parent / "storyarr/apps/web/src/shared",
    "LUCIDE_ICONS": ROOT.parent / "storyarr/apps/web/node_modules/lucide-react/dist/esm/icons",
}


def path(name):
    value = os.environ.get(name) or _saved.get(name)
    return pathlib.Path(value).expanduser() if value else _defaults[name]
