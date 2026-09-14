# -*- coding: utf-8 -*-
"""Y9 L11 · Lesson 2 of 5 — 对……好／不好 · 从小就 · 总是

Source: docs/lesson-plans/y9-l11/02-dui-congxiao-mixed.md
Textbook pp.100 (rest of Text 1), 103-104 (Act. 4, 6, 7);
workbook pp.118-119, 121 (Ex. 2, 3, 4, 9).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_listening, s_title, s_lisc, s_errors,
                   s_text, label)

SLUG = "l2-dui-congxiao"
TITLE = "Y9 L11 · 对……不好 · 从小就 · Lesson 2 of 5"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 对牙齿不好", "LESSON 2 OF 5", "第十一课 · 零食",
        s_title("对牙齿不好", "What's good for you — and what isn't",
                "Year 9 · Unit 4 · Lesson 11 · Lesson 2 of 5 · 50 minutes",
                "轻松学中文 3 · pp.100, 103–104"))

    add("02-review.html", "Review · Bingo + body parts", "0–8 MIN · REVIEW",
        "复习 · Lesson 1",
        s_task("复习 · 宾果 Bingo · 5 分钟 · 老师只说中文，不说英文、不说拼音",
               ["画一个 <b>3×3</b> 的格子，从下面十二个词里挑九个填进去：",
                "零食 · 巧克力 · 蛋糕 · 冰淇淋 · 饼干 · 糖果 · 薯片 · 薯条 · 炸鸡翅 · 盒饭 · 三明治 · 汽水",
                "先连成一行，再满堂红。然后两个同学各说一句「各种各样……比如……」。",
                "<b>快问快答（练习册 p.119 Ex. 4）</b> · 写汉字：tooth · mouth · tongue · nose · ear"],
               None,
               "这五个部位里，只有一个是今天的新词 —— 其他四个是第一册第五单元的，应该不用想。"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what is good or bad for us, and to talk about things we have liked since we were small.",
               [("I can say 牙齿, 从小, 总是 and 正餐 in Chinese",
                 "能说出「牙齿」「从小」「总是」「正餐」"),
                ("I can say something is good or bad for something else — A 对 B 好／不好",
                 "能用「对……好／不好」说一句"),
                ("I can say what I have liked since childhood — 我从小就……",
                 "能用「我从小就……」介绍自己")]))

    add("04-c1-words.html", "Cycle 1 · A — 牙齿 / 正餐", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("牙齿", "yáchǐ", "tooth; teeth", "yachi"),
                ("正餐", "zhèngcān", "a proper meal", "zhengcan"))
        + '\n  <p class="support" style="margin-top:12pt;">'
          '「牙」和「齿」两个字都是 tooth —— 这个词自己叠了一遍，跟上节课的「各种各样」一样。'
          '「正餐」的「餐」你已经会了：早餐、午餐、晚餐。</p>')
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "他的<b>牙齿</b>很白。", "His teeth are very white."),
                    (None, "我每天都吃三个<b>正餐</b>。", "I eat three proper meals every day."),
                    (None, "我每天吃三个<b>正餐</b>，我的<b>牙齿</b>很好。",
                     "I eat three proper meals a day and my teeth are fine.", True)],
                   "你每天吃几个正餐？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我每天吃 ________ 个正餐。", "我的牙齿 ________ 。"],
                "用「比」写一句，比较正餐和零食。再说你自己一天吃几个正餐、吃几次零食，"
                "最后说妈妈听了会说什么。<b>三句。</b>"))

    add("07-c2-words.html", "Cycle 2 · A — 从小 / 总是", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("从小", "cóngxiǎo", "from childhood", None),
                ("总是", "zǒngshì", "always", None)))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我<b>从小</b>就喜欢吃巧克力。", "I've liked chocolate since I was small."),
                    (None, "我妈妈<b>总是</b>买各种各样的零食。",
                     "My mum is always buying all kinds of snacks."),
                    (None, "我<b>从小</b>就喜欢吃冰淇淋，妈妈<b>总是</b>买给我。",
                     "I've liked ice cream since I was small, and mum always buys it for me.", True)],
                   "「总是」和「常常」，哪一个多？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我从小就喜欢 ________ 。", "我妈妈总是 ________ 。"],
                "三句，<b>不看屏幕</b>：一句用「我从小就……」说一个爱好（<b>不是吃的</b> —— "
                "第二册的音乐、运动都行），一句说你现在做得怎么样，一句用「因为……，所以……」说为什么。"))

    add("10-recall.html", "Checkpoint · 认字 recall", IDO, "检查点 · Checkpoint",
        s_recall(["牙齿", "正餐", "从小", "总是"], "四个词一起读出来。再说一遍上节课的六个。", cols=4))

    add("11-pattern.html", "I Do · 句型 对……好／不好", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · A 对 B 好／不好。 注意：这个「对」不是「你说得对」的对",
                  "A 对 B 好 / 不好。",
                  [("汽水对牙齿不好。", "Soft drinks are bad for your teeth."),
                   ("我们学校的老师都对学生很好。", "The teachers at our school are all good to the students."),
                   ("多吃蔬菜和水果对身体好。", "Eating plenty of vegetables and fruit is good for you.")],
                  "黑板上写两句放在一起：<b>你说得对</b> / <b>对牙齿不好</b> —— 同一个字，两件事。"))

    add("12-pattern2.html", "I Do · 最难的一句", IDO, "句型 · 难句 · two clauses",
        s_focus("再难一点 · 两个分句 · 这就是课文里的那一句",
                "我知道糖果和汽水<b>对牙齿不好</b>，可是我<b>从小就</b>喜欢吃零食。",
                "I know sweets and soft drinks are bad for my teeth, "
                "but I've liked snacks since I was small.",
                "「可是」把两半连起来：前面说你知道什么，后面说你还是这样做。",
                "照这个样子说你自己一件事 —— 我知道……对……不好，可是我从小就…… 不写，直接说。"))

    add("13-ganxingqu.html", "I Do · 对……感兴趣", IDO, "句型 · 对……感兴趣 · 课本 p.103",
        s_pattern("同一个「对」的另一个用法 · 课本 Act. 4",
                  "我对 ____ （非常）感兴趣。 / 我对 ____ 一点儿都不感兴趣。",
                  [("我对中国音乐非常感兴趣。", "I'm very interested in Chinese music."),
                   ("我对足球一点儿都不感兴趣。", "I'm not the least bit interested in football."),
                   ("我们学校的老师都对我很好。", "The teachers at our school are all good to me.")]))

    add("14-text1.html", "课文一 · 后半段 (CD 41)", IDO, "课文一 · Text 1 · p.100",
        s_text("课文一 · 后半段 · 再听一遍 CD 41",
               "我知道糖果和汽水<b>对牙齿不好</b>，可是我<b>从小就</b>喜欢吃零食。"
               "妈妈<b>总是</b>对我说，不要吃太多零食，应该多吃<b>正餐</b>。",
               "1 他知道糖果对什么不好？ · 2 妈妈总是对他说什么？ · 3 他听妈妈的话吗？为什么你这样想？",
               "顺便记住妈妈的两个词：<b>不要</b> + 动词（don't）· <b>应该</b> + 动词（should）。"
               "下节课写翻译的时候要用。"))

    add("15-summary.html", "词汇总览 · summary board", PRAC, "词汇总览 · Summary board",
        s_summary([("牙齿", "yachi"), ("正餐", "zhengcan"), ("从小", None), ("总是", None)],
                  "这块板留在屏幕上 —— 下面四句话，每句要用一个。"))

    add("16-task.html", "We Do · 任务 我从小就…… (Act. 7)", PRAC,
        "任务 · 课本 p.104 · Act. 7",
        s_task("We Do · 写四句介绍你自己 · 一个人写 · 3 分钟",
               ["四句，每句用总览板上的一个词。<b>四句要连起来读成一段话</b>，不是四个不相干的句子。",
                "课本 p.104 的样子：我从小就喜欢吃零食，比如蛋糕、巧克力、薯片、糖果等。"
                "我从小就喜欢喝可乐……我从小就喜欢弹钢琴。我现在钢琴弹得很好，已经考过了五级。",
                "写完的同学做<b>练习册 p.118 Ex. 2</b>：你从小就喜欢吃什么？你从小就喜欢做什么？"],
               "同样四个词，可是写<b>别人</b> —— 你的弟弟、妹妹或者一个朋友。要用「他／她」，"
               "还要加一句「我觉得……」说你的看法。",
               "例：我从小就喜欢吃零食。妈妈总是说吃太多糖对牙齿不好。她说我应该多吃正餐。可是我的牙齿现在还很好。"))

    add("17-act2.html", "You Do · Act. 4 + 练习册 Ex. 9 / Ex. 3", PRAC,
        "活动二 · 课本 p.103 · Act. 4",
        s_task("You Do · 写五句 · 练习本 · 6 分钟",
               ["<b>课本 p.103 Act. 4</b> —— 1 我对 ____ 非常感兴趣。 · 2 多吃糖果对 ____ 不好。 · "
                "3 我们学校的老师都对 ____ 很好。 · 4 我对 ____ 一点儿都不感兴趣。 · 5 ____ 对 ____ 。",
                "<b>练习册 p.121 Ex. 9</b> 第 1–4 题 —— 同样的句型。",
                "<b>练习册 p.119 Ex. 3</b> 的填空 —— 词框里是今天整节课："
                "总是 / 每天 / 最 / 从小 / 各种各样 / 对……好 / 比如 / 正餐。全班一起做也行。"],
               "第五题写<b>三个</b>不同的答案，三个都要是真的，而且不能都说吃的。"
               "写完以后把最有意思的一句读给全班听，全班要用「为什么」问你。"))

    add("18-act3.html", "You Do · 听力 CD 42", PRAC, "活动三 · 课本 p.104 · Act. 6",
        s_listening("You Do · 听力 · CD 42 · 放两遍 · 6 分钟",
               [("她喜欢 ____ 。", "a) 在学校买零食 &nbsp; b) 从市场上买糖果 &nbsp; c) 妈妈做蛋糕"),
                ("她吃 ____ 。", "a) 巧克力和糖果 &nbsp; b) 蛋糕和饼干 &nbsp; c) 糖果和薯片"),
                ("她喝 ____ 。", "a) 水和可乐 &nbsp; b) 汽水 &nbsp; c) 牛奶"),
                ("她从小喜欢吃 ____ 。", "a) 主食 &nbsp; b) 糖果 &nbsp; c) 水果"),
                ("她晚饭 ____ 。", "a) 吃得多 &nbsp; b) 吃得少 &nbsp; c) 不吃"),
                ("她每天有 ____ 。", "a) 四十块零用钱 &nbsp; b) 三十块 &nbsp; c) 三十四块")],
               "对完答案，把第 5 题再放一遍：<b>我早饭吃得多，但是晚饭通常吃得少。</b> "
               "「吃得多 / 吃得少」记下来 —— 下面的活动要用。"))

    add("19-game.html", "Game · 改老师的错 Correct the Teacher", PRAC,
        "游戏 · 改错 · 4 分钟",
        s_errors([("我从小喜欢吃巧克力。", "我从小<b>就</b>喜欢……", "「从小就」是固定说法"),
                  ("我对音乐非常感兴趣的。", "我对音乐非常感兴趣。", "多了一个「的」"),
                  ("吃太多零食对牙齿比不好。", "吃太多零食对牙齿不好。", "这里不用「比」")],
                 "改错 · 黑板上五句，三句是错的 —— 找出来，在白板上写对的",
                 "另外两句是对的：<b>汽水对牙齿很不好。</b> · <b>妈妈总是对我说，应该多吃正餐。</b> "
                 "进阶：让说得好的同学自己出一对句子，还要说出错在哪里。"))

    add("20-plenary.html", "Plenary · exit ticket & preview", "43–50 MIN · PLENARY",
        "小结 · Plenary",
        s_list("小结 · 43–50 分钟",
               [("<b>回看目标</b> · 全班一起读三条，然后问：哪一条最难？", ""),
                ("<b>自评</b> · 白板上写红／黄／绿，三条各一个颜色。", ""),
                ("<b>Exit ticket</b> · 翻译：Eating too much chocolate is bad for your teeth.",
                 "再加一句，用「我从小就……」说你自己。"),
                ("<b>下节课</b> · 不说零食了，说早饭 —— 谷类早餐、面包、煎蛋、香肠。", "")]))
    return S
