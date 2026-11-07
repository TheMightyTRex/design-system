# Screenshots in help

How screenshots in help are chosen, taken, marked up and described, for every app that uses this design system.
The rules are written so a person or an AI tool can follow them without guessing. Section 9 is a short version to
give an AI tool with its task.

## About this guide

### What it is for

A screenshot is there to carry a step the reader could not follow from the words alone. These rules keep every
screenshot accurate, safe to publish and readable with a screen reader, and make the pictures in every app's help
look the same.

### Who it is for

Anyone adding or replacing a screenshot in an app's help, by hand or with an AI tool. It sits with
`HELP-WRITING.md` (section 8 points here), `ALT-TEXT.md` (text descriptions) and `CONTENT-DESIGN.md` (rules 2.20
and 2.23).

### How to use it

1. Write the steps first (`HELP-WRITING.md`).
2. Decide which steps need a picture (section 1).
3. Take it from made-up data (section 2), after the page has settled (section 3).
4. Mark it up (sections 4 and 5), check it (section 7), and describe it (section 6).

## 1. When a screenshot earns its place

- **An app may set a minimum, and Starboard's is 3 in every topic** (tier one, owner, 7 November 2026). Choose them
  with the test below: the steps a reader could least follow from the words, the page they start on, and what
  they see when it has worked. Beyond the minimum, test each picture: does it carry a step the reader could not
  otherwise follow? If not, leave the step as text.
- **Worth a picture:** a control with no words on it (a menu of three dots, an icon button), a dialog the reader
  has not seen before, a page where the control is hard to find.
- **Rarely worth a picture:** a menu that looks the same on every page, a second table repeating the one above it,
  a control the step already names in bold, "Select Save".
- **Split rather than crowd.** An article that needs ten pictures is two articles; split it where the task has a
  natural break, losing no step.
- When you finish, say which steps you left as text on purpose.

## 2. Data: only made-up data, never real data

- **Take screenshots from a test copy of the app with made-up data** (rule 2.23 in `CONTENT-DESIGN.md`): example
  names, `.example` addresses, `07700 900` numbers. Never from a real server, a real account or anyone's own
  library.
- **Where a page can only be reached with real data, mask it before capturing.** Replace names, addresses,
  numbers and messages with made-up values in the page itself, then add a visible note: "Example data". Repeat
  the note in the text description, so a screen-reader user is told too.
- **Check the mask both ways.** Nothing real is left, and no label of the app was replaced by mistake. Make the
  list of labels to keep from the app's own text files, not by typing it.
- **Blur is not a mask.** Blur hides pixels, not the words underneath, and can be undone. Replace the text.
- **Never fake a screenshot.** If a page cannot be reached (not released yet, needs data that does not exist,
  hidden behind a setting), keep the step as text, say which picture is missing, and add it once the page exists.
  A clearly labelled mock-up is allowed only when the article says it is one.
- **Never crop or hide part of a page and present the result as the whole page.**

## 3. Taking the screenshot

- **Light theme,** unless the article is about the dark theme. The same window size for every picture in one
  article. Text size at 100%.
- **Let the page settle first.** Wait at least 10 seconds after a page loads, and at least 8 seconds after a
  click, a filter change or a section opening. Look at a small preview before marking it up. Anything still
  loading, a menu still opening or a list still moving means wait again.
- **Open a menu or dialog before marking it up,** and take a settling picture first when an overlay has to be
  clicked open.
- **Look at the first picture of each kind of page yourself.** After that, check the rest from the page's own
  structure (section 7) instead of taking extra pictures to check them.
- **Name files by what they show, with the language:** `apps-add-an-app-en.png`, not `image1.png`.

## 4. Marking up: the outline and the arrow

- **Outline:** a box in red `#C71F1F`, 3 pixels thick, drawn 5 pixels outside the control, so the control and its
  label are never covered.
- **Arrow:** a curved tail ending in a solid, filled triangular head that touches the outline. Never a straight
  arrow, never an open arrow drawn with two lines.
- **At most three outlines in one picture.** A fourth step on the same page is a second picture.
- **A choice includes its words.** An outline round a radio button or tick box takes in the control, its label and
  the description under it, as one box. One box round the whole group of choices is better than one per choice.
- **Anchor every outline to the real control on the page**, found from the page's own structure (its text, its
  role or its CSS class), never placed by eye from a picture. After drawing, check the outline still wraps the
  control, the arrow head touches it, nothing is off the screen and nothing covers it. Never take the picture if
  that check fails.
- **Two things cannot be anchored:** anything drawn on a canvas and anything inside a frame from another site.
  Outline nothing inside them; outline the page around them only.
- Use `tools/annotate.js` in this repository: it draws the outline, arrow and number to this specification and
  runs the check.

## 5. Marking up: step numbers

- **Write the step list first, then decide which steps each picture shows.** A step whose control is on the
  screen is a step the picture shows. If the picture shows a step the list does not have (a section to open, a
  tab to choose), add the step to the list first.
- **Every step the picture shows gets an outline, and every outline gets a number badge carrying that step's
  number in the article.** Steps 2, 3 and 4 are badged 2, 3 and 4, never 1, 2 and 3 by reading order.
- **An outline that belongs to no numbered step gets no badge.**
- **A control at the left edge still gets its number:** the badge moves to the top-right corner, then a bottom
  corner, when the top-left would leave the screen.
- Before writing the article, read the steps against the picture: each badge points at the control its step
  names.

## 6. Text descriptions

- **Every screenshot has a text description,** in the article's language, that names the page and what is
  outlined, quoting labels exactly as the picture shows them: "The Apps page, with Add an app outlined (step 2)".
  Never "screenshot", "image1" or "the button in the bottom right". `ALT-TEXT.md` has the full rules.
- **Everything the picture shows is also said in the steps** (rule 2.20). The picture helps; it never carries
  information alone.
- A picture with example data says so in its description: "with example data".

## 7. Checking before it is published

- Each outline wraps its control, each arrow touches its outline, each badge carries its step's number.
- The picture shows the page as the step describes it, in the right language and theme.
- No real names, addresses, keys or messages are visible.
- The picture appears on the published page (it loads, at its full size) and has its text description.
- Files are named by what they show, with the language.

## 8. For each app

Each app keeps its own help screenshots next to its help (Starboard: `docs/help/images/`), made from its own
preview with made-up data. An app's help writing notes (Starboard: `docs/help/HOW-THIS-HELP-IS-WRITTEN.md`) point
here instead of repeating these rules.

## 9. The short version, for an AI tool

Give an AI tool this with its task. It is the whole of this guide in rules it can check.

```text
Screenshots for help. Follow every rule; say which you could not.
1. At least the app's minimum (Starboard: 3 per topic), then only for steps a reader could not follow from words.
   Report which steps you left as text.
2. Made-up data only, from a test copy of the app. Never a real server or account. If real data cannot be
   avoided, replace it in the page with made-up values, add the visible note "Example data", and check both
   that nothing real is left and that no app label was overwritten. Blur is not a mask.
3. Never fake a picture. If a page cannot be reached, keep the step as text and list the missing picture.
4. Light theme, same window size, 100% text. Wait 10 s after a load and 8 s after a click before marking up.
5. Outline: red #C71F1F, 3 px, 5 px outside the control. Curved arrow with a filled triangle head touching the
   outline. At most 3 outlines per picture. A choice's outline includes its label and description.
6. Anchor each outline to the real element from the page structure (text, role, class), never by eye.
   Check it wraps the control, nothing is off screen or covered; never capture on a failed check.
   Nothing on a canvas or inside another site's frame is outlined.
7. Every step the picture shows is outlined; every outline has a badge with that step's number in the
   article (not reading order). An outline for no step has no badge.
8. Text description in the article's language: the page, what is outlined and the step numbers, labels
   quoted exactly. Everything shown is also said in the steps.
9. Name files by content and language: <page>-<what>-<lang>.png. Check each published picture loads.
```
