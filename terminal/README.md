# Terminal

The code behind `docs/TERMINAL.md`, shared by every app's terminal scripts. `tools/sync.py` copies it into the
apps: change it here, never in the copies.

| File | What it is | Starboard's copy |
|---|---|---|
| `terminal-frame.sh` | The frame for a bash wizard: the heading box and progress bar, the menu on the bottom lines, questions with numbered answers, help boxes, one bar per job with its timer and count, cards, feedback, plain mode for screen readers, and redrawing when the window changes size | `lib/terminal-frame.sh`, and a copy inside `run-first.sh` between its `terminal-frame` lines (that script arrives on its own through curl) |
| `qr.py` | A QR code encoder in the Python standard library, for feedback sent to a phone (`TERMINAL.md`, section 7) | `starboard/qr.py` |

## Using the frame

A script sets these, then sources `terminal-frame.sh`:

- `APP_NAME` (shown in the heading box), `APP_VERSION`, and `ISSUES`, the GitHub repository for the feedback link
  (`owner/name`).
- `IN`, the terminal to read answers from (empty when there is none), `PLAIN` (1 for plain lines), `LOG` (the
  file the jobs' output goes to), and an `err` function.
- `STEPS` and `TITLES` (each step's name), and `FIRST_BACK` when Back should start later than step 1.
- `app_feedback`, a function, when the app has its own feedback flow; it returns non-zero when it cannot run yet,
  and the frame then shows the feedback link.

Then each step calls `header "Title" n`, writes with `para`, `say`, `ok`, `bad` and `note`, and asks with `ask`
or `choose "Question" default "help" "Answer|about" …` (the answer is in `CHOICE`). A job runs with
`work "What it does" command n of` (one bar, drawn in place); set `JOB_DETAIL` or `JOB_COUNT` to the name of a
function that prints what it is doing now or how far it has got. When one fails, `job_failed name why tip code`
offers Try again, Show the details, Report this problem and Stop. Starboard's `install.sh` wraps `work` in its own
`job` function, which counts the jobs. `card` and `card_row` draw the end card.

## The QR code

```python
import qr
code = qr.encode("https://github.com/owner/repo/issues/new?title=…", largest=qr.largest_version(80, 21, 2))
print("\n".join(qr.draw(code, quiet=2)))
```

`TERMINAL.md`, section 7, How the QR code is made, gives the order of what goes in and how it is shown.
