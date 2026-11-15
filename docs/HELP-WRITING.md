# Help writing guide

Version 1.2, 14 November 2026. How help is written for every help centre (Starboard, Snaglist, the plug-in
collection and any later one) and any help shown inside the apps. Section 11 is the help centre standard: the
layout, the menus, flow charts, the journey, the problem solver and plug-in mode. Every word also follows `CONTENT-DESIGN.md`.

## About this guide

### What it is for

Help answers the question someone has at the moment they have it. This guide sets out how that help is
organised and laid out, so every app's help centre works in the same way: the same three tiers, the same
kinds of topic, the same layouts and the same checks. Someone who has used one help centre already
knows how the next one is organised.

Readers may know very little about computers. Write so that someone who has never opened a terminal can
follow every step, and link to the basics for anything they might not know.

### Who it is for

Anyone who writes or checks help: the help centre in an app's repository, help shown inside an app, and
README files that teach. That includes AI assistants: section 9 says what to give one and how to check what
it writes. It is public, so you may also use it for your own projects under the guide licence (CC BY 4.0).

### How to use it

1. Choose the tier (section 1): a topic, a guide or the basics.
2. For a topic, choose its one kind (section 2) and the area it belongs to (section 3).
3. Copy the layout for that tier (sections 4 to 6) and write to the rules in section 7.
4. Add screenshots only where section 8 says they help.
5. Before you finish, go through the checklist in section 10 and the one in `CONTENT-DESIGN.md`.

Working examples: the [Starboard help centre](https://github.com/TheMightyTRex/starboard/blob/main/docs/help/README.md)
and the [Snaglist help centre](https://github.com/TheMightyTRex/snaglist/blob/main/docs/README.md). The gallery,
the tools and the other guides are listed in
[Design resources and tools](https://themightytrex.github.io/design-system/resources/).

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

## 3. Areas and groups

Every help centre has the same seven main items, in this order: **Home**, **Get started**, **Use it**,
**Plug-ins**, **Accessibility**, **Fix a problem** and **Developers** (section 11). Each of the six areas holds a
few groups, named in the reader's words (Starboard's Use it: Dashboard, Apps, Library and downloads, Your server,
Alerts, Security, Backups, Updates), and every article sits in exactly one group. An article that fits two groups
belongs to the one the reader would try first. An area with nothing in it says so in one line, such as "Snaglist has
no plug-ins".

- **Get started:** before installing, installing, opening it on other devices, moving in.
- **Use it:** the app's own areas, in the order of its main menu, then settings, backups and updates.
- **Plug-ins:** adding and looking after plug-ins; in a plug-in collection, every plug-in (section 11.7).
- **Accessibility:** the display settings, ways to use it, how it is tested and its limits.
- **Fix a problem:** troubleshooting topics, each one flow chart first, and the problem solver.
- **Developers:** plug-in writing, the API, prompts for AI assistants, security and tests.

The tiers (section 1) still decide the folder and the layout; the area and group decide where an article is listed.

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
## The steps at a glance       (a numbered list, then a flow chart of the same steps)
## Step 1: <short name>        (one or two sentences, the link to the topic, and how you know it worked)
## What next
```

Name a guide after the goal ("Move from Plex to Jellyfin"), not after a feature. State what each step
depends on, so the order is clear. The flow chart (section 11.4) is drawn with the same steps written out in words.

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
   **Some people type them anyway,** so a command with a symbol that moves between keyboards (`|`, `~`, `\`,
   `"`, `@`, `$`, `&`) links to the app's keyboard help (US, UK and Ireland, German, French and Spanish), and a
   one-line command with `|` also shows a version without it. On UK keyboards the `¦` key is not `|`: say so.
5. **One action per step,** starting with the verb. Start from a page the reader can find, and give the full
   path the first time (`CONTENT-DESIGN.md` rule 2.19).
6. **Callouts by meaning** (`CONTENT-DESIGN.md` section 7): "Before you begin:", "Limitation:", "Warning:",
   "Tip:", "Example:". Never a callout without its lead word.

## 8. Screenshots

The full rules, for people and AI tools, are in `SCREENSHOTS.md`, with a mark-up helper in `tools/annotate.js`.
In short:

- Add one only for a step the reader could not follow from the words. There is no quota.
- Everything a screenshot shows is also said in words (rule 2.20). Text descriptions follow `ALT-TEXT.md`.
- Take them from a preview with made-up data (rule 2.23), never from a real server; never fake one.
- **Marking up:** a red outline 5 pixels outside the control, a curved arrow whose filled head touches it, at
  most three outlines, each with a badge carrying its step's number in the article.
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
- [ ] Screenshots only where needed, described in words, with made-up data, marked up to `SCREENSHOTS.md`
- [ ] The article has its `<!-- help: <area> / <group> -->` line, and the group is in `help-centre.json`
- [ ] A troubleshooting topic or a guide starts with its flow chart; every numbered answer has its section
- [ ] The help centre builds with no warnings (`build.py --strict`)
- [ ] Everything in the `CONTENT-DESIGN.md` checklist

## 11. The help centre standard

Chosen by the owner on 14 November 2026 (Starboard DASH-436): "I also want this design to become the standard.
This is to be used in all help centres." Every help centre is built by the design system's builder,
`tools/help_centre/build.py`, from the Markdown in the app's repository and one `help-centre.json`. Nothing here is
drawn by hand per build: change the Markdown or the settings, and build again. The pieces are components in
`components.css` and `components.js`, shown in the gallery, so an app can use them too.

### 11.1 Layout

- **Top bar:** the help centre's name, then the seven main items as quick links (`.top-links`), then **Search** and
  **Display**. The area you are in is marked. On tablets and phones the seven items move into the side menu and the
  bar keeps **Menu**, **Search** and **Display**.
- **A hub on every page:** the side menu on the left, the page on the right. Articles keep **On this page** beside
  them on wide screens, inside them on narrow ones.
- **Area pages:** each of the six areas has a page with a card for each group, listing every article in it.
- **Home:** the welcome heading with the latest version beside it on the same line, with no date (`.version-badge`,
  read from the changelog or a version file, never typed); then the journey; then the newest thing
  (`.feature-card`); then the problem solver card (`.solver-card`), always under the newest thing.

### 11.2 The side menu

A side menu that folds (`.side-tree`): **Home**, then each area, then the groups in it, then every article in each
group. Areas and groups are `details` and `summary`, so they work with no script and a screen reader hears each one
as expanded or collapsed; each group shows how many articles it holds. The page you are on is marked
(`aria-current="page"`) and its area and group are open; the rest are shut. Each area starts with **Overview**, its
area page, and Fix a problem also lists the **Problem solver**. On tablets and phones the menu opens from **Menu**
over the page, with the area you are in already open and the focus on the page you are on; the page behind cannot
be reached while it is open; Escape, **Menu** again or choosing a page closes it and the focus goes back to **Menu**.
With no script, the menu sits above the page.

Each article says where it belongs, on the line after its trail line:

```markdown
[Help centre](../README.md) · When something is wrong · troubleshooting
<!-- help: fix / starboard -->
```

The area is one of `start`, `use`, `plugins`, `a11y`, `fix` and `dev`; the group is a key from `help-centre.json`.
An article with no line, or an unknown group, is listed under **Other** and the build warns; `--strict` makes that
an error. Within a group, articles keep the order of the help home's lists, then the order of their titles.

### 11.3 The journey

The home page starts with the journey (`.journey`): three to five stages, left to right on a dashed path, each with
a column of two or three cards under it (`.stage-card`) that link to the articles for that stage. The first card in
each column is the one to start with. The first stage is the start, the last is fixing things; on phones the stages
stack with the path down the side. A plug-in collection's home has its own journey (choose, add, use, update or
remove). Keep each card to a title and one line.

### 11.4 Flow charts

**Every troubleshooting topic starts with a flow chart** (articles are flow chart first), and so does every guide
(its steps at a glance). A how-to with a real choice in it (which version, which kind of drive) may have one; a
reference topic or a basics article does not need one. Put the chart straight after the opening sentences.

Write the chart in a fenced `flow` block. It is plain to read on GitHub, and the builder draws it as an SVG that
follows Light, Dark and High contrast, then writes the same paths out in words under it (**The chart in words**), the
full text equivalent:

````markdown
```flow
title: Find your answer
start: An app's card says Not responding
step: Open the app's details | Select its name on Apps
q: What do the details say?
  Cannot reach the app -> q2
  Refused the API key -> 3
  Answered with an error -> 4
q2: Does the app open in your browser?
  No -> 1
  Yes -> 2
1: Start the app again #start-the-app-again
2: Check the address Starboard uses #check-the-address-starboard-uses
3: Copy the API key again #copy-the-api-key-again
4: Read the app's own messages #read-the-apps-own-messages
```
````

- One node a line: `start:` (exactly one, first), `q:` or `q<name>:` for a question (at least two answers),
  `step<name>:` for something that happens, `end<name>:` for a good end, `warn<name>:` for the last thing to try,
  and a number for a **numbered answer**. `| words` adds a short second line.
- Answers are indented under the node they leave from: `<what the reader sees or chooses> -> <target>`. The target
  is a question, a number, a step or end, or another article (`check-disk-health.md`). A start or a step with no
  answers leads to the next line.
- Each numbered answer is a section of the article: the heading given with `#its-id` at the end of the line, or the
  heading that starts with the number ("1. Start the app again"). The builder shows each as an answer card
  (`.answer-card`): the number and heading on a grey band, the steps under it. Using `#its-id` keeps the heading's
  words and its address, so links to it from release notes still work.
- An answer reached from another answer ("Still does not open -> 5") is drawn as the next thing to try.
- Keep questions short (under eight words), answers to what the reader sees, and a chart to about ten nodes. A
  chart that will not fit is two articles.
- Simple Mermaid flowcharts (`flowchart TD` with `A[...] --> B{...}`) are drawn the same way, so older guides need
  no change; write new charts as `flow` blocks. No chart library is loaded in the browser.

### 11.5 The problem solver

`solver.html` asks up to four questions and takes the reader to the article that fixes the problem. It is written in
`help-centre.json` under `solver` as a tree: each answer has `to` (an article) or `next` (the next question). With
no script it is the whole tree as lists of links; with script it asks one question at a time, with **Back** and
**Start again**, puts the focus on each new question and says it politely. Every Fix a problem article should be
reachable from it. Its card (`.solver-card`) goes on the home page under the newest thing, and at the top of Fix a
problem.

### 11.6 Pages

- **Articles:** breadcrumbs (help centre, area, group, title), the kind, the article, **On this page**, and a link to
  the Markdown on GitHub.
- **Search:** every article, searched in the browser; every word must appear, titles count most.
- **Display and accessibility:** the same choices as the apps, applied before the page draws.

### 11.7 Plug-in mode

A help centre for a plug-in collection adds `plugins` to `help-centre.json`. Its Plug-ins area becomes the plug-ins
themselves: each group of plug-ins is an area in the side menu, each plug-in a folding item in it, and under every
plug-in the same eight pages in the same order: **Overview**, **Install**, **Settings**, **Dashboard card**,
**Updates**, **Accessibility**, **Problems** and **For developers**. Overview is the plug-in's own README; the
others are `help/plugins/<id>/<page>.md`. A page with nothing to say shows one line saying so (the builder writes
one when the file is missing). A plug-in's pages start with its band (`.plugin-band`): the logo or initials, the
name, the version and plug-in API, a status chip and **How to add it**. The home and the Plug-ins area show a card
for each plug-in in the grey band design (`.plugin-card`): logo, name and status chip, what it does, and links to
Install, Settings and Problems. The Problems page starts with a flow chart, as any troubleshooting topic does.

### 11.8 help-centre.json

```json
{
  "name": "Starboard", "repo": "https://github.com/TheMightyTRex/starboard",
  "site": "https://themightytrex.github.io/starboard/help/", "help_dir": "docs/help",
  "version_from": "CHANGELOG.md",
  "home": { "title": "Welcome to Starboard help", "intro": "One sentence." },
  "areas": [
    { "key": "fix", "intro": "One sentence.", "groups": [ { "key": "starboard", "label": "Starboard and set-up" } ] },
    { "key": "plugins", "none": "Snaglist has no plug-ins: it is one file you add to a page." }
  ],
  "journey": { "title": "Your server, step by step", "stages": [
    { "label": "Set up", "icon": "compass", "tone": "start",
      "cards": [ { "title": "Quick start", "line": "One command sets up everything", "to": "guides/quick-start.md" } ] } ] },
  "featured": { "chip": "New in 0.18", "title": "Update Starboard from its own page", "text": "Two sentences.",
    "to": "topics/update-starboard.md", "flow": "start: Update now\nstep: Back up your settings\n..." },
  "solver": { "start": { "question": "What is wrong?", "answers": [
    { "label": "Starboard will not open", "to": "topics/starboard-does-not-open.md" },
    { "label": "Something is wrong with an app", "next": { "question": "What does the app do?", "answers": [] } } ] } },
  "plugins": { "catalogue": "catalogue.json", "overview": "{id}/README.md", "pages": "help/plugins/{id}/{page}.md",
    "groups": [ { "label": "Network and safety", "ids": ["remote-access", "vpn-check"] } ],
    "details": { "vpn-check": { "icon": "shield-check", "status": ["Recommended", "success"] } } }
}
```

- `version_from` names the changelog (the first released version in it, never Unreleased) or a file holding only
  the version; `version` gives it outright; `version_link` changes where the badge goes.
- `tone` is `start`, `step` or `fix`; `icon` is any icon in `icons.svg`. A `to` is an article (from the help
  folder), a page of the help centre (`solver.html`, `areas/plugins.html`) or a full address.
- `featured` takes `flow` (a small chart, in the format of 11.4) or `image` and `alt`.
- With no `areas`, the builder keeps the older layout: the side menu is the help home's own lists.
- `goatcounter` (optional) turns on visitor counting: the GoatCounter address, such as
  `https://<code>.goatcounter.com/count`. Every page loads its counter, and the footer says that visits are counted
  without cookies or personal data. Leave it out and nothing is counted.
- The older settings still work: `leave_out`, `sections`, `footer_note`, `banner` or `banners`, `sponsored_links`,
  `strip_between`, `search_example`, `front_door`, `logo_file`, `favicon_file`.
