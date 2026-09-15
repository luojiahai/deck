# Y8 L14 · 家具 Furniture — deck build

Six decks, 140 slides, from `docs/lesson-plans/y8-l14/`.
Output: `index/designs/y8-l14/`.

```bash
python3 scripts/y8l14/art.py        # 19 SVG drawings → index/designs/y8-l14/img/
python3 scripts/y8l14/build.py      # tokens.css + 140 slides + 6 deck shells + landing page
bash    scripts/y8l14/export.sh     # 6 × PPTX + 6 × PDF

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y8-l14
```

Canvas is **960pt**, so the PPTX export uses the skill's stock
`export_deck_pptx.mjs`, not this repo's 1920 fork.

## Why this series shares Lesson 13's palette

The repo groups a visual identity by **unit**, not by lesson: y8-l10/11/12
share one look because they are Book 2 Unit 4, and y9-l10/11/12 share
another. Lesson 13 opened Unit 5 with an architect's drafting vellum — cool
paper, graphite ink, slate, terracotta, brass — and Lesson 14 furnishes the
rooms Lesson 13 drew. Putting it in a different palette would say the two
lessons are unrelated, which is the opposite of true.

`style.py` is therefore a near-copy of `scripts/y8l13/style.py` rather than
an import, so each series stays self-contained and y8l13 can be edited
without silently changing this deck. The one addition is `.cv-row` /
`.cv-from` / `.cv-to`, for the 吗 → V-not-V rewrite in Lesson 5.

Nothing under `index/designs/y8-l14/` is hand-edited, the series landing
page included.

## What this series deliberately does NOT contain

The teacher asked for both, so they are enforced structurally rather than
left to care:

* **No answer slides.** `s_cfu` has no answers parameter — a CFU slide can
  only carry questions. Answers are the teacher's to take live, on
  whiteboards or by cold call.
* **No pinyin-discrimination practice.** Textbook Ex. 2 (c/ch, CD 67) and
  Ex. 10 (the group pinyin-writing game) are out of the decks entirely, and
  there is no helper that could render one.
* **Stroke-order copying of the lesson's own new words is not radical
  practice** and stays: `s_strokes` runs in Lessons 1–5 and is the only
  handwriting practice those fifteen characters get anywhere in the
  sequence.

## Radicals: out of five lessons, in for one

The series was built without radicals, on instruction, and the cost was
stated plainly at the time rather than buried: **Unit 5 Test parts 3 and 4**
ask for the radical of a character and the simple character inside a
compound, so students would have met two of the eleven test parts cold. The
teacher then asked for a slot, and Lesson 6 now carries it:

| Slide | What it is | From |
|---|---|---|
| `18-chars` | the eight simple characters the unit teaches, as reference | p.126 Ex. 7 (光 金 匕 入) · p.137 Ex. 11 (井 亡 乌 勺) |
| `19-radicals-1` | write the radical and its meaning — 层 厅 辆 冰 超 站 | Test part 3, verbatim |
| `20-radicals-2` | find the simple character inside — 毕 忘 返 蚂 仙 鸣 | Test part 4, verbatim |

Three things about how it was fitted:

* It **runs as the lesson's game**, not as a fourth activity, so the
  23-minute practice block still balances. 20 Questions went; the p.141
  Ex. 17 interview board stays as the fallback if the race runs short.
* Both boards are **task boards, not answer boards** — the no-answer-slide
  rule above applies to them too. Round 1 offers a bank of nine for six
  characters, because it is first exposure; the slide says out loud that
  the test gives no bank. Round 2 offers none, matching the test.
* `s_chars` and `s_radicals` are the only helpers that can produce a
  radical slide, and they live in Lesson 6 alone.

**Pinyin itself stays.** Excluding the pinyin *exercises* is not the same as
hiding pinyin, and the teacher confirmed this at scoping: it sits on every
new-word card and above every example sentence, then comes off the board
during practice. That is the Year 8 norm.

## Layout invariants the builder enforces

* a vocabulary slide carries **at most two** new words (`s_words`; Lesson 2's
  `里面`, Lesson 3's `电炉` and Lesson 4's `书桌` are the single-word cycles
  and centre themselves)
* every pair runs the three-slide cycle A → B → C, and every C slide has an
  Extension — `s_write` requires it positionally
* `s_pattern` asserts at most **3** worked examples; the hardest goes on its
  own `s_focus` slide
* `s_cfu`, `s_strokes`, `s_list`, `s_dialogue` and `s_recall` **tighten
  themselves** past a threshold rather than silently clipping. Three of
  those thresholds are one notch lower here than in y8l13, because this
  deck's activity rows carry a target sentence rather than a two-word gloss
  and so wrap: `s_list` packs at six rows and again at seven, `s_strokes`
  has a third notch for six characters (Lesson 1 copies 沙 发 茶 几 柜 张).
  Every tightened size is still at or above the classroom floor of 13pt
  (26px on the projector); the seven-row notch moves geometry only.
* `s_convert` is **not** `s_errors`: the 吗 column is correct Chinese, so it
  gets no strike-through and no red. A student who reads a struck-through
  左边 concludes 吗 questions are wrong, which is a worse error than the one
  the slide is preventing.
* `s_summary` in dense mode picks its column count from how many words it
  carries, so the fifteen-word board fits one screen. 张 and 把 pass `None`
  for their picture there — their counting diagrams are legible at 200px and
  a smudge at the 40px a summary cell gives them.
* `build_deck` **clears its slides directory** before writing. Writing over
  the top left an orphan behind when a slide was renamed — invisible in the
  browser because the shell's manifest stopped referencing it, but still
  shipped and still counted (built 140, checked 141).
* every drawing is an SVG, never an emoji — Chromium ships no colour emoji
  font and both exports run through Chromium, so an emoji is an empty box.
  Nor is there **text** in any drawing: the PNG rasteriser in `export.sh`
  has no CJK font, so a 汉字 inside an SVG would survive the browser and
  vanish from the PowerPoint. That is why 张 and 把 are taught by counting
  one, two, three objects rather than by a captioned diagram.

## Where each classroom lesson's content comes from

| Deck | Slides | Textbook / workbook | New words |
|---|---|---|---|
| `l1-living-room` | 23 | p.132 Text 1 (living-room half); p.133 Act. 1; p.135 Act. 5; WB pp.154–155 | 沙发 茶几 电视柜 张 |
| `l2-appliances-inside` | 24 | p.132 Text 1 complete; p.136 Act. 7; WB pp.155–156 | 空调 洗衣机 里面 |
| `l3-kitchen-measure-words` | 26 | p.132 Text 1 kitchen half; p.134 Act. 3, 4; p.135 Act. 6; p.137 Act. 9 (CD 68); WB pp.157–158 | 冰箱 烤箱 电炉 |
| `l4-my-own-room` | 23 | p.138 Text 2 (first half); p.139 Act. 12, 13; WB pp.160–161 | 椅子 把 书桌 |
| `l5-storage-v-not-v` | 23 | p.138 Text 2 complete; p.139 NOTE + Act. 14; p.141 Act. 16 (CD 70); WB pp.161–162 | 衣柜 书架 |
| `l6-furniture-shopping` | 21 | p.136 Act. 8; p.140 Act. 15; p.141 Act. 17; WB pp.162–163 | — (句型 应该上几楼？) |

Lesson 6 introduces no nouns on purpose, and says so on a slide of its own:
应该 (Unit 4), 楼 and 几 (Lesson 13), 上 and 请 (Year 7) are all already
known, so the pattern is assembled rather than taught. That is worth pointing
out to students at this stage.
