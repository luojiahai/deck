# -*- coding: utf-8 -*-
"""Y9 L13 · Lesson 6 of 6 — 看到 / 右手 / 钟 + 看到……就…… / 就在你的右手边

Source: docs/lesson-plans/y9-l13/06-multi-step-routes-game.md
Textbook p.130 Act. 11 (for early finishers), p.131 Act. 12 (CD 52) and
Act. 13. The class builds a shared town on the board and gives routes
across it.

Last deck of the six, so the plenary looks back over the whole sequence,
not just today.
"""
from build import (s_words, s_word_one, s_examples, s_write, s_recall,
                   s_summary, s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_route, s_title, s_lisc, label)

SLUG = "l6-build-the-town"
TITLE = "Y9 L13 · 社区 Neighbourhood · Lesson 6 of 6"
CARD = (SLUG, "我在哪儿？", "Build the Town, Give the Route",
        "game", "看到 · 右手边 · 钟。全班在黑板上建一座城，分组给路线，其他人猜终点。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

ALL_WORDS = ["市中心", "生活", "方便", "邮局", "诊所", "银行", "百货公司",
             "市政大楼", "教堂", "公园", "咖啡馆", "过", "一直", "往前",
             "红绿灯", "向", "拐", "转", "路口", "第", "看到", "右手", "钟"]


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我在哪儿？", "LESSON 6 OF 6", "第十三课 · 社区",
        s_title("我在哪儿？", "Build the Town, Give the Route",
                "Year 9 · Book 3 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 3 · pp.130–131 · 最后一课"))

    add("02-review.html", "Review · 抢词卡（方向版）", REV, "复习 · Lessons 4–5",
        s_task("复习 · 抢词卡 · 方向版 · 两队，每队一人上台",
               ["黑板上六张卡：往右拐 · 向左转 · 一直往前走 · 过马路 · "
                "第一个路口 · 红绿灯",
                "老师说英文，先拍到的得分。每两轮换人，直到每个人都上过一次。",
                "然后白板三十秒：写「在第二个路口往右拐」。"],
               cn="到现在为止，你们的路线一次只有两三步。今天走完整条路。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("give a full multi-step route across a map and follow one we hear.",
               [("I can use 看到……就…… to say what to look out for",
                 "能用「看到……就……」说路上要看什么"),
                ("I can finish a route with 就在你的右手边 or 你就可以看到……了",
                 "能把路线收尾"),
                ("I can give a three-step route someone else can actually follow",
                 "能说一条别人真的走得通的路线")]))

    # ── Cycle 1 · 看到 / 右手 ──
    add("04-c1-words.html", "Cycle 1 · A — 看到 / 右手", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("看到", "kàndào", "see", None),
                ("右手", "yòushǒu", "right hand", "youshou")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "你<b>看到</b>红绿灯就过马路。",
                     "When you see the lights, cross the road."),
                    (None, "银行就在你的<b>右手</b>边。",
                     "The bank is on your right-hand side."),
                    (None, "一直往前走，<b>看到</b>教堂，公园就在你的<b>右手</b>边。",
                     "Go straight; at the church, the park is on your right.", True)],
                   "「看」和「看到」有什么不一样？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["你看到 ________ 就 ________ 。", "________ 就在你的右手边。"],
                "同一条路线写两遍——一遍用「就在你的右手边」收尾，"
                "一遍用「<b>你就可以看到……了</b>」收尾。"
                "然后说说：对一个迷路的人，哪一种更有用？为什么？"))

    # ── Cycle 2 · 钟 ──
    add("07-c2-words.html", "Cycle 2 · A — 钟", IDO, "生词 2 · Cycle 2 of 2",
        s_word_one(("钟", "zhōng", "clock", "zhong")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "那个<b>钟</b>在市政大楼的前面。",
                     "That clock is in front of the city hall."),
                    (None, "走五分<b>钟</b>就到了。",
                     "Five minutes' walk and you're there."),
                    (None, "看到那个大<b>钟</b>，再走两分<b>钟</b>就到了。",
                     "At the big clock, two more minutes and you're there.", True)],
                   "「分钟」你们从第一课就在说了——今天才第一次见到这个字。"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["走 ________ 分钟就到了。"],
                "同一趟路说两个版本——<b>走路</b>和<b>坐车</b>，时间不一样："
                "<b>走路要二十分钟，坐车十分钟就到了。</b>"))

    add("10-recall.html", "Recall · 三个生词", IDO, "认一认 · Checkpoint",
        s_recall(["看到", "右手", "钟"],
                 "「看到」的「到」和「走到」「就到了」是同一个——看了，而且看<b>见</b>了。",
                 cols=3))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · 怎么收尾", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 一条路线要有<b>终点</b>",
                  "……就在你的右手边 ／ 你就可以看到……了",
                  [("医院就在你的右手边。", "The hospital is on your right."),
                   ("你就可以看到教堂了。", "And then you'll be able to see the church."),
                   ("看到红绿灯向右拐，银行就在你的右手边。",
                    "Turn right at the lights and the bank is on your right.")],
                  "指令说完不等于路线说完。要让对方知道<b>他到了</b>。"))
    add("12-route.html", "Focus · 课本 p.131 的范例", IDO, "句型 · 最难的一句",
        s_route("如果从你家去市中心公园……",
                ["先过马路", "然后一直走", "第三个路口向右拐", "再走五分钟"],
                "你就可以看到市中心公园了。",
                "全班一起数：一共几步？ 四步，然后收尾。"))

    add("13-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「看到」和「看」意思完全一样——对不对？", "这句是错的"),
               ("白板：写「邮局就在你的右手边」。", "Write it in characters"),
               ("这句少了一个字。是哪个？ 你看红绿灯就过马路。", None),
               ("「走五分钟就到了」是什么意思？", "点名，用中文说")]))

    # ── Flexible practice ──
    add("14-summary.html", "Summary board · 全课二十三个词", PRAC,
        "词汇总览 · 六节课的全部生词",
        s_recall(ALL_WORDS,
                 "这块板整节课都留在屏幕上——建城和猜路线都靠它。",
                 cols=6, head="第十三课 · 全部生词 · characters only"))

    add("15-build.html", "Activity 1 · 全班建一座城", PRAC, "活动一 · We Do · 8 分钟",
        s_task("活动一 · 全班建一座城 · 黑板上已经画好空白街道网（四横四竖）",
               ["每组拿一张 A4 卡，从上面的总览板里<b>挑一座建筑</b>，画出来，"
                "用汉字标上名字。",
                "一组一组上来，把卡贴在网格上任何位置——"
                "<b>贴的代价</b>是用中文说一句话，把它摆好：",
                "　<b>我们的银行在第二个路口，就在邮局对面。</b>",
                "最后黑板上是一座十二到十五座建筑的共享城市，"
                "而且每个学生都出声说过一句摆位句。"],
               "不贴自己的卡。听<b>前一组</b>的摆位句，按他们说的把<b>他们的</b>卡贴上去。"
               "贴错了，他们可以用中文纠正你。"))

    add("16-game.html", "Activity 2 · 我在哪儿？", PRAC, "活动二 · You Do · 11 分钟",
        s_task("活动二 · 我在哪儿？ · 今天的重头戏 · 三人一组",
               ["每组<b>偷偷</b>选一个终点，写一条<b>三步</b>的路线，"
                "起点是网格下方标着「你」的那一点。四分钟写。",
                "然后每组把路线<b>慢慢念一遍</b>，其余同学在心里走，"
                "把终点写在白板上。喊「三、二、一」，一起举起来。",
                "一半以上的人走对了，该组得 2 分；一个人都没走对，0 分，重写。"],
               "路线<b>倒着</b>说——从终点说回「你」——让全班推出起点在哪儿。"
               "或者：说一条<b>四步</b>的路线，里面故意藏一个错，"
               "全班要用中文说出<b>哪一步</b>错了、怎么改，不能只用手指地图。"))
    add("17-game-frame.html", "Activity 2 · 句型（前两轮留，之后擦掉）", PRAC,
        "活动二 · 句型支架",
        s_route("你先过马路，然后……",
                ["一直往前走", "第二个路口向左拐", "看到红绿灯"],
                "________ 就在你的右手边。",
                "<b>只留前两轮</b>，第三轮起擦掉——后面要他们自己组织。"))
    add("18-game-early.html", "Activity 2 · 早做完的组", PRAC, "活动二 · 更难的地图",
        s_task("早做完的组 · 换课本 p.130 第 11 题的地图",
               ["那张地图比黑板上的网格难——街道更多，没有提示，"
                "而且书上的范例答案是一条<b>三次转弯</b>的真路线。",
                "四个情境全写：去医院 · 去体育中心 · 去咖啡馆 · 去市政大楼",
                "写完两人互相走一遍，趁全班还在起草。"],
               cn="写完还有时间，就把四条连成一趟，一口气说完。"))

    add("19-listening.html", "Activity 3 · 听力 CD 52（计分）", PRAC,
        "活动三 · You Do · 4 分钟",
        s_task("活动三 · 听力 · 课本 p.131 第 12 题 · CD 52 · 放两遍 · 按队计分",
               ["每人一张 A5 街道图，格子 A–H。六条指路，六个地方写字母：",
                "　超市 · 邮局 · 诊所 · 银行 · 市政大楼 · 教堂",
                "各队统计答对几个，加进活动二的总分。"],
               "<b>只听一遍</b>，而且不写字母——写下六条里各自的<b>转弯动作</b>："
               "往右拐 / 过马路 / 往右转两次 / 在第二个路口过马路 / 往左拐 / 往右拐。"
               "然后念出来，看全班同不同意。"))

    # ── Plenary: whole sequence ──
    add("20-plenary-review.html", "Plenary · 回看六节课", PLEN, "小结 · 整个单元",
        s_list("小结 · 这是第六课，所以回看<b>六节课</b>，不只是今天",
               [("<b>一</b> · 我家住在哪儿 —— 离……远／不远",),
                ("<b>二</b> · 社区里有什么 —— 诊所、银行、百货公司、市政大楼",),
                ("<b>三</b> · 前面、后面 —— 把整条街连成一段话",),
                ("<b>四</b> · 请问，怎么走？ —— 过马路、一直往前走",),
                ("<b>五</b> · 第……个路口、往左／右拐 —— 写路线",),
                ("<b>六</b> · 看到……就……、右手边 —— 收尾",)],
               "每一行写：会了 · 差不多 · 还要练。"
               "<b>「差不多」最多的那一行，就是测验前要先热身的那一课。</b>",
               compact=True))

    add("21-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 读今天三条，再问全班：哪一节课最难？"
                "取三个答案，能用中文就用中文。",
                "<b>出门条</b> · 写一条<b>完整</b>的路线，从教室到学校里任何一个地方，"
                "至少三步，用「就在你的右手边」或「你就可以看到……了」收尾。",
                "<b>下一课</b> · 第十四课《问路》——一样是问路，可是这次要坐公共汽车："
                "坐几路车？坐几站？在哪站下车？"],
               cn="出门条：从我们的教室去 ____________ ，怎么走？"))

    return S
