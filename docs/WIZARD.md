# Wizard: the rules

4 November 2026. One set of rules for every wizard in every app that uses the library: first-run set-up,
upgrades, restores, migrations and any other job done in steps. The classes are in `components.css`, the
behaviour in `components.js`, and a live example is in the gallery, section Wizard. A wizard in a terminal follows
`TERMINAL.md` as well.

A wizard is a page, not a dialog: people link to it, come back to it and spend time in it ("Slide-out,
dialog or page" in `LIBRARY.md`).

## 1. Shape

**Only what the app can show.** A wizard runs inside the app, so it starts once the app is installed and
running. Anything needed before that (Docker, a folder, running the installer) belongs on the help page and in
the installer, which checks it and stops with what to do. Never ask in the wizard about something the wizard
could not run without (4 November 2026). A mock-up that shows those earlier steps marks them off as "Before the
wizard", with their own count, and the wizard's progress starts at its own first step.


| Part | Where | Classes |
|---|---|---|
| Progress bar | Top of the wizard | `.wizard-progress` (a `.meter` with a `.progress` bar) |
| Step bar for a step in parts | Under the progress bar, only on a step in parts | `.steps.steps--sub` |
| The step | Under them | `.wizard`, with `.wizard__foot` for the buttons |
| Help | At the end of the part of the step it explains | `.help-links` with `.help-link` buttons, opening a slide-out (`.side-panel`) |
| Review aids, testing only | Beside the step on computers, under it on phones | `.wizard-aside` holding `.wizard-next` (What happens next) and `.wizard-tree` (decision tree) |

**Review aids are for testing, never the finished product (TheMightyTRexUK, 4 November 2026).** What happens next
and the decision tree help people who review a wizard see where each choice leads. An app shows them only
while its testing setting is active (the same setting as its Send feedback button, [Snaglist](https://github.com/TheMightyTRex/snaglist)),
and mock-ups show them.
Leave `.wizard-aside` out of the page, or give it `hidden`, and the step takes the whole width.

`.wizard-layout` puts the step on the left and the review aids on the right from 1100px, one under the
other below that. The step always comes first in the reading order.

## 2. The first question

1. **Ask which job first, when there is more than one.** For a set-up, that is "New install", "Restore a
   backup" or "Migrate from other apps". Each answer has its own wizard, with its own steps and count.
   `.wizard-paths` shows each job as a card with its stages and number of steps, the chosen one marked.
2. **Ask nothing the app can find out.** A migration looks at what is already there and plans from it,
   instead of asking.
3. **Ask in the order a person would do the job by hand.** Install, sign in, decide what to follow, then
   build each part in the order it depends on the last.

4. **The same first question in the browser and the terminal.** An app with both kinds of set-up asks "How do
   you want to start?" in both, with the same answers, plus "Already installed" when the app finds itself there.
   The recommended answer comes from what was found, never from a guess.

### One wizard, two ways to show it

An app that can be set up in a browser and in a terminal has **one set of questions**: the same steps, in the
same order, with the same answers, defaults, words and help. The terminal is a different drawing, not a different
wizard (`TERMINAL.md`).

- **Change both together.** A step, question, answer, default or help text added to one is added to the other in
  the same change. If one way truly cannot do something yet, the other says so in words and points to it, and the
  gap is a task, not an accident.
- **One source for the words** where the code allows it (a shared list of steps and help), so they cannot drift.
- **A run first script hands over, it does not decide.** It finds what is on the computer (an existing install,
  apps already running, the memory) and passes it on, so both set-ups recommend the same answers.
- **Check it before every release:** walk each job in both and compare the steps side by side (section 13).

## 3. Steps

1. **One question per step.** The heading is the question or the job ("Choose a torrent app"), never the
   name of a settings section.
2. **Steps that do not apply are left out**, not shown and skipped. While testing, the decision tree still
   lists them, crossed through, with the reason ("Left out: you follow music only").
3. **A step with too much in it is split into parts**, each its own screen. `.steps--sub` under the
   progress bar names the parts, with done ones ticked and the current one outlined. It is as wide as the
   progress bar, the parts share the width equally, and a line joins each part to the next (in the
   accent colour after a done part). The parts are numbered 1, 2, 3 within the step. **Each part is a
   step in the progress bar's total**: when Download apps is steps 6 to 8 of 18, the progress bar says
   "step 7 of 18" on its second part. On phones the step bar is just the numbers joined by lines, and a
   done part's number becomes a tick (the names stay for screen readers). The summary at the end
   shows the parts as one line.
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
  it does ("Open Storyarr", "Go to the dashboard").
- Back returns to the step before, including the part before in a step in parts. Nothing is lost by going
  back.
- Continue saves the answer. Nothing is lost silently.

## 5. Progress bar

- Words first, bar under them: "New install · step 7 of 18 · Build your media server" on the left, "11 to
  go" on the right, and "Last step" on the last.
- The bar is `role="progressbar"` with `aria-valuenow`, `aria-valuemax` and `aria-valuetext` ("Step 7 of
  18: Usenet").
- The count is for the chosen job only, and changes when a choice leaves steps out.
- On phones the step list (`.steps--collapse`) becomes "Step 6 of 18" (`.steps__short`).

### A job's progress, in the browser and the terminal

When a step runs a job that takes time (installing, downloading, building, restoring):

- **One bar per job, drawn once and updated in place.** It never repeats down the page or the window. A redraw
  replaces it; a retry draws the step afresh with one new bar, and the jobs already done listed with a tick.
- **Words beside the bar:** what is happening, "Please wait, this can take some time...", and which job of how many.
- **On the right, after the timer, how far it has got** when the job can tell: "3 min 12 s · 5 of 12 installed"
  while the apps download, then "9 of 12 running" while they start (TheMightyTRexUK, 7 November 2026). Count from
  the thing itself (Docker), not from the job's words, and leave the count out when it cannot be asked. In the
  browser the count is the bar's `aria-valuetext`; in the terminal it follows the timer on the bar line.
- **Errors go below the bar.** The bar stays where it stopped, marked "did not finish", and the problem is under it
  in plain words, with the choices: Try again (recommended), Show the details, or Stop. Never write over the bar,
  and never move the error above it.
- **No wrapping:** a bar line is cut to the width it has, so it never runs onto a second line.
- In the browser it is `role="progressbar"` with `aria-valuetext` in words; the error is a notice below it, tied
  to it with `aria-describedby`, and focus moves to the error's heading.

## 6. Review aid: What happens next

Testing only (section 1).

- Beside every step: one item for each choice on this step, saying what follows from it ("If: Install and
  set it up for me" then what the app will do).
- The current choice comes first, outlined, with "Your choice".
- Skip this step, where there is one, is the last item, saying where to do it later.
- Long words such as folder paths wrap, so they never make the page wider.

## 7. Review aid: decision tree

Testing only (section 1).

- An ordered list of the chosen job's stages and steps, under a heading that says which wizard and how many
  steps ("New install wizard, 18 steps").
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
- **The links go at the end of the part they explain**, not under the heading: the API key link after the
  API key fields. `.help-links` holds them, one `.help-link` each with the square `help` icon, written as the
  question ("What is a terminal?").
- **A step's own help goes at the bottom of the step**, above the buttons, in one `.help-links` row: the step's
  questions first ("Which one is right for me?"), then "Help with this step", which opens the step's help centre
  article in the slide-out (TheMightyTRexUK, 7 November 2026). Never a fold-out (`details`) for help.
- A link opens a slide-out (`.side-panel-layer` with `.side-panel`, opened with `data-opens`), because help is
  longer reading beside the step ("Slide-out, dialog or page" in `LIBRARY.md`; 4 November 2026). The step stays
  in view beside it on computers; on phones the slide-out is full width.
- The help slide-out is the wide one, about half the screen (`.side-panel--wide`). Its header (the question,
  or "Help: " and the step's question, and Close) and its foot stay in view, and only `.side-panel__body` scrolls.
  The foot has "Back to set-up" (a secondary button) first, then, when the help is a help centre article, "Read
  it in the help centre" with the `help-new-tab` icon.
- When the step has a required field, the help ends with the key "* = Required" (`.required-key`); the form
  itself only has the stars (`LIBRARY.md`, Field).
- It follows every slide-out's behaviour: focus moves to Close, Tab stays inside, Escape, Close and a press
  outside close it, focus returns to the link, and the page behind does not scroll.
- Help follows `HELP-WRITING.md`: the basics first, then what it means for this step. Pictures are
  figures made from real text, with a caption that says what they show.

## 9. Addresses and commands

- A server address is a link that opens in a new tab ("(opens in a new tab)" for screen readers), with a
  copy button beside it: `.address`, with `.copy-btn`.
- A command to run is a `.command` with a labelled copy button (`.copy-btn.copy-btn--label`, the word
  Copy beside the icon), because newcomers may not know the icon.
- Copying works on plain http too: when the browser refuses the clipboard, `components.js` copies from a
  hidden text box. The toast says what was copied (`data-copied`, such as "Address copied").

### Choosing an outside service (a VPN provider, a Usenet provider)

- A grid of option cards that fits the width (`.option-cards--row`), at most six of the best known, each with
  its name spelt as on the service's own site and its site under it as a new-tab link with the `external-link`
  icon. Then one card, "Another one that … supports", which shows a field to type the name.
- Nothing is chosen the first time: the service is the person's own. When they come back, their last answer is
  kept. The terminal lists the same services, from the same list file, with no default the first time.

### Check before writing

- The step before anything is written is a table (`.table.table--fixed.table--middle` in `.table-wrap[data-stack]`):
  What, Your answer and a Change button on each row that goes back to that step. Settings shown in full are a
  table too, never a list of terms (TheMightyTRexUK, 7 November 2026).

## 10. The end

- `.wizard-summary`: one line for each step, what was set (with a tick) or skipped (with a warning edge and
  where to set it later), each linking to its settings page.
- Then the one next thing, as the primary button.

## 11. Words

Every word follows `CONTENT-DESIGN.md`. The ones wizards get wrong most often:

- Questions and jobs as headings, in sentence case, with no question numbers typed in ("STEP 1 OF 9").
- No contractions and no "Let's".
- "Select", not "click"; "enter", not "type in".
- Example data is made up: addresses in 192.0.2.x, people called Alex and Sam.
- A link that leaves the app says "(opens in a new tab)".
- An error is beside its field and says what to do.

## 12. Feedback in a wizard

Every wizard carries [Snaglist](https://github.com/TheMightyTRex/snaglist), so people can say where it went
wrong while they are in it (5 November 2026):

- The **Send feedback** button is always there, and each report says which step it came from (the step's
  id as Snaglist's page or part), so a report can be followed back to the exact question.
- Reports go to the app's GitHub issues by default. A wizard often runs on a computer that is not online yet,
  so offer Snaglist's **Show as a QR code** too: the phone scans it and opens the same pre-filled issue. When
  the browser says it is offline, that choice comes first, with the reason.
- The QR code is never the only way: the link is shown as text with a Copy button, and Download keeps the whole
  report.
- When a step fails, its error message offers **Report this problem**, with the error already in the report.
- Snaglist's privacy rules hold: nothing typed into the wizard's own fields, no passwords, keys or set-up codes.
- A wizard in a terminal has the same feedback, drawn differently: see `TERMINAL.md`, section 6.

## 13. Checks before a wizard ships

1. Walk every job, and every choice that leaves steps out, to the end.
2. Every step has help for each term and, for testing, What happens next and a place in the tree.
3. With the testing setting off, neither review aid shows and the step has the whole width.
4. Four themes, 175% text, a phone at 390px wide: nothing wider than the screen.
5. Keyboard only: every choice, link, dialog and Back works, and focus moves to each new step's heading.
6. A screen reader hears the progress, the step's state and the chosen choice.
7. Send feedback opens from every step, the report names the step, and the QR code scans with a phone.
8. An app with a browser and a terminal set-up: every job walked in both, step by step side by side, asks the
   same questions in the same order with the same defaults (section 2, One wizard, two ways to show it).
