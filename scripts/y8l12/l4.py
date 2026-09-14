# -*- coding: utf-8 -*-
"""Lesson 4 of 6 — 做得特别好吃 · the 得 complement.

From docs/lesson-plans/y8-l12/04-de-complement-mixed.md.
One vocabulary cycle only: 好吃 and 特别 are the two words students use,
and 特 / 别 are the characters they are built from — those get the
character-copying slide (练习册 p.133 Ex.11), not a teaching cycle of
their own. The room that buys goes to 得, which the unit test asks for
in three separate parts.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, title, tag, section, body, cls=""):
    S.append((f, title, tag, section, body, cls))

add("01-title.html", "Y8 L12 · Title · 做得特别好吃", "Lesson 4 of 6", "Y8 · Lesson 12",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 12", "做得特别好吃", "How Well Something Is Done",
                "Lesson 4 of 6 · 50 minutes · 课本 p.115–117",
                ["haochi", "tebie", "chaomian", "bisabing", "fandian"]))

add("02-review.html", "Y8 L12 · Review · 可以 quick quiz", "0–8 MIN · 复习", "Review · Lesson 3",
    task_slide("复习 · 可以 · Five on whiteboards", "WHITEBOARDS · 4 MIN",
               ["① Translate: &ldquo;May I use RMB?&rdquo;",
                "cn:② 我 ______ 用英语说吗？",
                "cn:③ 我用可以人民币吗？　—— 哪里错了？",
                "④ Write the character for <b>hù</b>, household.",
                "cn:⑤ 一共多少钱？　—— 用中文回答"],
               None))

add("03-review2.html", "Y8 L12 · Review · 阅读 reading comprehension", "0–8 MIN · 复习",
    "Review · 练习册 p.131 Ex.8",
    '  <p class="section-label">复习 · 阅读 · 练习册 p.131 Ex.8</p>\n'
    '  <div class="task-box">\n'
    '    <p class="task-cn">上个星期天我跟妈妈去市场买菜了。市场上人很多。妈妈先买了两条鱼和一斤猪肉。'
    '那天的苹果特别便宜，十块钱九个。妈妈买了二十块钱的苹果。我们还买了八个橙子，花了二十块钱。'
    '最后，我们又买了一些青菜。市场离我家很近，我们走路回家了。</p>\n  </div>\n'
    + callout("warn", "对还是错 · True or false — on whiteboards",
              "① 昨天她跟妈妈一起去市场买菜了。　② 她妈妈买了十八个苹果。<br>"
              "③ 她妈妈没有买蔬菜。　④ 她们走路回家了。", None,
              "鱼、猪肉、橙子、便宜 are unknowns. Work around them — that is what the test's reading section asks for."))

add("04-li-sc.html", "Y8 L12 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to say how well something is done, using 得 after the verb.",
             [("I can say and write the new words", "好吃、特别"),
              ("I can use the 好吃 scale", "特别好吃 → 不好吃"),
              ("I can build a sentence with 得", "他钢琴弹得很好听")]))

# ── Cycle 1 · 好吃 / 特别 ──────────────────────────────────────────
add("05-c1-words.html", "Y8 L12 · Cycle 1 · A — 好吃 / 特别", T, "生词 · Cycle 1 of 1",
    words_slide(("好吃", "hǎochī", "delicious", "haochi"),
                ("特别", "tèbié", "special; unusually", "tebie")))
add("06-c1-examples.html", "Y8 L12 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 1",
    sentences_slide([
        ("Zhè ge bāozi hěn hǎochī.", "这个包子很<b>好吃</b>。", "This bun is delicious.", False),
        ("Zhè jiā fàndiàn de chǎocài bú tài hǎochī.", "这家饭店的炒菜不太<b>好吃</b>。",
         "This restaurant's fried dishes aren't very nice.", False),
        ("Tāmen de bāozi tèbié hǎochī.", "他们的包子<b>特别好吃</b>。",
         "Their buns are especially delicious.", True)]))
add("07-c1-write.html", "Y8 L12 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 1",
    write_slide(["______ 特别好吃。"],
                "60 seconds. Name a real dish.",
                "One sentence with <b>特别</b> and <b>可是</b> —— good and expensive at the same time.",
                "这家的比萨饼特别好吃，可是特别贵。"))

add("08-chars.html", "Y8 L12 · 写一写 · 特 / 别", T, "写字 · 练习册 p.133 Ex.11",
    '  <p class="section-label">写一写 · 特别 是两个字 · 练习册 p.133 Ex.11</p>\n'
    '  <div class="stack gap-sm">\n'
    '    <div class="stroke-row"><p class="stroke-char">特</p><div class="stroke-meta">'
    '<p class="stroke-py">tè</p><p class="stroke-en">special</p><p class="stroke-count">10 strokes · 牛字旁</p></div></div>\n'
    '    <div class="stroke-row"><p class="stroke-char">别</p><div class="stroke-meta">'
    '<p class="stroke-py">bié</p><p class="stroke-en">other</p><p class="stroke-count">7 strokes</p></div></div>\n'
    '  </div>\n  <div style="height:18px"></div>\n'
    + callout("warn", "笔顺 · Stroke order",
              "别 is written <b>口 first</b>, then 力 —— not the other way round.", None,
              "Copy each three times. Books closed for the last one."))

# ── The 好吃 ladder ───────────────────────────────────────────────
add("09-ladder.html", "Y8 L12 · 好吃的程度 · the ladder", T, "程度 · 课本 p.116",
    '  <p class="section-label">好吃的程度 · 课本 p.116 Words for Reference</p>\n'
    + examples_block([
        ("特别好吃", "the strongest", False),
        ("非常好吃", None, False),
        ("很好吃", None, False),
        ("好吃　·　不错", None, False),
        ("不太好吃", None, False),
        ("不好吃", "the weakest", True)],
        note="Same shape as the 喜欢 ladder you already know. Read it down, then <b>up</b>.",
        label="")
    )

# ── Pattern · 得 ──────────────────────────────────────────────────
add("10-pattern.html", "Y8 L12 · 句型 · 得", T, "句型 · The 得 complement",
    pattern_slide("主语 ＋ 动词 ＋ <b>得</b> ＋ 很/特别/不太 ＋ 形容词",
                  "得 comes AFTER the verb. ✗ 他得跑很快")
    + "\n" + callout("tip", "两种说法 · 课本 p.117 NOTE",
                     "Same meaning, two shapes. Both are in the book.",
                     "他<b>说</b>汉语<b>说得</b>很好。　　他汉语<b>说得</b>很好。", None))

add("11-examples.html", "Y8 L12 · 模仿我说 · four sentences", T, "句型 · The 得 complement",
    examples_block([
        ("他跑<b>得</b>很快。", None, False),
        ("他跑步跑<b>得</b>很快。", None, False),
        ("他们的饭菜做<b>得特别好吃</b>。", None, False),
        ("姐姐的小提琴拉<b>得</b>不太好听，可是她钢琴弹<b>得特别</b>好。",
         "Two clauses, two 得, and a contrast.", True)]))

add("12-cfu.html", "Y8 L12 · CFU · check for understanding", T, "CFU · 检查理解",
    cfu_slide([("Does 得 go before or after the verb?", None),
               ("Translate: &ldquo;My dad plays basketball very well.&rdquo;", None),
               ("What is wrong with this?", "他跑得快很。"),
               ("Give me the <b>strongest</b> way to say something is delicious.", None),
               ("Answer in a full sentence.", "这家饭店的饭菜做得怎么样？")]))

add("13-text2.html", "Y8 L12 · 课文二 · Text 2 opening (CD 59)", T, "课文二 · 课本 p.115",
    dialogue_block([
        ("A", "Nǐmen jiā cháng qù fàndiàn chīfàn ma?", "你们家常去饭店吃饭吗？"),
        ("B", "Chàbuduō měi liǎng xīngqī qù yí cì.", "差不多每两星期去一次。"),
        ("A", "Nǐmen jīngcháng qù nǎ jiā fàndiàn chīfàn?", "你们经常去哪家饭店吃饭？"),
        ("B", "Wǒmen jīngcháng qù yì jiā Shànghǎi fàndiàn chīfàn. Tāmen de fàncài zuò de tèbié hǎochī.",
         "我们经常去一家上海饭店吃饭。他们的饭菜做<b>得特别好吃</b>。")],
        label="课文二 · Text 2 · CD 59 —— 前两句")
    + "\n" + callout("note", "先别教 · Leave these for next lesson",
                     "次 and 差不多每两星期 are Lesson 5's business. <b>Read</b> them today — don't teach them.",
                     "听懂了吗：他们去哪家饭店？那家饭店的饭菜怎么样？", None))

# ── Flexible Practice ─────────────────────────────────────────────
add("14-act1.html", "Y8 L12 · Activity 1 · 这炒面怎么样？ (We Do)", "20–27 MIN · WE DO",
    "Activity 1 · 课本 p.116 Ex.8",
    summary_slide([("炒面", "chaomian"), ("比萨饼", "bisabing"), ("香蕉", "xiangjiao"),
                   ("炒菜", "chaocai"), ("汉堡包", "hanbaobao"), ("西瓜", "xigua"),
                   ("苹果", "pingguo"), ("青菜", "qingcai")], 4,
                  "Activity 1 · 这……怎么样？ · 课本 p.116 Ex.8 —— eight dishes, all of them"))

add("15-act1b.html", "Y8 L12 · Activity 1 · 规则 the rule", "20–27 MIN · WE DO",
    "Activity 1 · 课本 p.116 Ex.8",
    task_slide("Activity 1 · 这炒面怎么样？", "PAIRS · 7 MIN",
               ["cn:A：这炒面怎么样？　B：非常好吃。",
                "Work through all eight dishes.",
                "<b>The rule:</b> no rung of the ladder twice by the same student. That forces all seven degrees into play.",
                "Three pairs read theirs out at the end."],
               "B justifies <b>every</b> answer with a second sentence using 因为 and something from an "
               "earlier lesson. Then A asks a follow-up —— and B answers without looking at the board.",
               "不太好吃，因为我不喜欢吃青菜，我一般吃水果。"))

add("16-act2.html", "Y8 L12 · Activity 2 · 用「得」造句 (You Do)", "27–35 MIN · YOU DO",
    "Activity 2 · 课本 p.117 Ex.10",
    task_slide("Activity 2 · 用「得」造句 · 课本 p.117 Ex.10", "BOOKS · 8 MIN",
               ["Six pictures. One sentence each, with 得 and a <b>different</b> degree word every time.",
                "cn:游泳　·　打网球　·　弹钢琴　·　穿衣服　·　画画儿　·　跳舞",
                "Pinyin stays up for two minutes, then comes <b>down</b>.",
                "Then 练习册 p.137 Ex.21 as a fast check —— match the six sentence halves."],
               "Write all six in <b>both</b> shapes, then a four-sentence paragraph about one real person in "
               "your family: what they do well, what they don't, what they cook. Every sentence with 得, "
               "joined with 可是 and 除了……以外. No word bank.",
               None))

add("17-act3.html", "Y8 L12 · Activity 3 · 很好吃／很好喝／很好看", "35–39 MIN · YOU DO",
    "Activity 3 · 练习册 p.134 Ex.12",
    task_slide("Activity 3 · 好 ＋ 动词 · 练习册 p.134 Ex.12", "WHITEBOARDS · 3 MIN",
               ["cn:<u>　这条裙子　</u>很好看。　　______ 很好喝。　　______ 不好看。",
                "cn:______ 很好吃。　　______ 不好吃。　　______ 很好听。",
                "All held up at once."],
               "Add 好玩 and 好学 to the family, one sentence each —— then one sentence that uses <b>three</b> "
               "members of the family at once.",
               None)
    + "\n" + callout("tip", "一家人 · One family of words",
                     "好 ＋ 动词 ＝ &ldquo;good to do&rdquo;.", "好吃　·　好喝　·　好看　·　好听", None))

add("18-game.html", "Y8 L12 · Game · 找不同 Odd One Out", "39–43 MIN · 游戏", "Game · 找不同",
    task_slide("Game · 找不同 · Odd One Out", "PAIRS · 3 MIN",
               ["Which word doesn't belong —— and <b>why, in Chinese</b>? The reason is the point.",
                "cn:① 特别好吃 / 非常好吃 / 不好吃 / 很好吃",
                "cn:② 炒面 / 包子 / 米饭 / 可乐",
                "cn:③ 得 / 很 / 特别 / 非常",
                "cn:④ 好吃 / 好喝 / 好看 / 好人",
                "cn:⑤ 苹果 / 西瓜 / 土豆 / 香蕉"],
               "Give a reason that works for a <b>different</b> word in the set too —— so there are two "
               "defensible answers —— then argue for yours in Chinese.",
               None))

add("19-plenary.html", "Y8 L12 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n'
    '  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Traffic light on your whiteboard —— one per criterion. {RATE}", None) + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Write <b>one</b> sentence with 得 about someone in your family.", None,
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "How <b>often</b> you eat out, and roughly how much it costs.", "差不多每两星期去一次。") +
    "\n  </div>")

write_deck("l4-de-complement", S, "Y8 L12 · 做得特别好吃 · The 得 Complement · Lesson 4 of 6")
