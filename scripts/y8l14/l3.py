# -*- coding: utf-8 -*-
"""Y8 L14 · Lesson 3 of 6 — the kitchen, and 有 vs 在

Source: docs/lesson-plans/y8-l14/03-kitchen-measure-words-mixed.md
Textbook p.132 (Text 1 kitchen half; New Words 9–12), p.134 Act. 3 and 4,
p.135 Act. 6, p.137 Act. 9 (CD 68). Workbook pp.157–158.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_contrast,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_text, s_tickgrid, s_errors, s_title, s_lisc)

SLUG = "l3-kitchen-measure-words"
TITLE = "Y8 L14 · 家具 Furniture · Lesson 3 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='厨房里面有……', en='The kitchen & every measure word',
            desc='The three kitchen words finish Text 1, and then the whole measure-word pool comes back at once — 间 层 辆 张 台 个, grouped by category rather than memorised. 有 and 在 get a slide of their own, because the unit test asks about them twice.',
            words='冰箱 · 烤箱 · 电炉', n=3)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 厨房 The kitchen", "LESSON 3 OF 6", "第十四课 · 家具",
        s_title("厨房里面有什么？", "The Kitchen, and Every Measure Word",
                "Year 8 · Book 2 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 2 · p.132 · p.134 · p.137"))

    add("02-review.html", "Review · Correct the Teacher", REV, "复习 · 改一改",
        s_errors([("洗衣机有厨房里面。", "洗衣机在厨房里面。", "洗衣机是已知的 → 在"),
                  ("我们家的客厅不算大也不小。", "我们家的客厅不大也不小。", "两个说法，选一个，不要合起来"),
                  ("我家有一个空调在客厅。", "客厅里有一个空调。", "地方在前，「有」在后")],
                 "三句里有错 · 两人一组找出来，一组上来改一句",
                 "「有」和「在」这一对二十分钟以后会变成一整个活动，考试也考两次。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what is in a kitchen, and choose the right measure word for "
               "anything in the house.",
               [("I can name three kitchen appliances", "能说出三样厨房电器"),
                ("I can pick the right measure word from 个 间 张 辆 台", "会选量词，不都用「个」"),
                ("I can tell 有 and 在 apart and use each correctly",
                 "分得清「有」和「在」，两个都会用")]))

    # ── Cycle 1 · 冰箱 / 烤箱 ──
    add("04-c1-words.html", "Cycle 1 · A — 冰箱 / 烤箱", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("冰箱", "bīngxiāng", "refrigerator", "bingxiang"),
                ("烤箱", "kǎoxiāng", "oven", "kaoxiang")))
    add("05-c1-note.html", "两个「箱」— an ice-box and a roasting-box", IDO,
        "生词 1 · 同一个字",
        s_figure("bingxiang", "冰箱　烤箱　—　后面是同一个字",
                 ["<b>箱</b>　xiāng　=　箱子，装东西的盒子。",
                  "<b>冰</b>　bīng　=　冰。冰 + 箱 = 装冰的箱子 = 冰箱。",
                  "<b>烤</b>　kǎo　=　烤。烤 + 箱 = 烤东西的箱子 = 烤箱。",
                  "两个词一起记，比分开记快一半。"],
                 cn="厨房里面有一个冰箱和一个烤箱。"))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("厨房里面有一个<b>冰箱</b>。", "Inside the kitchen there's a fridge."),
                    ("我家的<b>烤箱</b>很大。", "Our oven is big."),
                    ("<b>冰箱</b>在<b>烤箱</b>左面。", "The fridge is to the left of the oven.", True)],
                   "你家有没有烤箱？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家的厨房里面有 ________ 。"],
                "两样都说，还要说它们跟别的东西在哪边："
                "<b>冰箱在洗衣机右面，烤箱在冰箱下面。</b>　再用「可是」说你家没有的那一样。"))

    # ── Cycle 2 · 电炉 ──
    add("08-c2-words.html", "Cycle 2 · A — 电炉", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("电炉（電爐）", "diànlú", "electric stove", "dianlu")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("厨房里有一个<b>电炉</b>。", "There's an electric stove in the kitchen."),
                    ("我们家的<b>电炉</b>不大也不小。", "Our stove is neither big nor small."),
                    ("厨房里面有冰箱、烤箱和一个<b>电炉</b>。",
                     "Inside the kitchen there's a fridge, an oven and a stove.", True)],
                   "电炉在厨房里面还是外面？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["厨房里面有 ________ 和一个电炉。"],
                "把课文里厨房那一句默写出来，再改成<b>你们家</b>的——"
                "没有的东西要用「可是」或者「没有」说出来，不要偷偷不说。"))

    add("11-recall.html", "Recall · ten characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["沙发", "茶几", "电视柜", "张", "空调",
                  "洗衣机", "里面", "冰箱", "烤箱", "电炉"],
                 "十个了。读不出来就停下来重教——不要往下走。", cols=5))

    # ── 有 / 在 ──
    add("12-contrast.html", "有 vs 在 — the spine of the unit", IDO, "句型 · 有 还是 在",
        s_contrast(("有", "there is / there are", "地方 + 有 + 东西", "厨房里有一个冰箱。"),
                   ("在", "is located at", "东西 + 在 + 地方", "冰箱在厨房里。"),
                   "两句说的是同一件事，只是从哪一头开始说。"
                   "<b>新的东西 → 有。已知的东西找地方 → 在。</b>"))
    add("13-pattern.html", "Pattern · 有 / 在", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 同样两样东西，两种说法",
                  "地方 + 有 + 东西　／　东西 + 在 + 地方",
                  [("厨房里<b>有</b>一个冰箱。", "有 brings something new into a place you already know."),
                   ("冰箱<b>在</b>厨房里。", "在 tells you where a thing you already know sits."),
                   ("客厅里<b>有</b>一张沙发；沙发<b>在</b>电视柜前面。",
                    "Both, back to back, with the same two objects.")]))
    add("14-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("四个小句，「有」和「在」轮流用",
                "我们家的房子有两层，楼下有厨房和客厅，我的房间在楼上，房间里面有一张床。",
                "Our house has two storeys; downstairs there's the kitchen and the "
                "living room; my room is upstairs; inside my room there's a bed.",
                "有 · 有 · 在 · 有 —— 第三个换成「在」，因为「我的房间」已经说过了。"))

    add("15-text.html", "Text 1 · p.132 complete — no blanks left", IDO, "课文一 · CD 66",
        s_text("课文一 · 课本 p.132 · 全班齐读",
               "我们家的客厅不算大。客厅里有一张三人沙发、一个茶几、一个电视柜和一个空调"
               "（冷气机）。我们家的厨房不大也不小，里面有<b>冰箱</b>、洗衣机、<b>烤箱</b>"
               "和<b>电炉</b>。",
               "他们家的厨房里有几样东西？",
               "上节课那三个空，今天填满了。", size=22))

    add("16-listening.html", "Listening · p.137 Ex.9 (CD 68)", IDO, "听力 · CD 68",
        s_tickgrid(["沙发", "电视", "电视柜", "茶几", "空调"],
                   ["第一段 · 客厅"],
                   "听力 · 课本 p.137 第 9 题 · 听两遍，有的打钩",
                   "第二段说的是厨房：冰箱 · 电话 · 电炉 · 烤箱 · 洗衣机。"
                   "<b>他最后说「可是我们没有烤箱」——谁听到了？</b>"))

    add("17-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「冰」和「烤」各是什么意思？", "两个词后面是同一个字"),
               ("有 还是 在？　厨房里 ____ 一个电炉。", "写在小白板上"),
               ("有 还是 在？　洗衣机 ____ 厨房里面。", "写在小白板上"),
               ("「洗衣机」的量词是什么？", "不是「个」——是机器用的那个"),
               ("他们家有没有烤箱？", "刚才听力里说了")]))

    # ── Practice ──
    add("18-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("沙发", "shafa"), ("茶几", "chaji"), ("电视柜", "dianshigui"),
                   ("张", None), ("空调", "kongtiao"), ("洗衣机", "xiyiji"),
                   ("里面", "limian"), ("冰箱", "bingxiang"), ("烤箱", "kaoxiang"),
                   ("电炉", "dianlu")],
                  "十个词，全在这儿。这一页留在屏幕上，后面三个活动都看它。", dense=True))

    add("19-act1.html", "Activity 1 · Finish the kitchen (7 min)", PRAC,
        "活动一 · 7 分钟",
        s_figure("chufang", "活动一 · 厨房写完，再写你自己的",
                 ["<b>甲 · 3 分钟</b>　只看图，把课文里厨房那一句完整写出来。",
                  "<b>乙 · 4 分钟</b>　改成写你们家的厨房。",
                  "规矩：总览页上<b>十个词全部</b>要出现——所以客厅那几个",
                  "得另外写一句放进去。一共四到五句。",
                  "写完请两个同学念——总览页还在屏幕上。"],
                 cn="我们家的厨房不大也不小，里面有冰箱、洗衣机、烤箱和电炉。"))
    add("20-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["写<b>两个</b>厨房：你们家的，和一个你知道的（亲戚家、度假的房子、学校食堂）。",
                "十个词还是全部都要出现，用「可是」和「也」连起来。",
                "不看总览页。"],
               cn="我们家的厨房不大也不小，里面有冰箱和电炉，可是没有烤箱；"
                  "我奶奶家的厨房特别大……"))

    add("21-act2.html", "Activity 2 · p.134 Ex.3 measure words (We Do, 6 min)", PRAC,
        "活动二 · 量词 · We Do · 6 分钟",
        s_list("活动二 · 量词归类（课本 p.134 第 3 题 · 十六个空）",
               [("<b>间</b>　房间", "卧室 · 书房 · 浴室 · 洗手间"),
                ("<b>层</b>　楼层", "这个房子有三层"),
                ("<b>辆</b>　车", "两辆车"),
                ("<b>张</b>　平的东西", "沙发 · 床 · 书桌 · 纸"),
                ("<b>台</b>　机器", "电视 · 电脑 · 洗衣机"),
                ("<b>个</b>　其他", "茶几 · 电视柜 · 冰箱 · 花园 · 车库")],
               "老师念，全班写，数三下一起举。举起来以后老师才说答案。"
               "全班对的不到七成就停下来，同一类再来两个。", compact=True))
    add("22-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难",
               ["不要填空——<b>写规律</b>。每一个量词写出它管的是哪一类，"
                "再各举两个词，其中至少一个不在题目上。",
                "然后找出题目里<b>可以配两个量词</b>的那两个词，说说差别在哪儿。"],
               cn="张 = 平的、有面的东西：一张沙发、一张地图。"))

    add("23-act3.html", "Activity 3 · p.134 Ex.4 有／在 translation (You Do, 5 min)", PRAC,
        "活动三 · 翻译 · You Do · 5 分钟",
        s_task("活动三 · 课本 p.134 第 4 题 · 九句，英译中",
               ["安静，自己做，写在纸上。",
                "每一句旁边写一个字：<b>有</b> 或者 <b>在</b>——标出你用的是哪条规律。",
                "做完全班一起对，自己改自己的。"],
               ext="做完九句，自己再写<b>三句英文</b>，要故意设陷阱，"
                   "让同学容易选错「有」还是「在」。跟同伴交换，互相批改。"))

    add("24-strokes.html", "Characters · 冰 箱 烤 炉 (Workbook pp.157–158)", PRAC,
        "写汉字 · 练习册 p.157",
        s_strokes([("冰", 6, "左边两点水，不是三点水"),
                   ("箱", 15, "竹字头，下面「相」——笔画多，慢慢来"),
                   ("烤", 10, "左边火字旁，右边「考」"),
                   ("炉", 8, "左边火字旁，右边「户」")],
                  "笔顺 · 每个字写三遍",
                  "「冰」是两点水，「洗」是三点水——这两个今天都在屏幕上，正好比一比。"))

    add("25-game.html", "Game · p.135 Ex.6 whole-class knockout (5 min)", PRAC,
        "游戏 · 说不出来就坐下 · 5 分钟",
        s_list("游戏 · 课本 p.135 第 6 题 · 全班站起来",
               [("老师说一个英文词，点到谁，谁用中文说出来", "第十三课和第十四课的词都可以"),
                ("说错，或者三秒说不出来，坐下", "最后还站着的三个人赢"),
                ("<b>加难</b>：剩下不到八个人的时候换规则——", "老师说<b>量词</b>，学生要给一个配得上的词"),
                ("而且要用它说一句完整的话，一个词全场只能用一次", "「一张……」→ 一张沙发，客厅里有一张沙发。")],
               "不用准备任何东西——老师看总览页和第十三课的房间表就行。", compact=True))

    add("26-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 全班齐读三条。",
                "<b>自评</b> · 一条一条举大拇指。第三条要特别看——"
                "「有／在」如果还不稳，下节课的复习就从它开始。",
                "<b>出门条</b> · 两题，写在同一张纸条上。",
                "<b>下节课</b> · 离开大家共用的房间，进你自己的卧室——"
                "书桌、椅子，还有一个几乎只给椅子用的量词。"],
               cn="出门条：① 厨房里有什么？一句话，三样东西。　② 「洗衣机」的量词。"))
    return S
