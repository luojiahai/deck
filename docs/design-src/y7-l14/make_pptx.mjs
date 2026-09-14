#!/usr/bin/env node
/**
 * make_pptx.mjs — export the Y7 L14 decks to editable PPTX.
 *
 *   node docs/design-src/y7-l14/make_pptx.mjs [deck-folder ...]
 *
 * WHY THIS EXISTS RATHER THAN JUST CALLING export_deck_pptx.mjs
 *
 * The stock exporter fails on these decks for three reasons, all real:
 *
 *  1. It hardcodes `pres.layout = 'LAYOUT_WIDE'` (13.333" x 7.5"), and
 *     html2pptx treats a canvas/layout mismatch as fatal. Our canvas is
 *     1920x1080 = 20" x 11.25" at 96dpi. Note the other decks in this repo
 *     already ship 20" x 11.25" PPTX, so a custom layout is the house
 *     convention, not a deviation.
 *
 *  2. html2pptx only emits text that sits inside <p>/<h1>-<h6>/<ul>/<ol>.
 *     Text directly inside a <div> is silently dropped, so it validates
 *     against it. Our templates put text in <div>s and <span>s.
 *
 *  3. html2pptx has NO SVG handling whatsoever, and our garment drawings
 *     are inline SVG. It also crashes on SVG elements, because it calls
 *     el.className.includes() and an SVGElement's className is an
 *     SVGAnimatedString, not a string.
 *
 * Rather than degrade the HTML decks to suit PowerPoint — they are the
 * primary deliverable, they are live, and they have been verified slide by
 * slide — this transforms a THROWAWAY COPY at build time:
 *
 *     rasterise each distinct <svg> to a PNG once
 *     wrap every bare text node in <p style="margin:0;padding:0">
 *     swap each <svg> for an <img> pointing at its PNG
 *     export that copy, then discard it
 *
 * The shipped HTML keeps its vector drawings and its markup. Nothing under
 * index/designs/y7-l14/*\/slides/ is modified.
 */

import { chromium } from 'playwright';
import pptxgen from 'pptxgenjs';
import fs from 'fs';
import fsp from 'fs/promises';
import path from 'path';
import os from 'os';
import { fileURLToPath } from 'url';

const REPO = '/Users/luojiahai/code/deck';
const DECK_ROOT = path.join(REPO, 'index/designs/y7-l14');
const HTML2PPTX = path.join(REPO, '.claude/skills/huashu-design/scripts/html2pptx.js');

// 1920x1080 at 96dpi. Matches the canvas exactly, so nothing is rescaled and
// text keeps the sizes the classroom typography floor was designed around.
const LAYOUT = { name: 'DECK_20x1125', width: 20, height: 11.25 };

const decks = process.argv.slice(2).length
  ? process.argv.slice(2)
  : fs.readdirSync(DECK_ROOT).filter(d =>
      d.startsWith('l') && fs.existsSync(path.join(DECK_ROOT, d, 'slides')));

const work = await fsp.mkdtemp(path.join(os.tmpdir(), 'y7l14-pptx-'));
const artDir = path.join(work, 'art');
await fsp.mkdir(artDir, { recursive: true });

// html2pptx.js is CommonJS (module.exports = fn), so the fn is `default`
const { default: html2pptx } = await import(HTML2PPTX);
const browser = await chromium.launch();

/** Rasterise one <svg> outerHTML to a transparent PNG. Cached by content. */
const svgCache = new Map();
async function svgToPng(page, outer, w, h) {
  const key = outer + '|' + Math.round(w) + 'x' + Math.round(h);
  if (svgCache.has(key)) return svgCache.get(key);
  const file = path.join(artDir, `art-${svgCache.size}.png`);
  // 3x so the drawings stay crisp when PowerPoint scales the slide up
  const sw = Math.max(1, Math.round(w * 3)), sh = Math.max(1, Math.round(h * 3));
  await page.setViewportSize({ width: sw, height: sh });
  await page.setContent(
    `<body style="margin:0;background:transparent">` +
    `<div style="width:${sw}px;height:${sh}px">` +
    outer.replace('<svg', `<svg width="${sw}" height="${sh}"`) +
    `</div></body>`);
  await page.screenshot({ path: file, omitBackground: true });
  svgCache.set(key, file);
  return file;
}

const results = [];

for (const deck of decks.sort()) {
  const srcDir = path.join(DECK_ROOT, deck, 'slides');
  const outDir = path.join(work, deck, 'slides');
  await fsp.mkdir(outDir, { recursive: true });
  // slides reference ../../shared/tokens.css — mirror that shape
  await fsp.mkdir(path.join(work, deck, '..', 'shared'), { recursive: true });
  await fsp.copyFile(path.join(DECK_ROOT, 'shared/tokens.css'),
                     path.join(work, 'shared/tokens.css'));

  const files = (await fsp.readdir(srcDir)).filter(f => f.endsWith('.html')).sort();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  const shot = await browser.newPage();

  for (const f of files) {
    await page.goto('file://' + path.join(srcDir, f), { waitUntil: 'networkidle' });

    // Collect every <svg> with its rendered box, rasterise, then swap for <img>.
    const svgs = await page.evaluate(() => [...document.querySelectorAll('svg')].map((s, i) => {
      s.setAttribute('data-svg-idx', i);
      const r = s.getBoundingClientRect();
      return { i, outer: s.outerHTML, w: r.width, h: r.height };
    }));
    for (const s of svgs) {
      if (s.w < 1 || s.h < 1) continue;
      const png = await svgToPng(shot, s.outer, s.w, s.h);
      await page.evaluate(({ i, png, w, h }) => {
        const el = document.querySelector(`svg[data-svg-idx="${i}"]`);
        if (!el) return;
        const img = document.createElement('img');
        img.src = 'file://' + png;
        img.style.cssText = `width:${w}px;height:${h}px;display:block`;
        el.replaceWith(img);
      }, { i: s.i, png, w: s.w, h: s.h });
    }

    // PowerPoint safe margin: html2pptx requires every text box to end at
    // least 0.5in (48px here) from the slide edge. Our footer chrome sits
    // 0.16in off the bottom, which is fine on a projector but trips the
    // check. Lift the footer bar in the export copy only.
    await page.addStyleTag({ content: `
      .slide-footer { bottom: 52px !important; }
      .slide-header { top: 12px !important; }
    ` });

    // html2pptx only emits text that lives inside <p>/<h*>/<li>, so every
    // element holding raw text needs one. Wrap each such element's WHOLE
    // child list in a single <p>, not each text node individually: <p> is
    // block-level, so per-text-node wrapping puts "这是" and <span>衬衫</span>
    // on separate lines and the slide grows off the bottom of the canvas.
    // One <p> per element keeps the inline flow intact, and gives PowerPoint
    // one text box per logical line instead of a pile of fragments.
    await page.evaluate(() => {
      const TEXT_TAGS = new Set(['P','H1','H2','H3','H4','H5','H6','LI','UL','OL']);
      const targets = [];
      for (const el of document.body.querySelectorAll('*')) {
        if (TEXT_TAGS.has(el.tagName)) continue;
        if (el.closest('p,h1,h2,h3,h4,h5,h6,li')) continue;
        const hasOwnText = [...el.childNodes].some(
          n => n.nodeType === 3 && n.textContent.trim());
        if (hasOwnText) targets.push(el);
      }
      // Only wrap the OUTERMOST element of any nested pair. A <p> inside a
      // <p> auto-closes the outer one when the file is re-parsed, which
      // shatters the markup and orphans the text back into a bare <div>.
      // The outer wrap already carries the inner element's text anyway.
      const outermost = targets.filter(el => !targets.some(o => o !== el && o.contains(el)));
      for (const el of outermost) {
        const p = document.createElement('p');
        p.style.cssText = 'margin:0;padding:0;background:none;border:none;box-shadow:none';
        while (el.firstChild) p.appendChild(el.firstChild);
        el.appendChild(p);
      }
    });

    // PowerPoint has no concept of margin on an inline run, and html2pptx
    // decides "inline" from the TAG, not the computed display — so an
    // inline-block <span> trips it too. Convert every margin on an
    // inline-ish tag to the padding equivalent, which renders the same in
    // the browser and is representable in PowerPoint.
    await page.evaluate(() => {
      const INLINE_TAGS = new Set(['SPAN','A','B','I','EM','STRONG','SMALL','LABEL','CODE']);
      for (const el of document.body.querySelectorAll('*')) {
        const cs = getComputedStyle(el);
        const inlineish = INLINE_TAGS.has(el.tagName) ||
                          cs.display.startsWith('inline');
        if (!inlineish) continue;
        for (const side of ['Top', 'Right', 'Bottom', 'Left']) {
          const m = parseFloat(cs['margin' + side]) || 0;
          if (!m) continue;
          el.style['padding' + side] =
            ((parseFloat(cs['padding' + side]) || 0) + m) + 'px';
        }
        el.style.margin = '0';
      }
    });

    // Wrapping text in <p> and turning inline margins into padding shifts
    // heights by a few px, which can tip an already-full slide past the
    // 0.5in bottom safe margin PowerPoint insists on. The token sheet
    // already has a `dense` modifier for exactly this — apply it here when
    // the export copy needs it, without touching the shipped HTML.
    await page.evaluate(() => {
      const c = document.querySelector('.slide-content');
      if (!c) return;
      const over = () => {
        const box = c.getBoundingClientRect();
        let worst = 0;
        for (const el of c.querySelectorAll('*')) {
          const r = el.getBoundingClientRect();
          if (String(el.className).includes('bg-char')) continue;
          worst = Math.max(worst, r.bottom - (box.bottom - 8));
        }
        return worst;
      };
      if (over() > 0) c.classList.add('dense');
    });

    const html = await page.evaluate(() => '<!DOCTYPE html>' + document.documentElement.outerHTML);
    await fsp.writeFile(path.join(outDir, f), html, 'utf8');
  }
  await page.close();
  await shot.close();

  // Export the transformed copy.
  const pres = new pptxgen();
  pres.defineLayout(LAYOUT);
  pres.layout = LAYOUT.name;
  let ok = 0, fail = [];
  for (const f of files) {
    try {
      // html2pptx adds its own slide to `pres`
      await html2pptx(path.join(outDir, f), pres);
      ok++;
    } catch (e) {
      fail.push(`${f}:\n      ${String(e.message || e).split('\n').join('\n      ')}`);
    }
  }
  const out = path.join(DECK_ROOT, deck, `${deck}.pptx`);
  if (ok) await pres.writeFile({ fileName: out });
  results.push({ deck, ok, total: files.length, fail, out });
  console.log(`${deck}: ${ok}/${files.length} slides` + (fail.length ? `  ✗ ${fail.length} failed` : '  ✓'));
  fail.slice(0, 4).forEach(x => console.log('    ' + x));
}

await browser.close();
console.log(`\nwork dir: ${work}`);
console.log(results.every(r => r.ok === r.total) ? 'ALL SLIDES CONVERTED' : 'SOME SLIDES FAILED');
