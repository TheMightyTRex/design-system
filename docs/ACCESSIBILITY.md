# Accessibility guide

Version 1.2, 4 November 2026. For Storyarr and Starboard. The floor is **WCAG 2.2 level AA** on every page, in
every theme (Light, Dark, High contrast) and every layout (Storyarr: Classic and Shelf). Content rules are in
`CONTENT-DESIGN.md` section 8. How each WCAG point is met, and what each app must still do, is in `WCAG.md`;
how to write text descriptions for images is in `ALT-TEXT.md`.

**For AI agents:** every item marked **Check** must pass before a UI change is finished. Section 6 says how
to test each one.

## 1. Display and accessibility

Every page of both apps, Sign in and Set up included, has the **Display** button as the last item in the
header. It opens the Display and accessibility slide-out (gallery: Display button). The choices, in this
order:

| Setting | Values | Default |
|---|---|---|
| Theme | Match device, Light, Dark | Match device |
| Text size | 100%, 125%, 150%, 175% | 100% |
| Reduce motion | Match device, On, Off | Match device |
| High contrast | Switch | Inactive |
| Underline links | Switch | Inactive |
| Wider text spacing | Switch | Inactive |
| An app's own choices | After these (Starboard: Design) | |
| Done, Reset | Buttons in the foot | |

Choices apply at once. They are saved to the person's account where the app has accounts (Storyarr task
UX-29), otherwise in the browser. `components.js` applies them from `data-display` inputs.

Every page uses Atkinson Hyperlegible Next, a typeface designed for readers with low vision, so there is no
separate low-vision font switch.

## 2. Checks

**Structure**
- **Check:** one h1 per page; headings in order; landmarks (`header`, `nav`, `main`) on every page.
- **Check:** a "Skip to main content" link is the first focusable element.
- **Check:** the browser tab title names the page ("Activity · Storyarr").

**Keyboard and focus**
- **Check:** everything works with a keyboard alone, in a logical order.
- **Check:** focus is always visible (3px outline at 3:1 contrast against both neighbours).
- **Check:** the sticky header and save bar never cover what has focus (WCAG 2.4.11). The library's
  `scroll-padding` does this for `.site-header` and `.save-bar`; never add a sticky part of your own.
- **Check:** drawers and dialogs move focus in, trap it, return it to the opener on close, and close with
  Escape. Side panels (BookSummary, bookshelf drawer) follow the same rule.
- **Check:** no keyboard trap anywhere else.
- **Check:** no single-key shortcuts, or a way to deactivate them (WCAG 2.1.4).
- **Check:** every drag has a way to do the same with buttons or the keyboard (WCAG 2.5.7).

**Size and spacing**
- **Check:** controls are at least 44 by 44 pixels (24 is the AA minimum; 44 is Storyarr's standard). Ticks and
  choices are 24 by 24 at least, and a row's or card's name is at least 24 pixels tall (`components.css`).
- **Check:** works at 400% zoom and 320px width with no horizontal scrolling of the page (wide tables may
  scroll inside their own region).
- **Check:** text uses relative units, so the text size setting and browser zoom both work.
- **Check:** pages work in portrait and landscape (WCAG 1.3.4).

**Colour and contrast**
- **Check:** body text 4.5:1, large text and UI parts 3:1, in Light, Dark and High contrast.
- **Check:** status is never shown by colour alone: every chip has text (and its icon).
- **Check:** links in body text are distinguishable without colour (underline, or Underline links on).

**Motion**
- **Check:** with Reduce motion on (or `prefers-reduced-motion`), slide-ins, fades and the loading bar
  animation stop or become instant.
- **Check:** nothing flashes more than three times a second; anything moving for over five seconds can be
  paused.

**Screen readers**
- **Check:** icon-only buttons have an `aria-label` that starts with any words they show; covers have the
  text description "Cover of <title>", or `alt=""` inside a link that already names the book (`ALT-TEXT.md`).
- **Check:** text in another language is marked with `lang`, such as a French book title (WCAG 3.1.2).
- **Check:** any video has captions and any recorded speech a transcript (WCAG 1.2).
- **Check:** status changes without a page load are announced (`aria-live="polite"`), such as downloads
  finishing and search results arriving.
- **Check:** form fields have visible labels, and errors are tied to their field (`aria-describedby`).
- **Check:** name, email, username and password fields have `autocomplete`; signing in allows pasting and
  password managers, with no puzzle or CAPTCHA (WCAG 1.3.5, 3.3.8).
- **Check:** nothing asks for the same information twice in one task (WCAG 3.3.7).
- **Check:** Help, where the app has it, is in the footer of every page (WCAG 3.2.6).
- **Check:** anything a toast offers, such as Undo, can also be done on the page (WCAG 2.2.1).
- **Check:** horizontal shelves can be operated by buttons, not only by scrolling (task UX-30).

## 3. Components and their accessibility contract

| Component | Contract |
|---|---|
| Status chip | Text always present; icon `aria-hidden`; colour from the status tone tokens |
| Cover | `alt="Cover of <title>"` on its own; `alt=""` inside a link or button that already has the title as its name |
| Drawer / side panel | `role="dialog"` or `aside` with a heading; focus moves to the heading; Escape closes |
| Dialog | `role="dialog"` `aria-modal="true"`, labelled by its title; focus trapped |
| Tabs / sub-menu | Navigation links with `aria-current="page"`, or real tabs with arrow-key support; never a mix |
| Filter chips | Toggle buttons with `aria-pressed`; the count is part of the name ("Waiting, 1") |
| Loading bar | `role="progressbar"` or a live text label; hidden from screen readers when idle |
| Toast | Read out through hidden regions: errors through `role="alert"`, the rest through `role="status"`; focus never moves to it. Success and info at least 5 seconds (10 with an action), warning 10, error until closed; each waits while the pointer or keyboard focus is on it; Close is named with the message |
| Saved note | `role="status"` beside the button that saved; stays until the next change |

## 4. Themes

Tokens live in the web app's theme CSS (see `DESIGN-SYSTEM.md`; the shared values are in `../tokens.css`). Each theme defines the same token
names. High contrast raises borders, focus rings and muted text, and removes shadows as separators.

## 5. Known gaps (31 October 2026 audit)

- Horizontal scroll shelves on Discover → For you (task UX-30).
- Theme default is Light; target is Match device.
- Starboard has an automated check (12 November 2026): `tools/a11y.sh` runs axe-core (WCAG 2.2 AA) on every page in
  Light, Dark and High contrast, with the structure, keyboard, slide-out focus, reflow, forced colours and reduced
  motion checks of section 2. Storyarr has none yet (task A11Y-01).

## 6. How to test

1. Keyboard: unplug the mouse; Tab through the page, open and close every drawer and dialog.
2. Zoom: browser at 400%, and the Text size setting at 175%.
3. Themes: Light, Dark, High contrast; check chips, focus rings and disabled controls.
4. Screen reader: Orca on this computer, or NVDA on Windows; read the page headings list and one task.
5. Automated: Starboard's `tools/a11y.sh` (axe-core and the checks above), before each release.
