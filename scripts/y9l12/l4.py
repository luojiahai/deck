# -*- coding: utf-8 -*-
"""Y9 L12 · Lesson 4 of 6 — 菜单/点菜/饿/烤鸭/只 + 来 + Text 2 first half

Source: docs/lesson-plans/y9-l12/04-ordering-menu-mixed.md
Textbook pp.115-116, 120 (Text 2, New Words, Act. 14 + NOTE); workbook p.136 (Ex. 21).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_errors, s_dialogue,
                   s_title, s_lisc, label)

SLUG = "l4-ordering-menu"
TITLE = "Y9 L12 · 外出就餐 Eating Out · Lesson 4 of 6"

IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 点菜 Ordering", "LESSON 4 OF 6", "第十二课 · 外出就餐",
        s_title("点菜", "Ordering at a Restaurant",
                "Year 9 · Book 3 · Unit 4 · Lesson 12 · 50 minutes",
                "轻松学中文 3 · pp.115–116, 120"))

    add("02-review.html", "Review · Correct the Teacher", "0–8 MIN · REVIEW",
        "复习 · 改错句",
        s_errors([("以后我吃完饭看电视。", "我吃完饭以后看电视。", "「以后」要放在分句后面"),
                  ("我们都很饱吃。", "我们都吃得很饱。", "「得」连动词和结果"),
                  ("这家饭店挺贵。", "这家饭店挺贵的。", "「挺……的」要有「的」")],
                 "找错、改对 · 白板 · 改完以后用中文说为什么",
                 "第二句是对的：<b>我们一共花了三百多块。</b> 看谁没上当。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("order food in a Chinese restaurant using 点 and 来.",
               [("I can ask to order using 请问可以点菜了吗？", "能问「请问可以点菜了吗？」"),
                ("I can order a dish using 来 + 数量 + 菜名", "能用「来半只烤鸭」点菜"),
                ("I can say I'm hungry and read a menu", "能说「我饿了」，看得懂菜单")]))

    # ── Cycle 1 ──
    add("04-c1-words.html", "Cycle 1 · A — 菜单 / 点菜", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("菜单（單）", "càidān", "menu", "caidan"),
                ("点菜", "diǎncài", "order food", "diancai")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "各位好，这是<b>菜单</b>。", "Good evening, here's the menu."),
                    (None, "请问可以<b>点菜</b>了吗？", "May I take your order?"),
                    (None, "我们看完<b>菜单</b>以后就<b>点菜</b>。",
                     "We'll order once we've looked at the menu.", True)],
                   "服务员先说什么？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["服务员：请问可以点菜了吗？", "你：________ 。"],
                "「点菜」可以拆开——点什么<b>菜</b>、点了三个<b>菜</b>。写两句<b>拆开</b>的，不要写不拆的。"))

    # ── Cycle 2 ──
    add("07-c2-words.html", "Cycle 2 · A — 饿 / 烤鸭", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("饿（餓）", "è", "hungry　·　饿 ↔ 饱", None),
                ("烤鸭（鴨）", "kǎoyā", "roast duck", "kaoya")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我们都很<b>饿</b>了。", "We're all hungry."),
                    (None, "北京<b>烤鸭</b>做得非常好吃。", "The Peking duck is delicious."),
                    (None, "我很<b>饿</b>，我想吃<b>烤鸭</b>。",
                     "I'm hungry — I'd like roast duck.", True)],
                   "「饿」和「饱」左边都是什么？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我很饿，我想吃 ________ 。"],
                "一句话里「饿」和「饱」都要用上：<b>我们进饭店的时候都很饿，吃完以后都很饱。</b> "
                "再加一个「因为」的分句说为什么。"))

    # ── Cycle 3 ──
    add("10-c3-words.html", "Cycle 3 · A — 只", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("只（隻）", "zhī", "measure word — animals, one of a pair", None),
                ("半只", "bàn zhī", "half a （烤鸭）　·　半 在量词前面", None)))
    add("11-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "来半<b>只</b>烤鸭。", "We'll have half a roast duck."),
                    (None, "我家有两<b>只</b>猫。", "We have two cats at home."),
                    (None, "我们点了一<b>只</b>烤鸭和一<b>个</b>炒青菜。",
                     "We ordered a roast duck and a stir-fried greens.", True)],
                   "为什么烤鸭用「只」，炒青菜用「个」？"))
    add("12-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["来 ________ 只 ________ 。"],
                "「只」是动物，「碗」是米饭和汤，「杯」是茶，「瓶」是可乐——第六节课再学后面三个。"
                "写四个短的点菜句，每句用一个不同的量词，菜不许重复。"))

    add("13-recall.html", "Recall · 认一认", IDO, "认字 · characters only",
        s_recall(["菜单", "点菜", "饿", "烤鸭", "只"],
                 "读不出来就回头再教一遍。", cols=5))

    # ── Pattern ──
    add("14-pattern.html", "Pattern · 来 + 数量 + 量词 + 菜名", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 点菜",
                  "来 + 数量 + 量词 + 菜名",
                  [("来半只烤鸭。", "We'll have half a roast duck."),
                   ("来一个炒青菜。", "We'll have a stir-fried greens."),
                   ("来三碗米饭吧。", "Three bowls of rice, please.")],
                  "课本 p.120 NOTE：<b>点</b> 和 <b>来</b> 都可以用来点菜。"
                  "「半<b>只</b>」，不是 ✗只半——「半」在量词前面。"))
    add("15-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 一口气点四个菜",
                "来半只烤鸭、一个炒肉丝，再来一个蒸鱼。",
                "Half a roast duck, a shredded pork, and a steamed fish as well.",
                "<b>再来</b> = and also bring……，在同一句话里接着点下一样。"))

    add("16-text2.html", "Text 2 · p.115 · CD 47 (first half)", IDO, "课文二 · Text 2",
        s_dialogue("课文二 · 课本 p.115 · CD 47 · 前半段",
                   [("A", "服务员：各位好，这是菜单……请问可以点菜了吗？"),
                    ("B", "爸爸：我们都很饿了。我们现在就点。来半只烤鸭……"),
                    ("A", "服务员：要不要米饭？"),
                    ("B", "爸爸：来三碗米饭吧。")],
                   "半个班当服务员，半个班当爸爸，一起读。烤鸭后面的菜留到下节课。<br>"
                   "<b>用中文回答</b>：谁先说话？· 他们要了几碗米饭？· 「各位」是什么意思？"))

    add("17-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「饿」和「饱」哪个是 hungry？", "饿 举手，饱 手往下——老师乱着说"),
               ("怎么说 menu？", "写在小白板上"),
               ("这句话对不对？ ✗ 来只半烤鸭。", "怎么改？"),
               ("一__烤鸭，一__米饭 —— 哪个用「只」？哪个用「碗」？", "点名回答")]))

    # ── Practice ──
    add("18-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("菜单", "caidan"), ("点菜", "diancai"), ("饿", None),
                   ("烤鸭", "kaoya"), ("只", None)],
                  "这一页留在屏幕上——活动一要用。"))

    add("19-menus.html", "The four menus · 课本 p.120", PRAC, "四张菜单 · Four menus",
        s_list("四张菜单 · 每组一套 · 课本 p.120 第 14 题",
               [("<b>快乐自助餐厅</b>", "龙虾 · 寿司 · 烤牛排 · 沙拉 · 巧克力蛋糕 · 各种水果、甜品 · 果汁"),
                ("<b>天天快餐店</b>", "热狗 · 汉堡包 · 比萨饼 · 香肠 · 煎蛋 · 可乐 · 汽水"),
                ("<b>北京饭店</b>", "烤鸭 · 红烧豆腐 · 蒸鱼 · 炒肉丝 · 炒青菜 · 炒大虾"),
                ("<b>欢欢茶餐厅</b>", "蛋炒饭 · 鱼蛋面 · 炒面 · 白粥 · 鱼片粥 · 绿茶")],
               "选一家，点的菜必须在这家的菜单上。", compact=True))

    add("20-act1.html", "Activity 1 · Complete the dialogue (We Do, 8 min)", PRAC,
        "活动一 · We Do · 8 分钟",
        s_task("活动一 · 补全对话 · 课本 p.120 第 14 题",
               ["两人一组，选一家饭店，把空的地方写出来。",
                "点的菜<b>必须在你选的那张菜单上</b>，至少点三个。"],
               "写给五个人，一个不吃肉，一个不吃海鲜——点菜要有理由。再加一句服务员推荐，"
               "顾客接受或者拒绝，拒绝要说原因。",
               cn="服务员：各位好，这是菜单……请问可以点菜了吗？<br>"
                  "爸爸：可以。来 ________ 。　服务员：________ ？　爸爸：________ 。<br>"
                  "服务员：几位想喝什么？　爸爸：________ 。"))

    add("21-act2.html", "Activity 2 · Perform it (You Do, 9 min)", PRAC,
        "活动二 · You Do · 9 分钟",
        s_task("活动二 · 演出来 · 稿子翻过去",
               ["同一组，稿子翻过来放桌上，站起来演一遍。",
                "然后<b>交换角色</b>，换<b>另一家饭店</b>再演一遍——第二遍没有稿。",
                "两组演给全班看。"],
               "什么都不写：老师给一张没看过的菜单，三十秒准备，直接点给四个人吃。"
               "服务员要问一个稿上没有的问题（要不要米饭？想喝点儿什么？几位？），顾客现场答。"))

    add("22-game.html", "Game · Slap the Character (5 min)", PRAC, "游戏 · 拍字 · 5 分钟",
        s_list("游戏 · 拍字 Slap the Character",
               [("黑板上四张字卡", "菜单 · 点菜 · 饿 · 烤鸭"),
                ("老师说词，两个同学抢拍", "先拍到的得一分"),
                ("<b>加难</b>：老师说一整句，中间空一个词", "我们都很____了，快点菜吧"),
                ("<b>加难</b>：拍对以后要把整句说完整", "说不出来不算分")],
               "字卡打印两套，用蓝丁胶贴。"))

    add("23-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 同学用中文念三条。",
                "<b>自评</b> · 白板上写 👍 / 😐 / 👎，一起举起来。",
                "<b>出门条</b> · 翻译成中文。",
                "<b>下节课</b> · 我们学怎么说一道菜是怎么做的——红烧、蒸、炒。"],
               cn="出门条：翻译成中文 —— <i>May I order now? We'll have half a roast duck.</i>"))
    return S
