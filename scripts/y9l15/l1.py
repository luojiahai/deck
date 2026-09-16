# -*- coding: utf-8 -*-
"""Y9 L15 · Lesson 1 of 6 — 最近 / 搬家 / 邻居 / 烦人 + 最近……有没有……？

Source: docs/lesson-plans/y9-l15/01-moving-in-neighbours-mixed.md
Textbook p.142 Text 1 (first half), p.143 Act. 1 (cutaway house),
p.144 Act. 3 (最近……有没有……). Workbook p.164 Ex. 1.

Four new words, so two cycles and no recall checkpoint — the checkpoint
exists to catch a stall before a third pair arrives, and there is no third
pair. The summary board does that job here.

最近 is a time word and 烦人 is a quality; neither has a picturable
referent, so both get textonly cards.
"""
from build import (s_words, s_examples, s_write, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_errors, s_text,
                   s_title, s_lisc, label)

SLUG = "l1-moving-in"
TITLE = "Y9 L15 · 邻居 Neighbours · Lesson 1 of 6"
CARD = (SLUG, "我们家最近搬家了", "Moving In · 最近……有没有……？",
        "vocab", "最近 · 搬家 · 邻居 · 烦人，加房子里的房间。"
                 "从上一课的路上回到家里——谁住在你旁边？")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我们家最近搬家了", "LESSON 1 OF 6", "第十五课 · 邻居",
        s_title("我们家最近搬家了", "Moving In",
                "Year 9 · Book 3 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 3 · p.142–144 · 第 1、3 题"))

    add("02-review.html", "Review · L14 被 + 怎么去", REV, "复习 · Lesson 14",
        label("认字快闪 · characters only · 一起读")
        + '  <div class="recall-grid" style="grid-template-columns:repeat(4,1fr);">\n'
        + "\n".join('    <div class="recall-cell" style="padding:16pt 8pt;">'
                    '<p class="recall-hanzi" style="font-size:30pt;">%s</p></div>' % w
                    for w in ["被", "偷", "警察", "身份证",
                              "坐几路车", "坐几站", "在哪站下车", "找到了"])
        + "\n  </div>\n"
        + '  <div class="task-box" style="margin-top:12pt;">\n'
          '    <p class="task-line"><b>白板</b> · 我说英文，你写中文——'
          '四句都用「被」。</p>\n'
          '    <p class="task-line" style="margin-top:6pt;"><b>转过去问同伴</b> · '
          '从你家怎么去学校？坐几路车？ 三十秒。</p>\n  </div>')

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say that we have recently moved house, and to describe "
               "what our neighbours are like.",
               [("I can say we moved recently", "能说：我们家最近搬家了"),
                ("I can name the rooms of a house",
                 "能说房间：书房 阳台 浴室 卧室 厨房 客厅 餐厅"),
                ("I can ask and answer 最近……有没有……？",
                 "能问也能答：你最近有没有……？"),
                ("I can say whether my neighbours are annoying",
                 "能说邻居怎么样：楼上的邻居很烦人")]))

    # ── Cycle 1 · 最近 / 搬家 ──
    add("04-c1-words.html", "Cycle 1 · A — 最近 / 搬家", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("最近", "zuìjìn", "recently", None),
                ("搬家", "bānjiā", "move house", "banjia")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我<b>最近</b>很忙。", "I've been busy recently."),
                    (None, "我们家<b>搬家</b>了。", "We've moved house."),
                    (None, "我们家<b>最近搬家</b>了，新家离学校很近。",
                     "We moved recently; the new place is near school.", True)],
                   "你们家最近搬家了吗？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我最近 ________ 。", "我们家 ________ 搬家。"],
                "用「因为……，所以……」写两个小句："
                "<b>我们家最近搬家了，因为爸爸的公司很远，所以我们搬到市中心。</b>"
                " 没搬过家的同学，说说你的朋友。"))

    # ── Cycle 2 · 邻居 / 烦人 ──
    add("07-c2-words.html", "Cycle 2 · A — 邻居 / 烦人", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("邻居", "línjū", "neighbour", "linju"),
                ("烦人", "fánrén", "annoying", None)))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "楼上的<b>邻居</b>很<b>烦人</b>。",
                     "The neighbours upstairs are annoying."),
                    (None, "我的<b>邻居</b>是中国人。", "My neighbour is Chinese."),
                    (None, "隔壁的<b>邻居</b>不<b>烦人</b>，可是楼上的<b>邻居</b>很<b>烦人</b>。",
                     "Next door aren't annoying, but upstairs are.", True)],
                   "你的邻居烦人吗？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我的邻居 ________ 。", "________ 的邻居很烦人。"],
                "用「虽然……，但是……」写一句："
                "<b>虽然楼上的邻居很烦人，但是隔壁的邻居对我们很好。</b>"
                " 同一句里说清楚是<b>楼上、楼下还是隔壁</b>。"))

    add("10-hanzi.html", "字 · 邻居 / 烦人 拆开看", IDO, "看字 · How the words are built",
        s_list("看字 · 两个词，各两个字——分开看就懂了",
               [("邻 · 旁边的 · 居 · 住", "住在我们旁边的人 —— 就是「邻居」"),
                ("烦 · 让人不舒服 · 人", "让人不舒服的 —— 就是「烦人」"),
                ("搬 · 把东西移走 · 家", "把整个家移走 —— 就是「搬家」"),
                ("「搬」不一定跟「家」", "搬桌子、搬椅子都可以说「搬」")],
               "「烦人」说的是<b>吵你的那个人</b>，不是<b>被吵的你</b>。"))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · 最近……有没有……？", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 问最近发生的事",
                  "你最近 + 有没有 + 动词……？",
                  [("你<b>最近有没有</b>搬家？", "Have you moved recently?"),
                   ("你<b>最近有没有</b>去新的地方？",
                    "Have you been anywhere new recently?"),
                   ("你<b>最近有没有</b>见到你的邻居？他们怎么样？",
                    "Have you seen your neighbours recently? What are they like?")],
                  "回答的时候把动词再说一遍："
                  "<b>有，我们上个月搬家了。／没有，我们没搬家。</b>"))
    add("12-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 问一件事，再问为什么",
                "你最近有没有住在很烦人的邻居旁边？他们做了什么？为什么烦人？",
                "Have you lived next to annoying neighbours recently? "
                "What did they do? Why were they annoying?",
                "三个问题连成一串——第一个用句型，后面两个逼对方多说几句。"))
    add("13-errors.html", "时间词放哪儿？", IDO, "注意 · The one to get right",
        s_errors([("我搬家最近了。", "我最近搬家了。", "时间词在动词<b>前面</b>"),
                  ("我烦人楼上的邻居。", "楼上的邻居很烦人。", "「烦人」是形容词，不是动词")],
                 "最近 在前，不在后",
                 "中文的时间词永远走在动词前面。这一节课会有人写反——先说在前面。"))

    add("14-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「最近」说的是过去还是将来？", "过去的比大拇指朝上"),
               ("白板：写「我们家最近搬家了」。", "写完举起来"),
               ("这句哪里错了？ 我搬家最近了。", "找出来，改过来"),
               ("举手：「邻居」里边，哪个字是「住」的意思？", "两个字，选一个")]))

    add("15-text1.html", "Text 1 · 前两句", IDO, "课文一 · p.142 · CD 57",
        s_text("课文一 · 前两句 · 先听，再一起读",
               "我们家最近搬家了。新房子很好，可是楼上的邻居很烦人。",
               "他们家什么时候搬家的？ · 新房子好不好？ · "
               "房子这么好，他为什么还是不高兴？",
               "「可是」是转折——听到「可是」，后面一定有问题。"))

    # ── Flexible practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("最近", None), ("搬家", "banjia"),
                   ("邻居", "linju"), ("烦人", None)],
                  "这块板整个活动一都留在屏幕上——写的时候可以看。"))
    add("17-task.html", "Activity 1 · 介绍我的新家", PRAC, "活动一 · We Do · 8 分钟",
        s_task("活动一 · 介绍我的新家 · 两人一组，一张课本 p.143 的房子图",
               ["情境：<b>你们家最近搬家了，这就是你的新房子。</b>",
                "说给同伴听，<b>四个生词都要用上</b>，"
                "再说<b>至少四个房间</b>：书房 阳台 浴室 卧室 厨房 客厅 餐厅。",
                "样子："],
               "把房子和<b>住在里面的人</b>连成一段话，五句以上——"
               "谁搬的家、什么时候搬的、哪个房间是谁的、哪个邻居烦人、他做了什么。"
               "每句都要用连词（<b>因为……所以……／可是／虽然……但是……</b>），"
               "而且不看总览板。说完，同伴用「最近……有没有……？」问你三个问题。",
               cn="我们家最近搬家了。楼下有客厅和厨房，楼上有三个卧室。"
                  "我的卧室有一个小阳台。我们的邻居很好，可是楼上的邻居很烦人。"))
    add("18-activity2.html", "Activity 2 · 我的邻居", PRAC, "活动二 · You Do · 8 分钟",
        s_list("活动二 · 写四句，说你自己的邻居 · 六分钟",
               [("我住在 ________ 。", None),
                ("我家 ________ 的邻居是 ________ 。", "楼上／楼下／隔壁／对面"),
                ("我的邻居 ________ 烦人。", "很／不／有一点儿"),
                ("我最近有没有见到我的邻居：________ 。", None)],
               "词库（楼上 楼下 隔壁 对面 附近）<b>不上屏</b>——"
               "老师走动，只发给需要的组。写完老师收三句读出来。"))
    add("19-activity2-ext.html", "Activity 2 · Extension", PRAC,
        "活动二 · 给写得快的同学",
        s_task("活动二 · Extension · 不要写四个句子，写<b>一段话</b>",
               ["一个你<b>喜欢</b>的邻居，一个很<b>烦人</b>的邻居，各说清楚为什么。",
                "最后加一句：<b>第一天见面，你会问新邻居什么？</b>（用中文写出那个问题）",
                "没有句型，没有词库，不看屏幕。"],
               cn="隔壁的邻居很好，因为他们常常帮我们。"
                  "可是楼上的邻居很烦人，他们晚上很吵。"))
    add("20-game.html", "Game · 抢词 Slap the Character", PRAC, "游戏 · 7 分钟",
        s_task("游戏 · 抢词 · 十六张卡片贴在黑板上，两人一组上来",
               ["卡片：最近 搬家 邻居 烦人 房子 阳台 卧室 厨房",
                "　　　客厅 餐厅 浴室 书房 楼上 楼下 隔壁 附近",
                "老师说<b>英文</b>，先摸到正确卡片的人得分。输的坐下，下一位上来。"],
               "给流利的同学：老师不说英文，说<b>中文定义</b>或者留一个空——"
               "「住在我们旁边的人」、「楼上的 ________ 很烦人」。"
               "摸到以后还要用这个词说一句话，不然不算分。"))

    add("21-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 请一位同学读四条 Success Criteria。",
                "<b>自评</b> · 每一条举手：会了 · 差不多 · 还要练。",
                "<b>出门条</b> · 白板写一句，走的时候给我看。",
                "<b>下节课</b> · 邻居到底做了什么？我们说说你半夜听见了什么。"],
               cn="出门条：用「最近」写一句话，说你们家或者你的邻居。"))

    return S
