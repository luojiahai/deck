# -*- coding: utf-8 -*-
"""Y8 L13 · Lesson 4 of 6 — where things are: the six position words

Source: docs/lesson-plans/y8-l13/04-position-words-mixed.md
Textbook p.124 Act. 3 + the 在/有 NOTE, p.128 Act. 8 (Extra Words).
Workbook p.147 Ex. 7, p.151 Ex. 14 and Ex. 15.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_contrast,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_title, s_lisc)

SLUG = "l4-position-words"
TITLE = "Y8 L13 · 房子 House · Lesson 4 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

# Card shown on the series landing page (index/designs/y8-l13/index.html),
# written by build.py. Lives beside the lesson it describes.
CARD = dict(cn='在哪儿', en='Position words',
            desc='Six words in three cycles — the heaviest vocabulary load in the sequence. TPR first, then the p.124 cluttered room, then the nine pictures of p.128 written alone.',
            words='上面 · 下面 · 里面 · 外面 · 左面 · 右面', n=6)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 在哪儿 Where things are", "LESSON 4 OF 6", "第十三课 · 房子",
        s_title("在哪儿？", "Where Things Are · Position Words",
                "Year 8 · Book 2 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 2 · pp.124, 128"))

    add("02-review.html", "Review · Slap the Board, thirteen rooms", REV, "复习 · Lessons 1–3",
        s_recall(["房子", "房间", "卧室", "书房", "浴室", "洗手间",
                  "客厅", "餐厅", "厨房", "楼上", "楼下", "层"],
                 "两个同学上来拍字。老师不说单词——说整句话，要从句子里听出那个词。",
                 cols=6, head="拍字 Slap the Board · 十二个词"))
    add("03-review-wb.html", "Review · 有 or 在", REV, "复习 · 小白板",
        s_list("三题 · 小白板 · 写完整句",
               [("有 还是 在？ 楼下 ____ 客厅和餐厅。", ""),
                ("有 还是 在？ 我的卧室 ____ 楼上。", ""),
                ("翻译：<i>The kitchen is downstairs.</i>", "厨房在楼下。")],
               "到今天为止，「在」只告诉我们<b>哪一层</b>。今天它要变精确。", compact=True))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say exactly where something is, using position words with 在 and 有.",
               [("I can use the six position words", "能用六个方位词"),
                ("I can say where a thing is with 在", "能用「在」说东西在哪儿"),
                ("I can say what is in a place with 有", "能用「有」说一个地方有什么")]))

    # ── Cycle 1 · 上面 / 下面 ──
    add("05-c1-words.html", "Cycle 1 · A — 上面 / 下面", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("上面", "shàngmiàn", "above; on top", "shangmian"),
                ("下面", "xiàmiàn", "below; underneath", "xiamian")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我的房间在客厅<b>上面</b>。", "My room is above the living room."),
                    ("厨房在卧室<b>下面</b>。", "The kitchen is below the bedroom."),
                    ("我的房间在<b>上面</b>，厨房在<b>下面</b>。",
                     "My room is above, the kitchen is below.", True)],
                   "你的房间在什么上面？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 在 ________ 上面。", "________ 在 ________ 下面。"],
                "两个房间都不可以是你的卧室，而且要说出各在几楼："
                "<b>我家的餐厅在厨房下面，餐厅在一楼，厨房在二楼。</b>"))

    # ── Cycle 2 · 里面 / 外面 ──
    add("08-c2-words.html", "Cycle 2 · A — 里面 / 外面", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("里面", "lǐmiàn", "inside", "limian"),
                ("外面", "wàimiàn", "outside", "waimian")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我在房子<b>里面</b>。", "I'm inside the house."),
                    ("我家的车在房子<b>外面</b>。", "Our car is outside the house."),
                    ("妈妈在房子<b>里面</b>，爸爸在房子<b>外面</b>。",
                     "Mum's inside, Dad's outside.", True)],
                   "现在你在房子里面还是外面？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["________ 在房子里面，________ 在房子外面。"],
                "说三个人，每个人还要在做一件事："
                "<b>我妈妈在厨房里面做饭，我弟弟在客厅里面看电视，我爸爸在外面。</b>"))

    # ── Cycle 3 · 左面 / 右面 ──
    add("11-c3-words.html", "Cycle 3 · A — 左面 / 右面", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("左面", "zuǒmiàn", "left", "zuomian"),
                ("右面", "yòumiàn", "right", "youmian")))
    add("12-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([("厨房在客厅<b>左面</b>。", "The kitchen is to the left of the living room."),
                    ("餐厅在客厅<b>右面</b>。", "The dining room is to the right of the living room."),
                    ("客厅的<b>左面</b>是厨房，<b>右面</b>是餐厅。",
                     "To the left of the living room is the kitchen, to the right is the dining room.", True)],
                   "你的左面坐着谁？"))
    add("13-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["________ 在 ________ 左面。", "________ 在 ________ 右面。"],
                "用一句话说你的卧室在另外两个房间中间（左面……右面……），"
                "然后<b>反过来再说一次</b>——如果 A 在 B 的左面，那 B 在 A 的哪一面？"))

    add("14-recall.html", "Recall · six characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["上面", "下面", "里面", "外面", "左面", "右面"],
                 "读两遍：第一遍老师说中文，第二遍老师说英文，你们说中文。"))

    # ── Pattern ──
    add("15-contrast.html", "在 / 有, now with position words", IDO, "句型 · 课本 p.124 NOTE",
        s_contrast(("在", "thing → place", "东西 + 在 + 地方 + 面", "电视在客厅里面。"),
                   ("有", "place → thing", "地方 + 面 + 有 + 东西", "客厅里面有电视。"),
                   "这两句说的是<b>同一件事</b>。差别只在你从哪一头开始说。"))
    add("16-pattern.html", "Pattern · 地方 + 面", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 六个方位词，一个用法",
                  "东西 + 在 + 地方 + 面",
                  [("电视<b>在</b>客厅里面。", "The TV is in the living room."),
                   ("客厅里面<b>有</b>电视。", "In the living room there is a TV — same facts, other end."),
                   ("我的书房<b>在</b>卧室右面。", "My study is to the right of the bedroom.")],
                  "方位词不能省。✗ 我的书在桌子 —— 要说 <b>桌子上面</b>。"))
    add("17-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("三个小句，中间那句用「是」",
                "我的卧室在楼上，卧室左面是浴室，右面有一个小书房。",
                "My bedroom is upstairs; to the left of it is the bathroom; "
                "to the right there's a small study.",
                "地方放在前面的时候，中国人常常说<b>「是」</b>，不说「在」——"
                "「卧室左面<b>是</b>浴室」。"))

    add("18-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("我说方位词，你们指——上面……外面……左面……", "用手指，不要说话"),
               ("在 还是 有？ 客厅里面 ____ 电视。", "写在小白板上"),
               ("在 还是 有？ 电视 ____ 客厅里面。", "写在小白板上"),
               ("怎么说 inside？ outside？ underneath？", "写汉字"),
               ("这句话少了什么？ ✗ 我的书在桌子。", "补上那个词")]))

    # ── Practice ──
    add("19-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("上面", "shangmian"), ("下面", "xiamian"), ("里面", "limian"),
                   ("外面", "waimian"), ("左面", "zuomian"), ("右面", "youmian")],
                  "这一页整节课留在屏幕上。"))

    add("20-act1.html", "Activity 1 · TPR, then describe the room (We Do, 8 min)", PRAC,
        "活动一 · We Do · 8 分钟",
        s_task("活动一 · 先动起来，再看图说话",
               ["<b>先用真东西</b>　书放在椅子上、椅子下、书包里、门外面。每次问：<b>书在哪儿？</b> 全班一起答。",
                "然后叫一个同学上来，老师只用中文说：<b>把书放在椅子下面。</b> 五六轮，越来越快。",
                "<b>再看课本 p.124 第 3 题</b>　那张乱七八糟的房间图，点名一人一句。",
                "图上的家具只认不写：沙发 · 椅子 · 书架 · 杯子 · 牙刷 · 相框 · 咖啡桌。"],
               cn="电视机在地上。　书在书架里面。　杯子在咖啡桌上面。"))
    add("21-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["图上东西超过十二样——写成一段话，不要写成清单。"],
               "至少六句，<b>六个方位词一个都不能重复</b>，其中两句要用「还有」或者「可是」连起来。"
               "写完把眼睛闭上，同桌问你：<b>相框在哪儿？牙刷呢？</b>"))

    add("22-act2.html", "Activity 2 · Nine pictures (You Do, 10 min)", PRAC,
        "活动二 · You Do · 10 分钟 · 课本 p.128 第 8 题",
        s_list("活动二 · 九张图，把句子补完整 · 先自己安静写",
               [("蔬菜在 <u>　餐桌上面　</u> 。", "例子"), ("牛仔裤在 ________ 。", ""),
                ("汽车在 ________ 。", ""), ("厨房在 ________ 。", ""),
                ("水彩画儿在 ________ 。", ""), ("书房在 ________ 。", ""),
                ("校车在 ________ 。", ""), ("杂志在 ________ 。", ""),
                ("花园在 ________ 。", "")],
               "写完跟同桌对一对，然后念三句出来。", compact=True))
    add("23-act2-wb.html", "Activity 2 · Workbook p.151 Ex.14", PRAC, "活动二 · 练习册 p.151",
        s_task("练习册 p.151 第 14 题 · 句型反过来了",
               ["p.128 是「东西 + 在 + 地方」，这一题是「<b>地方 + 有 + 东西</b>」。",
                "中间要换句型——这就是这两题放在一起做的原因。"],
               "不看印出来的那张纸，只看投影，每一题写<b>两遍</b>——"
               "一遍用「在」，一遍用「有」（汽车在车库里面。／ 车库里面有汽车。）"
               "写完直接做 <b>p.151 第 15 题</b>，六句英译中，不给词库。",
               cn="钢琴上面有 ________ 。　钢琴的下面有 ________ 。"))

    add("24-wb-opposites.html", "Workbook p.147 Ex.7 · opposites (2 min)", PRAC,
        "练习册 · p.147 第 7 题",
        s_task("练习册 p.147 第 7 题 · 反义词 · 两分钟写完",
               ["十二个，写反义词。四个跟方位有关，所以放在今天。",
                "单元测验里有一模一样的题型。"],
               cn="大 → 小　高 → ____　黑 → ____　短 → ____　这 → ____　热 → ____　"
                  "买 → ____　对 → ____　左 → ____　东 → ____　北 → ____　多 → ____"))

    add("25-game.html", "Game · 老师说 Simon Says (5 min)", PRAC, "游戏 · 老师说 · 5 分钟",
        s_list("游戏 · 老师说 Simon Says · 方位词版",
               [("全班站起来，指令只用中文", "老师说：把手放在头上面。"),
                ("没有「老师说」三个字就照做的，坐下", "把书放在桌子下面。（陷阱）"),
                ("越说越快，三四分钟", "老师说：站在椅子右面。"),
                ("<b>加难</b>：最后站着的三个人轮流当老师", "每人说五条，方位词不能重复")],
               "不用道具——用桌上现成的东西。"))

    add("26-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 问一句：六个词里哪个最难记？（多半是里面／外面）",
                "<b>自评</b> · 小白板写 👍 / 😐 / 👎，三条一起举。",
                "<b>出门条</b> · 同一件事要写两遍。",
                "<b>下节课</b> · 我们走出大门——花园、车库，还有你家住什么样的房子。"],
               cn="出门条：用一个方位词写一句关于这间教室的话，"
                  "然后同一件事从<b>地方</b>开头再写一遍。"))
    return S
