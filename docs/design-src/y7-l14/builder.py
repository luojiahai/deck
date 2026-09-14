# -*- coding: utf-8 -*-
"""
Slide templates for the Y7 L14 (Clothing 穿着) decks.

Every slide type here obeys the classroom typography floor defined in
index/designs/y7-l14/shared/tokens.css. No template may set a font-size
below the floor, and none of them emits a Scaffold or OTR box — those are
teacher-facing and belong in the lesson plan, not on a projector.

The three-slide vocabulary cycle (vocab_a / vocab_b / vocab_c) is the
backbone: two new words, then those two words used in sentences, then
students writing one themselves. Slide count follows the vocabulary,
never the other way round.
"""

import html as _html
import os
import re

from svg_library import svg, swatch_svg

INDIGO = "#2C4C7C"
MADDER = "#B03C2C"
OLIVE = "#5F7040"

OUT_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "..", "index", "designs", "y7-l14")
OUT_ROOT = os.path.normpath(os.path.join(
    "/Users/luojiahai/code/deck", "index", "designs", "y7-l14"))


# ── page shell ────────────────────────────────────────────────────────────

def page(title, section, body, footer_l, footer_r, extra_css="", dense=False):
    css = f"<style>\n{extra_css}\n</style>" if extra_css.strip() else ""
    dense_cls = " dense" if dense else ""
    return f"""<!DOCTYPE html><html lang="zh-CN"><head>
<meta charset="UTF-8">
<title>{_html.escape(title)}</title>
<link rel="stylesheet" href="../../shared/tokens.css">
{css}
</head>
<body>

<div class="slide-header">
  <div class="accent-line"></div>
  <span class="lesson-tag">Y7 · L14 穿着</span>
  <span class="sep"></span>
  <span class="section-name">{section}</span>
</div>

<div class="slide-content{dense_cls}">
{body}
</div>

<div class="slide-footer">
  <span>{footer_l}</span>
  <span class="brand">{footer_r}</span>
</div>

</body></html>
"""


def _art(spec):
    """spec is either a garment key, ('swatch', '#rrggbb'), or None."""
    if spec is None:
        return ""
    if isinstance(spec, tuple) and spec[0] == "swatch":
        return swatch_svg(spec[1])
    return svg(spec, INDIGO)


# ── cycle A — the two new words ───────────────────────────────────────────

def vocab_a(words):
    """words: list of exactly 2 dicts {hanzi, pinyin, en, art, clue?}"""
    assert len(words) == 2, "a teaching slide carries two new words. Two."
    cards = []
    for w in words:
        art = _art(w.get("art"))
        art_block = f'<div class="wc-art">{art}</div>' if art else '<div class="wc-art"></div>'
        long = " long" if len(re.sub(r"[（(].*?[）)]", "", w["hanzi"])) >= 3 else ""
        clue = (f'<div class="wc-clue">{w["clue"]}</div>' if w.get("clue") else "")
        cards.append(f'''    <div class="word-card">
      {art_block}
      <div class="wc-hanzi{long}">{w["hanzi"]}</div>
      <div class="wc-pinyin">{w["pinyin"]}</div>
      <div class="wc-english">{w["en"]}</div>
{clue}
    </div>''')
    return '  <div class="word-pair">\n' + "\n".join(cards) + "\n  </div>"


# ── cycle B — the two words used in sentences ─────────────────────────────

def vocab_b(rows, note=None):
    """rows: list of (pinyin, hanzi_with_<b> marks, english)"""
    out = ['  <div class="ex-list">']
    for i, (py, hz, en) in enumerate(rows, 1):
        hz = hz.replace("<b>", '<span class="new">').replace("</b>", "</span>")
        out.append(f'''    <div class="ex-row">
      <div class="ex-pinyin">{py}</div>
      <div class="ex-hanzi"><span class="ex-num">{i}</span>{hz}</div>
      <div class="ex-en">{en}</div>
    </div>''')
    out.append("  </div>")
    if note:
        out.append(f'''  <div class="note-box" style="margin-top:34px;">
    <span class="note-icon">问</span>
    <span><span class="note-text">{note[0]}</span>
    <span class="note-sub">{note[1]}</span></span>
  </div>''')
    return "\n".join(out)


# ── cycle C — write your own ──────────────────────────────────────────────

def vocab_c(frames, instruction, extension, seconds="60 秒"):
    fr = "\n".join(
        f'    <div class="sentence-frame">{f}</div>' for f in frames)
    return f'''  <div style="display:flex;flex-direction:column;gap:26px;">
{fr}
    <div style="display:flex;align-items:center;gap:20px;margin-top:6px;">
      <span class="badge badge-indigo">{seconds}</span>
      <span class="body-lg" style="color:var(--text-primary);">{instruction}</span>
    </div>
    <div class="extension-box">
      <span class="ext-label">更难</span>
      <span class="ext-body">{extension}</span>
    </div>
  </div>'''


# ── summary / recall board ────────────────────────────────────────────────

def board(items, cols=None, caption=None, show_pinyin=False):
    """items: list of dicts {hanzi, art?, pinyin?, en?, swatch?}"""
    cols = cols or min(len(items), 6)
    cells = []
    for it in items:
        bits = []
        if it.get("art"):
            bits.append(f'<div class="vc-art">{_art(it["art"])}</div>')
        if it.get("swatch"):
            bits.append(f'<span class="vc-swatch{" white" if it.get("white") else ""}" '
                        f'style="background:{it["swatch"]};"></span>')
        long = " long" if len(it["hanzi"]) >= 3 else ""
        bits.append(f'<div class="vc-hanzi{long}">{it["hanzi"]}</div>')
        if show_pinyin and it.get("pinyin"):
            bits.append(f'<div class="vc-pinyin">{it["pinyin"]}</div>')
        if it.get("en"):
            bits.append(f'<div class="vc-english">{it["en"]}</div>')
        cells.append('    <div class="vocab-card">' + "".join(bits) + "</div>")
    cap = (f'  <div class="caption" style="text-align:center;margin-bottom:26px;">'
           f'{caption}</div>\n' if caption else "")
    return (cap + f'  <div class="grid-{cols}">\n' + "\n".join(cells) + "\n  </div>")


# ── sentence pattern ──────────────────────────────────────────────────────

def pattern(formula, examples, note=None):
    ex = "\n".join(
        f'''      <div class="ex-row">
        <div class="ex-pinyin">{py}</div>
        <div class="ex-hanzi">{hz.replace("<b>", '<span class="new">').replace("</b>", "</span>")}</div>
        <div class="ex-en">{en}</div>
      </div>''' for py, hz, en in examples)
    nb = ""
    if note:
        nb = f'''  <div class="{note[0]}-box" style="margin-top:18px;">
    <span class="{note[0][:4] if note[0] != "warning" else "warn"}-icon">{note[1]}</span>
    <span><span class="{note[0][:4] if note[0] != "warning" else "warn"}-text">{note[2]}</span>
    <span class="{note[0][:4] if note[0] != "warning" else "warn"}-sub">{note[3]}</span></span>
  </div>'''
    return f'''  <div class="pattern-wrap">
    <div><span class="formula-box">{formula}</span></div>
    <div class="ex-list">
{ex}
    </div>
  </div>
{nb}'''


# ── question / answer set ─────────────────────────────────────────────────

def qa(pairs, heading=None):
    head = f'  <div class="heading-sm" style="margin-bottom:30px;">{heading}</div>\n' if heading else ""
    rows = []
    for kind, py, hz, en in pairs:
        rows.append(f'''    <div class="qa-row">
      <span class="qa-tag {kind}">{"问" if kind == "q" else "答"}</span>
      <span class="qa-body">
        <span class="qa-pinyin">{py}</span>
        <span class="qa-hanzi">{hz}</span>
        {f'<span class="qa-en">{en}</span>' if en else ''}
      </span>
    </div>''')
    return head + "\n".join(rows)


# ── text / passage ────────────────────────────────────────────────────────

def text_slide(lines, questions=None, track=None):
    body = []
    for py, hz in lines:
        body.append(f'''    <div class="ex-row" style="gap:4px;">
      <div class="ex-pinyin">{py}</div>
      <div class="ex-hanzi">{hz}</div>
    </div>''')
    q = ""
    if questions:
        qs = "".join(f'<li style="margin-bottom:12px;">{x}</li>' for x in questions)
        q = f'''  <div class="card" style="margin-top:22px;padding:26px 34px;">
    <div class="badge badge-madder" style="margin-bottom:16px;">听 · 读 · 问</div>
    <ol class="body-md" style="margin:0;padding-left:34px;color:var(--text-primary);">{qs}</ol>
  </div>'''
    t = (f'<div style="margin-bottom:22px;"><span class="badge badge-indigo">'
         f'CD {track}</span></div>' if track else "")
    return t + '  <div class="ex-list" style="gap:20px;">\n' + "\n".join(body) + "\n  </div>\n" + q


# ── activity ──────────────────────────────────────────────────────────────

def activity(kind, title, minutes, steps, target=None, extension=None, source=None):
    st = "".join(
        f'''      <div class="rule">
        <span class="rule-n">{i}</span>
        <span class="rule-t">{cn}{f'<br><span class="gloss">{en}</span>' if en else ''}</span>
      </div>''' for i, (cn, en) in enumerate(steps, 1))
    tgt = ""
    if target:
        tl = "".join(f'<div class="tgt-line">{x}</div>' for x in target)
        tgt = f'''    <div class="target-box">
      <div class="caption" style="margin-bottom:14px;">你要说 / 写的中文</div>
      {tl}
    </div>'''
    ext = ""
    if extension:
        ext = f'''    <div class="extension-box" style="margin-top:26px;">
      <span class="ext-label">更难</span>
      <span class="ext-body">{extension}</span>
    </div>'''
    src = f'<span class="badge badge-olive" style="margin-left:16px;">{source}</span>' if source else ""
    return f'''  <div class="act-head">
    <span class="badge badge-teal">{kind}</span>
    <span class="heading-sm">{title}</span>
    <span class="badge badge-madder">{minutes}</span>{src}
  </div>
  <div class="act-grid">
    <div class="rules">
{st}
{ext}
    </div>
{tgt}
  </div>'''


ACT_CSS = """
  .act-head { display:flex; align-items:center; gap:20px; margin-bottom:34px; flex-wrap:wrap; }
  .act-grid { display:grid; grid-template-columns:1.1fr 0.9fr; gap:48px; align-items:start; }
  .act-grid.solo { grid-template-columns:1fr; }
  .rules { display:flex; flex-direction:column; gap:22px; }
  .rule { display:flex; align-items:flex-start; gap:20px; }
  .rule-n { font-family:var(--font-display); font-size:40px; font-weight:900;
            color:var(--accent-teal); opacity:0.45; min-width:44px; line-height:1.2; }
  .rule-t { font-size:30px; color:var(--text-primary); line-height:1.45; }
  .target-box { background:var(--bg-tertiary); border:2px solid var(--border-medium);
                border-radius:var(--radius-lg); padding:30px 32px; }
  .tgt-line { font-family:var(--font-display); font-size:42px; font-weight:700;
              color:var(--text-primary); line-height:1.5; margin-bottom:12px; }
  .tgt-line .py { display:block; font-family:var(--font-body); font-size:28px;
                  font-weight:500; color:var(--accent-indigo); letter-spacing:0.03em; }
  .tgt-line .en { display:block; font-family:var(--font-body); font-size:26px;
                  font-weight:400; color:var(--text-secondary); }
"""


# ── radicals ──────────────────────────────────────────────────────────────

RADICAL_CSS = """
  .rad-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:30px; }
  .rad { background:var(--bg-secondary); border:2px solid var(--border-light);
         border-radius:var(--radius-lg); padding:26px 22px; text-align:center; }
  .rad-top { display:flex; align-items:center; justify-content:center; gap:16px;
             padding-bottom:16px; margin-bottom:18px;
             border-bottom:1px dashed var(--border-medium); }
  .rad-mark { font-family:var(--font-display); font-size:76px; font-weight:900;
              color:var(--accent-madder); line-height:1; }
  .rad-mean { font-size:28px; color:var(--text-secondary); text-align:left; line-height:1.25; }
  .rad-mean .cn { display:block; font-family:var(--font-display); font-size:32px;
                  font-weight:700; color:var(--text-primary); }
  .rad-eg { font-family:var(--font-display); font-size:92px; font-weight:900;
            color:var(--text-primary); line-height:1; }
  .rad-py { font-size:28px; color:var(--accent-indigo); margin-top:8px; }
"""


def radicals(items, note=None):
    """items: list of (radical, chinese meaning, english meaning, example, pinyin)"""
    cells = "\n".join(f'''    <div class="rad">
      <div class="rad-top">
        <span class="rad-mark">{r}</span>
        <span class="rad-mean"><span class="cn">{cn}</span>{en}</span>
      </div>
      <div class="rad-eg">{eg}</div>
      <div class="rad-py">{py}</div>
    </div>''' for r, cn, en, eg, py in items)
    nb = ""
    if note:
        nb = f'''  <div class="warning-box" style="margin-top:30px;">
    <span class="warn-icon">考</span>
    <span><span class="warn-text">{note[0]}</span>
    <span class="warn-sub">{note[1]}</span></span>
  </div>'''
    return f'  <div class="rad-grid">\n{cells}\n  </div>\n{nb}'


# ── learning intention + success criteria ─────────────────────────────────

def li_sc(walt, criteria):
    rows = "\n".join(
        f'''    <div class="sc-row">
      <span class="sc-num">{i}</span>
      <span class="sc-text">{cn}<span class="en">{en}</span></span>
    </div>''' for i, (cn, en) in enumerate(criteria, 1))
    return f'''  <div style="display:flex;flex-direction:column;gap:30px;">
    <div>
      <div class="badge badge-indigo" style="margin-bottom:18px;">今天我们学 · Learning Intention</div>
      <div class="display-md">{walt}</div>
    </div>
    <div>
      <div class="badge badge-teal" style="margin-bottom:18px;">我会 · Success Criteria</div>
      <div style="display:flex;flex-direction:column;gap:18px;margin-top:4px;">
{rows}
      </div>
    </div>
  </div>'''


# ── plenary ───────────────────────────────────────────────────────────────

def plenary(criteria, ticket, ticket_sub=None, wide=False):
    rows = "\n".join(
        f'''      <div class="sc-row" style="padding:18px 24px;">
        <span class="sc-num">{i}</span>
        <span class="sc-text">{c}</span>
      </div>''' for i, c in enumerate(criteria, 1))
    sub = f'<div class="body-md" style="margin-top:14px;">{ticket_sub}</div>' if ticket_sub else ""
    head = ("回顾整个单元 · the whole sequence" if wide else "自评 · 对照今天的目标")
    return f'''  <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start;">
    <div>
      <div class="badge badge-teal" style="margin-bottom:20px;">{head}</div>
      <div style="display:flex;flex-direction:column;gap:14px;">
{rows}
      </div>
      <div class="caption" style="margin-top:20px;">👍 会了　😐 快会了　👎 还要练</div>
    </div>
    <div>
      <div class="badge badge-madder" style="margin-bottom:20px;">出门条 · Exit Ticket</div>
      <div class="card" style="border:3px solid var(--accent-madder);">
        <div class="display-md" style="line-height:1.35;">{ticket}</div>
        {sub}
      </div>
    </div>
  </div>'''


# ── title / preview ───────────────────────────────────────────────────────

TITLE_CSS = """
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
"""


def title_slide(n, cn, en, art, meta):
    m = '<span class="s"></span>'.join(f"<span>{x}</span>" for x in meta)
    return f'''<div class="bg-char">穿</div>
<div class="t-main">
  <div class="t-num">Lesson {n} of 6 · Y7 Unit 5 · 轻松学中文 1</div>
  <div class="t-art">{_art(art)}</div>
  <h1 class="t-cn">{cn}</h1>
  <div class="t-en">{en}</div>
  <div class="t-meta">{m}</div>
</div>'''


def preview_slide(line_cn, line_en, art=None):
    a = (f'<div class="pv-art" style="height:200px;margin-bottom:36px;">'
         f'{_art(art)}</div>') if art else ""
    return f'''  <div style="text-align:center;">
    <div class="badge badge-indigo" style="margin-bottom:30px;">下一课 · Next Lesson</div>
    {a}
    <div class="display-md" style="line-height:1.4;margin-bottom:22px;">{line_cn}</div>
    <div class="body-lg">{line_en}</div>
  </div>'''


# ── writer ────────────────────────────────────────────────────────────────

def write_deck(folder, manifest, lesson_label):
    d = os.path.join(OUT_ROOT, folder, "slides")
    os.makedirs(d, exist_ok=True)
    for fn, _, html_text in manifest:
        with open(os.path.join(d, fn), "w", encoding="utf-8") as f:
            f.write(html_text)
    entries = ",\n".join(
        f'    {{ file: "slides/{fn}", label: {label!r} }}'.replace("'", '"')
        for fn, label, _ in manifest)
    idx = DECK_INDEX.replace("{{TITLE}}", lesson_label).replace("{{ENTRIES}}", entries)
    with open(os.path.join(OUT_ROOT, folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)
    return len(manifest)


DECK_INDEX = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{{TITLE}}</title>
<script>
  window.DECK_MANIFEST = [
{{ENTRIES}}
  ];
  window.DECK_WIDTH = 1920;
  window.DECK_HEIGHT = 1080;
</script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; overflow: hidden; font-family: -apple-system, "PingFang SC", sans-serif; background: #0a0a0a; }
  #stage { position: fixed; top: 50%; left: 50%; transform-origin: top left; will-change: transform; background: #fff; box-shadow: 0 10px 60px rgba(0,0,0,0.4); }
  #frame { width: 1920px; height: 1080px; overflow: hidden; position: relative; background: #FBF9F4; }
  .counter-pill { position: fixed; bottom: 20px; right: 20px; display: flex; align-items: center; gap: 10px; background: rgba(0,0,0,0.65); color: #fff; padding: 6px 14px; border-radius: 999px; font-size: 13px; letter-spacing: 0.05em; font-variant-numeric: tabular-nums; z-index: 100; opacity: 0.7; }
  .counter-pill .label { color: rgba(255,255,255,0.7); margin-left: 8px; }
  .list-btn { color: rgba(255,255,255,0.85); text-decoration: none; padding-right: 10px; border-right: 1px solid rgba(255,255,255,0.25); opacity: 0.85; }
  .list-btn:hover { opacity: 1; }
  .nav-zone { position: fixed; top: 0; bottom: 0; width: 15%; cursor: pointer; z-index: 50; }
  .nav-zone.left { left: 0; } .nav-zone.right { right: 0; }
  .nav-hint { position: absolute; top: 50%; transform: translateY(-50%); width: 44px; height: 44px; border-radius: 999px; background: rgba(255,255,255,0.08); color: rgba(255,255,255,0.6); display: flex; align-items: center; justify-content: center; font-size: 22px; opacity: 0; transition: opacity .2s; }
  .nav-zone.left .nav-hint { left: 20px; } .nav-zone.right .nav-hint { right: 20px; }
  .nav-zone:hover .nav-hint { opacity: 1; }
</style>
</head>
<body>
<div id="stage"><div id="frame"></div></div>
<div class="nav-zone left" id="navL"><div class="nav-hint">&lsaquo;</div></div>
<div class="nav-zone right" id="navR"><div class="nav-hint">&rsaquo;</div></div>
<div class="counter-pill">
  <a class="list-btn" href="../">&larr; 列表</a>
  <span id="counter">1 / 1</span>
</div>
<script>
(function () {
  const W = window.DECK_WIDTH || 1920, H = window.DECK_HEIGHT || 1080;
  const deck = window.DECK_MANIFEST || [];
  const stage = document.getElementById('stage'), frame = document.getElementById('frame'), counter = document.getElementById('counter');
  let current = 0;
  stage.style.width = W + 'px'; stage.style.height = H + 'px';
  function fit() {
    const s = Math.min(innerWidth / W, innerHeight / H);
    stage.style.transform = 'translate(' + ((innerWidth - W*s)/2) + 'px,' + ((innerHeight - H*s)/2) + 'px) scale(' + s + ')';
    stage.style.top = '0'; stage.style.left = '0';
  }
  let loadedFile = null;
  function show(idx) {
    if (idx < 0 || idx >= deck.length) return;
    current = idx;
    const item = deck[idx];
    counter.innerHTML = (idx+1) + ' / ' + deck.length + ' <span class="label">' + (item.label||'') + '</span>';
    if (location.hash !== '#'+(idx+1)) history.replaceState(null,'','#'+(idx+1));
    if (loadedFile !== item.file) {
      loadedFile = item.file;
      fetch(item.file).then(r=>r.text()).then(html=>{
        var linkRe=/<link[^>]*rel=["']stylesheet["'][^>]*href=["']([^"']+)["'][^>]*>/gi, cssLinks=[], lm;
        while((lm=linkRe.exec(html))!==null){cssLinks.push(lm[1]);}
        return Promise.all(cssLinks.map(href=>{
          var url=/^https?:/.test(href)?href:new URL(href,new URL(item.file,location.href)).href;
          return fetch(url).then(r=>r.text()).catch(()=>'');
        })).then(cssContents=>{
          var linkedCss=cssContents.join('\\n');
          var styles=linkedCss?'<style>'+linkedCss.replace(/\\b(html|body)\\b(?=\\s*[{,])/g,'#frame')+'</style>':'';
          var styleRe=/<style[^>]*>([\\s\\S]*?)<\\/style>/gi, m;
          while((m=styleRe.exec(html))!==null){styles+='<style>'+m[1].replace(/\\b(html|body)\\b(?=\\s*[{,])/g,'#frame')+'</style>';}
          var bodyM=html.match(/<body[^>]*>([\\s\\S]*?)<\\/body>/i);
          frame.innerHTML=styles+(bodyM?bodyM[1]:'');
        });
      }).catch(()=>{frame.innerHTML='<div style="color:#333;padding:40px;text-align:center;font-size:24px;">Slide not found</div>';});
    }
  }
  function next(){show(Math.min(current+1,deck.length-1));}
  function prev(){show(Math.max(current-1,0));}
  document.addEventListener('keydown',function(e){
    if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;
    switch(e.key){
      case'ArrowRight':case' ':case'PageDown':e.preventDefault();next();break;
      case'ArrowLeft':case'PageUp':e.preventDefault();prev();break;
      case'Home':e.preventDefault();show(0);break;
      case'End':e.preventDefault();show(deck.length-1);break;
      case'p':case'P':window.print();break;
    }
  });
  document.getElementById('navL').addEventListener('click',prev);
  document.getElementById('navR').addEventListener('click',next);
  window.addEventListener('resize',fit);
  fit();
  var h=parseInt((location.hash||'#1').slice(1),10);
  show(isNaN(h)?0:Math.max(0,Math.min(h-1,deck.length-1)));
})();
</script>
</body>
</html>
"""
