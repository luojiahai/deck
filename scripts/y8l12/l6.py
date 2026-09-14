# -*- coding: utf-8 -*-
"""Lesson 6 of 6 — 不算太贵 · the bill, and the whole meal out.

From docs/lesson-plans/y8-l12/06-huaqian-text2-mixed.md.
Last lesson of the unit: the Review and the Plenary both reach back over
all six lessons, because there is no 复习 lesson after this one.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, title, tag, section, body, cls=""):
    S.append((f, title, tag, section, body, cls))

add("01-title.html", "Y8 L12 · Title · 不算太贵", "Lesson 6 of 6", "Y8 · Lesson 12",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 12", "不算太贵", "The Whole Meal Out",
                "Lesson 6 of 6 · 50 minutes · 课本 p.115、p.119–121",
                ["hua", "bai", "suan", "gui", "fandian"]))

add("02-review.html", "Y8 L12 · Review · 六题 one from every lesson", "0–8 MIN · 复习",
    "Review · Lessons 1–5",
    task_slide("复习 · 六题 · One from every lesson so far", "WHITEBOARDS · 5 MIN",
               ["① Write <b>¥45.60</b> in characters.",
                "cn:② 这些苹果怎么卖？　—— 回答它",
                "③ Translate: &ldquo;May I use RMB?&rdquo;",
                "cn:④ 他们的饭菜做 ______ 特别好吃。",
                "cn:⑤ 你一星期吃几次快餐？　—— 完整句子",
                "⑥ Write the four simple characters: corpse, household, leather, man."],
               None))

add("03-review2.html", "Y8 L12 · Review · 听力 CD 60", "0–8 MIN · 复习",
    "Review · 课本 p.119 Ex.14",
    task_slide("复习 · 听一听，打勾 · 课本 p.119 Ex.14 · CD 60", "BOOKS · 3 MIN",
               ["Six items, three options each. Played twice, ticked in the book, checked chorally.",
                "cn:① 黄瓜／苹果／西瓜　② 快餐／中餐／早餐　③ 买水果／打篮球／看电视",
                "cn:④ 周末／吃饭／朋友　⑤ 天气／爱好／家人　⑥ 炒菜／包子／米饭"],
               None)
    + "\n" + callout("note", "Connection · 接上节课",
                     "Everything in this lesson happens in <b>one</b> conversation —— and it ends with the bill. "
                     "That's the last piece.", None))

add("04-li-sc.html", "Y8 L12 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to say how much a meal cost and whether it was worth it.",
             [("I can say and write the new words", "花、百、算、贵"),
              ("I can say how much I spent", "我们一共花了两百块"),
              ("I can hedge with 不算太贵 and 左右", None),
              ("I can describe an eating-out experience in four or more sentences", None)]))

# ── Cycle 1 · 花 / 百 ──────────────────────────────────────────────
add("05-c1-words.html", "Y8 L12 · Cycle 1 · A — 花 / 百", T, "生词 · Cycle 1 of 2",
    words_slide(("花", "huā", "spend", "hua"),
                ("百", "bǎi", "hundred", "bai")))
add("06-c1-note.html", "Y8 L12 · 花 —— 你见过这个字", T, "生词 · Cycle 1 of 2",
    '  <p class="section-label">这个字你见过 · You have met this character before</p>\n'
    '  <div class="compare">\n'
    '    <div class="compare-col tell">\n'
    '      <p class="compare-head">第十课</p>\n'
    '      <p class="compare-sub">Lesson 10 — a flower</p>\n'
    '      <p class="compare-line">菜<b>花</b>儿　càihuār</p>\n'
    '      <p class="compare-line">cauliflower</p>\n'
    '    </div>\n'
    '    <div class="compare-col ask">\n'
    '      <p class="compare-head">今天</p>\n'
    '      <p class="compare-sub">Today — to spend</p>\n'
    '      <p class="compare-line">我<b>花</b>了五十块</p>\n'
    '      <p class="compare-line">I spent fifty yuan</p>\n'
    '    </div>\n  </div>\n'
    + callout("tip", "同一个字，两个意思",
              "Same character, second meaning. Nothing new to write —— only something new to <b>mean</b>.", None))
add("07-c1-examples.html", "Y8 L12 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 2",
    sentences_slide([
        ("Wǒ huā le wǔshí kuài qián.", "我<b>花</b>了五十块钱。", "I spent fifty yuan.", False),
        ("Yí ge bǐsàbǐng liùshí kuài, liǎng bǎi kuài kěyǐ mǎi sān ge.",
         "一个比萨饼六十块，两<b>百</b>块可以买三个。",
         "A pizza is sixty; two hundred buys three.", False),
        ("Wǒmen yígòng huā le liǎng bǎi kuài.", "我们一共<b>花</b>了两<b>百</b>块。",
         "We spent two hundred altogether.", True)]))
add("08-c1-write.html", "Y8 L12 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 2",
    write_slide(["上个星期我花了 ______ 块钱买 ______ 。"],
                "60 seconds. A real amount.",
                "Two sentences —— one with <b>大概</b>, one with <b>一共</b>. Both need 花 and a three-digit price.",
                None))

# ── Cycle 2 · 算 / 贵 ──────────────────────────────────────────────
add("09-c2-words.html", "Y8 L12 · Cycle 2 · A — 算 / 贵", T, "生词 · Cycle 2 of 2",
    words_slide(("算", "suàn", "regard as; count as", "suan"),
                ("贵", "guì", "expensive", "gui", "貴")))
add("10-c2-examples.html", "Y8 L12 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 2",
    sentences_slide([
        ("Zhè jiàn yīfu hěn guì.", "这件衣服很<b>贵</b>。", "These clothes are expensive.", False),
        ("Sān bǎi kuài bú suàn guì.", "三百块不<b>算贵</b>。",
         "Three hundred isn't what you'd call expensive.", False),
        ("Wǒmen měi cì dàgài huā liǎng bǎi kuài, bú suàn tài guì.",
         "我们每次大概花两百块，不<b>算</b>太<b>贵</b>。",
         "We spend roughly two hundred each time — not too expensive.", True)]))
add("11-c2-write.html", "Y8 L12 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 2",
    write_slide(["______ 块钱，不算太贵。", "______ 块钱，太贵了。"],
                "One of each. 90 seconds.",
                "One sentence with <b>可是</b> —— expensive on one side, delicious on the other.",
                "这家饭店特别贵，可是他们的炒面做得特别好吃。"))

add("12-recall.html", "Y8 L12 · Checkpoint · 认字 recall", T, "Checkpoint · 四个字",
    recall_slide(["花", "百", "算", "贵"], 4,
                 "认字 · Read them back — no pinyin, no English"))

# ── Pattern ───────────────────────────────────────────────────────
add("13-pattern.html", "Y8 L12 · 句型 · 大概 · 左右 · 不算太", T, "句型 · Hedging",
    '  <p class="section-label">句型 · 三个说法，一句话里都有</p>\n'
    '  <div class="pattern-box"><p class="pattern-text">五百块 <b>左右</b> ，<b>不算太</b> 贵。</p>'
    '<p class="pattern-note">课文二的最后一句</p></div>\n'
    + '\n' + examples_block([
        ("<b>大概</b> ＋ 数目", "goes BEFORE the amount — 大概五百块", False),
        ("数目 ＋ <b>左右</b>", "goes AFTER it — 五百块左右", False),
        ("<b>不算太</b> ＋ 形容词", "softens a verdict — 不算太贵、不算太好吃", False)],
        label="三个位置 · Where each one sits"))

add("14-examples.html", "Y8 L12 · 模仿我说 · four sentences", T, "句型 · Hedging",
    examples_block([
        ("大概一百块。", None, False),
        ("一百块左右。", None, False),
        ("不算太贵。", None, False),
        ("我们每次吃饭大概要花五百块左右，不算太贵，因为他们的饭菜做得特别好吃。",
         "Three hedges, a reason clause, and a 得 complement.", True)]))

add("15-cfu.html", "Y8 L12 · CFU · check for understanding", T, "CFU · 检查理解",
    cfu_slide([("Put 大概 in the right place.", "______ 五十块 ______ 。"),
               ("Translate: &ldquo;It isn't too expensive.&rdquo;", None),
               ("花 —— which meaning here?", "我花了一百块。"),
               ("Write <b>360</b> in characters.", None),
               ("What is missing from this sentence?", "我花了一百块钱买了。")]))

add("16-text2a.html", "Y8 L12 · 课文二 · Text 2 in full — 前半 (CD 59)", T, "课文二 · 课本 p.115",
    dialogue_block([
        ("A", "Nǐmen jiā cháng qù fàndiàn chīfàn ma?", "你们家常去饭店吃饭吗？"),
        ("B", "Chàbuduō měi liǎng xīngqī qù yí cì.", "差不多每两星期去一次。"),
        ("A", "Nǐmen jīngcháng qù nǎ jiā fàndiàn chīfàn?", "你们经常去哪家饭店吃饭？"),
        ("B", "Wǒmen jīngcháng qù yì jiā Shànghǎi fàndiàn chīfàn. Tāmen de fàncài zuò de tèbié hǎochī.",
         "我们经常去一家上海饭店吃饭。他们的饭菜做得特别好吃。")],
        label="课文二 · Text 2 · CD 59 —— 前半，齐读"))

add("16-text2b.html", "Y8 L12 · 课文二 · Text 2 in full — 后半 (CD 59)", T, "课文二 · 课本 p.115",
    dialogue_block([
        ("A", "Nǐmen shàng ge zhōumò qù le ma?", "你们上个周末去了吗？"),
        ("B", "Qù le.", "去了。"),
        ("A", "Nǐmen měi cì chīfàn dàgài yào huā duōshao qián?", "你们每次吃饭大概要<b>花</b>多少钱？"),
        ("B", "Wǔ bǎi kuài zuǒyòu, bú suàn tài guì.", "五<b>百</b>块左右，不<b>算</b>太<b>贵</b>。")],
        label="课文二 · Text 2 · CD 59 —— 后半，然后两人一组"))

add("16b-text2-q.html", "Y8 L12 · 课文二 · 听懂了吗 comprehension", "10–20 MIN · I DO", "课文二 · 课本 p.115",
    '  <p class="section-label">听懂了吗 · Comprehension —— 用中文回答</p>\n'
    + examples_block([("他们多长时间去一次饭店？", None, False),
                      ("那家饭店的饭菜怎么样？", None, False),
                      ("五百块贵不贵？为什么？", None, True)],
                     label=""))

add("17-act1.html", "Y8 L12 · Activity 1 · 开店 market and shop (We Do)",
    "20–30 MIN · WE DO", "Activity 1 · 课本 p.120 Ex.16",
    task_slide("Activity 1 · 开店 · 课本 p.120 Ex.16", "GROUPS OF 3–4 · 10 MIN",
               ["Each group opens <b>either</b> a fresh market <b>or</b> a clothing shop.",
                "cn:菜市场　黄瓜 ¥1.20/斤 · 生菜 ¥1.00/斤 · 西红柿 ¥2.00/斤",
                "cn:　　　　苹果 ¥10.00/四个 · 西瓜 ¥1.20/斤 · 橘子 ¥10.00/五个",
                "cn:服装店　牛仔裤 ¥260.00/条 · 衬衫 ¥150.00/件 · 毛衣 ¥220.00/件 · 外套 ¥200.00/件",
                "At each stall: ask <b>two</b> prices, buy at least two things, ask 一共多少钱？, "
                "and finish with a verdict —— 贵 or 不算太贵."],
               "You have <b>500 块</b> and must come back with a full outfit <b>and</b> a family dinner, "
               "visiting both a shop and a market. Compare two stalls out loud with 比, justify each buy with "
               "因为……所以, then report: what you bought, 一共花了多少钱, and what you left behind and why.",
               "这家的衬衫比那家的便宜，所以我买这件。"))

add("18-act1b.html", "Y8 L12 · Activity 1 · 示范 the model exchange", "20–30 MIN · WE DO",
    "Activity 1 · 示范",
    dialogue_block([
        ("A", "Càihuār zěnme mài?", "菜花儿怎么卖？"),
        ("B", "Sān kuài yí ge.", "三块一个。"),
        ("A", "Tǔdòu duōshao qián yì jīn?", "土豆多少钱一斤？"),
        ("B", "Yí kuài wǔ.", "一块五。"),
        ("A", "Mǎi yí ge càihuār hé yì jīn tǔdòu.", "买一个菜花儿和一斤土豆。"),
        ("B", "Yígòng sì kuài wǔ.", "一共四块五。")],
        label="示范 · 课本 p.120 —— run it like this"))

add("19-act2.html", "Y8 L12 · Activity 2 · 说说你的一次外出就餐 (You Do)",
    "30–38 MIN · YOU DO", "Activity 2 · 课本 p.119 Ex.15",
    '  <p class="section-label">Activity 2 · 说说你的一次外出就餐 · 课本 p.119 Ex.15</p>\n'
    + examples_block([
        ("上个星期六我们全家人去饭店吃饭了。", "when · who", False),
        ("我们去了一家上海饭店。", "where", False),
        ("我们吃了炒菜、炒面、粥、饺子等等。", "what you ate", False),
        ("我们还喝了可乐和汽水。", "what you drank", False),
        ("我们一共花了两百多块，不算贵。", "what it cost — and the verdict", True)],
        label="课本的示范 · The model — on screen for three minutes, then it comes down"))

add("20-act2b.html", "Y8 L12 · Activity 2 · 写五句 write it yourself", "30–38 MIN · YOU DO",
    "Activity 2 · 课本 p.119 Ex.15",
    task_slide("Activity 2 · 写五句 · A real meal out", "BOOKS · 8 MIN",
               ["Five sentences about a meal you really had —— when, where, what you ate, what you drank, "
                "what it cost and whether it was worth it.",
                "Every sentence must carry something from this lesson: a <b>了</b>, an <b>等等</b>, a price, "
                "<b>一共</b>, <b>不算太贵</b>.",
                "Three students read theirs out at the end."],
               "Write it as the 练习册 p.137 Ex.22 essay instead —— your <b>favourite restaurant</b>: how often "
               "you go （次）, what food you like, what you normally eat （一般）, what one meal costs "
               "（大概……左右）, and one sentence on why, using 得. Six to eight sentences, nothing on screen.",
               None))

add("21-game.html", "Y8 L12 · Game · 听写比赛 character dictation race", "38–43 MIN · 游戏",
    "Game · 课本 p.121 Ex.17",
    task_slide("Game · 听写比赛 · 课本 p.121 Ex.17", "GROUPS · 5 MIN",
               ["Ninety seconds to memorise. Then the screen goes <b>off</b>.",
                "cn:尸　户　革　丁　贝　·　虫　叉　食　果　欠",
                "cn:平　石　角　页　舌　·　瓜　旦　矢　皿　斗　·　青　立　寸　巾　足",
                "Teacher dictates twelve of them by <b>English meaning</b>. Most correct wins.",
                "Then 练习册 p.135 Ex.17 as the written record —— pinyin <b>and</b> character, two minutes."],
               "Dictated by <b>pinyin only</b>, and you must write a <b>word</b> containing the character, "
               "not the bare character.",
               "革 → 皮革　·　户 → 门户　·　足 → 足球"))

add("22-plenary.html", "Y8 L12 · Plenary · the whole unit", "43–50 MIN · 小结",
    "Plenary · Lessons 1–6",
    '  <p class="section-label">小结 · 回头看这六节课</p>\n'
    + recall_slide(["块 毛 分", "怎么卖", "可以", "得", "几次", "不算太贵"], 3,
                   "六节课，六个句型 · One from each lesson — read them back, then say a sentence with each")
    )

add("23-plenary2.html", "Y8 L12 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n'
    '  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Thumbs on today's four criteria —— {RATE}", None,
            "Then one show of hands: which of the six lessons do you most want another go at before the test?") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "上次你去饭店吃饭，花了多少钱？贵不贵？",
            "—— 两句话，要有「一共」和「不算太贵」或者「太贵了」。",
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下一课 · Next lesson",
            "That's the whole of Unit 4. Next we start Unit 5 —— 房子, describing where you live.", None) +
    "\n  </div>")

write_deck("l6-huaqian-text2", S, "Y8 L12 · 不算太贵 · The Whole Meal Out · Lesson 6 of 6")
