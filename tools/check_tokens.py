"""Lists every custom property a style sheet uses that tokens.css does not have (DESIGN-SYSTEM.md, Names that are
not tokens). A name that is not a token falls back to whatever follows it, so the design system no longer decides.

Run: python3 tools/check_tokens.py [css files]   (components.css when none are given; an app passes its own,
such as ../starboard/web/css/*.css). Exits 1 when it finds one."""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent

# Names that look like tokens but are not, with the token to use.
NOT_TOKENS = {
    "--radius-1": "--radius", "--radius-2": "--radius", "--radius-3": "--radius", "--radius-control": "--radius",
    "--focus-width": "--focus-w", "--weight-normal": "--weight-regular", "--text-base": "--text-md",
}
# Set by a style or a page, not by tokens.css: a style's own choices, and values a page sets on one element.
SET_ELSEWHERE = {"--color-rail", "--font-heading", "--flow-w", "--logo", "--logo-ratio", "--shelf-arrow-top",
                 "--show-art-bg", "--show-art-fg", "--stages", "--sw-a", "--sw-b", "--type-colour", "--cover-w",
                 "--topic-tabs-h"}  # --topic-tabs-h: the page's script sets the height of the page topic tabs


def main(argv):
    files = [pathlib.Path(a) for a in argv] or [root / "components.css"]
    defined = set(re.findall(r"(--[\w-]+)\s*:", (root / "tokens.css").read_text(encoding="utf-8")))
    texts = {f: f.read_text(encoding="utf-8") for f in files}
    for text in texts.values():
        defined |= set(re.findall(r"(--[\w-]+)\s*:", text))
    found = 0
    for f, text in texts.items():
        for n, line in enumerate(text.splitlines(), 1):
            for name in re.findall(r"var\(\s*(--[\w-]+)", line):
                if name in NOT_TOKENS:
                    print(f"{f}:{n}: {name} is not a token; use {NOT_TOKENS[name]}")
                    found += 1
                elif name not in defined and name not in SET_ELSEWHERE:
                    print(f"{f}:{n}: {name} is not in tokens.css")
                    found += 1
    if found:
        print(f"\n{found} uses of names that are not tokens.")
        return 1
    print(f"Tokens: every name used in {len(files)} files is in tokens.css, or set by a style or a page.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
