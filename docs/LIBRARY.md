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

Names (TheMightyTRexUK, 4 November 2026: "Side menu, Level 1 menu and Level 2 Menu"):

- **Side menu:** the icon rail on the left, in both apps: the logo with the app's name underneath, Search,
  then the sections. Starboard moves to the side menu (TheMightyTRexUK, 4 November 2026), with Library, Discover,
  Activity, System and Settings; see `areas/starboard-menu.html`.
- **Level 1 menu:** header row 1, the section's pages (Starboard: TV, Films, Radio, Books, Audiobooks). In
  Starboard it starts with the server's own name, up to 10 characters, as plain text with no icon.
- **Level 2 menu:** header row 2, a page's own tabs (Starboard: My library, Series, Authors, Stations), only
  when the page has them.
- On phones the header shows only the logo on the left, with no names (TheMightyTRexUK, 4 November 2026); the app's
  name and the server name stay for screen readers.
- All three have icons. In the phone menu, only the side menu and the level 1 menu have icons; the level 2
  menu stays under the header on phones.

## Components

### Foundations
| Component | Classes | Notes |
|---|---|---|
| Colour roles | `--color-*`, `--status-<tone>-bg/-fg`, `--chart-*`, `--series-1` to `--series-7`, `--series-empty` | Four themes; accent is one token (UX-02 board offers Indigo, Teal, Amber) |
| Palettes | `palettes/indigo.css`, `forest.css`, `plum.css`, `ember.css`, `graphite.css` (Teal, the default, is `tokens.css`) | For building a new design or site with the same components: load `tokens.css`, one palette, then `components.css`. Light and Dark colours only; status colours, chart series and High contrast stay the same. Written by `tools/palettes.py`; not synced into the apps |
| Type | `--text-xs` to `--text-2xl`, `--font` | One typeface; scales with Text size |
| Space and size | `--space-1` to `--space-12`, `--control-h` (44px), `--control-h-compact` (32px, dense tables only) | |
| Icons | `icons.svg`, `svg.i`, `.i-lg`, `.i-xl` | Lucide, 2px stroke, decorative beside words |
| Utilities | `.nowrap`, `.clamp-2`, `.clamp-3`, `.visually-hidden`, `.skip-link`, `.muted`, `.small`, `.numeric`, `code`, `.code-block`, `.stack-1`, `.stack-2`, `.stack-4` | Stacks put children one under another with a 4, 8 or 16px gap |

### Shell
| Component | Classes | Notes |
|---|---|---|
| Side menu (rail) | `.rail`, `.rail__brand` and `.rail__name` (logo with the name underneath), `.rail__logo` (logo only), `.rail__search`, `.rail__end`, `.rail__version`, `.with-rail` | Both apps; hidden on phones. `.rail__search` comes straight after the brand. The app's version, "v0.9.1", sits at the bottom in `.rail__end > .rail__version`: plain text, not a link |
| Header | `.site-header`, `.site-header--no-rail` (pages without a rail: name and logo start row 1), `.site-header__bar`, `.site-header__brand`, `.site-header__search`, `.site-header__search-btn` (phones), `.site-header__server` (the server name, start of the level 1 menu), `.site-header__actions`, `.site-header__tabs` | Row 1: 1st level, search, Help, Display. Row 2: 2nd level, only when the page has tabs. Nothing else. Help opens the help centre article for the page you are on, not the help centre's front page: the article for what the page does, or the help index's section when no one article covers the page. Its hidden text names the article's subject ("Help with checking your disks' health (opens in a new tab)"). Every page with the header has its own link, kept in one list in the app, and the app's build stops if a page has none or an article is missing |
| Menu tabs (level 1 and level 2 menus) | `.menu-tabs`, `.menu-tabs__label`, `.is-compact` | Icons and names; icons only when they do not fit; current page bar |
| Count and update dot | `.count`, `.update-dot` | Meaning in hidden text |
| Phone menu | `.phone-menu-button`, `.phone-menu`, `.phone-menu__section > a` (an item with no 1st level), `.phone-menu__search`, `.phone-menu__section`, `.phone-menu__foot` | Drawer from the left; search, main menu, 1st level; the version and sign out at the foot |
| Page and page head | `.page`, `.page--narrow` (Sign in, Set up), `.section-head`, `.section-head__control`, `.page-head`, `.page-head__text`, `.page-head__summary` | One visible h1; page actions on the right |
| Settings: Updates | the 2nd level menu | Settings, Updates has three pages: Update settings (the version, how to update, what the app can access, About), Releases (the Releases accordion) and Restore (a Restore your settings accordion with the saved copies and Restore from a file, then Go back to an earlier version) |
| Sign out | `.btn` with the `log-out` icon in `.page-head .actions` | On every Settings page, beside the page title, so it is always one step away on a computer. Not in the Settings menu: with it there the menu falls back to icons only. Phones keep Sign out at the foot of the phone menu as well |
| Footer | `.site-footer`, `.site-footer__app`, `.site-footer__brand`, `.site-footer__links`, `.site-footer__maker`, `.maker-mark` | On every page but Sign in and Set up. Left: app icon and name, then Help (only when the app has a help centre), Release notes (opens the release notes slide-out), the app's GitHub repository, and About and updates, with "Upgrade available" when a newer release is out. The version is not in the footer: it is at the bottom of the side menu and the phone menu. Right: the dinosaur mark and TheMightyTRexUK, one link to the GitHub profile (copy the markup from the gallery) |
| Display button | `.icon-btn` (sun icon, `.label` Display), `aria-haspopup="dialog"`, opening a `.side-panel` titled Display and accessibility; inputs with `data-display`, `data-display-save`, `data-display-reset` | Last item in the header on every page. The choices and their order are in `ACCESSIBILITY.md` section 1 |

### Actions
| Component | Classes | Notes |
|---|---|---|
| Button | `.btn`, `.btn--primary`, `.btn--quiet`, `.btn--danger`, `.btn--compact` | One primary per view; words say what happens. **Where buttons sit** (TheMightyTRexUK, 7 November 2026): in every dialog, slide-out and wizard foot the buttons start on the left, the main action first, then Cancel or Back. A slide-out's danger button (Remove app) and a wizard's Skip this step sit on their own on the right. On phones a dialog's buttons take the full width, the main action on top. Never right-aligned with the main action last |
| Icon button | `.icon-btn`, `.icon-btn--bare` | Always named, including the thing it acts on |
| Split button | `.split-btn` | Main action plus a menu of related ones |
| Menu button and menu | `.menu-wrap`, `.menu`, `.menu__label`, `role="menu"` items | Related actions in one button (the Lists menu); sort as `menuitemradio` |
| Copy button | `.copy-btn`, `data-copy` | Confirms in a status message |
| Action row | `.actions` | |

### Inputs
| Component | Classes | Notes |
|---|---|---|
| Links that open a new tab | `a[target="_blank"]` with the `external-link` icon last | Every link that opens a new tab shows the `external-link` icon after its words and says "(opens in a new tab)" for screen readers, such as a provider's site in a list (TheMightyTRexUK, 7 November 2026). Help that opens in a new tab uses `help-new-tab` in front instead |
| Field | `.field`, `.field__label`, `.hint`, `.field-error`, `.field__required`, `.required-key` | Label above, hint, error that says how to fix it. **Required fields** (TheMightyTRexUK, 7 November 2026): a required field's label ends with `<span class="field__required" aria-hidden="true">*</span>` and its control has `required` (or `aria-required="true"` for a group of choices); the key, "* = Required" (`.required-key`), is not in the form: it goes at the bottom of the help slide-out opened from a form or step that has a required field, because most people know the star and the help is where it is explained (TheMightyTRexUK, 7 November 2026). Optional fields are not marked |
| Text, select, text area | `.input`, `.select`, `.textarea` | 44px; `aria-invalid` shows the error border. `readonly` (TheMightyTRexUK, 10 November 2026): a sunken box with a dashed edge for a value the app filled in and uses itself, such as the setup code from the installer's link; its hint says so |
| Search field | `.search-field` | A box with a Search icon button inside it at the right (the default for every `input type="search"`, added by components.js; opt out with `data-no-search-icon`) |
| Input with unit | `.input-group`, `.input-group__unit` | |
| Checkbox and radio | `.check`, `.check__text`, `.check__hint` | 22px box, 44px row |
| Switch | `.switch` with `role="switch"` | For settings that apply at once |
| Segmented control | `.segmented` | Two to five short options (theme, text size, view, cover size) |
| Option cards | `.option-cards`, `.option-cards--row` (side by side), `.option-card` | Choices that need a line of explanation; text stays at the top of each card |
| Filter chips | `.filter-chips`, `.filter-chip` with `aria-pressed` | In toolbars |
| Sortable list | `.sortable`, `.sortable__row`, `.sortable__handle`, `.sortable__label`, `.sortable__meta`, `.sortable__moves` with `[data-move="up"]` and `[data-move="down"]`; `.sortable__row--marker`, `.sortable__row--off` | Rows in an order the person sets, such as Reelix's qualities best first (UX-51, TheMightyTRexUK, 10 November 2026). Move up and Move down on every row are the keyboard, screen reader and phone way; the handle drags with a mouse or finger. Each button's label names its row ("Move 1080p web up"). Buttons are never disabled: at an end the status says so. A marker row (Stop upgrading here) moves like any row. Each move announces the new place and fires `sortable-change` with `detail.order` (each row's `data-value`) |
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
| Table | `.table-wrap[data-stack]`, `.table`, `th[aria-sort]`, `.table--middle` | Real tables only; stack into cards on phones. A row's heading (`th scope="row"`) looks like its cells, in bold. `.table--middle` puts every cell on the row's middle line, for a summary with a button on each row, such as a wizard's Check step with Change (7 November 2026) |
| Tables that line up | `.table.table--fixed` with the same `<colgroup>` in each; `col.col-id`, `.col-date`, `.col-state`, `.col-number`, `.col-quarter`, `.col-third`, and no class on the column that takes the rest | Several tables one after another, such as tasks by category or a menu by section, keep their columns in line (4 November 2026) |
| Notice and callout | `.notice[data-tone]` (`success`, `warning`, `danger`, `muted`; none is info), `.notice__title`, `.notice__body` | Icon and words; `role="status"` or `role="alert"`. As a callout in long text, the title is the lead word: Before you begin (info), Limitation (warning), Warning (danger, cannot be undone), Tip (success), Example (muted) |
| Prose | `.prose`, `.prose__lead`, `.prose__kind` | Help topics, guides and release notes shown in an app (`HELP-WRITING.md`) |
| Time ago | `<time datetime>` with `.visually-hidden` exact time | "Updated 10 seconds ago" on screen, the exact time for screen readers |
| Empty state | `.empty`, `.empty__icon` | What, why, one next step |
| Loading | `.skeleton`, `.loading-bar[data-active]`, `aria-busy` | Skeletons in the shape of the content |
| Toast (option C) | `.toasts`, `.toast[data-tone="success"\|"info"\|"warning"\|"danger"]`, `.toast__text`, `.toast__title`, `.toast__detail`, `.toast__action`, `.toast__close`; `SharedComponents.toast(title, { detail, tone, action })`, `toast.error(...)`, `toast.warning(...)` | Card in the corner (full width on phones), status edge and icon, up to three stacked; a new one never pushes out an error. Success and info 5 seconds (10 with an action), warning 10, error until closed; waits under the pointer or focus. Errors read out at once |
| Saved note (option D) | `.saved-note`; `SharedComponents.savedNote(element)` | Settings pages: "Saved at 16:31" beside the button that saved, instead of a toast; goes at the next change |
| Icons in built parts | `data-sprite` on the `components.js` script tag, or `window.SharedComponentsSprite` | The toast and saved note draw icons as `<use href="#i-name">`. An app whose icons are in a separate file names it (Starboard: `/icons/sprite.svg`), or the icons and Close button are blank |
| Help | `.help`, `.help__text` | A disclosure button, not a hover tooltip |
| Disclosure | `.disclosure` (`details`), `.disclosure__body`, `.disclosure__meta` | SMART report, advanced settings, Restore your settings |
| Releases | `.disclosure.release`, `.release__date`, `.release__counts`, `.release__type[data-type="added|changed|deprecated|removed|fixed|security|settings"]`, `.releases-head` | Each release in its own accordion, newest first, the installed one open, with Open all. Summary: "Version 0.9.1" as a heading, an Installed chip, the date, and a count chip for each type of change (added success, changed info, fixed warning, security danger, deprecated and removed muted). Body: each type with a bar in its colour, every change as a bold title and one sentence, then Your settings and the way back on a sunken background, and a link to the release on GitHub. On the app's Releases page (Settings, Updates); the footer's Release notes slide-out shows the same notes |
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
| A to Z jump list | `nav.az-jump > ol > li > a.az-jump__letter`, `[aria-disabled="true"]`, `[aria-current="location"]`, `.wall-letter` headings (`#letter-a`, `#letter-num`) | Over a long wall: # then A to Z from the sort title, accents folded; letters with nothing shown but not choosable ("Q, no titles"); sticky under the header; 44px targets; one Tab stop with Arrow keys, Home and End; focus moves to the heading after a jump; sideways scrolling on phones. `SharedComponents.azLetter`, `azJump`, `azGo` and the `az-jump` event |
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
| Help links | `.help-links`, `.help-link` (a button), opening a slide-out (`.side-panel`) titled with the link's question | "What is…" and "Which one is right for me?" at the end of the part of a page they explain. Every piece of in-page help works this way: never a fold-out (`details`), never a dialog. Help that is an article in the help centre is shown in the slide-out too, with "Read it in the help centre" in its foot. **Two help icons, both square** (TheMightyTRexUK, 7 November 2026): `help` (a question mark in a square) for help that opens in the page, in a slide-out; `help-new-tab` (the square opening at the top right, with the new-tab arrow) for help that opens in a new tab: the header's Help and "Read it in the help centre". Never `circle-help` for help. A link that opens a new tab also says "(opens in a new tab)" for screen readers |
| Address | `.address` with `.copy-btn` (`data-copied="Address copied"`) | A server address as a link that opens in a new tab, with a copy button |
| Settings rows | `.settings-section`, `.settings-section__head`, `.settings-rows`, `.setting`, `.setting--opens`, `.setting__text`, `.setting__label`, `.setting__hint`, `.setting__control`, `.settings-section__head--action` | Things with several fields open a slide-out |
| Panel header | `.panel-header`, `.panel-header__title`, `.panel-header__brand`, `.panel-header__actions` (Previous, Next) | The same bar on slide-outs, dialogs and the phone menu; on slide-outs and the phone menu it wears the page background (`--color-slide-header`) |
| Slide-out | `.side-panel-layer`, `.side-panel-backdrop`, `.side-panel`, `.side-panel--wide`, `.side-panel__body`, `.side-panel__foot`, `.side-panel__lead` | From the right; 420px, 640px wide, full width on phones; header in the page background, body and foot on the raised surface |
| Dialog | `.dialog` (`<dialog>`), `.dialog__body`, `.dialog__foot`, `.dialog--scroll`, `data-close-outside` | Decisions and short tasks only. `.dialog--scroll`: only the body scrolls, the header and foot stay in view. `data-close-outside`: a press outside closes it (help only, never a dialog with fields) |

## Slide-out, dialog or page

| Use | When | Examples |
|---|---|---|
| Slide-out | Details of one item in a list, or editing it, where seeing the list still helps; longer reading beside the page | Book summary; a request; a download client, indexer, reading account or user; a log entry; an app, disk, download or backup run on Starboard; release notes; Display and accessibility; a wizard's "What is…" help |
| Dialog | A decision or short task that must finish before going on; one or two fields | Confirm remove or reset; Add list; a password check before a download or restore |
| Page | Something people return to, link to or spend time in | Book, author, series and narrator pages; Disk health; each Settings section; Upgrade wizard |
| In place | A small change to a value already in view | Switches and selects in settings rows; filter chips; cover size |

**Slide-out widths** (TheMightyTRexUK, 7 November 2026): release notes and help take about half the screen (`.side-panel--wide`, at least 640px); every other slide-out takes about a third (at least 420px, `--panel-w`). On phones both take the whole width.

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

**Keeping them in step (TheMightyTRexUK, 2 November 2026: the library is shared by both apps and kept up to date):**
change the component here first, never in an app, and follow the steps in
[Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html). Add the change to the Decisions list in this file, commit it here and
push, so every checkout picks it up.

**Decisions:** which item to use (Starboard DASH-309, 12 November 2026): `DESIGN-SYSTEM.md` section 10 picks rows, cards, chips, filters, toolbars, notices, toasts, dialogs or tables by what the thing is; accent teal (UX-02 option B); status chip style B, outline with icon (UX-04); cover actions (UX-42: `.cover-card` with `.cover-actions` on the cover by default, beside it as a per-account setting); shelves without scroll bars (UX-30 option A: `.shelf-scroller`, arrows over an edge fade); covers always line up (`.media-card` titles take two lines); small covers (UX-44: `.book-row` with `.cover-actions--row` in rows, `.cover-card__more` with the actions in words on small tiles); square radio art in the book shape (FEAT-R decision 2, fill 4: `.show-art`, label in the image's colour) and `.logo-tile`; slide-outs look like slide-outs (TheMightyTRexUK, 2 November 2026: `--color-slide-header`, the page background, on slide-out and phone menu headers over a raised-surface body; dialogs keep the plain header; Display and accessibility and Release notes are slide-outs). App logos without a tile (TheMightyTRexUK, 2 November 2026: `.app-icon.has-image` is just the image, with no border or background; initials keep the tile). The logo editor on every way to get a logo (TheMightyTRexUK, 2 November 2026: From a cover, Find online and Upload your own all use the box, Shape from lightness or transparency, four cleaning levels, and a small eraser and paintbrush on `.checker[data-tool]`; found files show as plain pictures in `.logo-candidate__art > img`). Nicer scroll bars (TheMightyTRexUK, 2 November 2026): thin and square in every scrolling area, `--color-scrollbar` (the border colour, the text colour in High contrast) on a clear track; they stay visible, and only shelves hide theirs behind arrows. UX notes for testing (TheMightyTRexUK, 2 November 2026): `ux-notes.js` (copied to both apps by sync.py) puts Note an issue in the corner of every page while an app's testing setting is on; choose the part (click, or Tab and Enter), say what is wrong, the kind and how bad; Notes lists them with Copy as text, Download and Mark as fixed. Notes keep the page, the part, a selector and the display settings. An app passes a store to keep them on its server; otherwise they stay in the browser. Styles: `.ux-dock`, `.ux-banner` (at the bottom, clear of the header), `.ux-outline`, `.ux-notes`. Security checks the same in both apps (TheMightyTRexUK, 3 November 2026): `docs/SECURITY-CHECKS.md` sets the checks (tests, live journeys, Trivy, ZAP on a private network, Gitleaks, Bandit and Semgrep, ShellCheck, Hadolint, CodeQL, a separate review, install tests), how to sort findings, a security page in each app with a "Security checks for each release" table, and a Security section in every release's notes (`CONTENT-DESIGN.md`, release notes). Starboard is the worked example; Storyarr has to catch up. Focus not obscured (WCAG 2.2, 4 November 2026): the page keeps the sticky header (and row 2) and an open save bar clear when it scrolls, with `scroll-padding` on `:root`; `WCAG.md` and `ALT-TEXT.md` added after the GOV.UK Service Manual and BBC GEL. Search is always one button away (TheMightyTRexUK, 4 November 2026: "update the design system to ensure there is a search button"): `.rail__search` is first in the rail, under the logo, and moves focus to the header's search box; on phones, where the box is hidden, `.site-header__search-btn` in the header opens the same box as a row under the header, and Escape or a press outside closes it and returns focus to the button that opened it. Both use `data-search-open` and `aria-controls` (`setupSearch()` in `components.js`). No single-key shortcut (WCAG 2.1.4). The `radio` icon is added. Wizard rules (TheMightyTRexUK, 4 November 2026): `docs/WIZARD.md` sets one set of rules for every wizard, from the installer mock-up: the first question asks which job, each with its own wizard; one question per step; steps that do not apply left out; a step in parts has `.steps--sub`, as wide as the progress bar with a line between parts, numbered 1, 2, 3, each part counting in the progress bar's total, and on phones only the numbers, with ticks for done parts; "(recommended)" with a reason, never "easiest"; "What is…" help at the end of the part it explains, in a dialog that scrolls inside and closes on a press outside; addresses as links with copy; a summary of what was set and skipped. What happens next and the decision tree are review aids for testing only, never in the finished product. Copying falls back to a hidden text box on plain http (`copyText()` in `components.js`), and a dialog returns focus to the button that opened it. Step numbers grow with Text size. Changelogs (TheMightyTRexUK, 5 November 2026): `docs/CHANGELOGS.md` sets one way to keep `CHANGELOG.md` in every project, after Keep a Changelog 1.1.0: for people, never a commit log; an Unreleased section at the top; every version newest first, linked, as `## [x.y.z] (day month year)`, with dates as in `CONTENT-DESIGN.md` rather than year, month, day; changes under Added, Changed, Deprecated, Removed, Fixed and Security only; withdrawn releases marked `[Withdrawn]`. In-app release notes use the same six types. Terminal wizards and feedback (TheMightyTRexUK, 5 November 2026): `docs/TERMINAL.md` sets how a wizard looks in a terminal (boxed with a heading box reading "App | step", a progress bar and a menu fixed on the bottom line with b Back, ? Help, f Feedback and q Stop; or plain numbered lines for screen readers, never redrawn), with help as a box over the step and feedback sent as a QR code sized to the window; `docs/WIZARD.md` section 12 puts Snaglist on every wizard step, naming the step, with Show as a QR code for a computer that is not online yet.

## Help centre (7 November 2026)

Every app's help is Markdown in its own repository, published as web pages by one builder,
`tools/help_centre/build.py`, with this library's tokens, components, fonts and icons. Agreed by the owner on
7 November 2026, after a check with axe-core (WCAG 2.2 AA): no problems on 25 combinations of page, light and dark
theme, desktop and phone, and open menu, search and Display.

**Layout**

- **Header:** logo and name, search, Display. On phones it is one bar: **Menu**, logo, **Search** and **Display**
  as icon buttons with their names kept for screen readers. **Search** opens the search bar under the header with
  the cursor in it; Escape or the button again closes it and returns the focus to the button.
- **Banner** (optional, `banner` or `banners` in `help-centre.json`): a labelled region under the header (for
  example "Ad"), with a button to hide it, remembered in the browser. Its links to other sites carry
  `rel="sponsored"`. With `banners` (up to six), each page shows one and the next page shows the next one in turn,
  chosen before the page draws; nothing moves or changes while a page is open, so there is no carousel to pause.
- **Left menu:** the help home's own lists, one group for each heading, each opening and closing with a button
  (`aria-expanded`, `aria-controls`). The page you are on has `aria-current="page"` and is scrolled into view.
  **Hide the menu** and **Show the menu** keep the choice. On tablets and phones the menu opens from **Menu**, over
  the page, scrolls inside itself, keeps the page behind still, and closes with Escape or when an article is chosen.
- **Article:** breadcrumbs from the article's first line, the kind (How-to, Reference), `.prose`. A wide table is a
  labelled region the keyboard can reach and scroll.
- **On this page:** a small menu on the right listing the article's sections, marking the one being read with
  `aria-current="location"` as you scroll. On phones it opens inside the article as a disclosure.
- **Footer:** an optional note on every page (`footer_note`), then links to the help home, the repository and
  reporting a problem with the help.
- **Display and accessibility:** the same choices and classes as the apps (theme, text size, reduce motion, high
  contrast, underline links, wider text spacing), applied before the page draws.
- **Search:** a page that searches every article in the browser; every word must appear, titles count most.

**For each app:** a `help-centre.json` at its root (name, repository, site address, help folder, logo, and the
optional `leave_out`, `sections`, `footer_note`, `banner` or `banners`, `sponsored_links`, `strip_between`, `search_example`,
`front_door`), and a workflow that checks out this repository and runs the builder. Starboard and Snaglist use it.
Build one here with `tools/help_centre/build.sh` from the app's folder.

## App-only patterns (2 November 2026)

Built from the tokens, used by one app, so not in `components.css`:

- **Starboard:** `.access-change` (what Starboard can access, with the command to change it), `.job-run` (a server job
  with Run now), the storage charts (`--media-*` map to `--series-*`), the release notes slide-out
  (`.release-notes`, opened from Release notes in the footer).
- **Storyarr:** the bookshelf and series views.


- 11 November 2026: `--font-heading` (headings h1 to h4) and `--color-rail` (the side menu) are optional, for Starboard's styles. Unset, nothing changes.
