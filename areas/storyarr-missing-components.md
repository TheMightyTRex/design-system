# Storyarr boards: components missing from the shared library

Found while building the Storyarr area boards (2 November 2026). The boards make do with existing classes plus
minimal inline layout styles; each item below says what the boards did instead. Nothing here was added to
`components.css`.

| # | What is missing | Where the boards needed it | What the boards did instead |
|---|---|---|---|
| 1 | **Icon sizes.** The README lists `svg.i`, `.i-lg`, `.i-xl`, but the rules live only in the gallery's own `<style>`. Without them an icon renders at 300 by 150px | Every board | A three-line board `<style>` copied from the gallery. Move the rules into `components.css` section 1 |
| 2 | **The `hidden` attribute loses to the library's display rules** (`.rows`, `.media-grid`, `.notice`, `.toolbar` set `display`), so `hidden` does not hide them | View switches (Covers or List, Month or List) | Board `<style>`: `[hidden] { display: none !important; }`. Add the same rule to the base layer |
| 3 | **Toolbar chips do not shrink on phones.** `.filter-chips` scrolls sideways only if it can shrink, but as a flex item in `.toolbar__row` it keeps its full width, so the page scrolls sideways | Every toolbar with chips | `style="max-width:100%;min-width:0"` on each chip group. Add `min-width: 0; max-width: 100%` to `.toolbar__row > .filter-chips` |
| 4 | **`.page` has no column template**, so a wide child (chips, a table) widens the whole page on phones | Every board | `style="grid-template-columns:minmax(0,1fr)"` on `main.page`. Add it to `.page` |
| 5 | **List and detail layout** (list on the left, detail on the right, list alone on phones) | Following (authors and their shelf) | Inline flex with wrap. Wanted: `.list-detail`, `.list-detail__list`, `.list-detail__detail` |
| 6 | **Selected row** state for list and detail | Following (current author) | `aria-current` plus an inline background and accent edge. Wanted: `.row[aria-current]` |
| 7 | **Item header** (cover or portrait, title, byline, status chips, facts, main actions) | Book, author, series, narrator pages | Inline flex: 176px art, text column. Wanted: `.item-header`, `.item-header__art`, `.item-header__body` |
| 8 | **Back link** | Item pages | `.btn--quiet` with an arrow icon and a negative inline margin. Wanted: `.back-link` |
| 9 | **Shelf** (horizontal row with heading, caption, View all, More, 44px arrows) | Discover For you | `.panel__head` for the header and an inline one-row `media-grid`. Wanted: `.shelf`, `.shelf__head`, `.shelf__track`, with arrows that move the track and roving focus (task UX-30) |
| 10 | **Calendar month** | Calendar | A `.table` with weekday headings and fixed cell height (works well for screen readers). Wanted: `.calendar` with an out-of-month day style and a today marker |
| 11 | **Save bar** (sticky footer with Save changes, Discard changes and the save state), modelled on File naming | Every Settings section with fields | Inline sticky `div` with `role="group"`, raised surface, border and shadow; each section wrapped so the bar sticks only while its section is in view. Wanted: `.save-bar`, `.save-bar__state` with saved, unsaved and saving states |
| 12 | **Selection bar** (sticky "n selected" with bulk actions) | Series reading order, Activity Wanted | Inline sticky `div`, same look as the save bar. Wanted: `.selection-bar` |
| 13 | **Row with a checkbox and a cover** (four columns) | Series reading order, Activity Wanted | Inline `grid-template-columns` on `.row`. Wanted: `.row--select` |
| 14 | **Cover thumbnail in rows** (48px cover as the row lead) | Library review, Activity, search, calendar | `.cover` with an inline width. Wanted: `.cover--thumb` |
| 15 | **Timeline** (ordered events with time, title and detail) | Activity request slide-out (recovery timeline) | `ol.rows` with `.row--no-lead`. Wanted: `.timeline` with a marker per event and a "now" state |
| 16 | **Extra buttons in the panel header** (Previous, Next beside Close) | Library review slide-out | Icon buttons in an inline flex span before Close. Wanted: `.panel-header__actions` |
| 17 | **Wizard step list that collapses on phones** to "Step 3 of 7" | Onboarding, upgrade | `.steps` wraps on phones, so Continue is pushed down. Wanted: `.steps` phone variant |
| 18 | **Wizard step card footer** (Continue, Back, Skip with a divider) | Onboarding, upgrade | `.actions` with an inline top border. Wanted: `.wizard__foot` |
| 19 | **Settings section head with an action** (heading and hint left, Add button right) | Notifications, Users and access, Libraries, Download clients | Inline flex inside `.settings-section__head`. Wanted: `.settings-section__action` |
| 20 | **Count inside a pressed filter chip** keeps the count colours on the accent fill; check contrast in all themes | Every toolbar | Left as is. Check, then add `.filter-chip[aria-pressed="true"] .count` |
| 21 | **Cover art** for sample books | Every board | Inline gradients, as in the gallery. Real covers are images, so no component is needed |
| 22 | **Phone preview frame** (board only, not for the apps) | Every board | `storyarr-board.js` puts a 390px iframe of the same page beside the board, so the library's real phone rules apply |
| 23 | **Folder path breadcrumbs** | Folder picker slide-out | Plain links in a `nav`. Wanted: `.breadcrumbs` |


## Added to the library (2 November 2026)

Fixed: icon sizes, `[hidden]` always hides, toolbar chips shrink on phones, `.page` has one `minmax(0, 1fr)` column. Added: `.list-detail`, `.row[aria-current]`, `.item-header`, `.back-link`, `.shelf`, `.calendar`, `.save-bar`, `.selection-bar`, `.row--select`, `.cover--thumb`, `.timeline`, `.panel-header__actions`, `.steps--collapse` with `.steps__short`, `.wizard` and `.wizard__foot`, `.settings-section__head--action`, a frame on a count inside a pressed chip, and `.breadcrumbs`. The boards keep their inline patches until they are next generated; removing them is a small clean-up in `storyarr-gen/`.
