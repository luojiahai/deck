#!/usr/bin/env bash
# Export the Y9 L11 decks to PPTX and PDF. Run after scripts/y9l11/build.py.
#
# Same reasoning as scripts/export_y7_l13.sh: html2pptx.js (behind
# export-deck-pptx-1920.mjs) imposes constraints the served slides do not meet,
# so the PPTX export runs against a throwaway copy:
#
#   1. Text must sit in <p>/<h1-6>; our slide-header <span>s hold bare text.
#      wrap-leaf-text.mjs fixes that on the copy — doing it to the served
#      slides would inject default <p> margins and push slides over the canvas.
#   2. pptxgenjs cannot read an SVG. This series references its drawings as
#      <img src="../../img/name.svg">, so every drawing is rasterised to PNG at
#      3x and the references rewritten. (svg_to_png.mjs handles INLINE <svg>;
#      this deck uses external files, hence the sharp pass below.)
#   3. Use the SKILL's stock export_deck_pptx.mjs, not this repo's
#      export-deck-pptx-1920.mjs: these slides are 960pt (13.33in x 7.5in),
#      which is exactly the stock LAYOUT_WIDE. The 1920 variant declares a
#      20in x 11.25in layout and rejects every slide.
#   4. No text may end within 0.5" of a slide edge — handled by the CSS
#      appended to the copy's stylesheet.
#
# The PDF export is a browser print, so it runs against the real slides.
set -euo pipefail

BASE="index/designs/y9-l11"
DECKS="l1-snack-nouns l2-dui-congxiao l3-breakfast l4-lunch-dinner l5-wan-yihou"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

mkdir -p "$TMP/shared" "$TMP/img"
cp "$BASE/shared/tokens.css" "$TMP/shared/tokens.css"
cat >> "$TMP/shared/tokens.css" <<'CSS'

/* ── export copy only — see scripts/y9l11/export.sh ── */
p { margin: 0; padding: 0; }
span { margin-top: 0 !important; margin-bottom: 0 !important; }
CSS

echo "── rasterising drawings ──"
node -e '
const sharp = require("sharp"); const fs = require("fs");
const src = "'"$BASE"'/img", out = "'"$TMP"'/img";
let n = 0;
Promise.all(fs.readdirSync(src).filter(f => f.endsWith(".svg")).map(f => {
  n++;
  return sharp(src + "/" + f).resize(600, 600, { fit: "contain",
    background: { r: 0, g: 0, b: 0, alpha: 0 } }).png()
    .toFile(out + "/" + f.replace(/\.svg$/, ".png"));
})).then(() => console.log("  " + n + " drawings → png"));
'

for d in $DECKS; do
  mkdir -p "$TMP/$d/slides"
  cp "$BASE/$d/slides/"*.html "$TMP/$d/slides/"
  sed -i '' 's|\(\.\./\.\./img/[a-z0-9_-]*\)\.svg|\1.png|g' "$TMP/$d/slides/"*.html
done

echo "── preparing export copy ──"
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
#   node scripts/check_slides.mjs --design y9-l11
