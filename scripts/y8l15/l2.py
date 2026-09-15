# -*- coding: utf-8 -*-
"""Y8 L15 · Lesson 2 of 6 — 离, and how far away things are

Source: docs/lesson-plans/y8-l15/02-distance-li-mixed.md
Textbook p.142 (Text 1 complete), p.144 Act. 2 (离 + 远/近), p.147 Act. 8
(CD 73). Workbook pp.165–166 (离 sentence building).

挺 is the one word in this series with nothing to draw, so it gets a
textonly card. 离 and 远 are abstract but spatial and get diagrams: 离 is
an architect's dimension line, 远 is the same two buildings pushed apart.
Drawn as a pair on purpose — students who meet them separately treat them
as synonyms.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_text, s_errors, s_listening, s_title, s_lisc)

SLUG = "l2-distance-li"
TITLE = "Y8 L15 · 社区 Neighbourhood · Lesson 2 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='超市离我家不远', en='Far or near',
            desc='One character does the whole job — 离 names the span between two places. It is not a verb, and the error it invites (a 离 sentence with nothing after it) is pre-empted on a slide of its own.',
            words='超市 · 离 · 远 · 挺', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 离 Far or near", "LESSON 2 OF 6", "第十五课 · 社区",
        s_title("超市离我家不远", "Far or Near",
                "Year 8 · Book 2 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 2 · p.142, p.144"))

    add("02-review.html", "Review · Lesson 1 — the four shops", REV, "复习 · 上一课",
        s_recall(["附近", "花店", "文具店", "家具店"],
                 "只有汉字，没有拼音。三十秒，全班一起读。", cols=4))
    add("03-review-errors.html", "Review · Correct the teacher", REV, "复习 · 改一改",
        s_errors([("我家有附近花店。", "我家附近有花店。", "「附近」跟着「我家」走，不能拆开"),
                  ("我买笔在文具店。", "我在文具店买笔。", "「在 + 地方」放在动词前面")],
                 "改一改 · 哪里错了？",
                 "两人一组找错，各派一组上来改。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say how far one place is from another.",
               [("I can say 超市 and 远 in Chinese", "能说「超市」和「远」"),
                ("I can say how far one place is from another with A 离 B 远／近",
                 "会用「A 离 B 远／近」说两个地方有多远"),
                ("I can soften a judgement with 挺……的", "会用「挺……的」说「挺远的」")]))

    # ── Cycle 1 · 超市 / 远 ──
    add("05-c1-words.html", "Cycle 1 · A — 超市 / 远", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("超市", "chāoshì", "supermarket", "chaoshi"),
                ("远（遠）", "yuǎn", "far", "yuan")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家附近有一个<b>超市</b>。", "There's a supermarket near my home."),
                    ("花店不<b>远</b>，走路五分钟。",
                     "The flower shop isn't far — five minutes on foot."),
                    ("<b>超市</b>不<b>远</b>，我常常走路去。",
                     "The supermarket isn't far; I often walk there.", True)],
                   "你家附近的超市远不远？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 不远，走路 ________ 分钟。"],
                "一句话说两个地方，一个近一个远，中间用「可是」："
                "<b>超市不远，走路五分钟，可是家具店很远，我要坐公共汽车去。</b>"))

    # ── Cycle 2 · 离 / 挺 ──
    add("08-c2-words.html", "Cycle 2 · A — 离 / 挺", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("离（離）", "lí", "distance away from", "li"),
                ("挺", "tǐng", "rather; quite")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("超市<b>离</b>我家不远。", "The supermarket isn't far from my home."),
                    ("我家<b>挺</b>大的。", "Our house is quite big."),
                    ("学校<b>离</b>我家<b>挺</b>近的。",
                     "School is quite close to my home.", True)],
                   "「近」这个字你已经会了——在哪个词里见过？（附近）"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["________ 离我家 ________ 。"],
                "「挺……的」用两次，一次说近一次说远，还要说为什么："
                "<b>超市离我家挺近的，所以我天天去。机场离我家挺远的，我一年去一次。</b>"))

    add("11-recall.html", "Recall · four words, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["超市", "远", "离", "挺"],
                 "读不出来就停下来重教——不要往下走。", cols=4))

    # ── The pattern ──
    add("12-pattern.html", "Pattern · A 离 B 远／近", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说两个地方有多远",
                  "地方一 + 离 + 地方二 + 远／近",
                  [("超市<b>离</b>我家很<b>近</b>。", "The supermarket is very close to my home."),
                   ("我家<b>离</b>学校不<b>远</b>。", "My home isn't far from school."),
                   ("花店<b>离</b>我家<b>挺近的</b>。",
                    "The flower shop is quite close to my home. — 挺 + adj + 的")],
                  "问句：<b>你家离学校远吗？</b> 答：<b>挺远的。／不远。</b>"))
    add("13-errors.html", "The error to pre-empt · 离 is not a verb", IDO, "句型 · 最常见的错",
        s_errors([("我家离学校。", "我家离学校很远。",
                   "「离」后面一定要有「远」或者「近」——它不是动词"),
                  ("我离家学校很远。", "我家离学校很远。",
                   "两个地方各自是完整的：我家 / 离 / 学校")],
                 "改一改 · 「离」最常见的两个错",
                 "这两句今天会在小白板上出现很多次。现在看清楚，等一下就少写一次。"))
    add("14-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("三个分句，两个结构，还要有转折",
                "我家离学校挺远的，可是超市离我家很近，走路五分钟。",
                "My home is quite far from school, but the supermarket is very close "
                "to my home — five minutes on foot.",
                "「离」用两次，一次配「挺……的」，一次配「很近」。"))

    add("15-text.html", "Text 1 · p.142 complete", IDO, "课文一 · CD 71",
        s_text("课文一 · 全文 · 课本 p.142",
               "我家附近有饭店、文具店、家具店、花店等。超市离我家也不远，"
               "走路五分钟<span class='text-muted'>就</span>到了。我家离学校也挺近的。"
               "我每天走路上学。",
               "超市离他家远吗？　他家离学校远不远？　他每天怎么上学？",
               "第二句里那个灰色的「就」今天先放着——读过去，别停。下节课整节课都是它。",
               size=23))

    add("16-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("用「离」说一句。二十秒，小白板，举起来。", "老师专门看：后面有没有「远／近」"),
               ("「挺远的」比「很远」远还是近？", "软一点——quite far，不是 very far"),
               ("翻译：<i>The stationery shop isn't far from school.</i>", "文具店离学校不远。"),
               ("这句对不对？　我家离超市。", "竖大拇指还是朝下？")]))

    # ── Practice ──
    add("17-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("超市", "chaoshi"), ("远", "yuan"),
                   ("离", "li"), ("挺", None)],
                  "「挺」没有图——它不是东西，是一个程度。这一页留在屏幕上。"))

    add("18-act1.html", "Activity 1 · Distance ladder (We Do, 7 min)", PRAC,
        "活动一 · 7 分钟",
        s_figure("tijie", "活动一 · 远近梯子",
                 ["<b>发纸</b>　一条竖线，最上面是「很近」，最下面是「很远」，中间六格。",
                  "<b>填六个真的地方</b>　超市、花店、文具店、家具店、火车站、我家，"
                  "按离学校大门的远近排。",
                  "<b>写三句</b>　在梯子下面写三句，四个生词全部用上。三分钟。",
                  "写完请两个同学念自己最上面和最下面的那一格。"],
                 cn="超市离学校很近。家具店离学校挺远的。我家离学校不远。"))
    add("19-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["六个地方<b>全部</b>排好，然后<b>当场</b>说出其中两个为什么排在那儿——不许先写。",
                "理由要用<b>「因为……所以……」</b>。",
                "最后再用「比」比较两个地方。"],
               cn="因为家具店在马路那边，所以它离学校挺远的。<br>超市离学校比家具店近。"))

    add("20-listening.html", "Activity 2a · Listening — p.147 Act. 8 (CD 73)", PRAC,
        "听力 · CD 73 · 4 分钟",
        s_listening("听力 · 课本 p.147 第八题 · 放两遍",
                    [("第一段：这是什么地方？", "里边卖什么？说三样"),
                     ("第二段：这是什么地方？", "他们家什么做得好吃？"),
                     ("第三段：这是什么地方？", "他去那儿做什么？妈妈呢？")],
                    "三段都是「我家附近有……」开头。先听地方，再听里边有什么。"))
    add("21-act2.html", "Activity 2b · p.144 Act. 2 — writing (You Do, 5 min)", PRAC,
        "活动二 · 5 分钟",
        s_list("活动二 · 课本 p.144 第二题 · 写在本子上",
               [("七个句子，用「离」加「远／近」补完。", "括号里给了提示"),
                ("写完再自己写三句，说真的地方。", "学校、超市、火车站、你家"),
                ("老师走一圈，专找一种句子：<b>「离」后面什么都没有的那种</b>。",
                 "找到就当场改")],
               "写完的人不要停——看下一页。"))
    add("22-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难 · 不写句子，写一段",
               ["不做填空。写<b>一段五句话</b>，说从家走到学校这一路。",
                "「离」要用<b>两次</b>，「挺……的」用<b>一次</b>，"
                "还要说出上一课三个店的名字。",
                "桌上什么都不许放：没有词库，没有句型条。",
                "写完站起来念，不许低头看。"]))

    add("23-game.html", "Game · Distance Bingo (7 min)", PRAC, "游戏 · 远近宾果",
        s_task("游戏 · 远近宾果 · 7 分钟",
               ["自己画一个三乘三的格子，填九个地方："
                "超市、花店、文具店、家具店、饭店、学校、火车站、我家、公园。",
                "老师念一句：<b>这个地方离学校很远，要坐火车去。</b>",
                "你觉得是哪个，就划掉哪个。连成一线就喊「宾果」。"],
               ext="赢的人接着当<b>发牌的</b>：自己<b>现编</b>中文提示，"
                   "每一句都要有「离」，还要有一句用「挺……的」。其他人格子不换，接着玩。"))

    add("24-strokes.html", "Writing · copy the new characters", PRAC, "写字 · 课文一生词",
        s_strokes([("超", 12, "走字旁，右边是「召」"),
                   ("市", 5, "第一笔是点，不是横"),
                   ("离", 10, "上面是「亠」，中间那一横别忘"),
                   ("远", 7, "先写「元」，最后写走之底——跟「近」一样"),
                   ("挺", 9, "提手旁，右边是「廷」")],
                  "写字 · 课本笔顺 · 练习册 pp.165–166",
                  "每个字写三遍。「远」和「近」的走之底都是最后写。"))

    # ── Plenary ──
    add("25-plenary.html", "Plenary · 回头看目标", PLEN, "小结 · 43–50 分钟",
        s_list("小结 · 回头看今天的三个目标",
               [("能说「超市」和「远」", "👍 / 😐 / 👎"),
                ("会用「A 离 B 远／近」", "👍 / 😐 / 👎 —— 这一条最要紧"),
                ("会用「挺……的」", "👍 / 😐 / 👎")],
               "第二条如果四分之一的人举 😐，下节课开头再练一次「离」。"))
    add("26-exit.html", "Exit ticket", PLEN, "出门条 · Exit ticket",
        s_focus("出门条 · 翻译，写在纸条上交上来",
                "The supermarket isn't far from my home — five minutes on foot.",
                "一句话。写完检查一遍：「离」后面有没有东西？",
                "下节课：那个被我们跳过去的「就」——还有怎么说「就在马路对面」。",
                ext="写完了？再加一句，用「挺……的」。"))
    return S
