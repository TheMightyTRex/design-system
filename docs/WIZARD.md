# Wizard: the rules

4 November 2026. One set of rules for every wizard in every app that uses the library. That covers first-run set-up,
upgrades, restores, migrations and any other job done in steps. The classes are in `components.css` and the behaviour
is in `components.js`.

A live example is in the gallery, section Wizard. A wizard in a terminal follows `TERMINAL.md` as well.

A wizard is a page, not a dialog. People link to it, come back to it and spend time in it ("Slide-out, dialog or page"
in `LIBRARY.md`).

## 1. Shape

**Only what the app can show.** A wizard runs inside the app, so it starts once the app is installed and running.
Anything needed before that (Docker, a folder, running the installer) belongs on the help page and in the installer.
The installer checks it and stops with what to do.

Never ask in the wizard about something the wizard could not run without (4 November 2026). A mock-up that shows those
earlier steps marks them off as "Before the wizard", with their own count. The wizard's progress starts at its own
first step.


| Part | Where | Classes |
|---|---|---|
| Progress bar | Top of the wizard | `.wizard-progress` (a `.meter` with a `.progress` bar) |
| Step bar for a step in parts | Under the progress bar, only on a step in parts | `.steps.steps--sub` |
| The step | Under them | `.wizard`, with `.wizard__foot` for the buttons |
| Help | At the end of the part of the step it explains | `.help-links` with `.help-link` buttons, opening a slide-out (`.side-panel`) |
| Review aids, testing only | Beside the step on computers, under it on phones | `.wizard-aside` holding `.wizard-next` (What happens next) and `.wizard-tree` (decision tree) |

**Review aids are for testing, never the finished product (TheMightyTRexUK, 4 November 2026).** What happens next
and the decision tree help people who review a wizard follow where each choice leads. An app shows them only
while its testing setting is active (the same setting as its Send feedback button, [Snaglist](https://github.com/TheMightyTRex/snaglist)),
and mock-ups show them.
Leave `.wizard-aside` out of the page, or give it `hidden`, and the step takes the whole width.

`.wizard-layout` puts the step on the left and the review aids on the right from 1100px, one under the
other under that width. The step always comes first in the reading order.

## 2. The first question

1. **Ask which job first, when there is more than one.** For a set-up, the jobs are "New install", "Restore a backup"
   and "Migrate from other apps". Each answer has its own wizard, with its own steps and count. `.wizard-paths` shows
   each job as a card with its stages and number of steps, and marks the chosen one.
2. **Ask nothing the app can find out.** A migration checks what is already there and plans from it,
   instead of asking.
3. **Ask in the order a person would do the job by hand.** Install, sign in, decide what to follow, then
   build each part in the order it depends on the last.

4. **The same first question in the browser and the terminal.** An app with both kinds of set-up asks "How do you want
   to start?" in both, with the same answers. It adds "Already installed" when the app finds itself there. The
   recommended answer comes from what was found, never from a guess.

### One wizard, two ways to show it

An app that can be set up in a browser and in a terminal has **one set of questions**. The steps are the same, in the
same order, with the same answers, defaults, words and help. The terminal is a different drawing, not a different
wizard (`TERMINAL.md`).

- **Change both together.** When you add a step, question, answer, default or help text to one, add it to the other in
  the same change. If one way truly cannot do something yet, the other says so in words and points to it. The gap is
  then a task, not an accident.
- **One source for the words** where the code allows it (a shared list of steps and help), so they cannot drift.
- **A run first script hands over, it does not decide.** It finds what is on the computer, such as an existing
  install, apps already running and the memory. It passes that on, so both set-ups recommend the same answers.
- **Check it before every release:** walk each job in both and compare the steps side by side (section 13).

## 3. Steps

1. **One question per step.** The heading is the question or the job ("Choose a torrent app"), never the
   name of a settings section.
2. **Steps that do not apply are left out**, not shown and skipped. While testing, the decision tree still
   lists them, crossed through, with the reason ("Left out: you follow music only").
3. **A step with too much in it is split into parts**, each its own page. `.steps--sub` under the progress bar names
   the parts, with done ones ticked and the current one outlined. It is as wide as the progress bar, the parts share
   the width equally, and a line joins each part to the next (in the accent colour after a done part). The parts are
   numbered 1, 2, 3 within the step.

   **Each part is a step in the progress bar's total.** When Download apps is steps 6 to 8 of 18, the progress bar
   says "step 7 of 18" on its second part. On phones the step bar is only the numbers joined by lines. A done part's
   number becomes a tick, and the names stay for screen readers.

   The summary at the end shows the parts as one line.
4. **Choices are option cards** (`.option-cards`, one `.option-card` each), with a title and one line on
   what it means for the person.
5. **Mark one choice "(recommended)"** where one suits most people, in the title, with the reason in its
   line ("The one most guides use."). Never "easiest", "simple" or other words about difficulty.
6. **Every choice offers both ways:** "Install and set it up for me" and "I have it already", where the app
   can do both.
7. **An optional step has Skip this step**, and the summary at the end lists what was skipped, each with
   where to set it later.
8. **Defaults are filled in.** Keep the defaults and finish is offered where every remaining step has a
   safe default.

## 4. Buttons

- `.wizard__foot`: Continue (primary) first, then Back, then Skip this step on the right.
- Continue names the next thing when that helps ("Continue to Usenet"). The last step's button says what
  it does ("Open Starboard", "Go to the dashboard").
- Back returns to the step before, including the part before in a step in parts. Nothing is lost by going
  back.
- Continue saves the answer. Nothing is lost silently.

## 5. Progress bar

- Words first, bar under them. "New install · step 7 of 18 · Build your media server" is on the left, and "11 to go"
  is on the right. The last step says "Last step".
- The bar is `role="progressbar"` with `aria-valuenow`, `aria-valuemax` and `aria-valuetext` ("Step 7 of
  18: Usenet").
- The count is for the chosen job only, and changes when a choice leaves steps out.
- On phones the step list (`.steps--collapse`) becomes "Step 6 of 18" (`.steps__short`).

### A job's progress, in the browser and the terminal

When a step runs a job that takes time (installing, downloading, building, restoring):

- **One bar per job, drawn once and updated in place.** It never repeats down the page or the window. A redraw
  replaces it; a retry draws the step afresh with one new bar, and the jobs already done listed with a tick.
- **Words beside the bar:** what is happening, named ("Downloading and starting the apps…"), and which job of how
  many. Never a vague wait message: the timer and the count say that the job is still going.
- **On the right, after the timer, how far it has got** when the job can tell. It reads "3 min 12 s · 5 of 12
  installed" while the apps download, then "9 of 12 running" while they start (TheMightyTRexUK, 7 November 2026).
  Count from the thing itself (Docker), not from the job's words, and leave the count out when it cannot be asked. In
  the browser the count is the bar's `aria-valuetext`.

  In the terminal it follows the timer on the bar line.
- **Errors go under the bar.** The bar stays where it stopped, marked "did not finish". The problem is under it in
  plain words, with the choices Try again (recommended), Show the details, or Stop. Never write over the bar, and
  never move the error before it.
- **No wrapping:** a bar line is cut to the width it has, so it never runs onto a second line.
- In the browser the bar is `role="progressbar"` with `aria-valuetext` in words. The error is a notice after it, tied
  to it with `aria-describedby`, and focus moves to the error's heading.

## 6. Review aid: What happens next

Testing only (section 1).

- Beside every step, one item for each choice on this step says what follows from it. For example, "If: Install and
  set it up for me" is followed by what the app will do.
- The current choice comes first, outlined, with "Your choice".
- Skip this step, where there is one, is the last item, saying where to do it later.
- Long words such as folder paths wrap, so they never make the page wider.

## 7. Review aid: decision tree

Testing only (section 1).

- An ordered list of the chosen job's stages and steps. The heading says which wizard and how many steps ("New install
  wizard, 18 steps").
- Each step has a mark: its number to do, a tick when done, a dash when skipped, an outline when current.
  A decision is a diamond, so it does not rest on colour. A left-out step is dashed and crossed through.
- Each step says its state in words ("You are here", "Done", "Skipped", "Left out: …").
- Done and current steps are links that go back to that step.
- Each choice of a decision opens (`details`) to say what follows from it. The chosen one is marked with
  an icon and "(chosen)" for screen readers.
- The whole tree folds away (`details`, open by default on computers).

## 8. Help ("What is…")

- Every step has help for each thing a newcomer may not know: the app, the term, the folder, the command.
  Check this for every step before a wizard ships.
- **The links go at the end of the part they explain**, not under the heading. The API key link goes after the API key
  fields. `.help-links` holds them, one `.help-link` each with the square `help` icon, written as the question ("What
  is a terminal?").
- **A step's own help goes at the end of the step**, before the buttons, in one `.help-links` row. The step's
  questions come first ("Which one is right for me?"). Then comes "Help with this step", which opens the step's help
  centre article in the slide-out (TheMightyTRexUK, 7 November 2026). Never use a fold-out (`details`) for help.
- A link opens a slide-out (`.side-panel-layer` with `.side-panel`, opened with `data-opens`), because help is longer
  reading beside the step ("Slide-out, dialog or page" in `LIBRARY.md`; 4 November 2026). The step stays in view
  beside it on computers. On phones the slide-out is full width.
- The help slide-out is the wide one, about half the screen (`.side-panel--wide`). Its header (the question, or "Help:
  " and the step's question, and Close) and its foot stay in view. Only `.side-panel__body` scrolls. The foot has
  "Back to set-up" (a secondary button) first.

  When the help is a help centre article, it then has "Read it in the help centre" with the `help-new-tab` icon.
- When the step has a required field, the help ends with the key "* = Required" (`.required-key`); the form
  itself only has the stars (`LIBRARY.md`, Field).
- It follows every slide-out's behaviour. Focus moves to Close and Tab stays inside. Escape, Close and a press outside
  close it. Focus returns to the link, and the page behind does not scroll.
- Help follows `HELP-WRITING.md`: the basics first, then what it means for this step. Pictures are
  figures made from real text, with a caption that says what they show.

## 9. Addresses and commands

- A server address is a link that opens in a new tab ("(opens in a new tab)" for screen readers), with a copy button
  beside it. Use `.address` with `.copy-btn`.
- A command to run is a `.command` with a labelled copy button (`.copy-btn.copy-btn--label`, the word Copy beside the
  icon), because newcomers may not know the icon.
- Copying works on plain http too: when the browser refuses the clipboard, `components.js` copies from a
  hidden text box. The toast says what was copied (`data-copied`, such as "Address copied").

### Choosing an outside service (a VPN provider, a Usenet provider)

- A grid of option cards that fits the width (`.option-cards--row`), with at most six of the best known. Each has its
  name spelt as on the service's own site, and its site under it as a new-tab link with the `external-link` icon. Then
  comes one card, "Another one that … supports", which shows a field to enter the name.
- Nothing is chosen the first time: the service is the person's own. When they come back, their last answer is
  kept. The terminal lists the same services, from the same list file, with no default the first time.

### Signing in to an outside service (a cloud service)

TheMightyTRexUK, 16 November 2026 (Starboard's Connect a cloud service). When a step signs in to a service on the
service's own page (OAuth), never ask for the person's password for that service.

- **Two ways to finish, the same weight**, as option cards: "Complete on the phone" and "Complete in this browser".
  Offer the phone only where the service has a device flow, which is a short code entered on its own page while the
  wizard waits by itself. Elsewhere offer the browser alone, with no empty choice. Remember the last way chosen.
- **On the phone:** `.qr-card` has the QR code of the service's own page, dark on white in every theme. The QR code is
  never the only way. The page is written out as an `.address` with Copy, and the code is a `.device-code` with a
  labelled Copy button, whose label spells it out a character at a time. Under it, `.signin-wait` shows the words and
  the time left in a polite live region, said only when they change, and a busy bar.

  When the approval arrives, the wizard moves on by itself and says so. At the time limit it says so, with Try again.
- **In this browser:** `.signin-card` with `.signin-steps` has three parts. First, open the sign-in page, as a new-tab
  link styled as a secondary button, because the step's primary button is Continue, after the address is pasted.
  Second, what the browser shows after (a made-up example of the address in `.signin-example`). Third, the field for
  the whole address.

  Say why in one plain sentence. The app checks what is pasted before it uses it.
- **Keys or a password instead:** a service that signs in with keys asks for them on the step, each field with where
  to find it.
- **Then test before saving:** `.test-checks`, one line for each check (reach, write, read back, remove), each with
  its state in an icon and in words. A failed check says what to do; a sign-in the service no longer accepts says
  "Sign in again", which goes back to the sign-in step.
- **Closing part way** ends the sign-in and keeps nothing; focus goes back to the button that opened the slide-out.
- Anything set up this way gets **Test connection** beside it afterwards. The result is in `.tested` (an icon, the
  word, and when it was tested), and it is kept so it shows when the page is opened again.

### Check before writing

- The step before anything is written is a table (`.table.table--fixed.table--middle` in `.table-wrap[data-stack]`).
  It has What, Your answer and a Change button on each row that goes back to that step. Settings shown in full are a
  table too, never a list of terms (TheMightyTRexUK, 7 November 2026).

## 10. The end

- `.wizard-summary` has one line for each step. It shows what was set (with a tick) or skipped (with a warning edge
  and where to set it later), and each line links to its settings page.
- Then the one next thing, as the primary button.

## 11. Words

Every word follows `CONTENT-DESIGN.md`. The ones wizards get wrong most often:

- Questions and jobs as headings, in sentence case, with no question numbers written in ("STEP 1 OF 9").
- No contractions and no "Let's".
- "Select", not "click"; "enter", not "type in".
- Example data is made up: addresses in 192.0.2.x, people called Alex and Sam.
- A link that leaves the app says "(opens in a new tab)".
- An error is beside its field and says what to do.

## 12. Feedback in a wizard

Every wizard carries [Snaglist](https://github.com/TheMightyTRex/snaglist), so people can say where it went
wrong while they are in it (5 November 2026):

- The **Send feedback** button is always there. Each report says which step it came from (the step's id as Snaglist's
  page or part), so you can follow a report back to the exact question.
- Reports go to the app's GitHub issues by default. A wizard often runs on a computer that is not online yet, so offer
  Snaglist's **Show as a QR code** too. The phone scans it and opens the same pre-filled issue. When the browser says
  it is offline, that choice comes first, with the reason.
- The QR code is never the only way: the link is shown as text with a Copy button, and Download keeps the whole
  report.
- When a step fails, its error message offers **Report this problem**, with the error already in the report.
- Snaglist's privacy rules hold: nothing entered in the wizard's own fields, no passwords, keys or set-up codes.
- A wizard in a terminal has the same feedback, drawn differently: read `TERMINAL.md`, section 7.

## 13. Checks before a wizard ships

1. Walk every job, and every choice that leaves steps out, to the end.
2. Every step has help for each term and, for testing, What happens next and a place in the tree.
3. With the testing setting off, neither review aid shows and the step has the whole width.
4. Four themes, 175% text, a phone at 390px wide: nothing wider than the screen.
5. Keyboard only: every choice, link, dialog and Back works, and focus moves to each new step's heading.
6. A screen reader hears the progress, the step's state and the chosen choice.
7. Send feedback opens from every step, the report names the step, and the QR code scans with a phone.
8. An app with a browser and a terminal set-up: walk every job in both, step by step side by side. Both ask the same
   questions in the same order with the same defaults (section 2, One wizard, two ways to show it).

## 14. A wizard in a slide-out (26 November 2026)

Most wizards are pages (section 1). A job of three steps or fewer, started from a screen and finished on it, may be a wizard in a wide slide-out instead: Starboard's media server switch is the model. The rules of this guide still hold, with these changes.

- **When.** Three steps or fewer, no review aids needed, and the person should come back to the screen they started from. Four steps or more, or a job that needs What happens next or a decision tree, is a page wizard.
- **Frame.** A wide slide-out (`.side-panel--wide`), with `.panel-wizard` in its body. The foot holds Next (primary), Back and Cancel, in that order. Cancel closes the slide-out and nothing has changed.
- **Progress.** One muted line, "Step 1 of 3", at the start of the body (`.panel-wizard__count`), then the step's heading (an `h3` with `tabindex="-1"`). A job that takes time also shows the bar and the count of section 5 (`.wizard-progress`, `.wizard-job`).
- **Focus and words.** When the step changes, focus moves to the step's heading and the step's result goes into a polite live region. The last step's button names the action ("Switch to Plex"), not "Finish".
- **Nothing changes until the last step.** The first step says so, and says what can be undone and for how long ("You can go back for 24 hours afterwards").
- **What moves.** A `.plain-list` where each item has a state chip in words (Works after the switch, Waits after the switch, Needs pointing at the new media server). The chips come from the status table in `CONTENT-DESIGN.md` section 6, or are added to it.
- **Help.** A "What is..." link in the step opens in a new slide-out only when the step is not itself in one; inside a slide-out, give the answer in the step.
- **Feedback.** The Snaglist link of section 12 sits in the foot of the last step.

The components page "Wizard in a slide-out" shows it, and `LIBRARY.md`, App patterns, lists the classes.

