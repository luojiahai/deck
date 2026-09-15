# -*- coding: utf-8 -*-
"""Y8 L15 · Lesson 5 of 6 — 要坐多长时间？ and 大约

Source: docs/lesson-plans/y8-l15/05-how-long-does-it-take-mixed.md
Textbook p.148 Text 2 (complete), p.152 Act. 13 (多长时间 ×8), p.153
Act. 15 (CD 75). Workbook pp.168–169.

机 is not new — it is the 机 of 洗衣机 and 冷气机 from Lesson 14, and the
cycle 2 word slide says so. Half of this lesson's "new" vocabulary is
recombination, which is worth telling students at this point in the book.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_dialogue, s_errors, s_listening, s_title, s_lisc)

SLUG = "l5-how-long"
TITLE = "Y8 L15 · 社区 Neighbourhood · Lesson 5 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='要坐多长时间？', en='How long does it take?',
            desc='The obvious next question after Lesson 4, and the answer that admits it is an estimate. Text 2 closes here, and with it the model dialogue the whole unit test is built on.',
            words='时间 · 大约 · 飞机 · 机场', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 多长时间 How long does it take?", "LESSON 5 OF 6",
        "第十五课 · 社区",
        s_title("要坐多长时间？", "How Long Does It Take?",
                "Year 8 · Book 2 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 2 · p.148, p.152–153"))

    add("02-review.html", "Review · Lesson 4 — two-leg journeys", REV, "复习 · 上一课",
        s_list("复习 · 两人一组，背着说 · 2 分钟",
               [("A 问：<b>从你家怎么去电影院？</b>", "B 答两段路"),
                ("A 问：<b>从学校怎么去火车站？</b>", "B 再答两段路"),
                ("换角色，再来一遍。", "然后请三个同学上来表演，桌上什么都不许放"),
                ("小白板：<i>First I take the boat, then the number 5 bus.</i>",
                 "我先坐船，然后坐五路公共汽车。")],
               "怎么去，你们已经会说了。今天是所有人接下来一定会被问的那一句。",
               compact=True))
    add("03-review-bridge.html", "Review · breaking the question apart", REV,
        "复习 · 拆开看",
        s_focus("多 + 长 + 时间",
                "多长时间",
                "how + long + time",
                "「多」和「长」你早就会了。今天真正新的只有中间那个「时间」。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("ask and answer how long a journey takes.",
               [("I can ask 要坐多长时间？ and answer with a length of time",
                 "会问「要坐多长时间？」，也会回答"),
                ("I can give an approximate answer using 大约", "会用「大约」说大概多久"),
                ("I can say 飞机 and 机场", "能说「飞机」和「机场」")]))

    # ── Cycle 1 · 时间 / 大约 ──
    add("05-c1-words.html", "Cycle 1 · A — 时间 / 大约", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("时间（時間）", "shíjiān", "time", "shijian"),
                ("大约（大約）", "dàyuē", "about; approximately", "dayue")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("你要坐多长<b>时间</b>？", "How long do you have to travel?"),
                    ("<b>大约</b>二十分钟。", "About twenty minutes."),
                    ("从我家到学校要多长<b>时间</b>？　—— <b>大约</b>半个小时。",
                     "How long from my home to school? — About half an hour.", True)],
                   "「时间」说的是一段，不是一个点——钟面上那个箭头扫过的一块。"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["从我家到 ________ 要大约 ________ 。"],
                "两条路一起说，还要比较，还要说结果："
                "<b>从我家到超市大约五分钟，可是到火车站要大约半个小时，"
                "所以我常常走路去超市，坐公共汽车去火车站。</b>"))

    # ── Cycle 2 · 飞机 / 机场 ──
    add("08-c2-words.html", "Cycle 2 · A — 飞机 / 机场", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("飞机（飛機）", "fēijī", "plane", "feiji"),
                ("(飞)机场（機場）", "(fēi)jīchǎng", "airport", "jichang")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我坐<b>飞机</b>去中国。", "I go to China by plane."),
                    ("我家离<b>机场</b>很远。", "My home is far from the airport."),
                    ("我家离<b>机场</b>挺远的，要先坐火车，然后坐<b>飞机</b>。",
                     "The airport is quite far — first the train, then the plane.", True)],
                   "「机」这个字你上一课就见过了——在哪两个词里？（洗衣机、冷气机）"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我家离机场 ________ ，要坐 ________ 去。"],
                "写一条<b>三段</b>的路去机场，每一段都说时间，最后说你为什么要早出门："
                "<b>我家离机场挺远的。我先坐十路公共汽车，大约十五分钟，"
                "然后坐火车，大约一个小时，所以我要很早出门。</b>"))

    add("11-recall.html", "Recall · four words, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["时间", "大约", "飞机", "机场"],
                 "读不出来就停下来重教——不要往下走。", cols=4))

    # ── The pattern ──
    add("12-pattern.html", "Pattern · 要坐多长时间？→ 大约……", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 问多久，答大概",
                  "要坐多长时间？　→　大约 + 时间。",
                  [("你家离火车站远吗？　—— 不远，就在马路对面。",
                    "Yesterday's 就 and Lesson 2's 离 — both still running."),
                   ("要坐<b>多长时间</b>？　—— <b>大约</b>二十分钟。",
                    "The new pair. 大约 goes in front of the amount."),
                   ("你家离(飞)机场远吗？　—— <b>挺远的</b>，要坐火车去。",
                    "This is Text 2, p.148 — and 挺……的 came from Lesson 2.")],
                  "三句里只有中间那一句是今天新的。另外两句是第二课和第三课"
                  "还在用的东西。"))
    add("13-errors.html", "The error to pre-empt · where 多长时间 goes", IDO,
        "句型 · 最常见的错",
        s_errors([("你要多长时间坐？", "你要坐<b>多长时间</b>？",
                   "「多长时间」在动词后面——它是问「坐多久」，不是问「多久坐」"),
                  ("大约二十分钟的时间要坐。", "要坐<b>大约</b>二十分钟。",
                   "「大约」贴在数量前面")],
                 "改一改 · 「多长时间」和「大约」"))
    add("14-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("一口气回答两个问题：怎么去，还有多久",
                "从你家怎么去机场？要坐多长时间？　—— 我先坐火车，然后坐公共汽车，大约一个小时。",
                "How do you get to the airport from your home, and how long does it "
                "take? — First the train, then the bus; about an hour.",
                "两个问题，一个回合答完：路线在前，时间在后。"
                "这就是课文二最后那几行在做的事。"))

    # Ten turns will not fit on one slide at a readable size, and s_dialogue
    # tightens rather than clips — past six it would still run 92px off the
    # bottom. Split the dialogue, never the type: the first slide is the
    # half students have already met plus the new question, the second is
    # the 离 exchange that closes it.
    add("15-text-a.html", "Text 2 · p.148 (first six lines)", IDO, "课文二 · CD 74 · 上",
        s_dialogue("课文二 · 上半 · 课本 p.148",
                   [("A", "你们家附近有电影院吗？"),
                    ("B", "没有。"),
                    ("A", "从你们家怎么去电影院？"),
                    ("B", "我先坐船，然后再坐五路公共汽车。"),
                    ("A", "要坐多长时间？"),
                    ("B", "大约二十分钟。")],
                   "前四行上节课读过了。今天新的是最后两行——也就是今天这一课。"))
    add("16-text-b.html", "Text 2 · p.148 (last four lines)", IDO, "课文二 · CD 74 · 下",
        s_dialogue("课文二 · 下半 · 课本 p.148",
                   [("A", "你家离火车站远吗？"),
                    ("B", "不远，就在马路对面。"),
                    ("A", "你家离(飞)机场远吗？"),
                    ("B", "挺远的，要坐火车去。")],
                   "这四行里没有一个今天的新词——「离」「就」「对面」「挺……的」"
                   "全是第二课和第三课的。整段是单元测验口语部分的样板："
                   "放 CD 74，齐读，两人一组读两遍换角色。"))
    add("17-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「多长时间」是问 <i>when</i> 还是 <i>how long</i>？", "是 how long 的举手"),
               ("翻译：<i>About forty minutes.</i>", "小白板：大约四十分钟。"),
               ("<b>用中文问我</b>：我到学校要多久？", "点两个人，第二个人要问得跟第一个不一样"),
               ("改一改：我要多长时间坐去机场？", "哪个部分放错了？")]))

    # ── Practice ──
    add("18-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("时间", "shijian"), ("大约", "dayue"),
                   ("飞机", "feiji"), ("机场", "jichang")],
                  "这一页留在屏幕上——后面两个活动都看它。"))

    add("19-act1.html", "Activity 1 · My journey-time chart (We Do, 7 min)", PRAC,
        "活动一 · 7 分钟",
        s_figure("tubiao", "活动一 · 我的时间表",
                 ["<b>发纸</b>　四栏：去哪儿 / 怎么去 / 多长时间 / 远不远。",
                  "<b>填六个真的地方</b>　学校、超市、火车站、电影院、机场，"
                  "再加一个你自己的。全部写汉字。",
                  "<b>时间那一栏每一格都要用「大约」开头。</b>三分钟。",
                  "填完两人一组互相采访，然后两个同学报告同桌<b>最长</b>的那一条路。"],
                 cn="从你家怎么去机场？　要坐多长时间？"))
    add("20-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难 · 表填完就扣过来",
               ["表填好，<b>盖起来</b>，然后<b>说一分钟</b>，面前什么都不看。",
                "六个地方要<b>从近到远</b>排着说，而且句子要连起来，不是一条一条念。"],
               cn="超市离我家最近，走路五分钟就到了。机场最远，要先坐火车，然后……"))

    add("21-listening.html", "Activity 2a · Listening — p.153 Act. 15 (CD 75)", PRAC,
        "听力 · CD 75 · 4 分钟",
        s_listening("听力 · 课本 p.153 第十五题 · 放两遍",
                    [("第一段：他家离学校远吗？", "他怎么上学？坐多久？"),
                     ("第二段：他家附近有超市吗？", "他怎么去超市？要开多久？")],
                    "两段听完再放<b>第三遍</b>——这一遍不做题，只听"
                    "「挺远的」和「大约十五分钟」在整句话里是什么声音。"))
    add("22-act2.html", "Activity 2b · p.152 Act. 13 — writing (You Do, 5 min)", PRAC,
        "活动二 · 5 分钟",
        s_list("活动二 · 课本 p.152 第十三题 · 写在本子上",
               [("八个问句，用「多长时间」补完。", "写在本子上"),
                ("老师走一圈，专找一种错：<b>「多长时间」跑到动词前面去了</b>。",
                 "找到就当场改"),
                ("写完的人不要停——看下一页。", "")],
               "这八句的格式跟单元测验第六部分一样。现在写顺了，考试就不是新东西。"))
    add("23-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难 · 自己写一段课文二",
               ["不做填空。写一段<b>八行</b>的对话，说你自己家附近。",
                "「附近有……」「离……远吗」「从……怎么去」「要坐多长时间」「大约」"
                "——五个都要出现。",
                "写完找一个<b>没看过你稿子</b>的同伴，当场演一遍——"
                "他要答<b>他自己家</b>的情况，不是照你写的念。"]))

    add("24-game.html", "Game · 20 Questions — mystery destination (7 min)", PRAC,
        "游戏 · 二十个问题 · 7 分钟",
        s_task("游戏 · 猜一个地方",
               ["一个同学心里想一个地方：超市、花店、文具店、家具店、饭店、"
                "火车站、电影院、机场、学校。",
                "全班<b>只能用中文</b>问：离学校远吗？要坐多长时间？在马路对面吗？"
                "那儿有沙发吗？",
                "他只能答：是／不是／挺远的／大约二十分钟。",
                "二十个问题之内猜出来算全班赢。"],
               ext="想地方的人<b>不许只答一个词</b>——每一句都要是完整的句子，"
                   "而且整轮里至少有三句要用「先……，然后……」。"
                   "问的人：同一个问法不能用第二次。"))

    add("25-strokes.html", "Writing · copy the new characters", PRAC, "写字 · 课文二生词",
        s_strokes([("时", 7, "日字旁，右边是「寸」"),
                   ("间", 7, "门字框，里面是「日」"),
                   ("约", 6, "绞丝旁，右边是「勺」"),
                   ("飞", 3, "只有三画——横斜钩，两点"),
                   ("场", 6, "提土旁，右边先写横折折折，再写撇")],
                  "写字 · 课本笔顺 · 练习册 pp.168–169",
                  "每个字写三遍。「飞」只有三画，很多人写成四画。"))

    # ── Plenary ──
    add("26-plenary.html", "Plenary · 回头看目标", PLEN, "小结 · 43–50 分钟",
        s_list("小结 · 回头看今天的三个目标",
               [("会问「要坐多长时间？」，也会回答", "全班一起回答：你家离学校要坐多长时间？"),
                ("会用「大约」", "👍 / 😐 / 👎"),
                ("能说「飞机」和「机场」", "👍 / 😐 / 👎")],
               "第一条不用举手——全班齐声答一次，答得出来就是会了。"))
    add("27-exit.html", "Exit ticket", PLEN, "出门条 · Exit ticket",
        s_focus("出门条 · 回答一句，交上来",
                "从你家到学校要坐多长时间？",
                "One sentence. It must have 大约 in it.",
                "下节课是这个单元的最后一课：再学四个店，看一张地图，"
                "然后你要给一个陌生人指路。",
                ext="写完了？再加一句说你<b>怎么</b>去，用「先……，然后……」。"))
    return S
