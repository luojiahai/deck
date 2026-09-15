# -*- coding: utf-8 -*-
"""Y9 L14 · Lesson 1 of 6 — 骑 / 自行车 / 购物 / 广场 / 车站 / 路 + 或者……，或者……

Source: docs/lesson-plans/y9-l14/01-transport-huozhe-mixed.md
Textbook p.133 Act. 1 (vehicles), p.134 Act. 2 (或者) and Act. 3 (transport
places). Workbook p.154 Ex. 3 and p.155 Ex. 4.

骑 and 路 have no picturable referent — 骑 is a verb and 路 here is the
counter for a bus route — so both get textonly cards. Drawing 骑 as a second
bicycle beside 自行车 would teach nothing.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_errors,
                   s_title, s_lisc, label)

SLUG = "l1-getting-around"
TITLE = "Y9 L14 · 问路 Asking the Way · Lesson 1 of 6"
CARD = (SLUG, "骑车还是坐车", "Getting Around · 或者……，或者……",
        "vocab", "骑 · 自行车 · 购物 · 广场 · 车站 · 路，加「或者……，或者……」。"
                 "一句话给两个办法——陈述句用「或者」，问句才用「还是」。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 骑车还是坐车", "LESSON 1 OF 6", "第十四课 · 问路",
        s_title("骑车还是坐车", "Getting Around",
                "Year 9 · Book 3 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 3 · p.133–134 · 第 1–3 题"))

    add("02-review.html", "Review · L13 路线 + 公共设施", REV, "复习 · Lesson 13",
        label("认字快闪 · characters only · 一起读")
        + '  <div class="recall-grid" style="grid-template-columns:repeat(4,1fr);">\n'
        + "\n".join('    <div class="recall-cell" style="padding:16pt 8pt;">'
                    '<p class="recall-hanzi" style="font-size:30pt;">%s</p></div>' % w
                    for w in ["邮局", "银行", "诊所", "教堂",
                              "过马路", "一直往前走", "红绿灯", "第一个路口"])
        + "\n  </div>\n"
        + '  <div class="task-box" style="margin-top:12pt;">\n'
          '    <p class="task-line"><b>白板</b> · 我说路线，你画箭头：'
          '一直往前走，看到红绿灯往左拐。</p>\n'
          '    <p class="task-line" style="margin-top:6pt;"><b>转过去问同伴</b> · '
          '从学校去邮局怎么走？ 三十秒。</p>\n  </div>')

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say there is more than one way to get somewhere, "
               "using 或者……，或者……。",
               [("I can say how I travel", "能说我怎么去：骑自行车／坐公共汽车／走路"),
                ("I can give two options in one sentence with 或者……，或者……",
                 "能用「或者……，或者……」一句话说两个办法"),
                ("I can say where a stop is, using last lesson's position words",
                 "能说车站在哪儿：车站就在……对面")]))

    # ── Cycle 1 · 骑 / 自行车 ──
    add("04-c1-words.html", "Cycle 1 · A — 骑 / 自行车", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("骑", "qí", "ride", None),
                ("自行车", "zìxíngchē", "bicycle", "zixingche")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我会<b>骑</b>车。", "I can ride a bike."),
                    (None, "我的<b>自行车</b>很新。", "My bicycle is new."),
                    (None, "我不会<b>骑</b>车，可是我姐姐会<b>骑自行车</b>。",
                     "I can't ride, but my sister can ride a bike.", True)],
                   "你会骑自行车吗？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我（会／不会）骑 ________ 。", "我的自行车 ________ 。"],
                "用「因为……，所以……」写一句：<b>因为我家离学校很近，所以我每天骑自行车上学。</b>"
                " 再写一句：<b>下雨的时候</b>呢？"))

    # ── Cycle 2 · 购物 / 广场 ──
    add("07-c2-words.html", "Cycle 2 · A — 购物 / 广场", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("购物", "gòuwù", "shopping", "gouwu"),
                ("广场", "guǎngchǎng", "square", "guangchang")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "妈妈周末去<b>购物</b>。", "Mum goes shopping at the weekend."),
                    (None, "我家附近有一个大<b>广场</b>。",
                     "There's a big square near my home."),
                    (None, "我们去<b>购物广场</b>买衣服。",
                     "We go to the shopping centre to buy clothes.", True)],
                   "你常去哪儿购物？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我（常常／不常）去 ________ 购物。"],
                "用「除了……以外」写一句：<b>除了衣服以外，我还在购物广场买鞋。</b>"
                " 再说一句为什么。"))

    # ── Cycle 3 · 车站 / 路 ──
    add("10-c3-words.html", "Cycle 3 · A — 车站 / 路", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("车站", "chēzhàn", "station; stop", "chezhan"),
                ("路", "lù", "route (bus number)", None)))
    add("11-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "<b>车站</b>就在教堂对面。",
                     "The stop is right opposite the church."),
                    (None, "我坐25<b>路</b>公共汽车上学。",
                     "I take the number 25 bus to school."),
                    (None, "我在<b>车站</b>等25<b>路</b>车，等了十分钟。",
                     "I waited ten minutes at the stop for the number 25.", True)],
                   "你家附近的车站在哪儿？"))
    add("12-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["我坐 ________ 路公共汽车 ________ 。", "车站就在 ________ 。"],
                "用<b>两个</b>方位词说车站在哪儿："
                "<b>车站在银行和邮局中间，就在诊所对面。</b>"))

    add("13-recall.html", "Recall · 六个生词", IDO, "认一认 · Checkpoint",
        s_recall(["骑", "自行车", "购物", "广场", "车站", "路"],
                 "读不出来就回去重教——别往下走。", cols=3))

    # ── Pattern ──
    add("14-pattern.html", "Pattern · 或者……，或者……", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 一句话，两个办法",
                  "或者 + 办法一，或者 + 办法二",
                  [("你<b>或者</b>骑自行车去，<b>或者</b>坐公共汽车去。",
                    "You can either cycle or take the bus."),
                   ("周末我<b>或者</b>在家看书，<b>或者</b>去公园跑步。",
                    "At the weekend I either read at home or go running in the park."),
                   ("去购物广场，你<b>或者</b>坐25路，<b>或者</b>坐97路。",
                    "To the shopping centre, take either the 25 or the 97.")],
                  "「或者」要出现<b>两次</b>——每个办法前面一次。"))
    add("15-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 条件 + 两个办法 + 结论",
                "如果下雨，我或者坐地铁去，或者请爸爸开车送我；"
                "如果天气好，我一定骑自行车去。",
                "If it rains I either take the subway or ask Dad to drive me; "
                "if the weather's good, I always cycle.",
                "两个条件，各配一个答案。第一个条件里还套了「或者……，或者……」。"))
    add("16-errors.html", "或者 or 还是？", IDO, "注意 · The one to get right",
        s_errors([("你还是骑自行车去，还是坐车去。",
                   "你或者骑自行车去，或者坐车去。", "陈述句 · 用「或者」"),
                  ("我或者骑自行车，或者坐车？",
                   "你骑自行车还是坐车？", "问句 · 用「还是」")],
                 "或者 ≠ 还是",
                 "「或者」说的是答案，「还是」问的是问题。今天一整节课都会有人写错这个。"
))

    add("17-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「自行车」怎么读？", "全班一起说两遍"),
               ("白板：写一句用「或者……，或者……」，说你周末做什么。", "写完举起来"),
               ("这句哪里错了？ 我还是骑自行车去，还是坐公共汽车去。", "找出来，改过来"),
               ("举手：「广场」的第一个字是什么意思？", "「广」——想想「广场」有多大")]))

    # ── Flexible practice ──
    add("18-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("骑", None), ("自行车", "zixingche"), ("购物", "gouwu"),
                   ("广场", "guangchang"), ("车站", "chezhan"), ("路", None)],
                  "这块板整个活动都留在屏幕上——写的时候可以看。"))
    add("19-task.html", "Activity 1 · 我的一天，怎么去？", PRAC, "活动一 · We Do · 6 分钟",
        s_task("活动一 · 我的一天，怎么去？ · 三次出门，三种走法，"
               "<b>六个生词都要用上</b>",
               ["三到四句话。写完，同伴数一数你漏了哪个词。",
                "样子："],
               "不看屏幕写，而且每句都要用连词连起来——"
               "<b>先……然后……</b>、<b>因为……所以……</b>、<b>……的时候</b>。"
               "最后加一句：哪一趟最花时间？为什么？",
               cn="早上我骑自行车去学校。下午我跟朋友去购物广场，"
                  "车站就在广场旁边，我们坐25路车回家。"))
    add("20-activity2.html", "Activity 2 · 或者 · 从纸上到嘴上", PRAC,
        "活动二 · We Do → You Do · 9 分钟",
        s_list("活动二 · 前五分钟写，后四分钟说",
               [("课本 p.134 第 2 题 · 六句填「或者」，再自己写两句",
                 "老师走动——看谁写成了「还是」"),
                ("写完的继续做练习册 p.154 第 3 题，然后 p.155 第 4 题",
                 "第 4 题是「或者」和「还是」同时出现的那一题"),
                ("接龙 · A 问「你怎么去学校？」，B 用「或者……，或者……」回答",
                 "B 回答完，转身问下一位<b>不一样</b>的问题——不能重复"),
                ("接龙断了，就从那个人重新开始", None)],
               "接龙的问题库：你周末做什么？你去哪儿购物？你怎么去市中心？"))
    add("21-game.html", "Game · 抢词 Slap the Board", PRAC, "游戏 · 8 分钟",
        s_task("游戏 · 抢词 · 十六张卡片贴在黑板上，两人一组上来",
               ["卡片：自行车 公共汽车 地铁 火车 出租车 飞机 船 电车",
                "　　　小巴 车站 地铁站 火车站 机场 码头 公路 马路",
                "老师说<b>英文</b>，先摸到正确卡片的人为自己队得分。两轮一换，每人都上一次。",
                "最后一分钟发课本 p.134 第 3 题，对一对哪些词出现过。"],
               "给流利的同学：老师不说英文，说<b>中文定义</b>——"
               "「你在这儿等公共汽车」、「船在这儿停」。摸到以后还要用这个词说一句话，"
               "不然不算分。"))

    add("22-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 请一位同学读三条 Success Criteria。",
                "<b>自评</b> · 每一条举手：会了 · 差不多 · 还要练。"
                "第二条如果大部分是「差不多」，下节课开头再教一遍「或者」。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下节课</b> · 我们看课文一——坐几路车？坐几站？在哪站下车？"],
               cn="出门条：写一句 —— 用「或者……，或者……」说你怎么去购物广场。"))

    return S
