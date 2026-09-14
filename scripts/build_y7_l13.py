#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the Y7 Lesson 13 slide decks (颜色) from the eight lesson plans in
docs/lesson-plans/y7-l13/.

Eight decks, one per classroom lesson — the teacher asked for eight rather
than the skill's default six, with a revision lesson at the end.

Markup and tokens deliberately match index/designs/y7-l14/: same unit, taught
back to back, so the two decks are one visual family. shared/tokens.css is
copied from there rather than forked.

Design constraints this script enforces, so they cannot drift:
  · a slide that INTRODUCES vocabulary carries at most two new words
  · every pair of new words runs the three-slide cycle A -> B -> C
  · every C slide carries an extension
  · nothing a student must read is set below 26px (see shared/tokens.css)
  · colour visuals are inline SVG swatches, never emoji (emoji export as
    empty boxes through Chromium into PPTX/PDF)

Run:  python3 scripts/build_y7_l13.py
"""

import os
import re
import shutil

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
BASE = os.path.join(ROOT, 'index', 'designs', 'y7-l13')
L14 = os.path.join(ROOT, 'index', 'designs', 'y7-l14')

TAG = 'Y7 · L13 颜色'
TOTAL_LESSONS = 8

# ══════════════════════════════════════════════════════════════════
#  Palette — content, not decoration. Matches shared/tokens.css.
# ══════════════════════════════════════════════════════════════════

SW = {
    '黑色': ('#1A1A1A', 'hēisè', 'black'),
    '白色': ('#FFFFFF', 'báisè', 'white'),
    '黄色': ('#E8B923', 'huángsè', 'yellow'),
    '蓝色': ('#2E5FA3', 'lánsè', 'blue'),
    '红色': ('#C23B2E', 'hóngsè', 'red'),
    '粉红色': ('#E88EA0', 'fěnhóngsè', 'pink'),
    '橙色': ('#D9762E', 'chéngsè', 'orange'),
    '紫色': ('#7A4E9E', 'zǐsè', 'purple'),
    '棕色': ('#8A5A34', 'zōngsè', 'brown'),
    '绿色': ('#4C8A4A', 'lǜsè', 'green'),
    '灰色': ('#9A9A94', 'huīsè', 'grey'),
    '天蓝色': ('#6FA8D6', 'tiānlánsè', 'sky blue'),
}

ALL_11 = ['黑色', '白色', '黄色', '蓝色', '红色', '粉红色',
          '橙色', '紫色', '棕色', '绿色', '灰色']
TEXT1_6 = ['黑色', '白色', '黄色', '蓝色', '红色', '粉红色']

# ══════════════════════════════════════════════════════════════════
#  Slide shell
# ══════════════════════════════════════════════════════════════════

STYLE_TITLE = '''<style>
  #frame, body { display:flex; align-items:center; justify-content:center; }
  .t-main { text-align:center; position:relative; z-index:1; }
  .t-num { font-size:26px; font-weight:700; letter-spacing:0.2em;
           color:var(--accent-indigo); text-transform:uppercase; margin-bottom:20px; }
  .t-art { height:150px; margin-bottom:18px; opacity:0.9; }
  .t-art svg { height:100%; width:auto; }
  .t-cn { font-family:var(--font-display); font-size:130px; font-weight:900;
          line-height:1.06; color:var(--text-primary); margin-bottom:12px; }
  .t-cn .dot { color:var(--accent-madder); }
  .t-en { font-size:34px; color:var(--text-secondary); margin-bottom:34px; }
  .t-meta { display:flex; align-items:center; justify-content:center; gap:26px;
            font-size:22px; color:var(--text-muted); letter-spacing:0.06em; }
  .t-meta .s { width:5px; height:5px; border-radius:50%; background:var(--accent-indigo); }
  .bg-char { position:absolute; right:70px; bottom:40px; font-family:var(--font-display);
             font-size:440px; color:var(--accent-indigo); opacity:0.045; line-height:1;
             pointer-events:none; user-select:none; }
</style>
'''

STYLE_CFU = '''<style>
  .cfu-list { display:flex; flex-direction:column; gap:26px; }
  .cfu-q { display:flex; align-items:flex-start; gap:22px; }
  .cfu-n { font-family:var(--font-display); font-size:42px; font-weight:900;
           color:var(--accent-madder); opacity:0.4; min-width:46px; }
  .cfu-t { font-size:32px; color:var(--text-primary); line-height:1.45; }
  .cfu-t .cn { font-family:var(--font-display); font-weight:700; font-size:42px; }
</style>
'''

STYLE_CENTRE = '''<style>
  #frame, body { display:flex; align-items:center; justify-content:center; }
</style>
'''

PAGE = '''<!DOCTYPE html><html lang="zh-CN"><head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="../../shared/tokens.css">
{style}</head>
<body>

<div class="slide-header">
  <div class="accent-line"></div>
  <span class="lesson-tag">{tag}</span>
  <span class="sep"></span>
  <span class="section-name">{section}</span>
</div>

<div class="slide-content{dense}">
{inner}</div>

<div class="slide-footer">
  <span>{foot}</span>
  <span class="brand">{brand}</span>
</div>

</body></html>
'''

# ══════════════════════════════════════════════════════════════════
#  Inline SVG — never emoji. Chromium ships no colour emoji font, so
#  emoji render as empty boxes in the PPTX and PDF exports.
# ══════════════════════════════════════════════════════════════════

def svg_swatch(hexv):
    """A colour word's visual is the colour itself."""
    stroke = '#CFC4A9' if hexv.upper() in ('#FFFFFF', '#FBF9F4') else 'none'
    sw = '3' if stroke != 'none' else '0'
    return (f'<svg viewBox="0 0 220 210" xmlns="http://www.w3.org/2000/svg">'
            f'<rect x="20" y="20" width="180" height="170" rx="22" '
            f'fill="{hexv}" stroke="{stroke}" stroke-width="{sw}"/></svg>')


def svg_smile():
    """喜欢 — a verb, but a face carries it without routing through English."""
    return ('<svg viewBox="0 0 220 210" xmlns="http://www.w3.org/2000/svg" fill="none" '
            'stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round">'
            '<circle cx="110" cy="105" r="76" stroke="#2C4C7C"/>'
            '<circle cx="84" cy="88" r="7" fill="#2C4C7C" stroke="none"/>'
            '<circle cx="136" cy="88" r="7" fill="#2C4C7C" stroke="none"/>'
            '<path d="M74 124 C 90 150, 130 150, 146 124" stroke="#B03C2C"/></svg>')


def svg_palette():
    """颜色 — the category word. A row of swatches, not one colour."""
    cols = ['#C23B2E', '#E8B923', '#4C8A4A', '#2E5FA3', '#7A4E9E', '#D9762E']
    cells = ''.join(
        f'<rect x="{18 + i * 31}" y="{72 + (i % 2) * 14}" width="26" height="66" rx="7" fill="{c}"/>'
        for i, c in enumerate(cols))
    return (f'<svg viewBox="0 0 220 210" xmlns="http://www.w3.org/2000/svg">'
            f'{cells}</svg>')


def svg_skyblue():
    """天蓝色 — sky blue needs the sky in it, or it is just blue."""
    return ('<svg viewBox="0 0 220 210" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="20" y="20" width="180" height="170" rx="22" fill="#6FA8D6"/>'
            '<path d="M62 132 a26 26 0 0 1 4 -50 a34 34 0 0 1 64 -6 a24 24 0 0 1 30 56 Z" '
            'fill="#FBF9F4"/></svg>')


ART = {'喜欢': svg_smile, '颜色': svg_palette, '天蓝色': svg_skyblue}


def art_for(word):
    if word in ART:
        return ART[word]()
    if word in SW:
        return svg_swatch(SW[word][0])
    return ''

# ══════════════════════════════════════════════════════════════════
#  Block builders — each returns inner HTML for one slide
# ══════════════════════════════════════════════════════════════════

def b_caption(text):
    return f'  <div class="caption" style="text-align:center;margin-bottom:26px;">{text}</div>\n'


def b_title(num, label, hanzi, en, meta, art_word):
    art = art_for(art_word)
    bg = hanzi.replace('·', '')[0]
    return f'''  <div class="bg-char">{bg}</div>
  <div class="t-main">
    <div class="t-num">Lesson {num} of {TOTAL_LESSONS} · Y7 Unit 5 · 轻松学中文 1</div>
    <div class="t-art">{art}</div>
    <h1 class="t-cn">{hanzi}</h1>
    <div class="t-en">{en}</div>
    <div class="t-meta">{meta}</div>
  </div>
'''


def b_words(items):
    """Slide A of a cycle. At most two items — the rule, enforced."""
    assert len(items) <= 2, 'a vocabulary slide carries at most two new words'
    cards = []
    for it in items:
        hz = it['hanzi']
        long = ' long' if len(hz) >= 3 else ''
        clue = f'<div class="wc-clue">{it["clue"]}</div>' if it.get('clue') else ''
        cards.append(f'''    <div class="word-card">
      <div class="wc-art">{art_for(hz)}</div>
      <div class="wc-hanzi{long}">{hz}</div>
      <div class="wc-pinyin">{it['pinyin']}</div>
      <div class="wc-english">{it['english']}</div>
      {clue}
    </div>''')
    return '  <div class="word-pair">\n' + '\n'.join(cards) + '\n  </div>\n'


def b_examples(rows, badge=None):
    out = []
    if badge:
        out.append(f'  <div style="margin-bottom:22px;"><span class="badge badge-indigo">{badge}</span></div>\n')
    out.append('  <div class="ex-list">\n')
    for r in rows:
        en = f'<div class="ex-en">{r["en"]}</div>' if r.get('en') else ''
        out.append(f'''    <div class="ex-row">
      <div class="ex-pinyin">{r['py']}</div>
      <div class="ex-hanzi">{r['cn']}</div>
      {en}
    </div>\n''')
    out.append('  </div>\n')
    return ''.join(out)


def b_write(frames, note, ext, secs='60 秒'):
    fl = '\n'.join(f'    <div class="sentence-frame">{f}</div>' for f in frames)
    return f'''  <div style="display:flex;flex-direction:column;gap:26px;">
{fl}
    <div style="display:flex;align-items:center;gap:20px;margin-top:6px;">
      <span class="badge badge-indigo">{secs}</span>
      <span class="body-lg" style="color:var(--text-primary);">{note}</span>
    </div>
{b_ext(ext)}  </div>
'''


def b_ext(ext):
    cn = f'<span class="cn">{ext["cn"]}</span>' if ext.get('cn') else ''
    sub = f'<span class="sub">{ext["sub"]}</span>' if ext.get('sub') else ''
    return f'''    <div class="extension-box">
      <span class="ext-label">更难</span>
      <span class="ext-body">{ext['text']}{cn}{sub}</span>
    </div>
'''


def b_cards(words, cols=6, caption=None, pinyin=False):
    """Recall / summary / review board. Known words only — scanned, not taught."""
    out = [b_caption(caption)] if caption else []
    cells = []
    for w in words:
        long = ' long' if len(w) >= 3 else ''
        if isinstance(w, tuple):
            w, py_txt = w
        else:
            py_txt = SW[w][1] if w in SW else ''
        if w in SW:
            hexv = SW[w][0]
            white = ' white' if hexv.upper() == '#FFFFFF' else ''
            vis = f'<span class="vc-swatch{white}" style="background:{hexv};"></span>'
        elif w in ART:
            vis = f'<div class="vc-art">{art_for(w)}</div>'
        else:
            vis = ''
        py = f'<div class="vc-pinyin">{py_txt}</div>' if pinyin and py_txt else ''
        cells.append(f'    <div class="vocab-card">{vis}<div class="vc-hanzi{long}">{w}</div>{py}</div>')
    out.append(f'  <div class="grid-{cols}">\n' + '\n'.join(cells) + '\n  </div>\n')
    return ''.join(out)


def b_pattern(formula, examples, note=None, note_kind='info', note_icon='的'):
    rows = []
    for e in examples:
        cn = e['cn']
        if e.get('hard'):
            cn = re.sub(r'\[(.+?)\]', r'<span class="new">\1</span>', cn)
        else:
            cn = cn.replace('[', '').replace(']', '')
        en = f'<div class="ex-en">{e["en"]}</div>' if e.get('en') else ''
        rows.append(f'''      <div class="ex-row">
        <div class="ex-pinyin">{e['py']}</div>
        <div class="ex-hanzi">{cn}</div>
        {en}
      </div>''')
    n = ''
    if note:
        pre = 'warn' if note_kind == 'warning' else note_kind
        n = f'''  <div class="{note_kind}-box" style="margin-top:2px;">
    <span class="{pre}-icon">{note_icon}</span>
    <span><span class="{pre}-text">{note['text']}</span>
    <span class="{pre}-sub">{note['sub']}</span></span>
  </div>
'''
    return f'''  <div class="pattern-wrap">
    <div><span class="formula-box">{formula}</span></div>
    <div class="ex-list">
{chr(10).join(rows)}
    </div>
  </div>
{n}'''


def b_cfu(questions, errors=None):
    qs = ''.join(f'    <div class="cfu-q"><span class="cfu-n">{i}</span>'
                 f'<span class="cfu-t">{q}</span></div>\n'
                 for i, q in enumerate(questions, 1))
    out = f'  <div class="cfu-list">\n{qs}  </div>\n'
    if errors:
        pairs = ''.join(f'''    <div class="error-pair">
      <span class="error-wrong">{w}</span>
      <span class="error-arrow">&rarr;</span>
      <span class="error-correct">{c}</span>
    </div>\n''' for w, c in errors)
        out += f'  <div style="display:flex;flex-direction:column;gap:16px;margin-top:36px;">\n{pairs}  </div>\n'
    return out


def b_lisc(intention, criteria):
    rows = ''.join(f'''      <div class="sc-row">
        <span class="sc-num">{i}</span>
        <span class="sc-text">{c['cn']}<span class="en">{c['en']}</span></span>
      </div>\n''' for i, c in enumerate(criteria, 1))
    gap = '14px' if len(criteria) >= 4 else '18px'
    return f'''  <div style="display:flex;flex-direction:column;gap:30px;">
    <div>
      <div class="badge badge-indigo" style="margin-bottom:18px;">今天我们学 · Learning Intention</div>
      <div class="display-md">{intention}</div>
    </div>
    <div>
      <div class="badge badge-teal" style="margin-bottom:18px;">我会 · Success Criteria</div>
      <div style="display:flex;flex-direction:column;gap:{gap};margin-top:4px;">
{rows}      </div>
    </div>
  </div>
'''


def b_qa(rows, badge=None, qs=None):
    out = []
    if badge:
        out.append(f'  <div style="margin-bottom:22px;"><span class="badge badge-indigo">{badge}</span></div>\n')
    out.append('  <div class="ex-list" style="gap:20px;">\n')
    for r in rows:
        who = r.get('who')
        tag = f'<span class="qa-tag {"a" if who == "A" else "q"}">{who}</span>' if who else ''
        if who:
            out.append(f'''    <div class="qa-row">{tag}
      <div class="qa-body"><div class="qa-pinyin">{r['py']}</div>
      <div class="qa-hanzi">{r['cn']}</div></div>
    </div>\n''')
        else:
            out.append(f'''    <div class="ex-row" style="gap:4px;">
      <div class="ex-pinyin">{r['py']}</div>
      <div class="ex-hanzi">{r['cn']}</div>
    </div>\n''')
    out.append('  </div>\n')
    if qs:
        li = ''.join(f'<li style="margin-bottom:12px;">{q}</li>' for q in qs)
        out.append(f'''  <div class="card" style="margin-top:22px;padding:26px 34px;">
    <div class="badge badge-madder" style="margin-bottom:16px;">听 · 读 · 问</div>
    <ol class="body-md" style="margin:0;padding-left:34px;color:var(--text-primary);">{li}</ol>
  </div>
''')
    return ''.join(out)


def b_task(badge, steps, cn_lines=None, ext=None, note=None):
    sh = ''.join(f'''    <div class="ex-row" style="flex-direction:row;gap:20px;align-items:baseline;">
      <span class="sc-num">{i}</span>
      <div class="body-lg" style="color:var(--text-primary);">{s}</div>
    </div>\n''' for i, s in enumerate(steps, 1))
    out = f'  <div style="margin-bottom:24px;"><span class="badge badge-olive">{badge}</span></div>\n'
    out += f'  <div class="ex-list" style="gap:18px;">\n{sh}  </div>\n'
    if cn_lines:
        lines = ''.join(f'      <div class="ex-row"><div class="ex-hanzi">{l}</div></div>\n' for l in cn_lines)
        out += ('  <div class="card" style="margin-top:24px;padding:24px 32px;">\n'
                '    <div class="ex-list" style="gap:10px;">\n' + lines + '    </div>\n  </div>\n')
    if note:
        nsub = f'<span class="note-sub">{note["sub"]}</span>' if note.get('sub') else ''
        out += f'''  <div class="note-box" style="margin-top:4px;">
    <span class="note-icon">!</span>
    <span><span class="note-text">{note['text']}</span>{nsub}</span>
  </div>
'''
    if ext:
        out += '  <div style="margin-top:20px;">\n' + b_ext(ext) + '  </div>\n'
    return out


def b_plenary(criteria, exit_text, exit_cn, preview):
    rows = ''.join(f'''      <div class="sc-row">
        <span class="sc-num">{i}</span>
        <span class="sc-text">{c}</span>
      </div>\n''' for i, c in enumerate(criteria, 1))
    return f'''  <div class="badge badge-teal" style="margin-bottom:20px;">我做到了吗？ 👍 / 😐 / 👎</div>
  <div style="display:flex;flex-direction:column;gap:14px;">
{rows}  </div>
  <div class="note-box" style="margin-top:28px;">
    <span class="note-icon">✎</span>
    <span><span class="note-text">出门条 · {exit_text}</span><span class="note-sub">{exit_cn}</span></span>
  </div>
  <div class="tip-box" style="margin-top:16px;">
    <span class="tip-icon">→</span>
    <span><span class="tip-text">下节课 · {preview}</span></span>
  </div>
'''


def b_preview(hanzi, en, lines):
    li = ''.join(f'      <div class="ex-row"><div class="ex-hanzi">{l}</div></div>\n' for l in lines)
    return f'''  <div style="display:flex;flex-direction:column;align-items:center;gap:28px;">
    <div class="hanzi-hero">{hanzi}</div>
    <div class="display-md">{en}</div>
    <div class="card" style="padding:30px 44px;">
      <div class="ex-list" style="gap:14px;">
{li}      </div>
    </div>
  </div>
'''


# ══════════════════════════════════════════════════════════════════
#  The eight decks
# ══════════════════════════════════════════════════════════════════
#  Each S(...) is one slide: file, nav label, header section, inner html.

def S(name, label, section, inner, style='', dense=False, foot=None):
    return dict(name=name, label=label, section=section, inner=inner,
                style=style, dense=dense, foot=foot)


META = ('<span>Year 7 Chinese</span><span class="s"></span><span>50 分钟</span>'
        '<span class="s"></span><span>Mixed</span><span class="s"></span><span>课本 {p}</span>')


def lesson1():
    s = []
    s.append(S('01-title', 'Title · 喜欢 + 黑白黄', 'Title',
               b_title(1, '', '喜欢<span class="dot">·</span>黑色',
                       'Like · Black · White · Yellow',
                       META.format(p='p.96'), '喜欢'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 交通工具 (0–8 min)', 'Review · 复习',
               b_cards([('校车', 'xiàochē'), ('火车', 'huǒchē'), ('汽车', 'qìchē'),
                        ('出租车', 'chūzūchē'), ('地铁', 'dìtiě'), ('电车', 'diànchē'),
                        ('走路', 'zǒulù'), ('开车', 'kāichē')], cols=4,
                       caption='上节课 — 你怎么上学？看到图就说', pinyin=True)
               + '  <div style="display:flex;align-items:center;gap:28px;margin-top:40px;justify-content:center;">\n'
                 '    <span class="formula-box">我 <span class="op">+</span> 坐 <span class="op">+</span> '
                 '<span class="slot">车</span> <span class="op">+</span> 上学。</span>\n'
                 '    <span class="body-lg">我坐校车上学。　我爸爸开车上班。</span>\n  </div>\n'))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们学怎么说谁喜欢什么颜色。', [
                   dict(cn='我会说三个颜色', en='I can say three colours — 黑色、白色、黄色'),
                   dict(cn='我会用「喜欢」说谁喜欢什么', en='I can use 喜欢 to say what someone likes — 我爸爸喜欢黑色'),
                   dict(cn='我会写「喜」和「色」', en='I can write 喜 and 色 with the correct stroke order'),
               ])))
    s.append(S('04-vocab-a1', 'I Do · 生词 1 · 喜欢 · 黑色', 'I Do · 生词 · 第一组',
               b_words([dict(hanzi='喜欢', pinyin='xǐhuan', english='like'),
                        dict(hanzi='黑色', pinyin='hēisè', english='black',
                             clue='每个颜色都有 <b>色</b> — 黑 alone is not a colour word')])))
    s.append(S('05-vocab-b1', 'I Do · 例句 1 · 喜欢 · 黑色', 'I Do · 例句 · 第一组',
               b_examples([
                   dict(py='wǒ xǐhuan wǒ de lǎoshī', cn='我<span class="new">喜欢</span>我的老师。', en='I like my teacher.'),
                   dict(py='wǒ bàba xǐhuan hēisè', cn='我爸爸<span class="new">喜欢黑色</span>。', en='My dad likes black.'),
                   dict(py='wǒ xǐhuan hēisè，wǒ māma bù xǐhuan hēisè',
                        cn='我<span class="new">喜欢黑色</span>，我妈妈不<span class="new">喜欢黑色</span>。',
                        en="I like black, my mum doesn't."),
               ])))
    s.append(S('06-vocab-c1', 'I Do · 写一句 1', 'I Do · 写一句 · 第一组',
               b_write(['我喜欢<span class="blank">　　　</span>。'],
                       '在小白板上写一句。写完了举起来。',
                       dict(text='写两个人，一句话 — ', cn='我喜欢黑色，我爸爸不喜欢黑色。',
                            sub='Then add a third with 也: 我妈妈也喜欢黑色。'))))
    s.append(S('07-vocab-a2', 'I Do · 生词 2 · 白色 · 黄色', 'I Do · 生词 · 第二组',
               b_words([dict(hanzi='白色', pinyin='báisè', english='white'),
                        dict(hanzi='黄色', pinyin='huángsè', english='yellow')])))
    s.append(S('08-vocab-b2', 'I Do · 例句 2 · 白色 · 黄色', 'I Do · 例句 · 第二组',
               b_examples([
                   dict(py='wǒ jiějie xǐhuan báisè', cn='我姐姐喜欢<span class="new">白色</span>。', en='My older sister likes white.'),
                   dict(py='wǒ mèimei xǐhuan huángsè', cn='我妹妹喜欢<span class="new">黄色</span>。', en='My younger sister likes yellow.'),
                   dict(py='wǒ jiějie xǐhuan báisè，wǒ mèimei xǐhuan huángsè',
                        cn='我姐姐喜欢<span class="new">白色</span>，我妹妹喜欢<span class="new">黄色</span>。',
                        en='My sister likes white, my little sister likes yellow.'),
               ])))
    s.append(S('09-vocab-c2', 'I Do · 写一句 2', 'I Do · 写一句 · 第二组',
               b_write(['我<span class="blank">　　　</span>喜欢<span class="blank">　　　</span>。'],
                       '在小白板上写一句。60 秒。',
                       dict(text='写三个人，一句话，其中一个人用「不」 — ',
                            cn='我姐姐喜欢白色，我妹妹喜欢黄色，我不喜欢黄色。',
                            sub='Cover the board first — no word bank.'))))
    s.append(S('10-board', 'I Do · 今天的四个词 · Summary Board', 'I Do · 词汇总览',
               b_cards(['喜欢', '黑色', '白色', '黄色'], cols=4,
                       caption='只有汉字和图 — 没有拼音，没有英文')))
    s.append(S('11-pattern', 'I Do · 句型 · 人 + 喜欢 + 颜色', 'I Do · 句型', dense=True,
               inner=b_pattern('<span class="slot">人</span> <span class="op">+</span> 喜欢 <span class="op">+</span> <span class="slot">颜色</span>。', [
                   dict(py='wǒ xǐhuan hēisè', cn='我喜欢黑色。', en='I like black.'),
                   dict(py='wǒ bàba xǐhuan báisè', cn='我爸爸喜欢白色。', en='My dad likes white.'),
                   dict(py='wǒ māma bù xǐhuan huángsè', cn='我妈妈不喜欢黄色。', en="My mum doesn't like yellow."),
                   dict(py='wǒ gēge xǐhuan hēisè，wǒ jiějie xǐhuan báisè，wǒ bù xǐhuan báisè',
                        cn='我哥哥喜欢黑色，我姐姐喜欢白色，[我不喜欢白色]。', hard=True,
                        en="My brother likes black, my sister likes white — I don't like white."),
               ], note=dict(text='「喜欢」的后面直接放颜色，中间什么都不要。',
                            sub='✗ 我黑色喜欢　✓ 我喜欢黑色'), note_icon='喜')))
    s.append(S('12-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '每个颜色后面都有一个字，是什么？会的举手。',
                   '怎么说 <b>my dad likes yellow</b>？写在小白板上。',
                   '这句对不对？ <span class="cn">我黑色喜欢。</span>',
               ], errors=[('我黑色喜欢。', '我喜欢黑色。'), ('我妈妈喜欢黄。', '我妈妈喜欢黄色。')])))
    s.append(S('13-text1', 'I Do · 课文一 · Text 1 上半 (CD T60)', 'I Do · 课文一',
               b_qa([
                   dict(py='wǒ bàba xǐhuan hēisè hé báisè', cn='我爸爸喜欢黑色和白色。'),
                   dict(py='wǒ māma xǐhuan huángsè', cn='我妈妈喜欢黄色。'),
               ], badge='CD T60 · 课本 p.96', qs=[
                   'What colour does mum like?', '爸爸喜欢几个颜色？',
                   '「和」以前学过 — 我家有三口人：爸爸、妈妈和我。',
               ])))
    s.append(S('14-act1', 'We Do · 活动一 · 我家的颜色 (7 min)', 'We Do · 活动一 (20–27)',
               b_task('活动一 · 我家的颜色 · 7 分钟', [
                   '写四句话，一个人一句 — 真的家人或者自己编的都可以。',
                   '四句话里，三个颜色都要用到，至少一次。',
                   '其中一句一定要用「不」。',
               ], cn_lines=['我爸爸喜欢黑色。', '我妈妈不喜欢白色。'],
                   ext=dict(text='写成一段话，不要分开的四句 — ',
                            cn='我喜欢黑色，我爸爸也喜欢黑色，我妈妈不喜欢黑色，她喜欢黄色。',
                            sub='Then read it to the class with the board covered.'))))
    s.append(S('15-act2', 'You Do · 活动二 · 笔顺 + 涂颜色 (9 min)', 'You Do · 活动二 (27–36)',
               b_task('活动二 · 练习本 pp.135–136 · 9 分钟', [
                   '练习本 Ex.2 — 按笔顺抄写：喜 欢 黑 色 白 黄。',
                   '练习本 Ex.3 第 1、3、4 格 — 用黑色、白色、黄色画一个小图，下面写汉字。',
               ], note=dict(text='「黑」下面的四点 <b>灬</b> 就是「火」，写扁了。',
                            sub='That radical comes back in Lesson 3 — 炒 has it on the left.'),
                   ext=dict(text='每个字旁边默写拼音和声调，再写一个你已经学过、下面也有「灬」的字 — ',
                            cn='点',
                            sub='Say what 黑 and 点 have in common.'))))
    s.append(S('16-game', 'Game · 抢字卡 Slap the Character (7 min)', 'Game · 抢字卡 (36–43)',
               b_task('游戏 · 抢字卡 · 7 分钟', [
                   '两队，每队一个人上来。黑板上八张卡片。',
                   '老师说中文，先拍到的得一分。',
                   '轮流上来，每个人都要玩到。',
               ], cn_lines=['喜欢　黑色　白色　黄色', '校车　火车　地铁　走路'],
                   ext=dict(text='老师说一整句 — ', cn='我爸爸喜欢白色。',
                            sub='The player slaps only the colour. Then reverse it: teacher says the English, player must say the Chinese before slapping.'))))
    s.append(S('17-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会说三个颜色：黑色、白色、黄色',
                          '我会用「喜欢」说谁喜欢什么颜色',
                          '我会写「喜」和「色」'],
                         'Translate into Chinese — <b>My mum likes black.</b>',
                         '写在小白板上，出门的时候给老师看。',
                         '三个新颜色，完整的课文一，还有把两个颜色连起来的那个字。')))
    s.append(S('18-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('和', 'Next — three more colours, and how to join two of them',
                               ['蓝色　红色　粉红色',
                                '我爸爸喜欢黑色<span class="new">和</span>白色。'])))
    return s


def lesson2():
    s = []
    s.append(S('01-title', 'Title · 蓝红粉 + 和', 'Title',
               b_title(2, '', '蓝色<span class="dot">·</span>红色<span class="dot">·</span>和',
                       'Blue · Red · Pink · and joining two colours',
                       META.format(p='p.96'), '蓝色'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 喜欢 + 黑白黄 (0–8 min)', 'Review · 复习',
               b_cards(['喜欢', '黑色', '白色', '黄色'], cols=4,
                       caption='上节课 — 看到就说，不要看拼音')
               + '  <div style="display:flex;flex-direction:column;gap:16px;margin-top:40px;">\n'
                 '    <div class="error-pair"><span class="error-wrong">我白色喜欢。</span>'
                 '<span class="error-arrow">&rarr;</span>'
                 '<span class="error-correct">我喜欢白色。</span></div>\n'
                 '    <div class="error-pair"><span class="error-wrong">我妈妈喜欢黄。</span>'
                 '<span class="error-arrow">&rarr;</span>'
                 '<span class="error-correct">我妈妈喜欢黄色。</span></div>\n  </div>\n'))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们学怎么说一个人喜欢两个颜色。', [
                   dict(cn='我会再说三个颜色', en='I can say three more colours — 蓝色、红色、粉红色'),
                   dict(cn='我会用「和」把两个颜色连起来', en='I can join two colours with 和 — 我爸爸喜欢黑色和白色'),
                   dict(cn='我看得懂课文一', en='I can understand Text 1 and say which colour each family member likes'),
               ])))
    s.append(S('04-vocab-a1', 'I Do · 生词 1 · 蓝色 · 红色', 'I Do · 生词 · 第一组',
               b_words([dict(hanzi='蓝色', pinyin='lánsè', english='blue'),
                        dict(hanzi='红色', pinyin='hóngsè', english='red')])))
    s.append(S('05-vocab-b1', 'I Do · 例句 1 · 蓝色 · 红色', 'I Do · 例句 · 第一组',
               b_examples([
                   dict(py='wǒ gēge xǐhuan lánsè', cn='我哥哥喜欢<span class="new">蓝色</span>。', en='My older brother likes blue.'),
                   dict(py='wǒ jiějie xǐhuan hóngsè', cn='我姐姐喜欢<span class="new">红色</span>。', en='My older sister likes red.'),
                   dict(py='wǒ xǐhuan lánsè，wǒ bù xǐhuan hóngsè',
                        cn='我喜欢<span class="new">蓝色</span>，我不喜欢<span class="new">红色</span>。',
                        en="I like blue, I don't like red."),
               ])))
    s.append(S('06-vocab-c1', 'I Do · 写一句 1', 'I Do · 写一句 · 第一组',
               b_write(['我喜欢<span class="blank">　　　</span>，我不喜欢<span class="blank">　　　</span>。'],
                       '在小白板上写一句。60 秒。',
                       dict(text='写两个人，意见不一样 — ',
                            cn='我哥哥喜欢蓝色，我妈妈不喜欢蓝色，她喜欢红色。',
                            sub='No board — cover it first.'))))
    s.append(S('07-vocab-a2', 'I Do · 生词 2 · 粉红色 · 和', 'I Do · 生词 · 第二组',
               b_words([dict(hanzi='粉红色', pinyin='fěnhóngsè', english='pink',
                             clue='<b>粉</b> = powder　+　红色 — powder-red. 只有「粉」是新字'),
                        dict(hanzi='和', pinyin='hé', english='and')])))
    s.append(S('08-vocab-b2', 'I Do · 例句 2 · 粉红色 · 和', 'I Do · 例句 · 第二组',
               b_examples([
                   dict(py='wǒ xǐhuan fěnhóngsè', cn='我喜欢<span class="new">粉红色</span>。', en='I like pink.'),
                   dict(py='wǒ māma xǐhuan hóngsè hé fěnhóngsè',
                        cn='我妈妈喜欢红色<span class="new">和粉红色</span>。', en='My mum likes red and pink.'),
                   dict(py='wǒ bàba xǐhuan hēisè hé báisè，wǒ xǐhuan fěnhóngsè',
                        cn='我爸爸喜欢黑色<span class="new">和</span>白色，我喜欢<span class="new">粉红色</span>。',
                        en='My dad likes black and white, I like pink.'),
               ])))
    s.append(S('09-vocab-c2', 'I Do · 写一句 2', 'I Do · 写一句 · 第二组',
               b_write(['我<span class="blank">　　　</span>喜欢<span class="blank">　　　</span>和<span class="blank">　　　</span>。'],
                       '在小白板上写一句。60 秒。',
                       dict(text='一句话，三个人，四个颜色，「和」用两次，再加一个「也」 — ',
                            cn='我爸爸喜欢黑色和白色，我哥哥也喜欢蓝色和红色。'))))
    s.append(S('10-recall', 'I Do · 认字 · 课文一的六个颜色', 'I Do · 认字',
               b_cards(TEXT1_6, cols=6, caption='读出来 — 没有拼音，没有英文，没有颜色块')))
    s.append(S('11-pattern', 'I Do · 句型 · 和', 'I Do · 句型', dense=True,
               inner=b_pattern('<span class="slot">人</span> <span class="op">+</span> 喜欢 <span class="op">+</span> '
                               '<span class="slot">X色</span> <span class="op">+</span> 和 <span class="op">+</span> '
                               '<span class="slot">Y色</span>。', [
                   dict(py='wǒ xǐhuan hóngsè hé lánsè', cn='我喜欢红色和蓝色。', en='I like red and blue.'),
                   dict(py='wǒ māma xǐhuan huángsè hé fěnhóngsè', cn='我妈妈喜欢黄色和粉红色。', en='My mum likes yellow and pink.'),
                   dict(py='wǒ gēge bù xǐhuan hēisè hé báisè', cn='我哥哥不喜欢黑色和白色。', en="My brother doesn't like black and white."),
                   dict(py='wǒ bàba xǐhuan hēisè hé báisè，wǒ māma xǐhuan huángsè，wǒ xǐhuan fěnhóngsè',
                        cn='我爸爸喜欢黑色和白色，[我妈妈喜欢黄色，我喜欢粉红色]。', hard=True,
                        en='Three people, one sentence — only the first needs 和.'),
               ], note=dict(text='「和」连两个东西，放在中间，不放在最后。',
                            sub='✗ 我喜欢红色蓝色　✗ 我喜欢红色蓝色和　✓ 我喜欢红色和蓝色'), note_icon='和')))
    s.append(S('12-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '「和」可以连几个东西？用手指给我看。',
                   '怎么说 <b>I like red and blue</b>？写在小白板上。',
                   '这句少了什么？ <span class="cn">我喜欢红色蓝色。</span>',
               ], errors=[('我喜欢红色蓝色。', '我喜欢红色和蓝色。')])))
    s.append(S('13-text1', 'I Do · 课文一 · Text 1 全文 (CD T60)', 'I Do · 课文一', dense=True,
               inner=b_qa([
                   dict(py='wǒ bàba xǐhuan hēisè hé báisè', cn='我爸爸喜欢黑色和白色。'),
                   dict(py='wǒ māma xǐhuan huángsè', cn='我妈妈喜欢黄色。'),
                   dict(py='wǒ gēge xǐhuan lánsè', cn='我哥哥喜欢蓝色。'),
                   dict(py='wǒ jiějie xǐhuan hóngsè', cn='我姐姐喜欢红色。'),
                   dict(py='wǒ xǐhuan fěnhóngsè', cn='我喜欢粉红色。'),
               ], badge='CD T60 · 课本 p.96', qs=[
                   '谁喜欢红色？　爸爸喜欢几个颜色？',
               ])))
    s.append(S('14-act1', 'We Do · 活动一 · 我家的颜色 (7 min)', 'We Do · 活动一 (20–27)',
               b_task('活动一 · 五个人，六个颜色 · 7 分钟', [
                   '写五句话，一个家人一句。',
                   '六个颜色都要用到 — 五句话装六个颜色，所以有人要拿两个。',
                   '至少两句要用「和」。',
               ], cn_lines=['我爸爸喜欢黑色和白色。', '我妈妈喜欢黄色。'],
                   ext=dict(text='写成一段话，不是五句 — 用「也」和一个「不」，最后写你自己 — ',
                            cn='我爸爸喜欢黑色和白色，我哥哥也喜欢黑色，我妈妈不喜欢黑色，她喜欢黄色和粉红色，我喜欢蓝色和红色。',
                            sub='Deliver it to the class with the board covered.'))))
    s.append(S('15-act2', 'You Do · 活动二 · 听力 T62 (5 min)', 'You Do · 活动二 (27–32)',
               b_task('活动二 · 课本 p.98 Ex.4 · CD T62 · 5 分钟', [
                   '听两遍，把六个家人和 A–F 的颜色连起来。',
                   '全班一起对答案，一题一举手。',
               ], ext=dict(text='合上书，把听到的默写成完整的句子 — ',
                           cn='爸爸喜欢……　妈妈喜欢……',
                           sub='Then invent two more items in the same style for the teacher to read to the class.'))))
    s.append(S('16-act3', 'You Do · 活动三 · 笔顺 + 涂颜色 (4 min)', 'You Do · 活动三 (32–36)',
               b_task('活动三 · 练习本 pp.135–136 · 4 分钟', [
                   '练习本 Ex.2 — 按笔顺抄写：蓝 红 粉。课文一的字就全了。',
                   '练习本 Ex.3 第 2、5、6 格 — 红色、蓝色、粉红色，画图写汉字。',
               ], note=dict(text='「蓝」上面是 <b>艹</b>（草）— 蓝色本来是植物染的。十三笔。',
                            sub='「红」快得多 — 左边 纟, silk.'),
                   ext=dict(text='不画图，改做练习本 p.138 Ex.8 — 四个格子，每格两三个颜色，下面写一整句 — ',
                            cn='我喜欢黑色和白色。'))))
    s.append(S('17-game', 'Game · 传声筒 Telephone (7 min)', 'Game · 传声筒 (36–43)',
               b_task('游戏 · 传声筒 · 7 分钟', [
                   '一排五六个人。老师悄悄告诉第一个人，一个传一个。',
                   '最后一个人大声说出来。三轮，一轮比一轮长。',
               ], cn_lines=['粉红色', '蓝色和红色', '我姐姐喜欢粉红色。'],
                   note=dict(text='难点是三个音的「粉红色」fěn-hóng-sè，还有 蓝/红 的声调。',
                             sub='That is where the chain usually breaks.'),
                   ext=dict(text='让说得好的同学自己编一句带「和」的话开头，最后一个人不说出来，',
                            cn='上黑板写汉字。'))))
    s.append(S('18-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会说蓝色、红色、粉红色',
                          '我会用「和」连两个颜色',
                          '我看得懂课文一'],
                         'Translate into Chinese — <b>My older brother likes blue and pink.</b>',
                         '写在小白板上。',
                         '颜色放到东西前面 — 黑色的火车、黄色的校车。中间有一个小字。')))
    s.append(S('19-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('的', 'Next — putting a colour in front of a thing',
                               ['黑色<span class="new">的</span>火车　黄色<span class="new">的</span>校车',
                                '少了「的」就错了。'])))
    return s


def lesson3():
    s = []
    s.append(S('01-title', 'Title · 颜色 + 的 + 名词', 'Title',
               b_title(3, '', '的',
                       'Colour + 的 + noun — 黑色的火车',
                       META.format(p='p.97'), '蓝色'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 六个颜色 + 交通工具 (0–8 min)', 'Review · 复习',
               b_cards(TEXT1_6, cols=6, caption='一边是颜色……')
               + b_cards([('校车', 'xiàochē'), ('火车', 'huǒchē'), ('出租车', 'chūzūchē'),
                          ('公共汽车', 'gōnggòng qìchē'), ('地铁', 'dìtiě'), ('电车', 'diànchē')],
                         cols=6, caption='……一边是车。今天把它们连起来。', pinyin=True)))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们学怎么用颜色说一个东西。', [
                   dict(cn='我会用「的」把颜色放在东西前面', en='I can put a colour in front of a noun with 的 — 黑色的火车'),
                   dict(cn='我会把英文的短语翻译成中文', en='I can translate colour-and-object phrases into Chinese'),
                   dict(cn='我会写 疒、火、爫 三个部首', en='I can write the radicals 疒 火 爫 and name a character for each'),
               ])))
    s.append(S('04-pattern', 'I Do · 句型 · 颜色 + 的 + 名词', 'I Do · 句型', dense=True,
               inner=b_pattern('<span class="slot">颜色</span> <span class="op">+</span> 的 <span class="op">+</span> '
                               '<span class="slot">东西</span>', [
                   dict(py='hēisè de huǒchē', cn='黑色的火车', en='a black train'),
                   dict(py='huángsè de xiàochē', cn='黄色的校车', en='a yellow school bus'),
                   dict(py='hóngsè de chūzūchē', cn='红色的出租车', en='a red taxi'),
                   dict(py='wǒ bàba xǐhuan báisè de qìchē，wǒ māma měitiān zuò lánsè de diànchē shàngbān',
                        cn='我爸爸喜欢白色的汽车，[我妈妈每天坐蓝色的电车上班]。', hard=True,
                        en='Two clauses, two 的 phrases, and the whole Unit 4 transport frame inside.'),
               ], note=dict(text='颜色 + 的 + 东西 ✓　　颜色 + 东西 ✗',
                            sub='English has nothing in the middle. Chinese has to have 的. 这一课最容易错的就是它。'))))
    s.append(S('05-no-new-words', 'I Do · 今天没有新词 · 只有句型', 'I Do · 说明', style=STYLE_CENTRE,
               inner='''  <div style="display:flex;flex-direction:column;align-items:center;gap:34px;text-align:center;">
    <div class="hanzi-hero">的</div>
    <div class="display-md">今天没有新的颜色。</div>
    <div class="body-lg" style="max-width:1100px;color:var(--text-secondary);">
      每个字你都学过了 — 六个颜色，还有四单元的车。新的只有中间这一个字。</div>
    <div class="formula-box">黑色 <span class="op">+</span> 的 <span class="op">+</span> 火车</div>
  </div>
'''))
    s.append(S('06-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '「的」放在哪里？指黑板。',
                   '怎么说 <b>the yellow school bus</b>？写在小白板上。',
                   '这句对不对？ <span class="cn">火车黑色的。</span>',
                   '怎么说 <b>my dad likes the white taxi</b>？',
               ], errors=[('火车黑色的。', '黑色的火车'), ('红色出租车', '红色的出租车')])))
    s.append(S('07-act1', 'We Do · 活动一 · 七辆车 (8 min)', 'We Do · 活动一 (20–28)',
               b_task('活动一 · 课本 p.97 Ex.1 · 8 分钟', [
                   '全班一起 — 老师指图，大家一起说：黑色的火车。',
                   '两个人一组 — 一个指，一个说，然后换。',
                   '写到本子上，七个短语。六个颜色都要用到，至少一次。',
               ], cn_lines=['黑色的火车　黄色的校车　红色的出租车'],
                   ext=dict(text='每个短语加一个人、一个四单元的动词，写四句 — ',
                            cn='我弟弟每天坐黄色的校车上学。我妈妈坐蓝色的地铁上班。',
                            sub='Then say all four aloud with the board covered.'))))
    s.append(S('08-radicals', 'I Do · 部首 · 第一组 (疒 火 爫)', 'I Do · 部首',
               b_cards([], cols=3)
               + '''  <div class="grid-3">
    <div class="vocab-card highlight"><div class="vc-hanzi">疒</div><div class="vc-pinyin">disease</div><div class="vc-english">病</div></div>
    <div class="vocab-card highlight"><div class="vc-hanzi">火</div><div class="vc-pinyin">fire</div><div class="vc-english">炒</div></div>
    <div class="vocab-card highlight"><div class="vc-hanzi">爫</div><div class="vc-pinyin">claw</div><div class="vc-english">爱</div></div>
  </div>
  <div class="info-box" style="margin-top:32px;">
    <span class="info-icon">黑</span>
    <span><span class="info-text">「黑」下面的四点 <b>灬</b> 就是「火」，写扁了。</span>
    <span class="info-sub">第一课抄过「黑」了 — 先在自己的本子上把 炒 里的火和 黑 里的灬圈出来，再开始抄。</span></span>
  </div>
'''))
    s.append(S('09-act2', 'You Do · 活动二 · 部首 + 翻译 (8 min)', 'You Do · 活动二 (28–36)',
               b_task('活动二 · 练习本 p.134 / p.138 / p.139 · 8 分钟', [
                   '练习本 Ex.1 — 按笔顺抄 疒、火、爫。',
                   '练习本 Ex.9 第 1–3 题 — 写出 炒、爱、病 的部首。',
                   '练习本 Ex.10 — 六个短语翻译成中文。第一个已经给了。',
               ], cn_lines=['black taxi　→　黑色的出租车', 'blue car　·　red public bus　·　yellow school bus　·　pink watch　·　white bed'],
                   note=dict(text='第 5、6 题要用 <b>手表</b> 和 <b>床</b>。',
                             sub='They go on the board as recognition words — the exercise is asking for the colour and the 的, not for two new nouns.'),
                   ext=dict(text='自己再写四个「颜色的东西」，名词可以是一册书里任何一个，再把其中两个写成句子 — ',
                            cn='我姐姐七点坐红色的公共汽车上学。'))))
    s.append(S('10-game', 'Game · 排句子 Sentence Jumble (7 min)', 'Game · 排句子 (36–43)',
               b_task('游戏 · 排句子 · 7 分钟', [
                   '四个人一组，每组一套卡片。',
                   '比谁先排对，排完举手，老师来看。',
                   '三轮，每轮换一套。',
               ], cn_lines=['我弟弟 · 每天 · 坐 · 黄色的 · 校车 · 上学'],
                   ext=dict(text='第四轮偷偷把一组的「的」卡拿走，看他们发不发现 — ',
                            cn='少了哪个字？放在哪里？为什么？',
                            sub='Then 90 seconds to build the longest correct sentence from a shared pool of leftover cards.'))))
    s.append(S('11-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会用「的」把颜色放在东西前面',
                          '我会翻译「颜色 + 东西」',
                          '我会写 疒、火、爫'],
                         'Two items — <b>the red taxi</b>, then <b>My mum likes the white car.</b>',
                         '写在小白板上。两题都要有「的」。',
                         '怎么问别人「你喜欢什么颜色？」，还有四个新颜色。')))
    s.append(S('12-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('什么', 'Next — asking the question',
                               ['你喜欢<span class="new">什么颜色</span>？',
                                '颜色　橙色　紫色　棕色'])))
    return s


def lesson4():
    s = []
    s.append(S('01-title', 'Title · 你喜欢什么颜色？', 'Title',
               b_title(4, '', '你喜欢<span class="dot">什么</span>颜色？',
                       'Colour · Orange · Purple · Brown',
                       META.format(p='p.100'), '颜色'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 的 (0–8 min)', 'Review · 复习',
               b_caption('上节课 — 写在小白板上，一起举起来')
               + '''  <div class="ex-list" style="gap:26px;">
    <div class="ex-row"><div class="ex-hanzi">the black train　·　the pink bus　·　the white taxi</div></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:16px;margin-top:44px;">
    <div class="error-pair"><span class="error-wrong">我喜欢红色出租车。</span><span class="error-arrow">&rarr;</span><span class="error-correct">我喜欢红色的出租车。</span></div>
    <div class="error-pair"><span class="error-wrong">校车黄色的。</span><span class="error-arrow">&rarr;</span><span class="error-correct">黄色的校车</span></div>
  </div>
'''))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们学怎么问别人喜欢什么颜色。', [
                   dict(cn='我会问「你喜欢什么颜色？」', en='I can ask 你喜欢什么颜色？and answer it'),
                   dict(cn='我会说橙色、紫色、棕色', en='I can say 橙色、紫色、棕色'),
                   dict(cn='我会写「颜」和「橙」', en='I can write 颜 and 橙 with the correct stroke order'),
               ])))
    s.append(S('04-vocab-a1', 'I Do · 生词 1 · 颜色 · 橙色', 'I Do · 生词 · 第一组',
               b_words([dict(hanzi='颜色', pinyin='yánsè', english='colour',
                             clue='这是「颜色」这个类 — <b>不是</b>一个颜色'),
                        dict(hanzi='橙色', pinyin='chéngsè', english='orange')])))
    s.append(S('05-vocab-b1', 'I Do · 例句 1 · 颜色 · 橙色', 'I Do · 例句 · 第一组',
               b_examples([
                   dict(py='nǐ xǐhuan shénme yánsè', cn='你喜欢什么<span class="new">颜色</span>？', en='What colour do you like?'),
                   dict(py='wǒ xǐhuan chéngsè', cn='我喜欢<span class="new">橙色</span>。', en='I like orange.'),
                   dict(py='nǐ xǐhuan shénme yánsè — wǒ xǐhuan chéngsè hé hóngsè',
                        cn='A: 你喜欢什么<span class="new">颜色</span>？ B: 我喜欢<span class="new">橙色</span>和红色。',
                        en='Both words, one exchange.'),
               ])))
    s.append(S('06-vocab-c1', 'I Do · 写一句 1', 'I Do · 写一句 · 第一组',
               b_write(['你喜欢什么颜色？',
                        '我喜欢<span class="blank">　　　</span>和<span class="blank">　　　</span>。'],
                       '先写问题，再写自己的答案。60 秒。',
                       dict(text='一次写三个人 — ',
                            cn='我喜欢橙色，我爸爸喜欢黑色和白色，我妈妈不喜欢橙色。',
                            sub='Then ask the teacher the question in Chinese and write down the answer.'))))
    s.append(S('07-vocab-a2', 'I Do · 生词 2 · 紫色 · 棕色', 'I Do · 生词 · 第二组',
               b_words([dict(hanzi='紫色', pinyin='zǐsè', english='purple'),
                        dict(hanzi='棕色', pinyin='zōngsè', english='brown')])))
    s.append(S('08-vocab-b2', 'I Do · 例句 2 · 紫色 · 棕色', 'I Do · 例句 · 第二组',
               b_examples([
                   dict(py='wǒ jiějie xǐhuan zǐsè', cn='我姐姐喜欢<span class="new">紫色</span>。', en='My older sister likes purple.'),
                   dict(py='wǒ bù xǐhuan zōngsè', cn='我不喜欢<span class="new">棕色</span>。', en="I don't like brown."),
                   dict(py='wǒ māma xǐhuan zǐsè hé zōngsè',
                        cn='我妈妈喜欢<span class="new">紫色</span>和<span class="new">棕色</span>。', en='My mum likes purple and brown.'),
               ])))
    s.append(S('09-vocab-c2', 'I Do · 写一句 2', 'I Do · 写一句 · 第二组',
               b_write(['我<span class="blank">　　　</span>喜欢<span class="blank">　　　</span>色。'],
                       '在小白板上写一句。60 秒。',
                       dict(text='问旁边的同学「你喜欢什么颜色？」，把他的答案写成一句话 — ',
                            cn='他喜欢紫色和蓝色。',
                            sub='Then report it to the class without looking at what you wrote.'))))
    s.append(S('10-recall', 'I Do · 认字 · 十个颜色 + 颜色', 'I Do · 认字',
               b_cards(ALL_11[:9] + ['颜色'], cols=5,
                       caption='读出来 — 最后一个不是颜色，是什么？为什么？')))
    s.append(S('11-pattern', 'I Do · 句型 · 你喜欢什么颜色？', 'I Do · 句型', dense=True,
               inner=b_pattern('你 <span class="op">+</span> 喜欢 <span class="op">+</span> '
                               '<span class="slot">什么颜色</span>？', [
                   dict(py='nǐ xǐhuan shénme yánsè — wǒ xǐhuan chéngsè',
                        cn='你喜欢什么颜色？ — 我喜欢橙色。', en='What colour do you like? — I like orange.'),
                   dict(py='nǐ māma xǐhuan shénme yánsè — tā xǐhuan zǐsè',
                        cn='你妈妈喜欢什么颜色？ — 她喜欢紫色。', en='What colour does your mum like? — She likes purple.'),
                   dict(py='nǐ gēge xǐhuan shénme yánsè — tā xǐhuan zōngsè hé hēisè',
                        cn='你哥哥喜欢什么颜色？ — 他喜欢棕色和黑色。', en='— He likes brown and black.'),
                   dict(py='nǐ měitiān zuò shénme yánsè de xiàochē shàngxué',
                        cn='你每天坐[什么颜色的]校车上学？ — 我坐黄色的校车上学。', hard=True,
                        en='什么颜色 inside a 的 phrase, carrying the whole Unit 4 sentence.'),
               ], note=dict(text='「什么」放在答案的位置上。',
                            sub='✗ 什么颜色你喜欢？　✓ 你喜欢什么颜色？'),
                   note_icon='什')))
    s.append(S('12-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '「什么」在「喜欢」前面还是后面？',
                   '怎么问 <b>What colour does your dad like?</b> 写在小白板上。',
                   '这句对不对？ <span class="cn">什么颜色你喜欢？</span>',
               ], errors=[('什么颜色你喜欢？', '你喜欢什么颜色？')])))
    s.append(S('13-act1', 'We Do · 活动一 · 这是什么颜色？ (7 min)', 'We Do · 活动一 (20–27)',
               b_task('活动一 · 课本 p.98 Ex.3 · 7 分钟', [
                   '两个人一组，轮流 — A 指图问，B 回答。',
                   '葡萄、云、柠檬、蝴蝶结、兔子、橙子、灭火器。',
                   '草和灰的那几个留到下节课 — 那时候才有绿色和灰色。',
               ], cn_lines=['A: 这是什么颜色？　B: 紫色。'],
                   ext=dict(text='B 回答完再反问回去 — ',
                            cn='葡萄是紫色。你喜欢紫色吗？',
                            sub='A must answer, then name a different colour they prefer. Run the whole set as a conversation, not a naming drill.'))))
    s.append(S('14-act2', 'You Do · 活动二 · 笔顺 + 找不同 (9 min)', 'You Do · 活动二 (27–36)',
               b_task('活动二 · 练习本 p.141 / p.142 · 9 分钟', [
                   '练习本 Ex.15 — 按笔顺抄 颜、橙、紫、棕。绿和灰下节课。',
                   '练习本 Ex.16 — 六组词，圈出不一样的那个。',
               ], note=dict(text='「颜」十五笔，是这一课最难的字 — 左边 彦，右边 页。',
                            sub='「橙」左边是 <b>木</b> — 先有橙子这个水果，才有橙色。'),
                   ext=dict(text='不只是圈 — 其中两组用中文写出为什么 — ',
                            cn='火车、汽车是车，电话不是车。',
                            sub='Then build a seventh set of your own with two colours and one non-colour, and try it on a partner.'))))
    s.append(S('15-game', 'Game · 抢词卡 Slap the Board (7 min)', 'Game · 抢词卡 (36–43)',
               b_task('游戏 · 抢词卡 · 十个颜色 · 7 分钟', [
                   '分四组，每组一个人上来。黑板上十张颜色卡。',
                   '老师说一个颜色，最快拍对的得一分。',
                   '轮流上，每个人都要玩到。',
               ], ext=dict(text='老师不说颜色，改问「你喜欢什么颜色？」— 上来的人要先说一整句 ',
                           cn='我喜欢紫色。',
                           sub='…and only then slap the card they named. Wrong sentence, no point, even if the right card gets hit.'))))
    s.append(S('16-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会问「你喜欢什么颜色？」',
                          '我会说橙色、紫色、棕色',
                          '我会写「颜」和「橙」'],
                         'Write the question 你喜欢什么颜色？ then your own answer with two colours and 和.',
                         '问题和答案都要写。',
                         '最后两个颜色，课文二，还有怎么说「我不喜欢」和「我也不喜欢」。')))
    s.append(S('17-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('也', 'Next — saying no, and agreeing',
                               ['绿色　灰色',
                                '你喜欢灰色<span class="new">吗</span>？ — 不喜欢。 — 我<span class="new">也</span>不喜欢。'])))
    return s


def lesson5():
    s = []
    s.append(S('01-title', 'Title · 课文二 · 吗 / 也', 'Title',
               b_title(5, '', '绿色<span class="dot">·</span>灰色',
                       'Text 2 — 你喜欢灰色吗？ · 我也不喜欢',
                       META.format(p='p.100'), '绿色'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 你喜欢什么颜色？ (0–8 min)', 'Review · 复习',
               b_cards(ALL_11[:9], cols=5, caption='上节课的十个颜色 — 看到就说')
               + '''  <div style="display:flex;align-items:center;gap:28px;margin-top:40px;justify-content:center;">
    <span class="formula-box">你喜欢 <span class="slot">什么颜色</span>？</span>
    <span class="body-lg">两个人一组，问答，然后换人再问一次。</span>
  </div>
'''))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们学怎么问别人喜不喜欢一个颜色，还有怎么说「我也是」。', [
                   dict(cn='我会说绿色和灰色', en='I can say 绿色 and 灰色'),
                   dict(cn='我会回答「你喜欢灰色吗？」', en='I can answer 你喜欢灰色吗？with 喜欢。or 不喜欢。'),
                   dict(cn='我会用「也」说我跟他一样', en='I can agree with someone using 我也不喜欢'),
               ])))
    s.append(S('04-vocab-a1', 'I Do · 生词 · 绿色 · 灰色', 'I Do · 生词',
               b_words([dict(hanzi='绿色', pinyin='lǜsè', english='green',
                             clue='<b>lǜ</b> — 跟「女」一样的 ü，不是 "loo"'),
                        dict(hanzi='灰色', pinyin='huīsè', english='grey')])))
    s.append(S('05-vocab-b1', 'I Do · 例句 · 绿色 · 灰色', 'I Do · 例句',
               b_examples([
                   dict(py='wǒ xǐhuan lǜsè', cn='我喜欢<span class="new">绿色</span>。', en='I like green.'),
                   dict(py='wǒ bù xǐhuan huīsè', cn='我不喜欢<span class="new">灰色</span>。', en="I don't like grey."),
                   dict(py='wǒ gēge xǐhuan lǜsè，tā bù xǐhuan huīsè',
                        cn='我哥哥喜欢<span class="new">绿色</span>，他不喜欢<span class="new">灰色</span>。',
                        en="My brother likes green, he doesn't like grey."),
               ])))
    s.append(S('06-vocab-c1', 'I Do · 写一句', 'I Do · 写一句',
               b_write(['我喜欢<span class="blank">　　　</span>，我不喜欢<span class="blank">　　　</span>。'],
                       '在小白板上写一句。60 秒。',
                       dict(text='用「也」写两句，跟别人一样 — ',
                            cn='我不喜欢灰色，我姐姐也不喜欢灰色。',
                            sub='Then a third with 和 that gives one person two colours.'))))
    s.append(S('07-recall', 'I Do · 认字 · 十一个颜色', 'I Do · 认字',
               b_cards(ALL_11, cols=6,
                       caption='全部十一个 — 没有拼音。从这里开始只复习，不再加新的了')))
    s.append(S('08-pattern', 'I Do · 句型 · 吗 / 不喜欢 / 也', 'I Do · 句型', dense=True,
               inner=b_pattern('你喜欢 <span class="slot">X色</span> 吗？ <span class="op">→</span> '
                               '喜欢。 ／ 不喜欢。', [
                   dict(py='nǐ xǐhuan huīsè ma — bù xǐhuan', cn='你喜欢灰色吗？ — 不喜欢。', en="Do you like grey? — No."),
                   dict(py='nǐ xǐhuan lǜsè ma — xǐhuan', cn='你喜欢绿色吗？ — 喜欢。', en='Do you like green? — Yes.'),
                   dict(py='wǒ bù xǐhuan huīsè — wǒ yě bù xǐhuan', cn='我不喜欢灰色。 — 我也不喜欢。', en="I don't like grey. — I don't either."),
                   dict(py='nǐ māma xǐhuan zōngsè ma — bù xǐhuan，tā xǐhuan zǐsè hé lǜsè，wǒ yě xǐhuan zǐsè',
                        cn='你妈妈喜欢棕色吗？ — 不喜欢，[她喜欢紫色和绿色，我也喜欢紫色]。', hard=True,
                        en='A negative answer, a correction, and 也 agreeing with only part of it.'),
               ], note=dict(text='回答不用「是」— 把动词再说一遍：喜欢。／不喜欢。',
                            sub='「也」放在动词前面：✓ 我也不喜欢　✗ 我不喜欢也'),
                   note_icon='也')))
    s.append(S('09-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '「你喜欢灰色吗？」— 不喜欢的话怎么回答？<b>不是</b>「是」。',
                   '怎么说 <b>I don\'t like it either</b>？写在小白板上。',
                   '这句对不对？ <span class="cn">我不喜欢也。</span>',
               ], errors=[('你喜欢灰色吗？ — 不是。', '你喜欢灰色吗？ — 不喜欢。'),
                          ('我不喜欢也。', '我也不喜欢。')])))
    s.append(S('10-text2', 'I Do · 课文二 · Text 2 (CD T63)', 'I Do · 课文二', dense=True,
               inner=b_qa([
                   dict(who='A', py='nǐ xǐhuan shénme yánsè', cn='你喜欢什么颜色？'),
                   dict(who='B', py='wǒ xǐhuan chéngsè、zǐsè、zōngsè hé lǜsè', cn='我喜欢橙色、紫色、棕色和绿色。'),
                   dict(who='A', py='nǐ xǐhuan huīsè ma', cn='你喜欢灰色吗？'),
                   dict(who='B', py='bù xǐhuan', cn='不喜欢。'),
                   dict(who='A', py='wǒ yě bù xǐhuan', cn='我也不喜欢。'),
               ], badge='CD T63 · p.100 · 四个颜色中间是顿号「、」，最后一个才用「和」', qs=[
                   'B 喜欢几个颜色？　谁不喜欢灰色？',
               ])))
    s.append(S('11-act1', 'We Do · 活动一 · 课文二，换成自己的颜色 (7 min)', 'We Do · 活动一 (20–27)',
               b_task('活动一 · 两个人一组 · 7 分钟', [
                   '先花 60 秒补完课本 p.98 Ex.3 剩下的几个 — 草和灰的那些，上节课没词可用。',
                   '两个人一组，用自己的颜色演课文二 — 四个颜色用「、」和「和」，再问第五个颜色。',
                   '换角色再演一遍。',
                   '规定：两个人两遍加起来，十一个颜色都要说到。',
               ], cn_lines=['A: 你喜欢什么颜色？　B: 我喜欢……、……、……和……。',
                            'A: 你喜欢……吗？　B: 不喜欢。　A: 我也不喜欢。'],
                   ext=dict(text='演成三轮，每个人多加一个「也」或者「不」，最后一轮转述给全班 — ',
                            cn='他喜欢橙色和绿色，他不喜欢灰色，我也不喜欢灰色。',
                            sub='No script, no board.'))))
    s.append(S('12-act2', 'You Do · 活动二 · 听力 T64 + 写答案 (9 min)', 'You Do · 活动二 (27–36)',
               b_task('活动二 · 课本 p.103 / 练习本 p.143 / p.141 · 9 分钟', [
                   '课本 Ex.10 (CD T64) — 六个人，听两遍，勾出每个人喜欢的颜色。',
                   '练习本 Ex.19 第 1–4 题 — 写完整的句子。第 1 题是「吗」的问句，小心不要写「是」。',
                   '练习本 Ex.15 — 补完绿、灰的笔顺。做完的再做 Ex.19 第 5、6 题。',
               ], ext=dict(text='听完以后用「也」写三句 — ',
                           cn='王月喜欢红色，小文也喜欢红色。',
                           sub='Then one sentence about someone in the recording who agrees with you.'))))
    s.append(S('13-game', 'Game · 颜色宾果 Bingo (7 min)', 'Game · 宾果 (36–43)',
               b_task('游戏 · 宾果 · 课本 p.99 Ex.6 · 7 分钟', [
                   '在小白板上画一个 4×4 的格子。',
                   '从黑板上的十六个词里随便选，一格一个。',
                   '老师说中文，听到就划掉。先连成一条线的喊「有了！」，再把那一行念出来。',
               ], cn_lines=['十一个颜色　+　喜欢　颜色　+　校车　火车　地铁'],
                   ext=dict(text='老师不说词，说一整句 — ',
                            cn='我姐姐喜欢粉红色。',
                            sub='Students cross off only the colour inside. The winner reads back not the line but a sentence for each word in it.'))))
    s.append(S('14-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会说绿色和灰色',
                          '我会回答「你喜欢灰色吗？」',
                          '我会用「也」'],
                         'Translate — <b>I don\'t like grey. — I don\'t like it either.</b>',
                         '两句都要写。注意「也」的位置。',
                         '汉字。部首藏在字的哪里，还有听到一个词怎么写出声调。')))
    s.append(S('15-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('礻', 'Next — the radicals inside the characters',
                               ['弓　力　礻',
                                '<b>礻</b> 一点　·　<b>衤</b> 两点 — 下一课(第十四课)每件衣服都有它。'])))
    return s


def lesson6():
    s = []
    s.append(S('01-title', 'Title · 部首 · 笔画 · 声调', 'Title',
               b_title(6, '', '弓<span class="dot">·</span>力<span class="dot">·</span>礻',
                       'Radicals · Strokes · Tone marks',
                       META.format(p='p.97, 99'), '颜色'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 十一个颜色 + 也 (0–8 min)', 'Review · 复习',
               b_cards(ALL_11, cols=6, caption='全部十一个，只有汉字 — 两遍，第二遍快一点')
               + '''  <div style="display:flex;flex-direction:column;gap:16px;margin-top:36px;">
    <div class="error-pair"><span class="error-wrong">我不喜欢也。</span><span class="error-arrow">&rarr;</span><span class="error-correct">我也不喜欢。</span></div>
  </div>
'''))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们学怎么看出一个字里的部首，还有听到词写出声调。', [
                   dict(cn='我会写 弓、力、礻，每个都能说一个字', en='I can write 弓, 力 and 礻 and name a character for each'),
                   dict(cn='我会找出一个字的部首，还知道它是什么意思', en='I can find the radical in a character and say what it means'),
                   dict(cn='我听到一个词，会写拼音和声调', en='I can hear a word and write its pinyin with the correct tone mark'),
               ])))
    s.append(S('04-radicals', 'I Do · 部首 · 第二组 (弓 力 礻)', 'I Do · 部首',
               '''  <div class="grid-3">
    <div class="vocab-card highlight"><div class="vc-hanzi">弓</div><div class="vc-pinyin">bow</div><div class="vc-english">弹</div></div>
    <div class="vocab-card highlight"><div class="vc-hanzi">力</div><div class="vc-pinyin">strength</div><div class="vc-english">加</div></div>
    <div class="vocab-card highlight"><div class="vc-hanzi">礻</div><div class="vc-pinyin">ritual</div><div class="vc-english">视</div></div>
  </div>
  <div class="caption" style="text-align:center;margin-top:26px;">加上第三课的 疒、火、爫，课本 p.99 的六个部首就全了。</div>
'''))
    s.append(S('05-shi-vs-yi', 'I Do · 礻 还是 衤？', 'I Do · 部首 · 礻/衤', style=STYLE_CENTRE,
               inner='''  <div style="display:flex;flex-direction:column;align-items:center;gap:30px;text-align:center;">
    <div style="display:flex;align-items:center;gap:90px;">
      <div><div class="hanzi-hero">礻</div><div class="body-lg" style="margin-top:10px;">一点 · ritual</div><div class="ex-list"><div class="ex-row"><div class="ex-hanzi">视</div></div></div></div>
      <div><div class="hanzi-hero">衤</div><div class="body-lg" style="margin-top:10px;">两点 · clothing</div><div class="ex-list"><div class="ex-row"><div class="ex-hanzi">衬　衫　裤　裙</div></div></div></div>
    </div>
    <div class="warning-box" style="margin-top:10px;">
      <span class="warn-icon">!</span>
      <span class="warn-text">下一课(第十四课)每一件衣服的字都有「衤」。多一点就错了 — 现在先看清楚。</span>
    </div>
  </div>
'''))
    s.append(S('06-find', 'I Do · 部首藏在哪里', 'I Do · 找部首', dense=True,
               inner=b_pattern('左边 <span class="op">·</span> 上面 <span class="op">·</span> 下面 — 按这个顺序找', [
                   dict(py='chǎo', cn='炒 → 火', en='fire, on the left'),
                   dict(py='ài', cn='爱 → 爫', en='claw, on top'),
                   dict(py='hēi', cn='黑 → 灬', en='fire underneath — you wrote this one in Lesson 1'),
                   dict(py='jiā', cn='加 → [力]', hard=True, en='on the RIGHT — the awkward one'),
               ])))
    s.append(S('07-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '「炒」的部首在哪一边？指给我看。',
                   '<b>礻</b> 和 <b>衤</b>，哪个有两点？是什么意思？',
                   '写一个你已经学过、下面有「灬」的字。',
                   '光看部首，猜猜「病」是什么意思？',
               ])))
    s.append(S('08-act1', 'We Do · 活动一 · 听声调 + 数笔画 (8 min)', 'We Do · 活动一 (20–28)',
               b_task('活动一 · 课本 p.97 Ex.2 (CD T61) + 练习本 p.137 · 8 分钟', [
                   '九个词，听一遍写一遍，三个一组对答案。',
                   'Ex.6 — 数笔画：粉 色 黑 黄 红 白 蓝 喜。',
                   '练习本 Ex.4 — 看拼音写汉字再数笔画。都是一到四单元的字，应该很快。',
                   '练习本 Ex.21 — 在十六个格子里圈出颜色词。',
               ], cn_lines=['fàndiàn · jīngcháng · shòushāng · xuésheng · shítou',
                            'jiǎngbēi · jīnyú · yúncai · piàoliang'],
                   note=dict(text='「学生」和「石头」有轻声 — 不要乱加声调符号，轻声没有符号。'),
                   ext=dict(text='默写这一课的三个词，不看黑板 — ',
                            cn='fěnhóngsè　yánsè　lǜsè',
                            sub='The ü in lǜsè is the target. Then dictate two of your own to a partner and mark their work.'))))
    s.append(S('09-act2', 'You Do · 活动二 · 部首上纸 (8 min)', 'You Do · 活动二 (28–36)',
               b_task('活动二 · 练习本 p.134 / 138 / 137 / 144 · 8 分钟', [
                   'Ex.1 — 按笔顺抄 弓、力、礻。',
                   'Ex.9 第 4–6 题 — 写出 弹、加、视 的部首。',
                   'Ex.5 — 十二个部首，每个找一个字：目 纟 灬 艹 士 米 钅 冫 ⻊ 王 亻 方。',
                   'Ex.20 — 改错句，六句，全是语序。第 6 题就是上节课说过的那个。',
               ], note=dict(text='Ex.5 和 Ex.20 就是单元测验的第 3 部分和第 8 部分，一模一样的形式。',
                             sub='什么颜色你喜欢？ → 你喜欢什么颜色？'),
                   ext=dict(text='做 Ex.5 的时候，能填颜色字的就填颜色字 — ',
                            cn='纟→红 或 绿　米→粉　灬→黑',
                            sub='Then explain one of them aloud — 红 has 纟 because 纟 is silk, and silk was dyed red.'))))
    s.append(S('10-ladder', 'You Do · 加油题 · 笔画梯子', 'You Do · 加油题',
               b_task('练习本 p.137 Ex.7 · 做完的人做这个', [
                   '写一个一笔的字，再写两笔的，一直写到九笔。',
                   '书上最后一个是「美」。',
               ], cn_lines=['一 → ？ → ？ → ？ → ？ → ？ → ？ → ？ → 美'],
                   ext=dict(text='没有上限，也没有词库 — ',
                            cn='最后三格是真的难。',
                            sub='A standing extension for anyone who lands early, in any lesson.'))))
    s.append(S('11-game', 'Game · 接力写字 Writing Relay (7 min)', 'Game · 接力写字 (36–43)',
               b_task('游戏 · 接力写字 · 7 分钟', [
                   '两队，每队排一列在黑板前。',
                   '老师出一个短语 — 第一个人写第一个字，跑回来，第二个人写第二个字。',
                   '写对得一分；笔顺也对、「的」没丢，再得一分。',
               ], cn_lines=['喜欢黑色　·　粉红色的校车　·　紫色和棕色'],
                   ext=dict(text='短语只给拼音，或者只给英文，队伍自己写出汉字。最后一轮 ',
                            cn='下面还要写一行拼音，声调对才算分。',
                            sub='The tone marks are worth the point, not the characters.'))))
    s.append(S('12-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会写 弓、力、礻，每个都能说一个字',
                          '我会找出一个字的部首，还知道它的意思',
                          '我听到一个词会写声调'],
                         'Two items — write the radical of <b>视</b> and what it means; then any character that uses <b>火</b>.',
                         '写在小白板上。',
                         '全班调查 — 问所有人喜欢什么颜色，数出来，再报告。还有两个颜色混在一起会变成什么。')))
    s.append(S('13-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('五个人', 'Next — the class survey, and mixing colours',
                               ['你喜欢红色吗？ → 五个人喜欢黑色。',
                                '蓝色 <span class="new">和</span> 白色 <span class="new">是</span> 天蓝色。'])))
    return s


def lesson7():
    s = []
    s.append(S('01-title', 'Title · 调查 · 混色 · 天蓝色', 'Title',
               b_title(7, '', '天蓝色',
                       'The class survey · Mixing colours · 王红',
                       META.format(p='p.101–102'), '天蓝色'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 吗 + 不喜欢 (0–8 min)', 'Review · 复习',
               b_caption('全班接龙 — 老师先问，答完换一个颜色问下一个人。两圈，越来越快。')
               + '''  <div class="ex-list" style="gap:24px;">
    <div class="qa-row"><span class="qa-tag q">问</span><div class="qa-body">
      <div class="qa-pinyin">nǐ xǐhuan lǜsè ma</div><div class="qa-hanzi">你喜欢绿色吗？</div></div></div>
    <div class="qa-row"><span class="qa-tag a">答</span><div class="qa-body">
      <div class="qa-pinyin">xǐhuan ／ bù xǐhuan</div><div class="qa-hanzi">喜欢。／ 不喜欢。</div></div></div>
  </div>
  <div class="warning-box" style="margin-top:36px;">
    <span class="warn-icon">!</span>
    <span class="warn-text">答「是」的人把问题传给下一个，下一圈再试一次。</span>
  </div>
'''))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们学怎么问全班喜欢什么颜色，再把结果说出来。', [
                   dict(cn='我会问「你喜欢X色吗？」，还会记下答案', en='I can ask 你喜欢X色吗？and record the answers'),
                   dict(cn='我会报告结果：五个人喜欢黑色。', en='I can report a result — 五个人喜欢黑色'),
                   dict(cn='我会说两个颜色混在一起是什么颜色', en='I can say what two colours make — 蓝色和白色是天蓝色'),
               ])))
    s.append(S('04-vocab-a1', 'I Do · 生词 · 天蓝色', 'I Do · 生词',
               b_words([dict(hanzi='天蓝色', pinyin='tiānlánsè', english='sky blue',
                             clue='<b>天</b> 学过（今天、明天）　<b>蓝色</b> 第二课学过 — 只有合起来是新的')])))
    s.append(S('05-vocab-bc1', 'I Do · 例句 + 写一句 · 天蓝色', 'I Do · 例句 · 写一句',
               b_examples([
                   dict(py='lánsè hé báisè shì tiānlánsè', cn='蓝色和白色是<span class="new">天蓝色</span>。', en='Blue and white make sky blue.'),
                   dict(py='wǒ xǐhuan tiānlánsè de qìchē', cn='我喜欢<span class="new">天蓝色</span>的汽车。', en='I like sky-blue cars.'),
               ])
               + b_write(['我喜欢天蓝色的<span class="blank">　　　</span>。'],
                         '写一句。60 秒。',
                         dict(text='写一个三个颜色的算式 — ', cn='红色、黄色和蓝色是棕色。',
                              sub='Then say which of the two blues you prefer: 我喜欢天蓝色，我不喜欢蓝色。'))))
    s.append(S('06-board', 'I Do · 十二个颜色 · Summary Board', 'I Do · 词汇总览',
               b_cards(ALL_11 + ['天蓝色'], cols=6,
                       caption='这节课这块板一直留着 — 做活动的时候可以看')))
    s.append(S('07-pattern', 'I Do · 句型 · 五个人喜欢黑色', 'I Do · 句型', dense=True,
               inner=b_pattern('<span class="slot">数字</span> <span class="op">+</span> 个人 '
                               '<span class="op">+</span> 喜欢 <span class="op">+</span> <span class="slot">颜色</span>。', [
                   dict(py='nǐ xǐhuan lǜsè ma — xǐhuan', cn='你喜欢绿色吗？ — 喜欢。', en='Do you like green? — Yes.'),
                   dict(py='wǔ ge rén xǐhuan hēisè', cn='五个人喜欢黑色。', en='Five people like black.'),
                   dict(py='sān ge rén bù xǐhuan huīsè', cn='三个人不喜欢灰色。', en="Three people don't like grey."),
                   dict(py='shí ge rén xǐhuan lánsè，liǎng ge rén xǐhuan tiānlánsè，wǒ yě xǐhuan tiānlánsè',
                        cn='十个人喜欢蓝色，[两个人喜欢天蓝色，我也喜欢天蓝色]。', hard=True,
                        en='Two counts, a contrast between the two blues, and 也 attaching the speaker to the smaller group.'),
               ], note=dict(text='数人用「<b>个</b>」，不用「口」。',
                            sub='我家有三口人 — 口 is only for family. 五个人喜欢黑色 — everyone else takes 个.'),
                   note_icon='个')))
    s.append(S('08-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '数班上的人，用「口」还是「个」？为什么？',
                   '怎么说 <b>five people like black</b>？写在小白板上。',
                   '<span class="cn">红色和黄色是什么颜色？</span> 用中文回答。',
               ], errors=[('五口人喜欢红色。', '五个人喜欢红色。')])))
    s.append(S('09-act1', 'We Do · 活动一 · 混色 (5 min)', 'We Do · 活动一 (20–25)',
               b_task('活动一 · 课本 p.102 Ex.8 + 练习本 p.142 Ex.17 · 5 分钟', [
                   '七个算式，写到本子上，再大声说成完整的句子。',
                   '第一个已经给了。',
               ], cn_lines=['白色和黑色是灰色。',
                            '蓝色 + 白色　·　红色 + 黄色　·　红色 + 黄色 + 蓝色',
                            '白色 + 红色　·　黄色 + 蓝色　·　紫色 + 黄色'],
                   note=dict(text='这七个算式差不多把这一课的颜色全用上了。',
                             sub='Anyone who only remembers four gets found out here, rather than on the test.'),
                   ext=dict(text='自己编三个算式，每个后面加一个「的」短语 — ',
                            cn='蓝色和黄色是绿色，我喜欢绿色的校车。',
                            sub='Then quiz a partner with the board covered — you say two colours, they say the third.'))))
    s.append(S('10-act2', 'You Do · 活动二 · 全班调查 (9 min)', 'You Do · 活动二 (25–34)',
               b_task('活动二 · 课本 p.101 Ex.7 · 9 分钟', [
                   '每个人一张表，十一个颜色写在左边。',
                   '站起来问，问到谁就打一个勾。五分钟。',
                   '回座位数一数，写三个结果，完整的句子。',
               ], cn_lines=['你喜欢黑色吗？ — 喜欢。／不喜欢。',
                            '五个人喜欢黑色。'],
                   ext=dict(text='不只是数，要比 — ',
                            cn='五个人喜欢黑色，两个人不喜欢黑色，我也喜欢黑色。',
                            sub='Then work out the most and least popular colour in the room and announce both in Chinese. In mixed pairs the fluent student asks and the partner records.'))))
    s.append(S('11-act3', 'You Do · 活动三 · 阅读 · 王红 (5 min)', 'You Do · 活动三 (34–39)',
               b_task('活动三 · 练习本 p.140 Ex.14 · 5 分钟', [
                   '一起读一遍，然后两个人一组口头回答四个问题，其中两个写下来。',
               ], cn_lines=['我叫王红。我家有三口人：爸爸、妈妈和我。',
                            '我爸爸是律师，我妈妈不工作。',
                            '我喜欢红色，爸爸和妈妈<span class="new">都</span>喜欢黑色。'],
                   note=dict(text='「都」不是这一课的词 — 在黑板上写一下意思就行，不用教。',
                             sub='both / all — understanding it is enough.'),
                   ext=dict(text='四个问题全部写成完整的句子，再自己出第五个问题 ',
                            cn='考旁边的同学。'))))
    s.append(S('12-game', 'Game · 猜字游戏 Hangman (4 min)', 'Game · 猜字 (39–43)',
               b_task('游戏 · Hangman · 课本 p.103 Ex.11 · 4 分钟', [
                   '老师在黑板上画空格，全班猜字母。猜错就画一笔。',
                   '猜出来全班一起说这个词和意思。',
               ], cn_lines=['hóng sè　·　xǐ huan　·　fàng xué'],
                   ext=dict(text='猜的人要连声调一起说对才算 — ',
                            cn='ó 还是 ǒ？',
                            sub='And whoever solves the word has to use it in a full sentence before the next round starts.'))))
    s.append(S('13-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会问「你喜欢X色吗？」，还会记下答案',
                          '我会报告：五个人喜欢黑色。',
                          '我会说两个颜色混起来是什么'],
                         'Two items — <span class="cn">红色和黄色是什么颜色？</span> and one survey result as a full sentence.',
                         '两题都写在小白板上。',
                         '第十三课全部复习一遍，还有一篇课文 — 一个男孩的名字是两个颜色。')))
    s.append(S('14-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('复习', 'Next — revision, and 王黑白',
                               ['十二个颜色　·　喜欢　·　的　·　两种问句',
                                '他爸爸喜欢黑色和白色，<span class="new">所以</span>给他起名「黑白」。'])))
    return s


def lesson8():
    s = []
    s.append(S('01-title', 'Title · 复习', 'Title',
               b_title(8, '', '复习',
                       'Revision — everything from Lesson 13, all at once',
                       META.format(p='p.96–103'), '颜色'), STYLE_TITLE))
    s.append(S('02-review', 'Review · 十二个颜色 (0–8 min)', 'Review · 复习',
               b_cards(ALL_11 + ['天蓝色'], cols=6,
                       caption='只有汉字 — 两遍，第二遍打乱顺序')
               + '''  <div class="tip-box" style="margin-top:32px;">
    <span class="tip-icon">▶</span>
    <span><span class="tip-text">课本 p.102 Ex.9 — 老师说英文的东西，两队抢答中文颜色。</span>
    <span class="tip-sub">a lemon · the sky · an elephant · a school bus · grass · a taxi — some have two right answers, both score.</span></span>
  </div>
'''))
    s.append(S('03-li-sc', 'Learning Intention & Success Criteria (8–10 min)', 'LI · SC',
               b_lisc('我们把第十三课学的东西一起用一遍。', [
                   dict(cn='我会说十二个颜色，不看拼音', en='I can name all twelve colours without pinyin'),
                   dict(cn='我会问两种问句', en='I can ask both 你喜欢什么颜色？and 你喜欢X色吗？'),
                   dict(cn='我会用「颜色 + 的 + 东西」', en='I can describe something with 颜色 + 的 + noun'),
                   dict(cn='我会找部首，也会改语序', en='I can find the radical in a character and repair word order'),
               ])))
    s.append(S('04-shape1', 'I Do · 形式一 · 分类', 'I Do · 测验形式 1',
               b_task('第 1 种 · 分类 — 单元测验第 1 部分', [
                   '三个标题：颜色 · 车 · 每天做的事。',
                   '老师做前两个，剩下的全班一起说。',
               ], cn_lines=['橙色　出租车　起床　灰色　地铁　睡觉　紫色　校车　吃饭',
                            '橙色 → 颜色　　出租车 → 车'])))
    s.append(S('05-shape2', 'I Do · 形式二 · 部首 → 意思', 'I Do · 测验形式 2',
               b_task('第 2 种 · 部首和意思 — 单元测验第 2、3 部分', [
                   '每个字找出部首，再说部首是什么意思。',
                   '老师做第一个，「爱」和「病」全班一起。',
               ], cn_lines=['弹　·　爱　·　病　·　视　·　炒　·　加',
                            '弹 → 弓 → bow'])))
    s.append(S('06-shape3', 'I Do · 形式三 · 改语序', 'I Do · 测验形式 3', style=STYLE_CFU,
               inner='''  <div class="caption" style="margin-bottom:26px;">第 3 种 · 改语序 — 单元测验第 4、8 部分。这三个错，这一单元一路上都出现过。</div>
  <div style="display:flex;flex-direction:column;gap:20px;">
    <div class="error-pair"><span class="error-wrong">什么颜色你喜欢？</span><span class="error-arrow">&rarr;</span><span class="error-correct">你喜欢什么颜色？</span></div>
    <div class="error-pair"><span class="error-wrong">我不喜欢也。</span><span class="error-arrow">&rarr;</span><span class="error-correct">我也不喜欢。</span></div>
    <div class="error-pair"><span class="error-wrong">火车黑色的。</span><span class="error-arrow">&rarr;</span><span class="error-correct">黑色的火车</span></div>
  </div>
'''))
    s.append(S('07-shape4', 'I Do · 形式四 · 两个方向翻译', 'I Do · 测验形式 4', dense=True,
               inner=b_pattern('中文 <span class="op">↔</span> 英文 — 单元测验第 7、10 部分', [
                   dict(py='hēisè de chūzūchē', cn='黑色的出租车', en='→ a black taxi'),
                   dict(py='wǒ xǐhuan hóngsè hé lǜsè', cn='我喜欢红色和绿色。', en='← I like red and green colours.'),
                   dict(py='wǒ měitiān zǒulù shàngxué', cn='我每天走路上学。', en='← I walk to school every day.'),
                   dict(py='bàba měitiān kāichē shàngbān，tā xǐhuan báisè de qìchē',
                        cn='[爸爸每天开车上班，他喜欢白色的汽车。]', hard=True,
                        en='Colour, 的, and the whole Unit 4 frame in one sentence.'),
               ])))
    s.append(S('08-cfu', 'I Do · 检查 · CFU', 'I Do · 检查', style=STYLE_CFU,
               inner=b_cfu([
                   '十二个里面，哪一个<b>不是</b>颜色？',
                   '两种问句 — 一个开放的，一个「吗」的。两个都写。',
                   '这句对不对？ <span class="cn">我喜欢红色出租车。</span>',
                   '<span class="cn">我喜欢黑色的火车。</span> 里面有几个「的」？在哪里？',
               ], errors=[('我喜欢红色出租车。', '我喜欢红色的出租车。')])))
    s.append(S('09-act1', 'We Do · 活动一 · 阅读 · 王黑白 (7 min)', 'We Do · 活动一 (20–27)',
               b_task('活动一 · 练习本 p.145 Ex.23 · 7 分钟', [
                   '一起读一遍，再齐读一遍。',
                   '八个问题两个人一组口头答完，其中四个写下来。',
               ], cn_lines=['我爸爸喜欢黑色和白色，<span class="new">所以</span>他给我起名黑白。',
                            '我妈妈每天坐地铁上班。她喜欢蓝色和棕色。'],
                   note=dict(text='全文在练习本 p.145 — 「所以」「给我起名」只要看得懂，不用教。',
                             sub='Recycles name, city, family, jobs, transport and time from Units 1–4, all hung on colour.'),
                   ext=dict(text='自己写一段「王黑白」— 名字、城市、家人、一个家长的工作和怎么上班、每个人喜欢的颜色。',
                            cn='至少五句，至少三个颜色，至少一个「的」短语。',
                            sub='Board covered.'))))
    s.append(S('10-act2', 'You Do · 活动二 · 测验形式上纸 (8 min)', 'You Do · 活动二 (27–35)',
               b_task('活动二 · 练习本 p.140 / 144 / 143 / 139 · 8 分钟', [
                   'Ex.13 — 用给的词造句。就是单元测验第 4 部分的形式。',
                   'Ex.22 — 四句翻译成中文。只有第一句是颜色，后面三句是四单元 — 这是故意的。',
                   'Ex.18 — 填空的自我介绍：年龄、年级、五口人、父母的工作、每个人喜欢的颜色。',
                   'Ex.11 — 八个问题，全是一到四单元，一个颜色都没有。颜色就搭在这上面。',
               ], cn_lines=['喜欢/我妹妹　·　红色/不喜欢　·　每天/校车　·　怎么/你爸爸　·　十点/睡觉'],
                   ext=dict(text='先做练习本 p.140 Ex.12 — 用「几」自己写六个问题，挑两个问全班 — ',
                            cn='他几岁？　你几点起床？',
                            sub='Then write Ex.18 from scratch about yourself instead of filling in the blanks: every family member gets two colours with 和, and one sentence uses 的 with something from Unit 4.'))))
    s.append(S('11-game', 'Game · 找一个人 Find Someone Who (8 min)', 'Game · 找一个人 (35–43)',
               b_task('游戏 · 找一个人 · 8 分钟', [
                   '每人一张表，每一格找一个<b>不同</b>的同学，问到了就写名字。',
                   '只能用中文问 — 用英文问不算。',
               ], cn_lines=['……喜欢紫色　·　……<b>不</b>喜欢灰色　·　……的爸爸喜欢黑色',
                            '……坐黄色的校车　·　……喜欢天蓝色　·　……跟你喜欢一样的颜色',
                            '你喜欢紫色吗？　你爸爸喜欢什么颜色？'],
                   ext=dict(text='每个名字后面还要写一个追问的答案，不能只打勾。最后用「也」向全班报告两条 — ',
                            cn='她喜欢紫色，我也喜欢紫色。'))))
    s.append(S('12-plenary', 'Plenary · 出门条 (43–50 min)', 'Plenary',
               b_plenary(['我会说十二个颜色，不看拼音',
                          '我会问两种问句',
                          '我会用「颜色 + 的 + 东西」',
                          '我会找部首，也会改语序'],
                         'Two items — one sentence using a colour, 的 and a noun; then any radical with its meaning.',
                         '这一次看的是整个第十三课，不只是今天。四条里，全班想再练哪一条？',
                         '第十四课 — 衣服。一样的「的」，后面换成衬衫和裙子。你已经知道它们是什么部首了。')))
    s.append(S('13-preview', 'Preview · 下一课', 'Preview', style=STYLE_CENTRE,
               inner=b_preview('衤', 'Next — Lesson 14, clothing',
                               ['衬衫　牛仔裤　裙子',
                                '白色<span class="new">的</span>衬衫 — 一样的句型，一样的「的」。'])))
    return s


# ══════════════════════════════════════════════════════════════════
#  Deck registry
# ══════════════════════════════════════════════════════════════════

DECKS = [
    dict(n=1, dir='l1-xihuan-colours1', fn=lesson1, page='p.96',
         cn='喜欢 + 黑白黄', en='喜欢 and the First Three Colours',
         badge='Vocab + Mixed', cls='badge-vocab',
         foot='Lesson 1 of 8 · 喜欢 + 黑色 白色 黄色'),
    dict(n=2, dir='l2-text1-he', fn=lesson2, page='p.96',
         cn='蓝红粉 + 和', en='Text 1, and joining two colours with 和',
         badge='Vocab + Mixed', cls='badge-vocab',
         foot='Lesson 2 of 8 · 蓝色 红色 粉红色 + 和'),
    dict(n=3, dir='l3-de-frame', fn=lesson3, page='p.97',
         cn='颜色的东西', en='Colour + 的 + noun · radicals 疒 火 爫',
         badge='Grammar + Mixed', cls='badge-grammar',
         foot='Lesson 3 of 8 · 颜色 + 的 + 名词'),
    dict(n=4, dir='l4-yanse-question', fn=lesson4, page='p.100',
         cn='你喜欢什么颜色？', en='Asking the question · 颜色 橙色 紫色 棕色',
         badge='Vocab + Mixed', cls='badge-vocab',
         foot='Lesson 4 of 8 · 你喜欢什么颜色？'),
    dict(n=5, dir='l5-text2-ma-ye', fn=lesson5, page='p.100',
         cn='课文二 · 吗 / 也', en='Text 2 — 绿色 灰色, answering 吗, agreeing with 也',
         badge='Grammar + Mixed', cls='badge-grammar',
         foot='Lesson 5 of 8 · 课文二 · 吗 / 不喜欢 / 也'),
    dict(n=6, dir='l6-radicals-pinyin', fn=lesson6, page='p.97, 99',
         cn='部首 · 笔画 · 声调', en='Radicals 弓 力 礻 · strokes · tone marks',
         badge='Characters + Mixed', cls='badge-vocab',
         foot='Lesson 6 of 8 · 部首 · 笔画 · 声调'),
    dict(n=7, dir='l7-survey-mixing', fn=lesson7, page='p.101–102',
         cn='调查 · 混色', en='The class survey, mixing colours, 天蓝色',
         badge='Speaking + Mixed', cls='badge-speaking',
         foot='Lesson 7 of 8 · 调查 · 混色 · 天蓝色'),
    dict(n=8, dir='l8-revision', fn=lesson8, page='p.96–103',
         cn='复习', en='Revision — 王黑白 and the Unit Test formats',
         badge='Revision + Mixed', cls='badge-speaking',
         foot='Lesson 8 of 8 · 复习'),
]

BRAND = '轻松学中文 Book 1 · Unit 5 · 课本 {p}'

# ══════════════════════════════════════════════════════════════════
#  Deck viewer — taken from y7-l14 so the two decks page identically.
# ══════════════════════════════════════════════════════════════════

VIEWER_SRC = os.path.join(L14, 'l1-chuan-text1', 'index.html')


def viewer_html(title, slides):
    if not os.path.exists(VIEWER_SRC):
        raise SystemExit(f'viewer template missing: {VIEWER_SRC}')
    src = open(VIEWER_SRC, encoding='utf-8').read()
    manifest = ',\n'.join(
        f'    {{ file: "slides/{s["name"]}.html", label: {label_js(s["label"])} }}'
        for s in slides)
    src = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', src, count=1, flags=re.S)
    src = re.sub(r'window\.DECK_MANIFEST = \[.*?\n  \];',
                 'window.DECK_MANIFEST = [\n' + manifest + '\n  ];', src, count=1, flags=re.S)
    return src


def label_js(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


# ══════════════════════════════════════════════════════════════════
#  Lesson-list page — the design's own index.html
# ══════════════════════════════════════════════════════════════════

GRAMMAR = [
    ('L1', '喜欢', 'To like — 我爸爸喜欢黑色'),
    ('L2', '……和……', 'Joining two colours'),
    ('L3', '颜色+的+名词', 'Colour + noun (黑色的火车)'),
    ('L4', '你喜欢什么颜色？', 'The open question'),
    ('L5', '……吗？ / 我也不喜欢', 'Yes-no question, and agreeing'),
    ('L7', 'X色和Y色是Z色', 'Colour-mixing · 几个人喜欢……'),
]


def rebuild_index():
    """Keep the existing page's chrome; replace the lesson cards and the
    grammar panel, both of which are keyed to lesson numbers."""
    path = os.path.join(BASE, 'index.html')
    src = open(path, encoding='utf-8').read()

    gitems = ''.join(f'''
      <div class="grammar-item">
        <div class="g-num">{n}</div>
        <div class="g-zh">{zh}</div>
        <div class="g-en">{en}</div>
      </div>''' for n, zh, en in GRAMMAR)
    src = re.sub(r'<div class="grammar-grid">.*?\n    </div>',
                 '<div class="grammar-grid">' + gitems + '\n    </div>',
                 src, count=1, flags=re.S)
    cards = []
    for d in DECKS:
        cards.append(f'''
      <div class="lesson-card">
        <a href="{d['dir']}/" class="card-link">
          <div class="card-num">{d['n']:02d}</div>
          <div class="card-title">{d['cn']}</div>
          <div class="card-en">{d['en']}</div>
          <span class="card-badge {d['cls']}">{d['badge']}</span>
        </a>
        <a href="{d['dir']}/{d['dir']}.pptx" class="card-pptx">📥 PPTX</a>
      </div>
''')
    block = '<div class="lesson-grid">' + ''.join(cards) + '\n    </div>'
    src = re.sub(r'<div class="lesson-grid">.*?\n    </div>', block, src, count=1, flags=re.S)
    open(path, 'w', encoding='utf-8').write(src)


# ══════════════════════════════════════════════════════════════════
#  Emit
# ══════════════════════════════════════════════════════════════════

def build():
    # shared tokens come from y7-l14 — same unit, one visual family
    os.makedirs(os.path.join(BASE, 'shared'), exist_ok=True)
    css = open(os.path.join(L14, 'shared', 'tokens.css'), encoding='utf-8').read()
    # The callout sub-lines carry margin-top but are inline spans, so the margin
    # is dead and the sub runs on from the text: "…likes black.写在小白板上". Their
    # sibling .ext-body .sub already sets display:block; these were missed.
    # Appended here rather than fixed upstream so y7-l14's shipped exports stay valid.
    css += ("""
/* ── y7-l13: callout sub-lines are blocks, like .ext-body .sub ── */
.note-box .note-sub, .warning-box .warn-sub,
.tip-box .tip-sub, .info-box .info-sub { display: block; }

/* Pattern slides carry four worked examples plus a callout. Tightening the
   leading (NOT the size - still 52px, far above the floor) is what keeps the
   fourth, hardest example on the canvas instead of dropping it. */
.pattern-wrap .ex-row .ex-hanzi { line-height: 1.16; }
.pattern-wrap .ex-row { gap: 2px; }
.pattern-wrap { gap: 22px; }
.pattern-wrap .ex-list { gap: 20px; }

/* Task slides with a callout run a few pixels long for the same reason. */
.slide-content.dense .ex-list { gap: 16px; }
""")
    open(os.path.join(BASE, 'shared', 'tokens.css'), 'w', encoding='utf-8').write(css)

    # drop every old lesson folder (the boundaries changed, the names changed)
    for entry in sorted(os.listdir(BASE)):
        p = os.path.join(BASE, entry)
        if os.path.isdir(p) and re.match(r'^l\d', entry):
            shutil.rmtree(p)

    total_slides = 0
    for d in DECKS:
        slides = d['fn']()
        sdir = os.path.join(BASE, d['dir'], 'slides')
        os.makedirs(sdir, exist_ok=True)
        n = len(slides)
        for s in slides:
            html = PAGE.format(
                title=f"L{d['n']}-{s['name'][:2]} · {s['section']}",
                style=s['style'],
                tag=TAG,
                section=s['section'],
                dense=' dense' if s['dense'] else '',
                inner=s['inner'],
                foot=s['foot'] or d['foot'],
                brand=BRAND.format(p=d['page']),
            )
            open(os.path.join(sdir, s['name'] + '.html'), 'w', encoding='utf-8').write(html)
        open(os.path.join(BASE, d['dir'], 'index.html'), 'w', encoding='utf-8').write(
            viewer_html(f"L{d['n']} · {d['cn']} · 颜色", slides))
        total_slides += n
        print(f"  {d['dir']:<22} {n:>3} slides")

    rebuild_index()
    print(f'\n  {len(DECKS)} decks · {total_slides} slides')


if __name__ == '__main__':
    build()
