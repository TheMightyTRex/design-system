#!/usr/bin/env python3
"""Checks every text and control colour pair in tokens.css against WCAG 2.2 AA in all four themes.

Run: python3 tools/contrast.py > contrast-report.txt   (exit code 1 if any pair fails)
"""
import pathlib
import re
import sys

TOKENS = (pathlib.Path(__file__).resolve().parent.parent / "tokens.css").read_text()


def block(selector_regex):
    m = re.search(selector_regex + r"\s*\{(.*?)\n\s*\}", TOKENS, re.S)
    return dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6})", m.group(1)))


light = dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6})", TOKENS.split("color-scheme: light;")[0]))
dark = {**light, **block(r':root\[data-theme="dark"\]')}
hc = {**light, **block(r":root\.pref-contrast")}
hcd = {**dark, **hc, **block(r':root\.pref-contrast\[data-theme="dark"\],\s*:root\.pref-contrast\.is-dark')}
THEMES = [("Light", light), ("Dark", dark), ("High contrast", hc), ("High contrast dark", hcd)]


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


PAIRS = [
    ("color-text", "color-bg", 4.5), ("color-text", "color-surface", 4.5), ("color-text", "color-surface-raised", 4.5),
    ("color-text-muted", "color-bg", 4.5), ("color-text-muted", "color-surface", 4.5),
    ("color-text-muted", "color-surface-raised", 4.5), ("color-text-muted", "color-surface-sunken", 4.5),
    ("color-accent", "color-bg", 4.5), ("color-accent", "color-surface", 4.5), ("color-accent", "color-surface-raised", 4.5),
    ("color-accent-text", "color-accent", 4.5), ("color-text", "color-accent-soft", 4.5), ("color-accent", "color-accent-soft", 4.5),
    ("color-count-text", "color-count", 4.5),
    ("color-border", "color-surface-raised", 3), ("color-border", "color-bg", 3),
    ("color-focus", "color-bg", 3), ("color-focus", "color-surface-raised", 3),
    ("color-text", "color-header", 4.5), ("color-text-muted", "color-header", 4.5),
]
TONES = ["success", "info", "neutral", "warning", "danger", "muted"]

fails = 0
for name, t in THEMES:
    print(f"\n{name}")
    for fg, bg, need in PAIRS:
        if fg not in t or bg not in t:
            continue
        r = ratio(t[fg], t[bg])
        ok = r >= need
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} {fg[6:] if fg.startswith('color-') else fg} on {bg[6:]}: {r:.2f} (needs {need})")
    for tone in TONES:
        fg = t[f"status-{tone}-fg"]
        # Chip style B: tone text and border on the surface and on raised surfaces; notices use the tint.
        for bg_name in ("color-surface", "color-surface-raised", f"status-{tone}-bg"):
            r = ratio(fg, t[bg_name])
            ok = r >= 4.5
            fails += not ok
            print(f"  {'ok  ' if ok else 'FAIL'} status {tone} on {bg_name.replace('color-', '')}: {r:.2f} (needs 4.5)")
print(f"\n{fails} failures")
sys.exit(1 if fails else 0)
