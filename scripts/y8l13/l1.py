# -*- coding: utf-8 -*-
"""Y8 L13 · Lesson 1 of 6 — the house, its storeys, and 有 vs 在

Source: docs/lesson-plans/y8-l13/01-house-storeys-mixed.md
Textbook p.122 (Text 1, first half; New Words 1–4), p.126 Act. 6 Q1/Q3/Q4.
Workbook p.144 Ex. 1, p.146 Ex. 4 and Ex. 5.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_contrast,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes, s_figure,
                   s_title, s_lisc, label)

SLUG = "l1-house-storeys"
TITLE = "Y8 L13 · 房子 House · Lesson 1 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

# Card shown on the series landing page (index/designs/y8-l13/index.html),
# written by build.py. Lives beside the lesson it describes.
CARD = dict(cn='房子有几层', en='The house & its storeys',
            desc='The first six words, and the contrast the whole textbook lesson turns on — 有 for what a place contains, 在 for where a thing is. Students draw their own house in section and label it.',
            words='房子 · 房间 · 层 · 楼 · 楼上 · 楼下', n=6)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 房子 The house", "LESSON 1 OF 6", "第十三课 · 房子",
        s_title("房子有几层？", "The House and Its Storeys",
                "Year 8 · Book 2 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 2 · p.122"))

    add("02-review.html", "Review · Unit 4 recap", REV, "复习 · Unit 4",
        s_list("小白板 · 五题 · 写完举起来",
               [("你每天吃几种水果？", "要用「种」"),
                ("翻译：<i>My family eats vegetables every day.</i>", "我们家每天吃蔬菜。"),
                ("应该 还是 可是？ 妈妈说我 ____ 每天吃蔬菜。", ""),
                ("用中文写：三 · 五 · 十", ""),
                ("写两个：起床 · 睡觉 · 放学", "")],
               "上一个单元你用「有」加数字说吃几种水果——今天同样的句型，数房间。", compact=True))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say how many storeys and rooms a house has, and where a room is.",
               [("I can name the parts of a house I have learnt today", "能说出今天学的房子的部分"),
                ("I can use 有 to say what a house contains", "能用「有」说房子里有什么"),
                ("I can use 在 to say where a room is", "能用「在」说房间在哪儿")]))

    # ── Cycle 1 · 房子 / 房间 ──
    add("04-c1-words.html", "Cycle 1 · A — 房子 / 房间", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("房子", "fángzi", "house", "fangzi"),
                ("房间", "fángjiān", "room", "fangjian")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家的<b>房子</b>很大。", "My house is big."),
                    ("我的<b>房间</b>不大。", "My room isn't big."),
                    ("我家的<b>房子</b>有五个<b>房间</b>。", "My house has five rooms.", True)],
                   "你家的房子大不大？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家的房子 ________ 。", "我的房间 ________ 。"],
                "两句连起来，用「可是」：<b>我家的房子很大，可是我的房间不大。</b>"))

    # ── Cycle 2 · 层 / 楼 ──
    add("07-c2-words.html", "Cycle 2 · A — 层 / 楼", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("层（層）", "céng", "storey; layer", "ceng"),
                ("楼（樓）", "lóu", "floor; multi-storey building", "lou")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我家的房子有两<b>层</b>。", "My house has two storeys."),
                    ("我的房间在三<b>楼</b>。", "My room is on the third floor."),
                    ("这个房子有五<b>层</b>，我住在四<b>楼</b>。",
                     "This house has five storeys; I live on the fourth floor.", True)],
                   "你住在几楼？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我家的房子有 ________ 层。", "我的房间在 ________ 楼。"],
                "说别人的，再比一比：<b>我家的房子有两层，我朋友家的房子有三层。</b>"))

    # ── Cycle 3 · 楼上 / 楼下 ──
    add("10-c3-words.html", "Cycle 3 · A — 楼上 / 楼下", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("楼上", "lóushàng", "upstairs", "loushang"),
                ("楼下", "lóuxià", "downstairs", "louxia")))
    add("11-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([("我的房间在<b>楼上</b>。", "My room is upstairs."),
                    ("我妈妈在<b>楼下</b>。", "My mum is downstairs."),
                    ("我在<b>楼上</b>，我妈妈在<b>楼下</b>。",
                     "I'm upstairs, my mum is downstairs.", True)],
                   "你的房间在楼上还是楼下？"))
    add("12-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["________ 在楼上，________ 在楼下。"],
                "三句，不看屏幕：你在哪儿、家里谁在哪儿、房子有几层。"))

    add("13-recall.html", "Recall · six characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["房子", "房间", "层", "楼", "楼上", "楼下"],
                 "读不出来就停下来重教——不要往下走。"))

    # ── The pattern this whole textbook lesson turns on ──
    add("14-contrast.html", "有 vs 在 — the contrast", IDO, "句型 · 有 还是 在",
        s_contrast(("有", "there is / there are", "place + 有 + thing", "楼上有三个房间。"),
                   ("在", "is located at", "thing + 在 + place", "我的房间在楼上。"),
                   "课本 p.124 的 NOTE 就是这两条。两边说的是同一件事，只是从哪一头开始说。"))
    add("15-pattern.html", "Pattern · 有 / 在", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说房子里有什么、在哪儿",
                  "地方 + 有 + 东西　／　东西 + 在 + 地方",
                  [("我家的房子<b>有</b>两层。", "My house has two storeys — saying what exists."),
                   ("我的房间<b>在</b>楼上。", "My room is upstairs — saying where it is."),
                   ("楼上<b>有</b>三个房间。", "Upstairs there are three rooms — place first, then 有.")]))
    add("16-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("三句连起来，一口气说完",
                "我家的房子有三层，我的房间在三楼，我爸爸妈妈的房间在二楼。",
                "My house has three storeys; my room is on the third floor; "
                "my parents' room is on the second.",
                "一个「有」，两个「在」——先说房子，再说人在哪儿。"))

    add("17-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「层」是什么意思？", "懂了就举大拇指"),
               ("有 还是 在？ 我的房间 ____ 楼上。", "写在小白板上"),
               ("有 还是 在？ 楼下 ____ 两个房间。", "写在小白板上"),
               ("这句话对不对？ ✗ 我的房间有楼上。", "哪里错了？怎么改？")]))

    # ── Practice ──
    add("18-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("房子", "fangzi"), ("房间", "fangjian"), ("层", "ceng"),
                   ("楼", "lou"), ("楼上", "loushang"), ("楼下", "louxia")],
                  "这一页留在屏幕上——活动一、活动二都看它。"))

    add("19-act1.html", "Activity 1 · Draw your house in section (We Do, 9 min)", PRAC,
        "活动一 · We Do · 9 分钟",
        s_figure("ceng", "活动一 · 画你家的房子（剖面图）",
                 ["先一起在黑板上画一个——两层，标 <b>楼上</b>、<b>楼下</b>。",
                  "每一层写有几个 <b>房间</b>，用箭头标出 <b>我的房间</b>。",
                  "图下面写三句：一句用 <b>有</b>，一句用 <b>在</b>，一句说有几个房间。",
                  "房子至少要有两 <b>层</b>。"],
                 cn="我家的房子有两层。楼上有三个房间。我的房间在楼上。"))
    add("20-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["写成一段话，五句连起来，不要写成三条分开的句子。"],
               "五句要有一句用「可是」：<b>我家的房子很大，可是我的房间不大。</b> "
               "再说一个别人的房间，不只说自己的。写的时候把纸翻过来，不看总览页。"))

    add("21-act2.html", "Activity 2 · 有 or 在 (You Do, 9 min)", PRAC,
        "活动二 · You Do · 9 分钟",
        s_list("活动二 · 有 还是 在？ 小白板，六题一轮",
               [("我的房间 ____ 楼上。", ""), ("我家的房子 ____ 两层。", ""),
                ("楼下 ____ 三个房间。", ""), ("我 ____ 楼下。", ""),
                ("这个房子 ____ 五层。", ""), ("我妈妈的房间 ____ 二楼。", "")],
               "写完举起来。然后把屏幕关掉，自己写三句，至少一句用「有」、一句用「在」。",
               compact=True))
    add("22-act2-wb.html", "Activity 2 · Workbook p.146 Ex.4 + Ex.5", PRAC,
        "活动二 · 练习册 · p.146",
        s_task("练习册 p.146 · 第 4 题、第 5 题",
               ["<b>第 4 题</b>　把句子补完整。第一句就是今天的句型：",
                "<b>第 5 题</b>　从方格里选两个字组词。今天先写你会读的：",
                "楼上 · 楼下 · 房间 · 起床 · 睡觉 · 上课 · 下课 · 放学 · 走路"],
               cn="我家的房子有两层，我的房间 ________ 。"))

    add("23-strokes.html", "Characters · 房 层 楼 间 (Workbook p.144 Ex.1)", PRAC,
        "写汉字 · 练习册 p.144",
        s_strokes([("房", 8, "上面是「户」，先写点，再写横折"),
                   ("层", 7, "「尸」在外面，「云」在里面"),
                   ("楼", 13, "左边木，右边米加女——一笔一笔来"),
                   ("间", 7, "先写门，再写里面的日")],
                  "笔顺 · 每个字写三遍",
                  "练习册上另外几个字（卧 室 浴 洗 澡 厅 厨）下两节课学到再写，今天留空。"))

    add("24-game.html", "Game · Slap the Character (5 min)", PRAC, "游戏 · 拍字 · 5 分钟",
        s_list("游戏 · 拍字 Slap the Character",
               [("两个同学上来，黑板上贴六张字卡", "房子 · 房间 · 层 · 楼 · 楼上 · 楼下"),
                ("老师说中文，先拍到的得一分", "赢的留下，换下一个同学"),
                ("<b>第二轮</b>：老师不说词，说整句话", "我的房间在<b>楼上</b>。"),
                ("<b>加难</b>：拍到以后要用这个词说一句完整的话", "说不出来不算分，也不能重复别人说过的")],
               "字卡打印两套，A4 大小，用蓝丁胶贴。"))

    add("25-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 一个同学念三条 success criteria，全班说英文意思。",
                "<b>自评</b> · 三条目标，一条一条来：👍 / 😐 / 👎。",
                "<b>出门条</b> · 写在纸条上，出门交。",
                "<b>下节课</b> · 我们上楼，学楼上的房间——还有为什么「卧室」的量词跟「房间」不一样。"],
               cn="出门条：翻译——My house has three storeys. My room is upstairs."))
    return S
