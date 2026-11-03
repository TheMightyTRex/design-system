# The design system in Penpot

Version 1.0, 3 November 2026. How to build the TRex Design System in [Penpot](https://penpot.app), the
free and open-source design tool, so designs can be made with the same colours, text styles, icons and
components as Storyarr and Starboard. Every word follows `CONTENT-DESIGN.md`.

## About this guide

### What it is for

The library in this repository is the source. A plugin builds it into a Penpot file from
the same `tokens.css` and `icons.svg` the apps use, so the Penpot file never has values of its own.

### Who it is for

Anyone who designs for Storyarr or Starboard in Penpot, or wants to use the design system in their own
Penpot work. You need a Penpot account; the free plan is enough.

### What the plugin builds

- **Library colours:** every colour role in four themes (Light, Dark, High contrast and High contrast dark),
  grouped by theme.
- **Library text styles:** Heading 1 to 3, Lead, Body, Body strong, Small, Label and Caption, in Atkinson
  Hyperlegible Next when Penpot has it.
- **Cover:** what the file is and where it comes from.
- **Foundations:** a swatch of every colour in each theme, the text styles, and the space and size scales.
- **Icons:** every library icon as a component.
- **Components:** buttons, icon button, status chips, tag, notices, toast, field, field with an error,
  checkbox, switch, segmented control and card, each a component that uses the library colours.

The components use the Light colours. The other three themes are in the library and on the Foundations page.

## Build the design system in Penpot

1. Sign in to [Penpot](https://design.penpot.app) and create a new, empty file.
2. Open the plugin manager: press Ctrl, Alt and P together (on a Mac, Command, Option and P).
3. Enter the plugin's address, then install it:
   `https://themightytrex.github.io/design-system/penpot/manifest.json`
4. Open the plugin and select **Build the design system**. Each part shows Done, or Failed with the reason.
5. Name the file "TRex Design System".

The plugin asks Penpot for permission to read and change the file and its library, and nothing else. Run it
once in each new file: it adds to the file every time it runs.

## Share it

1. In your projects, open the file's menu and add it as a shared library, so other files can use its
   colours, text styles and components.
2. To give people a link, share the file from its **Share** menu with view access.

## Import the tokens

`penpot/tokens.json` holds every token for Penpot's Tokens panel: a Core set (space, text sizes, weights,
sizes) and one colour set per theme, with a theme for each. Import it from the Tokens panel. Choose a theme
there to switch between Light, Dark and the two High contrast themes.

## Keep it in step

When the library changes:

1. Run `python3 penpot/make.py`. It writes `penpot/plugin.js` and `penpot/tokens.json` from `tokens.css`
   and `icons.svg`.
2. Commit and push, as in [Make a change](https://themightytrex.github.io/design-system/resources/make-a-change.html).
3. Run the plugin again in a new file, and replace the shared library with it.

Change `penpot/plugin.src.js` to change what the plugin builds, never `plugin.js`.

## Connect an AI assistant to Penpot

Penpot has an MCP server (a way for AI assistants to work in an open file). With it, an assistant such as
Claude Code can read the file, run the same plugin code, and check the result. Penpot's guide is
[Penpot MCP server](https://help.penpot.app/mcp/).

1. In Penpot, go to **Your account**, then **Integrations**, then **MCP Server**, and activate it.
2. Generate an MCP key. Penpot shows it once, inside the server address.
3. Add the server to Claude Code in your own terminal, with your key in place of `YOUR_MCP_KEY`:

   ```bash
   claude mcp add --transport http penpot "https://design.penpot.app/mcp/stream?userToken=YOUR_MCP_KEY"
   ```

4. In Penpot, open the file, then go to **File**, then **MCP Server**, and select **Connect**. Keep that tab
   open while the assistant works.

Warning: the MCP key lets anyone with it change your files. Keep it out of chats, commits and screenshots,
and delete it in Penpot if it is ever shared.
