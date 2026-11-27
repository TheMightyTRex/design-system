# Components by area

Updated 26 November 2026 (rewritten for Starboard as it is; the Storyarr inventory this file once held is in git history). Every component in the shared library, by the area it belongs to, as the component pages
(`components/index.html`) group them. `LIBRARY.md` is the reference, with each component's classes, behaviour and rules. When
you add a component, add it here and in `LIBRARY.md`.

| Area | Components |
|---|---|
| Foundations | Colour roles and status tones, accent palettes, type, space and size, icons, utilities (`.visually-hidden`, `.stack-*`, `.numeric`) |
| Shell | Side menu (rail), header and its level 1 and level 2 menus (`.menu-tabs`), phone menu, page and page head, footer, Display button, page banner, popover, alerts centre, command palette |
| Actions | Button, icon button, split button, menu button and menu, copy button, action row, action list |
| Inputs | Field, text box, select and text area, search field, input with unit, checkbox and radio, switch, segmented control, option cards, filter chips and applied filters, sortable list, form layout, file picker, folder picker, combobox, tag input, secret field, schedule picker, error summary and field errors, range |
| Content | Status chip, title with status, status icon, tooltip, count and update dot, tag, avatar and app icon, cover, facts, stat, sparkline and gauge, progress and meter, waiting mark and busy button, rows, table, tables that line up, pagination, notice and callout, empty state, skeleton and loading line, toast, saved note, help, disclosure, releases, steps, command, line chart, log viewer, load more as you scroll, prose, time ago |
| Containers | Panel, card and card band, media card and grid, A to Z jump list, section toolbar, save bar, settings rows and section group, timeline, list and detail, item header, series header, shelf, calendar month, selection bar, tabs, slide-out, dialog, panel header, back link and breadcrumbs |
| Patterns | Slide-out, dialog or page; which item to use (`DESIGN-SYSTEM.md` section 10); wizard and its pieces (`WIZARD.md`); signing in to a service; restart where it is needed; terminal (`TERMINAL.md`) |
| App patterns | Page topics, the update list, places and service logos, the dashboard grid and cards, show once, a wizard in a slide-out, folding sections (`LIBRARY.md`, App patterns) |
| Help centre | Top links, side tree, journey, flow chart, answer card, feature card, solver card and solver, version badge, plug-in card and band (`HELP-WRITING.md` section 11) |

Some class names differ from the component's name: - `.disclosure` is the accordion, `.side-panel` the slide-out and
`.segmented` the segmented control. - `.steps` and `.wizard` are the step list and wizard, and `.shelf` is the row
that scrolls sideways. - `.count`, `.chip` and `.tag` are the number, status and kind labels. - `.range` is the
slider, `.file-field` the file picker and `.side-tree` the folding side menu. - `.help` is the question button, and
`.command` is a command to copy (not the command palette).


---

## Starboard's screens and the parts each uses

Starboard as it is on 26 November 2026, by main menu item and screen. "Library classes" are the parts of the shared library the screen is drawn with; the board is the design page in `areas/` (a screen without a board is listed in the Boards section of `README.md`). The words of every status chip are in `CONTENT-DESIGN.md` section 6.

| Menu | Screen | Built from | Board |
|---|---|---|---|
| Home | Dashboard | `.dash-grid`, `.dash-card`, `.card-band`, gauge, sparkline, `.guide-card`, `.spark-card`, `.dash-edit` | Dashboard |
| Library | My library (TV, Films, Music, Radio, Books, Audiobooks) | A to Z jump, load more, media card and grid, series header, shelf, cover | Library |
| Library | Networks, Collections, Series, Authors, Narrators, Stations | Poster cards (Starboard's own, listed in `LIBRARY.md`), `.az-jump` | Library |
| Discover | Search, Discover rows, Coming up, On demand history | Shelf, filter chips, rows, `.discover-card` | Discover |
| Activity | Queue, Recently finished, From a link | Rows, progress, chips, toolbar, sortable | Downloads |
| Activity | Wanted (one tab each for Missing and Quality wanted) | Tabs, rows, selection bar, chips | Wanted |
| Activity | Requests, Issues | Rows, chips, slide-out | Requests |
| Activity | History, Across apps | Event list, rows, filter chips | History |
| System | Overview, Monitor, Busy now | Stat, gauge, line chart, table, notice | Overview, Monitor, Busy now |
| System | Apps, Other services, Install apps | Cards, app icon, rows, wizard, option cards | Apps, Other services |
| System | Updates | Update list (`.updates-table`), selection bar, disclosure, **Check now** | Updates |
| System | Storage, Pool, Disk health | Meter, table, rows, notice, chips | Storage, Disk health |
| System | Network | Facts, stat, switch | Network |
| System | Clean up, Holding folder | Rows, selection bar, dialog | none |
| System | Logs | Log viewer | Logs |
| Settings | General (ten pages: Names and apps, Appearance, Pages and lists, Discover rows, Download hours, Logs and feedback, Alerts, Performance, Pictures, Backup and restore) | Page topics (`.topic-tabs`), `.settings-sections`, settings rows, saved note, places for backups, show once | General tabs, Backup places |
| Settings | Apps (Manage apps, Your install, Reelix, the media server tab) | Sortable categories, option cards, wizard in a slide-out | Manage apps, Media server |
| Settings | Downloads, Radio | Settings rows, secret field, tag input, schedule | Downloads settings |
| Settings | Security | Secret field, show once, `.recovery-codes`, tables | Security |
| Settings | Plug-ins (Manage, Catalogue, one tab for each plug-in) | `.plugin-card`, `.plugin-band`, folds, `.dash-stat`, requires tags | Plug-ins |
| Settings | Updates, Releases, Restore | Settings rows, release list, wizard | About and updates |
| Any | Bring in | Wizard, sortable, signin card, meter, `.wizard-job` | Bring in |
| Any | Sign in, Set up | `.page--narrow`, `.site-header--no-rail`, wizard | Sign in, Set up |

## Where the other records are

- The status words: `CONTENT-DESIGN.md` section 6.
- The tokens: `foundations/tokens.html` on the site, made from `tokens.css`.
- The classes of each component, and its rules: `LIBRARY.md`.
- The `SharedComponents` functions an app can call: `LIBRARY.md`, JavaScript.
