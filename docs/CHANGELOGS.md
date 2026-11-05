# Changelogs

Version 1.0, 5 November 2026. How every project that uses this design system keeps its changelog: Storyarr,
Starboard, Snaglist and the design system itself. It follows the principles of
[Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), written in our own words, with dates and
wording from `CONTENT-DESIGN.md`. Release notes shown in an app follow the same change types
(`CONTENT-DESIGN.md`, section 7).

**For AI agents:** treat every rule marked **Rule** as a check that must pass before a release is finished.
Section 8 is the checklist.

## 1. What a changelog is for

A changelog is a file that lists the notable changes in each version of a project, newest first, so the
people who use it can tell what is different before they upgrade.

1.1 **Rule: changelogs are for people.** Write for the person who runs the app or uses the library, not for
the developer who made the change. Say what someone can now do, what works differently and what was fixed.
The words follow `CONTENT-DESIGN.md`: British English, sentence case, no em dashes, no contractions.

1.2 **Rule: never dump a commit log.** Commits record the steps of the work; a changelog records the
difference those steps made. Leave out merge commits, refactoring, test-only changes, formatting and
version bumps. One entry often covers several commits, and one commit may not be worth an entry.

1.3 **Rule: keep it complete.** A changelog with gaps misleads, because people trust it as the record.
Small changes may be left out, but every new feature, every change in behaviour, every removal and every
security fix goes in.

1.4 **Rule: one file, `CHANGELOG.md`,** at the root of the repository, so people find it where they expect
it. A project may also publish each release's notes (on GitHub or in the app), made from the same entries.

## 2. The file

```markdown
# Changelog

All notable changes to Starboard are listed here, newest first. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with dates written as in the TRex Design System,
and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- **Set up in the terminal.** `./install.sh --terminal` asks the set-up questions with no browser.

## [0.7.7] (4 November 2026)

Lighter, from the performance review.

### Changed
- **Pages open faster.** A page and its files share one connection.

### Security
- **Error answers.** Every answer carries the same security headers.

[Unreleased]: https://github.com/TheMightyTRex/starboard/compare/v0.7.7...HEAD
[0.7.7]: https://github.com/TheMightyTRex/starboard/compare/v0.7.6...v0.7.7
```

2.1 **Rule: the title is `# Changelog`,** then one short paragraph. It names the project, says the list is
newest first, links Keep a Changelog, and says whether the version numbers follow
[Semantic Versioning](https://semver.org/). A fork also says what it is a fork of, with the version.

2.2 **Rule: an Unreleased section at the top,** `## [Unreleased]`, always present, even when it is empty.
Add each change there as it is made, not at release time. When you release, rename the heading to the version
and date, and start a new empty Unreleased section above it.

2.3 **Rule: an entry for every version, newest first.** Every version that was tagged or published has a
section, including test releases people may have installed. Never skip a number without saying why: if
versions were never published, say so in one line under the next version.

2.4 **Rule: the version heading is `## [1.2.3] (4 November 2026)`.** The version in square brackets, so it
links (rule 2.6), then the release date in brackets. Dates follow `CONTENT-DESIGN.md`: "4 November 2026",
never "2026-11-04" or "04/11/26". This is where we differ from Keep a Changelog, which uses year, month,
day: our way matches the dates in both apps and leaves no doubt about the month.

2.5 **Rule: a short summary is allowed** under the version heading, in one or two sentences: the theme of
the release, what to do when upgrading, database changes, and the way back to the version before. Never a
change of its own: changes go under their types.

2.6 **Rule: every version links.** Link references go at the end of the file, one per version, in the same
order as the sections. Each one compares the version with the one before; Unreleased compares the newest
tag with `HEAD`; the first version links to its tag or release page.

```markdown
[Unreleased]: https://github.com/TheMightyTRex/storyarr/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/TheMightyTRex/storyarr/compare/v0.5.9...v0.6.0
[0.1.0]: https://github.com/TheMightyTRex/snaglist/releases/tag/v0.1.0
```

## 3. Types of change

3.1 **Rule: group changes by type,** each as a level 3 heading, always in this order, and leave out a type
with nothing in it:

| Type | What goes in it |
|---|---|
| Added | New features, pages, settings and options |
| Changed | Changes to how something that exists works or looks |
| Deprecated | Features that still work but will be removed, and what to use instead |
| Removed | Features taken out in this version |
| Fixed | Bugs fixed |
| Security | Security fixes, and the checks the release passed |

3.2 **Rule: no other headings under a version.** Not "Improvements", "Documentation", "Database",
"Performance" or a feature name. A faster page is Changed; documentation people read goes under Added or
Changed; database changes go in the summary (rule 2.5). When one feature needs several entries, nest them
under one entry (`CONTENT-DESIGN.md`, rule 2.24).

3.3 **Rule: deprecate before you remove.** List a deprecation in the version before the removal, with what to
do instead, so the upgrade that removes it holds no surprise. Breaking changes are never hidden inside
Changed: say plainly what stops working and what to do.

3.4 **Rule: every security fix goes under Security.** Write each one as `CONTENT-DESIGN.md` says for release
notes: what could happen, to whom, and what happens now, with nothing that helps someone attack an older
version. The last entry names the checks the release passed (`SECURITY-CHECKS.md`).

## 4. Entries

4.1 **Rule: one entry is one change,** as a bullet: a bold headline that says what the person can now do, then
one or two sentences on what changed and who it helps. Add "Find out more in **<help topic>**" when a topic
exists.

4.2 **Rule: write each entry so it reads alone.** Expand abbreviations in every entry, name the page with its
full path ("Settings, then Apps"), and copy on-screen labels exactly.

4.3 **Rule: true when written, and kept true.** An entry describes what the version shipped. If an entry is
wrong, correct it, and say so in the entry ("Corrected 5 November 2026: the limit is 10 books, not 20."). A changelog may be rewritten
to add a missing version or to note a breaking change that was missed.

4.4 Task and issue numbers (DASH-79, storyarr#1) may follow an entry in brackets, for people who track them.
Commit hashes, branch names and file paths do not belong in an entry, unless the reader has to run or edit
that file.

## 5. Withdrawn releases

5.1 **Rule: mark a withdrawn release.** A release taken back because of a serious bug or a security problem
keeps its section, with `[Withdrawn]` after the date, and a first line saying why and which version to use
instead. Keep a Changelog calls this "yanked" and writes it in capitals; we use the plain word in sentence
case, in square brackets so tools can still find it.

```markdown
## [2.4.0] (3 March 2027) [Withdrawn]

Withdrawn because upgrading from 2.3.0 could lose saved searches. Use 2.4.1 or later.
```

## 6. Release notes in the app and on GitHub

6.1 **Rule: one set of words.** The release notes in an app, the upgrade wizard and the GitHub release say
the same as the changelog, in the same types and order. Where a project keeps release notes in code (such as
Starboard's `starboard/releases.py`), the changelog and the code are changed in the same commit.

6.2 The in-app notes may be shorter than the changelog: a headline and one sentence per entry.

## 7. Forks and other people's projects

7.1 **Rule: keep the upstream changelog as it is** in a fork that sends changes back, so merges stay clean.
Changes made only in the fork go in a section of their own, or in a separate file, and follow these rules.

7.2 A change offered to another project follows that project's changelog format, not ours.

## 8. Checklist before a release is finished

- [ ] `CHANGELOG.md` has an `## [Unreleased]` section at the top, empty after the release
- [ ] The new version has a section, `## [x.y.z] (day month year)`, newest first
- [ ] Every change is under Added, Changed, Deprecated, Removed, Fixed or Security, in that order
- [ ] Nothing is a copy of a commit message; every entry says what changed for the reader
- [ ] Every security fix is under Security, and the last entry names the checks
- [ ] A link reference for the new version, and Unreleased compares from the new tag
- [ ] A withdrawn release is marked `[Withdrawn]` with the reason
- [ ] The in-app release notes and the GitHub release say the same
- [ ] Everything in the `CONTENT-DESIGN.md` checklist
