# -*- coding: utf-8 -*-
"""Y8 L13 · Lesson 3 of 6 — rooms downstairs, and the whole of Text 1

Source: docs/lesson-plans/y8-l13/03-downstairs-rooms-speaking.md
Textbook p.122 (Text 1 complete; New Words 8, 10, 11), p.123 Act. 2,
p.126 Act. 6, p.130 Act. 10. Workbook pp.144–145 Ex. 1, p.145 Ex. 2,
p.146 Ex. 5, p.150 Ex. 12.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_text, s_dialogue, s_title, s_lisc)

SLUG = "l3-downstairs-text1"
TITLE = "Y8 L13 · 房子 House · Lesson 3 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

# Card shown on the series landing page (index/designs/y8-l13/index.html),
# written by build.py. Lives beside the lesson it describes.
CARD = dict(cn='楼下有什么', en='Rooms downstairs · Text 1',
            desc='The downstairs rooms complete Text 1, which is read in full for the first time. A speaking lesson: the p.123 cutaway house, a house-tour role-play, the class survey, and 20 Questions.',
            words='客厅 · 餐厅 · 厨房 · 洗手间', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 楼下有什么 Rooms downstairs", "LESSON 3 OF 6", "第十三课 · 房子",
        s_title("楼下有什么？", "Rooms Downstairs · Text 1 Complete",
                "Year 8 · Book 2 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 2 · p.122 · CD 61"))

    add("02-review.html", "Review · pair dialogue from memory", REV, "复习 · Lesson 2",
        s_dialogue("两人一组 · 看 30 秒，然后把它关掉 · 说完交换",
                   [("A", "你家有几间卧室？"), ("B", "我家有 ____ 间卧室。"),
                    ("A", "你家有几个浴室？"), ("B", "有 ____ 个。"),
                    ("A", "你家有书房吗？"), ("B", "有，在楼上。／ 没有。")],
                   "老师走一圈，听有没有人说成「个卧室」。第二轮不给句型，直接点名。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("name the rooms downstairs and describe a whole house out loud.",
               [("I can name the downstairs rooms", "能说出楼下的房间"),
                ("I can say what someone is doing in a room", "能说某人在哪个房间做什么"),
                ("I can describe a whole house without reading from a script",
                 "能不看稿子说整个房子")]))

    # ── Cycle 1 · 客厅 / 餐厅 ──
    add("04-c1-words.html", "Cycle 1 · A — 客厅 / 餐厅", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("客厅", "kètīng", "living room", "keting"),
                ("餐厅", "cāntīng", "dining room", "canting")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家的<b>客厅</b>很大。", "Our living room is big."),
                    ("我们在<b>餐厅</b>吃饭。", "We eat in the dining room."),
                    ("楼下有<b>客厅</b>和<b>餐厅</b>。",
                     "Downstairs there's a living room and a dining room.", True)],
                   "两个词里，哪一个字是一样的？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家的客厅 ________ 。", "我们在 ________ 吃饭。"],
                "别用「很大」——用上节课听力里的 <b>不算大</b> 或 <b>不大也不小</b>，"
                "两句连起来：<b>我家的客厅不算大，可是餐厅很大。</b>"))

    # ── Cycle 2 · 厨房 / 洗手间 ──
    add("07-c2-words.html", "Cycle 2 · A — 厨房 / 洗手间", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("厨房", "chúfáng", "kitchen", "chufang"),
                ("洗手间", "xǐshǒujiān", "toilet", "xishoujian")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我家的<b>厨房</b>不大。", "Our kitchen isn't big."),
                    ("<b>洗手间</b>在楼下。", "The toilet is downstairs."),
                    ("楼下有<b>厨房</b>和<b>洗手间</b>。",
                     "Downstairs there's a kitchen and a toilet.", True)],
                   "「洗手间」和「浴室」一样吗？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我家的厨房 ________ 。", "洗手间在 ________ 。"],
                "一句话里放进今天四个词，按顺序说，每个后面加上在几楼。"))

    add("10-recall.html", "Recall · four characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["客厅", "餐厅", "厨房", "洗手间"], "一起读两遍。", cols=4))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · 在 + 地方 + 做什么", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说某人在哪儿做什么",
                  "人 + 在 + 地方 + 做什么",
                  [("他<b>在房间里</b>打电话。", "He's making a phone call in his room — the textbook's own example, p.123."),
                   ("她<b>在厨房</b>吃饭。", "She's eating in the kitchen."),
                   ("我妈妈<b>在客厅</b>看电视。", "My mum is watching TV in the living room.")],
                  "「在房间里」和「在房间」都行。「里面、上面、外面」下节课学，今天「里」就够了。"))
    add("12-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("两个小句，每句都有楼层和房间",
                "我在楼上的卧室看书，我弟弟在楼下的客厅看电视。",
                "I'm reading in the bedroom upstairs; my little brother is watching TV "
                "in the living room downstairs.",
                "地方放在动词<b>前面</b>——不是「我看书在客厅」。"))

    add("13-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("怎么说 kitchen？ living room？ dining room？", "写在小白板上"),
               ("「洗手间」和「浴室」是同一个房间吗？", "对就举大拇指，不对就朝下"),
               ("「客厅」和「餐厅」共用哪一个字？", "写那一个字"),
               ("有人在做饭。他在哪儿？在做什么？", "一句完整的话，写在小白板上"),
               ("这句话对不对？ ✗ 我在吃饭厨房。", "哪里错了？怎么改？")]))

    # ── Text 1 complete ──
    add("14-text.html", "Text 1 · complete", IDO, "课文一 · p.122 · CD 61",
        s_text("课文一 · 整篇 · 现在四个词都会了",
               "我家的房子有两层。楼上有三间卧室、一个书房和一个浴室(洗澡间)，"
               "楼下有客厅、餐厅、厨房和洗手间。我的房间在楼上。我特别喜欢我的房间。",
               "这个房子有几层？　楼下有几个房间？说一说。　"
               "说话的人的房间在楼上还是楼下？　他喜欢他的房间吗？你怎么知道？",
               "放 CD，学生跟着看。一起读。第三遍把拼音关掉再读一次。", size=23))

    # ── Practice ──
    add("15-summary.html", "Summary board · 十三个词", PRAC, "词汇总览 · stays on screen",
        s_summary([("客厅", "keting"), ("餐厅", "canting"), ("厨房", "chufang"),
                   ("洗手间", "xishoujian"), ("卧室", "woshi"), ("书房", "shufang"),
                   ("浴室", "yushi"), ("房间", "fangjian"), ("房子", "fangzi"),
                   ("楼上", "loushang")],
                  "三节课的词都在这儿——这一页整节课都留在屏幕上。", dense=True))

    add("16-act1.html", "Activity 1 · One sentence per person (We Do, 8 min)", PRAC,
        "活动一 · We Do · 8 分钟 · 课本 p.123 第 2 题",
        s_task("活动一 · 看图说话 · 九个人，九个房间",
               ["课本 p.123 的剖面图投到屏幕上，放大。",
                "先全班一起，一个人一句，点名回答。",
                "有人只说「他在厨房」，就追一句：<b>他在厨房做什么？</b>",
                "然后两人一组，九个人再说一遍，轮流。"],
               cn="他在房间里打电话。　她在厨房吃饭。　他在书房看书。"))
    add("17-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["不看图，从头到尾把九个人的房间和动作说一遍。"],
               "再把九句连成一段话，用「还有」「一边……一边……」连起来，"
               "读起来要像在说<b>一家人</b>，不是九句分开的话。"
               "最后用中文回答：<b>这家人一共有几个人？你怎么知道？</b>"))

    add("18-act2.html", "Activity 2 · House tour role-play (You Do, 10 min)", PRAC,
        "活动二 · You Do · 10 分钟",
        s_task("活动二 · 带同桌参观你家 · 角色卡",
               ["每组一张房子卡：几层、哪个房间在哪一层、一个特别的地方。",
                "A 带 B 参观，B 没来过，要问清楚东西在哪儿。",
                "B 至少要问到五个房间。问完交换卡片，再来一次。"],
               "A 的卡片开始前就收走——要靠记。B 不是客人，是<b>不想买这个房子的人</b>，"
               "要挑两个毛病（这个房子没有书房吗？厨房太小了），A 每次都要用「可是」"
               "或「因为」说服他。最后 B 用中文向全班报告买不买、为什么。",
               cn="B：你家的房子有几层？　A：有两层。　B：厨房在楼上还是楼下？　A：在楼下。"))

    add("19-act2-survey.html", "Textbook p.126 Act.6 · class survey", PRAC,
        "活动二 · 课本 p.126 第 6 题",
        s_list("站起来走动 · 问四个不同的同学 · 答案要写下来",
               [("你家的房子有几层？", ""), ("你家有几间卧室？", ""),
                ("客厅在几楼？", ""), ("厨房在楼上还是楼下？", ""),
                ("你家有书房吗？有几个？", ""), ("你的卧室在几楼？", ""),
                ("你爸爸、妈妈的卧室大还是你的卧室大？", "")],
               "七个问题，四个同学——不要问同一个人两次。", compact=True))

    add("20-act2-visit.html", "Textbook p.130 Act.10 · arranging a visit", PRAC,
        "活动二 · 课本 p.130 第 10 题",
        s_dialogue("回到两人一组 · 约时间去他家 · B 要先拒绝三次",
                   [("A", "我今晚可以去你家吗？"), ("B", "对不起，我今晚不在家。"),
                    ("A", "我明天上午去，好吗？"), ("B", "不可以，我上午要去买东西。"),
                    ("A", "周末去，可以吗？"), ("B", "可以，你周末来吧，我在家等你。")],
                   "B 每次拒绝的理由都要不一样——三次以后才可以答应。"))

    add("21-strokes.html", "Characters · 厅 厨 (Workbook p.145)", PRAC,
        "写汉字 · 练习册 p.145",
        s_strokes([("厅", 4, "厂字头，里面一个丁——只有四画"),
                   ("厨", 12, "厂字头，里面是「豆」加「寸」")],
                  "笔顺 · 每个字写三遍 · 最后两个字",
                  "写完这两个，练习册第 1 题就全部写完了。"))
    add("22-wb.html", "Workbook · p.145 Ex.2 + p.146 Ex.5", PRAC, "练习册 · pp.145–146",
        s_task("练习册 · 现在两题都能做完了",
               ["<b>p.145 第 2 题</b>　七个房间全部认得出来了——把号码填上。",
                "<b>p.146 第 5 题</b>　方格组词，今天解锁的：",
                "客厅 · 餐厅 · 厨房 · 洗手间 · 卧室 · 书房 · 浴室 · 房间 · 楼上 · 楼下"],
               cn="客 + 厅 → 客厅　·　厨 + 房 → 厨房　·　洗 + 手 + 间 → 洗手间"))

    add("23-game.html", "Game · 20 Questions — guess the room (5 min)", PRAC,
        "游戏 · 二十个问题 · 5 分钟",
        s_list("游戏 · 猜房间 20 Questions",
               [("一个同学想一个房间，不说出来", "从屏幕上十三个词里选"),
                ("全班用中文问是非题，最多二十个", "这个房间在楼上吗？你在这个房间吃饭吗？"),
                ("猜到了就说", "是不是厨房？"),
                ("用英文问一次，就扣掉一个问题", "问完二十个还没猜到，答案公布")],
               "<b>加难</b>：猜对的人当下一个答题的，全班只有十个问题——问题要问得准。"))

    add("24-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 特别问第三条：谁不看东西说了整整一分钟？",
                "<b>自评</b> · 三条目标，举手表决。",
                "<b>出门条</b> · 口头的，在门口说，一人一句。",
                "<b>下节课</b> · 不再数房间了——学怎么说东西在<b>哪儿</b>：上面、下面、里面、外面。"],
               cn="出门条：说一个你家在楼上的房间，和一个在楼下的，要说完整的句子。"))

    add("25-wb-extra.html", "If the room runs quick · Workbook p.150 Ex.12", PLEN,
        "机动 · 练习册 p.150 第 12 题",
        s_task("时间有多的话 · 写一写",
               ["四层楼的公寓，八个住户，每个人在做一件事。",
                "跟 p.123 第 2 题一样，只是写下来，而且要说清楚住在几楼。"],
               cn="小明住在四楼。他正在看电视。大力也住在 ________ 。"))
    return S
