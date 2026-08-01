#!/usr/bin/env node
/**
 * export-deck-pptx-1920.mjs — editable PPTX export for this repo's 1920×1080
 * slide decks (deck.liyu.dev design gallery convention, see CLAUDE.md).
 *
 * Identical to the huashu-design skill's export_deck_pptx.mjs, except the
 * PPTX presentation layout is declared at 20in × 11.25in (1920×1080px @ 96dpi)
 * instead of the skill's hardcoded LAYOUT_WIDE (13.333in × 7.5in / 960×540pt).
 * This repo's slide HTML is locked to 1920×1080 by shared/tokens.css, so this
 * script — not the skill's stock one — is the one to use for every deck here.
 *
 * Usage: node scripts/export-deck-pptx-1920.mjs --slides <dir> --out <file.pptx>
 *
 * Slides must still satisfy html2pptx.js's other 3 constraints (no CSS
 * gradients, no background-image on divs, text wrapped in <p>/<h1-6>).
 */
import pptxgen from 'pptxgenjs';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const SKILL_SCRIPTS = '/Users/luojiahai/code/deck/.claude/skills/huashu-design/scripts';
const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs() {
  const args = {};
  const a = process.argv.slice(2);
  for (let i = 0; i < a.length; i += 2) {
    const k = a[i].replace(/^--/, '');
    args[k] = a[i + 1];
  }
  if (!args.slides || !args.out) {
    console.error('用法: node export-deck-pptx-1920.mjs --slides <dir> --out <file.pptx>');
    process.exit(1);
  }
  return args;
}

async function main() {
  const { slides, out } = parseArgs();
  const slidesDir = path.resolve(slides);
  const outFile = path.resolve(out);

  const files = (await fs.readdir(slidesDir))
    .filter(f => f.endsWith('.html'))
    .sort();
  if (!files.length) {
    console.error(`No .html files found in ${slidesDir}`);
    process.exit(1);
  }

  console.log(`Converting ${files.length} slides via html2pptx (1920×1080 layout)...`);

  const { createRequire } = await import('module');
  const require = createRequire(import.meta.url);
  const html2pptx = require(path.join(SKILL_SCRIPTS, 'html2pptx.js'));
  const { fixPptx } = await import(path.join(SKILL_SCRIPTS, 'fix_pptx_duplicate_ppr.mjs'));

  const pres = new pptxgen();
  pres.defineLayout({ name: 'CANVAS_1920x1080', width: 20, height: 11.25 });
  pres.layout = 'CANVAS_1920x1080';

  const errors = [];
  for (let i = 0; i < files.length; i++) {
    const f = files[i];
    const fullPath = path.join(slidesDir, f);
    try {
      await html2pptx(fullPath, pres);
      console.log(`  [${i + 1}/${files.length}] ${f} ✓`);
    } catch (e) {
      console.error(`  [${i + 1}/${files.length}] ${f} ✗  ${e.message}`);
      errors.push({ file: f, error: e.message });
    }
  }

  if (errors.length) {
    console.error(`\n⚠️ ${errors.length} 张 slide 转换失败。`);
    if (errors.length === files.length) {
      console.error(`✗ 全部失败，不生成 PPTX。`);
      process.exit(1);
    }
  }

  await pres.writeFile({ fileName: outFile });

  const { totalFixed } = await fixPptx(outFile);
  if (totalFixed > 0) {
    console.log(`  ↳ repaired ${totalFixed} paragraph(s) with duplicate <a:pPr> (Windows-乱码 fix)`);
  }

  console.log(`\n✓ Wrote ${outFile}  (${files.length - errors.length}/${files.length} slides, 可编辑 PPTX, 1920×1080)`);
}

main().catch(e => { console.error(e); process.exit(1); });
