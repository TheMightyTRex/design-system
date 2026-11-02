# Contributing

Thank you for helping. This repository is the one source of the design system for Storyarr and Starboard,
so a change here reaches both apps.

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

## Making a change

1. Change the library files, not the copies inside the apps.
2. Run `python3 tools/build.py` and check the gallery in all four themes and at 175% text.
3. Run `python3 tools/contrast.py`. It must report 0 failures.
4. Meet the accessibility floor in `docs/ACCESSIBILITY.md` (WCAG 2.2 AA).
5. Add the change to the decisions list in `docs/LIBRARY.md` when it changes how something looks or works.
6. Commit, push, then run `python3 tools/sync.py` and commit in each app.

## Licences

By contributing, you agree that code is under the [MIT licence](LICENSE) and guides under
[CC BY 4.0](LICENSE-DOCS.md).
