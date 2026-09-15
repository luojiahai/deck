# -*- coding: utf-8 -*-
"""Y8 L15 · Lesson 1 of 6 — the shops near my home

Source: docs/lesson-plans/y8-l15/01-shops-nearby-mixed.md
Textbook p.142 (Text 1, first line), p.143 Act. 1 (the shop-matching board).
Workbook pp.164–165 (copy the new words of Text 1).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_text, s_errors, s_title, s_lisc)

SLUG = "l1-shops-nearby"
TITLE = "Y8 L15 · 社区 Neighbourhood · Lesson 1 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='我家附近有花店', en='Shops near my home',
            desc='Lesson 14 furnished the house; this one opens the front door. Four shops, three of which are a character students already own plus 店 — and the list pattern that strings them together.',
            words='附近 · 花店 · 文具店 · 家具店', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我家附近 Shops near my home", "LESSON 1 OF 6",
        "第十五课 · 社区",
        s_title("我家附近有什么？", "Shops Near My Home",
                "Year 8 · Book 2 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 2 · p.142"))

    add("02-review.html", "Review · Lesson 14 — the furniture", REV, "复习 · 第十四课",
        s_list("小白板 · 五题 · 写完举起来",
               [("翻译：<i>wardrobe</i>", "衣柜"),
                ("翻译：<i>bookshelf</i>", "书架"),
                ("翻译：<i>washing machine</i>", "洗衣机"),
                ("翻译：<i>a desk and a chair</i>", "量词：一张书桌、一把椅子"),
                ("问一问同桌：<i>What's in your room?</i>", "你的房间里有什么？")],
               "上一课你把房子装满了。今天走出大门。", compact=True))
    add("03-review-bridge.html", "Review · 家具 → 家具店", REV, "复习 · 从家具到家具店",
        s_focus("家具　→　家具店",
                "家具",
                "You already know this word — Lesson 14 spent fifty minutes on it. "
                "Add one character and it becomes the shop the furniture came from.",
                "今天四个生词，有三个是「你已经会的字 + 店」。"
                "生词表看着长，其实要记的只有前面那个字。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("name the shops near our home and list them in one sentence.",
               [("I can name four shops in Chinese", "能说出四个商店的名字"),
                ("I can say what is near my home using 我家附近有……",
                 "能用「我家附近有……」说家附近有什么"),
                ("I can list several things in one sentence with 、 and 等",
                 "会用「、」和「等」把几样东西放进一句话里")]))

    # ── Cycle 1 · 附近 / 花店 ──
    add("05-c1-words.html", "Cycle 1 · A — 附近 / 花店", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("附近", "fùjìn", "nearby", "fujin"),
                ("花店", "huādiàn", "flower shop", "huadian")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家<b>附近</b>有一个学校。", "There is a school near my home."),
                    ("<b>花店</b>里有很多花。", "There are lots of flowers in the flower shop."),
                    ("我家<b>附近</b>有一个<b>花店</b>。",
                     "There is a flower shop near my home.", True)],
                   "你家附近有花店吗？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家附近有 ________ 。"],
                "两个地方，用「和」连起来，再说你常去哪一个："
                "<b>我家附近有一个学校和一个花店，我常常去花店。</b>"))

    # ── Cycle 2 · 文具店 / 家具店 ──
    add("08-c2-words.html", "Cycle 2 · A — 文具店 / 家具店", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("文具店", "wénjùdiàn", "stationery shop", "wenjudian"),
                ("家具店", "jiājùdiàn", "furniture shop", "jiajudian")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我常常去<b>文具店</b>。", "I often go to the stationery shop."),
                    ("<b>家具店</b>里有沙发和书桌。",
                     "There are sofas and desks in the furniture shop."),
                    ("我家附近有<b>文具店</b>和<b>家具店</b>。",
                     "There's a stationery shop and a furniture shop near my home.", True)],
                   "家具店里卖什么？说三样。"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我在 ________ 买 ________ 。"],
                "一句话说两个店，各买一样："
                "<b>我在文具店买笔，在家具店买书桌。</b>"))

    add("11-recall.html", "Recall · four words, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["附近", "花店", "文具店", "家具店"],
                 "读不出来就停下来重教——不要往下走。", cols=4))

    # ── The pattern ──
    add("12-pattern.html", "Pattern · X 附近有 A、B、C 等", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说说你家附近有什么",
                  "地方 + 附近有 + A、B、C + 等",
                  [("我家<b>附近有</b>花店。", "One shop — the simplest form."),
                   ("我家<b>附近有</b>花店<b>和</b>文具店。", "Two shops, joined with 和."),
                   ("我家<b>附近有</b>饭店<b>、</b>文具店<b>、</b>家具店<b>、</b>花店<b>等</b>。",
                    "Four shops. 「、」between them, 「等」at the end. This is Text 1.")],
                  "「等」就是第四单元的「等等」。「、」是中文的列举号——它不是句号，"
                  "一句话还没说完。"))
    add("13-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("两个分句，加一个去年学的词",
                "学校附近有文具店和家具店等，我常常去那儿买东西。",
                "Near the school there's a stationery shop, a furniture shop and so on — "
                "I often go there to buy things.",
                "「那儿」是七年级的词。新句型拿旧词来装，才是真的会了。"))

    add("14-text.html", "Text 1 · p.142 (first line)", IDO, "课文一 · CD 71",
        s_text("课文一 · 第一句 · 课本 p.142",
               "我家附近有<span class='text-muted'>饭店</span>、文具店、家具店、花店等。",
               "他家附近有几个店？他家附近有没有家具店？",
               "「饭店」今天只认，不写：「饭」你会，「店」今天四个词里有三个都带。"))

    add("15-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「附近」是什么意思？", "是「nearby」就竖大拇指，是「far」就朝下"),
               ("翻译：<i>flower shop</i>", "写在小白板上，举起来"),
               ("这句话哪里错了？　我家花店附近有。", "「附近」跟着「我家」走"),
               ("我说一个店，你说一样在那儿买的东西——中文。",
                "家具店。文具店。花店。")]))

    # ── Practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("附近", "fujin"), ("花店", "huadian"),
                   ("文具店", "wenjudian"), ("家具店", "jiajudian")],
                  "这一页留在屏幕上——后面两个活动都看它。"))

    add("17-act1.html", "Activity 1 · Build my street (We Do, 7 min)", PRAC,
        "活动一 · 7 分钟",
        s_figure("jiedao", "活动一 · 画一条你家附近的街",
                 ["<b>发纸</b>　纸上有五个空店面。",
                  "<b>写店名</b>　花店、文具店、家具店、饭店，再加一个你自己想的。三分钟。",
                  "<b>写一句</b>　在下面写一句话，把五个店<b>全部</b>放进去。",
                  "写完请两个同学念自己的——总览页还在屏幕上，可以看。"],
                 cn="我家附近有花店、文具店、家具店、饭店等。"))
    add("18-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["写成<b>两句</b>，不是一句：第一句说有哪些店，"
                "第二句说你最常去哪一个，还要说为什么。",
                "第二句要用<b>「因为……所以……」</b>。",
                "写完把纸盖上，不看，再说一遍。"],
               cn="我家附近有花店、文具店、家具店和饭店等。因为我很喜欢吃快餐，"
                  "所以我常常去饭店。"))

    add("19-act2.html", "Activity 2 · Neighbourhood survey (You Do, 9 min)", PRAC,
        "活动二 · 9 分钟",
        s_list("活动二 · 站起来，问四个人",
               [("问四个不同的同学：<b>你家附近有什么？</b>", "答案用汉字记在纸背面"),
                ("四个人问完就坐下。", "记不下来就请他再说一遍——这也是中文"),
                ("请三个同学报告<b>别人</b>的：小明家附近有超市和书店。",
                 "报告的那一句才是这个活动的重点：要用第三人称")],
               "记下来才报告得出来。光听不写，一坐下就忘了。"))
    add("20-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难 · 你当采访的人",
               ["问的时候用上一课的<b>有没有</b>：你家附近<b>有没有</b>文具店？",
                "对方说「没有」，你要追问：<b>没有的话，你去哪儿买笔？</b>",
                "最后报告<b>两个</b>同学，一口气说完，还要比较。"],
               cn="小明家附近有文具店，可是小红家附近没有，"
                  "她要坐公共汽车去买笔。"))

    add("21-game.html", "Game · Slap the Character (7 min)", PRAC, "游戏 · 拍字卡",
        s_task("游戏 · 拍字卡 · 7 分钟",
               ["黑板上摆一套卡：今天四个词 + 饭店 + 上一课的五个家具词（干扰项）。",
                "两个同学上来，老师说<b>英文</b>，谁先拍到谁得分，赢的留下。",
                "全班两人一轮，轮完为止。"],
               ext="老师不说英文了，改说一句<b>缺词</b>的中文："
                   "我在 ______ 买沙发。 学生拍那个店。"
                   "最强的一对：老师不出声，上一轮的赢家自己编中文提示。"))

    add("22-strokes.html", "Writing · copy the new characters", PRAC, "写字 · 课文一生词",
        s_strokes([("附", 7, "左边是「阝」，两画写完，不是三画"),
                   ("近", 7, "先写「斤」，最后写走之底"),
                   ("花", 7, "草字头三画，下面是「化」"),
                   ("店", 8, "广字头，里面是「占」"),
                   ("具", 8, "中间是三横，不是两横")],
                  "写字 · 课本笔顺 · 练习册 pp.164–165",
                  "每个字写三遍。这是这五个字在整个单元里唯一一次动笔的机会。"))

    # ── Plenary ──
    add("23-plenary.html", "Plenary · 回头看目标", PLEN, "小结 · 43–50 分钟",
        s_list("小结 · 回头看今天的三个目标",
               [("能说出四个商店的名字", "👍 / 😐 / 👎"),
                ("能用「我家附近有……」", "👍 / 😐 / 👎"),
                ("会用「、」和「等」", "👍 / 😐 / 👎 —— 这一条举 👎 的人多，下节课再来一次")],
               "举手或者写在小白板上。这不是打分，是给老师看的。"))
    add("24-exit.html", "Exit ticket", PLEN, "出门条 · Exit ticket",
        s_focus("出门条 · 写一句，交上来",
                "我家附近有 ________ 。",
                "At least two shops, and it must have 等 in it.",
                "下节课：超市，还有那个告诉你有多远的字——「离」。",
                ext="写完了？把它写成三句话的一段，不是一句。"))
    return S
