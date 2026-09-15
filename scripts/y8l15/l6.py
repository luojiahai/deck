# -*- coding: utf-8 -*-
"""Y8 L15 · Lesson 6 of 6 — the whole neighbourhood

Source: docs/lesson-plans/y8-l15/06-my-neighbourhood-mixed.md
Textbook p.145 Act. 4 (the eight-question interview, run as the Review),
p.146 Act. 6 (town map), p.149 Act. 10 (the recognition bank), p.151
Act. 12 (information desk), p.153 Act. 16 (dream city). Workbook
pp.170–173.

No new sentence pattern, on purpose, and the deck says so on a slide of
its own: the work is running all five patterns at once. The four new
words are the recognition set from p.143's answer bank, and all four are
「你已经会的字 + 店」 — which is why they fit in a lesson whose real
content is the map and the directions.

This lesson closes the sequence, so the plenary looks back over all six
learning intentions rather than only today's three.

The radical slot runs as this lesson's game, exactly as it does in
y8l14's Lesson 6: the series was built without radicals on instruction,
the cost was stated (Unit 5 Test parts 3 and 4 would be met cold), and
the teacher then asked for a slot. Three slides — p.147 Ex. 9's four
simple characters, then the two test formats — and they are task boards,
not answer boards.

Three of Test part 4's six compounds hide a character this very lesson
sequence teaches: 返 holds 反, 蚂 holds 马 (Lesson 3's 马路), 仙 holds 山.
That is why the slot belongs in THIS deck rather than only in y8l14's.

Those three pairings stay here, in teacher-facing source. The board tells
students that three of the six hide a character they learned this week
and points them back a page — it does not name the pairs. Writing them
onto the slide would make it an answer board, which is the one thing this
series does not have.

Fitting it cost four minutes across the other three activities rather
than cutting one of them: the map talk drops 6→5, the information desk
9→8, the dream city 8→5. All four textbook activities survive.
"""
from build import (s_words, s_examples, s_write, s_recall, s_summary,
                   s_pattern, s_focus, s_task, s_list, s_cfu,
                   s_figure, s_text, s_errors, s_chars, s_radicals,
                   s_title, s_lisc)

SLUG = "l6-my-neighbourhood"
TITLE = "Y8 L15 · 社区 Neighbourhood · Lesson 6 of 6"

REV = "0–8 MIN · REVIEW"
IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"

CARD = dict(cn='我们的社区', en='My whole neighbourhood',
            desc='Four more shops, all of them a known character plus 店 — and then the real work: a map, five patterns running at once, a stranger at the information desk, and the unit\u2019s one radical slot, run as the lesson\u2019s game.',
            words='水果店 · 书店 · 理发店 · 快餐店', n=4)


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 我们的社区 My whole neighbourhood", "LESSON 6 OF 6",
        "第十五课 · 社区",
        s_title("我们的社区", "My Whole Neighbourhood",
                "Year 8 · Book 2 · Unit 5 · Lesson 15 · 50 minutes",
                "轻松学中文 2 · p.145–146, p.151, p.153"))

    add("02-review.html", "Review · p.145 Act. 4 — the eight-question interview", REV,
        "复习 · 课本 p.145 第四题",
        s_list("复习 · 站起来，两人一组，八个问题",
               [("你家附近有什么？", "用「等」"),
                ("你家离学校远吗？", "用「挺……的」或者「不远」"),
                ("你家离超市远不远？走路要多长时间？", "用「离」和「大约」"),
                ("从你家怎么去电影院？", "用「先……，然后……」"),
                ("火车站在哪儿？", "用「就在……对面」"),
                ("你家的房子有几层？你的房间里有什么？", "第十三课和第十四课")],
               "A 问完八题换 B。老师一边走一边听两件事："
               "「离」后面有没有东西，「就」有没有跑到动词后面去。", compact=True))
    add("03-review-bridge.html", "Review · what you just did", REV, "复习 · 你刚才做的是什么",
        s_focus("刚才那八个问题，就是单元测验的口语部分",
                "而且你是<b>背着</b>做完的。",
                "That interview is the speaking half of the unit test, and you just "
                "did it from memory.",
                "今天先加最后四个店，然后把整个社区放到一张地图上。"))

    add("04-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("describe a whole neighbourhood and tell someone how to get around it.",
               [("I can name four more shops", "再多说四个商店的名字"),
                ("I can describe a map using 附近、离、就、对面",
                 "会用「附近」「离」「就」「对面」描述一张地图"),
                ("I can tell a visitor how to reach a place, and how long it takes",
                 "会告诉别人怎么去，还要说多久")]))

    # ── Cycle 1 · 水果店 / 书店 ──
    add("05-c1-words.html", "Cycle 1 · A — 水果店 / 书店", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("水果店", "shuǐguǒdiàn", "fruit shop", "shuiguodian"),
                ("书店（書店）", "shūdiàn", "bookshop", "shudian")))
    add("06-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([("<b>水果店</b>里有苹果和香蕉。",
                     "There are apples and bananas in the fruit shop."),
                    ("我常常去<b>书店</b>买书。", "I often go to the bookshop to buy books."),
                    ("<b>书店</b>就在<b>水果店</b>对面。",
                     "The bookshop is right opposite the fruit shop.", True)],
                   "今天四个词的最后一个字都一样——是哪个字？"))
    add("07-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["________ 就在 ________ 对面。"],
                "两句连起来：先摆位置，再说你更常去哪一个，还要说为什么。"
                "<b>书店就在水果店对面。因为我很喜欢看书，所以我常常去书店，"
                "可是妈妈天天去水果店买苹果。</b>"))

    # ── Cycle 2 · 理发店 / 快餐店 ──
    add("08-c2-words.html", "Cycle 2 · A — 理发店 / 快餐店", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("理发店（理髮店）", "lǐfàdiàn", "hairdresser's", "lifadian"),
                ("快餐店", "kuàicāndiàn", "fast-food shop", "kuaicandian")))
    add("09-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([("<b>理发店</b>在花店右面。",
                     "The hairdresser's is to the right of the flower shop."),
                    ("我们常常去<b>快餐店</b>吃饭。",
                     "We often eat at the fast-food shop."),
                    ("<b>理发店</b>和<b>快餐店</b>都在马路对面。",
                     "Both the hairdresser's and the fast-food shop are across the road.",
                     True)],
                   "「快餐」＝ 快 + 餐。两个字你都会了。"))
    add("10-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["我家附近有 ________ 和 ________ 。"],
                "今天四个店<b>全部</b>放进一句，用「等」收尾；再写第二句，"
                "说哪一个最远、你怎么去："
                "<b>我家附近有水果店、书店、理发店、快餐店等。理发店最远，"
                "我要先走路，然后坐五路公共汽车，大约十五分钟。</b>"))

    add("11-extra.html", "Recognition only · p.149 Act. 10's answer bank", IDO,
        "只认不写 · Recognition only",
        s_recall(["医院", "公园", "地铁站", "加油站", "玩具店"],
                 "这五个词<b>只认，不写</b>——课本 p.149 第十题的选项里有它们。"
                 "一起读一遍，认得出来就够了。", cols=5))
    add("12-recall.html", "Recall · today's four, no pinyin", IDO, "认一认 · checkpoint",
        s_recall(["水果店", "书店", "理发店", "快餐店"],
                 "读不出来就停下来重教——不要往下走。", cols=4))

    # ── No new pattern; run all of them ──
    add("13-nopattern.html", "Today there is no new pattern", IDO, "句型 · 今天没有新句型",
        s_focus("今天没有新句型",
                "今天的活儿，是把前面五课的句型<b>一起</b>用出来。",
                "No new pattern today. The job is running all of them at once.",
                "下一页老师在黑板上一句一句搭出来，每搭一句就说出它是哪一课的。"))
    add("14-pattern.html", "Pattern · the five, in one paragraph", IDO,
        "句型 · 五个句型，一段话",
        s_pattern("句型 · 老师在黑板上一句一句搭",
                  "附近有…等　·　离…远／近　·　就在…对面　·　挺…的　·　先…然后…",
                  [("我家<b>附近有</b>水果店、书店、快餐店<b>等</b>。",
                    "第一课"),
                   ("超市<b>离</b>我家不远，走路五分钟<b>就</b>到了。"
                    "书店<b>就在</b>马路<b>对面</b>。",
                    "第二课 + 第三课"),
                   ("我<b>先</b>坐船，<b>然后</b>坐公共汽车，<b>大约</b>二十分钟。",
                    "第四课 + 第五课")],
                  "搭完擦掉，只留结构的名字——全班照着名字重说一遍。"))

    add("15-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("水果店里卖什么？用中文说三样。", "苹果、香蕉、橘子……"),
               ("翻译：<i>The bookshop is right across the road.</i>",
                "小白板：书店就在马路对面。"),
               ("我说五句，错的那一句大拇指朝下。",
                "我家离超市很近。／书店在就马路对面。／大约二十分钟。／"
                "我先走路，然后坐船。／理发店在花店右面。"),
               ("用「等」说一句，里面要有<b>四个</b>店。三十秒。", "写在小白板上")]))

    # ── Practice ──
    add("16-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("水果店", "shuiguodian"), ("书店", "shudian"),
                   ("理发店", "lifadian"), ("快餐店", "kuaicandian")],
                  "这一页留在屏幕上——后面三个活动都看它。"))

    add("17-act1.html", "Activity 1 · Read the map (We Do, 5 min)", PRAC,
        "活动一 · 5 分钟",
        s_figure("ditu", "活动一 · 看地图，轮着说",
                 ["<b>三人一组</b>，每组一张 A3 地图，屏幕上是同一张。",
                  "轮流说，一人一句——<b>句型不能重复</b>。",
                  "所以一组要凑齐：附近有……等 / 离……远近 / 就在……对面 / "
                  "挺……的 / 先……，然后……。每组至少六句。",
                  "然后全班：老师指一个店，全班齐声答<b>那是什么店？</b>"],
                 cn="超市离学校很近，走路三分钟就到了。"))
    add("18-act1-ext.html", "Activity 1 · Extension", PRAC, "活动一 · Extension",
        s_task("活动一 · 加难 · 关掉投影",
               ["投影关掉，地图扣过来，三个人<b>凭记忆</b>把地图说出来。",
                "一个人负责<b>记下</b>另外两个人说的。",
                "说完再翻开地图核对，错的地方要<b>用中文</b>自己改。"],
               cn="不对，理发店不在书店对面，在书店右面。"))

    add("19-act2.html", "Activity 2 · The information desk (You Do, 8 min)", PRAC,
        "活动二 · 8 分钟",
        s_figure("zhilu", "活动二 · 火车站的问讯处 · 课本 p.151 第十二题",
                 ["两人一组，用那张 A3 地图。一个坐<b>问讯处</b>，一个是<b>刚下车的客人</b>。",
                  "客人要问<b>五个</b>地方，每个地方都要问到三件事：",
                  "① 在哪儿？　② 怎么去？　③ 要多长时间？",
                  "四分钟换角色。"],
                 cn="请问，电影院在哪儿？　—— 电影院就在马路对面。<br>"
                    "从这儿怎么去超市？　—— 你先走路，然后坐五路公共汽车。<br>"
                    "要多长时间？　—— 大约十五分钟。"))
    add("20-act2-ext.html", "Activity 2 · Extension", PRAC, "活动二 · Extension",
        s_task("活动二 · 加难 · 客人很难伺候",
               ["客人拖着一个很重的箱子——<b>不能走路</b>。",
                "客人<b>只有二十分钟</b>，火车就要开了。",
                "客人要在开车前去<b>两个</b>地方。",
                "问讯处要<b>安排顺序</b>，还要说出为什么这么排。客人<b>看不到地图</b>。"],
               cn="你先去水果店，因为它很近，然后去书店，书店就在对面，"
                  "大约二十分钟就够了。"))

    add("21-act3.html", "Activity 3 · Dream city — gallery walk (5 min)", PRAC,
        "活动三 · 5 分钟 · 课本 p.153 第十六题",
        s_list("活动三 · 画你梦想中的城市",
               [("两人一组，一张 A3。两分半，画至少<b>六个</b>地方，"
                 "全部写汉字，其中至少四个是这六课学过的店。", ""),
                ("下面写<b>两句</b>给一个要来玩的朋友：去哪儿，怎么去。", ""),
                ("全部贴到墙上。九十秒大家走一圈，"
                 "在<b>最想去</b>的那一张旁边打一个勾。", ""),
                ("票最多的两组把他们写的两句念出来。", "")],
               "画得漂亮不算分，写得清楚才算。", compact=True))
    add("22-act3-ext.html", "Activity 3 · Extension", PRAC, "活动三 · Extension",
        s_task("活动三 · 加难 · 写成一封信",
               ["不写两句，写<b>五句</b>，而且要写成一封给朋友的信。",
                "「你好」开头；「附近有……等」「离……挺远的」「先……，然后……」"
                "各至少用一次；最后推荐一个地方，还要说为什么。",
                "这就是练习册那篇社区作文，也是<b>单元测验第十一部分</b>——"
                "现在先写一遍，而且是当众写。"],
               cn="最好的两封留下来，下节课贴出来。"))

    # ── The radical slot · runs as this lesson's game ──
    # Three boards, five minutes, at the teacher's request. See the module
    # docstring for why it lives here and what it cost.
    add("23-chars.html", "Game · step 1 — the four simple characters", PRAC,
        "游戏 · 第一步 · 独体字",
        s_chars([("反", "fǎn", "reverse", "第十五课 p.147"),
                 ("血", "xuè", "blood", "第十五课 p.147"),
                 ("习", "xí", "study", "第十五课 p.147"),
                 ("山", "shān", "mountain", "第十五课 p.147")],
                "独体字 · 课本 p.147 第九题 · 九十秒看一遍",
                "这四个字课本教过，我们一直没碰。现在看九十秒——"
                "下面两轮要用，单元测验也要用。"
                "第十三课的<b>光 金 匕 入</b>、第十四课的<b>井 亡 乌 勺</b>"
                "也一起回忆一下，一共十二个。"))

    add("24-radicals-1.html", "Game · round 1 — write the radical", PRAC,
        "游戏 · 第二步 · 部首抢答",
        s_radicals(["层", "厅", "辆", "冰", "超", "站"],
                   "游戏 · 第一轮 · 写部首 · 四人一组，写在纸上",
                   "每个字的部首是什么？写下来，再写它的意思。九十秒。",
                   bank=["尸", "厂", "车", "冫", "走", "立", "口", "火", "氵"],
                   note="写对最多的一组得分。<b>方格里有三个是多出来的。</b>　"
                        "这六个字就是单元测验第三部分考的，"
                        "而且<b>考试不给方格</b>。"))

    add("25-radicals-2.html", "Game · round 2 — find the simple character", PRAC,
        "游戏 · 第三步 · 找独体字",
        s_radicals(["毕", "忘", "返", "蚂", "仙", "鸣"],
                   "游戏 · 第二轮 · 找里面的独体字 · 同一组，继续写",
                   "每个字里面藏着一个独体字，把它找出来，写下来。九十秒。",
                   note="这一轮<b>没有方格</b>，跟单元测验第四部分一样。"
                        "这六个字里<b>有三个</b>，藏的是你<b>这个星期刚学过的字</b>——"
                        "上一页那四个，还有第三课「马路」的第一个字。"
                        "先回头看一眼，别问老师。两轮加起来分最高的一组赢。"))

    # ── Plenary · the whole sequence ──
    add("26-plenary-all.html", "Plenary · all six lessons", PLEN,
        "小结 · 六课一起回头看",
        s_list("小结 · 这六节课，你学会了什么",
               [("第一课　我家附近有花店、文具店、家具店等", "举一个中文例子"),
                ("第二课　超市离我家不远　·　挺远的", "举一个中文例子"),
                ("第三课　火车站就在马路对面", "举一个中文例子"),
                ("第四课　我先坐船，然后坐公共汽车", "举一个中文例子"),
                ("第五课　要坐多长时间？　—— 大约二十分钟", "举一个中文例子"),
                ("第六课　水果店、书店、理发店、快餐店", "举一个中文例子")],
               "今天不是只看今天的三条——六节课一条一条过。"
               "每一条请一个同学用中文举例，说得出来才算学会。", compact=True))
    add("27-selfassess.html", "Plenary · self-assessment", PLEN, "自评 · 小白板",
        s_summary([("附近", "fujin"), ("离", "li"), ("就", None), ("然后", "ranhou"),
                   ("大约", "dayue"), ("对面", "duimian"), ("挺", None),
                   ("多长时间", "shijian")],
                  "小白板：这八样，哪一样你还是 😐？写下来举起来。"
                  "举得最多的那一个，就是复习要从哪儿开始。", dense=True))
    add("28-exit.html", "Exit ticket", PLEN, "出门条 · Exit ticket",
        s_task("出门条 · 写三句你自己的社区，交上来",
               ["第一句用<b>「附近有……等」</b>。",
                "第二句用<b>「离……远／近」</b>。",
                "第三句用<b>「先……，然后……」</b>。"],
               ext="写完了？再写第四句，用「就」。",
               cn="三句都写对的那几张，就是单元测验写作部分的样子——"
                  "下节课带回来。"))
    return S
