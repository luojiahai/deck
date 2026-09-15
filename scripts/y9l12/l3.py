# -*- coding: utf-8 -*-
"""Y9 L12 · Lesson 3 of 6 — 完……以后, 挺……的, 一共花了 + ¥200 role-play + CD 46

Source: docs/lesson-plans/y9-l12/03-meal-story-mixed.md
Textbook pp.112-114 (Act. 4, 5, 6, 7); workbook p.136 (Ex. 21).
No new vocabulary — this is the consolidation lesson of the sequence.
"""
from build import (s_write, s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_errors, s_listening, s_recall, s_title, s_lisc, label)

SLUG = "l3-meal-story"
TITLE = "Y9 L12 · 外出就餐 Eating Out · Lesson 3 of 6"

IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 说一说你去饭店吃饭", "LESSON 3 OF 6", "第十二课 · 外出就餐",
        s_title("一共花了", "Telling the Story of a Meal Out",
                "Year 9 · Book 3 · Unit 4 · Lesson 12 · 50 minutes",
                "轻松学中文 3 · pp.112–114"))

    add("02-review.html", "Review · Bingo on Text 1's nine words", "0–8 MIN · REVIEW",
        "复习 · Bingo",
        s_recall(["自助餐", "龙虾", "三文鱼", "寿司", "烤", "牛排", "甜品", "奶酪", "饱"],
                 "画一个 3×3 的格子，选九个词填进去。老师不念词，念解释——"
                 "听懂了才划得掉。", cols=5))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("describe a meal out from start to finish — the courses, "
               "what it cost, and what we thought of it.",
               [("I can use 完……以后…… to say what I do after finishing something",
                 "能用「完……以后……」说做完一件事再做什么"),
                ("I can say what a meal cost using 一共花了……块", "能说一共花了多少钱"),
                ("I can give an opinion using 挺……的", "能用「挺……的」说我的看法")]))

    add("04-no-new-words.html", "Today · no new words, a lot of talking", IDO,
        "今天没有生词",
        s_task("今天没有生词——但是要说很多话",
               ["这是这一课的<b>巩固课</b>：Text 1 的九个词全部用上。",
                "学三个句型：完……以后…… · 一共花了……块 · 挺……的",
                "然后拿二百块去买菜。"],
               cn="今天没有生词，但是要说很多话。"))

    # ── Pattern 1 ──
    add("05-pattern1.html", "Pattern 1 · 完……以后……", IDO, "句型一 · Sentence pattern",
        s_pattern("句型一 · 做完一件事再做下一件",
                  "动词 + 完 + (宾语) + 以后 + 再 + 动词",
                  [("我一般喝完汤以后再吃主食。",
                    "I usually finish my soup before eating the main course."),
                   ("我一般吃完主食以后再吃甜品。",
                    "I usually finish the main before eating dessert."),
                   ("我一般踢完球以后洗澡。", "I usually shower after playing football.")],
                  "「完」紧跟动词，「以后」收尾。不是 ✗以后我吃完饭做作业。"))
    add("06-focus1.html", "Focus · the hardest example", IDO, "句型一 · 最难的一句",
        s_focus("句型一 · 加「才」和「所以」",
                "我一般做完作业以后才能看电视，所以我每天都做得很快。",
                "I can only watch TV after I finish my homework, so I do it fast every day.",
                "「才」= not until。后面再加一个「所以」的分句。"))

    # ── Pattern 2 ──
    add("07-pattern2.html", "Pattern 2 · 一共花了 · 挺……的", IDO, "句型二 · Sentence pattern",
        s_pattern("句型二 · 花了多少钱 · 你觉得怎么样",
                  "一共花了 + 金额　·　挺 + 形容词 + 的",
                  [("我们一共花了三百多块。", "Altogether we spent three hundred odd."),
                   ("挺便宜的。", "Quite cheap."),
                   ("我们一共花了六百多块，挺贵的。",
                    "Altogether we spent six hundred odd — quite pricey.")],
                  "「三百<b>多</b>块」= three hundred <i>odd</i>，不是正好三百。"))

    add("08-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「完」放在哪里？动词前面还是后面？", "举手回答"),
               ("这句话对不对？ ✗ 以后我看完书做作业。", "白板上改写——这是练习册第 21 题的题型"),
               ("「挺便宜的」和「很便宜」哪个语气轻一点？", "点名回答"),
               ("三百多块——是三百块吗？还是更多？", "Thumbs up / down")]))

    # ── Practice ──
    add("09-act1.html", "Activity 1 · 完……以后 drill (We Do, 5 min)", PRAC,
        "活动一 · We Do · 5 分钟",
        s_list("活动一 · 白板接龙 · 课本 p.112 第 4 题",
               [("我一般喝完汤以后再 ________ 。", None),
                ("我一般吃完主食以后再 ________ 。", None),
                ("我一般踢完球以后 ________ 。", None),
                ("我一般做完 ________ 。", None),
                ("我一般 ________ 。", None)],
               "每一轮念两个答案。到第五题，整句都要自己写。<br>"
               "<b>加难</b>：一句里串三个动作——我一般做完作业以后先吃晚饭，吃完晚饭以后再看电视。"
               "然后用第三人称，写家里另一个人。", compact=True))

    add("10-act2-listening.html", "Activity 2 · CD 46 listening (6 min)", PRAC,
        "活动二 · 听力 · 课本 p.114 第 6 题 · CD 46",
        s_listening("听一听，选一选 · 放两遍 · 第一遍放下笔",
                    [("他们家一般____去吃一次。", "a) 一周　b) 两周　c) 一个月"),
                     ("他们家常去吃____。", "a) 西式自助餐　b) 中式自助餐　c) 日本料理"),
                     ("上个周末____。", "a) 她爸爸病了　b) 她妈妈病了　c) 她自己不舒服"),
                     ("那家饭店____。", "a) 烤牛排做得最好吃　b) 烤羊排做得不好吃　c) 烤猪排做得一般"),
                     ("那家饭店的饭菜____。", "a) 又不好吃又贵　b) 又好吃又便宜　c) 做得好吃，但是挺贵的"),
                     ("下个月____。", "a) 爸爸要出差　b) 爸爸回来　c) 妈妈要出差")],
                    "第 5 题讲完以后把「<b>又……又……</b>」写在黑板上——它是「挺……的」的好搭档。<br>"
                    "<b>加难</b>：写下每题的<b>理由</b>——录音里哪一句说了答案。"))

    add("11-act3-speaking.html", "Activity 3 · It is your turn (3 min)", PRAC,
        "活动三 · 说一说 · 课本 p.114 第 7 题",
        s_task("活动三 · 说你自己的一次外出就餐 · 三分钟",
               ["先看范文（课本 p.114）：上个星期天是我妈妈的生日……爸爸一共花了六百多块，挺便宜的。",
                "转过身跟同桌说三十秒——每个人都说。",
                "老师点三个同学说给全班听。",
                "每个人都要有：<b>一共花了……</b> 和 <b>挺……的</b>。"],
               "用第三人称，说那个付钱的人。再加一句下次要点什么，为什么（下次我要点……，因为……）。"))

    add("12-act4-roleplay.html", "Activity 4 · ¥200 at the market (You Do, 9 min)", PRAC,
        "活动四 · You Do · 9 分钟 · 课本 p.113 第 5 题",
        s_task("活动四 · 二百块，买给你们一家人吃",
               ["两人一组。A 是<b>售货员</b>，B 是<b>顾客</b>，手里有 ¥200。",
                "B 至少问三样的价钱，至少买两样。然后交换。"],
               "二百块要花得<b>尽量正好</b>。每买一样，B 要用中文说出现在一共花了多少"
               "（现在一共花了一百三十四块）。用「比」比较两个摊子（这里的牛排比那里的便宜）。"
               "最后向全班报告买了什么、<b>没买什么、为什么</b>（我没买龙虾，因为太贵了）。"
               "然后交换——新的售货员要想办法让顾客买更贵的。",
               cn="售货员：我能帮你吗？　顾客：我想买几个龙虾。多少钱一个？　售货员：六十块。"
                  "　顾客：挺贵的。　售货员：不算贵，已经很便宜了。　顾客：我觉得很贵。我不买了。"))

    add("13-prices.html", "Price board · 课本 p.113", PRAC, "价目表 · Price board",
        label("价目表 · 每组一张 · ¥200")
        + '  <div class="recall-grid" style="grid-template-columns:repeat(3,1fr);">\n'
        + "\n".join('    <div class="recall-cell" style="padding:10pt 6pt;">'
                     '<p class="recall-hanzi" style="font-size:26pt;">%s</p></div>' % w
                     for w in ["龙虾 ¥60/个", "三文鱼 ¥68/块", "寿司 ¥5/个",
                               "鸡腿 ¥12/斤", "活鱼 ¥12/条", "牛排 ¥22/斤",
                               "活虾 ¥25/斤", "鸡翅 ¥10/斤", "香肠 ¥18/斤"])
        + "\n  </div>\n"
        + '  <p class="support" style="margin-top:12pt;">'
          '注意量词：个 · 块 · 斤 · 条——问价钱的时候要说对。</p>')

    add("14-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 一个同学念一条，全班马上给一个例子。",
                "<b>自评</b> · 三条目标，👍 / 😐 / 👎。",
                "<b>出门条</b> · 写一句。",
                "<b>下节课</b> · 我们进饭店坐下来——怎么看菜单，怎么点菜。"],
               cn="出门条：写一句用「完……以后……」，说你放学以后做什么。"))
    return S
