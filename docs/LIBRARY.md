# TRex Design System: the component library

Version 1, 2 November 2026. One component library for both apps, so they share one design and one behaviour.
It follows `DESIGN-SYSTEM.md` and the guides in this folder (`CONTENT-DESIGN.md`, `HELP-WRITING.md` and `ACCESSIBILITY.md`).
File names in the tables in this guide are relative to the root of the repository.

**Open `gallery.html` in a browser**: every component in it works as it does in the apps. The gallery uses the same header and menus
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
| `accent-report.txt` | Made by `tools/check_accents.py --report accent-report.txt`: every token pair the components draw, for every accent colour, in all four themes, including the menu hover fill and its edge; all pass WCAG 2.2 AA |
| `areas/` | Design boards for every area of both apps, using the library, with slide-outs where they fit |
| `tools/build.py` | Turns `{{i:name}}` into icons and `<!--ICONS-->` into the sprite for any `*.src.html` |
| `tools/icons.py` | Rebuilds `icons.svg` from Lucide in Storyarr's `node_modules` |
| `tools/sync.py`, `tools/paths.py` | Copies the library into both apps; `paths.py` says where the apps are (`tools/paths.local.json`, not committed) |

## Principles

1. **One design, two apps.** Same tokens, same classes, same behaviour. An app may add its own components
   (charts on Starboard, the bookshelf on Storyarr) but builds them from the tokens.
2. **Accessible is the baseline.** WCAG 2.2 AA in every theme; 44px controls and targets; a visible 3px focus
   ring; status always in words plus a shape or icon, never colour alone; keyboard first; everything works at
   175% text and with wider spacing; nothing moves when Reduce motion is active.
3. **Mica, calm and dense enough.** 6px corners, one typeface, card edges and rules in one colour, one accent
   colour, one primary button per view. The dashboard card is the model for panels, settings sections, tables,
   slide-outs and dialogs: a grey band on top, the body under it.
4. **Things open where they make sense.** Slide-out for the details or editing of one item in a list; dialog
   for a decision; page for something people return to. Read "Slide-out, dialog or page" in this guide.

## Menu names

Names (TheMightyTRexUK, 4 November 2026: "Side menu, Level 1 menu and Level 2 Menu"):

- **Side menu:** the icon rail on the left, in both apps: the logo with the app's name underneath, Search,
  then the sections. Starboard moves to the side menu (TheMightyTRexUK, 4 November 2026), with Library, Discover,
  Activity, System and Settings; read the Starboard menu board, `areas/starboard-menu.html`.
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
| Accent colours | `palettes/teal.css`, `indigo.css`, `forest.css`, `plum.css`, `ember.css`, `graphite.css` (Blue, the default, is `tokens.css`; Teal is the colour before Mica) | An accent over Mica's neutral greys: load `tokens.css`, one palette, then `components.css`. Each sets the accent, its soft tint, the chosen item, the count and the logo in Light, Dark, High contrast and High contrast dark (a stronger shade, 7:1). Surfaces, text, focus, status colours and chart series stay the same. Written by `tools/palettes.py` and checked by `tools/check_accents.py`. For an app where people choose (Starboard's own style), `palettes/app-palettes.css` holds all six under `:root[data-palette="…"]`; `tools/sync.py` copies it to Starboard's `css/palettes.css` with `palettes.json`. An app's own styles still win |
| Type | `--text-xs` to `--text-2xl`, `--font` | One typeface; scales with Text size |
| Space and size | `--space-1` to `--space-12`, `--control-h` (44px), `--control-h-compact` (32px, dense tables only) | |
| Icons | `icons.svg`, `svg.i`, `.i-lg`, `.i-xl` | Lucide, 2px stroke, decorative beside words |
| Utilities | `.nowrap`, `.clamp-2`, `.clamp-3`, `.visually-hidden`, `.skip-link`, `.muted`, `.small`, `.numeric`, `code`, `.code-block`, `.stack-1`, `.stack-2`, `.stack-4` | Stacks put children one under another with a 4, 8 or 16px gap |

### Shell
| Component | Classes | Notes |
|---|---|---|
| Side menu (rail) | `.rail`, `.rail__brand` and `.rail__name` (logo with the name underneath), `.rail__logo` (logo only), `.rail__search`, `.rail__end`, `.rail__version`, `.with-rail` | Both apps; hidden on phones. `.rail__search` comes straight after the brand. The app's version, "v0.9.1", sits at the bottom in `.rail__end > .rail__version`, a link to the app's update page. When a newer release is out, an `.update-dot` sits directly before the number inside the link and pulses gently (still when Reduce motion is active), and the link's hidden text and title say "update available" with the version |
| Header | `.site-header`, `.site-header--no-rail` (pages without a rail: name and logo start row 1), `.site-header__bar`, `.site-header__brand`, `.site-header__search`, `.site-header__search-btn` (phones), `.site-header__server` (the server name, start of the level 1 menu), `.site-header__actions`, `.site-header__tabs` | Row 1: 1st level, search, Help, Display. Row 2: 2nd level, only when the page has tabs. Nothing else. Help opens the help centre article for the page you are on, not the help centre's front page: the article for what the page does, or the help index's section when no one article covers the page. Its hidden text names the article's subject ("Help with checking your disks' health (opens in a new tab)"). Every page with the header has its own link, kept in one list in the app, and the app's build stops if a page has none or an article is missing |
| Menu tabs (level 1 and level 2 menus) | `.menu-tabs`, `.menu-tabs__label`, `.is-compact` | Icons and names; icons only when they do not fit; current page bar |
| Count and update dot | `.count`, `.update-dot` | Meaning in hidden text |
| Phone menu | `.phone-menu-button`, `.phone-menu`, `.phone-menu__section > a` (an item with no 1st level), `.phone-menu__search`, `.phone-menu__section`, `.phone-menu__foot` | Drawer from the left; search, main menu, 1st level; the version and sign out at the foot |
| Page and page head | `.page`, `.page--narrow` (Sign in, Set up), `.section-head`, `.section-head__control`, `.page-head`, `.page-head__text`, `.page-head__summary` | One visible h1; page actions on the right |
| Settings: Updates | the 2nd level menu | Settings, Updates has three pages: Update settings (the version, how to update, what the app can access, About), Releases (the Releases accordion) and Restore (a Restore your settings accordion with the saved copies and Restore from a file, then Go back to an earlier version) |
| Sign out | `.btn` with the `log-out` icon in `.page-head .actions` | On every Settings page, beside the page title, so it is always one step away on a computer. Not in the Settings menu: with it there the menu falls back to icons only. Phones keep Sign out at the foot of the phone menu as well |
| Footer | `.site-footer`, `.site-footer__app`, `.site-footer__brand`, `.site-footer__links`, `.site-footer__maker`, `.maker-mark` | On every page but Sign in and Set up. Left: app icon and name, then Help (only when the app has a help centre), Discord support server (only when the app has one: opens in a new tab, with the external-link icon and the hidden words "(opens in a new tab)"), Release notes (opens the release notes slide-out), the app's GitHub repository, and About and updates, with "Upgrade available" when a newer release is out. The version is not in the footer: it is at the bottom of the side menu and the phone menu. Right: the dinosaur mark and TheMightyTRexUK, one link to the GitHub profile (copy the markup from the gallery) |
| Display button | `.icon-btn` (sun icon, `.label` Display), `aria-haspopup="dialog"`, opening a `.side-panel` titled Display and accessibility; inputs with `data-display`, `data-display-save`, `data-display-reset` | Last item in the header on every page. The choices and their order are in `ACCESSIBILITY.md` section 1 |
| Page banner | `.page-banner[data-tone]`, `.page-banner__text`, `.page-banner__actions`; `SharedComponents.pageBanner(title, { text, tone, action })` returns the function that takes it away | One message for the whole app that stays while its state lasts (Connection lost, Restart needed, Read only), directly after `.site-header`, before the page (20 November 2026). Not for one page (`.notice`) or a result (a toast); a restart of one app stays in its place (DASH-470). One at a time. It does not stick, so it never covers focus. `pageBanner()` says it once: danger through the alert region, the rest politely |
| Popover | `.popover-wrap`, `.popover[data-align="start"]` (`role="dialog"`, not modal, `aria-labelledby` its heading), `.popover__head`, `__body`, `__body--flush`, `__foot`; `[data-popover][aria-controls]` on the button; `popover-open` and `popover-close` events | A small layer from a button to read and act on without leaving the page (20 November 2026). Focus moves to its heading (or `[data-autofocus]`); Escape returns it to the button; a press outside or Tab out closes it. Full width under the header on phones. Not for actions alone (`.menu`), a task (slide-out or dialog) or help (help links) |
| Alerts centre | `.popover[data-alerts]`, `ul.alerts`, `li.alerts__item[data-unread][data-tone][data-id]`, `.alerts__unread` (hidden "Unread: "), `.alerts__title` (a link), `.alerts__time`, `.alerts__read` (icon button "Mark as read: <alert>"), `[data-alerts-read-all]`; the button holds `.count` with hidden " unread"; `alerts-read` event with `{ ids }` | Header button "Alerts" (Starboard's word, `CONTENT-DESIGN.md` section 5) opening the newest alerts, with All alerts in the foot (20 November 2026). Unread: a dot, bold words and hidden text. Opening one or Mark as read marks it; focus stays on the alert; Mark all as read keeps focus and says so |
| Command palette | `[data-command-palette]` on its button (`.btn.command-palette-open` with `kbd` Ctrl K), `[data-command]` on buttons it should list, `.command-palette`; `SharedComponents.commandPalette.items = () => [{ label, hint, keywords, href \| run }]` | Find a page or action by name and go with Enter (20 November 2026). Ctrl+K or Command+K opens it as well as the button; `data-no-shortcut` on `<html>` takes the shortcut away (an app's setting, WCAG 2.1.4). A dialog holding the combobox, always open; it lists the side menu, menu tabs and phone menu links unless the app gives its own. Never the only way to anything |

### Actions
| Component | Classes | Notes |
|---|---|---|
| Button | `.btn`, `.btn--primary`, `.btn--quiet`, `.btn--danger`, `.btn--compact` | One primary per view; words say what happens. **Where buttons sit** (TheMightyTRexUK, 7 November 2026): in every dialog, slide-out and wizard foot the buttons start on the left, the main action first, then Cancel or Back. A slide-out's danger button (Remove app) and a wizard's Skip this step sit on their own on the right. On phones a dialog's buttons take the full width, the main action on top. Never right-aligned with the main action last |
| Icon button | `.icon-btn`, `.icon-btn--bare` | Always named, including the thing it acts on |
| Split button | `.split-btn` | Main action plus a menu of related ones |
| Menu button and menu | `.menu-wrap`, `.menu`, `.menu__label`, `role="menu"` items | Related actions in one button (the Lists menu); sort as `menuitemradio`. Something to read and act on is a popover instead |
| Copy button | `.copy-btn`, `data-copy` | Confirms in a status message |
| Action row | `.actions` | |

### Inputs
| Component | Classes | Notes |
|---|---|---|
| Links that open a new tab | `a[target="_blank"]` with the `external-link` icon last | Every link that opens a new tab shows the `external-link` icon after its words and says "(opens in a new tab)" for screen readers, such as a provider's site in a list (TheMightyTRexUK, 7 November 2026). Help that opens in a new tab uses `help-new-tab` in front instead |
| Play in another app (Starboard, DASH-480) | `a.btn` (`.btn--primary` when it is the page's main action) with the `play` icon first and the `external-link` icon last | A link that opens a film or episode in the media server's own player, in a new tab, styled as a button. Visible word "Play"; screen readers hear the item and the app as well: "Play The Lost Valley in Jellyfin (opens in a new tab)". Always the full 44px button, never `.btn--compact`, as it can be the only way to play. Only where the app has the item and an address a browser can open is known: the app's address for browsers, or, when its only address is local to the server (127.0.0.1), the host the page was opened with and the app's port, as other Open links do; never an address only the server can reach, such as a container's name. Not in the app yet: no link, and words where it would be ("Not in Jellyfin yet"). No address can be made: one info notice that names where to add it, with a link to that setting, in place of links that would fail |
| Field | `.field`, `.field__label`, `.hint`, `.field-error`, `.field__required`, `.required-key` | Label first, then hint, then error that says how to fix it. **Required fields** (TheMightyTRexUK, 7 November 2026): a required field's label ends with `<span class="field__required" aria-hidden="true">*</span>` and its control has `required` (or `aria-required="true"` for a group of choices); the key, "* = Required" (`.required-key`), is not in the form: it goes at the bottom of the help slide-out opened from a form or step that has a required field, because most people know the star and the help is where it is explained (TheMightyTRexUK, 7 November 2026). Optional fields are not marked |
| Text, select, text area | `.input`, `.select`, `.textarea` | 44px; `aria-invalid` shows the error border. `readonly` (TheMightyTRexUK, 10 November 2026): a sunken box with a dashed edge for a value the app filled in and uses itself, such as the setup code from the installer's link; its hint says so |
| Search field | `.search-field` | A box with a Search icon button inside it at the right (the default for every `input type="search"`, added by components.js; opt out with `data-no-search-icon`) |
| Input with unit | `.input-group`, `.input-group__unit` | |
| Checkbox and radio | `.check`, `.check__text`, `.check__hint` | 22px box, 44px row |
| Switch | `.switch` with `role="switch"` | For settings that apply at once |
| Segmented control | `.segmented` | Two to five short options (theme, text size, view, cover size) |
| Option cards | `.option-cards`, `.option-cards--row` (side by side), `.option-card` | Choices that need a line of explanation; text stays at the top of each card |
| Filter chips | `.filter-chips`, `.filter-chip` with `aria-pressed` | In toolbars |
| Sortable list | `.sortable`, `.sortable__row`, `.sortable__handle`, `.sortable__label`, `.sortable__meta`, `.sortable__moves` with `[data-move="up"]` and `[data-move="down"]`; `.sortable__row--marker`, `.sortable__row--off` | Rows in an order the person sets, such as Reelix's qualities best first (UX-51, TheMightyTRexUK, 10 November 2026). Move up and Move down on every row are the keyboard, screen reader and phone way; the handle drags with a mouse or finger. Each button's label names its row ("Move 1080p web up"). Buttons are always available: at an end the status says so. A marker row (Stop upgrading here) moves like any row. Each move announces the new place and fires `sortable-change` with `detail.order` (each row's `data-value`) |
| Applied filters | `.applied`, `.applied__item` | Each removable, plus Clear all |
| Form layout | `.form-grid`, `[data-span="all"]`, `fieldset` | |
| Folder picker | `.folder-field`, `.folder-places` with `.folder-place` (`__icon`, `__text`, `__name`, `__detail`), `.folder-pathbar`, `.folder-crumbs`, `.folder-list` (`role="listbox"`) with `.folder-row` (`__name`, `__meta`) | Idea A (TheMightyTRexUK, 16 November 2026): a slide-out that opens on places (This computer, each disk, and each network share and cloud service where the page brings things in from them), then one list of folders with a path bar (Back, then where you are) and each folder's size and what is in it, counted after the list shows ("Counting…" until then). Use this folder (primary) chooses the folder you are in. Back goes up, and from the top of a place to the places. Up and Down move, Enter or Right opens, Left or Backspace goes up, letters jump. Places are buttons, one Tab stop each. Every page that picks a folder uses this one. A terminal draws it as a numbered list with the path at the top (`TERMINAL.md`) |
| Combobox (searchable select) | `.combobox[data-combobox][data-noun][data-noun-one]`, `.combobox__input` (`role="combobox"`, `aria-autocomplete="list"`, `aria-expanded`, `aria-controls`), `__toggle` (`tabindex="-1"`, "Show all <noun>"), `__popup`, `__list` (`role="listbox"`), `__option` (`role="option"`, `data-value`, `data-hint`, `data-keywords`), `__hint`, `__none`, a hidden input; `SharedComponents.combobox(box, { options, onChoose, always })`; `combobox-change` event | ARIA 1.2 list autocomplete without automatic choice (20 November 2026). Focus stays in the box; `aria-activedescendant` and the focus ring mark the option the arrows reach. Down opens, Up and Down move, Enter chooses, Escape closes and then clears, Tab leaves; an exact name is kept on leaving, anything else goes back. The match is underlined, "No <noun> match" shows, and the number found is said politely after a pause, from a status inside the box. For more than about 15 options; fewer is a select or radios |
| Tag input | `.tag-input[data-tag-input]`, `.tag-input__list` (named like the field), `__tag`, `__field`, a hidden input with the words joined by commas; `tags-change` event | Short free words (words to skip, tags), 20 November 2026. Enter or a comma adds (pasted commas add several); leaving the box adds what is in it; a word already there says so. Each tag's Remove button is named "Remove <word>"; focus goes to the next one, or the box. Backspace in an empty box moves to the last Remove. Changes said politely |
| Secret field | `.secret-field[data-secret][data-name]`, `.secret-field__input` (`type="password"`, `readonly`), `[data-secret-show]` (`aria-pressed`), `[data-secret-copy]`, `[data-secret-replace]`; `secret-change` event with `{ value }` | An API key, token or password the app keeps (20 November 2026). Show and Hide named with the thing ("Show API key"), said politely. Copy confirms in a toast without the value. Replace empties the box with Save and Cancel (Enter and Escape); an empty Save shows the field's error. Set the value with `input.value`, never in markup; it is never in an attribute, a message, the title or the console. A key the server must not send back shows "Saved" and Replace only |
| Schedule picker | `fieldset.schedule[data-schedule]`, `.schedule__row`, `.schedule__days` (a fieldset named Days), `.schedule__day` (checkbox valued 0 to 6, short name shown, full name for screen readers), `.schedule__words` (`role="status"`); `[data-schedule-repeat]` (day, week, hour), `-time`, `-minute`, `-days`, `-words`, `-next`; `scheduleWords()`, `nextRun()`, `schedule-change` event | How often, which days and what time, read back in words ("Every weekday at 07:00", "Every hour at 15 minutes past") with the next run ("Next: tomorrow at 07:00"), 20 November 2026. 24-hour times. Days show only for On chosen days; the minute only for Every hour. Chosen days have a tick, not colour alone |
| Error summary | `.error-summary` (`role="alert"`, `tabindex="-1"`), `.error-summary__title`, `.error-summary__list`; `SharedComponents.showErrors(form, [{ field, message }])`, `clearErrors(form)`, `setFieldError(control, message)` | After GOV.UK (20 November 2026): at the top of a form after a failed submit, titled "There is a problem", focused, with "Error: " at the start of the page title. Each link uses the field's own error words and moves focus to the field with its label (or legend) in view. `showErrors()` also writes each `.field-error` (with hidden "Error: "), `aria-invalid` and `aria-describedby`. For forms of more than one field; a single inline-save field keeps its own error |

### Content
| Component | Classes | Notes |
|---|---|---|
| Settings helpers | `.inline-save`, `.form-stack`, `.setting__cost` | A field and its Save on one line; fields one under another; the muted line saying what a setting costs |
| Icon on a phone | `.btn--icon-on-phone` on a button with an icon | At 720px wide or less, the icon only, words kept for screen readers; for a repeated action in a list row, such as Watched (19 November 2026) |
| Section group | `section.settings-section.settings-section--group` holding `section.settings-section` cards with h3 headings | One topic with several cards, such as a plug-in's General (State, Versions, Jobs, What it may do, Remove); topic tabs give the group one tab (19 November 2026) |
| File picker | `.file-field` > `span.btn.file-field__button` (icon, words, `input[type=file]`) + `.file-field__name` (`.is-chosen` once a file is chosen) | Every file upload: a button in the site's style, "Choose a file", with the file's name and size beside it, then "Choose another file"; the real input lies over the button, so keyboards and screen readers work as usual. The form's button says what happens, such as "Upload and check" (owner, 19 November 2026) |
| Status chip | `.chip[data-tone]` | Word, shape and colour: dot, diamond (warning), square (danger), ring (muted). On a phone, a chip with an icon in a list row (`.rows .row`) shows its icon only; screen readers still read the words (19 November 2026) |
| Title with status | `.title-status`, `.title-status__chips` | A heading's status chips straight after the name, centred on its line; never on a line under it (read "Where status goes") |
| Status icon | `.status-icon[data-tone]` with `tabindex="0"` and `data-tooltip` | In a list of things with a state: an icon after the name, the word in hidden text and the library's tooltip (since 20 November 2026, not `title`, so keyboards reach it) |
| Tag | `.tag` | Format or kind, not status |
| Avatar, app icon | `.avatar`, `.app-icon`, `.app-icon--compact` (32px) | Initials on a tile when there is no logo; `.has-image` for a logo |
| Cover | `.cover`, `.cover--row` (48px in rows), `.cover__badge` | 2:3; square audio covers letterboxed |
| Facts | `.facts` (`dl`) | Author first, then Series; names are links |
| Stat | `.stats`, `.stat[data-tone]`, `.stat__value`, `.stat__label` | Edge colour plus words |
| Progress and meter | `.progress[data-tone]`, `.progress--busy`, `.progress--running`, `.meter`, `.meter__label`, `creepProgress()` | Value always in words. Waiting standard (DASH-493, TheMightyTRexUK, 20 November 2026): a bar that is working is 14px with rounded ends and moving stripes. `.progress--busy`: the end is not known, a striped band runs along. `.progress--running`: a count that is still going (such as 4 of 5); it starts with a visible piece and `creepProgress(bar, done, total, eachMs)` eases onto each count and creeps towards the next. Taken off when it ends; still with less motion asked for |
| Waiting mark and busy button | `.wait`, `.wait__mark`, `.btn[aria-busy="true"]` | Waiting standard, option A, the ring: a short wait shows the ring with words, never a plain "Loading…". A busy button draws the ring before its doing word ("Testing"), keeps its size and has `aria-disabled`. After 0.3 seconds the place the answer goes shows its waiting state; the end replaces it with the result, and focus moves to an error. With less motion the ring fades instead of turning |
| Rows | `.rows`, `.row`, `.row--no-lead`, `.row--opens`, `.row__title`, `.row__meta`, `.row__side` | `.row--opens`: the whole row opens a slide-out |
| Group heading | `.group-heading` | Sentence case, no capitals |
| Table | `.table-wrap[data-stack]`, `.table`, `th[aria-sort]`, `.table--middle` | Real tables only; stack into cards on phones. A row's heading (`th scope="row"`) has the same style as its cells, in bold. `.table--middle` puts every cell on the row's middle line, for a summary with a button on each row, such as a wizard's Check step with Change (7 November 2026) |
| Tables that line up | `.table.table--fixed` with the same `<colgroup>` in each; `col.col-id`, `.col-date`, `.col-state`, `.col-number`, `.col-quarter`, `.col-third`, and no class on the column that takes the rest | Several tables one after another, such as tasks by category or a menu by section, keep their columns in line (4 November 2026) |
| Notice and callout | `.notice[data-tone]` (`success`, `warning`, `danger`, `muted`; none is info), `.notice__title`, `.notice__body` | Icon and words; `role="status"` or `role="alert"`. As a callout in long text, the title is the lead word: Before you begin (info), Limitation (warning), Warning (danger, cannot be undone), Tip (success), Example (muted) |
| Prose | `.prose`, `.prose__lead`, `.prose__kind` | Help topics, guides and release notes shown in an app (`HELP-WRITING.md`) |
| Time ago | `<time datetime>` with `.visually-hidden` exact time | "Updated 10 seconds ago" on screen, the exact time for screen readers |
| Empty state | `.empty`, `.empty__icon` | What, why, one next step |
| Loading | `.skeleton`, `.loading-bar[data-active]`, `aria-busy` | Skeletons in the shape of the content. The loading line (TheMightyTRexUK, 12 November 2026): on the header's lower edge, shown while something takes longer than a moment, until it has loaded. Chase: a long and a short bar follow each other across; since 20 November 2026 (option E) 6px with moving stripes. With Reduce motion it does not slide; it fades in and out across its width, so it still shows that something is happening |
| Toast (option C) | `.toasts`, `.toast[data-tone="success"\|"info"\|"warning"\|"danger"]`, `.toast__text`, `.toast__title`, `.toast__detail`, `.toast__action`, `.toast__close`; `SharedComponents.toast(title, { detail, tone, action })`, `toast.error(...)`, `toast.warning(...)` | Card in the corner (full width on phones), status edge and icon, up to three stacked; a new one never pushes out an error. Success and info 5 seconds (10 with an action), warning 10, error until closed; waits under the pointer or focus. Errors read out at once |
| Saved note (option D) | `.saved-note`; `SharedComponents.savedNote(element)` | Settings pages: "Saved at 16:31" beside the button that saved, instead of a toast; goes at the next change |
| Icons in built parts | `data-sprite` on the `components.js` script tag, or `window.SharedComponentsSprite` | The toast and saved note draw icons as `<use href="#i-name">`. An app whose icons are in a separate file names it (Starboard: `/icons/sprite.svg`), or the icons and Close button are blank |
| Help | `.help`, `.help__text` | A disclosure button, not a hover tooltip. A tooltip (`data-tooltip`) only names an icon; anything that explains is help |
| Disclosure | `.disclosure` (`details`), `.disclosure__body`, `.disclosure__meta` | SMART report, More settings, Restore your settings |
| Releases | `.disclosure.release`, `.release__date`, `.release__counts`, `.release__type[data-type="added|changed|deprecated|removed|fixed|security|settings"]`, `.releases-head` | Each release in its own accordion, newest first, the installed one open, with Open all. Summary: "Version 0.9.1" as a heading, an Installed chip, the date, and a count chip for each type of change (added success, changed info, fixed warning, security danger, deprecated and removed muted). Body: each type with a bar in its colour, every change as a bold title and one sentence, then Your settings and the way back on a sunken background, and a link to the release on GitHub. On the app's Releases page (Settings, Updates); the footer's Release notes slide-out shows the same notes |
| Steps | `.steps`, `aria-current="step"`, `[data-done]` | Onboarding and upgrade wizard |
| Command | `.command` with `.code-block` and `.copy-btn` (`.copy-btn--label` shows the word Copy) | Commands to copy (How to upgrade); wizards use the labelled button |
| Line chart | `.chart`, `.chart__svg`, `.chart__grid`, `.chart__axis`, `.chart__line--1/--2`, `.chart__legend`, `.chart__swatch` | Second series dashed; always with a table view in a disclosure |
| Load more as you scroll (UX-52) | `.load-more`, `.load-more__count`, `.load-more__status`; `SharedComponents.loadMore(box, { load, items, noun, pageSize, auto, maxAuto, said })`, then `reset()` after a new search, filter or A to Z jump | A long list ends with a count and a real Show more button. One IntersectionObserver per list loads the next page as the end comes within 600px of the screen; no scroll handlers, no timers. While loading, "Loading the next 40" shows; then a polite status says "40 more shown" and focus stays where it was. After three pages in a row it pauses ("Paused here so you can reach the end of the page") until the button is pressed, so the footer stays in reach. The button alone with Reduce motion, when the app's setting asks for it, without IntersectionObserver or without script; pressing it moves focus to the first new item. `DESIGN-SYSTEM.md` section 11 says when to use it |
| Log viewer | `.log-view[data-log-view][data-file]`, `__bar`, `__search`, `__count`, `__scroll` (`role="region"`, `tabindex="0"`, named), `__lines` (`ol`), `__line[data-level="error\|warning\|info\|debug"]`, `__time`, `__level`, `__text`, `__match`, `__earlier`, `[data-wrap]`; `.filter-chip`s with `[data-log-level]` and a `[data-count]`, `[data-log-follow]`, `[data-log-wrap]`, `[data-log-download]`; `SharedComponents.logView(box, { lines, maxLines, show, fileName })` returns `add(lines)` and `clear()` | An app's or job's log (20 November 2026). Lines are strings ("12:01:03 ERROR …") or `{ time, level, text }`. Keeps the newest 10,000, draws only the newest 1,000 that match with Show earlier lines, and adds new lines on their own (never redrawing the list). Search marks each match and says how many; the level buttons carry their counts. Following keeps the newest line in view; scrolling up pauses it and the count line says so. New lines are never read out; new errors are, politely and only while following, gathered over 1.5 seconds. Download gives every line held, as text |
| Sparkline | `svg.sparkline[data-values][data-unit][data-period][data-min][data-max]` with `.sparkline__area` and `.sparkline__line`, `.stat__trend`; `SharedComponents.sparkline(svg, values, options)` | The shape of the last hour or day under a stat's value (20 November 2026), in `--chart-1`. Hidden from screen readers; `.stat__trend` says "Last hour: 18% to 42%, lowest 18%, highest 61%". For reading values or comparing, the line chart with its table |
| Gauge | `.gauge[data-value][data-max][data-unit][data-warn][data-danger]`, `.gauge__dial`, `__svg` (`aria-hidden`), `__track`, `__fill` (`pathLength="100"`, `stroke-dasharray`), `__value`, `__label`; `SharedComponents.gauge(el, value)` | One value against a known most, in a stat tile (20 November 2026). The value is in words in the middle; the arc's colour turns warning or danger at `data-warn` and `data-danger`, and the tile then carries a status chip, so the state is never colour alone |
| Pagination | `nav.pagination` (named for what it pages), `__summary`, `__pages`, `__link` (`aria-current="page"`, `rel="prev"`, `rel="next"`), `__gap` (`aria-hidden`), `__size` (Rows per page); `SharedComponents.pagination(nav, { page, pageSize, total, noun, sizes, href, onPage, onSize, focus })` | Tables people sort, compare or come back to by place (20 November 2026): "Showing 21 to 40 of 312", Previous and Next (with hidden "page"), the first, last and either side of this page, and rows per page. Links are 44px. In place, it says the new place politely and moves focus to the table's heading; from the server, real links. Walls and lists people browse use load more instead |
| Tooltip | `data-tooltip="…"` on the thing; one `.tooltip` (`aria-hidden`) for the page | The name of something that shows only an icon (20 November 2026): an icon button, or a `.status-icon` with `tabindex="0"`. On hover after 0.3 seconds and at once on keyboard focus; the pointer can move onto it; Escape closes it without closing a dialog behind it (WCAG 1.4.13). Its words are already the thing's name, so it is hidden from screen readers and never holds anything needed to act. Replaces `title`. Help that explains stays in help links |

### Containers
| Component | Classes | Notes |
|---|---|---|
| Panel | `.panel[data-tone]`, `.panel__head` | Groups content |
| Card | `.cards`, `.card[data-tone]`, `.card__top`, `.card__title`, `.card__meta`, `.card__actions` | One thing; whole card is the target; opens its slide-out or page |
| Card band (DASH-428) | `.has-band` on the card, `.card-band`, `.card-band__title` (the heading), `.card-band__sub`, `.card-band__side`, `.card-band__time`, `.card-foot` | A grey band across the top: the logo (`.app-icon--compact`), the name as the heading, the status chip at the right, and `.card-foot`, a lighter grey strip at the foot of the card, with when it last updated, so the band stays on one line (16 November 2026); Starboard's plug-in cards (design 2, "band with status", TheMightyTRexUK, 14 November 2026). The chip starts with hidden "Status: " and the time with hidden "Updated ", so each makes sense alone. The heading keeps its own line: when the side does not fit beside it, the side moves under it rather than squeezing it onto two lines (DASH-443) |
| Media card and grid | `.media-grid[data-size]`, `.media-card`, `.media-card__title`, `.media-card__meta`, `.media-row` | Books and films; Small, Medium, Large |
| A to Z jump list | `nav.az-jump > ol > li > a.az-jump__letter`, `[aria-disabled="true"]`, `[aria-current="location"]`, `.wall-letter` headings (`#letter-a`, `#letter-num`) | Over a long wall: # then A to Z from the sort title, accents folded; letters with nothing shown but not choosable ("Q, no books" from the noun given to `azJump(nav, letters, noun)` or `data-noun`, or "Q, none"); sticky under the header; 44px targets; one Tab stop with Arrow keys, Home and End; focus moves to the heading after a jump; sideways scrolling on phones. `SharedComponents.azLetter`, `azJump`, `azGo` and the `az-jump` event |
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
| Wizard review aids | `.wizard-aside`, `.wizard-next`, `.wizard-tree`, `.wizard-tree-toggle` | What happens next and the decision tree: for testing only, shown while the app's testing setting is active, never in the finished product |
| Help links | `.help-links`, `.help-link` (a button), opening a slide-out (`.side-panel`) titled with the link's question | "What is…" and "Which one is right for me?" at the end of the part of a page they explain. Every piece of in-page help works this way: never a fold-out (`details`), never a dialog. Help that is an article in the help centre is shown in the slide-out too, with "Read it in the help centre" in its foot. **Two help icons, both square** (TheMightyTRexUK, 7 November 2026): `help` (a question mark in a square) for help that opens in the page, in a slide-out; `help-new-tab` (the square opening at the top right, with the new-tab arrow) for help that opens in a new tab: the header's Help and "Read it in the help centre". Never `circle-help` for help. A link that opens a new tab also says "(opens in a new tab)" for screen readers |
| Address | `.address` with `.copy-btn` (`data-copied="Address copied"`) | A server address as a link that opens in a new tab, with a copy button |
| Signing in to a service (DASH-452) | `.signin-card`, `.signin-steps`, `.signin-example`, `.signin-way`, `.qr-card` (`__code`, `__text`), `.device-code` (`__value`), `.signin-wait` (`__words`, with `.progress--busy`), `.test-checks` (`li[data-state="done|failed|waiting"]`, `__state`), `.tested[data-tone]` | A wizard step that signs in on a service's own page: on the phone (QR code dark on white, the page and code written out with Copy, waiting by itself in a polite live region) or in this browser (the link, then the address it ends on pasted back); a test's checks; Test connection's result beside a place. Rules: `WIZARD.md` section 9 |
| Restart where it is needed (Starboard, DASH-470) | `.notice[data-tone="warning"]` holding a `.btn--primary` "Restart <app>", a `.small` line that says what restarting does (`aria-describedby`), `.progress--busy` and a `.small[role="status"]` | Shown only while the app says Restart needed, in the place that says so, never as a standing button. It asks first (a careful confirm, starting on Cancel), then follows the app until it answers again, in words in the polite status ("Jellyfin is restarting", "Still waiting: 40 seconds so far", "Jellyfin restarted and answers again"); the button keeps focus while it works (`aria-disabled`, as Show more) and focus moves to the result. A failure is an inline error beside the button, which works again. The notice becomes a success notice, "<app> restarted". It asks one small request every few seconds, only after the button is pressed, for at most 3 minutes |
| Settings rows | `.settings-section`, `.settings-section__head`, `.settings-rows`, `.setting`, `.setting--opens`, `.setting__text`, `.setting__label`, `.setting__hint`, `.setting__control`, `.settings-section__head--action` | Things with several fields open a slide-out |
| Panel header | `.panel-header`, `.panel-header__title`, `.panel-header__brand`, `.panel-header__actions` (Previous, Next) | The same bar on slide-outs, dialogs and the phone menu; on slide-outs and the phone menu it wears the page background (`--color-slide-header`) |
| Action list (Starboard, 19 November 2026) | `.action-list`, `.action-list__item`, `.action-list__hint`, `.file-kind` | Everything that can be done with one thing, in its slide-out, such as a download that needs attention: each action a button (with its icon) and one line under it that says what happens, tied to the button with `aria-describedby`. The actions that fix it first, under a heading such as Fix it; the ones that take it away or delete files in a second list under their own heading, the deleting ones `.btn--danger`, each asking first and naming what is deleted and how much space it frees. Only the actions that fit are shown; one primary. A result is said in the live region, and focus stays on the button, or goes back to the item's name when the slide-out closes. A file list is `.rows` with a `.tag.file-kind` (Media, Sample, Archive, Program, Other) and the size |
| Slide-out | `.side-panel-layer`, `.side-panel-backdrop`, `.side-panel`, `.side-panel--wide`, `.side-panel__body`, `.side-panel__foot`, `.side-panel__lead` | From the right; 420px, 640px wide, full width on phones; header in the page background, body and foot on the raised surface |
| Dialog | `.dialog` (`<dialog>`), `.dialog__body`, `.dialog__foot`, `.dialog--scroll`, `data-close-outside` | Decisions and short tasks only. `.dialog--scroll`: only the body scrolls, the header and foot stay in view. `data-close-outside`: a press outside closes it (help only, never a dialog with fields) |
| Tabs | `.tabs` (`data-activation="manual"`), `.tabs__list` (`role="tablist"`, named), `.tabs__tab` (`role="tab"`, `aria-selected`, `aria-controls`, a `.count` allowed), `.tabs__panel` (`role="tabpanel"`, `aria-labelledby`, `tabindex="0"`); `SharedComponents.setupTabs(root)`; `tabs-change` event | Real tabs for the parts of one item's page, as `DESIGN-SYSTEM.md` section 5 asks (20 November 2026). One Tab stop; Left and Right move round, Home and End go to the ends; a tab is chosen as focus reaches it, or by Enter or Space with manual activation. A link to a panel's id opens it. Without script every panel shows. Moving between pages is the level 2 menu, never tabs. `.logo-tabs` can move to these |

## Slide-out, dialog or page

| Use | When | Examples |
|---|---|---|
| Slide-out | Details of one item in a list, or editing it, where keeping the list in view helps; longer reading beside the page | Book summary; a request; a download client, indexer, reading account or user; a log entry; an app, disk, download or backup run on Starboard; release notes; Display and accessibility; a wizard's "What is…" help |
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
2. Add `components.css` in a `shared` layer under the app's own layers, so nothing changes until a page
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
  others) unchanged until each page moves over. Delete a rule there when its page moves.

**components.js changes:** `openLayer(idOrElement, opener, onClose)` now accepts an element, returns its
close function, cleans up its listeners and can be reopened safely. Loading the file with `data-manual`
(or setting `window.SharedComponentsManual = true` first) skips the automatic `setup()`.

**Keeping them in step (TheMightyTRexUK, 2 November 2026: the library is shared by both apps and kept up to date):**
change the component here first, never in an app, and follow the steps in
[Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html). Add the change to the Decisions list in this file, commit it here and
push, so every checkout picks it up.

**Decisions:** a Discord link in the footer (TheMightyTRexUK, 22 November 2026, DASH-526: "I want a discord link on starboard footer as well as the help center"): an app with a Discord support server links to it after Help, as "Discord support server" with the external-link icon and "(opens in a new tab)" in hidden words; the help centre builder adds it to every page when `help-centre.json` has `discord`; which item to use (Starboard DASH-309, 12 November 2026): `DESIGN-SYSTEM.md` section 10 picks rows, cards, chips, filters, toolbars, notices, toasts, dialogs or tables by what the thing is; accent teal (UX-02 option B); status chip style B, outline with icon (UX-04); cover actions (UX-42: `.cover-card` with `.cover-actions` on the cover by default, beside it as a per-account setting); shelves without scroll bars (UX-30 option A: `.shelf-scroller`, arrows over an edge fade); covers always line up (`.media-card` titles take two lines); small covers (UX-44: `.book-row` with `.cover-actions--row` in rows, `.cover-card__more` with the actions in words on small tiles); square radio art in the book shape (FEAT-R decision 2, fill 4: `.show-art`, label in the image's colour) and `.logo-tile`; every slide-out has the same header and body (TheMightyTRexUK, 2 November 2026: `--color-slide-header`, the page background, on slide-out and phone menu headers over a raised-surface body; dialogs keep the plain header; Display and accessibility and Release notes are slide-outs). App logos without a tile (TheMightyTRexUK, 2 November 2026: `.app-icon.has-image` is only the image, with no border or background; initials keep the tile). The logo editor on every way to get a logo (TheMightyTRexUK, 2 November 2026: From a cover, Find online and Upload your own all use the box, Shape from lightness or transparency, four cleaning levels, and a small eraser and paintbrush on `.checker[data-tool]`; found files show as plain pictures in `.logo-candidate__art > img`). Nicer scroll bars (TheMightyTRexUK, 2 November 2026): thin and square in every scrolling area, `--color-scrollbar` (the border colour, the text colour in High contrast) on a clear track; they stay visible, and only shelves hide theirs behind arrows. UX notes for testing (TheMightyTRexUK, 2 November 2026): `ux-notes.js` (copied to both apps by sync.py) puts Note an issue in the corner of every page while an app's testing setting is active; select the part (with the pointer, or Tab and Enter), say what is wrong, the kind and how bad; Notes lists them with Copy as text, Download and Mark as fixed. Notes keep the page, the part, a selector and the display settings. An app passes a store to keep them on its server; otherwise they stay in the browser. Styles: `.ux-dock`, `.ux-banner` (at the bottom, clear of the header), `.ux-outline`, `.ux-notes`. Security checks the same in both apps (TheMightyTRexUK, 3 November 2026): `docs/SECURITY-CHECKS.md` sets the checks (tests, live journeys, Trivy, ZAP on a private network, Gitleaks, Bandit and Semgrep, ShellCheck, Hadolint, CodeQL, a separate review, install tests), how to sort findings, a security page in each app with a "Security checks for each release" table, and a Security section in every release's notes (`CONTENT-DESIGN.md`, release notes). Starboard is the worked example; Storyarr has to catch up. Focus not obscured (WCAG 2.2, 4 November 2026): the page keeps the sticky header (and row 2) and an open save bar clear when it scrolls, with `scroll-padding` on `:root`; `WCAG.md` and `ALT-TEXT.md` added after the GOV.UK Service Manual and BBC GEL. Search is always one button away (TheMightyTRexUK, 4 November 2026: "update the design system to ensure there is a search button"): `.rail__search` is first in the rail, under the logo, and moves focus to the header's search box; on phones, where the box is hidden, `.site-header__search-btn` in the header opens the same box as a row under the header, and Escape or a press outside closes it and returns focus to the button that opened it. Both use `data-search-open` and `aria-controls` (`setupSearch()` in `components.js`). No single-key shortcut (WCAG 2.1.4). The `radio` icon is added. Wizard rules (TheMightyTRexUK, 4 November 2026): `docs/WIZARD.md` sets one set of rules for every wizard, from the installer mock-up: the first question asks which job, each with its own wizard; one question per step; steps that do not apply left out; a step in parts has `.steps--sub`, as wide as the progress bar with a line between parts, numbered 1, 2, 3, each part counting in the progress bar's total, and on phones only the numbers, with ticks for done parts; "(recommended)" with a reason, never "easiest"; "What is…" help at the end of the part it explains, in a dialog that scrolls inside and closes on a press outside; addresses as links with copy; a summary of what was set and skipped. What happens next and the decision tree are review aids for testing only, never in the finished product. Copying falls back to a hidden text box on plain http (`copyText()` in `components.js`), and a dialog returns focus to the button that opened it. Step numbers grow with Text size. Changelogs (TheMightyTRexUK, 5 November 2026): `docs/CHANGELOGS.md` sets one way to keep `CHANGELOG.md` in every project, after Keep a Changelog 1.1.0: for people, never a commit log; an Unreleased section at the top; every version newest first, linked, as `## [x.y.z] (day month year)`, with dates as in `CONTENT-DESIGN.md` rather than year, month, day; changes under Added, Changed, Deprecated, Removed, Fixed and Security only; withdrawn releases marked `[Withdrawn]`. In-app release notes use the same six types. Terminal wizards and feedback (TheMightyTRexUK, 5 November 2026): `docs/TERMINAL.md` sets how a wizard appears in a terminal (boxed with a heading box reading "App | step", a progress bar and a menu fixed on the bottom line with b Back, ? Help, f Feedback and q Stop; or plain numbered lines for screen readers, never redrawn), with help as a box over the step and feedback sent as a QR code sized to the window; `docs/WIZARD.md` section 12 puts Snaglist on every wizard step, naming the step, with Show as a QR code for a computer that is not online yet.

## Help centre (7 November 2026; the standard since 14 November 2026)

Every app's help is Markdown in its own repository, published as web pages by one builder,
`tools/help_centre/build.py`, with this library's tokens, components, fonts and icons. Since 14 November 2026 every
help centre uses the standard the owner chose (Starboard DASH-436): the seven main items as top links, a hub with a
side menu that folds (areas, groups, every article), the journey, the newest thing and the problem solver card on
the home page, the latest version beside the heading, articles flow chart first with numbered answer cards, a
problem solver page, and plug-in mode for a plug-in collection. `docs/HELP-WRITING.md` section 11 is the full
standard, with the flow chart format and the shape of `help-centre.json`.

**Components** (in `components.css` and `components.js`, shown in the gallery under Help centre):

| Component | Classes | Rules |
|---|---|---|
| Top links | `nav.top-links > ul > li > a` | The seven main items, the current area with `aria-current="page"`. Hidden on tablets and phones, where the side menu carries them |
| Side tree | `.side-tree`, `.side-tree__home`, `.side-tree__label`, `details.side-tree__area`, `details.side-tree__group`, `.side-tree__tile`, `.side-tree__count`, `.side-tree__chev` | A side menu that folds three levels deep, built from `details` and `summary`, so it works with no script. The page you are on has `aria-current="page"` and its area and group are open. `setupSideTrees()` opens them if a page forgets and scrolls the link into view inside a menu marked `data-side-scroll`. Any app may use it for a long side menu |
| Journey | `section.journey`, `ol.journey__stages` (`--stages`), `li.journey__stage[data-tone="start|step|fix"]`, `.journey__marker`, `.journey__dot`, `.journey__n`, `h3.journey__label`, `ul.journey__cards`, `a.stage-card`, `.is-lead` | An ordered list, so a screen reader meets each stage and then its cards. The marker is decoration (`aria-hidden`); the label carries the number and the name. Stacks on phones with the path down the side |
| Flow chart | `figure.flow-chart`, `.flow-chart__scroll` (`role="region"`, `tabindex="0"`), `svg.flow-chart__svg` (`--flow-w`), `details.flow-chart__words` and the drawing classes `.flow-chart__start`, `__question`, `__answer`, `__next`, `__step`, `__link`, `__line`, `__head`, `__text`, `__sub`, `__label`, `__pill`, `__n` | Drawn by `tools/help_centre/flowchart.py`. The SVG has `role="img"` and a short name; the words under it are the full text equivalent. It grows with Text size and scrolls inside its own region when narrow |
| Answer card | `section.answer-card`, `.answer-card__band`, `.answer-card__n`, `.answer-card__body` | A numbered answer: the number and the heading (which keeps its id) on a grey band |
| Feature card | `section.feature-card`, `.feature-card__text`, `.feature-card__pic` | The newest thing, with a chip saying which version it is new in and a small chart or picture |
| Solver card and solver | `section.solver-card`, `.solver-card__tile`; `.solver[data-solver]`, `.solver__node`, `.solver__question`, `.solver__answers`, `.solver__choice`, `.solver__step`, `.solver__options`, `.solver__nav`, `.solver__progress` | With no script the solver is nested lists of links; `setupSolvers()` asks one question at a time, puts the focus on the new question, says it in a polite status, and offers Back (focus returns to the answer chosen) and Start again |
| Version badge | `a.version-badge > .chip + b` | The latest version, no date, linking to the release notes |
| Plug-in card and band | `ul.plugin-cards > li > article.card.has-band.plugin-card` (with `.card-band`, `.app-icon--compact`, `ul.plugin-card__links`); `.plugin-band`, `.plugin-band__name`, `.plugin-band__sub`, `.plugin-band__side` | The grey band design (DASH-428) for a plug-in in a list and at the top of its own pages. An `.app-icon` holds a sprite icon or the initials |

**Layout only in the help centre** (`tools/help_centre/help.css`): the header bar, the hub grid, the side menu's
place and its phone overlay, area and landing pages, the article and On this page, the banner, search results and
the footer. **Behaviour only in the help centre** (`tools/help_centre/help.js`): Menu on tablets and phones (the page
behind is inert while it is open), Search moving the focus to the search box, Display and accessibility, the banner,
On this page following the article, and search.

**Accessibility:** checked on 14 November 2026 with axe-core 4.14 (WCAG 2.2 AA and best practice) on the home page,
an article, the problem solver, an area page and plug-in pages of all three help centres, in Light, Dark, High
contrast, 175% text and at phone width, with a reading order check, a Tab walk through the header, search, side menu
and disclosures, focus after the menu and Display open and close, and the live regions.

**For each app:** a `help-centre.json` at its root and a `<!-- help: <area> / <group> -->` line in each article
(`HELP-WRITING.md` section 11), and a workflow that checks out this repository and runs the builder. Starboard,
Snaglist and the plug-in collection use it. Build one here with `tools/help_centre/build.sh` from the app's folder.

## App-only patterns (2 November 2026)

Built from the tokens, used by one app, so not in `components.css`:

- **Starboard:** `.access-change` (what Starboard can access, with the command to change it), `.job-run` (a server job
  with Run now), the storage charts (`--media-*` map to `--series-*`), the release notes slide-out
  (`.release-notes`, opened from Release notes in the footer).
- **Storyarr:** the bookshelf and series views.


- 11 November 2026: `--font-heading` (headings h1 to h4) and `--color-rail` (the side menu) are optional, for Starboard's styles. Unset, nothing changes.
