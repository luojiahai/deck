#!/usr/bin/env node
/**
 * fit_slides.mjs — reclaim whitespace on slides whose content is clipped.
 *
 * Every fix here is WHITESPACE ONLY. No font-size is touched, so the classroom
 * typography floor is untouched by construction; this follows the reclaim order
 * in the lesson-planning skill (fewer items → tighter .slide-content padding →
 * drop decorative chrome → only then shorter text).
 *
 * For each slide it walks a ladder of progressively tighter scoped rules,
 * measures after each rung, and keeps the first that fits. A slide that still
 * does not fit at the last rung is reported and left alone — that one needs
 * splitting, which is a content decision, not a CSS one.
 *
 * Usage: node scripts/y9l11/fit_slides.mjs <design-id> [...]
 */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const MARK_OPEN = '<style data-fit="whitespace">';
const MARK_CLOSE = '</style>';

// Each rung is additive: rung n applies rules 0..n.
const LADDER = [
  '.slide-content { padding-top: 16pt; padding-bottom: 16pt; }',
  '.sentence-list { gap: 9pt; } .stack.gap-md { gap: 9pt; }',
  '.sentence-row { padding: 9pt 18pt; } .task-box { padding: 14pt 20pt; }',
  '.slide-content { padding-top: 10pt; padding-bottom: 10pt; }',
  '.sentence-list { gap: 7pt; } .sentence-row { padding: 7pt 16pt; }',
  '.recall-cell { padding: 18pt 10pt; } .extension-box { padding: 10pt 14pt; margin-top: 9pt; }',
];

const ROOT = path.join(process.cwd(), 'index', 'designs');
const browser = await chromium.launch();
let fixed = 0, stuck = 0, seen = 0;

function strip(html) {
  const i = html.indexOf(MARK_OPEN);
  if (i === -1) return html;
  const j = html.indexOf(MARK_CLOSE, i) + MARK_CLOSE.length;
  return html.slice(0, i).replace(/\n$/, '') + html.slice(j);
}

for (const design of process.argv.slice(2)) {
  const base = path.join(ROOT, design);
  for (const deck of fs.readdirSync(base).filter(d =>
       fs.existsSync(path.join(base, d, 'slides')))) {
    const dir = path.join(base, deck, 'slides');
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
    if (!files.length) continue;

    // one canvas per deck
    let page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
    await page.goto('file://' + path.join(dir, files[0]));
    const canvas = await page.evaluate(() => ({
      width: document.body.clientWidth || 1920,
      height: document.body.clientHeight || 1080,
    }));
    await page.setViewportSize(canvas);

    const measure = async (file) => {
      await page.goto('file://' + path.join(dir, file));
      await page.evaluate(() => document.fonts && document.fonts.ready);
      return page.evaluate(() => {
        const c = document.querySelector('.slide-content');
        return c ? c.scrollHeight - c.clientHeight : 0;
      });
    };

    for (const file of files) {
      seen++;
      const p = path.join(dir, file);
      const original = strip(fs.readFileSync(p, 'utf8'));
      fs.writeFileSync(p, original);
      let over = await measure(file);
      if (over <= 0) continue;

      const before = over;
      let rung = -1;
      for (let i = 0; i < LADDER.length; i++) {
        const css = LADDER.slice(0, i + 1).join('\n  ');
        const patched = original.replace('</head>',
          `${MARK_OPEN}\n  /* whitespace only - no type size changed */\n  ${css}\n${MARK_CLOSE}\n</head>`);
        fs.writeFileSync(p, patched);
        over = await measure(file);
        if (over <= 0) { rung = i; break; }
      }
      if (rung === -1) {
        fs.writeFileSync(p, original);
        stuck++;
        console.log(`  STILL OVER ${String(before).padStart(4)}px  ${design}/${deck}/${file}  — needs splitting`);
      } else {
        fixed++;
        console.log(`  fixed ${String(before).padStart(4)}px → 0  rung ${rung + 1}/${LADDER.length}  ${design}/${deck}/${file}`);
      }
    }
    await page.close();
  }
}

console.log(`\n  ${seen} slides checked · ${fixed} fixed by reclaiming whitespace · ${stuck} still need splitting`);
await browser.close();
process.exit(stuck === 0 ? 0 : 1);
