# -*- coding: utf-8 -*-
"""Y8 L15 · Lesson 4 of 6 — 先……，然后…… (the games lesson)

Source: docs/lesson-plans/y8-l15/04-first-then-game.md
Textbook p.148 Text 2 (first four lines), p.150 Act. 11 (six picture
journeys). Workbook pp.167–168.

The teacher chose a game-dominated practice block for this lesson, so the
23 minutes are three games rather than two activities and a game. The
consolidation task that normally opens Flexible Practice is folded into
the first of them: the relay decks are stacked so every team writes 船,
电影院 and 然后 before the round ends.

Cycle 2 is a single word. 然后 has no partner in this lesson's word list
and pairing it with a filler would break the two-word rule from the other
direction — a cycle is at most two words, not exactly two.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_figure, s_dialogue, s_errors, s_title, s_lisc)

SLUG = "l4-first-then"
TITLE = "Y8 L15 · 社区 Neighbourhood · Lesson 4 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE · GAMES"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='先坐船，然后坐车', en='First… then…',
            desc='A journey with two legs, and the question that asks for one. The practice block is three games end to end — the teacher picked game-dominated for this lesson, so the consolidation task is folded into the relay rather than sitting beside it.',
            words='电影院 · 船 · 然后', n=3)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 先……，然后…… First, then", "LESSON 4 OF 6",
        "第十五课 · 社区",
        s_title("我先坐船，然后坐公共汽车", "First… Then…",
                "Year 8 · Book 2 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 2 · p.148, p.150"))

    add("02-review.html", "Review · Slap the Board — everything so far", REV,
        "复习 · 拍黑板",
        s_recall(["马路", "对面", "火车站", "路", "超市", "离", "远", "挺"],
                 "黑板上八个词，只有汉字。两个同学上来，老师说英文，"
                 "谁先拍到谁得分。三对，每对九十秒。", cols=4))
    add("03-review-errors.html", "Review · where 就 goes", REV, "复习 · 「就」在哪儿",
        s_errors([("电影院在马路对面就。", "电影院<b>就</b>在马路对面。",
                   "「就」在动词前面——昨天练过一次了")],
                 "改一改 · 小白板",
                 "黑板上那个「电影院」是新词，是今天的。"
                 "它在哪儿你已经会说了，<b>怎么去</b>还不会——这就是今天。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("describe a journey that has two parts.",
               [("I can say 电影院 and 船", "能说「电影院」和「船」"),
                ("I can join two stages of a journey with 先……，然后……",
                 "会用「先……，然后……」把两段路连起来"),
                ("I can ask how someone gets somewhere with 从……怎么去……？",
                 "会问「从你家怎么去电影院？」")]))

    # ── Cycle 1 · 电影院 / 船 ──
    add("05-c1-words.html", "Cycle 1 · A — 电影院 / 船", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("电影院（電影院）", "diànyǐngyuàn", "cinema", "dianyingyuan"),
                ("船", "chuán", "boat; ship", "chuan")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我家附近有一个<b>电影院</b>。", "There's a cinema near my home."),
                    ("我坐<b>船</b>去学校。", "I go to school by boat."),
                    ("<b>电影院</b>离我家很远，要坐<b>船</b>去。",
                     "The cinema is far from my home; you have to go by boat.", True)],
                   "你家附近有没有电影院？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 离我家很远，要坐 ________ 去。"],
                "两句，一近一远，中间用「可是」，还要说时间："
                "<b>超市离我家很近，走路三分钟就到了，可是电影院挺远的，要坐船去。</b>"))

    # ── Cycle 2 · 然后（single word） ──
    add("08-c2-words.html", "Cycle 2 · A — 然后", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("然后（然後）", "ránhòu", "then; after that", "ranhou")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("我先走路，<b>然后</b>坐五路公共汽车。",
                     "First I walk, then I take the number 5 bus."),
                    ("我先坐船，<b>然后</b>坐火车去电影院。",
                     "First the boat, then the train to the cinema."),
                    ("我先坐公共汽车，<b>然后</b>走路十分钟就到了。",
                     "First the bus, then ten minutes on foot and I'm there.", True)],
                   "「先」在前，「然后」在后——两个都在动词前面。"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我先 ________ ，然后 ________ 。"],
                "三段路，不是两段——中间加一个「再」："
                "<b>我先走路，然后坐船，再坐五路公共汽车。</b> "
                "写完了，再把这条路<b>倒过来</b>说一遍：从电影院回家。"))

    add("11-recall.html", "Recall · three words, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["电影院", "船", "然后"],
                 "读不出来就停下来重教——不要往下走。", cols=3))

    # ── The pattern ──
    add("12-pattern.html", "Pattern · 从 A 怎么去 B？", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 问路线，答两段",
                  "从 A 怎么去 B？　→　我先……，然后……。",
                  [("从我家怎么去学校？　—— 我<b>先</b>走路，<b>然后</b>坐校车。",
                    "Two legs — the standard answer."),
                   ("从你们家怎么去电影院？　—— 我<b>先</b>坐船，<b>然后</b>再坐五路公共汽车。",
                    "This is Text 2, p.148. Note the extra 再 before the second verb."),
                   ("从学校怎么去超市？　—— 走路五分钟就到了。",
                    "The answer doesn't have to have two legs. Did you notice?")],
                  "第三句是故意的：问句问的是「怎么去」，不是「有几段」。"
                  "一段路就说一段。"))
    add("13-errors.html", "The error to pre-empt · 先 and 然后", IDO, "句型 · 最常见的错",
        s_errors([("我坐船先，坐公共汽车然后。", "我<b>先</b>坐船，<b>然后</b>坐公共汽车。",
                   "「先」「然后」都在动词前面——跟昨天的「就」一样"),
                  ("我先坐船，然后我坐公共汽车。", "我先坐船，然后坐公共汽车。",
                   "主语说过一次就够了，第二个「我」多余")],
                 "改一改 · 「先……，然后……」最常见的两个错"))
    add("14-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("两段路，加车号，加昨天的「就」",
                "从学校怎么去火车站？　—— 我先坐十路公共汽车，然后走路十分钟就到了。",
                "How do you get from school to the train station? — First the number 10 "
                "bus, then ten minutes on foot and you're there.",
                "昨天的「就」在这儿回来了。新句型装旧词，才叫会用。"))

    add("15-text.html", "Text 2 · p.148 (first four lines)", IDO, "课文二 · CD 74",
        s_dialogue("课文二 · 前四行 · 课本 p.148",
                   [("A", "你们家附近有电影院吗？"),
                    ("B", "没有。"),
                    ("A", "从你们家怎么去电影院？"),
                    ("B", "我先坐船，然后再坐五路公共汽车。")],
                   "放 CD 74，齐读，然后两人一组读两遍，换角色。"
                   "后面「要坐多长时间？」那几行今天先盖住——下节课的。"))

    add("16-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「先」和「然后」哪个在前面？跟我一起说。", "先……，然后……"),
               ("翻译：<i>First I walk, then I take the bus.</i>",
                "小白板：我先走路，然后坐公共汽车。"),
               ("<b>怎么去电影院？</b>先跟同桌说，三十秒。", "然后老师点两个人说"),
               ("改一改：我坐船先，然后坐火车。", "哪个词放错了？")]))

    # ── Practice · three games ──
    add("17-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("电影院", "dianyingyuan"), ("船", "chuan"), ("然后", "ranhou")],
                  "这一页整节课都留在屏幕上——三个游戏都看它。"))

    add("18-game1a.html", "Game 1 · Round 0 — p.150 Act. 11 (2 min)", PRAC,
        "游戏一 · 第零轮 · 2 分钟",
        s_figure("ranhou", "第零轮 · 课本 p.150 第十一题 · 坐着做",
                 ["屏幕上六张图，是一家人各自怎么出门。",
                  "老师指一张，<b>全班齐声</b>用「先……，然后……」说出来。",
                  "六张说完，课本这一题就做完了——它同时也是等一下接力赛的样板。"],
                 cn="爸爸先走路，然后坐火车。"))
    add("19-game1b.html", "Game 1 · Journey Relay (7 min)", PRAC, "游戏一 · 接力赛 · 7 分钟",
        s_task("游戏一 · 路线接力赛",
               ["分两队，黑板分两栏。每队一叠<b>交通卡</b>、一叠<b>地点卡</b>，都扣着。",
                "一个人上来抽<b>两张交通卡</b>、<b>一张地点卡</b>，跑到黑板写完整一句，"
                "跑回来拍下一个人。",
                "写错了？下一个人要先改对，才能写自己那一句。",
                "每队六个人，先写完而且全对的那一栏赢。"],
               cn="我先坐船，然后坐公共汽车去电影院。",
               ext="强的同学<b>排最后</b>，抽<b>三张</b>交通卡——句子要用"
                   "「先……，然后……，再……」，还要说出<b>为什么这么排</b>："
                   "因为坐船太慢了。写完还要当对方那一栏的<b>裁判</b>，"
                   "判错要<b>用中文</b>说出错在哪儿。"))

    add("20-game2.html", "Game 2 · Telephone 传声筒 (7 min)", PRAC, "游戏二 · 传声筒 · 7 分钟",
        s_task("游戏二 · 传声筒",
               ["六个人一排。老师悄悄告诉每排第一个人一句<b>两段路</b>的话。",
                "一个一个往下传，只能小声说，不能写。",
                "最后一个人写在小白板上举起来。跟原句最像的那一排赢。",
                "三轮，三句不同的话，每句都有「然后」加一个今天的词。"],
               cn="我先坐船，然后坐十路公共汽车去电影院。",
               ext="第四轮：赢的那一排最后一个人<b>自己编</b>一句来传——"
                   "里面必须有「先……，然后……」、一个车号、一个地点，"
                   "而且别人质疑的时候他要能<b>写对</b>。"))

    add("21-game3.html", "Game 3 · 从……怎么去……? chain (7 min)", PRAC,
        "游戏三 · 接龙 · 7 分钟",
        s_list("游戏三 · 全班站成一圈",
               [("第一个人问第二个人：<b>从学校怎么去电影院？</b>", "地点自己挑"),
                ("第二个人用「先……，然后……」回答，然后转向第三个人，换一个<b>新的</b>地点问。",
                 "地点不能重复"),
                ("地点重复、停超过五秒、漏掉「然后」——坐下。", "最后站着的三个人赢")],
               "屏幕上的总览页不要关——卡住的时候看一眼就想起来了。", compact=True))
    add("22-game3-ext.html", "Game 3 · Extension", PRAC, "游戏三 · Extension",
        s_task("游戏三 · 加难 · 你站到圈外面去",
               ["剩下的强的同学退出圈子，改当<b>提问的人</b>，从外面问。",
                "问法<b>不能重复</b>——同一个句型只能用一次。",
                "觉得别人答得太短，要当场追加一个中文问题。",
                "（「那要坐多长时间？」还不能用——那是下节课的。"
                "「你为什么不走路？」可以。）"]))

    add("23-strokes.html", "Writing · copy the new characters", PRAC, "写字 · 生词",
        s_strokes([("院", 9, "左边是「阝」——跟第一课的「附」一样"),
                   ("船", 11, "舟字旁，右边先写「几」，再写「口」"),
                   ("然", 12, "上面「月」「犬」，下面四点底"),
                   ("后", 6, "先写撇，再写横")],
                  "写字 · 课本笔顺 · 练习册 pp.167–168",
                  "每个字写三遍。「然」的四点底是四笔，不是一笔。"))

    # ── Plenary ──
    add("24-plenary.html", "Plenary · 回头看目标", PLEN, "小结 · 43–50 分钟",
        s_list("小结 · 回头看今天的三个目标",
               [("能说「电影院」和「船」", "👍 / 😐 / 👎"),
                ("会用「先……，然后……」", "👍 / 😐 / 👎 —— 请一个今天还没说过话的同学举例"),
                ("会问「从……怎么去……？」", "👍 / 😐 / 👎")],
               "游戏玩得热闹，不代表学会了。这三条一条一条问。"))
    add("25-exit.html", "Exit ticket", PLEN, "出门条 · Exit ticket",
        s_focus("出门条 · 回答一句，交上来",
                "从你家怎么去电影院？",
                "Answer in one sentence, with 先……，然后……。",
                "下节课：今天 B 没被问到的那一句——<b>要坐多长时间？</b>",
                ext="写完了？火车站那一条路也写一句。"))
    return S
