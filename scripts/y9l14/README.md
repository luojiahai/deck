# Y9 L14 · 问路 Asking the Way — deck build

Six decks, 120 slides, from `docs/lesson-plans/y9-l14/`.
Output: `index/designs/y9-l14/`.

```bash
python3 scripts/y9l14/art.py        # 19 SVG drawings → index/designs/y9-l14/img/
python3 scripts/y9l14/build.py      # tokens.css + 120 slides + 6 deck shells + series index

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y9-l14
```

Canvas is **960pt**. `build.py` writes the whole tree — `shared/tokens.css`,
every `slides/*.html`, each deck's `index.html` viewer, and the series
`index.html`. The only thing it does not own is `img/`, which `art.py` owns,
and `thumb.png`, which is a 1440×900 screenshot of the series index.

## Web-only — no PPTX

No `export.sh`, and the deck shells link no `.pptx` — same as y9-l13. If you
add an export later, use the skill's stock `export_deck_pptx.mjs` (960pt
canvas, not the repo's 1920 fork) and add the download link back into `SHELL`
in `build.py` **at the same time**; a shell that links a `.pptx` it does not
have 404s on the teacher.

## Visual identity

Deliberately identical to **y9-l13**: same Unit 5 palette (map paper, ink,
signal red `#B3321E`, route green, slate blue), same chrome, same type scale,
same three-slide cycle. L13 and L14 are consecutive lessons in one unit and
should read as one series on a projector — this is not a new design, it is
the same design carrying different content. `build.py` here is y9l13's with
the deck identity swapped; the helper set and `TOKENS` are byte-identical.

The series index differs in three places only: the hero motif (被 rather than
路), the three-pattern grammar panel, and the footnote's reason for having no
radical practice — see below.

## What this series deliberately does NOT contain

The teacher asked for both of these, so they are enforced structurally rather
than left to care:

* **No answer slides.** `s_cfu` has no answers parameter, so a CFU slide can
  only carry questions. Answers are the teacher's to take live.
* **No radical or component practice.** ⚠️ The reason differs from y9-l13's,
  and the series index says so: **Lesson 14 genuinely has component work in
  the workbook** — Ex. 9 (p.157, simple characters) and Ex. 14 (p.159,
  character-meaning pairs). They are out **on the teacher's instruction**, not
  because the book lacks them. Don't copy y9-l13's footnote wording back over
  this one; it would be false here.

  One exception, and it is not an exercise: `l1.py`'s 骑 note points out the
  马 radical as a *mnemonic* inside the vocabulary card. That is vocabulary
  teaching, not radical practice.

## Layout invariants the builder enforces

Inherited from y9l13 and all still live — at most two new words on a
vocabulary slide, every pair running A → B → C with an Extension on every C,
`s_pattern` ≤ 3 worked examples, `s_cfu` ≤ 4 questions, `s_list` ≤ 5 rows,
`s_recall` ≤ 4 rows, `s_route` ≤ 4 steps, textonly cards for words with no
picturable referent, never emoji.

Two words are odd-numbered in this series and use `s_word_one` rather than
being padded out with an already-taught word: 姓名 (l5 cycle 3) and 借书证
(l6 cycle 2).

## Where each classroom lesson's content comes from

| Deck | Slides | Textbook / workbook | New words |
|---|---|---|---|
| `l1-getting-around` | 22 | p.133 Act. 1, p.134 Act. 2–3; WB 3, 4 | 骑 自行车 购物 广场 车站 路 |
| `l2-bus-route` | 20 | p.132 Text 1 (CD 53); WB 1, 5, 8 | 座 庙 河 桥 |
| `l3-journeys-from-home` | 12 | p.135 Act. 4, p.136 Act. 5–6 (CD 54); WB 6, 7, 10, 11, 12 | — none |
| `l4-whats-in-the-bag` | 21 | p.138 Act. 7; WB 12, 15 | 手提包 钱包 钥匙 手机 现金 服装 |
| `l5-stolen` | 26 | p.137 Text 2 (CD 55), p.139 Act. 9, p.140 Act. 11 (CD 56); WB 16, 17, 21 | 偷 警察 被 留 姓名 |
| `l6-lost-property` | 19 | p.139 Act. 8, p.140 Act. 10, p.141 Act. 12; WB 18, 19, 22, 23 | 身份证 学生证 借书证 |

All 13 numbered textbook activities appear somewhere in the six.

**Lesson 3 is the short deck (12 slides) and that is correct** — it carries no
new vocabulary, so it has no cycles and no summary board. Don't "fix" it by
padding; the lesson is a speaking lesson and the slides are there to start
activities, not to be read.

Two placements moved after the lesson plans were written, both noted to the
teacher: **路** sits in l1 rather than arriving unexplained in l2, and **服装**
sits in l4 rather than l6 so 四彩服装店 is known before Text 2.

Out of the sequence by the teacher's decision at scoping: textbook Act. 13
(the round-the-world project) and workbook Ex. 2 (full measure-word cloze),
Ex. 13, Ex. 20. Ex. 9 and Ex. 14 are out on the separate no-radicals
instruction.

## One thing to know before editing l5

`l5-stolen` is the heaviest lesson in the sequence — three cycles, 被, and
Text 2. Text 2 therefore runs as **Activity 1 of Flexible Practice**, not
inside the I Do block, and the slide `section` strings say so. Text 2 is also
**split across two slides**: eight turns overflow one slide even at
`s_dialogue`'s tight tier. Don't merge them back.
