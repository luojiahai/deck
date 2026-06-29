# Deck — Frame UI Redesign

**Date:** 2026-06-30
**Scope:** The website *frame* only — the gallery homepage (`index/index.html`) and the manifest it reads (`index/designs.json`). Individual designs/decks and their slides are **untouched**.

## Goal

Elevate the gallery homepage so it feels as crafted as the designs it holds, while keeping it a **generic design gallery** — it indexes every kind of artifact the `huashu-design` skill produces (slides, prototypes, animations, app mockups, infographics, web pages, …), not just lesson decks. Direction: **Warm Modern** — warm earthy palette, rounded thumbnail-forward cards, serif display type, a single color-coded category chip per card. Add a light/dark theme toggle.

## Non-goals (YAGNI)

- No tag/category **filter** controls and no sort control (only a handful of designs today).
- No category **legend** band on the page.
- No changes to any design under `index/designs/<id>/`, no changes to slides.
- No build step — stays a no-build static serve (per `CLAUDE.md`).

## Design decisions (locked)

1. **Ambition:** elevate, keep the bones — header → masthead → grid → footer.
2. **Masthead:** a quiet editorial intro band. Oversized serif `Deck.` wordmark (accent dot), a bilingual tagline (用专注做好每一页 · A gallery of crafted HTML designs), and a count line reading exactly **`N DESIGNS`** (uppercase, small, gold number) — nothing after it.
3. **Language:** balanced bilingual (Chinese + English) across masthead, search placeholder, and footer.
4. **Function:** purely a visual elevation **plus** a light/dark theme toggle. No filters, no sort.
5. **Generic model:** the gallery is type-agnostic. The one useful generic facet is **design type**, shown as a single color-coded chip per card. Optional free-form **tags** add context.
6. **Cards:** thumbnail-forward (the thumbnail *is* the artifact). Category chip overlaid top-left on the thumbnail; below it title, short description, then a footer row with date (left) and optional tags (right).

## Manifest model (`index/designs.json`)

Each design entry gains two **optional** fields. Existing fields unchanged. Frame degrades gracefully when a field is absent.

```json
{
  "id": "y7-l10",
  "title": "Y7 L10 · 几点？Telling Time in Chinese",
  "description": "…",
  "createdAt": "2026-06-28",
  "thumbnail": "designs/y7-l10/thumb.png",
  "type": "slides",
  "tags": ["Year 7", "中文"]
}
```

- **`type`** (optional, string): one of the category keys below. Absent → card renders with no chip.
- **`tags`** (optional, string[]): free-form context labels. Absent/empty → footer shows only the date.

The two existing entries (`y7-l10`, `y8-l7`) get `"type": "slides"` and sensible tags.

### Category taxonomy (chip label + color)

Earthy, slop-free palette — no purple-neon. Colors are CSS variables, themed for light & dark.

| key | label (bilingual) | light color | dark color |
|------|-------------------|-------------|------------|
| `slides` | Slides 幻灯片 | `#b88a3e` (gold) | `#d6a85c` |
| `prototype` | Prototype 原型 | `#d44c2f` (terracotta) | `#e8704f` |
| `animation` | Animation 动画 | `#4a8a72` (sage) | `#6cb39a` |
| `app` | App 应用 | `#3a5a78` (navy) | `#6f9cc4` |
| `infographic` | Infographic 信息图 | `#8a5a8c` (muted plum) | `#b98abb` |
| `web` | Web 网页 | `#a9742e` (clay) | `#cf9a52` |

Unknown/missing `type` → no chip (graceful default), so adding a new category later never breaks rendering.

## Visual system

- **Type:** existing serif stack (`"Songti SC", "Noto Serif SC", "Source Serif 4", Georgia, serif`) for display/titles; `system-ui, sans-serif` for small UI/meta text (search, chips, tags, count, footer).
- **Light palette:** `--bg:#f4f1ea`, `--panel:#fbfaf7`, `--card:#ffffff`, `--ink:#1f1e1b`, `--muted:#6f6e66`, `--faint:#a9a79c`, `--line:#e7e2d6`, `--accent:#d44c2f`, `--gold:#b88a3e`.
- **Dark palette:** `--bg:#1b1a17`, `--panel:#232220`, `--card:#262420`, `--ink:#f0ede4`, `--muted:#a6a298`, `--faint:#75726a`, `--line:#34322c`, `--accent:#e8704f`, `--gold:#d6a85c`. Category vars swap per table above.
- **Cards:** `border-radius:15px`, 1px `--line` border, soft warm shadow; hover lifts `translateY(-4px)`, deepens shadow, border → `--gold`. Thumbnail `aspect-ratio:16/10`, `object-fit:cover`; falls back to a warm gradient placeholder when `thumbnail` is absent.
- **Grid:** `repeat(auto-fill, minmax(320px, 1fr))`, `gap:24px`.
- **Header:** sticky, translucent blurred background, 1px bottom border. `Deck.` logo (left), spacer, search (right), theme toggle button (far right).
- **Footer:** quiet bilingual sign-off (`© 2026 Deck · 用专注做好每一页 · Made with focus`).

## Theme toggle behavior

- Toggle button in the header (☾ in light / ☀ in dark) flips a `dark` class on `<html>`/`<body>`.
- **Initial theme:** respect `prefers-color-scheme`; user's explicit choice persists in `localStorage` and overrides the media query on later visits.
- Apply the stored/preferred theme **before first paint** (tiny inline script in `<head>`) to avoid a flash.
- Palette transitions (`background`/`color`) animate ~0.35s for a smooth flip.

## Behavior (carried over, unchanged in spirit)

- Fetch `/designs.json`; render cards into the grid.
- **Search** filters across `title`, `description`, `type`, and `tags` (case-insensitive). Updates the count line.
- **States:** empty (no designs at all) and no-results (search matched nothing) — both restyled to match the warm system, bilingual copy retained.
- `escapeHtml` on all interpolated strings (kept from current implementation).

## Implementation notes

- Single self-contained `index/index.html` (inline `<style>` + `<script>`), consistent with the current no-build static serve. No new files, no dependencies.
- The render template adds: category chip (looked up from `type`), tags in the card footer, and the thumbnail-as-cover treatment.
- Keep accessibility basics: toggle is a real `<button>` with an `aria-label`; search input keeps a label/placeholder.

## Acceptance criteria

- [ ] Homepage shows the warm masthead with `Deck.` wordmark, bilingual tagline, and a count line reading exactly `N DESIGNS`.
- [ ] No category legend band on the page.
- [ ] Each card is thumbnail-forward with a single color-coded category chip (when `type` present), title, description, date, and optional tags.
- [ ] Working light/dark toggle: respects system preference, persists choice, no flash on load.
- [ ] Search filters across title/description/type/tags and updates the count.
- [ ] Empty and no-results states render in the new style.
- [ ] `designs.json` gains optional `type`/`tags`; both existing entries set to `type: "slides"` with tags. Missing fields degrade gracefully (no chip / date-only footer).
- [ ] Still a no-build static serve; `index/` previews correctly via a static server.
- [ ] Designs under `index/designs/` and all slides are byte-for-byte unchanged.
