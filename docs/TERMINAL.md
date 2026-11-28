# Terminal wizards: the rules

5 November 2026. The same jobs as `WIZARD.md`, for a wizard that runs in a terminal. That means a server with no
desktop, reached over SSH, with no browser to finish in. Starboard's `./install.sh --terminal` is the first one.

Every rule in `WIZARD.md` about questions, words and help still applies. This guide says how each appears in a
terminal.

## 1. Two ways to draw it, one set of words

- **Boxed** is the default in a terminal at least 60 characters wide and 20 lines tall. Each step starts on a cleared
  screen, with a heading box, a progress bar and a menu fixed on the bottom line.
- **Plain** applies with an `APP_PLAIN=1` setting such as `STARBOARD_PLAIN=1`, a `--plain` option, a smaller window,
  `TERM=dumb`, or output that is not a terminal. It gives numbered lines that scroll, with nothing cleared, redrawn or
  drawn over. Screen readers lose their place when a screen is redrawn, and they read box characters aloud. So plain
  mode is the one for them.

  Say how to choose it in the help.
- Both ask the same questions in the same order, with the same answers. Only the drawing changes.
- **The browser set-up too.** The terminal wizard asks the same questions, in the same order, with the same
  answers and help as the app's browser wizard. A change to one is made to the other in the same change
  (`WIZARD.md` section 2, One wizard, two ways to show it).
- `NO_COLOR` keeps the boxes and drops the colour.

## 2. Fit the window, and keep the frame in place

- **The frame never moves.** The heading box and the progress bar stay at the top, and the menu stays on the bottom
  two lines, at all times. Only the lines between them scroll (a scrolling area set between the two). A long list,
  a card or a message never pushes the heading or the menu out of view.
- **Measure the window at every step,** and again when it changes size (SIGWINCH). Draw the step again to fit. Draw
  the frame, then the step's last lines, then the question that is waiting, so the person can carry on entering the
  answer.
- **A column, centred.** The frame, text and menu sit in a column at most 100 characters wide. In a wider window the
  column is centred, with equal space either side; at 60 to 100 columns it is the whole window. The column is worked
  out again at every step and every change of size, and the waiting question moves with it.
- **Text wraps between words** at the column's width, and is wrapped again when the window changes size, never cut
  mid-word.
- **Under 60 columns or 20 lines,** use the plain way (section 1).
- **A long list in a short window** shows what fits, then "4 more: press m to show them".

## 3. The heading box

- One line in a box: the app's name in bold, a dim `|`, then the step's name, and `step 2 of 5` on the right:
  `Starboard | Your media server`.
- Under it, a progress bar the width of the box, and the percentage done.
- The box and the bar are the column's full width (at most 100 characters), and every line ends at the same column.

## 4. Questions

- One question at a time, numbered answers, the recommended one first, marked with a dot and the word
  "(recommended)". Colour never carries the meaning on its own.
- The default is in brackets, and Enter takes it: `› Your choice [1]:`.
- **Several answers at once:** in the boxed way, a list with `[x]` and `[ ]`. Up and Down move, Space ticks or
  unticks, Enter carries on, and a line under the list says so. Entering a number ticks that line too. The list is
  drawn in place, never repeated.

  In plain mode (screen readers), you enter the numbers with commas: `1,2,7`.
- **A job's progress:** one line, drawn in place and cut to the column. On a failure the line stays, marked, and the
  problem and its choices go under it (`WIZARD.md` section 5, A job's progress). The line reads the job, which job of
  how many, what it is doing now and the timer. It then says how far the job has got, when it can tell ("· 5 of 12
  installed", then "· 9 of 12 running").
- **A long job in plain mode is never silent.** It writes a line when it starts, "Still working: the job (12 min)"
  every 2 minutes while it runs, and "Done" or "Did not finish" at the end. Each "Still working" line says how far the
  job has got, when it can tell. A screen reader user then knows it has not stopped. Never write more often than every
  2 minutes, because each line is read aloud.
- **An optional question says "(optional)"** after its words, as the browser's does (`WIZARD.md` section 3), and offers
  `s` to skip it. A question that needs an answer has no skip. Never an asterisk.
- **Check your answers (28 November 2026, `WIZARD.md` section 10).** Before anything is written, the terminal shows the same
  page as the browser: the heading "Check your answers", one numbered line for each answer (the question, then the
  answer), and a menu line "Enter writes it  ·  1 to 9 changes that answer  ·  b goes back". Entering a number asks that
  one question again, with its answer ready to keep, and then returns to Check your answers. The last line names
  what Enter does ("Enter writes the files"). In a Run again, only what changes is listed, each with "Was" and "Now".
- **Errors are plain lines under the question**, in the app's own words (`WIZARD.md` section 11), after the heading line
  "There is a problem". The question is asked again with the answer kept.
- **Progress stays.** The heading box shows the step count in every terminal wizard (`WIZARD.md`, section 15, owner
  decision, 28 November 2026). Back stays on `b`, as before.
- A long list on a short screen shows what fits, then "4 more: press m to show them".
- Passwords and keys are entered hidden: say "(nothing appears as you enter it)". After Back, Enter keeps the one
  entered before, without showing it.
- An answer the app refuses is explained on the next line in the app's own words, and the question is asked
  again. Refused again, the message and the question replace the last ones in place: the step never fills with
  the same two lines.
- A question with no default (the person's own service, such as their VPN provider) shows "Your choice:" with no
  brackets. The menu does not say what Enter does, and Enter alone says "Choose one: enter a number from 1 to 7".
- A question longer than the column wraps between words, its first lines first, so the line the answer is
  entered on fits. An address is never cut: it may run past the edge so it copies whole.
- Keys pressed show only while a question waits. Keys pressed between questions (Enter pressed twice, say) would
  otherwise move the lines the step writes next. A line entered ahead like that is shown after the next question,
  as if entered there.
- A password is not a question of choice: run with `--yes` in a real window, the script still asks for it there,
  rather than stopping.

## 5. The menu on the bottom line

- Always the keys that work on this step, then what Enter does on the right:
  `b Back   ? Help   f Feedback   q Stop        Enter: recommended`.
- **b Back** goes back one step, with the last answers as the defaults. The right side says "Enter: keep", and the
  step says "You came back to this step". Back stops at the step that changed something. Once files are written, you
  change earlier answers in the app's settings instead.
- **? Help** opens help as a box over the step (section 6).
- **f Feedback** opens the feedback flow (section 7).
- **q Stop** stops with nothing else changed, and says how to carry on later.
- In plain mode there is no menu bar. Each step's first line says "Press b to go back, ? for help, f to send feedback
  or q to stop".

## 6. Help as a box over the step

- The step behind is dimmed. The box sits in the middle with "Help: " and the question as its title, and the bottom
  line says "Enter Close help".
- Long help shows a page at a time ("Enter: show more"; the menu says "Enter Show more").
- Closing it draws the step again exactly as it was, with the cursor at the question.
- Plain mode prints the help under the question instead.

## 7. Feedback, sent with a QR code

The terminal version of Snaglist ("Feedback in a wizard" in `WIZARD.md`):

1. The kind, numbered, as Snaglist offers them. They are Something is broken, Confusing to use, Words are wrong, Hard
   to use with my tools or needs, A new feature, Make something better and Something else.
2. One or two questions, the same as Snaglist asks.
3. The whole report, before anything leaves the machine.
4. How to send it: **Show as a QR code** (recommended), Show the link, Save to a file, or Cancel.

- The report keeps Snaglist's rules. It holds the step and the app's version, the operating system and processor type,
  and the last error if there was one. It never holds an answer, a password, a key or a set-up code. It replaces email
  addresses, network addresses, user names in paths and anything like a key.
- **The QR code** holds a short pre-filled new-issue address. The address has the kind, the step, the person's words
  cut to fit, and the version and system on one line. The whole report is saved on the server at the same time, and
  the issue says where.
- **It fits the window, and a larger window holds more.** Half-block characters draw two rows of the code on each
  line, so the code's width is its number of modules and its height is half that. Use every line but the title line
  and the two menu lines. Work out the largest version from the window's width and height.

  Use the standard 4-module quiet zone, or a 2-module one (which phones still read) when the window is small. Then put
  in as much of the report as that version holds at error correction level L, from the most to the least:

  | Tier | What it holds | Usual window |
  |---|---|---|
  | 1 | The report without its technical details | 140 by 60 and larger (version 22, about 1,000 bytes) |
  | 2 | A short report: the kind, the step and the person's words cut to fit | 80 by 30 to 80 by 40 (version 8 to 12) |
  | 3 | The step, the version and where the whole report is saved | in between |
  | 4 | The title alone | 80 by 24, the usual SSH window (version 5, 2-module edge, about 100 bytes) |

  The line before the code says which ("It holds a short report"); if there is no room there, the link's view
  says it. The whole report is always saved on the server. If not even the title fits, say "Make the window
  larger, or use Show the link".
- Draw it dark on light, in forced colours, so it scans on a dark terminal too. Show it on a view of its own. The view
  has the title "Scan it with your phone's camera to open the report there", the code, and the menu (Enter Done, l
  Show the link).
- Plain mode never draws the code (a screen reader cannot read it): it prints the link and saves the file.
- When a step fails, offer **Report this problem** with the error already in the report.

### How the QR code is made

The code is `terminal/qr.py` (standard library only, every QR version, levels L and M); Starboard's terminal
set-up (`starboard/terminal_setup.py`, `qr_fit` and `_show_qr`) is the worked example. In order:

1. **Save the whole report first**, on the computer, so the short one in the code can say where it is.
2. **Measure the room:** the window's lines less three (the title line and the two menu lines), and its columns.
3. **Find the largest code that fits:** `qr.largest_version(columns, lines, quiet)`, first with the standard 4-module
   quiet zone, then with a 2-module one. Two module rows go on each line (half blocks). So a code of *n* modules is
   *n* columns wide and *n*/2 lines high, plus the quiet zone. Keep the 4-module edge, unless it leaves room for less
   than about 180 bytes and the 2-module edge allows a larger code.
4. **Fill it from the most to the least:** the room is `qr.byte_capacity(version, "L")`, at most 1,200 bytes, because
   larger codes are hard to scan off a screen. Try these in order:
   - the pre-filled new-issue address with the report without its technical details
   - shorter reports, with the person's words cut to 300, 200, 140, 90 and 50 characters
   - the step, the version and where the whole report is saved
   - the title alone

   Take the first that fits.
5. **Encode and draw:** `code = qr.encode(address, largest=version)`, then `qr.draw(code, quiet=edge)` gives the
   lines, dark on light with the colours forced. Centre it.
6. **Show it on a page of its own.** It has the title line "Scan it with your phone's camera to open the report
   there". Beside it, when it fits, it says what the code holds ("It holds a short report. The whole report is in …").
   Then come the code, the link under it when there is room, and the menu, Enter Done and l Show the link.
7. **When nothing fits,** show the link with "The QR code does not fit this window. Make the window larger, or use
   Show the link". Plain mode never draws a code: it prints the link and saves the file.

The address is a GitHub new-issue link (`https://github.com/<owner>/<repo>/issues/new?title=…&body=…&labels=…`) with
every part URL-encoded. A phone opens the report ready to send, already saying the app, its version, the system and
the step. Before the app itself is on the computer (a Run first script's first steps), the frame's own feedback shows
that link without a code (`terminal-frame.sh`, `feedback`).

In the browser, Snaglist offers the same choice, Show as a QR code (`WIZARD.md`, section 12), using the same
address and the same order of what goes in.

### When it stops

- Every way a script can stop has an error number, such as `RF-11` or `IN-21`, explained on one help page. The last
  lines say why it stopped. Then come "Error IN-21. What it means and how to fix it:" and the address of that number's
  help on a line of its own, so it is never cut and copies whole.
- When one job does not finish, the job's line stays, marked, and the choices go under it. First come the problem, its
  error number and the address of its help on a line of its own, the same in the boxed frame and in plain lines. Then
  come Try again (recommended), Show the details, Carry on without it (when the rest can), Report this problem and
  Stop.
- When one script runs another (a Run first script runs the app's installer) and the inner one stops with its own
  error number, the outer one ends on that number and its address, never on a second number of its own. The outer
  one's own number is only for a stop the inner one gave no number for. A person's own stop (q or Ctrl+C) is not an
  error and has no number. The frame writes "stopped" to STOP_FILE so the outer script can tell.

## 8. The end

- The heading box says "Done". A card then says where to open the app (this computer, other devices) and gives the
  command to ask the questions again.
- The menu line is cleared, the whole window scrolls again, and the cursor is left under the last line, ready
  for the shell.

## 9. A run first script: the one thing to launch

After the operating system is installed, a person launches one script and everything else is set up for them.
Starboard's `run-first.sh` (the "Run first script") is the first one.

- **One command,** shown first in the README and the help: `curl -fsSL …/run-first.sh | bash`. Show the careful
  way too (download, read, run) and a `--check` option that only reports.
- **Ask about the layout first, in plain words, before anything is drawn:** "Press Enter to start, or press a for
  accessible mode". Software that reads text aloud must be able to read that line. Accessible mode is the plain way
  (section 1). The script passes it on to everything it starts (`--plain`), so it holds for the whole installation.
- **The same frame as the wizard it starts:** heading box, progress bar, menu, help over the step. The first step
  is a welcome with the app's logo (The logo in a terminal, in this section) and what will happen.
- **Check, then ask, then change.** List what is there and what is missing, with a tick or a cross and the word,
  changing nothing. Then show the exact commands and ask once before running them. Install only what is missing,
  and never run as root by itself: sudo asks for the password, and the script never types or keeps it.
- **Choose the next wizard for the computer.** With a desktop, recommend the browser wizard and open it at the end.
  Fill in any one-time code from the address (after `#`, so it never reaches the server's log). With no desktop,
  recommend the terminal wizard. Always offer the other one.
- **Safe to run again:** a second run finds everything in place, says so, and updates rather than downloads again.
- **Answers come from the terminal** (`/dev/tty`), so it works when the script arrives through a pipe.

### The logo in a terminal

- Draw it with block characters (`█ ▀ ▄`, two pixels a character), about 20 characters wide and 10 lines tall, beside
  the welcome text. Use the logo's two colours, as 256-colour codes close to the tokens.
- Only in the boxed way. Plain mode and screen readers get the app's name in words, never the blocks.
- With `NO_COLOR` the shape stays, in the terminal's own colour.

## 10. Checks before a terminal wizard ships

1. Walk every job to the end, boxed and plain, at 80 by 24, 80 by 30, 140 by 60 and 60 by 20. Change the window's size
   in the middle of a step. The heading, the bar and the menu stay in place.
2. Back from every step, including after a hidden answer, keeps the answers and never shows a secret. Change on Check
   your answers returns to Check your answers, not through every step in between.
3. Help and feedback open and close from every step, and the step comes back as it was.
4. Plain mode: no clearing, no box characters, no QR code; a screen reader (espeakup or Orca) reads every
   question.
5. A QR code from each step scans with a phone, and the address it opens is the one shown by Show the link.
6. No answer, and no secret, appears on screen, in a log or in a report.
7. A run first script: on a bare system with nothing installed, and again with everything installed, in a
   throwaway virtual machine for each supported system.

## Choosing a folder

16 November 2026 (TheMightyTRexUK, Idea A). The same picker as the browser's, drawn as numbered lists:

1. **Places first:** a numbered list of This computer, each disk, and each network share where the step brings
   things in from them. A cloud service says it needs the browser to sign in.
2. **Then the folders:** the path first (`Where you are: Disk 2 / Video`), then `1. Use this folder`. Then comes one
   line for each folder with its size and what is in it (`2. Films (1.9 TB, 412 films)`), and `b` to go back a level
   (from the top of a place, back to the places). Enter takes Use this folder.
3. A long list pages as every other list does. The words are the browser's.
