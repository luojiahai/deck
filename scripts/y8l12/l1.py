# -*- coding: utf-8 -*-
"""Lesson 1 of 6 — 人民币 · the six money words.

From docs/lesson-plans/y8-l12/01-money-rmb-mixed.md. Every example
sentence uses only words already taught: 这/是/我/有/个/苹果 from Book 1
and 汉堡包 from Lesson 11. The only new things on any Slide B are the
two words that slide is teaching.

No audio in this lesson — the un/ün pinyin exercise (课本 p.111 Ex.2,
track 57) is out at the teacher's request, and it was the only audio item.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, title, tag, section, body, cls=""):
    S.append((f, title, tag, section, body, cls))

add("01-title.html", "Y8 L12 · Title · 人民币", "Lesson 1 of 6", "Y8 · Lesson 12",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 12", "人民币", "Talking About Money",
                "Lesson 1 of 6 · 50 minutes · 课本 p.110–111",
                ["qian", "kuai", "mao", "jiao", "fen"]))

add("02-review.html", "Y8 L12 · Review · Lesson 11", "0–8 MIN · 复习", "Review · Lesson 11",
    '  <p class="section-label">复习 · Five on whiteboards — hold them up together</p>\n'
    + examples_block([
        ("你午饭一般吃什么？", "Answer in Chinese.", False),
        ("我晚饭吃米饭 ______ 面条。", "One word in the gap.", False),
        ("你想吃中餐 ______ 西餐？", "One word in the gap.", False),
        ("&ldquo;It is likely to rain this afternoon.&rdquo;", "Translate into Chinese.", False),
        ("你们家常去饭店吃饭吗？", "Answer in a full sentence.", True)],
        label="复习 · 五题 · From Lesson 11")
    + "\n" + callout("note", "Connection · 接上节课",
                     "You can say <b>where</b> you eat and <b>what</b> you eat.",
                     "今天学的是最有用的一部分 —— 钱。",
                     "Today we add the part everybody actually needs at a market or a restaurant."))

add("03-li-sc.html", "Y8 L12 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to read and say amounts of money in Chinese renminbi.",
             [("I can say the six money words", "钱、块、元、毛、角、分"),
              ("I can read an amount aloud and write it down", "三十块五毛五分"),
              ("I can explain when Chinese uses 块/毛 and when it uses 元/角", None)]))

# ── Cycle 1 · 钱 / 块 ──────────────────────────────────────────────
add("04-c1-words.html", "Y8 L12 · Cycle 1 · A — 钱 / 块", T, "生词 · Cycle 1 of 3",
    words_slide(("钱", "qián", "money", "qian", "錢"),
                ("块", "kuài", "yuan （spoken）", "kuai", "塊")))
add("05-c1-examples.html", "Y8 L12 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 3",
    sentences_slide([
        ("Zhè shì shí kuài qián.", "这是十<b>块钱</b>。", "This is ten yuan.", False),
        ("Wǒ yǒu wǔ kuài qián.", "我有五<b>块钱</b>。", "I have five yuan.", False),
        ("Yí ge hànbǎobāo èrshí kuài qián.", "一个汉堡包二十<b>块钱</b>。",
         "A hamburger is twenty yuan.", True)]))
add("06-c1-write.html", "Y8 L12 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 3",
    write_slide(["我有 ______ 块钱。"],
                "60 seconds. Mini whiteboards. One sentence.",
                "Write <b>two</b> questions with a price in each, using two different Lesson 11 foods.",
                "一个热狗多少块钱？一个比萨饼呢？"))

# ── Cycle 2 · 元 / 毛 ──────────────────────────────────────────────
add("07-c2-words.html", "Y8 L12 · Cycle 2 · A — 元 / 毛", T, "生词 · Cycle 2 of 3",
    words_slide(("元", "yuán", "yuan （written）", "yuan"),
                ("毛", "máo", "1/10 yuan （spoken）", "mao")))
add("08-c2-examples.html", "Y8 L12 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 3",
    sentences_slide([
        ("Wǔ kuài = wǔ yuán.", "五块 = 五<b>元</b>。", "Five kuai = five yuan.", False),
        ("Yí ge píngguǒ sān máo qián.", "一个苹果三<b>毛</b>钱。", "An apple is three mao.", False),
        ("Shí yuán wǔ máo.", "十<b>元</b>五<b>毛</b>。", "Ten yuan fifty.", True)]))
add("09-c2-write.html", "Y8 L12 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 3",
    write_slide(["______ 元 ______ 毛。"],
                "Write any amount — then read it aloud the <b>spoken</b> way.",
                "Write three prices: one in 块毛, one in 元角, one written <b>both</b> ways.",
                "十二块五毛 = 十二元五角"))

# ── Cycle 3 · 角 / 分 ──────────────────────────────────────────────
add("10-c3-words.html", "Y8 L12 · Cycle 3 · A — 角 / 分", T, "生词 · Cycle 3 of 3",
    words_slide(("角", "jiǎo", "1/10 yuan （written）", "jiao"),
                ("分", "fēn", "1/100 yuan", "fen")))
add("11-c3-examples.html", "Y8 L12 · Cycle 3 · B — 例句", T, "生词 · Cycle 3 of 3",
    sentences_slide([
        ("Sān máo = sān jiǎo.", "三毛 = 三<b>角</b>。", "Three mao = three jiao.", False),
        ("Yì fēn qián.", "一<b>分</b>钱。", "One fen.", False),
        ("Yí kuài wǔ jiǎo wǔ fēn.", "一块五<b>角</b>五<b>分</b>。", "One yuan fifty-five.", True)]))
add("12-c3-write.html", "Y8 L12 · Cycle 3 · C — 写一句", T, "生词 · Cycle 3 of 3",
    write_slide(["______ 块 ______ 毛 ______ 分。"],
                "One amount. Then say it aloud to your partner.",
                "Write the same amount again using <b>元角分</b>, then say it once more the spoken way.",
                "一块五毛五分 = 一元五角五分"))

add("13-recall.html", "Y8 L12 · Checkpoint · 认字 recall", T, "Checkpoint · 六个字",
    recall_slide(["钱", "块", "元", "毛", "角", "分"], 3,
                 "认字 · Read them back — no pinyin, no English. Then backwards."))

# ── Pattern ───────────────────────────────────────────────────────
add("14-pattern.html", "Y8 L12 · 句型 · reading an amount", T, "句型 · Reading an amount",
    pattern_slide("三十 <b>块</b> 五 <b>毛</b> 五 <b>分</b>",
                  "Largest unit first. No word for &ldquo;and&rdquo; — the units do that work."))

add("15-examples.html", "Y8 L12 · 模仿我说 · four amounts", T, "句型 · Reading an amount",
    examples_block([
        ("十块。", "¥10.00", False),
        ("十块五毛。", "¥10.50", False),
        ("三十块五毛五分。", "¥30.55", False),
        ("一百二十块五毛 —— 用「元角」怎么说？", "¥120.50 — now say it the written way.", True)]))

add("16-note.html", "Y8 L12 · NOTE · 块/元 · 毛/角", T, "课本 p.111 NOTE",
    '  <p class="section-label">课本 p.111 · NOTE</p>\n'
    '  <div class="compare">\n'
    '    <div class="compare-col ask">\n'
    '      <p class="compare-head">说 · Spoken</p>\n'
    '      <p class="compare-sub">What people actually say</p>\n'
    '      <p class="compare-line"><b>块</b> · <b>毛</b> · 分</p>\n'
    '      <p class="compare-line">五<b>块</b> · 三<b>毛</b></p>\n'
    '    </div>\n'
    '    <div class="compare-col tell">\n'
    '      <p class="compare-head">写 · Written</p>\n'
    '      <p class="compare-sub">Price tags, receipts, the notes themselves</p>\n'
    '      <p class="compare-line"><b>元</b> · <b>角</b> · 分</p>\n'
    '      <p class="compare-line">五<b>元</b> · 三<b>角</b></p>\n'
    '    </div>\n  </div>\n'
    + callout("tip", "分 doesn't change", "分 is the same in both. It is only the top two units that swap.",
              None, "五块 = 五元　·　三毛 = 三角　·　五分 = 五分"))

add("17-cfu.html", "Y8 L12 · CFU · check for understanding", T, "CFU · 检查理解",
    cfu_slide([("「三毛」= 几角？", None),
               ("Write ¥25.60 in characters — both ways.", None),
               ("Read this aloud: 一百零五块", "Did you hear the 零?"),
               ("What is wrong with this? ", "五钱块"),
               ("一块 = 几毛？", None)]))

# ── Flexible Practice ─────────────────────────────────────────────
add("18-summary.html", "Y8 L12 · 词汇总览 · summary board", "20–27 MIN · WE DO", "词汇总览",
    summary_slide([("钱", "qian"), ("块", "kuai"), ("元", "yuan"),
                   ("毛", "mao"), ("角", "jiao"), ("分", "fen")], 6,
                  "词汇总览 · Stays on screen for the whole activity"))

add("19-act1a.html", "Y8 L12 · Activity 1 · 钱币板 money board", "20–27 MIN · WE DO",
    "Activity 1 · 课本 p.111 Ex.1",
    money_row([("一毛（角）", "jiao"), ("五毛（角）", "mao"), ("一块（元）", "kuai"),
               ("一分", "fen"), ("一百块", "renminbi"), ("钱", "qian")],
              "Activity 1 · 认一认 · 课本 p.111 Ex.1 — say each one chorally"))

add("19-act1b.html", "Y8 L12 · Activity 1 · 卡片对练 card pairs (We Do)", "20–27 MIN · WE DO",
    "Activity 1 · 课本 p.111 Ex.1",
    task_slide("Activity 1 · 卡片对练 · Card pairs", "PAIRS · 7 MIN",
               ["Shuffle your card set. One holds a card up, the other says it. 30 seconds each way.",
                "<b>Second round:</b> put two or three cards down together — the partner says the <b>total</b>.",
                "cn:五十块 + 二十块 + 五毛 → 七十块五毛"],
               "Say each total <b>twice</b> — once as 块/毛, once as 元/角 — then say what it could buy.",
               "七十块五毛。七十元五角。这些钱可以吃七个汉堡包。"))

add("20-act2.html", "Y8 L12 · Activity 2 · 听写价钱 listen and write (You Do)",
    "27–37 MIN · YOU DO", "Activity 2 · 练习册 p.129 Ex.2",
    task_slide("Activity 2 · 听写价钱 · Listen and write the amount", "WHITEBOARDS · 10 MIN",
               ["Teacher reads an amount in Chinese. Write the <b>figure</b>. Hold it up.",
                "Twice each for the first four, once after that.",
                "cn:五块 · 十二块 · 三毛 · 一块五毛 · 二十块八毛 · 九十九块",
                "cn:一百块 · 三十块五毛五分 · 六块二毛 · 四十五块 · 二百块 · 一百零八块五毛",
                "<b>Then flip it:</b> 练习册 p.129 Ex.2 — seven pictures of notes. Write each amount in <b>characters</b>."],
               "Write all seven <b>both</b> ways, then one sentence each for two of them saying what that money could buy.",
               "一百块可以买十个热狗。"))

add("21-game.html", "Y8 L12 · Game · 拍价钱 Slap the Board", "37–43 MIN · 游戏", "Game · 拍价钱",
    task_slide("Game · 拍价钱 · Slap the Board", "TWO AT THE BOARD · 6 MIN",
               ["Nine amounts written large on the board, in characters.",
                "cn:五毛 · 一块 · 五块 · 十块 · 二十块 · 五十块 · 一百块 · 三块五 · 十二块八毛",
                "Teacher calls an amount — first to slap it scores. Winner stays on."],
               "Call a <b>sum</b> instead of an amount （五块加五块 → slap 十块）, or call it in 元/角 so the "
               "student has to slap the 块/毛 version.",
               None))

add("22-plenary.html", "Y8 L12 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n'
    '  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Thumbs on each success criterion — {RATE}", None,
            "Watch criterion 3 — the 块/元 split is the one that fades before next lesson.") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Write <b>¥32.50</b> in Chinese characters — then write it again the other way.",
            "三十二块五毛　/　三十二元五角",
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "How to <b>ask</b> the price.", "这些苹果怎么卖？") +
    "\n  </div>")

write_deck("l1-money-rmb", S, "Y8 L12 · 人民币 Money · Lesson 1 of 6")
