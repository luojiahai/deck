---
name: lesson-planning
description: >
  Plan 50-minute Chinese lessons for Years 7–9, aligned to 轻松学中文 (Easy Steps to Chinese) textbooks.
  Source of truth: Y7 Book 1 Unit 4, Y8 Book 2 Unit 3, Y9 Book 3 Unit 3.
  Use this skill whenever a teacher asks you to plan a Chinese lesson, design a Chinese class activity,
  create Chinese learning materials, or brainstorm Chinese teaching ideas — for any of these year levels.
  Also trigger when the user mentions specific unit topics (time, daily routine, transport, hobbies,
  music, sports, dance, school subjects, school facilities, stationery) in a teaching context.
  If the user is clearly talking about a different subject or year level, do NOT trigger.
---

# Chinese Lesson Planning (轻松学中文)

This skill creates 50-minute Chinese lesson plans for Years 7–9, drawing content exclusively from the 轻松学中文 (Easy Steps to Chinese) textbook series. Students are English-native speakers; approximately 30% speak Chinese fluently.

## Critical Process Rules

These rules override everything else. Follow them in order.

### Rule 1: Never Prescribe Activities Without Asking

**The teacher chooses the activities. You do not.** For every lesson, present 2–3 options (different directions: speaking-heavy, writing-heavy, game-heavy, mixed) and let the teacher pick. Only write the full lesson plan AFTER they've chosen.

If the teacher asks for multiple lessons at once, ask lesson-by-lesson. Do not batch-skip this step — that's the #1 failure mode of this skill.

### Rule 2: Read the Reference, Then Verify Coverage

Before finalizing any lesson plan, read the relevant reference file. Then cross-check:

1. Is every vocabulary item covered?
2. Is every sentence pattern covered?
3. Are the **radicals** from the textbook taught? (Each unit has "Learn the radicals" sections — check the reference file's "Radicals" or "Textbook Activities" section.)
4. Are the **pinyin exercises** covered? (Y7 especially has "Circle the correct pinyin" exercises.)
5. Are all **textbook activities** represented? (The reference file lists them page-by-page: speaking practice, listening exercises, group work, games, word-building.)

If any are missing, add them before presenting to the teacher.

### Rule 3: Save to `docs/lesson-plans/`

All lesson plans go to `docs/lesson-plans/<filename>.md`. Create the directory if it doesn't exist.

---

## Before You Begin

### Step 0: Establish Context

Ask only what isn't already clear from the request:

1. **Year level** — 7, 8, or 9
2. **Which lesson within the unit** — Each unit has 3 lessons. Which specific lesson are they teaching? (e.g., "Lesson 10: Time", "Lesson 7: Hobbies — Music")
3. **Where in the lesson sequence** — Is this the first lesson in the unit? Second? Have students already seen some of the vocabulary?
4. **Available materials** — Does the classroom have a projector? Do students have 1:1 devices (for Kahoot/Quizlet)? Mini whiteboards?
5. **Recent issues** — Anything from the last lesson that needs revisiting? Any students who need extra attention?

If the teacher doesn't specify which lesson, show them what's in the unit and ask them to pick:

| Y7 Unit 4 | Y8 Unit 3 | Y9 Unit 3 |
|---|---|---|
| Lesson 10: Time 时间 | Lesson 7: Hobby (1) — Music 音乐 | Lesson 7: Subjects of Study 科目 |
| Lesson 11: Daily Routine 日常起居 | Lesson 8: Hobby (2) — Sports 运动 | Lesson 8: School Facilities 学校设施 |
| Lesson 12: Means of Transport 交通工具 | Lesson 9: Hobby (3) — Dance 跳舞 | Lesson 9: Stationery 文具 |

### The Hard Rule: Content Comes From the Textbook

**You must not invent vocabulary, grammar points, dialogues, or cultural content.** Everything comes from these sources — read the relevant reference file before designing anything:

- **Y7**: `references/y7-unit4.md` — 轻松学中文 1, Unit 4 (Lessons 10–12)
- **Y8**: `references/y8-unit3.md` — 轻松学中文 2, Unit 3 (Lessons 7–9)
- **Y9**: `references/y9-unit3.md` — 轻松学中文 3, Unit 3 (Lessons 7–9)

These references contain the actual vocabulary lists, grammar structures, text passages, and workbook exercise types from each unit. The companion tests (`references/*-tests.md`) show what students are assessed on.

If the reference doesn't contain something the teacher wants, tell them — don't make it up.

---

## Multi-Lesson Planning

When the teacher asks for multiple lessons for a single textbook lesson (e.g., "8 lessons for Lesson 10: Time"), follow this process:

### Step A: Scope the Sequence

First, read the reference file. Present a table showing how the textbook content maps to lessons:

```
| Lesson | Focus | Textbook Content Covered |
|---|---|---|
| 1 | O'clock (点) | p82 vocab: 点, numbers review |
| 2 | Minutes (分) | p82-83: 分, 零, X点Y分, speaking practice |
| ... | ... | ... |
```

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

Only after ALL activity preferences are confirmed, write each lesson as a **separate file**:

```
docs/lesson-plans/
├── y7-l10-01-oclock.md
├── y7-l10-02-minutes.md
├── y7-l10-03-half-past.md
├── ...
```

**One lesson per file.** Use a consistent naming pattern: `<year>-l<lesson-number>-<seq>-<slug>.md`. Do not put all lessons in a single file — the teacher needs to open them individually for each class.

### Step D: Verify Coverage

After writing, check each lesson against the reference file's "Textbook Activities" section. Confirm every textbook page element (vocabulary, patterns, radicals, pinyin exercises, activities) appears somewhere in the sequence. If anything is missing, add it and tell the teacher what was added.

---

## Lesson Structure (50 Minutes)

Every lesson follows this exact structure. Times are guides — the teacher can adjust.

```
 0–8 min   Review (复习) — revisit last lesson's content
 8–10 min  Learning Intention + Success Criteria — state and display
10–20 min  I Do — explicit teaching, model the new language
20–43 min  Flexible Practice — We Do → You Do, with OTR, CFU, differentiation, games
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

1. **Present the new vocabulary** (3–5 min)
   - Show each word: Chinese character → pinyin → English meaning
   - Model pronunciation twice, class repeats twice (choral response)
   - Point out radical clues where helpful (e.g., "Notice 泳 has 氵(water) — swimming!")
   - For Y7: keep pinyin visible. For Y8/Y9: gradually hide pinyin during practice

2. **Model the key sentence pattern** (3–5 min)
   - Present the target structure clearly
   - Do a think-aloud: "To say 'I go to school by bus', I need... 我 + 坐 + 公共汽车 + 上学"
   - Model 2–3 examples, each slightly different
   - Insert one "silly" example to grab attention (e.g., "我每天坐飞机上学" — wait for reactions)

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

This is a single 23-minute block. Move gradually from **We Do** (guided, scaffolded) to **You Do** (independent, with differentiation). Throughout, embed OTR (Opportunities to Respond) and CFU (Check for Understanding).

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
- **Scaffolded/step-by-step**: slow build, concept-first, layers of support

If the teacher has told you their classroom setup (projector but no whiteboards, etc.), incorporate that into every option — don't suggest activities that require unavailable materials.

After the teacher picks, fill the 23-minute block with a sequence of 2–4 activities that:
- Start guided (We Do), end independent (You Do)
- Include at least 2 OTR moments where every student responds
- Include at least 1 game
- Have built-in differentiation
- Cover the relevant textbook activities from the reference file

### Differentiation (Required in Every Lesson)

Every lesson plan must include:

| Level | Strategy |
|---|---|
| **Extension** (for fluent speakers) | More complex sentence structures, less scaffolding, push for paragraph-level output, remove pinyin earlier, ask "why" follow-ups |
| **Scaffolding** (for learners who need support) | Keep pinyin visible longer, provide sentence frames with blanks, allow English for comprehension checks, pair with stronger student for speaking |

Write differentiation into the activity descriptions — don't put it in a separate table at the end. Show how each activity has a scaffolded version and an extension version.

Example:
> "**Dialogue practice (all students)**: A: 你怎么上学? B: 我坐____上学。
> - **Scaffold**: Give students a word bank (公共汽车, 地铁, 校车, 走路) with pinyin.
> - **Extension**: Students must add how long it takes and what time they leave: 我每天七点半坐公共汽车上学，要半个小时。"

### OTR Strategies — Menu

Pick from this menu based on the activity and classroom setup. Every practice phase should include at least 2 OTR moments.

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

Write the lesson plan to `docs/lesson-plans/<filename>.md`. Create the directory if needed.

Produce a **Markdown lesson plan** using this exact template:

```markdown
# [Lesson Title]

**Year Level:** Year [7/8/9]
**Unit:** [Unit number and name]
**Lesson:** [Lesson number and name]
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
#### New Vocabulary
| 汉字 | 拼音 | English |
|---|---|---|
| ... | ... | ... |

#### Key Sentence Pattern
[Target structure with 2–3 modelled examples]

#### CFU Checkpoints
- [Specific CFU questions embedded in the I Do phase]

#### Text / Dialogue (if applicable)
[The passage with pinyin for Y7/Y8, character-only for Y9]
[2–3 comprehension questions]

### Flexible Practice (20–43 min)
#### Activity 1: [Name] — We Do ([X] min)
[Description]
- **Scaffold:** [How to support learners]
- **Extension:** [How to stretch fluent speakers]
- **OTR:** [Which OTR strategy]

#### Activity 2: [Name] — You Do ([X] min)
[Description]
- **Scaffold:** [...]
- **Extension:** [...]

#### Game: [Name] ([X] min)
[How to play, what language it practices]
- **Setup needed:** [Cards printed? Projector? Nothing?]

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

If they choose option 1, hand off to the `huashu-design` skill with the lesson plan content.

---

## Reference Files

- `references/y7-unit4.md` — Y7 vocabulary, grammar, texts, workbook exercises, and test items for Unit 4
- `references/y8-unit3.md` — Y8 vocabulary, grammar, texts, workbook exercises, and test items for Unit 3
- `references/y9-unit3.md` — Y9 vocabulary, grammar, texts, workbook exercises, and test items for Unit 3

Read the relevant reference file before designing any lesson. These are your source of truth.
