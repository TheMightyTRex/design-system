# Changelog

All notable changes to the TRex Design System are listed here, newest first. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with dates written as in this design system
(`docs/CHANGELOGS.md`). The design system has no numbered versions yet, so every change since the first
commit on 2 November 2026 is under Unreleased. Once versions are tagged, they will follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- **Help centre.** `tools/help_centre/build.py` builds an app's Markdown help into web pages with this design
  system: search, a collapsible menu of every article on the left (it can be hidden), On this page following the
  article on the right with the section being read marked, Display and accessibility, and on phones one header bar
  with search and the menu as icons. Each app keeps a `help-centre.json`; `build.sh` runs it in a container
  (7 November 2026).
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
