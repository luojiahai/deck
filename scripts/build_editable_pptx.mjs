#!/usr/bin/env node
import fs from 'fs/promises';
import path from 'path';
import { pathToFileURL } from 'url';
import { chromium } from 'playwright';
import pptxgen from 'pptxgenjs';

const PX_PER_IN = 144; // 1920px wide source -> 13.333in PowerPoint canvas
const PT_PER_PX = 0.5;

function arg(name) {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 ? process.argv[i + 1] : undefined;
}

const slidesDir = path.resolve(arg('slides') || '');
const outFile = path.resolve(arg('out') || '');
if (!arg('slides') || !arg('out')) {
  console.error('Usage: node scripts/build_editable_pptx.mjs --slides DIR --out FILE.pptx');
  process.exit(2);
}

const rgbHex = (value, fallback = 'FFFFFF') => {
  const m = value?.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
  return m ? m.slice(1, 4).map(n => Number(n).toString(16).padStart(2, '0')).join('').toUpperCase() : fallback;
};

const alphaTransparency = value => {
  const m = value?.match(/rgba\([^,]+,[^,]+,[^,]+,\s*([\d.]+)\)/);
  return m ? Math.round((1 - Number(m[1])) * 100) : 0;
};

const browser = await chromium.launch({ headless: true });
const files = (await fs.readdir(slidesDir)).filter(f => f.endsWith('.html')).sort();
if (!files.length) throw new Error(`No HTML slides in ${slidesDir}`);

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'deck.liyu.dev';
pptx.subject = 'Editable classroom lesson slides';
pptx.company = 'deck.liyu.dev';
pptx.lang = 'zh-CN';
pptx.theme = {
  headFontFace: 'Noto Serif SC',
  bodyFontFace: 'Noto Sans SC',
  lang: 'zh-CN'
};

for (const [index, file] of files.entries()) {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(slidesDir, file)).href, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts?.ready).catch(() => {});

  const data = await page.evaluate(() => {
    const visible = (el, r, cs) => r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden' && Number(cs.opacity) > 0;
    const rect = r => ({ x: r.left, y: r.top, w: r.width, h: r.height });
    const shapes = [];
    const texts = [];
    const textCovered = new Set();
    const tags = new Set(['P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'LI', 'TD', 'TH']);

    for (const el of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if (!visible(el, r, cs)) continue;

      const bg = cs.backgroundColor;
      const borderWidths = [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth].map(parseFloat);
      const hasBg = bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent';
      const hasBorder = borderWidths.some(n => n > 0);
      if (hasBg || hasBorder) {
        shapes.push({
          ...rect(r), bg, opacity: cs.opacity,
          radius: parseFloat(cs.borderRadius) || 0,
          borderColor: cs.borderTopColor,
          borderWidth: Math.max(...borderWidths),
          tag: el.tagName
        });
      }

      if (textCovered.has(el)) continue;
      const directText = [...el.childNodes].some(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim());
      const blockChild = [...el.children].some(c => !['inline', 'inline-block'].includes(getComputedStyle(c).display));
      const isText = tags.has(el.tagName) || (directText && !blockChild);
      if (!isText) continue;
      if (el.closest('table') && !['TD', 'TH'].includes(el.tagName)) continue;

      const text = el.innerText?.replace(/\u00a0/g, ' ').trim();
      if (!text) continue;
      texts.push({
        ...rect(r), text,
        color: cs.color,
        opacity: cs.opacity,
        fontSize: parseFloat(cs.fontSize),
        fontFamily: cs.fontFamily.split(',')[0].replace(/["']/g, '').trim(),
        bold: parseInt(cs.fontWeight) >= 600,
        italic: cs.fontStyle === 'italic',
        align: cs.textAlign,
        lineHeight: parseFloat(cs.lineHeight),
        letterSpacing: parseFloat(cs.letterSpacing) || 0,
        transform: cs.textTransform
      });
      el.querySelectorAll('*').forEach(child => textCovered.add(child));
    }
    return { background: getComputedStyle(document.body).backgroundColor, shapes, texts };
  });

  const slide = pptx.addSlide();
  slide.background = { color: rgbHex(data.background) };

  for (const s of data.shapes) {
    const fillTransparency = Math.max(alphaTransparency(s.bg), Math.round((1 - Number(s.opacity)) * 100));
    const options = {
      x: s.x / PX_PER_IN, y: s.y / PX_PER_IN, w: s.w / PX_PER_IN, h: s.h / PX_PER_IN,
      fill: { color: rgbHex(s.bg), transparency: fillTransparency },
      line: s.borderWidth > 0
        ? { color: rgbHex(s.borderColor, 'D9D9D9'), width: Math.max(0.25, s.borderWidth * PT_PER_PX) }
        : { color: rgbHex(s.bg), transparency: 100 }
    };
    slide.addShape(s.radius > 0 ? pptx.ShapeType.roundRect : pptx.ShapeType.rect, options);
  }

  for (const t of data.texts) {
    let text = t.text;
    if (t.transform === 'uppercase') text = text.toUpperCase();
    const fontSize = Math.max(6, t.fontSize * PT_PER_PX);
    slide.addText(text, {
      x: t.x / PX_PER_IN,
      y: t.y / PX_PER_IN,
      w: Math.max(0.05, t.w / PX_PER_IN + 0.03),
      h: Math.max(0.05, t.h / PX_PER_IN + 0.02),
      fontFace: t.fontFamily || 'Noto Sans SC',
      fontSize,
      color: rgbHex(t.color, '1E2A38'),
      transparency: Math.max(alphaTransparency(t.color), Math.round((1 - Number(t.opacity)) * 100)),
      bold: t.bold,
      italic: t.italic,
      align: ['center', 'right', 'justify'].includes(t.align) ? t.align : 'left',
      valign: 'mid',
      margin: 0,
      breakLine: false,
      fit: 'shrink',
      lineSpacingMultiple: t.lineHeight && t.fontSize ? t.lineHeight / t.fontSize : 1.15,
      charSpacing: t.letterSpacing * PT_PER_PX
    });
  }

  await page.close();
  console.log(`[${index + 1}/${files.length}] ${file}`);
}

await browser.close();
await fs.mkdir(path.dirname(outFile), { recursive: true });
await pptx.writeFile({ fileName: outFile });
console.log(`Wrote ${outFile}`);
