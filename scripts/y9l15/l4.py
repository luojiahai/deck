# -*- coding: utf-8 -*-
"""Y9 L15 · Lesson 4 of 6 — 注意 / 办法 + 能不能……？ and Adj/V得 + 一点儿

Source: docs/lesson-plans/y9-l15/04-polite-requests-mixed.md
Textbook p.147 Text 2 (complete), p.149 Act. 10 (……一点儿), p.150 Act. 11
(role play), p.151 Act. 13 (CD 60), and the rest of p.146 Act. 6's dotted
structures. Workbook p.172 Ex. 20.

Only two new words, so one cycle — the time that would have gone to a
second and third pair goes to the two patterns and to Text 2 in full.
Both words are abstract, so both cards are textonly.

Text 2's four exchanges fit one s_dialogue at the tight tier (eight turns),
so it is not split the way y9-l14's Text 2 had to be.
"""
from build import (s_words, s_examples, s_write, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_errors, s_dialogue,
                   s_listening, s_title, s_lisc, label)

SLUG = "l4-polite-requests"
TITLE = "Y9 L15 · 邻居 Neighbours · Lesson 4 of 6"
CARD = (SLUG, "能不能小点儿声？", "Complaining Politely · 能不能……一点儿？",
        "speaking", "注意 · 办法，加「能不能……？」和「……一点儿」。"
                    "课文二全文、CD 60，最后四个情境角色扮演。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 能不能小点儿声？", "LESSON 4 OF 6", "第十五课 · 邻居",
        s_title("能不能小点儿声？", "Complaining Politely",
                "Year 9 · Book 3 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 3 · p.147–151 · 课文二、第 10、11、13 题"))

    add("02-review.html", "Review · L3 的「把」", REV, "复习 · Lesson 3",
        s_list("复习 · 三轮 · 白板",
               [("第一轮 · 老师说英文，你写「把」字句", "四句，*my brother took my phone* 那一类"),
                ("第二轮 · 同样四句，改写成「被」字句", "跟同伴换白板，互相改"),
                ("第三轮 · 全班念词序：谁 — 把 — 什么 — 动词 — 了", "念两遍"),
                ("点名 · 昨天晚上什么把你吵醒了？", "一位同学，口头回答")],
               "上一课邻居把你吵醒了，你很生气。可是生气没有用——"
               "今天你去敲门，跟他们说话。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("ask a neighbour politely to change something, and answer a "
               "complaint — either by agreeing to be careful, or by saying "
               "there is nothing we can do.",
               [("I can make a polite request with 能不能……？",
                 "能有礼貌地请求：能不能小点儿声？"),
                ("I can ask for more or less with 一点儿",
                 "能说：请说慢一点儿／把声音开得小一点儿"),
                ("I can promise to be careful", "能回答：好，我以后注意"),
                ("I can say there's nothing I can do",
                 "能回答：对不起，我没有办法")]))

    # ── Cycle 1 · 注意 / 办法 ──
    add("04-c1-words.html", "Cycle 1 · A — 注意 / 办法", IDO, "生词 · 今天只有一组",
        s_words(("注意", "zhùyì", "pay attention; be careful", None),
                ("办法", "bànfǎ", "way; method", None)))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 · See them used",
        s_examples([(None, "好，我以后<b>注意</b>。",
                     "All right, I'll be careful from now on."),
                    (None, "对不起，我没有<b>办法</b>。",
                     "Sorry, there's nothing I can do."),
                    (None, "我会<b>注意</b>的，可是小孩子哭，我真的没有<b>办法</b>。",
                     "I'll watch it — but a crying child, I can't help.", True)],
                   "哪一件事是真的没有办法的？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 · Write your own",
        s_write(["好，我以后注意 ________ 。", "________ ，我没有办法。"],
                "写<b>三句对话</b>：一句投诉，一句用「注意」回答，"
                "再一句投诉是对方真的<b>做不到</b>的，"
                "用「没有办法」回答，还要用「因为……，所以……」说清楚为什么。"))

    add("07-hanzi.html", "词 · 注意 / 办法 怎么用", IDO, "用词 · How they're used",
        s_list("用词 · 这两个词，位置很固定",
               [("我以后注意。", "被投诉以后说的——不是「我注意到了」"),
                ("有办法 · 没有办法 · 想办法", "「办法」几乎只跟这三个搭配"),
                ("法 · 方法 · 语法", "「法」就是「方法」，以后还会再见"),
                ("对不起，我没有办法。", "这是礼貌的<b>拒绝</b>，不是不理你")],
               "第六课还会用到「<b>想想办法</b>」——遇到问题，你打算怎么办。"))

    # ── Patterns ──
    add("08-pattern.html", "Pattern · 能不能……？", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 有礼貌地请别人改一改",
                  "能不能 + 动词 + 一点儿／小点儿声？",
                  [("请说慢<b>一点儿</b>。", "Please speak more slowly."),
                   ("<b>能不能</b>小点儿声？", "Could you keep it down?"),
                   ("<b>能不能</b>把电视机开得小<b>一点儿</b>？",
                    "Could you turn the television down?")],
                  "「能不能」本身已经是问句了——后面<b>不要</b>再加「吗」。"))
    add("09-pattern2.html", "Pattern · 动词 + 得 + 形容词 + 一点儿", IDO, "句型 · 从「很」到「一点儿」",
        s_pattern("句型 · 不是说它多响，是要它<b>改</b>",
                  "动词 + 得 + 形容词 + 一点儿",
                  [("电视机开得很<b>响</b>。", "It's on loud. (saying how it is)"),
                   ("请把电视机开得小<b>一点儿</b>。",
                    "Turn it down a bit. (asking it to change)"),
                   ("你跑得快<b>一点儿</b>！", "Run a bit faster!")],
                  "「一点儿」放在形容词<b>后面</b>：快一点儿，不是「一点儿快」。"))
    add("10-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 先体谅，再请求，再给理由",
                "我知道你们在看球赛，可是已经半夜了，能不能小点儿声？我明天要考试。",
                "I know you're watching the match, but it's midnight — "
                "could you keep it down? I've got an exam tomorrow.",
                "有礼貌的投诉有三层：先说我懂你，再提要求，最后给理由。"
                "只说「小点儿声」不算不礼貌，可是这样说更管用。"))
    add("11-errors.html", "能不能……？ 常见的错", IDO, "注意 · The one to get right",
        s_errors([("能不能小点儿声吗？", "能不能小点儿声？", "已经是问句，不要「吗」"),
                  ("请你一点儿快说。", "请你说快一点儿。", "「一点儿」在形容词后面"),
                  ("你小声！", "能不能小点儿声？", "这不是错句，是不礼貌——今天要练礼貌的说法")],
                 "能不能 ≠ 能不能……吗",
                 "第三个不是语法错。同一个意思，说法不一样，结果完全不一样。"))

    add("12-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("「能不能……？」后边要不要加「吗」？", "要的比大拇指朝上，不要的朝下"),
               ("白板：写「能不能把声音开得小一点儿？」", "老师看：有没有多写「吗」"),
               ("这句哪里错了？ 请你一点儿快说。", "写出改好的句子"),
               ("邻居说「对不起」，你怎么回答？", "全班一起说")]))

    add("13-text2.html", "Text 2 · 全文", IDO, "课文二 · p.147 · CD 59",
        s_dialogue("课文二 · 全文 · 分角色，再换一次，最后全班读楼下、老师读楼上",
                   [("A", "我就住在楼下。每天早上有人在房间里跑步，对吗？"),
                    ("B", "对。"),
                    ("A", "你把我吵醒了。"),
                    ("B", "对不起。我以后晚一点儿跑。"),
                    ("A", "每天晚上，你们的电视机开得很响。请问能不能小点儿声？"),
                    ("B", "好，我以后注意。"),
                    ("A", "每天半夜，我还听见小孩子哭。"),
                    ("B", "对不起，小孩子哭，我没有办法。")],
                   "楼下的人一共提了几件事？ · 哪一件楼上没有办法解决？为什么？ · "
                   "哪一句是有礼貌的请求？请读出来。"))

    # ── Flexible practice ──
    add("14-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("注意", None), ("办法", None),
                   ("能不能……？", None), ("……一点儿", None)],
                  "今天只有两个生词，所以板上多放两个句型——活动一整段都留着。"))
    add("15-listening.html", "Activity 1 · CD 60 · 听", PRAC,
        "活动一 · We Do · 7 分钟",
        s_listening("活动一 · 听 CD 60 · 每题放两遍 · 课本 p.151 第 13 题",
                    [("1 · 王先生的女儿晚上做什么？", "第一遍：写问题是什么（两三个字）"),
                     ("2 · 周太太家的什么太响了？", "跳舞／电视／鸟／音乐／踢球／看电视"),
                     ("3 · 王小姐家的鸟怎么了？", "第二遍：挑三题写完整"),
                     ("4 · 小英的音乐怎么样？", "写<b>请求</b>：能不能……？"),
                     ("5 · 小天在房间里做什么？", "再写<b>回答</b>：用「注意」或者「办法」"),
                     ("6 · 小明看了多久电视？", "老师走动，看第二遍")],
                    "两人对一对那三题，再请两位同学把一整组读出来。"))
    add("16-listening-ext.html", "Activity 1 · Extension", PRAC,
        "活动一 · 给写得快的同学",
        s_task("活动一 · Extension · 六题全写，而且<b>六个回答都不一样</b>",
               ["一个用「注意」答应，一个用「没有办法」加理由拒绝，",
                "一个给别的办法（<b>我以后在外面……</b>），",
                "一个给时间（<b>我以后十点以后不……</b>）。",
                "再自己编第七组，就在你住的那栋楼里，两个角色都要能读出来。"],
               cn="对不起，我以后把鸟放在别的房间里。"))
    add("17-activity2.html", "Activity 2 · ……一点儿", PRAC,
        "活动二 · You Do · 7 分钟",
        s_list("活动二 · 课本 p.149 第 10 题 · 十句填完 · 本子上写，五分钟",
               [("十句都用「快一点儿／大一点儿／高一点儿……」结尾", "自己写，不讨论"),
                ("写完的看黑板，再写三句 · 课本 p.146 第 6 题",
                 "<b>多……点儿</b> · <b>如果……应该……</b> · <b>……的时候</b>"),
                ("老师收三句读出来", "三个结构各一句")],
               "答案不上屏——老师现场对。"))
    add("18-activity2-ext.html", "Activity 2 · Extension", PRAC,
        "活动二 · 给写得快的同学",
        s_task("活动二 · Extension · 十句做完以后",
               ["挑<b>四句</b>，改写成对<b>真人</b>的有礼貌的请求——"
                "邻居、老师、弟弟，用「能不能」。",
                "再用 p.146 剩下的三个结构各写一句，都要说住在楼房里的事：",
                "<b>在……过</b> · <b>从小就</b> · <b>不用</b>"],
               cn="能不能说慢一点儿？我听不懂。"))
    add("19-game.html", "Game · 角色卡 Role Play", PRAC, "游戏 · 9 分钟",
        s_task("游戏 · 角色卡 · 课本 p.150 第 11 题 · 两人一张卡，准备两分钟",
               ["四个情境：<b>音乐开得很响 · 半夜有人在房间里唱歌 · "
                "小孩儿在房间里踢球 · 两个男孩儿在楼上打乒乓球</b>",
                "每一场都要有三样东西：<b>投诉 · 能不能……？ · "
                "用「注意」或者「办法」回答</b>。",
                "演给另外一组看，然后换卡、换角色，再演一次。"
                "最后两组演给全班，全班投票选最有礼貌的回答。"],
               "给流利的同学：换成课本 p.151 第 14 题的<b>借东西</b>情境，"
               "不给参考句，不准备。投诉的人<b>整场不准说「对不起」</b>，"
               "邻居要先有礼貌地拒绝一次，第二次才答应。"))

    add("20-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 老师读一条，全班给一句对得上的中文。",
                "<b>自评</b> · 白板：会了 · 差不多 · 还要练。",
                "<b>出门条</b> · 白板写一句，走的时候给我看。",
                "<b>下节课</b> · 他们正在干什么呢？还有——借了东西不还的邻居。"],
               cn="出门条：你的邻居半夜开派对。用「能不能」写一句有礼貌的话。"))

    return S
