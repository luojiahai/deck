# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A static design gallery deployed on Vercel at **deck.liyu.dev**. All designs share one Vercel project — each design lives in its own subfolder under `index/designs/` and is accessible at `deck.liyu.dev/designs/<design-id>/`.

## Repo structure

```
deck/
├── index/                  ← All servable content (Vercel deploys from here)
│   ├── index.html          ← Gallery homepage (reads designs.json, renders cards + search)
│   ├── designs.json        ← Design manifest (add entries when creating new designs)
│   └── designs/
│       └── <design-id>/
│           ├── index.html  ← Entry point for each design
│           └── thumb.png   ← Thumbnail for gallery card (1440×900)
├── vercel.json             ← Build: copies index/* → .vercel/output/static/
└── .vercel/                ← Vercel project config (do not delete)
```

## Adding a new design

1. Place the design's static files in `index/designs/<design-id>/` (entry point must be `index.html`)
2. Add a `thumb.png` (1440×900) to the design folder — this is the gallery card image
3. Add an entry to `index/designs.json`:
   ```json
   { "id": "<design-id>", "title": "Name", "description": "...", "createdAt": "YYYY-MM-DD", "thumbnail": "designs/<design-id>/thumb.png" }
   ```
4. Commit and push to `main` — Vercel deploys it to production automatically

Downloadable `.pptx` / `.pdf` exports (linked from a design's `index.html`) are an **optional, per-design** feature — see [Editable PPTX export](#editable-pptx-export). Keep PPTX/PDF source artifacts that aren't served (`slides-pptx/`, slide-preview `thumbs/`) out of `index/` — they bloat the deploy and are unreferenced.

## Editable PPTX export

The shipped `.pptx` files carry **real, editable text runs and shapes** — not
pictures of slides. `pptxgenjs` (via the huashu-design skill's `html2pptx.js`)
converts slide HTML into native PowerPoint objects. `playwright` measures the
slides, `sharp` rasterises drawings, `pdf-lib` backs the PDF path. All four are
local-only tooling and must never be installed on deploy (see [Deployment](#deployment)).

### Pick the exporter by canvas size

This repo has two slide canvases, and the PPTX layout must match or **every
slide is rejected**:

| Deck canvas (`shared/tokens.css`) | Exporter | Designs |
|---|---|---|
| `width: 1920px` | `scripts/export-deck-pptx-1920.mjs` (20in × 11.25in) | y7-l10…l14, y8-l7…l11, y9-l7…l9 |
| `width: 960pt` | the **skill's stock** `.claude/skills/huashu-design/scripts/export_deck_pptx.mjs` (`LAYOUT_WIDE`, 13.33in × 7.5in) | y9-l10, y9-l11 |

> The header of `export-deck-pptx-1920.mjs` claims it is the one to use for
> every deck here. That predates the 960pt decks — trust the table.

PDF export always uses the skill's `export_deck_pdf.mjs`, and runs against the
**real** slides (it's a browser print, so no massaging needed).

### Export runs against a throwaway copy, never the served slides

`html2pptx.js` imposes constraints the served slides deliberately do not meet —
satisfying them in place would wreck the pages (injected `<p>` margins alone
overflow ~84 slides). So each export script copies the slides to a temp dir,
fixes them there, and exports from the copy:

* **Text must sit in `<p>`/`<h1-6>`/`<ul>`/`<ol>`** — our text lives in `<div>`s
  and header `<span>`s. `scripts/wrap-leaf-text.mjs` wraps it on the copy, and
  appended CSS zeroes the resulting margins.
* **pptxgenjs cannot read SVG.** `scripts/svg_to_png.mjs` handles *inline*
  `<svg>`; decks referencing external `img/*.svg` need a `sharp` pass plus a
  `sed` rewriting the references (see `scripts/y9l11/export.sh`).
* **No text within 0.5" of a slide edge**, and no margins on inline elements —
  both fixed by CSS appended to the copy's stylesheet.
* **Background, border and shadow survive only on a `<div>`**, never on a text
  element. A styled chip must be `<div class="x"><p>…</p></div>`.
* Also unsupported: CSS gradients, `background-image` on divs.

### Working examples

Only two series have their export committed; the rest were exported ad hoc.
Copy whichever matches your canvas:

```bash
bash scripts/export_y7_l13.sh    # 1920px canvas, inline SVG
bash scripts/y9l11/export.sh     # 960pt canvas, external SVG files
```

Both print `✓ <deck>  pptx N/N · pdf ✓` per deck and exit non-zero if any deck
exports incompletely — a partial count means constraints were violated, so read
the count rather than assuming success.

### Building the slides themselves

Slide *content* is generated per series by its own Python builder — these are
not superseded by one another, each encodes its own lesson content and layout
invariants:

```
scripts/build_y7_l13.py          scripts/y8l11/build.py   (+ l1..l5.py, manifests)
scripts/build_y8_l10.py          scripts/y9l11/build.py   (+ art.py, l1..l5.py)
```

`scripts/y9l11/README.md` documents that series end to end, including the
layout invariants its builder enforces (max two new words per vocabulary slide,
max three worked examples, six listening items in two columns, …). Read it
before building a new series — those limits are measured, not stylistic.

### Verify before shipping

`scripts/check_slides.mjs` is the **only** checker; it catches content clipped
inside `.slide-content` and type under the classroom floor, and it measures each
deck at the canvas that deck declares. Measuring at the wrong size mis-reports
overflow, which is why the two canvases matter here too.

```bash
python3 -m http.server 8087 --directory index &
node scripts/check_slides.mjs --design y9-l11
```

## URL routing

No rewrites. Clean directory-based URLs:
- `deck.liyu.dev/` → `index/index.html`
- `deck.liyu.dev/designs/<id>/` → `index/designs/<id>/index.html`

## Local preview

Serve `index/` with any static server to preview locally before deploying:

```bash
cd index && python3 -m http.server 8080   # → http://localhost:8080
```

## Deployment

`vercel.json` is a no-build static serve:

```json
{ "framework": null, "installCommand": "", "buildCommand": "", "outputDirectory": "index" }
```

> **Why this config?** The servable content lives under `index/`, so `outputDirectory` points Vercel there directly — the gallery resolves at `/` and designs at `/designs/<id>/`. `installCommand`/`buildCommand` are empty because serving static HTML needs no build, and the root `package.json` deps (playwright, sharp, etc.) are local-only export tooling that must NOT be installed on deploy. `.vercelignore` keeps `node_modules/`, `scripts/`, `docs/`, and `.archive/` out of the upload.

The Vercel project is connected to `github.com/luojiahai/deck`, so deploys are
continuous — **push to `main` and it ships** to deck.liyu.dev. Open a PR instead
and Vercel comments a preview URL on it, which is the way to eyeball a new design
before it's public.

The CLI still works as a manual escape hatch (useful when Git is unavailable or
you want to deploy uncommitted work):

```bash
vercel deploy --prod    # production → deck.liyu.dev
vercel deploy           # preview URL
```

## Design generation

Use the **huashu-design** skill (`/huashu-design`) to generate HTML design prototypes.

🔴 **Hard rule: all design output MUST go under `index/designs/<design-id>/`.** Do not create design directories at the repo root or anywhere else. One subfolder per design, entry file must be named `index.html`.

### Slides convention

For multi-page designs (slideshows, courseware, presentations), put individual slides under `index/designs/<design-id>/slides/`:

```
index/designs/<design-id>/
├── index.html              ← Main entry point (e.g. slide overview / nav)
├── thumb.png
└── slides/
    ├── l1-intro.html
    ├── l2-content.html
    └── ...
```

Each slide is a self-contained HTML file. Use descriptive filenames (`l1-hobbies-intro.html`, `l8-review-quiz.html`) so the structure is scannable.
