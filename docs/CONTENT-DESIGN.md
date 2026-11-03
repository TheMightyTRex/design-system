# Content design guide

Version 1.1, 3 November 2026. How every word in Storyarr and Starboard is written: page titles, menus,
buttons, settings, messages, release notes, help and the README. It applies to new text and to anything you
touch. Help articles also follow `HELP-WRITING.md`.

**For AI agents:** treat every rule marked **Rule** as a check that must pass before a change is finished.
Section 9 is the checklist. When a rule and an on-screen label disagree, copy the label exactly (rule 2.11).
To get an AI assistant to write instructions, and to check what it writes, follow `HELP-WRITING.md` section 9.

---

## 1. Voice and tone

Both apps are calm and capable. Storyarr is a librarian: it tells you what is happening with your books,
what it is doing about it, and what you can do next. Starboard looks after the server in the same way: what
is running, what needs attention, and what to do about it.

| Always | Never |
|---|---|
| Plain and direct: the answer first | Clever, jokey or chatty |
| Calm: nothing is urgent unless it is | Alarming, shouty or pushy |
| Helpful: every problem comes with a next step | Blaming the person ("you entered the wrong…") |
| Honest: say when the app is unsure or something failed | Vague ("something went wrong") |

Assume the reader arrived mid-task and wants to get back to it. Give exactly what is needed.

## 2. Rules

2.1 **Rule: no em dashes.** Use a comma, a colon or a new sentence. A spaced en dash only for a range
("1 – 5 books" is still better as "1 to 5 books").

2.2 **Rule: no contractions.** "cannot", "do not", "it is", "you will". Never "can't", "won't", "it's".
This includes headings: "What is new", not "What's new".

2.3 **Rule: British English.** organise, colour, catalogue, licence (noun), license (verb), centre,
favourite, behaviour, travelled, enquiry, programme.

2.4 **Rule: sentence case everywhere,** including menus, tabs, chips, buttons, headings and page titles:
"My library", "Add missing books", "Install apps". Product and service names keep their capitals: Storyarr,
Starboard, Audiobookshelf, Jellyfin, Docker, Hardcover, Prowlarr, qBittorrent, SABnzbd, MyAnonamouse, Audible.

2.5 **Rule: "select", not "click" or "tap".** "Select Save." For navigation: "Go to Settings, then Sources."

2.6 **Rule: no "see" or "look".** Make the subject act: "A message appears", not "You will see a message".
"The results appear below the search", not "see the results". "to show today's downloads", not "to see".
"Find", not "look for". A cross-reference is "Read **Add an app**", with the link text naming the article.

2.7 **Rule: no positional directions.** Never "top right", "the menu on the left", "scroll down", "shown
above", "listed below" or "the table below". Name the control, the section or the item: "Select Display in
the header." Positions change between layouts, phone and desktop, and they mean nothing to a screen reader
user.

2.8 **Rule: "page", not "screen".**

2.9 **Rule: "activate" and "deactivate".** "Activate **Upgrade automatically**", "Deactivate alerts". A
setting's state is "active" or "inactive". Never "enable", "disable", "turn on", "turn off" or "toggle".
State the result: "Active: Storyarr backs up your settings and keeps the defaults."

2.10 **Rule: no exclamation marks and no emoji.**

2.11 **Rule: on-screen labels beat every rule.** When text refers to a control, copy its label exactly and
put it in bold inside steps: "Select **Add missing books**." Outside a step, put the label in single
quotation marks: "the 'Upgrade automatically' setting". Double quotation marks are for words people say or
type. If a label breaks a rule, fix the label in the app rather than misquoting it.

2.12 **Rule: sentences under 25 words, paragraphs of two to four sentences.** Active voice, present tense.
Address the reader as "you". The app refers to itself by name ("Storyarr searches again in 6 hours"), not
"we", except in error messages where the system is at fault ("We could not reach Hardcover").

2.13 **Rule: lead with the answer.** The first sentence says what this is or what happened.

2.14 **Rule: expand an abbreviation the first time on each page:** "NZB (Usenet download file)". Common ones
need no expansion: ebook, URL, API. In release notes, expand it in every item, because each item is read
alone.

2.15 **Rule: never say how difficult something is,** in either direction. Not simple, simply, easy, just,
straightforward, obviously, complex, hard, difficult or advanced. Give the fact the word stood in for: a step
count, a time, or what you need first. "This takes 3 steps", not "This is easy".

2.16 **Rule: the specific word, never a figure of speech.** No metaphors. Write "layout", "order",
"template" or "type", not "shape". One word per thing, and never the same word for two things (section 5).

2.17 **Rule: say it once, and positively.** No double negatives. Say what someone can do before what they
cannot. Never describe the reader by what they cannot do. Nothing said twice in one sentence.

2.18 **Rule: "enter" for typing.** "Enter your API key", not "type" or "input".

2.19 **Rule: the full path the first time.** Name the whole route on first use: "Go to **Settings**, then
**Apps**." After that, the last step alone is enough.

2.20 **Rule: describe what a picture shows.** Anything shown only in a screenshot is also said in words, for
screen readers and for search.

2.21 **Rule: never point at our own gaps.** No apology for a missing help topic, an old screenshot or a
feature that is not built yet. Name a limitation as a fact: "Storyarr does not import ebooks from Calibre."

2.22 **Rule: no promises about timing.** Do not say when something will arrive, and do not mention plans.

2.23 **Rule: made-up example data, and only that.** Never "Test user", "John Doe", "Lorem ipsum" or real
data. Use the same made-up people everywhere (Alex, Sam, Priya, Jordan). Emails end `@example.com`; phone
numbers are `07700 900` then three digits; domains end `.example`. In mock-ups, the gallery and screenshots,
network addresses use the documentation ranges `192.0.2.x`, `198.51.100.x` and `203.0.113.x`. Help that
teaches home network addresses may show a made-up `192.168.1.x` address, because that is what the reader
will find on their own network.

2.24 **Rule: nest related points.** When bullets explain one point, nest them under it. The parent states
the fact; the children say why, how long and what to do.

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
  "at 4.30pm" only if the app never shows the same time. Write "midday" and "midnight", never "noon" or
  "12am".
- Thousands with a comma: 10,000.

## 4. Links and buttons

- Link text names the destination: "Open the Docker guide". Never "click here", "here", "read more",
  "learn more" or a bare URL.
- A link that leaves the app says so: "Hardcover (opens in a new tab)".
- A link to a file names its type: "Download the backup (ZIP)".
- Buttons start with a verb and name the thing: "Search now", "Add missing books", "Delete book",
  "Save changes". Not "OK", "Submit" or "Yes".
- A pair of buttons: the main action first, then "Cancel". A destructive action says what it destroys:
  "Delete permanently", not "Confirm".

## 5. Words each app uses

One word per thing, everywhere. If a page needs a new term, add it here first.

### Storyarr

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

### Starboard

| Use | Not | Meaning |
|---|---|---|
| app | container, service (for an app with a page) | Something Starboard installs, opens and watches: Jellyfin, Sonarr, Storyarr |
| background service | daemon, container | A service with no page of its own |
| server | box, machine, host | The computer Starboard runs on |
| disk | drive, HDD, volume | One physical disk. "Storage" is all of them together |
| backup | snapshot, archive | A saved copy of settings or of the server |
| alert | notification, warning (as a noun) | A message Starboard sends when something needs attention |
| update | upgrade (as a noun) | A newer version of an app or of Starboard |

## 6. Status vocabulary (Storyarr)

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

Use the pattern, then adapt the words. Do not invent a new layout.

**Page title and heading.** One main heading (h1) per page, matching the menu item and the browser tab:
"Activity", tab "Activity · Storyarr". Headings go h1, h2, h3 in order without skipping.

**Empty state.** Heading names what will appear, one sentence says how it gets there, one button starts it.
- Heading: "No followed authors yet"
- Body: "Follow an author and Storyarr gets each new book as it comes out."
- Button: "Find an author"
Never "No data", "Nothing here" or "This page is empty".

**Loading.** Name what is happening: "Loading your library…". Every spinner or bar has a text label for
screen readers. A percentage only when it is real.

**Error.** What happened, why if it helps, what to do, then what is safe. Never an error code alone, never
blame.
- "We could not reach Prowlarr. Check that it is running, then select **Try again**. Your requests are
  kept."
- Details (codes, responses) go in an expandable "Technical details" section.

**Confirmation (toast).** Past tense, specific, short, no full stop: "Follow saved", "3 books added to
Wanted". An optional line of detail: "New books by Ben Aaronovitch come in by themselves". One optional next
step: "Undo" or "Open Activity". No celebration for routine actions.

**Confirmation on a settings page (saved note).** No toast: the words appear beside the button that saved,
"Saved at 16:31", and stay until the next change.

**Destructive dialog.** Title asks the question with the object: "Delete The Hollow Boy?". The body says what
is removed, what is kept and how to get it back. The button names the action: "Delete book". Type-to-confirm
(DELETE) only for permanent deletion.

**Setting.** Label in sentence case, then one line saying what changes: "Upgrade automatically. Storyarr
backs up your settings and keeps the defaults for anything new." Defaults are stated when they matter.

**Help text and tooltips.** One sentence. Not a duplicate of the label.

**Callout.** One colour means one thing, and the first word says it, so the meaning never rests on colour
(`.notice`, gallery: Callouts).

| Lead word | Tone | Use it for |
|---|---|---|
| Before you begin: | Info (blue) | What must be true or to hand first |
| Limitation: | Warning | Something that changes the outcome |
| Warning: | Danger | Something that cannot be undone |
| Tip: | Success | An optional better way |
| Example: | Muted | An aside the reader may skip |

No steps and no emoji inside a callout.

**Time ago.** "Updated 10 seconds ago" on screen, in a `<time>` element whose `datetime` holds the exact
time, with the exact date and time in words for screen readers.

**A change from a date.** A muted tag under the title: "From 1 December 2026". Only for a change that has an
agreed date and has not happened yet. Leave it off once the change is live.

**Release notes and upgrade wizard.** Group as Added, Changed and Fixed. Each item:
- a bold headline that says what the person can now do, in sentence case, with no marketing words
  ("seamlessly", "easily", "enhanced");
- one or two sentences on what changed and who it helps;
- "Find out more in **<help topic>**" when a topic exists.
Write for the person using the app, not the developer. Never compare with before ("you used to…"): describe
the new state. Database changes and the way back go in their own section.

**What is new (announcement).** For a release's headline feature, in the release notes slide-out or the
upgrade guide.
- A new feature: the benefit as the title (under nine words), one sentence on what it means for the reader,
  one picture of it working, "What is new" with three gains, "How to start" with up to three steps (what
  you need first is step 1), and one button: "Open the guide: <topic>".
- An improvement: the same without the steps. "What has changed" with three gains, one line saying where to
  find it, and "Nothing to set up" when that is true.

**Retiring something.** A removal is not news. Say what is going, the date, and what to do instead, with a
link to the steps. Show it as a warning notice in the app until the date passes.

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
- [ ] "Select", "Go to", "Enter", "page", "activate"; no "click", "see", "look", "enable", "disable",
      "turn on", "toggle", "screen"
- [ ] No positional directions, no "above" or "below"
- [ ] No difficulty words, no figures of speech, no double negatives
- [ ] Words match section 5; statuses match section 6 exactly
- [ ] One h1, headings in order, browser tab title matches
- [ ] Buttons start with a verb and name the object; links name the destination and the file type
- [ ] Empty, loading and error states follow section 7; errors say what is safe
- [ ] Sentences under 25 words; the answer comes first
- [ ] Icon-only controls have labels; alt text written; screenshots described in words
- [ ] Example data is made up and follows rule 2.23

The rest of this list is checked by reading, until a content linter is added (task CD-02 in `TASKS.md`).
