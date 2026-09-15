# -*- coding: utf-8 -*-
"""Y9 L12 · Lesson 5 of 6 — 红烧/蒸/肉丝/青菜 + Text 2 complete + phone takeaway

Source: docs/lesson-plans/y9-l12/05-cooking-methods-mixed.md
Textbook pp.115-117 (Text 2 complete, Act. 8, Act. 10); workbook p.135 (Ex. 18).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_dialogue,
                   s_title, s_lisc, label)

SLUG = "l5-cooking-methods"
TITLE = "Y9 L12 · 外出就餐 Eating Out · Lesson 5 of 6"

IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 红烧、蒸、炒", "LESSON 5 OF 6", "第十二课 · 外出就餐",
        s_title("红烧 · 蒸", "How It's Cooked",
                "Year 9 · Book 3 · Unit 4 · Lesson 12 · 50 minutes",
                "轻松学中文 3 · pp.115–117"))

    add("02-review.html", "Review · pair dialogue from memory", "0–8 MIN · REVIEW",
        "复习 · 第四节课",
        s_task("复习 · 两人对话 · 三十秒一轮，然后交换",
               ["A 是服务员，开口：各位好，这是菜单……请问可以点菜了吗？",
                "B 用「来」点两个菜。",
                "然后交换。老师点三组演给全班看。"]))

    add("03-review-jumble.html", "Review · WB Ex. 18 sentence jumble (test format)",
        "0–8 MIN · REVIEW", "复习 · 连词成句 · 考试题型",
        s_list("连词成句 · 三分钟 · 白板 · 这是第四单元测验的题型",
               [("吗／请问，／点菜／了／可以？", None),
                ("一碗米饭／了／要／弟弟／又。", None),
                ("了／我们大家／饿／都。", None),
                ("和／炒青菜／点／红烧豆腐／了／我。", None)],
               "写完举起来。第四题里有两个今天要学的词。", compact=True))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say how a dish is cooked, and order a whole meal over the phone.",
               [("I can name three ways of cooking in Chinese", "能说出「红烧」「蒸」「炒」"),
                ("I can name a dish by its cooking method", "能说「红烧豆腐」「蒸鱼」「炒青菜」"),
                ("I can order a takeaway by phone and ask the total",
                 "能打电话叫外卖，问一共多少钱")]))

    # ── Cycle 1 ──
    add("05-c1-words.html", "Cycle 1 · A — 红烧 / 蒸", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("红烧（燒）", "hóngshāo", "braise in soy sauce", "hongshao"),
                ("蒸", "zhēng", "steam", "zheng")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "<b>红烧</b>豆腐是我最喜欢的菜。",
                     "Braised tofu is my favourite dish."),
                    (None, "妈妈<b>蒸</b>的鱼做得非常好吃。",
                     "The fish mum steams is delicious."),
                    (None, "我们点了一个<b>红烧</b>豆腐和一个<b>蒸</b>鱼。",
                     "We ordered a braised tofu and a steamed fish.", True)],
                   "「烧」左边是什么？跟「烤」一样吗？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我喜欢吃红烧 ________ ，也喜欢吃蒸 ________ 。"],
                "烤、红烧、蒸、炒——四种做法。用「比」写一句比较两种"
                "（我觉得蒸鱼比红烧鱼好吃），再用「因为」说为什么。"))

    # ── Cycle 2 ──
    add("08-c2-words.html", "Cycle 2 · A — 肉丝 / 青菜", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("肉丝（絲）", "ròusī", "shredded meat", "rousi"),
                ("青菜", "qīngcài", "green vegetables", "qingcai")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "炒<b>肉丝</b>是一个很简单的菜。",
                     "Stir-fried shredded pork is a simple dish."),
                    (None, "我每天晚饭都吃<b>青菜</b>。",
                     "I eat green vegetables with dinner every day."),
                    (None, "来一个炒<b>肉丝</b>、一个炒<b>青菜</b>。",
                     "A shredded pork and a stir-fried greens, please.", True)],
                   "「丝」是什么意思？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["来一个炒 ________ 。"],
                "「丝」说的是<b>刀工</b>，不是肉——土豆丝、胡萝卜丝是一样的切法。"
                "写三个带「丝」的菜，配不同的材料，再写一句说你点哪个、为什么。"))

    add("11-recall.html", "Recall · 认一认", IDO, "认字 · characters only",
        s_recall(["红烧", "蒸", "肉丝", "青菜"],
                 "读不出来就回头再教一遍。", cols=4))

    # ── Pattern ──
    add("12-pattern.html", "Pattern · 做法 + 材料 = 菜名", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 菜名怎么来的",
                  "做法 + 材料 = 菜名",
                  [("烤 + 鸭 → 烤鸭　·　烤 + 牛排 → 烤牛排", "roast duck · roast beefsteak"),
                   ("红烧 + 豆腐 → 红烧豆腐　·　蒸 + 鱼 → 蒸鱼",
                    "braised tofu · steamed fish"),
                   ("炒 + 青菜 → 炒青菜　·　炒 + 肉丝 → 炒肉丝",
                    "stir-fried greens · stir-fried shredded pork")],
                  "做法在<b>前</b>，材料在<b>后</b>。不是 ✗豆腐红烧。"))
    add("13-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 四种做法，一句话",
                "我们点了半只烤鸭、一个炒肉丝、一个红烧豆腐和一个蒸鱼。",
                "We ordered half a roast duck, a shredded pork, a braised tofu "
                "and a steamed fish.",
                "这就是课文二爸爸点的菜——烤、炒、红烧、蒸，四种做法在一句话里。"))

    add("14-text2.html", "Text 2 · p.115 · CD 47 (complete)", IDO, "课文二 · Text 2 全文",
        s_dialogue("课文二 · 全文 · 课本 p.115 · CD 47",
                   [("A", "服务员：各位好，这是菜单……请问可以点菜了吗？"),
                    ("B", "爸爸：我们都很饿了。我们现在就点。来半只烤鸭、一个炒肉丝、"
                          "一个红烧豆腐、一个蒸鱼。再来一个炒青菜。"),
                    ("A", "服务员：要不要米饭？"),
                    ("B", "爸爸：来三碗米饭吧。"),
                    ("A", "服务员：请问，想喝点儿什么？"),
                    ("B", "爸爸：来两杯绿茶，再来两瓶可乐。")],
                   "分两半读，再一起读，最后两个同学演出来。<br>"
                   "<b>用中文回答</b>：爸爸点了几个菜？· 哪个菜是蒸的？· 「再来」是什么意思？"))

    add("15-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「蒸」字下面的四点是什么？跟什么有关系？", "举手回答"),
               ("怎么说 green vegetables？", "写在小白板上"),
               ("红烧豆腐、蒸鱼、炒青菜——哪一个用最多的油？", "点名回答"),
               ("这句话对不对？ ✗ 来一个豆腐红烧。", "怎么改？")]))

    # ── Practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("红烧", "hongshao"), ("蒸", "zheng"),
                   ("肉丝", "rousi"), ("青菜", "qingcai")],
                  "这一页留在屏幕上——活动一要用。"))

    add("17-act1.html", "Activity 1 · A few sentences about each dish (We Do, 8 min)",
        PRAC, "活动一 · We Do · 8 分钟",
        s_task("活动一 · 每张图说两句 · 课本 p.116 第 8 题",
               ["两人一组，十四张图卡背面朝上洗好。",
                "轮流翻一张，说<b>两句</b>——照范例。",
                "十四张全部翻完才能停。"],
               "每张说<b>三句</b>，第三句要把这张和上一张连起来"
               "（蒸鱼比烤鸭清淡，所以我妈妈更喜欢蒸鱼）。翻完以后，挑四样配成一桌菜，"
               "说出来为什么这样配。",
               cn="范例：我非常喜欢吃龙虾。我每个月吃一次龙虾。"))

    add("18-dishes.html", "The fourteen dishes · 课本 p.116", PRAC, "十四张图卡 · The dishes",
        s_recall(["奶酪蛋糕", "白巧克力", "寿司", "烤鸭", "红烧豆腐", "蒸鱼", "炒青菜",
                  "烤牛排", "水果沙拉", "绿茶", "香肠", "薯条", "青豆蛋炒饭", "冰淇淋"],
                 "这些词都学过了——这一页是给你们<b>看</b>的，不是教的。",
                 cols=7, size="12pt 4pt", head="十四道菜 · 课本 p.116 · 图卡背面的字"))

    add("19-act2.html", "Activity 2 · Phone takeaway order (You Do, 10 min)", PRAC,
        "活动二 · You Do · 10 分钟",
        s_task("活动二 · 打电话叫外卖 · 给五个人点午饭 · 课本 p.117 第 10 题",
               ["两人一组，<b>背对背坐</b>——打电话看不见嘴，也看不见手势。",
                "先写下来（2 分钟），背对背演一遍（4 分钟），",
                "然后交换，换一家饭店，<b>不写稿</b>再演一遍（4 分钟）。"],
               "服务员故意听错一样，把单子念错；顾客要当场听出来改正（不是四个，是两个）。"
               "顾客还要问两个稿上没有的问题——要等多长时间？你们送到学校吗？——服务员现场答。"
               "两边都<b>什么都不写</b>。",
               cn="服务员：晚上好！家乐快餐店。　小明：我想叫外卖。　服务员：请说。<br>"
                  "小明：来一个比萨饼、四个炸鸡腿、两个汉堡包和四瓶可乐。一共多少钱？"
                  "　服务员：一百五十六块。"))

    add("20-game.html", "Game · Odd One Out — cooking methods (5 min)", PRAC,
        "游戏 · 找不同 · 5 分钟",
        s_list("游戏 · Odd One Out · 用中文说为什么",
               [("红烧豆腐 · 蒸鱼 · 冰淇淋", "冰淇淋不用做。"),
                ("烤鸭 · 烤牛排 · 炒青菜", "炒青菜不是烤的。"),
                ("炒肉丝 · 炒青菜 · 红烧豆腐", "红烧豆腐不是炒的。"),
                ("薯条 · 炸鸡翅 · 蒸鱼", "蒸鱼不是炸的。")],
               "用活动一的图卡就行。<b>加难</b>：题目让学生出——每组出一轮给全班，理由要站得住。"))

    add("21-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 同学用中文念三条。",
                "<b>自评</b> · 三条目标，👍 / 😐 / 👎。",
                "<b>出门条</b> · 写一句。",
                "<b>下节课</b> · 我们喝点儿东西——还要自己开一家饭店，写自己的菜单。"],
               cn="出门条：写一句 —— 来一个 ________ 和一个 ________ 。（用两种不同的做法）"))
    return S
