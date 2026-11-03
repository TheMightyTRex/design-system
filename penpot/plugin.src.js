// @ts-check
/// <reference types="@penpot/plugin-types" />
/** @typedef {import("@penpot/plugin-types").Font} Font */
/** @typedef {import("@penpot/plugin-types").LibraryColor} LibraryColor */
/** @typedef {import("@penpot/plugin-types").LibraryTypography} LibraryTypography */
/** @typedef {import("@penpot/plugin-types").Board} Board */
/** @typedef {import("@penpot/plugin-types").Shape} Shape */
// TRex Design System for Penpot: builds the design system into the open file. penpot/make.py writes the
// library's values in place of DATA and saves the result as plugin.js; change this file, then run make.py.

/** @type {{font: string, themes: Record<string, Record<string, {hex: string, opacity: number}>>,
 *  core: {space: Record<string, number>, text: Record<string, number>, weight: Record<string, number>, size: Record<string, number>},
 *  icons: Record<string, string>}} */
// @ts-ignore: written by make.py
const DATA = /*DATA*/null;

const UI = "https://themightytrex.github.io/design-system/penpot/ui.html";
const BUILD = "/*BUILD*/"; // make.py writes the build number, the same as in manifest.json
const THEME = "Light"; // Components use the Light colours; the other themes are in the library and Foundations.

penpot.ui.open("TRex Design System", `${UI}?theme=${penpot.theme}`, { width: 380, height: 600 });

/** @param {Record<string, unknown>} message */
const tell = (message) => penpot.ui.sendMessage(message);
const pause = () => new Promise((done) => setTimeout(done, 30));

penpot.ui.onMessage(async (/** @type {{type: string}} */ message) => {
  if (message.type === "ready") tell({ type: "build-number", build: BUILD });
  if (message.type === "build") await build();
  if (message.type === "close") penpot.closePlugin();
});

// Fonts, colours and the small builders every part uses ---------------------------------------------------

/** @type {Font | null} */
let font = null;

function findFont() {
  for (const name of [DATA.font, "Atkinson Hyperlegible", "Source Sans Pro"]) {
    const found = penpot.fonts.findByName(name);
    if (found) return found;
  }
  return null;
}

/** @param {string} weight */
function variantFor(weight) {
  if (!font) return undefined;
  const upright = font.variants.filter((v) => v.fontStyle !== "italic");
  return upright.find((v) => v.fontWeight === weight)
    || upright.sort((a, b) => Math.abs(Number(a.fontWeight) - Number(weight)) - Math.abs(Number(b.fontWeight) - Number(weight)))[0];
}

/** @type {Map<string, LibraryColor>} */
const libraryColours = new Map();

/** @param {string} name a colour role without its dashes, such as "color-accent" or "status-danger-fg" */
function fill(name, theme = THEME) {
  const shared = libraryColours.get(`${theme}/${name}`);
  if (shared) return shared.asFill();
  const c = DATA.themes[theme][name];
  return { fillColor: c ? c.hex : "#ff00ff", fillOpacity: c ? c.opacity : 1 };
}

/** @param {string} name @param {number} width */
function stroke(name, width = 1, theme = THEME) {
  const shared = libraryColours.get(`${theme}/${name}`);
  const s = shared ? shared.asStroke() : { strokeColor: DATA.themes[theme][name]?.hex || "#ff00ff", strokeOpacity: 1 };
  return { ...s, strokeWidth: width, strokeAlignment: /** @type {"inner"} */ ("inner"), strokeStyle: /** @type {"solid"} */ ("solid") };
}

/**
 * @param {string} characters
 * @param {{size?: number, weight?: number, colour?: string, typography?: LibraryTypography}} [o]
 */
function text(characters, o = {}) {
  const t = penpot.createText(characters);
  if (!t) throw new Error(`Penpot did not make the text "${characters}"`);
  if (o.typography) t.applyTypography(o.typography);
  else {
    if (font) font.applyToText(t, variantFor(String(o.weight || 400)));
    t.fontSize = String(o.size || DATA.core.text["text-md"]);
    t.lineHeight = "1.4";
  }
  t.fills = [fill(o.colour || "color-text")];
  t.growType = "auto-width";
  t.name = characters.length > 40 ? characters.slice(0, 40) : characters;
  return t;
}

/**
 * A board with flex layout. Sizes: a number is fixed; "hug" fits the content.
 * @param {string} name
 * @param {{dir?: "row" | "column", gap?: number, padX?: number, padY?: number, pad?: [number, number, number, number],
 *  w?: number | "hug", h?: number | "hug", fill?: string | null, stroke?: [string, number] | null,
 *  align?: "start" | "center" | "end" | "stretch", justify?: "start" | "center" | "end" | "space-between", wrap?: boolean}} [o]
 */
function box(name, o = {}) {
  const b = penpot.createBoard();
  b.name = name;
  b.fills = o.fill ? [fill(o.fill)] : [];
  b.strokes = o.stroke ? [stroke(o.stroke[0], o.stroke[1])] : [];
  b.clipContent = false;
  const w = o.w ?? "hug", h = o.h ?? "hug";
  b.resize(typeof w === "number" ? w : 100, typeof h === "number" ? h : 100);
  const flex = b.addFlexLayout();
  flex.dir = o.dir || "row";
  flex.wrap = o.wrap ? "wrap" : "nowrap";
  flex.alignItems = o.align || "center";
  flex.justifyContent = o.justify || "start";
  flex.rowGap = o.gap ?? 0;
  flex.columnGap = o.gap ?? 0;
  const [top, right, bottom, left] = o.pad || [o.padY ?? 0, o.padX ?? 0, o.padY ?? 0, o.padX ?? 0];
  flex.topPadding = top; flex.rightPadding = right; flex.bottomPadding = bottom; flex.leftPadding = left;
  // Penpot accepts "auto" (fits the content), "fix" and "fill", whatever its published types say.
  flex.horizontalSizing = /** @type {any} */ (w === "hug" ? "auto" : "fix");
  flex.verticalSizing = /** @type {any} */ (h === "hug" ? "auto" : "fix");
  return b;
}

/** @param {Board} parent @param {...Shape} children */
function add(parent, ...children) {
  for (const child of children) {
    if (parent.flex) parent.flex.appendChild(child);
    else parent.appendChild(child);
  }
  return parent;
}

/** @param {string} name @param {number} size @param {string} colour */
function icon(name, size = DATA.core.size["icon-md"], colour = "color-text") {
  const c = DATA.themes[THEME][colour];
  const body = DATA.icons[name];
  if (!body) throw new Error(`No icon called ${name}`);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="${c ? c.hex : "#000000"}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
  const g = penpot.createShapeFromSvg(svg);
  if (!g) throw new Error(`Penpot did not read the icon ${name}`);
  g.name = name;
  g.resize(size, size);
  return g;
}

/** @param {number} w @param {number} h @param {string} colour */
function rect(w, h, colour) {
  const r = penpot.createRectangle();
  r.resize(w, h);
  r.fills = [fill(colour)];
  return r;
}

/**
 * Makes a shape a library component, then puts its main copy in a row of the page.
 * @param {Shape} shape @param {string} path @param {string} name @param {Board} row
 */
function component(shape, path, name, row) {
  shape.name = name;
  const c = penpot.library.local.createComponent([shape]);
  c.name = name;
  c.path = path;
  const main = c.mainInstance();
  if (main && row) add(row, main);
  return c;
}

// Pages -----------------------------------------------------------------------------------------------------

/** @param {string} name */
async function newPage(name) {
  const page = penpot.createPage();
  page.name = name;
  penpot.openPage(page);
  await pause();
  return page;
}

/** A section on a page: a heading, a line of words, and a row for the items. @param {string} title @param {string} about */
function section(title, about, rowOptions = {}) {
  const s = box(title, { dir: "column", gap: 16, pad: [32, 32, 32, 32], w: 1280, fill: "color-bg", align: "start" });
  add(s, text(title, { size: DATA.core.text["text-xl"], weight: 700 }));
  if (about) add(s, text(about, { size: DATA.core.text["text-sm"], colour: "color-text-muted" }));
  const row = box(`${title} items`, { gap: 16, wrap: true, w: 1216, align: "start", ...rowOptions });
  add(s, row);
  return { s, row };
}

/** Stacks the sections of a page one under another. @param {Board[]} sections */
function stack(sections) {
  let y = 0;
  for (const s of sections) {
    s.x = 0;
    s.y = y;
    y += s.height + 40;
  }
}

// The parts --------------------------------------------------------------------------------------------------

function buildColours() {
  const lib = penpot.library.local;
  let count = 0;
  for (const [theme, colours] of Object.entries(DATA.themes)) {
    for (const [name, c] of Object.entries(colours)) {
      const lc = lib.createColor();
      lc.name = name;
      lc.path = theme;
      lc.color = c.hex;
      lc.opacity = c.opacity;
      libraryColours.set(`${theme}/${name}`, lc);
      count++;
    }
  }
  return `${count} colours in ${Object.keys(DATA.themes).length} themes`;
}

/** @type {Record<string, LibraryTypography>} */
const typographies = {};

function buildTypographies() {
  const t = DATA.core.text;
  const styles = [
    ["Heading 1", t["text-2xl"], "700", "1.25"], ["Heading 2", t["text-xl"], "700", "1.25"],
    ["Heading 3", t["text-lg"], "700", "1.3"], ["Lead", t["text-lg"], "400", "1.5"],
    ["Body", t["text-md"], "400", "1.5"], ["Body strong", t["text-md"], "600", "1.5"],
    ["Small", t["text-sm"], "400", "1.5"], ["Label", t["text-sm"], "600", "1.4"],
    ["Caption", t["text-xs"], "600", "1.4"],
  ];
  for (const [name, size, weight, lineHeight] of styles) {
    const ty = penpot.library.local.createTypography();
    ty.name = String(name);
    ty.path = "Text";
    if (font) ty.setFont(font, variantFor(String(weight)));
    ty.fontSize = String(size);
    ty.fontWeight = String(weight);
    ty.lineHeight = String(lineHeight);
    ty.letterSpacing = "0";
    typographies[String(name)] = ty;
  }
  return `${styles.length} text styles in ${font ? font.name : "Penpot's default font"}`;
}

async function buildCover() {
  await newPage("Cover");
  const c = box("Cover", { dir: "column", gap: 16, pad: [64, 64, 64, 64], w: 1280, h: 720, fill: "color-bg", align: "start", justify: "center" });
  add(c,
    text("TRex Design System", { typography: typographies["Heading 1"] }),
    text("One design system for Storyarr and Starboard: tokens, components, icons and guides.", { typography: typographies.Lead }),
    text("Built by the TRex Design System plugin from the library at github.com/TheMightyTRex/design-system.", { typography: typographies.Small, colour: "color-text-muted" }),
    text("Every colour meets WCAG 2.2 AA in all four themes. Change the library there, then run the plugin again in a new file.", { typography: typographies.Small, colour: "color-text-muted" }));
  c.x = 0; c.y = 0;
  return "1 board";
}

async function buildFoundations() {
  await newPage("Foundations");
  const sections = [];
  for (const [theme, colours] of Object.entries(DATA.themes)) {
    const { s, row } = section(`Colour: ${theme}`, `The ${theme} theme. Components use role names, never a raw colour.`, { gap: 12 });
    for (const name of Object.keys(colours)) {
      const card = box(name, { dir: "column", gap: 4, w: 172, align: "start" });
      const sw = rect(172, 48, "color-bg");
      sw.fills = [fill(name, theme)];
      sw.strokes = [stroke("color-divider")];
      add(card, sw, text(name, { size: 12, weight: 600 }),
        text(`${colours[name].hex}${colours[name].opacity < 1 ? ` at ${Math.round(colours[name].opacity * 100)}%` : ""}`, { size: 12, colour: "color-text-muted" }));
      add(row, card);
    }
    sections.push(s);
    await pause();
  }
  const type = section("Type", `${font ? font.name : "The default font"}, one typeface at five sizes. Text scales with the Text size setting in each app.`, { dir: "column", gap: 12 });
  for (const [name, ty] of Object.entries(typographies)) add(type.row, text(`${name}: the lighthouse keeper's niece`, { typography: ty }));
  sections.push(type.s);
  const space = section("Space and size", "Space on a 4px scale. Controls and targets are 44px; 32px only in dense tables.", { dir: "column", gap: 8 });
  for (const [name, v] of Object.entries(DATA.core.space)) {
    const line = box(name, { gap: 12 });
    add(line, rect(v, 16, "color-accent"), text(`${name}: ${v}px`, { size: 14 }));
    add(space.row, line);
  }
  for (const [name, v] of Object.entries(DATA.core.size)) add(space.row, text(`${name}: ${v}px`, { size: 14, colour: "color-text-muted" }));
  sections.push(space.s);
  stack(sections);
  return `${sections.length} sections`;
}

async function buildIcons() {
  await newPage("Icons");
  const { s, row } = section("Icons", "Lucide icons at 24px with a 2px stroke. Beside words they are decorative; alone, the control carries the name.", { gap: 8 });
  let count = 0;
  for (const name of Object.keys(DATA.icons)) {
    const cell = box(`${name} cell`, { dir: "column", gap: 6, w: 112, padY: 8, align: "center" });
    add(row, cell);
    const c = component(icon(name, 24), "Icons", name, cell);
    add(cell, text(name, { size: 11, colour: "color-text-muted" }));
    if (c) count++;
    if (count % 20 === 0) await pause();
  }
  stack([s]);
  return `${count} icon components`;
}

/** @param {"default" | "primary" | "quiet" | "danger"} kind @param {string} label @param {string | null} iconName */
function button(kind, label, iconName = null, compact = false) {
  const colours = {
    default: ["color-surface", "color-border", "color-text"],
    primary: ["color-accent", "color-accent", "color-accent-text"],
    quiet: [null, null, "color-accent"],
    danger: ["color-surface", "status-danger-fg", "status-danger-fg"],
  }[kind];
  const b = box(label, { gap: 8, padX: compact ? 12 : 16, h: compact ? DATA.core.size["control-h-compact"] : DATA.core.size["control-h"],
    fill: colours[0], stroke: colours[1] ? [colours[1], 1] : null, justify: "center" });
  const ink = colours[2] || "color-text";
  if (iconName) add(b, icon(iconName, DATA.core.size["icon-md"], ink));
  add(b, text(label, { typography: typographies.Label, colour: ink }));
  return b;
}

const TONES = {
  success: ["circle-check", "In library"], info: ["info", "Downloading"], warning: ["triangle-alert", "Needs attention"],
  danger: ["circle-x", "Failed"], neutral: ["clock", "Waiting"], muted: ["circle", "Excluded"],
};

async function buildComponents() {
  await newPage("Components");
  const sections = [];
  let count = 0;

  const buttons = section("Buttons", "44px high, square, bold small text. One primary button per view; the words say what happens.");
  for (const [kind, label, ic] of /** @type {const} */ ([["primary", "Save changes", null], ["default", "Search now", "search"], ["quiet", "Cancel", null], ["danger", "Delete book", "trash-2"]])) {
    component(button(kind, label, ic), "Buttons", kind[0].toUpperCase() + kind.slice(1), buttons.row); count++;
  }
  component(button("default", "Search now", null, true), "Buttons", "Compact", buttons.row); count++;
  const ib = box("Icon button", { w: 44, h: 44, stroke: ["color-border", 1], justify: "center" });
  add(ib, icon("ellipsis"));
  component(ib, "Buttons", "Icon button", buttons.row); count++;
  sections.push(buttons.s);
  await pause();

  const chips = section("Status chips", "A word, an icon and a colour together, so status never rests on colour alone.");
  for (const [tone, [ic, word]] of Object.entries(TONES)) {
    const fg = `status-${tone}-fg`;
    const chip = box(word, { gap: 4, padX: 8, h: 24, fill: "color-surface", stroke: [fg, 1] });
    add(chip, icon(ic, 14, fg), text(word, { typography: typographies.Caption, colour: fg }));
    component(chip, "Status chips", tone[0].toUpperCase() + tone.slice(1), chips.row); count++;
  }
  const tag = box("Tag", { gap: 4, padX: 8, h: 24, stroke: ["color-divider", 1] });
  add(tag, text("Audiobook", { typography: typographies.Caption, colour: "color-text-muted" }));
  component(tag, "Status chips", "Tag", chips.row); count++;
  sections.push(chips.s);
  await pause();

  const notices = section("Notices and callouts", "The lead word says the meaning, so it never rests on colour.", { dir: "column", gap: 12 });
  const leads = { info: ["info", "Before you begin:", "You need the server address and an API key."], success: ["circle-check", "Tip:", "Select a row to open its details."],
    warning: ["triangle-alert", "Limitation:", "Storyarr does not import ebooks from Calibre."], danger: ["circle-alert", "Warning:", "Deleting a book cannot be undone."] };
  for (const [tone, [ic, title, body]] of Object.entries(leads)) {
    const fg = `status-${tone}-fg`;
    const n = box(title, { w: 560, fill: `status-${tone}-bg`, align: "stretch" });
    const edge = rect(4, 40, fg);
    add(n, edge);
    if (edge.layoutChild) edge.layoutChild.verticalSizing = "fill";
    const inner = box("Content", { gap: 12, padX: 16, padY: 12, align: "start" });
    const words = box("Words", { dir: "column", gap: 4, align: "start" });
    add(words, text(title, { typography: typographies.Label, colour: fg }), text(body, { typography: typographies.Small, colour: fg }));
    add(inner, icon(ic, DATA.core.size["icon-md"], fg), words);
    add(n, inner);
    component(n, "Notices", tone[0].toUpperCase() + tone.slice(1), notices.row); count++;
  }
  const toast = box("Toast", { w: 360, fill: "color-surface-raised", stroke: ["color-border", 1], align: "stretch" });
  const tEdge = rect(DATA.core.size["status-edge-w"], 40, "status-success-fg");
  add(toast, tEdge);
  if (tEdge.layoutChild) tEdge.layoutChild.verticalSizing = "fill";
  const tInner = box("Content", { gap: 12, padX: 12, padY: 12, align: "start" });
  const tWords = box("Words", { dir: "column", gap: 2, align: "start" });
  add(tWords, text("Follow saved", { typography: typographies.Label }), text("New books by Mara Ellison come in by themselves", { typography: typographies.Small, colour: "color-text-muted" }));
  add(tInner, icon("circle-check", DATA.core.size["icon-md"], "status-success-fg"), tWords, icon("x", 16, "color-text-muted"));
  add(toast, tInner);
  component(toast, "Notices", "Toast", notices.row); count++;
  sections.push(notices.s);
  await pause();

  const inputs = section("Inputs", "A visible label above every control, a hint when needed, and an error that says how to fix it.", { gap: 32 });
  /** @param {boolean} error */
  const field = (error) => {
    const f = box(error ? "Field with error" : "Field", { dir: "column", gap: 4, w: 320, align: "stretch" });
    add(f, text("Server address", { typography: typographies.Label }), text("Include the port, such as :8080.", { typography: typographies.Small, colour: "color-text-muted" }));
    const input = box("Input", { padX: 12, h: DATA.core.size["control-h"], fill: "color-surface-raised", stroke: error ? ["status-danger-fg", 2] : ["color-border", 1] });
    add(input, text(error ? "qbittorrent" : "http://qbittorrent.example:8080", { typography: typographies.Body }));
    add(f, input);
    if (input.layoutChild) input.layoutChild.horizontalSizing = "fill";
    if (error) {
      const e = box("Error", { gap: 4 });
      add(e, icon("circle-alert", 16, "status-danger-fg"), text("Enter an address that starts with http:// or https://", { typography: typographies.Label, colour: "status-danger-fg" }));
      add(f, e);
    }
    return f;
  };
  component(field(false), "Inputs", "Field", inputs.row); count++;
  component(field(true), "Inputs", "Field with error", inputs.row); count++;
  /** @param {boolean} on */
  const check = (on) => {
    const c = box(on ? "Checkbox, selected" : "Checkbox", { gap: 12, h: DATA.core.size["control-h"] });
    const tick = box("Box", { w: 22, h: 22, fill: on ? "color-accent" : "color-surface-raised", stroke: [on ? "color-accent" : "color-border", 2], justify: "center" });
    if (on) add(tick, icon("check", 16, "color-accent-text"));
    add(c, tick, text("Include audiobooks", { typography: typographies.Body }));
    return c;
  };
  component(check(false), "Inputs", "Checkbox", inputs.row); count++;
  component(check(true), "Inputs", "Checkbox selected", inputs.row); count++;
  /** @param {boolean} on */
  const toggle = (on) => {
    const s = box(on ? "Switch, active" : "Switch", { gap: 16, h: DATA.core.size["control-h"] });
    const track = box("Track", { w: 44, h: 24, padX: 3, fill: on ? "color-accent" : "color-surface-sunken", stroke: [on ? "color-accent" : "color-border", 1], justify: on ? "end" : "start" });
    add(track, rect(16, 16, on ? "color-accent-text" : "color-border"));
    add(s, text("Upgrade automatically", { typography: typographies.Body }), track);
    return s;
  };
  component(toggle(false), "Inputs", "Switch", inputs.row); count++;
  component(toggle(true), "Inputs", "Switch active", inputs.row); count++;
  const seg = box("Segmented", { stroke: ["color-border", 1] });
  ["Light", "Dark", "Match device"].forEach((label, i) => {
    const part = box(label, { padX: 12, h: DATA.core.size["control-h"], fill: i === 0 ? "color-accent" : null, justify: "center" });
    add(part, text(label, { typography: typographies.Label, colour: i === 0 ? "color-accent-text" : "color-text" }));
    add(seg, part);
  });
  component(seg, "Inputs", "Segmented", inputs.row); count++;
  sections.push(inputs.s);
  await pause();

  const containers = section("Containers", "A card is one thing, and the whole card opens it.");
  const card = box("Card", { dir: "column", gap: 8, w: 320, padX: 16, padY: 16, fill: "color-surface", stroke: ["color-divider", 1], align: "start" });
  add(card, text("The Glass Harbour", { typography: typographies["Body strong"] }), text("Mara Ellison · Book 2 of The Glass Harbour", { typography: typographies.Small, colour: "color-text-muted" }));
  const cardChip = box("In library", { gap: 4, padX: 8, h: 24, fill: "color-surface", stroke: ["status-success-fg", 1] });
  add(cardChip, icon("circle-check", 14, "status-success-fg"), text("In library", { typography: typographies.Caption, colour: "status-success-fg" }));
  add(card, cardChip);
  component(card, "Containers", "Card", containers.row); count++;
  sections.push(containers.s);

  stack(sections);
  return `${count} components`;
}

// The run ----------------------------------------------------------------------------------------------------

async function build() {
  font = findFont();
  tell({ type: "font", name: font ? font.name : null });
  const steps = [
    ["Colours", buildColours], ["Text styles", buildTypographies], ["Cover", buildCover],
    ["Foundations", buildFoundations], ["Icons", buildIcons], ["Components", buildComponents],
  ];
  let failed = 0;
  for (const [label, run] of steps) {
    tell({ type: "step", label, status: "working" });
    try {
      const detail = await /** @type {() => Promise<string> | string} */ (run)();
      tell({ type: "step", label, status: "done", detail });
    } catch (error) {
      failed++;
      tell({ type: "step", label, status: "failed", detail: error instanceof Error ? error.message : String(error) });
    }
    await pause();
  }
  tell({ type: "finished", failed });
}
