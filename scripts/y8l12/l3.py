# -*- coding: utf-8 -*-
"""Lesson 3 of 6 — 我可以用人民币吗？ Permission, and Text 1 in full.

From docs/lesson-plans/y8-l12/03-keyi-text1-mixed.md.
Carries 课本 p.114 Ex.6 (CD 58) and Ex.7, the simple characters 尸户革丁.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, title, tag, section, body, cls=""):
    S.append((f, title, tag, section, body, cls))

add("01-title.html", "Y8 L12 · Title · 我可以用人民币吗？", "Lesson 3 of 6", "Y8 · Lesson 12",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 12", "我可以用人民币吗？", "Asking Permission",
                "Lesson 3 of 6 · 50 minutes · 课本 p.110、p.114",
                ["keyi", "renminbi", "bi", "yong", "qian"]))

add("02-review.html", "Y8 L12 · Review · 课文一 pair dialogue", "0–8 MIN · 复习", "Review · Lesson 2",
    task_slide("复习 · 课文一 · From memory", "PAIRS · 5 MIN",
               ["Rebuild the first half of Text 1 with <b>only</b> these English prompts on screen.",
                "① how are these apples sold　② how much per jin for watermelon",
                "③ I'll buy four apples, a watermelon and two jin of tangerines　④ how much altogether",
                "Rehearse twice, swap roles. Two pairs perform."],
               None))

add("03-review2.html", "Y8 L12 · Review · 改错 correct the teacher", "0–8 MIN · 复习",
    "Review · 改错",
    '  <p class="section-label">复习 · 改错 · Correct the teacher</p>\n'
    '  <div class="stack gap-md">\n'
    '    <div class="warn-box"><div><p class="cb-label">✗ 这句话错了</p>'
    '<p class="cb-cn">这些苹果卖怎么？</p></div></div>\n'
    '    <div class="warn-box"><div><p class="cb-label">✗ 这句话错了</p>'
    '<p class="cb-cn">西瓜一斤多少？</p></div></div>\n'
    '    <div class="warn-box"><div><p class="cb-label">✗ 这句话错了 —— 你是顾客</p>'
    '<p class="cb-cn">我卖两斤橘子。</p></div></div>\n  </div>\n'
    + callout("note", "Connection · 接上节课",
              "You've bought the fruit and you know the total. One thing left to settle at the till —— "
              "<b>what you're allowed to pay with</b>.", None))

add("04-li-sc.html", "Y8 L12 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to ask whether we are allowed to do something, using 可以.",
             [("I can say and write the new words", "用、人民币、可以"),
              ("I can ask permission and answer it", "我可以……吗？—— 可以。／不可以。"),
              ("I can read the whole of Text 1 aloud with a partner", None),
              ("I can write the four simple characters", "尸、户、革、丁")]))

# ── Cycle 1 · 用 / 可以 ────────────────────────────────────────────
add("05-c1-words.html", "Y8 L12 · Cycle 1 · A — 用 / 可以", T, "生词 · Cycle 1 of 3",
    words_slide(("用", "yòng", "use", "yong"),
                ("可以", "kěyǐ", "can; may", "keyi")))
add("06-c1-examples.html", "Y8 L12 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 3",
    sentences_slide([
        ("Wǒ yòng Hànyǔ shuō.", "我<b>用</b>汉语说。", "I'll say it in Chinese.", False),
        ("Wǒ kěyǐ chī ma?", "我<b>可以</b>吃吗？", "May I eat?", False),
        ("Wǒ kěyǐ yòng Yīngyǔ shuō ma?", "我<b>可以用</b>英语说吗？", "May I say it in English?", True)]))
add("07-c1-write.html", "Y8 L12 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 3",
    write_slide(["我可以 ______ 吗？"],
                "60 seconds. Something you would really ask.",
                "Two questions — one to a teacher, one to a parent — both using <b>可以</b> and <b>用</b>.",
                "我可以用你的电脑吗？"))

# ── Cycle 2 · 人民 / 币 ────────────────────────────────────────────
add("08-c2-words.html", "Y8 L12 · Cycle 2 · A — 人民 / 币", T, "生词 · Cycle 2 of 3",
    words_slide(("人民", "rénmín", "the people", None),
                ("币", "bì", "currency", "bi", "幣")))
add("09-c2-examples.html", "Y8 L12 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 3",
    sentences_slide([
        ("Rénmín hěn duō.", "<b>人民</b>很多。", "There are a lot of people.", False),
        ("Zhè shì Zhōngguó de qiánbì.", "这是中国的钱<b>币</b>。", "This is Chinese currency.", False),
        ("Rénmín + bì = rénmínbì.", "<b>人民</b> ＋ <b>币</b> ＝ 人民币。",
         "The people + currency = the people's currency.", True)]))
add("10-c2-write.html", "Y8 L12 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 3",
    write_slide(["中国的钱是 ______ 。"],
                "60 seconds. One sentence.",
                "China uses 人民币. What does <b>your</b> country use? Write one sentence.",
                None))

# ── Cycle 3 · 人民币 ───────────────────────────────────────────────
add("11-c3-words.html", "Y8 L12 · Cycle 3 · A — 人民币", T, "生词 · Cycle 3 of 3",
    words_slide(("人民币", "rénmínbì", "RMB, Chinese currency", "renminbi")))
add("12-c3-examples.html", "Y8 L12 · Cycle 3 · B — 例句", T, "生词 · Cycle 3 of 3",
    sentences_slide([
        ("Wǒ yǒu yìbǎi kuài rénmínbì.", "我有一百块<b>人民币</b>。", "I have a hundred yuan of RMB.", False),
        ("Wǒ kěyǐ yòng rénmínbì ma?", "我可以用<b>人民币</b>吗？", "May I use RMB?", False),
        ("Zài Zhōngguó, wǒmen yòng rénmínbì.", "在中国，我们用<b>人民币</b>。",
         "In China we use RMB.", True)]))
add("13-c3-write.html", "Y8 L12 · Cycle 3 · C — 写一句", T, "生词 · Cycle 3 of 3",
    write_slide(["我可以用 ______ 吗？"],
                "60 seconds. Then read it to your partner and get an answer.",
                "Write a two-line exchange: the question, then a <b>refusal with a reason</b>.",
                "不可以，因为你还没有做作业。"))

add("14-recall.html", "Y8 L12 · Checkpoint · 认字 recall", T, "Checkpoint · 五个词",
    recall_slide(["用", "可以", "人民", "币", "人民币"], 5,
                 "认字 · Read them back — no pinyin, no English"))

# ── Pattern ───────────────────────────────────────────────────────
add("15-pattern.html", "Y8 L12 · 句型 · 可以", T, "句型 · Asking permission",
    pattern_slide("我 <b>可以</b> ＋ 动词 ＋ 吗？",
                  "可以 goes BEFORE the verb. ✗ 我用可以人民币吗")
    + "\n" + callout("tip", "两种说法 · Two shapes, one meaning",
                     "The book uses both. The second is the one 练习册 p.132 drills.",
                     "我<b>可以</b>现在回家<b>吗</b>？　　我现在想回家，<b>可以吗</b>？", None))

add("16-examples.html", "Y8 L12 · 模仿我说 · four questions", T, "句型 · Asking permission",
    examples_block([
        ("我可以吃吗？", None, False),
        ("我可以用人民币吗？", None, False),
        ("我现在可以听音乐吗？", None, False),
        ("我一边做作业一边听音乐，可以吗？", "The tag form — whole sentence first, 可以吗 on the end.", True)]))

add("17-cfu.html", "Y8 L12 · CFU · check for understanding", T, "CFU · 检查理解",
    cfu_slide([("Does 可以 go before or after the verb?", None),
               ("Translate: &ldquo;May I use Chinese?&rdquo;", None),
               ("Answer this question.", "我可以吃你的苹果吗？"),
               ("Turn this into the tag form.", "我可以现在回家吗？"),
               ("Thumbs up if 币 means &ldquo;currency&rdquo;, down if it means money in general.", None)]))

add("18-text1a.html", "Y8 L12 · 课文一 · Text 1 in full — 前半 (CD 56)", T, "课文一 · 课本 p.110",
    dialogue_block([
        ("A", "Zhè xiē píngguǒ zěnme mài?", "这些苹果怎么卖？"),
        ("B", "Shí kuài (yuán) qián sì ge.", "十块（元）钱四个。"),
        ("A", "Xīguā duōshao qián yì jīn?", "西瓜多少钱一斤？"),
        ("B", "Liǎng kuài wǔ yì jīn.", "两块五一斤。")],
        label="课文一 · Text 1 · CD 56 —— 前半，齐读"))

add("18-text1b.html", "Y8 L12 · 课文一 · Text 1 in full — 后半 (CD 56)", T, "课文一 · 课本 p.110",
    dialogue_block([
        ("A", "Wǒ mǎi sì ge píngguǒ, yí ge xīguā, zài lái liǎng jīn júzi. Yígòng duōshao qián?",
         "我买四个苹果、一个西瓜，再来两斤橘子。一共多少钱？"),
        ("B", "Yígòng sānshí kuài wǔ máo (jiǎo) wǔ (fēn).", "一共三十块五毛（角）五（分）。"),
        ("A", "Wǒ kěyǐ yòng rénmínbì ma?", "我<b>可以用人民币</b>吗？"),
        ("B", "Kěyǐ.", "<b>可以</b>。")],
        label="课文一 · Text 1 · CD 56 —— 后半，然后两人一组"))

add("18b-text1-q.html", "Y8 L12 · 课文一 · 听懂了吗 comprehension", "10–20 MIN · I DO", "课文一 · 课本 p.110",
    '  <p class="section-label">听懂了吗 · Comprehension —— 用中文回答</p>\n'
    + examples_block([("她买了什么？", None, False),
                      ("一共多少钱？", None, False),
                      ("她用什么钱？", None, True)],
                     label=""))

add("19-act1.html", "Y8 L12 · Activity 1 · 可以吗？ (We Do)", "20–27 MIN · WE DO",
    "Activity 1 · 练习册 p.132 Ex.9",
    task_slide("Activity 1 · 可以吗？ · 练习册 p.132 Ex.9", "WHITEBOARDS · 7 MIN",
               ["Complete each one into a full 可以吗？question. One at a time, all held up together.",
                "cn:我用<u>　英语　</u>说，可以吗？",
                "cn:我用 ______ 买这些衣服，可以吗？",
                "cn:我一边做作业 ______ ，可以吗？",
                "cn:我今天晚上想 ______ ，可以吗？",
                "cn:我再打一会儿 ______ ，可以吗？",
                "cn:______ ，可以吗？　　—— entirely your own"],
               "Write the <b>answer</b> to each of your last three, and make one a refusal with a reason. "
               "Then 练习册 p.131 Ex.7 —— one sentence of your own for 要、不要、条、应该、可以、会.",
               None))

add("20-act2.html", "Y8 L12 · Activity 2 · 听力 CD 58 (You Do)", "27–33 MIN · YOU DO",
    "Activity 2 · 课本 p.114 Ex.6",
    task_slide("Activity 2 · 听一听，打勾 · 课本 p.114 Ex.6 · CD 58", "SOLO, THEN PAIRS · 6 MIN",
               ["Six items, three options each. Played <b>twice</b>. Tick in the book, then check in pairs.",
                "The items reach back across the whole year —— weather, illness, 除了……以外, food, phone language.",
                "<b>Don't pre-teach.</b> Working around an unknown word is exactly what the test's listening asks for."],
               "Write the <b>whole sentence</b> you hear for items 3, 4 and 5 instead of ticking. Then rewrite item 5 about yourself.",
               None))

add("21-act3.html", "Y8 L12 · Activity 3 · 简单字 尸户革丁", "33–38 MIN · YOU DO",
    "Activity 3 · 课本 p.114 Ex.7",
    '  <p class="section-label">Activity 3 · 简单字 · 课本 p.114 Ex.7 · 练习册 p.132 Ex.10</p>\n'
    '  <div class="stack gap-sm">\n'
    '    <div class="stroke-row"><p class="stroke-char">尸</p><div class="stroke-meta">'
    '<p class="stroke-py">shī</p><p class="stroke-en">corpse</p><p class="stroke-count">3 strokes</p></div></div>\n'
    '    <div class="stroke-row"><p class="stroke-char">户</p><div class="stroke-meta">'
    '<p class="stroke-py">hù</p><p class="stroke-en">household</p><p class="stroke-count">4 strokes</p></div></div>\n'
    '    <div class="stroke-row"><p class="stroke-char">革</p><div class="stroke-meta">'
    '<p class="stroke-py">gé</p><p class="stroke-en">leather</p><p class="stroke-count">9 strokes</p></div></div>\n'
    '    <div class="stroke-row"><p class="stroke-char">丁</p><div class="stroke-meta">'
    '<p class="stroke-py">dīng</p><p class="stroke-en">man</p><p class="stroke-count">2 strokes</p></div></div>\n'
    '  </div>\n  <div style="height:18px"></div>\n'
    + callout("warn", "这两个字最难分 · The whole difficulty",
              "户 is 尸 with a dot on top. That is the only difference.", "尸 · 户", None))

add("22-game.html", "Y8 L12 · Game · 写字接力 Writing Relay", "38–43 MIN · 游戏", "Game · 写字接力",
    task_slide("Game · 写字接力 · Writing Relay", "TEAMS · 5 MIN",
               ["Teams line up. Teacher calls a character by its <b>English meaning</b> —— &ldquo;household!&rdquo;",
                "First student runs up, writes it, runs back. Next student.",
                "Wrong stroke order can be <b>challenged</b> by the other team for a bonus point."],
               "Call by <b>pinyin only</b>, and the runner must write a <b>word</b> containing the character, "
               "not the bare character.",
               "户 → 门户　·　革 → 皮革　·　足 → 足球"))

add("23-plenary.html", "Y8 L12 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n'
    '  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Thumbs on each of the four criteria —— {RATE}", None) + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Write <b>one</b> 可以 question you would actually ask a teacher. One sentence.", None,
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "From the market to the restaurant —— and how to say the food is <b>especially</b> good.",
            "他们的饭菜做得特别好吃。") +
    "\n  </div>")

write_deck("l3-keyi-text1", S, "Y8 L12 · 我可以用人民币吗？ Permission · Lesson 3 of 6")
