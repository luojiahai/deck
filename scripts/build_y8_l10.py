#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the Y8 Lesson 10 slide decks (蔬菜、水果) from the six lesson plans
in docs/lesson-plans/y8-l10/.

Six decks, one per classroom lesson. Each deck is a folder of standalone
1920×1080 slides plus an index.html shell that pages through them.

Design constraints this script enforces, so they cannot drift:
  · a slide that INTRODUCES vocabulary carries at most two new words
  · every pair of new words runs the three-slide cycle A → B → C
  · every C slide carries an extension
  · nothing a student must read is set below 26px (see shared/tokens.css)

Run:  python3 scripts/build_y8_l10.py
"""

import os
import shutil

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
BASE = os.path.join(ROOT, 'index', 'designs', 'y8-l10')

# ══════════════════════════════════════════════════════════════════
#  Slide shell
# ══════════════════════════════════════════════════════════════════

PAGE = '''<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta charset="UTF-8">
<title>Y8 L10 · {title}</title>
<link rel="stylesheet" href="../../shared/tokens.css">
</head>
<body>
<div class="slide-header">
  <span class="lesson-tag">{tag}</span>
  <span class="sep"></span>
  <span class="section-name">{section}</span>
  <span class="slide-num">{n} / {total}</span>
  <div class="accent-line"></div>
</div>
<div class="slide-content{top}">
{inner}
</div>
</body></html>
'''


def esc(s):
    return s


# ══════════════════════════════════════════════════════════════════
#  Block builders — each returns inner HTML for one slide
# ══════════════════════════════════════════════════════════════════

def b_label(text):
    return f'  <p class="section-label">{text}</p>\n'


def b_title(kicker, hanzi, en, meta, strip):
    imgs = ''.join(f'<img src="../../img/{s}.svg" alt="">' for s in strip)
    return f'''  <div class="title-wrap">
    <p class="title-kicker">{kicker}</p>
    <h1 class="title-hanzi">{hanzi}</h1>
    <p class="title-en">{en}</p>
    <p class="title-meta">{meta}</p>
    <div class="title-strip">{imgs}</div>
  </div>
'''


def b_words(items, label='New Words · 跟我读两遍 · repeat after me, twice'):
    """Slide A of a cycle. At most two items — the rule, enforced."""
    assert len(items) <= 2, 'a vocabulary slide carries at most two new words'
    single = ' single' if len(items) == 1 else ''
    cards = []
    for it in items:
        if it.get('img'):
            img = f'<div class="wc-img"><img src="../../img/{it["img"]}.svg" alt=""></div>'
            cls = 'word-card'
        else:
            img = ''
            cls = 'word-card textonly'
        hz = 'word-hanzi long' if len(it['hanzi']) >= 4 else 'word-hanzi'
        trad = f'<p class="word-trad">traditional 繁体：{it["trad"]}</p>' if it.get('trad') else ''
        cards.append(f'''    <div class="{cls}">
      {img}
      <p class="word-pinyin">{it['pinyin']}</p>
      <p class="{hz}">{it['hanzi']}</p>
      <p class="word-english">{it['english']}</p>
      {trad}
    </div>''')
    return b_label(label) + f'  <div class="word-pair{single}">\n' + '\n'.join(cards) + '\n  </div>\n'


def b_examples(rows, label='例句 · See them used'):
    out = [b_label(label), '  <div class="sentence-list">\n']
    for r in rows:
        cls = 'sentence-row both' if r.get('both') else 'sentence-row'
        py = f'<p class="sentence-py">{r["py"]}</p>' if r.get('py') else ''
        en = f'<p class="sentence-en">{r["en"]}</p>' if r.get('en') else ''
        out.append(f'''    <div class="{cls}">
      {py}
      <p class="sentence-cn">{r['cn']}</p>
      {en}
    </div>\n''')
    out.append('  </div>\n')
    return ''.join(out)


def b_write(lines, note, ext, label='写一句 · Write your own'):
    ls = '\n'.join(f'      <p class="frame-line">{l}</p>' for l in lines)
    return b_label(label) + f'''  <div class="frame-box">
{ls}
      <p class="frame-note">{note}</p>
  </div>
{b_ext(ext)}'''


def b_ext(ext):
    cn = f'<p class="extension-cn">{ext["cn"]}</p>' if ext.get('cn') else ''
    return f'''  <div class="extension-box">
    <p class="extension-label">Extension · 加油题</p>
    <p class="extension-text">{ext['text']}</p>
    {cn}
  </div>
'''


def b_recall(words, cols=3, label='认字 · Read these back — no pinyin, no English'):
    c = {3: '', 4: ' c4', 5: ' c5'}[cols]
    cells = ''.join(
        f'    <div class="recall-cell"><p class="recall-hanzi{" long" if len(w) >= 4 else ""}">{w}</p></div>\n'
        for w in words)
    return b_label(label) + f'  <div class="recall-grid{c}">\n{cells}  </div>\n'


def b_summary(cells, cols=4, label='词汇总览 · Everything from this lesson'):
    c = {4: '', 5: ' c5', 6: ' c6'}[cols]
    out = []
    for cell in cells:
        if isinstance(cell, str):
            hz, img = cell, None
        else:
            hz, img = cell
        long = ' long' if len(hz) >= 3 else ''
        if img:
            out.append(f'''    <div class="summary-cell">
      <div class="sc-img"><img src="../../img/{img}.svg" alt=""></div>
      <p class="summary-hanzi{long}">{hz}</p>
    </div>\n''')
        else:
            out.append(f'    <div class="summary-cell noimg"><p class="summary-hanzi{long}">{hz}</p></div>\n')
    return b_label(label) + f'  <div class="summary-grid{c}">\n' + ''.join(out) + '  </div>\n'


def b_pattern(pattern, note, examples, label='句型 · Key sentence pattern'):
    rows = []
    for i, e in enumerate(examples, 1):
        hard = ' hardest' if e.get('hard') else ''
        en = f'<p class="example-en">{e["en"]}</p>' if e.get('en') else ''
        rows.append(f'''    <div class="example-row{hard}">
      <p class="example-num">{i}</p>
      <div><p class="example-cn">{e['cn']}</p>{en}</div>
    </div>\n''')
    n = f'<p class="pattern-note">{note}</p>' if note else ''
    return b_label(label) + f'''  <div class="pattern-box">
    <p class="pattern-text">{pattern}</p>
    {n}
  </div>
  <div class="example-list" style="margin-top:36px">
{''.join(rows)}  </div>
'''


def b_callout(kind, label, text, cn=None, sub=None):
    cnh = f'<p class="cb-cn">{cn}</p>' if cn else ''
    subh = f'<p class="cb-sub">{sub}</p>' if sub else ''
    return f'''  <div class="{kind}-box">
    <div>
      <p class="cb-label">{label}</p>
      <p class="cb-text">{text}</p>
      {cnh}{subh}
    </div>
  </div>
'''


def b_lisc(intention, criteria):
    """Learning intention + success criteria.

    Four criteria do not fit the canvas at the three-criteria sizes, so
    the four-criteria version gets its own compact class. Compacting is
    padding and leading only — every size still clears the floor."""
    compact = ' lisc-compact' if len(criteria) >= 4 else ''
    rows = ''.join(f'''    <div class="sc-row">
      <p class="sc-num">{i}</p>
      <div><p class="sc-main">{c['en']}</p><p class="sc-cn">{c['cn']}</p></div>
    </div>\n''' for i, c in enumerate(criteria, 1))
    gap = 'gap-sm' if compact else 'gap-sm'
    return f'''  <div class="lisc{compact}">
  <p class="section-label">Learning Intention · 学习目标</p>
  <div class="pattern-box" style="text-align:left">
    <p class="display-md">{intention}</p>
  </div>
  <p class="section-label lisc-2nd">Success Criteria · 我会……</p>
  <div class="stack {gap}">
{rows}  </div>
  </div>
'''


def b_dialogue(rows, label='课文 · Text', qs=None):
    out = [b_label(label), '  <div class="dialogue">\n']
    for r in rows:
        who = r.get('who', 'A')
        cls = 'dl-row b' if who == 'B' else 'dl-row'
        py = f'<p class="dl-py">{r["py"]}</p>' if r.get('py') else ''
        out.append(f'''    <div class="{cls}">
      <p class="dl-who">{who}</p>
      <div class="dl-body">{py}<p class="dl-cn">{r['cn']}</p></div>
    </div>\n''')
    out.append('  </div>\n')
    if qs:
        qh = ''.join(f'<p class="task-cn">{i}. {q}</p>' for i, q in enumerate(qs, 1))
        out.append(f'  <div class="task-box" style="margin-top:32px">{qh}</div>\n')
    return ''.join(out)


def b_task(label, badge, steps, ext=None, cn_lines=None):
    # step-num and badge carry a background, so they must be <div> wrappers:
    # the PPTX exporter only allows backgrounds/borders on <div>, not on text tags.
    sh = ''.join(f'''    <div class="step-row">
      <div class="step-num"><p>{i}</p></div>
      <p class="step-text">{s}</p>
    </div>\n''' for i, s in enumerate(steps, 1))
    cn = ''
    if cn_lines:
        cn = '  <div class="task-box" style="margin-top:26px">\n' + \
             ''.join(f'    <p class="task-cn">{l}</p>\n' for l in cn_lines) + '  </div>\n'
    out = b_label(label) + (f'  <div class="badge badge-orange" style="margin-bottom:24px"><p>{badge}</p></div>\n' if badge else '') \
        + f'  <div class="stack gap-sm">\n{sh}  </div>\n' + cn
    if ext:
        out += b_ext(ext)
    return out


def b_opts(items, cols=3, label='', correct=None):
    correct = correct or []
    c = '' if cols == 3 else ' c2'
    cells = ''.join(
        f'    <div class="opt-cell{" correct" if i in correct else ""}">'
        f'<span class="opt-key">{k}</span><span class="opt-cn">{v}</span></div>\n'
        for i, (k, v) in enumerate(items))
    return (b_label(label) if label else '') + f'  <div class="opt-grid{c}">\n{cells}  </div>\n'


def b_table(head, rows, label=''):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''
    for r in rows:
        tds = ''.join(f'<td class="{cls}">{val}</td>' for cls, val in r)
        tr += f'    <tr>{tds}</tr>\n'
    return (b_label(label) if label else '') + f'''  <table class="pair-table">
    <tr>{th}</tr>
{tr}  </table>
'''


def b_plenary(criteria, exit_ticket, preview):
    rows = ''.join(f'    <div class="sc-row"><p class="sc-num">{i}</p>'
                   f'<div><p class="sc-main">{c}</p></div></div>\n'
                   for i, c in enumerate(criteria, 1))
    return f'''  <p class="section-label">Plenary · 我做到了吗？ 👍 / 😐 / 👎</p>
  <div class="stack gap-sm">
{rows}  </div>
{b_callout('note', 'Exit ticket · 出门条', exit_ticket['text'], exit_ticket.get('cn'))}
{b_callout('tip', 'Next lesson · 下节课', preview)}
'''


# ══════════════════════════════════════════════════════════════════
#  The six decks
# ══════════════════════════════════════════════════════════════════
# Each entry: (filename, nav label, header tag, header section, inner html)

def lesson1():
    S = []
    S.append(('01-title', 'Title · 蔬菜 Vegetables', 'Lesson 1 of 6', 'Y8 · Lesson 10',
              b_title('轻松学中文 2 · Unit 4 · Lesson 10',
                      '蔬菜', 'Vegetables',
                      'Lesson 1 of 6 · 50 minutes · 课本 p.90–91',
                      ['shucai', 'shengcai', 'huanggua', 'tudou', 'caihuar', 'xihongshi'])))

    S.append(('02-review', 'Review · Unit 3 degree scale', '0–8 MIN · REVIEW', '复习 · Unit 3 recap',
              b_label('复习 · How much do you like it?') +
              b_opts([('最', '最喜欢'), ('非常', '非常喜欢'), ('很', '很喜欢'),
                      ('不太', '不太喜欢'), ('不', '不喜欢'), ('？', '你喜欢做什么运动？')]) +
              b_callout('tip', 'Connection · 今天',
                        'You already know how to say how much you like doing something. '
                        'Today we keep that language and change what comes after 吃.',
                        '你喜欢吃什么蔬菜？')))

    S.append(('03-li-sc', 'Learning Intention & Success Criteria', '8–10 MIN', '学习目标',
              b_lisc('We are learning to name common vegetables in Chinese '
                     'and say which ones we like eating.',
                     [{'en': 'I can say and read six vegetables in Chinese',
                       'cn': '蔬菜 · 生菜 · 黄瓜 · 土豆 · 菜花儿 · 西红柿'},
                      {'en': 'I can ask someone what vegetables they like',
                       'cn': '你喜欢吃什么蔬菜？'},
                      {'en': 'I can say how much I like a vegetable using 很 / 不太',
                       'cn': '我很喜欢吃黄瓜。'}])))

    # Cycle 1
    S.append(('04-c1-words', 'Cycle 1 · A — 蔬菜 / 生菜', '10–20 MIN · I DO', '生词 · Cycle 1 of 3',
              b_words([{'hanzi': '蔬菜', 'pinyin': 'shūcài', 'english': 'vegetables', 'img': 'shucai'},
                       {'hanzi': '生菜', 'pinyin': 'shēngcài', 'english': 'lettuce', 'img': 'shengcai'}])))
    S.append(('05-c1-examples', 'Cycle 1 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 1 of 3',
              b_examples([
                  {'py': 'Wǒ xǐhuan chī shūcài.', 'cn': '我喜欢吃<b>蔬菜</b>。', 'en': 'I like eating vegetables.'},
                  {'py': 'Wǒ hěn xǐhuan chī shēngcài.', 'cn': '我很喜欢吃<b>生菜</b>。', 'en': 'I really like eating lettuce.'},
                  {'py': 'Wǒ xǐhuan chī shūcài, wǒ měi tiān dōu chī shēngcài.',
                   'cn': '我喜欢吃<b>蔬菜</b>，我每天都吃<b>生菜</b>。',
                   'en': 'I like vegetables — I eat lettuce every day.', 'both': True}])))
    S.append(('06-c1-write', 'Cycle 1 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 1 of 3',
              b_write(['我 ______ 喜欢吃 ______ 。'],
                      '60 seconds. Mini whiteboards. One sentence.',
                      {'text': 'Write about <b>someone else</b>, in two clauses — then say it aloud without reading it.',
                       'cn': '我妈妈很喜欢吃生菜，我不太喜欢吃。'})))

    # Cycle 2
    S.append(('07-c2-words', 'Cycle 2 · A — 黄瓜 / 土豆', '10–20 MIN · I DO', '生词 · Cycle 2 of 3',
              b_words([{'hanzi': '黄瓜', 'pinyin': 'huángguā', 'english': 'cucumber', 'img': 'huanggua'},
                       {'hanzi': '土豆', 'pinyin': 'tǔdòu', 'english': 'potato', 'img': 'tudou'}])))
    S.append(('08-c2-examples', 'Cycle 2 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 2 of 3',
              b_examples([
                  {'py': 'Wǒ xǐhuan chī huángguā.', 'cn': '我喜欢吃<b>黄瓜</b>。', 'en': 'I like eating cucumber.'},
                  {'py': 'Tǔdòu wǒ yě xǐhuan chī.', 'cn': '<b>土豆</b>我也喜欢吃。', 'en': 'I like potatoes too.'},
                  {'py': 'Huángguā hé tǔdòu wǒ dōu xǐhuan chī.',
                   'cn': '<b>黄瓜</b>和<b>土豆</b>我都喜欢吃。',
                   'en': 'I like both cucumber and potato.', 'both': True}])))
    S.append(('09-c2-write', 'Cycle 2 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 2 of 3',
              b_write(['______ 和 ______ 我都喜欢吃。'],
                      '60 seconds. Both blanks. Characters, not pinyin.',
                      {'text': 'Use 除了…以外 instead, then add a third vegetable and keep the structure working.',
                       'cn': '除了黄瓜以外，我还喜欢吃土豆。'})))

    # Cycle 3
    S.append(('10-c3-words', 'Cycle 3 · A — 菜花儿 / 西红柿', '10–20 MIN · I DO', '生词 · Cycle 3 of 3',
              b_words([{'hanzi': '菜花儿', 'pinyin': 'càihuār', 'english': 'cauliflower', 'img': 'caihuar'},
                       {'hanzi': '西红柿', 'pinyin': 'xīhóngshì', 'english': 'tomato', 'img': 'xihongshi'}])))
    S.append(('11-c3-examples', 'Cycle 3 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 3 of 3',
              b_examples([
                  {'py': 'Wǒ bú tài xǐhuan chī càihuār.', 'cn': '我不太喜欢吃<b>菜花儿</b>。',
                   'en': "I don't much like eating cauliflower."},
                  {'py': 'Xīhóngshì shì hóngsè de.', 'cn': '<b>西红柿</b>是红色的。', 'en': 'Tomatoes are red.'},
                  {'py': 'Wǒ xǐhuan chī xīhóngshì, bù xǐhuan chī càihuār.',
                   'cn': '我喜欢吃<b>西红柿</b>，不喜欢吃<b>菜花儿</b>。',
                   'en': "I like tomatoes, I don't like cauliflower.", 'both': True}])))
    S.append(('12-c3-write', 'Cycle 3 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 3 of 3',
              b_write(['我 ______ 喜欢吃菜花儿。', '我 ______ 喜欢吃西红柿。'],
                      '60 seconds. Two sentences that disagree with each other.',
                      {'text': 'Ask your partner about both, then report what <b>they</b> said — third person.',
                       'cn': '他很喜欢吃西红柿，不太喜欢吃菜花儿。'})))

    S.append(('13-recall', 'Checkpoint · 认字 recall', '10–20 MIN · I DO', '认字 · checkpoint',
              b_recall(['蔬菜', '生菜', '黄瓜', '土豆', '菜花儿', '西红柿'])))

    S.append(('14-pattern', 'I Do · 句型 你喜欢吃什么蔬菜？', '10–20 MIN · I DO', '句型 · sentence pattern',
              b_pattern('你喜欢吃什么<b>蔬菜</b>？ → 我喜欢吃……。',
                        'Nǐ xǐhuan chī shénme shūcài?',
                        [{'cn': '你喜欢吃什么蔬菜？ — 我喜欢吃黄瓜。'},
                         {'cn': '你喜欢吃什么蔬菜？ — 我喜欢吃生菜和土豆。'},
                         {'cn': '我最喜欢吃黄瓜，不太喜欢吃菜花儿。'},
                         {'cn': '除了生菜以外，我还喜欢吃西红柿和土豆。',
                          'en': 'Two structures, three vegetables — the hardest one.', 'hard': True}])))

    S.append(('15-summary', '词汇总览 · summary board', '20–43 MIN · WE DO', '词汇总览 · stays on screen',
              b_summary([('蔬菜', 'shucai'), ('生菜', 'shengcai'), ('黄瓜', 'huanggua'),
                         ('土豆', 'tudou'), ('菜花儿', 'caihuar'), ('西红柿', 'xihongshi')],
                        cols=6)))

    S.append(('16-task', 'Activity 1 · 分类 sort them (We Do)', '20–43 MIN · WE DO', '活动一 · 分类 sorting · 7 min',
              b_task('Activity 1 · 分类 Sort them — We Do', 'Pairs · 7 minutes',
                     ['Take the two-column sheet: 我喜欢吃 / 我不太喜欢吃.',
                      'Place <b>all six</b> words. Every word goes in a column — nothing left out.',
                      'Write them in characters, not pinyin.',
                      'Then say two of your placements aloud as full sentences.'],
                     {'text': 'Three columns instead of two — 我每天吃 / 我有时候吃 / 我不吃 — '
                              'then join two placements with 除了…以外, and justify one aloud with no notes.',
                      'cn': '除了黄瓜以外，我还每天吃西红柿。'},
                     cn_lines=['我很喜欢吃生菜。', '我不太喜欢吃菜花儿。'])))

    S.append(('17-act2', 'Activity 2 · 采访 interview (You Do)', '20–43 MIN · YOU DO', '活动二 · 采访 interview · 8 min',
              b_task('Activity 2 · 采访 Vegetable interview — You Do', 'Stand up · three partners · 8 minutes',
                     ['Ask three people: 你喜欢吃什么蔬菜？',
                      'Write each answer on your whiteboard — in characters.',
                      'Back at your seat, write one sentence about one person you asked.'],
                     {'text': 'Ask five people and add a follow-up each time — 你每天都吃吗？ '
                              'Then report the whole set to the class using 都. No notes on screen.',
                      'cn': '他们都喜欢吃黄瓜，可是没有人喜欢吃菜花儿。'},
                     cn_lines=['你喜欢吃什么蔬菜？', '小明很喜欢吃土豆。'])))

    S.append(('18-game', 'Game · 拍字 Slap the Character', '20–43 MIN · GAME', '游戏 · 拍字 · 7 min',
              b_task('Game · 拍字 Slap the Character', 'Two teams · 7 minutes',
                     ['One player from each team at the board, facing the six character cards.',
                      'Teacher says a vegetable in Chinese — first to slap the right card wins the point.',
                      'Rotate every round so everyone plays.'],
                     {'text': 'The teacher says the word <b>inside a sentence</b> instead of on its own — '
                              '我妈妈每天都吃这个。 For the last three rounds the slapper must also say the word '
                              'aloud correctly to keep the point.'})))

    S.append(('19-plenary', 'Plenary · exit ticket & preview', '43–50 MIN · PLENARY', '小结 · plenary',
              b_plenary(['I can say and read six vegetables in Chinese',
                         'I can ask 你喜欢吃什么蔬菜？',
                         'I can say how much I like a vegetable using 很 / 不太'],
                        {'text': 'Complete this in characters. The second half must name at least two vegetables.',
                         'cn': '我喜欢吃蔬菜，我 ____________ 。'},
                        'How to tell someone what they <b>should</b> eat — 应该.')))
    return S


def lesson2():
    S = []
    S.append(('01-title', 'Title · 应该 Should', 'Lesson 2 of 6', 'Y8 · Lesson 10',
              b_title('轻松学中文 2 · Unit 4 · Lesson 10',
                      '应该', 'Should · and listing with 等等',
                      'Lesson 2 of 6 · 50 minutes · 课本 p.91–93',
                      ['qingcai', 'nangua', 'shengcai', 'huanggua'])))

    S.append(('02-review', 'Review · p.93 Ex.5 acting game', '0–8 MIN · REVIEW', '复习 · 表演游戏 acting game',
              b_task('复习 · Act it out — textbook p.93 Ex.5', 'Two teams · 3 minutes',
                     ['Teacher says a phrase. One member of each team acts it out in turn.',
                      'Correct action = one point.',
                      'Then: the six vegetables in characters — class reads them back with no pinyin.'],
                     None,
                     cn_lines=['跑步 · 游泳 · 听音乐 · 打篮球 · 吃饭 · 唱歌 · 弹钢琴 · 看电视',
                               '洗澡 · 睡觉 · 打网球 · 画画儿 · 跳舞 · 跳高 · 穿衣服 · 拉小提琴'])))

    S.append(('03-li-sc', 'Learning Intention & Success Criteria', '8–10 MIN', '学习目标',
              b_lisc('We are learning to say what someone should do, '
                     'and to list several things in one sentence.',
                     [{'en': 'I can use 应该 to give advice', 'cn': '你应该每天吃蔬菜。'},
                      {'en': "I can report someone else's advice", 'cn': '妈妈说我应该多吃青菜。'},
                      {'en': 'I can list three or more things and close the list with 等等',
                       'cn': '我喜欢吃黄瓜、土豆、生菜等等。'},
                      {'en': 'I can use 非常 to say I like something a lot', 'cn': '我非常喜欢吃黄瓜。'}])))

    S.append(('04-c1-words', 'Cycle 1 · A — 青菜 / 南瓜', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_words([{'hanzi': '青菜', 'pinyin': 'qīngcài', 'english': 'green vegetable', 'img': 'qingcai'},
                       {'hanzi': '南瓜', 'pinyin': 'nánguā', 'english': 'pumpkin', 'img': 'nangua'}])))
    S.append(('05-c1-examples', 'Cycle 1 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_examples([
                  {'py': 'Wǒ māma měi tiān dōu chī qīngcài.', 'cn': '我妈妈每天都吃<b>青菜</b>。',
                   'en': 'My mum eats green vegetables every day.'},
                  {'py': 'Wǒ bú tài xǐhuan chī nánguā.', 'cn': '我不太喜欢吃<b>南瓜</b>。',
                   'en': "I don't much like eating pumpkin."},
                  {'py': 'Qīngcài hé nánguā wǒ dōu xǐhuan chī.', 'cn': '<b>青菜</b>和<b>南瓜</b>我都喜欢吃。',
                   'en': 'I like both green vegetables and pumpkin.', 'both': True}])))
    S.append(('06-c1-write', 'Cycle 1 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_write(['我 ______ 喜欢吃青菜。', '我 ______ 喜欢吃南瓜。'],
                      '60 seconds. Mini whiteboards.',
                      {'text': 'Use both words in <b>one</b> sentence with 除了…以外.',
                       'cn': '除了青菜以外，我还喜欢吃南瓜。'})))

    S.append(('07-extra', 'Extra Words · recognition only', '10–20 MIN · I DO', '补充词 · recognition only',
              b_label('Extra Words · p.91 — you only need to recognise these, not write them') +
              b_table(['汉字', '拼音', 'English'],
                      [[('hanzi-cell', '冬瓜'), ('pinyin-cell', 'dōngguā'), ('english-cell', 'winter melon')],
                       [('hanzi-cell', '四季豆'), ('pinyin-cell', 'sìjìdòu'), ('english-cell', 'green beans')],
                       [('hanzi-cell', '大白菜'), ('pinyin-cell', 'dàbáicài'), ('english-cell', 'Chinese cabbage')]]) +
              b_callout('note', 'Notice · 瓜 and 菜',
                        'Words that share a character share a category. 南瓜、冬瓜、西瓜 are all 瓜. '
                        '青菜、生菜、菜花儿 are all 菜.')))

    S.append(('08-c2-words', 'Cycle 2 · A — 应该 / 非常', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_words([{'hanzi': '应该', 'pinyin': 'yīnggāi', 'english': 'should', 'trad': '應該'},
                       {'hanzi': '非常', 'pinyin': 'fēicháng', 'english': 'very; extremely'}])))
    S.append(('09-c2-examples', 'Cycle 2 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_examples([
                  {'py': 'Wǒ fēicháng xǐhuan chī xīhóngshì.', 'cn': '我<b>非常</b>喜欢吃西红柿。',
                   'en': 'I really like eating tomatoes.'},
                  {'py': 'Nǐ yīnggāi měi tiān chī shūcài.', 'cn': '你<b>应该</b>每天吃蔬菜。',
                   'en': 'You should eat vegetables every day.'},
                  {'py': 'Wǒ fēicháng xǐhuan chī tǔdòu, kěshì māma shuō wǒ yīnggāi duō chī qīngcài.',
                   'cn': '我<b>非常</b>喜欢吃土豆，可是妈妈说我<b>应该</b>多吃青菜。',
                   'en': 'I really like potatoes, but Mum says I should eat more green vegetables.', 'both': True}])))
    S.append(('10-c2-write', 'Cycle 2 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_write(['我 ______ 喜欢 ______ 。', '你应该 ______ 。'],
                      '60 seconds. One sentence of each kind.',
                      {'text': 'Write the <b>reported</b> version — not advice to the listener, but advice you were '
                              'given. Two sentences, two different advice-givers.',
                       'cn': '我的老师说我应该 ____________ 。'})))

    S.append(('11-recall', 'Checkpoint · 认字 recall', '10–20 MIN · I DO', '认字 · checkpoint',
              b_recall(['青菜', '南瓜', '应该', '非常', '等等'], cols=5)))

    S.append(('12-copy', '写字 · copy the new words (WB Ex.1)', '10–20 MIN · I DO', '写字 · character copying',
              b_label('写字 · Copy the Text 1 new words — stroke order on the board') +
              b_table(['汉字', '拼音', 'English', '部首 radical'],
                      [[('hanzi-cell', '蔬'), ('pinyin-cell', 'shū'), ('english-cell', 'vegetables'), ('pinyin-cell', '艹 plant')],
                       [('hanzi-cell', '菜'), ('pinyin-cell', 'cài'), ('english-cell', 'vegetable; dish'), ('pinyin-cell', '艹 plant')],
                       [('hanzi-cell', '非'), ('pinyin-cell', 'fēi'), ('english-cell', 'wrong; not'), ('pinyin-cell', '非')],
                       [('hanzi-cell', '花'), ('pinyin-cell', 'huā'), ('english-cell', 'flower'), ('pinyin-cell', '艹 plant')],
                       [('hanzi-cell', '柿'), ('pinyin-cell', 'shì'), ('english-cell', 'persimmon'), ('pinyin-cell', '木 tree')],
                       [('hanzi-cell', '应'), ('pinyin-cell', 'yīng'), ('english-cell', 'should'), ('pinyin-cell', '广')],
                       [('hanzi-cell', '该'), ('pinyin-cell', 'gāi'), ('english-cell', 'should'), ('pinyin-cell', '讠 speech')]]) +
              b_callout('warn', 'This is a test question',
                        'The unit test asks you to <b>write the radical and its meaning</b>. '
                        'That is exactly the last column.')))

    S.append(('13-pattern-yinggai', 'I Do · 句型 应该', '10–20 MIN · I DO', '句型 · 应该',
              b_pattern('主语 + <b>应该</b> + 动词',
                        '应该 goes BEFORE the verb — never after it.',
                        [{'cn': '你应该每天吃蔬菜。', 'en': 'You should eat vegetables every day.'},
                         {'cn': '今天很冷，你应该穿大衣。', 'en': "It's cold today — you should wear a coat."},
                         {'cn': '妈妈说我应该每天吃青菜。', 'en': 'Mum says I should eat green vegetables every day.'},
                         {'cn': '老师说我们不应该一边做作业一边听音乐。',
                          'en': 'Negative, reported, and carrying 一边…一边… from Unit 3.', 'hard': True}])))

    S.append(('14-pattern-dengdeng', 'I Do · 句型 等等', '10–20 MIN · I DO', '句型 · 等等',
              b_pattern('A、B、C <b>等等</b>。',
                        'Items separated by 、 — then the list is closed with 等等.',
                        [{'cn': '我喜欢吃黄瓜、土豆、生菜等等。',
                          'en': 'I like cucumber, potato, lettuce and so on.'},
                         {'cn': '老师说我们应该多吃青菜、菜花儿、西红柿等等。',
                          'en': 'Both structures in one sentence.', 'hard': True}]) +
              b_callout('warn', 'Common mistake',
                        '等等 needs a <b>list</b> in front of it. 我应该吃青菜等等。 on its own is wrong — '
                        'one item is not a list.')))

    S.append(('15-act1', 'Activity 1 · 完成句子 finish the advice', '20–43 MIN · WE DO', '活动一 · 完成句子 · 7 min',
              b_task('Activity 1 · Finish the advice — textbook p.91 Ex.2', 'Whiteboards · hold up after each · 7 minutes',
                     ['Complete each stem in characters.',
                      'Hold up after each one — two answers read aloud before we move on.',
                      'Items 3 and 5 must use food vocabulary from this unit.'],
                     {'text': 'Write all five in your book as <b>two-clause</b> sentences that give the reason '
                              'as well as the advice. Then write one more stem for a partner to complete.',
                      'cn': '今天很冷，你应该穿大衣，可是不应该穿短裤。'},
                     cn_lines=['1. 今天很冷，你应该 ____________ 。',
                               '2. 北京现在是冬天，你应该 ____________ 。',
                               '3. 妈妈说我应该 ____________ 。',
                               '4. 不要看电视了，你应该 ____________ 。',
                               '5. 周末你应该 ____________ 。'])))

    S.append(('16-act2', 'Activity 2 · 翻译 translation (You Do)', '20–43 MIN · YOU DO', '活动二 · 翻译 · 8 min',
              b_task('Activity 2 · Translate into English — 练习册 Ex.7', 'In your books · 8 minutes',
                     ['Translate all six sentences into English.',
                      'Then "It is your turn!" — two sentences of your own using 应该.'],
                     {'text': 'Translate the <b>other way</b> too, sheet turned over: '
                              '"The doctor said I should eat green vegetables, cauliflower, tomatoes and so on." '
                              'Every item on the list, closed with 等等.'},
                     cn_lines=['1. 今天很冷，你应该多穿点儿衣服。',
                               '2. 妈妈说我应该每天吃水果和蔬菜。',
                               '3. 爸爸说我应该每天做两个小时作业。',
                               '4. 老师说我应该多看中文小说。',
                               '5. 老师说我应该多学一门外语。',
                               '6. 我感冒了，医生说我应该多休息、多睡觉。'])))

    S.append(('17-game', 'Game · 排句子 Sentence Jumble', '20–43 MIN · GAME', '游戏 · 排句子 · 8 min',
              b_task('Game · 排句子 Sentence Jumble', 'Pairs · one envelope each · 8 minutes',
                     ['Rebuild each of the six jumbled sentences and write it down.',
                      'All six contain 应该 or a list closed with 等等.',
                      'First pair with all six correct wins.'],
                     {'text': 'Strips face down — you may only turn over <b>three at a time</b>, so the rest '
                              'has to be held in memory. Then cut up two sentences of your own and swap with '
                              'the next pair.'},
                     cn_lines=['我们 / 吃 / 每天 / 水果 / 应该。',
                               '说 / 妈妈 / 应该 / 我 / 每天 / 吃 / 蔬菜。',
                               '非常 / 我 / 吃 / 喜欢 / 青菜。',
                               '等等 / 我 / 喜欢 / 吃 / 黄瓜、土豆、生菜。',
                               '不 / 一边 / 应该 / 听音乐 / 你 / 一边 / 做作业。'])))

    S.append(('18-plenary', 'Plenary · exit ticket & preview', '43–50 MIN · PLENARY', '小结 · plenary',
              b_plenary(['I can use 应该 to give advice',
                         "I can report someone else's advice",
                         'I can list things and close the list with 等等',
                         'I can use 非常 to say I like something a lot'],
                        {'text': 'Translate into Chinese, on a slip:',
                         'cn': '"Mum says I should eat vegetables every day."'},
                        'We put a "but" in the middle — 可是 — and read the whole Text 1 dialogue.')))
    return S


def lesson3():
    S = []
    S.append(('01-title', 'Title · 可是 But', 'Lesson 3 of 6', 'Y8 · Lesson 10',
              b_title('轻松学中文 2 · Unit 4 · Lesson 10',
                      '可是', 'But · Text 1 · the supermarket project',
                      'Lesson 3 of 6 · 50 minutes · 课本 p.90, 93–94',
                      ['shucai', 'caihuar', 'xihongshi', 'qingcai'])))

    S.append(('02-review', 'Review · listen and choose (p.92 Ex.4)', '0–8 MIN · REVIEW', '复习 · 听力 listen and choose',
              b_label('听一听，选一选 · The teacher reads each dialogue twice — 课本 p.92') +
              b_table(['#', '句子', 'a', 'b', 'c'],
                      [[('pinyin-cell', '1'), ('hanzi-cell', '美文应该每天____'), ('english-cell', '吃蔬菜'), ('english-cell', '弹钢琴'), ('english-cell', '画画儿')],
                       [('pinyin-cell', '2'), ('hanzi-cell', '小明应该每天____'), ('english-cell', '拉小提琴'), ('english-cell', '说汉语'), ('english-cell', '弹钢琴')],
                       [('pinyin-cell', '3'), ('hanzi-cell', '大生应该每天____'), ('english-cell', '做作业'), ('english-cell', '读书'), ('english-cell', '跑步')],
                       [('pinyin-cell', '4'), ('hanzi-cell', '京京差不多每天吃__'), ('english-cell', '菜花儿'), ('english-cell', '生菜'), ('english-cell', '西红柿')],
                       [('pinyin-cell', '5'), ('hanzi-cell', '东东不应该一边做作业一边__'), ('english-cell', '唱歌'), ('english-cell', '看电视'), ('english-cell', '听音乐')],
                       [('pinyin-cell', '6'), ('hanzi-cell', '他妈妈不应该一边开车一边__'), ('english-cell', '睡觉'), ('english-cell', '打电话'), ('english-cell', '看杂志')]])))

    S.append(('02b-review-answers', 'Review · answers', '0–8 MIN · REVIEW', '复习 · 答案 answers',
              b_label('答案 · Answers — the correct option in green') +
              b_opts([('1', 'a · 吃蔬菜'), ('2', 'c · 弹钢琴'), ('3', 'b · 读书'),
                      ('4', 'b · 生菜'), ('5', 'c · 听音乐'), ('6', 'b · 打电话')],
                     correct=[0, 1, 2, 3, 4, 5]) +
              b_callout('warn', 'Correct the teacher · 改错',
                        'Two sentences, each wrong in one way. Fix them on your whiteboard.',
                        '① 我吃应该蔬菜。　② 妈妈说我每天应该吃青菜等等。') +
              b_callout('tip', 'Connection · 今天',
                        'Items 1 and 5 used a word we have not taught yet — the one that lets you push back.',
                        '……，可是……')))

    S.append(('03-li-sc', 'Learning Intention & Success Criteria', '8–10 MIN', '学习目标',
              b_lisc('We are learning to join two contrasting ideas with 可是, '
                     'and to read the whole Text 1 dialogue about vegetables.',
                     [{'en': 'I can use 可是 to join two clauses that disagree',
                       'cn': '我不太喜欢吃菜花儿，可是妈妈说我应该吃。'},
                      {'en': 'I can read Text 1 aloud with a partner and answer questions about it',
                       'cn': '你喜欢吃什么蔬菜？'},
                      {'en': 'I can write the simple characters 食、果、欠、石', 'cn': '食 · 果 · 欠 · 石'},
                      {'en': 'I can hear and mark the tones on ie and üe syllables', 'cn': 'ie · üe'}])))

    S.append(('04-c1-words', 'Cycle 1 · A — 可是', '10–20 MIN · I DO', '生词 · Cycle 1 of 1',
              b_words([{'hanzi': '可是', 'pinyin': 'kěshì', 'english': 'but'}])))
    S.append(('05-c1-examples', 'Cycle 1 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 1 of 1',
              b_examples([
                  {'py': 'Wǒ bú tài xǐhuan chī càihuār, kěshì wǒ měi tiān dōu chī.',
                   'cn': '我不太喜欢吃菜花儿，<b>可是</b>我每天都吃。',
                   'en': "I don't much like cauliflower, but I eat it every day."},
                  {'py': 'Wǒ fēicháng xǐhuan chī tǔdòu, kěshì māma shuō wǒ yīnggāi duō chī qīngcài.',
                   'cn': '我非常喜欢吃土豆，<b>可是</b>妈妈说我应该多吃青菜。',
                   'en': 'I really like potatoes, but Mum says I should eat more green vegetables.'},
                  {'py': 'Wǒ bú tài xǐhuan chī shūcài, kěshì wǒ māma shuō wǒ yīnggāi měi tiān chī.',
                   'cn': '我不太喜欢吃蔬菜，<b>可是</b>我妈妈说我应该每天吃。',
                   'en': 'Straight out of Text 1 — the line you are about to read.', 'both': True}])))
    S.append(('06-c1-write', 'Cycle 1 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 1 of 1',
              b_write(['我不太喜欢 ____________ ，', '可是 ____________ 。'],
                      '90 seconds. Both halves. The second half must disagree with the first.',
                      {'text': 'Three clauses, not two. Then write a second one where the <b>second</b> '
                              'clause is the positive.',
                       'cn': '我非常喜欢吃西红柿，可是我不喜欢吃菜花儿，妈妈说我应该都吃。'})))

    S.append(('07-characters', '简单字 · 食 果 欠 石', '10–20 MIN · I DO', '简单字 · simple characters',
              b_label('简单字 · Learn the simple characters — 课本 p.94') +
              b_summary(['食', '果', '欠', '石'], cols=4, label='') +
              b_table(['汉字', '拼音', 'English', '笔画 strokes'],
                      [[('hanzi-cell', '食'), ('pinyin-cell', 'shí'), ('english-cell', 'food'), ('english-cell', '9')],
                       [('hanzi-cell', '果'), ('pinyin-cell', 'guǒ'), ('english-cell', 'fruit'), ('english-cell', '8')],
                       [('hanzi-cell', '欠'), ('pinyin-cell', 'qiàn'), ('english-cell', 'owe'), ('english-cell', '4')],
                       [('hanzi-cell', '石'), ('pinyin-cell', 'shí'), ('english-cell', 'stone'), ('english-cell', '5')]]) +
              b_callout('tip', 'Why now?',
                        '果 turns up inside 苹果 and 水果 in two lessons. 食 is the source of the 饣 radical '
                        'you meet in Lesson 11. The book teaches them here on purpose.')))

    S.append(('08-text1', '课文一 · Text 1', '10–20 MIN · I DO', '课文一 · Text 1 · p.90',
              b_dialogue([
                  {'who': 'A', 'py': 'Nǐ xǐhuan chī shūcài ma?', 'cn': '你喜欢吃蔬菜吗？'},
                  {'who': 'B', 'py': 'Wǒ fēicháng xǐhuan chī.', 'cn': '我非常喜欢吃。'},
                  {'who': 'A', 'py': 'Nǐ xǐhuan chī shénme shūcài?', 'cn': '你喜欢吃什么蔬菜？'},
                  {'who': 'B', 'py': 'Wǒ xǐhuan chī huángguā、càihuār、tǔdòu、shēngcài、xīhóngshì děngděng. Nǐ ne?',
                   'cn': '我喜欢吃黄瓜、菜花儿、土豆、生菜、西红柿等等。你呢？'},
                  {'who': 'A', 'py': 'Wǒ bú tài xǐhuan chī. Kěshì wǒ māma shuō wǒ yīnggāi měi tiān chī shūcài.',
                   'cn': '我不太喜欢吃。<b>可是</b>我妈妈说我应该每天吃蔬菜。'}],
                  label='课文一 · Text 1 — 课本 p.90')))

    S.append(('09-text1-q', '课文一 · 问题 comprehension', '10–20 MIN · I DO', '课文一 · 问题 questions',
              b_label('回答问题 · Answer in Chinese if you can — English if you stall') +
              b_task('', None,
                     ['B 喜欢吃蔬菜吗？',
                      'B 喜欢吃什么蔬菜？ — name at least three.',
                      'A 为什么每天吃蔬菜？'],
                     None) +
              b_callout('note', 'Look for these three things',
                        'The degree word (非常). The list closed with 等等. And the 可是 that turns the '
                        'whole dialogue around at the end.')))

    S.append(('10-act1', 'Activity 1 · 课文对读 Text 1 in pairs', '20–43 MIN · WE DO', '活动一 · 对读 · 5 min',
              b_task('Activity 1 · Text 1 in pairs — We Do', 'Pairs · 5 minutes',
                     ['Read the dialogue aloud, A and B, from the handout with pinyin.',
                      'Swap roles and read it again — handout turned over, characters only on screen.',
                      'Listen for 蔬 (shū, not shù) and the neutral tone on 什么.'],
                     {'text': 'Perform it from memory with one substitution: B names <b>three different</b> '
                              'vegetables, and A\'s last line changes who gave the advice — 爸爸说 / 老师说 / 医生说. '
                              'No handout at all.'})))

    S.append(('11-act2', 'Activity 2 · 可是 完成句子', '20–43 MIN · YOU DO', '活动二 · 完成句子 · 5 min',
              b_task('Activity 2 · Complete with 可是 — textbook p.93 Ex.7', 'In your books · 5 minutes',
                     ['Complete four of these in characters.', 'Two answers read aloud for each.'],
                     {'text': 'Complete all seven, and make the second clause of each one <b>longer</b> than '
                              'the first — it must contain a time expression or a second verb. Then flip two of '
                              'them so the negative is in the second clause.',
                      'cn': '我很喜欢吃土豆，可是妈妈说我不应该每天吃。'},
                     cn_lines=['1. 我不太喜欢运动，可是 ____________ 。',
                               '2. 我不太喜欢看电视，可是 ____________ 。',
                               '3. 我不喜欢做作业，可是 ____________ 。',
                               '4. 我不太喜欢吃蔬菜，可是 ____________ 。'])))

    S.append(('12-act3', 'Activity 3 · 超市 supermarket project', '20–43 MIN · YOU DO', '活动三 · 超市 project · 10 min',
              b_task('Activity 3 · The supermarket project — textbook p.94 Ex.8', 'A4 paper · 10 minutes',
                     ['Draw the vegetable section of the supermarket near your home.',
                      'Label every vegetable in Chinese characters. <b>Minimum six labels.</b>',
                      'At least four must be words from this unit — use the Extra Words for the rest.',
                      'Last two minutes: gallery walk. Find one vegetable on someone else\'s drawing '
                      'that is not on yours.'],
                     {'text': 'Label ten, and add a caption line under the drawing using <b>both</b> of '
                              'this lesson\'s structures.',
                      'cn': '我们家附近的超市有青菜、南瓜、生菜、西红柿等等。<br>我非常喜欢吃西红柿，可是我不喜欢吃南瓜。'})))

    S.append(('13-game', 'Game · 声调 tone-mark race (ie / üe)', '20–43 MIN · GAME', '游戏 · 声调 · 3 min',
              b_label('拼音 · Add the tone marks — 课本 p.93 Ex.6 · Practice focus: ie · üe') +
              b_opts([('1', 'jiejue'), ('2', 'xiejue'), ('3', 'queqie'),
                      ('4', 'jielue'), ('5', 'juelie'), ('6', 'jieyue')]) +
              b_callout('note', 'How it runs',
                        'Teacher reads each syllable twice. Write it with the tone marks and hold up. '
                        'One point per correct board.')))

    S.append(('13b-game-answers', 'Game · answers', '20–43 MIN · GAME', '游戏 · 答案 answers',
              b_opts([('1', 'jiějué'), ('2', 'xièjué'), ('3', 'quèqiè'),
                      ('4', 'jiélüè'), ('5', 'juéliè'), ('6', 'jiéyuē')],
                     label='答案 · Answers', correct=[0, 1, 2, 3, 4, 5]) +
              b_callout('tip', 'Harder version',
                        'Write the syllable <b>and</b> one character you know containing that sound — '
                        '解、谢、月. Or take the teacher\'s job and read the syllables to the class yourself.')))

    S.append(('14-plenary', 'Plenary · exit ticket & preview', '43–50 MIN · PLENARY', '小结 · plenary',
              b_plenary(['I can use 可是 to join two clauses that disagree',
                         'I can read Text 1 aloud and answer questions about it',
                         'I can write 食、果、欠、石',
                         'I can mark the tones on ie and üe syllables'],
                        {'text': 'Both blanks filled, in characters:',
                         'cn': '我不太喜欢吃 ____________ ，可是 ____________ 。'},
                        'We leave the vegetables and start on fruit — 水果.')))
    return S


def lesson4():
    S = []
    S.append(('01-title', 'Title · 水果 Fruits', 'Lesson 4 of 6', 'Y8 · Lesson 10',
              b_title('轻松学中文 2 · Unit 4 · Lesson 10',
                      '水果', 'Fruits · and 都 covering a list',
                      'Lesson 4 of 6 · 50 minutes · 课本 p.95–96',
                      ['shuiguo', 'pingguo', 'xiangjiao', 'juzi'])))

    S.append(('02-review', 'Review · 阅读 reading (WB Ex.6)', '0–8 MIN · REVIEW', '复习 · 阅读 reading',
              b_label('阅读 · Read it together — 练习册 Ex.6') +
              b_dialogue([
                  {'who': '一', 'cn': '在天喜家里，他妈妈做饭。我非常喜欢吃她做的饭。她有时候做西餐，有时候做中餐。'},
                  {'who': '二', 'cn': '她在花园里种了黄瓜、土豆和西红柿。她用这些蔬菜做沙拉，非常好吃。'},
                  {'who': '三', 'cn': '我以前不喜欢吃蔬菜，<b>但是</b>现在我喜欢吃了。'}], label='') +
              b_callout('note', '但是 = 可是',
                        'Same job, different word. The test will use either one.')))

    S.append(('02b-review-answers', 'Review · true or false', '0–8 MIN · REVIEW', '复习 · 对还是错 true or false',
              b_task('对还是错？ · True or false — on your whiteboards', None,
                     ['天喜家里妈妈做饭。 → <b>对</b>',
                      '他妈妈每天做西餐，她不会做中餐。 → <b>错</b> · 有时候做西餐，有时候做中餐',
                      '她在花园里种了黄瓜和菜花儿。 → <b>错</b> · 黄瓜、土豆和西红柿',
                      '我现在还是不喜欢吃蔬菜。 → <b>错</b> · 现在我喜欢吃了'], None) +
              b_callout('tip', 'Connection · 今天',
                        'Three lessons on vegetables. Same sentences, new food — today it is fruit 水果, '
                        'and a word that lets you say you like <b>all</b> of something.')))

    S.append(('03-li-sc', 'Learning Intention & Success Criteria', '8–10 MIN', '学习目标',
              b_lisc('We are learning to name fruits in Chinese and to say we like '
                     'a whole group of things using 都.',
                     [{'en': 'I can say and write four fruits in Chinese', 'cn': '水果 · 苹果 · 香蕉 · 橘子'},
                      {'en': 'I can ask what fruit someone likes', 'cn': '你喜欢吃什么水果？'},
                      {'en': 'I can use 都 to cover a list', 'cn': '苹果、香蕉、橘子，我都喜欢吃。'},
                      {'en': 'I can sort food words into vegetables and fruits', 'cn': '蔬菜 / 水果'}])))

    S.append(('04-c1-words', 'Cycle 1 · A — 水果 / 苹果', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_words([{'hanzi': '水果', 'pinyin': 'shuǐguǒ', 'english': 'fruit', 'img': 'shuiguo'},
                       {'hanzi': '苹果', 'pinyin': 'píngguǒ', 'english': 'apple', 'img': 'pingguo', 'trad': '蘋果'}])))
    S.append(('05-c1-examples', 'Cycle 1 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_examples([
                  {'py': 'Wǒ měi tiān dōu chī shuǐguǒ.', 'cn': '我每天都吃<b>水果</b>。',
                   'en': 'I eat fruit every day.'},
                  {'py': 'Wǒ fēicháng xǐhuan chī píngguǒ.', 'cn': '我非常喜欢吃<b>苹果</b>。',
                   'en': 'I really like eating apples.'},
                  {'py': 'Píngguǒ shì wǒ zuì xǐhuan de shuǐguǒ.', 'cn': '<b>苹果</b>是我最喜欢的<b>水果</b>。',
                   'en': 'Apples are my favourite fruit.', 'both': True}]) +
              b_callout('note', 'Look at 果',
                        'You wrote 果 as a simple character last lesson. It is the same character doing '
                        'the same job inside both of today\'s words.')))
    S.append(('06-c1-write', 'Cycle 1 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_write(['我 ______ 喜欢吃苹果。', '我每天 ______ 吃水果。'],
                      '60 seconds. Mini whiteboards.',
                      {'text': 'Two clauses joined with 可是 — then say which fruit you <b>do</b> like, '
                              'in the same sentence.',
                       'cn': '我每天都吃水果，可是我不太喜欢吃苹果。'})))

    S.append(('07-c2-words', 'Cycle 2 · A — 香蕉 / 橘子', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_words([{'hanzi': '香蕉', 'pinyin': 'xiāngjiāo', 'english': 'banana', 'img': 'xiangjiao'},
                       {'hanzi': '橘子', 'pinyin': 'júzi', 'english': 'tangerine', 'img': 'juzi'}])))
    S.append(('08-c2-examples', 'Cycle 2 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_examples([
                  {'py': 'Xiāngjiāo shì huángsè de.', 'cn': '<b>香蕉</b>是黄色的。', 'en': 'Bananas are yellow.'},
                  {'py': 'Wǒ māma xǐhuan chī júzi.', 'cn': '我妈妈喜欢吃<b>橘子</b>。',
                   'en': 'My mum likes eating tangerines.'},
                  {'py': 'Xiāngjiāo hé júzi wǒ dōu xǐhuan chī.', 'cn': '<b>香蕉</b>和<b>橘子</b>我都喜欢吃。',
                   'en': 'I like both bananas and tangerines.', 'both': True}])))
    S.append(('09-c2-write', 'Cycle 2 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_write(['______ 和 ______ 我都喜欢吃。'],
                      '60 seconds. Both blanks, in characters.',
                      {'text': 'Write about <b>three people</b> — you, someone at home, and a friend — '
                              'one sentence each, and make the three sentences disagree with each other.',
                       'cn': '我喜欢吃香蕉，可是我妹妹不喜欢吃。'})))

    S.append(('10-recall', 'Checkpoint · 认字 recall', '10–20 MIN · I DO', '认字 · checkpoint',
              b_recall(['水果', '苹果', '香蕉', '橘子'], cols=4) +
              b_recall(['蔬菜', '生菜', '黄瓜', '土豆', '菜花儿', '西红柿'], cols=3,
                       label='…… and last week\'s six. Read all ten back.')))

    S.append(('11-copy', '写字 · copy the new words (WB Ex.9)', '10–20 MIN · I DO', '写字 · character copying',
              b_label('写字 · Copy the Text 2 new words — stroke order on the board') +
              b_table(['汉字', '拼音', 'English', '部首 radical · why'],
                      [[('hanzi-cell', '苹'), ('pinyin-cell', 'píng'), ('english-cell', 'apple'), ('pinyin-cell', '艹 · a plant')],
                       [('hanzi-cell', '香'), ('pinyin-cell', 'xiāng'), ('english-cell', 'fragrant'), ('pinyin-cell', '禾 · grain')],
                       [('hanzi-cell', '蕉'), ('pinyin-cell', 'jiāo'), ('english-cell', 'broadleaf plants'), ('pinyin-cell', '艹 · 15 strokes')],
                       [('hanzi-cell', '橘'), ('pinyin-cell', 'jú'), ('english-cell', 'tangerine'), ('pinyin-cell', '木 · grows on a tree')]]) +
              b_callout('tip', 'Extra Words · recognition only',
                        '葡萄 pútao grapes · 李子 lǐzi plum · 桃子 táozi peach · 草莓 cǎoméi strawberry')))

    S.append(('12-pattern', 'I Do · 句型 都 covering a list', '10–20 MIN · I DO', '句型 · 都',
              b_pattern('A、B、C，我<b>都</b>喜欢吃。',
                        'The list comes first — then 都 — then the verb.',
                        [{'cn': '苹果、香蕉、橘子，我都喜欢吃。',
                          'en': 'Apples, bananas, tangerines — I like them all.'},
                         {'cn': '这些水果我都不喜欢吃。', 'en': "I don't like any of these fruits."},
                         {'cn': '我每天都吃水果。', 'en': '都 with a time word, not a list.'},
                         {'cn': '苹果、香蕉、橘子，我都喜欢吃，可是我最喜欢吃苹果。',
                          'en': 'The list, 都, 可是, and a superlative — the hardest one.', 'hard': True}]) +
              b_callout('warn', 'Common mistake',
                        '我都喜欢吃苹果。 is wrong. 都 needs a <b>plural set</b> in front of it, not one item.')))

    S.append(('13-summary', '词汇总览 · summary board', '20–43 MIN · WE DO', '词汇总览 · stays on screen',
              b_summary([('水果', 'shuiguo'), ('苹果', 'pingguo'), ('香蕉', 'xiangjiao'), ('橘子', 'juzi'),
                         ('蔬菜', 'shucai'), ('生菜', 'shengcai'), ('黄瓜', 'huanggua'), ('土豆', 'tudou'),
                         ('菜花儿', 'caihuar'), ('西红柿', 'xihongshi')], cols=5)))

    S.append(('14-task', 'Activity 1 · 分类 sort all ten (We Do)', '20–43 MIN · WE DO', '活动一 · 分类 sorting · 6 min',
              b_task('Activity 1 · Sort all ten — 练习册 Ex.10', 'Pairs · three columns · 6 minutes',
                     ['Sort every word into 蔬菜 / 水果 / 运动. Write them in characters.',
                      'Two of the fruits have not been taught yet — work them out. '
                      'What does the 瓜 in 西瓜 tell you?',
                      'Then justify one placement aloud.'],
                     {'text': 'After sorting, write one sentence for <b>each</b> column using at least three '
                              'words from it and closing with 等等. Then a fourth sentence using 都 across '
                              'two columns.',
                      'cn': '我喜欢吃黄瓜、青菜、土豆等等。'},
                     cn_lines=['黄瓜　青菜　苹果　游泳　香蕉　西红柿',
                               '橘子　南瓜　冬瓜　土豆　生菜　菜花儿',
                               '西瓜　梨　　篮球　跑步　网球　足球'])))

    S.append(('15-act2', 'Activity 2 · 采访 fruit interview (You Do)', '20–43 MIN · YOU DO', '活动二 · 采访 · 8 min',
              b_task('Activity 2 · Fruit interview — You Do', 'Pairs, then report · 8 minutes',
                     ['A asks: 你喜欢吃什么水果？',
                      'B must answer with <b>at least two</b> fruits and 都.',
                      'Swap. Then write one sentence about your partner in your book.'],
                     {'text': 'Interview three people, ask a follow-up each time — 你每天都吃水果吗？ '
                              '你最喜欢吃什么？ — then report the <b>whole group</b> to the class in Chinese, '
                              'with no notes.',
                      'cn': '他们都喜欢吃苹果，可是只有一个人喜欢吃橘子。'},
                     cn_lines=['你喜欢吃什么水果？', '苹果和香蕉我都喜欢吃。', '他喜欢吃香蕉和橘子。'])))

    S.append(('16-game', 'Game · Quizlet Live', '20–43 MIN · GAME', '游戏 · Quizlet Live · 9 min',
              b_task('Game · Quizlet Live', 'Devices out · two rounds · 9 minutes',
                     ['Round 1 — characters prompt English.',
                      'Round 2 — English prompts characters.',
                      'Ten words in the set: today\'s four fruits and last week\'s six vegetables.'],
                     {'text': 'Round 2 runs with pinyin hidden entirely, and adds the four Extra Words '
                              '(葡萄, 李子, 桃子, 草莓). If your team finishes first, write two extra terms for '
                              'the class set on the board before the next round starts.'}) +
              b_recall(['水果', '苹果', '香蕉', '橘子'], cols=4, label='')))

    S.append(('17-plenary', 'Plenary · exit ticket & preview', '43–50 MIN · PLENARY', '小结 · plenary',
              b_plenary(['I can say and write four fruits in Chinese',
                         'I can ask 你喜欢吃什么水果？',
                         'I can use 都 to cover a list',
                         'I can sort food words into vegetables and fruits'],
                        {'text': 'Complete it, then add one more sentence naming your favourite:',
                         'cn': '苹果、香蕉、橘子，我都 __________ 。'},
                        'Two more fruits, the word 这些, and the whole Text 2 dialogue.')))
    return S


def lesson5():
    S = []
    S.append(('01-title', 'Title · 这些 These', 'Lesson 5 of 6', 'Y8 · Lesson 10',
              b_title('轻松学中文 2 · Unit 4 · Lesson 10',
                      '这些', 'These · 西瓜 · 梨 · Text 2',
                      'Lesson 5 of 6 · 50 minutes · 课本 p.95, 99',
                      ['xigua', 'li', 'pingguo', 'xiangjiao', 'juzi'])))

    S.append(('02-review', 'Review · 都 and the four fruits', '0–8 MIN · REVIEW', '复习 · 认字 flashcards',
              b_recall(['水果', '苹果', '香蕉', '橘子', '蔬菜', '生菜', '黄瓜', '土豆', '西红柿'],
                       cols=3, label='认字 · Pinyin and English, chorally — then again at double speed') +
              b_callout('tip', 'Then one question on your whiteboards',
                        'Answer in a full sentence with 都.', '苹果、香蕉、橘子，你都喜欢吃吗？')))

    S.append(('03-li-sc', 'Learning Intention & Success Criteria', '8–10 MIN', '学习目标',
              b_lisc('We are learning to use 这些 / 那些 / 一些 to talk about groups of things, '
                     'and to read the Text 2 dialogue about fruit.',
                     [{'en': 'I can say and write 西瓜 and 梨', 'cn': '西瓜 · 梨'},
                      {'en': 'I can use 这些、那些、一些 with a noun', 'cn': '我不喜欢吃这些水果。'},
                      {'en': 'I can read Text 2 aloud with a partner and answer questions about it',
                       'cn': '你喜欢吃什么水果？'},
                      {'en': 'I can ask who something belongs to', 'cn': '这些是谁的？'}])))

    S.append(('04-c1-words', 'Cycle 1 · A — 西瓜 / 梨', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_words([{'hanzi': '西瓜', 'pinyin': 'xīguā', 'english': 'watermelon', 'img': 'xigua'},
                       {'hanzi': '梨', 'pinyin': 'lí', 'english': 'pear', 'img': 'li'}])))
    S.append(('05-c1-examples', 'Cycle 1 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_examples([
                  {'py': 'Wǒ fēicháng xǐhuan chī xīguā.', 'cn': '我非常喜欢吃<b>西瓜</b>。',
                   'en': 'I really like eating watermelon.'},
                  {'py': 'Lí hé píngguǒ wǒ dōu xǐhuan chī.', 'cn': '<b>梨</b>和苹果我都喜欢吃。',
                   'en': 'I like both pears and apples.'},
                  {'py': 'Wǒ xǐhuan chī xīguā hé lí.', 'cn': '我喜欢吃<b>西瓜</b>和<b>梨</b>。',
                   'en': 'Straight out of Text 2 — the line you are about to read.', 'both': True}])))
    S.append(('06-c1-write', 'Cycle 1 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 1 of 2',
              b_write(['我 ______ 喜欢吃西瓜。', '______ 和 ______ 我都喜欢吃。'],
                      '60 seconds. Mini whiteboards.',
                      {'text': 'Two clauses with 可是, <b>both</b> new words in the same sentence — '
                              'then add when you eat it.',
                       'cn': '我非常喜欢吃西瓜，可是我不太喜欢吃梨。夏天我每天都吃西瓜。'})))

    S.append(('07-c2-words', 'Cycle 2 · A — 这些', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_words([{'hanzi': '这些', 'pinyin': 'zhèxiē', 'english': 'these'}])))
    S.append(('08-c2-examples', 'Cycle 2 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_examples([
                  {'py': 'Zhèxiē shuǐguǒ hěn hǎo.', 'cn': '<b>这些</b>水果很好。', 'en': 'These fruits are good.'},
                  {'py': 'Wǒ bù xǐhuan chī zhèxiē shuǐguǒ.', 'cn': '我不喜欢吃<b>这些</b>水果。',
                   'en': "I don't like eating these fruits."},
                  {'py': 'Zhèxiē shuǐguǒ wǒ dōu bù xǐhuan chī, kěshì wǒ xǐhuan chī xīguā hé lí.',
                   'cn': '<b>这些</b>水果我都不喜欢吃，可是我喜欢吃西瓜和梨。',
                   'en': 'Both cycles in one sentence.', 'both': True}]) +
              b_callout('warn', 'Common mistake',
                        '这些个水果 is wrong — 些 is <b>already</b> the measure word. Never add 个 after it.')))
    S.append(('09-c2-write', 'Cycle 2 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 2 of 2',
              b_write(['这些 ________ 我 ________ 喜欢。'],
                      '60 seconds. Characters, not pinyin.',
                      {'text': 'Three sentences — one each with 这些 / 那些 / 一些 — about three different '
                              'categories: fruit, vegetables, and something from an earlier unit '
                              '(衣服, 小说, 画儿). No word bank.'})))

    S.append(('10-recall', 'Checkpoint · 认字 recall', '10–20 MIN · I DO', '认字 · checkpoint',
              b_recall(['西瓜', '梨', '这些', '苹果', '香蕉', '橘子'], cols=3)))

    S.append(('11-wordfamily', '词族 · the 瓜 and 菜 families', '10–20 MIN · I DO', '词族 · word families',
              b_label('词族 · A shared character is a shared category — 练习册 Ex.11') +
              b_table(['瓜 family', '拼音', 'English'],
                      [[('hanzi-cell', '西瓜'), ('pinyin-cell', 'xīguā'), ('english-cell', 'watermelon')],
                       [('hanzi-cell', '冬瓜'), ('pinyin-cell', 'dōngguā'), ('english-cell', 'winter melon')],
                       [('hanzi-cell', '南瓜'), ('pinyin-cell', 'nánguā'), ('english-cell', 'pumpkin')]]) +
              b_table(['菜 family', '拼音', 'English'],
                      [[('hanzi-cell', '青菜'), ('pinyin-cell', 'qīngcài'), ('english-cell', 'green vegetable')],
                       [('hanzi-cell', '生菜'), ('pinyin-cell', 'shēngcài'), ('english-cell', 'lettuce')],
                       [('hanzi-cell', '菜花儿'), ('pinyin-cell', 'càihuār'), ('english-cell', 'cauliflower')]])))

    S.append(('12-text2', '课文二 · Text 2', '10–20 MIN · I DO', '课文二 · Text 2 · p.95',
              b_dialogue([
                  {'who': 'A', 'py': 'Nǐ xǐhuan chī shénme shuǐguǒ?', 'cn': '你喜欢吃什么水果？'},
                  {'who': 'B', 'py': 'Píngguǒ、xiāngjiāo、júzi, wǒ dōu xǐhuan chī.',
                   'cn': '苹果、香蕉、橘子，我都喜欢吃。'},
                  {'who': 'A', 'py': 'Wǒ bù xǐhuan chī zhèxiē shuǐguǒ. Wǒ xǐhuan chī xīguā hé lí.',
                   'cn': '我不喜欢吃<b>这些</b>水果。我喜欢吃<b>西瓜</b>和<b>梨</b>。'},
                  {'who': 'B', 'py': 'Nǐ měi tiān dōu chī shuǐguǒ ma?', 'cn': '你每天都吃水果吗？'},
                  {'who': 'A', 'py': 'Wǒ měi tiān dōu chī liǎng sān zhǒng shuǐguǒ.',
                   'cn': '我每天都吃两三种水果。'}],
                  label='课文二 · Text 2 — 课本 p.95')))

    S.append(('13-text2-q', '课文二 · 问题 comprehension', '10–20 MIN · I DO', '课文二 · 问题 questions',
              b_label('回答问题 · Answer in Chinese') +
              b_task('', None,
                     ['B 喜欢吃什么水果？',
                      'A 喜欢吃什么水果？',
                      'A 每天吃水果吗？'], None) +
              b_callout('note', 'That last line · 两三种',
                        'We are reading it today, not learning it. 两三种 is next lesson\'s whole business.')))

    S.append(('14-act1', 'Activity 1 · 课文对读 Text 2 in pairs', '20–43 MIN · WE DO', '活动一 · 对读 · 6 min',
              b_task('Activity 1 · Text 2 in pairs — We Do', 'Pairs · 6 minutes',
                     ['Read A and B aloud from the handout with pinyin.',
                      'Swap roles.',
                      'Read it a third time, handout face down, characters only on screen.',
                      'Listen for 橘 (jú, not jū) and the neutral tone on 些.'],
                     {'text': 'Perform it from memory with the fruits swapped — B names three fruits that are '
                              '<b>not</b> in the book, A rejects them with 这些 and names two others. '
                              'The last line stays as it is.'})))

    S.append(('15-act2', 'Activity 2 · 翻译 translation with 这些', '20–43 MIN · YOU DO', '活动二 · 翻译 · 8 min',
              b_task('Activity 2 · Translate into English — 练习册 Ex.15', 'In your books · 8 minutes',
                     ['Translate all four sentences.',
                      'Then two sentences of your own — one with 这些, one with 那些.'],
                     {'text': 'Translate the other way too, book closed. Then write a fifth sentence that '
                              'uses 这些 <b>and</b> 都 <b>and</b> 可是 together.',
                      'cn': '这些水果我都不喜欢吃，可是我妈妈说我应该每天吃。'},
                     cn_lines=['1. 我不喜欢吃这些水果。你们有西瓜吗？',
                               '2. 那些画儿我都不喜欢。你们有国画儿吗？',
                               '3. 这些电视节目我都不喜欢看。我们看动画片吧！',
                               '4. 我有一些衣服太小了，但是很好看。你要吗？'])))

    S.append(('16-game', 'Game · 这些是谁的？', '20–43 MIN · GAME', '游戏 · 这些是谁的 · 9 min',
              b_task('Game · 这些……是谁的？ — textbook p.99 Ex.16', 'Groups of four · cards face down · 9 minutes',
                     ['Take two cards and ask the group.',
                      'Everyone must ask at least twice.'],
                     {'text': 'The asker may <b>not</b> use the card\'s word — describe the object in Chinese '
                              'until someone names it, then ask the question. The answer must give a reason.',
                      'cn': '是小明的，因为他每天都看。'},
                     cn_lines=['A：这些小说是你的吗？　B：不是我的。',
                               'A：那是谁的？　　　　　B：是小明的。'])))
    S.append(('16b-game-cards', 'Game · the eight object cards', '20–43 MIN · GAME',
              '游戏 · 卡片 the object cards',
              b_recall(['小说', '杂志', '小人书', '画儿', '网球', '短裤', '汗衫', '衣服'],
                       cols=4, label='卡片 · Eight objects, face down in the middle')))

    S.append(('17-plenary', 'Plenary · exit ticket & preview', '43–50 MIN · PLENARY', '小结 · plenary',
              b_plenary(['I can say and write 西瓜 and 梨',
                         'I can use 这些、那些、一些 with a noun',
                         'I can read Text 2 aloud and answer questions about it',
                         'I can ask 这些是谁的？'],
                        {'text': 'Name at least three more fruits, in characters:',
                         'cn': '我家冰箱里有苹果、____________ 。'},
                        'The last lesson on this topic — how to say "two or three kinds", 两三种.')))
    return S


def lesson6():
    S = []
    S.append(('01-title', 'Title · 种 and number ranges', 'Lesson 6 of 6', 'Y8 · Lesson 10',
              b_title('轻松学中文 2 · Unit 4 · Lesson 10',
                      '两三种', 'Kinds · and approximate number ranges',
                      'Lesson 6 of 6 · 50 minutes · 课本 p.96–99',
                      ['shuiguo', 'xigua', 'li', 'shucai', 'nangua'])))

    S.append(('02-review', 'Review · Text 2 from memory + 听写', '0–8 MIN · REVIEW', '复习 · 课文二 + 简单字听写',
              b_task('复习 · Two halves', 'Pairs, then groups · 8 minutes',
                     ['<b>课文二 from memory (4 min)</b> — Text 2 is not on the screen. '
                      'Rebuild as much as you can, A and B, then swap. Who got the last line?',
                      '<b>听写 character race (4 min)</b> — textbook p.97 Ex.12. Two minutes to memorise '
                      'the twelve characters below, then books closed and the teacher dictates eight of them.'],
                     None)))
    S.append(('02b-review-chars', 'Review · 简单字 dictation grid', '0–8 MIN · REVIEW',
              '复习 · 简单字 · 听写 dictation',
              b_recall(['夕', '心', '目', '方', '平', '土', '角', '页', '食', '果', '欠', '石'],
                       cols=4,
                       label='简单字 · Two minutes to memorise — then books closed, eight dictated') +
              b_callout('warn', 'These are test characters',
                        'The unit test\'s "find the simple character" question is built from exactly this grid.')))

    S.append(('03-li-sc', 'Learning Intention & Success Criteria', '8–10 MIN', '学习目标',
              b_lisc('We are learning to say roughly how many kinds of something '
                     'there are, using 种 and number ranges like 两三、三四.',
                     [{'en': 'I can use 种 as the measure word for kinds', 'cn': '我每天吃两三种水果。'},
                      {'en': 'I can make an approximate number from two consecutive numbers',
                       'cn': '三四天 · 四五种 · 七八个'},
                      {'en': 'I can ask and answer 你每天吃几种水果？', 'cn': '你每天吃几种水果？'},
                      {'en': 'I can recognise the food vocabulary from the whole of Lesson 10',
                       'cn': '蔬菜、水果 — 十八个词'}])))

    S.append(('04-c1-words', 'Cycle 1 · A — 种', '10–20 MIN · I DO', '生词 · Cycle 1 of 1',
              b_words([{'hanzi': '种', 'pinyin': 'zhǒng', 'english': 'kind; type', 'trad': '種'}])))
    S.append(('05-c1-examples', 'Cycle 1 · B — 例句', '10–20 MIN · I DO', '生词 · Cycle 1 of 1',
              b_examples([
                  {'py': 'Wǒ měi tiān chī liǎng zhǒng shuǐguǒ.', 'cn': '我每天吃两<b>种</b>水果。',
                   'en': 'I eat two kinds of fruit every day.'},
                  {'py': 'Nǐ xǐhuan jǐ zhǒng shūcài?', 'cn': '你喜欢几<b>种</b>蔬菜？',
                   'en': 'How many kinds of vegetable do you like?'},
                  {'py': 'Wǒ měi tiān dōu chī liǎng sān zhǒng shuǐguǒ.', 'cn': '我每天都吃两三<b>种</b>水果。',
                   'en': 'The last line of Text 2 — now you know all of it.', 'both': True}])))
    S.append(('06-c1-write', 'Cycle 1 · C — 写一句', '10–20 MIN · I DO', '生词 · Cycle 1 of 1',
              b_write(['我每天吃 ______ 种水果。', '我喜欢 ______ 种蔬菜。'],
                      '60 seconds. Mini whiteboards.',
                      {'text': 'Use 种 with something that is <b>not food</b>, reaching back to earlier units — '
                              'then join the two with 除了…以外.',
                       'cn': '我会说两种语言。　我喜欢三四种运动。'})))

    S.append(('07-pattern-ranges', 'I Do · 句型 number ranges', '10–20 MIN · I DO', '句型 · 两三、三四',
              b_pattern('两三 · 三四 · 四五 · 七八',
                        'Two CONSECUTIVE numbers side by side make an approximation. Never skip a number.',
                        [{'cn': '我每天吃两三种水果。'},
                         {'cn': '我三四天没去游泳了。'},
                         {'cn': '我们家每天都吃四五种蔬菜、水果。'},
                         {'cn': '我每天都吃两三种水果，可是我妈妈说我应该吃四五种。',
                          'en': 'The range twice, plus 可是 and 应该 — the hardest one.', 'hard': True}]) +
              b_callout('warn', 'Common mistake',
                        '两四种 is wrong. The two numbers must be <b>next to each other</b>: '
                        '两三 ✓ · 三四 ✓ · 四五 ✓ · 两四 ✗')))

    S.append(('08-pattern-zhong-ge', 'I Do · 种 or 个？', '10–20 MIN · I DO', '句型 · 种 vs 个',
              b_label('种 or 个？ · kinds versus items') +
              b_table(['', '汉字', 'English'],
                      [[('pinyin-cell', 'kinds'), ('hanzi-cell', '两三种水果'), ('english-cell', 'two or three KINDS of fruit')],
                       [('pinyin-cell', 'items'), ('hanzi-cell', '两三个苹果'), ('english-cell', 'two or three APPLES')],
                       [('pinyin-cell', 'kinds'), ('hanzi-cell', '两种语言'), ('english-cell', 'two languages')],
                       [('pinyin-cell', 'ask'), ('hanzi-cell', '几种？'), ('english-cell', 'how many kinds?')]]) +
              b_callout('note', 'On your whiteboards',
                        '种 or 个？', '我买了两三 ____ 苹果。　我每天吃四五 ____ 蔬菜。')))

    S.append(('09-summary', '词汇总览 · the whole of Lesson 10', '20–43 MIN · WE DO', '词汇总览 · 十八个词 · stays on screen',
              b_summary([('蔬菜', 'shucai'), ('生菜', 'shengcai'), ('黄瓜', 'huanggua'),
                         ('土豆', 'tudou'), ('菜花儿', 'caihuar'), ('西红柿', 'xihongshi'),
                         ('青菜', 'qingcai'), ('南瓜', 'nangua'), ('水果', 'shuiguo'),
                         ('苹果', 'pingguo'), ('香蕉', 'xiangjiao'), ('橘子', 'juzi'),
                         ('西瓜', 'xigua'), ('梨', 'li')], cols=6)))
    S.append(('09b-summary-grammar', '词汇总览 · the six grammar words', '20–43 MIN · WE DO',
              '词汇总览 · 语法词 · stays on screen',
              b_recall(['应该', '非常', '等等', '可是', '这些', '种'], cols=3,
                       label='词汇总览 · The six words that are not food — read them back')))

    S.append(('10-act1', 'Activity 1 · 连一连 match the halves', '20–43 MIN · WE DO', '活动一 · 连一连 · 6 min',
              b_task('Activity 1 · Match the two halves — textbook p.97 Ex.13', 'Pairs · 6 minutes',
                     ['Match all nine. Every ending contains a number range.',
                      'Write the completed sentences in your books.'],
                     {'text': 'Rewrite three of them about <b>yourself and your own family</b>, changing both '
                              'the range and the noun. Then one sentence that uses two ranges at once.',
                      'cn': '我每天看一两个小时的电视，做三四个小时的作业。'},
                     cn_lines=['他会说 ____ · 她今年学了 ____ · 妈妈打了 ____',
                               '爸爸开了 ____ · 弟弟在家休息了 ____ · 他学了 ____',
                               '姐姐每天吃 ____ · 哥哥每天看 ____ · 妹妹每天弹 ____'])))
    S.append(('10b-act1-halves', 'Activity 1 · the nine endings', '20–43 MIN · WE DO',
              '活动一 · 下半句 the endings',
              b_opts([('a', '八九门课'), ('b', '三四个小时的车'), ('c', '两三种语言'),
                      ('d', '四五天'), ('e', '一两个小时的电话'), ('f', '三四种水果'),
                      ('g', '一两个小时的钢琴'), ('h', '五六年的油画儿'), ('i', '一两个小时的电视')],
                     label='下半句 · Every one of them contains a number range')))

    S.append(('11-act2', 'Activity 2 · 听一听，连一连 (p.98 Ex.14)', '20–43 MIN · YOU DO', '活动二 · 听力 · 7 min',
              b_label('听一听，连一连 · The teacher reads each item twice, then once slowly — 课本 p.98') +
              b_opts([('1', '大生'), ('2', '小明'), ('3', '美美'),
                      ('4', '冬冬'), ('5', '王星'), ('6', '小英')]) +
              b_opts([('a', '每天看一两个小时的电视。'), ('b', '去过七八个国家。'),
                      ('c', '三四天没去游泳了。'), ('d', '每个周末画两三个小时画儿。'),
                      ('e', '每天吃四五种蔬菜、水果。'), ('f', '病了两三天。')], cols=2)))

    S.append(('11b-act2-answers', 'Activity 2 · answers', '20–43 MIN · YOU DO', '活动二 · 答案 answers',
              b_opts([('大生', 'b · 去过七八个国家'), ('小明', 'c · 三四天没去游泳了'),
                      ('美美', 'f · 病了两三天'), ('冬冬', 'e · 每天吃四五种蔬菜、水果'),
                      ('王星', 'd · 每个周末画两三个小时画儿'), ('小英', 'a · 每天看一两个小时的电视')],
                     cols=2, label='答案 · Answers', correct=[0, 1, 2, 3, 4, 5]) +
              b_ext({'text': 'Write down the <b>whole sentence</b> you hear, not just the letter — full '
                             'characters, first listen. Then write two new items in the same format for a '
                             'partner, and read them aloud yourself.'})))

    S.append(('12-act3', 'Activity 3 · 回答问题 answer in Chinese', '20–43 MIN · YOU DO', '活动三 · 回答问题 · 4 min',
              b_task('Activity 3 · Answer in Chinese — 练习册 Ex.12', 'In your books · full sentences · 4 minutes',
                     None if False else
                     ['Full sentences, not one-word answers.',
                      'Every answer must contain 种.'],
                     {'text': 'Answer all four with a <b>range</b> rather than an exact number, and add a '
                              'second clause to each with 可是 or 除了…以外.',
                      'cn': '我今天吃了两三种水果，可是我没吃蔬菜。'},
                     cn_lines=['1. 你会说几种语言？什么语言？',
                               '2. 你喜欢做几种体育运动？什么运动？',
                               '3. 你今天吃了几种蔬菜？什么蔬菜？',
                               '4. 你今天吃了几种水果？什么水果？'])))

    S.append(('13-game', 'Game · 组词 build a phrase', '20–43 MIN · GAME', '游戏 · 组词 · 6 min',
              b_task('Game · 组词 Build a phrase — textbook p.99 Ex.17', 'Groups of four · 5 minutes',
                     ['Add one character to each to form a real phrase.',
                      'Characters if you can, pinyin if you cannot.',
                      'Most correct phrases wins.'],
                     {'text': '<b>Two</b> phrases per character, both in characters, no pinyin. And for any five '
                              'of them, write a full sentence using the phrase — those five are worth double.'},
                     cn_lines=['年__　电__　号__　多__　学__',
                               '中__　秘__　下__　上__　走__',
                               '地__　蓝__　校__　长__　汗__',
                               '毛__　喜__　起__　早__　火__'])))

    S.append(('14-plenary', 'Plenary · the whole sequence', '43–50 MIN · PLENARY', '小结 · 整课复习 plenary',
              b_plenary(['Can I name six vegetables and six fruits in characters?',
                         'Can I use 应该 to give advice?',
                         'Can I join two clauses with 可是?',
                         'Can I use 都、这些 and 种 correctly?'],
                        {'text': 'Answer in one full sentence using a number range:',
                         'cn': '你每天吃几种水果？'},
                        'Lesson 11 — 一日三餐, three meals a day. You already have the food words; '
                        'now you get the meals.')))
    return S


DECKS = [
    ('l1-vegetables-vocab', 'Lesson 1 · 蔬菜 Vegetables', lesson1),
    ('l2-yinggai-should', 'Lesson 2 · 应该 Should', lesson2),
    ('l3-keshi-text1', 'Lesson 3 · 可是 But · Text 1', lesson3),
    ('l4-fruits-vocab', 'Lesson 4 · 水果 Fruits', lesson4),
    ('l5-zhexie-text2', 'Lesson 5 · 这些 These · Text 2', lesson5),
    ('l6-zhong-ranges', 'Lesson 6 · 种 · Number ranges', lesson6),
]


# ══════════════════════════════════════════════════════════════════
#  Deck shell (index.html per lesson)
# ══════════════════════════════════════════════════════════════════

DECK_SHELL = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Y8 L10 · 蔬菜、水果 · {label}</title>
<script>
  window.DECK = [
{manifest}
  ];
</script>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{height:100%;background:#1A1D14;font-family:-apple-system,"PingFang SC",sans-serif;overflow:hidden}}
  #stage{{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}}
  #wrap{{width:1920px;height:1080px;transform-origin:center center;background:#FBFAF2;box-shadow:0 12px 70px rgba(0,0,0,.5)}}
  iframe{{width:1920px;height:1080px;border:0;display:block}}
  .zone{{position:fixed;top:0;bottom:0;width:14%;cursor:pointer;z-index:20}}
  .zone.l{{left:0}}.zone.r{{right:0}}
  .bar{{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);z-index:50;
       display:flex;align-items:center;gap:14px;background:rgba(0,0,0,.66);color:#fff;
       padding:9px 20px;border-radius:999px;font-size:13px;letter-spacing:.04em;white-space:nowrap;
       max-width:calc(100vw - 32px);overflow-x:auto}}
  .bar b{{font-variant-numeric:tabular-nums;font-weight:600}}
  .bar span{{color:rgba(255,255,255,.62)}}
  .bar button,.bar a{{background:none;border:0;color:rgba(255,255,255,.85);font:inherit;cursor:pointer;padding:0;text-decoration:none}}
  .bar button:hover,.bar a:hover{{color:#fff}}
  .bar a.home{{color:#A9C77E}}
  .bar a.home:hover{{color:#fff}}
  #grid{{position:fixed;inset:0;background:#1A1D14;z-index:40;overflow:auto;padding:36px;display:none;
        grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px;align-content:start}}
  #grid.on{{display:grid}}
  .cell{{cursor:pointer}}
  .cell .thumb{{width:100%;aspect-ratio:16/9;overflow:hidden;border-radius:8px;background:#FBFAF2;position:relative;
               border:2px solid transparent}}
  .cell:hover .thumb{{border-color:#8FB35E}}
  .cell .thumb iframe{{transform-origin:top left;pointer-events:none;position:absolute;top:0;left:0}}
  .cell p{{color:rgba(255,255,255,.74);font-size:12.5px;margin-top:8px;line-height:1.4}}
  .cell p b{{color:#A9C77E;font-weight:600;margin-right:6px}}
</style>
</head>
<body>

<div id="stage"><div id="wrap"><iframe id="fr" src="slides/{first}"></iframe></div></div>
<div class="zone l" onclick="go(-1)"></div>
<div class="zone r" onclick="go(1)"></div>

<div class="bar">
  <a class="home" href="../" title="回到课程列表 · Back to the lesson list">← 课程列表</a>
  <span>·</span>
  <button onclick="toggleGrid()">All slides</button>
  <span>·</span>
  <a href="{slug}.pptx" download>PPTX</a>
  <span>·</span>
  <b><span id="n">1</span> / {total}</b>
  <span id="lbl"></span>
</div>

<div id="grid"></div>

<script>
  const D = window.DECK; let i = 0;
  const fr = document.getElementById('fr'), wrap = document.getElementById('wrap');
  const KEY = 'y8l10-{slug}';

  function fit() {{
    const s = Math.min(window.innerWidth / 1920, (window.innerHeight - 70) / 1080);
    wrap.style.transform = 'scale(' + s + ')';
  }}
  function show(k) {{
    i = (k + D.length) % D.length;
    fr.src = 'slides/' + D[i].file;
    document.getElementById('n').textContent = i + 1;
    document.getElementById('lbl').textContent = D[i].label;
    try {{ localStorage.setItem(KEY, i); }} catch (e) {{}}
  }}
  function go(d) {{ show(i + d); }}
  function toggleGrid() {{
    const g = document.getElementById('grid');
    g.classList.toggle('on');
    if (g.classList.contains('on') && !g.dataset.built) build();
  }}
  function build() {{
    const g = document.getElementById('grid');
    D.forEach((s, k) => {{
      const c = document.createElement('div');
      c.className = 'cell';
      c.innerHTML = '<div class="thumb"><iframe src="slides/' + s.file + '" scrolling="no"></iframe></div>'
                  + '<p><b>' + (k + 1) + '</b>' + s.label + '</p>';
      c.onclick = () => {{ show(k); toggleGrid(); }};
      g.appendChild(c);
      const f = c.querySelector('iframe');
      const scale = () => {{
        const w = c.querySelector('.thumb').clientWidth;
        f.style.width = '1920px'; f.style.height = '1080px';
        f.style.transform = 'scale(' + (w / 1920) + ')';
      }};
      scale(); window.addEventListener('resize', scale);
    }});
    g.dataset.built = '1';
  }}

  addEventListener('keydown', e => {{
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{ e.preventDefault(); go(1); }}
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{ e.preventDefault(); go(-1); }}
    if (e.key === 'Home') show(0);
    if (e.key === 'End') show(D.length - 1);
    if (e.key === 'g' || e.key === 'Escape') toggleGrid();
  }});
  addEventListener('resize', fit);
  fit();
  let start = 0;
  try {{ start = parseInt(localStorage.getItem(KEY) || '0', 10) || 0; }} catch (e) {{}}
  show(start);
</script>
</body>
</html>
'''


# ══════════════════════════════════════════════════════════════════
#  Lesson-list page (the design's own index.html)
# ══════════════════════════════════════════════════════════════════

LIST_PAGE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Y8 L10 · 蔬菜、水果 Vegetables and Fruits</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@700;900&family=Noto+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  :root{{
    --bg:#FBFAF2; --bg2:#F2EFDE; --line:#E1DBC0;
    --ink:#24321C; --ink2:#4E5A42; --mute:#78805F;
    --green:#4C7A2C; --orange:#B96A12; --tomato:#B93F2C;
    --serif:'Noto Serif SC','Songti SC',serif;
    --sans:'Noto Sans','Noto Sans SC','PingFang SC',-apple-system,sans-serif;
  }}
  body{{background:var(--bg);color:var(--ink);font-family:var(--sans);
       padding:0 0 96px;line-height:1.55}}
  .topbar{{border-bottom:1px solid var(--line);padding:16px 32px;margin-bottom:56px}}
  .topbar a{{color:var(--ink2);text-decoration:none;font-size:14px}}
  .topbar a:hover{{color:var(--green)}}
  .wrap{{max-width:1120px;margin:0 auto;padding:0 32px}}
  .kicker{{font-size:13px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--orange)}}
  h1{{font-family:var(--serif);font-size:64px;font-weight:900;line-height:1.08;margin:14px 0 6px}}
  .sub{{font-family:var(--serif);font-size:27px;font-weight:700;color:var(--green)}}
  .meta{{font-size:15px;color:var(--ink2);margin-top:20px;max-width:660px}}
  .rule{{height:4px;background:var(--green);width:96px;margin:34px 0 44px;border-radius:2px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:22px}}
  a.card{{display:block;text-decoration:none;color:inherit;background:var(--bg2);
         border:2px solid var(--line);border-radius:18px;padding:26px 28px 28px;
         transition:border-color .15s, transform .15s}}
  a.card:hover{{border-color:var(--green);transform:translateY(-3px)}}
  .n{{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--orange)}}
  .t{{font-family:var(--serif);font-size:34px;font-weight:900;margin:10px 0 2px;line-height:1.2}}
  .e{{font-size:16px;color:var(--green);font-weight:500}}
  .d{{font-size:14px;color:var(--ink2);margin-top:14px}}
  .w{{margin-top:18px;padding-top:14px;border-top:1px solid var(--line);
     font-family:var(--serif);font-size:19px;font-weight:700;color:var(--ink)}}
  .w span{{color:var(--mute);font-weight:400;font-size:13px;font-family:var(--sans);
          display:block;margin-bottom:4px;letter-spacing:.1em;text-transform:uppercase}}
  .focus{{background:var(--bg2);border:2px solid var(--line);border-radius:18px;
         padding:26px 30px 30px;margin-bottom:34px}}
  .focus h2{{font-family:var(--serif);font-size:23px;font-weight:900;margin-bottom:18px}}
  .fgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}}
  .fcell{{background:var(--bg);border:1px solid var(--line);border-radius:12px;
         padding:14px 16px;text-align:center}}
  .fcell .l{{font-size:11px;font-weight:700;letter-spacing:.12em;color:var(--tomato)}}
  .fcell .p{{font-family:var(--serif);font-size:25px;font-weight:900;margin:6px 0 3px}}
  .fcell .g{{font-size:12.5px;color:var(--ink2)}}
  footer{{margin-top:56px;padding-top:26px;border-top:1px solid var(--line);
         font-size:14px;color:var(--mute);max-width:760px}}
  footer b{{color:var(--ink2)}}
</style>
</head>
<body>
<div class="topbar"><a href="../../">← Deck Gallery · 设计画廊</a></div>
<div class="wrap">
  <p class="kicker">轻松学中文 2 · Unit 4 · Lesson 10</p>
  <h1>蔬菜、水果</h1>
  <p class="sub">Vegetables and Fruits · Year 8</p>
  <p class="meta">Six 50-minute lessons. Eighteen new words spread across the sequence — four to six
  per lesson, each pair taught as a three-slide cycle: the words, then the words used, then the
  students using them. Revision happens inside every lesson rather than in a review lesson at the end.</p>
  <div class="rule"></div>
  <div class="focus">
    <h2>Grammar Focus · 本课语法点</h2>
    <div class="fgrid">
      <div class="fcell"><p class="l">L1</p><p class="p">你喜欢吃什么蔬菜？</p><p class="g">Asking preference in a category</p></div>
      <div class="fcell"><p class="l">L2</p><p class="p">应该 + 动词</p><p class="g">Should — before the verb, never after</p></div>
      <div class="fcell"><p class="l">L2</p><p class="p">A、B、C 等等</p><p class="g">Closing a list</p></div>
      <div class="fcell"><p class="l">L3</p><p class="p">……，可是……</p><p class="g">Joining two clauses that disagree</p></div>
      <div class="fcell"><p class="l">L4</p><p class="p">A、B、C，我都……</p><p class="g">都 covering a whole list</p></div>
      <div class="fcell"><p class="l">L5</p><p class="p">这些 / 那些 / 一些</p><p class="g">些 is already the measure word</p></div>
      <div class="fcell"><p class="l">L6</p><p class="p">两三种</p><p class="g">Consecutive numbers = approximation</p></div>
    </div>
  </div>
  <div class="grid">
{cards}
  </div>
  <footer>
    <p>Textbook pp.90–99 · workbook pp.108–117. Every listening exercise is written to be <b>read aloud
    by the teacher</b> — the track&nbsp;47 and track&nbsp;50 scripts are transcribed into the lesson plans,
    so the CD is not needed.</p>
  </footer>
</div>
</body>
</html>
'''

CARD = '''    <a class="card" href="{slug}/">
      <p class="n">Lesson {n} of 6</p>
      <p class="t">{hanzi}</p>
      <p class="e">{en}</p>
      <p class="d">{desc}</p>
      <p class="w"><span>New words · {count}</span>{words}</p>
    </a>'''

CARD_DATA = [
    ('l1-vegetables-vocab', 1, '蔬菜', 'Vegetables',
     'Six vegetables in three cycles, then a sorting task that needs all six and a vegetable interview.',
     '蔬菜 · 生菜 · 黄瓜 · 土豆 · 菜花儿 · 西红柿', 6),
    ('l2-yinggai-should', 2, '应该', 'Should · listing with 等等',
     'Giving and reporting advice, plus closing a list with 等等. Writing-focused: sentence completion, '
     'translation, Sentence Jumble.', '青菜 · 南瓜 · 应该 · 非常 · 等等', 5),
    ('l3-keshi-text1', 3, '可是', 'But · Text 1 · the project',
     'Joining two clauses that disagree, the whole Text 1 dialogue, the ie/üe pinyin focus, and the '
     'supermarket drawing project.', '可是 · 食 · 果 · 欠 · 石', 5),
    ('l4-fruits-vocab', 4, '水果', 'Fruits · 都',
     'Four fruits in two cycles, 都 covering a list, and a sorting task over all ten food words.',
     '水果 · 苹果 · 香蕉 · 橘子', 4),
    ('l5-zhexie-text2', 5, '这些', 'These · Text 2',
     'Two more fruits, the 这些/那些/一些 family, the whole Text 2 dialogue, and 这些…是谁的？',
     '西瓜 · 梨 · 这些', 3),
    ('l6-zhong-ranges', 6, '两三种', 'Kinds · number ranges',
     'The measure word 种 and approximate ranges. The plenary looks back over the whole sequence.',
     '种 · 两三 · 三四 · 四五', 1),
]


# ══════════════════════════════════════════════════════════════════
#  Emit
# ══════════════════════════════════════════════════════════════════

def build():
    for slug, label, fn in DECKS:
        slides = fn()
        total = len(slides)
        d = os.path.join(BASE, slug)
        sd = os.path.join(d, 'slides')
        if os.path.isdir(sd):
            shutil.rmtree(sd)
        os.makedirs(sd)

        for n, (fname, navlabel, tag, section, inner) in enumerate(slides, 1):
            top = ' top' if inner.count('<div class="') > 7 else ''
            html = PAGE.format(title=navlabel, tag=tag, section=section,
                               n=n, total=total, inner=inner, top=top)
            open(os.path.join(sd, fname + '.html'), 'w').write(html)

        manifest = ',\n'.join(
            '    {{ file: "{f}.html", label: "{l}" }}'.format(f=s[0], l=s[1].replace('"', "'"))
            for s in slides)
        open(os.path.join(d, 'index.html'), 'w').write(
            DECK_SHELL.format(label=label, manifest=manifest,
                              first=slides[0][0] + '.html', total=total,
                              slug=slug))
        print(f'  {slug}: {total} slides')

    cards = '\n'.join(
        CARD.format(slug=s, n=n, hanzi=h, en=e, desc=d, words=w, count=c)
        for s, n, h, e, d, w, c in CARD_DATA)
    open(os.path.join(BASE, 'index.html'), 'w').write(LIST_PAGE.format(cards=cards))
    print('  index.html (lesson list)')


if __name__ == '__main__':
    print('Building Y8 L10 · 蔬菜、水果')
    build()
    print('Done.')
