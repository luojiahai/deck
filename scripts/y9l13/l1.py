# -*- coding: utf-8 -*-
"""Y9 L13 · Lesson 1 of 6 — 市中心 / 方便 / 生活 / 邮局 + A 离 B 远／不远

Source: docs/lesson-plans/y9-l13/01-where-i-live-mixed.md
Textbook p.122 (Text 1, first half), p.124 Act. 2. Workbook p.145 Ex. 4
supplies two of the six Sentence Jumble sets.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_errors,
                   s_title, s_lisc, label)

SLUG = "l1-where-i-live"
TITLE = "Y9 L13 · 社区 Neighbourhood · Lesson 1 of 6"
CARD = (SLUG, "我家住在哪儿", "Where I Live · 离 + distance",
        "vocab", "市中心 · 生活 · 方便 · 邮局，加「A 离 B 远／不远」。采访同伴，再用第三人称报告。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我家住在哪儿", "LESSON 1 OF 6", "第十三课 · 社区",
        s_title("我家住在哪儿", "Where I Live",
                "Year 9 · Book 3 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 3 · p.122 · 课文一"))

    add("02-review.html", "Review · L12 外出就餐 recap", REV, "复习 · Lesson 12",
        label("认字快闪 · flashcards, characters only · 一起读")
        + '  <div class="recall-grid">\n'
        + "\n".join('    <div class="recall-cell"><p class="recall-hanzi">%s</p></div>' % w
                    for w in ["饭店", "自助餐", "服务员", "菜单", "点菜", "好吃"])
        + "\n  </div>\n"
        + '  <div class="task-box" style="margin-top:14pt;">\n'
          '    <p class="task-line"><b>白板</b> · 写一句：给全桌点两杯绿茶、一瓶可乐。'
          '（来 + 数量 + 杯／瓶）</p>\n  </div>')

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say where we live and how far it is from the places we go.",
               [("I can say where I live", "能说出我家住在哪儿"),
                ("I can use A 离 B 远／不远／很近 to talk about distance",
                 "能用「A 离 B 远／不远」说距离"),
                ("I can say whether life where I live is convenient",
                 "能说我住的地方生活方不方便")]))

    # ── Cycle 1 · 市中心 / 方便 ──
    add("04-c1-words.html", "Cycle 1 · A — 市中心 / 方便", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("市中心", "shì zhōngxīn", "city centre", "shizhongxin"),
                ("方便", "fāngbiàn", "convenient", None)))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我家住在<b>市中心</b>。", "I live in the city centre."),
                    (None, "在我家买东西很<b>方便</b>。",
                     "Buying things where I live is very convenient."),
                    (None, "我家在<b>市中心</b>，买东西很<b>方便</b>。",
                     "My home is in the city centre, so shopping is convenient.", True)],
                   "你家在市中心吗？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家住在 ________ 。", "在我家 ________ 很方便。"],
                "用「因为……，所以……」写一句：<b>因为我家住在市中心，所以买东西很方便。</b> "
                "再写一件<b>不</b>方便的事。"))

    # ── Cycle 2 · 生活 / 邮局 ──
    add("07-c2-words.html", "Cycle 2 · A — 生活 / 邮局", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("生活", "shēnghuó", "life", None),
                ("邮局", "yóujú", "post office", "youju")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我很喜欢我的<b>生活</b>。", "I like my life a lot."),
                    (None, "<b>邮局</b>就在学校旁边。",
                     "The post office is right beside the school."),
                    (None, "我家旁边有<b>邮局</b>，<b>生活</b>很方便。",
                     "There's a post office beside my home, so life is convenient.", True)],
                   "你家附近有邮局吗？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我家旁边有 ________ 。", "我的生活 ________ 。"],
                "写两句，要连起来：我家附近有 ________ ，<b>可是</b>没有 ________ ，"
                "<b>所以</b> ________ 。"))

    add("10-recall.html", "Recall · 四个生词", IDO, "认一认 · Checkpoint",
        s_recall(["市中心", "方便", "生活", "邮局"],
                 "读不出来就回去重教——别往下走。", cols=4))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · A 离 B 远／不远", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说距离",
                  "A + 离 + B + 很近／不远／很远",
                  [("我家离学校很近。", "My home is very close to school."),
                   ("邮局离我家不远。", "The post office is not far from my home."),
                   ("我家离市中心很远，坐车三十分钟。",
                    "My home is far from the city centre — thirty minutes by car.")],
                  "顺序：<b>要量的地方</b>在前，<b>起点</b>在后。不是「离我家邮局不远」。"))
    add("12-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 距离 + 时间 + 原因",
                "我家离市中心不远，走路十分钟就到了，所以生活很方便。",
                "My home isn't far from the city centre — ten minutes' walk — "
                "so life here is convenient.",
                "三段：距离 → 要走多久 → 所以怎么样。今天的四个生词用了三个。"))

    add("13-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「方便」是什么意思？", "会的举手，不太确定的手放平"),
               ("白板：写「邮局离我的学校不远」。", "Write it in characters"),
               ("这句哪里错了？ 我家离很远学校。", "找出来，改过来"),
               ("你家离学校远吗？", "点名两位同学，用中文回答")]))

    # ── Flexible practice ──
    add("14-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("市中心", "shizhongxin"), ("方便", None),
                   ("生活", None), ("邮局", "youju")],
                  "这块板整个活动都留在屏幕上——写的时候可以看。"))
    add("15-task.html", "Activity 1 · 我住的地方", PRAC, "活动一 · We Do · 7 分钟",
        s_task("活动一 · 我住的地方 · 四句话，四个生词都要用上",
               ["1 · 我家住在 ________ 。",
                "2 · 我家离学校 ________ 。",
                "3 · 我家离市中心 ________ 。",
                "4 · 我家 ________ 有邮局／没有邮局，生活 ________ 。"],
               "不写四句，写<b>一段</b>——用「因为……所以……」和「可是」连起来，"
               "最后加一句：<b>如果我家附近有 ________ ，生活就更方便了。</b> 不看屏幕。"))

    add("16-interview.html", "Activity 2 · 采访同伴", PRAC, "活动二 · You Do · 10 分钟",
        s_list("活动二 · 采访同伴，然后向全班报告（课本 p.124 第 2 题）",
               [("你们学校离你家远吗？你每天怎么上学？", "A 问 B，然后换过来"),
                ("你家离市中心远吗？你怎么去市中心？", None),
                ("你家住的地方生活方便吗？附近有什么商店？", None),
                ("报告：用<b>第三人称</b>说同伴的答案", "他们学校离他家不远。他每天走路上学。")],
               "报告是重点——不是复述自己的答案，是说<b>同伴</b>的。取四五位。"))

    add("17-game.html", "Game · 句子拼图 Sentence Jumble", PRAC, "游戏 · 6 分钟",
        s_task("游戏 · 句子拼图 · 六组卡片，六张桌子，拼完换桌",
               ["这是课本练习册 p.145 第 4 题——也是<b>单元测验第四部分</b>的题型。",
                "两组用书上的原题：",
                "　· 住 / 我家 / 市中心 / 在 / 。",
                "　· 很远 / 邮局 / 市政大楼 / 离 / 。",
                "其余四组用今天的词自己编。"],
               "两个信封里是<b>两句连起来</b>的长句（我家离市中心不远，走路十分钟就到了），"
               "而且<b>多一张用不上的卡片</b>——要说出是哪一张、为什么。",
               cn="「市政大楼」下节课才学——让他们从「市」和「大楼」猜。"))

    add("18-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 请一位同学用中文读三条 Success Criteria。",
                "<b>自评</b> · 每一条举手：会了 · 差不多 · 还要练。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下节课</b> · 我们看看家附近有什么——银行、诊所、百货公司。"],
               cn="出门条：写一句 —— 我家离 ____________ 。"))

    return S
