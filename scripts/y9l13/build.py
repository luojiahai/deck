# -*- coding: utf-8 -*-
"""Slide generator for the Y9 L13 社区 (Neighbourhood) deck series.

Six decks, one per classroom lesson, from docs/lesson-plans/y9-l13/.
Same structural system as y9-l10 / y9-l11 / y9-l12: same chrome, same
three-slide vocabulary cycle, same typography floor. Unit 5 gets its own
palette — map paper and ink with a signal red — so a teacher can tell a
社区 deck from a 外出就餐 deck across the room.

Nothing here invents Chinese. Every sentence comes from the lesson plans,
which come from 轻松学中文 3 pp.122–131 and the workbook pp.144–153.

This file writes the WHOLE tree, per CLAUDE.md: shared/tokens.css, every
slides/*.html, each deck's index.html viewer, and the series index.html.
Nothing under index/designs/y9-l13/ is hand-maintained except img/, which
scripts/y9l13/art.py owns.

Constraints this file enforces so they cannot drift:
  · a slide that INTRODUCES vocabulary carries at most two new words
  · every pair runs the three-slide cycle A (words) → B (例句) → C (写一句)
  · every C slide carries an extension (s_write requires it positionally)
  · a word with no picturable referent gets a textonly card, not a
    forced drawing, and never an emoji — Chromium ships no colour emoji
    font and the PPTX/PDF export runs through Chromium
  · CFU slides carry questions only — s_cfu has no answers parameter, so
    an answer slide cannot be added by accident (the teacher asked for none)
  · no pinyin-discrimination and no radical/component slides in this
    series: s_components is deliberately absent from this builder

Run:  python3 scripts/y9l13/build.py
"""
import os, json, importlib

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(ROOT, "index", "designs", "y9-l13")

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


def s_words(a, b):
    return (label("New Words · 跟我读两遍 · repeat after me, twice")
            + '  <div class="word-pair">\n' + word_card(*a) + "\n"
            + word_card(*b) + "\n  </div>")


def s_word_one(a):
    """A single new word, centred. Used when a lesson's word count is odd —
    padding the slide out with an already-taught word to make a pair reads
    as two new words and is worse than an honest one-word slide."""
    return (label("New Word · 跟我读两遍 · repeat after me, twice")
            + '  <div class="word-pair single">\n' + word_card(*a) + "\n  </div>")


# ── Cycle B · example sentences ────────────────────────────────────
def s_examples(rows, question=None):
    out = [label("例句 · See them used").rstrip("\n"), '  <div class="sentence-list">']
    for r in rows:
        py, cn, en = r[0], r[1], r[2]
        both = " both" if (len(r) > 3 and r[3]) else ""
        py_line = '      <p class="sentence-py">%s</p>\n' % py if py else ""
        out.append('    <div class="sentence-row%s">\n%s'
                   '      <p class="sentence-cn">%s</p>\n'
                   '      <p class="sentence-en">%s</p>\n    </div>' % (both, py_line, cn, en))
    out.append("  </div>")
    if question:
        out.append('  <p class="support" style="margin-top:10pt;">问：%s</p>' % question)
    return "\n".join(out)


# ── Cycle C · write your own ───────────────────────────────────────
def s_write(frames, ext, minutes="60–90 秒"):
    """The extension is positional, not optional. Every write-your-own slide
    in this series carries one — it is the cheapest extension in the lesson
    and the one most often skipped."""
    lines = "\n".join('    <p class="frame-line">%s</p>' % f for f in frames)
    return (label("写一句 · Write one sentence · %s" % minutes)
            + '  <div class="frame-box">\n%s\n  </div>\n' % lines
            + '  <div class="extension-box">\n'
            '    <p class="extension-label">Extension</p>\n'
            '    <p class="extension-text">%s</p>\n  </div>' % ext)


# ── Checkpoints and boards ─────────────────────────────────────────
def s_recall(words, note, cols=3, head="认一认 · characters only · 一起读出来"):
    """A characters-only recall board.

    Three tiers, because a 4-word checkpoint and a 23-word end-of-sequence
    board are the same slide type at very different densities. The dense
    tier exists for the Lesson 6 board that carries every word in the
    series; without it that board runs 27px off the bottom of the canvas.
    """
    rows = -(-len(words) // cols)
    assert rows <= 4, ("%d words at %d columns is %d rows — the canvas holds 4. "
                       "Widen cols or split the board." % (len(words), cols, rows))
    dense = len(words) > 12
    if dense:
        size, pad, gap = ' style="font-size:26pt;"', ' style="padding:10pt 6pt;"', 10
    elif cols >= 5:
        size, pad, gap = ' style="font-size:30pt;"', ' style="padding:16pt 8pt;"', 14
    else:
        size, pad, gap = "", "", 16
    cells = "\n".join('    <div class="recall-cell"%s><p class="recall-hanzi"%s>%s</p></div>'
                      % (pad, size, w) for w in words)
    grid = ' style="grid-template-columns:repeat(%d,1fr);gap:%dpt;"' % (cols, gap)
    return (label(head)
            + '  <div class="recall-grid"%s>\n%s\n  </div>\n' % (grid, cells)
            + '  <p class="support" style="margin-top:10pt;">%s</p>' % note)


def s_errors(rows, head, note=None):
    """Correct the Teacher: wrong form struck through, right form beside it."""
    out = [label(head).rstrip("\n"), '  <div class="stack" style="gap:2pt;">']
    for wrong, right, why in rows:
        out.append('    <div class="err-row">'
                   '<div class="err-wrong"><p>%s</p></div>'
                   '<span class="err-arrow">›</span>'
                   '<div class="err-right"><p>%s</p></div>'
                   '<p class="support" style="margin-left:6pt;">%s</p></div>' % (wrong, right, why))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)


def s_cfu(rows, head="检查理解 · Check for understanding", note=None):
    """CFU question slide. Questions only — there is no answers parameter and
    no answer slide anywhere in this series, by the teacher's instruction. The
    answers are the teacher's to take live, on whiteboards or by cold call.

    Four questions is the ceiling at this size — a fifth is clipped silently
    by .slide-content's overflow:hidden, and a CFU the teacher never sees is
    worse than no CFU at all."""
    assert len(rows) <= 4, "s_cfu takes at most 4 questions, got %d" % len(rows)
    out = [label(head).rstrip("\n"), '  <div class="stack gap-md">']
    for i, r in enumerate(rows, 1):
        q = r[0]
        how = ('<p class="sc-cn">%s</p>' % r[1]) if len(r) > 1 and r[1] else ""
        out.append('    <div class="sc-row"><p class="sc-num">%d</p><div>'
                   '<p class="task-cn">%s</p>%s</div></div>' % (i, q, how))
    out.append("  </div>")
    out.append('  <p class="support" style="margin-top:10pt;">'
               '%s</p>' % (note or "答案不上屏——老师现场收（白板／点名）。"))
    return "\n".join(out)


def s_text(head, passage, questions, note=None):
    """A text/dialogue slide: the passage in a frame, questions under it."""
    out = [label(head).rstrip("\n"),
           '  <div class="frame-box">\n'
           '    <p class="frame-line" style="font-size:24pt;line-height:1.6;">%s</p>\n'
           '  </div>' % passage,
           '  <div class="task-box" style="margin-top:12pt;">\n'
           '    <p class="task-line"><b>用中文回答</b> · %s</p>' % questions]
    if note:
        out.append('    <p class="task-line" style="margin-top:6pt;">%s</p>' % note)
    out.append("  </div>")
    return "\n".join(out)


def s_dialogue(head, turns, note=None):
    """A two-voice dialogue, A/B alternating. Tightens itself past four turns."""
    tight = len(turns) > 4
    out = [label(head).rstrip("\n"),
           '  <div class="stack" style="gap:%dpt;">' % (5 if tight else 8)]
    pad = ' style="padding:8pt 14pt;"' if tight else ""
    fs = ' style="font-size:19pt;"' if tight else ""
    for who, cn in turns:
        col = "var(--accent-signal)" if who == "A" else "var(--accent-route)"
        out.append('    <div class="sc-row"%s><p class="sc-num" style="color:%s;font-size:20pt;'
                   'min-width:20pt;">%s</p>'
                   '<p class="task-cn"%s>%s</p></div>' % (pad, col, who, fs, cn))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)


def s_summary(items, note):
    cells = []
    for hz, pic in items:
        long = " long" if len(hz) >= 4 else ""
        pic_html = ('      <div class="sc-img">%s</div>\n' % img(pic)) if pic else ""
        cells.append('    <div class="summary-cell">\n%s'
                     '      <p class="summary-hanzi%s">%s</p>\n    </div>' % (pic_html, long, hz))
    cols = 4 if len(items) > 6 else 3
    grid = ' style="grid-template-columns:repeat(%d,1fr);"' % cols if cols != 3 else ""
    return (label("词汇总览 · 这一课的生词 · stays up while you work")
            + '  <div class="summary-grid"%s>\n%s\n  </div>\n' % (grid, "\n".join(cells))
            + '  <p class="support" style="margin-top:12pt;">%s</p>' % note)


# ── Pattern, task, activity, game, plenary ─────────────────────────
def s_pattern(head, formula, rows, note=None):
    # Three worked examples is what fits above the fold at 21pt. A fourth
    # gets clipped silently by .slide-content's overflow:hidden — put the
    # hardest one on its own s_focus slide instead.
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
    """One hard example on its own slide, set large. Used for the last and
    hardest example of a pattern, which never fits under the other three."""
    size = 24 if len(cn) > 30 else 27
    out = [label(head).rstrip("\n"),
           '  <div class="frame-box">\n'
           '    <p class="frame-line" style="font-size:%dpt;line-height:1.55;">%s</p>\n'
           '  </div>' % (size, cn),
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
    cap = 6 if compact else 5
    assert len(rows) <= cap, ("s_list takes at most %d rows%s, got %d"
                              % (cap, " compact" if compact else "", len(rows)))
    out = [label(head).rstrip("\n"),
           '  <div class="stack"%s>' % (' style="gap:5pt;"' if compact else ' class="gap-md"')]
    pad = ' style="padding:7pt 14pt;"' if compact else ""
    num = ' style="font-size:19pt;min-width:19pt;"' if compact else ""
    for i, r in enumerate(rows, 1):
        main = r[0]
        cn = ('<p class="sc-cn">%s</p>' % r[1]) if len(r) > 1 and r[1] else ""
        out.append('    <div class="sc-row"%s><p class="sc-num"%s>%d</p><div>'
                   '<p class="sc-main">%s</p>%s</div></div>' % (pad, num, i, main, cn))
    out.append("  </div>")
    if note:
        out.append('  <p class="support" style="margin-top:%s;">%s</p>'
                   % ("8pt" if compact else "10pt", note))
    return "\n".join(out)


def s_listening(head, items, note=None):
    """Six listening items in two columns.

    One column of six sc-rows is 94px too tall for the canvas — the last two
    items drop off the bottom and nobody notices until the CD is playing.
    """
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


# ── Unit 5 specific: routes and direction arrows ───────────────────
def s_route(head, steps, landing=None, note=None):
    """A multi-step route as numbered chips with arrows between them.

    Unit 5's whole point is that a route is a SEQUENCE. Setting the steps
    as a chain, not a bulleted list, is the sentence structure made visible.
    Four steps is the ceiling at this size — a fifth wraps into the footer.
    """
    assert len(steps) <= 4, "s_route takes at most 4 steps, got %d" % len(steps)
    cells = []
    for i, s in enumerate(steps):
        cells.append('    <div class="step"><span class="step-n">%d</span>%s</div>' % (i + 1, s))
        if i < len(steps) - 1:
            cells.append('    <span class="step-arrow">&rsaquo;</span>')
    out = [label(head).rstrip("\n"),
           '  <div class="route">\n%s\n  </div>' % "\n".join(cells)]
    if landing:
        out.append('  <div class="landing"><p class="landing-text">%s</p></div>' % landing)
    if note:
        out.append('  <p class="support" style="margin-top:12pt;">%s</p>' % note)
    return "\n".join(out)


def s_arrows(head, items, note=None):
    """The direction phrases beside their arrow diagrams. Six per board."""
    cells = "\n".join(
        '    <div class="arrow-cell">\n'
        '      <div class="ac-img">%s</div>\n'
        '      <p class="ac-hanzi">%s</p>\n    </div>' % (img(pic), hz)
        for hz, pic in items)
    return (label(head)
            + '  <div class="arrow-grid">\n%s\n  </div>\n' % cells
            + ('  <p class="support" style="margin-top:12pt;">%s</p>' % note if note else ""))


def s_title(cn, en, meta, motif):
    return ('  <p class="section-label">%s</p>\n'
            '  <p class="display-xl" style="margin-top:10pt;">%s</p>\n'
            '  <p class="display-md text-route" style="margin-top:6pt;">%s</p>\n'
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
def build_deck(slug, title, slides):
    """slides: list of dicts {file, label, tag, section, body, cls}

    No pptx link in the shell: this is a web-only series (see README), and a
    shell that links a .pptx it does not have 404s on the teacher.
    """
    d = os.path.join(OUT, slug)
    os.makedirs(os.path.join(d, "slides"), exist_ok=True)
    total = len(slides)
    for n, s in enumerate(slides, 1):
        html = PAGE.format(title="Y9 L13 · " + s["label"], tag=s["tag"],
                           section=s["section"], num=n, total=total,
                           body=s["body"], cls=s.get("cls", ""))
        with open(os.path.join(d, "slides", s["file"]), "w", encoding="utf-8") as f:
            f.write(html)
    manifest = ",\n".join(
        '    { file: "slides/%s", label: %s }' % (s["file"], json.dumps(s["label"], ensure_ascii=False))
        for s in slides)
    shell = SHELL.format(title=title, manifest=manifest, total=total, slug=slug)
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
  html,body{{height:100%;background:#12171C;font-family:-apple-system,"PingFang SC",sans-serif;overflow:hidden}}
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
  .bar a.home{{color:#E4A08C}}
  .bar a.home:hover{{color:#fff}}
  #grid{{position:fixed;inset:0;background:#12171C;z-index:40;overflow:auto;padding:36px;display:none;
        grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;align-content:start}}
  #grid.on{{display:grid}}
  .cell{{cursor:pointer}}
  .cell .thumb{{width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:8px;background:#fff;position:relative;
               border:2px solid transparent}}
  .cell:hover .thumb{{border-color:#B3321E}}
  .cell .thumb iframe{{transform-origin:top left;pointer-events:none;position:absolute;top:0;left:0}}
  .cell p{{color:rgba(255,255,255,.72);font-size:12.5px;margin-top:8px;line-height:1.4}}
  .cell p b{{color:#E4A08C;font-weight:600;margin-right:6px}}
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
  <span>·</span>
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

LESSONS = ["l1", "l2", "l3", "l4", "l5", "l6"]


def write_tokens():
    os.makedirs(os.path.join(OUT, "shared"), exist_ok=True)
    with open(os.path.join(OUT, "shared", "tokens.css"), "w", encoding="utf-8") as f:
        f.write(TOKENS)


def write_series_index(decks):
    cards = []
    for i, (slug, cn, en, badge, blurb) in enumerate(decks, 1):
        cards.append(
            '        <div class="lesson-card">\n'
            '          <a class="card-link" href="%s/">\n'
            '            <span class="card-num">%02d</span>\n'
            '            <h3 class="card-title">%s</h3>\n'
            '            <p class="card-en">%s</p>\n'
            '            <p class="card-blurb">%s</p>\n'
            '            <span class="card-badge badge-%s">%s</span>\n'
            '          </a>\n'
            '        </div>' % (slug, i, cn, en, blurb, badge, badge))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(SERIES_INDEX.replace("{{CARDS}}", "\n".join(cards)))


def main():
    write_tokens()
    total = 0
    metas = []
    for mod_name in LESSONS:
        mod = importlib.import_module("scripts.y9l13." + mod_name) if __package__ else \
              importlib.import_module(mod_name)
        n = build_deck(mod.SLUG, mod.TITLE, mod.slides())
        print("  %-26s %2d slides" % (mod.SLUG, n))
        metas.append(mod.CARD)
        total += n
    write_series_index(metas)
    print("built %d slides across %d decks" % (total, len(LESSONS)))
    print("wrote shared/tokens.css and the series index.html")


TOKENS = """/* ═══════════════════════════════════════════════════
   Y9 L13 · Neighbourhood 社区 · 6-lesson deck series
   GENERATED by scripts/y9l13/build.py — do not hand-edit.

   Canvas is 960pt × 540pt, so every pt here is 2px on the
   1920×1080 projector, and the classroom typography floor
   (26px for anything a student must read, 18px for anything
   at all) becomes 13pt / 9pt here. The smallest type in this
   file is the 10pt header tag = 20px. Nothing is below the
   floor, and no slide may override below it.

   Unit 5 gets its own palette — map paper, ink, and a signal
   red — so a 社区 deck is distinguishable from the Unit 4
   食物 decks across a staffroom. Same type scale, same
   structural vocabulary as y9-l10 / y9-l11 / y9-l12.
   ═══════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600;700;900&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Sans:wght@400;500;700&display=swap');

/* ── Canvas lock: 1920×1080 projector ── */
html, body {
  margin: 0; padding: 0;
  width: 960pt; height: 540pt;
  overflow: hidden;
  font-family: var(--font-body);
  color: var(--text-primary);
  background: var(--bg-primary);
}
p, h1, h2, h3, h4 { margin: 0; }

:root {
  --bg-primary: #F7F5F0;
  --bg-secondary: #ECE8DF;
  --bg-tertiary: #DFD9CC;
  --text-primary: #1F2933;
  --text-secondary: #4A5763;
  --text-muted: #6B7784;
  --accent-signal: #B3321E;
  --accent-signal-dim: rgba(179, 50, 30, 0.11);
  --accent-route: #2D6A4F;
  --accent-route-dim: rgba(45, 106, 79, 0.10);
  --accent-slate: #2F5A7A;
  --accent-slate-dim: rgba(47, 90, 122, 0.12);
  --border-light: #DCD5C7;
  --border-medium: #BFB6A4;

  --font-display: 'Noto Serif SC', 'Songti SC', 'STSong', serif;
  --font-body: 'Noto Sans', 'Noto Sans SC', 'PingFang SC', -apple-system, 'Microsoft YaHei', sans-serif;

  --space-sm: 8pt;
  --space-md: 12pt;
  --space-lg: 20pt;
  --radius-md: 6pt;
  --radius-lg: 10pt;
}

/* ── Chrome ── */
.slide-header {
  position: absolute; top: 0; left: 0; right: 0;
  height: 42pt; display: flex; align-items: center;
  padding: 0 40pt;
  border-bottom: 0.5pt solid var(--border-light);
  background: var(--bg-primary);
}
.slide-header .lesson-tag {
  font-size: 10pt; font-weight: 700; letter-spacing: 0.10em;
  color: var(--accent-signal);
}
.slide-header .sep { width: 0.5pt; height: 13pt; background: var(--border-medium); margin: 0 11pt; }
.slide-header .section-name { font-size: 11pt; color: var(--text-secondary); font-weight: 500; }
.slide-header .accent-line {
  position: absolute; top: 0; left: 40pt; right: 40pt;
  height: 2.5pt; background: var(--accent-signal);
}
.slide-num { margin-left: auto; font-size: 10pt; color: var(--text-muted); letter-spacing: 0.04em; }

.slide-content {
  position: absolute; top: 42pt; left: 0; right: 0; bottom: 40pt;
  padding: 24pt 48pt;
  display: flex; flex-direction: column; justify-content: center;
  overflow: hidden;
}
.slide-content.top { justify-content: flex-start; }

/* ── Type scale — every size at or above the classroom floor ── */
.display-xl { font-family: var(--font-display); font-size: 66pt; font-weight: 900; line-height: 1.08; }
.display-lg { font-family: var(--font-display); font-size: 42pt; font-weight: 900; line-height: 1.14; }
.display-md { font-family: var(--font-display); font-size: 30pt; font-weight: 700; line-height: 1.2; }
.heading    { font-family: var(--font-display); font-size: 23pt; font-weight: 700; line-height: 1.25; }
.body-lg    { font-size: 18pt; line-height: 1.5;  color: var(--text-secondary); }
.body-md    { font-size: 15pt; line-height: 1.55; color: var(--text-secondary); }
.support    { font-size: 12pt; line-height: 1.5;  color: var(--text-muted); }
.caption    { font-size: 11pt; color: var(--text-muted); letter-spacing: 0.04em; }

.section-label {
  font-size: 11pt; font-weight: 700; letter-spacing: 0.12em;
  color: var(--accent-signal); text-transform: uppercase;
}

.text-signal { color: var(--accent-signal); }
.text-route  { color: var(--accent-route); }
.text-slate  { color: var(--accent-slate); }

/* ── Two-word vocabulary slide ── */
.word-pair { display: grid; grid-template-columns: 1fr 1fr; gap: 28pt; margin-top: 8pt; }
/* odd word count: one card, centred, same height as a pair */
.word-pair.single { grid-template-columns: minmax(0, 340pt); justify-content: center; }
.word-card {
  background: var(--bg-secondary);
  border: 1pt solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 30pt 22pt;
  display: flex; flex-direction: column; align-items: center; gap: 9pt;
}
.word-card .wc-img { height: 150pt; display: flex; align-items: center; justify-content: center; }
.word-card .wc-img img { height: 150pt; width: auto; }
.word-pinyin { font-size: 17pt; font-weight: 500; color: var(--accent-route); letter-spacing: 0.02em; }
.word-hanzi  { font-family: var(--font-display); font-size: 48pt; font-weight: 900; line-height: 1.1; color: var(--text-primary); }
.word-hanzi.long { font-size: 38pt; }
.word-english { font-size: 15pt; color: var(--text-secondary); }

/* no-visual variant: the two words carry the slide */
.word-card.textonly { padding: 74pt 22pt; gap: 14pt; }
.word-card.textonly .word-hanzi { font-size: 66pt; }

/* ── Example-sentence slide ── */
.sentence-list { display: flex; flex-direction: column; gap: 12pt; margin-top: 6pt; }
.sentence-row {
  background: var(--bg-secondary);
  border-left: 4pt solid var(--accent-route);
  border-radius: 0 var(--radius-md) var(--radius-md) 0;
  padding: 12pt 18pt;
}
.sentence-row.both { border-left-color: var(--accent-signal); background: var(--accent-signal-dim); }
.sentence-cn {
  font-family: var(--font-display); font-size: 26pt; font-weight: 700;
  line-height: 1.35; color: var(--text-primary);
}
.sentence-cn b { color: var(--accent-signal); font-weight: 900; }
.sentence-en { font-size: 13.5pt; color: var(--text-secondary); margin-top: 5pt; }

/* ── Write-your-own slide ── */
.frame-box {
  background: var(--bg-tertiary);
  border: 1.5pt solid var(--accent-slate);
  border-radius: var(--radius-lg);
  padding: 24pt 26pt;
}
.frame-line {
  font-family: var(--font-display); font-size: 30pt; font-weight: 700;
  line-height: 1.75; color: var(--text-primary);
}
.frame-line b { color: var(--accent-signal); }
.extension-box {
  background: var(--accent-route-dim);
  border: 1.5pt solid var(--accent-route);
  border-radius: var(--radius-md);
  padding: 14pt 18pt;
  margin-top: 14pt;
}
.extension-label {
  font-size: 11pt; font-weight: 700; letter-spacing: 0.10em;
  color: var(--accent-route); text-transform: uppercase; margin-bottom: 5pt;
}
.extension-text { font-size: 16pt; line-height: 1.45; color: var(--text-primary); }
.extension-text b { color: var(--accent-route); }

/* ── Recall / summary boards ── */
.recall-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16pt; margin-top: 10pt; }
.recall-cell {
  background: var(--bg-secondary);
  border: 1pt solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 26pt 10pt;
  text-align: center;
}
.recall-hanzi { font-family: var(--font-display); font-size: 44pt; font-weight: 900; color: var(--text-primary); }

.summary-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14pt; margin-top: 8pt; }
.summary-cell {
  background: var(--bg-secondary);
  border: 1pt solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 10pt 8pt;
  display: flex; flex-direction: column; align-items: center; gap: 8pt;
}
.summary-cell .sc-img { height: 66pt; display: flex; align-items: center; justify-content: center; }
.summary-cell .sc-img img { height: 66pt; width: auto; }
.summary-hanzi { font-family: var(--font-display); font-size: 28pt; font-weight: 900; color: var(--text-primary); }
.summary-hanzi.long { font-size: 23pt; }

/* ── Task / activity slide ── */
.task-box {
  background: var(--bg-secondary);
  border: 1.5pt dashed var(--border-medium);
  border-radius: var(--radius-lg);
  padding: 18pt 24pt;
}
.task-line { font-size: 17pt; line-height: 1.6; color: var(--text-primary); }
.task-line b { color: var(--accent-signal); }
.task-cn { font-family: var(--font-display); font-size: 21pt; font-weight: 700; color: var(--text-primary); line-height: 1.5; }

.pattern-box {
  background: var(--bg-tertiary);
  border: 1.5pt solid var(--accent-signal);
  border-radius: var(--radius-lg);
  padding: 15pt 24pt;
  text-align: center;
}
.pattern-text { font-family: var(--font-display); font-size: 31pt; font-weight: 900; color: var(--text-primary); letter-spacing: 0.02em; }

.sc-row {
  display: flex; align-items: flex-start; gap: 13pt;
  padding: 12pt 16pt;
  background: var(--bg-secondary);
  border: 0.5pt solid var(--border-light);
  border-radius: var(--radius-md);
}
.sc-num { font-family: var(--font-display); font-size: 23pt; font-weight: 900; color: var(--accent-signal); min-width: 23pt; line-height: 1.2; }
.sc-main { font-size: 16pt; line-height: 1.4; color: var(--text-primary); }
.sc-cn { font-family: var(--font-display); font-size: 15pt; font-weight: 700; color: var(--accent-route); margin-top: 4pt; }

.stack { display: flex; flex-direction: column; }
.gap-md { gap: var(--space-md); }
.gap-lg { gap: var(--space-lg); }

/* ── Error-correction pair, used by Correct the Teacher ── */
.err-row { display: flex; align-items: center; gap: 16pt; padding: 10pt 0; }
/* The chip is a <div>: html2pptx only carries background/border/shadow on a
   div, never on a text element, so the <p> inside holds type alone. */
.err-wrong, .err-right { padding: 9pt 16pt; border-radius: var(--radius-md); }
.err-wrong { background: rgba(179, 50, 30, 0.10); }
.err-right { background: var(--accent-route-dim); }
.err-wrong p, .err-right p {
  font-family: var(--font-display); font-size: 24pt; font-weight: 700;
}
.err-wrong p { color: #8A2C1C; text-decoration: line-through; }
.err-right p { color: var(--accent-route); }
.err-arrow { font-size: 21pt; color: var(--text-muted); }

/* ── Route chain: a journey is a sequence, so it is set as one ── */
.route { display: flex; align-items: stretch; gap: 8pt; margin-top: 10pt; }
.route .step {
  flex: 1;
  background: var(--bg-secondary);
  border: 1pt solid var(--border-light);
  border-top: 3pt solid var(--accent-slate);
  border-radius: var(--radius-md);
  padding: 16pt 12pt;
  font-family: var(--font-display); font-size: 21pt; font-weight: 700;
  color: var(--text-primary); line-height: 1.4;
  display: flex; flex-direction: column; gap: 7pt;
}
.route .step-n {
  font-family: var(--font-body); font-size: 11pt; font-weight: 700;
  letter-spacing: 0.10em; color: var(--accent-slate);
}
.route .step-arrow { align-self: center; font-size: 26pt; color: var(--text-muted); }
.landing {
  background: var(--accent-signal-dim);
  border: 1.5pt solid var(--accent-signal);
  border-radius: var(--radius-md);
  padding: 14pt 20pt; margin-top: 14pt;
}
.landing-text { font-family: var(--font-display); font-size: 25pt; font-weight: 700; color: var(--text-primary); }

/* ── Direction-arrow board ── */
.arrow-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14pt; margin-top: 10pt; }
.arrow-cell {
  background: var(--bg-secondary);
  border: 1pt solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 10pt 8pt;
  display: flex; flex-direction: column; align-items: center; gap: 6pt;
}
.arrow-cell .ac-img { height: 74pt; display: flex; align-items: center; justify-content: center; }
.arrow-cell .ac-img img { height: 74pt; width: auto; }
.ac-hanzi { font-family: var(--font-display); font-size: 25pt; font-weight: 900; color: var(--text-primary); }
"""


SERIES_INDEX = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Y9 L13 · 社区 Neighbourhood</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600;700;900&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg: #F7F5F0; --text: #1F2933; --text-muted: #6B7784;
    --accent: #B3321E; --accent-route: #2D6A4F; --accent-slate: #2F5A7A;
    --border: #DCD5C7; --card-bg: #ECE8DF;
    --font-display: 'Noto Serif SC', 'Songti SC', serif;
    --font-body: 'Noto Sans', 'Noto Sans SC', 'PingFang SC', -apple-system, sans-serif;
  }
  body { font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.6; -webkit-font-smoothing: antialiased; min-height: 100vh; }
  .container { max-width: 1200px; margin: 0 auto; padding: 0 32px; }

  .top-nav { border-bottom: 1px solid var(--border); padding: 12px 0; }
  .top-nav a { font-size: 13px; letter-spacing: 0.06em; color: var(--text-muted); text-decoration: none; }
  .top-nav a:hover { color: var(--accent); }

  .hero { padding: 40px 0 30px; }
  .hero-inner { display: flex; align-items: center; gap: 36px; }
  .hero-text { display: flex; flex-direction: column; }
  .unit-tag { display: inline-block; align-self: flex-start; font-size: 14px; font-weight: 700; letter-spacing: 0.16em; color: var(--accent); text-transform: uppercase; margin-bottom: 12px; padding: 4px 16px; border: 1px solid var(--accent); border-radius: 999px; }
  .hero h1 { font-family: var(--font-display); font-size: 56px; font-weight: 900; letter-spacing: -0.02em; line-height: 1.15; margin-bottom: 6px; }
  .subtitle { font-size: 20px; color: var(--text-muted); margin-bottom: 20px; letter-spacing: 0.02em; }
  .meta { display: flex; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 15px; color: var(--text-muted); letter-spacing: 0.04em; }
  .meta .pill { background: var(--card-bg); padding: 5px 14px; border-radius: 999px; }
  .hero-motif { width: 104px; height: 104px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 2px solid var(--border); font-family: var(--font-display); font-size: 42px; font-weight: 900; color: var(--accent); line-height: 1; opacity: 0.8; }

  .grammar-panel { margin-bottom: 40px; background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 26px 32px; }
  .grammar-panel h2 { font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 20px; }
  .grammar-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
  .grammar-item { text-align: center; padding: 16px 12px; border-radius: 12px; background: var(--bg); border: 1px solid var(--border); }
  .grammar-item .g-num { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent); margin-bottom: 6px; }
  .grammar-item .g-zh { font-family: var(--font-display); font-size: 20px; font-weight: 700; color: var(--text); margin-bottom: 4px; }
  .grammar-item .g-en { font-size: 13px; color: var(--text-muted); }

  .lessons { padding: 0 0 80px; }
  .section-title { font-family: var(--font-display); font-size: 28px; font-weight: 700; margin-bottom: 24px; color: var(--text-muted); letter-spacing: 0.04em; }
  .lesson-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
  .lesson-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 26px 24px; color: inherit; transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease; display: flex; flex-direction: column; }
  .lesson-card:hover { transform: translateY(-3px); box-shadow: 0 12px 32px rgba(31,41,51,0.10); border-color: var(--accent); }
  .card-link { text-decoration: none; color: inherit; display: flex; flex-direction: column; flex: 1; }
  .card-num { font-family: var(--font-display); font-size: 48px; font-weight: 900; color: var(--accent); opacity: 0.22; line-height: 1; margin-bottom: -8px; }
  .card-title { font-family: var(--font-display); font-size: 24px; font-weight: 700; margin-bottom: 4px; line-height: 1.3; }
  .card-en { font-size: 14px; color: var(--text-muted); margin-bottom: 10px; letter-spacing: 0.03em; }
  .card-blurb { font-size: 14px; color: var(--text-muted); line-height: 1.55; margin-bottom: 14px; }
  .card-badge { display: inline-block; align-self: flex-start; font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; padding: 3px 10px; border-radius: 999px; margin-top: auto; }
  .badge-vocab    { background: #E7E2D6; color: #8A4A20; }
  .badge-grammar  { background: #DFEAE2; color: #1E6055; }
  .badge-speaking { background: #F2E0DB; color: #9C3C2C; }
  .badge-writing  { background: #DEE7EE; color: #2F5A7A; }
  .badge-game     { background: #EDE4D8; color: #7A4426; }

  .footnote { margin-top: 36px; font-size: 13px; color: var(--text-muted); line-height: 1.7; }
  .footnote b { color: var(--text); }

  @media (max-width: 900px) { .lesson-grid, .grammar-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 620px) { .lesson-grid, .grammar-grid { grid-template-columns: 1fr; } .hero h1 { font-size: 40px; } .hero-motif { display: none; } }
</style>
</head>
<body>

<div class="top-nav">
  <div class="container">
    <a href="../../">← Deck Gallery · 设计画廊</a>
  </div>
</div>

<header class="hero">
  <div class="container hero-inner">
    <div class="hero-text">
      <span class="unit-tag">Year 9 · Book 3 · Unit 5 · Lesson 13</span>
      <h1>社区</h1>
      <p class="subtitle">Neighbourhood · 六节课 · 轻松学中文 3 pp.122–131</p>
      <div class="meta">
        <span class="pill">6 decks</span>
        <span class="pill">27 new words</span>
        <span class="pill">50 min each</span>
        <span class="pill">CFU, no answer slides</span>
      </div>
    </div>
    <div class="hero-motif">路</div>
  </div>
</header>

<div class="container">
  <section class="grammar-panel">
    <h2>这一课的三个句型 · The three patterns</h2>
    <div class="grammar-grid">
      <div class="grammar-item">
        <p class="g-num">Lessons 1–3</p>
        <p class="g-zh">A 离 B 远／不远</p>
        <p class="g-en">distance from a landmark</p>
      </div>
      <div class="grammar-item">
        <p class="g-num">Lessons 2–3</p>
        <p class="g-zh">A 就在 B 对面／前面</p>
        <p class="g-en">placing one building against another</p>
      </div>
      <div class="grammar-item">
        <p class="g-num">Lessons 4–6</p>
        <p class="g-zh">先……，然后……，就到了</p>
        <p class="g-en">giving a route, step by step</p>
      </div>
    </div>
  </section>

  <section class="lessons">
    <h2 class="section-title">六节课 · The six lessons</h2>
    <div class="lesson-grid">
{{CARDS}}
    </div>

    <p class="footnote">
      Every pair of new words runs a three-slide cycle — <b>生词 → 例句 → 写一句</b> —
      and every 写一句 slide carries an extension. Each lesson has a CFU board;
      <b>there are no answer slides anywhere in this series</b>, by the teacher's
      instruction — the answers are taken live, on whiteboards or by cold call.
      <b>No pinyin-discrimination and no radical practice</b>: Lesson 13 has no
      radicals box in the textbook, and Book 3 has dropped pinyin exercises.
      Type is set to the classroom floor — nothing a student must read is under
      26px on a 1920×1080 projector.
    </p>
  </section>
</div>

</body>
</html>
"""


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
