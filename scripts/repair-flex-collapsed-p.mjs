#!/usr/bin/env node
// Repairs the specific bug where an earlier wrap pass merged ALL of a
// flex/grid container's inline children (e.g. multiple <span> pills in a
// `.meta { display:flex; gap:24px }` row) into ONE shared <p>, collapsing
// the gap/alignment between them. Detects: a <p> that is the sole child of
// a flex/grid-display parent AND itself contains 2+ element children.
// Fix: unwrap that shared <p>, and instead give each of ITS children (and
// stray text runs between them) their own <p>, restoring them as direct
// flex/grid items of the original parent.
import { chromium } from 'playwright';
import fs from 'fs/promises';

async function processFile(browser, filePath) {
  const page = await browser.newPage();
  await page.goto('file://' + filePath);
  const result = await page.evaluate(() => {
    let repaired = 0;
    const FLEXY = new Set(['flex','inline-flex','grid','inline-grid']);
    const INLINE = new Set(['SPAN','STRONG','EM','B','I','BR','SUP','SUB','A']);

    const containers = Array.from(document.querySelectorAll('div'));
    for (const container of containers) {
      const display = getComputedStyle(container).display;
      if (!FLEXY.has(display)) continue;
      const directPs = Array.from(container.children).filter(c => c.tagName === 'P');
      if (directPs.length !== 1) continue; // only handle the "one shared p ate everything" case
      const p = directPs[0];
      const elementChildren = Array.from(p.children);
      if (elementChildren.length < 2) continue; // not the collapsed-multi-item case

      // Split: move each child node of p back out as a sibling, wrapping
      // bare text runs and inline elements' own content in fresh <p>s.
      const nodes = Array.from(p.childNodes);
      let run = [];
      const flush = () => {
        if (!run.length) return;
        const text = run.map(n => n.textContent).join('').trim();
        if (text) {
          const np = document.createElement('p');
          run.forEach(n => np.appendChild(n));
          container.insertBefore(np, p);
        }
        run = [];
      };
      for (const node of nodes) {
        if (node.nodeType === Node.ELEMENT_NODE && INLINE.has(node.tagName)) {
          flush();
          // wrap this inline element's own content in a <p>, then move the element itself out
          if (node.textContent.trim() && !node.querySelector('p,h1,h2,h3,h4,h5,h6')) {
            const innerP = document.createElement('p');
            while (node.firstChild) innerP.appendChild(node.firstChild);
            node.appendChild(innerP);
          }
          container.insertBefore(node, p);
        } else if (node.nodeType === Node.TEXT_NODE) {
          if (node.textContent.trim()) run.push(node);
        } else {
          flush();
          container.insertBefore(node, p);
        }
      }
      flush();
      p.remove();
      repaired++;
    }
    return { repaired, html: document.documentElement.outerHTML };
  });
  await page.close();
  return result;
}

async function main() {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error('Usage: node repair-flex-collapsed-p.mjs <file1.html> ...');
    process.exit(1);
  }
  const browser = await chromium.launch();
  for (const f of files) {
    const abs = f.startsWith('/') ? f : process.cwd() + '/' + f;
    const { repaired, html } = await processFile(browser, abs);
    if (repaired > 0) {
      await fs.writeFile(abs, '<!DOCTYPE html>\n' + html, 'utf8');
      console.log(`${f}: repaired ${repaired} collapsed flex row(s)`);
    } else {
      console.log(`${f}: no collapsed flex rows found`);
    }
  }
  await browser.close();
}
main();
