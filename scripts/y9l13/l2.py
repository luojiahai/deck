# -*- coding: utf-8 -*-
"""Y9 L13 · Lesson 2 of 6 — 诊所 / 银行 / 百货公司 / 市政大楼 + 就在……对面

Source: docs/lesson-plans/y9-l13/02-facilities-position-mixed.md
Textbook p.122 (Text 1, second half), p.123 Act. 1, p.125 Act. 4.
Exit ticket is workbook p.148 Ex. 9 items 4 and 5.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_errors,
                   s_title, s_lisc, label)

SLUG = "l2-facilities"
TITLE = "Y9 L13 · 社区 Neighbourhood · Lesson 2 of 6"
CARD = (SLUG, "我家附近有什么", "Facilities · 就在……对面",
        "vocab", "诊所 · 银行 · 百货公司 · 市政大楼，两种摆位说法：「就在……对面」和「的左边是……」。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我家附近有什么", "LESSON 2 OF 6", "第十三课 · 社区",
        s_title("我家附近有什么", "What's in My Neighbourhood",
                "Year 9 · Book 3 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 3 · pp.122–123, 125"))

    add("02-review.html", "Review · L1 复习", REV, "复习 · Lesson 1",
        s_errors([("我家离学校很方便。", "我家离学校很近。", "方便说生活，不说距离"),
                  ("邮局离不远我家。", "邮局离我家不远。", "「离 B」要先说完，再说远近")],
                 "改错 · 白板，九十秒",
                 "然后白板两题：写「我家住在市中心」· 写「邮局离我家不远」。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("name the main buildings in a neighbourhood and say where each one is.",
               [("I can name four neighbourhood buildings in Chinese",
                 "能说出四个社区建筑：诊所、银行、百货公司、市政大楼"),
                ("I can use A 就在 B 对面／旁边", "能用「就在……对面／旁边」摆位置"),
                ("I can use A 的左边／右边是 B", "能用「……的左边／右边是……」说一排建筑")]))

    # ── Cycle 1 · 诊所 / 银行 ──
    add("04-c1-words.html", "Cycle 1 · A — 诊所 / 银行", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("诊所", "zhěnsuǒ", "clinic", "zhensuo"),
                ("银行", "yínháng", "bank", "yinhang")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "<b>诊所</b>离我家很近。", "The clinic is very close to my home."),
                    (None, "我妈妈在<b>银行</b>工作。", "My mum works at a bank."),
                    (None, "<b>银行</b>就在<b>诊所</b>旁边。",
                     "The bank is right beside the clinic.", True)],
                   "你家附近有诊所吗？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 离我家很近。", "银行就在 ________ 旁边。"],
                "用「因为……，所以……」写两句：<b>因为诊所离我家很近，"
                "所以生病的时候很方便。</b>"))

    # ── Cycle 2 · 百货公司 / 市政大楼 ──
    add("07-c2-words.html", "Cycle 2 · A — 百货公司 / 市政大楼", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("百货公司", "bǎihuò gōngsī", "department store", "baihuo"),
                ("市政大楼", "shìzhèng dàlóu", "city hall", "shizheng")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我们常常去<b>百货公司</b>买东西。",
                     "We often go to the department store to buy things."),
                    (None, "<b>市政大楼</b>在市中心。", "The city hall is in the city centre."),
                    (None, "<b>市政大楼</b>就在<b>百货公司</b>对面。",
                     "The city hall is right opposite the department store.", True)],
                   "市政大楼在哪儿？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我们常常去 ________ 买东西。", "________ 就在 ________ 对面。"],
                "一句话，把今天四个建筑<b>全部</b>摆进一条街："
                "<b>银行的左边是诊所，右边是百货公司，市政大楼在百货公司对面。</b>"))

    add("10-recall.html", "Recall · 四个生词", IDO, "认一认 · Checkpoint",
        s_recall(["诊所", "银行", "百货公司", "市政大楼"],
                 "「银行」念 yínháng，不是 yínxíng——这个最容易错。", cols=4))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · 两种摆位说法", IDO, "句型 · Sentence pattern",
        s_pattern("句型 A · 从自己出发",
                  "A + 就在 + B + 对面／旁边／附近",
                  [("银行就在邮局对面。", "The bank is right opposite the post office."),
                   ("诊所就在我家附近。", "The clinic is right near my home."),
                   ("百货公司就在银行旁边。", "The department store is right beside the bank.")],
                  "「就」＝正好、就是那儿。去掉也对，加上才像本地人说的。"))
    add("12-pattern2.html", "Pattern · 从地标出发", IDO, "句型 · 另一种说法",
        s_pattern("句型 B · 从地标出发",
                  "A + 的左边／右边 + 是 + B",
                  [("邮局的左边是诊所。", "On the post office's left is the clinic."),
                   ("邮局的右边是银行。", "On the post office's right is the bank."),
                   ("邮局的左边是诊所，右边是银行。",
                    "On its left is the clinic, on its right the bank.")],
                  "句型 A 从<b>要找的地方</b>说起，句型 B 从<b>地标</b>说起。两种都要会。"))
    add("13-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 一口气摆三个",
                "市政大楼在百货公司的前面，百货公司的左边是银行，右边是邮局。",
                "The city hall is in front of the department store; on the store's "
                "left is the bank and on its right the post office.",
                "三个位置，一口气说完。「前面」下节课学——先听一听。"))

    add("14-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「bank」中文怎么说？「行」念什么声调？", "点名"),
               ("白板：写「诊所就在市政大楼对面」。", "Write it in characters"),
               ("这句哪里错了？ 银行在对面邮局。", "地标要在「对面」前面"),
               ("看地图（p.125）：银行在哪儿？诊所在哪儿？百货公司在哪儿？", "点三位同学")]))

    # ── Flexible practice ──
    add("15-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("诊所", "zhensuo"), ("银行", "yinhang"),
                   ("百货公司", "baihuo"), ("市政大楼", "shizheng"),
                   ("邮局", "youju")],
                  "五个词——四个今天的，加上第一课的邮局。整个活动留在屏幕上。"))

    add("16-task.html", "Activity 1 · 我的一条街", PRAC, "活动一 · We Do · 8 分钟",
        s_task("活动一 · 我的一条街",
               ["<b>先做课本 p.123 第 1 题</b>（两分钟）· 十四张建筑图，全班一起快速念出来。"
                "大部分是学过的：超级市场、电影院、书店、飞机场、教堂、公园、文具店、"
                "家具店、医院。卡住的圈出来，游戏时再补。",
                "<b>然后</b> · 在白板上画一排<b>五</b>座建筑（上面五个词，顺序随便），"
                "再写<b>四</b>句话描述这排——四句要用<b>四个不同</b>的位置词："
                "对面 · 旁边 · 的左边是 · 的右边是。"],
               "<b>不要先画。</b> 听同伴用中文描述<b>他</b>那条街，你照着画，"
               "然后两张图对一对。画错的人要用中文说出是哪一句听错了。"))

    add("17-map.html", "Activity 2 · 看地图问答", PRAC, "活动二 · You Do · 9 分钟",
        s_task("活动二 · 看地图问答（课本 p.125 第 4 题）· 每组一张 A5 地图",
               ["A：医院在哪儿？　B：在我家后面。",
                "A：百货公司在哪儿？　B：就在银行对面。",
                "每人至少问六个地方，然后换。",
                "第一轮词库留在黑板上（对面 · 旁边 · 附近 · 的左边是 · 的右边是），"
                "<b>第二轮擦掉</b>。"],
               "B <b>不说地名</b>，只说位置，让 A 猜是哪一座："
               "<b>它就在邮局对面，银行的左边。</b> → A：是诊所吗？ "
               "然后两人合作，说一条经过<b>三座</b>建筑的路线。"))

    add("18-game.html", "Game · 抢词卡 Slap the Character", PRAC, "游戏 · 6 分钟",
        s_task("游戏 · 抢词卡 · 两队，每队一人上台",
               ["黑板上六张卡：诊所 · 银行 · 百货公司 · 市政大楼 · 邮局 · 市中心",
                "老师说英文，先拍到正确那张的得分。每两轮换人，每个人都要上一次。"],
               "老师<b>不说词</b>，改说它的<b>位置</b>——「就在邮局对面的那个」——"
               "拍的人要听完整句才知道拍哪张。"))

    add("19-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 读三条，再问：今天哪一条最难？取两个答案。",
                "<b>自评</b> · 白板上举手：会了 · 差不多 · 还要练，一条一条来。",
                "<b>出门条</b> · 练习册 p.148 第 9 题的第 4、5 小题，两句都要写。",
                "<b>下节课</b> · 学「前面」和「后面」，然后把整个社区连成一段话。"],
               cn="出门条：超市 ____________ 。 · 市政大楼 ____________ 。"))

    return S
