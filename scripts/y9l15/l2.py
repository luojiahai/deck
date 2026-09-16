# -*- coding: utf-8 -*-
"""Y9 L15 · Lesson 2 of 6 — 听见 / 响 / 半夜 / 哭 + V + 得 + 形容词

Source: docs/lesson-plans/y9-l15/02-noisy-neighbour-text1-writing.md
Textbook p.142 Text 1 (complete), p.146 Act. 5 (CD 58). Workbook p.164
Ex. 1, p.166 Ex. 7.

The teacher chose a writing direction for this lesson, so the CD 58 tick
exercise runs as listen-and-WRITE — students write the noise in characters
rather than ticking a, b or c. The six items keep their numbering so the
textbook page still works alongside.

得 is the whole lesson. The错误 slide is not decoration: 的 written for 得
is the single most common slip in this structure and it is invisible when
students say the sentence aloud.
"""
from build import (s_words, s_examples, s_write, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_errors, s_text,
                   s_listening, s_title, s_lisc, label)

SLUG = "l2-noisy-neighbour"
TITLE = "Y9 L15 · 邻居 Neighbours · Lesson 2 of 6"
CARD = (SLUG, "烦人的邻居", "What You Can Hear · V + 得 + 形容词",
        "writing", "听见 · 响 · 半夜 · 哭，加「开得很响」。"
                   "课文一全文，CD 58 听写，整节课都在写。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 烦人的邻居", "LESSON 2 OF 6", "第十五课 · 邻居",
        s_title("烦人的邻居", "What You Can Hear",
                "Year 9 · Book 3 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 3 · p.142、p.146 · 课文一、第 5 题"))

    add("02-review.html", "Review · L1 四个词", REV, "复习 · Lesson 1",
        s_task("复习 · 今天是写的课，复习也用写的 · 六分钟",
               ["<b>第一轮</b> · 本子上写中文，四句："
                "we moved recently · the neighbours upstairs are annoying · "
                "my neighbour is Chinese · have you moved recently?",
                "<b>第二轮</b> · 跟同伴换本子，对着黑板改。改完一组读一句。",
                "<b>点名</b> · 三位同学，用「最近……有没有……？」问一个问题，口头回答。"],
               cn="上一课你们说邻居很烦人。可是——到底烦在哪儿？今天我们把它写下来。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("write about the noises we hear from our neighbours, and "
               "say how loudly something is done using V + 得 + 形容词。",
               [("I can say what I hear, using 听见 + a clause",
                 "能说我听见什么：我听见有人在房间里跑步"),
                ("I can say how something is done", "能说做得怎么样：电视机开得很响"),
                ("I can use 半夜 and 哭 in a written sentence",
                 "能在句子里用上「半夜」和「哭」"),
                ("I can write four sentences without looking at the board",
                 "不看屏幕，也能写出四句")]))

    # ── Cycle 1 · 听见 / 响 ──
    add("04-c1-words.html", "Cycle 1 · A — 听见 / 响", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("听见", "tīngjiàn", "hear", "tingjian"),
                ("响", "xiǎng", "loud; noisy", "xiang")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我<b>听见</b>有人在房间里跑步。",
                     "I hear someone running in the room."),
                    (None, "他们的电视机开得很<b>响</b>。",
                     "Their television is on very loud."),
                    (None, "我<b>听见</b>楼上的电视机开得很<b>响</b>。",
                     "I can hear the television upstairs on very loud.", True)],
                   "你在家里听见过什么声音？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我听见 ________ 。", "________ 开得很响。"],
                "用「一……就……」写一句：<b>我一回家就听见楼上的音乐开得很响。</b>"
                " 再加上<b>几点钟</b>，还有<b>是谁</b>。"))

    # ── Cycle 2 · 半夜 / 哭 ──
    add("07-c2-words.html", "Cycle 2 · A — 半夜 / 哭", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("半夜", "bànyè", "midnight", "banye"),
                ("哭", "kū", "cry", "ku")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "<b>半夜</b>我还听见孩子<b>哭</b>。",
                     "At midnight I can still hear a child crying."),
                    (None, "我弟弟每天<b>半夜哭</b>。",
                     "My little brother cries every night at midnight."),
                    (None, "<b>半夜</b>的时候，我听见楼下的小孩子<b>哭</b>得很响。",
                     "At midnight I heard the child downstairs crying loudly.", True)],
                   "半夜你听见过什么？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["半夜我听见 ________ 。", "________ 哭得很 ________ 。"],
                "用「因为……，所以……」写两个小句："
                "<b>因为楼上的小孩子半夜哭，所以我睡不好。</b>"
                " 再写一句：后来你做了什么？"))

    add("10-hanzi.html", "字 · 听 / 听见 · 半 / 夜", IDO, "看字 · How the words are built",
        s_list("看字 · 四个词，拆开看",
               [("听 · 听见", "「听」是动作，「见」是结果——听了不一定听见"),
                ("看 · 看见", "一样的道理，你们已经会这一对了"),
                ("半 · 夜 · 半夜", "夜里的一半——「半」你们在「五点半」见过"),
                ("哭 · 两只眼睛，一张嘴，泪掉下来", "老师在黑板上一笔一笔写一遍")],
               "「响」说的是声音<b>有多大</b>，不是你怎么弄出声音——"
               "电视机<b>开得</b>很响，不能说「我响电视机」。"))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · V + 得 + 形容词", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 事情做得怎么样",
                  "动词 + 得 + 很 + 形容词",
                  [("他跑<b>得</b>很快。", "He runs fast."),
                   ("小孩子哭<b>得</b>很响。", "The child is crying loudly."),
                   ("楼上的邻居半夜跑步跑<b>得</b>很响。",
                    "The neighbours upstairs run so loudly at midnight.")],
                  "有宾语的时候，动词要再说一遍："
                  "<b>跑步跑得很响</b>、<b>开电视机开得很响</b>。"))
    add("12-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 听见 + 得 + 转折",
                "我听见楼上的孩子哭得很响，可是我不知道他为什么哭。",
                "I can hear the child upstairs crying loudly, "
                "but I don't know why.",
                "一句话里有三样东西：听见、得、可是。今天的作文就照这个样子写。"))
    add("13-errors.html", "得 不是 的", IDO, "注意 · The one to get right",
        s_errors([("他跑的很快。", "他跑得很快。", "动词后面用<b>得</b>，不是「的」"),
                  ("他很快跑得。", "他跑得很快。", "顺序：动词 → 得 → 形容词"),
                  ("电视机响开。", "电视机开得很响。", "「响」不能当动词用")],
                 "得 / 的 —— 说出来一样，写出来不一样",
                 "这一课全班最容易错的就是这个。老师走动的时候，专门看这一个字。"))

    add("14-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「听」和「听见」有什么不一样？", "点名，中文或者英文都可以"),
               ("白板：写「电视机开得很响」。", "举起来——老师专门看「得」"),
               ("这句哪里错了？ 他很快跑得。", "写出改好的句子"),
               ("「半夜」是几点？", "大概十二点的比大拇指朝上")]))

    add("15-text1.html", "Text 1 · 全文", IDO, "课文一 · p.142 · CD 57",
        s_text("课文一 · 全文 · 前两句你们上节课见过",
               "我们家最近搬家了。新房子很好，可是楼上的邻居很烦人。"
               "我早上五点就听见有人在房间里跑步。晚上十二点，他们的电视机还开得很响。"
               "每天半夜还听见孩子哭。",
               "他早上五点听见了什么？ · 晚上十二点，楼上在做什么？ · "
               "课文里哪一句用了「得」？请读出来。",
               "三个时间：早上五点、晚上十二点、半夜。一整天都不安静。"))

    # ── Flexible practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("听见", "tingjian"), ("响", "xiang"),
                   ("半夜", "banye"), ("哭", "ku")],
                  "这块板整个活动一都留在屏幕上——写的时候可以看。"))
    add("17-task.html", "Activity 1 · 半夜，我听见……", PRAC, "活动一 · We Do · 7 分钟",
        s_task("活动一 · 半夜的那栋楼 · 屏幕上五个亮着的窗户 · 本子上写，五分钟",
               ["写<b>四句话</b>，说你在楼下听见了什么。",
                "规矩很紧：<b>每一句都要用「听见」</b>，"
                "四句里<b>四个生词都要用上</b>，<b>至少两句要用「得」</b>。",
                "写完跟同伴换本子，专门查对方的「得」。老师请两位读出来。"],
               "写成<b>一段话</b>，不是四个句子——你是住在一楼睡不着的那个人。"
               "五句以上，用<b>可是／因为……所以……／一……就……</b>连起来，"
               "三个「得」要配<b>三个不一样的形容词</b>（响、快、好）。"
               "最后一句：明天你打算怎么办？不看总览板。"))
    add("18-listening.html", "Activity 2 · CD 58 · 听写", PRAC,
        "活动二 · You Do · 8 分钟",
        s_listening("活动二 · 听 CD 58 · 每题放两遍 · 课本 p.146 第 5 题",
                    [("1 · 楼上的邻居养了什么？", "第一遍：写下那个声音（两三个字）"),
                     ("2 · 隔壁的孩子每天晚上做什么？", "狗／鸟／球／电视／电影／跳舞"),
                     ("3 · 小明家的邻居晚上做什么？", "第二遍：挑两题，写成完整的句子"),
                     ("4 · 小天的邻居早上五点听见什么？", "句子里要有「得」"),
                     ("5 · 小东的邻居周末做什么？", "例：电视机开得很响"),
                     ("6 · 小云家楼上的邻居晚上做什么？", "老师走动，看第二遍写得怎么样")],
                    "答案不上屏——第二遍写完，请三位同学把整句读出来。"))
    add("19-listening-ext.html", "Activity 2 · Extension", PRAC,
        "活动二 · 给写得快的同学",
        s_task("活动二 · Extension · 六题全写，而且每一题都<b>回一句</b>",
               ["你是被投诉的那个<b>邻居</b>。每题写两句：先道歉，再说你以后怎么改。",
                "六个回答不能一样——<b>我以后早一点儿／晚一点儿／小声一点儿／"
                "在外面……</b>",
                "最后自己编<b>第七题</b>，写成录音的样子，老师可能会念给全班听。"],
               cn="对不起，我以后十点以后不看电视了。"))
    add("20-game.html", "Game · Bingo", PRAC, "游戏 · 8 分钟",
        s_task("游戏 · Bingo · 自己画一个三乘三的格子，自己填",
               ["词库（十二个选九个，<b>要写汉字，不写拼音</b>）：",
                "听见 响 半夜 哭 跑步 电视机 狗叫 鸟叫 跳舞 踢球 看电影 邻居",
                "老师<b>不说单词</b>——老师说一整句，句子里有哪个词，就划掉哪个。",
                "例：<b>每天半夜，楼上的小孩子哭得很响。</b> 三个连成一线就喊「中了」。"],
               "喊「中了」以后，要先把那三个词读出来，"
               "再用<b>三个词一起</b>说一句话，才算数。说不出来，游戏继续，下一线再试。"))

    add("21-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 老师读一条，全班给一句对得上的中文。",
                "<b>自评</b> · 白板举手：会了 · 差不多 · 还要练。"
                "<b>第二条（得）</b>如果三分之一是「差不多」，下节课开头再教一遍。",
                "<b>出门条</b> · 本子上写一句，走的时候给我看。",
                "<b>下节课</b> · 邻居<b>把</b>你吵醒了——我们学一个新句子。"],
               cn="出门条：用「得」写一句话，说你的邻居半夜做什么。"))

    return S
