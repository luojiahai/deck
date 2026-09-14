# -*- coding: utf-8 -*-
"""Lesson 2 of 6 — 怎么卖？ Asking the price.

From docs/lesson-plans/y8-l12/02-asking-prices-mixed.md.
Text 1's first half (课本 p.110, CD 56). Every example sentence uses only
Lesson 1's money words and vocabulary from Lessons 10-11.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, title, tag, section, body, cls=""):
    S.append((f, title, tag, section, body, cls))

add("01-title.html", "Y8 L12 · Title · 怎么卖？", "Lesson 2 of 6", "Y8 · Lesson 12",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 12", "怎么卖？", "Asking the Price",
                "Lesson 2 of 6 · 50 minutes · 课本 p.110、p.112",
                ["mai-sell", "mai-buy", "jin", "yigong", "xigua"]))

add("02-review.html", "Y8 L12 · Review · money rapid fire", "0–8 MIN · 复习", "Review · Lesson 1",
    task_slide("复习 · 钱 · Money rapid fire", "WHITEBOARDS · 4 MIN",
               ["Teacher says an amount → write the <b>figure</b>. Six of them.",
                "Then teacher shows a figure → class says it <b>chorally</b>. Six more.",
                "cn:「二十块」用「元」怎么说？"],
               None))

add("03-review2.html", "Y8 L12 · Review · 动词 + 名词 verb and object", "0–8 MIN · 复习",
    "Review · 练习册 p.130 Ex.6",
    task_slide("复习 · 动词 + 名词 · 练习册 p.130 Ex.6", "PAIRS · 4 MIN",
               ["Sixteen verbs. Match each one to a noun from the box. Three minutes, one whiteboard per pair.",
                "cn:儿歌　汽车　外套　音乐　西餐　历史　钢琴　可乐",
                "cn:作业　衣服　小提琴　青菜　汉语　电影　篮球　水彩画儿",
                "Highest count reads theirs out."],
               None)
    + "\n" + callout("note", "Connection · 接上节课",
                     "买衣服、买青菜 —— today we find out how to ask what those <b>cost</b> before we buy them.", None))

add("04-li-sc.html", "Y8 L12 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to ask how much something costs and to ask for a total.",
             [("I can say and write the four new words", "买、卖、斤、一共"),
              ("I can ask a price two ways", "这些苹果怎么卖？／西瓜多少钱一斤？"),
              ("I can ask for the total and answer it", "一共多少钱？")]))

# ── Cycle 1 · 买 / 卖 ──────────────────────────────────────────────
add("05-c1-words.html", "Y8 L12 · Cycle 1 · A — 买 / 卖", T, "生词 · Cycle 1 of 2",
    words_slide(("买", "mǎi", "buy", "mai-buy", "買"),
                ("卖", "mài", "sell", "mai-sell", "賣")))
add("06-c1-examples.html", "Y8 L12 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 2",
    sentences_slide([
        ("Wǒ xiǎng mǎi yí ge xīguā.", "我想<b>买</b>一个西瓜。", "I want to buy a watermelon.", False),
        ("Tāmen mài shuǐguǒ.", "他们<b>卖</b>水果。", "They sell fruit.", False),
        ("Wǒ mǎi píngguǒ, tā mài píngguǒ.", "我<b>买</b>苹果，他<b>卖</b>苹果。",
         "I buy apples, he sells apples.", True)]))
add("07-c1-write.html", "Y8 L12 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 2",
    write_slide(["我想买 ______ 。"],
                "60 seconds. Mini whiteboards. One sentence.",
                "One sentence using <b>both</b> words — a shop that sells it and you buying it.",
                "这家店卖比萨饼，我想买一个。"))

# ── Cycle 2 · 斤 / 一共 ────────────────────────────────────────────
add("08-c2-words.html", "Y8 L12 · Cycle 2 · A — 斤 / 一共", T, "生词 · Cycle 2 of 2",
    words_slide(("斤", "jīn", "half a kilogram", "jin"),
                ("一共", "yígòng", "altogether", "yigong")))
add("09-c2-examples.html", "Y8 L12 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 2",
    sentences_slide([
        ("Yì jīn píngguǒ shí kuài qián.", "一<b>斤</b>苹果十块钱。", "A jin of apples is ten yuan.", False),
        ("Wǒ mǎi liǎng jīn júzi.", "我买两<b>斤</b>橘子。", "I'll buy two jin of tangerines.", False),
        ("Liǎng jīn júzi hé yí ge xīguā, yígòng èrshí kuài.",
         "两<b>斤</b>橘子和一个西瓜，<b>一共</b>二十块。",
         "Two jin of tangerines and a watermelon — twenty yuan altogether.", True)]))
add("10-c2-write.html", "Y8 L12 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 2",
    write_slide(["我买 ______ 和 ______ ，一共 ______ 块。"],
                "90 seconds. Work the total out — in Chinese.",
                "Three items and three prices, then the total. Add up in your head, not on paper.",
                None))

add("11-recall.html", "Y8 L12 · Checkpoint · 认字 recall", T, "Checkpoint · 买 vs 卖",
    recall_slide(["买", "卖", "斤", "一共"], 4,
                 "认字 · Read them back. Then: which one is buy and which is sell?"))

# ── Pattern ───────────────────────────────────────────────────────
add("12-pattern.html", "Y8 L12 · 句型 · asking a price", T, "句型 · Asking a price",
    '  <p class="section-label">句型 · Three questions</p>\n'
    '  <div class="stack gap-sm">\n'
    '    <div class="pattern-box"><p class="pattern-text">这些苹果 <b>怎么卖</b>？</p>'
    '<p class="pattern-note">Loose goods — you don\'t yet know what the unit is</p></div>\n'
    '    <div class="pattern-box"><p class="pattern-text">西瓜 <b>多少钱一斤</b>？</p>'
    '<p class="pattern-note">You name the unit yourself</p></div>\n'
    '    <div class="pattern-box"><p class="pattern-text"><b>一共</b>多少钱？</p>'
    '<p class="pattern-note">The total — and the answer starts with 一共 too</p></div>\n  </div>')

add("13-examples.html", "Y8 L12 · 模仿我说 · four exchanges", T, "句型 · Asking a price",
    examples_block([
        ("这些橘子怎么卖？ —— 十块钱四个。", None, False),
        ("苹果多少钱一斤？ —— 五块五一斤。", None, False),
        ("菜花儿怎么卖？ —— 三块一个。", None, False),
        ("我买一个菜花儿和两斤土豆，一共多少钱？ —— 一共六块五。", None, True)],
        note="List what you want first —— 我买 + 东西 + 和 + 东西 —— <b>then</b> ask 一共多少钱？"))

add("14-cfu.html", "Y8 L12 · CFU · check for understanding", T, "CFU · 检查理解",
    cfu_slide([("「多少钱一斤」and「一斤多少钱」— are both all right?", None),
               ("Which do you use for a whole watermelon: 一个 or 一斤?", None),
               ("You are the customer. What is wrong with this?", "我卖一个西瓜。"),
               ("Translate: &ldquo;How much altogether?&rdquo;", None),
               ("十块钱四个 —— 一个多少钱？", None)]))

add("15-text1.html", "Y8 L12 · 课文一 · Text 1 first half (CD 56)", T, "课文一 · 课本 p.110",
    dialogue_block([
        ("A", "Zhè xiē píngguǒ zěnme mài?", "这些苹果<b>怎么卖</b>？"),
        ("B", "Shí kuài (yuán) qián sì ge.", "十块（元）钱四个。"),
        ("A", "Xīguā duōshao qián yì jīn?", "西瓜<b>多少钱一斤</b>？"),
        ("B", "Liǎng kuài wǔ yì jīn.", "两块五一斤。"),
        ("A", "Wǒ mǎi sì ge píngguǒ, yí ge xīguā, zài lái liǎng jīn júzi. Yígòng duōshao qián?",
         "我<b>买</b>四个苹果、一个西瓜，再来两<b>斤</b>橘子。<b>一共</b>多少钱？"),
        ("B", "Yígòng sānshí kuài wǔ máo (jiǎo) wǔ (fēn).", "<b>一共</b>三十块五毛（角）五（分）。")],
        label="课文一 · Text 1 · CD 56"))

add("15b-text1-q.html", "Y8 L12 · 课文一 · 听懂了吗 comprehension", "10–20 MIN · I DO", "课文一 · 课本 p.110",
    '  <p class="section-label">听懂了吗 · Comprehension —— 用中文回答</p>\n'
    + examples_block([("苹果多少钱一个？", None, False),
                      ("她买了几个苹果？", None, False),
                      ("「再来两斤橘子」是什么意思？", "再来 = also give me —— 来 doing the work of 给我。", True)],
                     label=""))

add("16-act1.html", "Y8 L12 · Activity 1 · 量词 measure words (We Do)", "20–26 MIN · WE DO",
    "Activity 1 · 课本 p.112 Ex.3",
    task_slide("Activity 1 · 量词 · 课本 p.112 Ex.3", "PAIRS · 6 MIN",
               ["Twelve blanks. Fill them from the box, on one whiteboard per pair.",
                "cn:口　家　头　朵　个　位　台　条",
                "cn:三口人　一__花　一__电脑　一__学校　一__老师　一__裙子",
                "cn:一__白发　一__裤子　一__热狗　一__苹果　一__饭店　一__电视",
                "Then add today's: 一<b>斤</b>土豆、两<b>斤</b>橘子 —— 斤 is a measure word too, the one for things that get <b>weighed</b>."],
               "练习册 p.134 Ex.14 — the eighteen-item version, solo, against the clock. Then two sentences "
               "using a measure word that <b>wasn't</b> in the box.",
               "一包土豆　·　一门课"))

add("17-act2.html", "Y8 L12 · Activity 2 · 小摊 food stall (You Do)", "26–38 MIN · YOU DO",
    "Activity 2 · 课本 p.112 Ex.4",
    task_slide("Activity 2 · 小摊 · 课本 p.112 Ex.4", "GROUPS OF 3–4 · 12 MIN",
               ["cn:西红柿 ¥3.00/斤　·　菜花儿 ¥2.50/斤　·　苹果 ¥10.00/五个　·　比萨饼 ¥60.00/个",
                "Half the groups keep the stall. The other half go shopping — then swap after five minutes.",
                "At <b>each</b> stall: ask two prices using <b>both</b> question forms, buy at least two things, ask 一共多少钱？",
                "The stallholder works the total out <b>out loud</b>."],
               "You have <b>50 块</b> and must leave having spent between 45 and 50. Say aloud what you are "
               "<b>not</b> buying and why. Then report your total and your change — in Chinese.",
               "我想买比萨饼，可是六十块，太贵了。我买两斤西红柿和一斤菜花儿。"))

add("18-act2-model.html", "Y8 L12 · Activity 2 · 示范 the model exchange", "26–38 MIN · YOU DO",
    "Activity 2 · 示范",
    dialogue_block([
        ("A", "Xīhóngshì zěnme mài?", "西红柿怎么卖？"),
        ("B", "Sān kuài yì jīn.", "三块一斤。"),
        ("A", "Bǐsàbǐng duōshao qián yí ge?", "比萨饼多少钱一个？"),
        ("B", "Liùshí kuài.", "六十块。"),
        ("A", "Wǒ mǎi liǎng jīn xīhóngshì hé yí ge bǐsàbǐng. Yígòng duōshao qián?",
         "我买两斤西红柿和一个比萨饼。一共多少钱？"),
        ("B", "Yígòng liùshí liù kuài.", "一共六十六块。")],
        label="示范 · Run it like this")
    + "\n" + callout("note", "第二轮 · Second round",
                     "Pinyin comes <b>down</b> for the second round. Same task, nothing on screen.", None))

add("19-game.html", "Y8 L12 · Game · 排句子 Sentence Jumble", "38–43 MIN · 游戏", "Game · 排句子",
    task_slide("Game · 排句子 · Sentence Jumble", "PAIRS · 5 MIN",
               ["One jumble at a time. Reorder it on a whiteboard, hold it up. First correct board scores.",
                "cn:① 怎么 / 这些 / 卖 / 苹果",
                "cn:② 一斤 / 多少 / 西瓜 / 钱",
                "cn:③ 多少 / 一共 / 钱",
                "cn:④ 两斤 / 我 / 橘子 / 买",
                "cn:⑤ 钱 / 一共 / 三十块 / 五毛"],
               "After reordering, say a <b>second</b> sentence that answers or follows on from yours — "
               "out loud, nothing written.",
               None))

add("20-plenary.html", "Y8 L12 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n'
    '  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Write 1, 2, 3 on your whiteboard and put {RATE} beside each.", None) + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Write the <b>two</b> ways of asking a price — 香蕉 in one, 土豆 in the other.",
            "香蕉怎么卖？　土豆多少钱一斤？",
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "We finish the market dialogue and learn to ask <b>permission</b>.", "我可以用人民币吗？") +
    "\n  </div>")

write_deck("l2-asking-prices", S, "Y8 L12 · 怎么卖？ Asking the Price · Lesson 2 of 6")
