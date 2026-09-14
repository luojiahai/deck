#!/usr/bin/env node
/**
 * check_slides.mjs — projector-readiness check for a slide deck series.
 *
 * Two invariants, both of which fail silently in a browser and only show
 * up in a classroom:
 *
 *   1. NO OVERFLOW. A slide with more in it than fits loses content off the
 *      bottom of .slide-content — or, with plain `justify-content: center`,
 *      off the top and bottom at once, hidden behind the header. Because
 *      .slide-content is overflow:hidden the page never scrolls, so this
 *      fails silently in the browser and only shows up in the classroom.
 *   2. NO TYPE BELOW 18px. The classroom floor from the lesson-planning
 *      skill: nothing a student must read below 26px, nothing at all
 *      below 18px. Tone marks on pinyin are the first casualty.
 *
 * Both checks depend on the slide's own canvas, and this repo has two:
 * the y7/y8/y9-l7..l9 decks are 1920x1080px, while y9-l10 and y9-l11 are
 * 960pt x 540pt (=1280x720 CSS px, scaled up 1.5x by the deck shell at
 * presentation time). So:
 *
 *   · .slide-content is positioned against the initial containing block —
 *     the VIEWPORT, not the fixed-size body — so the viewport must match the
 *     slide's canvas or clientHeight is wrong and overflow is mis-reported in
 *     whichever direction the mismatch runs. Each slide is therefore measured
 *     at the size it declares.
 *   · the type floor is about what a student can read from the back of the
 *     room, so it is checked against the PROJECTED size: the CSS px are
 *     multiplied by 1920/canvasWidth. A 10pt header tag on a 960pt canvas is
 *     13.3 CSS px but projects at 20px, and passes.
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

// Every slide in a deck shares one canvas, so probe the first slide of each
// deck and reuse the answer rather than reloading twice per slide.
async function canvasOf(url) {
  await page.goto(url);
  return page.evaluate(() => ({
    width: document.body.clientWidth || 1920,
    height: document.body.clientHeight || 1080,
  }));
}

let overflows = 0, tiny = 0, total = 0;

for (const deck of decks) {
  const files = fs.readdirSync(path.join(base, deck, 'slides')).sort();
  if (!files.length) continue;

  const urlOf = f => `http://localhost:${port}/designs/${design}/${deck}/slides/${f}`;
  const canvas = await canvasOf(urlOf(files[0]));
  await page.setViewportSize(canvas);
  // What one CSS px becomes on a 1920-wide projector.
  const scale = 1920 / canvas.width;

  for (const file of files) {
    total++;
    await page.goto(urlOf(file));
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
      console.log(`  CLIPPED ${String(r.over).padStart(4)}px  ${deck}/${file}`);
    }
    const projected = r.min * scale;
    if (projected < floor) {
      tiny++;
      const as = scale === 1 ? `${r.min}px`
                             : `${r.min}px → ${projected.toFixed(1)}px projected`;
      console.log(`  TINY ${as} "${r.minText}"  ${deck}/${file}`);
    }
  }
}

console.log(`\n${design}: ${total} slides across ${decks.length} decks`);
console.log(overflows === 0 ? '  ✓ nothing clipped inside .slide-content'
                            : `  ✗ ${overflows} slides lose content off the bottom`);
console.log(tiny === 0 ? `  ✓ nothing rendered below ${floor}px`
                       : `  ✗ ${tiny} slides carry type under ${floor}px`);

await browser.close();
process.exit(overflows + tiny === 0 ? 0 : 1);
