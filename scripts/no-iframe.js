#!/usr/bin/env node
/**
 * Replace iframe-based slide loading with direct DOM injection.
 * Applies to all 8 lesson deck files under y7-l10.
 */
const fs = require('fs');
const path = require('path');

const DECK_FILES = [
  'l1-oclock/index.html',
  'l2-minutes/index.html',
  'l3-half-past/index.html',
  'l4-quarters/index.html',
  'l5-minutes-to/index.html',
  'l6-asking-time/index.html',
  'l7-mixed-practice/index.html',
  'l8-review-test-prep/index.html',
];

const BASE = path.join(__dirname, '..', 'index', 'designs', 'y7-l10');

// ── Scoped design tokens injected into parent CSS ──
const TOKENS_CSS = `
  /* ── Scoped design tokens for slide injection ── */
  #frame {
    --bg-primary: #FEFCF7;
    --bg-secondary: #F6F2E8;
    --bg-tertiary: #EDE7D7;
    --text-primary: #1E2A38;
    --text-secondary: #5B6677;
    --text-muted: #8B94A3;
    --accent-gold: #C8943E;
    --accent-gold-light: #E8CD8A;
    --accent-gold-dim: rgba(200, 148, 62, 0.12);
    --accent-teal: #3A7D8C;
    --accent-teal-light: #6BAFB9;
    --accent-teal-dim: rgba(58, 125, 140, 0.10);
    --accent-coral: #D4756B;
    --accent-coral-dim: rgba(212, 117, 107, 0.10);
    --border-light: #E5DFD0;
    --border-medium: #D5CEBB;
    --font-display: 'Noto Serif SC', 'Songti SC', 'STSong', serif;
    --font-body: 'Noto Sans SC', 'PingFang SC', -apple-system, 'Microsoft YaHei', sans-serif;
    --font-mono: 'SF Mono', 'JetBrains Mono', 'Menlo', monospace;
    --space-xs: 8px;
    --space-sm: 16px;
    --space-md: 24px;
    --space-lg: 40px;
    --space-xl: 64px;
    --space-2xl: 96px;
    --radius-sm: 6px;
    --radius-md: 12px;
    --radius-lg: 20px;
    --radius-xl: 28px;
  }
  /* Google Fonts — shared by all slides */
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600;700;900&family=Noto+Sans+SC:wght@400;500;700&display=swap');
`;

// ── Replacement: show() function ──
const NEW_SHOW = `  let loadedFile = null;

  function show(idx) {
    if (idx < 0 || idx >= deck.length) return;
    current = idx;
    const item = deck[idx];
    counter.innerHTML = (idx + 1) + ' / ' + deck.length + ' <span class="label">' + (item.label || '') + '</span>';
    try { localStorage.setItem(storageKey, String(idx)); } catch (_) {}
    if (location.hash !== '#' + (idx + 1)) history.replaceState(null, '', '#' + (idx + 1));

    if (loadedFile !== item.file) {
      loadedFile = item.file;
      fetch(item.file)
        .then(function(r) { return r.text(); })
        .then(function(html) {
          // Extract <style> blocks, rewrite body/html -> #frame
          var styles = '';
          var styleRe = /<style[^>]*>([\\s\\S]*?)<\\/style>/gi;
          var m;
          while ((m = styleRe.exec(html)) !== null) {
            styles += '<style>' + m[1].replace(/\\b(html|body)\\b(?=\\s*[{,])/g, '#frame') + '</style>';
          }
          // Extract <body> content
          var bodyM = html.match(/<body[^>]*>([\\s\\S]*?)<\\/body>/i);
          frame.innerHTML = styles + (bodyM ? bodyM[1] : '');
        })
        .catch(function() {
          frame.innerHTML = '<div style="color:#fff;padding:40px;text-align:center;font-size:24px;">Slide not found</div>';
        });
    }
  }`;

// ── Replacement: makeCard() — uses thumb JPGs ──
const NEW_MAKECARD = `  function makeCard(idx, useScale, useImg) {
    const card = document.createElement('div');
    card.className = 'card'; card.dataset.idx = idx;
    const item = deck[idx];
    // Derive thumb: slides/01-title.html -> thumbs/01-title.jpg
    const thumbPath = item.file.replace(/^slides\\//, 'thumbs/').replace(/\\.html$/, '.jpg');
    if (useImg) {
      const im = document.createElement('img');
      im.className = 'thumb-img'; im.src = thumbPath; im.decoding = 'async';
      im.onerror = function() { im.style.display = 'none'; };
      card.appendChild(im);
    } else {
      const thumb = document.createElement('div');
      thumb.className = 'thumb';
      if (useScale != null) thumb.style.transform = 'scale(' + useScale + ')';
      const img = document.createElement('img');
      img.className = 'thumb-img';
      img.src = thumbPath;
      img.style.position = 'absolute'; img.style.inset = '0';
      img.style.width = '100%'; img.style.height = '100%';
      img.style.objectFit = 'cover';
      img.onerror = function() { img.style.display = 'none'; };
      thumb.appendChild(img); card.appendChild(thumb);
    }
    const num = document.createElement('div');
    num.className = 'num';
    num.textContent = (idx + 1) + (item.label ? ' \\xb7 ' + item.label : '');
    card.appendChild(num);
    card.addEventListener('click', function() { current = idx; setMode('present'); });
    return card;
  }`;

// ── Exact strings to find & replace ──
// The old show() function — matches from "function show" to the line before "function next"
const SHOW_RE = /  function show\(idx\) \{[\s\S]*?\n  \}\n  function next/;

// The old makeCard() function
const MAKECARD_RE = /  function makeCard\(idx, useScale, useImg\) \{[\s\S]*?\n  \}\n\n  function buildOverview/;

// The old print handlers (identical across all files)
const OLD_PRINT = "  window.addEventListener('beforeprint', () => { printStack.innerHTML = ''; deck.forEach(item => { const f = document.createElement('iframe'); f.src = item.file; printStack.appendChild(f); }); printStack.style.display = 'block'; stage.style.display = 'none'; });\n  window.addEventListener('afterprint', () => { printStack.innerHTML = ''; printStack.style.display = 'none'; stage.style.display = ''; });";

const NEW_PRINT = "  window.addEventListener('beforeprint', function() { stage.style.display = 'none'; });\n  window.addEventListener('afterprint', function() { stage.style.display = ''; });";

for (const file of DECK_FILES) {
  const filePath = path.join(BASE, file);
  let html = fs.readFileSync(filePath, 'utf8');
  let changed = 0;

  // 1. Add design tokens CSS (once)
  if (!html.includes('--bg-primary')) {
    html = html.replace('</style>', TOKENS_CSS + '\n</style>');
    changed++;
  }

  // 2. Replace #stage iframe CSS rule
  if (html.includes('#stage iframe')) {
    html = html.replace(/#stage iframe\s*\{[^}]*\}/, '#frame { width: 1920px; height: 1080px; overflow: hidden; position: relative; background: #fff; }');
    changed++;
  }

  // 3. Replace <iframe> element with <div>
  if (html.includes('<iframe id="frame"')) {
    html = html.replace('<div id="stage"><iframe id="frame" src="about:blank"></iframe></div>', '<div id="stage"><div id="frame"></div></div>');
    changed++;
  }

  // 4. Replace show() function
  if (SHOW_RE.test(html)) {
    html = html.replace(SHOW_RE, NEW_SHOW + '\n  function next');
    changed++;
  }

  // 5. Replace makeCard() function
  if (MAKECARD_RE.test(html)) {
    html = html.replace(MAKECARD_RE, NEW_MAKECARD + '\n\n  function buildOverview');
    changed++;
  }

  // 6. Replace print handlers
  if (html.includes(OLD_PRINT)) {
    html = html.replace(OLD_PRINT, NEW_PRINT);
    changed++;
  }

  // 7. Remove scrolling attribute references (leftover from iframe era)
  html = html.replace(/ifr\.setAttribute\('scrolling', 'no'\);\s*/g, '');

  fs.writeFileSync(filePath, html, 'utf8');
  console.log('✓', file, '(' + changed + ' changes)');
}

console.log('\nDone.');
