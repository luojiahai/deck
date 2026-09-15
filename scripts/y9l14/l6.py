# -*- coding: utf-8 -*-
"""Y9 L14 · Lesson 6 of 6 — 身份证 / 学生证 / 借书证 + complement of result

Source: docs/lesson-plans/y9-l14/06-lost-property-result-mixed.md
Textbook p.139 Act. 8, p.140 Act. 10, p.141 Act. 12. Workbook p.161 Ex. 18,
p.162 Ex. 19, Ex. 22, p.163 Ex. 23.

Three new words is 2 + 1, so cycle 2 uses s_word_one. All three end in 证,
so they teach as one pattern rather than as three words.

Last lesson of the sequence: the plenary looks back over all six learning
intentions, not just today's — there is no review lesson after this one.
"""
from build import (s_words, s_word_one, s_examples, s_write, s_recall,
                   s_summary, s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_errors, s_title, s_lisc, label)

SLUG = "l6-lost-property"
TITLE = "Y9 L14 · 问路 Asking the Way · Lesson 6 of 6"
CARD = (SLUG, "找到了吗", "Lost Property · 结果补语",
        "grammar", "身份证 · 学生证 · 借书证，加结果补语：找<b>到</b>、吃<b>完</b>、"
                   "借<b>走</b>。「找」是做，「找到」是做成了。")

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 找到了吗", "LESSON 6 OF 6", "第十四课 · 问路",
        s_title("找到了吗", "Lost Property",
                "Year 9 · Book 3 · Unit 5 · Lesson 14 · 50 minutes",
                "轻松学中文 3 · p.139–141 · 第 8、10、12 题"))

    add("02-review.html", "Review · 改错 · 被字句", REV, "复习 · Lesson 5",
        s_errors([("我的自行车被哥哥骑。", "我的自行车被哥哥骑走了。",
                   "动词后面少了结果"),
                  ("被弟弟蛋糕吃完了。", "蛋糕被弟弟吃完了。", "东西要放最前面"),
                  ("我的书被同学借。", "我的书被同学借走了。", "同样——少了结果")],
                 "第 1 句和第 3 句坏在<b>同一个地方</b>：动词站在那儿没有结果。"
                 "少的那个字，就是今天要学的东西。"
                 "接着两分钟做练习册 p.162 第 22 题（二十个动词，限时），"
                 "改错 · 少的那个字，就是今天的语法",
                 "再两分钟口头做课本 p.141 第 12 题的购物问题。"
))

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("say whether an action reached its result — "
               "found it or didn't, finished it or didn't.",
               [("I can attach a result to a verb", "能给动词加结果：找到、吃完、借走、听见"),
                ("I can say what I could not do", "能说做不成：我没有找到 ／ 我找不到"),
                ("I can report something missing at a service desk",
                 "能在服务台说丢了什么，回答里边有什么")]))

    # ── Cycle 1 · 身份证 / 学生证 ──
    add("04-c1-words.html", "Cycle 1 · A — 身份证 / 学生证", IDO,
        "生词 1 · Cycle 1 of 2",
        s_words(("身份证", "shēnfènzhèng", "identity card", "shenfenzheng"),
                ("学生证", "xuéshēngzhèng", "student card", "xueshengzheng")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "我的<b>身份证</b>在钱包里。", "My ID card's in my wallet."),
                    (None, "学校给我们每个人一张<b>学生证</b>。",
                     "School gives each of us a student card."),
                    (None, "我的钱包里有<b>身份证</b>和<b>学生证</b>。",
                     "My wallet has my ID card and my student card in it.", True)],
                   "三个词都是「证」结尾——「证」是什么意思？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我的 ________ 在 ________ 里。", "我有一张 ________ 。"],
                "用「可以」写三句，说每一张证能做什么："
                "<b>用学生证可以买便宜的车票。</b>"
                "再说哪一张你最不想丢，为什么。"))

    # ── Cycle 2 · 借书证 (single) ──
    add("07-c2-word.html", "Cycle 2 · A — 借书证", IDO, "生词 2 · Cycle 2 of 2",
        s_word_one(("借书证", "jièshūzhèng", "library card", "jieshuzheng")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "用<b>借书证</b>可以借书。",
                     "You can borrow books with a library card."),
                    (None, "图书馆的<b>借书证</b>是绿色的。",
                     "The library card is green."),
                    (None, "我的<b>借书证</b>、学生证和身份证都被偷了。",
                     "My library card, student card and ID card were all stolen.",
                     True)],
                   "「借」这个字，十分钟以后还会再见——借<b>走</b>了。"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我的借书证 ________ 。"],
                "用「除了……以外，还有……」一句话说完被偷的钱包里所有东西——"
                "三张证和现金都要有。再说一句：你会先报哪一张？为什么？"))

    add("10-recall.html", "Recall · 三个生词 + 上节课五个", IDO, "认一认 · Checkpoint",
        s_recall(["身份证", "学生证", "借书证", "偷", "警察", "被", "留", "姓名"],
                 "前三个是今天的。后五个是昨天的——不看拼音，一起读。", cols=4))

    # ── Pattern ──
    add("11-pattern.html", "Pattern · 结果补语", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 做了，还是做成了？",
                  "动词 + 结果（+ 了）· 找到 · 吃完 · 借走 · 听见",
                  [("我<b>找到</b>我的手机了。", "I found my phone. (and I have it)"),
                   ("我的自行车被哥哥<b>骑走</b>了。",
                    "My bike was ridden off by my brother."),
                   ("钱都<b>花完</b>了。", "The money's all spent.")],
                  "「我找了」＝ 我找了很久，可是不知道找着没有。"
                  "「我找<b>到</b>了」＝ 东西在我手里。"))
    add("12-negative.html", "没有找到 · 还是 · 找不到？", IDO, "注意 · 否定最容易错",
        s_errors([("我找我的钱包到了。", "我找到我的钱包了。", "结果紧跟动词，中间不插东西"),
                  ("我不找到。", "我没有找到。", "已经发生的事，用「没有」"),
                  ("我没有找到。", "我找不到。",
                   "两句都对，意思不一样：找过了没找着 ／ 现在<b>怎么也</b>找不着")],
                 "否定 · 没有找到 / 找不到",
                 "第三行不是改错——是两个都对。测验的翻译题两种都考。"
))
    add("13-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 先没找到，后来找到了",
                "我找了三次都没有找到，后来老师在体育馆门口找到了我的书包。",
                "I looked three times and didn't find it; later the teacher "
                "found my school bag by the gym door.",
                "同一个「找到」，前半句否定，后半句肯定。"
                "两个分句，还带了地点——这一句能说对，语法就过关了。"))

    add("14-cfu.html", "CFU · 检查理解", IDO, "检查理解 · CFU",
        s_cfu([("白板：写 —— I finished my homework.", "用「完」"),
               ("「找」跟「找到」有什么不一样？", "用手比一比：一个是做，一个是做成了"),
               ("这句哪里错了？ 我找我的钱包到了。", "找出来，改过来"),
               ("白板：写 —— I looked for it three times but didn't find it.",
                "两个分句")]))

    # ── Flexible practice ──
    add("15-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · Summary board",
        s_summary([("身份证", "shenfenzheng"), ("学生证", "xueshengzheng"),
                   ("借书证", "jieshuzheng"), ("手提包", "shoutibao"),
                   ("钱包", "qianbao"), ("钥匙", "yaoshi"),
                   ("手机", "shouji"), ("现金", "xianjin")],
                  "这块板整个活动都留在屏幕上——写失物招领的时候可以看。"))
    add("16-task.html", "Activity 1 · 失物招领", PRAC, "活动一 · We Do · 6 分钟",
        s_task("活动一 · 先填表，再在本子上写四句",
               ["表格：姓名 ／ 电话 ／ 丢了什么 ／ 在哪儿丢的 ／ 里边有什么",
                "四句话里<b>一定要有</b>：三张证 · 至少一个「被」字句 · "
                "至少一个结果补语。",
                "念的时候，全班听见结果补语就举手。样子："],
               "写成<b>告示</b>，不是故事——第三人称，不用「我」，"
               "最后加一句告诉捡到的人怎么办：<b>如果你找到了，请打电话给……</b>"
               "再加一句谢礼。（这就是练习册 p.160 第 16 题的格式。）",
               cn="昨天我的手提包在服装店被偷了。包里有钱包、钥匙和手机。"
                  "钱包里有身份证、学生证和借书证。我找了很久，可是没有找到。"))
    add("17-paper.html", "Activity 2 · 结果补语 · 笔头", PRAC,
        "活动二 · You Do · 8 分钟 · 本子上",
        s_list("活动二 · 按顺序做 · 老师走动批改",
               [("课本 p.139 第 8 题 · 八句填结果补语，再自己写两句", "4 分钟"),
                ("练习册 p.161 第 18 题 · 八句翻译成<b>英文</b>",
                 "测验考的就是这个方向，平常练得最少"),
                ("写完的做练习册 p.162 第 19 题 · 三张图各写一段对话",
                 "写完等一下角色扮演就有自己的台词")],
               "直接跳去练习册 p.163 第 23 题——读小偷那一篇，"
               "然后写 80–100 字丢包的经过。里面至少两个「被」字句、"
               "三个<b>不一样</b>的结果补语。做到这题比做完第 18 题更值。"))
    add("18-roleplay.html", "Game · 服务台 · Role-play Cards", PRAC, "游戏 · 9 分钟",
        s_task("游戏 · 课本 p.140 第 10 题 · 两人一组，卡片扣着，三个情况轮着来",
               ["<b>丢了手机 · 丢了钱包 · 丢了书包</b>",
                "A 在服务台，要<b>按顺序</b>问清楚五件事：",
                "　你丢了什么？ 什么时候丢的？ 在哪儿丢的？ 里边有什么？ 请留下姓名和电话。",
                "B 拿活动一写的表格回答。每演完一个情况就换角色。"],
               "给流利的同学：服务台说东西<b>已经有人送来了</b>——"
               "可是要先确认是不是他的，得问他里边有什么才给看："
               "<b>你说说包里有什么，我看看对不对。</b>"
               "认领的人<b>不看表格</b>凭记忆说。两边对不上，服务台就不给。"))

    add("19-plenary.html", "Plenary · 回看这六节课", PLEN,
        "小结 · Plenary · 看整个单元",
        s_task("小结 · 43–50 分钟 · <b>这一次回看的是六节课，不只是今天</b>",
               ["<b>回看目标</b> · 先读今天的三条，然后屏幕换成六节课的六个学习目标。",
                "<b>自评</b> · 对<b>六个</b>目标一个一个举手，不只是今天的。",
                "　　要盯的是第 2 节（坐几路车）和第 5 节（被）——"
                "测验里分量最重，举手弱就下节课开头补五分钟。",
                "<b>出门条</b> · 一张纸条，走的时候交。",
                "<b>下一课</b> · 第十五课——邻居。你家楼上的邻居半夜还开着电视，很响。"
                "你怎么办？"],
               cn="出门条：写两句 —— 第一句用「被」，第二句用一个结果补语"
                  "（找到／吃完／借走／听见）。<b>两句要说同一件事。</b>"))

    return S
