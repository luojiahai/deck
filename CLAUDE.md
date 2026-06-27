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
2. Add an entry to `index/designs.json`:
   ```json
   { "id": "<design-id>", "title": "Name", "description": "...", "createdAt": "YYYY-MM-DD", "thumbnail": "designs/<design-id>/thumb.png" }
   ```
3. Run `vercel deploy --prod`

## URL routing

No rewrites. Clean directory-based URLs:
- `deck.liyu.dev/` → `index/index.html`
- `deck.liyu.dev/designs/<id>/` → `index/designs/<id>/index.html`

## Deployment

```bash
vercel deploy --prod    # production → deck.liyu.dev
vercel deploy           # preview URL
```

## Design generation

Use the **huashu-design** skill (`/huashu-design`) to generate HTML design prototypes. Output files go into `index/designs/<design-id>/`.
