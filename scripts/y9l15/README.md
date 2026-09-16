# Y9 L15 · 邻居 Neighbours — deck build

Six decks, 116 slides, from `docs/lesson-plans/y9-l15/`.
Output: `index/designs/y9-l15/`.

```bash
python3 scripts/y9l15/art.py        # 8 SVG drawings → index/designs/y9-l15/img/
python3 scripts/y9l15/build.py      # tokens.css + 116 slides + 6 deck shells + series index

# verify (needs a server: python3 -m http.server 8087 --directory index &)
node    scripts/check_slides.mjs --design y9-l15
```

Canvas is **960pt**. `build.py` writes the whole tree — `shared/tokens.css`,
every `slides/*.html`, each deck's `index.html` viewer, and the series
`index.html`. The only thing it does not own is `img/`, which `art.py` owns,
and `thumb.png`, which is a 1440×900 screenshot of the series index.

## Web-only — no PPTX

No `export.sh`, and the deck shells link no `.pptx` — same as y9-l13 and
y9-l14. If you add an export later, use the skill's stock
`export_deck_pptx.mjs` (960pt canvas, not the repo's 1920 fork) and add the
download link back into `SHELL` in `build.py` **at the same time**; a shell
that links a `.pptx` it does not have 404s on the teacher.

## Visual identity

Deliberately identical to **y9-l13** and **y9-l14**: same Unit 5 palette
(map paper, ink, signal red `#B3321E`, route green, slate blue), same
chrome, same type scale, same three-slide cycle. L13, L14 and L15 are the
three lessons of one unit and should read as one series on a projector —
this is not a new design, it is the same design carrying different content.
`build.py` here is y9l14's with the deck identity swapped; `TOKENS` is
byte-identical.

The series index differs in three places only: the hero motif (把 rather
than 被), the three-pattern grammar panel, and the footnote's reason for
having no radical practice — see below.

## What this series deliberately does NOT contain

The teacher asked for both of these, so they are enforced structurally
rather than left to care:

* **No answer slides.** `s_cfu` has no answers parameter, so a CFU slide can
  only carry questions. Answers are the teacher's to take live.
* **No radical or component practice.** ⚠️ The reason differs again from
  both siblings, and the series index says so: **Lesson 15 has no textbook
  radicals box at all.** The only component work in the lesson is workbook
  Ex. 5 (p.165, write the simple characters 匕 反 血 学 山 平 角 果 食), and
  that is out **on the teacher's instruction**. Don't copy y9-l14's footnote
  wording back over this one — it names textbook exercises that do not exist
  here.

  Workbook Ex. 21 (16 action verbs) is character writing, not component
  work, and was available; it did not end up in a lesson.

## Helper changes from y9l14

Three, all forced by this lesson's content and all in `build.py`:

* **`s_route` / `s_arrows` dropped.** They are L13/L14 direction helpers and
  Lesson 15 has no route content. Removed rather than left unused.
* **`s_lisc` gained a tight tier** at 4 criteria. Four criteria overflow the
  canvas by 61px at the default row metrics, and the criteria come from the
  lesson plan — the deck does not get to choose which one the class never
  sees. Only padding and gaps shrink; no type goes below the floor. The
  helper now asserts at 5.
* **`s_dialogue` gained a third tier** past 6 turns, for Lesson 4's Text 2.
  y9-l14 split its 8-turn Text 2 across two slides; here the complaint and
  the reply have to be on one board or the pattern is invisible, so the tier
  exists instead. 17pt is 34px — still over the 26px classroom floor.

## Layout invariants the builder enforces

Inherited and all still live — at most two new words on a vocabulary slide,
every pair running A → B → C with an Extension on every C, `s_pattern` ≤ 3
worked examples, `s_cfu` ≤ 4 questions, `s_lisc` ≤ 4 criteria, `s_list` ≤ 5
rows, `s_recall` ≤ 4 rows, textonly cards for words with no picturable
referent, never emoji.

## Where each classroom lesson's content comes from

| Deck | Slides | Textbook / workbook | New words |
|---|---|---|---|
| `l1-moving-in` | 21 | p.142 Text 1 (first half), p.143 Act. 1, p.144 Act. 3; WB 1 | 最近 搬家 邻居 烦人 |
| `l2-noisy-neighbour` | 21 | p.142 Text 1 (full), p.146 Act. 5 (CD 58); WB 1, 7 | 听见 响 半夜 哭 |
| `l3-ba-sentence` | 22 | p.147 Text 2 (first half), p.148 NOTE + Act. 7, Act. 8, p.146 Act. 6 (被, 一……就, 太……了); WB 14 | 吵 醒 声 把 |
| `l4-polite-requests` | 20 | p.147 Text 2 (full), p.149 Act. 10, p.150 Act. 11, p.151 Act. 13 (CD 60), p.146 Act. 6 (rest); WB 20 | 注意 办法 |
| `l5-right-now` | 16 | p.145 Act. 4, p.149 Act. 9, p.150 Act. 12, p.151 Act. 14; WB 13 | — none |
| `l6-my-neighbours` | 16 | p.152 Act. 15, p.153 Act. 16; WB 10, 16 | — none |

All 16 numbered textbook activities and both texts appear somewhere in the
six.

**Lessons 5 and 6 are the short decks (16 slides) and that is correct** —
neither carries new vocabulary, so neither has cycles or a summary board.
Don't pad them; they are a speaking lesson and a writing lesson, and the
slides are there to start activities, not to be read.

Out of the sequence by the teacher's decision at scoping: textbook Act. 2
(time-phrase race) and workbook Ex. 18 (internet research), Ex. 19 (typing),
Ex. 23 (80–100 word writing). Act. 4 and Act. 6 were on that same at-risk
list and the teacher **kept** them — Act. 4 sits in l5, Act. 6 splits across
l3 and l4.

## Two things to know before editing

**`l4-polite-requests` has one cycle, not three.** Two new words is all the
lesson carries, and the time that would have gone to a second and third pair
goes to the two patterns and to Text 2 in full. That is the plan, not an
omission.

**Act. 16 (p.153) runs compressed**, as l6's Activity 1 extension, and l6
carries a slide that says so out loud. As a full judged project it needs more
room than 300 minutes leaves. If the teacher ever wants it properly, it is a
standalone lesson, not a squeeze.
