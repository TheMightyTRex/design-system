# TRex Design System

The design system for Storyarr and Starboard.

One design system for two self-hosted apps, so they look, read and behave as one family. It holds the
shared component library (tokens, components, behaviour and icons), the design rules, the content design
guide and the accessibility guide.

## The two apps that use it

- **[Storyarr](https://github.com/TheMightyTRex/storyarr):** follow authors and series and keep your
  audiobook library complete. Built with React; it wraps the library's classes in its own components.
- **[Starboard](https://github.com/TheMightyTRex/starboard):** an accessible dashboard for a home media
  server. Plain HTML and JavaScript; it uses the library as it is.

Each app keeps a copy of the library files, made by `tools/sync.py`, including the terminal frame and QR encoder. This repository is the source: never
change the copies inside the apps.

## What is in it

| Path | What it is |
|---|---|
| `palettes/` | Five more colour lists (Indigo, Forest, Plum, Ember, Graphite) for a new design or site: load one after `tokens.css` |
| `tokens.css` | Every colour, size, space and motion value as role names, for Light, Dark, High contrast and High contrast dark |
| `components.css` | Every component, in `@layer shared`, using only the tokens |
| `components.js` | The behaviour every component must have (menus, slide-outs, dialogs, phone menu, filter chips, copy, help, display settings), in plain JavaScript |
| `icons.svg` | Lucide icons as an SVG sprite (`<use href="#i-book-open">`); `tools/icons.txt` lists them |
| `fonts/` | Atkinson Hyperlegible Next, with its licence |
| `gallery.src.html`, `gallery.html` | The live gallery of every component (edit the `.src` file, then build) |
| `areas/` | Design boards for each area of both apps, built from the library. `index.html` is the Boards landing page; `index-starboard.html` and `index-storyarr.html` show each app's boards in the page, chosen from the menu, written by `areas/make_index.py` |
| `docs/LIBRARY.md` | The component reference: every class, the rule for slide-out, dialog or page, and how each app adopts the library |
| `docs/DESIGN-SYSTEM.md` | Principles, tokens, shell, page templates and consistency rules |
| `docs/COMPONENTS.md` | Storyarr's interface before the redesign, and the duplicates to merge |
| `docs/WIZARD.md` | Every job done in steps, in the browser and the terminal: one question per step, buttons, a job's progress, help in a slide-out, outside services, the Check table, feedback with Snaglist |
| `docs/TERMINAL.md` | How a wizard looks and behaves in a terminal: the frame, questions, the menu line, help boxes, job bars, plain mode for screen readers, and feedback as a QR code |
| `terminal/` | The terminal frame every app's terminal scripts use (`terminal-frame.sh`) and the QR code encoder for feedback (`qr.py`); `terminal/README.md` says how to use them |
| `docs/CONTENT-DESIGN.md` | How every word is written: voice, rules, words each app uses, status vocabulary, patterns |
| `docs/HELP-WRITING.md` | How help is written: tiers, kinds of topic, categories, layouts, screenshots |
| `docs/CHANGELOGS.md` | How every project keeps its changelog, after Keep a Changelog: Unreleased first, the six change types, links, withdrawn releases |
| `docs/ACCESSIBILITY.md` | The accessibility floor and how to test it |
| `docs/WCAG.md` | How the design system meets each point of WCAG 2.2 AA, after the GOV.UK Service Manual, and what each app must still do |
| `docs/ALT-TEXT.md` | How to write text descriptions (alt text) for every kind of image, after the BBC's guidance |
| `docs/SCREENSHOTS.md` | Screenshots in help: when one earns its place, made-up data only, the outline, arrow and step-number mark-up, and a short version for AI tools; `tools/annotate.js` draws and checks the mark-up |
| `penpot/` | The Penpot plugin that builds the design system in a Penpot file, and `tokens.json` for Penpot's Tokens panel, both made by `penpot/make.py` |
| `docs/PENPOT.md` | How to build, share and keep the Penpot file in step |
| `docs/SECURITY-CHECKS.md` | The security checks both apps run, how to sort what they find, and how to record the results and release notes |
| `resources/` | The Design resources and tools pages: what you can use, the tools, outside tools, how to make a change and how to get feedback |
| `tools/` | Build, contrast, icon, sync and privacy scripts |

## Look at the gallery

Open `gallery.html` in a browser; it needs no server and no build. The switches at the top change the
theme (Light, Dark, High contrast), the text size, wider spacing and reduced motion. Menus, slide-outs, the
phone menu and the dialog all work. The gallery is also published at
<https://themightytrex.github.io/design-system/gallery.html>.

The boards open the same way: start at `areas/index.html`, choose an app, then a board in the menu. Each board
shows in the page; Open on its own shows it in the whole window.

## Penpot

The design system can be built in [Penpot](https://penpot.app), the free and open-source design tool, by a plugin
made from this library: install `https://themightytrex.github.io/design-system/penpot/manifest.json` in Penpot's
plugin manager and select **Build the design system**. It adds the colours for all four themes, the text styles,
the icons and the main components to the file's library. Penpot's Tokens panel can import `penpot/tokens.json`.
Steps, sharing and connecting an AI assistant: [The design system in Penpot](docs/PENPOT.md).

## Design resources and tools

[Design resources and tools](https://themightytrex.github.io/design-system/resources/) lists everything here you can use, on five pages:

- [Overview](https://themightytrex.github.io/design-system/resources/): the gallery, tokens, palettes, icons, font, boards, guides and licences.
- [Tools in this repository](https://themightytrex.github.io/design-system/resources/tools.html): what each script does and the command that runs it.
- [Outside tools for accessibility and testing](https://themightytrex.github.io/design-system/resources/outside-tools.html): contrast checkers, automatic
  checks, screen readers, magnifiers and voice control.
- [Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html): the 10 steps from `git pull` to the change in both apps.
- [Get feedback](https://themightytrex.github.io/design-system/resources/get-feedback.html): testing with real people, automatic checks, and feedback in the
  product with [Snaglist](https://github.com/TheMightyTRex/snaglist).

The pages are in `resources/`. Change the bodies in `resources/content/`, then run
`python3 resources/make.py` and `python3 tools/build.py`.

The site's header, main menu (Components, Boards, Guides, Resources), phone menu and footer come from
`tools/sitepage.py`, used by the resources pages and the Boards pages. The gallery keeps its own copy, because
its header also has search: change both when the main menu changes.

## Change a component and sync it

In short: pull first, change the library here (never the copies in the apps), build the gallery, check
four themes and 175% text, run `tools/contrast.py` (0 failures), run `tools/check-private.sh`, commit, ask
before you push, then run `tools/sync.py` and commit in each app. Every step, with its command, is in
[Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html).

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
