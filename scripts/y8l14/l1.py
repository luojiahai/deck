# -*- coding: utf-8 -*-
"""Y8 L14 · Lesson 1 of 6 — the living room, and 张 for flat things

Source: docs/lesson-plans/y8-l14/01-living-room-furniture-mixed.md
Textbook p.132 (Text 1, living-room half; New Words 1–4), p.133 Act. 1,
p.135 Act. 5. Workbook pp.154–155 (copy the new words of Text 1).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_text, s_errors, s_title, s_lisc)

SLUG = "l1-living-room"
TITLE = "Y8 L14 · 家具 Furniture · Lesson 1 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='客厅里有什么', en='The living room',
            desc='Lesson 13 drew the house; this one starts furnishing it. Three pieces of living-room furniture and the measure word 张 — the one the unit test asks for and the one students default to 个 instead.',
            words='沙发 · 茶几 · 电视柜 · 张', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 客厅 The living room", "LESSON 1 OF 6", "第十四课 · 家具",
        s_title("客厅里有什么？", "The Living Room",
                "Year 8 · Book 2 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 2 · p.132"))

    add("02-review.html", "Review · Lesson 13 — the whole house", REV, "复习 · 第十三课",
        s_list("小白板 · 五题 · 写完举起来",
               [("翻译：<i>upstairs</i>", "楼上"),
                ("翻译：<i>garage</i>", "车库"),
                ("翻译：<i>three bedrooms</i>", "量词是「间」"),
                ("翻译：<i>two cars</i>", "量词是「辆」"),
                ("翻译：<i>a two-storey house</i>", "量词是「层」")],
               "上一课你把房子盖起来了——房间、层、车库。今天开始往里面放东西。",
               compact=True))
    add("03-review-errors.html", "Review · 有 or 在", REV, "复习 · 有 还是 在",
        s_errors([("我的房间有楼上。", "我的房间在楼上。", "房间是已知的，问的是在哪儿 → 在"),
                  ("楼上在三间卧室。", "楼上有三间卧室。", "楼上是已知的，卧室是新的 → 有")],
                 "改一改 · 哪里错了？",
                 "规律：<b>新的东西进已知的地方，用「有」；已知的东西找地方，用「在」。</b>"
                 "这两个字今天还会回来。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what furniture is in a living room, with the right measure word.",
               [("I can name three pieces of living-room furniture", "能说出三件客厅里的家具"),
                ("I can use 张 for a sofa and 个 for the rest", "会说「一张沙发」「一个茶几」"),
                ("I can say what is in a room using 客厅里有……", "能用「客厅里有……」说房间里有什么")]))

    # ── Cycle 1 · 沙发 / 茶几 ──
    add("05-c1-words.html", "Cycle 1 · A — 沙发 / 茶几", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("沙发（沙發）", "shāfā", "sofa", "shafa"),
                ("茶几", "chájī", "tea table", "chaji")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("客厅里有一个<b>沙发</b>。", "There's a sofa in the living room."),
                    ("<b>茶几</b>上有一个电话。", "There's a phone on the tea table."),
                    ("<b>沙发</b>前面有一个<b>茶几</b>。",
                     "In front of the sofa is a tea table.", True)],
                   "你家的客厅里有沙发吗？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家的客厅里有 ________ 。"],
                "两件家具，再说一件在另一件哪边："
                "<b>我家的客厅里有一个沙发和一个茶几，茶几在沙发前面。</b>"))

    # ── Cycle 2 · 电视柜 / 张 ──
    add("08-c2-words.html", "Cycle 2 · A — 电视柜 / 张", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("电视柜（電視櫃）", "diànshìguì", "TV cupboard", "dianshigui"),
                ("张（張）", "zhāng", "measure word · flat things", "zhang")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("客厅里有一个<b>电视柜</b>。", "There's a TV cupboard in the living room."),
                    ("我家有一<b>张</b>大沙发。", "We have one big sofa."),
                    ("我们家的客厅里有一<b>张</b>沙发和一个<b>电视柜</b>。",
                     "Our living room has a sofa and a TV cupboard.", True)],
                   "电视在哪儿？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我家的客厅里有一 ________ 沙发。"],
                "把课文那一句默写出来，再加一句说电视在哪儿："
                "<b>电视在电视柜上面。</b>"))

    add("11-recall.html", "Recall · four characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["沙发", "茶几", "电视柜", "张"],
                 "读不出来就停下来重教——不要往下走。", cols=4))

    # ── The pattern ──
    add("12-pattern.html", "Pattern · place 里有 + 量词 + 东西", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说一个房间里有什么",
                  "地方 + 里有 + 量词 + 东西",
                  [("客厅<b>里有</b>一个沙发。", "One thing — the simplest form."),
                   ("客厅<b>里有</b>一<b>张</b>沙发和一个茶几。", "Two things, joined with 和."),
                   ("我们家的客厅<b>里有</b>一张三人沙发、一个茶几和一个电视柜。",
                    "Three things — 、between the first two, 和 before the last. This is Text 1.")],
                  "「三人沙发」= 三人 + 沙发，三个人坐的沙发。会用就用，不用也可以。"))
    add("13-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("从房子说到家具，一口气说完",
                "我家的房子有两层，楼下有客厅，客厅里有一张三人沙发、一个茶几和一个电视柜。",
                "My house has two storeys; downstairs is the living room; in the "
                "living room there's a three-seat sofa, a tea table and a TV cupboard.",
                "上一课的「层」「楼下」，加今天的句型——旧的不会丢，是拿来接新的。"))

    add("14-text.html", "Text 1 · p.132 (living-room half)", IDO, "课文一 · CD 66",
        s_text("课文一 · 客厅 · 课本 p.132",
               "客厅里有一张三人沙发、一个茶几、一个电视柜和一个<span class='text-muted'>空调</span>。",
               "他们家的客厅里有几个茶几？",
               "最后一个词你还不会说——下节课学。今天只读前面三样。"))

    add("15-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「沙发」的量词是什么？", "「个」举一根手指，「张」举两根"),
               ("这句话对不对？　我有一个茶几。", "对的话为什么课文用「张」说沙发？"),
               ("翻译：<i>There's a TV cupboard in the living room.</i>", "写在小白板上"),
               ("你家的客厅里有什么？", "点三个同学，一人说一样，不许重复")]))

    # ── Practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("沙发", "shafa"), ("茶几", "chaji"),
                   ("电视柜", "dianshigui"), ("张", None)],
                  "这一页留在屏幕上——后面两个活动都看它。"))

    add("17-act1.html", "Activity 1 · Design your 客厅 (We Do → You Do, 10 min)", PRAC,
        "活动一 · 10 分钟",
        s_figure("keting", "活动一 · 画你家的客厅",
                 ["<b>先一起来</b>　老师在黑板上画一个客厅，全班说放什么，"
                  "每放一样，老师就在下面写一句。",
                  "<b>再自己画</b>　发纸，画你自己的客厅。三分钟。",
                  "<b>写四句</b>　一样家具一句，四个生词都要用上。四分钟。",
                  "写完请两个同学念自己的——总览页还在屏幕上，可以看。"],
                 cn="客厅里有一张沙发。茶几在沙发前面。"))
    add("18-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["不要画你自己的客厅——写一个你去过、又不能改的："
                "爷爷奶奶家的、医院的等候室、学校图书馆。",
                "写成<b>一段话</b>，不是四条分开的句子：五句连起来，"
                "每一句说这一样在上一样的哪边。",
                "最后一句说大小，要用「特别」。",
                "写的时候不看总览页。"],
               cn="沙发在电视柜前面，茶几在沙发前面……客厅特别大。"))

    add("19-act2.html", "Activity 2 · 客厅里有什么？ (7 min)", PRAC,
        "活动二 · 接龙 + 两人对话 · 7 分钟",
        s_list("活动二 · 先接龙，再两人问答",
               [("<b>接龙 · 3 分钟</b>　一个人加一样，前面的要全部说一遍", "客厅里有沙发 → 客厅里有沙发和茶几 → ……"),
                ("说错或说不出来，从他那里重新开始", "家具说完了可以用第十三课的房间"),
                ("<b>两人问答 · 4 分钟</b>　看课本 p.133 第 1 题的图", "A：你家的客厅里有什么？"),
                ("B 说三样，每样都要带量词，然后换人", "两个人再互相问：你家的客厅大不大？")],
               "老师走动的时候，把词表从说得出来的那一组收走，留给需要的那一组。",
               compact=True))
    add("20-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难",
               ["当提问的那个人，而且要<b>自己想追问的问题</b>。",
                "B 回答完，A 一定要再问一个关于其中<b>一样</b>东西的问题。",
                "最后向全班报告你的同伴，要用「他」，不能用「我」。"],
               cn="你的沙发是什么颜色的？　→　他家的客厅里有一张沙发，可是没有茶几。"))

    add("21-strokes.html", "Characters · 沙 发 茶 几 柜 张 (Workbook pp.154–155)", PRAC,
        "写汉字 · 练习册 p.154",
        s_strokes([("沙", 7, "左边三点水，右边「少」"),
                   ("发", 5, "五画，最后一笔是点"),
                   ("茶", 9, "草字头，中间「人」，下面「木」"),
                   ("几", 2, "两画就写完——撇，横折弯钩"),
                   ("柜", 8, "左边木，右边「巨」"),
                   ("张", 7, "左边弓，右边「长」")],
                  "笔顺 · 每个字写三遍",
                  "这是这几个字今天唯一的一次写字练习——循环写完就写，别因为超时跳过。"))

    add("22-game.html", "Game · Slap the Character (6 min)", PRAC, "游戏 · 拍字 · 6 分钟",
        s_list("游戏 · 拍字 Slap the Character",
               [("黑板上贴十张字卡：今天四个 + 第十三课六个房间", "沙发 · 茶几 · 电视柜 · 张 + 卧室 · 客厅 · 厨房 · 餐厅 · 浴室 · 车库"),
                ("两个同学上来，老师说英文，先拍到的得一分", "赢的留下，换下一个"),
                ("<b>第二轮</b>：老师说一整句，句子里的名词全部要拍，按顺序", "客厅里有一张沙发和一个茶几 = 拍三下"),
                ("<b>加难</b>：老师只说量词，拍任何一个配得上的词", "「一张……」→ 拍沙发")],
               "字卡打印两套，A4 大小，用蓝丁胶贴。"))

    add("23-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 一个同学念三条 success criteria。",
                "<b>自评</b> · 一条一条来：👍 / 😐 / 👎。第二条要特别看——"
                "如果全班都是 😐，下节课的复习就从量词开始。",
                "<b>出门条</b> · 写在纸条上，出门交。",
                "<b>下节课</b> · 空调和洗衣机，还有怎么说一个房间「不算大」——"
                "这是整个单元最有用的一句。"],
               cn="出门条：翻译——There is a sofa and a tea table in my living room."))
    return S
