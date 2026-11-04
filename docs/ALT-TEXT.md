# Writing text descriptions (alt text)

Version 1.0, 4 November 2026. How to describe images in Storyarr, Starboard, their help and this design
system, following the principles in the BBC's
[How to write text descriptions (alt text)](https://www.bbc.co.uk/gel/how-to-write-text-descriptions-alt-text).
Every word follows `CONTENT-DESIGN.md`. The examples are made up, as `CONTENT-DESIGN.md` rule 2.23 asks.

## About this guide

### What it is for

A text description, also called alt text, says in words what an image shows or does. Screen readers read it
aloud and braille displays show it. It also appears when an image does not load, lets voice control users
name an image link, and helps search engines. For many people it is not an alternative: it is the image.

WCAG 2.2 success criterion 1.1.1 requires a text alternative for every image (`WCAG.md` section 2).

### Who it is for

Anyone who adds an image to a page, a board, a help topic, a release note or a README, and anyone who
reviews one.

### How to use it

1. Decide what kind of image it is (section 2).
2. Write the description for that kind (sections 3 to 7), and for people (section 8).
3. Go through the checklist in section 9.

## 1. Principles

- **Context decides.** There is no right length or set of words. The same image needs a different
  description on different pages, so never copy a description from another page without rereading it.
- **Say what matters here.** Ask why the image is on this page and what it tells the reader, then say that.
- **Imagine telling someone on the phone.** Describe the image, in plain words, to someone who does not have
  it in front of them.
- **Short, then the page.** Aim for about 150 characters. If an image needs more, put the detail in the
  page's own text, a list or a table, and keep the description short. Some screen readers read a
  description in one go, with no way to go back.
- **No "image of".** Screen readers already say it is an image. Name the style when it matters:
  "Screenshot of…", "Illustration of…", "Diagram of…".
- **Nothing the page already says.** If the text beside the image gives the facts, the description can be
  shorter.
- **Never leave it out.** An image with no `alt` makes a screen reader read the file name. An image that adds
  nothing gets an empty description, `alt=""`, so it is skipped.

## 2. The five kinds of image

| Kind | What it is | What its description does |
|---|---|---|
| Decorative | Adds nothing to the meaning: a border, a background pattern, an icon beside its own words | Empty: `alt=""`, or `aria-hidden="true"` on an SVG |
| Informative | Shows something the reader needs, or sets the scene | Says what it shows, in this page's context |
| Functional | Part of a link or button | Says what happens, not what it looks like |
| Image of text | Words in a picture: a screenshot, a sign, a banner | Gives the words that matter |
| Chart or diagram | A chart, diagram, map or infographic | Gives the main point; the full data is on the page |

## 3. Decorative images

- An icon beside its own label is decorative: the library's icons carry `aria-hidden="true"` for this reason.
- An app's logo beside its own name, as in the header, is decorative.
- A cover inside a link that already names the book is decorative, so the book's title is read once.

## 4. Informative images

- A book cover on its own: "Cover of The Glass Harbour".
- An author's photo on their page: "Mara Ellison, smiling, in a library". Describe only what the reader
  would miss; never "Photo of Mara Ellison".
- A screenshot in help names the page and what it points to: "The Apps page, with Add an app outlined"
  (`HELP-WRITING.md` section 8). Everything the screenshot shows is also said in the steps.

## 5. Functional images

- Say the action, not the shape: "Play", not "Triangle"; "Close summary", not "Cross".
- An icon-only button is named in `aria-label`, starting with any words it shows (`WCAG.md`, 2.5.3).
- A logo that links home is named by where it goes: "Storyarr, My library".
- A linked image with text in the same link needs no description of its own: `alt=""`.

## 6. Images of text

- Avoid them: put words in the page as text (WCAG 1.4.5). Logos are the exception.
- A logo is described by its name: "Storyarr". A wordmark that is real text needs nothing more.
- A screenshot of a message or a page gives the words that matter: "Screenshot of the sign-in page, with the
  message 'The password does not match. Try again.'"
- Text that happens to be in a photo, such as a street sign, is left out unless it matters to the page.

## 7. Charts and diagrams

- The description gives the main point, and the full data is on the page as text, a list or a table.
- Charts in the library always have a table view in a disclosure (`LIBRARY.md`, Line chart), so the
  description can be short: "Line chart of disk use over 30 days: Disk 3 rises from 70% to 92%; the others
  stay level. The table follows."
- A meter or progress bar carries its value in words: "76% used".
- A flowchart in help lists the same steps in words (`HELP-WRITING.md`, guide layout).
- Whoever makes a chart or diagram also writes its suggested description, and sends both together.

## 8. Describing people

- Describe what can be seen and matters to the page: what someone is doing, their expression, what they
  are holding, the setting.
- Never assume age, gender, ethnicity, religion, disability or how people are related. Two people at a table
  are "two people at a table", not "a couple".
- Mention ethnicity, a religious or cultural sign, or a disability only when it matters to the page, and
  never one that cannot be seen in the image.
- Use the person's name when the page gives it.

## 9. Captions and text descriptions

They do different jobs, so never copy one into the other.

- A caption, shown to everyone, repeats or points to something the page already says: "Disk 3 reached 92%
  on 3 November".
- A text description gives what the image shows, for someone who uses a screen reader or a braille display.

## 10. Checklist before an image is finished

- [ ] The image has an `alt` attribute, empty when it is decorative
- [ ] The description says what matters on this page, not everything in the image
- [ ] About 150 characters or fewer; longer detail is in the page as text, a list or a table
- [ ] No "image of" or "picture of"; the style is named when it matters
- [ ] A link or button says what happens
- [ ] Words in the image that matter are in the description
- [ ] A chart's main point is in the description and its data is on the page
- [ ] No assumptions about people: only what can be seen and matters
- [ ] The caption, if any, is not a copy of the description
- [ ] Read aloud with a screen reader, it makes sense in the page's order

Ask someone who uses a screen reader whether a description gives them enough, and remember that one
person's view is one view.

## Sources

- BBC GEL, [How to write text descriptions (alt text)](https://www.bbc.co.uk/gel/how-to-write-text-descriptions-alt-text),
  May 2024: the principles in sections 1, 2, 8 and 9 come from it, written here in our own words.
- W3C, [An alt decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/).
