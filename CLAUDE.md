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
├── vercel.json             ← No-build static serve of index/ (see Deployment)
├── docs/lesson-plans/<design-id>/   ← lesson plans the builders read (not served)
├── scripts/                ← per-series builders + export/check passes (not served)
├── .resources/             ← textbook & workbook PDFs (lesson-planning skill)
└── .vercel/                ← Vercel project config (do not delete)
```

## Adding a new design

1. Place the design's static files in `index/designs/<design-id>/` (entry point must be `index.html`)
2. Add a `thumb.png` (1440×900) to the design folder — this is the gallery card image
3. Add an entry to `index/designs.json`:
   ```json
   { "id": "<design-id>", "title": "Name", "description": "...", "createdAt": "YYYY-MM-DD",
     "thumbnail": "designs/<design-id>/thumb.png", "type": "slides", "tags": ["Year 7", "中文", "Topic"] }
   ```
   `type` drives the card's category chip; `type` and `tags` both feed the
   search index. **Just append it at the end** — array order no longer
   decides which column a card lands in.

   The gallery puts each year level in its own column at 3-up by placing
   every card in a column explicitly (`index/index.html`: cards carry a
   `data-col`, and the grid runs `grid-auto-flow: row dense`, which drops
   each card into the earliest free row of its own column). That holds
   whatever the per-year deck counts are and whatever order this file is
   in. It replaced an earlier convention of interleaving the years
   round-robin and letting the cards flow, which only worked while the
   years had compatible counts.

   Array order still controls two things, so keep it chronological: the
   order *within* each column, and the reading order at narrower widths,
   where the grid falls back to 2-up or 1-up and year columns switch off.
   Year columns also switch off while a search is active, so results are
   never stranded in one column.

4. Commit and push to `main` — Vercel deploys it to production automatically

Downloadable `.pptx` / `.pdf` exports (linked from a design's `index.html`) are an **optional, per-design** feature — see [Editable PPTX export](#editable-pptx-export). Keep PPTX/PDF source artifacts that aren't served (`slides-pptx/`, slide-preview `thumbs/`) out of `index/` — they bloat the deploy and are unreferenced.

## Editable PPTX export

The exporter is generic: the huashu-design skill's `html2pptx.js` turns slide
HTML into native PowerPoint text runs and shapes (real editable text, not
pictures). Everything in `scripts/` around it is a prep or check pass, also
design-agnostic. The skill's scripts live at
`.claude/skills/huashu-design/scripts/` (`export_deck_pptx.mjs`,
`export_deck_pdf.mjs`, `html2pptx.js`).

**Exporting a deck** — pick by the canvas its `shared/tokens.css` declares, or
every slide is rejected:

| Canvas | PPTX exporter |
|---|---|
| `960pt` — **use this for new decks** | the skill's stock `export_deck_pptx.mjs` |
| `1920px` — legacy, 13 decks, don't add more | `scripts/export-deck-pptx-1920.mjs`, the skill's exporter with one line changed |

PDF always uses the skill's `export_deck_pdf.mjs`, against the real slides.

Copy the nearest working script rather than starting fresh —
`scripts/export_y7_l13.sh` (1920px, inline SVG) or `scripts/y9l11/export.sh`
(960pt, external SVG). They are near-identical wrappers; the deltas are the
deck list, the exporter, and SVG handling. Both print `pptx N/N` per deck and
exit non-zero on a partial count — read the count, don't assume success.

**Why they export from a temp copy:** `html2pptx.js` requires text in
`<p>`/`<h1-6>`, no SVG, no CSS gradients, no `background-image` on divs,
background/border/shadow only on a `<div>`, and no text within 0.5" of an edge.
The served slides deliberately break these — wrapping text in place injects `<p>`
margins that overflow ~84 slides. So each script copies the slides, runs
`wrap-leaf-text.mjs` / `svg_to_png.mjs` and appended CSS on the copy, and
exports that. Never fix the served slides to please the exporter.

**Verify before shipping** (`check_slides.mjs` is the only checker; it measures
each deck at the canvas that deck declares):

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

**Every slide series is generated — edit the builder, not the output.** Each
series has a Python builder (`scripts/build_<design-id>.py`, or
`scripts/<design-id>/build.py` plus per-lesson modules for newer ones) that
reads `docs/lesson-plans/<design-id>/` and writes the whole tree:
`shared/tokens.css`, every `slides/*.html`, and each deck's `index.html`
viewer. Nothing under `index/designs/<design-id>/` is hand-maintained — a hand
edit is lost on the next run, so change the builder and rerun. Builders also
assert layout invariants (a vocab slide introduces at most two new words, at
most 3 worked examples per pattern slide, …) so a known overflow cannot come
back.

```bash
python3 scripts/<design-id>/art.py     # SVG drawings, if the series has them
python3 scripts/<design-id>/build.py   # slides + deck shells
bash    scripts/<design-id>/export.sh  # PPTX + PDF (optional, per design)
```

**New slide series use the 960pt canvas.** The whole contract, in
`shared/tokens.css`:

```css
html, body { width: 960pt; height: 540pt; margin: 0; padding: 0; overflow: hidden; }
p, h1, h2, h3, h4 { margin: 0; }
```

Type is then sized in `pt`, with a 13pt floor for anything a student must read
— 1pt = 2px on a 1080p projector, so 13pt lands at 26px.

Why: `html2pptx.js` reads the body's CSS size as physical inches, so 960pt
lands on 13.333in × 7.5in — PowerPoint's standard widescreen, and exactly
pptxgenjs's `LAYOUT_WIDE`, so the skill's stock exporter works unforked. The
older 1920px decks convert to a non-standard 20in × 11.25in and need the
repo's forked exporter. Both look identical on a projector (each deck shell
scales to fit); the canvas only shows up in the PPTX.

🔴 **Fix the canvas before authoring a single slide.** Converting a finished
series costs a full pass over every slide.

There is no shared stylesheet template — each series carries its own palette
and class vocabulary, so a sibling deck's `tokens.css` is that deck's design
language, not a starting point. Two ways to the canvas:

* **new visual identity** → author the stylesheet against the contract above.
* **same unit as an existing 1920px deck**, where the series should stay one
  visual family → convert *that* deck's stylesheet px → pt at 1pt = 2px in the
  builder, with a single `px2pt()` over both the stylesheet and every emitted
  slide: lesson content stays written in px, and there is one place to get the
  scale wrong.

When copying a 960pt **deck shell**, two details are per-deck and easy to miss:
the slide count in the progress bar is hardcoded, and the shell links its own
`.pptx` — which 404s in a web-only series.
