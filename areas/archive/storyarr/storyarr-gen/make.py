"""Write every Storyarr board: python3 areas/storyarr-gen/make.py [module ...]"""
import sys, importlib, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
mods = sys.argv[1:] or ["b_library", "b_items", "b_discover", "b_activity", "b_settings", "b_wizards", "b_index"]
for m in mods:
    for f in importlib.import_module(m).build():
        print(f)
