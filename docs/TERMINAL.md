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
- **The browser set-up too.** The terminal wizard asks the same questions, in the same order, with the same
  answers and help as the app's browser wizard. A change to one is made to the other in the same change
  (`WIZARD.md` section 2, One wizard, two ways to show it).
- `NO_COLOR` keeps the boxes and drops the colour.

## 2. Fit the window, and keep the frame in place

- **The frame never moves.** The heading box and the progress bar stay at the top, and the menu stays on the bottom
  two lines, at all times. Only the lines between them scroll (a scrolling area set between the two). A long list,
  a card or a message never pushes the heading or the menu out of view.
- **Measure the window at every step,** and again when it changes size (SIGWINCH). Draw the step again to fit: the
  frame, then the step's last lines, then the question that is waiting, so the person can carry on typing.
- **A column, centred.** The frame, text and menu sit in a column at most 100 characters wide. In a wider window the
  column is centred, with equal space either side; at 60 to 100 columns it is the whole window. The column is worked
  out again at every step and every change of size, and the waiting question moves with it.
- **Text wraps between words** at the column's width, and is wrapped again when the window changes size, never cut
  mid-word.
- **Below 60 columns or 20 lines,** use the plain way (section 1).
- **A long list in a short window** shows what fits, then "4 more: type m to see them".

## 3. The heading box

- One line in a box: the app's name in bold, a dim `|`, then the step's name, and `step 2 of 5` on the right:
  `Starboard | Your media server`.
- Below it, a progress bar the width of the box, and the percentage done.
- The box and the bar are the column's full width (at most 100 characters), and every line ends at the same column.

## 4. Questions

- One question at a time, numbered answers, the recommended one first, marked with a dot and the word
  "(recommended)". Colour never carries the meaning on its own.
- The default is in brackets, and Enter takes it: `› Your choice [1]:`.
- **Several answers at once:** in the boxed way, a list with `[x]` and `[ ]`: Up and Down move, Space ticks or
  unticks, Enter carries on, and a line under the list says so. Typing a number ticks that line too. The list is
  drawn in place, never repeated. In plain mode (screen readers), the numbers are typed with commas: `1,2,7`.
- **A job's progress:** one line, drawn in place and cut to the column; on a failure it stays, marked, and the
  problem and its choices go below it (`WIZARD.md` section 5, A job's progress).
- A long list on a short screen shows what fits, then "4 more: type m to see them".
- Passwords and keys are typed hidden: say "(nothing shows as you type)". After Back, Enter keeps the one typed
  before, without showing it.
- An answer the app refuses is explained on the next line in the app's own words, and the question is asked
  again.

## 5. The menu on the bottom line

- Always the keys that work on this step, then what Enter does on the right:
  `b Back   ? Help   f Feedback   q Stop        Enter: recommended`.
- **b Back** goes back one step, with the last answers as the defaults (the right side says "Enter: keep", and
  the step says "You came back to this step"). Back stops at the step that changed something: once files are
  written, earlier answers are changed in the app's settings instead.
- **? Help** opens help as a box over the step (section 6).
- **f Feedback** opens the feedback flow (section 7).
- **q Stop** stops with nothing else changed, and says how to carry on later.
- In plain mode there is no menu bar: each step's first line says "Type b to go back, ? for help, f to send
  feedback or q to stop".

## 6. Help as a box over the step

- The step behind is dimmed, the box sits in the middle with "Help: " and the question as its title, and the
  bottom line says "Enter Close help".
- Long help shows a page at a time ("Enter: more below").
- Closing it draws the step again exactly as it was, with the cursor at the question.
- Plain mode prints the help under the question instead.

## 7. Feedback, sent with a QR code

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
- **It fits the window, and a larger window holds more.** Half-block characters draw two rows of the code on
  each line, so the code's width is its number of modules and its height is half that. Use every line but the
  title line and the two menu lines. Work out the largest version from the window's width and height, with the
  standard 4-module quiet zone, or a 2-module one (which phones still read) when the window is small. Then put
  in as much of the report as that version holds at error correction level L, from the most to the least:

  | Tier | What it holds | Usual window |
  |---|---|---|
  | 1 | The report without its technical details | 140 by 60 and larger (version 22, about 1,000 bytes) |
  | 2 | A short report: the kind, the step and the person's words cut to fit | 80 by 30 to 80 by 40 (version 8 to 12) |
  | 3 | The step, the version and where the whole report is saved | in between |
  | 4 | The title alone | 80 by 24, the usual SSH window (version 5, 2-module edge, about 100 bytes) |

  The line above the code says which ("It holds a short report"); if there is no room there, the link's view
  says it. The whole report is always saved on the server. If not even the title fits, say "Make the window
  larger, or use Show the link".
- Draw it dark on light, in forced colours, so it scans on a dark terminal too. Show it on a view of its own:
  the title "Scan it with your phone's camera to open the report there", the code, and the menu
  (Enter Done, l Show the link).
- Plain mode never draws the code (a screen reader cannot read it): it prints the link and saves the file.
- When a step fails, offer **Report this problem** with the error already in the report.

## 8. The end

- The heading box says "Done", then a card with where to open the app (this computer, other devices) and the
  command to ask the questions again.
- The menu line is cleared, the whole window scrolls again, and the cursor is left under the last line, ready
  for the shell.

## 9. A run first script: the one thing to launch

After the operating system is installed, a person launches one script and everything else is set up for them.
Starboard's `run-first.sh` (the "Run first script") is the first one.

- **One command,** shown first in the README and the help: `curl -fsSL …/run-first.sh | bash`. Show the careful
  way too (download, read, run) and a `--check` option that only reports.
- **Ask about the look first, in plain words, before anything is drawn:** "Press Enter to start, or type a for
  accessible mode". Software that reads text aloud must be able to read that line. Accessible mode is the plain
  way (section 1), and it is passed on to everything the script starts (`--plain`), so it holds for the whole
  installation.
- **The same frame as the wizard it starts:** heading box, progress bar, menu, help over the step. The first step
  is a welcome with the app's logo (below) and what will happen.
- **Check, then ask, then change.** List what is there and what is missing, with a tick or a cross and the word,
  changing nothing. Then show the exact commands and ask once before running them. Install only what is missing,
  and never run as root by itself: sudo asks for the password, and the script never types or keeps it.
- **Choose the next wizard for the computer.** With a desktop, recommend the browser wizard and open it at the end,
  with any one-time code filled in from the address (after `#`, so it never reaches the server's log). With no
  desktop, recommend the terminal wizard. Always offer the other one.
- **Safe to run again:** a second run finds everything in place, says so, and updates rather than downloads again.
- **Answers come from the terminal** (`/dev/tty`), so it works when the script arrives through a pipe.

### The logo in a terminal

- Draw it with block characters (`█ ▀ ▄`, two pixels a character), about 20 characters wide and 10 lines tall,
  beside the welcome text, in the logo's two colours (256-colour codes close to the tokens).
- Only in the boxed way. Plain mode and screen readers get the app's name in words, never the blocks.
- With `NO_COLOR` the shape stays, in the terminal's own colour.

## 10. Checks before a terminal wizard ships

1. Walk every job to the end, boxed and plain, at 80 by 24, 80 by 30, 140 by 60 and 60 by 20, and change the
   window's size in the middle of a step: the heading, the bar and the menu stay in place.
2. Back from every step, including after a hidden answer, keeps the answers and never shows a secret.
3. Help and feedback open and close from every step, and the step comes back as it was.
4. Plain mode: no clearing, no box characters, no QR code; a screen reader (espeakup or Orca) reads every
   question.
5. A QR code from each step scans with a phone, and the address it opens is the one shown by Show the link.
6. Nothing typed as an answer, and no secret, appears on screen, in a log or in a report.
7. A run first script: on a bare system with nothing installed, and again with everything installed, in a
   throwaway virtual machine for each supported system.
