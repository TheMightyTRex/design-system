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
  a toast. Text fields save with `.inline-save` (one field) or `.save-bar` (several), and their Save button is
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
