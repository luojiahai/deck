# -*- coding: utf-8 -*-
"""Lesson 5 of 6 — 几次？大概多少钱？ Frequency and approximation.

From docs/lesson-plans/y8-l12/05-ci-guo-dagai-mixed.md.
Carries 课本 p.118 Ex.13, the four-tense revision grid — the unit-test
preparation that 课本 p.118 Ex.12 gave way to.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, title, tag, section, body, cls=""):
    S.append((f, title, tag, section, body, cls))

add("01-title.html", "Y8 L12 · Title · 几次？大概多少钱？", "Lesson 5 of 6", "Y8 · Lesson 12",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 12", "几次？", "How Often, and Roughly How Much",
                "Lesson 5 of 6 · 50 minutes · 课本 p.115–118",
                ["ci", "yici", "dagai", "fandian", "kuaican"]))

add("02-review.html", "Y8 L12 · Review · 「得」接龙 chain round the class", "0–8 MIN · 复习",
    "Review · Lesson 4",
    task_slide("复习 · 「得」接龙 · Chain response", "WHOLE CLASS · 4 MIN",
               ["Each student adds one 得 sentence about the person on their <b>left</b>.",
                "cn:他画画儿画得很好 → 她跳舞跳得很美 → ……",
                "No repeating a verb. If someone stalls, the class supplies the verb and they build the sentence."],
               None))

add("03-review2.html", "Y8 L12 · Review · 「得」quick quiz", "0–8 MIN · 复习", "Review · Lesson 4",
    task_slide("复习 · 四题 · On whiteboards", "WHITEBOARDS · 4 MIN",
               ["① Translate: &ldquo;The food at this restaurant is especially delicious.&rdquo;",
                "cn:② 姐姐的小提琴拉 ______ 不太好听。",
                "cn:③ 排一排（最强的在前）：很好吃／不好吃／特别好吃／不太好吃",
                "cn:④ 他得跑很快。　—— 哪里错了？"],
               None)
    + "\n" + callout("note", "Connection · 接上节课",
                     "You can say the food is especially good. Now —— how <b>often</b> do you actually go, "
                     "and what does it cost you?", None))

add("04-li-sc.html", "Y8 L12 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to say how many times we do something and to give an approximate amount.",
             [("I can say and write the new words", "次、一次、大概"),
              ("I can ask and answer with 几次", "你去过北京几次？／你一星期吃几次快餐？"),
              ("I can use 大概 to give a rough amount", "大概花五十块")]))

# ── Cycle 1 · 次 / 一次 ────────────────────────────────────────────
add("05-c1-words.html", "Y8 L12 · Cycle 1 · A — 次 / 一次", T, "生词 · Cycle 1 of 2",
    words_slide(("次", "cì", "times （measure word for actions）", "ci"),
                ("一次", "yícì", "once", "yici")))
add("06-c1-examples.html", "Y8 L12 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 2",
    sentences_slide([
        ("Wǒ yì xīngqī qù yí cì.", "我一星期去<b>一次</b>。", "I go once a week.", False),
        ("Wǒ yí ge yuè kàn liǎng cì diànyǐng.", "我一个月看两<b>次</b>电影。",
         "I see two films a month.", False),
        ("Wǒ qù guo Běijīng sān cì, qù guo Shànghǎi yí cì.",
         "我去过北京三<b>次</b>，去过上海<b>一次</b>。",
         "I've been to Beijing three times and Shanghai once.", True)]))
add("07-c1-write.html", "Y8 L12 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 2",
    write_slide(["我一星期 ______ 几次？", "我一星期 ______ ______ 次。"],
                "Ask it, then answer it. 90 seconds.",
                "Three sentences —— one with 一星期, one with 一个月, one with 一年. All three need 次.",
                None))

# ── Cycle 2 · 大概 ────────────────────────────────────────────────
add("08-c2-words.html", "Y8 L12 · Cycle 2 · A — 大概", T, "生词 · Cycle 2 of 2",
    words_slide(("大概", "dàgài", "roughly; probably", "dagai")))
add("09-c2-examples.html", "Y8 L12 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 2",
    sentences_slide([
        ("Zhè ge dàgài shí kuài qián.", "这个<b>大概</b>十块钱。", "This is roughly ten yuan.", False),
        ("Wǒ dàgài měi tiān chī liǎng zhǒng shuǐguǒ.", "我<b>大概</b>每天吃两种水果。",
         "I probably eat two kinds of fruit a day.", False),
        ("Wǒ yí ge yuè dàgài kàn liǎng cì diànyǐng.", "我一个月<b>大概</b>看两<b>次</b>电影。",
         "I see roughly two films a month.", True)]))
add("10-c2-write.html", "Y8 L12 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 2",
    write_slide(["我每个月大概花 ______ 块钱买 ______ 。"],
                "60 seconds. A real amount, in Chinese.",
                "One sentence with <b>大概</b> and one with <b>差不多</b> —— then say what the difference is.",
                "大概 = roughly　·　差不多 = nearly"))

add("11-recall.html", "Y8 L12 · Checkpoint · 认字 recall", T, "Checkpoint · 三个词",
    recall_slide(["次", "一次", "大概"], 3,
                 "认字 · Read them back — no pinyin, no English"))

# ── Two patterns ──────────────────────────────────────────────────
add("12-pattern.html", "Y8 L12 · 句型 · 次", T, "句型 · How often",
    pattern_slide("你 ＋ 一星期/一个月 ＋ 动词 ＋ <b>几次</b> ＋ 宾语？",
                  "The time period comes first. 几次 sits before the object.")
    + "\n" + callout("tip", "回答 · Answering",
                     "Same shape, with the number in place of 几.",
                     "你一星期吃<b>几次</b>快餐？　—— 我一星期吃<b>两次</b>快餐。", None))

add("13-pattern2.html", "Y8 L12 · 句型 · 过 ＋ 几次", T, "句型 · Have you ever",
    pattern_slide("你 ＋ 动词 ＋ <b>过</b> ＋ 地方 ＋ <b>几次</b>？",
                  "过 you already know from Unit 3 — now it carries 次.")
    + "\n" + callout("warn", "否定的说法 · The negative — 课本 p.116",
                     "&ldquo;Not even once.&rdquo; Without this, students reach for ✗ 没有几次.",
                     "你去过北京几次？　—— <b>一次也没有去过</b>。", None))

add("14-examples.html", "Y8 L12 · 模仿我说 · four questions", T, "句型 · How often",
    examples_block([
        ("你一星期看几次电视？", None, False),
        ("你一个月吃几次中餐？", None, False),
        ("你去过美国几次？ —— 一次也没有去过。", None, False),
        ("我们家差不多每两星期去一次饭店，每次大概花两百块。",
         "Frequency + 次 + 大概, in one sentence.", True)]))

add("15-cfu.html", "Y8 L12 · CFU · check for understanding", T, "CFU · 检查理解",
    cfu_slide([("Translate: &ldquo;I eat fast food twice a week.&rdquo;", None),
               ("Where does 几次 go?", "你一个月看 ______ 电影？"),
               ("Answer —— and use the negative form if the answer is none.", "你去过中国几次？"),
               ("次 or 种? 两 ___ 水果?　两 ___ 电影?", None),
               ("大概五十块 and 五十块左右 —— same or different?", None)]))

add("16-text2.html", "Y8 L12 · 课文二 · the frequency lines (CD 59)", T, "课文二 · 课本 p.115",
    dialogue_block([
        ("A", "Nǐmen jiā cháng qù fàndiàn chīfàn ma?", "你们家常去饭店吃饭吗？"),
        ("B", "Chàbuduō měi liǎng xīngqī qù yí cì.", "差不多每两星期去<b>一次</b>。"),
        ("A", "Nǐmen měi cì chīfàn dàgài yào huā duōshao qián?",
         "你们每<b>次</b>吃饭<b>大概</b>要花多少钱？")],
        label="课文二 · Text 2 · CD 59 —— 再听一次")
    + "\n" + callout("tip", "听懂了吗 · Comprehension",
                     "他们多长时间去一次饭店？　「差不多」是什么意思？", None, "Answer in Chinese."))

# ── Flexible Practice ─────────────────────────────────────────────
add("17-act1.html", "Y8 L12 · Activity 1 · 你去过……几次？ (We Do)", "20–25 MIN · WE DO",
    "Activity 1 · 课本 p.116 Ex.9",
    task_slide("Activity 1 · 你去过……几次？ · 课本 p.116 Ex.9", "PAIRS · 5 MIN",
               ["cn:北京　·　纽约　·　巴黎　·　伦敦　·　东京",
                "Most answers will be 一次也没有去过 —— that <b>is</b> the point. The negative gets twenty repetitions.",
                "Then the same shape over 练习册 p.130 Ex.4:",
                "cn:你去过北京吗？／画过国画儿吗？／吃过青菜吗？／学过法语吗？／看过中医吗？／用过人民币吗？"],
               "For every <b>yes</b>, add when and how it went, using 了 and 得. For every <b>no</b>, say what "
               "you'd like instead. Then write two 过 questions of your own and ask another pair.",
               "我去过北京两次，去年去的，玩得特别好。"))

add("18-act2.html", "Y8 L12 · Activity 2 · 问一问 Find Someone Who (You Do)",
    "25–35 MIN · YOU DO", "Activity 2 · 问一问",
    task_slide("Activity 2 · 问一问 · Find Someone Who", "MOVING · 10 MIN",
               ["A <b>different name</b> for each question. Ask in Chinese, write the answer in Chinese.",
                "cn:① 你一星期吃几次快餐？　② 你一个月看几次电影？",
                "cn:③ 你一星期做几次体育运动？　④ 你一个月吃几次中餐？",
                "cn:⑤ 你一星期看几次电视？　⑥ 你每个月大概花多少钱买衣服？",
                "Eight minutes moving, two minutes reporting. Three students report one classmate each."],
               "Report on <b>four</b> classmates as a connected paragraph — compare them with 比, group them "
               "with 都. Deliver it standing, with nothing written in front of you.",
               "美文和大生都一星期吃三次快餐，可是冬冬比他们吃得少，他一个月只吃一次。"))

add("19-act3.html", "Y8 L12 · Activity 3 · 大概花多少钱", "35–39 MIN · YOU DO",
    "Activity 3 · 课本 p.117 Ex.11",
    task_slide("Activity 3 · 大概花多少钱 · 课本 p.117 Ex.11 · 练习册 p.134 Ex.13", "PAIRS · 4 MIN",
               ["cn:你每个月大概花多少钱买杂志／午饭／CD／电脑游戏／衣服？",
                "cn:你每个月大概花多少钱打电话？",
                "Every answer must contain <b>大概</b> and a real amount in Chinese money words.",
                "Three read out at the end."],
               "Add up your own five answers and report the total with <b>一共</b> —— then say whether it is "
               "太贵 or 不算太贵, and why.",
               None))

add("20-act4.html", "Y8 L12 · Activity 4 · 四个时态 the four tenses", "39–43 MIN · YOU DO",
    "Activity 4 · 课本 p.118 Ex.13",
    '  <p class="section-label">Activity 4 · 四个时态 · 课本 p.118 Ex.13</p>\n'
    + examples_block([
        ("我上个周末去打网球<b>了</b>。", "past", False),
        ("我<b>每个</b>周末<b>都</b>去看电影。", "present", False),
        ("我<b>正在</b>看电视<b>呢</b>。", "present continuous", False),
        ("我下个周末<b>会</b>／<b>要</b>去北京。", "future", True)],
        label="模仿这四句 · One sentence per tense")
    + "\n" + callout("note", "词库 · From the banks on p.118",
                     "昨天 今天 明天　·　去年 今年 明年　·　上个月 这个月 下个月　·　上个星期 这个星期 下个星期",
                     None,
                     "去朋友家 · 在家看书 · 看电视 · 看电影 · 游泳 · 跑步 · 打篮球 · 画画儿 · 去饭店吃饭 · 去上海 · 去美国 · 吃中餐"))

add("21-act4b.html", "Y8 L12 · Activity 4 · 常见的两个错 the two usual errors",
    "39–43 MIN · YOU DO", "Activity 4 · 课本 p.118 Ex.13",
    task_slide("Activity 4 · 写四句 · Whiteboards up together", "WHITEBOARDS · 4 MIN",
               ["Four sentences, one per tense, each with a <b>different</b> activity.",
                "Hold them all up at once so the two usual errors show:",
                "cn:✗ 我下个周末去北京<b>了</b>。　　✗ 我<b>正在</b>看电视。"],
               "Write all four about the <b>same</b> activity, so the set reads as a story — and every "
               "sentence must carry a 次 or a 大概.",
               "我上个月去过一次上海饭店，我每个星期都想去，我正在看他们的菜单呢，我下个星期会再去一次。"))

add("22-plenary.html", "Y8 L12 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n'
    '  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Thumbs on each criterion —— {RATE}", None,
            "Watch criterion 1 —— 大概 is the one that fades fastest.") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "你一个月去几次饭店？每次大概花多少钱？", "—— 两个问题，写成一句。",
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "The last lesson of the unit —— the whole restaurant conversation, including the bill.",
            "五百块左右，不算太贵。") +
    "\n  </div>")

write_deck("l5-ci-guo-dagai", S, "Y8 L12 · 几次？大概多少钱？ · Lesson 5 of 6")
