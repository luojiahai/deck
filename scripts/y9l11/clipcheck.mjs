#!/usr/bin/env node
/**
 * clipcheck.mjs — catch content clipped INSIDE .slide-content.
 *
 * check_slides.mjs tests whether the document overflows the canvas. It
 * cannot fire here: .slide-content is absolutely positioned with
 * overflow:hidden, so a slide with too much in it crops the bottom off
 * silently and the body stays exactly 540pt tall. That is the failure
 * mode you only notice in the classroom, when the last example sentence
 * is missing.
 *
 * Usage: node scripts/y9l11/clipcheck.mjs <design-id> [<design-id> ...]
 */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const ROOT = path.join(process.cwd(), 'index', 'designs');
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
let bad = 0, seen = 0;

for (const design of process.argv.slice(2)) {
  const base = path.join(ROOT, design);
  for (const deck of fs.readdirSync(base).filter(d =>
       fs.existsSync(path.join(base, d, 'slides')))) {
    for (const f of fs.readdirSync(path.join(base, deck, 'slides')).filter(f => f.endsWith('.html')).sort()) {
      const file = path.join(base, deck, 'slides', f);
      await page.goto('file://' + file);
      const r = await page.evaluate(() => {
        const c = document.querySelector('.slide-content');
        if (!c) return null;
        return { over: c.scrollHeight - c.clientHeight, w: c.scrollWidth - c.clientWidth };
      });
      seen++;
      if (r && (r.over > 1 || r.w > 1)) {
        bad++;
        console.log(`  CLIPPED  ${String(r.over).padStart(4)}px  ${design}/${deck}/${f}`);
      }
    }
  }
}
console.log(bad === 0 ? `  ✓ ${seen} slides, nothing clipped inside .slide-content`
                      : `  ✗ ${bad} of ${seen} slides lose content off the bottom`);
await browser.close();
