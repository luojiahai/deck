# -*- coding: utf-8 -*-
"""Y8 L13 · Lesson 2 of 6 — rooms upstairs, and the measure word 间

Source: docs/lesson-plans/y8-l13/02-upstairs-rooms-mixed.md
Textbook p.122 (Text 1, upstairs half; New Words 5–9), p.125 Act. 4 (CD 63),
p.131 Act. 13. Workbook pp.144–145 Ex. 1, p.145 Ex. 2, p.147 Ex. 8.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_errors,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_listening, s_text, s_title, s_lisc)

SLUG = "l2-upstairs-rooms"
TITLE = "Y8 L13 · 房子 House · Lesson 2 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

# Card shown on the series landing page (index/designs/y8-l13/index.html),
# written by build.py. Lives beside the lesson it describes.
CARD = dict(cn='楼上有什么', en='Rooms upstairs',
            desc='The upstairs rooms, and the measure word that has no English equivalent: 卧室 takes 间, 浴室 takes 个. CD 63 runs twice — tick it, then draw it.',
            words='卧室 · 书房 · 浴室 · 洗澡', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 楼上有什么 Rooms upstairs", "LESSON 2 OF 6", "第十三课 · 房子",
        s_title("楼上有什么？", "Rooms Upstairs",
                "Year 8 · Book 2 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 2 · p.122 · CD 63"))

    add("02-review.html", "Review · flashcards", REV, "复习 · Lesson 1",
        s_recall(["房子", "房间", "层", "楼", "楼上", "楼下"],
                 "全班一起读两遍。读完马上进下一页——那三句里有错。",
                 head="认字快闪 · characters only · 一起读"))
    add("03-review-errors.html", "Review · Correct the Teacher", REV, "复习 · 改错",
        s_errors([("我的房间有楼上。", "我的房间在楼上。", "说在哪儿，用「在」"),
                  ("我家的房子在两层。", "我家的房子有两层。", "说有什么，用「有」"),
                  ("楼上有三个层。", "楼上有三层。", "「层」自己就是量词，不加「个」")],
                 "改错 · 三句都有问题 · 先写在小白板上，不要抢答",
                 "第三句是新的——「层」跟「个」不能一起用。今天还有一个量词要学。"))
    add("04-review-routine.html", "Review · 说说你的一天 (90 sec)", REV, "复习 · 课本 p.131 第 13 题",
        s_task("两人一组 · 说说你每天做什么 · 90 秒",
               ["用中文说，不要写。轮流说，每人至少四句。",
                "去年学过的词都可以用：起床 · 吃早饭 · 上学 · 放学 · 睡觉。"],
               cn="我每天早上六点半起床。我七点一刻吃早饭。我八点……"))

    add("05-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("name the rooms upstairs and count them with the right measure word.",
               [("I can name the upstairs rooms", "能说出楼上的房间"),
                ("I can count bedrooms with 间 and bathrooms with 个", "能用「间」数卧室，用「个」数浴室"),
                ("I can understand someone describing their house when I hear it",
                 "能听懂别人说他家的房子")]))

    # ── Cycle 1 · 卧室 / 书房 ──
    add("06-c1-words.html", "Cycle 1 · A — 卧室 / 书房", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("卧室", "wòshì", "bedroom", "woshi"),
                ("书房", "shūfáng", "study room", "shufang")))
    add("07-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家有三间<b>卧室</b>。", "My house has three bedrooms."),
                    ("我爸爸的<b>书房</b>在楼上。", "My dad's study is upstairs."),
                    ("楼上有三间<b>卧室</b>和一个<b>书房</b>。",
                     "Upstairs there are three bedrooms and a study.", True)],
                   "你家有书房吗？"))
    add("08-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家有 ________ 间卧室。", "我家的书房在 ________ 。"],
                "两句连起来，用「可是」或者「还有」：<b>我家有四间卧室，可是我们没有书房。</b>"))

    # ── Cycle 2 · 浴室 / 洗澡 ──
    add("09-c2-words.html", "Cycle 2 · A — 浴室 / 洗澡", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("浴室", "yùshì", "bathroom", "yushi"),
                ("洗澡", "xǐzǎo", "to bathe; have a shower", "xizao")))
    add("10-c2-note.html", "浴室 = 洗澡间", IDO, "生词 2 · 一样的意思",
        s_pattern("两个词，一个意思 · 课本 p.122 就是这样写的",
                  "浴室 ＝ 洗澡间",
                  [("我家有两个浴室。", "My house has two bathrooms."),
                   ("我家有两个洗澡间。", "Same sentence, the other word.")],
                  "课本写的是「浴室(洗澡间)」——两个都对，说哪个都行。"))
    add("11-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我家有两个<b>浴室</b>。", "My house has two bathrooms."),
                    ("我每天晚上<b>洗澡</b>。", "I have a shower every evening."),
                    ("我在<b>浴室洗澡</b>。", "I shower in the bathroom.", True)],
                   "你每天什么时候洗澡？"))
    add("12-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我家有 ________ 个浴室。", "我每天 ________ 洗澡。"],
                "把去年学的时间词用上，两个新词放进同一句："
                "<b>我每天晚上七点在楼上的浴室洗澡。</b>"))

    add("13-recall.html", "Recall · four characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["卧室", "书房", "浴室", "洗澡"], "读不出来就停下来重教。", cols=4))

    # ── The measure word ──
    add("14-pattern.html", "Pattern · 间 / 个", IDO, "句型 · 量词",
        s_pattern("量词 · 数房间用哪一个？",
                  "几 + 间 + 卧室　／　几 + 个 + 浴室",
                  [("楼上有三<b>间</b>卧室。", "Bedrooms take 间."),
                   ("楼下有一<b>间</b>卧室。", "Still 间 — it is not about which floor."),
                   ("我家有两<b>个</b>浴室。", "Bathrooms take 个.")],
                  "不是看大小，也不是看楼上楼下。<b>卧室</b>用「间」，<b>浴室、书房、房间</b>用「个」。"))
    add("15-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("一句话，两个量词",
                "我家的房子有两层，楼上有三间卧室和一个书房，楼下有一间卧室和一个浴室。",
                "My house has two storeys; upstairs there are three bedrooms and a study; "
                "downstairs there is a bedroom and a bathroom.",
                "「间」出现两次，「个」出现两次——每一个都要对。"))

    add("16-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「书房」是卧室的意思吗？", "对就举大拇指，不对就朝下"),
               ("间 还是 个？ 楼上有三 ____ 卧室。", "写在小白板上"),
               ("间 还是 个？ 我家有两 ____ 浴室。", "写在小白板上"),
               ("这句话对不对？ ✗ 我家有三个卧室。", "哪里错了？怎么改？"),
               ("屏幕上哪两个词是一个意思？", "点名回答")]))

    # ── Text ──
    add("17-text.html", "Text 1 · the upstairs half", IDO, "课文一 · p.122 · 楼上",
        s_text("课文一 · 楼上这半句 · CD 61",
               "楼上有三间卧室、一个书房和一个浴室(洗澡间)。",
               "楼上有几间卧室？　楼上有书房吗？　浴室在楼上还是楼下？",
               "先听，再一起读。读第二遍的时候把拼音关掉。"))

    # ── Practice ──
    add("18-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("卧室", "woshi"), ("书房", "shufang"),
                   ("浴室", "yushi"), ("洗澡", "xizao")],
                  "这一页留在屏幕上——听力、画图、游戏都看它。"))

    add("19-act1.html", "Activity 1 · Listen and draw (We Do, 9 min)", PRAC,
        "活动一 · We Do · 9 分钟 · CD 63",
        s_task("活动一 · 听一听，画出来 · 课本 p.125 第 4 题",
               ["<b>第一遍</b>　只在课本 p.125 上打勾，不要画。",
                "<b>第二遍</b>　发格子纸，第一段话画左边，第二段画右边，房间名用汉字写。",
                "<b>第三遍</b>　老师自己念一个新的，你们画。"],
               cn="这套房子有两层。楼上有四间卧室、一个书房和两个浴室。楼下有一间卧室。"))
    add("20-listening.html", "Listening · CD 63 items (textbook p.125)", PRAC,
        "听力 · 课本 p.125 第 4 题",
        s_listening("听一听，选一个 · CD 63",
                    [("① A　几间卧室？", "a) 两间　b) 三间，没有书房　c) 一间"),
                     ("① B　几个浴室？", "a) 两个浴室，一个洗手间　b) 一个浴室　c) 三个浴室"),
                     ("① C　客厅大不大？", "a) 特别大　b) 餐厅很大　c) 不大也不小"),
                     ("② A　几间卧室？", "a) 四间　b) 五间　c) 三间"),
                     ("② B　几个浴室？", "a) 四个　b) 三个　c) 两个浴室，两个洗手间"),
                     ("② C　客厅怎么样？", "a) 卧室不算大　b) 客厅特别大　c) 客厅不算小")],
                    "「洗手间」「客厅」「餐厅」是下节课的词——今天只要听出数字和「间／个」。"))
    add("21-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["不要画——把第一段话一个字一个字写下来。"],
               "写完以后用中文回答：为什么说话的人说「你可以用一间做书房」，"
               "而不是「我家有书房」？ 然后自己写第四段房子介绍，四个小句，"
               "今天的词全要用上，再加上节课的两个，给同桌画。"))

    add("22-act2.html", "Activity 2 · Floor-plan pairs (You Do, 9 min)", PRAC,
        "活动二 · You Do · 9 分钟",
        s_task("活动二 · 两人一组 · 一个人说，一个人画",
               ["每人在第二张格子纸上设计楼上，先不要给同桌看。",
                "中间隔一本书。A 说，B 画，画完对一对。",
                "然后交换，再来一次。"],
               "B 不可以问「有没有」这样的问题，只能问 <b>楼上有什么？</b> 和 <b>有几间？</b>——"
               "A 就必须自己说出完整的句子。交换以后，A 的房子里要有一个<b>不在楼上</b>的房间。"
               "最后两个人都用第三人称写三句：<b>他家的房子有两层，楼上有……</b>",
               cn="A：楼上有三间卧室。　B：（画）有书房吗？　A：有，书房在左边。"))

    add("23-wb-chain.html", "Workbook p.147 Ex.8 · word chains", PRAC, "练习册 · p.147 第 8 题",
        s_task("练习册 p.147 · 词语接龙 · 三分钟，能写几个写几个",
               ["上一个词的最后一个字，就是下一个词的第一个字。",
                "十八条，不用写完——写得越多越好。"],
               cn="客房 → 房子　·　炒面 → ________　·　中餐 → ________　·　非常 → ________"))

    add("24-strokes.html", "Characters · 卧 室 浴 洗 澡 (Workbook p.144–145)", PRAC,
        "写汉字 · 练习册 pp.144–145",
        s_strokes([("卧", 8, "左边「臣」，右边「卜」"),
                   ("室", 9, "宝盖头，下面「至」"),
                   ("浴", 10, "三点水在左"),
                   ("洗", 9, "三点水加「先」"),
                   ("澡", 16, "笔画最多的一个——慢慢写")],
                  "笔顺 · 每个字写三遍",
                  "「厅」和「厨」留到下节课。"))

    add("25-game.html", "Game · Room Bingo (5 min)", PRAC, "游戏 · 宾果 · 5 分钟",
        s_list("游戏 · 宾果 Bingo",
               [("发 3×3 的格子纸", "卧室 · 书房 · 浴室 · 洗澡 · 房间 · 楼上 · 楼下 · 层 · 楼"),
                ("老师不说单词，说整句话", "我每天晚上<b>洗澡</b>。／ 楼上有三间<b>卧室</b>。"),
                ("连成一行就喊「我赢了」", "听句子里的那个词，不是听单词"),
                ("<b>加难</b>：赢的人不能只喊", "要把那一行三个词，一个词说一句完整的话")],
               "格子纸打印几种不同排列。"))

    add("26-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 念三条 success criteria，问一句：哪一条最难？",
                "<b>自评</b> · 小白板写 👍 / 😐 / 👎，三条一起举起来。",
                "<b>出门条</b> · 量词写对才算对。",
                "<b>下节课</b> · 我们下楼——下课以前你就能读完整篇课文一了。"],
               cn="出门条：写中文——Upstairs there are three bedrooms and one bathroom."))
    return S
