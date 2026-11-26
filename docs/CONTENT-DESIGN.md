# Content design guide

Version 1.6, 26 November 2026. How every word in Starboard, its plug-ins and Stallboard is written: page titles, menus,
buttons, settings, messages, release notes, help and the README. It applies to new text and to anything you
touch. Help articles also follow `HELP-WRITING.md`; changelogs also follow `CHANGELOGS.md`.

## About this guide

### What it is

This is a content design system, not only a style guide. A style guide is a set of rules written by writers,
for writers. A content design system adds ready-made patterns for the moments that come up again and again:
an empty page, an error, a confirmation, a setting. With a pattern to start from, anyone can make a sound
decision about words without starting from a blank page.

It sits beside the component library in this repository, so words are designed with the components rather
than added at the end. It has four layers:

| Layer | What it covers | Where |
|---|---|---|
| Voice | How every app sound | Section 1 |
| Rules | Plain English, word choices, punctuation, links and statuses | Sections 2 to 6 |
| Patterns | Ready-made words for common moments | Section 7 |
| Checks | Accessibility in content, and the checklist | Sections 8 and 9 |

### Who it is for

Anyone who puts words in front of the people who use Starboard or Stallboard: developers writing a button or
an error, designers making a board, people writing help or release notes, and AI assistants doing any of
these. It is public, so you may also use it in your own projects under the guide licence (CC BY 4.0).

### How to use it

1. Read section 1 once, so you know how the apps sound.
2. Before you write something new, find its pattern in section 7 and start from that.
3. Keep sections 2 and 5 open while you write: the rules, and the words each app uses.
4. Before you finish, go through the checklist in section 9.

The gallery, the tools and the other guides are listed in
[Design resources and tools](https://themightytrex.github.io/design-system/resources/).

### Propose a change

Open an issue or a pull request on the
[design system repository](https://github.com/TheMightyTRex/design-system). Name the section and the rule
you want to add, change or remove, and give the words before and after. The guide is reviewed after any
release that changes words in either app. How to make and test a change is in
[Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html).

---

**For AI agents:** treat every rule marked **Rule** as a check that must pass before a change is finished.
Section 9 is the checklist. When a rule and an on-screen label disagree, copy the label exactly (rule 2.11).
To get an AI assistant to write instructions, and to check what it writes, follow `HELP-WRITING.md` section 9.

---

## 1. Voice and tone

Every app is calm and capable. Starboard cares for the server like a good caretaker: it tells you what is
running, what needs attention, what it is doing about it, and what you can do next.

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
"Manage apps", "Add missing books", "Install apps". Product and service names keep their capitals:
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
State the result: "Active: Starboard backs up your settings and keeps the defaults."

2.10 **Rule: no exclamation marks and no emoji.**

2.11 **Rule: on-screen labels beat every rule.** When text refers to a control, copy its label exactly and
put it in bold inside steps: "Select **Add missing books**." Outside a step, put the label in single
quotation marks: "the 'Upgrade automatically' setting". Double quotation marks are for words people say or
type. If a label breaks a rule, fix the label in the app rather than misquoting it.

2.12 **Rule: short sentences, one idea each.** The average sentence is 15 to 20 words, and no sentence is
longer than 25. Paragraphs have two to four sentences. Use the active voice and the present tense, and name who
does the action: "Starboard keeps the file", not "The file is kept". Address the reader as "you". The
organisation behind the app may say "we" ("We could not reach Hardcover", "We update the list each week"), and
the app may also name itself ("Starboard searches again in 6 hours"). Use one of the two in a given text, not
both. A passive is allowed when the doer is unknown or does not matter. Aim for about 80 to 90% active. The
standard is the Plain English Campaign (plainenglish.co.uk); this guide applies it and never copies its text.

2.13 **Rule: lead with the answer.** The first sentence says what this is or what happened.

2.14 **Rule: avoid jargon, and explain a technical word the first time on each page.** Prefer the everyday
word. When a technical word is the right one, add a short plain meaning: "NZB (Usenet download file)",
"a daemon (a program that runs in the background)". Common ones need no explanation: ebook, URL, API. In
release notes, explain it in every item, because each item is read alone.

2.15 **Rule: never say how difficult something is,** in either direction. Not simple, simply, easy, just,
straightforward, obviously, complex, hard, difficult or advanced. Give the fact the word stood in for: a step
count, a time, or what you need first. "This takes 3 steps", not "This is easy". Cut other filler words too:
actually, basically, really, quite, very, absolutely, "in order to" (write "to"), "note that", "at this
moment in time" (write "now") and "in the end". Prefer the plainer word: "use", not "utilise"; "start", not
"commence"; "about", not "approximately"; "help", not "assist"; "buy", not "purchase". Where a word is also a
label or a term in section 5 (select, enter, delete, request), the label wins.

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
feature that is not built yet. Name a limitation as a fact: "Starboard does not import ebooks from Calibre."

2.22 **Rule: no promises about timing.** Do not say when something will arrive, and do not mention plans.

2.23 **Rule: made-up example data, and only that.** Never "Test user", "John Doe", "Lorem ipsum" or real
data. Use the same made-up people everywhere (Alex, Sam, Priya, Jordan). Emails end `@example.com`; phone
numbers are `07700 900` then three digits; domains end `.example`. In mock-ups, the gallery and screenshots,
network addresses use the documentation ranges `192.0.2.x`, `198.51.100.x` and `203.0.113.x`. Help that
teaches home network addresses may show a made-up `192.168.1.x` address, because that is what the reader
will find on their own network.

2.24 **Rule: nest related points.** When bullets explain one point, nest them under it. The parent states
the fact; the children say why, how long and what to do.

2.25 **Rule: use the verb, not a hidden verb.** "Select", not "make a selection"; "install", not "carry out an
installation"; "when you finish", not "on completion of"; "remove", not "the removal of". A verb turned into a
noun adds words and hides who does what.

2.26 **Rule: reading level.** Aim for a Flesch-Kincaid grade of 6 or lower for text people read in the app,
the help and the README. Developer pages and changelogs may reach grade 8. The grade is a guide that cannot
detect jargon, so read the text as well as measuring it.

2.27 **Rule: word targets are warnings.** `tools/verbose-check.py` compares a page with a target length for its
kind. A page over its target gets a warning, never a failure, because the answer may be to move content, not to
cut it. A long sentence, or a paragraph of more than four sentences, is the only measure that can fail a
check, and only on a line a change adds. That part is not switched on yet.

## 3. Punctuation, numbers and dates

- No full stop on headings, buttons, menu items, tabs, chips, tooltips or single-line bullets.
- Bold only for on-screen labels inside steps. No italics. Underline only for links.
- Oxford comma in lists of three or more. Avoid semicolons: split the sentence.
- Ellipsis only for something in progress: "Searching…".
- Ampersand only where space is tight (a chip or a tab), never in sentences.
- Numbers: one to nine in sentences, numerals for 10 or more. Always numerals in counts, steps,
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

### Starboard

| Use | Not | Meaning |
|---|---|---|
| app | container, service (for an app with a page) | Something Starboard installs, opens and watches: Jellyfin, Sonarr, Reelix |
| background service | daemon, container | A service with no page of its own |
| server | box, machine, host | The computer Starboard runs on |
| disk | drive, HDD, volume | One physical disk. "Storage" is all of them together |
| backup | snapshot, archive | A saved copy of settings or of the server |
| alert | notification, warning (as a noun) | A message Starboard sends when something needs attention |
| update | upgrade (as a noun) | A newer version of an app or of Starboard |
| plug-in | add-on, extension, module | Something added to Starboard that has its own settings, cards or pages |
| media server | player, streamer | Jellyfin, Plex or Emby: the app that plays your library |
| place (for backups) | target, destination, remote | A disk, a network share or a cloud service where backups go |
| Check now | Refresh, Check again, Re-scan | The one name for asking an app, a disk or a service again. Same label before and after a first check |
| library | collection (for the whole), catalogue | The films, shows, music, books and audiobooks you have |
| wanted | missing, monitored | Something you asked for that is not here yet |
| request | order, ticket | Something a person asked to have added |

## 6. Status vocabulary (Starboard)

One word and one tone for each state, in every page, chip, row, card and alert. The words come from one map in `common.js` (`STATUS`), plus the words a screen needs for its own kind of state, all listed here. Do not invent a synonym ("Online", "OK", "Offline", "Done" for Installed). A status chip is one to three words. Never a sentence. Never colour alone: every chip has its word and an icon, and the icon differs by tone (a tick, an information mark, a warning triangle, a cross, a dash, a clock).

Tones: **success** (all is well), **info** (something is happening or is on offer), **warning** (needs checking, nothing is broken), **danger** (broken or at risk), **muted** (off, not used, no state to report), **neutral** (waiting, no judgement).

### Apps and services

| Word | Tone | Means |
|---|---|---|
| Running | Success | The app answers |
| Healthy | Success | The app and what it needs are fine |
| Not responding | Danger | The app does not answer; the slide-out says since when |
| Needs attention | Warning | Starboard found a problem the person can fix |
| Not working | Danger | The app is up but cannot do its job |
| Not checked | Muted | Starboard has not asked yet |
| Not read yet | Warning | A reading that has not come back |
| Active / Inactive | Success / Muted | A setting or a switch is on or off (never "Enabled") |
| Stopped | Warning | The app was stopped on purpose |
| Paused | Muted | Paused by a person; it resumes when they say |
| Restart needed | Warning | A change needs the app to restart |
| No container found | Muted | The app is listed but nothing runs for it |
| Cannot start | Danger | Starboard tried and the app would not start |
| Cannot check | Muted | The check cannot run here |
| Check skipped | Warning | The check was left out, with the reason beside it |
| Checking | Neutral | A check is running now |
| Checked | Success | A check finished and found nothing wrong |
| Check failed | Danger | The check itself broke |
| Error | Danger | Something failed; the words under it say what |

### Updates and backups

| Word | Tone | Means |
|---|---|---|
| Update available | Info | A newer version exists (a plug-in row says Update) |
| Up to date | Success | Nothing newer |
| Updated | Success | The update finished |
| Updating | Info | An update is running |
| Check before updating | Warning | Read the release notes first |
| Never updated | Warning | No update has ever run |
| Held back | Muted | A person held this version back (Held is the short form inside a table) |
| Went back | Warning | Starboard went back to the older version after a failure |
| Updates by itself | Muted | The app updates itself, so Starboard leaves it |
| Backing up | Info | A backup is running |
| Done | Success | The job finished |
| Failed | Danger | The job failed |
| Failed last time | Warning | The last run failed; the next may be fine |
| Not started | Warning | The job never started |
| In progress | Info | A long job is running |
| Sent | Success | A message or alert was sent |
| Not accepted | Warning | The service refused what Starboard sent |

### Downloads and the library

| Word | Tone | Means |
|---|---|---|
| Waiting | Neutral | Queued; with the time when it is known |
| Waiting to import | Neutral | Downloaded, not yet copied in |
| Downloading | Info | A client is fetching it |
| Downloaded | Success | The files are here |
| Importing | Info | Being copied into the library |
| In library | Success | It is in your library |
| Not in library | Muted | It is known but not in your library |
| Wanted | Neutral | Asked for; nothing found or chosen yet |
| Waiting for a match | Muted | Starboard is still trying to match a name |
| Matched / All matched | Success | A name was matched to the right item |
| In Starboard | Success | A thing Starboard also lists itself |
| Added already | Info | Already in the library, so it is not added again |
| Direct play | Success | A media server plays the file as it is |
| Converting | Warning | A media server has to convert it as it plays |
| Ends soon | Warning | Starts or ends within the hour |
| Not published | Muted | A plug-in's own page that is not shown |

### Library

The Library (films, TV, music, radio, books and audiobooks) uses these nine words and no others for what you have and what you want. They are the same on every tab, in every chip, filter, count, row and button (owner decisions, 26 November 2026). "Missing" is never used for a thing you want: "File missing" is only for a file gone from a disk.

| Word | Tone | Means | Replaces |
|---|---|---|---|
| In library | Success | The file is in your library | Have it, Has episodes, Complete |
| Partly in library | Info | A set (a series, a collection, an artist) with some of its parts | Episodes not in library, Tracks not in library (as a state) |
| Wanted | Neutral | Followed and released, not in your library yet. Reelix searches for it | Not in library, Missing, Episodes not in library, Tracks not in library |
| Downloading | Info | A download app has it now | no change |
| Below quality | Warning | In your library, but under the quality you chose. Reelix searches for a better one | The old label for this state |
| Not followed | Muted | Reelix has it and does not search for it | Not wanted, Not requested |
| Not added | Muted | A collection or series lists it, and Reelix does not have it | Not in your library (on a collection row) |
| Not released | Muted | The release date is in the future | no change |
| File missing | Danger | A file has gone from the disk | no change |

"In your library" and "Not in your library" stay as places, not states: they say where a Search result comes from. The action for a wanted thing is **Find** (Find it, Find wanted episodes, Find all wanted) (the Library patterns say how).

### Disks, network and plug-ins

| Word | Tone | Means |
|---|---|---|
| Mounted / Not mounted | Success / Muted (Danger when it is needed) | The disk is, or is not, attached |
| In use | Success | A disk or folder is used for something |
| Not used yet | Muted | Available and unused |
| Full | Danger | No room left |
| Nearly full | Warning | Over the warning level |
| Erases the disk | Danger | Tells the person before they choose it |
| Resting | Warning | A disk is spun down; Starboard does not wake it to read it |
| Windows file system: slower on Linux | Warning | A disk format that works but is slower |
| Connected / Not connected | Success / Muted | A link to another service |
| Reachable / Not reachable | Success / Danger | Starboard can or cannot reach an address |
| Reachable from outside / Not reachable from outside | Success / Warning | An address works from the internet |
| Checking from outside | Neutral | The outside check is running |
| Certificate runs out soon | Warning | The address's certificate needs renewing |
| Installed / Not added | Success / Muted | A plug-in or app is, or is not, on this server |
| Needs you / Waits for you | Warning | A step only the person can do |
| Suggested / Recommended | Info | Starboard offers it; it is not chosen |
| Built-in choice / Always here | Muted | Part of Starboard, so it cannot be removed |
| Read only | Neutral | Starboard can read but not change |
| Needs Reelix / Jellyfin only / Plex or Emby | Muted (Warning when it is not here) | A plug-in's requirement (a tag, not a state) |

**Rules.**
- One state, one word: where the table gives a short form, use it only inside a table cell or a card too small for the long one.
- A request outcome (Pending, Declined, Withdrawn, Failed) appears only in History. A library file that has gone from the disk is "File missing", never "Missing", so it is not mistaken for something Wanted.
- A word that is not in this table goes in it first, with its tone, in the same change.
- Never say "Online", "Offline", "OK", "Good" or "Bad". A status in a line of text, not a chip, still uses the same word.

## 7. Patterns

Use the pattern, then adapt the words. Do not invent a new layout.

**Page title and heading.** One main heading (h1) per page, matching the menu item and the browser tab:
"Updates", tab "Updates · Starboard". Headings go h1, h2, h3 in order without skipping.

**Empty state.** Heading names what will appear, one sentence says how it gets there, one button starts it.
- Heading: "No followed authors yet"
- Body: "Add an author and Starboard gets each new book as it comes out."
- Button: "Find an author"
Never "No data", "Nothing here" or "This page is empty".

**Loading.** Name what is happening: "Loading your library…". Every spinner or bar has a text label for
screen readers. A percentage only when it is real.

**Error.** What happened, why if it helps, what to do, then what is safe. Never an error code alone, never
blame.
- "We could not reach Prowlarr. Check that it is running, then select **Try again**. Your requests are
  kept."
- Details (codes, responses) go in an expandable "Technical details" section.
- Where the error shows: beside the thing it belongs to (a field, a row, a connection), as a danger notice
  at the top of the page, or, when nothing on the page belongs to it, as an error toast. An error toast
  stays until it is closed and can carry one action ("Try again"). Never pass a raw error message to a
  toast: write what happened and what to do, and put the raw message in "Technical details" or the log.

**Toasts.** Four kinds: success, information, warning and error. A warning says what may go wrong and
what to do: "Disk 3 is 92% full". An error follows the error pattern.

**Confirmation (toast).** Past tense, specific, short, no full stop: "Follow saved", "3 books added to
Wanted". An optional line of detail: "New books by Mara Ellison come in by themselves". One optional next
step: "Undo" or "Open Activity". No celebration for routine actions.

**Confirmation on a settings page (saved note).** No toast: the words appear beside the button that saved,
"Saved at 16:31", and stay until the next change.

**Find all wanted.** A button that asks a download app to search for everything wanted on a list, in four steps (owner, 26 November 2026). The same words on every Library tab, every Wanted page and every show or series.
- Count first, on the button: "Find all wanted (23)". With nothing wanted, the button is inactive and says "Nothing is wanted".
- Question: the title says how many ("Find 19 wanted episodes?"). The body says what happens in a sentence ("Reelix searches its sites for each wanted episode, a few at a time, and sends the best match it finds to your download app.") and three short lines: how many are wanted and how many were left out because they were searched in the last day; how fast ("Starboard asks for 10 at a time, with one minute between groups. This takes about 12 minutes."); and that you can stop at any time and leave the page. The main button repeats the number ("Find 19 wanted episodes"). Cancel is second.
- Progress: a panel under the page heading with words and a progress bar that has its own label ("Searched 8 of 19 wanted episodes. The next group starts in 40 seconds."), and **Stop**. The words change after each group, never more often, so a screen reader hears one update a minute. While Download hours pause downloads it says so and waits.
- Summary: a notice that stays until it is closed, not a toast ("Searched 19 wanted episodes. Reelix sends what it finds to your download app, and keeps searching while you follow them. 12 are still wanted."), with **Open Downloads**. A stopped run says "Stopped after 8 of 19" and how many were not searched. A failed run says what happened and "Nothing else changed".
- Limits, so a list cannot flood the sites: 10 searches in a group, one group a minute, at most 100 in a run (the question says how many wait for the next), nothing searched in the last 24 hours, one run at a time, 15 minutes between runs. A show, series or artist page uses the same verb for its own wanted items: "Find wanted episodes (7)".

**Destructive dialog.** Title asks the question with the object: "Delete The Glass Harbour?". The body says what
is removed, what is kept and how to get it back. The button names the action: "Delete book". Entering DELETE to confirm
is only for permanent deletion.

**Setting.** Label in sentence case, then one line saying what changes: "Upgrade automatically. Starboard
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

**Release notes and upgrade wizard.** Group as Added, Changed, Deprecated, Removed, Fixed and Security, in
that order, leaving out any type with nothing in it: the same types as the changelog (`CHANGELOGS.md`). Each
item:
- a bold headline that says what the person can now do, in sentence case, with no marketing words
  ("seamlessly", "easily", "enhanced");
- one or two sentences on what changed and who it helps;
- "Find out more in **<help topic>**" when a topic exists.
Write for the person using the app, not the developer. Never compare with before ("you used to…"): describe
the new state. Database changes and the way back go in their own section.

**Security in release notes.** Rule: every release with a security fix has a Security section, after Fixed,
that lists every security fix. Each fix is one bold title and one sentence, written so a person can judge it:
what could happen, to whom, and what happens now. No codes alone, no "various security improvements", and
nothing that helps someone attack an older version they cannot yet update: name the problem, not the exact
request.
- "**Sign-in.** The password is never put in the page address, even if Enter is pressed before the page has
  loaded."
- "**Saved keys.** A saved API key goes only to the server it was saved for, never to a new address or across
  a redirect."
The last item names the checks the release passed and where the results are: "**Checks.** This release passed
Trivy, OWASP ZAP, Gitleaks, Bandit, ShellCheck and Hadolint. The results are on the security page." The checks
themselves are in `SECURITY-CHECKS.md`.

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
- Alt text says what the image shows: "Cover of The Glass Harbour". Decorative images use `alt=""`. How to
  write every kind of text description is in `ALT-TEXT.md`.
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
- [ ] Average sentence 15 to 20 words and none over 25; active voice; no hidden verbs, filler or jargon; the answer comes first
- [ ] Icon-only controls have labels; alt text written; screenshots described in words
- [ ] Example data is made up and follows rule 2.23

`tools/check_words.py` checks the banned words. `tools/verbose-check.py` checks the sentence length, the
paragraph length, the passive voice, hidden verbs, filler, jargon, reading level and word targets, and warns only
(it fails on nothing yet). The rest of this list is checked by reading.
