# Changelog

All notable changes to the TRex Design System are listed here, newest first. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with dates written as in this design system
(`docs/CHANGELOGS.md`). The design system has no numbered versions yet, so every change since the first
commit on 2 November 2026 is under Unreleased. Once versions are tagged, they will follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- **Adverts that take turns in the help centre** (8 November 2026): `help-centre.json` takes `banners`, a list of up to six, as well as `banner`. Each page shows one and the next page shows the next, chosen before the page draws so it never flashes; nothing changes while a page is open. Each keeps its own label, and the one Hide button hides them all.
- **A to Z jump list** (8 November 2026): `.az-jump` over a long wall of covers, # then A to Z from the sort title ("The Expanse" under E, accents folded). Letters with nothing are shown but cannot be chosen and say so to screen readers; the row sticks under the header, keeps the letter in view marked with a bar, has 44px targets and one Tab stop (Arrow keys, Home, End), moves focus to the letter's heading (`.wall-letter`) after a jump, and scrolls sideways on phones. `components.js` adds `azLetter`, `azJump` and `azGo`, and an `az-jump` event for walls that show 40 at a time. In the gallery under Containers.
- **Terminal in the main design system** (7 November 2026): `terminal/` holds the terminal frame (`terminal-frame.sh`) and the QR encoder (`qr.py`) every app's terminal scripts use, copied by `tools/sync.py` (Starboard: `lib/terminal-frame.sh`, Run first's copy and `starboard/qr.py`); the frame takes the app's name, issue address and own feedback flow as settings. `DESIGN-SYSTEM.md` has a Terminal chapter, the README lists `WIZARD.md`, `TERMINAL.md` and `terminal/`, `TERMINAL.md` says step by step how the feedback QR code is made, and the gallery draws a question, a job bar, help, plain mode and a real QR code.
- **Two square help icons** (7 November 2026): `help` for help that opens in a slide-out and `help-new-tab` for help that opens in a new tab. In-page help is always a link that opens a slide-out, never a fold-out or a dialog.
- **Wizard pieces in the gallery** (7 November 2026): choosing an outside service, required fields, a job bar with its count and the Check table; `WIZARD.md` and `TERMINAL.md` say where a step's help goes, how a job shows its count and how the Check step looks.
- **Tidier tables** (7 November 2026): row headings look like their cells, in bold; `.table--middle` lines every cell up on the middle for a summary with Change buttons.
- **New-tab links** (7 November 2026): every link that opens a new tab shows the `external-link` icon after its words.
- **Required fields** (7 November 2026): a * after the label (`.field__required`); the key, "* = Required" (`.required-key`), at the bottom of the help slide-out, not in the form.
- **Slide-out widths** (7 November 2026): about half the screen for release notes and help (`.side-panel--wide`), about a third for every other slide-out.
- **Where buttons sit** (7 November 2026): on the left, the main action first, in dialogs, slide-outs and wizards; danger and Skip apart on the right.
- **Help centre.** `tools/help_centre/build.py` builds an app's Markdown help into web pages with this design
  system: search, a collapsible menu of every article on the left (it can be hidden), On this page following the
  article on the right with the section being read marked, Display and accessibility, and on phones one header bar
  with search and the menu as icons, an optional banner and footer note, and wide tables the keyboard can scroll.
  Each app keeps a `help-centre.json`; `build.sh` runs it in a container. `docs/LIBRARY.md`, Help centre, sets
  out the layout and its accessibility (7 November 2026).
- **Screenshots in help.** `docs/SCREENSHOTS.md`: a picture only for a step the words cannot carry, made-up data
  only (masking checked both ways, never blur alone, never a faked screen), settle times, a red outline 5px
  outside the control with a curved arrow and a filled head, at most three per picture, each badged with its step
  number in the article, text descriptions, checks before publishing, and a short version to give AI tools.
  `tools/annotate.js` draws the mark-up from the page's own elements and checks it before capture
  (7 November 2026).
- **Releases as accordions.** `.disclosure.release` with `.release__counts` and `.release__type`: each release in its
  own accordion, the installed one open, a count chip for each type of change and a bar in that type's colour.
  `docs/LIBRARY.md` also sets Settings, Updates as three pages (Update settings, Releases, Restore) and Sign out
  beside every Settings page title (5 November 2026).
- **Help goes to the page's own article.** `docs/LIBRARY.md`, Header: the Help button opens the help centre article
  for the page you are on, or the help index's section when no one article covers it, with hidden text naming the
  subject. Each app keeps one list of pages and articles, and its build stops if a page has none or an article is
  missing (5 November 2026).
- **The version in the side menu.** `.rail__version` at the bottom of the rail, in plain text; the footer gains
  Release notes and loses the version (5 November 2026).
- **Progress bars, a column, and multiple choice.** `docs/WIZARD.md` section 5, A job's progress: one bar per job,
  drawn once and updated in place, errors below it with Try again, Show the details or Stop. `docs/TERMINAL.md`:
  a column at most 100 characters wide, centred in a wider window, text wrapped again at any size, and multiple
  choice with the arrow keys and Space in the boxed way (5 November 2026).
- **Symbols that move between keyboards.** `docs/HELP-WRITING.md` section 7, rule 4: a command with `|`, `~`, `\`,
  `"`, `@`, `$` or `&` links to keyboard help for US, UK and Ireland, German, French and Spanish keyboards, and a
  one-line command with `|` also shows a version without it (5 November 2026).
- **One wizard, two ways to show it.** `docs/WIZARD.md` section 2: an app's browser and terminal set-ups ask the
  same questions in the same order, with the same answers, defaults and help, and change together; both start with
  "How do you want to start?", including "Already installed". A run first script hands over what it found and
  decides nothing. A new check in section 13; `docs/TERMINAL.md` section 1 points to it (5 November 2026).
- **A run first script, and the logo in a terminal.** `docs/TERMINAL.md` section 9: after the operating system is
  installed, one script sets up everything else. It asks about accessible mode first, in plain words, and passes it
  on; checks, then asks, then installs only what is missing; opens the browser wizard on a desktop or the terminal
  wizard without one. The logo is drawn in block characters in the boxed way only. Checks are now section 10
  (5 November 2026).
- **Terminal wizards fit the window.** `docs/TERMINAL.md` section 2: the heading box, progress bar and menu stay in
  place and only the lines between them scroll; the window is measured at every step and when it changes size. The
  feedback QR code holds more of the report the larger the window is, in four tiers, down to the title alone in
  80 by 24 (5 November 2026).
- **Terminal wizards.** `docs/TERMINAL.md` sets how a wizard looks in a terminal: boxed and plain ways to draw
  it, the heading box, a menu on the bottom line with Back, Help, Feedback and Stop, help over the step, and
  feedback sent as a QR code that fits the window (5 November 2026).
- **Feedback in every wizard.** `docs/WIZARD.md` section 12: Snaglist on every step, each report naming its
  step, and Show as a QR code for a computer that is not online yet (5 November 2026).
- **Changelog rules.** `docs/CHANGELOGS.md` sets how every project keeps its changelog, after Keep a
  Changelog 1.1.0, and this changelog follows it (5 November 2026).
- **Tables that line up.** `.table--fixed` with named column widths keeps the columns of several tables in
  line (4 November 2026).
- **Search is always one button away.** A search button first in the rail, and in the header on phones,
  opening the same search box (4 November 2026).
- **Wizard rules.** `docs/WIZARD.md` sets one set of rules for every wizard: one question per step, a step bar
  numbered 1, 2, 3 that shows only the numbers on phones, and help in a slide-out that asks only what the app
  can show (4 November 2026).
- **WCAG 2.2 and text descriptions.** `docs/WCAG.md` shows how each WCAG 2.2 AA point is met and what each
  app must still do; `docs/ALT-TEXT.md` sets how to write text descriptions for every kind of image
  (4 November 2026).
- **Starboard menu boards.** Design boards for the side menu, Library sub-menus, System and Clean up, the
  server name and the menu names (4 November 2026).
- **Penpot plugin.** A plugin that builds the colours, text styles, icons and main components into a Penpot
  file, with `penpot/tokens.json` for Penpot's Tokens panel. Steps are in `docs/PENPOT.md` (3 November 2026).
- **Security checks guide.** `docs/SECURITY-CHECKS.md` sets the same checks, sorting of findings and reporting
  in both apps (3 November 2026).
- **Design resources and tools pages,** and introductions to the writing guides (3 November 2026).
- **Boards landing page.** Boards are one main menu item, with each app's boards shown in the page
  (3 November 2026).
- **Content design and help writing.** `docs/CONTENT-DESIGN.md` for every word in both apps,
  `docs/HELP-WRITING.md` for help, and the callout and prose components (3 November 2026).
- **Toasts and saved notes.** Success, information, warning and error toasts, and a saved note beside the button
  on settings pages, with icons from the app's own sprite file (3 November 2026).
- **Five colour palettes** for new designs (3 November 2026).
- **UX notes for testing.** A Note an issue button on every page while an app's testing setting is active
  (2 November 2026).
- **The shared design system:** tokens, components, behaviour, icons, the gallery and the guides, one source
  for Storyarr and Starboard (2 November 2026).

### Changed
- **Release notes** in both apps use the six change types of the changelog rules: Added, Changed, Deprecated,
  Removed, Fixed and Security (5 November 2026).
- **Wizard help** opens in a slide-out, not a dialog (4 November 2026).
- **The gallery** has the apps' header, a logo and a footer (3 November 2026).
- **Scroll bars** are thin and square, in the border colour on a clear track (2 November 2026).
- **App logos** show without a tile; apps without a logo keep their initials on a tile (2 November 2026).
- **Slide-out headers** are in the page colour, and Display and accessibility is a slide-out
  (2 November 2026).

### Fixed
- **Terminal frame** (7 November 2026): a long question wraps between words with the answer's line last; plain-mode answers wrap with their indent; with no questions to ask (--yes) a real window still gets the boxed frame, its menu showing only Ctrl+C (`TTY`).
- **Meter words** (7 November 2026): the timer and count on the right of a meter stay on one line; `.nowrap` added to the utilities.
- **Segmented switch** (7 November 2026): no gap between its buttons when it is a fieldset, and the buttons keep their width when the choice changes.
- **Focus is not hidden** by the sticky header or the save bar when the page scrolls (WCAG 2.4.11,
  4 November 2026).
- **Penpot plugin** opens without "Something wrong has happened", uses layout sizes Penpot accepts and
  layer names without "/", and shows its build number (3 November 2026).
- **UX notes:** the list button has a name before the count loads (3 November 2026).
- **Logo editor:** found files show as plain pictures, with a drawing cursor on the cut-out (2 November 2026).

### Security
- **Privacy check.** A pre-commit check stops private names, addresses and keys reaching this public
  repository; a private word is let through only inside a public name (3 November 2026).

[Unreleased]: https://github.com/TheMightyTRex/design-system/commits/main
