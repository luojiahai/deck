# Lesson-set gallery: back-to-deck-index navigation

## Problem

Each lesson-set gallery (`y7-l10/index.html`, `y8-l7/index.html`, `y9-l7/index.html`) already has a "← Back to Gallery" link in its footer, but it points to `href="../"`. Relative to a page served at `/designs/<id>/`, `../` resolves to `/designs/` — a directory with no `index.html` and no rewrite, so the link 404s. There is no other way back to the main deck index (`/`) from these pages.

## Scope

- In scope: the 3 lesson-set gallery index pages — `index/designs/y7-l10/index.html`, `index/designs/y8-l7/index.html`, `index/designs/y9-l7/index.html`.
- Also in scope: the floating "back to gallery" button on the 24 individual lesson slide-deck viewers (`l1`…`l8` inside each of the 3 sets, e.g. `index/designs/y9-l7/l1-subjects/index.html`). Its link target (`href="../"`, pointing back to the lesson-set gallery) is already correct and is not touched — only its on-screen position changes (see below).
- Out of scope: the individual slide HTML files inside each lesson's `slides/` folder — the back button lives once per lesson, in the lesson's own `index.html` viewer shell, not duplicated per slide.

## Lesson-deck viewer back button reposition

Each of the 24 lesson slide-deck viewers (`<lesson>/index.html`) is a fullscreen, non-scrolling presentation page: a fixed-position `#stage` canvas with a `.list-btn` ("← 列表") floating fixed at `top: 20px; left: 20px`, and a `.counter` pill ("1 / 13") floating fixed at `bottom: 20px; right: 20px`. The `.list-btn` CSS rule is byte-identical across all 24 files.

Move `.list-btn` from the top-left to the bottom-left, mirroring the existing bottom-right counter pill so the two form a consistent bottom toolbar:

- Change `.list-btn { position: fixed; top: 20px; left: 20px; ... }` to `.list-btn { position: fixed; bottom: 20px; left: 20px; ... }` (only `top` → `bottom` changes; all other properties, the markup, and the link href are untouched).
- This is a single-property CSS change repeated identically across all 24 lesson viewer files. The existing fullscreen/print media query that hides `.counter, .nav-zone, .list-btn` is unaffected.

## Design

### New top bar

Add a slim, full-width bar as the first element inside `<body>`, immediately before the existing `<section class="hero">`, in all three files.

- Content: a single link, label `← Deck Gallery · 设计画廊`, `href="../../"` (resolves to `/`, the main deck index at `index/index.html`).
- Layout: wrapped in the page's existing `.container` (max-width) so it aligns with the hero content below it.
- Styling: per-design, using each design's own existing CSS custom properties (muted text color + border/accent tokens) rather than a shared stylesheet — each lesson set already has its own distinct palette/fonts. Visually quiet: small font size (~13–14px), letter-spacing similar to the existing `.unit-tag`/`.meta` treatment in each design, thin bottom border separating it from the hero, modest vertical padding (~12–14px). Link color uses the design's muted text color at rest and its accent color on hover. It must not visually compete with the hero — no large type, no background fill beyond the page background.

### Footer link fix

In all three files, change the existing footer link from `href="../"` to `href="../../"` so "← Back to Gallery" correctly reaches the main deck index. No other footer changes.

## Testing

Manual verification only (static HTML, no build step):
1. Serve `index/` locally (`cd index && python3 -m http.server 8080`).
2. For each of the 3 lesson-set gallery pages, confirm the new top bar link and the footer link both navigate to the main deck index (`/`), and that the page renders correctly (no layout shift/overlap with the hero).
3. For a sample of the 24 lesson slide-deck viewers (at least one per series), confirm the back button now floats bottom-left instead of top-left, does not overlap the bottom-right counter pill, still links to the lesson-set gallery, and is still hidden in fullscreen/print mode.
