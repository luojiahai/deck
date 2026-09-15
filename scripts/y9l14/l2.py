# -*- coding: utf-8 -*-
"""Y9 L14 · Lesson 2 of 6 — 座 / 庙 / 河 / 桥 + 坐几路车？要坐几站？在哪站下车？

Source: docs/lesson-plans/y9-l14/02-text1-bus-route-writing.md
Textbook p.132 Text 1 (CD 53). Workbook p.154 Ex. 1, p.155 Ex. 5, p.156 Ex. 8.

座 is a measure word and gets a textonly card. The written direction the
teacher chose means this deck leans on frame-boxes and the text slide rather
than on pair-speaking boards.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_errors,
                   s_text, s_route, s_title, s_lisc, label)

SLUG = "l2-bus-route"
TITLE = "Y9 L14 · 问路 Asking the Way · Lesson 2 of 6"
CARD = (SLUG, "坐几路车", "Text 1 · The Bus Route",
        "writing", "座 · 庙 · 河 · 桥，加三个坐车的问题和「过了……以后」。"
                "公交车上看不见路口——所以路线要说<b>路上会看见什么</b>。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 坐几路车", "LESSON 2 OF 6", "第十四课 · 问路",
        s_title("坐几路车", "The Bus Route",
                "Year 9 · Book 3 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 3 · p.132 · 课文一 · CD 53"))

    add("02-review.html", "Review · 改错 + 写两句", REV, "复习 · Lesson 1",
        s_errors([("我还是骑自行车去，还是坐公共汽车去。",
                   "我或者骑自行车去，或者坐公共汽车去。", "陈述句用「或者」"),
                  ("我坐公共汽车25路上学。", "我坐25路公共汽车上学。",
                   "「几路」在「公共汽车」<b>前面</b>"),
                  ("车站就在教堂对面。", "车站就在教堂对面。", "这句没错——别都改")],
                 "两人一组，九十秒，白板上找出来改过来。然后本子上写两句："
                 "改错 · 三句里有两句是坏的",
                 "一句用「或者」说你怎么上学，一句说你家附近的车站在哪儿。"
))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("ask for and write a bus route — which bus, how many stops, "
               "and where to get off.",
               [("I can ask the three bus questions",
                 "能问：坐几路公共汽车？要坐几站？在哪站下车？"),
                ("I can use 座 with buildings, temples and bridges",
                 "能用「座」：一座庙、一座桥"),
                ("I can write a route that says what you will pass on the way",
                 "能写出路上会看见什么：看见一条河，过了大桥以后……")]))

    # ── Cycle 1 · 座 / 庙 ──
    add("04-c1-words.html", "Cycle 1 · A — 座 / 庙", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("座", "zuò", "measure word · buildings, bridges, temples", None),
                ("庙", "miào", "temple", "miao")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我家附近有一<b>座</b>大楼。",
                     "There's a tall building near my home."),
                    (None, "车站就在那<b>座庙</b>的对面。",
                     "The stop is right opposite that temple."),
                    (None, "那<b>座庙</b>很老，我爷爷常常去。",
                     "That temple is very old; my grandad goes often.", True)],
                   "你家附近有庙吗？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家附近有一座 ________ 。", "________ 就在那座庙的 ________ 。"],
                "用「座」写两句，两个<b>不一样</b>的东西。"
                "然后写一句：为什么「一座自行车」是错的？"))

    # ── Cycle 2 · 河 / 桥 ──
    add("07-c2-words.html", "Cycle 2 · A — 河 / 桥", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("河", "hé", "river", "he"),
                ("桥", "qiáo", "bridge", "qiao")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我家后面有一条<b>河</b>。",
                     "There's a river behind my house."),
                    (None, "过了大<b>桥</b>就到了。",
                     "Once you're over the big bridge, you're there."),
                    (None, "<b>河</b>上有一座大<b>桥</b>，过了<b>桥</b>你就看到广场了。",
                     "There's a big bridge over the river; once you're across, "
                     "you'll see the square.", True)],
                   "河用「条」，桥用「座」——为什么？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["过了 ________ 以后，你就看到 ________ 了。"],
                "用「先……然后……」写两句，路上要经过<b>一座桥</b>和<b>一条河</b>。"
                "最后加一句：<b>大概要二十分钟。</b>"))

    add("10-recall.html", "Recall · 四个生词 + 上节课六个", IDO, "认一认 · Checkpoint",
        s_recall(["座", "庙", "河", "桥", "骑", "自行车",
                  "购物", "广场", "车站", "路"],
                 "前四个是今天的。后六个是昨天的——一起读，不看拼音。", cols=5))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · 三个坐车的问题", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 坐车，要问三件事",
                  "坐几路车？ → 要坐几站？ → 在哪站下车？",
                  [("坐几路公共汽车？", "坐25路或97路都可以。"),
                   ("要坐几站？", "大概坐五六站。"),
                   ("在哪站下车？", "在购物广场那站下车。")],
                  "「五六站」——两个数字并排放，意思是「大概五个或六个」。"
                  "「三四个」「十几分钟」一样。"))
    add("12-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 昨天的「或者」＋今天的路标",
                "你或者坐25路，或者坐97路，都可以。"
                "看见一条河，过了大桥以后，下一站就下车。",
                "Take either the 25 or the 97. When you see a river, "
                "get off at the stop after the big bridge.",
                "公交车上看不见路口——所以不能说「第二个路口拐」，"
                "要说<b>你会看见什么</b>。这就是课文一的写法。"))

    add("13-text.html", "课文一 · Text 1 (CD 53)", IDO, "课文一 · p.132 · CD 53",
        s_text("课文一 · 去八方购物广场 · 先听两遍，再看字",
               "请问，去八方购物广场怎么走？<br>"
               "—— 你或者骑自行车去，或者坐公共汽车去。<br>"
               "坐几路公共汽车？ —— 坐25路或97路都可以。<br>"
               "车站在哪儿？ —— 就在前面那座庙的对面。<br>"
               "我要坐几站？ —— 大概坐五六站。<br>"
               "看见一条河，过了大桥以后，在购物广场那站下车。",
               "1 · 去购物广场，有几个办法？　2 · 车站在哪儿？　3 · 怎么知道快到了？",
               "齐读一遍，然后两人一组分角色读，读完换过来。"))
    add("14-route.html", "路线 · Text 1 as four steps", IDO, "课文一 · 路线拆开看",
        s_route("把课文一的路线拆成四步",
                ["在庙对面上车", "坐25路或97路", "看见一条河", "过了大桥下一站下车"],
                landing="购物广场就到了。",
                note="路线是一条<b>链子</b>，不是一张单子——每一步接着上一步。"))

    add("15-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「一座庙」还是「一个庙」？", "举手投票，然后说为什么"),
               ("白板：写 —— How many stops do I need to take?", "写汉字"),
               ("这句哪里错了？ 我坐公共汽车几路？", "找出来，改过来"),
               ("用手比一比：「过了大桥以后」——你现在在桥的前面还是后面？",
                "全班一起比")]))

    # ── Flexible practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("座", None), ("庙", "miao"), ("河", "he"), ("桥", "qiao"),
                   ("自行车", "zixingche"), ("购物", "gouwu"),
                   ("广场", "guangchang"), ("车站", "chezhan")],
                  "这块板整个活动都留在屏幕上——写的时候可以看。"))
    add("17-task.html", "Activity 1 · 画路线，写路线", PRAC, "活动一 · We Do · 6 分钟",
        s_task("活动一 · 画路线，写路线 · 从「我家」到「购物广场」",
               ["路上<b>一定要经过</b>：一座庙 · 一条河 · 一座大桥 · 一个车站。",
                "先在地图纸上画，再在本子上写四到六句。"
                "屏幕上每个词都要出现。",
                "念的时候，请第三位同学拿笔在黑板地图上跟着走。"
                "走错地方——就说明路线写得不够清楚。"],
               "同一条路写<b>两遍</b>：一遍给走路的人（用上节课的 路口／拐／红绿灯），"
               "一遍给坐车的人（用 几路／几站／下车）。"
               "最后一句用「比」说哪个快，为什么。"))
    add("18-writing.html", "Activity 2 · 课文一 · 笔头", PRAC,
        "活动二 · You Do · 9 分钟 · 本子上", 
        s_list("活动二 · 四件事，按顺序做完 · 老师走动批改",
               [("用<b>完整句</b>回答课文三个问题，再加一句："
                 "你觉得骑自行车去好还是坐车去好？为什么？", "4 分钟"),
                ("练习册 p.154 第 1 题 · 十个地图上的词，写汉字", "3 分钟"),
                ("量词检查 · 庙 桥 河 自行车 山 大楼 公共汽车 手",
                 "八个词写量词——只有三个用「座」"),
                ("练习册 p.155 第 5 题 · 翻译成中文",
                 "这是<b>单元测验第三部分</b>的题型——慢慢做，别赶")],
               "写完的接着做练习册 p.156 第 8 题——看图写一段公园的话。"))
    add("19-game.html", "Game · 写字接力 Writing Relay", PRAC, "游戏 · 8 分钟",
        s_task("游戏 · 写字接力 · 四人一队，前面一块白板一支笔",
               ["老师读英文，第一个人跑上去写两三个字，跑回来交笔，第二个人接着写。",
                "不能说话，座位上的人不能纠正。",
                "第一队写完<b>而且全对</b>得分。写错字不得分。",
                "题目：Which bus should I take? · Get off at the shopping-centre stop. · "
                "The stop is opposite that temple. · Once you're over the big bridge, you're there."],
               "给流利的同学：写完以后还要<b>自己加一个分句</b>才算分——"
               "<b>在广场那站下车，然后过马路，服装店就在你的右手边。</b>"))

    add("20-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 全班一起读三条 Success Criteria。",
                "<b>自评</b> · 举手，一条一条来。第二条（座）老实点——量词忘得最快。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下节课</b> · 不学新词，全靠嘴巴——问同学："
                "从你家去机场怎么走？要多长时间？"],
               cn="出门条：写两个问题 —— 一个问几路车，一个问在哪站下车。"))

    return S
