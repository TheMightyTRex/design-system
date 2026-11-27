# AI-triggered checks

Version 1.0, 26 November 2026. How the owner asks an AI assistant to run a standard check with a short phrase, what
the assistant must do, what it must report, and what it cannot do without a person. The first check is the
**Accessibility check** (section 5). Every word follows `CONTENT-DESIGN.md`.

## About this guide

### What it is for

Some checks are long, and a quick version is tempting. A person who says "do an accessibility check" may mean a quick scan,
and an assistant may do only a quick scan. An AI-triggered check fixes that. It gives the check a name, a trigger
phrase, a fixed list of steps and a fixed report. When the owner uses the phrase, the assistant does all of it.

### Who it is for

The owner of a project who wants the same full check each time. Developers and reviewers who want to run or read
the same check. AI assistants, which follow the steps. It is public, so you may use it for your own projects under
the guide licence (CC BY 4.0).

### How to use it

1. Read section 1 to learn what an AI-triggered check is, and section 2 for how to ask for one.
2. Read section 3 for the rules every check keeps, and section 4 for the limits of every check.
3. For the Accessibility check, read section 5. Give an assistant the prompt in section 5.7.
4. Reviewers use the checklist in section 5.8 on the report that comes back.

**For AI agents:** treat every step of a check as required. If you skip a step, write "Not tested" in the report
and say why. Never write "Pass" for something you did not run.

---

## 1. What an AI-triggered check is

An AI-triggered check is a standard procedure with five parts:

| Part | What it is |
|---|---|
| A name | "Accessibility check" |
| Trigger phrases | The short words that start it |
| Steps | Every step, in order, with no step left to the assistant's taste |
| A report | One template, so every run can be compared |
| Limits | What the check cannot tell you, and what needs a person |

It is not a replacement for people. It is a way to get the same careful work, every time, quickly.

## 2. How the owner starts one

The owner enters the trigger phrase and, if needed, the scope. For example:

- "Accessibility check on the Updates page."
- "Run the accessibility check on the whole design system."
- "A11y check, plug-in tabs only."

If the owner gives no scope, the assistant asks one short question: "Which pages, plug-in or part?" It does not
guess a wider or narrower scope.

The skill file that holds the assistant's copy of a check lives in the assistant's skills folder (`SKILL.md`) on the
owner's computer. **The skill is the AI's copy of this guide.** This guide is the published version. When they
differ, the newer one wins, and whoever notices the difference tells the owner so that both are made the same.

## 3. Rules every check keeps

1. **Own worktree.** Work in a new git worktree in the project's build cache folder, never in the shared checkout the
   owner keeps. Other sessions use that checkout.
2. **Own ports.** Start servers on ports no one else uses, and stop them when the check ends.
3. **Sample data only.** Run against a copy of the app that holds made-up data.
4. **Never the owner's server.** Do not open, scan or change the owner's live server or media server.
5. **Never passwords.** Never type, read or ask for the owner's passwords, tokens or keys. Use test accounts made
   for the copy.
6. **Heavy jobs by the book.** Run heavy jobs through the project's heavy-run script and keep at most two at a
   time. Put large output in the build cache folder.
7. **Say what was tested.** The report states the scope, the date and the commit tested.
8. **Plain English.** Write the report in plain English, in British English, with no em dashes and no
   contractions.
9. **No merge, no release.** Open pull requests for fixes. The owner merges and releases.
10. **Leave nothing running.** Stop every server and browser started, and list files left behind.

## 4. What an AI cannot verify

An assistant can run tools, read code and use a browser. It cannot do these, and the report must say so:

- **Hear a screen reader on a device it does not have.** JAWS, NVDA, Narrator, VoiceOver, TalkBack and Dragon run
  on Windows, Apple or Android devices. An assistant on a Linux server may be able to run Orca, and that is all.
  Everything else is marked **Expected**: the steps and wording are written, and a person must confirm them.
- **Judge comfort.** Whether a page is tiring, confusing or slow to use for a real person.
- **Replace people who use assistive technology.** The check reduces the problems that testing with those people
  would find. It does not remove the need for that testing.
- **Be sure about wording.** Each screen reader says the same thing in its own way, and versions change. The
  wording in this guide is a guide, not a promise.

Anything an assistant cannot verify goes in the report under "What needs a person", with exact steps.

## 5. The Accessibility check

Added 26 November 2026 at the owner's request (task DASH-606): "do a full accessibility check for all types of
assistive technology and check it is in a logical order and is not repeating words and actions where it is not
needed."

### 5.1 Trigger phrases

Any of these starts the Accessibility check:

- "Accessibility check"
- "Run an accessibility check" or "do an accessibility test"
- "A11y check" or "a11y test"
- "Screen reader check", "keyboard check" or "logical order check" (all of the check still runs, not only the
  part named)

An accessibility check is never only a scan. The assistant does every step in this section, or says what it did not do.

### 5.2 Before you start

- Say the scope: which pages, plug-in or part of the design system.
- Make your own worktree and copy with sample data (section 3).
- Note the date and the commit you test.
- Read `ACCESSIBILITY.md` (the one accessibility guide), then `WCAG.md` and `ALT-TEXT.md` for the detail of the rules the pages must meet.

### 5.3 The steps

**Step 1: the automatic base.** The parts of the standard test in `ACCESSIBILITY.md` section 26.1 (the sixth, a person with a reader, is in step 2):

| Part | Command in Starboard | What it checks |
|---|---|---|
| Scan | `tools/a11y.sh` | WCAG 2.2 AA by axe-core in Light, Dark and High contrast; structure; target size; reflow; forced colours; reduced motion |
| Reading order | `ORDER=1 tools/a11y.sh` | What a screen reader reads against what is shown; Tab never jumps back; landmarks in order; h1 first |
| Keyboard walk | `TASKS=1 tools/a11y.sh` | The main tasks by keys alone |
| Focus after actions | The walk | Focus stays where the person was after a save, delete or redraw |
| What is said | The walk | Short spoken summaries only; a whole list is never a live region |

For the design system itself, which has no `a11y.sh`, run axe-core on each changed page in the four themes (Light,
Dark, High contrast, High contrast dark) and run `node tools/check_demos.mjs`. Also try large text (175%), wider
text spacing, a short window, 320 px wide and zoom to 400%. Record the numbers.

**Step 2: every type of assistive technology.** Section 5.4 lists the exact steps for each. Run each one you can.
Write "Not tested" and give the steps for the rest.

**Step 3: logical reading and focus order.** On every page, slide-out, dialog and wizard:

1. Tab through from the top. Focus moves in the same order as the eye: top to bottom, left to right in a language
   that reads that way, and in the order of the task.
2. Read the page with a screen reader or the accessibility tree. The reading order matches the visual order.
3. The headings list reads like a contents page: one h1, no skipped levels.
4. The landmarks (header, navigation, main, footer) are in order and each has a distinct name when there is more
   than one of a kind.
5. After every action, focus lands in a sensible place: a dialog or slide-out moves it in and returns it to the
   opener on close; a menu returns it to its button; an error moves it to the error summary or first bad field; a
   save, delete or update keeps it where the person was; a bulk action moves it to the next sensible item.
6. Nothing opens or moves focus by itself when the page loads.
7. Each live region says the right short thing, once.

**Step 4: no needless repeats.** Find anything a person hears or tabs through twice without need:

- the same link text for different places ("Edit", "Edit", "Edit") with no extra name;
- a button and a link that do the same thing next to each other;
- an `aria-label` that repeats the visible text, or a name that says "button" or "link" in words;
- a status said in a chip and said again in a live region;
- the same tip or hint on every row of a list;
- a section intro that repeats its heading;
- landmarks that add nothing, such as a `nav` around one link;
- tab stops that add nothing, such as a decorative icon that can take focus;
- an icon beside a name that is read as well as the name.

For each one, write the fix. Where a script can catch the problem (order, duplicate names), add or extend an
automatic check rather than fixing it by hand only.

**Step 5: report.** Use the template (section 5.6).

### 5.4 Each type of assistive technology

For each technology: how to start it, the steps for one page, what you expect to hear, and whether an assistant
can verify it. **Verified** means a person or assistant ran it and heard the result. **Expected** means the steps
and wording come from the vendors' guides and the standards in section 5.5, and nobody has run them on this page.

Use the same short test page set for every technology: the page's heading, its main navigation, one form with a
required field and an error, a button that opens a dialog, and a change that is announced (a save).

#### Screen readers

| Technology | Start and stop | Steps for one page | What to expect | Can an AI verify it? |
|---|---|---|---|---|
| **NVDA** (Windows, with Firefox or Chrome) | Start: Ctrl + Alt + N. Stop: NVDA + Q. The NVDA key is Insert, or Caps Lock if chosen. Open the Speech Viewer from NVDA + N, Tools, Speech Viewer, to read what was said. | 1. Press H to move through headings, and NVDA + F7 for the Elements list (headings, links, landmarks). 2. Press D for landmarks. 3. Tab to a field: NVDA switches to focus mode and beeps; NVDA + Space switches mode by hand. 4. Press Enter on the dialog button. 5. Press Escape. | "Updates, heading level 1". "Main landmark". "Name, edit, required" and after a mistake "invalid entry" with the error text. "Add a place, dialog". After saving, a short spoken "Saved". Focus returns to the opener. | No. Expected only. A person with Windows confirms. |
| **Orca** (Linux, GNOME, with Firefox) | Start or stop: Super + Alt + S, or run `orca` from a terminal. The Orca key is Insert, or Caps Lock on a laptop layout. | 1. Press H for the next heading and M for the next landmark. 2. Tab through the controls. 3. Open the dialog and close it. 4. Save, and listen for the live region. | The same sorts of words as NVDA: "heading level 1, Updates", "button, Save changes", "dialog". Orca's wording differs a little by version. | Sometimes. Only on a desktop session with Orca installed. Mark Verified only if you heard or logged the speech; otherwise Expected. |
| **JAWS** (Windows, with Chrome or Edge) | A person starts it from the Start menu or desktop. The JAWS key is Insert. | 1. H for headings and Insert + F6 for the headings list. 2. Insert + F7 for the links list. 3. R for the next landmark and Q to jump to the main region. 4. Enter on a field to use forms mode; the numeric keypad Plus returns to browse mode. | "Heading level 1, Updates". "Main region". "Name, edit, required". Dialogs are announced by name. | No. Expected only. Needs a person with Windows and a licence (JAWS has a free 40-minute demo mode). |
| **VoiceOver on Mac** (Safari) | Command + F5 (add fn on some laptops), or triple-press Touch ID. VO means Control + Option. Switch on full keyboard access in Safari's accessibility settings so Tab reaches every control. | 1. VO + A reads the page. 2. VO + Command + H jumps to the next heading. 3. VO + U opens the rotor; use Left and Right to pick Headings, Links, Landmarks or Form controls. 4. VO + Command + J jumps to the next form control. 5. VO + Space activates. | "Updates, heading level 1". "Save changes, button". "Name, required, edit text". Dialogs: "Add a place, dialog". | No. Expected only. A person with a Mac confirms. |
| **VoiceOver on iPhone** (Safari) | Settings, Accessibility, VoiceOver, or triple-click the side button if set. | 1. Touch the screen to hear the item under the finger. 2. Swipe right or left to move to the next or previous item. 3. Double-tap to activate. 4. Turn the rotor with two fingers, choose Headings, then swipe up or down to move by heading. 5. Scroll with three fingers. | Each item is read once: "Updates, heading". "Save changes, button". "Name, text field, required". Dialog contents are the only things reachable while it is open. | No. Expected only. A person with an iPhone confirms. |
| **TalkBack** (Android, Chrome) | Settings, Accessibility, TalkBack, or hold both volume keys if set. | 1. Drag a finger to explore the screen. 2. Swipe right or left to move item by item. 3. Double-tap to activate. 4. Use the reading controls (swipe up then down) to choose Headings or Controls, then swipe to move. 5. Open the dialog and close it with Back. | "Updates, heading". "Save changes, button, double-tap to activate". "Name, edit box, required". | No. Expected only. A person with an Android phone confirms. |
| **Narrator** (Windows, Edge) | Start or stop: Windows logo key + Ctrl + Enter. The Narrator key is Caps Lock or Insert. | 1. Scan mode is on in Edge; Narrator key + Space switches it. 2. Press H for the next heading and D for the next landmark. 3. Narrator key + S gives a summary of the headings, links and landmarks. 4. Narrator key + Alt + X opens the speech recap, which shows what was said. | "Heading level 1, Updates". The summary gives counts, so a wrong count is a clue to missing structure. | No. Expected only. A person with Windows confirms. |

Keys for headings and landmarks in Narrator, and for Orca, differ by version. Treat the table as the starting
point and check the vendor's guide for the version in use.

#### Keyboard, switches and voice

| Technology | Steps | What to expect | Can an AI verify it? |
|---|---|---|---|
| **Keyboard only** | Put the mouse away. Press Tab and Shift + Tab through the whole page. Use Enter and Space on controls, arrow keys inside menus, tabs and lists, and Escape to close. | Every control is reached once, in the visual order. Focus is always visible. No trap. A skip link is first. The sticky header never covers the focused item. | Yes. The keyboard walk (`TASKS=1 tools/a11y.sh`) and a browser run do this. |
| **Switch access and scanning** (one or two switches, or Switch Access on Android) | The software steps through controls in the tab order and a switch selects. Check that there is one tab stop for each control, nothing needs hover, and no timed action. | Each control can be reached by stepping. No action needs a drag, a long press or a hover (WCAG 2.5.1, 2.5.7). | Partly. An AI checks the structure by script; a person confirms with a real switch. |
| **Voice control** (Voice Control on Apple devices, Voice Access on Windows 11, Dragon) | Switch it on. Windows Voice Access: say `click Save`, `show numbers`, `click 12`. Dragon: say `click Save`, then `show numbers` and the number. macOS and iOS Voice Control: say `click Save` (iOS: `tap Save`), `show numbers` or `show names`, then the number. Exact steps: `ACCESSIBILITY.md` section 22. | Every control answers to the words shown on it. The accessible name contains the visible text at the start (WCAG 2.5.3 Label in Name). A control that needs `show numbers` because its name does not match is a finding, and the report names it. | Partly. An AI can compare each accessible name with its visible text by script (an automated Label in Name check is in progress in Starboard). It cannot speak to the software. A person runs the steps, and until then the result is Expected. |

#### Sight, colour and motion

| Technology or setting | Steps | What to expect | Can an AI verify it? |
|---|---|---|---|
| **Magnifier and zoom** | Browser zoom to 400% on a 1280 px window (a 320 px layout). Then the operating system magnifier (Windows Magnifier, Zoom on a Mac). Then the Text size setting at 175% and wider text spacing. | No sideways scroll for text. No overlapping or cut-off text. Messages appear near the thing they belong to. | Yes for zoom, text size and spacing. A person confirms the system magnifier. |
| **Forced colours and High contrast** | Switch on a Windows contrast theme, or emulate `forced-colors: active` in the browser tools. Also try the library's High contrast switch. | Text, borders, focus rings and icons remain visible. Controls are still recognisable. | Yes by emulation. A person confirms on a real Windows contrast theme. |
| **Dark** | Switch the theme to Dark and High contrast dark. | Text meets 4.5:1 and controls 3:1. | Yes (`tools/contrast.py`, axe). |
| **Reduced motion** | Switch on "reduce motion" in the system or emulate `prefers-reduced-motion: reduce`. | Nothing moves without need. Nothing flashes more than three times a second. | Yes by emulation. |
| **Colour is not the only signal** | View the page in greyscale. | Every status, error and chart is clear without colour. | Yes by emulation, and by reading. |

#### Touch, reading and thinking

| Need | Steps | What to expect | Can an AI verify it? |
|---|---|---|---|
| **Touch on a phone and target size** | Use a real phone or a 375 px emulation with touch. Measure each control. | Targets are at least 44 px, apart from dense table rows at 32 px (WCAG 2.5.8 sets 24 px as the floor, and nothing is smaller). No action needs a gesture with more than one finger or a drag with no button. The page works upright and sideways. | Yes for size and layout: the scan checks target size today, and a per-control confirmation is in progress in Starboard. A person confirms touch comfort. |
| **Reading and cognitive needs** | Read the page text. Run `tools/verbose-check.py`. Read the error messages and the steps of every task. | Plain English (the Plain English Campaign rules in `CONTENT-DESIGN.md`). One idea for each step. Clear errors that say what went wrong and how to fix it. No time limits without a warning and a way to extend. | Partly. An AI checks wording and reading level. A person judges clarity. |

### 5.5 Where the steps come from

Read on 26 November 2026. Each source is the maker's own, or a government or standards body.

- W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/), a Recommendation of 5 October 2023. The nine new criteria are in
  [What is new in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/).
- W3C, [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/), for keyboard interface and focus
  management (read 26 November 2026; the page carries no date of its own).
- GOV.UK Service Manual,
  [Testing with assistive technologies](https://www.gov.uk/service-manual/technology/testing-with-assistive-technologies),
  last updated 24 May 2022. It names JAWS, NVDA, VoiceOver on iOS, TalkBack, a magnifier and Dragon, and asks for
  magnifier testing to at least 4 times zoom. It also advises testing on real devices.
- GOV.UK Service Manual, [Understanding WCAG 2.2](https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag).
- WebAIM, [Using NVDA to evaluate web accessibility](https://webaim.org/articles/nvda/), last updated 28
  September 2020. Keys are still current.
- WebAIM, [Using VoiceOver to evaluate web accessibility](https://webaim.org/articles/voiceover/), last updated 17
  June 2026.
- Deque University, [JAWS keyboard shortcuts](https://dequeuniversity.com/screenreaders/jaws-keyboard-shortcuts),
  no date shown.
- Microsoft, [Complete guide to Narrator](https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1),
  no date shown.
- Google, [Basic TalkBack gestures](https://support.google.com/accessibility/android/answer/6151827), no date shown.
- Apple, [Use VoiceOver gestures on iPhone](https://support.apple.com/guide/iphone/learn-voiceover-gestures-iph3e2e2281/ios).
- GNOME, [Orca screen reader help](https://help.gnome.org/users/orca/stable/). Its command pages were not read in
  full, so the Orca keys in section 5.4 are marked Expected.

The design system's own list of free tools is
[Outside tools for accessibility and testing](https://themightytrex.github.io/design-system/resources/outside-tools.html).

Screen reader wording and keys change with each version. When you check this guide, read the sources again and
change the dates.

### 5.6 The report

Write the results to the file or folder the owner names, called `ACCESSIBILITY-CHECK-<date>.md`. Copy the
[report template](https://themightytrex.github.io/design-system/resources/accessibility-check-report-template.md)
(`resources/accessibility-check-report-template.md`). It has:

1. The scope: what, when, which commit, which computer, browser and versions.
2. A summary: counts of pass, fix and not tested, and the three most important findings.
3. The automatic base: each tool, its numbers and what it cannot cover.
4. One table for each page: area, result (**Pass**, **Fix** or **Not tested**), what was found and the next step.
5. The assistive technology table: each technology, its status (**Verified**, **Expected** or **Not tested**), what
   was announced and whether a person is needed.
6. The needless repeats found, and the fix for each.
7. The fixes, each as a small pull request that the assistant does not merge.
8. What needs a person, with exact steps.
9. Files left behind.

The report ends with the top findings, what needs the owner (real devices, JAWS, iPhone, with exact steps) and the
files left behind.

### 5.7 A prompt to give any AI assistant

Copy this and give it to an AI assistant that can run commands and use a browser. Replace the part in brackets.

```
Run an Accessibility check on [the pages, plug-in or part to check] of [the project and its address].

Follow https://themightytrex.github.io/design-system/guides/ai-checks.html section 5 in full.
Do all of these, and never only a scan:

1. Work in your own git worktree in the build cache folder, on your own ports, with sample data.
   Never use my server and never ask for or type my passwords. Stop everything you start.
2. Run the automatic base: axe-core for WCAG 2.2 AA in Light, Dark and High contrast, reading
   order, a keyboard and Tab walk of the main tasks, focus after each action, and live regions.
   Also test 400% zoom, 175% text, wide text spacing and 320 px width.
3. Check each type of assistive technology: NVDA, Orca, JAWS, VoiceOver on Mac and iPhone,
   TalkBack, Narrator, keyboard only, switch access, voice control, magnifiers, forced colours,
   High contrast, Dark, reduced motion, touch and reading needs. For each one, give the exact
   steps and the words you expect to hear. Mark each one Verified (you ran it and heard it),
   Expected (written from the vendor guide, not run) or Not tested.
4. Check that reading order and focus order match the visual order and the task, that headings
   and landmarks make sense, and that focus goes to the right place after every action.
5. Find everything a person hears or tabs through twice without need, and fix or list it.
6. Write the report with the template at
   https://themightytrex.github.io/design-system/resources/accessibility-check-report-template.md :
   a table for each page with Pass, Fix or Not tested, the numbers for each tool, what each tool
   cannot cover, the fixes as small pull requests (do not merge), and what needs a person with
   exact steps.
7. Write in plain English, British English, with no em dashes and no contractions.
   Never write Pass for something you did not run.
```

### 5.8 Checklist for reviewers

Use this on the report that comes back. Every answer should be yes.

- The report names the scope, date and commit.
- Every page has a table, and no cell is empty.
- The numbers for axe, reading order, the keyboard walk and the focus checks are given.
- All the technologies in section 5.4 are listed, each marked Verified, Expected or Not tested.
- Nothing is marked Verified for a technology the assistant could not have run.
- Reading order and focus order are reported for each page, slide-out and dialog.
- The needless repeats are listed, with fixes.
- Each fix is a pull request that is not merged, and any new automatic check is named.
- "What needs a person" has exact steps.
- The assistant used its own worktree, ports and sample data, and left no servers running.
- The words are plain English, British English, with no em dashes and no contractions.

### 5.9 Limits

- Automatic tools find only some problems, and the share is well under all of them. Treat a scan with no findings
  as a start.
- An assistant cannot hear JAWS, NVDA, VoiceOver, TalkBack, Narrator or Dragon unless it runs on a device that has
  them. Expected wording is not heard wording.
- Passing the check does not mean the page conforms to WCAG 2.2 AA. It means the checks that were run passed.
- People who use assistive technology find problems no check finds. Read how in
  [Get feedback](https://themightytrex.github.io/design-system/resources/get-feedback.html)).

## 6. Adding a new AI-triggered check

1. Name it and write its trigger phrases.
2. Write each step so that an assistant needs no further choice, and say what an assistant cannot verify.
3. Add a report template under `resources/` and link it from the check.
4. Add a prompt to copy and a checklist for reviewers.
5. Keep the assistant's skill file in step with this guide, and say which is newer.
6. Add the check to this guide's contents and to the site search (the site builder does this from the headings).

## 7. Checklist for every AI-triggered check

- [ ] It has a name, trigger phrases, steps, a report template and limits.
- [ ] It keeps the rules in section 3.
- [ ] It says what an assistant cannot verify.
- [ ] It has a prompt to copy and a checklist for reviewers.
- [ ] Its sources are cited and dated.
- [ ] It is linked from the guide it belongs to (for the Accessibility check, `ACCESSIBILITY.md`).
- [ ] The assistant's skill file matches it.
