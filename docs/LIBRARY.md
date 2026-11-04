# TRex Design System: the component library

Version 1, 2 November 2026. One component library for both apps, so they look and behave as one family.
It follows `DESIGN-SYSTEM.md` and the guides in this folder (`CONTENT-DESIGN.md`, `HELP-WRITING.md` and `ACCESSIBILITY.md`).
File names in the tables below are relative to the root of the repository.

**Open `gallery.html` in a browser** to see every component live. The gallery uses the same header and menus
as the apps: the main menu and search in row 1, the component groups in row 2, and Display opens the Display
and accessibility slide-out (theme, text size, reduced motion, high contrast, underlined links, wider
spacing). Slide-outs, menus, the phone menu and the dialog all work in the gallery.

## Files

| File | What it is |
|---|---|
| `tokens.css` | Every colour, size, space and motion value, as role names, for Light, Dark, High contrast and High contrast dark, plus the display preference classes |
| `components.css` | Every component, in `@layer shared`, using only the tokens |
| `components.js` | The behaviour every component must have (menus, slide-outs, dialogs, phone menu, filter chips, copy, help, display settings), in plain JavaScript |
| `icons.svg` | Lucide icons as an SVG sprite (`<use href="#i-book-open">`); `tools/icons.txt` lists them |
| `fonts/` | Atkinson Hyperlegible Next (OFL licence) |
| `gallery.src.html`, `gallery.html` | The gallery (edit the `.src` file, then build) |
| `contrast-report.txt` | Made by `tools/contrast.py` (not committed): measured contrast for every text and control pair in all four themes; all pass WCAG 2.2 AA |
| `areas/` | Design boards for every area of both apps, using the library, with slide-outs where they fit |
| `tools/build.py` | Turns `{{i:name}}` into icons and `<!--ICONS-->` into the sprite for any `*.src.html` |
| `tools/icons.py` | Rebuilds `icons.svg` from Lucide in Storyarr's `node_modules` |
| `tools/sync.py`, `tools/paths.py` | Copies the library into both apps; `paths.py` says where the apps are (`tools/paths.local.json`, not committed) |

## Principles

1. **One look, two apps.** Same tokens, same classes, same behaviour. An app may add its own components
   (charts on Starboard, the bookshelf on Storyarr) but builds them from the tokens.
2. **Accessible is the baseline.** WCAG 2.2 AA in every theme; 44px controls and targets; a visible 3px focus
   ring; status always in words plus a shape or icon, never colour alone; keyboard first; everything works at
   175% text and with wider spacing; nothing moves when reduced motion is on.
3. **Square, calm and dense enough.** Square corners, one typeface, thin dividers, one accent colour, one
   primary button per view.
4. **Things open where they make sense.** Slide-out for the details or editing of one item in a list; dialog
   for a decision; page for something people return to. See "Slide-out, dialog or page" below.

## Menu names

- **Main menu:** the icon rail on the left (Storyarr). Starboard has no rail: its main menu is header row 1.
- **1st level:** header row 1, the section's pages (My library, Following, Library review).
- **2nd level:** header row 2, the page's own tabs (In my libraries, Authors, Series, All saved titles).
- All three levels have icons. In the phone menu, only the main menu and the 1st level have icons; the
  2nd level stays under the header on phones.

## Components

### Foundations
| Component | Classes | Notes |
|---|---|---|
| Colour roles | `--color-*`, `--status-<tone>-bg/-fg`, `--chart-*`, `--series-1` to `--series-7`, `--series-empty` | Four themes; accent is one token (UX-02 board offers Indigo, Teal, Amber) |
| Palettes | `palettes/indigo.css`, `forest.css`, `plum.css`, `ember.css`, `graphite.css` (Teal, the default, is `tokens.css`) | For building a new design or site with the same components: load `tokens.css`, one palette, then `components.css`. Light and Dark colours only; status colours, chart series and High contrast stay the same. Written by `tools/palettes.py`; not synced into the apps |
| Type | `--text-xs` to `--text-2xl`, `--font` | One typeface; scales with Text size |
| Space and size | `--space-1` to `--space-12`, `--control-h` (44px), `--control-h-compact` (32px, dense tables only) | |
| Icons | `icons.svg`, `svg.i`, `.i-lg`, `.i-xl` | Lucide, 2px stroke, decorative beside words |
| Utilities | `.clamp-2`, `.clamp-3`, `.visually-hidden`, `.skip-link`, `.muted`, `.small`, `.numeric`, `code`, `.code-block`, `.stack-1`, `.stack-2`, `.stack-4` | Stacks put children one under another with a 4, 8 or 16px gap |

### Shell
| Component | Classes | Notes |
|---|---|---|
| Main menu (rail) | `.rail`, `.rail__logo`, `.rail__end`, `.with-rail` | Storyarr only; hidden on phones |
| Header | `.site-header`, `.site-header--no-rail` (Starboard: name and logo start row 1), `.site-header__bar`, `.site-header__brand`, `.site-header__search`, `.site-header__actions`, `.site-header__tabs` | Row 1: 1st level, search, Display. Row 2: 2nd level, only when the page has tabs. Nothing else |
| Menu tabs (1st and 2nd level) | `.menu-tabs`, `.menu-tabs__label`, `.is-compact` | Icons and names; icons only when they do not fit; current page bar |
| Count and update dot | `.count`, `.update-dot` | Meaning in hidden text |
| Phone menu | `.phone-menu-button`, `.phone-menu`, `.phone-menu__section > a` (an item with no 1st level), `.phone-menu__search`, `.phone-menu__section`, `.phone-menu__foot` | Drawer from the left; search, main menu, 1st level; account and sign out at the foot |
| Page and page head | `.page`, `.page--narrow` (Sign in, Set up), `.section-head`, `.section-head__control`, `.page-head`, `.page-head__text`, `.page-head__summary` | One visible h1; page actions on the right |
| Footer | `.site-footer`, `.site-footer__app`, `.site-footer__brand`, `.site-footer__links`, `.site-footer__maker`, `.maker-mark` | On every page but Sign in and Set up. Left: app icon, name, "Version 0.7.4", then Help (only when the app has a help centre), About, Updates. Right: the dinosaur mark and TheMightyTRexUK, one link to the GitHub profile (copy the markup from the gallery) |
| Display button | `.icon-btn` (sun icon, `.label` Display), `aria-haspopup="dialog"`, opening a `.side-panel` titled Display and accessibility; inputs with `data-display`, `data-display-save`, `data-display-reset` | Last item in the header on every page. The choices and their order are in `ACCESSIBILITY.md` section 1 |

### Actions
| Component | Classes | Notes |
|---|---|---|
| Button | `.btn`, `.btn--primary`, `.btn--quiet`, `.btn--danger`, `.btn--compact` | One primary per view; words say what happens |
| Icon button | `.icon-btn`, `.icon-btn--bare` | Always named, including the thing it acts on |
| Split button | `.split-btn` | Main action plus a menu of related ones |
| Menu button and menu | `.menu-wrap`, `.menu`, `.menu__label`, `role="menu"` items | Related actions in one button (the Lists menu); sort as `menuitemradio` |
| Copy button | `.copy-btn`, `data-copy` | Confirms in a status message |
| Action row | `.actions` | |

### Inputs
| Component | Classes | Notes |
|---|---|---|
| Field | `.field`, `.field__label`, `.hint`, `.field-error` | Label above, hint, error that says how to fix it |
| Text, select, text area | `.input`, `.select`, `.textarea` | 44px; `aria-invalid` shows the error border |
| Search field | `.search-field` | Plain box; hidden submit button |
| Input with unit | `.input-group`, `.input-group__unit` | |
| Checkbox and radio | `.check`, `.check__text`, `.check__hint` | 22px box, 44px row |
| Switch | `.switch` with `role="switch"` | For settings that apply at once |
| Segmented control | `.segmented` | Two to five short options (theme, text size, view, cover size) |
| Option cards | `.option-cards`, `.option-cards--row` (side by side), `.option-card` | Choices that need a line of explanation; text stays at the top of each card |
| Filter chips | `.filter-chips`, `.filter-chip` with `aria-pressed` | In toolbars |
| Applied filters | `.applied`, `.applied__item` | Each removable, plus Clear all |
| Form layout | `.form-grid`, `[data-span="all"]`, `fieldset` | |

### Content
| Component | Classes | Notes |
|---|---|---|
| Settings helpers | `.inline-save`, `.form-stack`, `.setting__cost` | A field and its Save on one line; fields one under another; the muted line saying what a setting costs |
| Status chip | `.chip[data-tone]` | Word, shape and colour: dot, diamond (warning), square (danger), ring (muted) |
| Title with status | `.title-status`, `.title-status__chips` | A heading's status chips straight after the name, centred on its line; never on a line under it (see "Where status goes") |
| Status icon | `.status-icon[data-tone]` | In a list of things with a state: an icon after the name, the word in hidden text and a tooltip |
| Tag | `.tag` | Format or kind, not status |
| Avatar, app icon | `.avatar`, `.app-icon` | |
| Cover | `.cover`, `.cover--row` (48px in rows), `.cover__badge` | 2:3; square audio covers letterboxed |
| Facts | `.facts` (`dl`) | Author first, then Series; names are links |
| Stat | `.stats`, `.stat[data-tone]`, `.stat__value`, `.stat__label` | Edge colour plus words |
| Progress and meter | `.progress[data-tone]`, `.meter`, `.meter__label` | Value always in words |
| Rows | `.rows`, `.row`, `.row--no-lead`, `.row--opens`, `.row__title`, `.row__meta`, `.row__side` | `.row--opens`: the whole row opens a slide-out |
| Group heading | `.group-heading` | Sentence case, no capitals |
| Table | `.table-wrap[data-stack]`, `.table`, `th[aria-sort]` | Real tables only; stack into cards on phones |
| Notice and callout | `.notice[data-tone]` (`success`, `warning`, `danger`, `muted`; none is info), `.notice__title`, `.notice__body` | Icon and words; `role="status"` or `role="alert"`. As a callout in long text, the title is the lead word: Before you begin (info), Limitation (warning), Warning (danger, cannot be undone), Tip (success), Example (muted) |
| Prose | `.prose`, `.prose__lead`, `.prose__kind` | Help topics, guides and release notes shown in an app (`HELP-WRITING.md`) |
| Time ago | `<time datetime>` with `.visually-hidden` exact time | "Updated 10 seconds ago" on screen, the exact time for screen readers |
| Empty state | `.empty`, `.empty__icon` | What, why, one next step |
| Loading | `.skeleton`, `.loading-bar[data-active]`, `aria-busy` | Skeletons in the shape of the content |
| Toast (option C) | `.toasts`, `.toast[data-tone="success"\|"info"\|"warning"\|"danger"]`, `.toast__text`, `.toast__title`, `.toast__detail`, `.toast__action`, `.toast__close`; `SharedComponents.toast(title, { detail, tone, action })`, `toast.error(...)`, `toast.warning(...)` | Card in the corner (full width on phones), status edge and icon, up to three stacked; a new one never pushes out an error. Success and info 5 seconds (10 with an action), warning 10, error until closed; waits under the pointer or focus. Errors read out at once |
| Saved note (option D) | `.saved-note`; `SharedComponents.savedNote(element)` | Settings pages: "Saved at 16:31" beside the button that saved, instead of a toast; goes at the next change |
| Icons in built parts | `data-sprite` on the `components.js` script tag, or `window.SharedComponentsSprite` | The toast and saved note draw icons as `<use href="#i-name">`. An app whose icons are in a separate file names it (Starboard: `/icons/sprite.svg`), or the icons and Close button are blank |
| Help | `.help`, `.help__text` | A disclosure button, not a hover tooltip |
| Disclosure | `.disclosure` (`details`), `.disclosure__body`, `.disclosure__meta` | Releases list, SMART report, advanced settings |
| Steps | `.steps`, `aria-current="step"`, `[data-done]` | Onboarding and upgrade wizard |
| Command | `.command` with `.code-block` and `.copy-btn` (`.copy-btn--label` shows the word Copy) | Commands to copy (How to upgrade); wizards use the labelled button |
| Line chart | `.chart`, `.chart__svg`, `.chart__grid`, `.chart__axis`, `.chart__line--1/--2`, `.chart__legend`, `.chart__swatch` | Second series dashed; always with a table view in a disclosure |
| Load more | `.load-more` | Infinite lists end with a count and a button |

### Containers
| Component | Classes | Notes |
|---|---|---|
| Panel | `.panel[data-tone]`, `.panel__head` | Groups content |
| Card | `.cards`, `.card[data-tone]`, `.card__top`, `.card__title`, `.card__meta`, `.card__actions` | One thing; whole card is the target; opens its slide-out or page |
| Media card and grid | `.media-grid[data-size]`, `.media-card`, `.media-card__title`, `.media-card__meta`, `.media-row` | Books and films; Small, Medium, Large |
| Section toolbar (design D) | `.toolbar`, `.toolbar__row`, `.toolbar__search`, `.toolbar__end`, `.toolbar__count` | Same on every list |
| Save bar | `.save-bar`, `.save-bar__text` | The one way to save a settings section: sticks to the bottom while there are unsaved changes |
| Timeline | `.timeline`, `.timeline__item[data-tone]`, `.timeline__title`, `.timeline__meta` | A request's history, a backup run; newest first |
| List and detail | `.list-detail`, `.list-detail__list`, `.row[aria-current]` | Following: authors on the left, the chosen one on the right; list alone on phones |
| Item header | `.item-header`, `.item-header__art` (`--round` for people), `.item-header__text`, `.item-header__byline`, `.item-header__chips` | Book, author, series and narrator pages |
| Series header (UX-43) | `.series-head`, `.series-head__text`, `__name` (`.wordmark` with no logo), `__meta`, `__desc`, `__progress`, `__actions`, `.cover-fan` | Series and radio show pages; the name stays the h1; the fan is hidden on phones |
| Solid-colour logo, wordmark | `.logo-mask` (`--logo`, `--logo-ratio`, `data-colour="accent"`), `.wordmark` | Any transparent logo as one colour through a CSS mask; the name set large when there is none |
| Logo slide-out (UX-43) | `.logo-saved`, `.logo-saved__row`, `.logo-saved__text`, `.logo-tabs`, `.logo-pane`, `.logo-step`, `.logo-candidates`, `.logo-candidate` (`__art`, `__text`), `.cover-pick`, `.logo-crop` (`__canvas`, `__controls`, `__readout`), `.range`, `.checker`, `.logo-drop`, `.logo-preview` (`__light`, `__dark`), `.inline-form` | From a cover, Find online, Upload your own; the saved copy and Remove |
| Back link, breadcrumbs | `.back-link`, `.breadcrumbs` | "Back to My library"; folder paths |
| Shelf | `.shelf`, `.shelf__head`, `.shelf__caption`, `.shelf__end`, `.shelf__track` | Discover shelves: one row that scrolls, arrows on computers |
| Calendar month | `.calendar` (a `table`), `td[data-outside]`, `td[aria-current="date"]`, `.calendar__day` | List view on phones |
| Selection bar | `.selection-bar`, `.selection-bar__text`, `.row--select`, `.cover--thumb` | Bulk actions (Wanted, series reading order) |
| Wizard | `.wizard`, `.wizard__foot`, `.steps--collapse`, `.steps__short`, `.wizard-layout`, `.wizard-main`, `.wizard-progress`, `.steps--sub`, `.wizard-paths`, `.wizard-summary` | Every job done in steps (set-up, upgrade, restore, migration). Rules in `docs/WIZARD.md`; steps become "Step 3 of 7" on phones |
| Wizard review aids | `.wizard-aside`, `.wizard-next`, `.wizard-tree`, `.wizard-tree-toggle` | What happens next and the decision tree: for testing only, shown while the app's testing setting is on, never in the finished product |
| Help links | `.help-links`, `.help-link`, opening `.dialog.dialog--scroll[data-close-outside]` | "What is…" at the end of the part of a page they explain |
| Address | `.address` with `.copy-btn` (`data-copied="Address copied"`) | A server address as a link that opens in a new tab, with a copy button |
| Settings rows | `.settings-section`, `.settings-section__head`, `.settings-rows`, `.setting`, `.setting--opens`, `.setting__text`, `.setting__label`, `.setting__hint`, `.setting__control`, `.settings-section__head--action` | Things with several fields open a slide-out |
| Panel header | `.panel-header`, `.panel-header__title`, `.panel-header__brand`, `.panel-header__actions` (Previous, Next) | The same bar on slide-outs, dialogs and the phone menu; on slide-outs and the phone menu it wears the page background (`--color-slide-header`) |
| Slide-out | `.side-panel-layer`, `.side-panel-backdrop`, `.side-panel`, `.side-panel--wide`, `.side-panel__body`, `.side-panel__foot`, `.side-panel__lead` | From the right; 420px, 640px wide, full width on phones; header in the page background, body and foot on the raised surface |
| Dialog | `.dialog` (`<dialog>`), `.dialog__body`, `.dialog__foot`, `.dialog--scroll`, `data-close-outside` | Decisions and short tasks only. `.dialog--scroll`: only the body scrolls, the header and foot stay in view. `data-close-outside`: a press outside closes it (help only, never a dialog with fields) |

## Slide-out, dialog or page

| Use | When | Examples |
|---|---|---|
| Slide-out | Details of one item in a list, or editing it, where seeing the list still helps; longer reading beside the page | Book summary; a request; a download client, indexer, reading account or user; a log entry; an app, disk, download or backup run on Starboard; release notes; Display and accessibility |
| Dialog | A decision or short task that must finish before going on; one or two fields | Confirm remove or reset; Add list; a password check before a download or restore |
| Page | Something people return to, link to or spend time in | Book, author, series and narrator pages; Disk health; each Settings section; Upgrade wizard |
| In place | A small change to a value already in view | Switches and selects in settings rows; filter chips; cover size |

Behaviour that every slide-out, dialog and phone menu must have: focus moves in (to Close), Tab stays inside,
Escape and Close close it, a press outside closes a slide-out or menu, focus returns to the opener, and the page
behind does not scroll. A slide-out's open item can be in the address, so Back closes it.

## Adopting the library

**Starboard** already uses these names. To adopt: replace `css/tokens.css` with `tokens.css` (adds panel
header, status edge, compact control and High contrast chart colours; High contrast dark page is now black),
then move each page's classes to the library's where they differ:
`.btn-primary` → `.btn--primary`, `.btn-quiet` → `.btn--quiet`, `.btn-danger` → `.btn--danger`,
`.filter` → `.filter-chip`, `.filters` → `.filter-chips`, `.seg` → `.segmented`, `.design-option` →
`.option-card`, `.dialog__head` and `.side-panel-header` → `.panel-header`, `.app` → `.card`,
`.app__icon` → `.app-icon`, `.status-pill` → `.chip`, `.meter-row` → `.meter`, `.switch-row` → `.switch`.
A private audit lists every duplicate to merge.

**Storyarr** has 1,285 generated `--c-*` colour tokens (492 uses) and a few role names in `styles.css`. To
adopt, one release at a time:
1. Add `tokens.css` and alias the old role names to the new ones: `--surface` → `--color-surface`,
   `--line` → `--color-divider` (or `--color-border` for control borders), `--muted` → `--color-text-muted`,
   `--accent` → `--color-accent`, `--control-active` → `--color-control-active`,
   `--control-height-large` → `--control-h`, `--control-height` → `--control-h-compact`,
   `--panel-header-bg` → `--color-panel-header`, `--panel-header-line` → `--color-divider`.
2. Add `components.css` in a `shared` layer below the app's own layers, so nothing changes until a page
   moves over.
3. Rebuild each page on the library's classes (a private audit lists the old classes and the
   duplicates), then delete the page's old CSS and the `--c-*` tokens it used.
4. React components wrap the classes: `Button`, `IconButton`, `MenuButton`, `Field`, `Switch`,
   `Segmented`, `Chip`, `Notice`, `SidePanel`, `Dialog`, `SectionToolbar`, `SettingsRow`, `Card`, `MediaCard`,
   with the behaviour in `components.js`.

**Adopted (2 November 2026):**
- **Starboard**, branch `shared-library` (commits 175a0c3 and 2129d68, not pushed). It loads `components.js`
  with `data-manual` (no automatic set-up, because its page scripts wire their own behaviour) and builds
  slide-outs, confirm dialogs and More actions menus with helpers in `web/js/common.js`: `sidePanel()`,
  `confirmDialog()`, `menuButton()` and `renderKeyed()` (rows updated in place so focus stays). Icons come
  from `web/icons/sprite.svg`.
- **Storyarr**, branch `covers-and-shelf-only` (commit 1beeb45, not pushed). Copies in
  `apps/web/src/shared/`: `tokens.css` (without the font, which Storyarr loads itself), `components.css`, and
  `compat.css`, which keeps the 18 class names both apps use (`.notice`, `.count`, `.empty`, `.panel` and
  others) looking as before until each page moves over. Delete a rule there when its page moves.

**components.js changes:** `openLayer(idOrElement, opener, onClose)` now accepts an element, returns its
close function, cleans up its listeners and can be reopened safely. Loading the file with `data-manual`
(or setting `window.SharedComponentsManual = true` first) skips the automatic `setup()`.

**Keeping them in step (David, 2 November 2026: the library is shared by both apps and kept up to date):**
change the component here first, never in an app, and follow the steps in
[Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html). Add the change to the Decisions list in this file, commit it here and
push, so every checkout picks it up.

**Decisions:** accent teal (UX-02 option B); status chip style B, outline with icon (UX-04); cover actions (UX-42: `.cover-card` with `.cover-actions` on the cover by default, beside it as a per-account setting); shelves without scroll bars (UX-30 option A: `.shelf-scroller`, arrows over an edge fade); covers always line up (`.media-card` titles take two lines); small covers (UX-44: `.book-row` with `.cover-actions--row` in rows, `.cover-card__more` with the actions in words on small tiles); square radio art in the book shape (FEAT-R decision 2, fill 4: `.show-art`, label in the image's colour) and `.logo-tile`; slide-outs look like slide-outs (David, 2 November 2026: `--color-slide-header`, the page background, on slide-out and phone menu headers over a raised-surface body; dialogs keep the plain header; Display and accessibility and Release notes are slide-outs). App logos without a tile (David, 2 November 2026: `.app-icon.has-image` is just the image, with no border or background; initials keep the tile). The logo editor on every way to get a logo (David, 2 November 2026: From a cover, Find online and Upload your own all use the box, Shape from lightness or transparency, four cleaning levels, and a small eraser and paintbrush on `.checker[data-tool]`; found files show as plain pictures in `.logo-candidate__art > img`). Nicer scroll bars (David, 2 November 2026): thin and square in every scrolling area, `--color-scrollbar` (the border colour, the text colour in High contrast) on a clear track; they stay visible, and only shelves hide theirs behind arrows. UX notes for testing (David, 2 November 2026): `ux-notes.js` (copied to both apps by sync.py) puts Note an issue in the corner of every page while an app's testing setting is on; choose the part (click, or Tab and Enter), say what is wrong, the kind and how bad; Notes lists them with Copy as text, Download and Mark as fixed. Notes keep the page, the part, a selector and the display settings. An app passes a store to keep them on its server; otherwise they stay in the browser. Styles: `.ux-dock`, `.ux-banner` (at the bottom, clear of the header), `.ux-outline`, `.ux-notes`. Security checks the same in both apps (David, 3 November 2026): `docs/SECURITY-CHECKS.md` sets the checks (tests, live journeys, Trivy, ZAP on a private network, Gitleaks, Bandit and Semgrep, ShellCheck, Hadolint, CodeQL, a separate review, install tests), how to sort findings, a security page in each app with a "Security checks for each release" table, and a Security section in every release's notes (`CONTENT-DESIGN.md`, release notes). Starboard is the worked example; Storyarr has to catch up. Penpot (David, 3 November 2026): a plugin (`penpot/`, made by `penpot/make.py` from `tokens.css` and `icons.svg`) builds the library colours for four themes, text styles, icons and the main components into a Penpot file; `penpot/tokens.json` is for Penpot's Tokens panel. Steps in `docs/PENPOT.md`. Wizard rules (David, 4 November 2026): `docs/WIZARD.md` sets one set of rules for every wizard, from the installer mock-up: the first question asks which job, each with its own wizard; one question per step; steps that do not apply left out; a step in parts has `.steps--sub`, as wide as the progress bar with a line between parts, and each part counts in the progress bar's total; "(recommended)" with a reason, never "easiest"; "What is…" help at the end of the part it explains, in a dialog that scrolls inside and closes on a press outside; addresses as links with copy; a summary of what was set and skipped. What happens next and the decision tree are review aids for testing only, never in the finished product. Copying falls back to a hidden text box on plain http (`copyText()` in `components.js`), and a dialog returns focus to the button that opened it. Step numbers grow with Text size.

## App-only patterns (2 November 2026)

Built from the tokens, used by one app, so not in `components.css`:

- **Starboard:** `.access-change` (what Starboard can access, with the command to change it), `.job-run` (a server job
  with Run now), the storage charts (`--media-*` map to `--series-*`), the release notes slide-out
  (`.release-notes`, opened from the version in the footer).
- **Storyarr:** the bookshelf and series views.

