#!/usr/bin/env node
/**
 * check_slides.mjs — projector-readiness check for a slide deck series.
 *
 * Two invariants, both of which fail silently in a browser and only show
 * up in a classroom:
 *
 *   1. NO OVERFLOW. A slide taller than the 1080px canvas loses content
 *      off the bottom — or, with plain `justify-content: center`, off the
 *      top and bottom at once, hidden behind the header.
 *   2. NO TYPE BELOW 18px. The classroom floor from the lesson-planning
 *      skill: nothing a student must read below 26px, nothing at all
 *      below 18px. Tone marks on pinyin are the first casualty.
 *
 * Needs a static server on the deck root. From the repo root:
 *     python3 -m http.server 8087 --directory index &
 *     node scripts/check_slides.mjs --design y8-l10
 *
 * Options: --design <id>  --port <n>  --floor <px>
 */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const args = {};
const a = process.argv.slice(2);
for (let i = 0; i < a.length; i += 2) args[a[i].replace(/^--/, '')] = a[i + 1];

const design = args.design || 'y8-l10';
const port = args.port || '8087';
const floor = parseFloat(args.floor || '18');

const base = path.join(__dirname, '..', 'index', 'designs', design);
if (!fs.existsSync(base)) {
  console.error(`No such design: ${design}`);
  process.exit(1);
}

const decks = fs.readdirSync(base)
  .filter(d => fs.existsSync(path.join(base, d, 'slides')))
  .sort();

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });

let overflows = 0, tiny = 0, total = 0;

for (const deck of decks) {
  for (const file of fs.readdirSync(path.join(base, deck, 'slides')).sort()) {
    total++;
    await page.goto(`http://localhost:${port}/designs/${design}/${deck}/slides/${file}`);
    await page.waitForTimeout(120);
    const r = await page.evaluate(() => {
      const c = document.querySelector('.slide-content');
      // Only <body> — a <title> in <head> is metadata, not slide text.
      let min = 999, minText = '';
      document.body.querySelectorAll('*').forEach(el => {
        if (!el.children.length && el.textContent.trim()) {
          const size = parseFloat(getComputedStyle(el).fontSize);
          if (size < min) { min = size; minText = el.textContent.trim().slice(0, 30); }
        }
      });
      return { over: c ? c.scrollHeight - c.clientHeight : 0, min, minText };
    });
    if (r.over > 0) {
      overflows++;
      console.log(`  OVERFLOW ${String(r.over).padStart(4)}px  ${deck}/${file}`);
    }
    if (r.min < floor) {
      tiny++;
      console.log(`  TINY ${r.min}px "${r.minText}"  ${deck}/${file}`);
    }
  }
}

console.log(`\n${design}: ${total} slides across ${decks.length} decks`);
console.log(overflows === 0 ? '  ✓ no slide overflows the canvas'
                            : `  ✗ ${overflows} slides overflow`);
console.log(tiny === 0 ? `  ✓ nothing rendered below ${floor}px`
                       : `  ✗ ${tiny} slides carry type under ${floor}px`);

await browser.close();
process.exit(overflows + tiny === 0 ? 0 : 1);
