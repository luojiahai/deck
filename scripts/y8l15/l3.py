# -*- coding: utf-8 -*-
"""Y8 L15 · Lesson 3 of 6 — 就, and what is across the road

Source: docs/lesson-plans/y8-l15/03-jiu-across-the-road-mixed.md
Textbook p.145 Act. 5 (the 就 translation set), p.152 Act. 14 (map with
前面／后面／左面／右面／对面). Workbook pp.166–167.

就 carries no picture of its own: it is not a thing, it is an emphasis.
The drawing work here goes to 对面 instead — a road seen from above with
one arrow crossing it — because that is what students get wrong (they
reach for 在……那边 and lose the road entirely).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_text, s_errors, s_title, s_lisc)

SLUG = "l3-jiu-across-the-road"
TITLE = "Y8 L15 · 社区 Neighbourhood · Lesson 3 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='就在马路对面', en='Right across the road',
            desc='The small character that was deliberately skipped in Lesson 2. 就 has no English word of its own and changes the whole feeling of a sentence — and it goes before the verb, which is the error this lesson exists to prevent.',
            words='马路 · 对面 · 火车站 · 路', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 就 Right across the road", "LESSON 3 OF 6",
        "第十五课 · 社区",
        s_title("就在马路对面", "Right Across the Road",
                "Year 8 · Book 2 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 2 · p.145, p.152"))

    add("02-review.html", "Review · Lesson 2 — 离 and 挺", REV, "复习 · 上一课",
        s_list("小白板 · 五题 · 英译中",
               [("The supermarket isn't far from my home.", "超市离我家不远。"),
                ("School is quite far from my home.", "我家离学校挺远的。"),
                ("Is the flower shop far from here?", "花店离这儿远吗？"),
                ("nearby", "附近"),
                ("quite close", "挺近的")],
               "第一题写完，请两个同学念出来——让全班听见「离」在句子中间，不在开头。",
               compact=True))
    add("03-review-bridge.html", "Review · the word we skipped", REV, "复习 · 跳过去的那个字",
        s_focus("上一课课文里，有一个字我们绕过去了",
                "走路五分钟<b>就</b>到了。",
                "Five minutes on foot and you're there.",
                "这个字很小，它没有自己的英文翻译，可是它一进句子，"
                "整句话的感觉就变了。今天一整节课都是它。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say exactly where a place is, and stress that it is close by.",
               [("I can say 马路、对面、火车站", "能说「马路」「对面」「火车站」"),
                ("I can use 就 to mean right there", "会用「就」说「就在马路对面」"),
                ("I can say how quickly I get somewhere with 走路……分钟就到了",
                 "会说「走路五分钟就到了」")]))

    # ── Cycle 1 · 马路 / 对面 ──
    add("05-c1-words.html", "Cycle 1 · A — 马路 / 对面", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("马路（馬路）", "mǎlù", "road; street", "malu"),
                ("对面（對面）", "duìmiàn", "opposite", "duimian")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家附近有一条大<b>马路</b>。", "There's a big road near my home."),
                    ("花店在超市<b>对面</b>。", "The flower shop is opposite the supermarket."),
                    ("<b>马路对面</b>有一个花店。",
                     "There's a flower shop across the road.", True)],
                   "「对面」跟第十三课的「左面」「右面」是一家的——最后一个字都是「面」。"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 在 ________ 对面。"],
                "两句连起来，三个店排好位置，用上第十三课的「右面」或者「左面」："
                "<b>花店在超市对面，文具店在花店右面。我常常先去超市，再去文具店。</b>"))

    # ── Cycle 2 · 火车站 / 路 ──
    add("08-c2-words.html", "Cycle 2 · A — 火车站 / 路", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("火车站（火車站）", "huǒchēzhàn", "train station", "huochezhan"),
                ("路", "lù", "route; bus number", "lu")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我家离<b>火车站</b>不远。", "My home isn't far from the train station."),
                    ("我坐五<b>路</b>公共汽车上学。", "I take the number 5 bus to school."),
                    ("<b>火车站</b>在马路对面，我坐十<b>路</b>公共汽车去。",
                     "The station is across the road; I take the number 10 bus.", True)],
                   "「五路公共汽车」的「路」，跟「马路」的「路」是同一个字。"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我坐 ________ 路公共汽车去 ________ 。"],
                "一句话说清楚从学校怎么去火车站：车号 + 时间："
                "<b>我坐十路公共汽车去火车站，十五分钟就到了。</b> "
                "再说一句：车不来的话你怎么办？"))

    add("11-recall.html", "Recall · four words, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["马路", "对面", "火车站", "路"],
                 "读不出来就停下来重教——不要往下走。", cols=4))

    # ── The pattern ──
    add("12-pattern.html", "Pattern · 就 — right; just", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 「就」放在动词<b>前面</b>",
                  "……　就　+　动词　……",
                  [("超市<b>就</b>在我家附近。", "The supermarket is <i>right</i> near my home."),
                   ("火车站<b>就</b>在马路对面。", "The station is <i>just</i> across the road."),
                   ("走路五分钟<b>就</b>到了。",
                    "Five minutes on foot and you're <i>there</i>.")],
                  "「就」没有一个对得上的英文字。它做的事是<b>强调</b>：近得出乎意料，"
                  "快得出乎意料。"))
    add("13-errors.html", "The error to pre-empt · where 就 goes", IDO, "句型 · 最常见的错",
        s_errors([("走路五分钟到了就。", "走路五分钟<b>就</b>到了。",
                   "「就」在动词前面，跟「先」「也」一样"),
                  ("火车站在就马路对面。", "火车站<b>就在</b>马路对面。",
                   "是「就在」，不是「在就」")],
                 "改一改 · 「就」最常见的两个错",
                 "手指指黑板：「就」该放在哪一半？全班一起指。"))
    add("14-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("三个分句，「就」用两次，还要接上一课的「离」",
                "我家离花店挺近的，走路两分钟就到了，家具店就在花店对面。",
                "My home is quite close to the flower shop — two minutes on foot and "
                "you're there — and the furniture shop is right opposite it.",
                "上一课的「离」「挺……的」，加今天的「就」「对面」。"
                "旧的不丢，是拿来接新的。"))

    add("15-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「就」放在动词前面还是后面？用手指黑板。", "全班一起指——看谁指错了那一半"),
               ("什么意思？　书店就在学校对面。", "先说英文，再说说为什么要加「就」"),
               ("翻译：<i>The furniture shop is right across the road.</i>",
                "小白板，家具店就在马路对面。"),
               ("改一改：我家离超市很近，走路三分钟到了就。", "哪里错了？")]))

    # ── Practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("马路", "malu"), ("对面", "duimian"),
                   ("火车站", "huochezhan"), ("路", "lu")],
                  "这一页留在屏幕上——后面两个活动都看它。"))

    add("17-act1.html", "Activity 1 · Map talk (We Do, 7 min)", PRAC, "活动一 · 7 分钟",
        s_figure("ditu", "活动一 · 看地图说话",
                 ["<b>两人一组</b>　每组一张 A3 地图，屏幕上也是同一张。",
                  "A 问：<b>超市在哪儿？</b> B 答，答案里<b>一定要有「就」</b>。",
                  "地图上八个地方，一人问四次，然后换。",
                  "最后全班一起：老师指一个地方，全班齐声回答。"],
                 cn="超市在哪儿？　—— 就在马路对面。／就在花店右面。"))
    add("18-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难 · 不看地图",
               ["B 先看三十秒地图，然后<b>把地图扣过来</b>，凭记忆回答。",
                "A 的问题也换：不问「在哪儿」，问<b>「从学校怎么去火车站？」</b>——"
                "B 要说一条<b>路线</b>，不是一个位置。",
                "桌上什么都不许放。"]))

    add("19-act2.html", "Activity 2 · The 就 sentences (You Do, 9 min)", PRAC,
        "活动二 · 9 分钟",
        s_list("活动二 · 课本两题 · 写在本子上",
               [("<b>p.145 第五题 · 5 分钟</b>　六个带「就」的句子翻成英文。",
                 "翻完自己再写三句，说学校附近真的地方"),
                ("老师收三个同学写得好的，抄到黑板上。", "抄的是学生自己写的，不是课本的"),
                ("<b>p.152 第十四题 · 4 分钟</b>　用「前面、后面、左面、右面、对面」"
                 "描述课本地图。", "写四句，至少两句有「就」")],
               "写完的人不要停——看下一页。"))
    add("20-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难 · 写一张走法，给别人用",
               ["不做翻译。写<b>六行</b>，说从学校大门走到火车站怎么走——"
                "要写得让一个七年级学生照着就能走到。",
                "「就」用<b>三次</b>，「对面」用一次，「离」用一次。",
                "写完把纸给同桌，他<b>只看你写的字</b>，把路线画出来。画错了就是你没写清楚。"]))

    add("21-game.html", "Game · Sentence Jumble (7 min)", PRAC, "游戏 · 句子拼图",
        s_task("游戏 · 句子拼图 · 7 分钟",
               ["四人一组，一个信封。信封里是六个句子，剪成了一个词一张。",
                "六个句子都带「就」，用的都是今天的词。",
                "哪一组先把六句全部摆对，哪一组赢。"],
               cn="火车站 / 就 / 在 / 马路 / 对面　　走路 / 五 / 分钟 / 就 / 到了",
               ext="强的那一组换信封：里面只有<b>四</b>句的卡片，"
                   "却多了三张<b>哪一句都不属于</b>的干扰卡（一个 / 很 / 了）。"
                   "四句摆对，还要<b>用中文</b>说出每一张多余的卡为什么放不进去。"))

    add("22-strokes.html", "Writing · copy the new characters", PRAC, "写字 · 生词",
        s_strokes([("马", 3, "只有三画——横折、竖折折钩、横"),
                   ("路", 13, "足字旁，右边是「各」"),
                   ("对", 5, "左边是「又」，右边是「寸」"),
                   ("面", 9, "外框先写，里面两横一竖"),
                   ("站", 10, "立字旁，右边是「占」——跟「店」的右边一样")],
                  "写字 · 课本笔顺 · 练习册 pp.166–167",
                  "每个字写三遍。「站」和「店」右边同一个「占」，左边不同。"))

    # ── Plenary ──
    add("23-plenary.html", "Plenary · 回头看目标", PLEN, "小结 · 43–50 分钟",
        s_list("小结 · 回头看今天的三个目标",
               [("能说「马路」「对面」「火车站」", "👍 / 😐 / 👎"),
                ("会用「就」说「就在马路对面」", "👍 / 😐 / 👎"),
                ("会说「走路五分钟就到了」", "👍 / 😐 / 👎")],
               "每一条请一个同学用中文举一个例子——说得出来才算 👍。"))
    add("24-exit.html", "Exit ticket", PLEN, "出门条 · Exit ticket",
        s_focus("出门条 · 写一句用「就」的句子，交上来",
                "________ 就在 ________ 。",
                "Must be about a real place you know.",
                "下节课是<b>游戏课</b>——你会需要的，因为要开始说两段的路："
                "先坐船，然后坐公共汽车。",
                ext="写完了？写两句：一句「就在」，一句「就到了」。"))
    return S
