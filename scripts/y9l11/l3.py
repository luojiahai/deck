# -*- coding: utf-8 -*-
"""Y9 L11 · Lesson 3 of 5 — breakfast, Text 2 first half, 加

Source: docs/lesson-plans/y9-l11/03-breakfast-text2-mixed.md
Textbook pp.105-106 (Text 2, New Words, Act. 8); workbook pp.121, 123 (Ex. 8, 12).
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_title, s_lisc, s_dialogue, label)

SLUG = "l3-breakfast"
TITLE = "Y9 L11 · 早饭 Breakfast · Lesson 3 of 5"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 你早饭吃什么？", "LESSON 3 OF 5", "第十一课 · 零食",
        s_title("你早饭吃什么？", "Breakfast",
                "Year 9 · Unit 4 · Lesson 11 · Lesson 3 of 5 · 50 minutes",
                "轻松学中文 3 · pp.105–106 · 课文二"))

    add("02-review.html", "Review · L2 对 / 从小就 / 总是", "0–8 MIN · REVIEW",
        "复习 · Lesson 2",
        s_task("复习 · 同桌对话（3 分钟）+ 白板五题（4 分钟）",
               ["<b>同桌对话，不看书：</b>A 问 <b>你从小就喜欢吃什么？</b> 和 "
                "<b>为什么妈妈说你应该多吃正餐？</b> B 各答两句，然后交换。",
                "<b>白板五题：</b>写「牙齿」 · 翻译 Soft drinks are bad for your teeth. · "
                "用「总是」说一句关于你妈妈的话 · 「我对足球一点儿都不感兴趣」是什么意思？ · "
                "「从小」后面要加哪个字？"],
               None,
               "接上：妈妈说应该多吃正餐。正餐里最重要的是哪一餐？<b>早饭。</b>"))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say what we eat for breakfast and to add one thing to another in Chinese.",
               [("I can name six breakfast foods in Chinese",
                 "能说出「谷类早餐」「牛奶」「面包」「煎蛋」「香肠」"),
                ("I can use 加 to combine two things — 谷类早餐加牛奶",
                 "能用「加」把两样东西放在一起说"),
                ("I can answer 你早饭吃什么？ with two or three sentences",
                 "能用中文回答「你早饭吃什么？」")]))

    add("04-c1-words.html", "Cycle 1 · A — 谷类 / 牛奶", IDO, "生词 1 · Cycle 1 of 3",
        s_words(("谷类", "gǔlèi", "cereal", "gulei"),
                ("牛奶", "niúnǎi", "milk", "niunai")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我早饭常常吃<b>谷类</b>早餐。", "I often have cereal for breakfast."),
                    (None, "我每天都喝一杯<b>牛奶</b>。", "I drink a glass of milk every day."),
                    (None, "我早饭吃<b>谷类</b>早餐，喝<b>牛奶</b>。",
                     "For breakfast I have cereal and milk.", True)],
                   "牛奶是吃还是喝？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我早饭吃 ________ 。", "我每天喝 ________ 。"],
                "用「比」写一句，比较牛奶和汽水，说哪个对身体好。"
                "再用「妈妈总是对我说……」加一句。"))

    add("07-c2-words.html", "Cycle 2 · A — 面包 / 煎蛋", IDO, "生词 2 · Cycle 2 of 3",
        s_words(("面包", "miànbāo", "bread", "mianbao"),
                ("煎蛋", "jiāndàn", "fried egg", "jiandan")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "我妈妈每天早上做<b>面包</b>。", "My mum makes bread every morning."),
                    (None, "我不太喜欢吃<b>煎蛋</b>。", "I don't much like fried eggs."),
                    (None, "今天早饭我吃了<b>面包</b>和<b>煎蛋</b>。",
                     "This morning I had bread and a fried egg.", True)],
                   "你今天早饭吃了什么？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["今天早饭我吃了 ________ 。", "我不太喜欢吃 ________ 。"],
                "写三句说你昨天的早饭，可是<b>「吃」不能用两次以上</b> —— 用「喝」「有」换一换。"
                "最后一句用「因为……，所以……」说你为什么吃那个。"))

    add("10-c3-words.html", "Cycle 3 · A — 香肠 / 加", IDO, "生词 3 · Cycle 3 of 3",
        s_words(("香肠", "xiāngcháng", "sausage", "xiangchang"),
                ("加", "jiā", "add; plus", None)))
    add("11-c3-examples.html", "Cycle 3 · B — 例句", IDO, "例句 3 · See them used",
        s_examples([(None, "我早饭喜欢吃<b>香肠</b>。", "I like sausages for breakfast."),
                    (None, "我的茶里要<b>加</b>牛奶。", "I want milk in my tea."),
                    (None, "我早饭吃谷类早餐<b>加</b>牛奶，还有<b>香肠</b>。",
                     "For breakfast I have cereal with milk, and sausages too.", True)],
                   "你的茶里要不要加牛奶和糖？"))
    add("12-c3-write.html", "Cycle 3 · C — 写一句", IDO, "写一句 3 · Write your own",
        s_write(["我的茶里要加 ________ 。", "________ 加 ________ 。"],
                "用「加」写两句，一句说吃的，一句说喝的。再写一句问同桌："
                "<b>你的茶里要不要加牛奶和糖？</b> 然后真的去问他，把答案写下来。"))

    add("13-recall.html", "Checkpoint · 认字 recall", IDO, "检查点 · Checkpoint",
        s_recall(["谷类", "牛奶", "面包", "煎蛋", "香肠", "加"],
                 "六个字一起读。读不出来的，我们回到第二个循环再教一遍。"))

    add("14-components.html", "I Do · 部件 煎 vs 炸", IDO, "汉字 · Character components",
        label("看部件 · 二十秒 · 这几个字都在告诉你它是什么")
        + '  <div class="stack gap-md">\n'
          '    <div class="sc-row"><p class="sc-num">奶</p><div><p class="sc-main">'
          '左边是 <b>女</b> —— 奶是给孩子的。</p></div></div>\n'
          '    <div class="sc-row"><p class="sc-num">肠</p><div><p class="sc-main">'
          '左边是 <b>月</b>（肉）—— 跟第十课的「翅膀」一样，是身体、是肉做的。</p></div></div>\n'
          '    <div class="sc-row"><p class="sc-num">煎</p><div><p class="sc-main">'
          '下面是 <b>灬</b>，四点是火。<b>煎</b>用一点点油，<b>炸</b>（第十课）用很多油。</p>'
          '<p class="sc-cn">煎蛋 · 炸鸡翅 —— 两个字放在一起看</p></div></div>\n'
          '  </div>\n'
        + '  <p class="support" style="margin-top:12pt;">'
          '快问：「香肠」的「肠」是什么部首？</p>')

    add("15-pattern.html", "I Do · 句型 A 加 B", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · A 加 B —— 把两样东西放在一起",
                  "A 加 B",
                  [("谷类早餐加牛奶", "cereal with milk"),
                   ("茶里加牛奶和糖", "tea with milk and sugar"),
                   ("我早饭吃谷类早餐加牛奶。", "For breakfast I have cereal with milk.")],
                  "「加」不是「和」。「和」是两样并排，「加」是一样<b>放进</b>另一样里。"))

    add("16-pattern2.html", "I Do · 一个好回答长什么样", IDO, "句型 · 难句 · 一般 vs 有时候",
        s_focus("最难的一句 · 这就是课文里的回答",
                "我早饭<b>一般</b>吃谷类早餐<b>加</b>牛奶，<b>有时候</b>吃面包、煎蛋和香肠。",
                "For breakfast I usually have cereal with milk; sometimes I have bread, "
                "a fried egg and sausages.",
                "<b>一个好回答的形状：</b>先说平常怎么样（一般／平时／通常），再说例外（有时候）。"
                "这两个词第十课就学过了 —— 今天把它们用进早饭里。",
                "照这个形状说午饭，再说晚饭。两句都要有「一般」和「有时候」。不写，直接说。"))

    add("17-text2.html", "课文二 · 上半段 (CD 43)", IDO, "课文二 · Text 2 · p.105",
        s_dialogue("课文二 · 先整段听一遍（CD 43），今天只做第一问",
                   [("A", "你早饭吃什么？"),
                    ("B", "吃<b>谷类</b>早餐<b>加牛奶</b>，有时候吃<b>面包</b>、<b>煎蛋</b>和<b>香肠</b>。")],
                   "一起读 → 同桌读两遍（换角色）→ 合上书，背出来。"
                   "问：1 他早饭一般吃什么？ 2 他有时候吃什么？ 3 他早饭喝什么？"))

    add("18-summary.html", "词汇总览 · summary board", PRAC, "词汇总览 · Summary board",
        s_summary([("谷类", "gulei"), ("牛奶", "niunai"), ("面包", "mianbao"),
                   ("煎蛋", "jiandan"), ("香肠", "xiangchang"), ("加", None)],
                  "这块板留在屏幕上 —— 下面的早饭表要用到每一个词。"))

    add("19-task.html", "We Do · 任务 三天的早饭表", PRAC, "任务 · 三天早饭表",
        s_task("We Do · 一个人写 · 4 分钟",
               ["写<b>星期一、星期二、星期三</b>三天的早饭。",
                "三天加起来要用到总览板上<b>每一个</b>词，而且至少有一天要用「加」。",
                "写完用一句话说哪一天的早饭最好，为什么。"],
               "不写表，写<b>一段话</b>。四到六句，三天都说到，每句都要连起来"
               "（用「星期一……，星期二……，可是星期三……」）。最后一句用「因为……，所以……」"
               "说哪一天的早饭对身体最好。<b>不看总览板。</b>",
               "星期一：谷类早餐加牛奶。 星期二：面包、煎蛋和香肠。 星期三：……"))

    add("20-act8.html", "You Do · 课本 Act. 8 picture talk", PRAC,
        "活动二 · 课本 p.106 · Act. 8",
        s_task("You Do · 十四张图，每张两句 · 两人轮流 · 7 分钟",
               ["课本 p.106 的样子：<b>我喜欢吃薯条。我每天都吃薯条。</b>",
                "第二句不要每次都一样 —— 换成 我不太喜欢…… / 我妈妈常常做…… / 这个对牙齿不好。",
                "图里的 <b>沙拉</b> 和 <b>酸奶</b> 是下节课的词。碰到就说"
                "<b>我不知道这个中文怎么说</b>，跳过去 —— 今天不教。"],
               "不是两句，是一个小对话：A 问一个问题（你喜欢吃……吗？为什么？），"
               "B 答两句，第二句一定要用「因为……，所以……」或者「对……好／不好」。"
               "十四张全部做完，中间不能停下来看屏幕。"))

    add("21-act3.html", "You Do · 练习册 Ex. 12 + Ex. 8", PRAC,
        "活动三 · 练习册 pp.123, 121",
        s_task("You Do · 先写图，再写翻译 · 5 分钟",
               ["<b>练习册 p.123 Ex. 12</b> 第 1–8 题（「面条」已给）—— 写汉字，不写拼音。"
                "老师看着「煎」和「肠」的笔顺，这两个字又新又密。",
                "<b>练习册 p.121 Ex. 8</b> 只做第 1、2、4 题 —— 三句说吃的：",
                "1 Do not eat fast food too often. · 2 You should eat more fruit. · "
                "4 You should eat less meat and more vegetables.",
                "<b>不要</b> 和 <b>应该</b> 是上节课课文里妈妈说的话 —— 今天真正写出来。"],
               "图写完以后，把八样东西分成两组：<b>早饭吃的 / 早饭不吃的</b>，"
               "每组下面写一句话说为什么。翻译题做全部六句，包括第三、五、六句"
               "（天气、暑假、爷爷奶奶）—— 那三句不是说吃的，要用第二册的词。"))

    add("22-game.html", "Game · 跑动听写 Running Dictation", PRAC,
        "游戏 · 跑动听写 · 5 分钟",
        s_task("Game · 跑动听写 Running Dictation",
               ["四句话贴在教室四面墙上。两人一组：一个跑去读，一个写。两句以后交换。",
                "<b>1</b> 我早饭吃谷类早餐加牛奶。 &nbsp; <b>2</b> 有时候我吃面包、煎蛋和香肠。",
                "<b>3</b> 我的茶里要加牛奶，不要加糖。 &nbsp; <b>4</b> 妈妈说早饭对身体很好。",
                "四句全对最快的一组赢。<b>全对＝写汉字</b>，写拼音不算。"],
               "跑的人<b>不能说中文</b> —— 他要把句子翻成英文说给写的人听，"
               "写的人再把它写回中文。不许回头看。"))

    add("23-plenary.html", "Plenary · exit ticket & preview", "43–50 MIN · PLENARY",
        "小结 · Plenary",
        s_list("小结 · 43–50 分钟",
               [("<b>回看目标</b> · 请一位同学读，然后全班一起用中文答一次「你早饭吃什么？」", ""),
                ("<b>自评</b> · 三条各举手一次 👍 / 😐 / 👎。", ""),
                ("<b>Exit ticket</b> · 用「加」写一句：你早饭吃什么、喝什么。", ""),
                ("<b>下节课</b> · 午饭和晚饭 —— 沙拉、酸奶、杂菜汤，"
                 "还要去问四个同学他们家吃什么。", "")]))
    return S
