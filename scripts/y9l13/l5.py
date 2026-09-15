# -*- coding: utf-8 -*-
"""Y9 L13 · Lesson 5 of 6 — 拐 / 转 / 向 / 路口 / 第 + 在第 X 个路口

Source: docs/lesson-plans/y9-l13/05-intersections-turns-writing.md
Textbook p.127 Text 2 dialogue 3. Workbook p.152 Ex. 18 is the main
writing task and p.148 Ex. 10 the reading comprehension.

Writing-focused lesson: the routes go in exercise books, because Unit 5
Test Part 7 asks students to write directions from a map.
"""
from build import (s_words, s_word_one, s_examples, s_write, s_recall,
                   s_summary, s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_dialogue, s_arrows, s_route, s_text, s_title, s_lisc,
                   label)

SLUG = "l5-turns"
TITLE = "Y9 L13 · 社区 Neighbourhood · Lesson 5 of 6"
CARD = (SLUG, "第二个路口往右拐", "Turning & Counting Intersections",
        "writing", "向 · 拐 · 转 · 路口 · 第。写路线课——三步以上写进本子，因为测验第七部分就考这个。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 第二个路口往右拐", "LESSON 5 OF 6", "第十三课 · 社区",
        s_title("第二个路口往右拐", "Turning & Counting Intersections",
                "Year 9 · Book 3 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 3 · p.127 · 练习册 pp.148, 152"))

    add("02-review.html", "Review · 白板快测", REV, "复习 · Lesson 4",
        s_list("复习 · 白板，五题，每题写完就举起来",
               [("写：cross the road", None),
                ("写：walk straight ahead", None),
                ("写：traffic lights", None),
                ("翻译：你先过马路，然后一直往前走。", None),
                ("改错：你先一直走往前。", "顺序错了")],
               "最后点名一位：<b>请问，去咖啡馆怎么走？</b> 要完整的两步答案。",
               compact=True))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("write directions that tell someone where to turn.",
               [("I can use 往／向 + 左／右 + 拐／转", "能说往哪边转"),
                ("I can count intersections with 第……个路口", "能数路口"),
                ("I can write a three-step route for someone reading a map",
                 "能写一条三步以上、别人看得懂的路线")]))

    # ── Cycle 1 · 拐 / 转 ──
    add("04-c1-words.html", "Cycle 1 · A — 拐 / 转", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("拐", "guǎi", "turn", "guai"),
                ("转", "zhuǎn", "turn", "zhuan")))
    add("05-c1-note.html", "Cycle 1 · 拐 = 转，别找区别", IDO, "生词 1 · 说清楚",
        s_focus("这两个字在这一课是<b>一样</b>的",
                "往右拐 ＝ 向右转 ＝ 往右转 ＝ 向右拐",
                "All four say the same thing. 拐 and 转 are interchangeable here, "
                "and so are 往 and 向.",
                "直接讲明白。学生会花十分钟找一个这个程度上<b>不存在</b>的区别。"))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "你往右<b>拐</b>。", "Turn right."),
                    (None, "看到红绿灯向左<b>转</b>。",
                     "When you see the lights, turn left."),
                    (None, "先往右<b>拐</b>，然后向左<b>转</b>。",
                     "First turn right, then turn left.", True)],
                   "往右拐和向右转，哪里不一样？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["你往 ________ 拐。", "看到 ________ 向左转。"],
                "同一个转弯写<b>四种</b>说法——拐／转各一次，往／向各一次——"
                "然后说出你自己真的会用哪一种。"))

    # ── Cycle 2 · 向 / 路口 ──
    add("08-c2-words.html", "Cycle 2 · A — 向 / 路口", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("向", "xiàng", "towards", None),
                ("路口", "lùkǒu", "intersection", "lukou")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "请<b>向</b>前走。", "Please walk forward."),
                    (None, "前面有一个<b>路口</b>。", "There's an intersection ahead."),
                    (None, "到<b>路口</b><b>向</b>右拐。",
                     "At the intersection, turn right.", True)],
                   "「路口」是哪两个字合起来的？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["前面有一个 ________ 。", "到路口 ________ 右拐。"],
                "写一条有<b>两个</b>转弯的路线，两个转弯方向<b>相反</b>，"
                "一个用「向」，一个用「往」。"))

    # ── Cycle 3 · 第 ──
    add("11-c3-words.html", "Cycle 3 · A — 第", IDO, "生词 3 · Cycle 3 of 3",
        s_word_one(("第", "dì", "(makes ordinal numbers)", "di")))
    add("12-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "这是<b>第</b>一个路口。", "This is the first intersection."),
                    (None, "在<b>第</b>二个路口过马路。",
                     "Cross the road at the second intersection."),
                    (None, "你在<b>第</b>一个路口往右拐，走五分钟就到了。",
                     "Turn right at the first intersection and it's five minutes.",
                     True)],
                   "「第」自己不是一个词——它把数字变成第几。<b>量词还要留着</b>：第一<b>个</b>路口。"))
    add("13-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["在第 ________ 个路口 ________ 。"],
                "用「第三个路口」写一句，再用「<b>就在你的右手边</b>」收尾。"))

    add("14-recall.html", "Recall · 五个生词", IDO, "认一认 · Checkpoint",
        s_recall(["拐", "转", "向", "路口", "第"],
                 "读完，请一位同学用<b>五个都用上</b>说一句话。", cols=5))

    # ── Pattern ──
    add("15-pattern.html", "Pattern · 在第 X 个路口 + 动作", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 地点在前，动作在后",
                  "在第 + 数字 + 个路口 + 动作",
                  [("往右拐。", "Turn right."),
                   ("在第一个路口往右拐。", "Turn right at the first intersection."),
                   ("你在前边的第一个路口过马路，然后往右转。",
                    "Cross at the first intersection ahead, then turn right.")],
                  "英文先说动作（turn right at…），中文先说<b>地点</b>。每次都这样。"))
    add("16-route.html", "Focus · 四步的路线", IDO, "句型 · 最难的一句",
        s_route("你一直往前走……",
                ["一直往前走", "第二个路口向左拐", "再走五分钟"],
                "医院就在你的右手边。",
                "四步，两个不同的转弯动词，最后落在目的地上。"))

    add("17-text2.html", "Text 2 · 对话三", IDO, "课文二 · p.127 · 对话三",
        s_dialogue("课文二 · 对话三 · 现在「拐、转、第、路口」都会了",
                   [("A", "请问，附近有医院吗？"),
                    ("B", "你在前边的第一个路口过马路，然后往右转。医院就在你的右手边。")],
                   "用中文回答：要在第几个路口过马路？ · 医院在左手边还是右手边？"))

    add("18-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("我说六句，是往右就往右指，是往左就往左指。",
                "往右拐 · 向左转 · 往左拐 · 向右转 · 一直往前走 · 过马路"),
               ("白板：写「在第二个路口向左拐」。", "Write it in characters"),
               ("这句有<b>两处</b>错。都找出来。 你拐右在第二路口。",
                "一处是词序，一处少了一个字"),
               ("「第三个路口」怎么说？", "点名")]))

    # ── Flexible practice ──
    add("19-arrows.html", "Activity 1 · 六个方向", PRAC, "活动一 · We Do · 4 分钟",
        s_arrows("活动一 · 六个方向 · 抄进本子，然后<b>盖起来</b>写英文",
                 [("往右拐", "guai"), ("向左转", "zhuan"), ("一直往前走", "yizhi"),
                  ("过马路", "guomalu"), ("在第一个路口", "di"), ("红绿灯", "honglvdeng")],
                 "抄完盖住板，凭记忆在旁边写英文，再打开用<b>另一种颜色</b>自己改。"
                 "然后还是盖着，自己编<b>第七个</b>——要把上面两个合起来。"))
    add("20-arrows-ext.html", "Activity 1 · Extension", PRAC, "活动一 · 延伸",
        s_task("延伸 · 给写得快的同学",
               ["<b>不抄。</b> 只看英文，把六个中文直接写出来。",
                "然后再写<b>三个书上没有的</b>：",
                "　· 在<b>第三</b>个路口转弯",
                "　· 过了红绿灯<b>以后</b>再过马路",
                "　· 先往左拐，<b>马上</b>再往右拐"],
               cn="写完和同伴换本子，互相挑错。"))

    add("21-write-route.html", "Activity 2 · 写路线", PRAC, "活动二 · You Do · 10 分钟",
        s_task("活动二 · 写路线（练习册 p.152 第 18 题）· 每人一张 A4 地图",
               ["写在本子上，三个目的地：",
                "　1 · 去电影院怎么走？　2 · 去书店怎么走？　3 · 去花店怎么走？",
                "每条<b>至少三步</b>，而且<b>至少用一次</b>「第……个路口」。",
                "第一条全班一起在黑板上示范，然后自己写六分钟，老师巡堂。",
                "写完两人换本子，用手指在地图上<b>走</b>对方的路线。"
                "走到别的地方去了，就回去找是哪一句写错了。"],
               "自己再挑<b>第四</b>个目的地，但写成<b>对话</b>——"
               "请问，去……怎么走？加上完整回答——"
               "而且要写进一个走的人容易搞错的地方："
               "<b>不要在第一个路口拐，要在第二个。</b>"))

    add("22-reading.html", "Activity 3 · 阅读理解", PRAC, "活动三 · You Do · 6 分钟",
        s_text("活动三 · 阅读理解（练习册 p.148 第 10 题）· <b>单元测验第九部分</b>就是这个题型",
               "我们最近搬了家。新家比老家大，也比老家的房子新，我很喜欢。"
               "新家离地铁站很近，走三分钟就到了。但是新家的周围还不太方便："
               "去超级市场要坐一站地铁；附近也没有邮局、诊所、饭店、银行等公共设施；"
               "去菜市场要走十到十五分钟。",
               "六题对错。每一题都要说出<b>课文里哪一句</b>证明它——那一句要念出来。",
               "「周围」「公共设施」是新词，不考——讲一次意思就过。"))

    add("23-game.html", "Game · 写字接力 Writing Relay", PRAC, "游戏 · 3 分钟",
        s_task("游戏 · 写字接力 · 两队排在黑板前",
               ["老师说英文，第一个人上去写<b>第一个字</b>，第二个人写第二个字，"
                "依次接下去。不能说话，不能改前面的人写的。",
                "四轮：turn right · cross the road · the second intersection · "
                "when you see the traffic lights, turn left"],
               "发令人给<b>整条三步路线</b>，整队接力写完，标点也要写。"
               "「第二个路口」漏了「个」的队，这一分不算。"))

    add("24-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 问：谁没看黑板就写出了三步的路线？",
                "<b>自评</b> · 在本子上今天的日期旁边写：会了 · 差不多 · 还要练，一条一个。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下节课</b> · 全部合起来——做一张大地图，互相问路。"],
               cn="出门条：写一句 —— 在第 ______ 个路口 ____________ 。"))

    return S
