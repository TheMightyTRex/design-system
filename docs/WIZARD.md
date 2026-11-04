# Wizard: the rules

4 November 2026. One set of rules for every wizard in every app that uses the library: first-run set-up,
upgrades, restores, migrations and any other job done in steps. The classes are in `components.css`, the
behaviour in `components.js`, and a live example is in the gallery, section Wizard.

A wizard is a page, not a dialog: people link to it, come back to it and spend time in it ("Slide-out,
dialog or page" in `LIBRARY.md`).

## 1. Shape

| Part | Where | Classes |
|---|---|---|
| Progress bar | Top of the wizard | `.wizard-progress` (a `.meter` with a `.progress` bar) |
| Step bar for a step in parts | Under the progress bar, only on a step in parts | `.steps.steps--sub` |
| The step | Under them | `.wizard`, with `.wizard__foot` for the buttons |
| Help | At the end of the part of the step it explains | `.help-links` with `.help-link` buttons, opening a `.dialog.dialog--scroll` |
| Review aids, testing only | Beside the step on computers, under it on phones | `.wizard-aside` holding `.wizard-next` (What happens next) and `.wizard-tree` (decision tree) |

**Review aids are for testing, never the finished product (David, 4 November 2026).** What happens next
and the decision tree help people who review a wizard see where each choice leads. An app shows them only
while its testing setting is on (the same setting as UX notes, `ux-notes.js`), and mock-ups show them.
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

## 3. Steps

1. **One question per step.** The heading is the question or the job ("Choose a torrent app"), never the
   name of a settings section.
2. **Steps that do not apply are left out**, not shown and skipped. While testing, the decision tree still
   lists them, crossed through, with the reason ("Left out: you follow music only").
3. **A step with too much in it is split into parts**, each its own screen. `.steps--sub` under the
   progress bar names the parts, with done ones ticked and the current one outlined. It is as wide as the
   progress bar, the parts share the width equally, and a line joins each part to the next (in the
   accent colour after a done part). **Each part is a step in the progress bar's total**, and the step
   bar's numbers carry on that count: when the parts are steps 6 to 8 of 18, the bar shows 6, 7 and 8
   (`style="counter-reset: step 5"`) and the progress bar says "step 7 of 18" on the second part. The
   summary at the end shows the parts as one line.
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
  API key fields. `.help-links` holds them, one `.help-link` each, written as the question ("What is a
  terminal?").
- A link opens a dialog (`.dialog.dialog--scroll`, `data-close-outside`): the heading and close button and
  the foot ("Back to set-up") stay in view, and only the text scrolls, with its own scroll bar.
- A press on the dimmed page outside the dialog closes it, as Escape and Close do. Focus returns to the link.
- Help follows `HELP-WRITING.md`: the basics first, then what it means for this step. Pictures are
  figures made from real text, with a caption that says what they show.

## 9. Addresses and commands

- A server address is a link that opens in a new tab ("(opens in a new tab)" for screen readers), with a
  copy button beside it: `.address`, with `.copy-btn`.
- A command to run is a `.command` with a labelled copy button (`.copy-btn.copy-btn--label`, the word
  Copy beside the icon), because newcomers may not know the icon.
- Copying works on plain http too: when the browser refuses the clipboard, `components.js` copies from a
  hidden text box. The toast says what was copied (`data-copied`, such as "Address copied").

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

## 12. Checks before a wizard ships

1. Walk every job, and every choice that leaves steps out, to the end.
2. Every step has help for each term and, for testing, What happens next and a place in the tree.
3. With the testing setting off, neither review aid shows and the step has the whole width.
4. Four themes, 175% text, a phone at 390px wide: nothing wider than the screen.
5. Keyboard only: every choice, link, dialog and Back works, and focus moves to each new step's heading.
6. A screen reader hears the progress, the step's state and the chosen choice.
