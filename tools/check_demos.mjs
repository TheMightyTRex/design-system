// Checks every component, foundation and pattern page: nothing in a demo sticks to the window or covers the site's header
// or another demo, at 375, 800 and 1280 px wide, in Light, Dark, High contrast and High contrast dark.
// Run with Playwright (npm i playwright), from the repository folder:  node tools/check_demos.mjs
// Env: BASE (default: serves the folder itself on port 18999), WIDTHS (default 375,800,1280). Exits 1 on any problem.
import { chromium } from "playwright";
import fs from "node:fs";
import http from "node:http";
import path from "node:path";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
let base = process.env.BASE;
let server;
if (!base) {
  const types = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".svg": "image/svg+xml", ".woff2": "font/woff2" };
  server = http.createServer((req, res) => {
    const file = path.join(root, decodeURIComponent(req.url.split("?")[0]));
    fs.readFile(file, (err, data) => {
      if (err) { res.writeHead(404); res.end(); return; }
      res.writeHead(200, { "Content-Type": types[path.extname(file)] || "application/octet-stream" });
      res.end(data);
    });
  }).listen(18999);
  base = "http://127.0.0.1:18999";
}
const pages = ["foundations", "components", "patterns"].flatMap((d) =>
  fs.readdirSync(path.join(root, d)).filter((f) => f.endsWith(".html") && f !== "index.html").map((f) => `${d}/${f}`));
const widths = (process.env.WIDTHS || "375,800,1280").split(",").map(Number);
const themes = { light: ["light", false], dark: ["dark", false], hc: ["light", true], hcd: ["dark", true] };
const problems = [];
const browser = await chromium.launch();
for (const width of widths) {
  const page = await (await browser.newContext({ viewport: { width, height: 900 } })).newPage();
  for (const p of pages) {
    await page.goto(`${base}/${p}`, { waitUntil: "load" });
    for (const [name, [mode, contrast]] of Object.entries(themes)) {
      await page.evaluate(([m, c]) => {
        document.documentElement.setAttribute("data-theme", m);
        document.documentElement.classList.toggle("pref-contrast", c);
      }, [mode, contrast]);
      const found = await page.evaluate(() => {
        const out = [];
        const header = document.querySelector("header.site-header");
        const bar = header.getBoundingClientRect();
        const hidden = (e) => e.closest(".side-panel-layer, [hidden], dialog:not([open])");
        // 1. Nothing in the page body sticks to the window or is fixed.
        document.querySelectorAll("main *").forEach((e) => {
          if (hidden(e)) return;
          const pos = getComputedStyle(e).position;
          if (pos === "fixed" || (pos === "sticky" && !e.closest(".s-scroll, .table-wrap"))) out.push(`${pos} ${e.tagName}.${String(e.className.baseVal ?? e.className).slice(0, 30)}`);
        });
        // 2. With each demo scrolled just under the header, no visible part of it reaches up into the header.
        document.querySelectorAll(".g-demo").forEach((demo, i) => {
          if (hidden(demo)) return;
          const top = demo.getBoundingClientRect().top + scrollY - bar.height - 8;
          scrollTo(0, Math.max(0, top));
          const h = header.getBoundingClientRect();
          demo.querySelectorAll("*").forEach((e) => {
            if (hidden(e) || e.closest("svg")) return;
            const r = e.getBoundingClientRect();
            if (r.width < 2 || r.height < 2 || e.children.length) return;
            const inside = e.closest(".s-scroll, .table-wrap, [data-scroll]");
            if (inside && inside.scrollWidth > inside.clientWidth) return;
            if (r.top < h.bottom - 1 && r.bottom > h.top + 1 && r.left < h.right && r.right > h.left && getComputedStyle(e).position !== "static") out.push(`demo ${i} reaches the header: ${e.tagName}.${String(e.className.baseVal ?? e.className).slice(0, 30)}`);
          });
        });
        scrollTo(0, 0);
        // 3. Siblings in a demo do not overlap each other.
        document.querySelectorAll(".g-demo").forEach((demo, i) => {
          if (hidden(demo)) return;
          const kids = [...demo.children].filter((k) => !hidden(k) && getComputedStyle(k).position === "static" && k.getBoundingClientRect().height > 2);
          for (let a = 0; a < kids.length; a++) for (let b = a + 1; b < kids.length; b++) {
            const x = kids[a].getBoundingClientRect(), y = kids[b].getBoundingClientRect();
            const w = Math.min(x.right, y.right) - Math.max(x.left, y.left), hh = Math.min(x.bottom, y.bottom) - Math.max(x.top, y.top);
            if (w > 4 && hh > 4) out.push(`demo ${i}: two parts overlap (${kids[a].className} and ${kids[b].className})`);
          }
        });
        return [...new Set(out)];
      });
      for (const f of found) problems.push(`${width}px ${name} ${p}: ${f}`);
    }
  }
}
await browser.close();
if (server) server.close();
console.log(problems.length ? problems.join("\n") : `Demos: no sticky, fixed or overlapping parts on ${pages.length} pages at ${widths.join(", ")} px in four themes.`);
process.exit(problems.length ? 1 : 0);
