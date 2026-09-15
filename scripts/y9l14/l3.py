# -*- coding: utf-8 -*-
"""Y9 L14 · Lesson 3 of 6 — no new words; journeys from home, CD 54

Source: docs/lesson-plans/y9-l14/03-journeys-from-home-speaking.md
Textbook p.135 Act. 4, p.136 Act. 5 and Act. 6 (CD 54). Workbook p.156 Ex. 6,
p.157 Ex. 7, p.158 Ex. 10 and Ex. 11, p.159 Ex. 12.

The only lesson in the series with no vocabulary cycles — so there is no
summary board and no 写一句 slide. The I Do time goes to CD 54 and to the
six question types instead.
"""
from build import (s_recall, s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_errors, s_listening, s_title, s_lisc, label)

SLUG = "l3-journeys-from-home"
TITLE = "Y9 L14 · 问路 Asking the Way · Lesson 3 of 6"
CARD = (SLUG, "从你家怎么去", "Journeys From Home · 采访 + 报告",
        "speaking", "没有生词，全靠嘴巴。六个问题采访同伴，然后用<b>第三人称</b>"
                    "向全班报告——这正是单元测验口试的题型。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 从你家怎么去", "LESSON 3 OF 6", "第十四课 · 问路",
        s_title("从你家怎么去", "Journeys From Home",
                "Year 9 · Book 3 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 3 · p.135–136 · 第 4–6 题 · CD 54"))

    add("02-review.html", "Review · 十五个公共设施", REV, "复习 · Lessons 1–2",
        label("认字快闪 · characters only · 全班一起读 · 练习册 p.156 第 6 题")
        + '  <div class="recall-grid" style="grid-template-columns:repeat(5,1fr);gap:10pt;">\n'
        + "\n".join('    <div class="recall-cell" style="padding:10pt 6pt;">'
                    '<p class="recall-hanzi" style="font-size:26pt;">%s</p></div>' % w
                    for w in ["邮局", "银行", "诊所", "百货公司", "市政大楼",
                              "教堂", "公园", "咖啡馆", "购物广场", "车站",
                              "服装店", "机场", "火车站", "图书馆", "体育中心"])
        + "\n  </div>\n"
        + '  <p class="support" style="margin-top:10pt;">'
          '然后两人一组，凭记忆演课文一——屏幕上只留三个问题：'
          '<b>坐几路车？要坐几站？在哪站下车？</b></p>')

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("interview someone about a real journey from their home, "
               "and report what they said to the class.",
               [("I can ask how long a journey takes",
                 "能问：走路要多长时间？坐车要多长时间？"),
                ("I can answer with a real journey from my own home",
                 "能说我自己家的真实路线，不是编的"),
                ("I can report a classmate's answer in the third person",
                 "能用第三人称报告：他每天骑自行车上学，大概要十五分钟")]))

    add("04-listening.html", "CD 54 · 听一听 (p.136 第 6 题)", IDO,
        "听力 · CD 54 · a 还是 b",
        s_listening("听两遍 · 第一遍整段，第二遍一句一停 · 说说是哪个词决定的",
                    [("从你家怎么去电影院？", "a 走路　　b 坐公共汽车"),
                     ("你家附近有什么商店？", "a 服装店、家具店　　b 只有超市"),
                     ("你们家常去哪儿买蔬菜、水果？", "a 菜市场　　b 超市"),
                     ("超市里的东西贵不贵？", "a 比菜市场贵　　b 比菜市场便宜"),
                     ("你生病去哪儿看医生？", "a 医院　　b 离家不远的诊所"),
                     ("你爸爸、妈妈工作的地方远吗？", "a 都很近　　b 一近一远")],
                    "这六段就是等一下采访要用的<b>范例</b>——听的是怎么答，不只是答什么。"))

    add("05-questions.html", "六个问题 · The interview questions", IDO,
        "句型 · 六个问题",
        s_list("采访要问的六件事（课本 p.136 第 5 题）",
               [("从你家去学校怎么走？", "问<b>路线</b>"),
                ("走路要多长时间？", "问<b>走路多久</b>"),
                ("需要坐车吗？坐几路？", "问<b>要不要坐车</b>"),
                ("你常去哪儿购物？怎么去？", "问<b>习惯 + 办法</b>"),
                ("从你家坐飞机去中国要飞几个小时？", "问<b>长途多久</b>")],
               "第六个问题留给你自己编——问同伴一件书上没有的事。", compact=True))

    add("06-model.html", "老师示范 · 一个完整的回答", IDO, "句型 · 想给他们听",
        s_focus("示范 · 从我家去学校",
                "从我家去学校，我先走五分钟到车站，然后坐25路公共汽车，坐三站。"
                "下车以后过马路，学校就在我的右手边。走路加坐车，大概二十分钟。",
                "From my home to school: five minutes' walk to the stop, "
                "then three stops on the 25. Cross the road when you get off "
                "and the school is on your right. About twenty minutes in all.",
                "走多久 → 坐什么 → 坐几站 → 下车以后 → 一共多久。五段，"
                "每一段都是他们已经会的。"))

    add("07-pattern.html", "Pattern · 离 还是 从？", IDO, "句型 · 最容易混的两个字",
        s_pattern("句型 · 两个都对，可是不一样",
                  "A 离 B 很远 ／ 从 A 去 B",
                  [("我家<b>离</b>学校很远。", "Distance between two fixed points."),
                   ("<b>从</b>我家去学校要二十分钟。",
                    "The journey — where it starts from."),
                   ("我家<b>离</b>机场不远，可是<b>从</b>我家去机场要换两次车。",
                    "Close in distance, awkward as a journey — both in one sentence.")],
                  "「离」量的是<b>距离</b>，「从」说的是<b>起点</b>。"
                  "测验的翻译题两个都会考。"))

    add("08-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("用中文问我：How long does it take on foot?", "全班一起问"),
               ("举手：「多长时间」问的是什么——多远，还是多久？", None),
               ("这句哪里错了？ 从我家学校很远。", "找出来，改过来"),
               ("填哪个字？ ________ 我家去机场要两个小时。", "「离」还是「从」？")]))

    # ── Flexible practice ──
    add("09-map.html", "Activity 1 · 地图上的路线", PRAC, "活动一 · We Do · 6 分钟",
        s_task("活动一 · 两人一张地图（课本 p.135），只说不写",
               ["四个情况，轮流：<b>去购物广场 · 去飞机场 · 去公共图书馆 · 去电影院</b>",
                "A 用三个问题问，B 看着地图答。做完两个就换。",
                "然后一起<b>口头</b>做练习册 p.158 第 10 题的四个路线问题——说，不写。"],
               "B <b>不看地图</b>回答，A 拿着地图检查。"
               "B 还要给一句提醒：<b>别在第一个路口拐，那是去医院的路——"
               "要在第二个路口拐。</b>"))
    add("10-interview.html", "Activity 2 · 采访同伴", PRAC,
        "活动二 · You Do · 10 分钟",
        s_list("活动二 · 先采访，再报告",
               [("采访 · 六个问题，答案记在格子里，不写整句", "6 分钟"),
                ("流利的同学<b>先当采访者</b>——让同伴先听见问题长什么样", None),
                ("报告 · 白板上写<b>两句</b>，用第三人称，然后点六七位念出来", "4 分钟"),
                ("全班听：谁把「他／她」说成了「我」？", "这是今天要抓的错")],
               "报告同伴，同时用「比」跟自己比："
               "<b>他家比我家离学校近。我要坐车，可是他走路十分钟就到了。</b>"
               "再加一句「我觉得……」。做完就去采访第二个人，说说谁的路更省事。"))
    add("11-game.html", "Game · 猜猜我要去哪儿 · 20 Questions", PRAC, "游戏 · 7 分钟",
        s_task("游戏 · 一位同学抽一张地点卡，不给别人看",
               ["全班猜他要去哪儿，可是<b>只能问路线问题</b>——",
                "　　你走路去吗？ 要坐几站？ 路上过桥吗？ 那个地方在市中心吗？",
                "<b>不能问</b>「那是什么地方？」。最多二十个问题。",
                "答的人只能说：对 · 不对 · 我不知道。"],
               "给流利的同学：不说「对／不对」，用<b>完整句</b>答——"
               "<b>不对，我不走路去，我坐公共汽车。</b> 信息更多，也逼他每次都要说话。"))

    add("12-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 请一位同学读，然后问：哪一条最难？取两个答案。",
                "<b>自评</b> · 举手，一条一条来。",
                "<b>出门条是<u>说</u>的</b> · 每个人在门口说一句同伴的路线，"
                "用第三人称，说完才能走。",
                "<b>下节课</b> · 换话题——你的包里有什么？下下节课，那个包被偷了。"],
               cn="没写完练习册 p.158 第 11 题、p.159 第 12 题的，"
                  "下节课复习的时候接着做。"))

    return S
