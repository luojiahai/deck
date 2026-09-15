# Y9 L12 · 外出就餐 Eating Out — deck build

Six decks, 114 slides, from `docs/lesson-plans/y9-l12/`.
Output: `index/designs/y9-l12/`.

```bash
python3 scripts/y9l12/art.py        # 18 SVG drawings → index/designs/y9-l12/img/
python3 scripts/y9l12/build.py      # 114 slides + 6 deck shells
bash    scripts/y9l12/export.sh     # 6 × PPTX + 6 × PDF

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y9-l12
```

Canvas is **960pt**, so the PPTX export uses the skill's stock
`export_deck_pptx.mjs`, not this repo's 1920 fork. Same visual family as
`y9-l10` 菜市场 and `y9-l11` 零食 — same Unit 4, same `tokens.css` palette
and type scale.

## What this series deliberately does NOT contain

The teacher asked for both of these, so they are enforced structurally
rather than left to care:

* **No answer slides.** `s_cfu` has no answers parameter — a CFU slide can
  only carry questions. Answers are the teacher's to take live, on
  whiteboards or by cold call.
* **No pinyin-discrimination and no radical/component practice.** Textbook
  Act. 2 (memorise 12 components) and workbook Ex. 2 and 17 are out of the
  decks entirely, and `s_components` — the helper the y9-l11 builder used
  for exactly that slide — is absent from this builder's copy of `build.py`
  so it cannot come back by accident. Lesson 12 has no pinyin exercise.

## Layout invariants the builder enforces

* a vocabulary slide carries **at most two** new words (`s_words`)
* every pair runs the three-slide cycle A → B → C, and every C slide has an
  Extension (`s_write` requires it positionally)
* `s_pattern` asserts at most **3** worked examples — the hardest one goes on
  its own `s_focus` slide
* `s_listening` lays six multiple-choice items out in two columns
* `s_dialogue` tightens its own rows past four turns
* a word with no picturable referent (饱, 饿, 只, 再来) gets a `textonly`
  card rather than a forced drawing — and never an emoji, which renders as an
  empty box in the PPTX and PDF because the export path goes through Chromium

## Where each classroom lesson's content comes from

| Deck | Slides | Textbook | New words |
|---|---|---|---|
| `l1-buffet-vocab` | 17 | pp.110–111, Act. 1 | 自助餐 龙虾 三文鱼 寿司 |
| `l2-desserts-text1` | 23 | pp.110–112, Act. 1, 3; WB 8 | 烤 牛排 甜品 奶酪 饱 |
| `l3-meal-story` | 14 | pp.112–114, Act. 4, 5, 6, 7; WB 21 | — (consolidation) |
| `l4-ordering-menu` | 23 | pp.115–116, 120, Act. 14 + NOTE | 菜单 点菜 饿 烤鸭 只 |
| `l5-cooking-methods` | 21 | pp.115–117, Act. 8, 10; WB 18 | 红烧 蒸 肉丝 青菜 |
| `l6-drinks-project` | 16 | pp.117, 119, 121, Act. 9, 12, 15 | 杯 绿茶 瓶 |

Textbook Act. 11 and 13 and workbook Ex. 22–24 are out of the sequence by
the teacher's decision at scoping, to make room for the Act. 15 project.
