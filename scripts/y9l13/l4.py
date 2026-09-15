# -*- coding: utf-8 -*-
"""Y9 L13 · Lesson 4 of 6 — 咖啡馆 / 过 / 一直 / 往前 / 红绿灯 + 先……然后……

Source: docs/lesson-plans/y9-l13/04-directions-basics-mixed.md
Textbook p.127 Text 2 dialogues 1–2 (CD 51), p.128 Act. 7, p.129 Act. 8
and Act. 9. Workbook p.147 Ex. 8 is the review cloze.

Five new words, so three cycles — the third carries one word plus the
recall board, which is where the teacher finds out whether to push on.
"""
from build import (s_words, s_word_one, s_examples, s_write, s_recall,
                   s_summary, s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_dialogue, s_arrows, s_route, s_title, s_lisc, label)

SLUG = "l4-directions"
TITLE = "Y9 L13 · 社区 Neighbourhood · Lesson 4 of 6"
CARD = (SLUG, "请问，怎么走？", "Asking the Way · 先……然后……",
        "speaking", "咖啡馆 · 过 · 一直 · 往前 · 红绿灯。第一次给路线——两步，用「先……然后……」连起来。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 请问，怎么走？", "LESSON 4 OF 6", "第十三课 · 社区",
        s_title("请问，怎么走？", "Asking the Way",
                "Year 9 · Book 3 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 3 · pp.127–129 · 课文二"))

    add("02-review.html", "Review · 地图 + 填空", REV, "复习 · Lessons 1–3",
        s_task("复习 · 两部分",
               ["<b>（甲）说地图，五分钟</b> · 拿出上节课画的社区地图。"
                "A 对 B 说六十秒，不停；B 听完问一个问题。然后换。取三位上台说。",
                "<b>（乙）填空，三分钟</b> · 练习册 p.147 第 8 题，白板作答。",
                "词库：船 · 中间 · 后面 · 方便 · 附近 · 前面 · 有 · 离 · 上边"],
               cn="小明家住在一个离岛上，生活不太＿＿。他们家＿＿没有超级市场，"
                  "要去超级市场得坐二十分钟的＿＿。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("ask for directions politely and give a simple two-step route.",
               [("I can ask 请问，……在哪儿？and 请问，去……怎么走？",
                 "能有礼貌地问路"),
                ("I can say 过马路 and 一直往前走", "能说「过马路」「一直往前走」"),
                ("I can join two steps with 先……，然后……",
                 "能用「先……，然后……」把两步连起来")]))

    # ── Cycle 1 · 咖啡馆 / 过 ──
    add("04-c1-words.html", "Cycle 1 · A — 咖啡馆 / 过", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("咖啡馆", "kāfēiguǎn", "café", "kafeiguan"),
                ("过", "guò", "cross", "guomalu")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "<b>咖啡馆</b>就在银行对面。",
                     "The café is right opposite the bank."),
                    (None, "你先<b>过</b>马路。", "First cross the road."),
                    (None, "<b>过</b>马路，<b>咖啡馆</b>就在你的左边。",
                     "Cross the road and the café is on your left.", True)],
                   "咖啡馆在哪儿？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["咖啡馆在 ________ 。", "你先过 ________ 。"],
                "写一问一答：一个人问咖啡馆在哪儿，另一个人回答，"
                "答句里要有<b>位置</b>，还要有<b>要走几分钟</b>。"))

    # ── Cycle 2 · 一直 / 往前 ──
    add("07-c2-words.html", "Cycle 2 · A — 一直 / 往前", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("一直", "yì zhí", "straight", "yizhi"),
                ("往前", "wǎng qián", "forward", "wangqian")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "你<b>一直</b>走。", "Keep going straight."),
                    (None, "请<b>往前</b>走。", "Please walk forward."),
                    (None, "你<b>一直</b><b>往前</b>走，五分钟就到了。",
                     "Keep walking straight ahead — five minutes and you're there.", True)],
                   "「一直往前走」是什么意思？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["你一直 ________ 走。", "________ 往前走，就到了。"],
                "同一句指路，说两遍——一遍对朋友说，一遍有礼貌地对陌生人说。"
                "哪里不一样？（请问 · 请 · 您）"))

    # ── Cycle 3 · 红绿灯 ──
    add("10-c3-words.html", "Cycle 3 · A — 红绿灯", IDO, "生词 3 · Cycle 3 of 3",
        s_word_one(("红绿灯", "hóng lǜ dēng", "traffic lights", "honglvdeng")))
    add("11-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "前面有<b>红绿灯</b>。", "There are traffic lights ahead."),
                    (None, "你看到<b>红绿灯</b>就过马路。",
                     "When you see the lights, cross the road."),
                    (None, "一直往前走，看到<b>红绿灯</b>，咖啡馆就在对面。",
                     "Go straight, and at the lights the café is opposite.", True)],
                   "红绿灯——中文按<b>颜色</b>叫它，英文按<b>用途</b>叫它。"))
    add("12-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["看到红绿灯，________ 。"],
                "用「先……，然后……」把<b>三个</b>动作连起来："
                "<b>先过马路，然后一直往前走，看到红绿灯就到了。</b>"))

    add("13-recall.html", "Recall · 五个生词", IDO, "认一认 · Checkpoint",
        s_recall(["咖啡馆", "过", "一直", "往前", "红绿灯"],
                 "卡住就回去重教——后面两课全都建在这五个词上。", cols=5))

    # ── Pattern ──
    add("14-pattern.html", "Pattern · 先……，然后……", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 一条路线是一个顺序",
                  "先 + 动作一 ，然后 + 动作二",
                  [("你先过马路。", "First cross the road."),
                   ("你先过马路，然后一直往前走。",
                    "First cross the road, then keep going straight."),
                   ("你一直往前走，看到红绿灯就过马路。",
                    "Go straight, and cross when you see the lights.")],
                  "顺序照<b>真的走</b>的顺序说。先＝first，然后＝then。"))
    add("15-route.html", "Focus · 一条完整的路线", IDO, "句型 · 最难的一句",
        s_route("请问，去银行怎么走？",
                ["过马路", "一直往前走", "走五分钟"],
                "……就到了。",
                "一问一答，三步加一个时间。这就是今天要会说的整句。"))

    add("16-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("举手／放平：「过马路」＝ cross the road？「一直」＝ turn？",
                "第二个是错的——要他们说出为什么"),
               ("白板：写「先过马路，然后一直往前走」。", "Write it in characters"),
               ("这句的顺序哪里错了？ 你先走一直，然后过马路。", "改过来"),
               ("请问，去咖啡馆怎么走？", "点名一位，要两步的答案")]))

    # ── Flexible practice ──
    add("17-arrows.html", "Activity 1 · 箭头配词", PRAC, "活动一 · We Do · 8 分钟",
        s_arrows("活动一 · 箭头配词（课本 p.129 第 8 题）· 白板作答",
                 [("一直往前走", "yizhi"), ("过马路", "guomalu"), ("往前走", "wangqian"),
                  ("往右拐", "guai"), ("向左转", "zhuan"), ("在第一个路口", "di")],
                 "只有<b>前三个</b>今天学过。后三个是下节课的——"
                 "让他们看箭头<b>猜</b>，猜的这一下就是下节课的预习。"))
    add("18-shops.html", "Activity 1b · 十二家店（只认不背）", PRAC, "活动一 b · 3 分钟",
        s_task("课本 p.128 第 7 题 · 十二张店铺图配名字 · <b>只认，不背</b>",
               ["中药房 · 剧场 · 灯具店 · 五金店 · 礼品店 · 糕饼店 · "
                "理发店 · 电器店 · 茶馆 · 钟表店 · 便利店 · 西洋乐器店",
                "<b>开始前先说清楚：这十二个都不是生词，也不考。</b> "
                "免得有人想把十二家店背下来。",
                "两分钟配对比赛，然后对答案。"],
               "价值不在词，在<b>推理</b>——几乎每一个都能从已经会的字拆出来："
               "中药＋房 · 灯具＋店 · 理发＋店 · 钟表＋店。"
               "请两位同学说说他们是怎么猜出来的。"))

    add("19-roleplay.html", "Activity 2 · 课文二角色扮演", PRAC, "活动二 · You Do · 7 分钟",
        s_dialogue("活动二 · 课文二对话一、二（p.127 · CD 51）· 先看书，再合上书",
                   [("A", "请问，咖啡馆在哪儿？"),
                    ("B", "你先过马路，然后一直往前走，走五分钟就到了。"),
                    ("A", "请问，去银行怎么走？"),
                    ("B", "你一直往前走，看到红绿灯向左拐，再走五分钟就到了。")],
                   "然后<b>换词</b>：句型不动，把目的地换成一到三课的建筑，分钟数也换。"
                   "取三组上台。第一轮句型留在黑板上，第二轮擦掉。"))
    add("20-roleplay-ext.html", "Activity 2 · Extension", PRAC, "活动二 · 延伸",
        s_task("延伸 · 给会说的同学",
               ["B 故意说一条<b>和地图不符</b>的路线，A 要听出来并用中文纠正：",
                "　<b>不对吧，过马路以后应该往前走，不是往回走。</b>",
                "然后再跑一遍：A 很急——<b>我很急，走路要几分钟？坐车呢？</b>——"
                "B 两个都要答。"],
               "都做完了，两人合作把这条路线<b>写</b>下来，"
               "写成一段，中间不能出现英文。"))

    add("21-map.html", "Activity 3 · 看地图问路", PRAC, "活动三 · You Do · 4 分钟",
        s_task("活动三 · 看地图问路（课本 p.129 第 9 题）· 每组一张 A5 地图",
               ["只用今天会的：请问，……在哪儿？ · 请问，去……怎么走？ · "
                "先……然后…… · 过马路 · 一直往前走 · 走 X 分钟就到了",
                "三个情境：1 去邮局　2 去教堂　3 去市政大楼"],
               "三个情境<b>连成一趟</b>——从邮局到教堂再到市政大楼，"
               "每一段的起点是上一段的终点。一口气说完，不停。"))

    add("22-game.html", "Game · 老师说 Simon Says", PRAC, "游戏 · 4 分钟",
        s_task("游戏 · 老师说 · 前面留出空地",
               ["老师说：一直往前走！ · 老师说：过马路！ · 老师说：停！",
                "<b>往前走！</b>（陷阱——没有「老师说」，动了就出局）",
                "练的是不经过英文、直接听懂方向动词。"],
               "指令<b>串起来</b>——老师说：先过马路，然后一直往前走，看到红绿灯就停——"
               "三步都要做对。最后两轮换一位会说的同学当发令人，他要自己编。"))

    add("23-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 请一位同学现场造一句，示范第三条。",
                "<b>自评</b> · 举手：会了 · 差不多 · 还要练，一条一条来。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下节课</b> · 学「在第二个路口往右拐」——怎么说转弯。"],
               cn="出门条：翻译 —— First cross the road, "
                  "then walk straight ahead for five minutes."))

    return S
