# Y9-L7: Split inline answers into next-slide reveals

## Problem

Eight slides in the `y9-l7` lesson set show a question/prompt and its answer/correction/translation on the same slide. This breaks the deck's existing convention (already used for `07b-text1-answers.html`, `09b-cfu-answers.html`, `08b-cfu-answers.html`) where answers are revealed on a separate slide shown immediately after the question, not baked into the same view as the prompt.

Affected slides:

| File | Issue |
|---|---|
| `l2-opinions/slides/11-game.html` | "Correct the Teacher" — wrong + correct sentence shown together in each error card |
| `l3-interest-reasons/slides/11-game.html` | Same game — table row shows correction column alongside the error |
| `l5-text2-vocab/slides/07-text2.html` | Comprehension questions (`cq-item`) show the answer (`cq-a`) inline next to each question |
| `l5-text2-vocab/slides/12-game.html` | Sentence Scramble — answer box shown next to each scrambled chip set |
| `l7-complement-numbers/slides/10-game.html` | Sentence Jumble — answer row shown directly under each round's tokens |
| `l8-review-test-prep/slides/10-game-r1.html` | Flash cards print the English answer in plain text under each Chinese card (note says "cover answers first" but nothing is actually hidden) |
| `l8-review-test-prep/slides/11-game-r2.html` | Round 2 prompt cards print the Chinese translation directly under the English prompt |
| `l8-review-test-prep/slides/12-game-r3.html` | Round 3 challenge cards show the answer box / correction / example inline on each card |

## Approach

For each of the 8 slides, apply the deck's existing answer-reveal pattern:

1. **Edit the original slide**: remove the answer/correction/translation content, leaving only the question/prompt. Where the existing convention has a cue (`07-text1.html`'s comprehension card → `09-cfu.html`'s "答案见下一张 · Answers on next slide →"), add the same cue text in the same dashed `answer-hidden` style.
2. **Create a new `Xb-...-answers.html` sibling slide** (file naming follows the existing `07b-text1-answers.html` / `09b-cfu-answers.html` convention: same number, `b` suffix, `-answers` in the name). Styling: gold accent (`--accent-gold`) header bar, "↳ Answers" in `section-name`, section-label "Answers Revealed · 答案", main-title `答案 · <original title>`. Contains exactly the content stripped from the original slide.
3. **Update that lesson's `index.html`** `DECK_MANIFEST` to insert the new slide entry immediately after the original, label prefixed with `  ↳ Answers · ...` (matching the existing `07b-text1-answers.html` entry's label format). No renumbering of subsequent slides — the `b` suffix slots in between existing numbers, exactly as already done elsewhere in this deck.

Manifests to update: `l2-opinions/index.html`, `l3-interest-reasons/index.html`, `l5-text2-vocab/index.html` (two insertions: after `07` and after `12`), `l7-complement-numbers/index.html`, `l8-review-test-prep/index.html` (three insertions: after `10`, `11`, `12`).

No new CSS classes are needed — every answer-slide already has a precedent in the existing `Xb` files to copy styling from.

## Per-slide content split

- **L2-11 game**: original keeps the 4 "✗ Wrong" sentences only (drop `ec-arrow`/`ec-correct-row`); answers slide shows all 4 corrections.
- **L3-11 game**: original table keeps only the "Error" column; answers slide shows the full table with corrections.
- **L5-07 text2**: original keeps dialogue + the 3 questions (drop `cq-a`); answers slide shows the 3 answers.
- **L5-12 game**: original keeps the 4 scrambled chip rows only (drop `answer-col`); answers slide shows the 4 unscrambled sentences.
- **L7-10 game**: original keeps the 5 rounds' tokens only (drop `answer-row`); answers slide shows the 5 correct sentences.
- **L8-10 game-r1**: original keeps the 5 flash cards' Chinese only (drop `answer-reveal`); answers slide shows the 5 English answers.
- **L8-11 game-r2**: original keeps the 5 English prompts only (drop `card-zh`); answers slide shows the 5 Chinese translations.
- **L8-12 game-r3**: original keeps the 3 challenge prompts only (drop answer boxes / correction rows / open-answer example); answers slide shows the 3 answers.

## Out of scope

- No other slides in `y9-l7` are touched beyond the 8 listed and their 5 manifests.
- No changes to `shared/tokens.css` — existing tokens cover all needed styling.
- No changes to other lesson sets (y7, y8).

## Memory update

Save a feedback memory: lesson slides must never reveal an answer on the same slide as its question/prompt — always split into a question slide followed by a separate "↳ Answers" reveal slide. All lesson slides are student-facing (the content projected to the class), not teacher lesson-plan notes — teacher-only instructions (pacing notes, OTR strips, "cold call" cues) are fine as supplementary annotations, but the actual answer/translation must not be visible until the reveal slide.
