# Storyarr content design guide

Version 1.0, 1 November 2026. How every word in Storyarr is written: page titles, menus, buttons, settings,
messages, release notes, guides and the README. It applies to new text and to anything you touch.

**For AI agents:** treat every rule marked **Rule** as a check that must pass before a change is finished.
Section 9 is the checklist. When a rule and an on-screen label disagree, copy the label exactly (rule 2.11).

---

## 1. Voice and tone

Storyarr is a calm, capable librarian. It tells you what is happening with your books, what it is doing
about it, and what you can do next.

| Always | Never |
|---|---|
| Plain and direct: the answer first | Clever, jokey or chatty |
| Calm: nothing is urgent unless it is | Alarming, shouty or pushy |
| Helpful: every problem comes with a next step | Blaming the person ("you entered the wrong…") |
| Honest: say when Storyarr is unsure or something failed | Vague ("something went wrong") |

Assume the reader arrived mid-task and wants to get back to their books. Give exactly what is needed.

## 2. Rules

2.1 **Rule: no em dashes.** Use a comma, a colon or a new sentence. A spaced en dash only for a range
("1 – 5 books" is still better as "1 to 5 books").

2.2 **Rule: no contractions.** "cannot", "do not", "it is", "you will". Never "can't", "won't", "it's".

2.3 **Rule: British English.** organise, colour, catalogue, licence (noun), license (verb), centre,
favourite, behaviour, travelled.

2.4 **Rule: sentence case everywhere,** including menus, tabs, chips, buttons, headings and page titles:
"My library", "Add missing books", "Download unconfirmed releases". Product and service names keep their
capitals: Storyarr, Audiobookshelf, Hardcover, Prowlarr, qBittorrent, SABnzbd, MyAnonamouse, Audible.

2.5 **Rule: "select", not "click" or "tap".** "Select Save." For navigation: "Go to Settings, then Sources."

2.6 **Rule: no "see" or "look".** "The results appear below the search" not "see the results". "Find" not
"look for".

2.7 **Rule: no positional directions.** Never "top right", "the menu on the left", "scroll down". Name the
control: "Select Display in the header." Positions change between Classic and Shelf layouts, phone and
desktop, and they mean nothing to a screen reader user.

2.8 **Rule: "page", not "screen".**

2.9 **Rule: switches are "on" and "off".** Settings in Storyarr are switches, so write "Turn on Upgrade
automatically", and state the result: "On: Storyarr backs up your settings and keeps the defaults."
Avoid "enable", "disable" and "toggle".

2.10 **Rule: no exclamation marks and no emoji.**

2.11 **Rule: on-screen labels beat every rule.** When text refers to a control, copy its label exactly and
put it in bold inside steps: "Select **Add missing books**." If a label breaks a rule, fix the label in the
app rather than misquoting it in the guide.

2.12 **Rule: sentences under 25 words, paragraphs of two to four sentences.** Active voice, present tense.
Address the reader as "you". Storyarr refers to itself by name ("Storyarr searches again in 6 hours"),
not "we", except in error messages where the system is at fault ("We could not reach Hardcover").

2.13 **Rule: lead with the answer.** The first sentence says what this is or what happened.

2.14 **Rule: expand an abbreviation the first time on each page:** "NZB (Usenet download file)".
Common ones need no expansion: ebook, URL, API.

## 3. Punctuation, numbers and dates

- No full stop on headings, buttons, menu items, tabs, chips, tooltips or single-line bullets.
- Bold only for on-screen labels inside steps. No italics. Underline only for links.
- Oxford comma in lists of three or more. Avoid semicolons: split the sentence.
- Ellipsis only for something in progress: "Searching…".
- Ampersand only where space is tight (a chip or a tab), never in sentences.
- Numbers: one to nine in sentences, numerals for 10 and above. Always numerals in counts, steps,
  percentages, sizes and times: "3 books", "Step 2", "45%", "1.2 GB", "6 hours".
- Dates: 1 November 2026, or 1 Nov in tight spaces. Never 01/11/26.
- Times: 24-hour clock in the app, because times sit next to schedules: "Next search 16:31". In prose, write
  "at 4.30pm" only if the app never shows the same time.
- Thousands with a comma: 10,000.

## 4. Links and buttons

- Link text names the destination: "Open the Docker guide". Never "click here", "here", "read more" or a
  bare URL.
- A link that leaves Storyarr says so: "Hardcover (opens in a new tab)".
- Buttons start with a verb and name the thing: "Search now", "Add missing books", "Delete book",
  "Save changes". Not "OK", "Submit" or "Yes".
- A pair of buttons: the main action first, then "Cancel". A destructive action says what it destroys:
  "Delete permanently", not "Confirm".

## 5. Words Storyarr uses

One word per thing, everywhere. If a page needs a new term, add it here first.

| Use | Not | Meaning |
|---|---|---|
| book | title, work, item | One book, whatever its formats |
| audiobook, ebook | audio book, e-book, eBook | The two formats. "Format" is the general word |
| edition | version | A specific publication of a book (narrator, length, publisher) |
| My library | Library (for the page), collection | The books you have |
| follow, Following | watch, monitor, track | Keeping up with an author or series automatically |
| series | saga, collection | A numbered run of books. Write "Book 3", not "#3" |
| author | writer | |
| narrator | reader, voice | |
| request | order, grab | Asking Storyarr to get a book |
| release | torrent, NZB, result | One downloadable file set found by a source |
| source | indexer, provider, tracker | Where Storyarr searches (Prowlarr, MyAnonamouse, AudioBook Bay, archive.org) |
| download client | downloader | qBittorrent, SABnzbd |
| import | copy, move (as nouns) | Bringing a finished download into the library |
| Activity | Queue (for the page) | Requests, downloads and review together |
| Discover | Browse (for the page) | Finding new books |
| Exclude, Excluded | ignore, hide, skip | A book a follow should not get |
| Delete | remove (for files) | "Remove" is fine for taking something off a list |

## 6. Status vocabulary

These are the only statuses. Every page, cover, row, chip, drawer and notification uses the same word, colour
and icon. Do not invent synonyms ("Owned", "Available", "Done").

| Status | Meaning | Tone | Extra detail allowed |
|---|---|---|---|
| In library | The book is in your library | Success | Format: "In library · Audiobook" |
| Downloading | A download client is fetching it | Info | Percentage: "Downloading 45%" |
| Importing | The download finished and is being copied in | Info | |
| Searching | A search is running now | Info | |
| Waiting | No release yet; Storyarr searches again later | Neutral | Next search: "Waiting · 16:31" |
| Not released | Publication date is in the future | Neutral | Date: "Not released · 3 Mar 2027" |
| Needs attention | Storyarr is stuck and needs a decision | Warning | Short reason in the drawer, not the chip |
| Wanted | Requested, nothing found or chosen yet | Neutral | |
| Excluded | A follow will not get this book | Muted | Reason: "Excluded · Play" |
| Not requested | Known, but nobody asked for it | Muted | |

A status chip is one or two words plus its detail. Never a sentence. Never rely on colour alone: every
chip has its text, and its icon where one exists.

**Request outcomes** (Activity history only, never on a book): Pending (waiting for approval, Neutral),
Declined (Muted), Withdrawn (Muted), Failed (Danger).

**Files, not books:** a library file that has gone from the disk is "File missing", never "Missing", so it is
not confused with a book that is Wanted.

## 7. Patterns

Use the pattern, then adapt the words. Do not invent a new shape.

**Page title and heading.** One main heading (h1) per page, matching the menu item and the browser tab:
"Activity", tab "Activity · Storyarr". Headings go h1, h2, h3 in order without skipping.

**Empty state.** Heading names what will appear, one sentence says how it gets there, one button starts it.
- Heading: "No followed authors yet"
- Body: "Follow an author and Storyarr gets each new book as it comes out."
- Button: "Find an author"
Never "No data", "Nothing here" or "This page is empty".

**Loading.** Name what is happening: "Loading your library…". Every spinner or bar has a text label for
screen readers. A percentage only when it is real.

**Error.** What happened, why if it helps, what to do. Never an error code alone, never blame.
- "We could not reach Prowlarr. Check that it is running, then select **Try again**."
- Details (codes, responses) go in an expandable "Technical details" section.

**Confirmation (toast).** Past tense, specific, short: "Follow saved", "3 books added to Wanted".
One optional next step: "Undo" or "Open Activity". No celebration for routine actions.

**Destructive dialog.** Title asks the question with the object: "Delete The Hollow Boy?". The body says what
is removed, what is kept and how to get it back. The button names the action: "Delete book". Type-to-confirm
(DELETE) only for permanent deletion.

**Setting.** Label in sentence case, then one line saying what changes: "Upgrade automatically. Storyarr
backs up your settings and keeps the defaults for anything new." Defaults are stated when they matter.

**Help text and tooltips.** One sentence. Not a duplicate of the label.

**Release notes and upgrade wizard.** Group as Added, Changed and Fixed. Each item starts with the feature
name in bold, then what the person can now do. Write for the person using Storyarr, not the developer.
Database changes and the way back go in their own section.

## 8. Accessibility in content

The full checklist is in `ACCESSIBILITY.md`. The content half:

- Every control has a visible text name written as an action. Icon-only buttons have an `aria-label` with
  that name ("Close summary").
- Alt text says what the image shows: "Cover of The Hollow Boy". Decorative images use `alt=""`.
- No instruction depends on colour, shape, icon or position alone.
- Status changes that happen without a page load (a download finishing, a search result) are announced in a
  live region, using the status vocabulary.
- Never put text inside an image.

## 9. Checklist before a change is finished

- [ ] No em dashes, contractions, exclamation marks or emoji
- [ ] British spelling, sentence case, product names capitalised correctly
- [ ] "Select", "Go to", "page"; no "click", "see", "look", "enable", "disable", "screen"
- [ ] No positional directions
- [ ] Words match section 5; statuses match section 6 exactly
- [ ] One h1, headings in order, browser tab title matches
- [ ] Buttons start with a verb and name the object
- [ ] Empty, loading and error states follow section 7
- [ ] Sentences under 25 words; the answer comes first
- [ ] Icon-only controls have labels; alt text written

The repository check `python3 scripts/storyarr_rename.py` only covers the product name. The rest of this
list is checked by reading, until a content linter is added (task CD-02 in `TASKS.md`).
