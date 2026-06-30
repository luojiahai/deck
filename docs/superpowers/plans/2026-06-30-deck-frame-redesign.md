# Deck Frame UI Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the Deck gallery homepage (`index/index.html`) as a warm, editorial, type-agnostic design gallery with a light/dark toggle, and extend the manifest with optional `type`/`tags`.

**Architecture:** Single self-contained `index/index.html` (inline `<style>` + `<script>`) reads `index/designs.json` and renders thumbnail-forward cards into a CSS grid. A pre-paint inline script in `<head>` applies the stored/system theme before first paint. No build step, no dependencies — the existing no-build static serve is preserved.

**Tech Stack:** Plain HTML/CSS/vanilla JS. Verification via `python3 -m http.server` + Playwright (already in the repo's local-only `devDependencies`).

## Global Constraints

Every task's requirements implicitly include these (verbatim from the spec):

- **No build step.** Stays a no-build static serve; `index/` must preview correctly via a plain static server. No new files, no new dependencies.
- **Serif stack for display/titles:** `"Songti SC", "Noto Serif SC", "Source Serif 4", Georgia, "Times New Roman", serif`. `system-ui, sans-serif` for small UI/meta (search, chips, tags, count, footer).
- **Light palette:** `--bg:#f4f1ea` `--panel:#fbfaf7` `--card:#ffffff` `--ink:#1f1e1b` `--muted:#6f6e66` `--faint:#a9a79c` `--line:#e7e2d6` `--accent:#d44c2f` `--gold:#b88a3e`.
- **Dark palette:** `--bg:#1b1a17` `--panel:#232220` `--card:#262420` `--ink:#f0ede4` `--muted:#a6a298` `--faint:#75726a` `--line:#34322c` `--accent:#e8704f` `--gold:#d6a85c`.
- **Category colors** (light / dark): slides `#b88a3e`/`#d6a85c`, prototype `#d44c2f`/`#e8704f`, animation `#4a8a72`/`#6cb39a`, app `#3a5a78`/`#6f9cc4`, infographic `#8a5a8c`/`#b98abb`, web `#a9742e`/`#cf9a52`.
- **Count line** reads exactly `N DESIGNS` (uppercase, gold number) with nothing after it when unfiltered.
- **No category legend band** anywhere on the page.
- **Balanced bilingual** copy (Chinese + English) in masthead tagline, search placeholder, footer, and state messages.
- **Untouched:** everything under `index/designs/` and all slides must remain byte-for-byte unchanged.

---

### Task 1: Extend the manifest with `type` and `tags`

**Files:**
- Modify: `index/designs.json`

**Interfaces:**
- Consumes: nothing.
- Produces: the manifest schema the frame reads — each design object MAY include `type` (string, one of `slides|prototype|animation|app|infographic|web`) and `tags` (string[]). Both existing entries set `type: "slides"`.

- [ ] **Step 1: Add `type` and `tags` to both existing entries**

Replace the entire contents of `index/designs.json` with:

```json
{
  "designs": [
    {
      "id": "y7-l10",
      "title": "Y7 L10 · 几点？Telling Time in Chinese",
      "description": "8 节课程幻灯片系列——Year 7 中文时间单元（点·分·半·刻·差·几点·混合·复习），含 3D 概览墙 + 全屏演示",
      "createdAt": "2026-06-28",
      "thumbnail": "designs/y7-l10/thumb.png",
      "type": "slides",
      "tags": ["Year 7", "中文", "Time"]
    },
    {
      "id": "y8-l7",
      "title": "Y8 L7 · 爱好·音乐 Hobbies & Music",
      "description": "8 节课程幻灯片系列——Year 8 中文爱好单元（词汇·一边……一边……·时间长度·拼音·阅读·正在·都·综合写作），含全屏演示",
      "createdAt": "2026-06-30",
      "thumbnail": "designs/y8-l7/thumb.png",
      "type": "slides",
      "tags": ["Year 8", "中文", "Hobbies"]
    }
  ]
}
```

- [ ] **Step 2: Verify the JSON is valid and the new fields are present**

Run:
```bash
python3 -c "import json; d=json.load(open('index/designs.json'))['designs']; assert all(x['type']=='slides' for x in d); assert all(isinstance(x['tags'],list) and x['tags'] for x in d); print('OK', len(d), 'entries')"
```
Expected: `OK 2 entries` (no traceback).

- [ ] **Step 3: Commit**

```bash
git add index/designs.json
git commit -m "feat(frame): add optional type/tags to design manifest"
```

---

### Task 2: Rebuild `index/index.html` (warm gallery + theme toggle + dynamic render)

**Files:**
- Modify: `index/index.html` (full rewrite)
- Test (temporary, scratchpad — not committed): `/private/tmp/claude-501/-Users-luojiahai-Code-deck/f419765b-2213-40e9-b5fe-ee0a9a9bf80a/scratchpad/verify-frame.mjs`

**Interfaces:**
- Consumes: `index/designs.json` with the schema from Task 1 (`id`, `title`, `description`, `createdAt`, `thumbnail`, optional `type`, optional `tags`).
- Produces: the homepage. Key DOM contract the verification relies on — `#count` (count line), `#grid` (cards), `#search` (input), `#theme-toggle` (button), `#empty` / `#no-results` (state blocks), `.design` (card anchor), `.chip[data-type]` (category chip). Theme = `dark` class on `<html>` (`document.documentElement`), persisted in `localStorage['deck-theme']`.

- [ ] **Step 1: Write the complete file**

Replace the entire contents of `index/index.html` with:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Deck — 设计画廊</title>
<script>
  /* Pre-paint theme: stored choice wins, else system preference. Applied before
     first paint to avoid a flash. */
  (function(){
    try{
      var t = localStorage.getItem('deck-theme');
      if(t === 'dark' || (!t && window.matchMedia('(prefers-color-scheme: dark)').matches)){
        document.documentElement.classList.add('dark');
      }
    }catch(e){}
  })();
</script>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root{
    --bg:#f4f1ea; --panel:#fbfaf7; --card:#ffffff;
    --ink:#1f1e1b; --muted:#6f6e66; --faint:#a9a79c; --line:#e7e2d6;
    --accent:#d44c2f; --gold:#b88a3e; --thumb1:#f6f3ee; --thumb2:#ebe6dc;
    --c-slides:#b88a3e; --c-prototype:#d44c2f; --c-animation:#4a8a72;
    --c-app:#3a5a78; --c-infographic:#8a5a8c; --c-web:#a9742e;
  }
  :root.dark{
    --bg:#1b1a17; --panel:#232220; --card:#262420;
    --ink:#f0ede4; --muted:#a6a298; --faint:#75726a; --line:#34322c;
    --accent:#e8704f; --gold:#d6a85c; --thumb1:#2d2a24; --thumb2:#34302a;
    --c-slides:#d6a85c; --c-prototype:#e8704f; --c-animation:#6cb39a;
    --c-app:#6f9cc4; --c-infographic:#b98abb; --c-web:#cf9a52;
  }

  body{
    font-family:"Songti SC","Noto Serif SC","Source Serif 4",Georgia,"Times New Roman",serif;
    background:var(--bg); color:var(--ink); line-height:1.6;
    -webkit-font-smoothing:antialiased; min-height:100vh;
    transition:background .35s, color .35s;
  }
  .wrap{ max-width:1160px; margin:0 auto; padding:0 44px; }

  /* Header */
  header{
    position:sticky; top:0; z-index:5; border-bottom:1px solid var(--line);
    background:color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter:blur(8px);
  }
  header .wrap{ display:flex; align-items:center; gap:20px; padding:15px 44px; }
  .logo{ font-size:21px; font-weight:700; letter-spacing:-.02em; color:var(--ink); text-decoration:none; white-space:nowrap; }
  .logo b{ color:var(--accent); }
  .spacer{ flex:1; }
  .search{ position:relative; width:260px; max-width:100%; }
  .search input{
    width:100%; padding:9px 14px 9px 34px; font-size:13.5px; font-family:system-ui,sans-serif;
    border:1px solid var(--line); border-radius:9px; background:var(--panel); color:var(--ink);
    outline:none; transition:border-color .2s, box-shadow .2s;
  }
  .search input:focus{ border-color:var(--accent); box-shadow:0 0 0 3px rgba(212,76,47,.12); }
  .search input::placeholder{ color:var(--faint); }
  .search .ic{ position:absolute; left:12px; top:50%; transform:translateY(-50%); color:var(--faint); font-size:14px; pointer-events:none; }
  .toggle{
    flex:none; width:38px; height:38px; border-radius:9px; border:1px solid var(--line);
    background:var(--panel); color:var(--muted); font-size:16px; cursor:pointer;
    display:grid; place-items:center; transition:border-color .2s, color .2s;
  }
  .toggle:hover{ border-color:var(--gold); color:var(--gold); }
  .toggle .sun{ display:none; }
  :root.dark .toggle .moon{ display:none; }
  :root.dark .toggle .sun{ display:inline; }

  /* Masthead */
  .mast{ padding:56px 0 36px; }
  .mast .wm{ font-size:60px; font-weight:700; letter-spacing:-.04em; line-height:1; }
  .mast .wm b{ color:var(--accent); }
  .mast .tl{ font-size:16.5px; color:var(--muted); margin-top:14px; font-family:system-ui,sans-serif; }
  .mast .count{ margin-top:16px; font-size:12.5px; color:var(--faint); font-family:system-ui,sans-serif; letter-spacing:.1em; text-transform:uppercase; }
  .mast .count b{ color:var(--gold); font-weight:700; }

  /* Grid + cards */
  .grid{ display:grid; grid-template-columns:repeat(auto-fill, minmax(320px,1fr)); gap:24px; padding-bottom:30px; }
  .design{
    background:var(--card); border:1px solid var(--line); border-radius:15px; overflow:hidden;
    text-decoration:none; color:inherit; display:flex; flex-direction:column;
    box-shadow:0 4px 16px rgba(120,90,40,.05); transition:transform .25s, box-shadow .25s, border-color .25s;
  }
  .design:hover{ transform:translateY(-4px); box-shadow:0 18px 44px rgba(120,90,40,.13); border-color:var(--gold); }
  .tw{
    position:relative; aspect-ratio:16/10; overflow:hidden;
    background:linear-gradient(135deg, var(--thumb1), var(--thumb2));
    display:flex; align-items:center; justify-content:center;
  }
  .tw img{ width:100%; height:100%; object-fit:cover; display:block; }
  .tw .ph{ font-size:13px; color:var(--faint); font-family:system-ui,sans-serif; letter-spacing:.08em; }
  .chip{
    position:absolute; top:11px; left:11px; font-size:10.5px; font-family:system-ui,sans-serif; font-weight:600;
    letter-spacing:.04em; padding:4px 10px; border-radius:999px; color:#fff; background:var(--gold);
  }
  .chip[data-type="slides"]{ background:var(--c-slides); }
  .chip[data-type="prototype"]{ background:var(--c-prototype); }
  .chip[data-type="animation"]{ background:var(--c-animation); }
  .chip[data-type="app"]{ background:var(--c-app); }
  .chip[data-type="infographic"]{ background:var(--c-infographic); }
  .chip[data-type="web"]{ background:var(--c-web); }
  .body{ padding:16px 18px 18px; flex:1; display:flex; flex-direction:column; }
  .body h3{ font-size:17.5px; font-weight:600; letter-spacing:-.01em; line-height:1.32; }
  .body .desc{ font-size:13px; color:var(--muted); margin-top:6px; line-height:1.55; font-family:system-ui,sans-serif; flex:1; }
  .body .foot{ margin-top:14px; display:flex; align-items:baseline; justify-content:space-between; gap:12px; }
  .body .date{ font-size:11.5px; color:var(--faint); font-family:system-ui,sans-serif; letter-spacing:.05em; white-space:nowrap; }
  .body .tags{ font-size:11px; color:var(--faint); font-family:system-ui,sans-serif; text-align:right; }

  /* States */
  .empty{ text-align:center; padding:72px 24px; color:var(--muted); }
  .empty .icon{ font-size:44px; margin-bottom:14px; opacity:.4; }
  .empty h2{ font-size:19px; font-weight:600; color:var(--ink); margin-bottom:8px; }
  .empty p{ font-size:14px; font-family:system-ui,sans-serif; }
  .empty code{ font-family:ui-monospace,monospace; background:var(--panel); padding:1px 6px; border-radius:5px; }
  .hidden{ display:none !important; }

  /* Footer */
  footer{ margin-top:46px; border-top:1px solid var(--line); padding:30px 0 50px; text-align:center; font-size:13px; color:var(--faint); font-family:system-ui,sans-serif; }
  footer b{ color:var(--muted); font-weight:600; }

  @media (max-width:768px){
    .wrap{ padding:0 24px; }
    header .wrap{ padding:14px 24px; gap:12px; }
    .search{ width:auto; flex:1; }
    .mast{ padding:40px 0 28px; }
    .mast .wm{ font-size:46px; }
    .grid{ grid-template-columns:1fr; }
  }
</style>
</head>
<body>

<header>
  <div class="wrap">
    <a href="/" class="logo">Deck<b>.</b></a>
    <div class="spacer"></div>
    <div class="search">
      <span class="ic">⌕</span>
      <input type="text" id="search" placeholder="Search designs 搜索…" autocomplete="off" aria-label="Search designs">
    </div>
    <button class="toggle" id="theme-toggle" type="button" aria-label="Toggle dark mode">
      <span class="moon" aria-hidden="true">☾</span><span class="sun" aria-hidden="true">☀</span>
    </button>
  </div>
</header>

<main class="wrap">
  <section class="mast">
    <div class="wm">Deck<b>.</b></div>
    <div class="tl">用专注做好每一页 · A gallery of crafted HTML designs</div>
    <div class="count" id="count"></div>
  </section>

  <section class="grid" id="grid"></section>

  <div class="empty hidden" id="empty">
    <div class="icon">🎨</div>
    <h2>还没有设计 · No designs yet</h2>
    <p>使用 <code>/huashu-design</code> 创建你的第一个设计</p>
  </div>
  <div class="empty hidden" id="no-results">
    <div class="icon">🔍</div>
    <h2>没有匹配的设计 · No matches</h2>
    <p>试试其他关键词 · Try another keyword</p>
  </div>
</main>

<footer>© 2026 <b>Deck</b> · 用专注做好每一页 · Made with focus</footer>

<script>
(async function(){
  var CATEGORIES = {
    slides:      "Slides 幻灯片",
    prototype:   "Prototype 原型",
    animation:   "Animation 动画",
    app:         "App 应用",
    infographic: "Infographic 信息图",
    web:         "Web 网页"
  };

  var grid = document.getElementById('grid');
  var count = document.getElementById('count');
  var empty = document.getElementById('empty');
  var noResults = document.getElementById('no-results');
  var searchInput = document.getElementById('search');

  function escapeHtml(str){
    var div = document.createElement('div');
    div.textContent = (str == null) ? '' : str;
    return div.innerHTML;
  }

  var designs = [];
  try{
    var resp = await fetch('designs.json');
    var data = await resp.json();
    designs = data.designs || [];
  }catch(e){ designs = []; }

  function matchesQuery(d, q){
    if(!q) return true;
    var hay = [d.title, d.description, d.type, (d.tags||[]).join(' ')].join(' ').toLowerCase();
    return hay.indexOf(q) !== -1;
  }

  function cardHtml(d){
    var type = (d.type && CATEGORIES[d.type]) ? d.type : null;
    var chip = type ? '<span class="chip" data-type="'+type+'">'+escapeHtml(CATEGORIES[type])+'</span>' : '';
    var thumb = d.thumbnail
      ? '<img src="'+escapeHtml(d.thumbnail)+'" alt="'+escapeHtml(d.title)+'" loading="lazy">'
      : '<span class="ph">预览 Preview</span>';
    var tags = (d.tags && d.tags.length) ? escapeHtml(d.tags.join(' · ')) : '';
    return ''
      + '<a class="design" href="designs/'+escapeHtml(d.id)+'/">'
      +   '<div class="tw">'+chip+thumb+'</div>'
      +   '<div class="body">'
      +     '<h3>'+escapeHtml(d.title)+'</h3>'
      +     '<p class="desc">'+escapeHtml(d.description||'')+'</p>'
      +     '<div class="foot"><span class="date">'+escapeHtml(d.createdAt||'')+'</span><span class="tags">'+tags+'</span></div>'
      +   '</div>'
      + '</a>';
  }

  function render(filter){
    var q = (filter||'').toLowerCase().trim();
    var list = designs.filter(function(d){ return matchesQuery(d, q); });

    count.innerHTML = designs.length
      ? (q ? '<b>'+list.length+'</b> / '+designs.length+' DESIGNS'
           : '<b>'+designs.length+'</b> DESIGNS')
      : '';

    empty.classList.toggle('hidden', designs.length > 0);
    noResults.classList.toggle('hidden', designs.length === 0 || list.length > 0);

    grid.innerHTML = list.map(cardHtml).join('');
  }

  searchInput.addEventListener('input', function(){ render(searchInput.value); });
  render();

  /* Theme toggle — initial theme already applied pre-paint in <head>. */
  var toggle = document.getElementById('theme-toggle');
  toggle.addEventListener('click', function(){
    var isDark = document.documentElement.classList.toggle('dark');
    try{ localStorage.setItem('deck-theme', isDark ? 'dark' : 'light'); }catch(e){}
  });
})();
</script>

</body>
</html>
```

- [ ] **Step 2: Write the verification script**

Create `/private/tmp/claude-501/-Users-luojiahai-Code-deck/f419765b-2213-40e9-b5fe-ee0a9a9bf80a/scratchpad/verify-frame.mjs`:

```js
import { chromium } from 'playwright';

const URL = 'http://localhost:8080/';
const OUT = '/private/tmp/claude-501/-Users-luojiahai-Code-deck/f419765b-2213-40e9-b5fe-ee0a9a9bf80a/scratchpad';

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
const errors = [];
page.on('pageerror', e => errors.push(String(e)));

await page.goto(URL, { waitUntil: 'networkidle' });
await page.screenshot({ path: OUT + '/frame-light.png' });

const count = (await page.textContent('#count')).trim();
const cards = await page.$$eval('.design', els => els.length);
const chips = await page.$$eval('.chip[data-type="slides"]', els => els.length);

await page.click('#theme-toggle');
await page.waitForTimeout(450);
const isDark = await page.evaluate(() => document.documentElement.classList.contains('dark'));
await page.screenshot({ path: OUT + '/frame-dark.png' });

await page.reload({ waitUntil: 'networkidle' });
const persisted = await page.evaluate(() => document.documentElement.classList.contains('dark'));

await page.fill('#search', 'zzzzz');
await page.waitForTimeout(150);
const noResultsVisible = await page.evaluate(() => !document.getElementById('no-results').classList.contains('hidden'));
await page.screenshot({ path: OUT + '/frame-noresults.png' });

await page.fill('#search', 'time');
await page.waitForTimeout(150);
const filteredCount = (await page.textContent('#count')).trim();

console.log(JSON.stringify({ count, cards, chips, isDark, persisted, noResultsVisible, filteredCount, errors }, null, 2));
await browser.close();
```

- [ ] **Step 3: Serve the site and run the verification**

Run (from repo root):
```bash
( cd index && python3 -m http.server 8080 >/tmp/deck-serve.log 2>&1 & echo $! > /tmp/deck-serve.pid )
npx playwright install chromium >/dev/null 2>&1
node "/private/tmp/claude-501/-Users-luojiahai-Code-deck/f419765b-2213-40e9-b5fe-ee0a9a9bf80a/scratchpad/verify-frame.mjs"
kill "$(cat /tmp/deck-serve.pid)"
```

Expected JSON output:
```json
{
  "count": "2 DESIGNS",
  "cards": 2,
  "chips": 2,
  "isDark": true,
  "persisted": true,
  "noResultsVisible": true,
  "filteredCount": "1 / 2 DESIGNS",
  "errors": []
}
```
(`chips` 2 = both slides chips rendered; `persisted` true = theme survived reload via `localStorage`; `filteredCount` `1 / 2 DESIGNS` = searching "time" matches only the Telling Time deck; `errors` empty = no console/page errors.)

- [ ] **Step 4: Eyeball the screenshots**

Open `scratchpad/frame-light.png`, `frame-dark.png`, `frame-noresults.png`. Confirm visually:
- Light: warm cream bg, oversized serif `Deck.` masthead with terracotta dot, bilingual tagline, `2 DESIGNS` count, two thumbnail-forward cards each with a gold `Slides 幻灯片` chip top-left, date + tags in the card footer. No legend band.
- Dark: warm near-black bg, legible ink text, chips/gold brighter, sun glyph in the toggle.
- No-results: masthead visible, grid empty, the 🔍 "没有匹配的设计 · No matches" block shown.

If anything is off, fix the CSS/markup in `index/index.html` and re-run Step 3.

- [ ] **Step 5: Confirm designs/ and slides are untouched**

Run:
```bash
git status --porcelain index/designs index/designs/*/slides 2>/dev/null; echo "exit: changed files above (should be empty)"
```
Expected: no lines printed (only `index/index.html` and `index/designs.json` changed in this work).

- [ ] **Step 6: Commit**

```bash
git add index/index.html
git commit -m "feat(frame): rebuild gallery homepage — warm editorial UI, type chips, dark mode"
```

---

## Self-Review

**1. Spec coverage:**
- Warm masthead + `Deck.` wordmark + bilingual tagline + `N DESIGNS` count → Task 2 (markup + render). ✓
- No legend band → Task 2 (omitted by construction; eyeball check Step 4). ✓
- Thumbnail-forward cards + single color-coded type chip + title/desc/date/tags → Task 2 (`cardHtml`, chip CSS). ✓
- Light/dark toggle, respects system pref, persists, no flash → Task 2 (pre-paint `<head>` script + toggle handler; verified `isDark`/`persisted`). ✓
- Search across title/description/type/tags + count update → Task 2 (`matchesQuery`, `render`; verified `filteredCount`). ✓
- Empty + no-results states restyled, bilingual → Task 2 (`#empty`/`#no-results` markup + `.empty` CSS; no-results verified). ✓
- Manifest gains optional `type`/`tags`, existing entries `type: slides`, graceful when absent → Task 1 (data) + Task 2 (`type` guarded by `CATEGORIES[d.type]`, `tags` guarded by length). ✓
- No-build static serve preserved → no `vercel.json`/deps touched; served via `http.server`. ✓
- designs/ and slides byte-for-byte unchanged → Task 2 Step 5 check. ✓

**2. Placeholder scan:** No TBD/TODO; every code step contains the full code; verification steps have exact commands and expected output. ✓

**3. Type consistency:** `CATEGORIES` keys match the `.chip[data-type="…"]` CSS selectors and the manifest `type` values (`slides|prototype|animation|app|infographic|web`). DOM ids used by the verification script (`#count`, `#grid`, `#search`, `#theme-toggle`, `#no-results`, `.design`, `.chip[data-type]`) all exist in the markup. Theme class is on `document.documentElement` consistently in the pre-paint script, the toggle handler, and the CSS (`:root.dark`). ✓
