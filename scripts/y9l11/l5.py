# -*- coding: utf-8 -*-
"""Y9 L11 · Lesson 5 of 5 — 帮忙 · 完 · ……完……以后 · 部件 · whole-lesson review

Source: docs/lesson-plans/y9-l11/05-wan-yihou-radicals-mixed.md
Textbook pp.107-109 (Act. 10, 11, 12, 13); workbook pp.122, 125-126
(Ex. 10, 16, 17, 18).
"""
from build import (s_words, s_examples, s_write, s_recall, s_pattern, s_focus,
                   s_task, s_list, s_listening, s_title, s_lisc, s_components, label)

SLUG = "l5-wan-yihou"
TITLE = "Y9 L11 · ……完……以后 · Lesson 5 of 5"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"

ALL24 = ["零食", "各种各样", "比如", "巧克力", "蛋糕", "冰淇淋",
         "饼干", "牙齿", "从小", "总是", "正餐", "谷类",
         "加", "牛奶", "面包", "煎蛋", "香肠", "酸奶",
         "有时", "杂菜汤", "沙拉", "帮忙", "完", "碗"]


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 吃完饭以后", "LESSON 5 OF 5", "第十一课 · 零食",
        s_title("吃完饭以后", "After we finish",
                "Year 9 · Unit 4 · Lesson 11 · Lesson 5 of 5 · 50 minutes",
                "轻松学中文 3 · pp.107–109 · 全课复习"))

    add("02-review.html", "Review · 全课 24 词", "0–8 MIN · REVIEW",
        "复习 · 第十一课全部生词",
        s_recall(ALL24,
                 "全班从左读到右。读完，老师随便点五个，问英文是什么。"
                 "这一课一共二十四个生词 —— 今天学最后两个。",
                 cols=6, size="9pt 5pt",
                 head="第十一课 · 二十四个生词 · 只有汉字 · 一起读"))

    add("03-radicals.html", "Review · 部件 (Act. 13)", "0–8 MIN · REVIEW",
        "汉字 · 课本 p.109 · Act. 13",
        s_components(["矢", "斗", "力", "寸", "青", "旦", "自", "己", "亡", "立", "几", "上"],
                     "记住这十二个部件 · 课本说五分钟，我们用三分钟",
                     "看三分钟 → 关屏幕 → 在白板上写，能写几个写几个。只数数目，不打分。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what we do after finishing something, and to recognise the character "
               "components behind this unit's food words.",
               [("I can say 帮忙 and use 完 to mean “finish”",
                 "能说「我帮妈妈洗碗」，会用「吃完」「做完」"),
                ("I can use ……完……以后，…… to link two actions",
                 "能用「……完……以后，……」说两件事"),
                ("I can write twelve character components from memory",
                 "能默写十二个部件")]))

    add("05-c1-words.html", "Cycle 1 · A — 帮忙 / 完", IDO, "生词 1 · Cycle 1 of 1",
        s_words(("帮忙", "bāngmáng", "to help", "bangmang"),
                ("完", "wán", "to finish", None)))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我常常<b>帮</b>妈妈洗碗。", "I often help my mum wash up."),
                    (None, "我做<b>完</b>作业了。", "I've finished my homework."),
                    (None, "我吃<b>完</b>晚饭以后，会<b>帮</b>妈妈洗碗。",
                     "After I finish dinner I help my mum wash up.", True)],
                   "「你会帮忙吗？」和「你会帮妈妈吗？」——两个都对吗？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我常常帮 ________ 。", "我 ________ 完了。"],
                "写三句：一句说你在家帮谁做什么，一句说你上个周末做完了什么，"
                "一句用「因为……，所以……」说你为什么帮忙（或者为什么不帮忙）。三句要连起来。")
        + '\n  <p class="support" style="margin-top:10pt;">'
          '注意：<b>帮忙</b> 后面不能再放人。「帮<b>忙</b>妈妈」是错的 —— '
          '说谁的时候把「忙」拿掉：<b>帮妈妈</b>。</p>')

    add("08-pattern.html", "I Do · 句型 ……完……以后", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · V + 完 + O + 以后，+ 第二件事",
                  "…… 完 …… 以后，……",
                  [("我吃完早饭以后刷牙。", "After I finish breakfast I brush my teeth."),
                   ("他游完泳以后去买零食。", "After he finishes swimming he goes to buy snacks."),
                   ("我们一家人看完电影以后去饭店吃饭。",
                    "After we finish the film the family goes out to eat.")],
                  "「完」放在动词<b>后面</b>，不是前面：吃<b>完</b>，不是<b>完</b>吃。"))

    add("09-note.html", "I Do · 课本 NOTE · 两种语序", IDO, "语序 · 课本 p.108 · NOTE",
        label("课本 p.108 的 NOTE · 这两句意思<b>完全一样</b>")
        + '  <div class="frame-box">\n'
          '    <p class="frame-line" style="font-size:28pt;">做完作业以后，他看电视。</p>\n'
          '    <p class="frame-line" style="font-size:28pt;">＝ 他做完作业以后看电视。</p>\n'
          '  </div>\n'
        + '  <p class="body-lg" style="margin-top:14pt;">'
          '「他」可以放在最前面，也可以放在「以后」前面 —— 两种都对，课本两种都印了。</p>\n'
        + '  <div class="extension-box">\n'
          '    <p class="extension-label">Extension</p>\n'
          '    <p class="extension-text">'
          '把黑板上三个例句每一句都用<b>另一种</b>语序再说一遍。说得出来，'
          '再自己造一句两种语序都说。</p>\n  </div>')

    add("10-focus.html", "I Do · 最难的一句", IDO, "句型 · 难句 · 用两次",
        s_focus("最难的一句 · 一句话里用两次 · 「才」是第二册的",
                "我吃<b>完</b>晚饭<b>以后帮</b>妈妈洗碗，洗<b>完</b>碗<b>以后</b>才做作业。",
                "After I finish dinner I help mum wash up, and only after the washing-up "
                "is done do I start my homework.",
                "两次「完……以后」，一件事接一件事。「才」是「一直到那时候才」—— 有点晚的意思。",
                "照这个样子说你自己的晚上，从放学说到睡觉，至少用两次「完……以后」。不写，直接说。"))

    add("11-act11.html", "We Do · 课本 Act. 11 (8 items)", PRAC,
        "任务 · 课本 p.108 · Act. 11",
        s_task("We Do · 八题 · 6 分钟 · <b>1–4 和 5–8 是反过来的，两边都要做</b>",
               ["<b>1–4 给了前半句，补后半句：</b>",
                "1 我吃完早饭以后 ____ 。（刷牙，课本已给） · 2 他游完泳以后去 ____ 。 · "
                "3 我们一家人看完电影以后去 ____ 。 · 4 她做完作业以后去 ____ 。",
                "<b>5–8 给了后半句，补「……完……以后」那一半：</b>",
                "5 ____ 帮妈妈洗碗。 · 6 ____ 跟姐姐一起去买菜。 · "
                "7 ____ 去图书馆看书。 · 8 ____ 跟爸爸一起去钓鱼。",
                "然后 <b>It is your turn!</b> —— 自己写三句。"],
               "做<b>练习册 p.125 Ex. 16</b> 的四组图，每组写一句「……完……以后」。"
               "然后把四句连成一段话，说一个人的一天，从早上到晚上，"
               "中间要用「先……，然后……，最后……」。"))

    add("12-act12.html", "You Do · 听力 CD 44", PRAC, "活动二 · 课本 p.108 · Act. 12",
        s_listening("You Do · 听力 · CD 44 · 放两遍，错得最多的两题再放一遍 · 6 分钟",
               [("今天早餐她想吃 ____ 。", "a) 面包、煎蛋 &nbsp; b) 谷类早餐加牛奶 &nbsp; c) 牛奶、面包"),
                ("她想在她的茶里加 ____ 。", "a) 糖和牛奶 &nbsp; b) 水和糖 &nbsp; c) 牛奶"),
                ("她今天午饭想吃 ____ 。", "a) 汉堡包和薯条 &nbsp; b) 炸鸡腿和沙拉 &nbsp; c) 炸鸡翅和沙拉"),
                ("她昨天晚饭吃了 ____ 。", "a) 杂菜汤、水果和面包 &nbsp; b) 比萨饼和沙拉 &nbsp; c) 杂菜汤、沙拉和面包"),
                ("他们家一般吃 ____ 。", "a) 西餐 &nbsp; b) 中餐 &nbsp; c) 快餐"),
                ("他们家平时 ____ 。", "a) 她做饭，妈妈洗碗 &nbsp; b) 妈妈做饭，妈妈洗碗 &nbsp; c) 妈妈做饭，她洗碗")],
               "第 6 题就是今天的句型：录音里说 <b>吃过晚饭，我经常洗碗。</b> "
               "再放一遍，问问「吃过」在这里是什么意思。"))

    add("13-act10.html", "You Do · 课本 Act. 10 · 五个问题", PRAC,
        "活动三 A · 课本 p.107 · Act. 10",
        s_list("You Do · 同桌互问 · 2 分钟 · 加点的词就是目标",
               [("你<b>有时候</b>在学校餐厅买午饭吃，你呢？", ""),
                ("你<b>小时候</b>在哪儿住过？", ""),
                ("<b>上课的时候</b>你可以吃东西吗？", ""),
                ("<b>放学以后</b>，你一般什么时候到家？", ""),
                ("你<b>从小就</b>喜欢吃什么？不喜欢吃什么？", "")],
               "<b>It is your turn!</b> —— 每个人再用其中一个加点的词自己造一个问题，去问同桌。"))

    add("14-wb18.html", "You Do · 练习册 Ex. 18 · 八个句型", PRAC,
        "活动三 B · 练习册 p.126 · Ex. 18",
        s_task("You Do · 八个句型，每个写一句 · 4 分钟",
               ["有时候 · 小时候 · ……的时候 · 从小 · 一……就…… · 除了……以外，…… · "
                "一边……，一边…… · 因为……，所以……",
                "<b>先做 从小 · 有时候 · 因为……所以……</b> —— 这三个测验要考。剩下的有时间再做。",
                "<b>每一句都要说吃的或者吃饭</b> —— 这样这一课的词就跟着老句型一起复习了。"],
               "八个句型全部写完，而且八句要组成<b>一段</b>话，说你自己的一天吃什么。"
               "不是八个不相关的句子 —— 要能从头读到尾。写完念给同桌，同桌说哪一句最好。"))

    add("15-game.html", "Game · 写字接力 Writing Relay", PRAC, "游戏 · 写字接力 · 5 分钟",
        s_task("Game · 两队，黑板上两列，老师说线索，下一个同学跑上来写",
               ["<b>第一轮 · 练习册 p.122 Ex. 10 的九个简单字：</b>",
                "tongue 舌 · melon 瓜 · sheep 羊 · seedling 苗 · east 东 · "
                "south 南 · west 西 · north 北 · bow 弓",
                "<b>第二轮 · 练习册 p.125 Ex. 17 组词：</b>老师说一半，跑上来的同学写出完整的词",
                "煎 ___ · ___ 肠 · 面 ___ · 热 ___ · 酸 ___ · "
                "___ 排 · 沙 ___ · 盒 ___ · ___ 汤 · 鸡 ___"],
               "第二轮要写词组<b>加量词</b>（一碗杂菜汤、一块牛排）。没有量词不算分。"
               "最后三个让说得最好的同学来当出题的人。"))

    add("16-plenary.html", "Plenary · 全课小结 whole sequence", "43–50 MIN · PLENARY",
        "小结 · 第十一课 · Plenary",
        s_list("小结 · 这次看的是<b>整个第十一课</b>，不只是今天 · 43–50 分钟",
               [("<b>五节课，五条目标</b> · 能说各种各样的零食 → 能用「对……不好」→ "
                 "能说早饭吃什么 → 能问同学然后报告 → 能用「……完……以后」",
                 "每一条举手 👍 / 😐 / 👎。哪一条 😐 最多，测验前就回去补哪一条。"),
                ("<b>问一句</b> · 五节课里，哪一节最难？", ""),
                ("<b>Exit ticket · 两句</b> · 第一句用「……完……以后，……」说你今天放学以后做什么。",
                 "第二句用「从小就」说一样你一直喜欢吃的东西。"),
                ("<b>下一课</b> · 第十一课学完了。下一课是第十二课 —— "
                 "外出就餐：去饭店点菜、看菜单、自助餐。", "")]))
    return S
