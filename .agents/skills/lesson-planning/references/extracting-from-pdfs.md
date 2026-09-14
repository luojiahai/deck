# Extracting a unit reference from the PDFs

The six 轻松学中文 PDFs in `.resources/` are **scanned images with no text layer**.
`pdftotext` returns nothing. To read them you render pages to PNG and look at them.

This procedure turns a unit's pages into a cached reference file. Do it once per
unit; after that, read the cached file instead.

---

## Step 1 — Check the cache first

```bash
ls .agents/skills/lesson-planning/references/
```

If `y<year>-unit<n>.md` already exists, read it and stop. Do not re-extract.

## Step 2 — Look up the pages

Open `book-index.md` and find the PDF page ranges for the unit's three lessons in
both the textbook and the workbook, plus the unit's Revision/Test block.

## Step 3 — Render the pages

Use the session scratchpad, never the repo:

```bash
OUT="$SCRATCH/y9u4"   # your scratchpad dir
mkdir -p "$OUT"
pdftoppm -png -r 110 -f 94 -l 103 ".resources/轻松学中文 3 textbook.pdf" "$OUT/tb"
```

- `-f` / `-l` are **PDF** page numbers from `book-index.md`, not printed ones.
- `-r 110` is enough to read hanzi, pinyin and exercise text. Drop to `-r 70` if you
  only need to identify a page; go to `-r 150` for dense pinyin-discrimination
  exercises or small radical tables.
- Render one lesson at a time (8–12 pages). Rendering a whole book wastes minutes.

## Step 4 — Read the pages

Read each PNG in order. For each textbook lesson capture:

1. **New Words** boxes for Text 1 and Text 2 — 汉字 (with traditional form in
   brackets where the book shows one), 拼音, English. Copy them all; do not abridge.
2. **Text 1 / Text 2** — the full passage or dialogues, plus the CD track number
   printed next to the Text label.
3. **Key sentence patterns** — the structures the texts drill.
4. **Grammar notes** — including the book's own explanation boxes.
5. **"Learn the radicals"** exercise — every radical, its meaning, its example
   character.
6. **Pinyin exercises** — listening/tone exercises and "circle the correct pinyin"
   discrimination pairs. List the actual pairs.
7. **Every numbered exercise on every page** — number, page, type (speaking,
   listening + CD track, writing, game, group work, dictionary work), and one line
   on what students actually do.

From the workbook capture:

8. **Exercise formats** that recur across the unit's three lessons (character
   copying with stroke order, radical writing, phrase building, translation both
   directions, reading comprehension, dictionary look-up, essay writing…).
9. **Per-lesson highlights** — the exercises worth pulling into class.
10. **Revision and Test** pages — what each part tests, and how many parts.

Then, from the textbook's **Listening Scripts** section (page range in
`book-index.md`), copy the scripts for this unit's CD tracks. They are the only
place the listening-exercise audio content is written down.

## Step 5 — Write the cached reference

Save to `.agents/skills/lesson-planning/references/y<year>-unit<n>.md` using the
structure of the existing `y7-unit4.md` / `y8-unit3.md` / `y9-unit3.md`:

```markdown
# Year <N> — Unit <N>: 轻松学中文 <book>, Lessons <a>–<c>

**Textbook**: …
**Unit**: … | **Lessons**: … | **Topics**: …
**Page range**: pp.X–Y (textbook page numbers)

## Lesson <n>: <Topic> — pp.X–Y
### Core Vocabulary          (New Words Text 1 / Text 2 tables)
### Key Texts                (full passages + CD track)
### Key Sentence Patterns
### Grammar Notes
### Radicals
### Pinyin Focus
### Textbook Activities      (page-by-page table: page | exercise | type | description)

## Test Coverage             (per-lesson test parts)
## Workbook Exercises        (formats, per-lesson highlights, Revision, Test)
## Audio Tracks              (track number → what it is)
## Cross-Cutting Notes       (skills progression, common student errors)
```

Cite **printed** page numbers in the reference file — that is what the teacher sees
in their copy of the book.

## Step 6 — Verify before using it

Re-render 2–3 pages you have already transcribed and check them against what you
wrote. Vocabulary tables and pinyin exercises are where transcription errors hide.

---

## Finding a page you can't locate

If a lesson does not start where `book-index.md` says (a differently-scanned copy,
for instance), sweep the header band of a page range instead of rendering full pages:

```bash
pdftoppm -png -r 50 -f 70 -l 90 "$PDF" "$OUT/p"
cd "$OUT" && for f in p-*.png; do
  magick "$f" -gravity North -crop 100%x22%+0+0 +repage -resize 380x \
    -bordercolor gray50 -border 1 -font /System/Library/Fonts/Helvetica.ttc \
    -pointsize 15 -fill red -gravity NorthWest -annotate +2+1 "${f:2:3}" "h-$f"
done
magick montage -font /System/Library/Fonts/Helvetica.ttc h-*.png \
  -tile 2x12 -geometry +2+2 -background white sheet.png
```

`sheet.png` shows 24 labelled page headers at once — the `Unit N / Lesson M` banner
is unmistakable. One image read locates any lesson.

ImageMagick 7 needs `magick`, not `convert`, and `-font` must be a real path
(`/System/Library/Fonts/Helvetica.ttc`) or annotation fails.

## Reading a printed page number

The printed number sits in a small coloured tab on the outer edge, low on the page:

```bash
magick page.png -gravity SouthWest -crop 16%x55%+0+0 +repage tab.png
```
