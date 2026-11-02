# Design system for Storyarr and Starboard

One design system for two self-hosted apps, so they look, read and behave as one family. It holds the
shared component library (tokens, components, behaviour and icons), the design rules, the content design
guide and the accessibility guide.

## The two apps that use it

- **[Storyarr](https://github.com/TheMightyTRex/storyarr):** follow authors and series and keep your
  audiobook library complete. Built with React; it wraps the library's classes in its own components.
- **[Starboard](https://github.com/TheMightyTRex/starboard):** an accessible dashboard for a home media
  server. Plain HTML and JavaScript; it uses the library as it is.

Each app keeps a copy of the library files, made by `tools/sync.py`. This repository is the source: never
change the copies inside the apps.

## What is in it

| Path | What it is |
|---|---|
| `tokens.css` | Every colour, size, space and motion value as role names, for Light, Dark, High contrast and High contrast dark |
| `components.css` | Every component, in `@layer shared`, using only the tokens |
| `components.js` | The behaviour every component must have (menus, slide-outs, dialogs, phone menu, filter chips, copy, help, display settings), in plain JavaScript |
| `icons.svg` | Lucide icons as an SVG sprite (`<use href="#i-book-open">`); `tools/icons.txt` lists them |
| `fonts/` | Atkinson Hyperlegible Next, with its licence |
| `gallery.src.html`, `gallery.html` | The live gallery of every component (edit the `.src` file, then build) |
| `areas/` | Design boards for each area of both apps, built from the library (`index-storyarr.html`, `index-starboard.html`) |
| `docs/LIBRARY.md` | The component reference: every class, the rule for slide-out, dialog or page, and how each app adopts the library |
| `docs/DESIGN-SYSTEM.md` | Principles, tokens, shell, page templates and consistency rules |
| `docs/COMPONENTS.md` | Storyarr's interface before the redesign, and the duplicates to merge |
| `docs/CONTENT-DESIGN.md` | How every word is written: voice, rules, status vocabulary |
| `docs/ACCESSIBILITY.md` | The accessibility floor and how to test it |
| `tools/` | Build, contrast, icon, sync and privacy scripts |

## Look at the gallery

Open `gallery.html` in a browser; it needs no server and no build. The switches at the top change the
theme (Light, Dark, High contrast), the text size, wider spacing and reduced motion. Menus, slide-outs, the
phone menu and the dialog all work. The gallery is also published at
<https://themightytrex.github.io/design-system/gallery.html>.

The area boards open the same way: start at `areas/index-storyarr.html` or `areas/index-starboard.html`.

## Change a component and sync it

You need Python 3 and checkouts of Storyarr and Starboard.

1. Pull first, so you start from the latest library: `git pull`.
2. Change `tokens.css`, `components.css`, `components.js` or `icons.svg`. To add an icon, add its Lucide
   name to `tools/icons.txt` and run `python3 tools/icons.py "$(tr '\n' ' ' < tools/icons.txt)"`.
3. Rebuild the gallery and the area boards: `python3 tools/build.py`. Check the gallery in all four themes
   and at 175% text.
4. Check contrast: `python3 tools/contrast.py > contrast-report.txt`. It must end with `0 failures`.
5. Tell `tools/sync.py` where the apps are, once. By default it looks for `../starboard` and `../storyarr`
   next to this repository. To use other folders, set `STARBOARD_WEB` and `STORYARR_SHARED`, or copy them
   into `tools/paths.local.json`, which git ignores:

   ```json
   {
     "STARBOARD_WEB": "~/src/starboard/web",
     "STORYARR_SHARED": "~/src/storyarr/apps/web/src/shared"
   }
   ```

6. Preview the copy with `python3 tools/sync.py --check`, then run `python3 tools/sync.py`. It writes the
   library into Starboard (`web/css`, `web/js`, `web/icons`) and Storyarr (`apps/web/src/shared/`). It does
   not commit.
7. Commit and push here, then commit in each app, rebuild it and test it.

`tools/install-hooks.sh` adds a pre-commit check that stops private details (home network addresses, email
addresses, keys and the words in your own `.private-words` file) from being committed.

## Accessibility floor

Everything here meets **WCAG 2.2 level AA** in every theme. In practice:

- 4.5:1 contrast for text and 3:1 for control borders and the focus ring, measured by `tools/contrast.py`.
- 44px controls and targets, and a visible 3px focus ring.
- Status in words plus a shape or an icon, never colour alone.
- Keyboard first: slide-outs and dialogs are named, keep focus inside, close with Escape and return focus.
- Everything works at 175% text and with wider spacing; nothing moves when reduced motion is on.

`docs/ACCESSIBILITY.md` has the full checklist and how to test each item.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Every word follows the [content design guide](docs/CONTENT-DESIGN.md).

## Licences

- Code (CSS, JavaScript, HTML and tools): [MIT](LICENSE).
- Guides and documentation (`docs/` and the Markdown files): [CC BY 4.0](LICENSE-DOCS.md).
- Font: Atkinson Hyperlegible Next, [SIL Open Font License 1.1](fonts/LICENSE-OFL.txt).
- Icons: [Lucide](https://lucide.dev), [ISC licence](licences/LUCIDE-ISC.txt); some Lucide icons come from
  Feather (MIT, in the same file).
