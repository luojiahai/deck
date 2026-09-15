# -*- coding: utf-8 -*-
"""Y9 L12 · Lesson 6 of 6 — 杯/绿茶/瓶 + measure-word race + the restaurant project

Source: docs/lesson-plans/y9-l12/06-drinks-measure-words-project.md
Textbook pp.117, 119, 121 (Act. 9, Act. 12 / CD 48, Act. 15 project).
The plenary looks back over all six lessons, not just this one.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_title, s_lisc, label)

SLUG = "l6-drinks-project"
TITLE = "Y9 L12 · 外出就餐 Eating Out · Lesson 6 of 6"

IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 开一家饭店", "LESSON 6 OF 6", "第十二课 · 外出就餐",
        s_title("开一家饭店", "Drinks, Measure Words and Your Own Restaurant",
                "Year 9 · Book 3 · Unit 4 · Lesson 12 · 50 minutes",
                "轻松学中文 3 · pp.117, 119, 121"))

    add("02-review.html", "Review · CD 48 listening (p.119 Act. 12)", "0–8 MIN · REVIEW",
        "复习 · 听力 · CD 48",
        s_list("听一听，连一连 · 课本 p.119 第 12 题 · CD 48 · 放两遍",
               [("小天 · 小文 · 小山", "A 午饭时吃水果。　B 不常吃快餐。　C 中午在学校买盒饭吃。"),
                ("冬冬 · 小云 · 小明", "D 爱吃西瓜和梨。　E 晚饭时常吃蔬菜。　F 很胖，因为常吃快餐。"),
                ("六个人，八个句子", "G 爱吃巧克力、冰淇淋、薯片等。　H 一家人常去饭店吃北京烤鸭。"),
                ("这是这六节课的总复习", "录音里有蔬菜、水果、快餐、零食、盒饭、烤鸭、红烧豆腐、炒肉丝。")],
               "对完答案问一句：<b>小明家爱吃什么？</b> 三道菜都要用中文说出来。", compact=True))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("order drinks with the right measure words, and design and "
               "present a restaurant of our own.",
               [("I can order a drink using 来 + 数量 + 杯／瓶", "能用「来两杯绿茶」点饮料"),
                ("I can match measure words to the right nouns", "量词能用对"),
                ("I can write a menu and describe my restaurant in Chinese",
                 "能写菜单，能介绍我的饭店")]))

    # ── Cycle 1 ──
    add("04-c1-words.html", "Cycle 1 · A — 杯 / 绿茶", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("杯", "bēi", "cup; glass", "bei"),
                ("绿茶", "lǜchá", "green tea", "lucha")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "来两<b>杯绿茶</b>。", "Two green teas, please."),
                    (None, "我每天早上喝一<b>杯</b>牛奶。",
                     "I drink a glass of milk every morning."),
                    (None, "吃完烤鸭以后，我们要了两<b>杯绿茶</b>。",
                     "After the roast duck we ordered two green teas.", True)],
                   "「杯」左边是「木」——为什么？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我每天喝 ________ 杯 ________ 。"],
                "「杯」热的冷的都能用。写两句，一句热饮一句冷饮，"
                "用「一边……一边……」或者「完……以后」连起来。"))

    # ── Cycle 2 ──
    add("07-c2-words.html", "Cycle 2 · A — 瓶", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("瓶", "píng", "bottle", "ping"),
                ("再来", "zài lái", "and also bring…　·　同一句里接着点", None)))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "再来两<b>瓶</b>可乐。", "And two bottles of cola as well."),
                    (None, "一<b>瓶</b>汽水多少钱？", "How much is a bottle of soft drink?"),
                    (None, "来两杯绿茶，再来两<b>瓶</b>可乐。",
                     "Two green teas, and two bottles of cola as well.", True)],
                   "为什么绿茶用「杯」，可乐用「瓶」？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["来 ________ 杯 ________ ，再来 ________ 瓶 ________ 。"],
                "给五个人点饮料，五个人要的都不一样，至少用三个不同的量词，最后说一共多少<b>块</b>。"))

    # ── Pattern ──
    add("10-pattern.html", "Pattern · 量词总复习", IDO, "句型 · 量词 Measure words",
        s_pattern("句型 · 量词用对",
                  "数量 + 量词 + 名词",
                  [("只 → 烤鸭、鸡、猫　·　碗 → 米饭、汤、面条",
                    "animals · rice, soup, noodles"),
                   ("杯 → 绿茶、咖啡、牛奶　·　瓶 → 可乐、汽水、水",
                    "cups and glasses · bottles"),
                   ("个 → 寿司、龙虾、蛋糕　·　块 → 三文鱼、巧克力",
                    "the general one · slabs and slices")],
                  "量词用错，句子就不对——测验第二题考的就是这个。"))
    add("11-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 四个量词，一句话",
                "来半只烤鸭、三碗米饭、两杯绿茶，再来两瓶可乐。",
                "Half a roast duck, three bowls of rice, two green teas, "
                "and two bottles of cola as well.",
                "这就是课文二的全部——只、碗、杯、瓶，一口气说完。"))

    add("12-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("一__绿茶，一__可乐 —— 哪个用「杯」？哪个用「瓶」？", "举手回答"),
               ("怎么说 <i>two bottles of cola</i>？", "写在小白板上"),
               ("这句话对不对？ ✗ 来两个绿茶。", "应该是什么？"),
               ("烤鸭用「只」，米饭用什么？", "点名回答")]))

    # ── Practice ──
    add("13-act1.html", "Activity 1 · Measure-word race (We Do, 5 min)", PRAC,
        "活动一 · We Do · 5 分钟",
        s_task("活动一 · 量词比赛 · 课本 p.117 第 9 题 · 三分钟",
               ["四人一组。黑板上八个量词：<b>瓶 杯 只 碗 个 块 斤 包</b>",
                "每个量词找<b>两个</b>名词，写在一张纸上。",
                "配对最多的组赢——<b>配错扣一分</b>，所以不要乱猜。"],
               "写完了就拿难的那一组：<b>辆 本 节 件 位 张 双 家</b>，"
               "其中两个还要用在完整的句子里。"))

    add("14-act2.html", "Activity 2 · Design your restaurant (You Do, 14 min)", PRAC,
        "活动二 · You Do · 14 分钟 · 课本 p.121 第 15 题",
        s_task("活动二 · 开一家自己的饭店 · 两人一组，两张 A4",
               ["<b>第一张 · 平面图</b>　几层楼、几张餐桌、厨房和厕所在哪儿——全部用中文标出来。",
                "<b>第二张 · 菜单</b>　饭店的名字，菜分成 主食／甜品／饮料，每样写价钱。",
                "菜单里<b>至少用六道这一课的菜</b>，<b>至少用三个不同的量词</b>。",
                "最后写三四句介绍你的饭店。"],
               "菜单以外再写一段<b>食评</b>——四到六句，用顾客的口气，"
               "要有「挺……的」、一个「比」的比较（跟另一家饭店比）、还有「完……以后」。"
               "全班提问的时候要能用中文为你们的定价辩护（为什么你们的龙虾这么贵？）。",
               cn="范例：这家饭店叫中港西餐馆，一共有两层。一楼有十张餐桌，可以坐下五十个人。"
                  "二楼有十二张餐桌，可以坐下六十个人。厨房在一楼。男、女厕所一楼、二楼都有。"
                  "在这家饭店你可以吃到……"))

    add("15-act3.html", "Activity 3 · Present and judge (4 min)", PRAC,
        "活动三 · 展示和评选 · 4 分钟",
        s_task("活动三 · 三四组上来展示",
               ["举起平面图和菜单，把介绍念出来。",
                "全班按课本的三个标准举手评分：<b>设计 · 画得好不好 · 中文用得怎么样</b>。",
                "其他组的作品贴在墙上。"],
               "全班可以照着菜单<b>点菜</b>——展示的那一组当服务员，现场接单，"
               "「来」和量词都要用对。"))

    add("16-plenary.html", "Plenary · looking back over all six lessons", PLEN,
        "小结 · Plenary · 六节课一起回看",
        s_task("小结 · 43–50 分钟 · 今天回看的是<b>六节课</b>，不只是今天",
               ["<b>回看目标</b> · 先念今天三条，再放六节课的目标——每一条全班说「会」或者「还不会」。",
                "<b>自评</b> · 白板上写<b>一个</b>这六节课里你最没把握的词，举起来。"
                "老师看哪几个词反复出现——测验前的复习就从那几个开始。",
                "<b>出门条</b> · 写一句。",
                "<b>下节课</b> · 第四单元学完了。下节课开始第五单元——社区，"
                "说一说你家附近有什么。"],
               cn="出门条：来 ________ 杯 ________ ，再来 ________ 瓶 ________ 。"))
    return S
