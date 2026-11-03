# Help writing guide

Version 1.0, 3 November 2026. How help is written for Storyarr and Starboard: the help centre in each
repository and any help shown inside the apps. Every word also follows `CONTENT-DESIGN.md`.

Readers may know very little about computers. Write so that someone who has never opened a terminal can
follow every step, and link to the basics for anything they might not know.

## 1. The three tiers

| Tier | Folder | What it is | Answers |
|---|---|---|---|
| 1 | `topics/` | A topic: one task, one question, one article | "How do I do this one thing?" |
| 2 | `guides/` | A guide: an ordered journey made of topics | "How do I get from nothing to this outcome?" |
| 3 | `basics/` | The basics: an idea explained from the start | "What is this, and why does it matter?" |

- **A topic covers one task.** A second task is a second topic, and the two link to each other.
- **A guide is mostly links.** Each step is one or two sentences and a link to the topic that holds the
  instructions. A guide never repeats a topic's steps, so each instruction is kept in one place. If a step
  has no topic, write the topic first.
- **Basics teach, topics and guides direct.** If a topic needs to explain what Docker is before it can give
  the steps, link to the basics article instead.

## 2. Kinds of topic

Every topic is exactly one of these. A topic that needs two kinds is two topics.

| Kind | Use it for | Title starts with |
|---|---|---|
| How-to | Doing one task | A verb: "Add an app" |
| Reference | Facts to look up: settings, limits, lists | The thing: "Display and accessibility settings" |
| Troubleshooting | One problem and its fix | The problem in the reader's words: "Starboard does not open" |
| Overview | A hub that routes onwards within one area | The area: "Backup and restore" |

## 3. Categories on the help home

Each app's help home (`README.md` in its help folder) lists the guides first, then the topics grouped by
area, then the basics. Areas follow the order someone meets them:

1. **Before you install**
2. **Install and update**
3. The app's own areas, in the order of its main menu (Starboard: Apps, Everyday use, Your server, Alerts,
   Security, Backup and restore; Storyarr: My library, Following, Discover, Activity, Sources, Download
   clients)
4. **Settings**
5. **When something is wrong**

Every topic sits in one area. A topic that fits two areas belongs to the one the reader would try first.

## 4. Topic layout (tier 1)

```
[Help centre](../README.md) · <Area>

# <The task, in the reader's words>

<Kind: how-to, reference or troubleshooting>

One or two sentences: what this does and what you will have at the end. The answer comes first.

## Before you begin          (omit when there is nothing)
- What must be true or to hand, each with a link to the topic that sets it up.

## When would you use it     (reference topics only)
- Real situations, each starting "You want to…" or "You need to…".

## Steps
1. One action per step, with the on-screen label in bold: Select **Add an app**.
2. Commands in a fenced `bash` block of their own, one command per block.
3. Say what happens after a step when it is not obvious: "Starboard shows the setup code."

## Things to note            (omit when there is nothing)
## If it does not work       (omit when there is nothing)
## Find out more
- Links to related topics, guides and basics, and to the topic's parent.
```

Empty sections are left out, never padded. "Find out more" points onwards; it never sums up the topic.

## 5. Guide layout (tier 2)

```
[Help centre](../README.md) · Guides

# <The outcome, in the reader's words>

Who this is for, what you will have at the end, and about how long it takes.

## Before you begin
## The steps at a glance       (a numbered list, then a flowchart of the same steps)
## Step 1: <short name>        (one or two sentences, the link to the topic, and how you know it worked)
## What next
```

Name a guide after the goal ("Move from Plex to Jellyfin"), not after a feature. State what each step
depends on, so the order is clear. The flowchart has alt text that lists the same steps in words.

## 6. Basics layout (tier 3)

```
[Help centre](../README.md) · The basics

# <What X is>

The idea in two or three sentences, with an everyday comparison where one helps.

## <A few short sections that build the idea up>
## What this means for <app>
## Find out more
```

## 7. Rules for help

1. **Titles in the reader's words,** with the word they would search for: "Set up two-step sign-in with an
   authenticator app".
2. **Other names once, near the top:** "two-step sign-in, also called 2FA or two-factor authentication".
   Search and screen readers both use them.
3. **Every child links to its parent,** and each topic links to its nearest neighbours under "Find out more".
4. **Commands are copied, not typed.** Put each command in its own `bash` block, and say what it does in the
   sentence before it. Mark anything the reader must change, such as `<your server>`, and say what to put
   there.
5. **One action per step,** starting with the verb. Start from a page the reader can find, and give the full
   path the first time (`CONTENT-DESIGN.md` rule 2.19).
6. **Callouts by meaning** (`CONTENT-DESIGN.md` section 7): "Before you begin:", "Limitation:", "Warning:",
   "Tip:", "Example:". Never a callout without its lead word.

## 8. Screenshots

- Add one only after a step where the control might be hard to find. Leave obvious steps as text.
- Everything a screenshot shows is also said in words (rule 2.20).
- Take them from a preview with made-up data (rule 2.23), never from a real server.
- **Annotating:** a box drawn just outside the control, in the danger colour, with a curved arrow whose head
  touches the box. Never cover the label you are pointing at.
- Alt text names the page and the control by its label: "The Apps page, with Add an app outlined". Never
  "the button in the bottom right".

## 9. Getting AI to write instructions

An AI assistant can draft help, release notes and on-screen words well, but only from facts it is given.
Left alone it fills gaps with what sounds likely: labels that do not exist, steps in the wrong order, and
the words this guide bans. Treat its draft as a first draft that you check.

### What to give it

- **This guide and `CONTENT-DESIGN.md`,** to read in full before it writes anything.
- **The facts:** the app's code or its running pages, so labels come from the app, not from memory. For a
  change, the commit or the release notes behind it.
- **The reader and the job:** who it is for, which tier (topic, guide or basics) and which kind of topic.
- **What already exists:** the help home and the nearest topics, so it links to them instead of repeating
  them, and does not write a second topic for the same task.

### What it must do

1. **Read the rules first,** then say which tier and kind it is writing.
2. **Copy every on-screen label exactly** from the code or the running app, in bold inside steps.
3. **Never invent behaviour, labels, limits or permissions.** Where it is unsure, it writes
   `[needs checking: …]` in the draft and carries on, rather than guessing.
4. **Use made-up example data only** (`CONTENT-DESIGN.md` rule 2.23).
5. **Link, do not repeat.** A step that has its own topic links to it. A missing topic is reported as a gap,
   not written inline.
6. **Change only what was asked.** When editing, keep the article's existing sections and links, and do not
   rewrite the voice while fixing one fact.
7. **Report back:** what it wrote, every `[needs checking]`, any label it left as it is because the app
   shows it that way, and anything wrong it noticed but did not fix.

### How to check its work

| Check | How |
|---|---|
| Banned words and punctuation | Run the sweep below. Fix every hit, or confirm it is an on-screen label. "See" is the one that slips through most, inside friendly sentences ("so you can see what is left"). |
| Labels | Open the page in the app and compare every bold label, letter for letter. |
| Steps | Follow the steps on a test install or a preview, from the starting page the topic names. A step you cannot follow is wrong. |
| Facts | Every number, limit, default and version matches the code or the release notes. Clear every `[needs checking]`. |
| Links | Every link opens the right article; the parent and related articles are linked. |
| Structure | Right tier, one kind, headings in order, empty sections left out (section 10 checklist). |
| Privacy | `tools/check-private.sh` passes: no real names, addresses, keys or server names. |

**The sweep**, run on the draft (it lists lines to read, not lines that are always wrong):

```bash
grep -nE "—|\b(can't|don't|won't|it's|isn't|doesn't|you're|we're|what's|that's|you'll)\b" draft.md
grep -niE "\b(click|tap|see|sees|look|looks|enable[ds]?|disable[ds]?|toggle|turn (on|off)|screen)\b" draft.md
grep -niE "\b(simple|simply|easy|just|straightforward|obviously|complex|difficult|advanced)\b" draft.md
grep -niE "\b(above|below|top right|on the left|on the right|scroll down|click here|read more|learn more)\b|!" draft.md
```

A tool reporting success is not the check: read the result back, in the file and on the page.

### A prompt to start with

```text
Write a help topic for <app>: "<task in the reader's words>".
First read docs/HELP-WRITING.md and docs/CONTENT-DESIGN.md in the design system, in full.
Take every on-screen label from <path to the page's code, or the running app>; copy them exactly.
Never invent behaviour, labels or limits: write [needs checking: ...] instead and carry on.
Use made-up example data only. Link to existing topics in <help folder> instead of repeating them.
When you finish, run the sweep in HELP-WRITING.md section 9 on your draft and fix every hit.
Then tell me: the tier and kind, every [needs checking], labels left as the app shows them, and any gaps.
```

## 10. Checklist before a help change is finished

- [ ] The article is in the right tier, and a topic has exactly one kind
- [ ] Title in the reader's words; other names given once near the top
- [ ] The answer comes first; empty sections left out
- [ ] A guide links to topics instead of repeating their steps
- [ ] Links to the parent and to related articles under "Find out more"
- [ ] Screenshots only where needed, described in words, with made-up data
- [ ] Everything in the `CONTENT-DESIGN.md` checklist
