# Meeting WCAG 2.2

Version 1.0, 4 November 2026. How the TRex Design System meets WCAG 2.2 level AA (the Web Content
Accessibility Guidelines), point by point, following the GOV.UK Service Manual's
[Understanding WCAG 2.2](https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag).
Every word follows `CONTENT-DESIGN.md`.

## About this guide

### What it is for

WCAG is the international standard for accessible websites and apps. GOV.UK services must meet level AA,
and so does everything in this design system. This guide says, for each thing the standard asks, what the
library already does and what each app must still do on its own pages. The checks to run are in
`ACCESSIBILITY.md`; this guide says why each one is there.

### Who it is for

Anyone who builds, reviews or tests a page of Storyarr or Starboard, or uses the design system for their
own work. No knowledge of WCAG is needed: each point is explained in plain words, with its success
criterion number for anyone who wants the full text.

### How to use it

1. Read section 1 once.
2. When you build a page, go through sections 2 to 5 and check each line marked "The app" for your page.
3. Then run the checks in `ACCESSIBILITY.md` section 2 and the tests in its section 6.

## 1. What WCAG asks

WCAG 2.2 has four principles. Content must be:

- **perceivable:** people can take it in with the senses they use, such as sight, hearing or touch;
- **operable:** people can use it however they work, such as with a keyboard, voice control or a switch;
- **understandable:** people can follow the content and predict how the page behaves;
- **robust:** browsers and assistive technology, such as screen readers, can read it reliably.

Each principle has guidelines, and each guideline has success criteria at level A, AA or AAA. Level AA
means meeting every A and AA criterion. WCAG helps people with sight, hearing, movement and thinking or
understanding impairments, and helps everyone using a small screen, bright sunlight or a slow connection.

In each table, "The library" is what `tokens.css`, `components.css` and `components.js` do for you, and
"The app" is what each page must still do.

## 2. Perceivable

| What is needed | Criterion | The library | The app |
|---|---|---|---|
| A text alternative for every image and icon | 1.1.1 | Icons beside words are hidden from screen readers; icon-only buttons need a name; meters and charts carry their value in words | Write each image's text description by `ALT-TEXT.md` |
| Captions and transcripts for video and audio | 1.2.1 to 1.2.5 | Nothing: there is no video component | Give any video captions, and any recorded speech a transcript |
| Structure a screen reader can follow | 1.3.1 | Headings, lists, tables and landmarks in every component; form fields with real labels | One h1, headings in order, `header`, `nav` and `main` on every page |
| Works in portrait and landscape | 1.3.4 | Every layout reflows; nothing is locked to one orientation | Never lock the orientation |
| Fields that say what they are for | 1.3.5 | Fields take `autocomplete` | Set `autocomplete` on name, email, username and password fields |
| Colour is never the only signal | 1.4.1 | Status chips, notices and callouts always have a word and an icon or shape; links can be underlined | Never ask people to find something by its colour |
| Text contrast of 4.5:1 | 1.4.3 | `tools/contrast.py` checks every text pair in all four themes | Use the colour tokens, never a raw colour |
| Text resized to 200% | 1.4.4 | Text sizes are in rem; Text size goes to 175%, and browser zoom past that | Never fix a height that text has to fit in |
| No images of text | 1.4.5 | Logos are SVG; wordmarks are text | Never put words in a picture |
| Reflow to one column at 400% zoom, 320px wide | 1.4.10 | Every component reflows; tables stack into cards on phones | Check each page at 320px with no sideways scrolling |
| Contrast of 3:1 for controls and focus | 1.4.11 | Control borders and the focus ring are checked by `tools/contrast.py` | Use the library's controls |
| Wider text spacing | 1.4.12 | The Wider text spacing setting; nothing clips when it is active | Leave room for text to grow |
| Hover and focus content that can be dismissed | 1.4.13 | Help is a disclosure button, not a hover tooltip; menus close with Escape | No content that appears only on hover |
| Important messages announced | 1.3.1, 4.1.3 | Toasts and saved notes use `role="status"` or `role="alert"` | Announce changes that happen without a page load |

## 3. Operable

| What is needed | Criterion | The library | The app |
|---|---|---|---|
| Everything works with a keyboard | 2.1.1, 2.1.2 | Menus, slide-outs, dialogs, the phone menu and filter chips all work by keyboard and never trap it | Use the library's components; test every page with Tab alone |
| Shortcut keys can be changed or switched off | 2.1.4 | The library sets no single-key shortcuts | Add none, or let people deactivate them |
| Time limits can be extended | 2.2.1 | Toasts wait while the pointer or focus is on them; errors stay until closed | Anything a toast offers, such as Undo, can also be done on the page |
| Moving content can be paused | 2.2.2 | Reduce motion stops animation; the loading bar stops when idle | Give anything that moves for over 5 seconds a pause control |
| Nothing flashes | 2.3.1 | Nothing in the library flashes | Never show flashing content |
| A way to skip to the content | 2.4.1 | `.skip-link`, the first thing on every page | Put the skip link first |
| Pages and frames have titles | 2.4.2 | The gallery and boards name every page and frame | "Activity · Storyarr": the page, then the app |
| A logical focus order | 2.4.3 | Slide-outs and dialogs move focus in and return it to the opener | Keep the order the page reads in |
| Links that say where they go | 2.4.4 | Link and button patterns in `CONTENT-DESIGN.md` section 4 | Name the destination and any file type |
| Meaningful headings and labels | 2.4.6 | Every field has a visible label | Follow `CONTENT-DESIGN.md` |
| Visible focus | 2.4.7 | A 3px focus ring at 3:1 contrast, in every theme | Never remove the focus ring |
| Focus never hidden by sticky parts | 2.4.11 (new in 2.2) | The page keeps the sticky header and save bar clear when it scrolls (`scroll-padding`) | Use `.site-header` and `.save-bar`, not sticky parts of your own |
| The name matches the visible label | 2.5.3 | Buttons are named by their words; hidden text only adds to the end | Start any `aria-label` with the visible words |
| Dragging has an alternative | 2.5.7 (new in 2.2) | The library has no drag-only control; the logo editor's crop is set with sliders | Give every drag a way to do the same with buttons or the keyboard |
| Targets at least 24 by 24 pixels | 2.5.8 (new in 2.2) | Controls are 44px; 32px only for dense table rows | Never make a control smaller than the library's |

## 4. Understandable

| What is needed | Criterion | The library | The app |
|---|---|---|---|
| The page's language is set | 3.1.1 | Every page is `lang="en-GB"` | Set `lang` on `html` |
| A change of language is marked | 3.1.2 | Nothing: the library has no foreign text | Mark a book title or name in another language with `lang`, such as `lang="fr"` |
| Navigation in the same place every time | 3.2.3 | One header, one main menu and one phone menu in both apps | Use the shell, never a page-specific menu |
| Help in the same place every time | 3.2.6 (new in 2.2) | Help is in the footer of every page, in an app with a help centre | Keep Help in the footer |
| Errors identified and explained | 3.3.1, 3.3.3 | `.field-error` beside the field, tied to it by `aria-describedby` | Say what is wrong and how to fix it (`CONTENT-DESIGN.md`, Error) |
| Labels and instructions | 3.3.2 | `.field__label` and `.hint` on every field | Put instructions before the field, not in the placeholder |
| No entering the same thing twice | 3.3.7 (new in 2.2) | Nothing in the library asks twice | Fill in what someone already gave, or let them choose it, in a wizard or a second form |
| Signing in without memory tests | 3.3.8 (new in 2.2) | Password fields take `autocomplete="current-password"` and `"new-password"` | Allow pasting and password managers; no puzzles or CAPTCHAs |

## 5. Robust

| What is needed | Criterion | The library | The app |
|---|---|---|---|
| Each control says what it is, its state and changes | 4.1.2 | Menus, switches, filter chips, tabs and dialogs use the right roles and states (`aria-expanded`, `aria-pressed`, `aria-current`) | Use the library's markup from the gallery, not your own |
| Status messages reach assistive technology | 4.1.3 | Toasts, saved notes and live regions | Announce results, progress and finished downloads |

WCAG 2.2 removed 4.1.1 Parsing, so valid HTML is good practice rather than a criterion.

## 6. How to check

- The checks before a change is finished: `ACCESSIBILITY.md` section 2.
- How to test with a keyboard, zoom, themes and a screen reader: `ACCESSIBILITY.md` section 6.
- Automatic checks, screen readers, magnifiers and voice control:
  [Outside tools for accessibility and testing](https://themightytrex.github.io/design-system/resources/outside-tools.html).
- Testing with people: [Get feedback](https://themightytrex.github.io/design-system/resources/get-feedback.html).

Automatic checks find only some problems. Test with a keyboard and a screen reader, and with people who use
assistive technology.

## Sources

- GOV.UK Service Manual,
  [Understanding WCAG 2.2](https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag),
  last updated 29 October 2024. Contains public sector information licensed under the
  [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
- W3C, [How to meet WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/): the full text of every criterion.
