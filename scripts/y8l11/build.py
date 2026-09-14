# -*- coding: utf-8 -*-
"""Slide generator for the Y8 L11 一日三餐 deck series.

Matches the y8-l10 system exactly: same tokens.css, same chrome, same
three-slide vocabulary cycle. Content comes from docs/lesson-plans/y8-l11/.
Nothing here invents Chinese — every sentence is from the lesson plans,
which in turn come from 轻松学中文 2 pp.100-109 and the workbook.
"""
import os, html

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(ROOT, "index", "designs", "y8-l11")


def page(title, tag, section, num, total, body, cls=""):
    c = (" " + cls) if cls else ""
    return f"""<!DOCTYPE html>
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
<div class="slide-content{c}">
{body}
</div>
</body></html>
"""


def img(name):
    return f'<img src="../../img/{name}.svg" alt="">'


def word_card(hz, py, en, pic=None, trad=None):
    """Slide A cell. No picture for abstract words - the space stays empty."""
    long = " long" if len(hz) >= 4 else ""
    if pic:
        inner = f'<div class="wc-img">{img(pic)}</div>'
        extra = ""
    else:
        inner = ""
        extra = " textonly"
    t = f'<p class="word-trad">{trad}</p>' if trad else ""
    return (f'    <div class="word-card{extra}">\n      {inner}\n'
            f'      <p class="word-pinyin">{py}</p>\n'
            f'      <p class="word-hanzi{long}">{hz}</p>\n'
            f'      <p class="word-english">{en}</p>\n{t}    </div>')


def words_slide(a, b):
    return ('  <p class="section-label">New Words · 跟我读两遍 · repeat after me, twice</p>\n'
            '  <div class="word-pair">\n' + word_card(*a) + "\n" + word_card(*b) + "\n  </div>")


def sentences_slide(rows):
    out = ['  <p class="section-label">例句 · See them used</p>', '  <div class="sentence-list">']
    for py, cn, en, both in rows:
        k = " both" if both else ""
        out.append(f'    <div class="sentence-row{k}">\n'
                   f'      <p class="sentence-py">{py}</p>\n'
                   f'      <p class="sentence-cn">{cn}</p>\n'
                   f'      <p class="sentence-en">{en}</p>\n    </div>')
    out.append("  </div>")
    return "\n".join(out)


def write_slide(frames, note, ext_text, ext_cn):
    lines = "\n".join(f'      <p class="frame-line">{f}</p>' for f in frames)
    cn = f'\n    <p class="extension-cn">{ext_cn}</p>' if ext_cn else ""
    return (f'  <p class="section-label">写一句 · Write your own</p>\n'
            f'  <div class="frame-box">\n{lines}\n'
            f'      <p class="frame-note">{note}</p>\n  </div>\n'
            f'  <div class="extension-box">\n'
            f'    <p class="extension-label">Extension · 加油题</p>\n'
            f'    <p class="extension-text">{ext_text}</p>{cn}\n  </div>')


def recall_slide(words, cols=3, label="认字 · Read them back — no pinyin, no English"):
    c = {3: "", 4: " c4", 5: " c5"}[cols]
    cells = "\n".join(
        f'    <div class="recall-cell"><p class="recall-hanzi{" long" if len(w)>=4 else ""}">{w}</p></div>'
        for w in words)
    return (f'  <p class="section-label">{label}</p>\n'
            f'  <div class="recall-grid{c}">\n{cells}\n  </div>')


def summary_slide(items, cols=3, label="词汇总览 · Everything from today"):
    c = {3: "", 4: "", 5: " c5", 6: " c6"}[cols]
    base = "summary-grid" if cols != 3 else "summary-grid"
    cells = []
    for hz, pic in items:
        long = " long" if len(hz) >= 4 else ""
        if pic:
            cells.append(f'    <div class="summary-cell"><div class="sc-img">{img(pic)}</div>'
                         f'<p class="summary-hanzi{long}">{hz}</p></div>')
        else:
            cells.append(f'    <div class="summary-cell noimg">'
                         f'<p class="summary-hanzi{long}">{hz}</p></div>')
    style = "" if cols == 3 else ""
    grid = f'  <div class="{base}{c}" style="grid-template-columns:repeat({cols},1fr)">\n'
    return (f'  <p class="section-label">{label}</p>\n{grid}' + "\n".join(cells) + "\n  </div>")


def examples_block(rows, label="模仿我说 · Watch me build it"):
    out = [f'  <p class="section-label">{label}</p>', '  <div class="example-list">']
    for i, (cn, en, hardest) in enumerate(rows, 1):
        k = " hardest" if hardest else ""
        e = f'<p class="example-en">{en}</p>' if en else ""
        out.append(f'    <div class="example-row{k}">\n'
                   f'      <p class="example-num">{i}</p>\n'
                   f'      <div><p class="example-cn">{cn}</p>{e}</div>\n    </div>')
    out.append("  </div>")
    return "\n".join(out)


def dialogue_block(rows):
    out = ['  <div class="dialogue">']
    for who, py, cn in rows:
        k = " b" if who == "B" else ""
        out.append(f'    <div class="dl-row{k}">\n      <p class="dl-who">{who}</p>\n'
                   f'      <div class="dl-body">\n        <p class="dl-py">{py}</p>\n'
                   f'        <p class="dl-cn">{cn}</p>\n      </div>\n    </div>')
    out.append("  </div>")
    return "\n".join(out)


def callout(kind, label, text, cn=None, sub=None):
    cn = f'\n    <p class="cb-cn">{cn}</p>' if cn else ""
    sub = f'\n    <p class="cb-sub">{sub}</p>' if sub else ""
    return (f'  <div class="{kind}-box">\n    <div>\n'
            f'    <p class="cb-label">{label}</p>\n'
            f'    <p class="cb-text">{text}</p>{cn}{sub}\n    </div>\n  </div>')


def task_slide(label, badge, lines, ext_text, ext_cn=None, steps=None):
    out = [f'  <p class="section-label">{label}</p>']
    if badge:
        out.append(f'  <div class="badge badge-orange"><p>{badge}</p></div>')
    out.append('  <div class="task-box stack gap-sm" style="margin-top:16px">')
    for l in lines:
        if l.startswith("cn:"):
            out.append(f'    <p class="task-cn">{l[3:]}</p>')
        elif l.startswith("py:"):
            out.append(f'    <p class="task-py">{l[3:]}</p>')
        else:
            out.append(f'    <p class="task-line">{l}</p>')
    out.append("  </div>")
    if steps:
        out.append('  <div class="stack gap-sm" style="margin-top:18px">')
        for i, s in enumerate(steps, 1):
            out.append(f'    <div class="step-row"><div class="step-num"><p>{i}</p></div>'
                       f'<p class="step-text">{s}</p></div>')
        out.append("  </div>")
    cn = f'\n    <p class="extension-cn">{ext_cn}</p>' if ext_cn else ""
    out.append('  <div class="extension-box">\n'
               '    <p class="extension-label">Extension · 加油题</p>\n'
               f'    <p class="extension-text">{ext_text}</p>{cn}\n  </div>')
    return "\n".join(out)


def sc_slide(walt, criteria, compact=False):
    rows = "\n".join(
        f'    <div class="sc-row"><p class="sc-num">{i}</p><div>'
        f'<p class="sc-main">{m}</p>' + (f'<p class="sc-cn">{c}</p>' if c else "") + '</div></div>'
        for i, (m, c) in enumerate(criteria, 1))
    k = " lisc-compact" if compact else ""
    return (f'  <div class="lisc{k}">\n'
            f'  <p class="section-label">Learning Intention · 学习目标</p>\n'
            f'  <div class="pattern-box"><p class="display-md">{walt}</p></div>\n'
            f'  <div class="lisc-2nd">\n'
            f'  <p class="section-label">Success Criteria · 我能……</p>\n'
            f'  <div class="stack gap-sm">\n{rows}\n  </div></div></div>')


def title_slide(kicker, hz, en, meta, strip):
    imgs = "".join(img(s) for s in strip)
    return ('  <div class="title-wrap">\n'
            f'    <p class="title-kicker">{kicker}</p>\n'
            f'    <h1 class="title-hanzi">{hz}</h1>\n'
            f'    <p class="title-en">{en}</p>\n'
            f'    <p class="title-meta">{meta}</p>\n'
            f'    <div class="title-strip">{imgs}</div>\n  </div>')


def write_deck(folder, slides, deck_title, deck_key, lesson_label):
    d = os.path.join(OUT, folder, "slides")
    os.makedirs(d, exist_ok=True)
    total = len(slides)
    manifest = []
    for i, (fname, title, tag, section, body, cls) in enumerate(slides, 1):
        open(os.path.join(d, fname), "w", encoding="utf-8").write(
            page(title, tag, section, i, total, body, cls))
        manifest.append((fname, title.split("· ", 1)[-1] if "· " in title else title))
    return manifest, total


RATE = ('<img src="../../img/rate-up.svg" alt="got it" style="height:40px;vertical-align:-9px"> / '
        '<img src="../../img/rate-mid.svg" alt="getting there" style="height:40px;vertical-align:-9px"> / '
        '<img src="../../img/rate-down.svg" alt="need practice" style="height:40px;vertical-align:-9px">')
"""Self-assessment icons as SVG, never emoji: Chromium ships no colour
emoji font, so 👍/😐/👎 export as empty boxes through the PPTX/PDF path.
The y8-l10 decks have that bug in every plenary slide."""
