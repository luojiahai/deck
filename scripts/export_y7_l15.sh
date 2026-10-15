#!/usr/bin/env bash
# Export the Y7 L15 decks to PPTX and PDF. Run after scripts/build_y7_l15.py.
#
# A cross of the two existing wrappers: the slides keep their drawings as
# inline <svg> like scripts/export_y7_l13.sh, but sit on the 960pt canvas like
# scripts/y9l11/export.sh. html2pptx.js imposes constraints the served slides
# do not meet, so the PPTX export runs against a throwaway copy:
#
#   1. Text must sit in <p>/<h1-6>; our text lives in <div>s and <span>s.
#      wrap-leaf-text.mjs fixes that on the copy — doing it to the served
#      slides would inject default <p> margins and push slides over the canvas.
#   2. Inline SVG breaks the converter outright, and pptxgenjs cannot read an
#      SVG data: URI, so svg_to_png.mjs rasterises each drawing on the copy.
#   3. Use the SKILL's stock export_deck_pptx.mjs, not this repo's
#      export-deck-pptx-1920.mjs: these slides are 960pt (13.33in x 7.5in),
#      which is exactly the stock LAYOUT_WIDE.
#   4. No text may end within 0.5" of a slide edge, and inline elements may not
#      carry margins — both fixed by CSS appended to the copy's stylesheet.
#   5. html2pptx.js drops `opacity`, so each title slide's 4.5% watermark
#      character came out solid indigo. The copy paints it in the colour it
#      blends to instead (accent-indigo at 0.045 over bg-primary).
#
# The PDF export is a browser print, so it runs against the real slides.
set -euo pipefail

BASE="index/designs/y7-l15"
DECKS="l1-face-parts l2-body-parts l3-extra-body-words l4-radicals-structure \
       l5-changshenmeyang l6-reduplication-hair l7-describing-people l8-paragraph-reading"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/shared"
cp "$BASE/shared/tokens.css" "$TMP/shared/tokens.css"
cat >> "$TMP/shared/tokens.css" <<'CSS'

/* ── export copy only — see scripts/export_y7_l15.sh ── */
p { margin: 0; padding: 0; }                       /* injected wrappers */
span { margin-top: 0 !important; margin-bottom: 0 !important; }
.slide-footer { bottom: 23pt; }                    /* 0.5" edge rule */
.bg-char { color: #F2F1EF !important; opacity: 1 !important; }
CSS

for d in $DECKS; do
  mkdir -p "$TMP/$d/slides"
  cp "$BASE/$d/slides/"*.html "$TMP/$d/slides/"
done

echo "── preparing export copy ──"
node scripts/svg_to_png.mjs "$TMP"/*/slides/*.html
node scripts/wrap-leaf-text.mjs "$TMP"/*/slides/*.html | tail -1

fail=0
for d in $DECKS; do
  out=$(node .claude/skills/huashu-design/scripts/export_deck_pptx.mjs --slides "$TMP/$d/slides" --out "$BASE/$d/$d.pptx" 2>&1 | tail -1)
  node .claude/skills/huashu-design/scripts/export_deck_pdf.mjs \
       --slides "$BASE/$d/slides" --out "$BASE/$d/$d.pdf" > /dev/null 2>&1
  n=$(printf '%s' "$out" | grep -oE '[0-9]+/[0-9]+ slides' || true)
  case "$n" in
    "") echo "  ✗ $d — PPTX export produced nothing"; fail=1 ;;
    *)  a=${n%%/*}; b=${n#*/}; b=${b%% *}
        if [ "$a" = "$b" ]; then echo "  ✓ $d  pptx $n · pdf ✓"
        else echo "  ✗ $d  pptx $n (incomplete)"; fail=1; fi ;;
  esac
done
exit $fail

# Verify afterwards with:
#   python3 -m http.server 8087 --directory index &
#   node scripts/check_slides.mjs --design y7-l15
