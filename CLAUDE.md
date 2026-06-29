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
4. Run `vercel deploy --prod`

Downloadable `.pptx` exports (linked from a design's `index.html`) are an **optional, per-design** feature — some designs ship them (e.g. `y7-l10`), others are web-only (e.g. `y8-l7`). Keep PPTX/PDF source artifacts that aren't served (`slides-pptx/`, slide-preview `thumbs/`) out of `index/` — they bloat the deploy and are unreferenced.

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
