# Changelog

All notable changes to the TRex Design System are listed here, newest first. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with dates written as in this design system
(`docs/CHANGELOGS.md`). The design system has no numbered versions yet, so every change since the first
commit on 2 November 2026 is under Unreleased. Once versions are tagged, they will follow
[Semantic Versioning](https://semver.org/).


## 27 November 2026

- **One accessibility guide.** `docs/ACCESSIBILITY.md` (version 2.0) now holds everything the design system says about accessibility in one place: what we promise, how the checks fit together, the gate before a change is called done, 20 topic sections (keyboard and focus, reading and focus order, names and labels with Label in Name 2.5.3, target size with the 44, 32 and 24 pixel sizes, colour and contrast, forms, dialogs, menus and tabs, wizards, tables, charts, live regions, images, motion, zoom, forced colours, plain English, voice control, switch access and touch), each with its WCAG numbers, a do and a do not, the component page that shows it and the check that proves it. It has exact manual steps for Windows Voice Access, Dragon and macOS and iOS Voice Control, every check with its command and what an AI cannot verify, and the standing rules. Checks being built in Starboard are named and marked in progress: the Label in Name check, the per-control target size confirmation, wizard keyboard tasks with a coverage checker, `tools/done-check.sh` and a light GitHub accessibility job. Every rule of the old guide is kept. `docs/AI-CHECKS.md` (voice control and touch rows) and `docs/WCAG.md` point to it and match it.
- **The hover outline of a page topic tab meets the rule under the tabs (Starboard issue #366).** The outline was an inset box-shadow, which stops at the padding box, so its lower edge sat 3px above the line under the tabs. It is now a 1px border on a pseudo-element over the whole tab, in the four themes; the tab keeps its size, the selected tab keeps its underline, and the focus ring is unchanged.
- **A printer icon.** `printer` joins the sprite (Lucide, ISC licence) for Print buttons, such as printing a page of sign-in details. It is listed in `tools/icons.txt` and shown in the icon row of Type, space and icons. No CSS or script changed, so `tools/sync.py` changes only Starboard's sprite.

## 26 November 2026

- **The unused cover card, cover actions and book row are removed.** `.cover-card*`, `.cover-actions*` and `.book-row*` (about 340 lines, built for Storyarr) were used by no app, plug-in, Stallboard or help centre; the Cover actions gallery section is gone and the Shelf demo uses plain media cards.
- **A progress bar builder (Starboard patterns audit):** `SharedComponents.progress(options)` and `setProgress(bar, value)` draw a `.progress` with the right role: `progressbar` with a value, the busy band with `aria-valuetext`, `img` for how full something is, or hidden when words beside it say the same. Starboard had 24 hand-built bars in four accessibility shapes.
- **An AI-triggered Accessibility check (DASH-606).** `docs/AI-CHECKS.md` is a new guide that says what an AI-triggered check is and sets out the Accessibility check in full, with a report template to download and a prompt to copy; it appears in the guides and in site search.
- **Every 2nd level menu row condenses like the plug-in tabs.** When the names do not fit (measured, so large text, spacing and translations count), `.site-header__tabs .menu-tabs.is-compact` shows icons only at 44px each, keeps the name of the current tab and the tab with focus, gives the others a `data-tooltip` (it replaces the `title`), moves between tabs with the arrow keys, Home and End, scrolls the current tab into view and fades the edge with more tabs. `.menu-tabs--scroll` goes: its rule is now the rule of every row. The 1st level row is unchanged.
- **Counts and clock times in words (Starboard patterns audit):** `SharedComponents.plural(n, one, many)`, `SharedComponents.clock(date)` and `SharedComponents.num(n)`. Starboard had eight copies of `plural` in four shapes and three of the clock.
- **A waiting mark builder (Starboard patterns audit):** `SharedComponents.wait(words)` returns the `.wait` line, the ring and the words, so a page does not write a plain "Loading…". Starboard had 21 of them and no use of `.wait`.
- **A notice builder (Starboard patterns audit):** `SharedComponents.notice(tone, title, text, options)` draws a `.notice` with one icon for each tone and `role="status"` unless the error blocks. Starboard had ten copies of it with nine different bodies.
- **Four more styles-only parts (Starboard patterns audit):** the styles of components that no page of Starboard, its plug-ins, Stallboard or Snaglist uses (split button, applied filters, timeline, shelf, the logo picker, the wizard review aids and more, 591 lines) are the parts `extras`, `media-extras`, `logo-picker` and `wizard-review`. An app with a parts folder no longer loads them. The gallery and the help centre load them as before. `tools/parts.py` accepts a part that is marked in more than one place.
- **A status word for a plug-in that cannot run: Needs an update.** The status table in `docs/CONTENT-DESIGN.md` section 6 has it, with the warning tone and shape, and what it means.
- **A 2nd level menu can scroll with a 44px tab for each icon.** `.menu-tabs--scroll` keeps every icons-only tab 44px wide and shows the name of the current tab and the tab with focus, `components.js` gives icons-only tabs their name as a tooltip, and `icons.svg` has two new icons, `image` and `palette`.
- **Demos no longer stick over the site's header.** The topic tabs, the A to Z list, the save bar and table heads stick under the app's header in the apps, but inside a component page's demo they now stay still; `tools/check_demos.mjs` checks every page at 375, 800 and 1280 px in four themes for sticky or fixed parts and overlaps.
- **A Tokens page, made from `tokens.css`.** It lists every token with its value in Light, Dark, High contrast and High contrast dark, so it cannot drift from the file.
- **`docs/COMPONENTS.md` describes Starboard as it is.** It keeps the components by area and replaces the old Storyarr inventory with a table of Starboard's screens and the library parts each uses.
- **One table of status words.** `docs/CONTENT-DESIGN.md` section 6 now lists the 100 or so chip words Starboard uses, with tone and meaning, in place of Storyarr's ten, and section 5 has the new terms (plug-in, media server, place, Check now).
- **`docs/WIZARD.md` has a section for a wizard in a slide-out.** `docs/LIBRARY.md` documents the 17 `SharedComponents` functions that had no entry.
- **14 new Starboard boards from the real screens.** Dashboard, Updates, Busy now, Bring in, Backup and restore with places, Media server, Plug-ins, General (Alerts), Library, Discover, Wanted, Requests, History and Logs were captured from Starboard 0.31 on an example server with made-up data and rebuilt from the shared library.
- **Starboard's own patterns are in the library.** Page topics (`.topic-tabs`, `.settings-sections`), the update list, places and service logos, the dashboard grid and cards, show once, a wizard in a slide-out, and folding sections have classes, gallery entries (App patterns) and a section in `docs/LIBRARY.md`.
- **Styles-only parts.** `tools/parts.py` and `tools/sync.py` can make a part that has styles and no script; six patterns use it, so an app loads each only on the pages that use it.
- **The media library is a styles-only part too.** Walls of covers, groups, network and collection cards, episode rows and Discover's shelves are Starboard's `library.css`, word for word, as the `media-library` part.
- **`service-logos.svg`** holds the Google Drive, OneDrive, Dropbox, Backblaze B2, Amazon S3 and WebDAV marks (CC0 artwork from simpleicons.org), and `tools/sync.py` copies it to Starboard as `icons/services.svg`.
- **Storyarr's boards are archived.** The 19 boards, their generator and their index page moved to `areas/archive/storyarr/`, and each old address under `areas/` is now a small page that sends visitors there.
- **Storyarr is no longer synced or named as a live app.** `tools/sync.py` and `tools/paths.py` drop it, the guides, README and gallery examples now speak of Starboard, its plug-ins and Stallboard, and `docs/SECURITY-CHECKS.md` has no Storyarr column.
- **`tools/sync.py` also copies the library into Stallboard and the two plug-ins that keep their own copy.** It covers `tv-station/ds-tokens.css` and `outside-services/ds.css`, and `--check` now exits with 1 when a copy differs.
- **The standard word is Check now (owner, 26 November 2026).** The guides, gallery and Starboard boards say Check now, with no Check again before or after a first check.
- **The tokens and classes Starboard used without a definition now exist.** They are `--radius-sm`, `--radius-md`, `--font-mono`, `--color-success-text`, `--color-danger-text`, `.stack-3`, `.stack-5`, `.input--narrow`, `.select--compact`, `.field__error` and `.btn--secondary`.
- **The guides index builds the same page every time.** Its section ids come from the group name, not a random number, so a rebuild no longer changes the file.

- **The content guide follows the Plain English Campaign.** Rules 2.12, 2.14 and 2.15 now ask for an average sentence of 15 to 20 words and none over 25, plain words, and an explanation of technical words. New rules 2.25 to 2.27 cover hidden verbs, reading level (grade 6, or 8 for developer pages and changelogs) and word targets as warnings. `docs/CHANGELOGS.md` asks for one sentence per entry.
- **A Plain English check, warn only.** `tools/verbose-check.py ci` warns about the lines a pull request adds, and `tools/sync.py` copies it into Starboard. It fails on nothing yet; the failing part, for a sentence over 25 words or a paragraph over 4 sentences, waits until a repository has fewer than 100 long sentences.
- **Plainer wording (DASH-593):** the README, the guides in `docs/` and the resources pages now have shorter sentences, with no change in meaning.

## 23 November 2026

- **The help centre follows Remove drop shadows (Starboard DASH-536):** the help centre builder now has the Remove drop shadows switch.
- **Remove drop shadows (Starboard DASH-536):** `data-shadows="off"` sets the shadow tokens to none, so cards, covers, menus, slide-outs and dialogs lose their shadow but keep their border.
- **Covers take the card shading (DASH-535):** every `.cover` now has the card's 1px border, 6px corner and layered shadow.

## 22 November 2026

- **A Discord support server link in the footer (DASH-526):** an app with a Discord support server links to it after Help, and the help centre builder adds it to every page footer when `help-centre.json` names the server in `discord`.
- **Parts (Starboard DASH-507):** an app can load twelve of the large components only on the pages that use them, which saves about 22 KB a page, and `docs/LIBRARY.md`, Parts, has the rules.

## 20 November 2026

- **Words from an app never go into HTML unescaped (CodeQL, 20 November 2026).** The secret field's hidden name, the pagination noun and link, and the error summary's links are now set as text or escaped, so a name with HTML in it shows as words.
- **Rose in Dark had dark blue text on its dark page.** Its dark blue ink is set for Light only, and the Light rule
  also applies in Dark, so Dark now sets the text back to white. A colour any palette sets in Light only now goes back
  to the dark neutral in Dark, so this cannot happen again (found in Starboard).
- **Thirteen components that were missing.** Each has a gallery section (an example, when to use it, when not to,
  and its accessibility) and an entry in `docs/LIBRARY.md`. All are plain JavaScript in `components.js`, wait until
  they are on the page, and listen to the page only while open.
  - **Log viewer** (`.log-view`): monospace lines with a level filter, search that marks each match, follow new
    lines with pause (scrolling up pauses it), wrap and download. It keeps the newest 10,000 lines and draws only the
    newest 1,000 that match, adding new lines on their own. New errors are said politely, only while following.
  - **Tabs** (`.tabs`): in-page tabs by the ARIA tabs pattern, with arrow keys, Home and End, and automatic or
    manual activation, as `DESIGN-SYSTEM.md` section 5 asks. Every panel shows without script.
  - **Combobox** (`.combobox`): a searchable select by ARIA 1.2, with the match underlined, "No languages match"
    and the number found said politely.
  - **Sparkline and gauge** (`svg.sparkline`, `.gauge`) for stat tiles, from the chart tokens, with the numbers in
    words beside them.
  - **Pagination** (`.pagination`): page links, "Showing 21 to 40 of 312" and rows per page.
  - **Error summary** (`.error-summary`), after GOV.UK: focused after a failed submit, with a link to each field, and
    `showErrors()` writes each field's `.field-error` too.
  - **Secret field** (`.secret-field`): Show and Hide, Copy and Replace, each said politely; the value is never put
    in an attribute, a message or the console.
  - **Schedule picker** (`.schedule`): repeat, days and time, read back in words ("Every weekday at 07:00") with the
    next time it runs.
  - **Tag input** (`.tag-input`): Enter or a comma adds, a Remove button on each, both said politely.
  - **Popover and alerts centre** (`.popover`, `.alerts`): a small layer from a button that is not a menu, and the
    header's Alerts with unread alerts, Mark as read and Mark all as read.
  - **Page banner** (`.page-banner`, `pageBanner()`): one message for the whole app under the header, such as
    Connection lost or Restart needed.
  - **Tooltip** (`data-tooltip`): on hover and keyboard focus, closed with Escape, and the pointer can move onto it
    (WCAG 1.4.13). Status icons now use it, with `tabindex="0"`, instead of a `title` that keyboards cannot reach.
  - **Command palette** (Ctrl+K, `[data-command-palette]`): find a page or action by name; it reuses the combobox,
    always has a button, and `data-no-shortcut` takes the shortcut away.
- **`docs/COMPONENTS.md`** now opens with the current components by area and marks the Storyarr inventory under it
  as a record from 1 November 2026, kept for the Starboard status words in its section 6.
- **Four new colour themes, with their own backgrounds.** Dusk (periwinkle on blue slate), Lime (lime on
  blue-black), Rose (fluorescent pink on warm paper, with dark blue ink) and Amber (amber on graphite) replace
  Indigo, Forest, Plum and Ember. They are after the Hallmark themes (MIT, credited in the README). A palette may now
  tint the page, the cards and the lines in Light and Dark as well as the accent; High contrast keeps pure white or
  black, and status colours, focus and chart series never change. Lime's light accent is a deeper olive
  (`#3a5700`, 8.3:1 on white) so it reads clearly. `palettes/renamed.json` maps each old name to its nearest new one,
  for an app to move saved choices on. Every theme passes `tools/check_accents.py` with 0 failures.
- **Windows Contrast themes.** Switches show on and off, the current page shows in the rail, top tabs and phone
  menu, progress bars, the loading line, the waiting ring and the update dot all show, and a chosen cover is
  outlined, all in system colours. Before, each was drawn only by a background or a border colour that the theme
  takes away.
- **`.wizard-step__count`.** A step-by-step slide-out puts "Step 3 of 7" and the step's own link, such as Open as a
  page, on one line, the link on the right; on a narrow slide-out the link wraps under the count. A framed step's
  head has half the space over the count.
- **One way to wait (DASH-493).** Every bar that is working is thicker, with rounded ends and moving stripes.
  `.progress--running` starts with a visible piece, and `creepProgress()` in `components.js` eases it onto each count
  and creeps it towards the next, so it never sits still. `.progress--busy` has a striped band running along it. The
  loading line under the header is a striped chase of a long and a short bar, 6px high.
- **Waiting mark and busy button.** `.wait` with `.wait__mark` is the ring for a short wait, always with words. A
  button with `aria-busy="true"` draws the same ring before its words and keeps full colour. With less motion asked
  for, the ring fades instead of turning and the stripes stay still.

## 19 November 2026

- **Action list.** `.action-list` puts everything that can be done with one thing in its slide-out, each a
  button with one line under it saying what happens, such as a download that needs attention in Starboard. A file
  list uses rows with a `.tag.file-kind` (Media, Sample, Archive, Program, Other).
- **File picker.** `.file-field` draws every file upload as a button in the site's style, "Choose a file", with the
  chosen file's name and size beside it, instead of the browser's own picker; the real input stays over the button.
- **`.plugin-screen-card` and `.row__image`.** A plug-in's own page in Starboard (plug-in API 1.16) can put each group
  of rows on a card with the grey band and a sentence under it, and show a small picture on a row, such as an
  uploaded logo, at most 10rem by 4rem on the sunken surface.
- **`.progress--running`.** A progress bar for a count that is still going, such as 4 of 5 updates: soft stripes move
  across the filled part until the class comes off. With less motion asked for, the stripes stay still.
- **Section groups.** `.settings-section--group` holds several settings sections as one topic: its heading sits on
  the page, each section inside is a card with an h3, and topic tabs give the group one tab.
- **Status chips in list rows show their icon only on a phone.** At 720px wide or less, a chip with an icon inside
  `.rows .row` keeps its icon, colour and border and hides its words from view; screen readers still read them.
  A chip with no icon keeps its words.
- **`.btn--icon-on-phone`.** A button with an icon shows the icon only at 720px wide or less, keeping its height
  and its words for screen readers; for a repeated action in a list row, such as Watched on each episode.

## 18 November 2026

- **Mica is the default design (owner, DASH-479).** `tokens.css` takes Mica's neutral greys, 6px corners on every
  control, card, panel, menu and dialog (`--radius`), a layered lift (`--shadow-card` on cards, panels, settings
  sections and tables, `--shadow-raised` on menus, slide-outs and dialogs), 600 headings and a neutral focus ring.
  The design before it is the Classic style in Starboard's Styles plug-in.
- **Accent colours.** Blue is the default accent; the palettes become six accents over Mica's greys (Teal, the old
  default, Indigo, Forest, Plum, Ember and Graphite), each with a stronger shade in High contrast and High contrast
  dark, so the chosen colour stays in every theme.
- **The dashboard card is the model for every container.** Panels that open with a head, settings sections, tables,
  slide-outs and dialogs wear the card's grey band across the top; card edges and rules share `--color-divider`,
  #898989 in light and #747474 in dark, the lightest greys that keep 3:1 on the tinted page and the card.
- **Menu hover with a clear edge.** Every menu, tab and side menu item shows `--color-hover` with an edge in
  `--color-hover-edge`, at least 3:1 against the menu behind it in every theme and with every accent; the current
  item keeps the soft accent fill and the accent bar. Help centre menu items are 44px high.
- **Glass and the page wash.** The header, side menu, menus, slide-outs and dialogs are frosted layers
  (`--glass-alpha`, 92% in light and 90% in dark, with `--glass-filter`), over a soft accent wash across the page
  (`--page-tint`, 3%). The share is the least that keeps secondary text at 4.5:1 with black or white right behind
  the glass. Solid in High contrast, with Reduce transparency, without backdrop-filter and under an app's own style.
  Cards carry Mica's layered drop shadow (`--shadow-card`) as well as their border.
- **Light by default.** Dark applies only when chosen (`data-theme="dark"`); Match device sets the device's choice in
  script (`SharedComponents.applyTheme`). The gallery, boards, resources and help centres start in Light.
- **`tools/check_accents.py`:** checks every token pair the components draw (136 pairs) for every accent in all
  four themes, including the hover fill and its edge, and fails on any that falls short of WCAG 2.2 AA.
- Play in another app (Starboard, DASH-480): a link styled as a button that opens a film or episode in the media
  server's player in a new tab, with the `play` icon first and the new-tab icon last, its full name for screen
  readers, the 44px size, and what to show when the item or the app's address is not known. `LIBRARY.md` has the
  pattern. Made from existing parts, so no new class.

## 17 November 2026

- Restart where it is needed (Starboard, DASH-470): a Restart button inside the warning notice that says an app needs
  a restart, shown only then, with what it does beside it, progress in words in a polite status, focus kept on the
  button while it works and moved to the result. `LIBRARY.md` has the pattern; `COMPONENTS.md` adds the state word
  Restart needed (Warning). Made from existing parts, so no new class.
- `tokens.css`: one theme set `--color-slide-header` twice; the extra line is gone. No change to how anything appears.
  Found by Biome in Starboard's new code checks.

## 16 November 2026

- Headings wrap a word too long for the line (`overflow-wrap: anywhere` on h1 to h4), so a folder path or an address in
  a heading never pushes a page sideways at 320 pixels (WCAG 1.4.10). Found on Starboard's Backup and restore.
- The folder picker, Idea A (TheMightyTRexUK; Starboard's Bring in media, DASH-455): a first screen of places
  (`.folder-places`, `.folder-place`), a path bar with Back (`.folder-pathbar`), and each folder's size and what is in
  it (`.folder-row`, `__name`, `__meta`). Gallery section Folder picker; `LIBRARY.md` and `TERMINAL.md` say how. The
  `cloud` icon.
- Signing in to an outside service from a wizard (Starboard's Connect a cloud service): `.signin-card` and
  `.signin-steps` (open the sign-in page, what the browser shows after, paste back the address it ends on),
  `.qr-card` (a QR code dark on white in every theme, with the page and the code written out beside it),
  `.device-code`, `.signin-wait` (the words and time left in a polite live region, with the busy bar),
  `.test-checks` (each check's state in an icon and in words) and `.tested` (Test connection's result beside a
  place). `WIZARD.md` section 9 has the rules: two ways to finish, the same weight, the phone only where the service
  has a device flow; the gallery has a new section, Signing in to an outside service.
- Card footer (`.card-foot`): a small strip across the foot of a card, edge to edge, a lighter grey than the band,
  with when the card last updated. The band keeps the logo, the name and the status chip on one line; the time
  moves to the footer (Starboard's dashboard). The gallery's banded cards show it.
- Card band: `.card.has-band` keeps the band at the top edge. `.card` set its padding later in the file, so banded
  cards (the help centres' plug-in cards among them) had a white strip above the band.
- Plug-in cards (`.plugin-cards`): at most three to a row, so a name and its chip share the band; two on medium
  screens and one on a phone. The cards in a row are the same height.
- Side menu version (Starboard 0.19.1): `.rail__version` is a link to the app's update page, at least 44 by 44
  pixels, underlined on hover. When a newer release is out, `.update-dot` sits just above the number inside the link
  and pulses gently (a ring that grows and fades every 2.4 seconds, `update-dot-pulse`); it keeps still when Reduce
  motion is on or the device asks for less motion. `.rail__update` (the dot with the word Update above the version)
  is gone. `.update-dot[hidden]` now hides the dot. The gallery shows both states.

## 15 November 2026

- Card band (Starboard DASH-443): the heading keeps its own line. When the status chip and the time do not fit beside
  it, they move under it, instead of the heading being squeezed onto two lines (`.card-band__title` grows from its
  own width, `flex: 1 1 auto`, not from 8rem). Larger text still wraps it, and nothing is cut.
- `docs/HELP-WRITING.md` version 1.3 (Starboard DASH-439): a new part of section 7, "Simplest first, advanced apart".
  Help is split by need, not by person; sections are named by what they hold ("Add more apps", "Advanced options");
  the default path comes first, with additional apps and advanced options after it under their own headings; a
  signpost at the top says what the page covers; Get started holds only the simplest path. The checklist has a line
  for it.
- Help centre builder (Starboard DASH-426, the plug-ins help centre): each plug-in's own logo, a rounded tile from the
  catalogue's `logo`, in the side menu, on its cards and in its band (written once to `assets/logos/`), with its
  initials or icon kept for a plug-in with none. `--strict` now also stops on any page still left as a placeholder
  ("still to be written", TODO, TBD, TBC, lorem ipsum, outside code), and on an area left with placeholder words;
  a help centre may give its own list as `placeholders`. In plug-in mode, the Plug-ins area keeps its own articles
  (such as Starboard's Add a plug-in) in the side menu above the plug-in groups.
- Large text, wider spacing and short windows (Starboard DASH-437, found while writing Starboard's accessibility
  help). The side menu grows with the text (`--rail-w` from `--text-xs` and `--rail-name-em`, never under 88px), so
  "Starboard" and "Feedback" no longer break in the middle or run past its edge; in a short window it scrolls on its
  own instead of squeezing its items on top of each other, and below 720 pixels tall its items sit a little closer.
- The header gives way in steps when its items do not fit, instead of cutting off menu items or squeezing the search
  box: icons only, then the Search button, then Help and Display as icons, then the level 1 menu under Menu. New in
  `components.js`: `setupHeaderFit()` and `fitHeader()`, run by `setup()`, measuring again with one ResizeObserver
  whenever the text size, spacing, a name or the window changes. New classes on `.site-header`:
  `.is-search-folded`, `.is-actions-compact` and `.is-crowded`.
- Reduce motion Off now means full movement even when the device asks for less. Every `prefers-reduced-motion` rule
  in `tokens.css` and `components.css` leaves out `:root.pref-motion-off`; the shelf arrows and the A to Z jump ask
  `motionStill()` (now also `SharedComponents.motionStill`), and Display radios set `pref-motion-off` for Off.
- Phones: a row with no leading picture (`.row--no-lead`) keeps one column, `.row__meta` wraps long release names,
  and buttons wrap their words at large text, so nothing pushes the page sideways.

## 14 November 2026

- The help centre standard (Starboard DASH-436, chosen by the owner on 14 November 2026: "I also want this design to
  become the standard. This is to be used in all help centres"). `tools/help_centre/build.py` now builds every help
  centre the same way: the seven main items as top links (Home, Get started, Use it, Plug-ins, Accessibility, Fix a
  problem, Developers) with Search and Display; a hub with a side menu that folds (areas, groups, every article),
  the page you are on marked and its area and group open, opening from Menu on tablets and phones with the page
  behind inert; a home page with the latest version beside the heading (read from the changelog, no date), the
  journey, the newest thing and the problem solver card; a page for each area with a card for each group; a
  problem solver page (up to four questions, lists of links with no script); articles flow chart first, with
  numbered answer cards; and plug-in mode, where each plug-in is a folding item with the same eight pages. Every
  article says its area and group in a `<!-- help: <area> / <group> -->` line; `--strict` stops the build when one
  is missing. A help centre with no `areas` in `help-centre.json` keeps the older layout.
- Flow charts with no library: `tools/help_centre/flowchart.py` reads a `flow` block (start, questions, steps, ends
  and numbered answers, one a line, answers indented) or a simple Mermaid flowchart, draws it as SVG that follows
  every theme and Text size, and writes the same paths out in words. Mermaid is no longer loaded from a CDN.
- New components in `components.css`, with gallery examples under Help centre: `.top-links`, `.side-tree`,
  `.journey` and `.stage-card`, `.flow-chart`, `.answer-card`, `.feature-card`, `.solver-card` and `.solver`,
  `.version-badge`, `.plugin-cards`, `.plugin-card` and `.plugin-band`; an `.app-icon` can hold a sprite icon. New
  behaviour in `components.js`: `setupSideTrees()` and `setupSolvers()`, run by `setup()`.
- `tools/help_centre/help.css` keeps only the help centre's layout; `help.js` drops Hide the menu, and Search moves
  the focus to the search box in the side menu. Code samples that scroll sideways can be reached with the keyboard.
- `docs/HELP-WRITING.md` version 1.2: section 3 is the seven areas and their groups, and section 11 is the standard
  (layout, side menu, journey, the flow chart format and when every article needs one, the problem solver, plug-in
  mode and the shape of `help-centre.json`). `docs/LIBRARY.md`, Help centre, lists the components and their rules.


## 13 November 2026

- UX notes leave the library (DEV-05, TheMightyTRexUK): `ux-notes.js`, its `.ux-dock`, `.ux-banner`, `.ux-outline`
  and `.ux-notes` styles and its gallery section are gone. [Snaglist](https://github.com/TheMightyTRex/snaglist),
  which grew from it, does the same and more, and each app copies it in itself. `tools/sync.py` no longer copies
  `ux-notes.js` and lists any copy an app still has as "retired", for the app to remove.

- Load more as you scroll (UX-52, owner, 9 November 2026): `SharedComponents.loadMore(box, options)` loads a list's
  next page as its end comes into view, with one IntersectionObserver per list. The Show more button stays as the
  way for keyboard and screen reader users and is the only way with Reduce motion or when a setting asks for it.
  "Loading the next 40" shows while it loads, a polite status says "40 more shown", focus stays where it was, and
  it pauses after three pages so the footer stays in reach. New `.load-more__count` and `.load-more__status`; a
  gallery example; `DESIGN-SYSTEM.md` section 11 says when to use it and when not.

- Palettes an app can offer (Starboard's own style, TheMightyTRexUK, 13 November 2026): `tools/palettes.py` also
  writes `palettes/app-palettes.css`, all five palettes under `:root[data-palette="…"]`, weaker than High contrast.
  `tools/sync.py` copies it, with `palettes.json`, into Starboard (`css/palettes.css`, `palettes.json`); its
  `--check` lists a file an app copy does not have yet as absent. The gallery's palette note says so.


## 12 November 2026

- Settings sections and locations take the page's width, as every other page does; the 880px limit is gone. Section
  lines and setting text keep a readable length (75 characters).

- Loading line: the chase (a long and a short bar following each other across) replaces the single sweep. With
  Reduce motion the line fades in and out across its width rather than standing still, so it still shows activity.

- Which item to use (Starboard DASH-309): `DESIGN-SYSTEM.md` section 10 says when to use list rows, cards, panels,
  status chips and icons, filter chips, segmented controls, toolbars, the selection bar, notices, toasts, empty
  states, dialogs, slide-outs and tables, with eight rules. The gallery has a Which item to use table that links to
  each example.

- Layout rule: a state chip sits on its title's line, at the right and centred, everywhere (`.title-chip`).

- Search field: every search box has a Search button with the search icon, inside the box at the right. It is the
  default: components.js adds it to any `input type="search"`, including boxes added later in slide-outs and
  dialogs. In a form it submits; a box that filters as you type gets a button that searches now. Opt out with
  `data-no-search-icon`.
## [Unreleased]

### Added
- **A banned words check** (17 November 2026, design audit): `tools/check_words.py` fails on the words the content
  design guide bans (`CONTENT-DESIGN.md` sections 1, 2 and 5) in the guides, the gallery, the Boards and
  resources pages, `components.js`, the help centre script and the terminal frame. Genuine exceptions are in
  `tools/words-allowed.txt`, each with its reason. `tools/install-hooks.sh` runs it before every commit.
- **A token check** (17 November 2026): `tools/check_tokens.py` lists every name a style sheet uses that `tokens.css`
  does not have. `DESIGN-SYSTEM.md` section 2 lists the names that are not tokens and the token to use:
  `--radius-1`, `--radius-2`, `--radius-3` and `--radius-control` are `--radius`, `--focus-width` is `--focus-w`,
  `--weight-normal` is `--weight-regular`, and `--text-base` is `--text-md`.
- **Starboard's status words** (17 November 2026): `COMPONENTS.md` section 6 has one word and one tone for each of
  Starboard's states, from its page maps, for one map in Starboard's `common.js`.
- **Card band and a compact app icon** (14 November 2026): `.card-band` puts a grey band across the top of a card (`.has-band`) with the logo, the name as the heading, and a status chip and when it last updated at the right, for Starboard's plug-in cards (DASH-428, design 2); `.app-icon--compact` is the 32px icon it uses, with initials on a tile when there is no logo.
- **Heading font and side menu colour for styles** (11 November 2026): headings use `--font-heading` and the side menu `--color-rail` when a style sets them; neither is set by default, so headings keep the body's font and the side menu the header's colour.
- **Update in the side menu** (9 November 2026): `.rail__update`, a dot and the word Update above `.rail__version` when a newer release is out, linking to About and updates.
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
- **Wording, from the design audit** (17 November 2026). The guides, the gallery and the boards no longer say "see",
  "look", "type", "above", "below", "turn on" or "turn off": a cross-reference is "read", a position is the name of
  the section, and a setting is Active or Inactive. `CONTENT-DESIGN.md` is version 1.5 and `HELP-WRITING.md`
  version 1.4.
- **The terminal frame's words** (17 November 2026): "Press b to go back, ? for help, f to send feedback or q to
  stop."; "Enter a number from 1 to 7, ? for help or q to stop."; long help ends "Enter: show more", with Show more
  in the menu; a job in plain mode says "Installing (2 of 3)…" in place of "Please wait..."; while a job runs, the
  menu shows only Ctrl+C Stop; a failed job says "Installing did not finish (error 3)."; plain mode's warning
  starts "Warning:"; a small window says "This window is too small for the box layout. Make it at least 60 columns
  wide and 20 lines high." `TERMINAL.md` says the same, with "4 more: press m to show them", and Snaglist's kind
  Confusing to use (Snaglist 0.5.0).
- **The wait text** (17 November 2026): `WIZARD.md` asks for the job by name ("Downloading and starting the apps…")
  beside the timer and count, never "Please wait, this can take some time...".
- **Display and accessibility** (17 November 2026): Reduce motion is Match device, Active or Inactive; the buttons
  are Close and Reset to defaults, in the gallery, the site's pages, the boards and the help centre builder.
- **Default texts in `components.js`** (17 November 2026): the copy button's toast is "Copied to the clipboard"
  when the button has no `data-copied`; a letter with nothing in the A to Z jump list is "Q, no books" from the noun
  (`azJump(nav, letters, noun)` or `data-noun`), or "Q, none"; Load more's error is "The next 40 books could not be
  loaded. Select Show more to try again."; a sortable row at an end is "already first" or "already last".
- **More options, not Advanced** (17 November 2026): the small settings switch is More settings and a location's
  path is under More options, in Enter a path. `HELP-WRITING.md` section 7 is "Default set-up first, more options
  apart", with the sections "The default set-up" and "More options"; its sweep finds more words.
- **Made-up example data** (17 November 2026): the gallery, `CONTENT-DESIGN.md` and the toast options board use
  made-up authors, books and radio shows, and the Starboard boards use `homeserver.example`.
- **Starboard boards** (17 November 2026): First reported, Last reported and Last version found; Enter the new
  password again; Deactivate network access, with Cancel.
- **Toolbars on phones** (9 November 2026): `.toolbar__row` may shrink below its chips, so a long row of filter chips scrolls inside the toolbar instead of making the page scroll sideways.
- **A long job in plain mode is never silent** (9 November 2026): `TERMINAL.md` adds the rule, and `terminal-frame.sh` says "Still working: the job (12 min)" every 2 minutes while a job runs in plain mode, with the job's count when it has one.
- **Terminal stops** (8 November 2026): a failed job shows its error number and the address of its help in
  both looks; a script run by another ends on its own number, and the outer script adds none of its own; the frame's
  STOP_FILE tells the outer script when the person stopped (q or Ctrl+C), which is not an error (Starboard DASH-147
  and DASH-152).
- **Plain menus** (8 November 2026): in plain mode, `choose` wraps each answer between words inside the window,
  the rest set in under its number, instead of printing it on one line.
- **Release notes** in both apps use the six change types of the changelog rules: Added, Changed, Deprecated,
  Removed, Fixed and Security (5 November 2026).
- **Wizard help** opens in a slide-out, not a dialog (4 November 2026).
- **The gallery** has the apps' header, a logo and a footer (3 November 2026).
- **Scroll bars** are thin and square, in the border colour on a clear track (2 November 2026).
- **App logos** show without a tile; apps without a logo keep their initials on a tile (2 November 2026).
- **Slide-out headers** are in the page colour, and Display and accessibility is a slide-out
  (2 November 2026).

### Removed
- **Penpot** (9 November 2026): the Penpot plugin (`penpot/`), its tokens file and `docs/PENPOT.md` are removed, because the Penpot file did not work as expected. The gallery on GitHub Pages stays the way to see every component.

### Fixed
- **Sentence case in the help centre** (17 November 2026): side menu group labels (`.side-tree__label`) and journey
  stage labels (`.journey__label`) are no longer in capitals.
- **Names that were not tokens** in `components.css` (17 November 2026): `--focus-width` (now `--focus-w`),
  `--radius-control` (now `--radius`), `--text-base` (now `--text-md`) and `--font-mono` (the monospace font
  written out). No change for the person: each fell back to the same value.
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
