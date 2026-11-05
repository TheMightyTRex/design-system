# Terminal wizards: the rules

5 November 2026. The same jobs as `WIZARD.md`, for a wizard that runs in a terminal: a server with no desktop,
reached over SSH, with no browser to finish in. Starboard's `./install.sh --terminal` is the first one. Every
rule in `WIZARD.md` about questions, words and help still applies; this guide says how each looks in a terminal.

## 1. Two ways to draw it, one set of words

- **Boxed** (the default in a terminal at least 60 characters wide and 20 lines tall): each step starts on a
  cleared screen, with a heading box, a progress bar and a menu fixed on the bottom line.
- **Plain** (an `APP_PLAIN=1` setting such as `STARBOARD_PLAIN=1`, a `--plain` option, a smaller window,
  `TERM=dumb`, or output that is not a terminal): numbered lines that scroll, with nothing cleared, redrawn or
  drawn over. Screen readers lose their place when a screen is redrawn, and read box characters aloud, so plain
  mode is the one for them. Say how to choose it in the help.
- Both ask the same questions in the same order, with the same answers. Only the drawing changes.
- `NO_COLOR` keeps the boxes and drops the colour.

## 2. The heading box

- One line in a box: the app's name in bold, a dim `|`, then the step's name, and `step 2 of 5` on the right:
  `Starboard | Your media server`.
- Below it, a progress bar the width of the box, and the percentage done.
- The box and the bar are the full width (at most 78 characters), and every line ends at the same column.

## 3. Questions

- One question at a time, numbered answers, the recommended one first, marked with a dot and the word
  "(recommended)". Colour never carries the meaning on its own.
- The default is in brackets, and Enter takes it: `› Your choice [1]:`.
- Several answers at once are typed as numbers with commas: `1,2,7`.
- A long list on a short screen shows what fits, then "4 more: type m to see them".
- Passwords and keys are typed hidden: say "(nothing shows as you type)". After Back, Enter keeps the one typed
  before, without showing it.
- An answer the app refuses is explained on the next line in the app's own words, and the question is asked
  again.

## 4. The menu on the bottom line

- Always the keys that work on this step, then what Enter does on the right:
  `b Back   ? Help   f Feedback   q Stop        Enter: recommended`.
- **b Back** goes back one step, with the last answers as the defaults (the right side says "Enter: keep", and
  the step says "You came back to this step"). Back stops at the step that changed something: once files are
  written, earlier answers are changed in the app's settings instead.
- **? Help** opens help as a box over the step (section 5).
- **f Feedback** opens the feedback flow (section 6).
- **q Stop** stops with nothing else changed, and says how to carry on later.
- In plain mode there is no menu bar: each step's first line says "Type b to go back, ? for help, f to send
  feedback or q to stop".

## 5. Help as a box over the step

- The step behind is dimmed, the box sits in the middle with "Help: " and the question as its title, and the
  bottom line says "Enter Close help".
- Long help shows a page at a time ("Enter: more below").
- Closing it draws the step again exactly as it was, with the cursor at the question.
- Plain mode prints the help under the question instead.

## 6. Feedback, sent with a QR code

The terminal version of Snaglist ("Feedback in a wizard" in `WIZARD.md`):

1. The kind, numbered, as Snaglist offers them: Something is broken, Hard to use, Words are wrong, Hard to use
   with my tools or needs, A new feature, Make something better, Something else.
2. One or two questions, the same as Snaglist asks.
3. The whole report, before anything leaves the machine.
4. How to send it: **Show as a QR code** (recommended), Show the link, Save to a file, or Cancel.

- The report keeps Snaglist's rules: the step and the app's version, the operating system and processor type,
  the last error if there was one, and never anything typed as an answer, a password, a key or a set-up code.
  Email addresses, network addresses, user names in paths and anything like a key are replaced.
- **The QR code** holds a short pre-filled new-issue address: the kind, the step, the person's words cut to fit,
  and the version and system on one line. The whole report is saved on the server at the same time, and the
  issue says where.
- **It must fit the window.** Half-block characters draw two rows of the code on each line, so the code's width
  is its number of modules and its height is half that. In a window of 78 by 30, with one title line and the
  two menu lines, the code can be version 8 at most (49 modules and a 2-module quiet zone), which holds about
  190 bytes at error correction level L. Work out the largest version from the window's width and height, cut
  the address to fit, and say when it was cut. If even the shortest address does not fit, say "Make the window
  larger, or use Show the link".
- Draw it dark on light, in forced colours, so it scans on a dark terminal too. Show it on a view of its own:
  the title "Scan it with your phone's camera to open the report there", the code, and the menu
  (Enter Done, l Show the link).
- Plain mode never draws the code (a screen reader cannot read it): it prints the link and saves the file.
- When a step fails, offer **Report this problem** with the error already in the report.

## 7. The end

- The heading box says "Done", then a card with where to open the app (this computer, other devices) and the
  command to ask the questions again.
- The menu line is cleared, the whole window scrolls again, and the cursor is left under the last line, ready
  for the shell.

## 8. Checks before a terminal wizard ships

1. Walk every job to the end, boxed and plain, at 78 by 30 and at 60 by 20.
2. Back from every step, including after a hidden answer, keeps the answers and never shows a secret.
3. Help and feedback open and close from every step, and the step comes back as it was.
4. Plain mode: no clearing, no box characters, no QR code; a screen reader (espeakup or Orca) reads every
   question.
5. A QR code from each step scans with a phone, and the address it opens is the one shown by Show the link.
6. Nothing typed as an answer, and no secret, appears on screen, in a log or in a report.
