#!/usr/bin/env node
// Wraps bare text (direct text nodes / inline-only runs) inside DIVs into <p>
// tags so html2pptx.js recognizes them as text frames.
//
// Two modes, chosen per-div by its own computed `display`:
//  - flex/grid (inline-flex/inline-grid too): each direct text node AND each
//    direct inline-element child (span/strong/em/...) is wrapped INDIVIDUALLY
//    — merging them would collapse the gap/alignment between flex/grid items
//    (e.g. a `.meta { display:flex; gap:24px }` row of `<span>` pills).
//  - normal flow (block/inline/etc.): consecutive text/inline-node runs are
//    grouped into ONE <p> — this is the correct behaviour for a prose block
//    with inline highlight spans, e.g. `<div>我 <span class="hl">喜欢</span> 你</div>`.
//
// Block-element children (DIV, UL, etc.) are always left alone; they get
// visited and processed themselves via the outer querySelectorAll('div') walk.
import { chromium } from 'playwright';
import fs from 'fs/promises';

async function processFile(browser, filePath) {
  const page = await browser.newPage();
  await page.goto('file://' + filePath);
  const result = await page.evaluate(() => {
    let wrapped = 0;
    const INLINE = new Set(['SPAN','STRONG','EM','B','I','BR','SUP','SUB','A']);
    const FLEXY = new Set(['flex','inline-flex','grid','inline-grid']);

    function isBlockEl(node) {
      return node.nodeType === Node.ELEMENT_NODE && !INLINE.has(node.tagName);
    }

    function wrapAlone(node) {
      const p = document.createElement('p');
      node.parentNode.insertBefore(p, node);
      p.appendChild(node);
      wrapped++;
    }

    function wrapInlineElOwnContent(el) {
      if (!el.textContent.trim()) return;
      if (el.querySelector('p, h1, h2, h3, h4, h5, h6')) return;
      const p = document.createElement('p');
      while (el.firstChild) p.appendChild(el.firstChild);
      el.appendChild(p);
      wrapped++;
    }

    function processDiv(div) {
      if (div.querySelector(':scope > p, :scope > h1, :scope > h2, :scope > h3, :scope > h4, :scope > h5, :scope > h6')) return;
      const display = getComputedStyle(div).display;
      const children = Array.from(div.childNodes);

      if (FLEXY.has(display)) {
        for (const child of children) {
          if (child.nodeType === Node.TEXT_NODE) {
            if (child.textContent.trim()) wrapAlone(child);
          } else if (child.nodeType === Node.ELEMENT_NODE && INLINE.has(child.tagName)) {
            wrapInlineElOwnContent(child);
          }
          // block element children are left alone (own div, processed separately)
        }
        return;
      }

      // Normal-flow: merge consecutive text/inline runs into one <p>.
      let run = [];
      const flush = () => {
        if (!run.length) return;
        const text = run.map(n => n.textContent).join('').trim();
        if (text) {
          const p = document.createElement('p');
          const first = run[0];
          first.parentNode.insertBefore(p, first);
          run.forEach(n => p.appendChild(n));
          wrapped++;
        }
        run = [];
      };
      for (const child of children) {
        if (isBlockEl(child)) {
          flush();
        } else {
          if (child.nodeType === Node.TEXT_NODE && !child.textContent.trim()) continue;
          run.push(child);
        }
      }
      flush();
    }

    const divs = Array.from(document.querySelectorAll('div'));
    for (const div of divs) processDiv(div);
    return { wrapped, html: document.documentElement.outerHTML };
  });
  await page.close();
  return result;
}

async function main() {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error('Usage: node wrap-leaf-text.mjs <file1.html> <file2.html> ...');
    process.exit(1);
  }
  const browser = await chromium.launch();
  for (const f of files) {
    const abs = f.startsWith('/') ? f : process.cwd() + '/' + f;
    const { wrapped, html } = await processFile(browser, abs);
    if (wrapped > 0) {
      const out = '<!DOCTYPE html>\n' + html;
      await fs.writeFile(abs, out, 'utf8');
      console.log(`${f}: wrapped ${wrapped} text run(s)`);
    } else {
      console.log(`${f}: no changes needed`);
    }
  }
  await browser.close();
}
main();
