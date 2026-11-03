// Runs plugin.js in SES, the sandbox Penpot uses, against a stand-in for Penpot that records what it makes.
// Run: penpot/test.sh (Docker). It fails if SES refuses the code or any part of the build fails.
import fs from "node:fs";
import "/tmp/ses/node_modules/ses/dist/ses.cjs";
lockdown({ errorTaming: "unsafe", consoleTaming: "unsafe" });
const code = fs.readFileSync(process.env.CODE || "/w/penpot/plugin.js", "utf8");
const made = { boards: 0, texts: 0, rects: 0, svgs: 0, pages: [], colours: 0, typographies: 0, components: [], messages: [] };
let handler = null, current = null;
const shape = (type) => {
  const s = { type, name: "", x: 0, y: 0, width: 100, height: 100, fills: [], strokes: [], children: [], parent: null,
    resize(w, h) { if (!(w > 0 && h > 0)) throw new Error(`bad size ${w}x${h} on ${type} ${s.name}`); s.width = w; s.height = h; },
    appendChild(c) { if (!c || !c.type) throw new Error("appendChild of nothing"); c.parent = s; s.children.push(c); c.layoutChild = s.flex ? { verticalSizing: "auto", horizontalSizing: "auto" } : undefined; } };
  (current?.shapes || []).push(s);
  return s;
};
const font = { name: "Atkinson Hyperlegible Next", fontId: "gfont-atkinson", fontFamily: "Atkinson Hyperlegible Next", fontVariantId: "regular", fontWeight: "400",
  variants: ["400", "600", "700"].map((w) => ({ name: w, fontVariantId: w, fontWeight: w, fontStyle: "normal" })),
  applyToText(t, v) { if (!v) throw new Error("no variant"); t.fontFamily = this.fontFamily; t.fontWeight = v.fontWeight; } };
const penpotMock = {
  theme: "light",
  ui: { open() {}, sendMessage(m) { made.messages.push(m); }, onMessage(f) { handler = f; } },
  fonts: { findByName: (n) => (n === "Atkinson Hyperlegible Next" ? font : null) },
  closePlugin() {},
  createPage() { const p = { name: "", shapes: [] }; made.pages.push(p); return p; },
  openPage(p) { current = p; },
  createBoard() { made.boards++; const b = shape("board"); b.addFlexLayout = () => (b.flex = { appendChild: (c) => b.appendChild(c) }); return b; },
  createText(t) { made.texts++; const s = shape("text"); s.characters = t; s.applyTypography = (ty) => { if (!ty) throw new Error("applyTypography of nothing for " + t); }; return s; },
  createRectangle() { made.rects++; return shape("rect"); },
  createShapeFromSvg(svg) { if (!svg.includes("<svg") || svg.includes("undefined")) throw new Error("bad svg"); made.svgs++; return shape("group"); },
  library: { local: {
    createColor() { made.colours++; const c = { asFill: () => ({ fillColorRefId: "x" }), asStroke: () => ({ strokeColorRefId: "x" }) }; return c; },
    createTypography() { made.typographies++; return { setFont(f, v) { if (!v) throw new Error("typography without variant"); } }; },
    createComponent(shapes) { if (shapes.length !== 1) throw new Error("component of " + shapes.length); const s = shapes[0]; const c = { name: "", path: "", mainInstance: () => s }; made.components.push(c); return c; },
  } },
};
const c = new Compartment({ penpot: harden(penpotMock), setTimeout: harden((f) => { Promise.resolve().then(f); return 0; }) });
c.evaluate(code);
await handler({ type: "build" });
const steps = made.messages.filter((m) => m.type === "step" && m.status !== "working");
for (const s of steps) console.log(s.status.toUpperCase(), s.label, "-", s.detail);
console.log("finished:", JSON.stringify(made.messages.at(-1)));
console.log(`pages ${made.pages.map((p) => p.name).join(", ")} | boards ${made.boards} texts ${made.texts} rects ${made.rects} icons ${made.svgs} colours ${made.colours} type ${made.typographies}`);
const paths = {}; for (const c of made.components) paths[c.path] = (paths[c.path] || 0) + 1;
console.log("components:", JSON.stringify(paths));
const loose = made.pages.flatMap((p) => p.shapes.filter((s) => !s.parent && s.type !== "board")).length;
console.log("shapes left outside any board:", loose);
const failedParts = made.messages.filter((m) => m.type === "step" && m.status === "failed").length;
if (failedParts || loose) process.exit(1);
