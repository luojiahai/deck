# -*- coding: utf-8 -*-
"""Y9 L12 · Lesson 1 of 6 — buffet nouns + 在……你可以吃到……

Source: docs/lesson-plans/y9-l12/01-buffet-vocab-mixed.md
Textbook pp.110-111 (Text 1 first half, New Words, Act. 1).
"""
from build import (s_words, s_examples, s_write, s_summary, s_pattern,
                   s_focus, s_task, s_list, s_cfu, s_title, s_lisc, label)

SLUG = "l1-buffet-vocab"
TITLE = "Y9 L12 · 外出就餐 Eating Out · Lesson 1 of 6"

IDO = "10–20 MIN · I DO"
PRAC = "20–43 MIN · FLEXIBLE PRACTICE"
PLEN = "43–50 MIN · PLENARY"


def slides():
    S = []
    add = lambda f, l, t, sec, body, cls="": S.append(
        dict(file=f, label=l, tag=t, section=sec, body=body, cls=cls))

    add("01-title.html", "Title · 自助餐 At the buffet", "LESSON 1 OF 6", "第十二课 · 外出就餐",
        s_title("自助餐", "At the Buffet", "Year 9 · Book 3 · Unit 4 · Lesson 12 · 50 minutes",
                "轻松学中文 3 · pp.110–111"))

    add("02-review.html", "Review · L11 零食 recap", "0–8 MIN · REVIEW", "复习 · Lesson 11",
        label("认字快闪 · flashcards, characters only · 一起读")
        + '  <div class="recall-grid" style="grid-template-columns:repeat(3,1fr);">\n'
        + "\n".join('    <div class="recall-cell"><p class="recall-hanzi">%s</p></div>' % w
                    for w in ["零食", "薯片", "巧克力", "冰淇淋", "饼干", "糖果"])
        + "\n  </div>\n"
        + '  <div class="task-box" style="margin-top:14pt;">\n'
          '    <p class="task-line"><b>白板</b> · 写一句：薯片多少钱一包？ · '
          '用汉字写两个价钱：四块五 · 十二块</p>\n  </div>')

    add("03-li-sc.html", "Learning Intention & Success Criteria", "8–10 MIN",
        "学习目标 · Learning Intention",
        s_lisc("name the main dishes at a buffet and say what you can eat there.",
               [("I can name four buffet dishes in Chinese", "能说出四种自助餐的菜"),
                ("I can use 在……你可以吃到…… to say what a place serves",
                 "能用「在……你可以吃到……」说一个地方卖什么"),
                ("I can sort foods into 主食 and 甜品", "能把食物分成主食和甜品")]))

    # ── Cycle 1 ──
    add("04-c1-words.html", "Cycle 1 · A — 自助餐 / 龙虾", IDO, "生词 1 · Cycle 1 of 2",
        s_words(("自助餐", "zìzhùcān", "buffet", "zizhucan"),
                ("龙虾", "lóngxiā", "lobster", "longxia")))
    add("05-c1-examples.html", "Cycle 1 · B — 例句", IDO, "例句 1 · See them used",
        s_examples([(None, "这家饭店的<b>自助餐</b>很好吃。",
                     "The buffet at this restaurant is delicious."),
                    (None, "我最喜欢吃<b>龙虾</b>。", "I like eating lobster best."),
                    (None, "上个周末我们去吃<b>自助餐</b>，我吃了三个<b>龙虾</b>。",
                     "Last weekend we went for a buffet; I ate three lobsters.", True)],
                   "你吃过龙虾吗？"))
    add("06-c1-write.html", "Cycle 1 · C — 写一句", IDO, "写一句 1 · Write your own",
        s_write(["我（喜欢／不喜欢）吃 ________ 。", "我们去吃 ________ 了。"],
                "用「比」写一句：<b>龙虾比三文鱼贵。</b> 再用「因为……，所以……」说原因。两句要连起来。"))

    # ── Cycle 2 ──
    add("07-c2-words.html", "Cycle 2 · A — 三文鱼 / 寿司", IDO, "生词 2 · Cycle 2 of 2",
        s_words(("三文鱼", "sānwényú", "salmon", "sanwenyu"),
                ("寿司", "shòusī", "sushi", "shousi")))
    add("08-c2-examples.html", "Cycle 2 · B — 例句", IDO, "例句 2 · See them used",
        s_examples([(None, "<b>三文鱼</b>很新鲜。", "The salmon is fresh."),
                    (None, "我妹妹非常爱吃<b>寿司</b>。", "My little sister loves sushi."),
                    (None, "在自助餐厅你可以吃到<b>三文鱼</b>和<b>寿司</b>。",
                     "At the buffet you can eat salmon and sushi.", True)],
                   "寿司是哪国菜？"))
    add("09-c2-write.html", "Cycle 2 · C — 写一句", IDO, "写一句 2 · Write your own",
        s_write(["在自助餐厅你可以吃到 ________ 。"],
                "写两句，一句用「除了……以外」：<b>除了寿司以外，我还喜欢吃三文鱼。</b> 不看屏幕。"))

    # ── Pattern ──
    add("10-pattern.html", "Pattern · 在……你可以吃到……", IDO, "句型 · Sentence pattern",
        s_pattern("句型 · 说一个地方卖什么",
                  "在 + 地方 + 你可以吃到 + 菜名",
                  [("在自助餐厅你可以吃到龙虾。", "At the buffet you can eat lobster."),
                   ("在快餐店你可以吃到汉堡包和薯条。",
                    "At a fast-food shop you can eat burgers and chips."),
                   ("在菜市场你可以买到新鲜的鱼和青菜。",
                    "At the market you can buy fresh fish and greens.")],
                  "注意：<b>买到</b>，不是吃到——地方变了，动词也要变。"))
    add("11-focus.html", "Focus · the hardest example", IDO, "句型 · 最难的一句",
        s_focus("句型 · 两半连起来",
                "在这家饭店，主食你可以吃到三文鱼、寿司，甜品你可以吃到蛋糕和冰淇淋。",
                "At this restaurant, for mains you can eat salmon and sushi; "
                "for dessert you can eat cake and ice cream.",
                "两半——先说主食，再说甜品。五样菜，一句话。"))

    add("12-cfu.html", "CFU · check for understanding", IDO, "检查理解 · CFU",
        s_cfu([("「自助餐」是什么意思？", "Thumbs up if you know"),
               ("怎么说 lobster？", "写在小白板上"),
               ("这句话对不对？ ✗ 我吃到可以龙虾在自助餐厅。", "哪里错了？怎么改？"),
               ("龙虾、三文鱼、寿司——哪一个是日本菜？", "点名回答")]))

    # ── Practice ──
    add("13-summary.html", "Summary board · 词汇总览", PRAC, "词汇总览 · stays on screen",
        s_summary([("自助餐", "zizhucan"), ("龙虾", "longxia"),
                   ("三文鱼", "sanwenyu"), ("寿司", "shousi")],
                  "这一页留在屏幕上——活动一、活动二都看它。"))

    add("14-act1.html", "Activity 1 · Describe the buffet (We Do, 8 min)", PRAC,
        "活动一 · We Do · 8 分钟",
        s_task("活动一 · 说一说这张图 · 课本 p.111 第 1 题",
               ["两人一组，一人说一样，轮流。",
                "图分成两半：左边 <b>主食</b>，右边 <b>甜品</b>。",
                "图上每一样都要说到才能停。"],
               "<b>不要只念菜名——把这家餐厅推销给一个只有 150 块的朋友。</b> "
               "四句连起来：哪个菜最好吃、为什么（因为……所以……）、用「比」比较两样（三文鱼比寿司贵）、"
               "150 块够不够。后半段把图翻过来，不看图说。",
               cn="A：在这个自助餐厅，主食你可以吃到龙虾。　B：主食你可以吃到三文鱼。"))

    add("15-act2.html", "Activity 2 · Build a buffet menu (You Do, 9 min)", PRAC,
        "活动二 · You Do · 9 分钟",
        s_task("活动二 · 写你自己的自助餐菜单",
               ["一个人写，写在练习本上。",
                "菜单要有 <b>主食</b> 和 <b>甜品</b> 两部分。",
                "今天的四个生词都要用上，每样后面写价钱（用「块」）。",
                "最后写一句：在我的自助餐厅你可以吃到……"],
               "写成一段话，不要写成单子——五六句连起来。加上一家三口一共要花多少钱"
               "（我们一家三口一共要花……块），再用「因为……所以……」说最贵的菜为什么这么贵。"))

    add("16-game.html", "Game · Slap the Character (5 min)", PRAC, "游戏 · 拍字 · 5 分钟",
        s_list("游戏 · 拍字 Slap the Character",
               [("两个同学上来，黑板上贴四张字卡", "自助餐 · 龙虾 · 三文鱼 · 寿司"),
                ("老师说中文，先拍到的得一分", "赢的留下，换下一个同学"),
                ("<b>加难</b>：老师不说词，说线索", "这是一种很大的红色海鲜 / 这是日本菜 / 这是一种粉红色的鱼"),
                ("<b>加难</b>：拍到以后要用这个词说一句完整的话", "说不出来不算分")],
               "字卡打印两套，用蓝丁胶贴。"))

    # ── Plenary ──
    add("17-plenary.html", "Plenary · self-assessment + exit ticket", PLEN,
        "小结 · Plenary",
        s_task("小结 · 43–50 分钟",
               ["<b>回看目标</b> · 一个同学用中文念三条 success criteria，全班说英文意思。",
                "<b>自评</b> · 三条目标，一条一条来：👍 / 😐 / 👎。",
                "<b>出门条</b> · 写一句，交到门口。",
                "<b>下节课</b> · 我们学甜品——蛋糕、奶酪，还有怎么说「吃饱了」。"],
               cn="出门条：在自助餐厅你可以吃到 ________ 。（用今天学的词）"))
    return S
