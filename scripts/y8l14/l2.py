# -*- coding: utf-8 -*-
"""Y8 L14 · Lesson 2 of 6 — appliances, 里面, and hedged size

Source: docs/lesson-plans/y8-l14/02-appliances-inside-mixed.md
Textbook p.132 (Text 1 complete; New Words 5–8), p.136 Act. 7.
Workbook pp.155–156 (copy 空 调 机).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_text, s_errors, s_title, s_lisc)

SLUG = "l2-appliances-inside"
TITLE = "Y8 L14 · 家具 Furniture · Lesson 2 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='不大也不小', en='Appliances & inside',
            desc='The two machines, the word 里面, and the phrase that carries the whole unit: a room is 不算大 or 不大也不小, never just 大. Text 1 becomes readable except for the three kitchen words, which are left visible as pictures.',
            words='空调 · 洗衣机 · 里面', n=3)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 不大也不小", "LESSON 2 OF 6", "第十四课 · 家具",
        s_title("里面有什么？", "Appliances, and What's Inside",
                "Year 8 · Book 2 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 2 · p.132 · p.136"))

    add("02-review.html", "Review · yesterday's four words", REV, "复习 · 第一节课",
        s_recall(["沙发", "茶几", "电视柜", "张"],
                 "字卡快问快答——全班一起读中文，然后点一个同学说英文。两轮，第二轮快一点。",
                 cols=4))
    add("03-review-errors.html", "Review · the exit tickets", REV, "复习 · 昨天的出门条",
        s_errors([("我家的客厅里有一个沙发。", "我家的客厅里有一张沙发。",
                   "两个都说得通，可是课文用「张」——考试也考「张」"),
                  ("茶几有客厅里。", "客厅里有一个茶几。", "地方在前，「有」在后")],
                 "昨天的出门条 · 改一改",
                 "昨天的条子挑三张贴上去，至少有一张是量词错的。没有人写错就老师自己写一张。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what appliances are inside a room, and describe its size "
               "without saying just 大 or 小.",
               [("I can name an air-conditioner and a washing machine", "能说出空调和洗衣机"),
                ("I can say what is inside something using 里面有……", "能用「里面有……」"),
                ("I can describe a room's size with 不算大 or 不大也不小",
                 "能说「不算大」或者「不大也不小」")]))

    # ── Cycle 1 · 空调 / 洗衣机 ──
    add("05-c1-words.html", "Cycle 1 · A — 空调 / 洗衣机", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("空调（空調）", "kōngtiáo", "air-conditioner", "kongtiao"),
                ("洗衣机（洗衣機）", "xǐyījī", "washing machine", "xiyiji")))
    add("06-c1-note.html", "空调 or 冷气机 — both are in the book", IDO,
        "生词 1 · 两种说法",
        s_figure("kongtiao", "同一样东西，两个名字",
                 ["<b>空调</b>　kōngtiáo　—　大陆的说法，课本里排在前面。",
                  "<b>冷气机</b>　lěngqìjī　—　香港、台湾的说法，课本括号里的那个。",
                  "两个都对，说哪个都可以，可是一句话里不要换来换去。",
                  "「洗<b>衣</b>机」的「衣」，衣服的衣——洗衣服的机器。"],
                 cn="客厅里有一个空调。／ 客厅里有一个冷气机。"))
    add("07-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("客厅里有一个<b>空调</b>。", "There's an air-conditioner in the living room."),
                    ("厨房里有一个<b>洗衣机</b>。", "There's a washing machine in the kitchen."),
                    ("客厅里有<b>空调</b>，厨房里有<b>洗衣机</b>。",
                     "The living room has an air-conditioner, the kitchen has a "
                     "washing machine.", True)],
                   "你们家的洗衣机在哪儿？"))
    add("08-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家的 ________ 里有一个 ________ 。"],
                "两样机器都说，还要各说一句关于它的话："
                "<b>我家的洗衣机在厨房里面，空调在客厅里面，客厅的空调特别大。</b>"))

    # ── Cycle 2 · 里面 ──
    add("09-c2-words.html", "Cycle 2 · A — 里面", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("里面", "lǐmiàn", "inside", "limian")))
    add("10-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("厨房<b>里面</b>有一个洗衣机。", "Inside the kitchen there's a washing machine."),
                    ("车库<b>里面</b>可以停两辆车。", "Inside the garage two cars can park."),
                    ("我的房间<b>里面</b>有一张床。", "Inside my room there's a bed.", True)],
                   "你的房间里面有什么？"))
    add("11-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["________ 里面有 ________ 。"],
                "一句话里同时用「里面」和「外面」，说同一个地方，再加原因："
                "<b>车库里面有一辆车，外面也有一辆车，因为车库不大。</b>"))

    add("12-recall.html", "Recall · seven characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["沙发", "茶几", "电视柜", "张", "空调", "洗衣机", "里面"],
                 "七个了——昨天四个，今天三个。读不出来就停下来重教。", cols=4))

    # ── The pattern ──
    add("13-pattern.html", "Pattern · 不算大 ／ 不大也不小", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说大小，不要只说「大」「小」",
                  "不算大　／　不大也不小",
                  [("我们家的客厅<b>不算大</b>。", "Not that big — a hedge, slightly on the small side."),
                   ("我们家的厨房<b>不大也不小</b>。", "Neither big nor small — right in the middle."),
                   ("我的卧室<b>不算大</b>，可是里面有很多书。",
                    "Hedge plus a 可是 clause — what it lacks in size it makes up for.")],
                  "为什么要学这个：「大」和「小」太绝对，说自己家的时候听起来很硬。"
                  "「不算大」才是人真的会说的话。"))
    add("14-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("两个大小，一个「可是」，四样家具",
                "我们家的房子不大也不小，楼上有三间卧室，楼下的客厅不算大，"
                "可是里面有一张沙发、一个茶几和一个电视柜。",
                "Our house is neither big nor small; upstairs there are three bedrooms; "
                "the living room downstairs isn't that big, but inside it there's a "
                "sofa, a tea table and a TV cupboard.",
                "两个大小说法都用上了，而且用的不是同一个地方——这是这句最难的地方。"))

    add("15-text.html", "Text 1 · p.132 complete", IDO, "课文一 · CD 66",
        s_text("课文一 · 课本 p.132 · 听两遍，边听边打钩",
               "我们家的客厅<b>不算大</b>。客厅里有一张三人沙发、一个茶几、一个电视柜和一个"
               "<b>空调</b>（冷气机）。我们家的厨房<b>不大也不小</b>，<b>里面</b>有 ____ 、"
               "<b>洗衣机</b>、 ____ 和 ____ 。",
               "他们家的厨房大不大？",
               "三个空还不会说——屏幕上给你看图。下节课把空填上。", size=22))

    add("16-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「不大也不小」是大还是小？", "用英文告诉同伴，五秒钟"),
               ("翻译：<i>the kitchen is not that big</i>", "写在小白板上"),
               ("这句话对不对？　我的房间不算大也不小。", "举大拇指或者倒过来"),
               ("你的卧室大不大？", "点名——要「不算大」，不要只说「大」或「不大」")]))

    # ── Practice ──
    add("17-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("沙发", "shafa"), ("茶几", "chaji"), ("电视柜", "dianshigui"),
                   ("张", None), ("空调", "kongtiao"), ("洗衣机", "xiyiji"),
                   ("里面", "limian")],
                  "这一页留在屏幕上——后面两个活动都看它。", dense=True))

    add("18-act1.html", "Activity 1 · 客厅 or 厨房? (8 min)", PRAC,
        "活动一 · 分类 · 8 分钟",
        s_task("活动一 · 七个词，分两边",
               ["黑板上写两个标题：<b>客厅</b>　<b>厨房</b>。",
                "两人一组，把总览页上的七个词分到两边去。",
                "有三个是<b>两边都说得通</b>的——那才是要讨论的地方。"
                "（还有一个根本不是东西，找出来。）",
                "全班对答案的时候，说出来的不是哪一栏，是<b>为什么</b>，要说一句完整的话。"],
               cn="洗衣机在厨房里面，因为我们家的洗衣机在那儿。"))
    add("19-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["换一个分法：这七样，<b>你们家有的</b>放一边，<b>没有的</b>放另一边。",
                "每一边写两句，不是列词。",
                "再从第十三课各加一个词进来，写成六句一段。",
                "不看总览页。"],
               cn="我们家有空调，可是没有洗衣机，我们家的洗衣机在楼下。"))

    add("20-act2.html", "Activity 2 · p.136 Ex.7 pair dialogue (9 min)", PRAC,
        "活动二 · 两人问答 · 9 分钟",
        s_list("活动二 · 抽题卡，问答，换人（课本 p.136 第 7 题）",
               [("你家住什么样的房子？", "第十三课"),
                ("你家的房子有几层？", "量词是「层」"),
                ("你家有几间卧室？", "量词是「间」"),
                ("你家的客厅大不大？", "← 今天要听的就是这一题"),
                ("客厅里有什么？", "带量词"),
                ("厨房里面有什么？", "用「里面」")],
               "大小那一题，答案一定要推到「不算大」或者「不大也不小」，不要放过「大」。",
               compact=True))
    add("21-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难",
               ["不要说你自己家——<b>扮一个人</b>：爷爷奶奶、电影里的人、"
                "住的地方跟你完全不一样的人。六个答案要前后对得上，不能自相矛盾。",
                "然后 B 用<b>第三人称</b>向全班说 A 的房子，三句，不看笔记。"],
               cn="他家住洋房，房子有两层，客厅不算大。"))

    add("22-strokes.html", "Characters · 空 调 机 (Workbook pp.155–156)", PRAC,
        "写汉字 · 练习册 p.155",
        s_strokes([("空", 8, "宝盖头，下面「工」"),
                   ("调", 10, "左边言字旁，右边「周」"),
                   ("机", 6, "左边木，右边「几」——「几」昨天写过")],
                  "笔顺 · 每个字写三遍",
                  "循环里的「写一句」写完，笔先别放下，把这三个字写完再放。"))

    add("23-game.html", "Game · Sentence Jumble (6 min)", PRAC, "游戏 · 排句子 · 6 分钟",
        s_list("游戏 · 排句子 Sentence Jumble",
               [("每组一个信封，里面是剪开的词条，六句", "厨房／里面／有／一个／洗衣机"),
                ("排好一句就举手，老师看语序，不看字写得好不好", "客厅／里／有／一个／空调"),
                ("六句全对的第一组赢", "我们家的／厨房／不大／也／不小"),
                ("<b>加难版</b>：有一个信封里是<b>两句混在一起</b>的词条，"
                 "而且没告诉你在哪儿分开", "排完还要用剩下的词条自己再造一句")],
               "词条要提前剪好——每组六句的量。"))

    add("24-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 一个同学念，然后问：哪一条最难？",
                "<b>自评</b> · 小白板上画三个点，红黄绿，一起举起来。",
                "<b>出门条</b> · 一句话，写在纸条上。",
                "<b>下节课</b> · 把课文里的三个空填上——冰箱、烤箱、电炉——"
                "然后整本书的量词一起回来。"],
               cn="出门条：我们家的厨房不算大，里面有一个洗衣机。"))
    return S
