# -*- coding: utf-8 -*-
"""Y9 L13 · Lesson 3 of 6 — 教堂 / 公园 / 前面 / 后面 + the whole of Text 1

Source: docs/lesson-plans/y9-l13/03-front-back-text1-mixed.md
Textbook p.122 Text 1 in full, p.124 Act. 3, p.126 Act. 5 (CD 50) and
Act. 6. Workbook p.147 Ex. 7 is the written task; p.148 Ex. 9 items 3, 7
and 8 feed the exit ticket.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu, s_errors,
                   s_text, s_title, s_lisc, label)

SLUG = "l3-front-back"
TITLE = "Y9 L13 · 社区 Neighbourhood · Lesson 3 of 6"
CARD = (SLUG, "前面、后面", "Front, Back & the Whole Street",
        "grammar", "教堂 · 公园 · 前面 · 后面。第一次把整段课文连起来说——一句挂着一句。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

TEXT1 = ("我家住在市中心，生活很方便。邮局离我家不远。超级市场就在邮局对面。"
         "邮局的左边是诊所，右边是银行。市政大楼在百货公司的前面。"
         "我家附近还有一个大教堂。教堂的后面是一个小学，旁边是一个公园。")


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 前面、后面", "LESSON 3 OF 6", "第十三课 · 社区",
        s_title("前面、后面", "Front, Back & the Whole Street",
                "Year 9 · Book 3 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 3 · pp.122, 124, 126 · 课文一"))

    add("02-review.html", "Review · 改错 Correct the Teacher", REV, "复习 · Lessons 1–2",
        s_errors([("银行在对面邮局。", "银行在邮局对面。", "地标先说，「对面」后说"),
                  ("我家离市中心很方便。", "我家离市中心很远。", "方便说生活，不说距离"),
                  ("市政大楼就在旁边公园。", "市政大楼就在公园旁边。", "同样：地标在前")],
                 "改错 · 白板，九十秒 · 黑板上还有一句是<b>对</b>的",
                 "第四句（对的，不要改）：<b>诊所的左边是百货公司。</b> "
                 "改法从台下来，不从台上来。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("use 前面 and 后面, and describe a whole neighbourhood in a "
               "connected paragraph.",
               [("I can name 教堂 and 公园 in Chinese", "能说出教堂和公园"),
                ("I can use A 在 B 的前面／后面", "能用「在……的前面／后面」摆位置"),
                ("I can describe a neighbourhood in four or more connected sentences",
                 "能说一段话（四句以上）介绍我的社区")]))

    # ── Cycle 1 · 前面 / 后面 ──
    add("04-c1-words.html", "Cycle 1 · A — 前面 / 后面", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("前面", "qián mian", "front", "qianmian"),
                ("后面", "hòu mian", "back", "houmian")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "银行在邮局的<b>前面</b>。", "The bank is in front of the post office."),
                    (None, "我家的<b>后面</b>有一个超市。",
                     "There's a supermarket behind my house."),
                    (None, "诊所在银行的<b>前面</b>，百货公司在银行的<b>后面</b>。",
                     "The clinic is in front of the bank, the department store behind it.",
                     True)],
                   "你家的后面有什么？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 在 ________ 的前面。", "我家的后面有 ________ 。"],
                "一句话摆<b>三</b>座建筑，用<b>三个不同</b>的位置词，"
                "其中至少一个是前面或后面。"))

    # ── Cycle 2 · 教堂 / 公园 ──
    add("07-c2-words.html", "Cycle 2 · A — 教堂 / 公园", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("教堂", "jiàotáng", "church", "jiaotang"),
                ("公园", "gōngyuán", "park", "gongyuan")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "<b>教堂</b>离我家很近，走路十分钟就到了。",
                     "The church is close to my home — ten minutes' walk."),
                    (None, "<b>公园</b>在市政大楼的后面。",
                     "The park is behind the city hall."),
                    (None, "<b>教堂</b>的旁边是一个<b>公园</b>。",
                     "Beside the church is a park.", True)],
                   "公园在哪儿？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["教堂在 ________ 。", "________ 的旁边是一个公园。"],
                "用「因为……，所以……」：<b>因为我家附近有一个大公园，"
                "所以我每天都去跑步。</b> 再说公园在哪儿——要用两个别的建筑定位。"))

    add("10-recall.html", "Recall · 四个生词", IDO, "认一认 · Checkpoint",
        s_recall(["前面", "后面", "教堂", "公园"],
                 "「面」自己是「side」——前面、后面、对面，都是同一个「面」。", cols=4))

    # ── Text 1 in full ──
    add("11-pattern.html", "Pattern · 一句挂着一句", IDO, "句型 · 连成一段",
        s_pattern("句型 · 一段话是怎么连起来的",
                  "先说「我家」→ 每一句挂在上一句提过的地方上",
                  [("我家住在市中心，生活很方便。", "Opens with the speaker."),
                   ("邮局离我家不远。", "Hangs off 我家."),
                   ("超级市场就在邮局对面。", "Hangs off 邮局.")],
                  "这不是一张清单——是一条<b>链子</b>。每一句都抓住前一句里的地方。"))
    add("12-text1.html", "Text 1 · 课文一（全文）", IDO, "课文一 · p.122",
        s_text("课文一 · 全文 · 一起读两遍", TEXT1,
               "超级市场在哪儿？ · 邮局的右边是什么？ · 教堂的后面有什么？",
               "注意「还有」——它把一个新地标带进来，然后「教堂」就变成下两句的地标。"))

    add("13-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("我说两座建筑和一个位置词——是「前面」就往前指，是「后面」就往后指。",
                "六次，全班一起"),
               ("白板：写「公园在教堂的后面」。", "Write it in characters"),
               ("这句哪里错了？ 公园在后面教堂。", "改过来"),
               ("教堂的后面是什么？", "用中文回答，答案在课文里")]))

    # ── Flexible practice ──
    add("14-summary.html", "Summary board · 十个词", PRAC, "词汇总览 · Summary board",
        s_summary([("市中心", "shizhongxin"), ("邮局", "youju"), ("诊所", "zhensuo"),
                   ("银行", "yinhang"), ("百货公司", "baihuo"), ("市政大楼", "shizheng"),
                   ("教堂", "jiaotang"), ("公园", "gongyuan")],
                  "加上「生活」和「方便」——一共十个。看一分钟，然后<b>盖起来</b>。"))
    add("15-task.html", "Activity 1 · 社区总览", PRAC, "活动一 · We Do · 6 分钟",
        s_task("活动一 · 社区总览 · 看一分钟，然后把板盖起来",
               ["<b>第一轮</b> · 两人一组，凭记忆把十个词用汉字写下来，"
                "然后打开板自己对。",
                "<b>第二轮</b> · 漏掉的每一个词，写一句话，把它摆在一个你<b>记得</b>的词旁边。"],
               "不写清单。写一段<b>四句</b>话，描述一条想象的街，十个词全部用上，"
               "每句挂着上一句。<b>板全程盖着。</b>"))

    add("16-cards.html", "Activity 2 · 词卡走动 Sentence cards", PRAC, "活动二 · We Do · 7 分钟",
        s_task("活动二 · 词卡走动（课本 p.124 第 3 题）· 每人一张卡",
               ["卡片：我们学校 · 离 · 很远 · 有 · 附近 · 市中心 · 银行 · 每个星期天 · "
                "在 · 对面 · 百货公司 · 教堂 · 公园 · 的前面 · 的后面 · 是 · 一个 · 大",
                "走动，找到能和你的卡组成句子的人，站成一句。",
                "各组念出自己的句子，全班表决：对 / 不对。做两轮，中间换卡。"],
               "一位同学拿<b>多余的卡</b>（一个用不上的「很」或「了」），"
               "他的任务是去<b>加入</b>每一组。每组都要用中文把他赶走，并说出理由："
               "<b>不行，因为这句不要「了」。</b>"))

    add("17-listening.html", "Activity 3 · 听力 CD 50", PRAC, "活动三 · You Do · 5 分钟",
        s_task("活动三 · 听力 · 课本 p.126 第 5 题 · CD 50 · 放两遍",
               ["两层楼平面图，格子 A–J。把九个房间的字母写下来：",
                "哥哥的卧室 · 客厅 · 浴室 · 爸爸、妈妈的卧室 · 厨房 · 书房 · "
                "小明的卧室 · 电视房 · 活动室",
                "房间名是二年级学过的，<b>真正要听的是位置</b>——"
                "在……对面 · 在……的隔壁 · 在右手边 · 一上楼就看见了。"],
               "<b>只听一遍</b>，而且不写字母——写下你听到的<b>五个位置词组</b>。"
               "然后用其中三个说说学校的教学楼。"))

    add("18-write.html", "Activity 4 · 翻译 + 画地图", PRAC, "活动四 · You Do · 5 分钟",
        s_task("活动四 · 两部分",
               ["<b>（甲）翻译，三分钟</b> · 练习册 p.147 第 7 题——"
                "也是<b>单元测验第三部分</b>的题型。四句都写在本子上：",
                "　1 · The post office is not far from my home.",
                "　2 · The clinic is in front of the park.",
                "　3 · The church is opposite to the city hall.",
                "　4 · The bank is behind the department store.",
                "<b>（乙）画地图，两分钟</b> · A4 纸，画自己社区的草图，"
                "至少五个地方，用汉字标出来。下节课要用。"],
               "四句写完，自己<b>再用英文出四句</b>，和同伴交换翻译。"
               "你出的四句，位置词不能和书上的重复。"))

    add("19-plenary.html", "Plenary · 出门条", PLEN, "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 特别问第三条——今天「说一段话」做得到吗？",
                "<b>自评</b> · 白板：会了 · 差不多 · 还要练，一条一条来。",
                "<b>出门条</b> · 就写你刚画的那张地图。",
                "<b>下节课</b> · 走到街上——学怎么问路：「请问，咖啡馆在哪儿？」"],
               cn="出门条：写三句，讲你画的地图，"
                  "三个不同的位置词，至少一个是前面或后面。"))

    return S
