# -*- coding: utf-8 -*-
"""Y8 L14 · Lesson 6 of 6 — buying furniture, and describing a whole house

Source: docs/lesson-plans/y8-l14/06-furniture-shopping-describe-mixed.md
Textbook p.136 Act. 8, p.140 Act. 15, p.141 Act. 17.
Workbook pp.162–163 (E→C translation of the appliance and furniture names).

No new nouns. The pattern is assembled entirely from parts the class
already has — 应该 (Unit 4), 楼 and 几 (Lesson 13), 上 and 请 (Year 7) —
which is worth saying out loud to the students rather than glossing over.

This lesson also carries the series' only radical work, added at the
teacher's later request. The sequence was built without radicals on
instruction, and the cost was stated at the time: Unit 5 Test parts 3 and
4 ask for the radical of a character and the simple character inside a
compound, so students would have met two of eleven test parts cold. The
slot runs as this lesson's game rather than as a fourth activity, so the
23-minute practice block still balances — 20 Questions goes, and the
p.141 Ex. 17 interview board stays as the fallback if the race runs short.

Content is the book's own: the eight simple characters of p.126 Ex. 7 and
p.137 Ex. 11, then the exact six characters of Test part 3 and the exact
six compounds of Test part 4. Both boards are tasks, not answers.
"""
from build import (s_recall, s_summary, s_pattern, s_focus, s_task, s_list,
                   s_cfu, s_figure, s_dialogue, s_errors, s_chars, s_radicals,
                   s_title, s_lisc)

SLUG = "l6-furniture-shopping"
TITLE = "Y8 L14 · 家具 Furniture · Lesson 6 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='应该上几楼？', en='Buying furniture · describing a house',
            desc='No new nouns — the last lesson assembles what is already there. Pairs build a four-storey furniture store, run it, and then describe a whole furnished house to the class. The plenary looks back across all six lessons, not just this one.',
            words='（没有生词 · 句型：应该上几楼？）', n=0)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 应该上几楼？", "LESSON 6 OF 6", "第十四课 · 家具",
        s_title("我要买衣柜，应该上几楼？", "Buying Furniture, Describing a House",
                "Year 8 · Book 2 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 2 · p.136 · p.140 · p.141"))

    add("02-review.html", "Review · the fifteen, against the clock", REV,
        "复习 · 抢答 · 90 秒",
        s_recall(["沙发", "茶几", "电视柜", "张", "空调", "洗衣机", "里面", "冰箱",
                  "烤箱", "电炉", "椅子", "把", "书桌", "衣柜", "书架"],
                 "先把这一页换成<b>只有图、编号 1–15</b>，九十秒写出中文，量词也要写。"
                 "写得最多的念一遍，全班一起补。", cols=5))
    add("03-review-errors.html", "Review · three to fix", REV, "复习 · 改一改",
        s_errors([("我的房间有一个椅子。", "我的房间有一把椅子。", "椅子用「把」"),
                  ("洗衣机有厨房。", "洗衣机在厨房里面。", "已知的东西找地方 → 在，而且要方位词"),
                  ("你有不有书架？", "你有没有书架？", "「有」配「没」，不配「不」")],
                 "三句 · 五节课各挑一个最常错的",
                 "这三条正好是单元测验最爱考的三条。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("ask which floor of a store sells what we want, and describe a "
               "furnished house to the class.",
               [("I can ask which floor sells something", "会问「我要买衣柜，应该上几楼？」"),
                ("I can direct someone to a floor", "会答「请上三楼」"),
                ("I can describe a room out loud for a minute, without reading it",
                 "能不看稿，用中文说一分钟")]))
    add("05-no-new-words.html", "No new words today — and that's the point", IDO,
        "今天没有生词",
        s_figure("jiajudian", "今天一个新词都没有",
                 ["<b>应该</b>　第四单元学的。　<b>楼</b>　<b>几</b>　第十三课学的。",
                  "<b>上</b>　<b>请</b>　七年级就学了。",
                  "所以今天这个句型，是用你<b>已经有的零件</b>拼出来的——"
                  "这正是学到现在最该注意的一件事。",
                  "屏幕上的十五个词也一个不少，整节课都留着。"],
                 cn="我要买衣柜，应该上几楼？　——　请上三楼。"))

    add("06-summary.html", "Summary board · 词汇总览 · 十五个", IDO,
        "词汇总览 · stays on screen all lesson",
        s_summary([("沙发", "shafa"), ("茶几", "chaji"), ("电视柜", "dianshigui"),
                   ("张", None), ("空调", "kongtiao"), ("洗衣机", "xiyiji"),
                   ("里面", "limian"), ("冰箱", "bingxiang"), ("烤箱", "kaoxiang"),
                   ("电炉", "dianlu"), ("椅子", "yizi"), ("把", None),
                   ("书桌", "shuzhuo"), ("衣柜", "yigui"), ("书架", "shujia")],
                  "第十四课全部生词。今天三个活动都要用到它们——全部。", dense=True))

    add("07-pattern.html", "Pattern · 应该上几楼？", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 在家具店问路",
                  "（请问，）我要买 ＋ 东西 ＋ ，应该上几楼？　→　请上 ＋ 数字 ＋ 楼。",
                  [("我要买衣柜，<b>应该上几楼</b>？　——　<b>请上三楼</b>。",
                    "The basic exchange, straight from p.136."),
                   ("我要买冰箱，<b>应该上几楼</b>？　——　<b>请上四楼</b>。",
                    "Same frame, different item and floor."),
                   ("<b>请问</b>，你们有没有书架？　——　有，在二楼。",
                    "Opening with 请问, and last lesson's V-not-V carried straight in.")],
                  "<b>请问</b>是跟陌生人开口之前那一句。第十五课问路的时候，它会一直出现。"))
    add("08-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("一次买两样，回答要把两样都处理掉",
                "请问，我要买一张书桌和一把椅子，应该上几楼？"
                "　——　书桌在三楼，椅子也在三楼，请上三楼。",
                "Excuse me, I want to buy a desk and a chair — which floor should I go to? "
                "— Desks are on the third floor and chairs are too, so please go to the third.",
                "两样东西、两个量词，答话要先说清楚各在几楼，再给一句结论。"))

    add("09-dialogue.html", "Dialogue · p.136 Ex.8", IDO, "对话 · 课本 p.136 第 8 题",
        s_dialogue("老师先跟一个同学演两遍，再全班齐读，再两人练",
                   [("A", "请问，我要买沙发，应该上几楼？"),
                    ("B", "请上二楼。"),
                    ("A", "我还要买一个冰箱，应该上几楼？"),
                    ("B", "冰箱在四楼，请上四楼。")],
                   "两人练的时候，四轮，每轮换一样东西——从总览页上挑，不许重复。"))

    add("10-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("怎么问「在几楼」？", "全班一起说。再说一次，这次买冰箱"),
               ("翻译：<i>Please go to the fourth floor.</i>", "写在小白板上"),
               ("这句话对不对？　我要买衣柜，应该几楼？", "少了一个字，少了哪个？"),
               ("点三个同学，各说一样东西，全班答几楼", "答案是你们自己定的，只要说得出来就算")]))

    # ── Practice ──
    add("11-act1.html", "Activity 1 · Design a furniture store (7 min)", PRAC,
        "活动一 · 7 分钟",
        s_figure("jiajudian", "活动一 · 两人开一家四层的家具店",
                 ["<b>3 分钟</b>　把总览页上<b>十五个词全部</b>分到四层楼去——"
                  "一个都不能落下。",
                  "每一层用中文写一个名字，写得出理由才算数。",
                  "<b>2 分钟</b>　照你们自己的楼层表，写三组完整的问答。",
                  "请两组念自己的楼层表，全班检查有没有漏掉的词。"],
                 cn="我要买书架，应该上几楼？　——　请上三楼。"))
    add("12-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["开<b>五层</b>，第五层专门放「哪儿都不属于」的东西。",
                "用中文给第五层起个名字，还要替<b>两样</b>东西辩护，说明为什么放在那儿。",
                "再写一组客人要买你们店里<b>没有</b>的东西的对话，并且回答他。"],
               cn="电视柜不是厨房的东西，也不是卧室的东西，所以在五楼。"
                  "　／　对不起，我们没有……"))

    add("13-act2.html", "Activity 2 · Run the store (5 min)", PRAC,
        "活动二 · 角色扮演 · 5 分钟",
        s_list("活动二 · 一个当客人，一个当店员",
               [("老师发给每组一张纸条，上面四样东西", "每组的四样不一样"),
                ("客人问四次，然后换角色，再换四样", "开口一定要说「请问」"),
                ("回答不能只说数字，要说一整句", "✗ 三楼　　✓ 请上三楼。"),
                ("老师走动，把楼层表从说得出来的那组收走", "留给还需要看的那组")],
               "纸条提前写好——每组四样，从十五个词里挑。", compact=True))
    add("14-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难",
               ["客人<b>不说东西的名字</b>——只描述它，店员要先猜出来才能回答。",
                "店员回答的时候，东西的名字和楼层都要说出来。",
                "然后店员还要<b>多卖他一样</b>他本来没打算买的东西。"],
               cn="我要买一个大的，可以放很多书，在房间里面。"))

    add("15-act3.html", "Activity 3 · p.140 Ex.15 — describe the interior (6 min)", PRAC,
        "活动三 · 看图说话 · You Do · 6 分钟",
        s_task("活动三 · 课本 p.140 第 15 题",
               ["<b>3 分钟</b>　安静，看图写五到六句：房间、家具、位置、大小。",
                "<b>然后把书合上，图翻过去。</b>",
                "<b>2 分钟</b>　两人一组，一个人凭记忆说出来，"
                "另一个人数他用了几个生词（十五个里的）。",
                "每组数得最多的那一个，说给全班听。"],
               cn="客厅不算大，里面有一张沙发和一个茶几，电视在电视柜上面。"))
    add("16-act3-ext.html", "Activity 3 · Extension", PRAC, "活动三 · Extension",
        s_task("活动三 · 加难",
               ["不说图上的房子——说<b>你自己家</b>，而且要站起来对全班说满一分钟，不看纸。",
                "开头先说房子（第十三课：层、楼上、楼下），",
                "每个房间用「有」请东西进来，至少三样东西用「在」摆好位置，",
                "最后用「不算大」或者「特别」下一个判断。",
                "说完，接受全班两个「V 不 V」提问，并且回答。"],
               cn="我家的房子有两层，楼下有客厅和厨房……我的房间不算大，可是我特别喜欢。"))

    add("17-interview.html", "p.141 Ex.17 · the full interview", PRAC,
        "问题卡 · 课本 p.141 第 17 题",
        s_list("七组问题 · 课本 p.141 第 17 题 · 六节课走一遍，游戏接不上时用",
               [("你有没有自己的房间？", "第五节课"),
                ("你的房间里有什么？", "带量词"),
                ("你的房间大不大？", "不算大 ／ 不大也不小"),
                ("你的书桌上有什么？", "用「在」说位置"),
                ("你们家的客厅里有什么？", "第一、二节课"),
                ("你们家的厨房里面有什么？", "第三节课"),
                ("你想不想买新家具？买什么？", "「V 不 V」＋ 总览页")],
               compact=True))

    # ── The series' only radical work. Added after the fact, at the
    # teacher's request; see the module docstring for why it sits here and
    # why it replaced the game rather than becoming a fourth activity.
    add("18-chars.html", "Simple characters · p.126 Ex.7 + p.137 Ex.11", PRAC,
        "游戏 · 第一步 · 90 秒 · 先认清楚",
        s_chars([("光", "guāng", "light", "第十三课 p.126"),
                 ("金", "jīn", "gold", "第十三课 p.126"),
                 ("匕", "bǐ", "dagger", "第十三课 p.126"),
                 ("入", "rù", "enter", "第十三课 p.126"),
                 ("井", "jǐng", "well", "第十四课 p.137"),
                 ("亡", "wáng", "die", "第十四课 p.137"),
                 ("乌", "wū", "black; dark", "第十四课 p.137"),
                 ("勺", "sháo", "spoon", "第十四课 p.137")],
                "独体字 · 这个单元课本教的八个 · Unit 5's simple characters",
                "这八个字，这个单元一直没教——现在看九十秒，因为下面两轮要用，"
                "单元测验也要用。有的就藏在后面那六个字里面。"))

    add("19-radicals-1.html", "Game · round 1 — write the radical", PRAC,
        "游戏 · 第二步 · 部首抢答",
        s_radicals(["层", "厅", "辆", "冰", "超", "站"],
                   "游戏 · 第一轮 · 写部首 · 四人一组，写在纸上",
                   "每个字的部首是什么？写下来，再写它的意思。九十秒。",
                   bank=["尸", "厂", "车", "冫", "走", "立", "口", "火", "氵"],
                   note="写对最多的一组得分。<b>方格里有三个是多出来的。</b>　"
                        "单元测验第三部分考的就是这六个字，"
                        "而且<b>考试不给方格</b>——今天给，是因为这是第一次。"))

    add("20-radicals-2.html", "Game · round 2 — find the simple character", PRAC,
        "游戏 · 第三步 · 找独体字",
        s_radicals(["毕", "忘", "返", "蚂", "仙", "鸣"],
                   "游戏 · 第二轮 · 找里面的独体字 · 同一组，继续写",
                   "每个字里面藏着一个独体字，把它找出来，写下来。九十秒。",
                   note="这一轮<b>没有方格</b>，跟单元测验第四部分一样。"
                        "上一页那八个字里，有的就在这六个字里面——先回头看一眼。"
                        "两轮加起来分最高的一组赢。"))

    add("19-plenary.html", "Plenary · all six lessons", PLEN, "小结 · 六节课一起看",
        s_task("小结 · 43–50 分钟 · 这一次看的是整课，不只是今天",
               ["<b>回看目标</b> · 把六节课的 success criteria 一起放上来，"
                "一节课一节课念——一共十八条。",
                "<b>自评</b> · 小白板上画六行，一行一节课：👍 / 😐 / 👎。"
                "<b>收上来</b>——这是单元测验之前你能拿到的、最清楚的一张全班情况表。",
                "<b>出门条</b> · 两行，写在同一张纸条上。",
                "<b>下一课</b> · 第十五课，我们出门——社区、商店、有多远、怎么去。"],
               cn="出门条：① 我要买 ______，应该上几楼？　"
                  "② 用一句话说你家的任何一个房间，量词要对。"))
    return S
