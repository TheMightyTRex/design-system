# Accessibility check report

Use this template for every Accessibility check (`docs/AI-CHECKS.md`). Copy it, fill in every line, and write it
to the place the owner named. Use plain English, British English, no em dashes and no contractions. Never leave a
cell empty: write Pass, Fix or Not tested.

## 1. Scope

| Item | Entry |
|---|---|
| What was checked | (pages, plug-in or design system part) |
| Date of the check | (for example 26 November 2026) |
| Commit tested | (short hash and branch) |
| Who or what ran it | (AI assistant name and model, or a person) |
| Computer, browser and versions | |
| Data used | (sample data only: say so) |
| Standard | WCAG 2.2 level AA |
| Themes and layouts tried | (Light, Dark, High contrast, High contrast dark; 175% text; 320 px) |

## 2. Summary

- Pages checked: (number)
- Pass: (number) Fix: (number) Not tested: (number)
- The three most important findings, in plain words:
  1. (finding)
  2. (finding)
  3. (finding)

## 3. The automatic base

| Tool or step | Command | Numbers (pages, problems found) | What it cannot cover |
|---|---|---|---|
| axe-core, WCAG 2.2 AA | `tools/a11y.sh` | | Meaning, order and what a person hears |
| Reading order | `ORDER=1 tools/a11y.sh` | | Whether the order makes sense for the task |
| Keyboard and Tab walk | `TASKS=1 tools/a11y.sh` | | Comfort and speed |
| Focus after actions | the walk | | Actions the walk does not do |
| Live regions | the walk | | How a real screen reader reads them |
| Layout states | 400% zoom, 175% text, wide spacing, 320 px, short window | | |

## 4. Results for each page

Make one table for each page, slide-out, dialog or wizard step. Result is Pass, Fix or Not tested.

### Page: (name and address)

| Area | Result | What was found | Fix or next step |
|---|---|---|---|
| Structure: h1, headings, landmarks, page title | | | |
| Keyboard: reach, visible focus, no trap | | | |
| Focus after each action | | | |
| Logical reading and focus order | | | |
| No needless repeats | | | |
| Names, roles and states | | | |
| Live regions say the right thing once | | | |
| Forced colours and High contrast | | | |
| Dark and reduced motion | | | |
| Zoom to 400%, text size and spacing | | | |
| Touch targets of 44 px, no gesture-only action | | | |
| Voice control: name contains the visible text | | | |
| Plain English and clear errors | | | |

## 5. Assistive technology

Status is Verified (an AI or person used it and heard the result) or Expected (the steps and wording are written
but nobody has run them) or Not tested.

| Technology | Browser | Status | What was announced | Matches the expected wording? | Needs a person? |
|---|---|---|---|---|---|
| NVDA | | | | | |
| Orca | | | | | |
| JAWS | | | | | |
| VoiceOver on Mac | | | | | |
| VoiceOver on iPhone | | | | | |
| TalkBack | | | | | |
| Narrator | | | | | |
| Keyboard only | | | | | |
| Switch access and scanning | | | | | |
| Voice control (Voice Control, Voice Access, Dragon) | | | | | |
| Magnifier and zoom | | | | | |
| Forced colours, High contrast, Dark | | | | | |
| Touch on a phone | | | | | |
| Reading and cognitive needs | | | | | |

## 6. Needless repeats found

| Where | What is said or tabbed twice | Fix |
|---|---|---|
| | | |

## 7. Fixes

| Number | Fix | Pull request | Merged by the owner |
|---|---|---|---|
| 1 | | | |

## 8. What needs a person

List each item with exact steps, so the owner can do it in about five minutes.

1. (technology, device, steps, wording to expect)

## 9. Files left behind

- (worktrees, scratch folders, reports)
