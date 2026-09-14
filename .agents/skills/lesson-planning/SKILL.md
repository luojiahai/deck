---
name: lesson-planning
description: >
  Plan 50-minute Chinese lessons for Years 7–9, aligned to 轻松学中文 (Easy Steps to Chinese).
  Teaching focus is five units: Year 7 Book 1 Unit 5 (Lessons 13–15), Year 8 Book 2 Units 4 and 5
  (Lessons 10–15), Year 9 Book 3 Units 4 and 5 (Lessons 10–15).
  Source of truth: the six textbook and workbook PDFs in .resources/, plus cached unit references.
  Use this skill whenever a teacher asks you to plan a Chinese lesson, design a Chinese class activity,
  create Chinese learning materials, or brainstorm Chinese teaching ideas — for any of these year levels.
  Also trigger when the user mentions any of the focus topics in a teaching context: colours, clothing,
  parts of the body, vegetables and fruits, three meals a day, eating out, house, furniture,
  neighbourhood, fresh market, snacks, asking the way, neighbours.
  Earlier topics (time, daily routine, transport, hobbies, music, sports, dance, school subjects,
  school facilities, stationery) are taught material — still trigger, since they come up in Review
  phases and revision lessons.
  If the request has anything to do with planning, structuring, or designing activities for Chinese class
  at these year levels, use this skill — even if the user doesn't say "lesson plan" explicitly.
  If the user is clearly talking about a different subject or year level, do NOT trigger.
---

# Chinese Lesson Planning (轻松学中文)

This skill creates 50-minute Chinese lesson plans for Years 7–9, drawing content exclusively from the 轻松学中文 (Easy Steps to Chinese) series. Students are English-native speakers; approximately 30% speak Chinese fluently.

Year 7 = Book 1, Year 8 = Book 2, Year 9 = Book 3; each book is 5 units × 3 lessons. `references/book-index.md` maps every lesson in every book to its textbook and workbook pages.

## Teaching Focus — Five Units

Planning happens in these units only:

| Year | Unit | Lessons | Topics |
|---|---|---|---|
| 7 | Book 1 · Unit 5 | 13–15 | Colours 颜色 · Clothing 穿着 · Parts of the Body 人体部位 |
| 8 | Book 2 · Unit 4 | 10–12 | Vegetables and Fruits 蔬菜、水果 · Three Meals a Day 一日三餐 · Eating Out 外出就餐 |
| 8 | Book 2 · Unit 5 | 13–15 | House 房子 · Furniture 家具 · Neighbourhood 社区 |
| 9 | Book 3 · Unit 4 | 10–12 | Fresh Market 菜市场 · Snacks 零食 · Eating Out 外出就餐 |
| 9 | Book 3 · Unit 5 | 13–15 | Neighbourhood 社区 · Asking the Way 问路 · Neighbours 邻居 |

Everything earlier in the books is **taught material** — draw on it for Review phases and revision lessons, but don't plan new lessons from it unless the teacher asks.

If the teacher names a lesson outside these five units, plan it — just say once that it's outside the current focus, in case they misspoke.

## Critical Process Rules

These rules override everything else. Follow them in order.

### Rule 1: Never Prescribe Activities Without Asking

**The teacher chooses the activities. You do not.** For every lesson, present 2–3 options (different directions: speaking-heavy, writing-heavy, game-heavy, mixed) and let the teacher pick. Only write the full lesson plan AFTER they've chosen.

If the teacher asks for multiple lessons at once, ask lesson-by-lesson. Do not batch-skip this step — that's the #1 failure mode of this skill.

### Rule 2: Read the Reference, Then Verify Coverage

Before finalizing any lesson plan, read the relevant unit reference (see **Source Material** below — extract it from the PDFs if it isn't cached yet). Then cross-check:

1. Is every vocabulary item covered?
2. Is every sentence pattern covered?
3. Are the **radicals** from the textbook taught? (Each unit has "Learn the radicals" sections — check the reference's "Radicals" or "Textbook Activities" section.)
4. Are the **pinyin exercises** covered? (Y7 especially has "Circle the correct pinyin" exercises.)
5. Are all **textbook activities** represented? (The reference lists them page-by-page: speaking practice, listening exercises, group work, games, word-building.)
6. Are the **workbook exercises** drawn on? Character-copying with stroke order, radical writing, phrase building, translation both ways, reading comprehension and dictionary work all belong in class — there is no homework, so anything the workbook offers has to happen in a lesson or not at all.
7. Does the sequence prepare students for the unit's **Revision and Test** pages? There is no review lesson at the end, so this happens inside the six — see **Test readiness without a review lesson**.

If any are missing, add them before presenting to the teacher. If they genuinely don't fit in six lessons, say which ones and let the teacher choose what to cut — never drop content silently.

### Rule 3: Save to `docs/lesson-plans/<year>-l<lesson>/`

Lesson plans go in one directory per textbook lesson: `docs/lesson-plans/y9-l10/01-market-vocab-writing.md`. Create the directory if it doesn't exist. Full naming convention under **Multi-Lesson Planning** below.

---

## Before You Begin

### Step 0: Establish Context

Ask only what isn't already clear from the request:

1. **Year level** — 7, 8, or 9 (= Book 1, 2, 3)
2. **Which lesson** — which of the book's 15 lessons are they teaching? (e.g. "Lesson 10: Time", "Lesson 7: Hobbies — Music")
3. **Where in the lesson sequence** — Is this the first lesson in the unit? Second? Have students already seen some of the vocabulary?
4. **Available materials** — Does the classroom have a projector? Do students have 1:1 devices (for Kahoot/Quizlet)? Mini whiteboards?
5. **Recent issues** — Anything from the last lesson that needs revisiting? Any students who need extra attention?

If the teacher doesn't specify which lesson, show them the in-scope lessons for their year and ask them to pick:

| # | Year 7 (Book 1) | Year 8 (Book 2) | Year 9 (Book 3) |
|---|---|---|---|
| 10 | — | Vegetables and Fruits 蔬菜、水果 | Fresh Market 菜市场 |
| 11 | — | Three Meals a Day 一日三餐 | Snacks 零食 |
| 12 | — | Eating Out 外出就餐 | Eating Out 外出就餐 |
| 13 | Colours 颜色 | House 房子 | Neighbourhood 社区 |
| 14 | Clothing 穿着 | Furniture 家具 | Asking the Way 问路 |
| 15 | Parts of the Body 人体部位 | Neighbourhood 社区 | Neighbours 邻居 |

The full 15-lesson list for each book is in `references/book-index.md` if the teacher wants to go back to earlier material.

### The Hard Rule: Content Comes From the Books

**You must not invent vocabulary, grammar points, dialogues, or cultural content.** Everything comes from 轻松学中文. Read the unit's reference before designing anything, and if something the teacher wants isn't in the book, say so — don't make it up.

## Source Material

Three layers, in order of preference:

1. **Cached unit references** — `references/y<year>-unit<n>.md`. Fully extracted: vocabulary lists, grammar, texts, radicals, pinyin exercises, page-by-page textbook activities, workbook exercises, test coverage, audio tracks. Read these directly.

   Cached so far: `y7-unit4.md` (Book 1 U4, L10–12) · `y8-unit3.md` (Book 2 U3, L7–9) · `y9-unit3.md` (Book 3 U3, L7–9). All three are **already-taught** units that sit directly before an in-scope unit — read them for Review phases, not for new content.

   **None of the five in-scope units is cached yet.** The first lesson planned in each one pays the extraction cost; the other two are free.

2. **The PDFs in `.resources/`** — three textbooks and three workbooks, the source for every other unit:

   ```
   .resources/轻松学中文 1 textbook.pdf    .resources/轻松学中文1 workbook.pdf
   .resources/轻松学中文 2 textbook.pdf    .resources/轻松学中文2 workbook.pdf
   .resources/轻松学中文 3 textbook.pdf    .resources/轻松学中文 3 workbook.pdf
   ```

   They are **scanned images with no text layer** — `pdftotext` returns nothing. Render the pages and read them: `references/extracting-from-pdfs.md` has the procedure, and `references/book-index.md` has the page range for every lesson in every book.

3. **Nothing else.** `.resources/` is gitignored and local-only. If it's missing, tell the teacher rather than working from memory.

### Extracting a new unit

When the teacher picks a lesson whose unit has no cached reference:

1. Look up the lesson's PDF pages in `references/book-index.md`.
2. Follow `references/extracting-from-pdfs.md` to render and read them.
3. Write the result to `references/y<year>-unit<n>.md` so the next lesson in that unit costs nothing.
4. Then plan the lesson.

Extract the **whole unit** (all three lessons), not just the one being taught — lessons in a unit share a Revision/Test block and the later lessons build on the earlier ones.

---

## Single Lesson vs Multi-Lesson Planning

After Step 0, pick the right path:

- **One lesson** (e.g., "plan a lesson on time"): Read the reference file, then go straight to the Lesson Structure phases below (Phase 1–5). Write the plan in one pass using the output template.
- **A full sequence for one textbook lesson** (e.g. "Lesson 10: Time"): **six** classroom lessons. Follow the Multi-Lesson Planning process below.

---

## Multi-Lesson Planning

**One textbook lesson = six classroom lessons.** That's the default sequence length — six 50-minute lessons, six slide decks, six plan files. Build a different number only if the teacher asks for one.

**No review or test-prep lesson.** The sequence ends on content, not on revision. Lesson 6 teaches and consolidates like the rest; it does not become a 复习 lesson. Revision happens inside the lessons — see **Test readiness without a review lesson** below.

When the teacher asks for a sequence on a textbook lesson (e.g. "Lesson 10: Time"), follow this process:

### Step A: Scope the Sequence

First, read the reference file. Present a table showing how the textbook content maps to lessons:

```
| Lesson | Focus | New words | Textbook Content Covered |
|---|---|---|---|
| 1 | O'clock (点) | 点, 十点, 零 (3) | p.70 New Words; numbers review |
| 2 | Minutes (分) | 分, 五分, 刻 (3) | p.70–71: X点Y分; Ex.1 speaking, Ex.2 pinyin |
| ... | ... | ... | ... |
```

Cite **printed** page numbers here — that's what the teacher sees in their book.

**The "New words" column is not decoration.** Each lesson introduces about 4–6 new words, because every pair runs a three-slide cycle (see **Vocabulary Slides**). A textbook lesson with fifteen new words spreads them over several lessons in the sequence — this column is where the teacher sees that distribution and can move words between lessons before anything is written.

Ask: "Does this breakdown look right? Any changes?"

### Step B: Ask Activity Preferences — One Lesson at a Time

**This is the most important step. Do not skip it.** For each lesson in the sequence, present 2–3 activity options and let the teacher choose. Go lesson-by-lesson:

> "**Lesson 1: O'clock (点)** — three directions:
> A — Speaking + Listening heavy (choral, pair drill, Telephone game)
> B — Writing focused (paper exercises, Bingo)
> C — Game heavy (Slap the Board, Writing Relay, high energy)
> Which direction?"

Wait for the answer before moving to Lesson 2. Repeat for every lesson in the sequence.

### Step C: Generate Individual Lesson Files

Only after ALL activity preferences are confirmed, write each lesson as a **separate file**, in one directory per textbook lesson:

```
docs/lesson-plans/y9-l10/
├── 01-market-vocab-writing.md
├── 02-bi-comparison-writing.md
├── 03-text1-shopping-writing.md
├── 04-snack-vocab-writing.md
├── 05-text2-dialogue-speaking.md
└── 06-prices-measure-words-game.md
```

Six files, numbered `01`–`06`. No `07`, no `08`, and no `review` or `test-prep` file.

- Directory: `docs/lesson-plans/y<year>-l<lesson-number>/`
- File: `<NN>-<slug>-<direction>.md`, where `<direction>` is the activity direction the teacher chose in Step B — `writing`, `speaking`, `game`, or `mixed`.

**One lesson per file.** Do not put all lessons in a single file — the teacher needs to open them individually for each class.

### Step D: Verify Coverage

After writing, check each lesson against the reference file's "Textbook Activities" section. Confirm every textbook page element (vocabulary, patterns, radicals, pinyin exercises, activities) appears somewhere in the sequence. If anything is missing, add it and tell the teacher what was added.

**Six lessons is a tighter budget than it looks.** A textbook lesson runs 8–12 pages with fifteen-plus new words, several patterns, radicals, pinyin exercises and a dozen numbered activities, plus the workbook. Some of it will not fit in 300 minutes.

When it doesn't fit, **say which items are at risk and let the teacher choose what goes** — at Step A, before anything is written. Do not quietly drop the radicals exercise or the listening tasks because the sequence filled up. Silent omission is the failure mode here; a short list of "these three won't fit, which do you want?" is the fix.

### Test readiness without a review lesson

The sequence has no 复习 lesson, so the unit's Revision and Test pages get prepared inside the six:

- **Every lesson's Review phase (0–8 min) is the revision.** Six lessons means six cumulative recaps — that is more distributed practice than one review lesson at the end ever gave, and better spaced.
- **Pull test-format items into ordinary lessons.** The workbook Test uses particular formats — match the picture, write the radical, translate both ways, rearrange to form a sentence. Use those formats as the *practice activities* through the sequence, so the test format is familiar long before the test.
- **Lesson 6's plenary looks back over the whole sequence**, not just that lesson. Same 7-minute plenary, wider scope.
- **If the teacher wants a dedicated revision lesson before the test, that's a separate request** — offer it, don't build it into the six by default.

---

## Lesson Structure (50 Minutes)

Every lesson follows this exact structure. Times are guides — the teacher can adjust.

```
 0–8 min   Review (复习) — revisit last lesson's content
 8–10 min  Learning Intention + Success Criteria — state and display
10–20 min  I Do — explicit teaching, model the new language
20–43 min  Flexible Practice — We Do → You Do, with extension, CFU, games
43–50 min  Plenary — summarize, exit ticket, self-assessment
```

---

## Phase 1: Review (0–8 min)

Purpose: activate prior knowledge, surface gaps, build confidence for the new content.

### What to Review

- Key vocabulary and sentence patterns from the **previous lesson**
- If this is the first lesson of a unit, review the last lesson of the previous unit (or relevant prior knowledge from the year)

### How (Pick 1–2)

| Method | Description | Best for |
|---|---|---|
| Quick quiz (mini whiteboards) | 4–5 questions, students write answers, hold up | Grammar points, time expressions, translation |
| Pair dialogue | Students do last lesson's dialogue from memory, then swap roles | Speaking, fluency |
| Flashcard rapid fire | Teacher shows word (Chinese side), class chorally says pinyin + English | Vocabulary recall |
| Bingo | Pre-made bingo grids with last lesson's vocab | Vocabulary, low-pressure |
| Correct the teacher | Teacher says/writes 3 sentences with deliberate errors, students find and fix | Grammar, common mistakes |
| Slap the board | Two students at board, teacher says word, they slap it | Vocabulary, high energy |

### Key Rule

The review must connect to today's learning intention. If today is about daily routine, the review should surface time expressions (which they learned in the previous lesson). Name the connection explicitly: "Last lesson we learned how to tell the time — today we're going to use that to talk about our daily routine."

---

## Phase 2: Learning Intention + Success Criteria (8–10 min)

### Learning Intention

A single sentence. Start with "We are learning to..." (WALT) or "To understand...". State what students will **learn**, not what they will **do**.

Good: "We are learning to describe our daily routine in Chinese."
Bad: "We are going to do a worksheet on daily routine."

### Success Criteria

2–4 criteria. Format: **"I can..." followed by the target in Chinese (with English clarification)**.

Examples:
- "I can say what time I do things (用中文说日常活动的时间)"
- "I can use 一边…一边… to describe doing two things at once"
- "I can ask someone how they get to school (你怎么上学?)"

Write the success criteria on the board (or projector) and keep them visible for the entire lesson.

---

## Phase 3: I Do (10–20 min)

Teacher-directed instruction. This is where you introduce the new language.

### Components

1. **Present the new vocabulary in three-slide cycles** (5–8 min)

   Two words at a time, and each pair runs the same three steps — **words → example sentences → write your own**. Students never meet a new word without immediately seeing it used and then using it themselves. Full slide spec in **Vocabulary Slides** below.

   - **A · The two words** — character → pinyin → English, with a picture where the word is picturable. Model pronunciation twice, class repeats twice (choral). Point out radical clues where helpful ("Notice 泳 has 氵 (water) — swimming!")
   - **B · Example sentences** — 2–3 sentences using the new words, the last one using both. Only the two new words are new; everything else is already taught. Read aloud, class repeats, one comprehension question
   - **C · Write your own** — a sentence frame, 60–90 seconds writing on whiteboards or in books, teacher takes 2–3 aloud. Harder prompt on the same slide for whoever finishes early
   - After three cycles (six words), one recall slide: those six in characters only, class reads them back
   - For Y7: keep pinyin visible. For Y8/Y9: gradually hide pinyin during practice

   When the last cycle is done, close the block with a **summary slide** (all today's words, characters and pictures only) and a **task that uses all of them** — sorting, a shopping list, a described picture, a connected paragraph. That task usually runs as the first activity of Flexible Practice rather than inside I Do; see **Closing the block** below.

   **This paces a lesson at about 4–6 new words.** If the textbook lesson has more, spread them across the six-lesson sequence rather than speeding up the cycle.

2. **Model the key sentence pattern** (3–5 min)
   - Present the target structure clearly
   - Do a think-aloud: "To say 'I go to school by bus', I need... 我 + 坐 + 公共汽车 + 上学"
   - Model 3–4 examples, each slightly different
   - Keep every example **real and usable** — sentences a student could actually say about their own life. No joke examples (no 我每天坐飞机上学). They get the laugh and then get remembered instead of the correct form.
   - Make the last example the hardest one — two clauses, or the pattern combined with something from a previous lesson. The fluent students need something to bite on from the first minute.

3. **Check for understanding** (2–3 min) — embed CFU here:
   - "What does 公共汽车 mean? Thumbs up if you know."
   - "How would I say 'I go by train'? Write on your whiteboard."
   - "What's wrong with this sentence? 我坐上学公共汽车。"

4. **Present the text/dialogue** (if applicable, 3–5 min)
   - Read aloud, students follow
   - Read together (choral)
   - Ask 2–3 comprehension questions (can answer in English for Y7, push for Chinese in Y8/Y9)

---

## Phase 4: Flexible Practice (20–43 min)

This is a single 23-minute block. Move gradually from **We Do** (guided) to **You Do** (independent). Throughout, keep every student responding and keep checking understanding (CFU) — but deliver those live rather than labelling them in the plan.

### Activity Design

**🔴 Do not prescribe activities. Ask the teacher first.** This is Critical Process Rule 1. For each lesson, present 2–3 distinct options with clear direction labels. Example format:

> "**Lesson X: [Topic]** — For the practice phase, three directions:
> **A — [Label]** (e.g. Speaking-heavy): [brief description of activities]
> **B — [Label]** (e.g. Writing-focused): [brief description]
> **C — [Label]** (e.g. Game-dominated): [brief description]
> Which direction?"

Adapt the options based on the lesson content. Common option types:
- **Speaking-heavy**: choral response, pair dialogue, chain drills, role-play
- **Writing-focused**: worksheets, character writing, dictation, sentence building
- **Listening-heavy**: listen-and-draw, listen-and-tick, dictation, Bingo
- **Game-dominated**: multiple short games in sequence, competition format
- **Mixed/balanced**: one speaking activity + one writing activity + one game
- **Step-by-step**: slow build, concept-first, one idea at a time
- **Challenge-led**: harder entry point, independent production from the start, teacher circulating rather than leading

If the teacher has told you their classroom setup (projector but no whiteboards, etc.), incorporate that into every option — don't suggest activities that require unavailable materials.

After the teacher picks, fill the 23-minute block with a sequence of 2–4 activities that:
- Start guided (We Do), end independent (You Do)
- Include at least 1 game
- Give every activity a real **Extension** (below)
- Cover the relevant textbook activities from the reference file

**Do not annotate activities with Scaffold or OTR labels.** No "**Scaffold:** …" line, no "**OTR:** …" line, and no scaffold/OTR boxes on the slides. Support and questioning technique are things the teacher does live — writing them out as boilerplate under every activity padded the plans without changing the lesson. The one annotation that earns its place is the Extension.

### Extension (Required in Every Activity)

About 30% of the class speaks Chinese fluently. For them the main task is finished in two minutes, and a token "and write one more sentence" extension is not work — it's waiting dressed up as work. Every activity needs an extension that is **genuinely a different task**, not more repetitions of the same one.

**The test:** could a fluent speaker complete the extension without thinking? If yes, it isn't one.

#### What makes an extension actually harder

Raise at least two of these above the main task:

| Dimension | Main task | Extension |
|---|---|---|
| **Length** | One sentence | Connected paragraph, 4–6 sentences that hang together |
| **Clauses** | Single clause | Two clauses joined — 因为…所以…, 虽然…但是…, 除了…以外, 一边…一边… |
| **Support** | Word bank, sentence frame, pinyin visible | Nothing on screen; produce from memory |
| **Preparation** | Written first, then read | Spontaneous — respond live to an unseen prompt |
| **Register** | Statement about self | Report about someone else, compare two things, justify an opinion |
| **Reach back** | Today's vocabulary only | Today's pattern carrying vocabulary from an earlier lesson or unit |
| **Role** | Answer the question | Ask the questions — interview a partner, then summarise what they said |

#### Write it into the activity

Extensions go inside the activity description, not in a table at the end. Give the actual target language, not a description of it — the teacher needs something they can put on the board.

Weak (don't write this):
> - **Extension:** More complex sentences for stronger students.

Strong:
> **Activity 2: Market stall role-play — You Do (10 min)**
> Pairs. A is the stallholder, B is buying. B asks the price of three items and buys two.
> A: 西红柿多少钱一斤？ B: 五块钱一斤。
>
> **Extension —** B is buying for a family dinner on a budget of 50 块. B must compare two stalls using 比 (这家的鱼比那家的便宜), justify each choice out loud (因为…所以我买这个), and at the end report the total and what they didn't buy and why. No word bank, no frames. If they finish, they swap and run it again as the stallholder — who must talk them *up* to a more expensive item.

The extension above is a different activity: it adds comparison structures, a constraint that forces arithmetic in Chinese, justification, a summary turn, and a role reversal with an opposing goal. That's the level to aim for.

#### Three or four fluent students in one class

- **Don't seat them together by default.** Mixed pairs where the fluent student has the harder role (interviewer, stallholder, reporter-back) gives them work and gives their partner a model.
- **When they do work together**, give them the version with no English at all — task instructions in Chinese too.
- **Have a standing extension** for anyone who lands early: they write the exit ticket answer as a short paragraph rather than a sentence, or they prepare one question in Chinese to ask the class in the plenary.

#### Students who need support

Support stays in the lesson — it just isn't a labelled box. Build it into how the activity is set up: keep pinyin on the board during the first round and take it down for the second, hand the word bank to the pairs who need it rather than putting it on every slide, and pair deliberately. Mention it in the activity description only where it changes what the teacher does.

### Keeping Everyone Responding — Menu

Teacher-delivery techniques for keeping every student active, not plan furniture. Use them; **don't write them into the plan or onto the slides as labelled boxes.**

| Strategy | What it looks like in a Chinese lesson |
|---|---|
| **Choral response** | "Repeat after me: 现在七点半。" (whole class repeats) |
| **Mini whiteboards** | "Write 'half past three' in Chinese. Hold it up." |
| **Cold call** | "Alex, how do you say 'I like playing basketball' in Chinese?" (ask first, then name) |
| **Turn and talk** | "Tell your partner what time you get up. 30 seconds. Go." |
| **Gesture response** | "I'll say a time — if it's AM, thumbs up. If PM, thumbs down." |
| **Sentence frames** | "Complete this sentence with your own info: 我每天____点____。" |
| **TPR** (Total Physical Response) | "站起来。坐下。往前走。往后退。" (students do the action) |
| **Chain response** | Each student adds one element: "我七点起床 → 我七点半吃早饭 → 我八点上学 → ..." |

### CFU — Menu

Embed CFU throughout the lesson, not just at the end. Pick from this menu.

| Strategy | What it checks | Example |
|---|---|---|
| **Thumbs up/down** | Comprehension | "Thumbs up if 起床 means 'get up'." |
| **Quick translate** | Vocabulary | "How do you say 'sometimes' in Chinese?" |
| **Make a sentence** | Grammar application | "Give me a sentence with 除了…以外. Write on whiteboards." |
| **Error correction** | Language sensitivity | "我每天坐飞机上学 — what's wrong with this?" |
| **Listen and write** | Listening + writing | "Write the time you hear." (teacher says a time in Chinese) |
| **Pinyin ↔ Hanzi** | Bidirectional conversion | "Write the characters for shàng xué." |
| **Exit ticket** | End-of-lesson check | "Write one sentence using today's key structure." |
| **Self-assessment vs Success Criteria** | Metacognition | Point to each criterion: "👍 I can do this / 😐 I'm getting there / 👎 I need more practice" |

### Games — Menu

Pick 1 game per lesson based on the skill focus and energy level. Ask the teacher: "For today's game, do you want something high-energy or calmer?"

| Game | Skill | Time | Energy | Best when... |
|---|---|---|---|---|
| **Slap the Character** | Vocab recognition | 3–5 min | 🔥 High | Introducing new characters |
| **Bingo** | Vocab recall | 5–8 min | 😌 Low | End of lesson or Friday afternoon |
| **Telephone (传声筒)** | Pronunciation | 5 min | 🔥 High | Practicing tones, any year level |
| **Sentence Jumble** | Word order | 5 min | 😌 Low | After introducing a new sentence pattern |
| **Correct the Teacher** | Grammar, translation | 3 min | 😌 Low | Quick CFU, any point in the lesson |
| **Find Someone Who** | Speaking, whole-class | 8–10 min | 🔥 High | Getting students moving, using question forms |
| **Two Truths, One Lie** | Free speaking | 5–8 min | 🔥 Med | Mid-unit, students have enough vocab |
| **20 Questions** | Question forms | 5–10 min | 😌 Med | Plenary or filler |
| **Role-play Cards** | Communicative function | 8–10 min | 🔥 Med | Shopping, ordering food, asking directions |
| **Running Dictation** | Reading + writing | 5 min | 🔥 High | Waking up a sleepy class |
| **Kahoot / Quizlet Live** | Comprehensive review | 8–10 min | 🔥 High | Unit revision, all students have devices |
| **Writing Relay** | Character writing | 5 min | 🔥 High | Character-focused lesson |
| **Simon Says (老师说)** | Listening, verbs | 3–5 min | 🔥 Med | Y7, body parts or action verbs |
| **Odd One Out** | Categorization, reasoning | 3–5 min | 😌 Low | Plenary, mid-unit review |

---

## Phase 5: Plenary (43–50 min)

### Components

1. **Revisit the Learning Intention and Success Criteria** (2 min)
   - Read them aloud or have a student read them
   - Ask: "Did we achieve this today?"

2. **Self-assessment** (2–3 min)
   - Students rate themselves against each success criterion: 👍 / 😐 / 👎
   - Quick show of hands or whiteboards for each one
   - This is not for grading — it's metacognition and teacher feedback

3. **Exit ticket** (2–3 min)
   - One question on a slip of paper or mini whiteboard, collected on the way out
   - Must be quick: one sentence, one translation, or one correction
   - Tied directly to today's learning intention
   - Examples:
     - "Write one sentence about your daily routine using 才 or 就."
     - "Translate: 'I go to school by subway.'"
     - "True or false: this sentence is correct — 我对数学很好。"

4. **Preview** (30 sec)
   - "Next lesson we'll..." — one sentence teaser

---

## Language of Instruction

- **Y7**: Use more English for explanations and instructions. Keep pinyin visible for all new vocabulary. Push for Chinese in dialogues and set phrases (问候, 上课指令). Accept English answers for comprehension checks; ask for Chinese re-statements from fluent speakers.
- **Y8**: Shift to ~50% Chinese for classroom management. Hide pinyin during practice phase (keep it visible during I Do). Expect Chinese answers for simple questions. English OK for complex explanations.
- **Y9**: Aim for ~70% Chinese. Pinyin only for brand-new vocabulary. Expect Chinese for all target-language responses. English reserved for grammar explanations and emotional/behavioural conversations.

---

## No Homework

This program does not assign homework. All practice happens in class. The practice phase must be sufficient for students to consolidate the new language. If time is tight, prioritize speaking and listening over writing — writing can be the focus of the next lesson.

---

## Output Format

Write the lesson plan to `docs/lesson-plans/y<year>-l<lesson-number>/<NN>-<slug>-<direction>.md`. Create the directory if needed.

Produce a **Markdown lesson plan** using this exact template:

```markdown
# [Lesson Title]

**Year Level:** Year [7/8/9]
**Unit:** [Unit number and name]
**Lesson:** [Textbook lesson number and name] | Lesson [N] of 6
**Duration:** 50 minutes

## Learning Intention
[Single WALT statement]

## Success Criteria
- I can [target] (中文说明)
- I can [target] (中文说明)
- I can [target] (中文说明)

## Materials Needed
- [List everything: mini whiteboards, projector, printed cards, etc.]

---

## Lesson Sequence

### Review (0–8 min)
**What:** [What we're reviewing — specific vocab/structures from last lesson]
**How:** [Activity description]
**Connection:** [One sentence linking to today's learning]

### Learning Intention & Success Criteria (8–10 min)
[Display method — board/projector — and how you'll introduce them]

### I Do (10–20 min)
#### New Vocabulary — [N] words in [N/2] cycles
| Cycle | 汉字 | 拼音 | English | Visual |
|---|---|---|---|---|
| 1 | ... | ... | ... | [what to draw, or — for abstract words] |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

**Cycle 1 — example sentences:**
1. [Sentence using word 1, new word bolded] — [English]
2. [Sentence using word 2] — [English]
3. [Sentence using both] — [English]

**Cycle 1 — write your own:** [frame with blank]
**Extension —** [harder prompt]

*(Repeat for each cycle. Recall slide after cycle 3.)*

#### Vocabulary Consolidation Task ([X] min)
**Summary board:** all [N] words, characters + pictures, stays on screen throughout.
**Task:** [The task — sorting / shopping list / described picture / connected paragraph / interview / matching race. State it so that every word is needed.]
**Share:** [How 2–3 students report back]
**Extension —** [All words *plus* joined clauses, justification, or no reference to the board]

#### Key Sentence Pattern
[Target structure with 3–4 modelled examples, the last one the hardest]

#### CFU Checkpoints
- [Specific CFU questions embedded in the I Do phase]

#### Text / Dialogue (if applicable)
[The passage with pinyin for Y7/Y8, character-only for Y9]
[2–3 comprehension questions]

### Flexible Practice (20–43 min)
#### Activity 1: [Name] — We Do ([X] min)
[Description, including the target language students produce]

**Extension —** [A genuinely different, harder task. Give the actual Chinese, not a description of it. Raise at least two dimensions: length, clauses, support removed, spontaneity, register, reaching back to earlier vocabulary, or role reversal.]

#### Activity 2: [Name] — You Do ([X] min)
[Description]

**Extension —** [...]

#### Game: [Name] ([X] min)
[How to play, what language it practices]
- **Setup needed:** [Cards printed? Projector? Nothing?]
- **Harder version:** [How the game changes for fluent speakers — a rule that forces longer output, removes the word bank, or makes them the question-asker]

### Plenary (43–50 min)
- **Revisit Success Criteria:** [How — choral read, student volunteer]
- **Self-assessment:** [Method — thumbs, whiteboards, traffic light]
- **Exit ticket:** [The one question students answer]
- **Preview:** [One line about next lesson]
```

---

## After the Plan

Once the Markdown plan is written, ask the teacher:

> "The lesson plan is ready. Would you like me to:
> 1. **Generate slides** — I'll use `huashu-design` to turn this into HTML slides (with Chinese characters, pinyin, visuals).
> 2. **Stop here** — You'll take the plan and build your own slides/resources.
> Which would you prefer?"

If they choose option 1, hand off to the `huashu-design` skill with the lesson plan content. Decks follow the repo convention in `CLAUDE.md`: one design per textbook lesson at `index/designs/y<year>-l<lesson>/`, with `index.html` as the overview, one file per class under `slides/`, a 1440×900 `thumb.png`, and an entry in `index/designs.json`.

**Pass the next three sections to `huashu-design` along with the plan** — the classroom typography floor, the two-words-per-slide rule, and what belongs on an activity slide. They are classroom constraints, not general design preferences, so the design skill will not apply them on its own.

---

## Slide Typography — Classroom Floor

These slides are projected to a room, not read on a laptop. Earlier decks set pinyin at 17px and supporting text at 15px on a 1920×1080 canvas — unreadable past the third row. **Pass these minimums to `huashu-design` with the lesson plan, and check the generated `tokens.css` against them before exporting.**

### The rule

**Nothing a student must read is below 26px. Nothing at all is below 18px.** Canvas is 1920×1080, so these are canvas pixels — on a 960pt PPTX export they halve.

| Role | Minimum | Ideal |
|---|---|---|
| Hero hanzi (single character on display) | 160px | 200–240px |
| Hanzi being taught (vocab card, sentence frame, error pair) | 48px | 52–64px |
| Hanzi in a table cell | 40px | 44px |
| **Pinyin** | **28px** | 30–34px |
| English gloss | 26px | 28px |
| Section heading | 40px | 44–56px |
| Body text | 30px | 32–40px |
| Supporting text (extension callout, note sub-lines) | 24px | 26px |
| Captions, badges, labels | 20px | 22px |
| Slide chrome (header tag, footer) | 18px | 20px |

**Pinyin gets its own line in that table for a reason.** Tone marks are 2–3px features at small sizes — the first thing to disappear on a projector, and the whole point of showing pinyin. Pinyin is never smaller than the English gloss beside it.

### When it doesn't fit

**Split the slide. Do not shrink the type.** If a vocabulary set won't fit at 48px hanzi, it's two slides — eight words per slide, not fourteen at 30px. Reclaiming space in this order:

1. Fewer items per slide (split it)
2. Tighter `.slide-content` padding — `48px 96px` instead of `60px 120px`
3. Drop decorative chrome — badges, dashed borders, icon glyphs
4. Only then, shorter English glosses

### Token deltas from the current decks

The generated `tokens.css` files (e.g. `index/designs/y9-l10/shared/tokens.css`) need these raised:

```
.body-lg                      28 → 36
.body-md                      22 → 30
.caption                      16 → 22
.heading-sm                   36 → 44
.badge                        14 → 20

.vc-hanzi                     36 → 52
.vc-hanzi.long                26 → 38
.vc-pinyin                    17 → 28
.vc-english                   17 → 26

.table-compact th             18 → 24
.table-compact td             26 → 32
.table-compact .hanzi-cell    30 → 44
.table-compact .pinyin-cell   22 → 28
.table-compact .english-cell  22 → 28

.sc-text                      24 → 32
.sc-text .en                  18 → 26
.sc-num                       36 → 44

.note/warn/tip/info  text     22 → 30
.note/warn/tip/info  sub      16 → 24
.note/warn/tip/info  icon     28 → 36

.formula-box                  32 → 44
.formula-box .op              24 → 32
.sentence-frame               32 → 44
.error-wrong / .error-correct 30 → 44
.error-arrow                  24 → 32

.slide-header .lesson-tag     14 → 20
.slide-header .section-name   15 → 22
.slide-footer                 12 → 18
```

`.hanzi-hero` (200px) and `.display-*` (120/80/56px) are already fine.

**Delete `.sed-strip` / `.sed-item` entirely.** That's the three-up Scaffold / Extension / OTR strip at the foot of activity slides. Scaffold and OTR boxes are gone (see **Extension (Required in Every Activity)**), and 15px supporting text was the worst offender on the whole slide. If an extension belongs on screen, it goes in a normal callout at 24px+ — not a three-column strip of fine print.

### What goes on an activity slide

- The task, in language students can read from the back
- The target Chinese they're producing, at taught-hanzi size
- The extension, if it's one the whole class should see — otherwise the teacher gives it to the students who need it

Not on the slide: scaffold notes, OTR labels, teacher-facing annotations of any kind. Those belong in the lesson plan, and mostly not even there.

### Verify before exporting

Screenshot one dense slide — a vocabulary table or an activity page — and view it at 25%. That's roughly the back row. If you can't read the pinyin, the deck isn't finished.

### No per-slide overrides below the floor

Slides may add their own `<style>` block, but it must never push a size under the table above. `.vc-hanzi.long { font-size: 20px }` is not a styling decision — it's a symptom of too many words on one slide. Fix the slide, not the font size.

---

## Vocabulary Slides — Two New Words per Slide

**A slide that introduces new vocabulary carries at most two new words.** Two. Not three because they're related, not a six-cell grid, not a fifteen-card table.

This is the rule the existing decks break hardest. `index/designs/y9-l10/l1-market-vocab/slides/04-vocab.html` introduces **fifteen** words on one slide — five across, three deep — and to make them fit it overrides hanzi down to 20px and leaves pinyin at 17px. That isn't a teaching slide; it's a reference sheet that nobody past the front row can read.

### Slide count follows the vocabulary, not the reverse

Each pair of words is a **three-slide cycle** (below): the words, example sentences, then write-your-own. Six new words is three cycles — nine slides, plus a recall slide. Add as many as the lesson needs and don't apologise for the count; a deck is not improved by being short. If that feels like too much of the lesson, move words to the next lesson in the sequence. Never compress the cycle to fit more words in.

### Anatomy of a two-word slide

Two words, side by side, each with:

| Element | Size | Notes |
|---|---|---|
| 汉字 | 52px+ | Traditional form in brackets where the book shows one — 新鲜（鮮） |
| Pinyin | 28px+ | Directly above or below the characters, with tone marks |
| English | 26px+ | One gloss, not three synonyms |
| Visual | — | If the word is picturable (see below) |

Nothing else on the slide. No radical notes, no example sentence, no "words for reference" box. Those get their own slide.

**Example — one slide:** 苹果 píngguǒ apple · 香蕉 xiāngjiāo banana, each with a drawing. Next slide: the following two.

### Visuals

**Use one whenever the word names something you can show.** Your five focus units are unusually concrete — colours, clothing, parts of the body, vegetables and fruits, house, furniture, market items, snacks — so most of their vocabulary qualifies. A picture beside 西红柿 does work the English gloss can't: it gets the meaning across without routing through English at all.

**Skip it for abstract and function words.** 比, 各, 应该, 除了…以外, 新鲜 as a quality. A forced picture for an abstract word is decoration, and decoration on a teaching slide is noise. Leave the space empty rather than filling it.

**How to make them — in order of preference:**

1. **Inline SVG line drawings.** A simple, flat drawing — an apple is a circle, a stem and a leaf. Vector, so it exports to PDF and PPTX cleanly, needs no network, and has no licensing question. This is the default.
2. **Real photographs** for things a line drawing would misrepresent (a specific market vegetable, a Chinese dish, a style of housing). `huashu-design/scripts/fetch_images.py` pulls public-domain and CC images from Wikimedia Commons and prints the licence and attribution for each.

**🔴 Never use emoji as the visual.** 🍎🍌 look right in the browser and render as **empty boxes** in the PPTX and PDF export — Chromium ships no colour emoji font, and the export path goes through Chromium. Some existing decks have this bug already. Use SVG.

**Reference images with `<img>`, never `background-image` on a div** — the PPTX exporter can't carry a CSS background.

### Where the 2-word rule does *not* apply

It governs **introducing** vocabulary, not recalling it. The end-of-block summary board, a matching game board, a lesson-opening "everything from last time" grid — these may show the whole set at once, because those words are already known and the slide is being scanned, not taught from. They still obey the typography floor.

### The three-slide cycle

**Every pair of new words gets three slides, in this order.** Knowing a word means being able to use it, so presentation and use stay together — students meet the words, see them working in a sentence, then produce one themselves before any new words arrive.

```
A · Two new words      B · See them used      C · Write your own
   汉字 / pinyin          2–3 example             sentence frame
   English / picture      sentences               + 60–90 sec writing
```

#### Slide A — the two words

As specified above. Teacher models each twice, class repeats twice.

#### Slide B — See them used (例句)

Two or three sentences, each using one of the new words, with the new word in the accent colour so the eye lands on it.

**🔴 The only new language in these sentences is the two new words.** Everything else must be vocabulary and patterns the class has already been taught. If an example sentence needs a third unfamiliar word to work, it is teaching four words while claiming to teach two — rewrite it. Prefer sentences lifted straight from the textbook's Text 1 / Text 2; they are guaranteed in-level.

- Chinese at 44px+, pinyin above for Y7 and Y8, English below at 26px+
- Make the last sentence use **both** new words together
- Read each aloud, class repeats, then ask one comprehension question in Chinese

#### Slide C — Write your own (写一句)

A frame with a blank that every student can fill, and a clear instruction.

- Students write on mini whiteboards or in exercise books — 60–90 seconds
- Teacher circulates, then takes 2–3 answers aloud
- **Extension on the same slide:** one harder prompt for anyone who finishes — two clauses, both new words in one sentence, or a comparison. This is the cheapest extension in the lesson; never skip it

#### Worked example — 苹果 / 香蕉

> **Slide A** — 苹果 píngguǒ *apple* · 香蕉 xiāngjiāo *banana*, each with a drawing.
>
> **Slide B · 例句**
> 1. 我喜欢吃**苹果**。 *Wǒ xǐhuan chī píngguǒ.* — I like eating apples.
> 2. **香蕉**很便宜。 *Xiāngjiāo hěn piányi.* — Bananas are cheap.
> 3. 我不喜欢**香蕉**，我喜欢**苹果**。 — both words, one sentence.
>
> **Slide C · 写一句**
> 我喜欢吃 ________ 。 · ________ 很好吃。
> *Write one sentence. 60 seconds.*
> **Extension —** 用「比」写一句：苹果比香蕉贵。Then add why: 因为…所以…

Every word in those examples — 喜欢, 吃, 很, 便宜, 不, 比, 好吃 — is already known. Only 苹果 and 香蕉 are new.

### Rhythm and checkpoints

Cycle, cycle, cycle — then after **three cycles (six new words)**, one recall slide showing all six, characters only, no pinyin, no English. The class reads them back. That is the mid-block checkpoint: if it stalls, reteach before introducing more.

Then, once the **last** cycle is done, the vocabulary block always closes with two more slides.

### Closing the block — summary slide, then a task

Introducing words two at a time works, but it leaves the set fragmented — students have six or eight words that each live in their own little pair. The block doesn't end until they've handled all of them at once.

#### Summary slide (词汇总览)

Every new word from this lesson on one board: **characters and pictures, no pinyin, no English.**

This is the deliberate exception to the two-words-per-slide rule — these words have just been taught, so the slide is being *scanned*, not taught from. Leave it up on screen for the whole task below; it is the students' reference while they work.

#### Task slide — use all of them

One task, 4–6 minutes, that **requires every word from the lesson**.

> **The test:** could a student finish this having used only two of the words? If yes, it's the wrong task — tighten the instruction until all of them are needed.

Pick by what the lesson's vocabulary actually is:

| Task | What students do | Fits |
|---|---|---|
| **Sort into categories** | Put every word under a heading and justify two of the placements aloud | 蔬菜 vs 水果, 上衣 vs 裤子, rooms vs furniture |
| **Build an artefact** | Write a shopping list, a menu, a room plan, an outfit — using every word | market, meals, house, furniture, clothing |
| **Describe one picture** | A single scene containing every item; one sentence per item | any concrete set |
| **Connected paragraph** | 4–6 sentences that between them use all the words, joined so it reads as one text | any set, best for Y9 |
| **Partner interview** | Ask a question built on each word, note the answers, report two back to the class | any set |
| **Matching race** | Picture ↔ 汉字 ↔ pinyin against the clock, all words in play | any set, high energy |

Run it as: instruction on screen, 3–4 minutes working (pairs or solo), then 2–3 students share while the summary slide is still up.

**Extension —** on the same slide, as always: every word used *and* two clauses joined, or the artefact justified (为什么买这个？), or the paragraph written without looking at the summary board.

#### Where this sits in the lesson

Realistically this task runs **at the start of Flexible Practice, as the first We Do activity** — three cycles plus the sentence pattern already fill the I Do phase. Plan it as Activity 1 rather than trying to squeeze it into the 10-minute I Do block, and say so in the lesson plan so the timings stay honest.

### What this means for how much vocabulary a lesson can carry

Three slides per pair, roughly two minutes a cycle. Six new words is about eight minutes, which fits the I Do phase alongside modelling the sentence pattern. **So a lesson introduces about 4–6 new words — not thirteen.**

That is a real constraint, and it is the right one. When a textbook lesson has fifteen new words, they get distributed across the six-lesson sequence — three or four lessons carrying new vocabulary and the rest building on it. Say so explicitly in the Step A sequence table so the teacher can see where each word lands. Do not compress the cycle to fit more words into one lesson.

---

## Reference Files

| File | What it is |
|---|---|
| `references/book-index.md` | All 45 lessons across the three books, with textbook and workbook page ranges (printed **and** PDF) for every lesson and Revision/Test block. Start here. |
| `references/extracting-from-pdfs.md` | How to render and read the scanned PDFs, and the template for a new cached unit reference. |
| `references/y7-unit4.md` | Book 1, Unit 4 (L10–12): Time, Daily Routine, Means of Transport — taught; Review source for Y7 U5 |
| `references/y8-unit3.md` | Book 2, Unit 3 (L7–9): Hobbies — Music, Sports, Dance — taught; Review source for Y8 U4 |
| `references/y9-unit3.md` | Book 3, Unit 3 (L7–9): Subjects of Study, School Facilities, Stationery — taught; Review source for Y9 U4 |

The five in-scope units have no cached reference yet: `y7-unit5.md`, `y8-unit4.md`, `y8-unit5.md`, `y9-unit4.md`, `y9-unit5.md`. Extract each on first use.

Read the relevant unit reference before designing any lesson. If the unit isn't cached yet, extract it first (see **Source Material**) — never plan from memory.
