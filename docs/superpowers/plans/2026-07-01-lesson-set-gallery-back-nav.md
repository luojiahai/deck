# Lesson-Set Gallery Back-to-Deck-Index Navigation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a working "back to main deck index" navigation to each of the 3 lesson-set gallery pages (`y7-l10`, `y8-l7`, `y9-l7`), fix the existing broken footer link, and reposition the floating "back to gallery" button on all 24 lesson slide-deck viewers from top-left to bottom-left.

**Architecture:** Each lesson-set gallery is a single self-contained static HTML file with its own `<style>` block and CSS custom properties (no shared stylesheet, no build step). The gallery fix is purely additive/corrective within each file: one new CSS rule, one new markup element inserted right after `<body>`, and a one-character path fix to an existing `href`. The lesson-deck viewer fix is a single-property CSS change (`top` → `bottom`) repeated identically across 24 files, since their `.list-btn` rule is byte-identical in every file. No JavaScript, no new files, no shared assets.

**Tech Stack:** Static HTML/CSS, no build tooling. Verified with a local static file server (`python3 -m http.server`).

## Global Constraints

- Scope is exactly these 3 files: `index/designs/y7-l10/index.html`, `index/designs/y8-l7/index.html`, `index/designs/y9-l7/index.html`. Do not touch individual lesson pages (`l1-*` … `l8-*`).
- New top-bar link text (verbatim, all 3 files): `← Deck Gallery · 设计画廊`
- New top-bar link target (verbatim, all 3 files): `../../`
- Footer link target fix (verbatim, all 3 files): change `href="../"` to `href="../../"` on the existing "← Back to Gallery" link — do not change its visible text.
- Styling must reuse each file's own existing CSS custom properties (`--text-muted`, `--accent`, `--border`) — do not introduce new colors or a shared stylesheet.
- The top bar must sit inside the existing `.container` class (max-width 1200px) so it aligns with the hero content below it.
- Lesson-deck viewer `.list-btn` reposition is scoped to exactly these 24 files (do not touch files under `slides/`):
  `index/designs/y7-l10/l1-oclock/index.html`, `l2-minutes/index.html`, `l3-half-past/index.html`, `l4-quarters/index.html`, `l5-minutes-to/index.html`, `l6-asking-time/index.html`, `l7-mixed-practice/index.html`, `l8-review-test-prep/index.html`;
  `index/designs/y8-l7/l1-hobby-vocab/index.html`, `l2-text1-yibian/index.html`, `l3-duration/index.html`, `l4-pinyin-listening/index.html`, `l5-art-vocab-text2/index.html`, `l6-zhengzai/index.html`, `l7-dou/index.html`, `l8-characters-review/index.html`;
  `index/designs/y9-l7/l1-subjects/index.html`, `l2-opinions/index.html`, `l3-interest-reasons/index.html`, `l4-characters-interview/index.html`, `l5-text2-vocab/index.html`, `l6-tests-duration/index.html`, `l7-complement-numbers/index.html`, `l8-review-test-prep/index.html`.
- `.list-btn` change (verbatim, all 24 files): in the rule `.list-btn { position: fixed; top: 20px; left: 20px; ... }`, change `top: 20px;` to `bottom: 20px;`. No other property, no markup, and no `href` changes.

---

### Task 1: Fix navigation in `y7-l10/index.html`

**Files:**
- Modify: `index/designs/y7-l10/index.html:243` (CSS, insert before the `/* ── Footer ── */` comment block)
- Modify: `index/designs/y7-l10/index.html:314` (markup, right after `<body>`)
- Modify: `index/designs/y7-l10/index.html:431` (footer link href)

**Interfaces:** None — this is a leaf, self-contained static file. No other task depends on the markup/CSS class names chosen here (each file gets its own independent copy).

- [ ] **Step 1: Add the `.top-nav` CSS rule**

In `index/designs/y7-l10/index.html`, find this block (around line 241-249):

```css

  /* ── Footer ── */
  footer {
    border-top: 1px solid var(--border);
    padding: 32px 0;
    font-size: 14px;
    color: var(--text-muted);
    letter-spacing: 0.04em;
  }
```

Replace it with (adds a new `.top-nav` rule before the existing footer rule, leaves the footer rule unchanged):

```css

  /* ── Top nav ── */
  .top-nav { border-bottom: 1px solid var(--border); padding: 12px 0; }
  .top-nav a { font-size: 13px; letter-spacing: 0.06em; color: var(--text-muted); text-decoration: none; }
  .top-nav a:hover { color: var(--accent); }

  /* ── Footer ── */
  footer {
    border-top: 1px solid var(--border);
    padding: 32px 0;
    font-size: 14px;
    color: var(--text-muted);
    letter-spacing: 0.04em;
  }
```

- [ ] **Step 2: Insert the top-nav bar markup right after `<body>`**

Find (around line 314-317):

```html
<body>

<!-- ════════ Hero ════════ -->
<section class="hero">
```

Replace with:

```html
<body>

<div class="top-nav">
  <div class="container">
    <a href="../../">← Deck Gallery · 设计画廊</a>
  </div>
</div>

<!-- ════════ Hero ════════ -->
<section class="hero">
```

- [ ] **Step 3: Fix the footer link href**

Find (around line 429-433):

```html
<footer>
  <div class="container">
    Y7 Chinese · Unit 4.1 Telling Time · 8-lesson deck series · <a href="../">← Back to Gallery</a>
  </div>
</footer>
```

Replace with:

```html
<footer>
  <div class="container">
    Y7 Chinese · Unit 4.1 Telling Time · 8-lesson deck series · <a href="../../">← Back to Gallery</a>
  </div>
</footer>
```

- [ ] **Step 4: Verify the hrefs**

Run:

```bash
grep -n 'href="\.\./\.\./"' index/designs/y7-l10/index.html
```

Expected: 2 matches (the new top-nav link and the fixed footer link).

- [ ] **Step 5: Commit**

```bash
git add index/designs/y7-l10/index.html
git commit -m "fix(y7-l10): add top-nav back link and fix broken footer gallery link"
```

---

### Task 2: Fix navigation in `y8-l7/index.html`

**Files:**
- Modify: `index/designs/y8-l7/index.html:56` (CSS, insert before the `footer { ... }` line)
- Modify: `index/designs/y8-l7/index.html:80` (markup, right after `<body>`)
- Modify: `index/designs/y8-l7/index.html:223` (footer link href)

**Interfaces:** None — same as Task 1, independent self-contained file.

- [ ] **Step 1: Add the `.top-nav` CSS rule**

Find (around line 56-57):

```css
  footer { border-top: 1px solid var(--border); padding: 32px 0; font-size: 14px; color: var(--text-muted); letter-spacing: 0.04em; }
  footer a { color: var(--accent); text-decoration: none; }
```

Replace with:

```css
  .top-nav { border-bottom: 1px solid var(--border); padding: 12px 0; }
  .top-nav a { font-size: 13px; letter-spacing: 0.06em; color: var(--text-muted); text-decoration: none; }
  .top-nav a:hover { color: var(--accent); }
  footer { border-top: 1px solid var(--border); padding: 32px 0; font-size: 14px; color: var(--text-muted); letter-spacing: 0.04em; }
  footer a { color: var(--accent); text-decoration: none; }
```

- [ ] **Step 2: Insert the top-nav bar markup right after `<body>`**

Find (around line 80-82):

```html
<body>

<section class="hero">
```

Replace with:

```html
<body>

<div class="top-nav">
  <div class="container">
    <a href="../../">← Deck Gallery · 设计画廊</a>
  </div>
</div>

<section class="hero">
```

- [ ] **Step 3: Fix the footer link href**

Find (around line 221-225):

```html
<footer>
  <div class="container">
    Y8 Chinese · Unit 3 Hobbies 爱好 · 8-lesson deck series · <a href="../">← Back to Gallery</a>
  </div>
</footer>
```

Replace with:

```html
<footer>
  <div class="container">
    Y8 Chinese · Unit 3 Hobbies 爱好 · 8-lesson deck series · <a href="../../">← Back to Gallery</a>
  </div>
</footer>
```

- [ ] **Step 4: Verify the hrefs**

Run:

```bash
grep -n 'href="\.\./\.\./"' index/designs/y8-l7/index.html
```

Expected: 2 matches.

- [ ] **Step 5: Commit**

```bash
git add index/designs/y8-l7/index.html
git commit -m "fix(y8-l7): add top-nav back link and fix broken footer gallery link"
```

---

### Task 3: Fix navigation in `y9-l7/index.html`

**Files:**
- Modify: `index/designs/y9-l7/index.html:60` (CSS, insert before the `footer { ... }` line)
- Modify: `index/designs/y9-l7/index.html:70` (markup, right after `<body>`)
- Modify: `index/designs/y9-l7/index.html:203` (footer link href)

**Interfaces:** None — same as Task 1, independent self-contained file.

- [ ] **Step 1: Add the `.top-nav` CSS rule**

Find (around line 60-61):

```css
  footer { border-top: 1px solid var(--border); padding: 32px 0; font-size: 14px; color: var(--text-muted); letter-spacing: 0.04em; }
  footer a { color: var(--accent); text-decoration: none; }
```

Replace with:

```css
  .top-nav { border-bottom: 1px solid var(--border); padding: 12px 0; }
  .top-nav a { font-size: 13px; letter-spacing: 0.06em; color: var(--text-muted); text-decoration: none; }
  .top-nav a:hover { color: var(--accent); }
  footer { border-top: 1px solid var(--border); padding: 32px 0; font-size: 14px; color: var(--text-muted); letter-spacing: 0.04em; }
  footer a { color: var(--accent); text-decoration: none; }
```

- [ ] **Step 2: Insert the top-nav bar markup right after `<body>`**

Find (around line 70-72):

```html
<body>

<section class="hero">
```

Replace with:

```html
<body>

<div class="top-nav">
  <div class="container">
    <a href="../../">← Deck Gallery · 设计画廊</a>
  </div>
</div>

<section class="hero">
```

- [ ] **Step 3: Fix the footer link href**

Find (around line 201-205):

```html
<footer>
  <div class="container">
    Y9 Chinese · Unit 3 School Life 学校生活 · 8-lesson deck series · <a href="../">← Back to Gallery</a>
  </div>
</footer>
```

Replace with:

```html
<footer>
  <div class="container">
    Y9 Chinese · Unit 3 School Life 学校生活 · 8-lesson deck series · <a href="../../">← Back to Gallery</a>
  </div>
</footer>
```

- [ ] **Step 4: Verify the hrefs**

Run:

```bash
grep -n 'href="\.\./\.\./"' index/designs/y9-l7/index.html
```

Expected: 2 matches.

- [ ] **Step 5: Commit**

```bash
git add index/designs/y9-l7/index.html
git commit -m "fix(y9-l7): add top-nav back link and fix broken footer gallery link"
```

---

### Task 4: Reposition the back button on all 24 lesson-deck viewers

**Files:**
- Modify (one CSS property each, 24 files total): all 24 lesson-deck viewer `index.html` files listed in Global Constraints above, e.g. `index/designs/y7-l10/l1-oclock/index.html` … `index/designs/y9-l7/l8-review-test-prep/index.html`.

**Interfaces:** None — independent of Tasks 1-3 (different files, different component). No other task depends on this change.

Every file has the byte-identical CSS rule `.list-btn { position: fixed; top: 20px; left: 20px; background: rgba(0,0,0,0.55); color: rgba(255,255,255,0.85); border: 0; padding: 7px 14px; border-radius: 999px; font-size: 13px; font-family: inherit; cursor: pointer; z-index: 100; opacity: 0.6; text-decoration: none; display: block; }` (verified by `grep` across all 24 files before writing this plan), so the fix is a single repeated `sed` substitution rather than 24 hand-edits.

- [ ] **Step 1: Confirm all 24 files still match the expected rule (pre-condition check)**

```bash
grep -l '\.list-btn { position: fixed; top: 20px; left: 20px;' index/designs/*/l*/index.html | wc -l
```

Expected: `24`

- [ ] **Step 2: Apply the `top` → `bottom` substitution to all 24 files**

```bash
for f in index/designs/*/l*/index.html; do
  sed -i '' 's/\.list-btn { position: fixed; top: 20px; left: 20px;/.list-btn { position: fixed; bottom: 20px; left: 20px;/' "$f"
done
```

- [ ] **Step 3: Verify the substitution**

```bash
grep -l '\.list-btn { position: fixed; bottom: 20px; left: 20px;' index/designs/*/l*/index.html | wc -l
grep -l '\.list-btn { position: fixed; top: 20px; left: 20px;' index/designs/*/l*/index.html | wc -l
```

Expected: first command outputs `24`, second command outputs `0` (no files left with the old `top: 20px` rule).

- [ ] **Step 4: Spot-check the markup and href are untouched**

```bash
grep -n 'class="list-btn"' index/designs/y9-l7/l1-subjects/index.html
```

Expected: `<a class="list-btn" href="../">← 列表</a>` — unchanged from before.

- [ ] **Step 5: Commit**

```bash
git add index/designs/*/l*/index.html
git commit -m "fix(slides): reposition lesson-deck back button to bottom-left footer toolbar"
```

---

### Task 5: Manual cross-design smoke test

**Files:** None (verification only — reads the 3 files modified in Tasks 1-3 and the 24 files modified in Task 4).

**Interfaces:** Consumes the `.top-nav` markup/CSS and fixed footer `href` produced by Tasks 1-3 in all 3 gallery files, and the repositioned `.list-btn` produced by Task 4 in all 24 lesson-deck viewer files.

- [ ] **Step 1: Start a local static server**

```bash
cd index && python3 -m http.server 8080
```

- [ ] **Step 2: Visually check each lesson-set gallery**

Open each URL in a browser and confirm: the new top bar renders above the hero with no overlap, the bar's left edge aligns with the hero content's left edge, and the bar text reads `← Deck Gallery · 设计画廊`:

- `http://localhost:8080/designs/y7-l10/`
- `http://localhost:8080/designs/y8-l7/`
- `http://localhost:8080/designs/y9-l7/`

- [ ] **Step 3: Click both back links on each page**

On each of the 3 pages, click the new top-nav link, confirm it lands on `http://localhost:8080/` (the main deck gallery). Go back, scroll to the footer, click "← Back to Gallery", confirm it also lands on `http://localhost:8080/`.

- [ ] **Step 4: Visually check one lesson-deck viewer per series**

Open one lesson viewer per series and confirm the back button now sits bottom-left (not top-left), does not overlap the bottom-right "1 / N" counter pill, and clicking it lands back on the lesson-set gallery:

- `http://localhost:8080/designs/y7-l10/l1-oclock/`
- `http://localhost:8080/designs/y8-l7/l1-hobby-vocab/`
- `http://localhost:8080/designs/y9-l7/l1-subjects/`

- [ ] **Step 5: Stop the server**

Stop the `python3 -m http.server` process (Ctrl-C in its terminal, or kill the background job if run with `run_in_background`).

No commit for this task — it's verification only, nothing to stage.
