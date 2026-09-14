# -*- coding: utf-8 -*-
"""
Builds all six Y7 L14 (Clothing 穿着) classroom decks.

    python3 build.py

Content comes from docs/lesson-plans/y7-l14/*.md, which in turn comes from
轻松学中文 Book 1 Unit 5 (textbook pp.104–113, workbook pp.146–157) via the
cached reference at .agents/skills/lesson-planning/references/y7-unit5.md.

🔴 The rule that shapes this whole file: a slide that INTRODUCES vocabulary
carries exactly two new words, and every pair runs a three-slide cycle —
the words, the words used in sentences, then students writing one. In the
example sentences the ONLY new language is those two words; everything else
is already taught. Recall boards may show the whole set, because those words
are known and the slide is being scanned rather than taught from.
"""

from builder import (ACT_CSS, RADICAL_CSS, TITLE_CSS, activity, board, li_sc, page,
                     pattern, plenary, preview_slide, qa, radicals, text_slide,
                     title_slide, vocab_a, vocab_b, vocab_c, write_deck)

SW = {  # colour-word swatches, same values as the L13 deck
    "black": "#1A1A1A", "white": "#FFFFFF", "yellow": "#E8B923",
    "blue": "#2E5FA3", "red": "#C23B2E", "pink": "#E88EA0",
    "orange": "#D9762E", "purple": "#7A4E9E", "brown": "#8A5A34",
    "green": "#4C8A4A", "grey": "#9A9A94", "skyblue": "#6FA8D6",
}

CFU_CSS = """
  .cfu-list { display:flex; flex-direction:column; gap:26px; }
  .cfu-q { display:flex; align-items:flex-start; gap:22px; }
  .cfu-n { font-family:var(--font-display); font-size:42px; font-weight:900;
           color:var(--accent-madder); opacity:0.4; min-width:46px; }
  .cfu-t { font-size:32px; color:var(--text-primary); line-height:1.45; }
  .cfu-t .cn { font-family:var(--font-display); font-weight:700; font-size:42px; }
"""


def cfu(items, pairs=None):
    qs = "\n".join(
        f'''    <div class="cfu-q"><span class="cfu-n">{i}</span>'''
        f'''<span class="cfu-t">{t}</span></div>'''
        for i, t in enumerate(items, 1))
    ep = ""
    if pairs:
        rows = "\n".join(
            f'''      <div class="error-pair">
        <span class="error-wrong">{w}</span>
        <span class="error-arrow">&rarr;</span>
        <span class="error-correct">{r}</span>
      </div>''' for w, r in pairs)
        ep = f'''  <div style="display:flex;flex-direction:column;gap:16px;margin-top:36px;">
{rows}
  </div>'''
    return f'  <div class="cfu-list">\n{qs}\n  </div>\n{ep}'


# ══════════════════════════════════════════════════════════════════════════
# LESSON 1 — 穿 + Text 1 garments · mixed
# ══════════════════════════════════════════════════════════════════════════
def lesson1():
    FL, P = "Lesson 1 of 6 · 穿 + Text 1 Garments", "轻松学中文 Book 1 · Unit 5 · 课本 p.104"
    m = []

    m.append(("01-title.html", "Title · 穿 + Text 1 Garments",
              page("L1-01 · Title", "", title_slide(
                  1, "穿<span class='dot'>·</span>衬衫", "Wear · Shirt · Jeans · Skirt", "shirt",
                  ["Year 7 Chinese", "50 分钟", "Mixed", "课本 p.104"]),
                  FL, P, TITLE_CSS)))

    m.append(("02-review.html", "Review · 颜色 + 的 (0–8 min)",
              page("L1-02 · Review", "Review · 复习颜色 · 0–8 min",
                   board([{"hanzi": "黑色", "swatch": SW["black"]},
                          {"hanzi": "白色", "swatch": SW["white"], "white": True},
                          {"hanzi": "黄色", "swatch": SW["yellow"]},
                          {"hanzi": "蓝色", "swatch": SW["blue"]},
                          {"hanzi": "红色", "swatch": SW["red"]},
                          {"hanzi": "粉红色", "swatch": SW["pink"]},
                          {"hanzi": "橙色", "swatch": SW["orange"]},
                          {"hanzi": "紫色", "swatch": SW["purple"]},
                          {"hanzi": "棕色", "swatch": SW["brown"]},
                          {"hanzi": "绿色", "swatch": SW["green"]},
                          {"hanzi": "灰色", "swatch": SW["grey"]}],
                         cols=6, caption="上节课的颜色 — 看到就说，不要看拼音")
                   + '''
  <div style="display:flex;align-items:center;gap:28px;margin-top:44px;justify-content:center;">
    <span class="formula-box">颜色 <span class="op">+</span> 的 <span class="op">+</span> <span class="slot">名词</span></span>
    <span class="body-lg">黑色的火车　红色的出租车　黄色的校车</span>
  </div>''',
                   FL, "轻松学中文 Book 1 · 第十三课 颜色 · 课本 p.96–103")))

    m.append(("03-li-sc.html", "Learning Intention & Success Criteria (8–10 min)",
              page("L1-03 · LI & SC", "目标 · Learning Intention & Success Criteria",
                   li_sc("我们学怎么说别人喜欢穿什么衣服。",
                         [("我会说三件衣服的名字", "I can name three items of clothing — 衬衫、牛仔裤、裙子"),
                          ("我会用「穿」说谁穿什么", "I can use 穿 to say what someone wears — 他喜欢穿……"),
                          ("我会写「穿」，也知道为什么衣服的字有「衤」",
                           "I can write 穿 with the right stroke order, and I know why clothing characters take 衤")]),
                   FL, P)))

    m.append(("04-vocab-a1.html", "I Do · 生词 1 · 穿 · 衬衫",
              page("L1-04 · 生词 1", "I Do · 生词 · 第一组", vocab_a([
                  {"hanzi": "穿", "pinyin": "chuān", "en": "wear", "art": "chuan"},
                  {"hanzi": "衬衫", "pinyin": "chènshān", "en": "shirt", "art": "shirt",
                   "clue": "两个字都有 <b>衤</b> — clothing"},
              ]), FL, P)))

    m.append(("05-vocab-b1.html", "I Do · 例句 1 · 穿 · 衬衫",
              page("L1-05 · 例句 1", "I Do · 例句 · 穿 · 衬衫", vocab_b([
                  ("zhè shì chènshān", "这是<b>衬衫</b>。", "This is a shirt."),
                  ("wǒ bàba chuān báisè de chènshān", "我爸爸<b>穿</b>白色的<b>衬衫</b>。",
                   "My dad wears a white shirt."),
                  ("wǒ xǐhuan chuān lánsè de chènshān", "我喜欢<b>穿</b>蓝色的<b>衬衫</b>。",
                   "I like wearing a blue shirt."),
              ], note=("你爸爸喜欢穿什么颜色的衬衫？", "Answer in Chinese — colour + 的 + 衬衫.")),
                  FL, P)))

    m.append(("06-vocab-c1.html", "I Do · 写一句 1",
              page("L1-06 · 写一句 1", "I Do · 写一句 · 穿 · 衬衫", vocab_c(
                  ["我喜欢穿<span class='blank'>　　　</span>色的衬衫。"],
                  "在小白板上写一句。写完了举起来。",
                  "用两个人写一句 — <span class='cn'>我爸爸喜欢穿白色的衬衫，我妈妈喜欢穿红色的衬衫。</span>"
                  "<span class='sub'>Then add 也 or 不: 我也喜欢穿白色的衬衫。</span>"),
                  FL, P)))

    m.append(("07-vocab-a2.html", "I Do · 生词 2 · 牛仔裤 · 裙子",
              page("L1-07 · 生词 2", "I Do · 生词 · 第二组", vocab_a([
                  {"hanzi": "牛仔裤", "pinyin": "niúzǎikù", "en": "jeans", "art": "jeans",
                   "clue": "<b>牛</b> niú — 不是「午」"},
                  {"hanzi": "裙子", "pinyin": "qúnzi", "en": "skirt", "art": "skirt"},
              ]), FL, P)))

    m.append(("08-vocab-b2.html", "I Do · 例句 2 · 牛仔裤 · 裙子",
              page("L1-08 · 例句 2", "I Do · 例句 · 牛仔裤 · 裙子", vocab_b([
                  ("wǒ gēge xǐhuan chuān niúzǎikù", "我哥哥喜欢穿<b>牛仔裤</b>。",
                   "My older brother likes wearing jeans."),
                  ("wǒ jiějie xǐhuan chuān qúnzi", "我姐姐喜欢穿<b>裙子</b>。",
                   "My older sister likes wearing skirts."),
                  ("wǒ māma xǐhuan chuān lánsè de niúzǎikù hé fěnhóngsè de qúnzi",
                   "我妈妈喜欢穿蓝色的<b>牛仔裤</b>和粉红色的<b>裙子</b>。",
                   "My mum likes wearing blue jeans and a pink skirt."),
              ], note=("谁喜欢穿裙子？", "Answer with a full sentence, not just 姐姐.")),
                  FL, P)))

    m.append(("09-vocab-c2.html", "I Do · 写一句 2",
              page("L1-09 · 写一句 2", "I Do · 写一句 · 牛仔裤 · 裙子", vocab_c(
                  ["我<span class='blank'>　　　</span>喜欢穿<span class='blank'>　　　</span>。"],
                  "写一句。用一个家人 + 一件衣服。",
                  "写三个人，一句话 — <span class='cn'>我爸爸喜欢穿牛仔裤，我妈妈喜欢穿裙子，我不喜欢穿裙子。</span>"
                  "<span class='sub'>No word bank — turn away from the board.</span>"),
                  FL, P)))

    m.append(("10-board.html", "I Do · 今天的四个词 · Summary Board",
              page("L1-10 · 词汇总览", "I Do · 今天的词 · 看图说词",
                   board([{"hanzi": "穿", "art": "chuan"},
                          {"hanzi": "衬衫", "art": "shirt"},
                          {"hanzi": "牛仔裤", "art": "jeans"},
                          {"hanzi": "裙子", "art": "skirt"}],
                         cols=4, caption="只有汉字和图 — 没有拼音，没有英文"),
                   FL, P)))

    m.append(("11-pattern.html", "I Do · 句型 · 他喜欢穿……",
              page("L1-11 · 句型", "I Do · 句型 · 这是我爸爸。他喜欢穿……", pattern(
                  "这是我 <span class='slot'>家人</span> 。 他/她 喜欢 穿 <span class='slot'>衣服</span> 。",
                  [("zhè shì wǒ bàba， tā xǐhuan chuān chènshān",
                    "这是我爸爸。他喜欢穿衬衫。", "This is my dad. He likes wearing a shirt."),
                   ("zhè shì wǒ māma， tā xǐhuan chuān qúnzi",
                    "这是我妈妈。她喜欢穿裙子。", "This is my mum. She likes wearing a skirt."),
                   ("wǒ gēge xǐhuan chuān hēisè de niúzǎikù",
                    "我哥哥喜欢穿黑色的牛仔裤。", "My older brother likes wearing black jeans."),
                   ("wǒ jiějie xǐhuan chuān báisè de chènshān hé lánsè de niúzǎikù，"
                    "tā bù xǐhuan chuān qúnzi",
                    "我姐姐喜欢穿白色的衬衫和蓝色的牛仔裤，<b>她不喜欢穿裙子</b>。",
                    "My sister likes wearing a white shirt and blue jeans — she doesn't like skirts.")],
                  note=("info", "的", "颜色和衣服中间一定要有「的」。",
                        "✗ 红色衬衫　✓ 红色的衬衫 — the 的 is not optional.")),
                  FL, P, dense=True)))

    m.append(("12-cfu.html", "I Do · 检查 · CFU",
              page("L1-12 · CFU", "I Do · 检查一下 · Check for Understanding", cfu(
                  ["「<span class='cn'>穿</span>」是什么意思？会的举手。",
                   "怎么说 <b>a red skirt</b>？写在小白板上。",
                   "这句对不对？ <span class='cn'>我喜欢裙子穿。</span>"],
                  pairs=[("我喜欢裙子穿。", "我喜欢穿裙子。"),
                         ("红色衬衫", "红色的衬衫")]),
                  FL, P, CFU_CSS)))

    m.append(("13-text1.html", "I Do · 课文一 · Text 1 (CD T65)",
              page("L1-13 · 课文一", "I Do · 课文一 · Text 1", text_slide(
                  [("zhè shì wǒ bàba。 tā xǐhuan chuān chènshān hé niúzǎikù。",
                    "这是我爸爸。他喜欢穿衬衫和牛仔裤。"),
                   ("zhè shì wǒ māma。 tā xǐhuan chuān qúnzi。",
                    "这是我妈妈。她喜欢穿裙子。")],
                  questions=["Who likes wearing jeans?",
                             "妈妈喜欢穿什么？",
                             "Does dad wear a skirt?"],
                  track="T65"), FL, P, dense=True)))

    m.append(("14-act1-family.html", "We Do · 活动一 · 家人穿什么 (8 min)",
              page("L1-14 · 活动一", "Flexible Practice · We Do · 20–28 min", activity(
                  "We Do", "家人穿什么 · Family clothing profile", "8 min",
                  [("写四句话，四个家人，每句一件衣服和一个颜色。",
                    "Four sentences, four family members — a different garment and colour in each."),
                   ("四句话里面，今天的四个词都要用到。",
                    "Between them the four sentences must use all four of today's words."),
                   ("写完了，三个人读给全班听。", "Three students read theirs to the class.")],
                  target=["我爸爸喜欢穿灰色的衬衫。<span class='py'>wǒ bàba xǐhuan chuān huīsè de chènshān</span>",
                          "我姐姐喜欢穿蓝色的牛仔裤。<span class='py'>wǒ jiějie xǐhuan chuān lánsè de niúzǎikù</span>"],
                  extension="写成一段话，不是四句 — 用「和」「也」连起来，"
                            "而且要有一个人<b>不</b>喜欢一件衣服："
                            "<span class='cn'>我姐姐喜欢穿牛仔裤，她也喜欢穿衬衫，她不喜欢穿裙子。</span>"
                            "<span class='sub'>Then read it aloud without looking at the page.</span>"),
                  FL, P, ACT_CSS)))

    m.append(("14b-radicals.html", "I Do · 部首 · 第一组 (冂 牛 贝)",
              page("L1-14b · 部首", "I Do · 部首 · 课本 p.107 练习 4 · 第一组", radicals([
                  ("冂", "边框", "border", "周", "zhōu"),
                  ("牛", "牛", "cow", "物", "wù"),
                  ("贝", "贝壳", "shell", "贵", "guì"),
              ], note=("这六个部首，单元测验要考两次。",
                       "Unit Test Part 2 gives you the character and asks for the radical's meaning; "
                       "Part 3 gives you the radical and asks for a character. The other three come in Lesson 3.")),
                  FL, "轻松学中文 Book 1 · 课本 p.107 练习 4", RADICAL_CSS)))

    m.append(("15-act2-strokes.html", "You Do · 活动二 · 笔顺 + 衤 (8 min)",
              page("L1-15 · 活动二", "Flexible Practice · You Do · 28–36 min", activity(
                  "You Do", "笔顺 · 衤 还是 礻？", "8 min",
                  [("先在课本上把四个字里的「衤」圈出来 — 衬、衫、裤、裙。",
                    "Circle the 衤 in all four characters before you copy anything."),
                   ("练习册 p.147–148 第 2 题 — 按笔顺抄写 穿 衬 衫 牛 仔 裤 裙。",
                    "Workbook Ex.2 — copy the seven characters following the stroke order."),
                   ("练习册 p.148 第 4 题 — 写出两个问题的答案。",
                    "Workbook Ex.4 — write answers to 你喜欢穿衬衫吗？and 你喜欢穿牛仔裤吗？")],
                  target=["<span class='en'>上节课的部首</span>礻 — 视 &nbsp;&nbsp; "
                          "<span class='en'>衣服的部首</span>衤 — 衬 衫 裤 裙",
                          "<span class='en'>多一笔，意思完全不一样</span>"],
                  extension="第 4 题不要只写「喜欢／不喜欢」，写完整的两个分句："
                            "<span class='cn'>我喜欢穿衬衫，我不喜欢穿裙子。</span>"
                            "<span class='sub'>Then write two more characters that take 衤 without looking them up.</span>",
                  source="练习册 p.146–148"),
                  FL, "轻松学中文 Book 1 · 练习册 p.146–148", ACT_CSS)))

    m.append(("16-game-slap-board.html", "Game · 抢词卡 Slap the Board (7 min)",
              page("L1-16 · Game", "Game · 抢词卡 Slap the Board · 36–43 min", activity(
                  "Game", "抢词卡 · Slap the Board", "7 min",
                  [("四个小组。每组派一个人到黑板前。",
                    "Four groups. One player from each group at the board."),
                   ("老师说一个词 — 第一个拍到正确卡片的得一分。",
                    "Teacher calls a word. First hand on the right card scores."),
                   ("换人，每个人都要上来一次。", "Rotate — everyone takes a turn.")],
                  target=["<span class='en'>黑板上的卡片</span>穿　衬衫　牛仔裤　裙子",
                          "<span class='en'>加上第十三课的颜色词</span>红色　蓝色　黑色　白色　粉红色　黄色"],
                  extension="老师说一整句 — <span class='cn'>我姐姐喜欢穿粉红色的裙子。</span>"
                            "<span class='sub'>Slap TWO cards, in the right order: the colour first, then the garment.</span>",
                  source="课本 p.107 练习 5"),
                  FL, "轻松学中文 Book 1 · Unit 5 · 课本 p.107 练习 5", ACT_CSS)))

    m.append(("17-plenary.html", "Plenary · 出门条 (43–50 min)",
              page("L1-17 · Plenary", "Plenary · 回顾 · 自评 · 出门条", plenary(
                  ["我会说 衬衫、牛仔裤、裙子",
                   "我会用「穿」说谁穿什么",
                   "我会写「穿」，知道衣服的字有「衤」"],
                  "我姐姐喜欢穿蓝色的牛仔裤。",
                  "把这句话翻译成中文，写在小白板上。<br>"
                  "<span class='caption'>Translate into Chinese: My older sister likes wearing blue jeans.</span>"),
                  FL, P)))

    m.append(("18-preview.html", "Preview · 下一课",
              page("L1-18 · Preview", "Preview · 下一课", preview_slide(
                  "下一课 — 颜色 + 的 + 衣服，还有两种裤子：长裤和短裤。",
                  "Next lesson: colours and clothes together, and two kinds of trousers — 长裤 and 短裤.",
                  "trousers"), FL, P)))

    return write_deck("l1-chuan-text1", m, "L1 · 穿 + Text 1 Garments · 穿着一")


# ══════════════════════════════════════════════════════════════════════════
# LESSON 2 — colour + 的 + garment, 长/短 · speaking-heavy
# ══════════════════════════════════════════════════════════════════════════
def lesson2():
    FL, P = "Lesson 2 of 6 · 颜色的衣服 + 长/短", "轻松学中文 Book 1 · Unit 5 · 课本 p.105–106"
    m = []

    m.append(("01-title.html", "Title · 颜色 + 的 + 衣服",
              page("L2-01 · Title", "", title_slide(
                  2, "颜色<span class='dot'>·</span>长短", "Colour + 的 + Garment · Long and Short", "trousers",
                  ["Year 7 Chinese", "50 分钟", "Speaking-heavy", "课本 p.105–106"]),
                  FL, P, TITLE_CSS)))

    m.append(("02-review.html", "Review · 上节课的衣服 + 天蓝色 (0–8 min)",
              page("L2-02 · Review", "Review · 复习 · 0–8 min",
                   board([{"hanzi": "穿", "art": "chuan"}, {"hanzi": "衬衫", "art": "shirt"},
                          {"hanzi": "牛仔裤", "art": "jeans"}, {"hanzi": "裙子", "art": "skirt"}],
                         cols=4, caption="上节课的四个词 — 两人一组，一人说颜色，一人说衣服")
                   + '''
  <div style="display:flex;align-items:center;justify-content:center;gap:22px;margin-top:44px;flex-wrap:wrap;">
    <span class="colour-chip"><span class="dot" style="background:#FFFFFF;border-color:#8C8577;border-width:3px;"></span>白色</span>
    <span class="formula-box" style="font-size:38px;"><span class="op">+</span></span>
    <span class="colour-chip"><span class="dot" style="background:#2E5FA3;"></span>蓝色</span>
    <span class="formula-box" style="font-size:38px;"><span class="op">=</span></span>
    <span class="colour-chip"><span class="dot" style="background:#6FA8D6;"></span>天蓝色 <span style="font-family:var(--font-body);font-size:28px;font-weight:500;color:var(--accent-indigo);margin-left:10px;">tiānlánsè</span></span>
  </div>
  <div class="caption" style="text-align:center;margin-top:22px;">第十三课 p.102 的调色题 — 今天课本上的例子就是它</div>''',
                   FL, "轻松学中文 Book 1 · 第十三课 p.102 · 第十四课 p.104")))

    m.append(("03-li-sc.html", "Learning Intention & Success Criteria (8–10 min)",
              page("L2-03 · LI & SC", "目标 · Learning Intention & Success Criteria",
                   li_sc("我们学怎么说衣服的颜色和长短。",
                         [("我会把颜色放在衣服前面，中间用「的」",
                           "I can put any colour in front of any garment using 的 — 天蓝色的衬衫"),
                          ("我会分长裤和短裤，知道「长」和「短」的意思",
                           "I can tell 长裤 and 短裤 apart — 长 is long, 短 is short"),
                          ("我听得出声调，会写对拼音", "I can hear a word and write it in pinyin with the right tone mark")]),
                   FL, P)))

    m.append(("04-vocab-a1.html", "I Do · 生词 1 · 长裤 · 短裤",
              page("L2-04 · 生词 1", "I Do · 生词 · 第一组", vocab_a([
                  {"hanzi": "长裤", "pinyin": "chángkù", "en": "trousers", "art": "trousers",
                   "clue": "<b>长</b> cháng = long"},
                  {"hanzi": "短裤", "pinyin": "duǎnkù", "en": "shorts", "art": "shorts",
                   "clue": "<b>短</b> duǎn = short"},
              ]), FL, P)))

    m.append(("05-vocab-b1.html", "I Do · 例句 1 · 长裤 · 短裤",
              page("L2-05 · 例句 1", "I Do · 例句 · 长裤 · 短裤", vocab_b([
                  ("wǒ bàba xǐhuan chuān chángkù", "我爸爸喜欢穿<b>长裤</b>。",
                   "My dad likes wearing trousers."),
                  ("wǒ dìdi xǐhuan chuān duǎnkù", "我弟弟喜欢穿<b>短裤</b>。",
                   "My younger brother likes wearing shorts."),
                  ("wǒ xǐhuan chuān hēisè de chángkù， bù xǐhuan chuān duǎnkù",
                   "我喜欢穿黑色的<b>长裤</b>，不喜欢穿<b>短裤</b>。",
                   "I like wearing black trousers, I don't like wearing shorts."),
              ], note=("你今天穿长裤吗？", "Point and answer, then ask your partner the same about 短裤.")),
                  FL, P)))

    m.append(("06-vocab-c1.html", "I Do · 写一句 1",
              page("L2-06 · 写一句 1", "I Do · 写一句 · 长裤 · 短裤", vocab_c(
                  ["我喜欢穿<span class='blank'>　　　</span>色的<span class='blank'>　　　</span>。"],
                  "写一句 — 颜色 + 的 + 裤子。",
                  "两个人，一句话，用「也」或者「不」 — "
                  "<span class='cn'>我哥哥喜欢穿短裤，我也喜欢穿短裤，我姐姐不喜欢。</span>"),
                  FL, P)))

    m.append(("07-vocab-a2.html", "I Do · 生词 2 · 汗衫 · 天蓝色",
              page("L2-07 · 生词 2", "I Do · 生词 · 第二组", vocab_a([
                  {"hanzi": "汗衫", "pinyin": "hànshān", "en": "T-shirt", "art": "tee",
                   "clue": "没有扣子，圆领 — no buttons"},
                  {"hanzi": "天蓝色", "pinyin": "tiānlánsè", "en": "sky blue",
                   "art": ("swatch", SW["skyblue"])},
              ]), FL, P)))

    m.append(("08-vocab-b2.html", "I Do · 例句 2 · 汗衫 · 天蓝色",
              page("L2-08 · 例句 2", "I Do · 例句 · 汗衫 · 天蓝色", vocab_b([
                  ("tā chuān báisè de hànshān", "他穿白色的<b>汗衫</b>。",
                   "He's wearing a white T-shirt."),
                  ("wǒ xǐhuan tiānlánsè", "我喜欢<b>天蓝色</b>。", "I like sky blue."),
                  ("wǒ mèimei chuān tiānlánsè de hànshān hé hēisè de duǎnkù",
                   "我妹妹穿<b>天蓝色</b>的<b>汗衫</b>和黑色的短裤。",
                   "My little sister is wearing a sky-blue T-shirt and black shorts."),
              ], note=("汗衫和衬衫，哪里不一样？", "One has buttons and a collar. Which one?")),
                  FL, P)))

    m.append(("09-vocab-c2.html", "I Do · 写一句 2",
              page("L2-09 · 写一句 2", "I Do · 写一句 · 汗衫 · 天蓝色", vocab_c(
                  ["<span class='blank'>　　　</span>穿<span class='blank'>　　　</span>色的汗衫。"],
                  "写一句。可以写自己，也可以写家人。",
                  "描述教室里的一个人 — 两件衣服，两个颜色，不要说名字。"
                  "<span class='sub'>The class guesses who. 他是谁？</span>"),
                  FL, P)))

    m.append(("10-board.html", "I Do · 六件衣服 · Summary Board",
              page("L2-10 · 词汇总览", "I Do · 到现在的六件衣服",
                   board([{"hanzi": "衬衫", "art": "shirt"}, {"hanzi": "汗衫", "art": "tee"},
                          {"hanzi": "牛仔裤", "art": "jeans"}, {"hanzi": "长裤", "art": "trousers"},
                          {"hanzi": "短裤", "art": "shorts"}, {"hanzi": "裙子", "art": "skirt"}],
                         cols=6, caption="只有汉字和图 — 这块板整节课都在屏幕上"),
                   FL, P)))

    m.append(("11-pattern.html", "I Do · 句型 · 颜色 + 的 + 衣服",
              page("L2-11 · 句型", "I Do · 句型 · 颜色 + 的 + 衣服", pattern(
                  "<span class='slot'>颜色</span> <span class='op'>+</span> 的 <span class='op'>+</span> <span class='slot'>衣服</span>",
                  [("hóngsè de chènshān", "红色的衬衫", "a red shirt"),
                   ("tiānlánsè de chènshān", "天蓝色的衬衫", "a sky-blue shirt"),
                   ("huīsè de chángkù", "灰色的长裤", "grey trousers"),
                   ("wǒ jiějie jīntiān chuān tiānlánsè de chènshān hé huīsè de chángkù",
                    "我姐姐今天穿天蓝色的衬衫和灰色的长裤。",
                    "My sister is wearing a sky-blue shirt and grey trousers today.")],
                  note=("warning", "的", "「的」不能省。",
                        "✗ 蓝色牛仔裤　✓ 蓝色的牛仔裤 — the most common written error in this lesson.")),
                  FL, P, dense=True)))

    m.append(("12-act1-naming.html", "We Do · 活动一 · 快速说 (7 min)",
              page("L2-12 · 活动一", "Flexible Practice · We Do · 20–27 min", activity(
                  "We Do", "快速说 · Rapid-fire naming", "7 min",
                  [("第一遍：老师指，全班一起说。", "Round 1: teacher points, whole class answers together."),
                   ("第二遍：不举手，老师点名，快一点。", "Round 2: cold call, no hands up, faster."),
                   ("第三遍：老师只说颜色，一个同学补衣服，下一个同学说成一整句。",
                    "Round 3: teacher says the colour only — one student adds the garment, the next makes it a sentence with 穿.")],
                  target=["天蓝色的衬衫　橙色的长裤　蓝色的牛仔裤",
                          "他穿橙色的长裤。<span class='py'>tā chuān chéngsè de chángkù</span>"],
                  extension="你来当老师 — 指着图问 <span class='cn'>这是什么颜色的衣服？</span>"
                            "<span class='sub'>And correct a wrong answer in Chinese: 不对，是橙色的，不是红色的。</span>",
                  source="课本 p.105 练习 1 · p.106 练习 3"),
                  FL, P, ACT_CSS)))

    m.append(("13-act2-tones.html", "You Do · 活动二 · 声调冲刺 T66 (4 min)",
              page("L2-13 · 活动二", "Flexible Practice · You Do · 27–31 min", activity(
                  "You Do", "声调冲刺 · Tone-mark sprint", "4 min",
                  [("听两遍，把声调写在小白板上，举起来。",
                    "Listen twice, write the pinyin with its tone mark, hold it up."),
                   ("九个词里有两个是今天的中文 — 找出来。",
                    "Two of the nine are today's language. Spot them.")],
                  target=["gōngniú　kùnnan　<b>duǎnkù</b>",
                          "chuántǒng　tiáozi　tàozhuāng",
                          "duànliàn　yǒuqíng　<b>lǜsè</b>"],
                  extension="能写汉字的三个，也把汉字写出来 — "
                            "<span class='cn'>短裤　绿色　牛</span>",
                  source="课本 p.105 练习 2 · CD T66"),
                  FL, "轻松学中文 Book 1 · 课本 p.105 练习 2 · CD T66", ACT_CSS)))

    m.append(("14-act3-draw.html", "You Do · 活动三 · 说一说，画一画 (7 min)",
              page("L2-14 · 活动三", "Flexible Practice · You Do · 31–38 min", activity(
                  "You Do", "说一说，画一画 · Describe and draw", "7 min",
                  [("两人一组，中间放一本书，看不见对方的纸。",
                    "Pairs, with a book between you so you can't see each other's paper."),
                   ("A 说一套衣服 — 两件衣服，两个颜色。B 画出来，涂上颜色。",
                    "A describes an outfit — two garments, two colours. B draws and colours it."),
                   ("换过来再做一次。最后比一比，画错了是说错了还是听错了？",
                    "Swap. Then compare: if the drawing is wrong, was it the saying or the hearing?"),
                   ("接着做练习册 p.148 第 3 题和 p.155 第 17 题 — 按中文涂色。",
                    "Then workbook Ex.3 and Ex.17 — colour the pictures to match the Chinese.")],
                  target=["我穿天蓝色的汗衫和黑色的短裤。"
                          "<span class='py'>wǒ chuān tiānlánsè de hànshān hé hēisè de duǎnkù</span>"],
                  extension="B 不可以说「再说一遍」，A 要说<b>三</b>件衣服，用「、」和「和」："
                            "<span class='cn'>我穿天蓝色的汗衫、黑色的短裤和白色的运动鞋。</span>"
                            "<span class='sub'>Then B describes the drawing back in Chinese as a check.</span>",
                  source="练习册 p.148 · p.155"),
                  FL, "轻松学中文 Book 1 · 练习册 p.148 第 3 题 · p.155 第 17 题", ACT_CSS, dense=True)))

    m.append(("15-game-quizlet.html", "Game · Quizlet Live 配对赛 (5 min)",
              page("L2-15 · Game", "Game · Quizlet Live · 38–43 min", activity(
                  "Game", "Quizlet Live · 图 ↔ 汉字 配对赛", "5 min",
                  [("拿出平板，老师发房间号，系统自动分组。",
                    "Devices out. Teacher shares the join code; the app assigns teams."),
                   ("图配汉字，比谁快。六件衣服 + 十一个颜色都在里面。",
                    "Match picture to 汉字 against the clock — all six garments plus the eleven colours."),
                   ("时间够就打第二轮。", "Run a second round if there's time.")],
                  target=["衬衫　汗衫　牛仔裤　长裤　短裤　裙子",
                          "<span class='en'>加上第十三课的十一个颜色</span>"],
                  extension="第二轮换成 <b>汉字 ↔ 拼音</b> 模式，把图关掉 — "
                            "<span class='sub'>no picture shortcut, so the characters have to be read.</span>"),
                  FL, P, ACT_CSS)))

    m.append(("16-plenary.html", "Plenary · 出门条 (43–50 min)",
              page("L2-16 · Plenary", "Plenary · 回顾 · 自评 · 出门条", plenary(
                  ["我会用「的」把颜色放在衣服前面",
                   "我会分 长裤 和 短裤",
                   "我听得出声调，写得对拼音"],
                  "天蓝色的短裤",
                  "先写这个词，再用它写一整句。<br>"
                  "<span class='caption'>Write 'sky-blue shorts' in Chinese, then use it in a full sentence.</span>"),
                  FL, P)))

    m.append(("17-preview.html", "Preview · 下一课",
              page("L2-17 · Preview", "Preview · 下一课", preview_slide(
                  "下一课 — 课文二：你喜欢穿什么衣服？还有三件新衣服。",
                  "Next lesson: Text 2 — 你喜欢穿什么衣服？— plus 衣服, 毛衣 and 外套.",
                  "sweater"), FL, P)))

    return write_deck("l2-colour-garment", m, "L2 · 颜色 + 的 + 衣服 · 长裤短裤")


if __name__ == "__main__":
    import lessons456
    total = lesson1() + lesson2() + lessons456.lesson3()
    total += lessons456.lesson4() + lessons456.lesson5() + lessons456.lesson6()
    print(f"{total} slides written across 6 decks")
