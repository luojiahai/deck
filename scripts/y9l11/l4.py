# -*- coding: utf-8 -*-
"""Y9 L11 · Lesson 4 of 5 — lunch & dinner, the interview, 有时

Source: docs/lesson-plans/y9-l11/04-lunch-dinner-interview-mixed.md
Textbook pp.105 (rest of Text 2), 102 (Act. 3), 107 (Act. 9);
workbook pp.120, 122, 124 (Ex. 7, 11, 14, 15).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_title, s_lisc, s_ladder, s_dialogue, label)

SLUG = "l4-lunch-dinner"
TITLE = "Y9 L11 · 午饭和晚饭 · Lesson 4 of 5"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 午饭和晚饭", "LESSON 4 OF 5", "第十一课 · 零食",
        s_title("午饭和晚饭", "Lunch and dinner",
                "Year 9 · Unit 4 · Lesson 11 · Lesson 4 of 5 · 50 minutes",
                "轻松学中文 3 · pp.105, 107 · 课文二 + 采访"))

    add("02-review.html", "Review · L3 breakfast + 加", "0–8 MIN · REVIEW",
        "复习 · Lesson 3",
        s_task("复习 · 拍字（4 分钟）+ 同桌对话（3 分钟）",
               ["<b>拍字：</b>黑板上十个词 —— 谷类 · 牛奶 · 面包 · 煎蛋 · 香肠 · 加 · "
                "零食 · 巧克力 · 蛋糕 · 冰淇淋。两个同学上来，老师说词，他们拍。",
                "<b>同桌对话，不看书：</b>A 问 <b>你早饭吃什么？</b> "
                "B 要用「<b>一般</b>……，<b>有时候</b>……」两半都说到。"],
               None,
               "接上：早饭说完了。今天说午饭和晚饭 —— 然后去问四个同学，看全班吃得一样不一样。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what we eat for lunch and dinner, and to interview four classmates "
               "and report back what they said.",
               [("I can name four lunch and dinner foods in Chinese",
                 "能说出「沙拉」「酸奶」「杂菜汤」「碗」"),
                ("I can use 有时 = 有时候 and the right measure word for a dish",
                 "能用「有时」，也会说「一碗汤」「一杯牛奶」"),
                ("I can interview a classmate and report their answer to the class",
                 "能问同学，然后向全班报告：他早饭一般吃……")]))

    add("04-c1-words.html", "Cycle 1 · A — 沙拉 / 酸奶", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("沙拉", "shālā", "salad", "shala"),
                ("酸奶", "suānnǎi", "yoghurt", "suannai"))
        + '\n  <p class="support" style="margin-top:12pt;">'
          '「酸」的左边是 <b>酉</b>，一个酒坛子 —— 酸的东西、发酵的东西都用它。'
          '所以「酸奶」是 yoghurt，不是「坏掉的牛奶」。</p>')
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我午饭常常吃<b>沙拉</b>。", "I often have salad for lunch."),
                    (None, "<b>酸奶</b>对身体很好。", "Yoghurt is good for you."),
                    (None, "我午饭吃<b>沙拉</b>和<b>酸奶</b>。",
                     "For lunch I have salad and yoghurt.", True)],
                   "沙拉和薯条，哪个对身体好？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我午饭常常吃 ________ 。", "________ 对身体很好。"],
                "用「比」写一句，比较沙拉和薯条，说哪个对身体好，为什么。"
                "再加一句「可是我从小就喜欢……」说你其实爱吃哪个。"))

    add("07-c2-words.html", "Cycle 2 · A — 杂菜汤 / 碗", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("杂菜汤", "zácàitāng", "vegetable soup", "zacaitang"),
                ("碗", "wǎn", "bowl", "wan"))
        + '\n  <p class="support" style="margin-top:12pt;">'
          '「汤」的左边是 <b>氵</b>（水）。把它和第十课的「<b>场</b>」（菜市<b>场</b>）放在一起看 —— '
          '右边一样，左边不一样。「碗」的左边是 <b>石</b>。</p>')
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "妈妈做了<b>杂菜汤</b>。", "Mum made vegetable soup."),
                    (None, "我喝了一<b>碗</b>汤。", "I drank a bowl of soup."),
                    (None, "我晚饭喝一<b>碗杂菜汤</b>。",
                     "For dinner I have a bowl of vegetable soup.", True)],
                   "汤用什么量词？牛奶呢？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我喝了一碗 ________ 。", "妈妈做了 ________ 。"],
                "写三句说你们家昨天的晚饭，<b>每句都要有量词</b>（碗、杯、块、条、个）。"
                "写完把三句连成一段，加上「因为……，所以……」说为什么是妈妈做的。"))

    add("10-recall.html", "Checkpoint · 认字 recall", IDO, "检查点 · Checkpoint",
        s_recall(["沙拉", "酸奶", "杂菜汤", "碗"], "四个字一起读出来。", cols=4))

    add("11-ladder.html", "I Do · 有时 = 有时候 · 频率梯子", IDO, "句型 · 频率词 · Frequency",
        s_ladder([("总是", False), ("每天", False), ("常常／经常", False),
                  ("一般／平时／通常", False), ("有时／有时候", True), ("很少", False)],
                 "从最多到最少 · 今天的新词是第五格：<b>有时</b> yǒushí <i>sometimes</i>（课本写「有时＝有时候」）",
                 "红框是新的，其他五个第十课都学过了。「有时」只是「有时候」的短说法，"
                 "意思完全一样 —— 课本两个都用。",
                 "我午饭<b>一般</b>吃三明治，<b>有时</b>吃薯条。"))

    add("12-pattern.html", "I Do · 句型 一般…… 有时……", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 先说平常，再说例外",
                  "一般 / 平时 ……，有时 / 有时候 ……",
                  [("我们家晚饭有时候吃中餐，有时候吃西餐。",
                    "At home we sometimes eat Chinese, sometimes Western."),
                   ("我平时喝牛奶，有时喝酸奶。", "I usually drink milk; sometimes yoghurt."),
                   ("我午饭一般吃盒饭，有时吃三明治。",
                    "For lunch I usually have a box lunch; sometimes a sandwich.")]))

    add("13-pattern2.html", "I Do · 最难的一句", IDO, "句型 · 难句 · two lists",
        s_focus("最难的一句 · 两串单子对着说 · 这就是课文里的回答",
                "我午饭<b>一般</b>吃三明治、热狗、<b>酸奶</b>，<b>有时</b>吃薯条、"
                "<b>杂菜汤</b>、<b>沙拉</b>等。",
                "For lunch I usually have a sandwich, a hot dog and yoghurt; sometimes "
                "chips, vegetable soup, salad and so on.",
                "不是一样对一样 —— 是<b>一串对一串</b>。两边都用顿号「、」，后面用「等」收尾。",
                "照这个形状说晚饭：一般吃哪三样，有时吃哪三样。六样东西都要说出来，不写，直接说。"))

    add("14-text2.html", "课文二 · 后半段 (CD 43)", IDO, "课文二 · Text 2 · p.105",
        s_dialogue("课文二 · 后半段 · 再听一遍 CD 43",
                   [("A", "午饭呢？"),
                    ("B", "吃三明治、热狗、<b>酸奶</b>，<b>有时</b>吃薯条、<b>杂菜汤</b>、<b>沙拉</b>等。"),
                    ("A", "你们家晚饭吃什么？"),
                    ("B", "有时候吃中餐，有时候吃西餐。"),
                    ("A", "你们家平时谁做饭？你会帮忙吗？"),
                    ("B", "一般是妈妈做。有时候吃完晚饭以后，我会帮妈妈洗<b>碗</b>。")],
                   "最后一句的「帮忙」「吃完……以后」下节课学 —— 但「洗<b>碗</b>」是今天的词。"))

    add("15-summary.html", "词汇总览 · summary board", PRAC, "词汇总览 · Summary board",
        s_summary([("沙拉", "shala"), ("酸奶", "suannai"), ("杂菜汤", "zacaitang"),
                   ("碗", "wan"), ("有时", None)],
                  "这块板留在屏幕上 —— 分类和采访都要用。"))

    add("16-task.html", "We Do · 分类 (WB 15 + Act. 3 + WB 7)", PRAC,
        "任务 · 练习册 p.124 Ex. 15 · 课本 p.102 Act. 3",
        s_task("We Do · 二十四个词分五类 · 两人一组 · 5 分钟",
               ["五个格子：<b>中餐 / 西餐 / 快餐 / 零食 / 饮料</b>",
                "蒸鱼 · 牛排 · 汽水 · 薯条 · 冰淇淋 · 杂菜汤 · 沙拉 · 薯片 · 花茶 · 炒青菜 · "
                "比萨饼 · 炸鸡翅 · 热狗 · 可乐 · 糖果 · 三明治 · 巧克力 · 红烧豆腐 · "
                "饼干 · 绿茶 · 鸡汤 · 汉堡包 · 炸鸡腿 · 北京烤鸭",
                "分完，用中文说出两个的理由：<b>我觉得沙拉是西餐，因为……</b>",
                "然后做<b>课本 Act. 3 / 练习册 Ex. 7</b>：每一类自己再加五个，不能用板上有的。",
                "<b>这就是单元测验第一大题的样子。</b>"],
               "每一类加<b>五</b>个，五个里至少两个要是第十课学的（菜市场的词）。"
               "加完读练习册 p.122 Ex. 11 的短文，用中文回答五个问题，"
               "再把你们学校餐厅卖的东西填进「正餐／零食／小吃／饮料」四个格子里。全部用汉字。"))

    add("17-act9.html", "You Do · 采访四个同学 (Act. 9)", PRAC,
        "活动二 · 课本 p.107 · Act. 9",
        s_list("You Do · 采访 <b>四个</b>同学，笔记用中文写 · 10 分钟",
               [("你早饭一般吃什么？", ""), ("你午饭一般吃什么？", ""),
                ("你晚饭一般吃什么？", ""), ("你们家周末常常去饭店吃饭吗？", ""),
                ("你们一般去哪家饭店吃饭？", ""), ("你们一般吃什么？", "")],
               "<b>然后向全班报告</b>（这才是重点，报告要用第三人称）："
               "三个同学早饭一般吃水果和面包，喝牛奶。一个同学有时候早饭吃谷类早餐加牛奶。",
               compact=True))

    add("18-wb14.html", "You Do · 量词 (WB 14)", PRAC, "活动三 · 练习册 p.124 · Ex. 14",
        s_task("You Do · 十六个量词，每个写一样东西 · 4 分钟",
               ["件 · 条 · <b>碗</b> · 辆 · 支 · 架 · 副 · 顶 · 个 · 间 · 位 · 套 · 幢 · 双 · 口 · 种",
                "先做最容易的八个，再做剩下的。<b>「碗」是今天的词，必须在那八个里。</b>",
                "<b>这是单元测验第二大题的样子。</b>"],
               "十六个全部写完，而且每个词组都要写成一个<b>完整的句子</b>，不是只写名词。"
               "比如不写「碗：汤」，写「我喝了一碗杂菜汤」。"))

    add("19-game.html", "Game · 找不同 Odd One Out", PRAC, "游戏 · 找不同 · 4 分钟",
        s_list("Game · 哪个不一样？用中文说<b>为什么</b>",
               [("沙拉 · 酸奶 · 杂菜汤 · <b>碗</b>", "碗不是吃的"),
                ("总是 · 常常 · 有时 · <b>牛奶</b>", "牛奶不是频率词"),
                ("面包 · 煎蛋 · 香肠 · <b>冰淇淋</b>", "冰淇淋不是早饭"),
                ("碗 · 杯 · 条 · <b>汤</b>", "汤不是量词"),
                ("巧克力 · 饼干 · 蛋糕 · <b>正餐</b>", "正餐不是零食")],
               "第 2、5 题不止一个答案 —— 能用中文把<b>另一个</b>答案讲通的，那一轮就算赢。",
               compact=True))

    add("20-plenary.html", "Plenary · exit ticket & preview", "43–50 MIN · PLENARY",
        "小结 · Plenary",
        s_list("小结 · 43–50 分钟",
               [("<b>回看目标</b> · 读一遍，问两个报告过的同学：第三条打勾了吗？", ""),
                ("<b>自评</b> · 白板上三条一起写 👍 / 😐 / 👎。", ""),
                ("<b>Exit ticket</b> · 用「一般……，有时……」写一句：你午饭吃什么。", ""),
                ("<b>下节课</b> · 第十一课最后一节：学「吃完饭以后……」，"
                 "学十二个部件，还要把整课复习一遍。", "")]))
    return S
