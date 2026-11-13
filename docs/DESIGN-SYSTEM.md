# Storyarr design system

Version 0.1 (draft for the redesign), 1 November 2026. The target every page moves towards. What exists today
is in `COMPONENTS.md`; the redesign plan behind it is kept privately. Words are in `CONTENT-DESIGN.md` and changelogs in `CHANGELOGS.md`;
accessibility in `ACCESSIBILITY.md`, `WCAG.md` and `ALT-TEXT.md`; security checks and how to report them in `SECURITY-CHECKS.md`; the
component reference is `LIBRARY.md`.

**For AI agents:** when you build or touch UI, use these tokens, templates and components. If something you
need is missing, add it here first (and say so to TheMightyTRexUK) instead of inventing a one-off style.

## 1. Principles

1. **One way to do each job.** One status chip, one card, one side panel, one dialog, one toolbar.
2. **The same place every time.** Page title, section navigation, toolbar, content, side panel: same order on
   every page.
3. **Status first.** Every book shows its status with the same words, colour and icon wherever it appears.
4. **Calm by default.** Light theme, plenty of space, covers carry the colour; the interface stays quiet.
5. **Square corners.** Buttons, chips, cards, inputs, dialogs and covers are square. Avatars, spinners and
   status dots stay round.
6. **Accessible is the baseline.** WCAG 2.2 AA in every theme; 44px controls; keyboard first.
7. **Inspired, not copied.** Audiobookshelf and Radarr are references for ideas only; no copied code or assets.

## 2. Tokens

One token file (`apps/web/src/tokens.css`, task UX-02) with **role names**, defined once per theme
(Light, Dark, High contrast). Components use only these.

### Colour roles

| Token | Use |
|---|---|
| `--color-bg` | Page background |
| `--color-surface` | Panels, cards, header, side panel |
| `--color-surface-raised` | Dialogs, menus, toasts |
| `--color-surface-sunken` | Wells, code, empty cover placeholder |
| `--color-text` | Body text |
| `--color-text-muted` | Secondary text (still 4.5:1) |
| `--color-border` | Dividers and control borders (3:1 for controls) |
| `--color-accent`, `--color-accent-text` | Primary buttons, links, current item, focus ring |
| `--color-focus` | Focus outline (defaults to accent; stronger in high contrast) |
| `--status-success-bg/-fg` | In library |
| `--status-info-bg/-fg` | Downloading, Importing, Searching |
| `--status-neutral-bg/-fg` | Waiting, Not released, Wanted |
| `--status-warning-bg/-fg` | Needs attention |
| `--status-danger-bg/-fg` | Failed, danger actions (`.btn--danger`), errors |
| `--status-muted-bg/-fg` | Excluded, Not requested |

Map today's `--c-*` values onto these roles; delete the rest. Define the four undefined variables found in
`COMPONENTS.md` section 1 or replace them.

### Type

**One typeface everywhere: Atkinson Hyperlegible Next** (decided 1 November 2026, built in v0.4.8). It is set once
as `--font` on `:root` (`"Atkinson Hyperlegible Next Variable", system-ui, sans-serif`), loaded for everyone from
`@fontsource-variable/atkinson-hyperlegible-next`, and every `font-family` and `font:` rule uses `var(--font)`. No
serif headings, no monospace (versions, paths and commands use it too). Form controls inherit it. There is no
Low-vision font switch any more, because it is always on.

Base 16px (1rem), scaled by the Text size setting. Six steps only:

| Token | Size | Use |
|---|---|---|
| `--text-xs` | 0.75rem | Chip text, captions |
| `--text-sm` | 0.875rem | Secondary text, table cells, toolbar |
| `--text-md` | 1rem | Body |
| `--text-lg` | 1.25rem | Panel and section headings (h2) |
| `--text-xl` | 1.5rem | Page heading (h1) |
| `--text-2xl` | 2rem | Home and hero headings only |

Line height 1.5 for body, 1.25 for headings. Weights 400 and 600 only. Low-vision font swaps the family.

### Space, size, motion

- Space scale (4px grid): `--space-1` 4, `--space-2` 8, `--space-3` 12, `--space-4` 16, `--space-6` 24,
  `--space-8` 32, `--space-10` 40, `--space-12` 48.
- Control height `--control-h` 44px. `--control-h-compact` (32px, `.btn--compact`) only inside dense tables, never
  for the only way to act and never beside a 44px control.
- Radius `--radius` 0; `--radius-round` 50% for avatars and dots.
- Shadow `--shadow-raised` for dialogs and side panels only; none in high contrast (use borders).
- Motion `--motion-fast` 120ms, `--motion-panel` 200ms ease-out; both 0ms with Reduce motion.
- Cover sizes: `--cover-s` 96px wide (summary panel), `--cover-m` 128px (compact wall), `--cover-l` 176px
  (shelves). Aspect 2:3; audiobook squares are letterboxed, not cropped.

## 3. Shell

```
┌ Navigation ┬ Header: sub-menu (icons, current underlined) · search · actions · Display ┐
│ Library    │ Page heading (h1) · summary line                                         │
│ Discover   │ Toolbar: view switch · search in section · filters · sort · Customise    │
│ Activity   │ Content (template)                              │ Side panel (right)     │
│ Settings   │                                                 │ slides in on select    │
└────────────┴─────────────────────────────────────────────────┴────────────────────────┘
```

- **Main menu (5):** Home, Library, Discover, Activity, Settings. Icon rail on desktop, ☰ menu drawer on phones
  (each section's sub-menu inside it).
- **Header (one row, 2 November 2026):** the section's sub-menu on the left; search and Display on the right.
  Nothing else goes in the header. Page actions (the connection warning, the Lists menu on Discover) sit in a
  `.page-actions` row at the top right of the page body for now, until the section toolbar takes them. Display is always the last item. Below 1100px
  the sub-menu drops to a full-width row under search; on phones it lives in the ☰ drawer. Tabs show icons only
  (names as tooltips) when they do not fit.
- **One control height:** search and every header, toolbar, panel and menu control is `--control-h` (44px;
  Storyarr's `controls.css` still calls it `--control-height-large`). Never type 44px by hand; `--control-h-compact`
  (32px) is the compact size for dense tables only. Split or framed controls give the frame the height.
- **Page actions in the header are menus, not rows of buttons:** related actions share one menu button (Lists:
  Add list, Refresh all lists, refresh one service). Menus open with focus on the first item, arrow keys move,
  Escape closes and returns focus.
- **Menu names, renamed (TheMightyTRexUK, 4 November 2026):** *side menu*, *level 1 menu* and *level 2 menu*, in place of main menu, 1st level and 2nd level below.
- **Menu names (TheMightyTRexUK, 2 November 2026):** *main menu* = the left rail; *1st level* = header row 1 (a
  section's pages: My library, Following...); *2nd level* = header row 2 (a page's own tabs: In my libraries,
  Authors...). Main menu, 1st and 2nd level all have icons. In the ☰ menu only the main menu and 1st level
  have icons. All icons live in `apps/web/src/navigation.ts`.
- **Section navigation:** level 2, in the header row, in every section. Never page tabs underneath as well.
- **Page heading:** one visible h1 on every page (no hidden h1s), with an optional one-line summary
  ("12 of 13 in your library · 3 excluded").
- **Section header and toolbar (level 3), design D, chosen 1 November 2026** (design D, from a
  private mock-up):
  1. **Heading row:** the section's h1 and a one-line summary with counts on the left; the view switch
     (for example Covers or List, List and detail or List) on the right.
  2. **Filter row:** search within the section first; then quick-filter chips with counts (toggle buttons,
     `aria-pressed`); then dropdown filter chips ("Media", "Library", "Genre"), which turn accent-coloured and
     show their value when set ("Media: Audiobooks"); then, at the far end, Sort ("Sort: Title", with
     Reverse) and Customise.
  3. **Applied filters row** (only when something is filtered): "Filtered by", one removable chip per active
     filter, Clear all, and "Showing N" at the end.
  4. Results.
  Missing pieces leave no gap. On phones the filter row scrolls sideways with back and forward buttons, and
  Sort and Customise stay visible.
- **Level 4:** only inside a side panel or an item page's tabs.

## 4. Page templates

| Template | Used by | Shape |
|---|---|---|
| **Collection** | Library Books, Discover shelves, a follow's bookshelf, search results | Toolbar, status filter chips with counts, cover wall or list (view switch), side panel on select |
| **List and detail** | Library Authors and Series, Following, Activity | Toolbar, list of rows on the left, the selected item's bookshelf or details on the right; on phones the detail opens as its own page |
| **Item page** | Book, author, series | Header (cover, title, status chip, main actions), then tabs: Book = Overview, Editions and files, History |
| **Settings group** | Settings (six groups: General, Accounts, Sources, Library, Downloads, System) | Group navigation in the header; sections as cards with a heading, one-line description, fields; save per section |
| **Home** | Home | Three bands: Needs you (Needs attention items), Happening now (downloads, searches), Coming soon (Not released, calendar); each item links to its page |
| **Wizard** | Onboarding, upgrade | Step list, one question per step, Back and Continue, Keep the defaults and finish |

## 5. Components

| Component | Replaces | Notes |
|---|---|---|
| **StatusChip** | Every status badge in `COMPONENTS.md` section 5 | Props: status (vocabulary), detail. Tone from the status tokens; icon plus text |
| **CoverCard** | `.book-card`, `.cover-wall-book`, discovery cards | Cover, title, author, StatusChip; whole card selects; no action buttons on the cover |
| **Row** | Request rows, follow rows, review cards | Cover thumbnail, title and secondary line, StatusChip, one primary action, overflow menu |
| **SidePanel** | BookSummary, `.book-drawer`, `.release-drawer` | Right side, below the header, 360 to 420px; Escape and a click outside close it; focus managed; full screen on phones. **Header (standard, v0.4.8):** `.side-panel-header` from `apps/web/src/side-panel.css`: the panel's name in bold (`.side-panel-title`, 1rem, weight 700) and the close button (X, `aria-label` "Close …"), on a white bar (`--panel-header-bg`; the surface colour in dark) with a grey line under it (`--panel-header-line`), sticky while the panel scrolls, reaching the panel's edges (each panel sets `--panel-pad-top` and `--panel-pad-x`). Used by the My library summary ("Summary"), the bookshelf drawer ("Book") and the calendar day (the date) |
| **Dialog** | BookDialog and other `<dialog>`s | **Same header as SidePanel (2 November 2026):** `.side-panel-header` with the title in an h2 `.side-panel-title` (bold, 1rem) and the close X, white bar, grey line. Then body, buttons main-first; danger variant (`.btn--danger`). The Display dialog uses the same header |
| **Toolbar** | All filter bars | Slots in the order of section 3 |
| **FilterChips** | `.follow-status-filters`, `.activity-filters`, `.review-chips` | Toggle buttons (`aria-pressed`) with counts; "All" first |
| **Select** | Native selects and SelectMenu | One look; label always visible |
| **SectionNav** | `.page-tabs`, HeaderSubmenu, LibraryTabs | Links with `aria-current`, icon and label |
| **Tabs** | DetailTabs and BookDetail's copy | Real tabs with arrow keys, for item pages only |
| **Button** | Assorted | Variants: primary, secondary, quiet, danger (`.btn--danger`). One primary per view |
| **EmptyState, LoadingState, ErrorState** | Notice, Empty, Loading | Words follow the content guide patterns |
| **Toast** | Assorted inline confirmations | `role="status"`; Undo where possible |
| **ProgressBar** | Download percentages | Text label always |
| **SummaryHeader** | `.wall-header`, follow headers | Title, kind line, progress bar of released books in library, counts, main actions |

### Where status goes (2 November 2026)

One rule for both apps, so a state is always in the same place relative to the thing it describes:

| Place | Pattern | Example |
|---|---|---|
| A heading (panel, page, slide-out) | `.title-status`: the chip straight after the name, centred on the heading's line. Details such as a version or a time go on the right or in the muted line, not in the chip | System, Overview: "Jellyfin ✓ Up to date", "Version 10.11.2" on the right |
| A list of things that each have a state | `.status-icon`: an icon straight after the name, the word in hidden text and a tooltip | Manage apps, What Starboard can access |
| A row with actions | The chip in `.row__side`, before the actions | Requests, downloads |
| A card | The chip in `.card__meta` | Apps |
| A stat tile | The chip under the value | Storage, Drives over 90% full |
| A cover | The chip in the cover's corner | Book walls |

- Never put status on a line of its own under a heading: it pushes the content down and reads as a separate item.
- At most two chips in one place (such as "Restart needed" and "Update available"); more belongs in a facts list.
- The chip says the state in the shared vocabulary (`guides/CONTENT-DESIGN.md`); it never holds a number or a date.

### Consistency rules (2 November 2026, from the design review)

- **One name for one action.** Re-reading status is **Check again**, everywhere (page heads, slide-outs, Updates).
  **Run now** only starts a server job. Name a slower job by what it does (Storage: **Sort by type again**).
- **One way to save settings.** Choices (option cards, selects, switches, radios) save as soon as they change, with
  a saved note beside the control (section 9). Text fields save with `.inline-save` (one field) or `.save-bar` (several), and their Save button is
  secondary. At most one primary button in view. A slide-out or dialog that edits one thing (an app, a
  connection) keeps one Save as the primary button in its foot.
- **Buttons start on the left**, the main action first, in every dialog, slide-out and wizard foot; a danger button
  in a slide-out and Skip this step in a wizard sit apart on the right (LIBRARY.md, Button).
- **Danger is shown before and after.** A button that opens a danger dialog is `.btn--danger`; delete and remove
  use the `trash-2` icon; the dialog's other button is **Cancel**.
- **One-of-several filters** are `.segmented`; filter chips are for toggles that can be on together.
- **Headings at one level are one size.** Panel and section titles take the library's size for their level; do
  not resize them per page.
- **Chart text** follows Text size: SVG text uses `--text-xs` or `--text-sm` in a viewBox drawn at the real width,
  or sits in HTML beside the chart.
- **Slide-outs look like slide-outs** (2 November 2026, TheMightyTRexUK). Every slide-out, including the phone menu, has its
  header in the page background (`--color-slide-header`, which is `--color-bg` in every theme) and its body and
  foot on the raised surface (white in Light, the dark surface in Dark). Dialogs keep the plain panel header.
  **Display and accessibility** and **Release notes** are slide-outs, not dialogs.
- **Deliberate exception:** Starboard's Health first design fills a card that is not responding with the danger
  background, as well as the edge and chip, so trouble stands out from across the room. Other designs and
  Storyarr use the plain card.

## 6. Filters and the address

Every filter, sort, view switch and toggle that changes the page's address must start from
`currentParams()` (`apps/web/src/currentParams.ts`), the address as it is right now. Never build the
next address from `useSearchParams()`'s copy or from React Router's `setSearchParams(previous => …)`:
both are the copy from the last render, so a quick second change drops the first (found 1 November 2026).
Links rendered on the page can use the render-time copy, because they redraw with every change.
`tests/ui/quick-filter-changes.spec.ts` makes two changes at once and checks both stick.

## 7. Layout rules

- Content max width 1440px; side panel pushes content on wide screens, overlays it below 1100px.
- Breakpoints: phone below 640px, tablet 640 to 1099px, desktop 1100px and up.
- Covers wall: auto-fill grid with `--cover-m` minimum; titles under covers, two lines maximum.
- Tables only for real tabular data (Activity history, logs); everything else uses Rows.
- Numbers in rows right-aligned; dates as in the content guide.
- **A state chip sits on its title's line** (12 November 2026): the title on the left, the chip at the right,
  centred on the line; never on a line of its own under the title. Section headings, card headings, rows (in
  `row__side`), slide-out titles and sub-headings all follow it. In code: `.title-chip` around the title and the chip;
  on a narrow screen the chip wraps under the title, still at the right.

## 8. Terminal

Both apps also run in a terminal: the Run first script, the installer and the terminal set-up. A terminal wizard
is the same wizard as the browser one, with the same steps, words, answers and help, drawn as text
(`WIZARD.md`, One wizard, two ways to show it). The full rules are in `TERMINAL.md`; the code is in `terminal/`.

- **Two ways to draw it.** Boxed: a heading box ("App | step", "step 3 of 6"), a progress bar that ends where the
  box does, the step, and a menu fixed on the bottom two lines (b Back, ? Help, f Feedback, q Stop, and on the
  right what Enter does). Plain, for screen readers, `--plain`, a window under 60 by 20, `TERM=dumb` or no
  terminal: numbered lines, never redrawn, no colour, and the first line says which keys work.
- **Questions:** numbered answers, the recommended one first, marked with a dot and "(recommended)", or "(your
  last answer)" when someone comes back; the default in brackets, and Enter takes it.
- **Help** is a box over the step, titled "Help: " and the question; the step comes back as it was.
- **A job** has one bar, drawn in place: the job, which job of how many, what it is doing, the timer, then how far
  it has got ("5 of 12 installed"). Only Ctrl+C works while it runs, and keys typed meanwhile are hidden and
  dropped. A failure keeps the bar, marked, with the problem and the choices below it.
- **Feedback** is Snaglist's, drawn in the terminal: f from any question, or Report this problem after a failure.
  The report goes to the phone as a QR code that fits the window (`TERMINAL.md`, section 7), or as a link or a
  file. Nothing typed as an answer is ever in it.
- **Every error has a number** (RF-01, IN-01) that the help centre explains.

## 9. Settings patterns

Approved by TheMightyTRexUK on 12 November 2026 (Starboard DASH-308 and DASH-310). Every Settings page, every
plug-in's settings page and every settings slide-out is built from these nine patterns and nothing else. The
gallery's Settings patterns section shows each one.

| # | Pattern | Use it for | Code |
|---|---|---|---|
| 1 | **Section** | Each topic on a page: heading, one line about it, its state chip on the heading's line. Topic tabs above when a page has four sections or more | `.settings-section`, `.settings-section__head`, `.title-chip`, `.topic-tabs` |
| 2 | **Setting rows** | One setting each: label and hint on the left, control on the right. Switches, selects and numbers apply at once and show the saved note beside the control | `.settings-rows > .setting`, `.setting__text`, `.setting__control`, `.saved-note`; a number with a unit uses `.input-unit` |
| 3 | **Choice cards** | Two to four choices that each need a sentence | `.option-cards > .option-card` (radios) |
| 4 | **Location** | Every folder: the folder in words with free space, the path small under it, Browse (opens in the right place), Set automatically (the right folder for this setting), and the typed path under Advanced | `.location` |
| 5 | **Form with Save** | Typed text only (an address, a name, a key). One Save per section, at its foot, with the saved note beside it; Test beside Save when the text can be tested | `.form-stack`, `.actions`, `.saved-note` |
| 6 | **Status line and messages** | What is wrong or worth knowing: one sentence, then what to do, with at most one button | `.notice[data-tone]`, chip on the section's heading |
| 7 | **Empty and error states** | A list with nothing in it, or a part that could not load: what is missing and the one thing to do | `.empty` with one primary button |
| 8 | **Lists that open** | Things with several settings each (apps, sites, people): each row has its state chip and Edit, which opens a slide-out editor; Add at the foot of the list. A long list of apps (Manage apps) shows the state as `.status-icon` after the name instead (section 5, Where status goes) | `.rows > .row`, `.row__side`, slide-out |
| 9 | **Danger zone** | Remove, delete, reset, clear: last on the page, its own section with a red edge; each button opens a dialog that says what happens | `.settings-section--danger`, `.btn--danger`, danger dialog |

Rules:

- **No toast for a saved setting.** The saved note beside the control or the Save button says it ("Saved 16:31").
  A toast is for things that happen elsewhere or later.
- **A unit is part of the control** (`20 | MB/s`), never only in the label or the hint.
- **A folder is never a bare text box.** Starboard knows where each app sees its folders; Browse shows the
  computer's folders and gives the app the path as it sees it.
- **Advanced settings** are hidden until the page's small Advanced settings switch is on (at the right of the
  heading's line); a location's typed path is always under its own Type a path (Advanced).
- **Slide-outs use the same patterns** inside; their one Save is the primary button in the foot.


## 10. Repeated items: which one to use

Starboard DASH-309, 12 November 2026. Settings have their nine patterns (section 9); this section does the same for
the items every other page repeats. Pick by what the thing is, not by how it should look. The classes are in
`LIBRARY.md`; the gallery shows each one.

| Item | Use it for | Do not use it for | Code |
|---|---|---|---|
| **List rows** | A list of things that each have a state or an action: downloads, requests, apps, connections, jobs | Real tabular data (use a table); things people browse by picture (use cards or covers) | `.rows > .row`, `.row__title`, `.row__meta`, `.row__side` |
| **Row that opens** | A row whose details or settings live in a slide-out | A row with several unrelated buttons | `.row--opens`; the title is the button, the whole row is the target |
| **Cards** | One thing people pick from a few: an app, a drive, a plug-in in a catalogue. It opens its page or slide-out | A box to group content (use a panel); a list of more than about 24 (use rows) | `.cards > .card`, `.card__title`, `.card__meta`, `.card__actions` |
| **Panels** | Grouping parts of a page under one heading: Overview's parts, a dashboard area | One clickable thing (use a card) | `.panel`, `.panel__head` |
| **Status chips** | A state in words: Running, Needs attention, Not answering | A number, a date or a count (use the meta line or a count badge); more than two in one place (use facts) | `.chip[data-tone]`, beside its title (section 7) |
| **Status icons** | The state of each thing in a long list of apps or permissions | A single heading's state (use a chip) | `.status-icon[data-tone]` |
| **Filter chips** | Filters that can be on together: Films, Series, Missing | One choice of several (use a segmented control) | `.filter-chips > .filter-chip[aria-pressed]` |
| **Segmented control** | One of two to five short choices that changes the view: Week or Month, Rows or Covers | Filters that combine | `.segmented` |
| **Toolbar** | Everything that changes what a list shows, on one line under its heading: search, filters, sort, view, then the count at the end | Actions on the items (use a selection bar or the row's own buttons) | `.toolbar`, `.toolbar__row`, `.toolbar__end`, `.toolbar__count` |
| **Selection bar** | Actions on several chosen items: Follow, Delete | One item's action (use the row) | `.selection-bar` |
| **Notices** | Something on this page people should know or fix: one sentence, then what to do, with at most one button | Something that happened elsewhere or later (use a toast); a saved setting (use a saved note) | `.notice[data-tone]` with an icon and `.notice__title` |
| **Toasts** | Something that happened that the page does not show: an update started, a file downloaded | A saved setting, an error that belongs to a field or row (show it there) | `SharedComponents.toast` |
| **Empty state** | A list or part with nothing in it, or that could not load: what is missing and the one thing to do | A loading list (use skeletons) | `.empty` with one primary button |
| **Dialogs** | A decision or a short task that must finish first: confirm a removal, a password, one or two fields | Details of an item, or editing something with several fields (use a slide-out); help (use a slide-out) | `<dialog class="dialog">`; danger: `.btn--danger` and Cancel |
| **Slide-outs** | Details of one item, editing it, or help, while the list stays in view | Something people return to or link to (use a page) | `.side-panel` |
| **Tables** | Real tabular data that people compare across columns: logs, history, a comparison | A list of things with actions (use rows) | `.table-wrap[data-stack] > .table`; stacks into cards on phones |

Rules:

- **One kind per list.** A list is all rows, all cards or one table, never a mix. A list that can be rows or covers
  says so with a segmented control in its toolbar.
- **The state is next to its name.** In a row it is the first thing in `.row__side`; on a card it is in
  `.card__meta`; on a heading it is on the heading's line (section 7). Never on a line of its own.
- **Actions sit after the state.** A row has at most two buttons; more go in its slide-out or a menu button. A card
  has at most one button besides opening it.
- **A filter shows its count**, such as `Films 12`, and `All` comes first. The toolbar's count says how many are
  shown, such as `24 of 310`.
- **A notice says what to do.** Its title is the state ("Not answering"), its sentence says why and what to do, and
  its one button does that. Two notices in one place become one.
- **Feedback goes where people look.** A saved setting: a saved note beside it. An error about a field or a row:
  on the field or row, and focus goes there. Only what happens elsewhere or later is a toast.
- **Dialogs are short.** Up to two fields. Anything longer is a slide-out with its one Save in the foot.
- **Words for state changes** are Activate and Deactivate, never Turn on, Turn off, Enable or Disable.

## 11. Load more as you scroll

UX-52, owner, 9 November 2026. A long list can load its next page as its end comes into view, so people browse
without pressing Show more each time. It is built on the Show more button, never instead of it.

**Use it for** long walls and lists people browse in order: a library wall, a history, a wanted list.

**Do not use it for** results people compare or come back to by position, a table people sort and scan, or a list
with things after it that people need often. Use Show more alone, or pages.

**How it behaves** (`SharedComponents.loadMore`, classes in `LIBRARY.md`):

- The list ends with `.load-more`: a count ("Showing 40 of 2,418 films") and a real button ("Show 40 more"). The
  button is in the page's markup, so it is there before any script and if script fails.
- One IntersectionObserver per list watches that box and loads the next page when it comes within 600px of the
  screen. No scroll handlers and no timers, so a list costs nothing while nobody scrolls.
- While loading, a visible line says "Loading the next 40". When done, a polite status says "40 more shown" (or
  "40 more films shown"). A whole list is never a live region.
- Focus never moves on its own. A keyboard user who Tabs through the list reaches the new items next.
- Pressing the button loads the next page and moves focus to the first new item, so reading carries on there.
- **The footer stays in reach.** It loads only when the end comes into view, and after three pages in a row it
  pauses with "Paused here so you can reach the end of the page". The button starts a new run.
- **The button alone** when Reduce motion is on, when the person's setting asks for the button (an app offers one,
  saved per account), and in a browser without IntersectionObserver.
- **The A to Z list keeps working.** Jumping to a letter not yet shown loads up to it, moves focus to its heading,
  and starts the count of pages again (`reset()`). Back to top is never covered.
- A list of thousands may keep only what is near the screen (Show earlier titles at the top), so memory stays low.

