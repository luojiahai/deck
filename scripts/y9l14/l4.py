# -*- coding: utf-8 -*-
"""Y9 L14 · Lesson 4 of 6 — 手提包 / 钱包 / 钥匙 / 手机 / 现金 / 服装

Source: docs/lesson-plans/y9-l14/04-whats-in-the-bag-mixed.md
Textbook p.138 Act. 7 (the chained dialogue). Workbook p.159 Ex. 12 (as the
Review), p.160 Ex. 15.

服装 sits here rather than in Lesson 6 so that 四彩服装店 is already known
when Text 2 arrives next lesson. All six words are concrete, so all six
carry a drawing.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_title, s_lisc, label)

SLUG = "l4-whats-in-the-bag"
TITLE = "Y9 L14 · 问路 Asking the Way · Lesson 4 of 6"
CARD = (SLUG, "包里有什么", "What's In The Bag",
        "vocab", "手提包 · 钱包 · 钥匙 · 手机 · 现金 · 服装。"
                 "「……里有……、……和……」，再用「除了……以外，还有……」加一样。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 包里有什么", "LESSON 4 OF 6", "第十四课 · 问路",
        s_title("包里有什么", "What's In The Bag",
                "Year 9 · Book 3 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 3 · p.138 · 第 7 题"))

    add("02-review.html", "Review · 白板五题 + 补上地图那一段", REV,
        "复习 · Lessons 1–3",
        s_task("复习 · 前三分钟白板，后五分钟本子",
               ["<b>白板五题</b>，一题一举：",
                "　1 · 写 —— I'll either cycle or take the bus.",
                "　2 · 写 —— How many stops?　　3 · 一 ____ 桥",
                "　4 · 写 —— It's about fifteen minutes on foot.",
                "　5 · 从我家去机场，你要 ________ 。（自己接完）",
                "<b>本子</b> · 练习册 p.159 第 12 题——地图上再加三座建筑，写一段怎么去其中一个。"],
               cn="第 12 题收上来——这是上节课口语课的书面凭证。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what is inside a bag, a wallet or a pocket, "
               "with the right measure words.",
               [("I can name what I carry", "能说我带什么：手提包、钱包、钥匙、手机、现金"),
                ("I can list three or more things in one sentence",
                 "能一句话说三样东西：……里有……、……和……"),
                ("I can add something extra with 除了……以外，还有……",
                 "能用「除了……以外，还有……」再加一样")]))

    # ── Cycle 1 · 手提包 / 钱包 ──
    add("04-c1-words.html", "Cycle 1 · A — 手提包 / 钱包", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("手提包", "shǒutíbāo", "handbag", "shoutibao"),
                ("钱包", "qiánbāo", "wallet; purse", "qianbao")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "妈妈的<b>手提包</b>很大。", "Mum's handbag is big."),
                    (None, "我的<b>钱包</b>在书包里。",
                     "My wallet's in my school bag."),
                    (None, "<b>钱包</b>在<b>手提包</b>里，<b>手提包</b>在车上。",
                     "The wallet's in the handbag and the handbag's in the car.",
                     True)],
                   "「书包」「面包」「钱包」——哪一个不是包？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我的钱包在 ________ 里。", "________ 里有我的钱包。"],
                "写三样东西各在哪儿，连成一段。"
                "最后一句：哪一样丢了你最难过？为什么？"))

    # ── Cycle 2 · 钥匙 / 手机 ──
    add("07-c2-words.html", "Cycle 2 · A — 钥匙 / 手机", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("钥匙", "yàoshi", "key", "yaoshi"),
                ("手机", "shǒujī", "mobile phone", "shouji")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我有两把<b>钥匙</b>。", "I've got two keys."),
                    (None, "我的<b>手机</b>是新的。", "My phone is new."),
                    (None, "我的<b>手机</b>和<b>钥匙</b>都在钱包旁边。",
                     "My phone and my keys are both beside the wallet.", True)],
                   "「钥匙」第二个字是轻声——再读一遍。"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我的手机在 ________ ，钥匙在 ________ 。"],
                "用「一……就……」写一句：<b>我一到家就把钥匙放在桌子上。</b>"
                " 再写一句：<b>没这么做的那天呢？</b>"))

    # ── Cycle 3 · 现金 / 服装 ──
    add("10-c3-words.html", "Cycle 3 · A — 现金 / 服装", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("现金", "xiànjīn", "cash", "xianjin"),
                ("服装", "fúzhuāng", "clothing", "fuzhuang")))
    add("11-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "我有一百块<b>现金</b>。", "I've got a hundred yuan in cash."),
                    (None, "我妈妈在<b>服装</b>店工作。",
                     "My mum works in a clothes shop."),
                    (None, "我在<b>服装</b>店买衣服，付了两百块<b>现金</b>。",
                     "I bought clothes at the clothes shop and paid 200 in cash.",
                     True)],
                   "「现金」的「金」是金子。「钱」的左边也是金字旁——钱的字都带金属。"))
    add("12-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["我（有／没有）现金，我常常在 ________ 买 ________ 。"],
                "用「比」写一句：<b>在服装店买衣服比在百货公司便宜。</b>"
                " 再用「因为……所以……」说为什么。"))

    add("13-recall.html", "Recall · 六个生词", IDO, "认一认 · Checkpoint",
        s_recall(["手提包", "钱包", "钥匙", "手机", "现金", "服装"],
                 "读不出来就回去重教——「钥匙」最容易读错。", cols=3))

    # ── Pattern ──
    add("14-pattern.html", "Pattern · ……里有……", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 一句话说三样东西",
                  "地方 + 里有 + 东西、东西 和 东西",
                  [("我的书包里有书、本子和文具盒。",
                    "My school bag has books, exercise books and a pencil case."),
                   ("钱包里有两百多块现金。",
                    "There's over two hundred yuan in the wallet."),
                   ("手提包里有钱包、钥匙和手机。",
                    "The handbag has a wallet, keys and a phone.")],
                  "中间用顿号「、」，<b>只有最后一样前面用「和」</b>。"
                  "「两百<b>多</b>块」——整数后面加「多」，就是「超过」。"))
    add("15-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 一串东西，再加一样",
                "我的手提包里除了钱包、钥匙和手机以外，还有一本书和一瓶水。",
                "Apart from my wallet, keys and phone, my handbag also has "
                "a book and a bottle of water.",
                "「除了……以外」后面<b>一定</b>要有「还」或者「也」。"
                "这是三年级第二单元学过的，今天拿来用。"))

    add("16-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「钥匙」怎么读？", "全班两遍，注意第二个字的声调"),
               ("白板：写「我的钱包里有……」，三样东西，用「、」和「和」。", None),
               ("这句哪里错了？ 我的手提包里有钱包和钥匙和手机。", "找出来，改过来"),
               ("举手：谁的书包里有手机？", "用一句中文说说还有什么")]))

    # ── Flexible practice ──
    add("17-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("手提包", "shoutibao"), ("钱包", "qianbao"), ("钥匙", "yaoshi"),
                   ("手机", "shouji"), ("现金", "xianjin"), ("服装", "fuzhuang")],
                  "这块板整个活动都留在屏幕上——写的时候可以看。"))
    add("18-task.html", "Activity 1 · 我的购物日", PRAC, "活动一 · We Do · 6 分钟",
        s_task("活动一 · 我的购物日 · 四到六句，<b>六个生词都要用上</b>",
               ["本子上写。念的时候，全班用手指数听见了几个。", "开头可以这样："],
               "写成一件<b>出事</b>的事：到收银台才发现少了一样东西。"
               "还是那六个词，可是要用「可是」「因为……所以……」「……的时候」连起来，"
               "最后说你怎么办的。不看屏幕。",
               cn="今天我去服装店买衣服。我带了手提包……"))
    add("19-chain.html", "Activity 2 · 包里有什么 · 接龙", PRAC,
        "活动二 · You Do · 8 分钟",
        s_list("活动二 · 课本 p.138 第 7 题 · 两人一组，六个地方轮着来",
               [("书包里有什么？ → 钱包里有什么？ → 文具盒里有什么？",
                 "每个答案至少说三样东西"),
                ("六个地方：汉语教室 · 学校 · 学校的图书馆 · 家的客厅 · 你的房间 · 家的厨房",
                 None),
                ("做到一半，屏幕上的句型<b>撤掉</b>——后面三个自己说", None),
                ("最后两分钟：本子上做练习册 p.160 第 15 题，八个衣服、配件的词", None)],
               "问的人记账，最后<b>站起来</b>用第三人称向全班报告，"
               "顺便说这说明了什么：<b>他的书包里除了书以外，还有三个足球。"
               "我觉得他每天都踢球。</b>"))
    add("20-game.html", "Game · 记忆袋 + 两真一假", PRAC, "游戏 · 9 分钟",
        s_task("游戏 · 两段",
               ["<b>第一段（4 分钟）· 记忆袋</b> —— 真袋子倒出八样东西，看三十秒，盖上。"
                "白板上写下你记得的，写<b>汉字</b>，一个一分。",
                "<b>第二段（5 分钟）· 两真一假</b> —— 四人一组，每人说三句自己包里的东西，"
                "两句真一句假。",
                "　　我的包里有两把钥匙。 我的钱包里有五十块现金。 我有两个手机。",
                "组里投票哪句是假的。骗过组里一分，猜中一分。"],
               "给流利的同学：三句话要用<b>三种不同的说法</b>——"
               "一句带量词和数字，一句用「除了……以外」，一句用「可是」。"
               "投票前组里还可以用中文追问一个问题。"))

    add("21-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 全班一起读三条 Success Criteria。",
                "<b>自评</b> · 白板上画 👍 / 😐 / 👎，一条一条来。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下节课</b> · 小青去服装店买东西，她的手提包不见了——被偷了。"
                "我们学「被」。"],
               cn="出门条：写一句 —— 用「除了……以外，还有……」说你的包里有什么。"))

    return S
