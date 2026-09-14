# -*- coding: utf-8 -*-
"""Lesson 5 of 5 — 去饭店吃饭 Eating out + 会."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, t, tag, sec, body, cls=""): S.append((f, t, tag, sec, body, cls))

add("01-title.html", "Y8 L11 · Title · 去饭店吃饭 + 会", "Lesson 5 of 5", "Y8 · Lesson 11",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 11", "去饭店吃饭", "Eating Out · 会",
                "Lesson 5 of 5 · 50 minutes · 课本 p.105, p.108",
                ["fandian", "chifan", "kuaicandian", "shuiguodian"]))

add("02-reading.html", "Y8 L11 · Review · 阅读 田方", "0–8 MIN · 复习", "Review · 练习册 p.122 Ex.10",
    '  <p class="section-label">阅读 · Read it silently, then in pairs · 练习册 p.122 Ex.10</p>\n'
    '  <div class="task-box">\n'
    '    <p class="dl-cn" style="line-height:1.5">田方住在香港。她非常喜欢香港，因为香港有很多好吃的东西。'
    '在香港，除了<b>中餐</b>、<b>西餐</b>，她还可以吃到各种<b>快餐</b>。她最喜欢吃<b>汉堡包</b>，'
    '还经常吃<b>比萨饼</b>、<b>热狗</b>、炸鸡翅、炸薯条等。她每个星期六都去吃汉堡包。'
    '她妈妈说她应该少吃快餐，多吃蔬菜和水果。</p>\n  </div>\n' +
    callout("tip", "不用问 · Don't ask about 炸鸡翅 or 炸薯条",
            "Meet them as unknowns and work around them — that is the skill the test's reading section asks for.",
            None, "Everything else is Lessons 1–2 plus Lesson 10's 应该 and 可是."))

add("03-tf.html", "Y8 L11 · Review · 对还是错 True or false", "0–8 MIN · 复习", "Review · 对／错",
    '  <p class="section-label">对还是错 · True or false — whiteboards, held up together</p>\n' +
    examples_block([("田方不太喜欢住在香港。", None, False),
                    ("她除了爱吃汉堡包，还爱吃比萨饼。", None, False),
                    ("她每天都吃汉堡包。", None, False),
                    ("她妈妈叫她多吃蔬菜和水果。", None, False)], "四句 · Four statements") + "\n" +
    callout("note", "然后 · Then — 3 minutes",
            "Rapid discrimination: teacher reads six sentence halves aloud, students write only <b>还是</b> or <b>或者</b>.",
            None, "Three questions, three statements, mixed order."))

add("04-li-sc.html", "Y8 L11 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to talk about eating out, and to say something is likely to happen using 会.",
             [("I can say 饭店 and 吃饭, and build other 店 words", "快餐店、水果店"),
              ("I can use 会 to say something is likely", "这个周末我们会去饭店吃饭。"),
              ("I can read Text 2 aloud and answer in Chinese", "他们下个周末会去哪儿？")]))

add("05-c1-words.html", "Y8 L11 · Cycle 1 · A — 饭店 / 吃饭", T, "生词 · Cycle 1 of 2",
    words_slide(("饭店", "fàndiàn", "restaurant", "fandian", "飯店"),
                ("吃饭", "chīfàn", "to eat a meal", "chifan", "吃飯")))
add("06-c1-examples.html", "Y8 L11 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 2",
    sentences_slide([
        ("Wǒmen zhōumò qù fàndiàn.", "我们周末去<b>饭店</b>。", "We go to a restaurant at the weekend.", False),
        ("Wǒmen quán jiā rén yìqǐ chīfàn.", "我们全家人一起<b>吃饭</b>。", "Our whole family eats together.", False),
        ("Wǒmen zhōumò qù fàndiàn chīfàn.", "我们周末去<b>饭店吃饭</b>。", "We eat out at the weekend — straight from Text 2.", True)]))
add("07-c1-write.html", "Y8 L11 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 2",
    write_slide(["我们 ______ 去饭店吃饭。"],
                "60 seconds. Mini whiteboards.",
                "Two clauses contrasting home and out — then add what you eat there, using 或者.",
                "我们全家人一般在家吃饭，可是周末有时候去饭店吃饭。"))

add("08-c2-words.html", "Y8 L11 · Cycle 2 · A — 快餐店 / 水果店", T, "生词 · Cycle 2 of 2",
    words_slide(("快餐店", "kuàicāndiàn", "fast-food shop", "kuaicandian"),
                ("水果店", "shuǐguǒdiàn", "fruit shop", "shuiguodian")))
add("09-c2-examples.html", "Y8 L11 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 2",
    sentences_slide([
        ("Wǒ xǐhuan qù kuàicāndiàn chīfàn.", "我喜欢去<b>快餐店</b>吃饭。", "I like eating at a fast-food shop.", False),
        ("Shuǐguǒdiàn yǒu hěn duō shuǐguǒ.", "<b>水果店</b>有很多水果。", "The fruit shop has a lot of fruit.", False),
        ("Wǒ xǐhuan qù kuàicāndiàn, wǒ māma xǐhuan qù shuǐguǒdiàn.", "我喜欢去<b>快餐店</b>，我妈妈喜欢去<b>水果店</b>。", "I like the fast-food shop, my mother likes the fruit shop.", True)]) +
    "\n" + callout("tip", "店 · A shop, on the end",
                   "Both words are built from things you already know — 快餐 + 店, 水果 + 店."))
add("10-c2-write.html", "Y8 L11 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 2",
    write_slide(["______ 店　·　______ 店", "______ 店有 ______ 。"],
                "Build two more 店 words from words you know, then use one in a sentence.",
                "The full family from 练习册 Ex.13 — 玩具店、书店、花店. One sentence each with 有, then rank them with a 可是 clause.",
                "花店有很多花。　我最喜欢去书店，可是我妈妈最喜欢去花店。"))

add("11-recall.html", "Y8 L11 · Checkpoint · 认字 recall", T, "Checkpoint",
    recall_slide(["饭店", "吃饭", "快餐店", "水果店"], 4))

add("12-pattern.html", "Y8 L11 · I Do · 句型 会", T, "句型 · Sentence pattern",
    '  <div class="pattern-box"><p class="pattern-text"><b>会</b> + 动词</p>'
    '<p class="pattern-note">huì · “is likely to / will” — before the verb, like 应该 and 一般.</p></div>\n'
    '  <div style="margin-top:20px">' +
    examples_block([("今天<b>会</b>下雨。", "It's likely to rain today.", False),
                    ("今晚爸爸不<b>会</b>回家。", "Negative: 不会.", False),
                    ("我午饭<b>会</b>吃快餐。", "I'll probably eat fast food for lunch.", False),
                    ("我们下个周末<b>会</b>去一家北京饭店吃饭。", "Text 2's own final sentence — 会 + measure word 家 + a two-part verb phrase.", True)]) + "</div>\n" +
    callout("warn", "两个意思 · Two meanings of 会",
            "会 also means “be able to” — 我会游泳. The time word tells you which one.",
            "明天会下雨 = likely　·　我会游泳 = ability"))

add("13-text2.html", "Y8 L11 · 课文二 Text 2 (full)", T, "课文二 · p.105 · CD 54",
    '  <p class="section-label">课文二 · Text 2 · 全文 · CD track 54</p>\n'
    '  <div class="task-box">\n'
    '    <p class="dl-cn" style="line-height:1.55">我们全家人都喜欢吃中餐。早餐我们一般吃粥<b>或者</b>面条。'
    '我们午饭吃炒面<b>或者</b>包子。我们晚饭一般吃米饭、炒菜。我们家周末有时候去<b>饭店吃饭</b>。'
    '我们下个周末<b>会</b>去一家北京<b>饭店吃饭</b>。</p>\n  </div>\n' +
    callout("tip", "你们已经会了 · You built this",
            "Every sentence here is language you have made yourself over the last four lessons.",
            None, "The only genuinely new word is 会, in the last sentence. — 他们早餐一般吃什么？ 他们下个周末会去哪儿？"))

add("14-summary.html", "Y8 L11 · 词汇总览 · summary board", "20–43 MIN · 练习", "词汇总览",
    summary_slide([("饭店", "fandian"), ("吃饭", "chifan"), ("快餐店", "kuaicandian"), ("水果店", "shuiguodian"),
                   ("面条", "miantiao"), ("炒面", "chaomian"), ("米饭", "mifan"), ("炒菜", "chaocai"),
                   ("包子", "baozi"), ("会", None)], 5,
                  "词汇总览 · Today's words plus Lesson 4's dishes"))

add("15-act1.html", "Y8 L11 · Activity 1 · 这个周末 (We Do)", "20–26 MIN · WE DO", "Activity 1 · 周末计划",
    task_slide("Activity 1 · 这个周末 · Your family's weekend plan", "SOLO · 6 MIN",
               ["Four sentences. Every one uses <b>会</b>, and at least one uses <b>或者</b>.",
                "cn:这个周末我们全家人会去饭店吃饭。",
                "cn:我们会吃面条或者炒面。",
                "cn:我会喝可乐。",
                "cn:星期天我们会去水果店。"],
               "Six sentences across two days and all three meals, with two of them <b>negative</b> using 不会. Then a partner asks you two 还是 questions about the plan, answered live without your paper.",
               "星期六我们不会在家吃饭。"))

add("16-act2.html", "Y8 L11 · Activity 2 · 饭店 Role-play (You Do)", "26–35 MIN · YOU DO", "Activity 2 · 角色扮演",
    '  <p class="section-label">Activity 2 · 听一听 (CD 55, 3 min)，然后演一演 · PAIRS · 6 MIN</p>\n'
    '  <div style="margin-top:6px">' +
    dialogue_block([("A", "Nǐmen xiǎng chī zhōngcān háishi xīcān?", "你们想吃中餐还是西餐？"),
                    ("B", "Zhōngcān. Wǒmen huì chī miàntiáo huòzhě chǎomiàn.", "中餐。我们<b>会</b>吃面条<b>或者</b>炒面。"),
                    ("A", "Nǐmen xiǎng hē shénme yǐnliào?", "你们想喝什么饮料？"),
                    ("B", "Kělè, xièxie.", "可乐，谢谢。")]) + "</div>\n" +
    callout("note", "规则 · The rules",
            "<b>Restaurant</b> asks two 还是 questions. <b>Customer</b> uses 或者 and 会 once each. Swap, run it again.") + "\n"
    '  <div class="extension-box">\n    <p class="extension-label">Extension · 加油题</p>\n'
    '    <p class="extension-text">The restaurant has <b>run out</b> of whatever the customer asks for first — change the order in Chinese without restarting the dialogue. No word bank; fluent students take the restaurant role.</p>\n'
    '    <p class="extension-cn">对不起，今天没有炒面。／ 没关系，那我们吃面条或者包子。</p>\n  </div>')

add("17-game.html", "Y8 L11 · Game · 写字接力 (two rounds)", "35–43 MIN · 游戏", "Game · 写字接力",
    '  <p class="section-label">Game · 写字接力 · Writing Relay — two rounds</p>\n'
    '  <div class="badge badge-orange"><p>TEAMS OF FOUR · 8 MIN</p></div>\n'
    '  <div class="task-box" style="margin-top:14px">\n'
    '    <p class="task-line"><b>第一轮 · Round 1 (4 min)</b> — 简单字, 练习册 p.126 Ex.19. Teacher calls the English meaning.</p>\n'
    '    <p class="task-cn">虫　贝　刀　民　食　果　欠　石　东　南　西　北</p>\n'
    '    <p class="task-line" style="margin-top:12px"><b>第二轮 · Round 2 (4 min)</b> — 部首, 练习册 p.120 Ex.6. Teacher calls the radical\'s meaning; write the radical only.</p>\n'
    '    <p class="task-cn">革　厂　车　广　贝　礻　犭　虫</p>\n  </div>\n' +
    callout("warn", "贝 出现两次 · 贝 appears in both rounds",
            "Shell as a simple character, treasure as a radical. Two glosses, one character.",
            None, "That's exactly what the test's Part 3 turns on.") + "\n"
    '  <div class="extension-box">\n    <p class="extension-label">Extension · 加油题</p>\n'
    '    <p class="extension-text">Round 1 — also write a <b>two-character word</b> containing it. Round 2 — write a character that <b>uses</b> that radical. Worth two points; a wrong answer costs one.</p>\n'
    '    <p class="extension-cn">食 → 食物　·　西 → 西餐　·　犭 → 狗　·　饣 → 饭</p>\n  </div>')

add("18-sequence.html", "Y8 L11 · 全课复习 · all 26 words", "43–50 MIN · 小结", "全课复习 · Lesson 11",
    '  <p class="section-label">全课复习 · Everything from Lesson 11 — read them down in four chunks</p>\n'
    '  <div class="summary-grid" style="grid-template-columns:repeat(7,1fr);gap:14px">\n' +
    "\n".join(f'    <div class="summary-cell noimg" style="padding:20px 6px">'
              f'<p class="summary-hanzi{" long" if len(w)>=3 else ""}" style="font-size:{40 if len(w)>=3 else 50}px">{w}</p></div>'
              for w in ["中餐", "西餐", "还是", "快餐", "热狗", "汉堡包", "比萨饼",
                        "喝", "饮料", "可乐", "汽水", "早餐", "午饭", "晚饭",
                        "一般", "全", "粥", "面条", "炒面", "米饭", "炒菜",
                        "包子", "或者", "饭店", "吃饭", "会"]) +
    "\n  </div>\n" +
    callout("tip", "读不出来的 · Whatever stalls",
            "Say it aloud. That is exactly what to look at before the Unit 4 test.",
            None, "食物类 → 饮料类 → 三餐 → 中餐菜 · four chunks, four passes."))

add("19-plenary.html", "Y8 L11 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary — the whole sequence</p>\n  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Thumbs across the whole sequence — {RATE}", None,
            "One show of hands per group of words, not per criterion. All five lessons' criteria go up at once.") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Translate — <i>“I will probably eat fast food for lunch.”</i>",
            "我午饭会吃快餐。",
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "We start Lesson 12 — 外出就餐. Same restaurant, but this time <b>you pay</b>: prices, money, and how much things cost.") +
    "\n  </div>")

m, total = write_deck("l5-restaurant-hui", S, "", "", "")
json.dump([{"file": f, "label": l} for f, l in m],
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "l5-manifest.json"), "w"),
          ensure_ascii=False, indent=1)
print(f"L5: {total} slides")
