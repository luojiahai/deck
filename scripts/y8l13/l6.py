# -*- coding: utf-8 -*-
"""Y8 L13 · Lesson 6 of 6 — the garage, and your whole house

Source: docs/lesson-plans/y8-l13/06-garage-whole-house-mixed.md
Textbook p.125 Act. 5 (project), p.127 (Text 2, New Words 6–7),
p.129 Act. 9 (oral presentation), p.130 Act. 11 (CD 65),
p.131 Act. 12 (categorisation). Workbook p.146 Ex. 3, p.152 Ex. 18,
p.153 Ex. 20.

The plenary looks back over all six lessons, not just this one. There is no
review lesson after this: the sequence ends on content.
"""
from build import (s_words, s_examples, s_write, s_summary, s_pattern, s_focus,
                   s_task, s_list, s_cfu, s_tickgrid, s_dialogue, s_recall,
                   s_title, s_lisc)

SLUG = "l6-garage-whole-house"
TITLE = "Y8 L13 · 房子 House · Lesson 6 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

# Card shown on the series landing page (index/designs/y8-l13/index.html),
# written by build.py. Lives beside the lesson it describes.
CARD = dict(cn='停两辆车', en='The garage · your whole house',
            desc='The last two words finish Text 2, all four measure words come together, and students design and present a house of their own. The plenary looks back over all six lessons.',
            words='停 · 辆', n=2)

ALL18 = [("房子", "fangzi"), ("房间", "fangjian"), ("层", "ceng"), ("楼", "lou"),
         ("楼上", "loushang"), ("楼下", "louxia"), ("卧室", "woshi"),
         ("书房", "shufang"), ("浴室", "yushi"), ("洗澡", "xizao"),
         ("客厅", "keting"), ("餐厅", "canting"), ("厨房", "chufang"),
         ("洗手间", "xishoujian"), ("洋房", "yangfang"), ("花园", "huayuan"),
         ("车库", "cheku"), ("停", "ting"), ("辆", "liang")]


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 车库 The garage, and your whole house", "LESSON 6 OF 6",
        "第十三课 · 房子",
        s_title("停两辆车", "The Garage, and Your Whole House",
                "Year 8 · Book 2 · Unit 5 · Lesson 13 · 50 minutes",
                "轻松学中文 2 · pp.125, 129, 131 · CD 65"))

    add("02-review.html", "Review · CD 65 tick grid (textbook p.130 Act.11)", REV,
        "复习 · 听力 · 课本 p.130 第 11 题",
        s_tickgrid(["卧室", "浴室", "洗手间", "客厅", "厨房", "车库", "大花园", "小花园"],
                   ["楼上", "楼下", "房前", "房后"],
                   "听一听，打勾 · CD 65 · 放两遍",
                   "这一段话把前五节课的词几乎全用上了。对答案的时候不要只说「打勾了」——"
                   "用整句回答：<b>厨房在哪儿？→ 厨房在楼下。</b>"))
    add("03-review-q.html", "Review · one question before we start", REV, "复习 · 一个问题",
        s_task("刚才那段话最后提到一个「车库」",
               ["车库是<b>做什么用</b>的？",
                "现在还说不出来——二十分钟以后就说得出来了。"],
               cn="我家的车库可以 ________ 两 ________ 车。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("describe a whole house — inside and out — in a presentation to the class.",
               [("I can say how many cars a garage holds", "能说车库可以停几辆车"),
                ("I can use the right measure word for rooms, storeys and cars",
                 "能用对量词：间、个、层、辆"),
                ("I can present a description of a house without reading it out",
                 "能不看稿子，向全班介绍一个房子")]))

    # ── The last cycle ──
    add("05-c1-words.html", "Cycle 1 · A — 停 / 辆", IDO, "生词 · 最后两个词",
        s_words(("停", "tíng", "to stop; (of cars) be parked", "ting"),
                ("辆（輛）", "liàng", "measure word for vehicles", "liang")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 · See them used",
        s_examples([("我家的车库可以<b>停</b>两<b>辆</b>车。",
                     "Our garage holds two cars — the last line of Text 2.", True),
                    ("车<b>停</b>在房前。", "The car is parked in front of the house."),
                    ("我家有两<b>辆</b>车，都<b>停</b>在车库里面。",
                     "We have two cars, both parked in the garage.", True)],
                   "你家有几辆车？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 · Write your own",
        s_write(["我家有 ________ 辆车。", "车停在 ________ 。"],
                "两个小句加一个原因：<b>我家有三辆车，可是车库只可以停两辆，"
                "所以一辆停在房前。</b>"))

    add("08-text2.html", "Text 2 · complete", IDO, "课文二 · 现在整段都会了",
        s_dialogue("课文二 · 整段 · 不放拼音 · 两人读，然后交换",
                   [("A", "你家住什么样的房子？"), ("B", "我家住洋房。"),
                    ("A", "你家有花园吗？"), ("B", "有两个，房前一个，房后一个。"),
                    ("A", "你家有车库吗？"), ("B", "有。我家的车库可以停两辆车。")],
                   "读第二遍的时候把课本合上，黑板上只留四个问句。"))

    # ── Measure words, all four ──
    add("09-pattern.html", "Pattern · 间 · 个 · 层 · 辆", IDO, "句型 · 四个量词",
        s_pattern("量词 · 单元测验直接考这个",
                  "间 卧室　个 浴室　层 房子　辆 车",
                  [("楼上有三<b>间</b>卧室。", "Bedrooms take 间."),
                   ("我家有两<b>个</b>浴室和一<b>个</b>书房。", "Most other rooms take 个."),
                   ("我家的房子有两<b>层</b>。", "层 counts itself — no 个.")],
                  "「辆」只用在车上：两<b>辆</b>车、三<b>辆</b>公共汽车。"))
    add("10-focus.html", "Focus · every measure word in one sentence", IDO, "句型 · 最难的一句",
        s_focus("一句话，四个量词全用上",
                "我家住洋房，房子有两层，楼上有四间卧室和两个浴室，"
                "房后有一个大花园和一个车库，车库可以停两辆车。",
                "We live in a western-style house of two storeys; upstairs there are four "
                "bedrooms and two bathrooms; behind the house there's a big garden and a "
                "garage that holds two cars.",
                "层 · 间 · 个 · 辆 —— 一个都不能错。"))

    add("11-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("间、个、层 还是 辆？ 我家有三 ____ 车。", "写在小白板上"),
               ("间、个、层 还是 辆？ 楼下有一 ____ 卧室。", "写在小白板上"),
               ("这句话对不对？ ✗ 我家的房子有两个层。", "哪里错了？"),
               ("翻译：<i>Our garage holds three cars.</i>", "写整句"),
               ("这一课里，哪两个房间用「间」不用「个」？", "点名回答")]))

    add("12-summary.html", "Summary board · 十九个词，全在这儿", PRAC,
        "词汇总览 · 整节课留在屏幕上",
        s_summary(ALL18, "六节课的词。活动一、活动二只能看这一页——没有别的参考。", dense=True))

    # ── Practice ──
    add("13-act1.html", "Activity 1 · Categorisation race (We Do, 7 min)", PRAC,
        "活动一 · We Do · 7 分钟 · 课本 p.131 第 12 题",
        s_task("活动一 · 分类比赛 · 四人一组，一套字卡",
               ["二十五张字卡，分到桌上的类里：<b>房子 · 蔬菜 · 水果 · 饭菜 · 运动 · 爱好</b>。",
                "分完以后，从总览页再<b>自己加三个</b>到「房子」那一堆。",
                "分对最多的一组赢。「房子」那一堆全班一个一个对。",
                "每组要用中文说清楚其中两张为什么放那儿。"],
               cn="为什么把「浴室」放在「房子」？　因为浴室是房子里面的房间。"))
    add("14-act1-wb.html", "Straight after · Workbook p.146 Ex.3 + p.152 Ex.18", PRAC,
        "活动一 · 练习册 · 两分钟",
        s_task("练习册 · 同一件事，写下来 · 两分钟",
               ["给一个词，自己再加三个同类的。刚刚分过的那一堆直接用。",
                "<b>p.146 第 3 题</b>　苹果 · 客厅 · 晴天 · 炒菜 · 冰水 · 黄瓜 · 跑步 · 油画儿",
                "<b>p.152 第 18 题</b>　浴室 · 橘子 · 跑步 · 西红柿 · 冷开水 · 油画儿"],
               cn="客厅　________　________　________"))

    add("15-act2.html", "Activity 2 · Design your house (You Do, 10 min)", PRAC,
        "活动二 · You Do · 10 分钟 · 课本 p.125 第 5 题",
        s_task("活动二 · 设计一个房子 · 课本给的要求，一个都不能少",
               ["两间卧室 · 一个客房 · 一个浴室 · 一个洗手间 · 一个书房",
                "一个客厅、一个餐厅 · 一个正门、一个后门",
                "再加一个 <b>花园</b> 和一个 <b>车库</b>，还要说车库可以停几辆车。",
                "上半张纸画剖面图，房间名用汉字标；下半张写介绍，从课本那句开头。"],
               cn="这是我家的房子。我家的房子有两层。我家有一个正门和一个后门。楼上有……"))
    add("16-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难",
               ["写成一段话，至少八句，不要写成一张房间清单。"],
               "用「还有」「可是」「除了……还有……」连起来。里面要有一句"
               "<b>比较</b>（房后的花园比房前的大），还要有一句<b>说理由的想法</b>"
               "（我特别喜欢我的房间，因为它在楼上）。写完把纸翻过来——"
               "等一下上台，图和稿子都不能看。"))
    add("17-act2-alt.html", "Or · Workbook p.153 Ex.20", PRAC, "活动二 · 另一个选择",
        s_task("不想自己设计的，做这个 · 练习册 p.153 第 20 题",
               ["画好的三层房子，照着描述就行，开头也给好了。",
                "写的要求一样，只是不用从白纸开始。"],
               cn="我家的房子有三层。"))

    add("18-present.html", "Presentation · share back (6 min)", PRAC,
        "上台说 · 6 分钟 · 课本 p.129 第 9 题",
        s_task("四五个同学上台 · 举着图 · 说一分钟",
               ["老师先用课本 p.129 的例子示范一次。",
                "每个人说完，全班有两个同学用中文提问。",
                "<b>加难</b>：手上什么都不拿，屏幕也不放，回答三个问题，其中一个是老师临时问的。"],
               cn="我家住洋房。我家的房子有两层。楼上有一间主人房，还有一个洗澡间。"
                  "我的房间也在楼上。楼下有……我们家有一个前花园和一个车库。"))
    add("19-present-q.html", "Questions the class can ask", PRAC, "上台说 · 全班提问",
        s_list("每个人说完，全班问两个 · 只能用中文",
               [("你的卧室在几楼？", ""), ("车库可以停几辆车？", ""),
                ("你家有几个花园？在房前还是房后？", ""),
                ("你最喜欢哪一个房间？为什么？", "这一句要用「因为」")],
               "问题投在屏幕上，谁都可以问。", compact=True))

    # ── Plenary: the whole sequence ──
    add("20-plenary-recall.html", "Plenary · all nineteen, characters only", PLEN,
        "小结 · 六节课的词",
        s_recall(["房子", "房间", "层", "楼", "楼上", "楼下", "卧室", "书房",
                  "浴室", "洗澡", "客厅", "餐厅", "厨房", "洗手间", "洋房",
                  "花园", "车库", "停", "辆"],
                 "全班一起读一遍。这是第十三课的全部生词。",
                 cols=5, head="第十三课 · 十九个词 · 一起读"))
    add("21-plenary.html", "Plenary · self-assessment across all six lessons", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟 · 这一次回看的是整整六节课",
               ["<b>回看目标</b> · 先念今天的三条，再把六节课的学习目标放一页，从头念到尾。",
                "<b>自评</b> · 小白板分六栏，一节课一栏，写 👍 / 😐 / 👎，一起举起来。",
                "😐 最多的那一栏，就是下一课复习环节的开头。",
                "<b>出门条</b> · 写在纸条上，出门交。",
                "<b>下节课</b> · 进第十四课——家具。房间你全会说了，现在把它们填满。"],
               cn="出门条：写两句关于你家的话，一句用「有」，一句用「在」，"
                  "两句里至少用到这一课的三个词。"))
    return S
