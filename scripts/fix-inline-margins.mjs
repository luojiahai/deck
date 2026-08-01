#!/usr/bin/env node
// html2pptx.js rejects margin-left/right/top/bottom on inline elements
// (span/strong/em/b/i/a) — "not supported in PowerPoint". This script finds
// which CSS classes are applied to inline elements in each file and rewrites
// margin-* to padding-* ONLY within that class's own rule block (safe: does
// not touch margins on block-level elements elsewhere in the same file).
import { chromium } from 'playwright';
import fs from 'fs/promises';

const INLINE_TAGS = new Set(['SPAN','STRONG','EM','B','I','A']);

async function findInlineClasses(browser, filePath) {
  const page = await browser.newPage();
  await page.goto('file://' + filePath);
  const classes = await page.evaluate((inlineTags) => {
    const found = new Set();
    document.querySelectorAll('*').forEach(el => {
      if (inlineTags.includes(el.tagName)) {
        const cs = getComputedStyle(el);
        const hasMargin = ['marginLeft','marginRight','marginTop','marginBottom']
          .some(k => parseFloat(cs[k]) !== 0);
        if (hasMargin) {
          el.classList.forEach(c => found.add(c));
        }
      }
    });
    return Array.from(found);
  }, Array.from(INLINE_TAGS));
  await page.close();
  return classes;
}

function fixCssForClass(css, className) {
  // Match any selector ending in `.className { ...body... }` — including
  // compound/descendant selectors like `.combo-motif .sepdot { ... }`.
  const re = new RegExp(`([^{}]*\\.${className}\\b[^{]*\\{)([^}]*)(\\})`, 'g');
  return css.replace(re, (m, open, body, close) => {
    const fixedBody = body
      .replace(/margin-(left|right|top|bottom)\s*:/g, 'padding-$1:')
      .replace(/(?<![-\w])margin\s*:/g, 'padding:'); // shorthand `margin: 0 18px` etc.
    return open + fixedBody + close;
  });
}

async function main() {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error('Usage: node fix-inline-margins.mjs <file1.html> ...');
    process.exit(1);
  }
  const browser = await chromium.launch();
  for (const f of files) {
    const abs = f.startsWith('/') ? f : process.cwd() + '/' + f;
    const classes = await findInlineClasses(browser, abs);
    if (!classes.length) {
      console.log(`${f}: no inline-margin classes found`);
      continue;
    }
    let content = await fs.readFile(abs, 'utf8');
    let changed = false;
    for (const cls of classes) {
      const before = content;
      content = fixCssForClass(content, cls);
      if (content !== before) changed = true;
    }
    if (changed) {
      await fs.writeFile(abs, content, 'utf8');
      console.log(`${f}: fixed margin->padding for classes [${classes.join(', ')}]`);
    } else {
      console.log(`${f}: inline classes found but no CSS rule matched: [${classes.join(', ')}]`);
    }
  }
  await browser.close();
}
main();
