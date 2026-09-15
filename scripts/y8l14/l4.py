# -*- coding: utf-8 -*-
"""Y8 L14 · Lesson 4 of 6 — your own room, and 把 for chairs

Source: docs/lesson-plans/y8-l14/04-my-own-room-mixed.md
Textbook p.138 (Text 2, first half; New Words 1–3), p.139 Act. 12 and 13.
Workbook pp.160–161 (copy 桌 把 椅).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_dialogue, s_title, s_lisc)

SLUG = "l4-my-own-room"
TITLE = "Y8 L14 · 家具 Furniture · Lesson 4 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='我的房间里有……', en='Your own room',
            desc='Out of the shared rooms and into the bedroom. 椅子 and 把 are taught together on purpose — the measure word is worth nothing on its own, and a chair without it is where the test mark goes.',
            words='椅子 · 把 · 书桌', n=3)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我的房间 My own room", "LESSON 4 OF 6", "第十四课 · 家具",
        s_title("我的房间里有什么？", "Your Own Room",
                "Year 8 · Book 2 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 2 · p.138 · p.139"))

    add("02-review.html", "Review · 有／在 and the measure words", REV, "复习 · 第三节课",
        s_list("小白板 · 六题 · 老师说英文，写中文，举起来",
               [("<i>There is a fridge in the kitchen.</i>", "厨房里有一个冰箱。"),
                ("<i>The fridge is in the kitchen.</i>", "冰箱在厨房里。"),
                ("<i>one washing machine</i>", "量词是「台」"),
                ("<i>three bedrooms</i>", "量词是「间」"),
                ("<i>two cars</i>", "量词是「辆」"),
                ("<i>Our living room is not that big.</i>", "我们家的客厅不算大。")],
               "第一题和第二题并排贴在黑板上，「有」「在」各圈起来，"
               "问全班规律是什么：<b>新的东西 → 有；已知的东西找地方 → 在。</b>",
               compact=True))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("describe the furniture in our own bedroom and say exactly where "
               "each piece is.",
               [("I can name a desk and a chair in Chinese", "能说出书桌和椅子"),
                ("I can use 把 for chairs and 张 for desks and beds", "会说「一把椅子」「一张书桌」"),
                ("I can say where one thing is relative to another",
                 "能说「电脑在书桌上面」")]))

    # ── Cycle 1 · 椅子 / 把 ──
    add("04-c1-words.html", "Cycle 1 · A — 椅子 / 把", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("椅子", "yǐzi", "chair", "yizi"),
                ("把", "bǎ", "measure word · chairs", "ba")))
    add("05-c1-note.html", "把 exists for chairs, and almost nothing else", IDO,
        "生词 1 · 为什么一起学",
        s_figure("ba", "一把椅子 · 两把椅子 · 三把椅子",
                 ["<b>把</b> 是给椅子用的量词。",
                  "它还能用在刀、伞上面——除此之外你几乎用不到它。",
                  "所以不要单独记「把」：跟「椅子」一起记，一辈子都不会分开。",
                  "反过来说，说「椅子」的时候忘了「把」，考试就在这里扣分。"],
                 cn="我的房间里有一把椅子。"))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("<b>椅子</b>在电视前面。", "The chair is in front of the TV."),
                    ("我的房间里有一<b>把椅子</b>。", "There's a chair in my room."),
                    ("餐厅里有六<b>把椅子</b>。", "There are six chairs in the dining room.", True)],
                   "你们家的餐厅里有几把椅子？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我的房间里有 ________ 把椅子。"],
                "一句话数三个房间的椅子，再说哪个房间最多："
                "<b>客厅里有两把椅子，餐厅里有六把，我的房间里有一把。</b>"))

    # ── Cycle 2 · 书桌 ──
    add("08-c2-words.html", "Cycle 2 · A — 书桌", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("书桌（書桌）", "shūzhuō", "desk", "shuzhuo")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我的房间里有一张<b>书桌</b>。", "There's a desk in my room."),
                    ("电脑在我的<b>书桌</b>上。", "The computer is on my desk."),
                    ("<b>书桌</b>前面有一把椅子。", "In front of the desk is a chair.", True)],
                   "你的电脑在哪儿？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我的书桌上有 ________ 。"],
                "书桌上下四样东西，一句话说完，每一样都说在上一样的哪边："
                "<b>我的书桌上有电脑，电脑前面有书，书桌下面有一个书包。</b>"))

    add("11-recall.html", "Recall · thirteen characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["沙发", "茶几", "电视柜", "张", "空调", "洗衣机", "里面",
                  "冰箱", "烤箱", "电炉", "椅子", "把", "书桌"],
                 "十三个了。读不出来就停下来重教。", cols=5))

    # ── The pattern ──
    add("12-pattern.html", "Pattern · A 在 B 上面／前面", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说得更准——不只是「在房间里」",
                  "东西 A + 在 + 东西 B + 上面／前面／左面／右面／下面",
                  [("电脑<b>在</b>书桌<b>上面</b>。", "On top of — 书桌上 and 书桌上面 are both fine."),
                   ("椅子<b>在</b>书桌<b>前面</b>。", "In front of."),
                   ("我的床<b>在</b>房间<b>里面</b>，书桌<b>在</b>床<b>的</b>左面。",
                    "With a possessor in front, 的 goes in: 床的左面.")],
                  "上一课说东西在哪个<b>房间</b>，这一课说东西在哪样<b>东西</b>旁边。"))
    add("13-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("一个「有」开头，三个「在」跟着",
                "我的房间不算大，里面有一张床和一张书桌；电脑在书桌上面，椅子在书桌前面。",
                "My room isn't that big; inside there's a bed and a desk; the computer "
                "is on the desk, and the chair is in front of the desk.",
                "先用「有」把东西请进来，再用「在」一样一样摆好——顺序不能反过来。"))

    add("14-text.html", "Text 2 · p.138 (first half)", IDO, "课文二 · CD 69",
        s_dialogue("课文二 · 课本 p.138 · 两人读，再换角色",
                   [("A", "你的房间里有什么？"),
                    ("B", "有一张床、一张<b>书桌</b>和一<b>把椅子</b>。"),
                    ("A", "你的房间里有电脑吗？"),
                    ("B", "有，在我的<b>书桌</b>上。")],
                   "CD 69 放到 B 第二次回答就停——完整版里还有两个词，下节课学。"
                   "<b>用中文回答：他的电脑在哪儿？</b>"))

    add("15-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「椅子」的量词是什么？　「书桌」呢？　「床」呢？", "全班一起说，一个一个来"),
               ("翻译：<i>there are two chairs in my room</i>", "写在小白板上"),
               ("这句话对不对？　我的电脑在书桌。", "少了什么？"),
               ("你的房间里有什么？", "点三个同学，一人说一样，要带量词，不许重复")]))

    # ── Practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("沙发", "shafa"), ("茶几", "chaji"), ("电视柜", "dianshigui"),
                   ("张", None), ("空调", "kongtiao"), ("洗衣机", "xiyiji"),
                   ("里面", "limian"), ("冰箱", "bingxiang"), ("烤箱", "kaoxiang"),
                   ("电炉", "dianlu"), ("椅子", "yizi"), ("把", None),
                   ("书桌", "shuzhuo")],
                  "十三个词。这一页留在屏幕上——后面三个活动都看它。", dense=True))

    add("17-act1.html", "Activity 1 · Draw and label your bedroom (9 min)", PRAC,
        "活动一 · 9 分钟",
        s_figure("chuang", "活动一 · 画你的卧室，一样家具一句话",
                 ["<b>老师先画 · 90 秒</b>　黑板上画个房间，放三样东西，"
                  "全班说一句，老师写一句。",
                  "<b>再自己画 · 5 分钟</b>　发纸，画你自己的卧室。",
                  "<b>至少五句</b>，每句一样家具，量词一定要对。",
                  "<b>最后一句必须用「在」</b>加方位词，不能用「有」。"],
                 cn="我的房间里有一张床。书桌在床的左面。"))
    add("18-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["不写你现在的房间——写一个<b>你想要的</b>房间，只能放六样东西。",
                "写成一段话，不是一条一条：开头说大小（不算大／不大也不小），"
                "每一样都用「在」摆在另一样旁边，",
                "总览页上凡是卧室里放得下的词，全部要用上，",
                "最后一句说<b>为什么</b>这样摆。不看总览页。"],
               cn="因为我喜欢看书，所以书桌在窗户前面。"))

    add("19-act2.html", "Activity 2 · p.139 Ex.13 measure-word naming (We Do, 5 min)", PRAC,
        "活动二 · 量词快问 · 5 分钟",
        s_list("活动二 · 课本 p.139 第 13 题 · 十三张图，每组一份",
               [("A 指一张图，B 说出来——<b>一定要带量词</b>", "「一把椅子」，不是「椅子」"),
                ("量词错了，A 就再指同一张", "走完一轮，换人，第二轮快一点"),
                ("<b>全班</b>：老师指，全班一起说", "犹豫的那几个词写到黑板上"),
                ("<b>加难</b>：说出东西、量词，再说它属于哪个房间", "而且房间不能连着重复两次")],
               "图纸每两人一份，提前印好。", compact=True))

    add("20-act3.html", "Activity 3 · p.139 Ex.12 六句 (You Do, 5 min)", PRAC,
        "活动三 · 写六句 · You Do · 5 分钟",
        s_task("活动三 · 课本 p.139 第 12 题",
               ["安静，自己写，写在本子上。",
                "<b>三句用「有」，三句用「在」。</b>",
                "六句都要是<b>你家真的是这样</b>的。",
                "每句把「有」或者「在」画一条线。"],
               ext="六句要<b>连成一串</b>：每一句都得接上一句里出现过的一样东西，"
                   "读起来像走过你家一圈，不是六件互不相干的事。"))

    add("21-strokes.html", "Characters · 桌 把 椅 (Workbook pp.160–161)", PRAC,
        "写汉字 · 练习册 p.160",
        s_strokes([("桌", 10, "上面「⺊」和「日」，下面「木」"),
                   ("把", 7, "左边提手旁，右边「巴」"),
                   ("椅", 12, "左边木，右边「奇」——椅子是木头做的")],
                  "笔顺 · 每个字写三遍",
                  "「椅」和「桌」都有木字旁，因为都是木头做的——这是<b>词</b>的道理，"
                  "不是部首练习，不用背部首表。"))

    add("22-game.html", "Game · 20 Questions — the hidden room (4 min)", PRAC,
        "游戏 · 猜房间 · 4 分钟",
        s_list("游戏 · 20 Questions · 猜他想的是哪个房间",
               [("一个同学心里想一个自己家的房间，不说出来", "全班提问，只能用中文"),
                ("问题要能用「有／没有」回答，最多二十个", "房间里有沙发吗？ 床在房间里面吗？ 房间大不大？"),
                ("猜中就换人，玩两三轮", ""),
                ("<b>加难</b>：回答的人<b>不能说「有」也不能说「没有」</b>",
                 "每次都要说一整句，给一点新消息，又不能直接说出是哪个房间")],
               "什么都不用准备。", compact=True))

    add("23-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 一个同学念三条。",
                "<b>自评</b> · 小白板，三条一起举：👍 / 😐 / 👎。",
                "<b>出门条</b> · 一句话，量词写错不算数。",
                "<b>下节课</b> · 衣柜和书架把房间写完——"
                "然后一个新的问句，把「吗」整个去掉。"],
               cn="出门条：我的房间里有一张书桌和一把椅子。"))
    return S
