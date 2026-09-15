# -*- coding: utf-8 -*-
"""Slide generator for the Y8 L14 家具 (Furniture) deck series.

Six decks, one per classroom lesson, from docs/lesson-plans/y8-l14/.
Forked from scripts/y8l13 — same unit, same machinery, same palette: one
deck folder per lesson, a three-slide vocabulary cycle, the classroom
typography floor. Nothing here invents Chinese. Every sentence comes from
the lesson plans, which come from 轻松学中文 2 pp.132–141 and the workbook
pp.154–163.

L13 drew the house; L14 furnishes it. The grammatical spine runs
place 里有 + 量词 + object (L1–3) → A 在 B 上面/前面 (L3–4) → V-not-V
questions (L5) → 应该上几楼？ (L6).

Constraints this file enforces so they cannot drift:
  · a slide that INTRODUCES vocabulary carries at most two new words
  · every pair runs the three-slide cycle A (words) → B (例句) → C (写一句)
  · every C slide carries an extension — s_write requires it positionally
  · s_pattern takes at most three worked examples; a fourth is silently
    clipped by .slide-content's overflow, so the hardest goes on s_focus
  · a word with no picturable referent gets a textonly card, not a forced
    drawing, and never an emoji — Chromium ships no colour emoji font and
    both exports run through Chromium. 张, 把 and 里面 are the abstract
    ones here; each gets a counting or containment DIAGRAM, not a scene.
  · CFU slides carry questions only. s_cfu has no answers parameter, so an
    answer slide cannot be added to this series by accident. The teacher
    asked for none: the answers are taken live.
  · no pinyin-discrimination slides. Textbook Ex. 2 (c/ch, CD 67) and
    Ex. 10 (the group pinyin-writing game) are out of the series entirely,
    and there is no helper that could render one.
  · radicals are IN, but in exactly one place. The series was built
    without them at the teacher's instruction, and the consequence was
    stated plainly at the time: Unit 5 Test parts 3 and 4 test the radical
    of a character and the simple character inside a compound, so students
    would have met those two parts cold. The teacher then asked for a slot,
    so Lesson 6 carries three slides — s_chars for the eight simple
    characters the unit actually teaches (p.126 Ex. 7 and p.137 Ex. 11),
    then two s_radicals boards in the two test formats. They are the only
    radical slides in the series, and they are task boards, not answer
    boards: the no-answer-slide rule below still applies to them.
  · stroke-order copying of the lesson's OWN new words (s_strokes,
    Lessons 1–5) is vocabulary work rather than radical practice, and is
    the only writing practice those fifteen characters get.

Run:
    python3 scripts/y8l14/art.py     # drawings first
    python3 scripts/y8l14/build.py   # tokens.css + slides + deck shells
"""
import os, json, importlib

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(ROOT, "index", "designs", "y8-l14")

PAGE = """<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="../../shared/tokens.css">
</head>
<body>
<div class="slide-header">
  <span class="lesson-tag">{tag}</span>
  <span class="sep"></span>
  <span class="section-name">{section}</span>
  <span class="slide-num">{num} / {total}</span>
  <div class="accent-line"></div>
</div>
<div class="slide-content{cls}">
{body}
</div>
</body></html>
"""


def img(name):
    return '<img src="../../img/%s.svg" alt="">' % name


def label(text):
    return '  <p class="section-label">%s</p>\n' % text


# ── Cycle A · the two new words ────────────────────────────────────
def word_card(hz, py, en, pic=None):
    long = " long" if len(hz) >= 4 else ""
    if pic:
        inner = '      <div class="wc-img">%s</div>\n' % img(pic)
        extra = ""
    else:
        inner = ""
        extra = " textonly"
    return ('    <div class="word-card%s">\n%s'
            '      <p class="word-pinyin">%s</p>\n'
            '      <p class="word-hanzi%s">%s</p>\n'
            '      <p class="word-english">%s</p>\n'
            '    </div>' % (extra, inner, py, long, hz, en))


def s_words(a, b=None):
    """Two new words, never three. b may be omitted for a lone-word cycle —
    Lesson 5's 车库 and nothing else in this series."""
    cards = word_card(*a) if b is None else word_card(*a) + "\n" + word_card(*b)
    cols = ' style="grid-template-columns:1fr;max-width:330pt;margin:8pt auto 0;"' if b is None else ""
    return (label("New Words · 跟我读两遍 · repeat after me, twice")
            + '  <div class="word-pair"%s>\n' % cols + cards + "\n  </div>")


# ── Cycle B · example sentences ────────────────────────────────────
def s_examples(rows, question=None):
    out = [label("例句 · See them used").rstrip("\n"), '  <div class="sentence-list">']
    for r in rows:
        cn, en = r[0], r[1]
        both = " both" if (len(r) > 2 and r[2]) else ""
        out.append('    <div class="sentence-row%s">\n'
                   '      <p class="sentence-cn">%s</p>\n'
                   '      <p class="sentence-en">%s</p>\n    </div>' % (both, cn, en))
    out.append("  </div>")
    if question:
        out.append('  <p class="support" style="margin-top:10pt;">问：%s</p>' % question)
    return "\n".join(out)


# ── Cycle C · write your own ───────────────────────────────────────
def s_write(frames, ext, minutes="60–90 秒"):
    """ext is positional: a C slide without an extension cannot be built."""
    lines = "\n".join('    <p class="frame-line">%s</p>' % f for f in frames)
    return (label("写一句 · Write one sentence · %s" % minutes)
            + '  <div class="frame-box">\n%s\n  </div>\n' % lines
            + '  <div class="extension-box">\n'
              '    <p class="extension-label">Extension</p>\n'
              '    <p class="extension-text">%s</p>\n  </div>' % ext)


# ── Checkpoints and boards ─────────────────────────────────────────
def s_recall(words, note, cols=3, head="认一认 · characters only · 一起读出来"):
    # Four rows of cells at full padding runs off the bottom. The whole-lesson
    # board (nineteen words) is the case that needs the tighter cell; 26pt is
    # 52px on the projector, comfortably above the floor.
    rows_n = -(-len(words) // cols)
    packed = rows_n > 3
    fs = ' style="font-size:%dpt;"' % (26 if packed else 30) if cols >= 5 else ""
    pad = ' style="padding:13pt 8pt;"' if packed else ""
    cells = "\n".join('    <div class="recall-cell"%s><p class="recall-hanzi"%s>%s</p></div>'
                      % (pad, fs, w) for w in words)
    grid = ' style="grid-template-columns:repeat(%d,1fr);"' % cols if cols != 3 else ""
    return (label(head)
            + '  <div class="recall-grid"%s>\n%s\n  </div>\n' % (grid, cells)
            + '  <p class="support" style="margin-top:12pt;">%s</p>' % note)


def s_summary(items, note, dense=False):
    """items: (hanzi, picture-or-None). 张 and 把 pass None on purpose. The
    counting diagrams that teach them are 200x200 drawings; in a summary
    cell they render about 40px wide, at which size the three rows of sofas
    are an illegible smudge. A picture nobody can read is decoration, and
    this board is meant to be scanned."""
    cells = []
    for hz, pic in items:
        long = " long" if len(hz) >= 4 else ""
        pic_html = ('      <div class="sc-img">%s</div>\n' % img(pic)) if pic else ""
        cells.append('    <div class="summary-cell">\n%s'
                     '      <p class="summary-hanzi%s">%s</p>\n    </div>' % (pic_html, long, hz))
    # A dense board is the end-of-lesson summary and can carry anything from
    # five words to the whole lesson's nineteen. Four rows of five overflows,
    # so the column count follows the word count rather than being fixed.
    cls = " dense" if dense else ""
    n = len(items)
    cols = ""
    if dense:
        per = 5 if n <= 10 else (6 if n <= 12 else 7)
        cols = ' style="grid-template-columns:repeat(%d,1fr);"' % per
        if n > 12:
            cls += " packed"
    return (label("词汇总览 · 这一课的生词 · stays up while you work")
            + '  <div class="summary-grid%s"%s>\n%s\n  </div>\n' % (cls, cols, "\n".join(cells))
            + '  <p class="support" style="margin-top:10pt;">%s</p>' % note)


def s_cfu(rows, head="检查理解 · Check for understanding", note=None):
    """A CFU question slide.

    There is no answers parameter and there is no answer slide anywhere in
    this series, by the teacher's instruction. Adding one means changing
    this function, which is the point.
    """
    # Five questions at full size run 63px off the bottom and the last one
    # vanishes with no warning. Past four, the slide tightens itself.
    tight = len(rows) > 4
    pad = ' style="padding:7pt 14pt;"' if tight else ""
    num = ' style="font-size:19pt;min-width:19pt;"' if tight else ""
    q_fs = ' style="font-size:18pt;"' if tight else ""
    out = [label(head).rstrip("\n"),
           '  <div class="stack" style="gap:6pt;">' if tight else '  <div class="stack gap-md">']
    for i, r in enumerate(rows, 1):
        how = ('<p class="sc-cn">%s</p>' % r[1]) if len(r) > 1 and r[1] else ""
        out.append('    <div class="sc-row"%s><p class="sc-num"%s>%d</p><div>'
                   '<p class="task-cn"%s>%s</p>%s</div></div>' % (pad, num, i, q_fs, r[0], how))
    out.append("  </div>")
    out.append('  <p class="support" style="margin-top:%dpt;">%s</p>'
               % (6 if tight else 10, note or "答案不上屏——老师现场收（白板／点名）。"))
    return "\n".join(out)


def s_errors(rows, head, note=None):
    """Correct the Teacher: wrong form struck through, right form beside it."""
    out = [label(head).rstrip("\n"), '  <div class="stack" style="gap:2pt;">']
    for wrong, right, why in rows:
        out.append('    <div class="err-row">'
                   '<div class="err-wrong"><p>%s</p></div>'
                   '<span class="err-arrow">&rsaquo;</span>'
                   '<div class="err-right"><p>%s</p></div>'
                   '<p class="support" style="margin-left:6pt;">%s</p></div>' % (wrong, right, why))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)



# ── 吗-question → V-not-V · Lesson 5's whole point ──────────────────
def s_convert(rows, head, note=None):
    """rows: (吗 form, V-not-V form). Deliberately NOT s_errors: the left
    column is correct Chinese too. Students who read a struck-through left
    box conclude 吗 questions are wrong, which is a worse error than the
    one this slide is trying to prevent."""
    tight = len(rows) > 4
    pad = ' style="padding:6pt 13pt;"' if tight else ""
    fs = ' style="font-size:19pt;"' if tight else ""
    out = [label(head).rstrip("\n"),
           '  <div class="stack" style="gap:%dpt;">' % (1 if tight else 3)]
    for a, b in rows:
        out.append('    <div class="cv-row" style="padding:%dpt 0;">'
                   '<div class="cv-from"%s><p%s>%s</p></div>'
                   '<span class="cv-arrow">&rsaquo;</span>'
                   '<div class="cv-to"%s><p%s>%s</p></div></div>'
                   % (4 if tight else 7, pad, fs, a, pad, fs, b))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:%dpt;">%s</p>'
                   % (7 if tight else 12, note))
    return "\n".join(out)

# ── 有 / 在 — the contrast this whole textbook lesson turns on ──────
def s_contrast(left, right, note=None, head="有 还是 在？ · which one?"):
    """left/right: (key, gloss, form, example). Two columns, one structure
    each, so the difference is spatial rather than said twice."""
    def col(d, alt):
        k, g, f, eg = d
        return ('    <div class="contrast-col%s">\n'
                '      <p class="contrast-key">%s</p>\n'
                '      <p class="contrast-gloss">%s</p>\n'
                '      <p class="contrast-form">%s</p>\n'
                '      <p class="contrast-eg">%s</p>\n    </div>' % (alt, k, g, f, eg))
    out = [label(head).rstrip("\n"), '  <div class="contrast">',
           col(left, ""), col(right, " alt"), "  </div>"]
    if note:
        out.append('  <p class="support" style="margin-top:12pt;">%s</p>' % note)
    return "\n".join(out)


# ── Tick grid — textbook p.130 Ex.11, the CD-65 listening table ─────
def s_tickgrid(cols, rows, head, note=None):
    out = [label(head).rstrip("\n"), '  <table class="tick-grid">',
           "    <tr><th></th>" + "".join("<th>%s</th>" % c for c in cols) + "</tr>"]
    for r in rows:
        out.append('    <tr><td class="rowhead">%s</td>%s</tr>'
                   % (r, "<td></td>" * len(cols)))
    out.append("  </table>")
    if note:
        out.append('  <p class="support" style="margin-top:12pt;">%s</p>' % note)
    return "\n".join(out)


# ── Stroke order — the lesson's own new words, not radicals ─────────
def s_strokes(rows, head, note=None):
    """rows: (hanzi, stroke count, what to watch). Copying the new words of
    the text with correct stroke order is vocabulary work. Radical
    identification is the thing this series leaves out, and it has no
    helper here at all."""
    # Lesson 1 copies six characters (沙 发 茶 几 柜 张), which is two more
    # than y8l13 ever asked for and 9px more than the canvas holds. Third
    # notch: 26pt hanzi is 52px on the projector, still far above the floor.
    tight = len(rows) > 4
    vtight = len(rows) > 5
    row_s = ' style="padding:%dpt 16pt;"' % (4 if vtight else 6) if tight else ""
    hz_s = (' style="font-size:%dpt;min-width:%dpt;"' % (26 if vtight else 32,
            38 if vtight else 44)) if tight else ""
    out = [label(head).rstrip("\n"),
           '  <div class="stack" style="gap:%dpt;">' % (3 if vtight else (5 if tight else 7))]
    for hz, n, note_i in rows:
        out.append('    <div class="stroke-row"%s>'
                   '<p class="stroke-hanzi"%s>%s</p>'
                   '<p class="stroke-count">%s 画</p>'
                   '<p class="stroke-note">%s</p>'
                   '<div class="stroke-boxes"><div></div><div></div><div></div></div>'
                   '</div>' % (row_s, hz_s, hz, n, note_i))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)



# ── Radicals and simple characters — Lesson 6 only ─────────────────
def s_chars(rows, head, note=None):
    """rows: (hanzi, pinyin, english, where it comes from). The eight
    simple characters 轻松学中文 2 teaches across Unit 5 — 光 金 匕 入 on
    p.126 and 井 亡 乌 勺 on p.137. Straight reference, no task: they are
    what makes Test part 4 answerable at all, and the decks had cut them."""
    cells = "\n".join(
        '    <div class="char-cell">'
        '<p class="char-hz">%s</p>'
        '<p class="char-py">%s</p>'
        '<p class="char-en">%s</p>'
        '<p class="char-src">%s</p></div>' % r for r in rows)
    out = [label(head).rstrip("\n"), '  <div class="char-grid">', cells, "  </div>"]
    if note:
        out.append('  <p class="support" style="margin-top:12pt;">%s</p>' % note)
    return "\n".join(out)


def s_radicals(chars, head, prompt, bank=None, note=None):
    """A Unit 5 Test part 3 / part 4 board: the characters, and a rule to
    write the answer on.

    No answers, deliberately — s_cfu's rule holds here too. `bank` is the
    set to choose from on first exposure; the test gives none, and the
    caller says so in `note` rather than letting students find out in the
    exam."""
    cells = "\n".join(
        '    <div class="rad-cell"><p class="rad-char">%s</p>'
        '<div class="rad-slot"></div></div>' % c for c in chars)
    out = [label(head).rstrip("\n"),
           '  <p class="body-lg" style="margin-bottom:4pt;">%s</p>' % prompt,
           '  <div class="rad-grid">', cells, "  </div>"]
    if bank:
        out.append('  <div class="rad-bank"><p class="lbl">从这里选 · choose from</p>'
                   '<p class="chars">%s</p></div>' % "　".join(bank))
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)

# ── One drawing, set large, with the teaching point beside it ───────
def s_figure(pic, head, lines, cn=None):
    body = "\n".join('      <p class="task-line">%s</p>' % l for l in lines)
    cn_html = ('      <p class="task-cn" style="margin-top:10pt;">%s</p>\n' % cn) if cn else ""
    return (label(head)
            + '  <div class="figure-wrap">\n'
              '    <div class="fig">%s</div>\n'
              '    <div class="fig-body">\n%s\n%s    </div>\n  </div>' % (img(pic), body, cn_html))


# ── Pattern, focus, task, list, listening, text, dialogue ───────────
def s_pattern(head, formula, rows, note=None):
    assert len(rows) <= 3, "s_pattern takes at most 3 rows, got %d — use s_focus" % len(rows)
    out = [label(head).rstrip("\n"),
           '  <div class="pattern-box"><p class="pattern-text"%s>%s</p></div>'
           % (' style="font-size:24pt;"' if len(formula) > 24 else "", formula),
           '  <div class="stack gap-md" style="margin-top:10pt;">']
    for i, (cn, en) in enumerate(rows, 1):
        out.append('    <div class="sc-row"><p class="sc-num">%d</p><div>'
                   '<p class="task-cn">%s</p>'
                   '<p class="sc-main" style="margin-top:3pt;">%s</p></div></div>' % (i, cn, en))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)


def s_focus(head, cn, en, note=None, ext=None):
    """One hard example on its own slide, set large — the last and hardest
    example of a pattern never fits under the other three."""
    out = [label(head).rstrip("\n"),
           '  <div class="frame-box">\n'
           '    <p class="frame-line" style="font-size:27pt;line-height:1.55;">%s</p>\n'
           '  </div>' % cn,
           '  <p class="body-lg" style="margin-top:12pt;">%s</p>' % en]
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    if ext:
        out.append('  <div class="extension-box">\n'
                   '    <p class="extension-label">Extension</p>\n'
                   '    <p class="extension-text">%s</p>\n  </div>' % ext)
    return "\n".join(out)


def s_task(head, lines, ext=None, cn=None):
    out = [label(head).rstrip("\n"), '  <div class="task-box">']
    for l in lines:
        out.append('    <p class="task-line">%s</p>' % l)
    if cn:
        out.append('    <p class="task-cn" style="margin-top:10pt;">%s</p>' % cn)
    out.append("  </div>")
    if ext:
        out.append('  <div class="extension-box">\n'
                   '    <p class="extension-label">Extension</p>\n'
                   '    <p class="extension-text">%s</p>\n  </div>' % ext)
    return "\n".join(out)


def s_list(head, rows, note=None, compact=False):
    # y8l13 put this second notch at eight rows. It fires at six here: the
    # activity lists in this deck carry a longer second line (a target
    # sentence rather than a two-word gloss), so a six-row list wraps and
    # runs 37px off the bottom — silently, which is the whole problem.
    # 14pt is 28px on the projector, still above the 26px floor.
    packed = compact and len(rows) > 5
    # Lesson 6's interview board is seven rows and still overflowed packed.
    # The third notch takes geometry only — padding and gap — and leaves
    # every font size alone, so nothing moves toward the 26px floor.
    vpacked = compact and len(rows) > 6
    pad = (' style="padding:%dpt 14pt;"'
           % (3 if vpacked else (5 if packed else 8))) if compact else ""
    num = ' style="font-size:%dpt;min-width:19pt;"' % (17 if packed else 19) if compact else ""
    main = ' style="font-size:14pt;"' if packed else ""
    out = [label(head).rstrip("\n"),
           '  <div class="stack" style="gap:%dpt;">'
           % (2 if vpacked else (4 if packed else 6)) if compact
           else '  <div class="stack gap-md">']
    for i, r in enumerate(rows, 1):
        cn = ('<p class="sc-cn">%s</p>' % r[1]) if len(r) > 1 and r[1] else ""
        out.append('    <div class="sc-row"%s><p class="sc-num"%s>%d</p><div>'
                   '<p class="sc-main"%s>%s</p>%s</div></div>' % (pad, num, i, main, r[0], cn))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:%s;">%s</p>'
                   % ("8pt" if compact else "10pt", note))
    return "\n".join(out)


def s_listening(head, items, note=None):
    """Multiple-choice listening items in two columns. One column of six
    sc-rows overflows the canvas and the last two vanish silently."""
    half = (len(items) + 1) // 2
    out = [label(head).rstrip("\n"),
           '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14pt;">']
    n = 0
    for col in (items[:half], items[half:]):
        out.append('    <div class="stack" style="gap:8pt;">')
        for stem, opts in col:
            n += 1
            out.append('      <div class="sc-row" style="padding:9pt 13pt;">'
                       '<p class="sc-num" style="font-size:19pt;min-width:19pt;">%d</p><div>'
                       '<p class="task-cn" style="font-size:18pt;">%s</p>'
                       '<p class="sc-main" style="font-size:14pt;margin-top:3pt;">%s</p>'
                       '</div></div>' % (n, stem, opts))
        out.append("    </div>")
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)


def s_text(head, passage, questions, note=None, size=25):
    out = [label(head).rstrip("\n"),
           '  <div class="frame-box">\n'
           '    <p class="frame-line" style="font-size:%dpt;line-height:1.55;">%s</p>\n'
           '  </div>' % (size, passage),
           '  <div class="task-box" style="margin-top:12pt;">\n'
           '    <p class="task-line"><b>用中文回答</b> · %s</p>' % questions]
    if note:
        out.append('    <p class="task-line" style="margin-top:6pt;">%s</p>' % note)
    out.append("  </div>")
    return "\n".join(out)


def s_dialogue(head, turns, note=None):
    """Two voices, A/B alternating. Tightens itself past four turns."""
    tight = len(turns) > 4
    out = [label(head).rstrip("\n"),
           '  <div class="stack" style="gap:%dpt;">' % (5 if tight else 8)]
    pad = ' style="padding:8pt 14pt;"' if tight else ""
    fs = ' style="font-size:19pt;"' if tight else ""
    for who, cn in turns:
        col = "var(--accent-terra)" if who == "A" else "var(--accent-slate)"
        out.append('    <div class="sc-row"%s><p class="sc-num" style="color:%s;font-size:20pt;'
                   'min-width:20pt;">%s</p>'
                   '<p class="task-cn"%s>%s</p></div>' % (pad, col, who, fs, cn))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)


def s_title(cn, en, meta, motif):
    return ('  <p class="section-label">%s</p>\n'
            '  <p class="display-xl" style="margin-top:10pt;">%s</p>\n'
            '  <p class="display-md text-slate" style="margin-top:6pt;">%s</p>\n'
            '  <p class="body-lg" style="margin-top:18pt;">%s</p>' % (motif, cn, en, meta))


def s_lisc(walt, criteria):
    rows = "\n".join(
        '    <div class="sc-row"><p class="sc-num">%d</p><div>'
        '<p class="sc-main">%s</p><p class="sc-cn">%s</p></div></div>' % (i, en, cn)
        for i, (en, cn) in enumerate(criteria, 1))
    return ('  <p class="section-label">Learning Intention · 学习目标</p>\n'
            '  <div class="pattern-box" style="text-align:left;">'
            '<p class="heading">We are learning to %s</p></div>\n'
            '  <p class="section-label" style="margin-top:12pt;">Success Criteria · 我能……</p>\n'
            '  <div class="stack gap-md" style="margin-top:8pt;">\n%s\n  </div>' % (walt, rows))


# ── Assembly ───────────────────────────────────────────────────────
def build_deck(slug, title, slides, pptx=True):
    d = os.path.join(OUT, slug)
    sd = os.path.join(d, "slides")
    os.makedirs(sd, exist_ok=True)
    # Clear first. Writing over the top leaves an orphan behind whenever a
    # slide is renamed or removed: the deck shell's manifest stops
    # referencing it, so it is invisible in the browser, but it still ships
    # to Vercel and still gets counted by check_slides.mjs — which is how
    # this was noticed (built 140, checked 141). The builder owns this
    # directory completely, so it should leave nothing it did not write.
    for old_file in os.listdir(sd):
        if old_file.endswith(".html"):
            os.remove(os.path.join(sd, old_file))
    total = len(slides)
    for n, s in enumerate(slides, 1):
        html = PAGE.format(title="Y8 L14 · " + s["label"], tag=s["tag"],
                           section=s["section"], num=n, total=total,
                           body=s["body"], cls=s.get("cls", ""))
        with open(os.path.join(d, "slides", s["file"]), "w", encoding="utf-8") as f:
            f.write(html)
    manifest = ",\n".join(
        '    { file: "slides/%s", label: %s }' % (s["file"], json.dumps(s["label"], ensure_ascii=False))
        for s in slides)
    # The slide count in the progress bar and the .pptx link are both
    # per-deck. Both come from here so a copied shell cannot carry the
    # previous deck's numbers.
    shell = SHELL.format(title=title, manifest=manifest, total=total, slug=slug,
                         pptx=('\n  <a href="%s.pptx" download>PPTX</a>\n  <span>·</span>' % slug) if pptx else "")
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(shell)
    return total


SHELL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<script>
  window.DECK = [
{manifest}
  ];
</script>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{height:100%;background:#191D21;font-family:-apple-system,"PingFang SC",sans-serif;overflow:hidden}}
  #stage{{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}}
  #wrap{{width:1280px;height:720px;transform-origin:center center;background:#fff;box-shadow:0 12px 70px rgba(0,0,0,.5)}}
  iframe{{width:1280px;height:720px;border:0;display:block}}
  .zone{{position:fixed;top:0;bottom:0;width:14%;cursor:pointer;z-index:20}}
  .zone.l{{left:0}}.zone.r{{right:0}}
  .bar{{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);z-index:50;
       display:flex;align-items:center;gap:14px;background:rgba(0,0,0,.62);color:#fff;
       padding:8px 18px;border-radius:999px;font-size:13px;letter-spacing:.04em;white-space:nowrap;max-width:calc(100vw - 32px);overflow-x:auto}}
  .bar b{{font-variant-numeric:tabular-nums;font-weight:600}}
  .bar span{{color:rgba(255,255,255,.62)}}
  .bar button,.bar a{{background:none;border:0;color:rgba(255,255,255,.85);font:inherit;cursor:pointer;padding:0;text-decoration:none}}
  .bar button:hover,.bar a:hover{{color:#fff}}
  .bar a.home{{color:#C0764F}}
  .bar a.home:hover{{color:#fff}}
  #grid{{position:fixed;inset:0;background:#191D21;z-index:40;overflow:auto;padding:36px;display:none;
        grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;align-content:start}}
  #grid.on{{display:grid}}
  .cell{{cursor:pointer}}
  .cell .thumb{{width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:8px;background:#fff;position:relative;
               border:2px solid transparent}}
  .cell:hover .thumb{{border-color:#3D5A73}}
  .cell .thumb iframe{{transform-origin:top left;pointer-events:none;position:absolute;top:0;left:0}}
  .cell p{{color:rgba(255,255,255,.72);font-size:12.5px;margin-top:8px;line-height:1.4}}
  .cell p b{{color:#C0764F;font-weight:600;margin-right:6px}}
</style>
</head>
<body>

<div id="stage"><div id="wrap"><iframe id="fr" src="slides/01-title.html"></iframe></div></div>
<div class="zone l" onclick="go(-1)"></div>
<div class="zone r" onclick="go(1)"></div>

<div class="bar">
  <a class="home" href="../" title="回到课程列表 · Back to the lesson list">← 课程列表</a>
  <span>·</span>
  <button onclick="toggleGrid()">All slides</button>
  <span>·</span>{pptx}
  <b><span id="n">1</span> / {total}</b>
  <span id="lbl"></span>
</div>

<div id="grid"></div>

<script>
  const D = window.DECK; let i = 0;
  const fr = document.getElementById('fr'), wrap = document.getElementById('wrap');

  function fit(){{
    const s = Math.min(innerWidth / 1280, (innerHeight - 70) / 720);
    wrap.style.transform = 'scale(' + s + ')';
  }}
  function show(k){{
    i = (k + D.length) % D.length;
    fr.src = D[i].file;
    document.getElementById('n').textContent = i + 1;
    document.getElementById('lbl').textContent = D[i].label;
    try {{ localStorage.setItem('{slug}-pos', i); }} catch (e) {{}}
  }}
  function go(d){{ show(i + d); }}
  function toggleGrid(){{ document.getElementById('grid').classList.toggle('on'); }}

  addEventListener('keydown', e => {{
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{ go(1); e.preventDefault(); }}
    if (e.key === 'ArrowLeft'  || e.key === 'PageUp')                    {{ go(-1); e.preventDefault(); }}
    if (e.key === 'Escape') document.getElementById('grid').classList.remove('on');
    if (e.key === 'g') toggleGrid();
  }});
  addEventListener('resize', fit);

  const g = document.getElementById('grid');
  D.forEach((s, k) => {{
    const c = document.createElement('div');
    c.className = 'cell';
    c.innerHTML = '<div class="thumb"><iframe src="' + s.file + '" scrolling="no"></iframe></div>' +
                  '<p><b>' + String(k + 1).padStart(2, '0') + '</b>' + s.label + '</p>';
    c.onclick = () => {{ show(k); toggleGrid(); }};
    g.appendChild(c);
    const t = c.querySelector('.thumb'), f = c.querySelector('iframe');
    requestAnimationFrame(() => {{
      const sc = t.clientWidth / 1280;
      f.style.width = '1280px'; f.style.height = '720px';
      f.style.transform = 'scale(' + sc + ')';
    }});
  }});

  let start = 0;
  try {{ start = Math.min(parseInt(localStorage.getItem('{slug}-pos') || '0', 10) || 0, D.length - 1); }} catch (e) {{}}
  fit(); show(start);
</script>
</body>
</html>
"""



# ── Series landing page ────────────────────────────────────────────
# index/designs/y8-l14/index.html — the page the gallery card links to,
# and the page thumb.png is a screenshot of. Generated like everything
# else under index/designs/y8-l14/; nothing there is hand-maintained.
INDEX = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Y8 L14 · 家具 Furniture</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@700;900&family=Noto+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  :root{{
    --bg:#F2F4F4; --bg2:#E6EAEB; --line:#D5DBDD;
    --ink:#262B30; --ink2:#4B545C; --mute:#6E7780;
    --slate:#3D5A73; --terra:#B05B3B; --brass:#8F6C12;
    --serif:'Noto Serif SC','Songti SC',serif;
    --sans:'Noto Sans','Noto Sans SC','PingFang SC',-apple-system,sans-serif;
  }}
  body{{background:var(--bg);color:var(--ink);font-family:var(--sans);
       padding:0 0 96px;line-height:1.55}}
  .topbar{{border-bottom:1px solid var(--line);padding:16px 32px;margin-bottom:56px}}
  .topbar a{{color:var(--ink2);text-decoration:none;font-size:14px}}
  .topbar a:hover{{color:var(--slate)}}
  .wrap{{max-width:1120px;margin:0 auto;padding:0 32px}}
  .kicker{{font-size:13px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--terra)}}
  h1{{font-family:var(--serif);font-size:64px;font-weight:900;line-height:1.08;margin:14px 0 6px}}
  .sub{{font-family:var(--serif);font-size:27px;font-weight:700;color:var(--slate)}}
  .meta{{font-size:15px;color:var(--ink2);margin-top:20px;max-width:680px}}
  .rule{{height:4px;background:var(--slate);width:96px;margin:34px 0 44px;border-radius:2px}}
  .focus{{background:var(--bg2);border:2px solid var(--line);border-radius:18px;
         padding:26px 30px 30px;margin-bottom:34px}}
  .focus h2{{font-family:var(--serif);font-size:23px;font-weight:900;margin-bottom:18px}}
  .fgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}}
  .fcell{{background:var(--bg);border:1px solid var(--line);border-radius:12px;
         padding:14px 16px;text-align:center}}
  .fcell .l{{font-size:11px;font-weight:700;letter-spacing:.12em;color:var(--terra)}}
  .fcell .p{{font-family:var(--serif);font-size:25px;font-weight:900;margin:6px 0 3px}}
  .fcell .g{{font-size:12.5px;color:var(--ink2)}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:22px}}
  a.card{{display:block;text-decoration:none;color:inherit;background:var(--bg2);
         border:2px solid var(--line);border-radius:18px;padding:26px 28px 28px;
         transition:border-color .15s, transform .15s}}
  a.card:hover{{border-color:var(--slate);transform:translateY(-3px)}}
  .n{{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--terra)}}
  .t{{font-family:var(--serif);font-size:34px;font-weight:900;margin:10px 0 2px;line-height:1.2}}
  .e{{font-size:16px;color:var(--slate);font-weight:500}}
  .d{{font-size:14px;color:var(--ink2);margin-top:14px}}
  .w{{margin-top:18px;padding-top:14px;border-top:1px solid var(--line);
     font-family:var(--serif);font-size:19px;font-weight:700;color:var(--ink)}}
  .w span{{color:var(--mute);font-weight:400;font-size:13px;font-family:var(--sans);
          display:block;margin-bottom:4px;letter-spacing:.1em;text-transform:uppercase}}
  footer{{margin-top:56px;padding-top:26px;border-top:1px solid var(--line);
         font-size:14px;color:var(--mute);max-width:780px}}
  footer b{{color:var(--ink2)}}
  footer p + p{{margin-top:12px}}
</style>
</head>
<body>
<div class="topbar"><a href="../../">← Deck Gallery · 设计画廊</a></div>
<div class="wrap">
  <p class="kicker">轻松学中文 2 · Unit 5 · Lesson 14</p>
  <h1>家具</h1>
  <p class="sub">Furniture · Year 8</p>
  <p class="meta">Six 50-minute lessons, {slides} slides. Lesson 13 drew the house; this one furnishes it. Fifteen new words spread across the sequence — two to four per lesson, each pair taught as a three-slide cycle: the words, then the words used, then the students using them. Every lesson carries a CFU board straight after the new pattern, question-only: there is no answer slide anywhere in the series. Revision happens inside every lesson rather than in a review lesson at the end.</p>
  <div class="rule"></div>
  <div class="focus">
    <h2>Grammar Focus · 本课语法点</h2>
    <div class="fgrid">
      <div class="fcell"><p class="l">L1</p><p class="p">地方 里有 + 量词</p><p class="g">客厅里有一张沙发 — and why it is 张, not 个</p></div>
      <div class="fcell"><p class="l">L2</p><p class="p">不算大 ／ 不大也不小</p><p class="g">Size without saying just 大 or 小, plus 里面有</p></div>
      <div class="fcell"><p class="l">L3</p><p class="p">有　／　在</p><p class="g">New information takes 有; a known thing in an unknown place takes 在</p></div>
      <div class="fcell"><p class="l">L4</p><p class="p">A 在 B 上面／前面</p><p class="g">Precise position, and 把 for chairs</p></div>
      <div class="fcell"><p class="l">L5</p><p class="p">有没有 · 喜不喜欢</p><p class="g">V-not-V questions — the same question, without 吗</p></div>
      <div class="fcell"><p class="l">L6</p><p class="p">应该上几楼？</p><p class="g">Built entirely from parts already known, and the whole set in use</p></div>
    </div>
  </div>
  <div class="grid">
{cards}
  </div>
  <footer>
    <p><b>Six lessons, not seven.</b> The sequence ends on content, not revision — there is no 复习 lesson. Each lesson opens with a cumulative Review phase instead, and Lesson 6's plenary looks back across all six.</p>
    <p><b>No answer slides.</b> At the teacher's request, and enforced in the builder rather than left to care: the CFU helper takes no answers parameter, so an answer slide cannot be added by copying a sibling. The two radical boards in Lesson 6 follow the same rule — they carry the characters and a rule to write on, never the answers.</p>
    <p><b>No pinyin exercises — but radicals are in, in one place.</b> Textbook Ex. 2 (c/ch) and Ex. 10 are out of the series entirely. Radicals were too, until the consequence was weighed: <b>Unit 5 Test parts 3 and 4</b> ask for the radical of a character and the simple character inside a compound, so students would have met two of the eleven test parts cold. Lesson 6 now carries a five-minute slot — the eight simple characters the unit actually teaches (p.126 Ex. 7 and p.137 Ex. 11), then the exact six characters of Test part 3 and the exact six compounds of part 4, run as that lesson's game.</p>
    <p><b>Pinyin stays.</b> Excluding the pinyin <i>exercises</i> is not the same as hiding pinyin: it sits on every new-word card and above every example sentence, then comes off the board during practice, which is the Year 8 norm.</p>
    <p>Built from <b>docs/lesson-plans/y8-l14/</b> by <b>scripts/y8l14/build.py</b>. Nothing under this folder is hand-edited.</p>
  </footer>
</div>
</body>
</html>
"""

CARD = """    <a class="card" href="{slug}/">
      <p class="n">Lesson {i} of 6</p>
      <p class="t">{cn}</p>
      <p class="e">{en}</p>
      <p class="d">{desc}</p>
      <p class="w"><span>New words · {n}</span>{words}</p>
    </a>"""


def write_index(mods, total_slides):
    cards = "\n".join(
        CARD.format(slug=m.SLUG, i=i, **m.CARD) for i, m in enumerate(mods, 1))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(INDEX.format(slides=total_slides, cards=cards))
    print("  index.html                 series landing page")

LESSONS = ["l1", "l2", "l3", "l4", "l5", "l6"]


def write_tokens():
    import style
    d = os.path.join(OUT, "shared")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "tokens.css"), "w", encoding="utf-8") as f:
        f.write(style.CSS)
    print("  shared/tokens.css")


def main():
    write_tokens()
    total, mods = 0, []
    for mod_name in LESSONS:
        mod = importlib.import_module(mod_name)
        n = build_deck(mod.SLUG, mod.TITLE, mod.slides(), pptx=True)
        print("  %-26s %2d slides" % (mod.SLUG, n))
        total += n
        mods.append(mod)
    write_index(mods, total)
    print("built %d slides across %d decks" % (total, len(LESSONS)))


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
