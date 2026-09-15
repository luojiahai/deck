# -*- coding: utf-8 -*-
"""Y9 L12 · Lesson 2 of 6 — 烤/牛排/甜品/奶酪/饱 + V得很adj + Text 1

Source: docs/lesson-plans/y9-l12/02-desserts-text1-mixed.md
Textbook pp.110-112 (Text 1 complete, Act. 1 甜品 half, Act. 3); workbook p.131 (Ex. 8).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_text, s_dialogue,
                   s_title, s_lisc, label)

SLUG = "l2-desserts-text1"
TITLE = "Y9 L12 · 外出就餐 Eating Out · Lesson 2 of 6"

IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 烤牛排和甜品", "LESSON 2 OF 6", "第十二课 · 外出就餐",
        s_title("甜品", "Roast, Steak and Desserts",
                "Year 9 · Book 3 · Unit 4 · Lesson 12 · 50 minutes",
                "轻松学中文 3 · pp.110–112"))

    add("02-review.html", "Review · L1 recap", "0–8 MIN · REVIEW", "复习 · 第一节课",
        s_task("复习 · 两人对话 90 秒，然后交换",
               ["A：你们去吃自助餐了吗？吃了什么？",
                "B：回答，至少用两个词（自助餐 · 龙虾 · 三文鱼 · 寿司）。",
                "然后<b>白板快写</b>：老师放图，写汉字，不许写拼音。"]))

    add("03-review-sort.html", "Review · WB Ex. 8 categorise (test format)",
        "0–8 MIN · REVIEW", "复习 · 分类 · 考试题型",
        s_task("分类 · 三分钟 · 这是第四单元测验第一题的题型",
               ["两人一组，写在白板上，分成六类。",
                "分完以后，老师挑两个问：<b>为什么？</b>（用中文回答）"],
               cn="龙虾 糖果 猪肉 热狗 面条 香肠 牛排 蛋糕 盒饭 红豆汤 汉堡包 三文鱼 巧克力 冰淇淋 三明治"
                  "<br><br>海鲜 · 零食 · 肉类 · 快餐 · 中餐 · 甜品"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("talk about desserts at a buffet and say how full we are.",
               [("I can use 烤 with a dish", "能用「烤」说一道菜"),
                ("I can name three desserts in Chinese", "能说出三种甜品"),
                ("I can say how much someone ate using 吃得很饱", "能用「得」说吃了多少")]))

    # ── Cycle 1 ──
    add("05-c1-words.html", "Cycle 1 · A — 烤 / 牛排", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("烤", "kǎo", "bake; roast", "kao"),
                ("牛排", "niúpái", "beefsteak", "niupai")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "这家饭店的<b>烤</b>牛排做得最好吃。",
                     "This restaurant's roast beefsteak is the best."),
                    (None, "我爸爸每次都要吃<b>牛排</b>。", "My dad has steak every time."),
                    (None, "我们上个周末吃了<b>烤牛排</b>和龙虾。",
                     "Last weekend we ate roast beefsteak and lobster.", True)],
                   "「烤」字左边是什么？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我（喜欢／不喜欢）吃烤 ________ 。"],
                "「烤」可以配很多词——烤鱼、烤鸡、烤面包。写两句，用不同的食物；再写一句用「比」比较它们。"))

    # ── Cycle 2 ──
    add("08-c2-words.html", "Cycle 2 · A — 甜品 / 奶酪", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("甜品", "tiánpǐn", "dessert", "tianpin"),
                ("奶酪", "nǎilào", "cheese", "nailao")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我们还吃了很多<b>甜品</b>。", "We also ate a lot of desserts."),
                    (None, "<b>奶酪</b>蛋糕很甜。", "Cheesecake is very sweet."),
                    (None, "<b>甜品</b>有<b>奶酪</b>蛋糕、巧克力蛋糕和水果沙拉。",
                     "For dessert there is cheesecake, chocolate cake and fruit salad.", True)],
                   "你最喜欢哪个甜品？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["甜品我最喜欢吃 ________ 。"],
                "写一句用「除了……以外」：<b>除了奶酪蛋糕以外，我还喜欢吃冰淇淋。</b>"))

    # ── Cycle 3 ──
    add("11-c3-words.html", "Cycle 3 · A — 饱", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("饱（飽）", "bǎo", "full", None),
                ("饣 = 食", "shí", "the food radical — 饱、饿、饭、饼 all have it", None)))
    add("12-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "我们都吃得很<b>饱</b>。", "We all ate until we were full."),
                    (None, "我吃了两个龙虾，现在很<b>饱</b>。",
                     "I ate two lobsters — I'm full now."),
                    (None, "甜品太多了，我吃得非常<b>饱</b>。",
                     "There were too many desserts; I'm absolutely stuffed.", True)],
                   "「饱」的反义词是什么？下个星期学。"))
    add("13-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["我吃了 ________ ，吃得很饱。"],
                "「饱」的反义词是「饿」——从「饣」猜猜看。写一句，两个词都要用上："
                "<b>我去饭店的时候很饿，吃完以后很饱。</b>"))

    add("14-recall.html", "Recall · 认一认", IDO, "认字 · characters only",
        s_recall(["烤", "牛排", "甜品", "奶酪", "饱"],
                 "读不出来就回头再教一遍，不要往下走。", cols=5))

    # ── Pattern ──
    add("15-pattern.html", "Pattern · V 得 很 adj", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说做得怎么样",
                  "动词 + 得 + 很／非常 + 形容词",
                  [("我们都吃得很饱。", "We all ate until we were full."),
                   ("他吃得很快。", "He eats fast."),
                   ("他们的烤牛排做得非常好吃。",
                    "They make the roast beefsteak really well.")],
                  "「得」把动词和<b>做得怎么样</b>连起来。不是 ✗我很饱吃。"))
    add("16-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 两个分句", "那家饭店的菜做得好吃，但是挺贵的。",
                "That restaurant cooks well, but it's fairly expensive.",
                "两个分句，用「但是」连起来，后半用「挺……的」。"))

    add("17-text1.html", "Text 1 · p.110 · CD 45", IDO, "课文一 · Text 1",
        s_text("课文一 · 课本 p.110 · CD 45",
               "我们一家三口上个周末去吃自助餐了。我们吃了龙虾、三文鱼、寿司、烤牛排、炒面等。"
               "我们还吃了很多甜品，有奶酪、巧克力蛋糕和水果沙拉。我们都吃得很饱。"
               "我们一共花了三百多块，挺便宜的。",
               "他们家有几口人？ · 他们吃了什么甜品？ · 三百多块贵不贵？他们觉得呢？",
               "老师先读，全班跟读，然后一起读一遍。"))

    add("18-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「饱」的意思是什么？", "Thumbs up if you know"),
               ("怎么说 cheese？", "写在小白板上"),
               ("这句话对不对？ ✗ 我们都很饱吃。", "怎么改？"),
               ("「烤」字左边是什么部分？它跟什么有关系？", "点名回答")]))

    # ── Practice ──
    add("19-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("烤", "kao"), ("牛排", "niupai"), ("甜品", "tianpin"),
                   ("奶酪", "nailao"), ("饱", None)],
                  "这一页留在屏幕上——活动二要用。"))

    add("20-act1.html", "Activity 1 · The buffet dialogue (We Do, 8 min)", PRAC,
        "活动一 · We Do · 8 分钟",
        s_dialogue("活动一 · 课本 p.112 第 3 题 · 两人一组，做两遍，第二遍不看稿",
                   [("A", "我们星期天下午去红山饭店吃自助餐了。"),
                    ("B", "你们吃了什么？喝了什么？"),
                    ("A", "我们吃了甜品，有蛋糕、饼干、冰淇淋等。我们还吃了寿司、炒面和炒饭。"),
                    ("B", "有水果吗？"),
                    ("A", "当然有。我们吃了西瓜、苹果和香蕉。"),
                    ("B", "在那里吃饭贵不贵？"),
                    ("A", "还可以，每位一百五十块。")],
                   "<b>加难</b>：B 是美食评论员。问三个稿上没有的问题（什么菜做得最好吃？"
                   "人多不多？排队了吗？），A 每个答案都要带「因为……所以……」。"))

    add("21-act2.html", "Activity 2 · The dessert table (You Do, 9 min)", PRAC,
        "活动二 · You Do · 9 分钟",
        s_task("活动二 · 写一写自助餐的甜品那一半",
               ["一个人写，写在练习本上，至少四句。",
                "五个生词<b>都要用上</b>：烤了什么、甜品有什么（甜品、奶酪）、主食是什么（牛排）、大家吃得怎么样（饱）。"],
               "写别人，不写自己——用第三人称，再加上钱：<b>他们一家四口一共花了……块。</b> "
               "然后评一句：挺便宜的 还是 挺贵的？用「因为……所以……」说为什么。<b>不看总览页。</b>",
               cn="上个周末我们一家去吃自助餐了。主食有烤牛排……甜品有奶酪蛋糕……我们都吃得很饱。"))

    add("22-game.html", "Game · Odd One Out (5 min)", PRAC, "游戏 · 找不同 · 5 分钟",
        s_list("游戏 · Odd One Out · 用中文说为什么",
               [("龙虾 · 三文鱼 · 奶酪", "奶酪不是海鲜。"),
                ("甜品 · 蛋糕 · 牛排", "牛排不是甜品。"),
                ("烤牛排 · 炒面 · 冰淇淋", "冰淇淋是甜品。"),
                ("<b>加难</b>：理由里一定要有「因为」", "后面几轮不许重复前面用过的分类——要找第二个不同点。")],
               "六张图卡打印好放在黑板上。"))

    add("23-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 全班一起用中文念三条。",
                "<b>自评</b> · 白板上写 👍 / 😐 / 👎，一条一条举起来。",
                "<b>出门条</b> · 翻译成中文。",
                "<b>下节课</b> · 我们用二百块去买菜——要买给你们一家人吃。"],
               cn="出门条：翻译成中文 —— <i>We all ate until we were very full.</i>"))
    return S
