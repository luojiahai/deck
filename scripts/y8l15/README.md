# Y8 L15 · 社区 Neighbourhood — deck build

Six decks, 154 slides, from `docs/lesson-plans/y8-l15/`.
Output: `index/designs/y8-l15/`.

```bash
python3 scripts/y8l15/art.py        # 27 SVG drawings → index/designs/y8-l15/img/
python3 scripts/y8l15/build.py      # tokens.css + 154 slides + 6 deck shells + landing page
bash    scripts/y8l15/export.sh     # 6 × PPTX + 6 × PDF

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y8-l15
```

Canvas is **960pt**, so the PPTX export uses the skill's stock
`export_deck_pptx.mjs`, not this repo's 1920 fork.

## Why this series shares Lesson 13 and 14's palette

The repo groups a visual identity by **unit**, not by lesson. Lesson 13
opened Unit 5 with an architect's drafting vellum — cool paper, graphite
ink, slate, terracotta, brass — Lesson 14 furnished the rooms Lesson 13
drew, and Lesson 15 walks out of the front door onto the same drawing.
Putting it in a different palette would say the three lessons are
unrelated, which is the opposite of true.

`style.py` is therefore a near-copy of `scripts/y8l14/style.py` rather than
an import, so each series stays self-contained and y8l14 can be edited
without silently changing this deck. The one change is a deletion — see
below.

Nothing under `index/designs/y8-l15/` is hand-edited, the series landing
page included.

## What this series deliberately does NOT contain

The teacher asked for all three, so they are enforced structurally rather
than left to care:

* **No answer slides.** `s_cfu` has no answers parameter — a CFU slide can
  only carry questions. Answers are the teacher's to take live, on
  whiteboards or by cold call.
* **No pinyin-discrimination practice.** Textbook Ex. 7 (s/sh, CD 72) is
  out of the decks entirely, and there is no helper that could render one.
* **No 36-character dictation grid.** Ex. 3 is out too: it is a memory
  game over characters the students have not been taught, which is not
  what the test asks for.
* **Stroke-order copying of the lesson's own new words is not radical
  practice** and stays: `s_strokes` runs in Lessons 1–5 and is the only
  handwriting practice those twenty-three characters get anywhere in the
  sequence.

**Pinyin itself stays.** Excluding the pinyin *exercises* is not the same
as hiding pinyin: it sits on every new-word card and above every example
sentence, then comes off the board during practice. That is the Year 8
norm.

## Radicals: out of five lessons, in for one

The series was built without radicals, on instruction, and the cost was
stated plainly at the time rather than buried: **Unit 5 Test parts 3 and
4** ask for the radical of a character and the simple character inside a
compound, so students would have met two of the eleven test parts cold.
The teacher then asked for a slot, and Lesson 6 now carries it:

| Slide | What it is | From |
|---|---|---|
| `23-chars` | the four simple characters this lesson teaches, as reference | p.147 Ex. 9 (反 血 习 山) |
| `24-radicals-1` | write the radical and its meaning — 层 厅 辆 冰 超 站 | Test part 3, verbatim |
| `25-radicals-2` | find the simple character inside — 毕 忘 返 蚂 仙 鸣 | Test part 4, verbatim |

Four things about how it was fitted:

* It **runs as the lesson's game**. Fitting it cost four minutes taken
  across the other three activities rather than cutting one of them: the
  map talk 6→5, the information desk 9→8, the dream city 8→5. All four
  textbook activities survive.
* Both boards are **task boards, not answer boards** — the no-answer-slide
  rule above applies to them too. Round 1 offers a bank of nine for six
  characters, because it is the first time under timed conditions; the
  slide says out loud that the test gives no bank. Round 2 offers none,
  matching the test.
* **Lesson 15 is the right home for it**, not just the last one available.
  Three of Test part 4's six compounds hide a character this sequence
  itself teaches: 返 holds 反 and 仙 holds 山 (p.147 Ex. 9), 蚂 holds 马
  (Lesson 3's 马路). The round-2 board tells students that three of the
  six hide a character they met this week and points them back a page —
  **it does not name the pairs.** The pairings live in `l6.py`'s
  docstring, which is teacher-facing source; putting them on the slide
  would turn it into an answer board.
* `s_chars` shows **four** characters, not the unit's twelve. Three rows
  of four clips the canvas, and the eight from Lessons 13 and 14 are
  already a board in the y8l14 deck — they are recalled in the note
  instead.

`s_chars` and `s_radicals` are the only helpers that can produce a radical
slide, and they live in Lesson 6 alone.

## Layout invariants the builder enforces

* a vocabulary slide carries **at most two** new words (`s_words`; Lesson
  4's `然后` is the single-word cycle and centres itself — a cycle is *at
  most* two words, not exactly two)
* every pair runs the three-slide cycle A → B → C, and every C slide has an
  Extension — `s_write` requires it positionally
* `s_pattern` asserts at most **3** worked examples; the hardest goes on its
  own `s_focus` slide
* `s_cfu`, `s_strokes`, `s_list`, `s_dialogue` and `s_recall` **tighten
  themselves** past a threshold rather than silently clipping — but
  tightening is not unlimited. Text 2 is ten turns, which `s_dialogue`
  would still have run 92px off the bottom, so Lesson 5 **splits it across
  two slides** instead. Split the slide, never the type.
* `build_deck` **clears its slides directory** before writing, so a renamed
  slide cannot leave an orphan behind that still ships and still gets
  counted.
* every drawing is an SVG, never an emoji — Chromium ships no colour emoji
  font and both exports run through Chromium, so an emoji is an empty box.
  Nor is there **text** in any drawing: the PNG rasteriser in `export.sh`
  has no CJK font, so a 汉字 inside an SVG would survive the browser and
  vanish from the PowerPoint. That is why the bus for 五路 has a blank
  destination board and carries its route number as three brass pips, and
  why the eight shops are told apart by what is in the window rather than
  by a sign.

## Where each classroom lesson's content comes from

| Deck | Slides | Textbook / workbook | New words |
|---|---|---|---|
| `l1-shops-nearby` | 24 | p.142 Text 1 (first line); p.143 Act. 1; WB pp.164–165 | 附近 花店 文具店 家具店 |
| `l2-distance-li` | 26 | p.142 Text 1 complete; p.144 Act. 2; p.147 Act. 8 (CD 73); WB pp.165–166 | 超市 离 远 挺 |
| `l3-jiu-across-the-road` | 24 | p.145 Act. 5; p.152 Act. 14; WB pp.166–167 | 马路 对面 火车站 路 |
| `l4-first-then` | 25 | p.148 Text 2 (first half); p.150 Act. 11; WB pp.167–168 | 电影院 船 然后 |
| `l5-how-long` | 27 | p.148 Text 2 complete; p.152 Act. 13; p.153 Act. 15 (CD 75); WB pp.168–169 | 时间 大约 飞机 机场 |
| `l6-my-neighbourhood` | 28 | p.145 Act. 4; p.146 Act. 6; p.147 Act. 9; p.149 Act. 10; p.151 Act. 12; p.153 Act. 16; WB pp.170–173 | 水果店 书店 理发店 快餐店 |

All twenty numbered new-word entries of the textbook lesson land somewhere.
Lesson 6's four are the recognition set from p.143's answer bank, and all
four are 「a character you already own + 店」— which is why they fit in a
lesson whose real content is the map and the directions. Lesson 6
introduces **no new sentence pattern** on purpose, and says so on a slide
of its own: the work is running all five of them at once.

Lesson 4 is the only game-dominated lesson — the teacher picked that
direction for it — so its practice block is three games end to end, and
the consolidation task that normally opens Flexible Practice is folded
into the relay rather than sitting beside it.
