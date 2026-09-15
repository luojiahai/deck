# Y8 L13 · 房子 House — deck build

Six decks, 148 slides, from `docs/lesson-plans/y8-l13/`.
Output: `index/designs/y8-l13/`.

```bash
python3 scripts/y8l13/art.py        # 27 SVG drawings → index/designs/y8-l13/img/
python3 scripts/y8l13/build.py      # tokens.css + 148 slides + 6 deck shells + landing page
bash    scripts/y8l13/export.sh     # 6 × PPTX + 6 × PDF

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y8-l13
```

Canvas is **960pt**, so the PPTX export uses the skill's stock
`export_deck_pptx.mjs`, not this repo's 1920 fork.

## Why this series has its own palette

The repo groups a visual identity by **unit**, not by year: y9-l10/11/12
share one look because they are one unit, and y8-l10/11/12 share another.
Lesson 13 opens Book 2 Unit 5, so it opens a new one — an architect's
drafting vellum. Cool paper and graphite where Unit 4 was warm cream, with
slate (drawing ink), terracotta (roof tile) and brass. A unit about floor
plans, storeys and where things sit should look like something drawn with a
straightedge.

The stylesheet lives in `style.py` as a string and `build.py` writes it to
`shared/tokens.css`. Nothing under `index/designs/y8-l13/` is hand-edited,
the series landing page included.

## What this series deliberately does NOT contain

The teacher asked for both, so they are enforced structurally rather than
left to care:

* **No answer slides.** `s_cfu` has no answers parameter — a CFU slide can
  only carry questions. Answers are the teacher's to take live, on
  whiteboards or by cold call.
* **No pinyin-discrimination and no radical / simple-character practice.**
  Textbook Ex. 1 (z/zh, CD 62) and Ex. 7 (光 金 匕 入), and workbook Ex. 10
  and Ex. 13, are out of the decks entirely, and there is no
  `s_components`-style helper in this builder, so such a slide cannot be
  added by copying a sibling.
  **Stroke-order copying of the lesson's own new words is not the same
  thing** and stays: `s_strokes` runs in Lessons 1, 2, 3 and 5 for the
  characters of Text 1 and Text 2.

Consequence worth knowing: **Unit 5 Test parts 3 and 4** (write the radical
and its meaning; find the simple character inside a compound) test exactly
the excluded material. Students meet those two parts cold. This is stated in
`docs/lesson-plans/y8-l13/06-garage-whole-house-mixed.md` and on the series
landing page.

## Layout invariants the builder enforces

* a vocabulary slide carries **at most two** new words (`s_words`; the lone
  `车库` in Lesson 5 is the one single-word cycle and centres itself)
* every pair runs the three-slide cycle A → B → C, and every C slide has an
  Extension — `s_write` requires it positionally
* `s_pattern` asserts at most **3** worked examples; the hardest goes on its
  own `s_focus` slide
* `s_cfu`, `s_strokes`, `s_list` and `s_recall` **tighten themselves** past a
  threshold rather than silently clipping — five CFU questions, five stroke
  rows, eight compact list rows and a fourth grid row each used to fall off
  the bottom of the canvas with no warning. Every tightened size is still at
  or above the classroom floor of 13pt (26px on the projector).
* `s_summary` in dense mode picks its column count from how many words it
  carries, so the Lesson 6 board of nineteen fits on one screen
* every drawing is an SVG, never an emoji — Chromium ships no colour emoji
  font and both exports run through Chromium, so an emoji is an empty box

## Where each classroom lesson's content comes from

| Deck | Slides | Textbook / workbook | New words |
|---|---|---|---|
| `l1-house-storeys` | 25 | p.122 Text 1 (first half); p.126 Act. 6; WB pp.144, 146 Ex. 4, 5 | 房子 房间 层 楼 楼上 楼下 |
| `l2-upstairs-rooms` | 26 | p.122 Text 1 (upstairs); p.125 Act. 4 (CD 63); p.131 Act. 13; WB pp.144–145, 147 Ex. 8 | 卧室 书房 浴室 洗澡 |
| `l3-downstairs-text1` | 25 | p.122 Text 1 complete; p.123 Act. 2; p.126 Act. 6; p.130 Act. 10; WB pp.145–146, 150 Ex. 12 | 客厅 餐厅 厨房 洗手间 |
| `l4-position-words` | 26 | p.124 Act. 3 + NOTE; p.128 Act. 8; WB p.147 Ex. 7, p.151 Ex. 14, 15 | 上面 下面 里面 外面 左面 右面 |
| `l5-outside-text2` | 25 | p.127 Text 2 (CD 64); WB p.148 Ex. 9, p.149 Ex. 11, p.152 Ex. 17 | 洋房 花园 前 后 车库 |
| `l6-garage-whole-house` | 21 | p.125 Act. 5; p.129 Act. 9; p.130 Act. 11 (CD 65); p.131 Act. 12; WB p.146 Ex. 3, p.152 Ex. 18, p.153 Ex. 20 | 停 辆 |

Textbook Act. 14 (the holiday-resort pamphlet), workbook Ex. 19 (the garden
essay) and the dictionary work of workbook Ex. 6 and 16 are out of the
sequence by the teacher's decision at scoping — 300 minutes would not hold
them alongside everything above.
