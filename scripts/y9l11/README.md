# Y9 L11 · 零食 Snacks — deck build

Five decks, 102 slides, from `docs/lesson-plans/y9-l11/`.
Output: `index/designs/y9-l11/`.

```bash
python3 scripts/y9l11/art.py        # 17 SVG drawings → index/designs/y9-l11/img/
python3 scripts/y9l11/build.py      # 102 slides + 5 deck shells
bash    scripts/y9l11/export.sh     # 5 × PPTX + 5 × PDF

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y9-l11
```

## Verification

`scripts/check_slides.mjs` is the only checker — it catches both content
clipped inside `.slide-content` and type under the classroom floor. It measures
each deck at the canvas that deck declares, which matters because this repo has
two: the y7/y8/y9-l7..l9 decks are 1920x1080px and these are 960pt (=1280x720,
scaled 1.5x by the deck shell at presentation time). `.slide-content` is
positioned against the viewport rather than the fixed-size body, so measuring at
the wrong size mis-reports overflow in whichever direction the mismatch runs.

## Layout invariants the builder enforces

* a vocabulary slide carries **at most two** new words (`s_words`)
* every pair runs the three-slide cycle A → B → C, and every C slide has an
  Extension (`s_write` requires it positionally)
* `s_pattern` asserts at most **3** worked examples — a fourth is 100px too
  tall and gets cropped. The hardest example goes on its own `s_focus` slide.
* `s_listening` lays six multiple-choice items out in **two columns**; one
  column of six is 94px too tall.
* `s_dialogue` tightens its own rows past four turns.
* a word with no picturable referent (各种各样, 从小, 总是, 加, 完) gets a
  `textonly` card rather than a forced drawing.

## PPTX export

Use the **skill's stock** `export_deck_pptx.mjs`, not this repo's
`export-deck-pptx-1920.mjs`. These slides are 960pt (13.33in × 7.5in), which is
exactly the stock `LAYOUT_WIDE`; the 1920 variant declares 20in × 11.25in and
rejects every slide. See the header of `export.sh` for the other three
constraints the throwaway export copy fixes.

One constraint bit us and is worth remembering: **html2pptx carries
background/border/shadow only on a `<div>`, never on a text element.** The
Correct-the-Teacher chips were `<p class="err-wrong">`; they are now
`<div class="err-wrong"><p>…</p></div>`.
