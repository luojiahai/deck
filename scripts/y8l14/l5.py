# -*- coding: utf-8 -*-
"""Y8 L14 · Lesson 5 of 6 — storage, and questions without 吗

Source: docs/lesson-plans/y8-l14/05-storage-v-not-v-mixed.md
Textbook p.138 (Text 2 complete; New Words 4–5), p.139 NOTE and Act. 14,
p.141 Act. 16 (CD 70). Workbook pp.161–162.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_convert,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_strokes,
                   s_listening, s_dialogue, s_title, s_lisc)

SLUG = "l5-storage-v-not-v"
TITLE = "Y8 L14 · 家具 Furniture · Lesson 5 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='你有没有？', en='Storage & V-not-V questions',
            desc='Two words finish the bedroom, and then the biggest idea in the lesson, which costs nothing: 有没有 is just 有 and 没有 pushed together. Every verb the class already knows becomes a new question form.',
            words='衣柜 · 书架', n=2)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 你有没有自己的房间？", "LESSON 5 OF 6", "第十四课 · 家具",
        s_title("你有没有自己的房间？", "Storage, and Questions Without 吗",
                "Year 8 · Book 2 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 2 · p.138 · p.139 · p.141"))

    add("02-review.html", "Review · Text 2 from memory", REV, "复习 · 第四节课",
        s_dialogue("两人一组 · 屏幕看三十秒，然后关掉，自己说出来",
                   [("A", "你的房间里有什么？"),
                    ("B", "有一张床、一张书桌和一把椅子。"),
                    ("A", "你的房间里有电脑吗？"),
                    ("B", "有，在我的书桌上。")],
                   "两个角色都要说一遍。请两组上来演。"
                   "<b>A 的第一句今天会变一个样子——先记住它现在长什么样。</b>"))
    add("03-review-board.html", "Review · four on the whiteboard", REV, "复习 · 小白板",
        s_list("小白板 · 四题",
               [("<i>one chair</i>", "一把椅子"),
                ("<i>two desks</i>", "两张书桌"),
                ("<i>The computer is on the desk.</i>", "电脑在书桌上。"),
                ("<i>The chair is in front of the desk.</i>", "椅子在书桌前面。")],
               "那个房间还少两样东西——今天补上。课文第一句里还藏着一个问句，"
               "上节课跳过去了，今天也补上。", compact=True))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("ask questions using the verb-not-verb form, and finish describing "
               "a bedroom.",
               [("I can name a wardrobe and a bookshelf", "能说出衣柜和书架"),
                ("I can turn a 吗 question into a verb-not-verb question",
                 "能把「你有弟弟吗？」说成「你有没有弟弟？」"),
                ("I can interview a classmate with three V-not-V questions",
                 "能用三个「V不V」问句采访同学")]))

    # ── Cycle 1 · 衣柜 / 书架 ──
    add("05-c1-words.html", "Cycle 1 · A — 衣柜 / 书架", IDO, "生词 1 · Cycle 1 of 1",
        s_words(("衣柜（衣櫃）", "yīguì", "wardrobe", "yigui"),
                ("书架（書架）", "shūjià", "bookshelf", "shujia")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("我的房间里有一个<b>衣柜</b>。", "There's a wardrobe in my room."),
                    ("<b>书架</b>上有很多书。", "There are lots of books on the bookshelf."),
                    ("<b>衣柜</b>在<b>书架</b>左面。",
                     "The wardrobe is to the left of the bookshelf.", True)],
                   "你的房间里有没有书架？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我的房间里有一个 ________ 和一个 ________ 。"],
                "说说里面装了什么、满不满，两个小句连起来："
                "<b>我的衣柜里面有很多衣服，可是书架上没有很多书，"
                "因为我的书都在书桌上。</b>"))

    add("08-recall.html", "Recall · the complete fifteen", IDO, "认一认 · 十五个词",
        s_recall(["沙发", "茶几", "电视柜", "张", "空调", "洗衣机", "里面", "冰箱",
                  "烤箱", "电炉", "椅子", "把", "书桌", "衣柜", "书架"],
                 "第十四课的生词到这儿就齐了——十五个。一起读一遍。", cols=5))

    # ── V-not-V ──
    add("09-convert.html", "吗-question → V-not-V", IDO, "句型 · 不用「吗」的问句",
        s_convert([("你有自己的房间<b>吗</b>？", "你<b>有没有</b>自己的房间？"),
                   ("你喜欢你的房间<b>吗</b>？", "你<b>喜不喜欢</b>你的房间？"),
                   ("你想买一个书架<b>吗</b>？", "你<b>想不想</b>买一个书架？"),
                   ("这是你的衣柜<b>吗</b>？", "这<b>是不是</b>你的衣柜？"),
                   ("你要买椅子<b>吗</b>？", "你<b>要不要</b>买椅子？"),
                   ("你买书架<b>吗</b>？", "你<b>买不买</b>书架？")],
                  "课本 p.139 的 NOTE · 左边右边意思完全一样",
                  "<b>左边没有错。</b>两种都是对的中文，说哪个都行——"
                  "今天练的是右边这一种。"))
    add("10-pattern.html", "Pattern · V 不 V", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 动词说一遍，加「不」，再说一遍",
                  "动词 + 不 + 动词　（「有」用「没」：有没有）",
                  [("你<b>有没有</b>自己的房间？", "有 is the exception — it takes 没, never 不."),
                   ("你<b>喜不喜欢</b>你的房间？", "Two-syllable verbs split: 喜欢 → 喜不喜欢."),
                   ("你的房间里<b>有没有</b>书架？", "The question word sits where 吗 would have been.")],
                  "要小心的就一条：<b>「有」配「没」，别的动词配「不」。</b>"
                  "「你有不有书架？」是最常见的错。"))
    add("11-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("两个问句连着问，还要说理由",
                "你有没有自己的房间？你喜不喜欢？为什么？",
                "Do you have your own room? Do you like it? Why?",
                "第二个问句把宾语省掉了，因为上一句刚说过——这是真的会话里的说法。"
                "回答不能只说「有」，要说一整句。"))

    add("12-text.html", "Text 2 · p.138 complete", IDO, "课文二 · CD 69",
        s_dialogue("课文二 · 课本 p.138 · 完整版",
                   [("A", "<b>你有没有</b>自己的房间？"),
                    ("B", "有。"),
                    ("A", "你的房间里有什么？"),
                    ("B", "有一张床、一张书桌、一把椅子、一个<b>衣柜</b>和一个<b>书架</b>。"),
                    ("A", "你的房间里有电脑<b>吗</b>？"),
                    ("B", "有，在我的书桌上。")],
                   "A 第一句用「有没有」，第三句用「吗」——<b>两个都对</b>，"
                   "同一个人在同一段对话里换着用，很正常。"))

    add("13-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("改成 V 不 V：　你有空调吗？", "全班一起说"),
               ("不用「吗」，问：<i>Do you like your room?</i>", "写在小白板上"),
               ("这句话对不对？　你有不有书架？", "错在哪儿？"),
               ("你的房间里有没有衣柜？", "点名——要一整句，不能只说「有」")]))

    # ── Practice ──
    add("14-summary.html", "Summary board · 词汇总览 · 十五个", PRAC,
        "词汇总览 · stays on screen",
        s_summary([("沙发", "shafa"), ("茶几", "chaji"), ("电视柜", "dianshigui"),
                   ("张", None), ("空调", "kongtiao"), ("洗衣机", "xiyiji"),
                   ("里面", "limian"), ("冰箱", "bingxiang"), ("烤箱", "kaoxiang"),
                   ("电炉", "dianlu"), ("椅子", "yizi"), ("把", None),
                   ("书桌", "shuzhuo"), ("衣柜", "yigui"), ("书架", "shujia")],
                  "第十四课的全部生词。这一页今天和下一节课都留在屏幕上。", dense=True))

    add("15-act1.html", "Activity 1 · Your complete room (7 min)", PRAC,
        "活动一 · 7 分钟",
        s_task("活动一 · 把你的房间写完整",
               ["先照着课文里 B 那句长回答，写<b>你自己</b>房间的——一句话列完，量词要对。",
                "再写两句，用「在」说其中两样东西在哪儿。",
                "然后加第二小段说家里别的地方，"
                "让总览页上的<b>十五个词全部出现</b>。",
                "你们家没有的，用「没有」写进去，不要跳过。"],
               cn="我的房间里有一张床、一张书桌、一把椅子、一个衣柜和一个书架。"))
    add("16-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难",
               ["写成回答一个<b>没有人问过你</b>的问题：有人问你愿不愿意跟弟弟／妹妹换房间。",
                "十五个词全部用上，比较两个房间，",
                "用「可是」和「因为……所以……」连起来，最后要有一个决定。",
                "不看总览页。"],
               cn="我的房间不大，可是我有自己的书架……"))

    add("17-act2.html", "Activity 2 · CD 70 — two brothers sharing a room (6 min)", PRAC,
        "活动二 · 听力 · 6 分钟",
        s_listening("活动二 · 课本 p.141 第 16 题 · 听两遍，选 a 或 b",
                    [("他有没有自己的房间？", "a 有　　b 没有"),
                     ("他跟谁住一个房间？", "a 哥哥　　b 弟弟"),
                     ("他们的床是什么样的？", "a 上下床　　b 两张床"),
                     ("谁睡上床？", "a 他　　b 弟弟"),
                     ("房间里有几把椅子？", "a 一把　　b 两把"),
                     ("弟弟有没有电脑？", "a 有　　b 没有")],
                    "放之前先在黑板上写<b>上下床</b>（bunk bed）——只要听得懂，不用会写。"
                    "对完答案再放一遍，把听到的每一个「V 不 V」问句写下来。"))
    add("18-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难",
               ["把这段对话改成<b>弟弟</b>说的——同一个房间，同样的家具，换一个人说。",
                "哥哥问过的每一个问题，都要用「V 不 V」再问一次，",
                "而且<b>要换一个动词</b>，不能重复原来那个。"],
               cn="你喜不喜欢睡下床？"))

    add("19-act3.html", "Activity 3 · p.139 Ex.14 — write five, interview three (6 min)",
        PRAC, "活动三 · 采访 · You Do · 6 分钟",
        s_list("活动三 · 课本 p.139 第 14 题",
               [("<b>2 分钟</b>　自己写五个问句，五个动词各一个", "有没有 · 要不要 · 是不是 · 想不想 · 喜不喜欢"),
                ("五个问题都要问房子或者家具", "你有没有自己的书架？"),
                ("<b>2 分钟</b>　离开座位，采访三个同学，简单记下答案", ""),
                ("<b>回座位</b>　请两个同学用「他」报告一件事", "他有自己的房间，可是他不喜欢，因为房间不大。")],
               "写完就出发，不要等全班都写完。", compact=True))
    add("20-act3-ext.html", "Activity 3 · Extension", PRAC, "活动三 · Extension",
        s_task("活动三 · 加难",
               ["五个问题全部问<b>同一个</b>同学，而且要一个接一个——"
                "第四个问题得看第三个的答案才想得出来。",
                "报告的时候不是说一件事，是说<b>一段话，四句</b>，不看笔记。"],
               cn="他有自己的房间，房间不算大，里面有一个书架，可是书架上没有很多书……"))

    add("21-strokes.html", "Characters · 柜 架 (Workbook pp.161–162)", PRAC,
        "写汉字 · 练习册 p.161",
        s_strokes([("柜", 8, "左边木，右边「巨」——第一节课写过"),
                   ("架", 9, "上面「加」，下面「木」")],
                  "笔顺 · 每个字写三遍",
                  "「衣柜」的「衣」和「书架」的「书」都学过了——今天每个词只有一个新字。"))

    add("22-game.html", "Game · Find Someone Who (4 min)", PRAC, "游戏 · 找一个人 · 4 分钟",
        s_list("游戏 · Find Someone Who · 十个格子，全部是「V 不 V」问句",
               [("有没有自己的房间　·　有没有书架", "答「有」才能签名"),
                ("喜不喜欢自己的房间　·　房间里有没有电脑", "一个人只能签一次"),
                ("家里有没有烤箱　·　想不想买新书桌", "签满十格的先举手"),
                ("家里有没有空调　·　有没有两个浴室", "家里有没有车库　·　房间大不大"),
                ("<b>加难</b>：签名还要说<b>理由</b>，问的人要把理由用中文写进格子里",
                 "五格带理由，胜过十格没理由")],
               "格子纸每人一张，提前印好。", compact=True))

    add("23-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 全班齐读三条。",
                "<b>自评</b> · 举大拇指。第二条要特别看——"
                "如果还不稳，下节课开头先练两分钟改句子。",
                "<b>出门条</b> · 一问一答，写在同一张纸条上。",
                "<b>下节课</b> · 这一课最后一节：去买家具，"
                "问衣柜在几楼，然后把一整个房子说给全班听。"],
               cn="出门条：写一个关于卧室的「V 不 V」问句，再用一整句话回答它。"))
    return S
