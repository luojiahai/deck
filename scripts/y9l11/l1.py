# -*- coding: utf-8 -*-
"""Y9 L11 · Lesson 1 of 5 — snack nouns + 各种各样的……，比如……

Source: docs/lesson-plans/y9-l11/01-snack-nouns-mixed.md
Textbook pp.100-103 (Text 1, New Words, Act. 1, 2, 5); workbook p.118 (Ex. 1).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_title, s_lisc, label)

SLUG = "l1-snack-nouns"
TITLE = "Y9 L11 · 零食 Snacks · Lesson 1 of 5"

IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 零食 Snacks", "LESSON 1 OF 5", "第十一课 · 零食",
        s_title("零食", "Snacks", "Year 9 · Book 3 · Unit 4 · Lesson 11 · 50 minutes",
                "轻松学中文 3 · pp.100–103"))

    add("02-review.html", "Review · L10 canteen recap", "0–8 MIN · REVIEW",
        "复习 · Lesson 10",
        label("认字快闪 · flashcards, characters only")
        + '  <div class="recall-grid" style="grid-template-columns:repeat(4,1fr);">\n'
        + "\n".join('    <div class="recall-cell"><p class="recall-hanzi">%s</p></div>' % w
                    for w in ["糖果", "薯片", "薯条", "炸鸡翅", "盒饭", "咖喱", "猪排", "三明治"])
        + "\n  </div>\n"
        + '  <div class="task-box" style="margin-top:14pt;">\n'
          '    <p class="task-line"><b>白板四题</b> · 写「炸鸡翅」 · 翻译 Crisps are cheaper than a box lunch. · '
          '用「平时……，但是……」说今天的事 · 「不算太贵」是什么意思？</p>\n  </div>')

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("name the snacks we eat and to list examples of them in Chinese.",
               [("I can name six snack words in Chinese",
                 "能说出「零食」「巧克力」「蛋糕」「冰淇淋」「饼干」「各种各样」"),
                ("I can use 各种各样的……，比如：A、B、C 等 to list examples",
                 "能用「各种各样……比如」举例子"),
                ("I can say how much I like a snack — 非常／特别／挺／最／不太喜欢",
                 "能用五个程度词说自己爱吃什么")]))

    # ── Cycle 1 ──
    add("04-c1-words.html", "Cycle 1 · A — 零食 / 巧克力", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("零食", "língshí", "snack", "lingshi"),
                ("巧克力", "qiǎokèlì", "chocolate", "qiaokeli")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我很喜欢吃<b>零食</b>。", "I really like eating snacks."),
                    (None, "这块<b>巧克力</b>很好吃。", "This chocolate is delicious."),
                    (None, "我最喜欢的<b>零食</b>是<b>巧克力</b>。",
                     "My favourite snack is chocolate.", True)],
                   "你最喜欢的零食是什么？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我喜欢吃 ________ 。", "________ 很好吃。"],
                "用「比」写一句：<b>巧克力比薯片贵。</b> 再用「因为……，所以……」说你买哪一个。两句要连起来。"))

    # ── Cycle 2 ──
    add("07-c2-words.html", "Cycle 2 · A — 蛋糕 / 冰淇淋", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("蛋糕", "dàngāo", "cake", "dangao"),
                ("冰淇淋", "bīngqílín", "ice cream", "bingqilin")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我妈妈会做<b>蛋糕</b>。", "My mum can make cakes."),
                    (None, "夏天我常常吃<b>冰淇淋</b>。", "In summer I often eat ice cream."),
                    (None, "我不太喜欢<b>蛋糕</b>，我最喜欢<b>冰淇淋</b>。",
                     "I don't much like cake; ice cream is my favourite.", True)],
                   "夏天你常常吃什么？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我常常吃 ________ 。", "我不太喜欢 ________ 。"],
                "用「比」写两句，比较冰淇淋和蛋糕：哪个好吃？哪个便宜？"
                "然后说你买哪个，为什么。<b>不看屏幕。</b>"))

    # ── Cycle 3 ──
    add("10-c3-words.html", "Cycle 3 · A — 饼干 / 各种各样", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("饼干", "bǐnggān", "biscuit; cracker", "binggan"),
                ("各种各样", "gèzhǒng gèyàng", "all kinds of", None)))
    add("11-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "这家店卖<b>饼干</b>。", "This shop sells biscuits."),
                    (None, "这家店卖<b>各种各样</b>的零食。", "This shop sells all kinds of snacks."),
                    (None, "我妈妈买了<b>各种各样</b>的<b>饼干</b>。",
                     "My mum bought all kinds of biscuits.", True)],
                   "「各种各样」跟第十课的「各种」有什么不一样？"))
    add("12-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["这家店卖各种各样的 ________ 。"],
                "写一句比较两家店：<b>这家店的饼干比超市的便宜。</b> "
                "再用「因为……，所以……」说你为什么去那家店买。"))

    add("13-recall.html", "Checkpoint · 认字 recall", IDO, "检查点 · Checkpoint",
        s_recall(["零食", "巧克力", "蛋糕", "冰淇淋", "饼干", "各种各样"],
                 "六个字一起读出来。读不出来的，我们再教一遍 —— 不往下走。"))

    add("14-pattern.html", "I Do · 句型 各种各样……比如……", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 各种各样的 + N，比如：A、B、C 等。",
                  "各种各样的 ____ ，比如：A、B、C 等。",
                  [("这家超市卖各种各样的零食，比如巧克力、糖果等。",
                    "This supermarket sells all kinds of snacks — chocolate, sweets and so on."),
                   ("我每天都吃各种各样的零食，比如：饼干、薯片等。",
                    "I eat all kinds of snacks every day — biscuits, crisps and so on."),
                   ("这个菜市场卖各种各样的新鲜蔬菜，比如西红柿、黄瓜等。",
                    "This market sells all kinds of fresh vegetables — tomatoes, cucumbers and so on.")],
                  "新词：<b>比如</b> bǐrú <i>for example</i> —— 它打开单子，「等」把单子关上。"))

    add("15-pattern2.html", "I Do · 最难的一句 the hardest one", IDO, "句型 · 难句 · two clauses",
        s_focus("再难一点 · 两个分句 · 「比」是第十课学的",
                "我们学校的小卖部卖<b>各种各样</b>的东西，<b>比如</b>三明治、盒饭、饮料等，"
                "可是那里的东西<b>比</b>外面贵。",
                "Our tuck shop sells all sorts — sandwiches, box lunches, drinks — "
                "but the things there are dearer than outside.",
                "两件事：先说卖什么，再说贵不贵。「可是」把两个分句连起来。",
                "照这个样子说你家附近的一家店 —— 卖什么，比如什么，再比一比价钱。不写，直接说。"))

    add("16-degrees.html", "I Do · 程度词 how much you like it", IDO, "程度词 · Degree phrases",
        label("五个程度词 · 从最喜欢到不太喜欢 · 课本 p.101")
        + '  <div class="ladder">\n'
        + "\n".join(
            '    <div class="rung%s">%s</div>%s' % (
                "", w, '\n    <span class="arrow">›</span>' if i < 4 else "")
            for i, w in enumerate(["非常喜欢", "特别喜欢", "挺喜欢", "最喜欢", "不太喜欢"]))
        + "\n  </div>\n"
        + '  <div class="task-box" style="margin-top:18pt;">\n'
          '    <p class="task-cn">我<b>非常</b>喜欢吃巧克力。我每天都吃巧克力。可是我<b>不太</b>喜欢糖果。</p>\n'
          '    <p class="task-line" style="margin-top:8pt;">两三句，不是一句 —— 说了喜欢，还要说你怎么吃它。</p>\n  </div>')

    add("17-text1.html", "课文一 · Text 1 (CD 41)", IDO, "课文一 · Text 1 · p.100",
        label("课文一 · 先听一遍（CD 41），再一起读")
        + '  <div class="frame-box">\n'
          '    <p class="frame-line" style="font-size:26pt;line-height:1.6;">'
          '我特别喜欢吃<b>零食</b>。我每天都吃<b>各种各样</b>的<b>零食</b>，<b>比如</b>：糖果、'
          '<b>巧克力</b>、薯片、<b>蛋糕</b>、<b>冰淇淋</b>、<b>饼干</b>等。我还喜欢喝汽水。</p>\n'
          '  </div>\n'
        + '  <div class="task-box" style="margin-top:14pt;">\n'
          '    <p class="task-line"><b>用中文回答</b> · 1 他每天吃什么？ · 2 他喜欢喝什么？ · '
          '3 课文里有几种零食？请说出来。</p>\n'
          '    <p class="task-line" style="margin-top:6pt;">'
          '后面的「对牙齿不好 / 从小就 / 总是」下节课再学。</p>\n  </div>')

    add("18-summary.html", "词汇总览 · summary board", PRAC, "词汇总览 · Summary board",
        s_summary([("零食", "lingshi"), ("巧克力", "qiaokeli"), ("蛋糕", "dangao"),
                   ("冰淇淋", "bingqilin"), ("饼干", "binggan"), ("各种各样", None)],
                  "这块板留在屏幕上 —— 下面的任务要用到每一个词。"))

    add("19-task.html", "We Do · 任务 七家店 (Act. 5)", PRAC, "任务 · 课本 p.103 · Act. 5",
        s_task("We Do · 每家店说一句 · 两人一组 · 4 分钟",
               ["<b>七家店：</b>服装店 · 肉店 · 水果店 · 餐厅 · 文具店 · 家具店 · 电器店",
                "<b>第八家是你们学校的小卖部</b> —— 那一句要用到总览板上<b>每一个</b>词。"],
               "三句，不看总览板。第一句用「各种各样……比如」，第二句用「比」比较两种零食的价钱，"
               "第三句用「因为……，所以……」说你为什么常买那一种。写完念给同桌，同桌要问你一个问题。",
               "例：这家超市卖各种各样的零食，比如巧克力、糖果等。"))

    add("20-act1.html", "You Do · 课本 Act. 1 picture talk", PRAC, "活动二 · 课本 p.101 · Act. 1",
        s_task("You Do · 八张图，每张两三句 · 两人轮流 · 7 分钟",
               ["图上有：鸡翅·鸡腿 · 猪肉·牛肉·羊肉 · 水果·薯片 · 巧克力·糖果 · "
                "冰淇淋·饮料 · 蛋糕·饼干 · 西红柿·黄瓜 · 香蕉·苹果",
                "每一句都要用一个程度词。第一轮程度词留在黑板上，第二轮擦掉。"],
               "不是 B 自己挑程度词 —— A 指定（「用『挺喜欢』」），B 当场说三句，"
               "最后一句一定要用「比如」举两个例子。说完交换，A 拿 B 觉得最难的那张图。",
               "我非常喜欢吃巧克力。我每天都吃巧克力。可是我不太喜欢糖果。"))

    add("21-act2.html", "You Do · 课本 Act. 2 + 练习册 Ex. 1", PRAC,
        "活动三 · 课本 p.102 · Act. 2",
        s_task("You Do · 写五句 · 练习本 · 5 分钟",
               ["<b>句型：</b>程度词 + 比如 + 至少三样东西 + 等。",
                "第一句课本已给（说衣服），所以<b>五句不能全说吃的</b> —— 要回到第一册第五单元的词。",
                "写完的同学做<b>练习册 p.118 Ex. 1</b>：十二张零食图，写汉字（「炸鸡翅」已给）。"],
               "五句里至少两句不是说吃的 —— 一句说文具，一句说学校的科目（第三单元的词）。"
               "再加第六句，用「各种各样」说你的书包里有什么。",
               "我特别喜欢买衣服，比如连衣裙、汗衫、毛衣、牛仔裤等。"))

    add("22-game.html", "Game · 拍字 Slap the Character", PRAC, "游戏 · 拍字 · 5 分钟",
        s_task("Game · 拍字 Slap the Character",
               ["黑板上十二张字卡：今天的六个词 + 糖果 · 薯片 · 薯条 · 炸鸡翅 · 盒饭 · 三明治",
                "两个同学上来，老师说词，他们拍。赢的留下。"],
               "老师不说词了 —— 说中文提示（「这个东西很甜，是黑色的」→ 巧克力），"
               "或者说一句缺词的话。两轮以后，让说得最好的同学自己来出提示。"))

    add("23-plenary.html", "Plenary · exit ticket & preview", "43–50 MIN · PLENARY",
        "小结 · Plenary",
        s_list("小结 · 43–50 分钟",
               [("<b>回看目标</b> · 请一位同学读三条 Success Criteria，第二条用中文读。", ""),
                ("<b>自评</b> · 每条 👍 / 😐 / 👎 —— 第二条有多少人举 😐？", ""),
                ("<b>Exit ticket</b> · 用「各种各样」和「比如」写一句：你家里有什么零食。",
                 "写在白板上，出门的时候举起来给我看。"),
                ("<b>下节课</b> · 学怎么说「吃太多糖果对牙齿不好」，还有「我从小就……」。", "")]))
    return S
