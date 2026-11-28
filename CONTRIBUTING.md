# Contributing

Thank you for helping. This repository is the one source of the design system for Starboard, its plug-ins and Stallboard,
so a change here reaches every app.

## Before you start

- Pull the latest version: `git pull`.
- Read `docs/LIBRARY.md` and use an existing class before you write a new one.
- Run `tools/install-hooks.sh` once, so the privacy check runs before each commit.

## Words

Every word, in the components, the gallery, the guides and commit messages, follows the
[content design guide](docs/CONTENT-DESIGN.md). The rules people miss most often:

- British English (colour, organise, licence as a noun).
- Sentence case everywhere, including headings and buttons.
- No em dashes and no contractions.
- Name controls by their label, never by their position.

`python3 tools/check_words.py` finds the banned words in the text people read, and fails on each one.

`python3 tools/check_on_this_page.py` fails a page that has an "On this page" list of jump links. A page with more than one topic uses page topics (tabs) instead; only a long single-topic document may keep the list, and `tools/on-this-page-allowed.txt` names it with the reason.

## Making a change

Follow [Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html). Pull, change the
library here, build, check four themes and 175% text, check contrast, record the decision in `docs/LIBRARY.md`, run
the privacy check and commit. Ask the owner before you push, or open a pull request. To test a change with people,
read [Get feedback](https://themightytrex.github.io/design-system/resources/get-feedback.html).

## Licences

By contributing, you agree that code is under the [MIT licence](LICENSE) and guides under
[CC BY 4.0](LICENSE-DOCS.md).
