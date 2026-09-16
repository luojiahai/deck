# -*- coding: utf-8 -*-
"""Y9 L15 · Lesson 3 of 6 — 吵 / 醒 / 声 / 把 + the 把 sentence

Source: docs/lesson-plans/y9-l15/03-ba-sentence-mixed.md
Textbook p.147 Text 2 (first half), p.148 NOTE + Act. 7 (把 rewrites),
p.148 Act. 8 (TPR game), and three of p.146 Act. 6's dotted structures
(被, 一……就, 太……了). Workbook p.171 Ex. 14.

This is the unit's graded grammar and the heaviest lesson in the sequence.
把 gets the frame slide, the focus slide, the errors slide and the CFU —
four passes at one structure, which is the point.

把 is a function word and 声 is deliberately textonly (see art.py): cycle
2 is therefore two textonly cards, which is honest rather than padded.
"""
from build import (s_words, s_examples, s_write, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_errors,
                   s_dialogue, s_title, s_lisc, label)

SLUG = "l3-ba-sentence"
TITLE = "Y9 L15 · 邻居 Neighbours · Lesson 3 of 6"
CARD = (SLUG, "把我吵醒了", "The 把 Sentence · 谁—把—什么—动词—了",
        "grammar", "吵 · 醒 · 声 · 把。单元考试的语法点，"
                   "跟上一课的「被」并排放——同一件事，两头说。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 把我吵醒了", "LESSON 3 OF 6", "第十五课 · 邻居",
        s_title("把我吵醒了", "The 把 Sentence",
                "Year 9 · Book 3 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 3 · p.147–148 · 课文二、第 7、8 题"))

    add("02-review.html", "Review · L2 的「得」", REV, "复习 · Lesson 2",
        s_list("复习 · 三轮，每轮九十秒 · 白板",
               [("第一轮 · 老师说「他跑步」，你写「他跑得很快」", "四题，动词自己配形容词"),
                ("第二轮 · 屏幕上一个错句，你写改好的", "看「的／得」，看形容词的位置"),
                ("第三轮 · 转过去问同伴：半夜你听见过什么？", "三十秒，用「听见」"),
                ("连起来 · 「我听见小孩子哭」——那个哭声<b>做了什么</b>？",
                 "它<b>把你吵醒了</b>。今天就学这个")],
               "上一课你已经会说「我听见」。今天说的是：那个声音对你做了什么。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what someone did to something using the 把 sentence — "
               "and see how 把 and 被 tell the same story from opposite ends.",
               [("I can build a 把 sentence in the right order",
                 "能按顺序说：谁 + 把 + 什么 + 动词 + 了"),
                ("I can say someone woke me up", "能说：弟弟的哭声把我吵醒了"),
                ("I can use 吵, 醒 and 声 in a sentence", "能用上「吵」「醒」「声」"),
                ("I can turn a 被 sentence into a 把 sentence and back",
                 "能把「被」字句改成「把」字句，也能改回来")]))

    # ── Cycle 1 · 吵 / 醒 ──
    add("04-c1-words.html", "Cycle 1 · A — 吵 / 醒", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("吵", "chǎo", "noisy; make a noise", "chao"),
                ("醒", "xǐng", "wake up", "xing")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "楼上很<b>吵</b>。", "It's noisy upstairs."),
                    (None, "我半夜<b>醒</b>了。", "I woke up at midnight."),
                    (None, "楼上太<b>吵</b>了，所以我半夜<b>醒</b>了。",
                     "It was too noisy upstairs, so I woke up at midnight.", True)],
                   "你昨天晚上几点醒的？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 很吵。", "我 ________ 点醒了。"],
                "用「一……就……」写一句：<b>我一听见狗叫就醒了。</b>"
                " 再用「因为……，所以……」说一句：后来为什么睡不着？"))

    # ── Cycle 2 · 声 / 把 ──
    add("07-c2-words.html", "Cycle 2 · A — 声 / 把", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("声", "shēng", "sound", None),
                ("把", "bǎ", "marks what the action is done to", None)))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "电视机的<b>声</b>音太响了。",
                     "The television is far too loud."),
                    (None, "请<b>把</b>电视机关上。",
                     "Please turn the television off."),
                    (None, "请<b>把</b>电视机的<b>声</b>音开得小一点儿。",
                     "Please turn the television down.", True)],
                   "家里什么东西的声音最响？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["请把 ________ 关上。", "________ 的声音太响了。"],
                "同一个要求写<b>两遍</b>——一遍用「请把……」，一遍不用「把」。"
                " 然后说说：哪一句更像在<b>要求</b>别人？为什么？"))

    add("10-hanzi.html", "字 · 吵 / 醒 / 声 / 响", IDO, "看字 · How the words are built",
        s_list("看字 · 四个字，两两分开",
               [("吵 · 左边是「口」", "从嘴里出来的——所以又是「吵闹」，又是「吵架」"),
                ("吵醒 · 吵 + 醒", "用吵的方式把人弄醒。当成<b>一整块</b>记"),
                ("声 · 声音本身（名词）", "电视机的<b>声音</b>很响"),
                ("响 · 声音有多大（形容词）", "不能说「我响电视机」")],
               "「声」和「响」是这一课最容易混的一对——一个是<b>什么</b>，一个是<b>多大</b>。"))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · 把", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 「把」字句 · 课本 p.148 NOTE",
                  "谁 + 把 + 什么 + 动词 + 了／补语",
                  [("弟弟<b>把</b>牛奶喝了。", "My little brother drank the milk."),
                   ("请<b>把</b>你的电话号码留下。", "Please leave your phone number."),
                   ("弟弟的哭声<b>把</b>我吵醒了。",
                    "My brother's crying woke me up.")],
                  "动词后面<b>一定</b>还有东西——了、走、上、醒、下。"
                  "「我把手机借」不是一句话。"))
    add("12-chant.html", "谁—把—什么—动词—了", IDO, "句型 · 词序",
        s_task("词序 · 黑板上五张卡片，故意摆错，让全班摆回来",
               ["哥哥　·　把　·　我的手机　·　借走　·　了",
                "全班跟着念两遍：<b>谁 — 把 — 什么 — 动词 — 了</b>",
                "这一节课谁写错了，就回来念一遍这个顺序。"],
               cn="哥哥把我的手机借走了。"))
    add("13-ba-bei.html", "把 和 被 · 同一件事，两头说", IDO, "对照 · 把 vs 被",
        s_focus("对照 · 一件事，两个说法 · 这块留到下课",
                "哥哥把我的手机借走了。　／　我的手机被哥哥借走了。",
                "Same event, two sentences: start from the person who did it, "
                "or start from the thing it happened to.",
                "「把」从<b>做事的人</b>开始说，「被」从<b>被弄的东西</b>开始说。"
                "上一课学的「被」，今天就是它的另一头。",
                "把上面这一句改写成「被」字句：<b>妈妈把蛋糕吃了。</b>"
                " 改完，再自己写一对——一件你家真的发生过的事，两种说法都写。"))
    add("14-errors.html", "把 字句常见的错", IDO, "注意 · The one to get right",
        s_errors([("我把吵醒了你。", "你把我吵醒了。", "「把」后面放<b>东西／人</b>，不是动词"),
                  ("我把手机借。", "我把手机借走了。", "动词后面要有<b>结果</b>"),
                  ("我的自行车把哥哥骑走了。", "我的自行车被哥哥骑走了。",
                   "自行车不会骑人——这里要用「被」")],
                 "把 ≠ 被",
                 "第三个是整个单元最容易错的一句，考试也考。"))

    add("15-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「把」后边放什么——人／东西，还是动词？", "点名"),
               ("白板：写「弟弟的哭声把我吵醒了」。", "老师看：有没有「了」，「醒」怎么写"),
               ("这句哪里错了？ 我把吵醒了你。", "写出改好的句子"),
               ("「妈妈把蛋糕吃了」——用「被」怎么说？", "白板，举起来")]))

    add("16-text2.html", "Text 2 · 前两组", IDO, "课文二 · p.147 · CD 59",
        s_dialogue("课文二 · 前两组 · 两位同学分角色，再换一次",
                   [("A", "我就住在楼下。每天早上有人在房间里跑步，对吗？"),
                    ("B", "对。"),
                    ("A", "你把我吵醒了。"),
                    ("B", "对不起。我以后晚一点儿跑。")],
                   "说话的人住在几楼？ · 跑步的人说他以后会怎么做？"))

    # ── Flexible practice ──
    add("17-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("吵", "chao"), ("醒", "xing"), ("声", None), ("把", None)],
                  "这块板整个活动一都留在屏幕上。"))
    add("18-task.html", "Activity 1 · 改成「把」字句", PRAC, "活动一 · We Do · 7 分钟",
        s_task("活动一 · 上一课那五个声音，现在写成「把」字句 · 两人一组，白板，五分钟",
               ["屏幕上五句普通句子：<b>楼上的小孩子半夜哭。</b> ……",
                "每一句改成「把」字句，结尾是<b>吵醒了</b>。",
                "五句里，今天的四个词都要出现。样子："],
               "五句各写<b>两遍</b>——一遍「把」，一遍「被」。"
               "再写第六句：有一个声音<b>没有人投诉</b>，"
               "用「因为……，所以……」说清楚为什么那个没关系。"
               "不看屏幕，「被」那一句的「了」不能丢。",
               cn="楼上小孩子的哭声把我吵醒了。"))
    add("19-activity2.html", "Activity 2 · 课本 p.148 第 7 题", PRAC,
        "活动二 · You Do · 8 分钟",
        s_list("活动二 · 七句改写成「把」字句 · 本子上写，六分钟",
               [("课本 p.148 第 7 题 · 七句，两人一张纸条，各自写在本子上",
                 "老师走动——写不下去的，回去念词序"),
                ("写完的继续：课本 p.146 第 6 题，挑三个结构各写一句",
                 "<b>被</b> · <b>一……就……</b> · <b>太……了</b>"),
                ("最后老师收三句读出来", "一句「把」、一句「被」、一句「一……就……」")],
               "答案不上屏——老师现场对。"))
    add("20-activity2-ext.html", "Activity 2 · Extension", PRAC,
        "活动二 · 给写得快的同学",
        s_task("活动二 · Extension · 七句写完以后",
               ["挑三句，写出<b>邻居的回答</b>——能用「把」的就用："
                "<b>对不起，我马上把电视机关上。</b>",
                "再写两句你<b>自己家</b>的事：一件是你对东西做的，"
                "一件是别人对你的东西做的。",
                "一句用「把」，一句用「被」。"],
               cn="我把弟弟的玩具放回去了。我的书被妹妹拿走了。"))
    add("21-game.html", "Game · 老师说 TPR", PRAC, "游戏 · 8 分钟",
        s_task("游戏 · 老师说 · 全班站起来 · 课本 p.148 第 8 题",
               ["老师说一个动作，全班做出来。做错的、慢的，坐下。剩三个人为止。",
                "前八个动作照课本念。<b>从第九个开始，老师改说「把」字句</b>——",
                "<b>把书打开 · 把手机放下 · 把眼睛闭上</b>。"
                "游戏就变成今天语法的听力测验。"],
               "最后剩下的三个人来当老师，出题<b>必须</b>是自己现编的「把」字句。"
               "词序说错的人出局，换下一个来出题。"))

    add("22-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 全班再念一遍词序：谁 — 把 — 什么 — 动词 — 了。",
                "<b>自评</b> · 白板：会了 · 差不多 · 还要练。",
                "<b>出门条</b> · 白板写一句，走的时候给我看。",
                "<b>下节课</b> · 你已经被吵醒了——现在怎么<b>有礼貌地</b>去跟邻居说？"],
               cn="出门条：用「把」写一句话，说昨天晚上什么声音把你吵醒了。"))

    return S
