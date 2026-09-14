# -*- coding: utf-8 -*-
"""Slide generator for the Y8 L12 外出就餐 deck series.

Six decks, one per classroom lesson, from docs/lesson-plans/y8-l12/.
Nothing here invents Chinese: every sentence comes from the lesson plans,
which come from 轻松学中文 2 pp.110-121 and the workbook pp.128-137.

CANVAS — 960pt x 540pt, the standard for new series. The class vocabulary
and palette are y8-l11's, because L10, L11 and L12 are one textbook unit
taught over six weeks and a student should not be able to tell from the
slide furniture which lesson they are in. y8-l11 is a 1920px deck, so its
stylesheet is converted px -> pt at 1pt = 2px by px2pt() below, applied to
BOTH the stylesheet and every emitted slide. That is why the lesson content
in l1.py..l6.py is still written in px: one scale factor, one place to get
it wrong.

The classroom floor is unchanged in projected terms: 13pt = 26px.

Run:  python3 scripts/y8l12/art.py     # SVG drawings first
      python3 scripts/y8l12/build.py   # slides, deck shells, index
      bash    scripts/y8l12/export.sh  # PPTX + PDF — the shells link the .pptx
"""
import os, re, shutil, json

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(ROOT, "index", "designs", "y8-l12")
SRC_CSS = os.path.join(ROOT, "index", "designs", "y8-l11", "shared", "tokens.css")
L10_IMG = os.path.join(ROOT, "index", "designs", "y8-l10", "img")
L11_IMG = os.path.join(ROOT, "index", "designs", "y8-l11", "img")
VIEWER_SRC = os.path.join(ROOT, "index", "designs", "y9-l11", "l1-snack-nouns", "index.html")


def px2pt(text):
    """1pt = 2px on a 1920x1080 projector, so every px value halves into pt.

    Safe across the SVG drawings: their coordinates, viewBox and stroke
    widths are unitless user units and carry no 'px' to match."""
    return re.sub(r'(-?\d*\.?\d+)px', lambda m: ('%g' % (float(m.group(1)) / 2)) + 'pt', text)


# ══════════════════════════════════════════════════════════════════
#  Slide shell
# ══════════════════════════════════════════════════════════════════

def page(title, tag, section, num, total, body, cls=""):
    c = (" " + cls) if cls else ""
    return px2pt(f"""<!DOCTYPE html>
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
""")


def img(name):
    return f'<img src="../../img/{name}.svg" alt="">'


# ══════════════════════════════════════════════════════════════════
#  Components — identical class vocabulary to y8-l10 / y8-l11
# ══════════════════════════════════════════════════════════════════

def word_card(hz, py, en, pic=None, trad=None):
    """Slide A cell. No picture for abstract words — the space stays
    empty rather than being filled with decoration."""
    long = " long" if len(hz) >= 4 else ""
    inner = f'<div class="wc-img">{img(pic)}</div>' if pic else ""
    extra = "" if pic else " textonly"
    t = f'<p class="word-trad">{trad}</p>' if trad else ""
    return (f'    <div class="word-card{extra}">\n      {inner}\n'
            f'      <p class="word-pinyin">{py}</p>\n'
            f'      <p class="word-hanzi{long}">{hz}</p>\n'
            f'      <p class="word-english">{en}</p>\n{t}    </div>')


def words_slide(a, b=None):
    k = "" if b else " single"
    cells = word_card(*a) + (("\n" + word_card(*b)) if b else "")
    return ('  <p class="section-label">New Words · 跟我读两遍 · repeat after me, twice</p>\n'
            f'  <div class="word-pair{k}">\n' + cells + "\n  </div>")


def sentences_slide(rows, label="例句 · See them used"):
    out = [f'  <p class="section-label">{label}</p>', '  <div class="sentence-list">']
    for py, cn, en, both in rows:
        k = " both" if both else ""
        out.append(f'    <div class="sentence-row{k}">\n'
                   f'      <p class="sentence-py">{py}</p>\n'
                   f'      <p class="sentence-cn">{cn}</p>\n'
                   f'      <p class="sentence-en">{en}</p>\n    </div>')
    out.append("  </div>")
    return "\n".join(out)


def write_slide(frames, note, ext_text, ext_cn=None):
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


def summary_slide(items, cols=4, label="词汇总览 · Everything from today"):
    cells = []
    for hz, pic in items:
        long = " long" if len(hz) >= 4 else ""
        if pic:
            cells.append(f'    <div class="summary-cell"><div class="sc-img">{img(pic)}</div>'
                         f'<p class="summary-hanzi{long}">{hz}</p></div>')
        else:
            cells.append(f'    <div class="summary-cell noimg">'
                         f'<p class="summary-hanzi{long}">{hz}</p></div>')
    grid = f'  <div class="summary-grid" style="grid-template-columns:repeat({cols},1fr)">\n'
    return (f'  <p class="section-label">{label}</p>\n{grid}' + "\n".join(cells) + "\n  </div>")


def examples_block(rows, note=None, label="模仿我说 · Watch me build it"):
    out = [f'  <p class="section-label">{label}</p>', '  <div class="example-list">']
    for i, (cn, en, hardest) in enumerate(rows, 1):
        k = " hardest" if hardest else ""
        e = f'<p class="example-en">{en}</p>' if en else ""
        out.append(f'    <div class="example-row{k}">\n'
                   f'      <p class="example-num">{i}</p>\n'
                   f'      <div><p class="example-cn">{cn}</p>{e}</div>\n    </div>')
    out.append("  </div>")
    if note:
        out.append(f'  <p class="body-md" style="margin-top:18px">{note}</p>')
    return "\n".join(out)


def pattern_slide(text, note=None, label="句型 · The pattern"):
    n = f'\n    <p class="pattern-note">{note}</p>' if note else ""
    return (f'  <p class="section-label">{label}</p>\n'
            f'  <div class="pattern-box"><p class="pattern-text">{text}</p>{n}</div>')


def cfu_slide(rows, label="检查理解 · Check for understanding",
              badge="WHITEBOARDS · NO ANSWERS ON SCREEN"):
    """The CFU block the teacher asks straight after new vocabulary or a
    new pattern. Deliberately question-only — there is no answer slide,
    because an answer on the projector is a答案 students copy instead of
    a question they attempt."""
    cells = "\n".join(
        f'    <div class="sc-row"><p class="sc-num">{i}</p><div>'
        f'<p class="sc-main">{en}</p>' + (f'<p class="sc-cn">{cn}</p>' if cn else "") + '</div></div>'
        for i, (en, cn) in enumerate(rows, 1))
    return (f'  <p class="section-label">{label}</p>\n'
            f'  <div class="badge badge-tomato"><p>{badge}</p></div>\n'
            f'  <div class="stack gap-sm" style="margin-top:16px">\n{cells}\n  </div>')


def dialogue_block(rows, label=None):
    out = [f'  <p class="section-label">{label}</p>'] if label else []
    out.append('  <div class="dialogue">')
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
    if ext_text:
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
    k = " lisc-compact" if compact or len(criteria) >= 4 else ""
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


def money_row(items, label="认一认 · Say these in Chinese"):
    """The RMB note/coin board — textbook p.111 Ex.1. Pictures only, no
    characters: the class supplies those."""
    cells = "\n".join(
        f'    <div class="summary-cell"><div class="sc-img">{img(p)}</div>'
        f'<p class="summary-hanzi long">{hz}</p></div>' for hz, p in items)
    return (f'  <p class="section-label">{label}</p>\n'
            f'  <div class="summary-grid" style="grid-template-columns:repeat(3,1fr)">\n'
            f'{cells}\n  </div>')


# Self-assessment icons as SVG, never emoji: Chromium ships no colour
# emoji font, so the export path renders 👍/😐/👎 as empty boxes.
RATE = ('<img src="../../img/rate-up.svg" alt="got it" style="height:40px;vertical-align:-9px"> / '
        '<img src="../../img/rate-mid.svg" alt="getting there" style="height:40px;vertical-align:-9px"> / '
        '<img src="../../img/rate-down.svg" alt="need practice" style="height:40px;vertical-align:-9px">')


# ══════════════════════════════════════════════════════════════════
#  Deck writer — slides + the deck's own viewer shell
# ══════════════════════════════════════════════════════════════════

def viewer_html(title, folder, slides):
    """Reuse the y9-l11 960pt viewer so every deck in the repo pages the
    same way. Two things in that shell are per-deck and easy to miss: the
    slide count is hardcoded, and it links its OWN .pptx — both have to be
    rewritten for this deck. The .pptx is produced by scripts/y8l12/export.sh;
    run that after this builder or the link 404s."""
    src = open(VIEWER_SRC, encoding="utf-8").read()
    manifest = ",\n".join(
        f'    {{ file: "slides/{f}", label: {json.dumps(lbl, ensure_ascii=False)} }}'
        for f, lbl in slides)
    src = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", src, count=1, flags=re.S)
    src = re.sub(r"window\.DECK = \[.*?\n  \];",
                 "window.DECK = [\n" + manifest + "\n  ];", src, count=1, flags=re.S)
    src = re.sub(r"<b><span id=\"n\">1</span> / \d+</b>",
                 f'<b><span id="n">1</span> / {len(slides)}</b>', src, count=1)
    src = re.sub(r'<a href="[^"]*\.pptx" download>PPTX</a>',
                 f'<a href="{folder}.pptx" download>PPTX</a>', src, count=1)
    src = src.replace("l1-snack-nouns-pos", folder + "-pos")
    return src


def write_deck(folder, slides, deck_title):
    d = os.path.join(OUT, folder, "slides")
    os.makedirs(d, exist_ok=True)
    for old in os.listdir(d):
        os.remove(os.path.join(d, old))
    total = len(slides)
    manifest = []
    for i, (fname, title, tag, section, body, cls) in enumerate(slides, 1):
        open(os.path.join(d, fname), "w", encoding="utf-8").write(
            page(title, tag, section, i, total, body, cls))
        manifest.append((fname, title.split("· ", 1)[-1] if "· " in title else title))
    open(os.path.join(OUT, folder, "index.html"), "w", encoding="utf-8").write(
        viewer_html(deck_title, folder, manifest))
    print(f"{folder}: {total} slides")
    return total


# ══════════════════════════════════════════════════════════════════
#  Stylesheet + shared assets
# ══════════════════════════════════════════════════════════════════

HEADER = """/* ═══════════════════════════════════════════════════════════════
   Y8 L12 · 外出就餐 · Eating Out
   Six-lesson classroom deck series.

   Same system as the Y8 L10 and L11 decks next door — same palette,
   same type scale, same three-slide vocabulary cycle. All three sit
   in one textbook unit, taught over six weeks, so a student should
   not be able to tell from the slide furniture which lesson they
   are in.

   GENERATED FILE — do not edit. Written by scripts/y8l12/build.py,
   which converts y8-l11/shared/tokens.css px -> pt at 1pt = 2px.
   Edit the builder, not this.

   Canvas is 960pt × 540pt = 13.333in × 7.5in, PowerPoint's standard
   widescreen. Every number below is a point, and 1pt is 2px on the
   1920×1080 projector — so .word-hanzi 62pt reads as 124px and the
   classroom floor is unchanged: 13pt = 26px.
   ═══════════════════════════════════════════════════════════════ */
"""

# Drawn for Lessons 10 and 11 and reused here rather than redrawn.
BORROW_L10 = ["pingguo", "xigua", "juzi", "xihongshi", "caihuar", "tudou",
              "shengcai", "huanggua", "xiangjiao", "li", "shucai", "shuiguo", "qingcai"]
BORROW_L11 = ["fandian", "chaomian", "chaocai", "bisabing", "hanbaobao", "regou",
              "kele", "qishui", "baozi", "mifan", "zhou", "miantiao", "chifan",
              "kuaican", "zhongcan", "xican", "quanjiaren",
              "rate-up", "rate-mid", "rate-down"]


def write_shared():
    css = open(SRC_CSS, encoding="utf-8").read()
    # Drop the source file's own header comment; keep everything else.
    css = css[css.index("@import"):]
    css = px2pt(css)
    d = os.path.join(OUT, "shared")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "tokens.css"), "w", encoding="utf-8").write(HEADER + "\n" + css)

    img_dir = os.path.join(OUT, "img")
    os.makedirs(img_dir, exist_ok=True)
    for src, names in ((L10_IMG, BORROW_L10), (L11_IMG, BORROW_L11)):
        for n in names:
            s = os.path.join(src, n + ".svg")
            if not os.path.exists(s):
                raise SystemExit(f"missing borrowed drawing: {s}")
            shutil.copyfile(s, os.path.join(img_dir, n + ".svg"))
    print(f"shared: tokens.css + {len(BORROW_L10) + len(BORROW_L11)} borrowed drawings")


# ══════════════════════════════════════════════════════════════════
#  The series' own landing page
# ══════════════════════════════════════════════════════════════════

GRAMMAR = [
    ("L1", "块(元) · 毛(角) · 分", "Reading an amount — and what you say vs what you write"),
    ("L2", "这些苹果怎么卖？", "Two ways to ask a price, one to ask a total"),
    ("L3", "我可以……吗？", "Asking permission — 可以 before the verb"),
    ("L4", "动词 + 得 + 很/特别", "How well something is done — 做得特别好吃"),
    ("L5", "一星期……几次？", "How often, with 次 — and 一次也没有去过"),
    ("L5", "大概 + 数目 + 左右", "Roughly how much, hedged at both ends"),
    ("L6", "不算太 + 形容词", "Softening a verdict — 五百块左右，不算太贵"),
]

CARDS = [
    ("l1-money-rmb", "Lesson 1 of 6", "人民币", "Money words",
     "The six money words, a listen-and-write amounts drill, and Slap the Board. No audio needed — "
     "the pinyin exercise is out at the teacher's request, so this lesson runs entirely off the projector.",
     "New words · 6", "钱 · 块 · 元 · 毛 · 角 · 分"),
    ("l2-asking-prices", "Lesson 2 of 6", "怎么卖？", "Asking the price",
     "买 against 卖, the measure-word drill, and the p.112 food-stall role play with a 50块 budget "
     "as the extension.",
     "New words · 4", "买 · 卖 · 斤 · 一共"),
    ("l3-keyi-text1", "Lesson 3 of 6", "我可以用人民币吗？", "Permission · Text 1",
     "可以 in both its shapes, the market dialogue in full, listening track 58, and the simple "
     "characters 尸户革丁 as a writing relay.",
     "New words · 5", "用 · 人民 · 币 · 人民币 · 可以"),
    ("l4-de-complement", "Lesson 4 of 6", "做得特别好吃", "The 得 complement",
     "The 好吃 ladder from 特别好吃 down to 不好吃, then 得 after the verb — the structure the unit "
     "test asks for in three separate parts.",
     "New words · 4", "好吃 · 特 · 别 · 特别"),
    ("l5-ci-guo-dagai", "Lesson 5 of 6", "几次？大概多少钱？", "Frequency · 次 · 大概",
     "How often and roughly how much, a Find Someone Who survey round the room, and the four-tense "
     "revision grid kept in as the unit-test preparation.",
     "New words · 3", "次 · 一次 · 大概"),
    ("l6-huaqian-text2", "Lesson 6 of 6", "不算太贵", "Spending · Text 2",
     "The bill, the hedge, Text 2 in full, the market-and-shop role play, and a plenary that looks "
     "back across all six lessons.",
     "New words · 4", "花 · 百 · 算 · 贵"),
]


def write_index():
    src = open(os.path.join(ROOT, "index", "designs", "y8-l11", "index.html"),
               encoding="utf-8").read()
    src = re.sub(r"<title>.*?</title>",
                 "<title>Y8 L12 · 外出就餐 Eating Out</title>", src, count=1, flags=re.S)
    src = re.sub(r'<p class="kicker">.*?</p>',
                 '<p class="kicker">轻松学中文 2 · Unit 4 · Lesson 12</p>', src, count=1, flags=re.S)
    src = re.sub(r"<h1>.*?</h1>", "<h1>外出就餐</h1>", src, count=1, flags=re.S)
    src = re.sub(r'<p class="sub">.*?</p>',
                 '<p class="sub">Eating Out · Year 8</p>', src, count=1, flags=re.S)
    src = re.sub(r'<p class="meta">.*?</p>',
                 '<p class="meta">Six 50-minute lessons. Twenty-three new words spread across the '
                 'sequence — three to six per lesson, each pair taught as a three-slide cycle: the '
                 'words, then the words used, then the students using them. Every lesson carries a '
                 'CFU board straight after the new pattern, question-only: there is no answer slide '
                 'anywhere in the series. Revision happens inside every lesson rather than in a '
                 'review lesson at the end.</p>', src, count=1, flags=re.S)

    gitems = "".join(
        f'\n      <div class="fcell"><p class="l">{n}</p><p class="p">{zh}</p>'
        f'<p class="g">{en}</p></div>' for n, zh, en in GRAMMAR)
    src = re.sub(r'<div class="fgrid">.*?\n    </div>',
                 '<div class="fgrid">' + gitems + "\n    </div>", src, count=1, flags=re.S)

    cards = "".join(f'''
    <a class="card" href="{d}/">
      <p class="n">{n}</p>
      <p class="t">{cn}</p>
      <p class="e">{en}</p>
      <p class="d">{desc}</p>
      <p class="w"><span>{wl}</span>{ws}</p>
    </a>''' for d, n, cn, en, desc, wl, ws in CARDS)
    src = re.sub(r'<div class="grid">.*?\n  </div>\n  <footer>',
                 '<div class="grid">' + cards + "\n  </div>\n  <footer>", src, count=1, flags=re.S)

    src = re.sub(r"<footer>.*?</footer>", """<footer>
    <b>Six lessons, not seven.</b> The sequence ends on content, not revision — there is no 复习
    lesson, so the unit's Revision and Test pages get prepared inside the six. Every lesson opens
    with a cumulative Review phase, the workbook's test formats are used as the ordinary practice
    activities, and Lesson 6's plenary looks back across the whole sequence.
    <br><br>
    <b>No answer slides.</b> Every CFU board is questions only, by request. The answers live in the
    lesson plans in <code>docs/lesson-plans/y8-l12/</code>, where the teacher can see them and the
    class cannot.
    <br><br>
    <b>Not everything fitted.</b> 课本 p.111 Ex.2 (the un/ün pinyin exercise, dropped at the
    teacher's request), p.113 Ex.5 (clothing-shop role play, duplicated by p.120 Ex.16),
    p.118 Ex.12 (question words) and the two workbook dictionary sets are out — see the lesson plans
    for what was cut and why.
  </footer>""", src, count=1, flags=re.S)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(src)
    print("index.html written")


def check_images():
    """Every ../../img/NAME.svg a slide references must actually exist.
    A missing one renders as a broken image and no tool complains — which
    is exactly how 青菜 shipped blank on the first build."""
    have = {f[:-4] for f in os.listdir(os.path.join(OUT, "img")) if f.endswith(".svg")}
    missing = {}
    for deck in sorted(os.listdir(OUT)):
        sd = os.path.join(OUT, deck, "slides")
        if not os.path.isdir(sd):
            continue
        for f in sorted(os.listdir(sd)):
            html = open(os.path.join(sd, f), encoding="utf-8").read()
            for name in re.findall(r'\.\./\.\./img/([A-Za-z0-9_-]+)\.svg', html):
                if name not in have:
                    missing.setdefault(name, []).append(f"{deck}/{f}")
    if missing:
        for n, where in sorted(missing.items()):
            print(f"  MISSING img/{n}.svg  <- {where[0]}" +
                  (f" (+{len(where)-1} more)" if len(where) > 1 else ""))
        raise SystemExit(f"{len(missing)} drawing(s) referenced but not present")
    print("images: every reference resolves")


if __name__ == "__main__":
    write_shared()
    import l1, l2, l3, l4, l5, l6  # noqa: F401  — each writes its own deck
    write_index()
    check_images()
