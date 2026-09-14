#!/usr/bin/env node
/**
 * svg_to_png.mjs — replace inline <svg>…</svg> with <img src="art-N.png">.
 *
 * For the PPTX export copy only. Two reasons the inline SVG cannot stay:
 *   1. html2pptx.js walks elements calling el.className.includes(...), which
 *      throws on SVG nodes (their className is an SVGAnimatedString), so every
 *      slide with a drawing fails to convert.
 *   2. pptxgenjs cannot read an SVG data: URI — it wants a raster file.
 *
 * So each drawing is rendered to a PNG next to the slide and referenced by a
 * relative path. Rendered at 3x the viewBox so it stays crisp on a projector.
 *
 * Usage: node scripts/svg_to_png.mjs <file.html> ...
 */
import fs from 'fs/promises';
import path from 'path';
import sharp from 'sharp';

const SVG = /<svg\b[\s\S]*?<\/svg>/g;
const SCALE = 3;

let total = 0;
for (const file of process.argv.slice(2)) {
  let src = await fs.readFile(file, 'utf8');
  const dir = path.dirname(file);
  const stem = path.basename(file, '.html');
  const jobs = [];
  let i = 0;
  src = src.replace(SVG, (svg) => {
    const vb = /viewBox="([\d.\s-]+)"/.exec(svg);
    const [, , w, h] = vb ? vb[1].trim().split(/\s+/).map(Number) : [0, 0, 220, 210];
    const name = `${stem}-art${i++}.png`;
    jobs.push(sharp(Buffer.from(svg))
      .resize(Math.round(w * SCALE), Math.round(h * SCALE), { fit: 'contain',
        background: { r: 0, g: 0, b: 0, alpha: 0 } })
      .png().toFile(path.join(dir, name)));
    return `<img class="svg-art" src="${name}" alt="">`;
  });
  if (jobs.length) {
    await Promise.all(jobs);
    await fs.writeFile(file, src);
    total += jobs.length;
  }
}
console.log(`rasterised ${total} drawing(s)`);
