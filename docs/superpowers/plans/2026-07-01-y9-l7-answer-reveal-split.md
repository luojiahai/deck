# Y9-L7 Answer-Reveal Split Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the 8 flagged y9-l7 slides so answers/corrections/translations never appear on the same slide as the question — each gets a new gold-accented `Xb-...-answers.html` reveal slide shown immediately after it, matching the deck's existing `07b-text1-answers.html` / `08b-cfu-answers.html` / `07b-cfu-answers.html` convention.

**Architecture:** Each affected lesson is a static HTML deck (`index/designs/y9-l7/<lesson>/`) driven by a `DECK_MANIFEST` array in that lesson's `index.html`. Slides are self-contained HTML files under `slides/`. No build step, no test framework — this repo is design HTML reviewed visually. "Testing" a task means: grep-verifying the answer content was actually removed from the original slide and is present in the new slide, and that the manifest references the new file.

**Tech Stack:** Plain HTML/CSS, no JS framework. Shared tokens at `index/designs/y9-l7/shared/tokens.css`.

## Global Constraints

- Every new answer slide is named `<same-number>b-<original-basename-without-number>-answers.html`, e.g. `11-game.html` → `11b-game-answers.html`. This exactly matches the existing `07-text1.html` → `07b-text1-answers.html` pattern in this repo.
- New answer slides use: gold accent line (`background:var(--accent-gold);` on `.accent-line` inline override, matching `09b-cfu-answers.html` and `08b-cfu-answers.html`), `section-name` ending in `↳`, `section-label` reading `Answers Revealed · 答案`, `main-title` reading `答案 · <original main-title text>`.
- Every edited original slide that loses inline answer content gets a cue element in the same dashed-border `.answer-hidden` style used in `l1-subjects/slides/09-cfu.html` (`border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:10px 18px; color:var(--text-muted); font-style:italic; font-size:15px; opacity:0.5;`), with text `答案见下一张 · Answers on next slide →`.
- Every manifest insertion uses the existing label format: two leading spaces, `↳ Answers · <short label>` (copy the exact string style from `l2-opinions/index.html:15`: `"  ↳ Answers · Text 1 Comprehension"`).
- Do not touch any slide, file, or manifest entry not explicitly listed in this plan.
- Do not modify `shared/tokens.css`.

---

### Task 1: L2-11 game — split wrong/correct cards

**Files:**
- Modify: `index/designs/y9-l7/l2-opinions/slides/11-game.html`
- Create: `index/designs/y9-l7/l2-opinions/slides/11b-game-answers.html`
- Modify: `index/designs/y9-l7/l2-opinions/index.html:19`

**Interfaces:** None (static HTML, no shared interfaces between tasks).

- [ ] **Step 1: Remove the 4 correct-answer rows from the original slide**

In `index/designs/y9-l7/l2-opinions/slides/11-game.html`, each of the 4 `.error-card` blocks currently has this shape:

```html
    <div class="error-card card1">
      <div class="ec-num" style="color:var(--accent-coral);">Error 1</div>
      <div class="ec-wrong-row">
        <div class="ec-wrong-badge">✗ Wrong</div>
        <div class="ec-wrong-text">我很难学觉得数学。</div>
      </div>
      <div class="ec-arrow">↓</div>
      <div class="ec-correct-row">
        <div class="ec-correct-badge">✓ Correct</div>
        <div class="ec-correct-text">我觉得数学很难学。</div>
      </div>
    </div>
```

Remove the `.ec-arrow` and `.ec-correct-row` divs from all 4 cards, leaving only `ec-num` + `ec-wrong-row`. After editing, each card looks like:

```html
    <div class="error-card card1">
      <div class="ec-num" style="color:var(--accent-coral);">Error 1</div>
      <div class="ec-wrong-row">
        <div class="ec-wrong-badge">✗ Wrong</div>
        <div class="ec-wrong-text">我很难学觉得数学。</div>
      </div>
    </div>
```

Apply the same removal to cards 2 (`汉字容易不写。`), 3 (`英语很我觉得有用。`), 4 (`物理写难不容易。`).

Then replace the `.instructions-row` block:

```html
  <div class="instructions-row">
    <div class="inst-icon">✍️</div>
    <div class="inst-box">
      Project errors <strong>one at a time</strong> — students write correction in books, then reveal answer.
      Class compares: <strong>👍 = agreed · 👎 = still wrong, discuss</strong>
    </div>
  </div>
```

with:

```html
  <div class="instructions-row">
    <div class="inst-icon">✍️</div>
    <div class="inst-box">
      Project errors <strong>one at a time</strong> — students write correction in books.
    </div>
  </div>
  <div class="answer-hidden">答案见下一张 · Answers on next slide →</div>
```

Add the `.answer-hidden` CSS rule to the `<style>` block (insert after the `.inst-icon` rule):

```css
  .answer-hidden { border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:10px 18px; color:var(--text-muted); font-style:italic; font-size:15px; opacity:0.5; margin-top:10px; }
```

- [ ] **Step 2: Verify the corrections are gone**

Run: `grep -c "ec-correct-row" index/designs/y9-l7/l2-opinions/slides/11-game.html`
Expected: `0`

Run: `grep -c "answer-hidden" index/designs/y9-l7/l2-opinions/slides/11-game.html`
Expected: `2` (one CSS rule, one usage)

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l2-opinions/slides/11b-game-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L2-11b · Game Answers · Correct the Teacher</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:36px 100px 32px; }
  .section-label { font-size:15px; font-weight:700; letter-spacing:0.14em; color:var(--accent-gold); text-transform:uppercase; margin-bottom:8px; }
  .main-title { font-family:var(--font-display); font-size:50px; font-weight:900; margin-bottom:6px; }
  .errors-grid { display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:18px; }
  .error-card { border-radius:var(--radius-lg); padding:22px 26px; border:2px solid; }
  .error-card.card1 { background:rgba(201,106,92,0.04); border-color:var(--border-light); }
  .ec-num { font-size:13px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:10px; color:var(--accent-coral); }
  .ec-wrong-row { display:flex; align-items:center; gap:12px; margin-bottom:8px; }
  .ec-wrong-badge { background:var(--accent-coral-dim); border:1.5px solid var(--accent-coral); border-radius:var(--radius-sm); padding:3px 12px; font-size:13px; font-weight:700; color:var(--accent-coral); letter-spacing:0.06em; flex-shrink:0; }
  .ec-wrong-text { font-family:var(--font-display); font-size:28px; font-weight:700; color:var(--accent-coral); text-decoration:line-through; text-decoration-color:rgba(201,106,92,0.5); }
  .ec-arrow { text-align:center; font-size:22px; color:var(--text-muted); margin:4px 0; }
  .ec-correct-row { display:flex; align-items:center; gap:12px; }
  .ec-correct-badge { background:var(--accent-teal-dim); border:1.5px solid var(--accent-teal); border-radius:var(--radius-sm); padding:3px 12px; font-size:13px; font-weight:700; color:var(--accent-teal); letter-spacing:0.06em; flex-shrink:0; }
  .ec-correct-text { font-family:var(--font-display); font-size:28px; font-weight:700; color:var(--accent-teal); }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L2 · 我觉得</span>
  <span class="sep"></span>
  <span class="section-name">Game · Correct the Teacher ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">
  <div class="section-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · 改正老师的错误！</div>

  <div class="errors-grid">
    <div class="error-card card1">
      <div class="ec-num">Error 1</div>
      <div class="ec-wrong-row">
        <div class="ec-wrong-badge">✗ Wrong</div>
        <div class="ec-wrong-text">我很难学觉得数学。</div>
      </div>
      <div class="ec-arrow">↓</div>
      <div class="ec-correct-row">
        <div class="ec-correct-badge">✓ Correct</div>
        <div class="ec-correct-text">我觉得数学很难学。</div>
      </div>
    </div>

    <div class="error-card card1">
      <div class="ec-num">Error 2</div>
      <div class="ec-wrong-row">
        <div class="ec-wrong-badge">✗ Wrong</div>
        <div class="ec-wrong-text">汉字容易不写。</div>
      </div>
      <div class="ec-arrow">↓</div>
      <div class="ec-correct-row">
        <div class="ec-correct-badge">✓ Correct</div>
        <div class="ec-correct-text">汉字不容易写。</div>
      </div>
    </div>

    <div class="error-card card1">
      <div class="ec-num">Error 3</div>
      <div class="ec-wrong-row">
        <div class="ec-wrong-badge">✗ Wrong</div>
        <div class="ec-wrong-text">英语很我觉得有用。</div>
      </div>
      <div class="ec-arrow">↓</div>
      <div class="ec-correct-row">
        <div class="ec-correct-badge">✓ Correct</div>
        <div class="ec-correct-text">我觉得英语很有用。</div>
      </div>
    </div>

    <div class="error-card card1">
      <div class="ec-num">Error 4</div>
      <div class="ec-wrong-row">
        <div class="ec-wrong-badge">✗ Wrong</div>
        <div class="ec-wrong-text">物理写难不容易。</div>
      </div>
      <div class="ec-arrow">↓</div>
      <div class="ec-correct-row">
        <div class="ec-correct-badge">✓ Correct</div>
        <div class="ec-correct-text">物理很难学，也不容易写。</div>
      </div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l2-opinions/index.html`, find line 19:

```js
    { file: "slides/11-game.html",         label: "Game · Correct the Teacher (38–43 min)" },
```

Add immediately after it:

```js
    { file: "slides/11b-game-answers.html", label: "  ↳ Answers · Correct the Teacher" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "11b-game-answers" index/designs/y9-l7/l2-opinions/index.html`
Expected: `1`

Run: `python3 -c "import sys; from html.parser import HTMLParser; HTMLParser().feed(open('index/designs/y9-l7/l2-opinions/slides/11b-game-answers.html').read())"`
Expected: no error (valid HTML, parses without exception)

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l2-opinions/slides/11-game.html index/designs/y9-l7/l2-opinions/slides/11b-game-answers.html index/designs/y9-l7/l2-opinions/index.html
git commit -m "fix(y9-l7): split L2 game answers into next-slide reveal"
```

---

### Task 2: L3-11 game — split error-correction table

**Files:**
- Modify: `index/designs/y9-l7/l3-interest-reasons/slides/11-game.html`
- Create: `index/designs/y9-l7/l3-interest-reasons/slides/11b-game-answers.html`
- Modify: `index/designs/y9-l7/l3-interest-reasons/index.html:19`

- [ ] **Step 1: Remove the correction column from the original table**

In `index/designs/y9-l7/l3-interest-reasons/slides/11-game.html`, the table currently is:

```html
  <table class="game-table">
    <thead>
      <tr>
        <th class="wrong-h">&#10060; Error (Teacher says…)</th>
        <th></th>
        <th class="correct-h">&#10003; Correction</th>
      </tr>
    </thead>
    <tbody>
      <tr class="game-row">
        <td>我<span class="diff-wrong">在</span>历史很感兴趣。</td>
        <td>→</td>
        <td>我<span class="diff-correct">对</span>历史很感兴趣。</td>
      </tr>
      <tr class="game-row">
        <td>我对音乐感兴趣<span class="diff-wrong">很</span>。</td>
        <td>→</td>
        <td>我对音乐<span class="diff-correct">很</span>感兴趣。</td>
      </tr>
      <tr class="game-row">
        <td><span class="diff-wrong">所以</span>我喜欢化学。</td>
        <td>→</td>
        <td><span class="diff-correct">因为</span>我觉得化学很有意思，<span class="diff-correct">所以</span>我喜欢化学。</td>
      </tr>
      <tr class="game-row">
        <td style="font-size:22px;">因为老师对我很好，<span class="diff-wrong">我</span>喜欢上历史课。</td>
        <td>→</td>
        <td style="font-size:22px;">因为老师对我很好，<span class="diff-correct">所以</span>我喜欢上历史课。</td>
      </tr>
      <tr class="game-row">
        <td>我对数学<span class="diff-wrong">有很大兴趣</span>。</td>
        <td>→</td>
        <td>我对数学<span class="diff-correct">很感兴趣</span>。</td>
      </tr>
    </tbody>
  </table>
```

Replace it with a single-column version (drop the `→` column and the correction column, drop the `correct-h` header):

```html
  <table class="game-table">
    <thead>
      <tr>
        <th class="wrong-h">&#10060; Error (Teacher says…)</th>
      </tr>
    </thead>
    <tbody>
      <tr class="game-row">
        <td>我<span class="diff-wrong">在</span>历史很感兴趣。</td>
      </tr>
      <tr class="game-row">
        <td>我对音乐感兴趣<span class="diff-wrong">很</span>。</td>
      </tr>
      <tr class="game-row">
        <td><span class="diff-wrong">所以</span>我喜欢化学。</td>
      </tr>
      <tr class="game-row">
        <td style="font-size:22px;">因为老师对我很好，<span class="diff-wrong">我</span>喜欢上历史课。</td>
      </tr>
      <tr class="game-row">
        <td>我对数学<span class="diff-wrong">有很大兴趣</span>。</td>
      </tr>
    </tbody>
  </table>
  <div class="answer-hidden">答案见下一张 · Answers on next slide →</div>
```

Add the `.answer-hidden` rule to the `<style>` block (insert after `.timer-text`):

```css
  .answer-hidden { border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:10px 18px; color:var(--text-muted); font-style:italic; font-size:15px; opacity:0.5; margin-top:12px; }
```

- [ ] **Step 2: Verify the corrections are gone**

Run: `grep -c "diff-correct" index/designs/y9-l7/l3-interest-reasons/slides/11-game.html`
Expected: `0`

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l3-interest-reasons/slides/11b-game-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L3-11b · Game Answers · Correct the Teacher</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:36px 100px 32px; }
  .section-label { font-size:16px; font-weight:700; letter-spacing:0.14em; color:var(--accent-gold); text-transform:uppercase; margin-bottom:10px; }
  .main-title { font-family:var(--font-display); font-size:44px; font-weight:900; margin-bottom:20px; }
  .game-table { width:100%; border-collapse:separate; border-spacing:0 10px; }
  .game-table th { font-size:14px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; padding:8px 20px; color:var(--text-muted); text-align:left; }
  .game-table th.wrong-h { color:var(--accent-coral); }
  .game-table th.correct-h { color:var(--accent-teal); }
  .game-row td { padding:14px 20px; font-family:var(--font-display); font-size:26px; font-weight:700; vertical-align:middle; }
  .game-row td:first-child { border-radius:var(--radius-md) 0 0 var(--radius-md); background:rgba(201,106,92,0.08); color:var(--accent-coral); border:2px solid var(--accent-coral); border-right:none; }
  .game-row td:nth-child(2) { background:var(--bg-secondary); color:var(--text-muted); font-size:22px; font-weight:400; border-top:2px solid var(--border-light); border-bottom:2px solid var(--border-light); text-align:center; font-family:var(--font-body); min-width:60px; }
  .game-row td:last-child { border-radius:0 var(--radius-md) var(--radius-md) 0; background:rgba(46,125,110,0.08); color:var(--accent-teal); border:2px solid var(--accent-teal); border-left:none; }
  .diff-wrong { background:rgba(201,106,92,0.3); padding:2px 4px; border-radius:3px; }
  .diff-correct { background:rgba(46,125,110,0.3); padding:2px 4px; border-radius:3px; }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L3 · 兴趣与原因</span>
  <span class="sep"></span>
  <span class="section-name">Game · Correct the Teacher ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">
  <div class="section-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · Correct the Teacher!</div>

  <table class="game-table">
    <thead>
      <tr>
        <th class="wrong-h">&#10060; Error (Teacher says…)</th>
        <th></th>
        <th class="correct-h">&#10003; Correction</th>
      </tr>
    </thead>
    <tbody>
      <tr class="game-row">
        <td>我<span class="diff-wrong">在</span>历史很感兴趣。</td>
        <td>→</td>
        <td>我<span class="diff-correct">对</span>历史很感兴趣。</td>
      </tr>
      <tr class="game-row">
        <td>我对音乐感兴趣<span class="diff-wrong">很</span>。</td>
        <td>→</td>
        <td>我对音乐<span class="diff-correct">很</span>感兴趣。</td>
      </tr>
      <tr class="game-row">
        <td><span class="diff-wrong">所以</span>我喜欢化学。</td>
        <td>→</td>
        <td><span class="diff-correct">因为</span>我觉得化学很有意思，<span class="diff-correct">所以</span>我喜欢化学。</td>
      </tr>
      <tr class="game-row">
        <td style="font-size:22px;">因为老师对我很好，<span class="diff-wrong">我</span>喜欢上历史课。</td>
        <td>→</td>
        <td style="font-size:22px;">因为老师对我很好，<span class="diff-correct">所以</span>我喜欢上历史课。</td>
      </tr>
      <tr class="game-row">
        <td>我对数学<span class="diff-wrong">有很大兴趣</span>。</td>
        <td>→</td>
        <td>我对数学<span class="diff-correct">很感兴趣</span>。</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l3-interest-reasons/index.html`, after line 19 (`{ file: "slides/11-game.html", label: "Game · Correct the Teacher (37–43 min)" },`), add:

```js
    { file: "slides/11b-game-answers.html", label: "  ↳ Answers · Correct the Teacher" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "11b-game-answers" index/designs/y9-l7/l3-interest-reasons/index.html`
Expected: `1`

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l3-interest-reasons/slides/11-game.html index/designs/y9-l7/l3-interest-reasons/slides/11b-game-answers.html index/designs/y9-l7/l3-interest-reasons/index.html
git commit -m "fix(y9-l7): split L3 game answers into next-slide reveal"
```

---

### Task 3: L5-07 text2 — split comprehension question answers

**Files:**
- Modify: `index/designs/y9-l7/l5-text2-vocab/slides/07-text2.html`
- Create: `index/designs/y9-l7/l5-text2-vocab/slides/07b-text2-answers.html`
- Modify: `index/designs/y9-l7/l5-text2-vocab/index.html:14`

- [ ] **Step 1: Remove the inline answers from the comprehension question list**

In `index/designs/y9-l7/l5-text2-vocab/slides/07-text2.html`, the `.cq-list` block currently is:

```html
  <div class="cq-list">
    <div class="cq-item">
      <div class="cq-num">1</div>
      <div class="cq-q">他最喜欢哪个科目？</div>
      <div class="cq-a">→ 化学。</div>
    </div>
    <div class="cq-item">
      <div class="cq-num">2</div>
      <div class="cq-q">他为什么喜欢化学？</div>
      <div class="cq-a">→ 因为他觉得化学很有意思。</div>
    </div>
    <div class="cq-item">
      <div class="cq-num">3</div>
      <div class="cq-q">化学老师教得怎么样？</div>
      <div class="cq-a">→ 教得很好。/ 也教得好。</div>
    </div>
  </div>
```

Replace with (drop the `.cq-a` divs and the `auto` column they occupied):

```html
  <div class="cq-list">
    <div class="cq-item">
      <div class="cq-num">1</div>
      <div class="cq-q">他最喜欢哪个科目？</div>
    </div>
    <div class="cq-item">
      <div class="cq-num">2</div>
      <div class="cq-q">他为什么喜欢化学？</div>
    </div>
    <div class="cq-item">
      <div class="cq-num">3</div>
      <div class="cq-q">化学老师教得怎么样？</div>
    </div>
  </div>
  <div class="answer-hidden">答案见下一张 · Answers on next slide →</div>
```

Change the `.cq-item` grid so it no longer reserves a column for the dropped answer (currently `grid-template-columns:28px 1fr auto;`):

```css
  .cq-item { display:grid; grid-template-columns:28px 1fr; gap:16px; align-items:center; background:var(--bg-secondary); border-radius:var(--radius-md); padding:10px 18px; border:1px solid var(--border-light); }
```

Add the `.answer-hidden` rule to the `<style>` block (insert after `.highlight-red`):

```css
  .answer-hidden { border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:10px 18px; color:var(--text-muted); font-style:italic; font-size:15px; opacity:0.5; margin-bottom:14px; }
```

- [ ] **Step 2: Verify**

Run: `grep -c "cq-a" index/designs/y9-l7/l5-text2-vocab/slides/07-text2.html`
Expected: `0`

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l5-text2-vocab/slides/07b-text2-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L5-07b · Text 2 Comprehension Answers</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:36px 100px 32px; }
  .section-label { font-size:16px; font-weight:700; letter-spacing:0.14em; color:var(--accent-gold); text-transform:uppercase; margin-bottom:10px; }
  .main-title { font-family:var(--font-display); font-size:44px; font-weight:900; margin-bottom:24px; }
  .cq-list { display:flex; flex-direction:column; gap:12px; }
  .cq-item { display:grid; grid-template-columns:28px 1fr auto; gap:16px; align-items:center; background:var(--bg-secondary); border-radius:var(--radius-md); padding:14px 22px; border:1px solid var(--border-light); }
  .cq-num { font-family:var(--font-display); font-size:24px; font-weight:900; color:var(--accent-gold); opacity:0.6; text-align:center; }
  .cq-q { font-family:var(--font-display); font-size:24px; font-weight:700; color:var(--text-primary); }
  .cq-a { font-family:var(--font-display); font-size:22px; color:var(--accent-gold); font-weight:700; white-space:nowrap; }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L5 · 为什么？因为！</span>
  <span class="sep"></span>
  <span class="section-name">Text 2 Comprehension ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">
  <div class="section-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · Text 2 Dialogue</div>

  <div class="cq-list">
    <div class="cq-item">
      <div class="cq-num">1</div>
      <div class="cq-q">他最喜欢哪个科目？</div>
      <div class="cq-a">→ 化学。</div>
    </div>
    <div class="cq-item">
      <div class="cq-num">2</div>
      <div class="cq-q">他为什么喜欢化学？</div>
      <div class="cq-a">→ 因为他觉得化学很有意思。</div>
    </div>
    <div class="cq-item">
      <div class="cq-num">3</div>
      <div class="cq-q">化学老师教得怎么样？</div>
      <div class="cq-a">→ 教得很好。/ 也教得好。</div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l5-text2-vocab/index.html`, after line 14 (`{ file: "slides/07-text2.html", label: "I Do · Text 2 Opening (CD Track 27)" },`), add:

```js
    { file: "slides/07b-text2-answers.html", label: "  ↳ Answers · Text 2 Comprehension" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "07b-text2-answers" index/designs/y9-l7/l5-text2-vocab/index.html`
Expected: `1`

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l5-text2-vocab/slides/07-text2.html index/designs/y9-l7/l5-text2-vocab/slides/07b-text2-answers.html index/designs/y9-l7/l5-text2-vocab/index.html
git commit -m "fix(y9-l7): split L5 text2 comprehension answers into next-slide reveal"
```

---

### Task 4: L5-12 game — split sentence scramble answers

**Files:**
- Modify: `index/designs/y9-l7/l5-text2-vocab/slides/12-game.html`
- Create: `index/designs/y9-l7/l5-text2-vocab/slides/12b-game-answers.html`
- Modify: `index/designs/y9-l7/l5-text2-vocab/index.html:20`

- [ ] **Step 1: Remove the answer column from each sentence row**

In `index/designs/y9-l7/l5-text2-vocab/slides/12-game.html`, each `.sentence-row` currently has this shape (example, row 1):

```html
    <div class="sentence-row">
      <div class="snum">1</div>
      <div class="chips-wrap">
        <div class="chip blue">觉得</div>
        <div class="chip blue-light">我</div>
        <div class="chip blue">很</div>
        <div class="chip blue-light">化学</div>
        <div class="chip blue">有意思</div>
      </div>
      <div class="answer-col">
        <div class="ans-arrow">→</div>
        <div class="ans-box">
          <div class="ans-label">Answer · 答案</div>
          <div class="ans-cn">我觉得化学很有意思。</div>
        </div>
      </div>
    </div>
```

Remove the `.answer-col` div from all 4 rows, leaving only `snum` + `chips-wrap`. Row 1 becomes:

```html
    <div class="sentence-row">
      <div class="snum">1</div>
      <div class="chips-wrap">
        <div class="chip blue">觉得</div>
        <div class="chip blue-light">我</div>
        <div class="chip blue">很</div>
        <div class="chip blue-light">化学</div>
        <div class="chip blue">有意思</div>
      </div>
    </div>
```

Apply the same removal to rows 2 (你/历史/为什么/喜欢), 3 (因为/觉得/我/数学/没意思/很), 4 (我/对/很/音乐/感兴趣).

Update `.sentence-row` grid (currently `grid-template-columns:32px 1fr 1fr;`) to drop the now-unused second `1fr` column:

```css
  .sentence-row { background:var(--bg-secondary); border:1.5px solid var(--border-medium); border-radius:var(--radius-lg); padding:14px 20px; display:grid; grid-template-columns:32px 1fr; gap:16px; align-items:center; }
```

Replace the `.ext-note` block (currently references "after each answer is revealed"):

```html
  <div class="ext-note">
    <div class="ext-note-icon">★</div>
    Extension: after each answer is revealed, write one additional related sentence in exercise books.
  </div>
```

with:

```html
  <div class="answer-hidden">答案见下一张 · Answers on next slide →</div>
  <div class="ext-note">
    <div class="ext-note-icon">★</div>
    Extension: write one additional related sentence in exercise books.
  </div>
```

Add the `.answer-hidden` rule to the `<style>` block (insert after `.ext-note-icon`):

```css
  .answer-hidden { border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:10px 18px; color:var(--text-muted); font-style:italic; font-size:15px; opacity:0.5; margin-top:14px; }
```

- [ ] **Step 2: Verify**

Run: `grep -c "answer-col" index/designs/y9-l7/l5-text2-vocab/slides/12-game.html`
Expected: `0`

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l5-text2-vocab/slides/12b-game-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L5-12b · Game Answers: 理顺句子 Sentence Scramble</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:32px 100px 28px; }
  .section-label { font-size:16px; font-weight:700; letter-spacing:0.14em; color:var(--accent-gold); text-transform:uppercase; margin-bottom:8px; }
  .main-title { font-family:var(--font-display); font-size:44px; font-weight:900; margin-bottom:20px; }

  .sentences-grid { display:flex; flex-direction:column; gap:16px; }
  .sentence-row { background:var(--bg-secondary); border:1.5px solid var(--border-medium); border-radius:var(--radius-lg); padding:18px 24px; display:grid; grid-template-columns:32px 1fr; gap:16px; align-items:center; }
  .sentence-row:nth-child(odd) { border-color:var(--accent-blue); background:var(--accent-blue-dim); }
  .sentence-row:nth-child(even) { border-color:var(--accent-teal); background:var(--accent-teal-dim); }

  .snum { font-family:var(--font-display); font-size:26px; font-weight:900; opacity:0.4; text-align:center; }
  .sentence-row:nth-child(odd) .snum { color:var(--accent-blue); }
  .sentence-row:nth-child(even) .snum { color:var(--accent-teal); }

  .ans-cn { font-family:var(--font-display); font-size:28px; font-weight:700; color:var(--text-primary); }
  .sentence-row:nth-child(odd) .ans-cn { color:var(--accent-blue); }
  .sentence-row:nth-child(even) .ans-cn { color:var(--accent-teal); }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L5 · 为什么？因为！</span>
  <span class="sep"></span>
  <span class="section-name">Game · 理顺句子 Sentence Scramble ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">
  <div class="section-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · 理顺句子 Sentence Scramble</div>

  <div class="sentences-grid">
    <div class="sentence-row">
      <div class="snum">1</div>
      <div class="ans-cn">我觉得化学很有意思。</div>
    </div>
    <div class="sentence-row">
      <div class="snum">2</div>
      <div class="ans-cn">你为什么喜欢历史？</div>
    </div>
    <div class="sentence-row">
      <div class="snum">3</div>
      <div class="ans-cn">因为我觉得数学很没意思。</div>
    </div>
    <div class="sentence-row">
      <div class="snum">4</div>
      <div class="ans-cn">我对音乐很感兴趣。</div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l5-text2-vocab/index.html`, after line 20 (`{ file: "slides/12-game.html", label: "Game · 理顺句子 Sentence Scramble (38–43 min)" },`), add:

```js
    { file: "slides/12b-game-answers.html", label: "  ↳ Answers · Sentence Scramble" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "12b-game-answers" index/designs/y9-l7/l5-text2-vocab/index.html`
Expected: `1`

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l5-text2-vocab/slides/12-game.html index/designs/y9-l7/l5-text2-vocab/slides/12b-game-answers.html index/designs/y9-l7/l5-text2-vocab/index.html
git commit -m "fix(y9-l7): split L5 sentence scramble answers into next-slide reveal"
```

---

### Task 5: L7-10 game — split sentence jumble answers

**Files:**
- Modify: `index/designs/y9-l7/l7-complement-numbers/slides/10-game.html`
- Create: `index/designs/y9-l7/l7-complement-numbers/slides/10b-game-answers.html`
- Modify: `index/designs/y9-l7/l7-complement-numbers/index.html:18`

- [ ] **Step 1: Remove the `.answer-row` from each round card**

In `index/designs/y9-l7/l7-complement-numbers/slides/10-game.html`, each `.round-card` currently ends with an `.answer-row`, e.g. Round 1:

```html
    <div class="round-card">
      <div class="round-label">Round 1</div>
      <div class="tokens-row">
        <span class="token tok-coral">很快</span>
        <span class="token tok-blue">她</span>
        <span class="token tok-teal">跑步</span>
        <span class="token tok-blue">跑</span>
        <span class="token tok-grey">得</span>
      </div>
      <div class="answer-row"><span class="arr">→</span> 她跑步跑<span class="de">得</span>很快。</div>
    </div>
```

Remove the `.answer-row` div from all 5 round cards (Round 1 through Round 5), leaving only `round-label` + `tokens-row`. Round 1 becomes:

```html
    <div class="round-card">
      <div class="round-label">Round 1</div>
      <div class="tokens-row">
        <span class="token tok-coral">很快</span>
        <span class="token tok-blue">她</span>
        <span class="token tok-teal">跑步</span>
        <span class="token tok-blue">跑</span>
        <span class="token tok-grey">得</span>
      </div>
    </div>
```

Apply the same removal to Round 2 (老师教得也好), Round 3 (他钢琴弹得很好), Round 4 (每个学期考两三次), Round 5 (他不经常滑冰).

Replace the `.bonus-box` block:

```html
  <div class="bonus-box">
    ⭐ After each correct answer: "Can you add one word to make it more interesting?" · Grammar diagrams remain visible as reference.
  </div>
```

with:

```html
  <div class="answer-hidden">答案见下一张 · Answers on next slide →</div>
  <div class="bonus-box">
    ⭐ After each correct answer: "Can you add one word to make it more interesting?"
  </div>
```

Add the `.answer-hidden` rule to the `<style>` block (insert after `.de`):

```css
  .answer-hidden { border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:10px 18px; color:var(--text-muted); font-style:italic; font-size:15px; opacity:0.5; margin-bottom:12px; }
```

- [ ] **Step 2: Verify**

Run: `grep -c "answer-row" index/designs/y9-l7/l7-complement-numbers/slides/10-game.html`
Expected: `0`

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l7-complement-numbers/slides/10b-game-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L7-10b · Game Answers · 语法大挑战 Sentence Jumble</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:36px 100px 32px; }
  .section-label { font-size:15px; font-weight:700; letter-spacing:0.14em; color:var(--accent-gold); text-transform:uppercase; margin-bottom:6px; }
  .main-title { font-family:var(--font-display); font-size:42px; font-weight:900; color:var(--text-primary); margin-bottom:20px; }

  .rounds-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px 24px; }
  .round-card { background:var(--bg-secondary); border:1.5px solid var(--border-light); border-radius:var(--radius-lg); padding:18px 22px; }
  .round-label { font-size:12px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:var(--text-muted); margin-bottom:10px; }
  .answer-row { display:flex; align-items:center; gap:8px; font-family:var(--font-display); font-size:24px; font-weight:700; color:var(--accent-gold); }
  .arr { color:var(--text-muted); font-size:18px; }
  .round-card.full { grid-column:1/-1; }
  .de { color:var(--accent-coral); }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L7 · 动词 + 得</span>
  <span class="sep"></span>
  <span class="section-name">Game · 语法大挑战 Sentence Jumble ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">
  <div class="section-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · 语法大挑战 — Sentence Jumble</div>

  <div class="rounds-grid">
    <div class="round-card">
      <div class="round-label">Round 1</div>
      <div class="answer-row"><span class="arr">→</span> 她跑步跑<span class="de">得</span>很快。</div>
    </div>
    <div class="round-card">
      <div class="round-label">Round 2</div>
      <div class="answer-row"><span class="arr">→</span> 老师教<span class="de">得</span>也好。</div>
    </div>
    <div class="round-card">
      <div class="round-label">Round 3</div>
      <div class="answer-row"><span class="arr">→</span> 他钢琴弹<span class="de">得</span>很好。</div>
    </div>
    <div class="round-card">
      <div class="round-label">Round 4</div>
      <div class="answer-row"><span class="arr">→</span> 每个学期考<span style="color:var(--accent-coral)">两三次</span>。</div>
    </div>
    <div class="round-card full">
      <div class="round-label">Round 5</div>
      <div class="answer-row"><span class="arr">→</span> 他不经常滑冰。</div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l7-complement-numbers/index.html`, after line 18 (`{ file: "slides/10-game.html", label: "Game · 语法大挑战 Sentence Jumble (38–43 min)" },`), add:

```js
    { file: "slides/10b-game-answers.html", label: "  ↳ Answers · Sentence Jumble" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "10b-game-answers" index/designs/y9-l7/l7-complement-numbers/index.html`
Expected: `1`

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l7-complement-numbers/slides/10-game.html index/designs/y9-l7/l7-complement-numbers/slides/10b-game-answers.html index/designs/y9-l7/l7-complement-numbers/index.html
git commit -m "fix(y9-l7): split L7 sentence jumble answers into next-slide reveal"
```

---

### Task 6: L8-10 game-r1 — split flash card answers

**Files:**
- Modify: `index/designs/y9-l7/l8-review-test-prep/slides/10-game-r1.html`
- Create: `index/designs/y9-l7/l8-review-test-prep/slides/10b-game-r1-answers.html`
- Modify: `index/designs/y9-l7/l8-review-test-prep/index.html:17`

- [ ] **Step 1: Remove the answer text from each flash card**

In `index/designs/y9-l7/l8-review-test-prep/slides/10-game-r1.html`, each `.flash-card` currently has this shape (example, card 1):

```html
    <div class="flash-card">
      <span class="card-num"># 1</span>
      <div class="flash-cn">有意思</div>
      <div>
        <div class="answer-label">Answer</div>
        <div class="answer-reveal">interesting</div>
      </div>
    </div>
```

Remove the trailing `<div>...</div>` containing `.answer-label`/`.answer-reveal` from all 5 cards, leaving only `card-num` + `flash-cn`. Card 1 becomes:

```html
    <div class="flash-card">
      <span class="card-num"># 1</span>
      <div class="flash-cn">有意思</div>
    </div>
```

Apply the same removal to cards 2 (学期), 3 (大概), 4 (没意思), 5 (两次).

Replace the `.otr-note-strip` text:

```html
    <div class="otr-note-strip">
      <span class="otr-icon">&#128065;</span>
      <span class="otr-text">Cover answers first — reveal after teams respond</span>
    </div>
```

with:

```html
    <div class="otr-note-strip">
      <span class="otr-icon">&#128065;</span>
      <span class="otr-text">Teams call out the English — answers on next slide</span>
    </div>
```

- [ ] **Step 2: Verify**

Run: `grep -c "answer-reveal" index/designs/y9-l7/l8-review-test-prep/slides/10-game-r1.html`
Expected: `0`

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l8-review-test-prep/slides/10b-game-r1-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L8-10b · Game Round 1 Answers · 词汇闪卡</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:36px 100px 32px; }
  .page-label { font-size:13px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:var(--accent-gold); margin-bottom:4px; }
  .main-title { font-family:var(--font-display); font-size:48px; font-weight:900; color:var(--text-primary); line-height:1.1; margin-bottom:24px; }

  .cards-row { display:grid; grid-template-columns:repeat(5, 1fr); gap:18px; }
  .flash-card { background:#fff; border:2px solid var(--accent-gold); border-radius:var(--radius-lg); padding:24px 14px 20px; display:flex; flex-direction:column; align-items:center; gap:12px; position:relative; box-shadow:0 2px 12px rgba(26,37,53,0.06); }
  .flash-card .card-num { position:absolute; top:12px; left:14px; font-size:12px; font-weight:700; color:var(--text-muted); letter-spacing:0.08em; }
  .flash-cn { font-family:var(--font-display); font-size:36px; font-weight:900; color:var(--text-primary); line-height:1.1; text-align:center; }
  .answer-reveal { background:var(--accent-gold-dim); border:1.5px solid var(--accent-gold); border-radius:var(--radius-md); padding:6px 16px; font-size:18px; font-weight:700; color:var(--accent-gold); text-align:center; width:100%; box-sizing:border-box; }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L8 · 综合复习</span>
  <span class="sep"></span>
  <span class="section-name">Game · Round 1: 词汇闪卡 ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">
  <div class="page-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · Round 1 · 词汇闪卡</div>

  <div class="cards-row">
    <div class="flash-card">
      <span class="card-num"># 1</span>
      <div class="flash-cn">有意思</div>
      <div class="answer-reveal">interesting</div>
    </div>
    <div class="flash-card">
      <span class="card-num"># 2</span>
      <div class="flash-cn">学期</div>
      <div class="answer-reveal">semester / term</div>
    </div>
    <div class="flash-card">
      <span class="card-num"># 3</span>
      <div class="flash-cn">大概</div>
      <div class="answer-reveal">approximately / about</div>
    </div>
    <div class="flash-card">
      <span class="card-num"># 4</span>
      <div class="flash-cn">没意思</div>
      <div class="answer-reveal">boring / not interesting</div>
    </div>
    <div class="flash-card">
      <span class="card-num"># 5</span>
      <div class="flash-cn">两次</div>
      <div class="answer-reveal">twice / two times</div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l8-review-test-prep/index.html`, after line 17 (`{ file: "slides/10-game-r1.html", label: "Game · Round 1: 词汇闪卡 (30–32 min)" },`), add:

```js
    { file: "slides/10b-game-r1-answers.html", label: "  ↳ Answers · Round 1 词汇闪卡" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "10b-game-r1-answers" index/designs/y9-l7/l8-review-test-prep/index.html`
Expected: `1`

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l8-review-test-prep/slides/10-game-r1.html index/designs/y9-l7/l8-review-test-prep/slides/10b-game-r1-answers.html index/designs/y9-l7/l8-review-test-prep/index.html
git commit -m "fix(y9-l7): split L8 round 1 flash card answers into next-slide reveal"
```

---

### Task 7: L8-11 game-r2 — split English→Chinese answers

**Files:**
- Modify: `index/designs/y9-l7/l8-review-test-prep/slides/11-game-r2.html`
- Create: `index/designs/y9-l7/l8-review-test-prep/slides/11b-game-r2-answers.html`
- Modify: `index/designs/y9-l7/l8-review-test-prep/index.html:18`

- [ ] **Step 1: Remove the Chinese translation from each prompt card**

In `index/designs/y9-l7/l8-review-test-prep/slides/11-game-r2.html`, each `.prompt-card` currently has this shape (example, card 1):

```html
      <div class="prompt-card">
        <div class="card-num">1</div>
        <div class="card-en">be interested in</div>
        <div class="card-divider"></div>
        <div class="card-zh">对……感兴趣</div>
      </div>
```

Remove `.card-divider` and `.card-zh` from all 5 cards, leaving only `card-num` + `card-en`. Card 1 becomes:

```html
      <div class="prompt-card">
        <div class="card-num">1</div>
        <div class="card-en">be interested in</div>
      </div>
```

Apply the same removal to cards 2 (difficult), 3 (often / regularly), 4 (break time), 5 (examination).

Replace the `.otr-strip` text:

```html
  <div class="otr-strip">
    <span class="otr-label">OTR</span>
    <span class="otr-text"><strong>Teams write — teacher scans — one team reads aloud</strong></span>
  </div>
```

with:

```html
  <div class="answer-hidden">答案见下一张 · Answers on next slide →</div>
  <div class="otr-strip">
    <span class="otr-label">OTR</span>
    <span class="otr-text"><strong>Teams write — teacher scans — one team reads aloud</strong></span>
  </div>
```

Add the `.answer-hidden` rule to the `<style>` block (insert after `.otr-text strong`):

```css
  .answer-hidden { border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:8px 18px; color:var(--text-muted); font-style:italic; font-size:14px; opacity:0.5; margin-bottom:10px; }
```

- [ ] **Step 2: Verify**

Run: `grep -c "card-zh" index/designs/y9-l7/l8-review-test-prep/slides/11-game-r2.html`
Expected: `0`

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l8-review-test-prep/slides/11b-game-r2-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L8-11b · Game Round 2 Answers · 英译中</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:28px 100px 20px; }
  .section-label { font-size:13px; font-weight:700; letter-spacing:0.14em; color:var(--accent-gold); text-transform:uppercase; margin-bottom:6px; }
  .main-title { font-family:var(--font-display); font-size:42px; font-weight:900; color:var(--text-primary); margin-bottom:24px; }

  .cards-wrap { display:flex; flex-direction:column; gap:14px; }
  .cards-row { display:flex; gap:14px; }
  .cards-row.row-2 > .prompt-card { flex:1; }
  .cards-row.row-3 > .prompt-card { flex:1; }

  .prompt-card { background:var(--accent-gold-dim); border:1.5px solid var(--accent-gold); border-radius:var(--radius-lg); padding:22px 28px; display:flex; flex-direction:column; align-items:flex-start; gap:10px; }
  .card-num { width:34px; height:34px; border-radius:50%; background:var(--accent-gold); color:#fff; font-size:16px; font-weight:700; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
  .card-en { font-family:var(--font-body); font-size:28px; font-weight:700; color:var(--text-muted); line-height:1.1; }
  .card-divider { width:100%; height:1px; background:var(--border-light); }
  .card-zh { font-family:var(--font-display); font-size:34px; font-weight:700; color:var(--accent-gold); line-height:1.2; }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L8 · 综合复习</span>
  <span class="sep"></span>
  <span class="section-name">Game · Round 2: 英译中 ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">

  <div class="section-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · Round 2 · 英译中</div>

  <div class="cards-wrap">
    <div class="cards-row row-2">
      <div class="prompt-card">
        <div class="card-num">1</div>
        <div class="card-en">be interested in</div>
        <div class="card-divider"></div>
        <div class="card-zh">对……感兴趣</div>
      </div>
      <div class="prompt-card">
        <div class="card-num">2</div>
        <div class="card-en">difficult</div>
        <div class="card-divider"></div>
        <div class="card-zh">难</div>
      </div>
    </div>
    <div class="cards-row row-3">
      <div class="prompt-card">
        <div class="card-num">3</div>
        <div class="card-en">often / regularly</div>
        <div class="card-divider"></div>
        <div class="card-zh">经常</div>
      </div>
      <div class="prompt-card">
        <div class="card-num">4</div>
        <div class="card-en">break time</div>
        <div class="card-divider"></div>
        <div class="card-zh">课间休息</div>
      </div>
      <div class="prompt-card">
        <div class="card-num">5</div>
        <div class="card-en">examination</div>
        <div class="card-divider"></div>
        <div class="card-zh">考试</div>
      </div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
  <span>L8 · Game Round 2 Answers · 英译中</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l8-review-test-prep/index.html`, after line 18 (`{ file: "slides/11-game-r2.html", label: "Game · Round 2: 英译中 (32–34 min)" },`), add:

```js
    { file: "slides/11b-game-r2-answers.html", label: "  ↳ Answers · Round 2 英译中" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "11b-game-r2-answers" index/designs/y9-l7/l8-review-test-prep/index.html`
Expected: `1`

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l8-review-test-prep/slides/11-game-r2.html index/designs/y9-l7/l8-review-test-prep/slides/11b-game-r2-answers.html index/designs/y9-l7/l8-review-test-prep/index.html
git commit -m "fix(y9-l7): split L8 round 2 English-to-Chinese answers into next-slide reveal"
```

---

### Task 8: L8-12 game-r3 — split sentence challenge answers

**Files:**
- Modify: `index/designs/y9-l7/l8-review-test-prep/slides/12-game-r3.html`
- Create: `index/designs/y9-l7/l8-review-test-prep/slides/12b-game-r3-answers.html`
- Modify: `index/designs/y9-l7/l8-review-test-prep/index.html:19`

- [ ] **Step 1: Strip answer content from all 3 challenge cards**

In `index/designs/y9-l7/l8-review-test-prep/slides/12-game-r3.html`, Challenge 1 currently is:

```html
    <div class="challenge-card challenge-blue">
      <div class="c-header">
        <div class="c-num">1</div>
        <span class="c-type-badge">Complete · 补全句子</span>
      </div>
      <div class="c-sentence">
        因为我觉得历史很有意思，<span class="c-blank"></span>我喜欢历史。
      </div>
      <div style="display:flex; align-items:center; gap:12px;">
        <div class="c-answer-box">所以</div>
        <span class="c-note">连词 conjunction</span>
      </div>
    </div>
```

Remove the trailing answer row, leaving only the header and the sentence with the blank:

```html
    <div class="challenge-card challenge-blue">
      <div class="c-header">
        <div class="c-num">1</div>
        <span class="c-type-badge">Complete · 补全句子</span>
      </div>
      <div class="c-sentence">
        因为我觉得历史很有意思，<span class="c-blank"></span>我喜欢历史。
      </div>
    </div>
```

Challenge 2 currently is:

```html
    <div class="challenge-card challenge-coral">
      <div class="c-header">
        <div class="c-num">2</div>
        <span class="c-type-badge">Correct Error · 改错</span>
      </div>
      <div class="error-block">
        <div class="err-row">
          <span class="err-label">❌</span>
          <span class="err-text-wrong">我在数学很感兴趣。</span>
        </div>
        <div style="text-align:center; font-size:22px; color:var(--text-muted);">↓</div>
        <div class="err-row">
          <span class="err-label">✅</span>
          <span class="err-text-correct">我对数学很感兴趣。</span>
          <span class="err-fix-note">在→对</span>
        </div>
      </div>
    </div>
```

Remove the second `.err-row` (and the `↓` divider between them), leaving only the error:

```html
    <div class="challenge-card challenge-coral">
      <div class="c-header">
        <div class="c-num">2</div>
        <span class="c-type-badge">Correct Error · 改错</span>
      </div>
      <div class="error-block">
        <div class="err-row">
          <span class="err-label">❌</span>
          <span class="err-text-wrong">我在数学很感兴趣。</span>
        </div>
      </div>
    </div>
```

Challenge 3 currently is:

```html
    <div class="challenge-card challenge-teal">
      <div class="c-header">
        <div class="c-num">3</div>
        <span class="c-type-badge">Produce · 造句</span>
      </div>
      <div class="c-sentence">
        我们的数学老师<span class="c-blank"></span>。
      </div>
      <div class="c-requirement">
        Must use <strong>教得</strong> + complement<br>
        e.g. 教得很好 / 很有趣
      </div>
      <div class="c-open-badge">Open Answer ✦</div>
    </div>
```

Drop the worked example from `.c-requirement` (it gives away a model answer) so only the grammar requirement remains; keep `.c-open-badge` since "Open Answer" signals there's no single fixed answer to reveal, not a worked answer itself:

```html
    <div class="challenge-card challenge-teal">
      <div class="c-header">
        <div class="c-num">3</div>
        <span class="c-type-badge">Produce · 造句</span>
      </div>
      <div class="c-sentence">
        我们的数学老师<span class="c-blank"></span>。
      </div>
      <div class="c-requirement">
        Must use <strong>教得</strong> + complement
      </div>
      <div class="c-open-badge">Open Answer ✦</div>
    </div>
```

Replace the `.note-strip` block:

```html
  <div class="note-strip">
    <span class="note-strip-icon">⏱</span>
    <span class="note-strip-text">After each answer: <strong>10-second explanation in English max</strong></span>
  </div>
```

with:

```html
  <div class="answer-hidden">答案见下一张 · Answers on next slide →</div>
  <div class="note-strip">
    <span class="note-strip-icon">⏱</span>
    <span class="note-strip-text">After each answer: <strong>10-second explanation in English max</strong></span>
  </div>
```

Add the `.answer-hidden` rule to the `<style>` block (insert after `.note-strip-text strong`):

```css
  .answer-hidden { border:2px dashed var(--border-medium); border-radius:var(--radius-md); padding:10px 18px; color:var(--text-muted); font-style:italic; font-size:15px; opacity:0.5; margin-bottom:12px; }
```

- [ ] **Step 2: Verify**

Run: `grep -c "c-answer-box\|err-text-correct" index/designs/y9-l7/l8-review-test-prep/slides/12-game-r3.html`
Expected: `0`

- [ ] **Step 3: Create the answers slide**

Create `index/designs/y9-l7/l8-review-test-prep/slides/12b-game-r3-answers.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>L8-12b · Game Round 3 Answers · 句子挑战</title>
<link rel="stylesheet" href="../../shared/tokens.css">
<style>
  .slide-content { justify-content:flex-start; padding:28px 100px 20px; }
  .section-label { font-size:13px; font-weight:700; letter-spacing:0.14em; color:var(--accent-gold); text-transform:uppercase; margin-bottom:6px; }
  .main-title { font-family:var(--font-display); font-size:42px; font-weight:900; color:var(--text-primary); margin-bottom:20px; }

  .challenges-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; }
  .challenge-card { border-radius:var(--radius-lg); padding:22px 24px; display:flex; flex-direction:column; gap:12px; background:var(--accent-gold-dim); border:2px solid var(--accent-gold); }
  .c-header { display:flex; align-items:center; gap:12px; }
  .c-num { width:38px; height:38px; border-radius:50%; font-family:var(--font-display); font-size:20px; font-weight:900; display:flex; align-items:center; justify-content:center; flex-shrink:0; background:var(--accent-gold); color:#fff; }
  .c-type-badge { padding:4px 14px; border-radius:999px; font-size:13px; font-weight:700; letter-spacing:0.08em; white-space:nowrap; background:var(--accent-gold); color:#fff; }
  .c-sentence { font-family:var(--font-display); font-size:26px; font-weight:700; line-height:1.45; padding:12px 16px; border-left:4px solid var(--accent-gold); background:rgba(255,255,255,0.55); border-radius:0 var(--radius-md) var(--radius-md) 0; color:var(--text-primary); }
  .c-answer-box { padding:8px 18px; border-radius:var(--radius-md); font-family:var(--font-display); font-size:28px; font-weight:900; display:inline-block; align-self:flex-start; background:var(--accent-gold); color:#fff; }
  .c-note { font-size:16px; font-weight:700; letter-spacing:0.08em; color:var(--accent-gold); }
  .err-text-correct { font-family:var(--font-display); font-size:24px; font-weight:700; color:var(--accent-gold); }
  .err-row { display:flex; align-items:center; gap:14px; padding:10px 14px; border-radius:var(--radius-md); background:rgba(255,255,255,0.55); }
  .err-label { font-size:22px; flex-shrink:0; }
  .err-fix-note { font-size:16px; font-weight:700; background:var(--accent-gold); color:#fff; padding:3px 10px; border-radius:999px; white-space:nowrap; }
  .c-requirement { font-size:18px; color:var(--text-secondary); line-height:1.5; background:rgba(255,255,255,0.55); border-radius:var(--radius-md); padding:10px 14px; }
  .c-requirement strong { color:var(--accent-gold); }
</style>
</head>
<body>

<div class="slide-header">
  <span class="lesson-tag">L8 · 综合复习</span>
  <span class="sep"></span>
  <span class="section-name">Game · Round 3: 句子挑战 ↳</span>
  <div class="accent-line" style="background:var(--accent-gold);"></div>
</div>

<div class="slide-content">

  <div class="section-label">Answers Revealed · 答案</div>
  <div class="main-title">答案 · Round 3 · 句子挑战</div>

  <div class="challenges-grid">
    <div class="challenge-card">
      <div class="c-header">
        <div class="c-num">1</div>
        <span class="c-type-badge">Complete · 补全句子</span>
      </div>
      <div class="c-sentence">
        因为我觉得历史很有意思，所以我喜欢历史。
      </div>
      <div style="display:flex; align-items:center; gap:12px;">
        <div class="c-answer-box">所以</div>
        <span class="c-note">连词 conjunction</span>
      </div>
    </div>

    <div class="challenge-card">
      <div class="c-header">
        <div class="c-num">2</div>
        <span class="c-type-badge">Correct Error · 改错</span>
      </div>
      <div class="err-row">
        <span class="err-label">✅</span>
        <span class="err-text-correct">我对数学很感兴趣。</span>
        <span class="err-fix-note">在→对</span>
      </div>
    </div>

    <div class="challenge-card">
      <div class="c-header">
        <div class="c-num">3</div>
        <span class="c-type-badge">Produce · 造句</span>
      </div>
      <div class="c-requirement">
        Sample answer: 我们的数学老师<strong>教得很好</strong>。<br>
        Accept any valid 教得 + complement (e.g. 教得很有趣).
      </div>
    </div>
  </div>
</div>

<div class="slide-footer">
  <span class="brand">Y9 Chinese · Unit 3 科目</span>
  <span>L8 · Game Round 3 Answers · 句子挑战</span>
</div>

</body>
</html>
```

- [ ] **Step 4: Insert the new slide into the manifest**

In `index/designs/y9-l7/l8-review-test-prep/index.html`, after line 19 (`{ file: "slides/12-game-r3.html", label: "Game · Round 3: 句子挑战 (34–37 min)" },`), add:

```js
    { file: "slides/12b-game-r3-answers.html", label: "  ↳ Answers · Round 3 句子挑战" },
```

- [ ] **Step 5: Verify**

Run: `grep -c "12b-game-r3-answers" index/designs/y9-l7/l8-review-test-prep/index.html`
Expected: `1`

- [ ] **Step 6: Commit**

```bash
git add index/designs/y9-l7/l8-review-test-prep/slides/12-game-r3.html index/designs/y9-l7/l8-review-test-prep/slides/12b-game-r3-answers.html index/designs/y9-l7/l8-review-test-prep/index.html
git commit -m "fix(y9-l7): split L8 round 3 sentence challenge answers into next-slide reveal"
```

---

### Task 9: Full-deck sanity check + memory update

**Files:** None modified (verification + memory only).

- [ ] **Step 1: Verify every modified manifest has matching files on disk**

Run:
```bash
for f in index/designs/y9-l7/l2-opinions/index.html index/designs/y9-l7/l3-interest-reasons/index.html index/designs/y9-l7/l5-text2-vocab/index.html index/designs/y9-l7/l7-complement-numbers/index.html index/designs/y9-l7/l8-review-test-prep/index.html; do
  dir=$(dirname "$f")
  grep -oP '(?<=file: ")slides/[^"]+' "$f" | while read -r slide; do
    [ -f "$dir/$slide" ] || echo "MISSING: $dir/$slide"
  done
done
```
Expected: no output (every manifest entry resolves to a real file)

- [ ] **Step 2: Confirm no leftover answer content across all 8 edited originals**

Run:
```bash
grep -l "ec-correct-row\|diff-correct\|cq-a\|answer-col\|answer-row\|answer-reveal\|card-zh\|c-answer-box\|err-text-correct" \
  index/designs/y9-l7/l2-opinions/slides/11-game.html \
  index/designs/y9-l7/l3-interest-reasons/slides/11-game.html \
  index/designs/y9-l7/l5-text2-vocab/slides/07-text2.html \
  index/designs/y9-l7/l5-text2-vocab/slides/12-game.html \
  index/designs/y9-l7/l7-complement-numbers/slides/10-game.html \
  index/designs/y9-l7/l8-review-test-prep/slides/10-game-r1.html \
  index/designs/y9-l7/l8-review-test-prep/slides/11-game-r2.html \
  index/designs/y9-l7/l8-review-test-prep/slides/12-game-r3.html
```
Expected: no output (no matches in any of the 8 files)

- [ ] **Step 3: Save the memory rule**

Write `/Users/luojiahai/.claude/projects/-Users-luojiahai-Code-deck/memory/feedback_answer_reveal_slides.md`:

```markdown
---
name: feedback-answer-reveal-slides
description: Lesson slides must never show an answer on the same slide as its question — always a separate next-slide reveal
metadata:
  type: feedback
---

Never reveal an answer, correction, or translation on the same slide as the question/prompt that produces it. Always split into a question slide followed by a separate "↳ Answers" reveal slide shown next, matching the existing convention in this deck (e.g. `07-text1.html` → `07b-text1-answers.html`, `08-cfu.html` → `08b-cfu-answers.html`): gold accent line, "↳ Answers" in the header, "答案见下一张 · Answers on next slide →" cue on the question slide.

**Why:** Caught across 8 y9-l7 slides (game/comprehension/flash-card slides) on 2026-07-01 where wrong+correct sentences, comprehension answers, or translations were printed directly next to the prompt — defeating the point of a live class activity where students should attempt the answer before seeing it.

**How to apply:** Whenever creating or editing a lesson slide that poses a question, error-correction, translation, or fill-in-the-blank task, check whether the answer is visible on that same slide. If it is, split it into a new `Xb-...-answers.html` sibling and add it to the lesson's `DECK_MANIFEST` immediately after the question slide. Also applies more generally: all lesson slides are student-facing (what's projected to the class) — teacher-only pacing/cold-call/OTR notes are fine as supplementary annotations, but never the actual answer content.
```

Update `/Users/luojiahai/.claude/projects/-Users-luojiahai-Code-deck/memory/MEMORY.md` by adding one line (append, don't rewrite the file):

```
- [Answer-reveal slides](feedback_answer_reveal_slides.md) — never show answers on the same slide as the question; split into a next-slide reveal
```

- [ ] **Step 4: Final commit (if Step 1–2 required any fixes) or confirm clean**

If Steps 1–2 found issues, fix them and commit. If they passed cleanly, no commit is needed for this task — the 8 prior task commits already cover all code changes.
