#!/usr/bin/env bash
# Export the Y7 L13 decks to PPTX and PDF. Run after scripts/build_y7_l13.py.
#
# The PPTX path cannot use the served slide HTML as-is. html2pptx.js (behind
# export-deck-pptx-1920.mjs) imposes three constraints this repo's slide markup
# does not meet, so the export runs against a throwaway copy:
#
#   1. Text must sit in <p>/<h1-6>/<ul>/<ol>; our text lives in <div>s.
#      Wrapping the SERVED slides would fix the export and wreck the page —
#      the injected <p> tags bring default margins and ~84 slides overflow.
#   2. Inline SVG breaks the converter outright (it calls el.className.includes,
#      which throws on an SVGAnimatedString), and pptxgenjs cannot read an SVG
#      data: URI. Each drawing is rasterised to a PNG instead.
#   3. No text may end within 0.5" of a slide edge, and inline elements may not
#      carry margins — both fixed by CSS appended to the copy's stylesheet.
#
# That is why index/designs/y7-l13/*/slides/*.html contain no <p> and keep their
# inline SVG, while the shipped PPTX files carry real, editable text runs.
#
# The PDF export is a browser print, so it runs against the real slides.
set -euo pipefail

BASE="index/designs/y7-l13"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

DECKS="l1-xihuan-colours1 l2-text1-he l3-de-frame l4-yanse-question \
       l5-text2-ma-ye l6-radicals-pinyin l7-survey-mixing l8-revision"

mkdir -p "$TMP/shared"
cp "$BASE/shared/tokens.css" "$TMP/shared/tokens.css"
cat >> "$TMP/shared/tokens.css" <<'CSS'

/* ── export copy only — see scripts/export_y7_l13.sh ── */
p { margin: 0; padding: 0; }                       /* injected wrappers */
span { margin-top: 0 !important; margin-bottom: 0 !important; }
.slide-footer { bottom: 46px; }                    /* 0.5" edge rule */
.wc-art .svg-art, .vc-art .svg-art, .t-art .svg-art {
  height: 100%; width: auto; display: block; margin: 0 auto;
}
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
  out=$(node scripts/export-deck-pptx-1920.mjs --slides "$TMP/$d/slides" --out "$BASE/$d/$d.pptx" 2>&1 | tail -1)
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
