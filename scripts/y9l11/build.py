# -*- coding: utf-8 -*-
"""Slide generator for the Y9 L11 零食 (Snacks) deck series.

Five decks, one per classroom lesson, from docs/lesson-plans/y9-l11/.
Same system as y9-l10 菜市场: same chrome, same three-slide vocabulary
cycle, same typography floor. Nothing here invents Chinese — every
sentence comes from the lesson plans, which come from 轻松学中文 3
pp.100–109 and the workbook pp.118–127.

Constraints this file enforces so they cannot drift:
  · a slide that INTRODUCES vocabulary carries at most two new words
  · every pair runs the three-slide cycle A (words) → B (例句) → C (写一句)
  · every C slide carries an extension
  · a word with no picturable referent gets a textonly card, not a
    forced drawing

Run:  python3 scripts/y9l11/build.py
"""
import os, json, importlib

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(ROOT, "index", "designs", "y9-l11")

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
    lines = "\n".join('    <p class="frame-line">%s</p>' % f for f in frames)
    return (label("写一句 · Write one sentence · %s" % minutes)
            + '  <div class="frame-box">\n%s\n  </div>\n' % lines
            + '  <div class="extension-box">\n'
            '    <p class="extension-label">Extension</p>\n'
            '    <p class="extension-text">%s</p>\n  </div>' % ext)


# ── Checkpoints and boards ─────────────────────────────────────────
def s_recall(words, note, cols=3, size=None, head="认一认 · characters only · 一起读出来"):
    pad = ' style="padding:%s;"' % size if size else ""
    cells = "\n".join('    <div class="recall-cell"%s><p class="recall-hanzi"%s>%s</p></div>'
                       % (pad, ' style="font-size:30pt;"' if cols >= 6 else "", w)
                       for w in words)
    grid = ' style="grid-template-columns:repeat(%d,1fr);"' % cols if cols != 3 else ""
    return (label(head)
            + '  <div class="recall-grid"%s>\n%s\n  </div>\n' % (grid, cells)
            + '  <p class="support" style="margin-top:12pt;">%s</p>' % note)


def s_components(items, head, note):
    """Textbook 'memorize these characters within 5 minutes' grid."""
    cells = "\n".join('    <div class="comp-cell"><p class="comp-hanzi">%s</p></div>' % c
                       for c in items)
    return (label(head)
            + '  <div class="comp-grid">\n%s\n  </div>\n' % cells
            + '  <p class="support" style="margin-top:14pt;">%s</p>' % note)


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


def s_ladder(rungs, head, note=None, box=None):
    """Frequency ladder. rungs: list of (text, is_new)."""
    cells = []
    for i, (w, new) in enumerate(rungs):
        cells.append('    <div class="rung%s">%s</div>' % (" new" if new else "", w))
        if i < len(rungs) - 1:
            cells.append('    <span class="arrow">&rsaquo;</span>')
    out = [label(head).rstrip("\n"), '  <div class="ladder">', "\n".join(cells), "  </div>"]
    if box:
        out.append('  <div class="task-box" style="margin-top:16pt;">'
                   '<p class="task-cn">%s</p></div>' % box)
    if note:
        out.append('  <p class="support" style="margin-top:10pt;">%s</p>' % note)
    return "\n".join(out)


def s_text(head, passage, questions, note=None):
    """A text/dialogue slide: the passage in a frame, questions under it."""
    out = [label(head).rstrip("\n"),
           '  <div class="frame-box">\n'
           '    <p class="frame-line" style="font-size:25pt;line-height:1.55;">%s</p>\n'
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
        col = "var(--accent-brick)" if who == "A" else "var(--accent-jade)"
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
    return (label("词汇总览 · 这一课的生词 · stays up while you work")
            + '  <div class="summary-grid">\n%s\n  </div>\n' % "\n".join(cells)
            + '  <p class="support" style="margin-top:12pt;">%s</p>' % note)


# ── Pattern, task, activity, game, plenary ─────────────────────────
def s_pattern(head, formula, rows, note=None):
    # Three worked examples is what fits above the fold at 21pt. A fourth
    # gets clipped silently by .slide-content's overflow:hidden - put the
    # hardest one on its own s_focus slide instead.
    assert len(rows) <= 3, "s_pattern takes at most 3 rows, got %d - use s_focus" % len(rows)
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
    gap = ' style="gap:6pt;"' if compact else ' class="gap-md"'
    pad = ' style="padding:8pt 14pt;"' if compact else ""
    num = ' style="font-size:19pt;min-width:19pt;"' if compact else ""
    out = [label(head).rstrip("\n"),
           '  <div class="stack"%s>' % gap if compact else '  <div class="stack gap-md">']
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


def s_listening(head, items, note=None, track=None):
    """Six multiple-choice listening items in two columns.

    One column of six sc-rows is 94px too tall for the canvas - the last two
    items drop off the bottom and nobody notices until the CD is playing.
    """
    half = (len(items) + 1) // 2
    cols = [items[:half], items[half:]]
    out = [label(head).rstrip("\n"),
           '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14pt;">']
    n = 0
    for col in cols:
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


def s_title(cn, en, meta, motif):
    return ('  <p class="section-label">%s</p>\n'
            '  <p class="display-xl" style="margin-top:10pt;">%s</p>\n'
            '  <p class="display-md text-jade" style="margin-top:6pt;">%s</p>\n'
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
    """slides: list of dicts {file, label, tag, section, body, cls}"""
    d = os.path.join(OUT, slug)
    os.makedirs(os.path.join(d, "slides"), exist_ok=True)
    total = len(slides)
    for n, s in enumerate(slides, 1):
        html = PAGE.format(title="Y9 L11 · " + s["label"], tag=s["tag"],
                           section=s["section"], num=n, total=total,
                           body=s["body"], cls=s.get("cls", ""))
        with open(os.path.join(d, "slides", s["file"]), "w", encoding="utf-8") as f:
            f.write(html)
    manifest = ",\n".join(
        '    { file: "slides/%s", label: %s }' % (s["file"], json.dumps(s["label"], ensure_ascii=False))
        for s in slides)
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
  html,body{{height:100%;background:#14110d;font-family:-apple-system,"PingFang SC",sans-serif;overflow:hidden}}
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
  .bar a.home{{color:#D9A86B}}
  .bar a.home:hover{{color:#fff}}
  #grid{{position:fixed;inset:0;background:#14110d;z-index:40;overflow:auto;padding:36px;display:none;
        grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;align-content:start}}
  #grid.on{{display:grid}}
  .cell{{cursor:pointer}}
  .cell .thumb{{width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:8px;background:#fff;position:relative;
               border:2px solid transparent}}
  .cell:hover .thumb{{border-color:#A8700F}}
  .cell .thumb iframe{{transform-origin:top left;pointer-events:none;position:absolute;top:0;left:0}}
  .cell p{{color:rgba(255,255,255,.72);font-size:12.5px;margin-top:8px;line-height:1.4}}
  .cell p b{{color:#D9A86B;font-weight:600;margin-right:6px}}
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


LESSONS = ["l1", "l2", "l3", "l4", "l5"]


def main():
    total = 0
    for mod_name in LESSONS:
        mod = importlib.import_module("scripts.y9l11." + mod_name) if __package__ else \
              importlib.import_module(mod_name)
        n = build_deck(mod.SLUG, mod.TITLE, mod.slides())
        print("  %-26s %2d slides" % (mod.SLUG, n))
        total += n
    print("built %d slides across %d decks" % (total, len(LESSONS)))


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
