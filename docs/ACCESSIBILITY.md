# Accessibility guide

Version 2.0, 27 November 2026. For Starboard, its plug-ins, Stallboard, Snaglist and the design system itself. This is the one
place to read about accessibility. It brings together what the other guides say, so a person or an AI assistant does not
have to search. The floor is **WCAG 2.2 level AA** on every page, in every theme and every layout.

The other guides keep the detail, and this guide links to them. `WCAG.md` says how each WCAG point is met.
`ALT-TEXT.md` says how to write text descriptions. `AI-CHECKS.md` holds the AI-triggered **Accessibility check**.
`CONTENT-DESIGN.md` section 8 holds the content rules. [LIBRARY.md](LIBRARY.md) holds each component's own rules.

**For AI agents:** every rule marked **Check** must pass before a change is finished. Never say a change is done until
the gate in section 3 passes. Where a check is marked **in progress**, it does not exist yet: run the checks that do
exist, and say in the pull request which ones you could not run.

## Contents

1. [What we promise](#1-what-we-promise)
2. [How the checks fit together](#2-how-the-checks-fit-together)
3. [Finishing a change: the gate](#3-finishing-a-change-the-gate)
4. [Display and accessibility settings](#4-display-and-accessibility-settings)
5. [Keyboard and focus](#5-keyboard-and-focus)
6. [Reading and focus order](#6-reading-and-focus-order)
7. [Names and labels](#7-names-and-labels)
8. [Target size](#8-target-size)
9. [Colour and contrast](#9-colour-and-contrast)
10. [Forms and errors](#10-forms-and-errors)
11. [Dialogs and slide-outs](#11-dialogs-and-slide-outs)
12. [Menus and tabs](#12-menus-and-tabs)
13. [Wizards and long jobs](#13-wizards-and-long-jobs)
14. [Tables](#14-tables)
15. [Charts](#15-charts)
16. [Live regions and status messages](#16-live-regions-and-status-messages)
17. [Images, icons and alt text](#17-images-icons-and-alt-text)
18. [Motion and reduced motion](#18-motion-and-reduced-motion)
19. [Zoom and reflow](#19-zoom-and-reflow)
20. [Forced colours and high contrast](#20-forced-colours-and-high-contrast)
21. [Plain English and cognitive needs](#21-plain-english-and-cognitive-needs)
22. [Voice control](#22-voice-control)
23. [Switch access](#23-switch-access)
24. [Touch](#24-touch)
25. [Component contracts](#25-component-contracts)
26. [Testing: every check](#26-testing-every-check)
27. [Standing rules](#27-standing-rules)
28. [Themes and known gaps](#28-themes-and-known-gaps)
29. [Where the detail lives](#29-where-the-detail-lives)

## 1. What we promise

Every page of every app that uses this design system:

- **Meets WCAG 2.2 level AA.** `WCAG.md` lists each criterion and how it is met.
- **Works in four themes:** Light, Dark, High contrast and High contrast dark. Colour pairs are measured by `tools/contrast.py`.
- **Works by keyboard alone.** Every control is reached in a logical order, focus is always visible and nothing traps it.
- **Works with screen readers.** Pages have real headings, landmarks, labels, roles and states, and say short things politely.
- **Works with voice control.** Every control answers to the words shown on it (Label in Name, 2.5.3).
- **Works at 400% zoom and 320 pixels wide,** at 175% text size and with wider text spacing, with no sideways scrolling of the page.
- **Works in forced colours** (the Windows contrast themes) and in the library's own High contrast.
- **Respects reduced motion,** from the device or from the Display setting, and nothing flashes.
- **Uses plain English,** with errors that say what went wrong and how to fix it.

Passing the checks does not mean a page conforms. It means the checks that ran passed. Automatic tools find only
some problems, and people who use assistive technology find the rest (section 26).

## 2. How the checks fit together

Design rules are turned into checks that the agent runs itself, so nobody has to remember them. The table says, for each rule,
which check proves it, who runs it, when and where the result goes. A check marked **in progress** is being built in Starboard.
It is named here so that nobody claims it exists.

| Rule | Automatic check | Who runs it | When | Where results go |
|---|---|---|---|---|
| WCAG 2.2 AA, structure, target size, forced colours, reduced motion | `tools/a11y.sh` (axe-core) | The agent, through the gate | Before a pull request is marked ready | The gate summary in the pull request |
| Reading and focus order | `ORDER=1 tools/a11y.sh` | The agent | The same | The same |
| Keyboard tasks, focus after actions | `TASKS=1 tools/a11y.sh` | The agent | The same | The same |
| Side menu and header at large text, wider spacing, short window | `LAYOUT=1 tools/a11y.sh` | The agent | The same | The same |
| Colour contrast in four themes and every accent | `tools/contrast.py`, `tools/check_accents.py` | The agent | Every design system change | The reports in the repository folder (not committed) |
| Tokens only, no raw colours or sizes | `tools/check_tokens.py` | The agent | Every design system or app style change | The command output |
| Banned words, `See` and `Look`, plain English | `tools/check_words.py`, `tools/verbose-check.py` | The agent | Every change to text | The command output |
| Demos never cover the header | `node tools/check_demos.mjs` | The agent | Every design system change | The command output |
| Label in Name (2.5.3) | Automated check, **in progress** | The gate, once built | Every pull request | The gate summary |
| Target size of each control (2.5.8) | Per-control confirmation, **in progress** | The gate, once built | Every pull request | The gate summary |
| Keyboard-only and tab order in every wizard path | Playwright tasks and a coverage checker, **in progress** | The gate, once built | Every pull request | The gate summary |
| All of these in one run | `tools/done-check.sh`, **in progress** | The agent | Before "done" is said | The gate summary, in the pull request |
| Axe and reading order on the pages a change touches | A light GitHub accessibility job, **in progress** | GitHub | Each pull request | The pull request's checks |
| What no tool can judge: labels, plain wording, empty and error states, focus after actions | The per-screen acceptance checklist and the agent's self-review of its diff | The agent, then the owner | Before a pull request is marked ready | The pull request description |
| A real screen reader, voice control, a switch, touch comfort | The manual test plan (section 26) | A person | Before a release | `test-plan/runs/`, listed on the plan |
| Whole-product check on request | The AI-triggered Accessibility check (`AI-CHECKS.md` section 5) | An AI assistant, on the owner's words | When the owner asks | The report, from the template |

The full journeys, the security scans and the other heavy checks stay on the owner's computer, run through the heavy-run
script. GitHub runs only the light job, so a pull request stays quick.

## 3. Finishing a change: the gate

**Standing rule (27 November 2026):** never say a change is done, and never mark a pull request ready, until
`tools/done-check.sh` passes on the final tip and its summary is in the pull request.

`tools/done-check.sh` is **in progress** in Starboard. It runs the checks of section 2 in one go, through the heavy-run script. Known failures
on main are kept in a baseline file, and only new failures fail. Until it exists, run the checks of section 26 by hand and put their numbers in the pull request.
Never write Pass for a check that was not run.

**Before a pull request is marked ready, the agent reviews its own diff against the design system.** The review checks for:

- a colour or a size that is not a token (`tools/check_tokens.py`);
- the wrong control height token: side-by-side controls share one (`--control-h`, 44px; `--control-h-compact`, 32px, dense table rows only);
- a component the library does not list (use the library's classes first, and add a new one to the design system, not the app);
- a banned word, or `See` or `Look`, in interface text or help (`tools/check_words.py`);
- a control with no visible name, or a name that does not start with its visible words (section 7).

**Each screen or wizard has a short acceptance checklist** for what the checks cannot judge: the labels, plain wording, the empty and
error states, focus after each action, and what "done" means to a person. This is **in progress**. Until it exists, write
those five points in the pull request for each screen the change touches.

**Pictures wait until release.** Screenshots and help pictures are made once, before a release, and not for each pull
request. The rule of `HELP-WRITING.md` still holds when they are made: every tier one topic has at least 3 marked-up screenshots,
each described in words (`SCREENSHOTS.md`). Nothing in this guide asks for a picture to be committed.

## 4. Display and accessibility settings

Every page of every app, Sign in and Set up included, has the **Display** button as the last item in the header. It opens the
Display and accessibility slide-out ([the Shell page](../components/shell.html)). The choices, in this order:

| Setting | Values | Default |
|---|---|---|
| Theme | Match device, Light, Dark | Light (owner, 18 November 2026) |
| Text size | 100%, 125%, 150%, 175% | 100% |
| Reduce motion | Match device, Active, Inactive | Match device |
| High contrast | Switch | Inactive |
| Underline links | Switch | Inactive |
| Wider text spacing | Switch | Inactive |
| An app's own choices | After these (Starboard: Design) | |
| Done, Reset | Buttons in the foot | |

Choices apply at once. They are saved to the person's account where the app has accounts (the design task UX-29), otherwise in the
browser. `components.js` applies them from `data-display` inputs.

Every page uses Atkinson Hyperlegible Next, a typeface designed for readers with low vision, so there is no separate low-vision font switch.

**Check:** the structure of every page. One h1 per page; headings in order; landmarks (`header`, `nav`, `main`) on every page; a
"Skip to main content" link is the first focusable element; the browser tab title names the page ("Updates · Starboard") (WCAG 1.3.1, 2.4.1, 2.4.2).

## 5. Keyboard and focus

WCAG 2.1.1, 2.1.2, 2.1.4, 2.4.7, 2.4.11, 2.5.7.

- **Check:** everything works with a keyboard alone, in a logical order.
- **Check:** focus is always visible (3px outline at 3:1 contrast against both neighbours).
- **Check:** the sticky header and save bar never cover what has focus (2.4.11). The library's `scroll-padding` does this for `.site-header`
  and `.save-bar`; never add a sticky part of your own.
- **Check:** drawers and dialogs move focus in, trap it, return it to the opener on close, and close with Escape. Side panels follow the same rule.
- **Check:** no keyboard trap anywhere else.
- **Check:** no single-key shortcuts, or a way to turn them off (2.1.4).
- **Check:** every drag has a way to do the same with buttons or the keyboard (2.5.7). The library has no drag-only control.
- **Check:** horizontal shelves can be operated by buttons, not only by scrolling (task UX-30).
- Help, where the app has it, is in the footer of every page (3.2.6).

| Do | Do not |
|---|---|
| Use the library's components, which carry the keys | Add a sticky part of your own, or a shortcut of one key |
| Test with Tab, Shift + Tab, Enter, Space, arrows, Home, End and Escape | Remove the focus ring, or use `outline: none` |
| Give a drag a pair of Move up and Move down buttons (`setupSortables`) | Make an action that only a drag, a hover or a long press can do |

**Shows it:** [Menus and tabs](../components/menus-and-tabs.html), [Slide-outs and dialogs](../components/slide-outs-and-dialogs.html).
**Proved by:** `TASKS=1 tools/a11y.sh` (the keyboard walk) and the scan's focus checks.

## 6. Reading and focus order

WCAG 1.3.2, 2.4.3, 3.2.3.

- **Check:** the reading order, which a screen reader follows, matches the visual order and the order of the task; Tab never jumps back up a column;
  landmarks are in order and named when there is more than one of a kind.
- **Check:** after each action, focus lands in a sensible place (section 11 and this list).
- Nothing opens by itself on a page load; a slide-out opens only when the person asks for it.
- A form in a slide-out starts in its first field. A confirm box starts on its first field, or on Cancel when the choice is a danger.
- A notice goes after the page's heading, never before the h1.
- Show more moves focus to the first new item and says how many were added. Loading by itself (UX-52) never moves focus, says how many
  were added politely, and pauses after three pages.
- After a save, delete or redraw, focus stays where the person was, never the top of the page. A bulk action moves it to the next sensible item.
  The focus keeper in `common.js` and `renderKeyed()` do this.
- Navigation is in the same place every time: one header, one main menu and one phone menu in every app (3.2.3).
- No needless repeats: the same link text for different places with no extra name, a button and a link that do the same thing next to each other, a
  status said twice, the same tip on every row (`AI-CHECKS.md` section 5.3, step 4).

| Do | Do not |
|---|---|
| Keep the order the page reads in the order of the markup | Reorder with CSS so that Tab and the eye disagree |
| Return focus to the opener, or to a stand-in when it is gone | Let focus fall to the top of the page after a save |

**Shows it:** [Slide-outs and dialogs](../components/slide-outs-and-dialogs.html). **Proved by:** `ORDER=1 tools/a11y.sh` and the keyboard walk.

## 7. Names and labels

WCAG 1.3.1, 2.4.4, 2.4.6, 2.5.3 (Label in Name), 4.1.2.

- **Check:** every control has a visible text name written as an action. Icon-only buttons have an `aria-label` that **starts with** any words
  they show ("Close summary").
- **Label in Name (2.5.3):** the accessible name must contain the visible text, at the start. A person who says `click Save` must reach a
  control whose visible words are "Save". Hidden text only adds to the end ("Mark as read: the alert's title" is fine for a button that shows "Mark as read").
- **Check:** each control says what it is, its state and its changes (4.1.2): menus, switches, filter chips, tabs and dialogs use the right
  roles and states (`aria-expanded`, `aria-pressed`, `aria-current`). Filter chips put their count in the name ("Waiting, 1").
- Links name the destination and any file type. A link that opens a new tab shows the `external-link` icon and says "(opens in a new tab)" for screen readers.
- A name never says "button" or "link" in words, and an `aria-label` never repeats the visible text a second time.
- Text in another language is marked with `lang`, such as `lang="fr"` for a French book title (3.1.2). Every page is `lang="en-GB"` (3.1.1).
- Fields say what they are for with `autocomplete` (1.3.5).

| Do | Do not |
|---|---|
| Start an `aria-label` with the visible words | Give a button the visible name "Save" and the accessible name "Store changes" |
| Name the thing: "Show API key", "Remove Disk 3" | Use the same name, such as "Edit", for many controls with no extra name |
| Use `data-tooltip` to name an icon | Put information in a tooltip that exists nowhere else |

**Shows it:** [Actions](../components/actions.html), [Inputs](../components/inputs.html). **Proved by:** the scan (names, roles, duplicate names) today; the automated
Label in Name check is **in progress**. Voice control (section 22) is the human proof.

## 8. Target size

WCAG 2.5.8 (the AA floor is 24 by 24 CSS pixels). Starboard's sizes are higher, so the floor is never in doubt.

| Size | Where |
|---|---|
| 44px | Every control: buttons, fields, selects, the rows of choices, menu tabs, icon buttons (`--control-h`) |
| 32px | Dense table rows only (`--control-h-compact`) |
| 24px | The floor. Ticks and radios are drawn 22px inside a 44px row; a row's or card's name is at least 24px tall |

- **Check:** controls are at least 44 by 44 pixels, apart from dense table rows. Nothing is smaller than the library's targets.
- Side-by-side controls share one height token. Measure before you show anyone.
- A whole card is the target for a card that opens something.

| Do | Do not |
|---|---|
| Use `.btn`, `.input`, `.select`, `.check` and `.icon-btn` as they are | Shrink a control to fit a row, or set a height in pixels |
| Use 32px only in a dense table | Use 32px in a form, a toolbar or a card |

**Shows it:** [Actions](../components/actions.html), [Type, space and icons](../foundations/type-space-icons.html). **Proved by:** the scan's target size
rule today; a per-control target size confirmation is **in progress**.

## 9. Colour and contrast

WCAG 1.4.1, 1.4.3, 1.4.11.

- **Check:** body text 4.5:1, large text and parts of controls 3:1, in Light, Dark, High contrast and High contrast dark. `tools/contrast.py` and
  `tools/check_accents.py` measure every pair, for every accent, and fail any pair under its ratio.
- **Check:** status is never shown by colour alone: every chip has text and its icon or shape.
- **Check:** links in body text are distinguishable without colour (underline, or Underline links on).
- No instruction depends on colour, shape, icon or position alone (`CONTENT-DESIGN.md` section 8).
- Use the colour tokens, never a raw colour. Accent colours change only the accent roles.
- Chosen days, current items and selected rows carry a tick or a bar as well as colour.

| Do | Do not |
|---|---|
| Use `var(--color-*)` and `--status-<tone>-*` | Write a hex or `rgb()` value in a component |
| Say "Failed" with the danger shape | Ask someone to find "the red one" |

**Shows it:** [Colour](../foundations/colour.html), [Accent colours](../foundations/accent-colours.html). **Proved by:** `tools/contrast.py`, `tools/check_accents.py`, `tools/check_tokens.py` and axe.

## 10. Forms and errors

WCAG 1.3.5, 3.3.1, 3.3.2, 3.3.3, 3.3.7, 3.3.8.

- **Check:** form fields have visible labels (`.field__label`), with instructions in `.hint` before the field, never in the placeholder (3.3.2).
- **Check:** errors are tied to their field (`aria-describedby`, `aria-invalid`) and say what is wrong and how to fix it (3.3.1, 3.3.3).
- **Error summary:** after a failed submit of a form of more than one field, `.error-summary` is focused and read at once; its links move focus to each field; the page
  title starts with "Error: " and each field's error has a hidden "Error: " first.
- **Check:** name, email, username and password fields have `autocomplete`; signing in allows pasting and password managers, with no puzzle or CAPTCHA (1.3.5, 3.3.8).
- **Check:** nothing asks for the same information twice in one task (3.3.7). A wizard fills in what someone already gave, or lets them choose it.
- A required field's label ends with a star (`.field__required`, `aria-hidden`) and the control has `required`; the key "* = Required" is in the help slide-out.
- Secret fields say "Show API key" politely, never place the value in markup or a message, and copy confirms without the value.
- The schedule picker reads the schedule back in words and shows the next run through `role="status"`.

| Do | Do not |
|---|---|
| Put the label first, then the hint, then the error | Use the placeholder as the label |
| Say "Enter a server address that starts with http" | Say "Invalid input" |

**Shows it:** [Inputs](../components/inputs.html). **Proved by:** the scan, the keyboard walk and the demos check.

## 11. Dialogs and slide-outs

WCAG 2.1.2, 2.4.3, 2.4.11.

- **Check:** a slide-out, dialog or phone menu moves focus in (to Close), keeps Tab inside, closes with Escape and Close, returns focus to the opener, and the page behind does not scroll.
- A press outside closes a slide-out or menu. A slide-out's open item can be in the address, so Back closes it.
- A dialog is `<dialog class="dialog">` with `aria-modal="true"`, labelled by its title. Danger actions use `.btn--danger` and Cancel.
- A slide-out or popover is `role="dialog"` named by its heading; a popover is not modal and closes on a press outside or Tab out.
- A slide-out never opens by itself.
- Choose well: a slide-out for the details or editing of one item, a dialog for a decision that must finish first, a page for something people return to ([Choosing](../patterns/choosing.html)).

| Do | Do not |
|---|---|
| Start a form in its first field; a danger confirm on Cancel | Open anything by itself on a page load |
| Give focus to a stand-in if the opener is gone | Let focus fall to the top of the page |

**Shows it:** [Slide-outs and dialogs](../components/slide-outs-and-dialogs.html). **Proved by:** the keyboard walk (focus in, Escape, focus back) and axe.

## 12. Menus and tabs

WCAG 1.3.1, 2.1.1, 2.4.3, 2.4.7, 2.4.11, 2.5.8, 4.1.2. The full rules are in [Menu rows: condensing and accessibility](LIBRARY.md#menu-rows-condensing-and-accessibility).

- A 2nd level menu row is a `nav` with its own accessible name, links and `aria-current="page"` on the current one. It is **not** `role="tablist"`: each item is a link to a page.
- Real tabs (`.tabs`) use `role="tablist"`, `tab` and `tabpanel`, one Tab stop for the list, arrow keys, Home and End. Never mix links and tabs.
- Left, Right, Home and End move between links in a menu row. Enter opens. The focused tab shows its name and is scrolled clear of the fade.
- When the names do not fit, the row shows icons only. Every tab stays 44px wide. The current tab and the tab with focus keep their name; the others have `data-tooltip`.
- No hover-only information. Forced colours: a `Highlight` bar and outline. The scroll into view is a jump, not an animation.
- Filter chips are buttons with `aria-pressed`; the count is part of the name.

| Do | Do not |
|---|---|
| Short noun names in sentence case, a text name on every tab | Two tabs with the same icon or name in one row |
| Show the current tab by a bar and `aria-current`, plus colour | Show the current tab by colour or an icon alone |
| Use `.tabs` for panels inside a page | Use the menu row for panels inside a page |

**Shows it:** [Menus and tabs](../components/menus-and-tabs.html), [Panels, cards and tabs](../components/containers.html).
**Proved by:** axe in four themes at 100% and 175% text (clean on the gallery page, 26 November 2026), the Tab and arrow walk, and the menu minimum size at 320, 375, 430 and 768px.
Not covered: a full pass with each screen reader.

## 13. Wizards and long jobs

WCAG 2.4.3, 3.3.7, 4.1.3. The wizard rules are in [WIZARD.md](WIZARD.md); the terminal rules are in [TERMINAL.md](TERMINAL.md).

- **Check:** keyboard only. Every choice, link, dialog and Back works, and focus moves to each new step's heading (`tabindex="-1"` on the heading).
- The progress bar is `role="progressbar"` with `aria-valuenow`, `aria-valuemax` and `aria-valuetext` in words ("Step 7 of 18: Usenet"). A job's bar is drawn once and updated in place.
- An error goes under the bar, tied to it by `aria-describedby`, and focus moves to the error's heading. The choices are Try again, Show the details or Stop.
- The step's result goes into a polite live region. A wizard in a slide-out counts "Step 1 of 3" in one muted line.
- Back returns to the step before and loses nothing. Continue saves the answer.
- A state chip always has words ("Works after the switch"), never colour alone.
- In a terminal, plain mode is for screen readers: numbered choices, no clearing, no box characters, no QR code (the link is printed), and a progress line no more often than every few seconds.

**In progress in Starboard:** Playwright keyboard-only and tab order tasks for every wizard path (reach every control in the visible order, visible focus, no trap,
Escape returns focus to the opener, focus lands on the new step's heading), an axe scan of each wizard step, and a coverage checker that fails when a registered wizard has no keyboard task.

| Do | Do not |
|---|---|
| Walk every job and every choice that leaves steps out, to the end | Test only the first path |
| Name the last step's button for the action ("Switch to Plex") | Use "Finish" |

**Shows it:** [Wizard](../patterns/wizard.html), [Terminal](../patterns/terminal.html). **Proved by:** the keyboard walk today; the wizard tasks of this section are **in progress**.

## 14. Tables

WCAG 1.3.1, 1.4.10.

- Real tables only: `th`, `scope="row"` for a row's heading, `th[aria-sort]` for a sorted column. Never a grid of `div` elements.
- Tables stack into cards on phones (`.table-wrap[data-stack]`). A wide table may scroll inside its own region, and the keyboard reaches that region.
- A table has a caption or a heading that names it. Several tables one after another use `.table--fixed` and the same `colgroup` so the columns line up.
- A row's action buttons are 32px only in a dense table; they are still named with the thing ("Remove Disk 3").

| Do | Do not |
|---|---|
| Use `.table` and `.table-wrap` | Use a table for layout |
| Say a sort in words as well as the arrow | Show a sort by the arrow alone |

**Shows it:** [Content](../components/content.html). **Proved by:** the scan and the reflow check at 320px.

## 15. Charts

WCAG 1.1.1, 1.4.1, 1.4.11.

- A chart always has a table view in a disclosure, so the description can be short. The main point is in the text description, and the full data is on the page.
- A meter or progress bar carries its value in words ("76% used"). A sparkline is hidden from screen readers; `.stat__trend` says the same in words.
- A second series is dashed or shaped, never colour alone. Series colours are `--series-1` to `--series-7`, measured in all four themes. High contrast has its own chart colours.
- A gauge's drawing is `aria-hidden`; its value and label are text.

| Do | Do not |
|---|---|
| Give a chart its table and a one-sentence main point | Rely on the picture for the data |
| Use chart tokens | Pick a series colour by hand |

**Shows it:** [Content](../components/content.html) (line chart, sparkline, gauge, meter). **Proved by:** axe, `tools/contrast.py` and reading the page in order.

## 16. Live regions and status messages

WCAG 1.3.1, 4.1.3, 2.2.1.

- **Check:** status changes without a page load are announced politely (`aria-live="polite"`), such as downloads finishing and search results arriving.
- Toasts are read out through hidden regions: errors through `role="alert"`, the rest through `role="status"`. Focus never moves to a toast.
- A toast stays at least 5 seconds (10 with an action), a warning 10, an error until closed, and each waits while the pointer or focus is on it. Close is named with the message.
- **Check:** anything a toast offers, such as Undo, can also be done on the page (2.2.1).
- A saved note is `role="status"` beside the button that saved. A page banner is said once (danger at once, the rest politely) and is not sticky.
- Short spoken summaries only: counts, saved, errors. A whole list or section is never a live region. A status said in a chip is not said again in a live region.
- Load more: "40 more shown" is said politely. A combobox says the number found from inside the box. The log viewer never reads new lines, and says new errors politely only while following.
- A notice is `role="status"` unless it is an error that blocks (`role="alert"`).

| Do | Do not |
|---|---|
| Announce results, progress and finished downloads | Announce each row of a list that changes |
| Use `SharedComponents.toast`, `notice` and the kit's `announcer` | Write your own live region for the same job |

**Shows it:** [Content](../components/content.html) (toast, notice). **Proved by:** the keyboard walk (what is said). A real screen reader is **Expected** until a person confirms it.

## 17. Images, icons and alt text

WCAG 1.1.1, 1.4.5, 1.2. The full guide is [ALT-TEXT.md](ALT-TEXT.md).

- **Check:** every image has an `alt`, empty when it is decorative. Icons beside their own words are `aria-hidden="true"`. A cover has the text description "Cover of" and the title, or `alt=""` inside a link that already names the book.
- Say what matters on this page, in about 150 characters. No "image of". A functional image says the action ("Play"), not the shape.
- Never put words in a picture (1.4.5); a logo is the exception.
- **Check:** any video has captions and any recorded speech a transcript (1.2). There is no video component today.
- A screenshot in help names the page and what it points to, and the steps say everything the screenshot shows.
- Never assume anything about the people in an image, such as age, gender or how they are related.

| Do | Do not |
|---|---|
| Name an icon-only button with `aria-label` | Rely on the icon's shape |
| Put a chart's data on the page | Put the data only in the picture |

**Shows it:** [Covers, media and shelves](../components/media.html). **Proved by:** the scan, and reading the alt text against the checklist in `ALT-TEXT.md` section 10.

## 18. Motion and reduced motion

WCAG 2.2.2, 2.3.1.

- **Check:** with Reduce motion active (or `prefers-reduced-motion` with Match device), slide-ins, fades and the loading bar animation stop or become instant (`--motion-fast` and `--motion-panel` are 0ms).
- **Check:** with Reduce motion inactive, everything moves, even when the device asks for reduced motion. Every `prefers-reduced-motion` query leaves out `:root.pref-motion-off`, and scripts ask `motionStill()`, never the media query alone.
- **Check:** nothing flashes more than three times a second; anything moving for over five seconds can be paused.
- A progress bar eases only when motion is allowed (`creepProgress`). Scrolling a tab into view is a jump, not an animation.

| Do | Do not |
|---|---|
| Ask `motionStill()` in script | Test the media query alone |
| Use the motion tokens | Write a duration in a component |

**Shows it:** [Shell](../components/shell.html) (Display). **Proved by:** the scan's reduced motion step.

## 19. Zoom and reflow

WCAG 1.3.4, 1.4.4, 1.4.10, 1.4.12.

- **Check:** works at 400% zoom and 320px width with no horizontal scrolling of the page (wide tables may scroll inside their own region).
- **Check:** text uses relative units (rem), so the Text size setting (up to 175%) and browser zoom both work. Never fix a height that text has to fit in.
- **Check:** pages work in portrait and landscape (1.3.4). Never lock the orientation.
- **Check:** the side menu and header at every text size, with and without wider spacing, and in a window 600 pixels tall. No word breaks in the middle, and nothing runs past an edge, overlaps or is cut off. Use the app's layout check (`LAYOUT=1`), as axe's reflow check does not find a menu that cuts off its own items.
- Wider text spacing clips nothing: leave room for text to grow (1.4.12).

| Do | Do not |
|---|---|
| Test 320px, 375px, 175% text and wider spacing together | Test only one of them |
| Let content wrap | Fix a width or height in pixels |

**Shows it:** [Type, space and icons](../foundations/type-space-icons.html). **Proved by:** `LAYOUT=1 tools/a11y.sh`, the scan's reflow step and `check_demos.mjs`.

## 20. Forced colours and high contrast

WCAG 1.4.11, 1.4.3.

- **Check:** in forced colours (Windows contrast themes, or `forced-colors: active` emulated), text, borders, focus rings and icons stay visible and controls are recognisable.
- The library's own High contrast switch raises borders, focus rings and muted text, and removes shadows as separators. Borders carry the structure where a shadow cannot.
- A part of the library (`LIBRARY.md`, Parts) has its own Windows Contrast rules inside it.
- Use system colours (`Highlight`, `ButtonText`) where forced colours are on. Never rely on a background image or a shadow for meaning.

| Do | Do not |
|---|---|
| Test the four themes and forced colours | Test only Light |
| Keep a border on every control | Show a control's edge by a shadow |

**Shows it:** [Colour](../foundations/colour.html). **Proved by:** the scan's forced colours step by emulation; a real Windows contrast theme is **Expected** until a person confirms it.

## 21. Plain English and cognitive needs

WCAG 3.1.1, 3.2.3, 3.3.1, 2.2.1. The rules are in [CONTENT-DESIGN.md](CONTENT-DESIGN.md).

- Plain English, British English, sentence case, no em dashes, no contractions, active voice. Average sentence 15 to 20 words and none over 25.
- Never `See` or `Look` in interface text or help: name the thing ("What is new"). Use select, not `click` or `tap`; turn on and turn off, not `activate`, `deactivate`, `enable`, `disable` or `toggle`; and no `above` or `below`.
- One idea for each step. Errors say what went wrong and how to fix it, and what is safe. No time limit without a warning and a way to extend it.
- Navigation and Help are in the same place every time.
- Buttons start with a verb and name the object. Links name the destination.
- Empty, loading and error states follow `CONTENT-DESIGN.md` section 7.

| Do | Do not |
|---|---|
| Write "Select Save" | Write `click Save` |
| Say what changed and what to do | Say "Something went wrong" |

**Proved by:** `tools/check_words.py`, `tools/verbose-check.py` and reading. Whether wording is clear needs a person.

## 22. Voice control

WCAG 2.5.3 (Label in Name), 2.4.6. Voice control software lets a person speak the name of a control. It works only when the accessible name contains the
visible text (section 7).

**Rules**

- Every control answers to the words shown on it. The accessible name starts with the visible text.
- A control with no visible words (an icon button) has a name that makes sense when spoken: "Close summary".
- Two controls on a page do not share a name unless the extra words tell them apart ("Remove Disk 3", "Remove Disk 4").
- A control reached only by `show numbers` is a finding, because its name does not match.

**Automatic part.** An automated Label in Name check, which compares each control's accessible name with its visible text and fails new mismatches against a baseline,
is **in progress**. It cannot hear a person speak, and it cannot judge whether a spoken name is natural. A person must run the manual steps.

**Manual steps.** All of these are **Expected**: they are written from the vendors' guides and have not been run on this page. Use the sample page set of
`AI-CHECKS.md` section 5.4 (the heading, the main navigation, one form with a required field and an error, a button that opens a dialog, and a save). Use a test copy with made-up data.

| Software | Start it | Steps |
|---|---|---|
| Windows Voice Access (Windows 11) | Settings, Accessibility, Speech, Voice access. Say `voice access wake up` if it sleeps. | 1. Say `click Save` for a button, or `click` and a link's words.<br>2. Say `show numbers`; a number appears on each control.<br>3. Say `click 12` for the control numbered 12.<br>4. Say `hide numbers`.<br>5. Say `scroll down` and `go back`. |
| Dragon (Windows, with its Chrome or Edge extension) | Start Dragon, switch the browser extension on and the microphone on. | 1. Say `click Save`.<br>2. Say `show numbers`, then say the number.<br>3. Say `click` and a link's words.<br>4. Say `go to sleep` when finished. |
| macOS Voice Control | System Settings, Accessibility, Voice Control. | 1. Say `click Save`.<br>2. Say `show numbers`, then say `click 12`.<br>3. Say `show names` to list each control's spoken name.<br>4. Say `hide numbers`. |
| iOS and iPadOS Voice Control | Settings, Accessibility, Voice Control. | 1. Say `tap Save`.<br>2. Say `show numbers` or `show names`.<br>3. Say `tap 12`.<br>4. Say `scroll down`. |

**What to note**

- A control that needs `show numbers` because saying its visible name does nothing. Its name does not match its text (a Label in Name failure). Write down the page, the visible text and what it answered to.
- A name that more than one control answers to, so the software asks which one is meant. Note it if it is the only way to tell them apart.
- A field that does not answer to its label.
- A command that opens the wrong thing, or that is slow.
- Whether names and numbers also showed on a slide-out, a dialog and a menu, not only on the page.

**Shows it:** [Actions](../components/actions.html), [Inputs](../components/inputs.html). **Proved by:** the Label in Name check (in progress) and the manual test plan's accessibility category.
The vendors' guides (Microsoft's voice access, Apple's Voice Control and Nuance's Dragon help) were not re-read for this edit.

## 23. Switch access

WCAG 2.1.1, 2.2.1, 2.5.1, 2.5.7.

- Each control is one tab stop, in a logical order, so scanning software can step through them.
- No action needs a hover, a long press, a multi-finger gesture or a drag with no button alternative.
- No timed action without a way to extend it.
- Nothing that opens by itself changes where the scan starts.

**Proved by:** the keyboard walk by script, and a person with a real switch (Switch Access on Android, or a scanning device). The script is partial; a real switch is **Expected** until a person confirms it.

## 24. Touch

WCAG 2.5.1, 2.5.2, 2.5.8, 1.3.4.

- **Check:** controls are at least 44px (section 8). A touch target never sits on top of another.
- No action needs a gesture with more than one finger, or a drag with no button.
- Pages work upright and sideways.
- On phones, tables stack into cards and the side menu becomes the phone menu.
- No information appears only on hover.

**Proved by:** the scan's target size and layout at 375px. Touch comfort needs a real phone and a person.

## 25. Component contracts

The library gives each component its accessibility contract. Use the component from the gallery, not your own markup.

| Component | Contract |
|---|---|
| Status chip | Text always present; icon `aria-hidden`; colour from the status tone tokens |
| Cover | `alt="Cover of <title>"` on its own; `alt=""` inside a link or button that already has the title as its name |
| Drawer / side panel | `role="dialog"` or `aside` with a heading; focus moves to the heading; Escape closes |
| Dialog | `role="dialog"` `aria-modal="true"`, labelled by its title; focus trapped |
| Tabs / sub-menu | Navigation links with `aria-current="page"`, or real tabs with arrow-key support; never a mix |
| Filter chips | Buttons that are pressed or not (`aria-pressed`); the count is part of the name ("Waiting, 1") |
| Loading bar | `role="progressbar"` or a live text label; hidden from screen readers when idle |
| Toast | Read out through hidden regions: errors through `role="alert"`, the rest through `role="status"`; focus never moves to it. Success and info at least 5 seconds (10 with an action), warning 10, error until closed; each waits while the pointer or keyboard focus is on it; Close is named with the message |
| Saved note | `role="status"` beside the button that saved; stays until the next change |
| Load more as you scroll | A real Show more button is always there; loading by itself keeps focus where it is, shows "Loading the next 40" and says "40 more shown" through a polite status; it pauses after three pages so the footer stays in reach; the button alone with Reduce motion or when the person's setting asks for it |
| Tabs | `role="tablist"`, `tab` and `tabpanel`; one Tab stop for the list, arrow keys, Home and End; never mixed with links |
| Combobox | ARIA 1.2 with a listbox; focus stays in the box with `aria-activedescendant`; the number found and "No … match" said politely from inside the box |
| Error summary | Focused after a failed submit, read at once; links move focus to each field; "Error: " in the page title and before each field's error |
| Popover | Not modal, `role="dialog"` named by its heading; focus to the heading, Escape back to the button, closes on a press outside or Tab out |
| Tooltip | On hover and keyboard focus; the pointer can move onto it; Escape closes it; its words are already the thing's name, so screen readers skip it |
| Log viewer | A scrolling region the keyboard reaches; levels in words; new lines never read out, new errors said politely and only while following |
| Page banner | Said once (danger at once, the rest politely); not sticky; words and an icon for the tone |
| Menu row | A named `nav` of links with `aria-current="page"`; condenses to icons at 44px each (section 12) |
| Wizard progress | `role="progressbar"` with `aria-valuetext` in words; focus to the new step's heading (section 13) |

## 26. Testing: every check

### 26.1 The standard accessibility test

The standard accessibility test (TheMightyTRexUK, 12 November 2026: "needs adding to standard accessibility testing"). Whenever an accessibility test is asked for, it is all of these, never a scan alone:

| Part | How (Starboard) | What it proves | What it cannot verify |
|---|---|---|---|
| Scan | `tools/a11y.sh` | WCAG 2.2 AA by axe-core in Light, Dark and High contrast; structure; target size; reflow; forced colours; reduced motion | Meaning, order, what a person hears |
| Reading order | `ORDER=1 tools/a11y.sh` | What a screen reader reads against what is shown, on every page and in each app-card design; Tab never jumps back up a column; landmarks in order; the h1 first | Whether the order suits the task |
| Keyboard walk | `TASKS=1 tools/a11y.sh` | The main tasks by keys alone: sign in, skip link, search, open an item, change a setting, edit in a slide-out, make and revoke a key, Show more | Comfort and speed |
| Layout | `LAYOUT=1 tools/a11y.sh` | The side menu and header at large text, wider spacing and in a short window | Layouts it does not try |
| Focus after actions | The walk, and the focus keeper in `common.js` | After a save, delete or redraw, focus stays where the person was; slide-outs and dialogs give it back, or to a stand-in | Actions the walk does not do |
| What is said | The walk | Short spoken summaries only (counts, saved, errors); a whole list is never a live region | How a real reader says them |
| A person | Orca or NVDA | The headings list and one task, listened to | Tools cannot cover it |

The four themes: `tools/a11y.sh` scans Light, Dark and High contrast. High contrast dark is checked on the design system's gallery pages and by `tools/contrast.py`, and a
full scan of Starboard's pages in High contrast dark is **Not tested** until the scan does it.

### 26.2 The design system's own checks

The design system has no `a11y.sh`. For a change to it, run these on the final tip, through the heavy-run script:

| Check | Command | What it proves |
|---|---|---|
| Tokens | `python3 tools/check_tokens.py` | Every custom property used is a token |
| Words | `python3 tools/check_words.py` and `python3 tools/verbose-check.py files <file>` | No banned words (`See`, `Look`, `click` and the rest), plain English |
| Contrast | `python3 tools/contrast.py > contrast-report.txt` | Every text and control pair passes in four themes |
| Accents | `python3 tools/check_accents.py` | Every accent passes in four themes |
| Parts | `python3 tools/parts.py --check` | The light parts match the source |
| Private details | `tools/check-private.sh` | No private details in a public repository |
| Demos | `node tools/check_demos.mjs` | Nothing in a demo covers the header, in four themes at 375, 800 and 1280px |
| axe | axe-core 4.14 on each changed page, in four themes, at 100% and 175% text | WCAG 2.2 AA machine rules |
| Sync | `python3 tools/sync.py --check` | Starboard's and the others' copies match |

### 26.3 The new checks in Starboard (in progress)

These do not exist yet. Do not say they ran. The automation agent is adding them in Starboard.

| Name | What it will do |
|---|---|
| Label in Name check | An automated check that compares each control's accessible name with its visible text, and fails new mismatches against a baseline (WCAG 2.5.3) |
| Target size confirmation | A per-control confirmation of the size of each control, against the sizes in section 8 (WCAG 2.5.8) |
| Wizard keyboard tasks | Keyboard-only and tab order tasks for every wizard path, with a coverage checker that fails when a registered wizard has no keyboard task, and an axe scan of each step |
| `tools/done-check.sh` | The gate of section 3: all of the checks in one run, with known failures on main in a baseline file so only new failures fail |
| Light GitHub accessibility job | Axe and reading order on the pages a pull request changes; the full journeys and heavy checks stay on the owner's computer |

### 26.4 What an AI cannot verify

An assistant can run tools, read code and use a browser. It cannot, and the report must say so:

- hear JAWS, NVDA, Narrator, VoiceOver, TalkBack or Dragon on a device it does not have. These are marked **Expected**;
- speak to voice control, or use a real switch (section 22 and section 23);
- judge comfort: whether a page is tiring, confusing or slow;
- replace people who use assistive technology;
- be sure of wording, which changes by reader and version.

Use three marks: **Verified** (a person or assistant ran it and heard the result), **Expected** (written from the vendors' guides, not run) and **Not tested**.
`AI-CHECKS.md` section 4 and section 5 hold the full list, the steps for each technology and the report.

### 26.5 The Accessibility check (AI-triggered)

The words "Accessibility check" start the full procedure in [AI-CHECKS.md](AI-CHECKS.md) section 5: the standard test, every type of assistive technology, logical
order, no needless repeats and a report with a table for each page. It has a prompt to copy and the
[report template](../resources/accessibility-check-report-template.md).

### 26.6 The manual test plan: the human check

A person runs the manual test plan before a release. It has 288 tests in 25 categories, and the accessibility category covers a real screen reader pass, voice control and touch. Each test is ticked and
recorded. **Log an issue** opens a prefilled GitHub issue. Every saved run is kept in `test-plan/runs/` and listed on the plan. A real screen reader pass by a
person needs the plan's accessibility category; nothing in this guide replaces it.

### 26.7 How to test by hand

1. Keyboard: put the mouse away; Tab through the page; open and close every slide-out and dialog.
2. Zoom: browser at 400%, and the Text size setting at 175%.
3. Themes: Light, Dark, High contrast and High contrast dark; check chips, focus rings and controls that are not available.
4. Screen reader: Orca on this computer, or NVDA on Windows; read the headings list and one task.
5. Voice control: the steps of section 22.
6. Automatic: the scans of section 26.1 before each release, and the gate before each pull request is marked ready.

## 27. Standing rules

1. **Never say done until the checks pass.** Not "done", not "ready", until the gate (section 3) passes on the final tip and its summary is in the pull request. Never write Pass for a check that was not run.
2. **Pictures wait until release.** Screenshots and help pictures are made once, before a release, not for each pull request (the rule of 3 marked-up screenshots a tier one topic still holds).
3. **Plain English.** `CONTENT-DESIGN.md`: British English, sentence case, active voice, no em dashes, no contractions.
4. **No `See` or `Look`** in interface text or help. Name the thing ("What is new").
5. **Consistent control heights.** Side-by-side controls share one height token. Measure before you show anyone.
6. **Nothing smaller than the library's targets** (section 8): 44px, 32px only in dense table rows, 24px as the floor.
7. **Design rules are checks.** If a rule matters, a check proves it. Add the check, not a reminder.
8. **The agent reviews its own diff** against the design system before a pull request is marked ready (section 3).
9. **Be honest about what was tested.** Verified, Expected or Not tested. An AI never marks Verified what it could not run.

## 28. Themes and known gaps

Tokens live in the web app's theme CSS (read `DESIGN-SYSTEM.md`; the shared values are in `tokens.css`). Each theme defines the same token names. High contrast
raises borders, focus rings and muted text, and removes shadows as separators.

Known gaps:

- Horizontal scroll shelves on Discover, For you (task UX-30).
- A full scan of Starboard's pages in High contrast dark, and a real screen reader pass, are not done (section 26).
- The checks marked **in progress** in section 26.3.
- Starboard's automated check dates from 12 November 2026; the scan runs axe-core 4.14.

## 29. Where the detail lives

| Topic | Detail |
|---|---|
| How each WCAG criterion is met | [WCAG.md](WCAG.md) |
| Text descriptions for images | [ALT-TEXT.md](ALT-TEXT.md) |
| The AI-triggered Accessibility check, each assistive technology, the report | [AI-CHECKS.md](AI-CHECKS.md) |
| Words, errors, status words | [CONTENT-DESIGN.md](CONTENT-DESIGN.md) |
| Every component's classes and rules, including Menu rows | [LIBRARY.md](LIBRARY.md) |
| Wizards and the terminal | [WIZARD.md](WIZARD.md), [TERMINAL.md](TERMINAL.md) |
| Screenshots and help | [SCREENSHOTS.md](SCREENSHOTS.md), [HELP-WRITING.md](HELP-WRITING.md) |
| Free outside tools, and testing with people | [Outside tools](../resources/outside-tools.html), [Get feedback](../resources/get-feedback.html) |
| The report template | [Accessibility check report template](../resources/accessibility-check-report-template.md) |
