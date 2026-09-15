# Y9 L13 · 社区 Neighbourhood — deck build

Six decks, 124 slides, from `docs/lesson-plans/y9-l13/`.
Output: `index/designs/y9-l13/`.

```bash
python3 scripts/y9l13/art.py        # 21 SVG drawings → index/designs/y9-l13/img/
python3 scripts/y9l13/build.py      # tokens.css + 124 slides + 6 deck shells + series index

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y9-l13
```

Canvas is **960pt**. `build.py` writes the whole tree — `shared/tokens.css`,
every `slides/*.html`, each deck's `index.html` viewer, and the series
`index.html`. The only thing it does not own is `img/`, which `art.py` owns,
and `thumb.png`, which is a 1440×900 screenshot of the series index.

## Web-only — no PPTX

There is no `export.sh` in this directory and the deck shells link no
`.pptx`. Y9 L10–L12 ship one; this series does not. If you add an export
later, use the skill's stock `export_deck_pptx.mjs` (960pt canvas, not the
repo's 1920 fork) and add the download link back into `SHELL` in `build.py`
at the same time — a shell that links a `.pptx` it does not have 404s on the
teacher.

## Visual identity

Unit 5 gets its own palette — **map paper, ink, and a signal red**
(`#B3321E`), with a route green and a slate blue — so a 社区 deck is
distinguishable from the Unit 4 食物 decks (warm cream and brick) across a
staffroom. The *structural* vocabulary is shared with y9-l10 / y9-l11 /
y9-l12: same chrome, same three-slide cycle, same type scale, same
typography floor.

## What this series deliberately does NOT contain

The teacher asked for both of these, so they are enforced structurally
rather than left to care:

* **No answer slides.** `s_cfu` has no answers parameter — a CFU slide can
  only carry questions. Answers are the teacher's to take live, on
  whiteboards or by cold call.
* **No pinyin-discrimination and no radical/component practice.** Lesson 13
  has no "Learn the radicals" box in the textbook at all, and Book 3 has
  dropped pinyin-discrimination exercises. Workbook Ex. 2, 3 and 16 are the
  only component work in the lesson and they are out of the decks entirely;
  `s_components` — the helper the y9-l11 builder used for exactly that slide
  — is absent from this builder's copy of `build.py` so it cannot come back
  by accident.

## Layout invariants the builder enforces

Each of these is an assertion, so a known overflow cannot silently return:

* a vocabulary slide carries **at most two** new words (`s_words`); an odd
  word count gets `s_word_one`, a single centred card, rather than being
  padded out with an already-taught word
* every pair runs the three-slide cycle A → B → C, and every C slide has an
  Extension (`s_write` requires it positionally)
* `s_pattern` asserts at most **3** worked examples — the hardest one goes on
  its own `s_focus` slide
* `s_cfu` asserts at most **4** questions
* `s_list` asserts at most **5** rows, or 6 compact
* `s_recall` asserts at most **4** rows and has a dense tier for the Lesson 6
  board that carries all 23 words of the sequence
* `s_route` asserts at most **4** steps
* a word with no picturable referent (生活, 方便, 看到, 向) gets a `textonly`
  card rather than a forced drawing — and never an emoji, which renders as an
  empty box in a PPTX or PDF export because the export path goes through
  Chromium

Two notes on `art.py`:

* the `<g>` sets `fill="none"` as the group default. Without it a stroke-only
  `<path>` inherits `fill: black` and floods solid — that is how the first
  draft of the file lost all nine direction arrows.
* the direction words get **diagrams**, not pictures. An arrow that goes
  straight and then bends right *is* what 往右拐 means.

## Where each classroom lesson's content comes from

| Deck | Slides | Textbook / workbook | New words |
|---|---|---|---|
| `l1-where-i-live` | 18 | p.122 Text 1 (1st half), Act. 2; WB 4 | 市中心 方便 生活 邮局 |
| `l2-facilities` | 19 | p.122 Text 1 (2nd half), Act. 1, 4; WB 9 | 诊所 银行 百货公司 市政大楼 |
| `l3-front-back` | 19 | p.122 Text 1 in full, Act. 3, 5 (CD 50), 6; WB 7, 9 | 教堂 公园 前面 后面 |
| `l4-directions` | 23 | p.127 Text 2 dial. 1–2 (CD 51), Act. 7, 8, 9; WB 8 | 咖啡馆 过 一直 往前 红绿灯 |
| `l5-turns` | 24 | p.127 Text 2 dial. 3; WB 10, 18 | 向 拐 转 路口 第 |
| `l6-build-the-town` | 21 | Act. 11, 12 (CD 52), 13 | 看到 右手 钟 |

All 27 New Words from pp.123 and 128 are covered, and all 13 numbered
textbook activities appear somewhere in the six.

Workbook Ex. 1, 5, 6, 12, 13, 14, 15, 17, 19, 20, 21 and 22 are out of the
sequence by the teacher's decision at scoping — 300 minutes does not hold 22
workbook exercises on top of the textbook. Ex. 2, 3 and 16 are out on the
separate no-radicals instruction.

## Known cosmetic issue

`img/di.svg` — the 一 / 二 / 三 inside the three junction beads are hand-drawn
paths and read as "T" and "Z" at small sizes. A revision was proposed and the
teacher chose to keep the art as it is; noted here so the next person does not
think it went unseen.
