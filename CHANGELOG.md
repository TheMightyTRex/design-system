# Changelog

All notable changes to the TRex Design System are listed here, newest first. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with dates written as in this design system
(`docs/CHANGELOGS.md`). The design system has no numbered versions yet, so every change since the first
commit on 2 November 2026 is under Unreleased. Once versions are tagged, they will follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
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
