# -*- coding: utf-8 -*-
"""Y9 L15 · Lesson 5 of 6 — 正在……呢, the phrase bank, and borrowing

Source: docs/lesson-plans/y9-l15/05-zhengzai-borrowing-mixed.md
Textbook p.145 Act. 4 (activity pictures + connector bank), p.149 Act. 9
(正在……呢, 11 pictures), p.150 Act. 12 (谢谢你提醒我 …), p.151 Act. 14
(borrowing role play). Workbook p.169 Ex. 13.

No new vocabulary. There are therefore no cycles and no summary board —
the I Do time goes to one pattern and one phrase bank instead. This deck
is shorter than the vocabulary decks and that is correct: the slides are
here to start activities, not to be read.

Act. 4 was kept at the teacher's request when the sequence was scoped, and
sits here rather than in Lesson 1 because 平时 (what someone usually does)
only becomes worth teaching once 正在……呢 (right now) is there to contrast
it with.
"""
from build import (s_task, s_list, s_cfu, s_errors, s_pattern, s_focus,
                   s_recall, s_title, s_lisc, label)

SLUG = "l5-right-now"
TITLE = "Y9 L15 · 邻居 Neighbours · Lesson 5 of 6"
CARD = (SLUG, "他们正在干什么呢？", "In the Building Right Now · 正在……呢",
        "speaking", "没有生词——整节课在用。正在……呢、"
                    "谢谢你提醒我那一组说法，还有借了不还的邻居。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 他们正在干什么呢？", "LESSON 5 OF 6", "第十五课 · 邻居",
        s_title("他们正在干什么呢？", "In the Building Right Now",
                "Year 9 · Book 3 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 3 · p.145、p.149–151 · 第 4、9、12、14 题"))

    add("02-review.html", "Review · L4 的请求", REV, "复习 · Lesson 4",
        s_list("复习 · 三轮 · 白板 + 口头",
               [("第一轮 · 老师用中文说一个问题，你写有礼貌的请求",
                 "四个问题，例：你的同学说话太快了"),
                ("第二轮 · 同样四个，两人对话说出来",
                 "一个用「注意」回答，一个用「没有办法」"),
                ("点名 · 你的邻居半夜开派对，你会怎么说？", "两位同学")],
               "你们已经会敲门了。可是敲门<b>以前</b>，"
               "你得先知道他们正在做什么。今天说「现在」。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what people are doing right now, thank people and "
               "accept apologies properly, and ask a neighbour to give "
               "something back.",
               [("I can say what someone is doing at this moment",
                 "能说现在：他们正在看电视呢"),
                ("I can use the right phrase for the moment",
                 "能用对说法：谢谢你提醒我／不用客气／没关系"),
                ("I can join sentences with 因为……所以……, 可是, 平时, 经常",
                 "能用连词把句子连起来"),
                ("I can ask for something back politely",
                 "能有礼貌地要回来：能不能把我的……还给我？")]))

    add("04-no-new-words.html", "今天没有生词", IDO, "说明 · No new vocabulary",
        s_task("今天没有生词 · 今天全部是<b>用</b>",
               ["前面四节课的十二个生词，今天要说进长一点儿的话里。",
                "I Do 的时间给<b>一个句型</b>和<b>一组说法</b>，不做生词循环。",
                "下节课也一样——最后两节课是把学过的东西用出来。"],
               cn="最近 搬家 邻居 烦人 听见 响 半夜 哭 吵 醒 声 办法"))

    # ── Pattern ──
    add("05-pattern.html", "Pattern · 正在……呢", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 现在，这个时候",
                  "谁 + 正在 + 动词（+ 宾语）+ 呢",
                  [("他<b>正在</b>吃饭<b>呢</b>。", "He's having dinner right now."),
                   ("楼上的邻居<b>正在</b>跳舞<b>呢</b>。",
                    "The neighbours upstairs are dancing right now."),
                   ("我打电话的时候，他们<b>正在</b>吵架<b>呢</b>。",
                    "When I rang, they were in the middle of an argument.")],
                  "前面「正在」，后面「呢」。写的时候「呢」可以省，"
                  "说出来带上「呢」才自然——今天都带上。"))
    add("06-contrast.html", "平时 和 现在", IDO, "对照 · 这块留到下课",
        s_focus("对照 · 同一个人，两种说法",
                "我每天晚上看电视。　／　我正在看电视呢。",
                "One is a habit, the other is this exact moment.",
                "左边是<b>平时</b>、<b>通常</b>、<b>经常</b>；"
                "右边是<b>现在</b>、<b>这个时候</b>。活动二两种都要写。"))
    add("07-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 时间 + 正在 + 结果",
                "昨天半夜我醒了，楼上的小孩子正在踢球呢，所以我没有办法再睡。",
                "I woke up at midnight last night; the child upstairs was "
                "kicking a ball about, so there was no way I could get back "
                "to sleep.",
                "一句话里有四节课的东西：半夜、醒、正在……呢、没有办法。"))

    add("08-phrases.html", "说法 · 谢谢你提醒我", IDO, "p.150 第 12 题 · Phrase bank",
        s_recall(["谢谢你", "非常感谢", "不用客气",
                  "没关系", "对不起", "请注意", "谢谢你提醒我"],
                 "跟读两遍。老师读 p.150 四组图的第一句，全班接上该说的那一句——"
                 "两句都说得通的，问一问哪一句更好。",
                 cols=4, head="说法 · 课本 p.150 第 12 题 · 一起读两遍"))

    add("09-errors.html", "正在……呢 常见的错", IDO, "注意 · The one to get right",
        s_errors([("他正在呢跳舞。", "他正在跳舞呢。", "「呢」在<b>最后</b>"),
                  ("他正在每天看电视呢。", "他每天看电视。", "「每天」是习惯，不能配「正在」"),
                  ("我说谢谢，他说对不起。", "我说谢谢，他说不用客气。", "回「谢谢」要用「不用客气」")],
                 "正在 在前，呢 在后",
                 "第二个不是小错——「正在」和「每天」放在一起，意思就打架了。"))

    add("10-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「他看电视」和「他正在看电视呢」有什么不一样？", "点名，用中文回答"),
               ("白板：写「楼上的邻居正在跳舞呢」。", "举起来"),
               ("这句哪里错了？ 他正在呢跳舞。", "写出改好的句子"),
               ("我踩了你的脚，我说「对不起」，你说什么？", "全班一起说")]))

    # ── Flexible practice ──
    add("11-task.html", "Activity 1 · 他们正在干什么呢？", PRAC,
        "活动一 · We Do · 7 分钟",
        s_task("活动一 · 课本 p.149 第 9 题 · 十一张图 · 两人一张，各写各的本子",
               ["<b>先写四分钟</b> · 一张图一句「正在……呢」，能写几张写几张。",
                "<b>再说三分钟</b> · 同伴随便指一张，你<b>不看本子</b>回答。",
                "最后请两位同学，当场回答三张随机的图。"],
               "把十一张写成<b>一整段</b>——晚上十一点，从一楼扫到顶楼："
"<b>一楼的邻居正在……呢，二楼的……</b>。"
               "其中三句要说这个声音<b>传不传得到你那儿</b>（我听见……／我没听见……）。"
               "最后一句：最吵的那一个，你打算怎么办？用「把」或者「能不能」。"))
    add("12-activity2.html", "Activity 2 · 平时和现在", PRAC,
        "活动二 · You Do · 8 分钟",
        s_list("活动二 · 课本 p.145 第 4 题 · 七张图 · 本子上写，六分钟",
               [("每张图写两三句", "一句<b>平时</b>（平时／通常／经常），"
                                   "一句<b>现在</b>（正在……呢）"),
                ("连词至少用四个", "可是／但是 · 因为 · 所以 · 特别喜欢 · "
                                   "非常不喜欢 · 最喜欢 · 平时 · 通常 · 经常 · 很会"),
                ("老师收三位同学，各读一张图", "读的时候要听出「平时」和「现在」的分别")],
               "连词表印在图的下面，不上屏——写得顺的同学可以把它翻过去。"))
    add("13-activity2-ext.html", "Activity 2 · Extension", PRAC,
        "活动二 · 给写得快的同学",
        s_task("活动二 · Extension · 不要写七张，写<b>三张</b>——但写成一段话",
               ["一个邻居，三件事都是他做的。六句以上：",
                "他<b>平时</b>做什么 · 他<b>正在</b>做什么 · 你<b>特别喜欢</b>还是"
                "<b>非常不喜欢</b>，为什么。",
                "「因为……所以……」用两次，「虽然……但是……」用一次。连词表翻过去。"],
               cn="我楼上的邻居平时很安静，可是他今天正在开派对呢。"))
    add("14-game.html", "Game · 借东西 Role Play", PRAC, "游戏 · 8 分钟",
        s_task("游戏 · 借了不还 · 课本 p.151 第 14 题 · 两人一张卡，准备两分钟",
               ["借东西的人<b>第一次一定要推掉</b>——"
                "<b>我正在用呢 · 我找不到了 · 对不起，我忘了</b>，第二次才能还。",
                "要东西的人整场<b>不能生气</b>，每一轮都要用上一句礼貌的说法。",
                "演完换卡、换角色再来一次。最后两组演给全班，"
                "投票选<b>最有耐心的主人</b>和<b>最会找借口的邻居</b>。"],
               "给流利的同学：东西已经<b>弄坏了</b>。借的人要说出来、道歉、"
               "还要提一个解决办法（<b>我把你的……弄坏了，我会……</b>）。"
               "主人用「没关系」接受，然后两个人谈接下来怎么办。不准备，直接演。"))
    add("15-filler.html", "如果还有时间 · Quizlet Live", PRAC, "备用 · If time allows",
        s_task("备用 · 角色扮演提前结束的话",
               ["Quizlet Live，两轮，前四节课的十二个词：",
                "最近 搬家 邻居 烦人 听见 响 半夜 哭 吵 醒 声 办法",
                "两轮就停——下一节课还有 Kahoot。"],
               cn="设备今天要用，下节课还要用。"))

    add("16-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 一位同学读四条，全班给第一条和第四条的中文例句。",
                "<b>自评</b> · 白板：会了 · 差不多 · 还要练。",
                "<b>出门条</b> · 白板写一句，走的时候给我看。",
                "<b>下节课</b> · 最后一课：画一栋楼，说说每一家住的是谁，"
                "然后写一段「我的邻居」。"],
               cn="出门条：现在是晚上十一点。写一句话，说你楼上的邻居正在干什么呢。"))

    return S
