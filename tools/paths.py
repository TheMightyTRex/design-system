"""Where the apps' checkouts are, for sync.py and icons.py.

Each path comes from, in order: an environment variable, tools/paths.local.json (not committed, so your
own folders stay out of the repository), or a default that assumes the apps sit next to this repository.

  STARBOARD_WEB    Starboard's web folder                         default ../starboard/web
  STALLBOARD_DS    Stallboard's assets/ds folder                  default ../stallboard/assets/ds
  PLUGINS_DIR      the plug-ins repository (starboard-plugins)    default ../starboard-plugins
  LUCIDE_ICONS     Lucide's icon modules (lucide-react)           default node_modules/lucide-react/dist/esm/icons here

paths.local.json uses the same names as keys, for example {"PLUGINS_DIR": "/path/to/starboard-plugins"}.
Storyarr (retired on 11 November 2026) is no longer synced, so STORYARR_SHARED is gone.
"""
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
_local = ROOT / "tools" / "paths.local.json"
_saved = json.loads(_local.read_text()) if _local.exists() else {}
_defaults = {
    "STARBOARD_WEB": ROOT.parent / "starboard/web",
    "STALLBOARD_DS": ROOT.parent / "stallboard/assets/ds",
    "PLUGINS_DIR": ROOT.parent / "starboard-plugins",
    "LUCIDE_ICONS": ROOT / "node_modules/lucide-react/dist/esm/icons",
}


def path(name):
    value = os.environ.get(name) or _saved.get(name)
    return pathlib.Path(value).expanduser() if value else _defaults[name]
