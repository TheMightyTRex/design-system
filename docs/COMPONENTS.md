# Storyarr UI inventory: what exists today

Taken 1 November 2026 from Storyarr's `apps/web/src` (v0.4.6 on `main`). Paths are relative to
`apps/web/src/`. This is the "before" picture for the redesign; `DESIGN-SYSTEM.md` is the "after".

**For AI agents:** re-check a path before relying on it; the code moves. Update this file when a duplicate is
merged (tasks UX-02 to UX-11).

## 1. Tokens and themes

| Area | Today | Problem |
|---|---|---|
| Colour | `theme-tokens.css` (44 KB): about 330 `--c-*` properties, defined for light, dark, auto and high contrast | Names describe values (`--c-bg-indigo-27`), not roles; near-duplicates (`-2`, `-3` suffixes); no surface, success or danger tokens |
| Semantic aliases | `styles.css:301-304`: `--surface`, `--muted`, `--line`, `--accent` (heavily used), plus per-feature aliases `--request-*`, `--explore-*`, `--review-*`, `--mam-soft` | Partial and scattered |
| Undefined | `--text`, `--bg`, `--panel`, `--border` used in import-review, library-setup, controls, mounted-folders and entity-details CSS but never defined | Silent fallbacks |
| Spacing, type, radius | None. Gaps of 4 to 18px; 32 different font sizes; `border-radius: 0` 291 times | No scale |
| Controls | `--control-*` in `controls.css` and again in `settings.css`, with different heights (30, 38, 28px) | Two definitions; below the 44px target |
| Header | `--search-row-height`, `--submenu-height`, `--topbar-height` in `header.css` | Fine |
| Theme switch | `displayPreferences.ts` `applyDisplay()`: `data-theme` (light, dark, auto) on `<html>`, root font-size %, classes `pref-hc`, `pref-readable`, `pref-calm`, `pref-underline`, `pref-spacing` (rules in `theme.css`); saved in localStorage | Works; move to account (UX-29) |
| Focus | `:focus-visible` 3px outline in `--accent` (`theme.css`) | Good |

## 2. Shell

| Piece | File |
|---|---|
| Layout setting (Classic default, Shelf) | `displayPreferences.ts`; picker `components/LayoutChoice.tsx`; `data-layout` on `.app-shell` (`App.tsx`) |
| Classic sidebar: Discover, Following, My library, Library review, Requests, Settings | `App.tsx`, `styles.css` |
| Shelf icon rail: Library, Discover, Requests, Settings | `components/ShelfNavigation.tsx` (`ShelfRail`, `LibraryTabs`), `shelf-layout.css` |
| Fixed header: search, ConnectionHealth, page actions (Add list, Refresh lists on some pages), Display | `App.tsx`, `header.css` |
| Header sub-menu (Shelf only) | `components/HeaderSubmenu.tsx`; used by Discover, Requests, Settings, LibraryTabs |
| Loading bar | `components/LoadingBar.tsx` |
| Page title | `components/PageTitle.tsx` |
| Display and accessibility panel | `components/DisplayPanel.tsx` |
| Loading skeleton | `components/ContentSkeleton.tsx` |

## 3. Pages

| Route | Page | In-page navigation |
|---|---|---|
| `/library` (`?view=authors`, `series`, `saved`) | `pages/MyLibrary.tsx` | `.page-tabs`; search; `.library-filters` selects (Media, Library, Sort); cover wall; BookSummary panel |
| `/following` | `pages/Following.tsx` | `DetailTabs` (Authors, Series, Releases); `.follow-status-filters` chips; `.follow-toolbar` select; GroupShelf Detail/List switch |
| `/following/:listId` | `pages/FollowShelf.tsx` | `.wall-header`, status chips, cover wall, its own `.book-drawer` |
| `/review` | `pages/LibraryReview.tsx` | `.page-tabs` with counts; `.settings-subtabs` reused as a filter; `.review-card`, `.review-chip` |
| `/discover` (`?view=` home, series, browse, calendar, collections, awards, yours) | `pages/Discover.tsx`, `ReleaseCalendar`, `CustomizeDiscover` | Header sub-menu or `.page-tabs`; **Customise** dialog; `.explore-filters`; `.explore-segment`; calendar `.release-toolbar`, `.release-filters`, `.release-drawer` |
| `/discover/books/:provider/:id` | `pages/DiscoverBook.tsx` | `DetailTabs` |
| `/discover/lists`, `/lists` | `pages/CommunityLists.tsx`, `pages/Lists.tsx` | Shelves, infinite scroll |
| `/series/hardcover/:id` | `pages/Series.tsx` | `DetailTabs` (Reading order, About, Requests, Lists); `.series-filter` |
| `/authors/hardcover/:id` | `pages/AuthorDetail.tsx` | `DetailTabs` (Books, About the author) |
| `/books/:id` | `pages/BookDetail.tsx` | Hand-made tab list: Overview, Library copies, Editions, Authors, Reviews, Downloads, Sources |
| `/search` | `pages/ProviderSearch.tsx` | Search form, cover grid |
| `/requests` | `pages/Requests.tsx`, `ActivityRequests.tsx` | Queue, Wanted, History with counts; `.activity-filters` link chips; sort select |
| `/settings#…` | `pages/Settings.tsx`, `SettingsSections.tsx` | Six groups (General, Accounts, Sources, Library, Downloads, System); collapsible `SettingsGroup`s |
| `/organization/inspections` | `pages/ImportReview.tsx` | Own toolbar |
| `/upgrade`, `/onboarding` | `UpgradeWizard.tsx`, `GettingStarted.tsx` | Wizard steps |

`pages/Downloads.tsx` appears unused (nothing imports it). Check, then remove.

## 4. Components that already exist (rough number of files using each)

- **Covers and cards:** BookCover (18), BookCard (8), EnrichedBookCard (2), GoodreadsDiscoveryBook (2),
  BookPresentation (2), BookLink (8), LibraryFormatBadges (2), BookSourceIcon (4), RelatedBooks, RecentLibrary
- **Shelves and lists:** DiscoveryShelf (4), DeferredShelf, DiscoveryCollections (4), ShelfViewAll (3),
  ShelfPagination (5), BookPagination (2), InfiniteScroll (28), GroupShelf (2), LibraryGroups, FollowCatalog (7),
  FollowRelease (5), FollowCollection, FollowedLists, SeriesContinuation, ListDownloads (4), Sortable (3)
- **Panels:** BookSummary, BookReaderDetails (5), SourceReleaseDetails, DownloadRecoveryDetails (2)
- **Dialogs:** BookDialog (about 20), DisplayPanel, CustomizeDiscover, AddMissingBooks (5), DeleteConfiguration (7),
  DeleteLibraryCopy (2), CollectionReview, ReportDownloadProblem
- **Status:** BookDetailsStatus, QuickAddStatus, ConnectionStatus (4), ConnectionTestStatus (4), ConnectionHealth,
  RequestNextAction
- **Actions:** QuickAdd (6), SourceReleaseDownload (2), BookDownloads, ImportExecution (2), DownloadImportReview,
  DownloadMatchReview, CombineParts (2), AssetMatchForm (2)
- **Navigation:** HeaderSubmenu (5), DetailTabs (4), ShelfNavigation, NavigationContinuity (10), PageTitle, LoadingBar
- **Forms and settings:** SettingsGroup (5), SettingHelp (15), SelectMenu (global), LanguageSelect (7),
  EditionFormatSelect (2), FollowFilterFields (3), GroupingEditor, CalendarSettings, AudibleStoreSetting,
  LayoutChoice (3), MountedFolderBrowser (2), DownloadFileBrowser, UpgradeBackups (3)
- **States:** Notice, Empty, Loading (in `components.tsx`), ContentSkeleton (4)

## 5. Duplicates to merge

| Job | Variants today | Target (DESIGN-SYSTEM.md) | Task |
|---|---|---|---|
| Book details beside a list | BookSummary (`.book-summary`), FollowShelf `.book-drawer` (`wall.css`), ReleaseCalendar `.release-drawer` (`discovery.css`), BookDialog modals | SidePanel | UX-09 |
| Book card | `.book-card`, `.discovery-book`, EnrichedBookCard, GoodreadsDiscoveryBook, `.cover-wall-book`, `.release-day-card`, `.library-group-card`, `.review-card`, assorted `.panel` cards | CoverCard, Row, Panel | UX-10 |
| Status badge | `.request-status` (defined twice in `requests.css`), `.review-chip`, `.cover-wall-chip`, `.follow-book-status`, `.series-format-status`, `.library-series-status`, `.download-review-status`, `.connection-state`, `*-folder-status` | StatusChip | UX-04 |
| Tabs | `.page-tabs` (styled in 4 files), DetailTabs, BookDetail's copy, `.settings-subtabs` used as a filter | SectionNav (links) and Tabs (in-page) | UX-11 |
| Filter bar | `.library-filters`, `.explore-filters`, `.release-filters`, `.activity-filters`, `.follow-status-filters`, `.review-chips`, `.explore-segment` | Toolbar with FilterChips and Select | UX-11 |
| Dialog | BookDialog, DisplayPanel and ReleaseCalendar `<dialog>`s, feature `*-dialog` classes | Dialog | UX-10 |
| Control size | `--control-*` in `controls.css` and `settings.css` | One control scale | UX-02 |

**Inconsistencies to fix:** in Shelf layout, Discover, Requests and Settings put their tabs in the header,
while Library pages keep page tabs under a header menu (two levels). Sort sits among filters in Library, next
to tabs in Requests, and is missing on Discover. Page headers differ (eyebrow block, hidden h1, wall header).

## 6. Status words in use today

The same state has several names. Target vocabulary: `CONTENT-DESIGN.md` section 6.

| Target | Found today |
|---|---|
| In library | "In library", "✓ In library", "In your library", "Available" |
| Not requested | "Not in your library", "Not owned", "Not requested", "Saved in your catalog" |
| Wanted | "Wanted", "Missing" (ListRequests, SeriesRequests). "Missing" also means missing files in My library |
| Needs attention | "Needs review", "Needs attention", "Download needs attention", "Source needs review", "Needs matching", "Needs verification" |
| Searching, Waiting, Downloading, Importing | "Queued", "Request queued", "Searching sources", "Waiting for source", "Preparing download", "Check inventory", "Paused", "Download not started" |
| Request outcomes (Activity History only) | "Pending", "Declined", "Withdrawn" |

Status maps today: `pages/requestStatus.ts` and `statusNames` in `pages/Following.tsx`; others are local to
each page.

## 7. CSS

About 425 KB across 28 files, nearly all global (Tailwind plus two cascade layers, `app` and `controls`).
Biggest: `styles.css` 87 KB, `settings.css` 74 KB, `theme-tokens.css` 44 KB, `discovery.css` 30 KB. No CSS
modules; per-component files still emit global selectors.
