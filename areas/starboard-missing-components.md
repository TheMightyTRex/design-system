# Starboard boards: components the library does not have yet

Found while building the Starboard area boards (2 November 2026). Each board made do with existing classes
plus minimal inline layout styles; none of them adds CSS to the library.

| Component | What it would be | Where it is needed | What the boards do for now |
|---|---|---|---|
| Line chart | One chart for Overview, Monitor, Network and the storage folder: grid, axes, one or two series (the second dashed), latest dot, legend, and a "Show as a table" view that is always there. Keyboard reading as in Starboard's `lineChart()`. Uses `--chart-1` and `--chart-2`. | Overview, Monitor, Network, Storage (folder slide-out) | Inline SVG drawn by `areas/_starboard/gen.py`, legend with inline swatches, table in a `.disclosure` |
| Bar list | Labelled horizontal bars for comparisons (temperatures, ages, thread loads) with the value in words. | Disk health, Monitor | `.meter` with `.progress` in a `.panel`, which is close enough that a separate component may not be needed |
| Icon size class | `.i`, `.i-lg`, `.i-xl` sizes for sprite icons outside `.btn`. The build script writes these classes but only the gallery's own style block sizes them. | Every board (tabs, notices, empty states, app icons) | The same three lines as the gallery, in each board's `<style>` |
| Header brand on computers | Starboard has no rail, so its name and logo belong at the start of header row 1. `.site-header__brand` is hidden above 720px and `.site-header__bar` has no left padding. A modifier such as `.site-header--no-rail`. | Every Starboard page | Inline `display:inline-flex;padding-left` on the brand |
| Phone menu button visibility | `.phone-menu-button` is declared before `.icon-btn`, so `.icon-btn`'s `display:inline-flex` wins and the ☰ button shows on computers. | Every page with a phone menu | The boards leave the button out of the desktop header; the phone frame has its own |
| Phone menu link section | A main menu item with no 1st level (Search, Downloads, Coming up) in the ☰ drawer: same look as `.phone-menu__section > button`, but a link with `aria-current`. | Starboard phone menu | Inline styles on the link |
| Stat with status words | A slot in `.stat` for the status chip, so the warning is in words ("Hot", "Nearly full"). As a grid item the chip stretches to full width. | Overview, Storage, Disk health, Network | `.chip` with inline `justify-self:start` |
| Section head with range control | A heading row with a labelled segmented control at the end ("Time range: Last hour, 6 hours, 24 hours, Live"). `.toolbar` comes close but has no heading slot and the segmented control has no visible label slot. | Overview, Network | A flex row with an inline style and a visually hidden legend |
| Row cover thumbnail | A small cover (40 to 64px) as a row's leading slot, as in Storyarr's Row. `.cover` is 100% wide. | Search, Coming up | `.cover` with an inline width |
| Clamped text | Two or three line clamp for overviews in rows. | Search results | Inline `-webkit-line-clamp` |
| Rows inside a settings section | `.settings-section__head` and `.rows` both draw a line, so a list straight under a section head has a double divider. | Manage apps, General (categories) | Inline `border-top:0` on the list |
| Code with copy | A command block with a copy button beside it. | About and updates | `.code-block` and `.copy-btn` in an inline flex row |
| Auth layout | A narrow centred page with a slim header (brand and Display only) for Sign in and Set up. | Sign in, Set up | `.page` with an inline `max-width`, and the header built from `.site-header__bar` |
| Board frame | The phone-width frame and the "What changed" band are board scaffolding, not app components; listed so nobody adds them to the library by mistake. | All boards | Inline styles, as the brief asked |


## Added to the library (2 November 2026)

Icon sizes (`svg.i`, `.i-lg`, `.i-xl`), `.site-header--no-rail`, the phone menu button fix, `.phone-menu__section > a`, `.stat .chip`, `.section-head`, `.cover--row`, `.clamp-2` and `.clamp-3`, the settings head and list divider fix, `.command`, `.page--narrow` and the line chart (`.chart*`, second series dashed). The bar list stays as `.meter` plus `.progress`. Boards still carry their inline patches until they are next rebuilt.
