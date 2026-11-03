# Security checks guide

Version 1.0, 3 November 2026. How Storyarr and Starboard check their security, sort what the checks find, and
report the results. Both apps run the same checks and record them in the same way, so a person can compare
them and trust what each one says. Every word follows `CONTENT-DESIGN.md`.

## About this guide

### What it is for

A security check is only useful when someone acts on its results and writes them down. This guide lists the
checks, says what each one finds and misses, and sets the rules for sorting findings and recording them.

### Who it is for

Anyone who builds or releases Storyarr or Starboard, including AI agents, and anyone who wants to know how
far to trust them. No security background is needed: each check is explained from the start.

### How to use it

1. Read section 1 for the checks at a glance.
2. Before a release, run every check in sections 2 to 5 that the release touches. Section 7 says how each
   app runs them.
3. Sort what they find with section 8.
4. Record the results with section 9, and list the fixes in the release notes with section 10.
5. Go through the checklist in section 11.

The worked example is Starboard: its `tools/security-scan.sh`, `tools/zap-rules.tsv` and
[Security: how Starboard protects you, and how it was tested](https://github.com/TheMightyTRex/starboard/blob/main/docs/SECURITY-AND-TESTS.md).

**For AI agents:** treat every **Rule** as a check that must pass before a release is finished. Never mark a
finding as not real without the evidence that section 8 asks for.

---

## 1. The checks at a glance

| Check | What it finds | When | A pass is |
|---|---|---|---|
| Unit and API tests | A security rule in the code that has stopped working | Every change | Every test passes |
| Live browser journeys | Problems only a real browser shows: code run from data, a missing content policy, keys in a page, unsafe redirects | Every push | Every journey passes |
| Trivy | Known problems in the image, its libraries and the Dockerfile | Every release | 0 known problems, or each one explained |
| OWASP ZAP | Weaknesses in the running app, from outside | Every release; the active scan when sign-in, requests or pages change | No failures; each warning left is explained |
| Gitleaks | Keys and passwords anywhere in the git history | Every commit (GitHub) and every release | 0 findings, apart from made-up keys listed in `.gitleaksignore` |
| Bandit and Semgrep | Risky patterns in Python and in TypeScript or JavaScript | Every release | 0 medium or high findings, apart from lines marked with a reason |
| ShellCheck | Mistakes in shell scripts | Every release | 0 warnings |
| Hadolint | Mistakes in the Dockerfile | Every release | 0 warnings, apart from rules left out with a reason |
| CodeQL, secret scanning and push protection | Unsafe data flow in the code; keys pushed by mistake | Every push, on GitHub | No open alerts that have not been read |
| A separate code review | What the tools cannot reason about: logic, trust and design | Before a release that changes sign-in, requests or access | Every finding sorted and recorded |
| Install tests on clean systems | Security settings that only exist after a real install | Every release | Every install check passes on every system |
| Docker Bench, Nmap and Lynis | Problems with the server, not the app | When the server changes | Each finding read, and fixed or recorded |

## 2. Checks on the app's own rules

### 2.1 Unit and API tests for each security rule

- What it is: a short automatic test for each security rule the app makes, such as "every API route refuses
  without signing in".
- What it finds: a rule that a later change has broken. A rule with no test can stop working without anyone
  knowing.
- How it works: each test sends one request, or calls one function, and checks the answer. For example, it
  sends a change without the app's own header and checks that the answer is a refusal.
- Run it: Starboard `python3 -m unittest discover -s tests`. Storyarr `uv run pytest`.
- Pass: every test passes.
- Limits: a test checks only the rule someone thought to write. It finds nothing new.

**Rule: every security rule has a test, and every security fix adds one,** so the fix stays fixed. Give each
rule an ID (`SEC-01`, `SEC-02`) that the test prints beside its result and the security page uses.

### 2.2 Live browser journeys

- What it is: a real browser, driven by a script, that signs in and goes through the app like a person.
- What it finds: problems that only exist in a browser:
  - code shown as text: a book title or app name that contains HTML or a script appears as plain text and
    never runs;
  - the content policy on every page: each page sends a `Content-Security-Policy` header, and the browser
    blocks nothing the page needs;
  - keys never in a page: no API key, password or token appears in any page, answer or browser storage;
  - sign-in redirects: after signing in, the `next` address cannot send someone to another site.
- How it works: the journeys run against a copy of the app with made-up data, in the Playwright browser
  image, and fail when a page breaks a rule.
- Run it: Starboard `tools/journeys.sh`. Storyarr `python3 scripts/check.py ui --full` (mocked), then the
  live journeys against a local copy with its own database.
- Pass: every journey passes.
- Limits: a journey checks only the pages and data it is given.

## 3. Scanners

Each scanner runs in Docker from a pinned image, so nothing is installed and every run uses the same version.

### 3.1 Trivy

- What it is: a scanner that compares everything inside the app's image with public lists of known problems
  (CVEs, the public catalogue of known security problems).
- What it finds: system packages and libraries (Python, npm) with known problems, and risky settings in the
  Dockerfile, such as running as root.
- How it works: it reads the version of every package in the image and looks each one up. It never runs the
  app.
- Run it, for the image and then the Dockerfile:

  ```bash
  docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:0.69.1 image --scanners vuln,secret --exit-code 1 starboard:scan
  ```

  ```bash
  docker run --rm -v "$PWD:/src:ro" aquasec/trivy:0.69.1 config --exit-code 1 /src
  ```

- Pass: 0 known problems, or each one left is explained on the security page (for example, no fixed version
  exists yet).
- Limits: it finds only problems that are already public. It says nothing about the app's own code.

### 3.2 OWASP ZAP

- What it is: a free scanner that attacks a running web app from outside, the way someone on the network
  would.
- What it finds: missing security headers, cookies without the right settings, forms that leak data, and,
  in the active scan, injection, path tricks and other attacks that work.
- How it works: it has two modes.
  - Baseline, signed out: ZAP follows every link it can find and reads each answer. It sends no attacks, and
    takes a few minutes.
  - Active scan, signed in: ZAP is given a sign-in cookie and sends attacks to every page and API route it
    finds. It changes data, so it runs only against a throwaway copy, never the live app. It takes about 45
    minutes.
- Where it runs: the throwaway copy and ZAP share a private Docker network made with `--internal`, which has
  no way out. The reason: ZAP's crawler treats every port on one address as one site. Both apps link to other
  apps on the same computer, so a scan of `localhost:8095` would follow a link to `localhost:8096` and attack
  that app too. On the private network, the copy is the only thing ZAP can reach, and nothing reaches the
  internet.
- Rules file: `tools/zap-rules.tsv` lists each ZAP rule the app ignores, one a line, with the reason:

  ```
  10202	IGNORE	(Anti-CSRF tokens: changes need the X-Starboard header and a matching Origin)
  ```

  The same reason is on the security page. A rule is never ignored without one.
- Run it: `tools/security-scan.sh` runs the baseline; `tools/security-scan.sh --full` adds the active scan.
- Pass: no FAIL. Every WARN is either fixed or ignored in the rules file with its reason.
- Limits: ZAP finds only the pages it can reach, and does not understand what the app is for. It cannot tell
  that one person can open another person's books.

### 3.3 Gitleaks

- What it is: a scanner for keys, passwords and tokens.
- What it finds: a secret in any file, in any commit, including one that was deleted later. A deleted secret
  is still in the history, so it is still public.
- How it works: it matches every line of every commit against patterns for known kinds of key.
- Run it over the whole history:

  ```bash
  docker run --rm -v "$PWD:/repo:ro" zricethezav/gitleaks:v8.28.0 git /repo --no-banner --redact
  ```

- Made-up keys: tests that check the app hides keys need a key to hide. List each one in `.gitleaksignore`
  with a comment that says it is made up and where it is:

  ```
  # A made-up key in the test that checks the log hides keys (tests/test_logs.py), not a real one.
  09652c38c436007ef040927e16c88018f28ae1da:tests/test_logs.py:generic-api-key:16
  ```

- Pass: 0 findings that are not listed in `.gitleaksignore`.
- Limits: it knows the common kinds of key, not every one. A real secret that was ever pushed must be
  changed at its source: removing it from the history is not enough.

### 3.4 Bandit and Semgrep

- What they are: scanners that read source code for risky patterns. Bandit reads Python. Semgrep does the
  same for TypeScript and JavaScript.
- What they find: commands built from text, unsafe file and web address handling, weak randomness, and
  `dangerouslySetInnerHTML` or `innerHTML` that could run code from data.
- How they work: they read the code without running it, and flag each line that matches a risky pattern.
- Run them:

  ```bash
  docker run --rm -v "$PWD:/src:ro" python:3.12-alpine sh -c "pip install -q bandit && bandit -q -r /src/starboard -ll"
  ```

  ```bash
  docker run --rm -v "$PWD:/src:ro" semgrep/semgrep semgrep scan --config p/typescript --config p/react --error /src/apps/web/src
  ```

  Pin the Semgrep version in the app's own script, as for the other scanners.
- Pass: 0 medium or high findings. A line that has been checked by hand and is safe is marked, with the
  reason in the same comment: `# only http and https addresses reach this line  # nosec B310` (Bandit). For
  Semgrep, put the reason in a comment on the line before `// nosemgrep: <rule ID>`.
- Limits: they flag patterns, not proof. Many findings are safe in context, and that has to be checked by a
  person.

### 3.5 ShellCheck

- What it is: a checker for shell scripts.
- What it finds: unquoted names that break on a space, commands that fail silently, and other mistakes that
  can make an installer or updater do the wrong thing.
- Run it: `docker run --rm -v "$PWD:/mnt:ro" koalaman/shellcheck:v0.11.0 -S warning install.sh tools/*.sh`
- Pass: 0 warnings.
- Limits: it checks the script, not what the script does on a real system. Install tests do that.

### 3.6 Hadolint

- What it is: a checker for Dockerfiles.
- What it finds: images that run as root, unpinned base images, and installs that leave caches and tools in the
  image.
- Run it: `docker run --rm -i hadolint/hadolint:v2.14.0 hadolint - < Dockerfile`
- Pass: 0 warnings, apart from rules left out with `--ignore` and a reason in the script and on the security
  page.
- Limits: it reads the Dockerfile only, not what ends up in the image. Trivy does that.

## 4. Checks on GitHub

These are free for public repositories. Activate them in the repository's **Settings**, under
**Code security**.

- CodeQL code scanning: GitHub's own analysis runs on every push. It follows data from where it comes in,
  such as a request, to where it is used, such as a file path, and raises an alert when nothing checks it on
  the way. Scan Python, JavaScript and TypeScript, and the workflow files. Pass: no open alert that has not
  been read and sorted (section 8).
- Secret scanning: GitHub checks every push for keys from known providers and tells the owner.
- Push protection: stops a push that contains a known kind of key, before it becomes public.

Limits: CodeQL raises many alerts that are safe in context, and it cannot know the app's design. Secret
scanning knows only the providers it has patterns for.

## 5. Review and install tests

### 5.1 A code review by a separate agent

- What it is: a reviewer, a person or an AI agent, that did not write the code. It has not seen the other
  checks or the reasoning behind the changes.
- What it finds: what tools cannot: a rule that is right in one place and missing in another, a trust that
  should not be given, a design that leaks by being used as intended.
- How it works: give the reviewer the code, how the app is used and who might attack it, and ask for each
  finding with its severity, the evidence and a way to show it. Do not give it your own conclusions.
- Pass: every finding is sorted (section 8) and recorded (section 9).
- Limits: a review is as good as the time and knowledge behind it, and its mistakes sound as sure as its
  findings. Check each one.

### 5.2 Install tests on clean systems

- What it is: a fresh install on throwaway systems, from the same instructions people follow.
- What it finds: security settings that only exist after a real install: file permissions, the user the app
  runs as, ports it opens, and options that should stay inactive until someone activates them.
- Run it: Starboard `tools/vm/vm.sh test <system>` on Ubuntu, Debian, Fedora and 64-bit ARM. Storyarr: the
  `compose.yaml` install on a clean Linux system, then `scripts/smoke_image.sh`.
- Pass: every install check passes on every system.
- Limits: only the systems tested.

## 6. Checks for the server, not the app

These check the computer the apps run on. Run them when the server changes, not for each release, and keep
their results private: they describe a home network.

- Docker Bench for Security: checks Docker's own set-up against the CIS benchmark (a public list of good
  settings), such as who can use Docker and how containers are limited. The command, with the folders it
  needs, is in [Docker Bench for Security](https://github.com/docker/docker-bench-security).
- [Nmap](https://nmap.org), from another device: lists the ports the server really has open, as anyone else on the network finds
  them. Run it from a different computer, or the server's own firewall is not tested.
  `nmap -p- 192.0.2.10` (use the server's own address)
- [Lynis](https://cisofy.com/lynis/): audits the server's system settings, such as updates, sign-in and firewall, and suggests changes.
  `sudo lynis audit system`

Limits: each lists findings for a person to judge. Many suggestions do not suit a home server.

## 7. How each app runs the checks

**Rule: each app has one script that runs every scanner,** `tools/security-scan.sh`, from pinned Docker
images, against a throwaway copy, never the live app. It prints PASS or FAIL for each scanner and ends with a
failure when any scanner fails.

| Check | Starboard | Storyarr |
|---|---|---|
| Unit and API tests | `python3 -m unittest discover -s tests` | `uv run pytest` (unit, contract and integration tests in CI) |
| Browser journeys | `tools/journeys.sh` | `python3 scripts/check.py ui --full`, and the live journeys before every push |
| Trivy, ZAP, Gitleaks, Bandit, ShellCheck, Hadolint | `tools/security-scan.sh` (`--full` for the active ZAP scan) | Not yet: a `tools/security-scan.sh` to add |
| Semgrep for TypeScript and JavaScript | Not yet (CodeQL covers the JavaScript) | Not yet: `apps/web/src` |
| Secret scanning and push protection on GitHub | Active | Inactive. A Gitleaks workflow scans the current files on every push; the whole history is not scanned yet |
| CodeQL | Python, JavaScript and workflows | Inactive |
| Install tests | `tools/vm/vm.sh test <system>` on 5 systems | `scripts/smoke_image.sh` on the built image |

What changes for Storyarr's script:
- The throwaway copy needs its database: start `postgres` and Storyarr from `compose.yaml` on the private
  network, with made-up settings.
- Bandit reads `services/`, Semgrep reads `apps/web/src`, ShellCheck reads `scripts/*.sh`, and Trivy also
  scans `apps/web/package-lock.json`.
- Gitleaks scans the whole history with `git`, not only the current files.

## 8. Sort what the checks find

Every finding is sorted before a release, by a person or an agent who has read it.

1. Read the finding in full: the file, the line or address, and what the tool says can happen.
2. Decide whether it is real, with evidence:
   - Real: show it happening, with a request, a test or the exact data that does it.
   - Not real: name the check that stops it, such as the line that validates the path, or the test that
     proves it. "It looks fine" is not evidence.
3. Give a real finding a severity (critical, high, medium, low or information) from what it lets someone do,
   and who could do it.
4. Fix a real finding with a test that fails before the fix and passes after it.
5. Anything left on purpose, such as a design choice, is explained on the security page in words a person can
   judge. Mark it in the tool too (`tools/zap-rules.tsv`, `.gitleaksignore`, `nosec`, or the reason when
   dismissing a CodeQL alert), with the same reason.

**Rule: never dismiss an alert that has not been read,** and never ignore a rule only to get a pass. A
dismissed alert says "someone checked this", so it must be true.

## 9. Record the checks in each app

**Rule: each app's repository records its checks and their results** on one security page
(Starboard: `docs/SECURITY-AND-TESTS.md`). The page has:

- How the app protects people: each protection in plain words.
- Security tests and results: each rule's ID, what is tested, how, and the result.
- A section for each check (each scan, CodeQL, each review): what it found, how each finding was fixed, and
  the date.
- Left as they are, on purpose: each choice and why.
- Not tested yet: each rule that is in the code but has no automatic test.
- Security checks for each release: one row a release, added before the release is tagged.

| Release | Unit and API tests | Browser journeys | Security scans | CodeQL | Install tests | Notes |
|---|---|---|---|---|---|---|
| 0.7.4 (3 November 2026) | 117 passed | 19 passed | Trivy 0, ZAP no failures, Gitleaks 0, Bandit 0, ShellCheck 0, Hadolint 0 | 19 alerts, 3 fixed | 4 systems: 17 of 17 each | Pillow 13.0.0 |

Write a result as a number or a word ("117 passed", "0", "Not run"), never a tick, so it reads the same with a
screen reader. A check that was not run says "Not run" and why.

## 10. Security in the release notes

**Rule: release notes have a Security section that lists every security fix,** one title and one sentence
each, written so a person can judge it: what could happen before, and what happens now. Leave out the
section only when a release has no security fixes. The pattern is in `CONTENT-DESIGN.md`, section 7, under
"Release notes and upgrade wizard".

## 11. Checklist before a release

- [ ] Unit, API and browser journey tests pass, and each new security rule has a test with an ID
- [ ] `tools/security-scan.sh` passes; `--full` too when sign-in, requests or pages changed
- [ ] CodeQL and secret scanning have no alert that has not been read
- [ ] Every finding is sorted with evidence; every fix has a test
- [ ] Everything left on purpose is explained on the security page and marked in the tool with the same reason
- [ ] The security page has a row for this release
- [ ] The release notes have a Security section listing every security fix
- [ ] Nothing in the notes, the page or the rules file names a real server, address, key or person
