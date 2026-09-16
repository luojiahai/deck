# -*- coding: utf-8 -*-
"""Y9 L15 · Lesson 6 of 6 — 我的邻居: the block, 想想办法, the paragraph

Source: docs/lesson-plans/y9-l15/06-my-neighbours-mixed.md
Textbook p.152 Act. 15 (the nine-flat block + It's your turn!), p.153
Act. 16 (the pair project). Workbook p.170 Ex. 16 (想想办法), p.167 Ex. 10.

No new vocabulary. The last deck of the sequence, and the last before the
unit test, so two things differ from the other five:

  · the recall board carries ALL FOURTEEN words of the lesson, not a
    cycle checkpoint — s_recall's dense tier exists for exactly this
  · the plenary looks back over the whole six-lesson sequence, and the
    exit ticket is four of the workbook's own Unit 5 Revision oral
    questions (p.175), asked at the door

Act. 16 runs compressed, as the Activity 1 extension. As a full judged
project it needs more room than 300 minutes leaves, and the deck says so
rather than pretending otherwise.
"""
from build import (s_task, s_list, s_cfu, s_errors, s_recall, s_pattern,
                   s_focus, s_title, s_lisc, label)

SLUG = "l6-my-neighbours"
TITLE = "Y9 L15 · 邻居 Neighbours · Lesson 6 of 6"
CARD = (SLUG, "我的邻居", "Describing the Whole Block · 一段话",
        "writing", "整栋楼九家人、想想办法，最后写一段「我的邻居」——"
                   "就是单元考试最后一题的格式。复习整个六课。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我的邻居", "LESSON 6 OF 6", "第十五课 · 邻居",
        s_title("我的邻居", "Describing the Whole Block",
                "Year 9 · Book 3 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 3 · p.152–153 · 第 15、16 题"))

    add("02-review.html", "Review · 六节课一起复习", REV, "复习 · Lessons 1–5",
        s_list("复习 · 这一次不只复习上一节——考试前最后一节课 · 白板，三轮",
               [("第一轮 · 六个词，英文写中文",
                 "recently · move house · annoying · midnight · wake up · way"),
                ("第二轮 · 三句话，各一个结构",
                 "一句用<b>把</b>，一句用<b>被</b>，一句用<b>得</b>"),
                ("第三轮 · 转过去问同伴：你的邻居烦人吗？为什么？", "三十秒，来回各一次")],
               "这六课从搬家开始，说了声音、「把」字句、有礼貌的请求。"
               "今天把它们放在一起，写成一段完整的话。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("describe everyone who lives in a block of flats, suggest "
               "what to do about a difficult neighbour, and write a "
               "paragraph introducing our own neighbours.",
               [("I can say who lives on which floor",
                 "能说谁住哪儿：三零一住着一家人／楼上是……"),
                ("I can suggest a solution",
                 "能出主意：我会想办法／如果……，我会……"),
                ("I can write a paragraph about my neighbours",
                 "能写一段「我的邻居」——几口人、哪国人、周末做什么、我觉得"),
                ("I can use 把, 被 and 得 inside that paragraph",
                 "那一段里，「把」「被」「得」各要用一次")]))

    add("04-all-words.html", "整课生词 · 十四个", IDO, "词汇总览 · The whole lesson",
        s_recall(["最近", "搬家", "邻居", "烦人", "听见",
                  "响", "半夜", "哭", "吵", "醒",
                  "声", "注意", "办法", "把"],
                 "这块板<b>整节课</b>都留在屏幕上——今天写的每一样东西都可以看它。",
                 cols=5, head="整课生词 · 十四个 · 只有汉字 · 一起读出来"))

    add("05-skeleton.html", "一段话的四步", IDO, "示范 · The four moves",
        s_list("示范 · 跟全班一起在黑板上写一段 · 顺序比词更重要",
               [("① 谁", "我家隔壁住着一家人。／我们楼上是一对老夫妻。"),
                ("② 几口人，哪国人", "他们家有四口人，是从中国来的。"),
                ("③ 平时做什么", "他们平时很忙，周末常常在花园里种花。"),
                ("④ 我觉得", "我觉得他们很好，可是他们的狗很吵，半夜常常把我吵醒。")],
               "第 ④ 步是「把」「被」「得」该出现的地方——"
               "一段九年级的话，就是靠这一步从「一句一句」变成「一段」。"))
    add("06-focus.html", "Focus · 整段念一遍", IDO, "示范 · 连起来听",
        s_focus("示范 · 四步连起来就是一段",
                "我家隔壁住着一家人。他们家有四口人，是从中国来的。"
                "他们平时很忙，周末常常在花园里种花。"
                "我觉得他们很好，可是他们的狗很吵，半夜常常把我吵醒。",
                "Four moves, one paragraph. This is the shape the last "
                "page of the unit test asks for.",
                "老师先用正常速度整段念一遍，再回头指四个部分各在哪儿。"))

    add("07-structures.html", "这一段要用上的结构", IDO, "句型 · Recycled",
        s_pattern("句型 · 今天不学新的，今天把学过的放进一段话里",
                  "住着 / 楼上是…… · 如果……，我会…… · 把 · 被 · 得",
                  [("三零一<b>住着</b>一家人，三零二<b>是</b>一对老夫妻。",
                    "Who is where."),
                   ("<b>如果</b>楼上太吵，我<b>会</b>去敲门，请他们小点儿声。",
                    "What you'd do about it."),
                   ("他们的狗<b>把</b>我吵醒了，可是他们的电视开<b>得</b>不响。",
                    "把 and 得 in one sentence.")],
                  "「被」今天也要出现一次——想一想：你家有什么东西<b>被</b>邻居借走过？"))

    add("08-errors.html", "把 / 被 最后一次", IDO, "注意 · The one the test asks",
        s_errors([("我的自行车把哥哥骑走了。", "我的自行车被哥哥骑走了。",
                   "自行车不会骑人——东西开头用<b>被</b>"),
                  ("哥哥被我的自行车骑走了。", "哥哥把我的自行车骑走了。",
                   "人开头用<b>把</b>"),
                  ("他们的狗吵醒我。", "他们的狗把我吵醒了。",
                   "有「吵醒」这种结果，就该用「把」")],
                 "这一对，考试一定考",
                 "整个单元最容易错的就是这里。今天写那一段的时候，"
                 "老师专门看这两个字。"))

    add("09-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「三零一」是几楼？", "点名"),
               ("白板：写「他们的狗半夜把我吵醒了」。", "老师看词序，还有最后的「了」"),
               ("这句哪里错了？ 我的自行车把哥哥骑走了。", "写出改好的句子"),
               ("一段话四个部分，第三个部分是什么？", "点名——看第 05 张")]))

    # ── Flexible practice ──
    add("10-task.html", "Activity 1 · 这栋楼住着谁？", PRAC, "活动一 · We Do · 6 分钟",
        s_task("活动一 · 课本 p.152 第 15 题 · 九户人家 · 两人一组，一张图，四分钟",
               ["三零一 三零二 三零三 · 二零一 二零二 二零三 · 一零一 一零二 一零三",
                "你们自己决定每一家住的是谁，说给对方听。",
                "规矩：<b>九家都要说到</b>，<b>至少三家</b>要说他们正在干什么，"
                "<b>至少一家</b>很烦人。最后两组各说三家给全班听。"],
               "课本 p.153 第 16 题的压缩版：在白纸上画<b>其中一户</b>的房间图，"
               "写清楚每个房间里有什么，然后<b>不看纸</b>用中文讲给另一组听——"
               "房间、家具、谁睡哪儿，还有这一户让楼下最受不了的一件事。"))
    add("11-project-note.html", "关于第 16 题", PRAC, "说明 · Act. 16",
        s_task("说明 · 课本 p.153 第 16 题（画房子 + 家具表 + 全班评比）",
               ["完整版是一个<b>项目</b>，六节课装不下——今天只跑压缩版，"
                "当活动一的 Extension。",
                "想做完整版的话，它很适合单独占一节课：画图、列家具、"
                "上台介绍、全班评分。",
                "老师决定，不在这六节课里。"],
               cn="这不是删掉，是放不下——告诉学生它去哪儿了。"))
    add("12-activity2.html", "Activity 2 · 想想办法", PRAC,
        "活动二 · We Do → You Do · 6 分钟",
        s_list("活动二 · 练习册 p.170 第 16 题 · 五个情境 · 先说后写",
               [("两人先口头讨论五个情境", "三分钟"),
                ("然后自己写<b>其中三个</b>的答案", "每个都用「如果……，我会……」"
                                                    "或者「我会想办法……」"),
                ("至少有一个要以<b>直接跟邻居说的话</b>结尾", "用「能不能……？」"),
                ("老师挑三个情境各读一个答案", "同一个问题，故意挑不同同学的不同办法")],
               "答案不上屏——五个情境本来就没有标准答案。"))
    add("13-activity2-ext.html", "Activity 2 · Extension", PRAC,
        "活动二 · 给写得快的同学",
        s_task("活动二 · Extension · 五个全写，而且其中两个要写<b>第二步</b>",
               ["第一个办法<b>没用</b>的话，你接下来怎么办？",
                "<b>第一次我会……，如果他还是不注意，我会……</b>",
                "五个里面有一个<b>整段不准用「我」</b>——"
                "说别人应该怎么做：<b>你应该……／他应该……</b>"],
               cn="第一次我会去敲门，如果他还是不注意，我会跟大楼管理员说。"))
    add("14-writing.html", "Activity 3 · 我的邻居", PRAC,
        "活动三 · You Do · 7 分钟 · 安静写",
        s_task("活动三 · 写一段「我的邻居」 · 本子上写，自己写，不讨论",
               ["照第 05 张的<b>四步</b>写：谁 · 几口人哪国人 · 平时做什么 · 我觉得。",
                "<b>八句以上。</b>",
                "硬性要求：<b>「把」「被」「得」各用一次。</b>",
                "老师走动——只指黑板上的四步，不给词。下课收本子。"],
               "写<b>两个</b>邻居，一段里比较："
               "<b>楼上的……，可是隔壁的……</b>，「虽然……但是……」至少用一次。"
               "最后一句：两个里你宁可住在谁旁边？为什么？不看第 05 张，凭记忆写。"))
    add("15-game.html", "Game · Kahoot", PRAC, "游戏 · 4 分钟",
        s_list("游戏 · Kahoot · 十二题 · 课前建好",
               [("六题生词", "汉字 ↔ 英文，两个方向都有"),
                ("三题词序", "四选一：哪一句「把」是对的？「被」呢？「能不能」呢？"),
                ("两题「得」", "电视机开得 ________ ——选对的"),
                ("一题说法", "邻居跟你说「对不起」，你说什么？")],
               "一口气跑完，讲错题<b>不超过一分钟</b>。"
               "记住全班分成两半的那两题——下节课从那里开始。"))

    add("16-plenary.html", "Plenary · 六节课一起回看", PLEN, "小结 · Whole sequence",
        s_task("小结 · 43–50 分钟 · 今天回看的是<b>整个六节课</b>",
               ["<b>回看目标</b> · 今天四条读完，再把六节课的六个学习目标放上来，"
                "问全班：哪一个你最想再讲一遍？",
                "<b>自评</b> · 白板，对着<b>整个单元</b>的四个结构一个一个举："
                "<b>把 · 被 · V得 · 能不能……？</b> "
                "哪一个「差不多」最多，下节课就从哪一个开始。",
                "<b>出门条</b> · 口头，在门口一人一题（练习册 p.175 的复习问题）。",
                "<b>下节课</b> · 第十五课学完了。"
                "下一次把第五单元三课放在一起复习，准备考试。"],
               cn="你们家的邻居怎么样？他们烦人吗？ · 你家隔壁邻居的电视会开得很响吗？"
                  " · 你们最近会搬家吗？ · 你被偷过吗？"))

    return S
