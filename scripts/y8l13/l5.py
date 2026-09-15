# -*- coding: utf-8 -*-
"""Y8 L13 · Lesson 5 of 6 — outside the house, and Text 2

Source: docs/lesson-plans/y8-l13/05-text2-outside-writing.md
Textbook p.127 (Text 2, New Words 1–5; CD 64).
Workbook p.148 Ex. 9 (review), p.149 Ex. 11, p.152 Ex. 17.

The stroke-order slide here copies the lesson's OWN new words. That is
vocabulary work. Radical identification — workbook Ex. 13, textbook Act. 7 —
is out of this series by the teacher's instruction and has no helper.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_text, s_dialogue, s_title, s_lisc)

SLUG = "l5-outside-text2"
TITLE = "Y8 L13 · 房子 House · Lesson 5 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

# Card shown on the series landing page (index/designs/y8-l13/index.html),
# written by build.py. Lives beside the lesson it describes.
CARD = dict(cn='走出大门', en='Outside the house · Text 2',
            desc="A writing lesson. Text 2, then stroke-order rows for the five new characters, then the six jumbled sentences typed up — producing characters from pinyin, which is what the unit test's translation asks for.",
            words='洋房 · 花园 · 前 · 后 · 车库', n=5)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 洋房、花园、车库 Outside the house", "LESSON 5 OF 6",
        "第十三课 · 房子",
        s_title("走出大门", "Outside the House · Text 2",
                "Year 8 · Book 2 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 2 · p.127 · CD 64"))

    add("02-review.html", "Review · Workbook p.148 Ex.9 reading", REV,
        "复习 · 练习册 p.148 第 9 题",
        s_text("先读，再回答 · 天喜家的房子",
               "天喜家住<b>洋房</b>。他家的房子很大，有两层，还有一个地下室。"
               "二楼有三间卧室：爸爸妈妈的卧室、姐姐的卧室和天喜的卧室。"
               "除了卧室，楼上还有两个浴室和爸爸的书房。"
               "一楼有一间客房、一个大厨房、一个大客厅和一个洗手间。",
               "天喜家有几间卧室？　天喜的卧室在楼上还是楼下？　"
               "他家有书房吗？在几楼？　厨房在几楼？",
               "地下室 = basement · 客房 = guest room（只认，不用写）。"
               "<b>洋房</b> 先不说意思——看图猜，等一下就学。", size=20))
    add("03-review-wb.html", "Review · 在 / 有, two items", REV, "复习 · 小白板",
        s_list("两题 · 写完整句",
               [("在 还是 有？ 卧室右面 ____ 一个浴室。", ""),
                ("从地方开头再说一次：我的书在桌子上面。→ ?", "桌子上面有我的书。")],
               "天喜住的是「洋房」——今天第一个词就是它。", compact=True))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("write about what kind of house we live in and what is outside it.",
               [("I can name what is outside a house", "能说出房子外面有什么"),
                ("I can answer 你家住什么样的房子？ in writing", "能写出「你家住什么样的房子？」的答案"),
                ("I can write 洋、园、前、后、库 with the correct stroke order",
                 "能用正确笔顺写洋、园、前、后、库")]))

    # ── Cycle 1 · 洋房 / 花园 ──
    add("05-c1-words.html", "Cycle 1 · A — 洋房 / 花园", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("洋房", "yángfáng", "western-style house", "yangfang"),
                ("花园", "huāyuán", "garden", "huayuan")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家住<b>洋房</b>。", "We live in a western-style house."),
                    ("我家有一个<b>花园</b>。", "We have a garden."),
                    ("我家住<b>洋房</b>，房子有一个大<b>花园</b>。",
                     "We live in a western-style house with a big garden.", True)],
                   "洋房跟楼房有什么不一样？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我家住 ________ 。", "我家有 ________ 花园。"],
                "不要只说有花园——说它多大、在哪儿、里面有什么，用上节课的方位词："
                "<b>我家住洋房，花园在房子外面，花园里面有很多花。</b>"))

    # ── Cycle 2 · 前 / 后 ──
    add("08-c2-words.html", "Cycle 2 · A — 前 / 后", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("前", "qián", "front", "fangqian"),
                ("后（後）", "hòu", "back", "fanghou")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("<b>房前</b>有一个花园。", "There's a garden in front of the house."),
                    ("<b>房后</b>有一个大花园。", "There's a big garden behind the house."),
                    ("我家有两个花园，<b>房前</b>一个，<b>房后</b>一个。",
                     "We have two gardens, one in front and one behind.", True)],
                   "「房前」跟「房子前面」一样吗？"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["房前有 ________ 。", "房后有 ________ 。"],
                "写成一句，中间加上大小的比较，就像课文里那样："
                "<b>房前的花园小，房后的花园大。</b> 再说一句你喜欢哪一个。"))

    # ── Cycle 3 · 车库 ──
    add("11-c3-words.html", "Cycle 3 · A — 车库", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("车库", "chēkù", "garage", "cheku")))
    add("12-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([("我家有一个<b>车库</b>。", "We have a garage."),
                    ("<b>车库</b>在房后。", "The garage is behind the house."),
                    ("我家有一个花园和一个<b>车库</b>，<b>车库</b>在房前。",
                     "We have a garden and a garage; the garage is in front.", True)],
                   "你家的车停在哪儿？"))
    add("13-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["我家 ________ 车库。车库在 ________ 。"],
                "三个小句，不给句型：住什么样的房子、花园在哪儿、车库在哪儿，"
                "连起来读像<b>一段话</b>，不是三句。"))

    add("14-recall.html", "Recall · five characters, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["洋房", "花园", "前", "后", "车库"], "一起读两遍。", cols=5))

    # ── Pattern + Text 2 ──
    add("15-pattern.html", "Pattern · 你家住什么样的房子？", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 问、答住什么样的房子",
                  "你家住什么样的房子？",
                  [("我家住<b>洋房</b>。", "We live in a western-style house."),
                   ("我家住<b>楼房</b>。", "We live in an apartment block."),
                   ("你家有花园吗？ → 有两个，房前一个，房后一个。",
                    "Do you have a garden? — Two: one in front, one behind.")],
                  "这个问句记住——下节课的报告和单元测验的作文都是从它开头。"))
    add("16-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("四件事，两个小句连起来",
                "我家住洋房，房子有两层。房前有一个小花园，房后有一个大花园和一个车库。",
                "We live in a western-style house with two storeys. There's a small "
                "garden in front and a big garden and a garage behind.",
                "「房前」「房后」在同一句里各出现一次——顺序不要说反。"))
    add("17-text.html", "Text 2 · the dialogue", IDO, "课文二 · p.127 · CD 64",
        s_dialogue("课文二 · 先听，再跟读，最后把拼音关掉",
                   [("A", "你家住什么样的房子？"), ("B", "我家住洋房。"),
                    ("A", "你家有花园吗？"), ("B", "有两个，房前一个，房后一个。"),
                    ("A", "你家有车库吗？"), ("B", "有。我家的车库可以停两辆车。")],
                   "最后一句里的 <b>停</b> 和 <b>辆</b> 还没学——下节课就学，"
                   "学完这段对话才算完整。"))
    add("18-text-q.html", "Text 2 · comprehension", IDO, "课文二 · 用中文回答",
        s_cfu([("B 家住什么样的房子？", ""),
               ("B 家有几个花园？在哪儿？", ""),
               ("B 家的车库可以停几辆车？", "这一句里有两个新词——下节课学")],
              head="课文二 · 三个问题 · 用中文回答",
              note="答案不上屏——口头回答，或者写在小白板上。"))

    # ── Practice ──
    add("19-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("洋房", "yangfang"), ("花园", "huayuan"), ("车库", "cheku"),
                   ("房前", "fangqian"), ("房后", "fanghou")],
                  "这一页留在屏幕上——写字、排句子都看它。", dense=True))

    add("20-act1.html", "Activity 1 · Stroke order (We Do, 8 min)", PRAC,
        "活动一 · We Do · 8 分钟 · 练习册 p.149 第 11 题",
        s_strokes([("洋", 9, "三点水在左，右边「羊」"),
                   ("园", 7, "先写外框三笔，写里面，最后封口"),
                   ("前", 9, "上面两点，中间「一」，下面「月」加「刂」"),
                   ("后", 6, "撇、横，再写「口」"),
                   ("库", 7, "广字头，里面一个「车」——「车」你已经会写了")],
                  "笔顺 · 老师先在黑板上一笔一笔写，学生跟着空写，再下笔 · 每个字三遍",
                  "老师走一圈看握笔和笔画方向，不看谁写得快。"))
    add("21-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["写完三遍以后，每个字<b>放进词里</b>写，不要单写。"],
               "洋房 · 花园 · 房前 · 房后 · 车库 —— 五个词写完，再用这五个字"
               "写一段四句的房子介绍，<b>不看总览页</b>。"))

    add("22-act2.html", "Activity 2 · Rearrange, then type (You Do, 11 min)", PRAC,
        "活动二 · You Do · 11 分钟 · 练习册 p.152 第 17 题",
        s_list("活动二 · 排句子 · 先写在本子上",
               [("住／我家／楼房。", ""), ("三间／有／楼上／卧室。", ""),
                ("二楼／在／我的房间。", ""), ("大花园／有／房后／一个。", ""),
                ("上海饭店／楼下／有／他家／一家。", ""),
                ("的／车库／右边／我家房子／在。", "")],
               "六句排好以后，照练习册说的，在电脑上把六句<b>打</b>出来——"
               "打字要从拼音变成汉字，跟照着描不一样，单元测验的翻译题要的就是这个。",
               compact=True))
    add("23-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难",
               ["六句做完，自己再编六句，一样的玩法。"],
               "每一句都要有<b>今天的一个词</b>加<b>上节课的一个方位词</b>，"
               "至少两句是两个小句的。打乱了打在电脑上，跟同桌换电脑解。"))

    add("24-game.html", "Game · Writing Relay (4 min)", PRAC, "游戏 · 接力写字 · 4 分钟",
        s_list("游戏 · 接力写字 Writing Relay",
               [("四人一组，一支笔，一次写一个字", "老师说英文，第一个人写第一个字，跑回来换人"),
                ("词表", "洋房 · 花园 · 车库 · 房前 · 房后 · 卧室 · 客厅 · 厨房"),
                ("<b>算分看字对不对，不看谁快</b>", "先写完但笔顺错，分让给后面那一组"),
                ("<b>加难</b>：老师说中文，而且要写一整句", "一人一个字，出发前全组要先讲好写哪一句")],
               "黑板分成几栏，每组一支笔。"))

    add("25-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 第三条当场就能查——请全班把练习册举起来。",
                "<b>自评</b> · 三条目标，举手；再问一句：哪个字最难写？",
                "<b>出门条</b> · 写在本子上，收上来。",
                "<b>下节课</b> · 课文二最后那两个词，然后你自己设计一个房子，讲给全班听。"],
               cn="出门条：用中文回答——你家住什么样的房子？你家有花园吗？（至少两句）"))
    return S
