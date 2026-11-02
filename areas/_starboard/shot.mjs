import { chromium } from "/repo/apps/web/node_modules/playwright/index.mjs";
import fs from "fs";
const files = (process.env.FILES || "").split(",").filter(Boolean);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const errs = [];
page.on("pageerror", e => errs.push(e.message));
page.on("console", m => { if (m.type() === "error") errs.push(m.text()); });
for (const f of files) {
  await page.goto(`http://127.0.0.1:8765/areas/${f}.html`, { waitUntil: "networkidle" });
  await page.screenshot({ path: `/out/${f}.png`, fullPage: true });
  // overflow check
  const ov = await page.evaluate(() => document.documentElement.scrollWidth);
  console.log(f, "scrollWidth", ov);
  if (process.env.PANEL) {
    for (const id of process.env.PANEL.split(",")) {
      const opener = page.locator(`[data-opens="${id}"]:visible, [data-dialog="${id}"]:visible`).first();
      if (!(await opener.count())) { console.log("no opener", id); continue; }
      await opener.click(); await page.waitForTimeout(400);
      await page.screenshot({ path: `/out/${f}--${id}.png` });
      await page.keyboard.press("Escape"); await page.waitForTimeout(250); await page.keyboard.press("Escape"); await page.waitForTimeout(200);
    }
  }
}
console.log("errors", JSON.stringify(errs));
await browser.close();
