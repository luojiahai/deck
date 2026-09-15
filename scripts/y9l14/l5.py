# -*- coding: utf-8 -*-
"""Y9 L14 · Lesson 5 of 6 — 偷 / 警察 / 被 / 留 / 姓名 + the 被 passive

Source: docs/lesson-plans/y9-l14/05-text2-bei-stolen-mixed.md
Textbook p.137 Text 2 (CD 55), p.139 Act. 9, p.140 Act. 11 (CD 56).
Workbook p.160 Ex. 16, p.161 Ex. 17, p.162 Ex. 21.

Five words is 2 + 2 + 1, so cycle 3 uses s_word_one rather than padding the
slide with an already-taught word. 被 and 留 are function words and get
textonly cards; 偷 is drawn as a diagram (a wallet leaving a bag) rather
than a hand.

This is the heaviest 50 minutes of the sequence — three cycles, 被, and
Text 2. Text 2 therefore runs as Activity 1 of Flexible Practice, not
inside the I Do block, and the slide sections say so.
"""
from build import (s_words, s_word_one, s_examples, s_write, s_recall,
                   s_summary, s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_errors, s_dialogue, s_listening, s_title, s_lisc, label)

SLUG = "l5-stolen"
TITLE = "Y9 L14 · 问路 Asking the Way · Lesson 5 of 6"
CARD = (SLUG, "被偷了", "Text 2 · Reporting a Theft · 被",
        "grammar", "偷 · 警察 · 被 · 留 · 姓名。中文平常先说谁做的——"
                   "「被」是给<b>不知道</b>或者<b>不在乎</b>谁做的时候用的。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 被偷了", "LESSON 5 OF 6", "第十四课 · 问路",
        s_title("被偷了", "Reporting a Theft",
                "Year 9 · Book 3 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 3 · p.137 · 课文二 · CD 55"))

    add("02-review.html", "Review · 宾果 + 写一句", REV, "复习 · Lesson 4",
        s_task("复习 · 宾果三分钟，写三分钟",
               ["<b>宾果</b> · 画一个九宫格，从十二个词里选九个填进去：",
                "　　手提包 钱包 钥匙 手机 现金 服装 自行车 车站 广场 购物 庙 桥",
                "老师说<b>英文</b>，你划掉。一条线就喊「中了」。",
                "<b>白板</b> · 写一句 —— 你的手提包里有什么？至少三样，"
                "用「除了……以外，还有……」。"],
               cn="取三位同学念出来，然后进今天的课。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("use 被 to say that something happened to you, "
               "rather than that you did it.",
               [("I can build a 被 sentence in the right order",
                 "能把「被」字句的顺序排对：我的钱包被偷了"),
                ("I can say who did it when I know",
                 "知道是谁的时候能说出来：我的自行车被哥哥骑走了"),
                ("I can report a theft and answer the officer's questions",
                 "能向警察报案，回答他的问题")]))

    add("04-why-bei.html", "为什么要「被」", IDO, "先说清楚 · Why 被 exists",
        s_focus("为什么中文要有「被」",
                "中文平常先说「谁做的」。可是有的时候，"
                "你<b>不知道</b>是谁做的，或者你<b>不在乎</b>——"
                "你只在乎东西没有了。这时候用「被」。",
                "Chinese normally leads with who did it. 被 is for when you "
                "don't know, or don't care — you only care what happened "
                "to the thing.",
                "先讲这一句，再讲语法。不然「被」就只是一个要背的字。"))

    # ── Cycle 1 · 偷 / 警察 ──
    add("05-c1-words.html", "Cycle 1 · A — 偷 / 警察", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("偷", "tōu", "steal", "tou"),
                ("警察", "jǐngchá", "policeman", "jingcha")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "有人在商店里<b>偷</b>东西。",
                     "Someone's stealing in the shop."),
                    (None, "<b>警察</b>就在广场的车站旁边。",
                     "The police officer is right by the stop on the square."),
                    (None, "<b>警察</b>问我：谁<b>偷</b>了你的钱包？",
                     "The officer asked me: who stole your wallet?", True)],
                   "「偷」的左边是什么旁？为什么？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["警察在 ________ 。", "我的 ________ 被人偷了。"],
                "写警察<b>接下来</b>会问的两个问题——不是屏幕上那个。"
                "他真正需要知道什么？"))

    # ── Cycle 2 · 被 / 留 ──
    add("08-c2-words.html", "Cycle 2 · A — 被 / 留", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("被", "bèi", "passive marker", None),
                ("留", "liú", "leave (behind)", None)))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我的钱包<b>被</b>偷了。", "My wallet was stolen."),
                    (None, "请<b>留</b>下你的电话号码。",
                     "Please leave your phone number."),
                    (None, "我的手机<b>被</b>偷了，警察请我<b>留</b>下电话号码。",
                     "My phone was stolen, and the officer asked me to leave "
                     "my phone number.", True)],
                   "「留下」是留在这儿，不是走。"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我的 ________ 被 ________ 了。", "请留下你的 ________ 。"],
                "写三句「被」字句，<b>没有一句跟偷东西有关</b>——"
                "我的自行车被哥哥骑走了／蛋糕被弟弟吃完了／我的书被同学借走了。"
                "「被」不是坏事专用的字。"))

    # ── Cycle 3 · 姓名 (single) ──
    add("11-c3-word.html", "Cycle 3 · A — 姓名", IDO, "生词 3 · Cycle 3 of 3",
        s_word_one(("姓名", "xìngmíng", "full name", "xingming")))
    add("12-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "请写下你的<b>姓名</b>。", "Please write your full name."),
                    (None, "请留下你的<b>姓名</b>和电话号码。",
                     "Please leave your name and phone number."),
                    (None, "老师叫我们在本子上写<b>姓名</b>。",
                     "Teacher tells us to write our names on our books.", True)],
                   "「姓名」＝ 姓 + 名。「姓」一年级就学过了——你姓什么？"))
    add("13-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["请留下你的 ________ 和 ________ 。"],
                "「姓名」跟「名字」有什么不一样？用中文写一句说明，"
                "再说哪一个写在表格上。"))

    add("14-recall.html", "Recall · 五个生词", IDO, "认一认 · Checkpoint",
        s_recall(["偷", "警察", "被", "留", "姓名"],
                 "读不出来就回去重教——「被」尤其要读得准。", cols=5))

    # ── Pattern ──
    add("15-pattern.html", "Pattern · 被 (课本 p.139 NOTE)", IDO,
        "句型 · Sentence pattern",
        s_pattern("句型 · 被字句",
                  "东西 + 被 + [谁] + 动词 + 了／走了／完了",
                  [("我的钱包<b>被</b>偷了。", "My wallet was stolen. (don't know who)"),
                   ("我的自行车<b>被</b>哥哥骑走了。",
                    "My bike was taken by my brother. (we know who)"),
                   ("蛋糕<b>被</b>弟弟吃完了。",
                    "The cake was eaten up by my little brother.")],
                  "三条规矩：① <b>东西在前</b>，不是人。 ② <b>谁做的可以不写</b>。 "
                  "③ <b>动词不能光秃秃</b>——要有「了」，或者带个结果：骑<b>走</b>了、吃<b>完</b>了。"))
    add("16-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 被 + 地点，再接一个分句",
                "我的手提包在服装店被偷了，里边的现金、钥匙和手机都不见了。",
                "My handbag was stolen at the clothes shop, and the cash, "
                "keys and phone inside are all gone.",
                "地点放在「被」<b>前面</b>。第二个分句用的全是上节课的词。"))
    add("17-errors.html", "被字句 · 三种错法", IDO, "注意 · The three that break",
        s_errors([("我的钱包偷了被。", "我的钱包被偷了。", "「被」在动词<b>前</b>"),
                  ("被弟弟蛋糕吃完了。", "蛋糕被弟弟吃完了。", "东西要放最前面"),
                  ("我的自行车被哥哥骑。", "我的自行车被哥哥骑走了。",
                   "动词后面要有「了」或者结果")],
                 "被字句 · 常见的三种错",
                 "第三种最常见——写的时候句子看起来「说完了」，其实还差一个字。"
))

    add("18-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("白板：写 —— My bicycle was taken by my brother.", None),
               ("举手投票：「被」后面一定要写是谁做的吗？", "然后说为什么"),
               ("这句哪里错了？ 我的自行车被哥哥骑。", "找出来，改过来"),
               ("转过去问同伴：你被偷过吗？什么东西被偷了？", "三十秒")]))

    # ── Flexible practice ──
    add("19-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("偷", "tou"), ("警察", "jingcha"), ("被", None),
                   ("留", None), ("姓名", "xingming")],
                  "这块板整个活动都留在屏幕上——写报案的时候可以看。"))
    # Eight turns overflow one slide even at s_dialogue's tight tier, and the
    # dialogue splits cleanly anyway: where and what, then what was inside.
    add("20-text-a.html", "Activity 1 · 课文二 · 上半 (CD 55)", PRAC,
        "活动一 · We Do · 课文二 · p.137 · 1/2",
        s_dialogue("课文二 · 小青报案 · 先听两遍，再看字",
                   [("A", "小青：我在购物广场买东西的时候手提包被偷了。"),
                    ("B", "警察：在哪家商店被偷的？"),
                    ("A", "小青：在四彩服装店。"),
                    ("B", "警察：包里有什么？")],
                   "第一件事：<b>在哪儿</b>被偷的。地点放在「被」前面。"))
    add("21-text-b.html", "Activity 1 · 课文二 · 下半 (CD 55)", PRAC,
        "活动一 · We Do · 课文二 · p.137 · 2/2",
        s_dialogue("课文二 · 接着上一页",
                   [("A", "小青：有钱包、钥匙和手机。"),
                    ("B", "警察：钱包里有什么？"),
                    ("A", "小青：有两百多块现金、身份证、学生证和借书证。"),
                    ("B", "警察：请留下你的姓名和电话号码。")],
                   "齐读，再两人分角色读，读完换过来。"
                   "「身份证、学生证、借书证」下节课才学——先听个响。"))
    add("22-write-report.html", "Activity 1 · 写你自己的报案", PRAC,
        "活动一 · You Do · 4 分钟",
        s_task("在纸条上写你<b>自己</b>的报案 · 四句话 · 五个生词都要用上",
               ["换一个地方，换一包东西——别抄小青的。",
                "这张纸条<b>等一下要交给警察</b>（活动三的同伴），"
                "所以要让别人看得懂。",
                "三个问题必须答得出来：在哪儿被偷的？包里有什么？钱包里有什么？"],
               "换个角度写——用<b>警察</b>的口气记录，第三人称："
               "<b>小青说她的手提包在四彩服装店被偷了，包里有……</b>"
               "最后加一句：警察<b>忘了问</b>的那个问题是什么？"))
    add("23-bei-paper.html", "Activity 2 · 被字句 · 笔头", PRAC,
        "活动二 · You Do · 7 分钟 · 本子上",
        s_list("活动二 · 两件事，按顺序做 · 老师走动，专抓两种错",
               [("课本 p.139 第 9 题 · 七句填完，再自己写两句", "4 分钟"),
                ("练习册 p.161 第 17 题 · 再七句", "3 分钟"),
                ("老师抓的两种错：动词后面少了「了」／结果；东西和人的顺序反了", None)],
               "从第 9 题里挑四句，<b>去掉「被」</b>重写，把做的人放回前面："
               "<b>哥哥把我的自行车骑走了。</b>"
               "然后用英文写一句：什么时候你会选哪一种说法？"
               "（「把」是第十五课的，今天先碰一下没关系。）"))
    add("24-listening.html", "Activity 3 · CD 56 (p.140 第 11 题)", PRAC,
        "活动三 · 听力 · 3 分钟",
        s_listening("手机被偷了 · 听一听，勾 a、b 还是 c",
                    [("手机是什么时候被偷的？", "a 上课　b 上体育课　c 放学"),
                     ("手机本来放在哪儿？", "a 书包里　b 口袋里　c 桌子上"),
                     ("书包放在哪儿了？", "a 教室　b 体育馆门口　c 图书馆"),
                     ("去体育馆找过吗？", "a 没有　b 找过一次　c 找过好几次"),
                     ("学校办公室有吗？", "a 有　b 没有　c 还没问"),
                     ("最后决定怎么办？", "a 报警　b 回家再找　c 买新的")],
                    "这段就是下面角色扮演的范本——听警察是怎么一步一步问的。"))
    add("25-roleplay.html", "Game · 报案 · Role-play Cards", PRAC, "游戏 · 5 分钟",
        s_task("游戏 · 两人一组，卡片扣着 · A 是警察，B 报案",
               ["A 按卡片上的四个问题问：在哪儿被偷的？包里有什么？"
                "钱包里有什么？姓名和电话？",
                "B <b>用自己活动一写的那张纸条</b>回答。",
                "做完换卡片，用同伴的纸条再演一次。"],
               "给流利的同学：警察那张卡是<b>空白</b>的——问题自己编，"
               "至少问六个，其中一个要是书上没有的："
               "<b>什么时候被偷的？当时旁边有人吗？你去问过商店了吗？</b>"
               "报案的人<b>不看纸条</b>回答。"))

    add("26-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 请一位同学读三条 Success Criteria。",
                "<b>自评</b> · 举手。第一条最重要——"
                "顺序还不稳的话，下节课开头再花两分钟。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下节课</b> · 这个单元的最后一节——东西丢了以后怎么办？"
                "你去服务台说：我找不到我的书包。"],
               cn="出门条：写一句 —— 说一样东西被偷了，或者被别人拿走了。"
                  "<b>不能用「钱包」。</b>"))

    return S
