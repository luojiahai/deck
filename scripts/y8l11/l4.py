# -*- coding: utf-8 -*-
"""Lesson 4 of 5 — 中餐菜 Chinese dishes + 或者."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, t, tag, sec, body, cls=""): S.append((f, t, tag, sec, body, cls))

add("01-title.html", "Y8 L11 · Title · 中餐菜 + 或者", "Lesson 4 of 5", "Y8 · Lesson 11",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 11", "中餐菜", "Chinese Dishes · 或者",
                "Lesson 4 of 5 · 50 minutes · 课本 p.106–107, p.109",
                ["miantiao", "chaomian", "mifan", "chaocai", "baozi"]))

add("02-review.html", "Y8 L11 · Review · 改错 Correct the Teacher", "0–8 MIN · 复习", "Review · Lesson 3",
    '  <p class="section-label">改错 · Correct the teacher — three of these are wrong</p>\n' +
    examples_block([("我吃一般早餐粥。", "一般 in the wrong place.", False),
                    ("我们全家人都喜欢吃中餐。", "Nothing wrong with this one.", False),
                    ("我午饭一般吃快餐还是汉堡包。", "You can hear it's broken — but you can't fix it yet.", True),
                    ("我晚饭吃一般中餐。", "一般 in the wrong place again.", False)],
                   "Find and fix each on your whiteboard") + "\n" +
    callout("warn", "第三句 · Leave number 3 on the board",
            "We haven't got the word for this one. You'll have it in fifteen minutes.",
            None, "It stays in the corner of the board all lesson, and gets fixed in the plenary."))

add("03-li-sc.html", "Y8 L11 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to name Chinese dishes and use 或者 to say “or” in a statement.",
             [("I can say and read five Chinese dishes", "面条、炒面、米饭、炒菜、包子"),
              ("I can use 或者 in a statement", "我午饭一般吃面条或者炒面。"),
              ("I can choose between 还是 and 或者", "还是 asks　·　或者 tells")]))

add("04-c1-words.html", "Y8 L11 · Cycle 1 · A — 面条 / 炒面", T, "生词 · Cycle 1 of 3",
    words_slide(("面条", "miàntiáo", "noodles", "miantiao", "麵條"),
                ("炒面", "chǎomiàn", "stir-fried noodles", "chaomian", "炒麵")))
add("05-c1-examples.html", "Y8 L11 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 3",
    sentences_slide([
        ("Wǒ wǔfàn yìbān chī miàntiáo.", "我午饭一般吃<b>面条</b>。", "I normally eat noodles for lunch.", False),
        ("Wǒ hěn xǐhuan chī chǎomiàn.", "我很喜欢吃<b>炒面</b>。", "I really like stir-fried noodles.", False),
        ("Miàntiáo hé chǎomiàn wǒ dōu xǐhuan chī.", "<b>面条</b>和<b>炒面</b>我都喜欢吃。", "I like both noodles and stir-fried noodles.", True)]) +
    "\n" + callout("tip", "部首 · Radical clue",
                   "炒 has 火 (fire) on the left — 炒面 and 炒菜 are both cooked in a hot wok."))
add("06-c1-write.html", "Y8 L11 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 3",
    write_slide(["我 ______ 喜欢吃面条。", "我 ______ 喜欢吃炒面。"],
                "60 seconds. Two sentences.",
                "Use 除了……以外, then a second sentence saying which you prefer and when you eat it.",
                "我晚饭一般吃面条，可是我最喜欢吃炒面。"))

add("07-c2-words.html", "Y8 L11 · Cycle 2 · A — 米饭 / 炒菜", T, "生词 · Cycle 2 of 3",
    words_slide(("米饭", "mǐfàn", "cooked rice", "mifan", "米飯"),
                ("炒菜", "chǎocài", "fried dishes", "chaocai")))
add("08-c2-examples.html", "Y8 L11 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 3",
    sentences_slide([
        ("Wǒmen wǎnfàn yìbān chī mǐfàn.", "我们晚饭一般吃<b>米饭</b>。", "We normally eat rice for dinner.", False),
        ("Wǒ māma zuò chǎocài.", "我妈妈做<b>炒菜</b>。", "My mother makes stir-fried dishes.", False),
        ("Wǒmen wǎnfàn yìbān chī mǐfàn, chǎocài.", "我们晚饭一般吃<b>米饭</b>、<b>炒菜</b>。", "Rice and stir-fried dishes — straight from Text 2.", True)]))
add("09-c2-write.html", "Y8 L11 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 3",
    write_slide(["我们晚饭一般吃 ______ 和 ______ 。"],
                "60 seconds. Mini whiteboards.",
                "Report on the <b>whole family</b>, then break it with one exception. Deliver it standing, no notes.",
                "我们全家人晚饭一般吃米饭、炒菜，可是我爸爸不太喜欢吃炒菜。"))

add("10-c3-words.html", "Y8 L11 · Cycle 3 · A — 包子 / 或者", T, "生词 · Cycle 3 of 3",
    words_slide(("包子", "bāozi", "steamed stuffed bun", "baozi"),
                ("或者", "huòzhě", "or (in statements)", None)))
add("11-c3-examples.html", "Y8 L11 · Cycle 3 · B — 例句", T, "生词 · Cycle 3 of 3",
    sentences_slide([
        ("Wǒ zǎocān yìbān chī bāozi.", "我早餐一般吃<b>包子</b>。", "I normally eat steamed buns for breakfast.", False),
        ("Wǒ wǔfàn yìbān chī miàntiáo huòzhě chǎomiàn.", "我午饭一般吃面条<b>或者</b>炒面。", "I normally eat noodles or stir-fried noodles for lunch.", False),
        ("Wǒ zǎocān yìbān chī zhōu huòzhě bāozi.", "我早餐一般吃粥<b>或者包子</b>。", "Congee or steamed buns — Text 2's own sentence shape.", True)]))
add("12-c3-write.html", "Y8 L11 · Cycle 3 · C — 写一句", T, "生词 · Cycle 3 of 3",
    write_slide(["我早餐一般吃 ______ 或者 ______ 。"],
                "60 seconds. Both blanks must be real food.",
                "Write three 或者 sentences, one per meal — then turn <b>one</b> of them into a 还是 question and write both side by side. That pair is what the test asks for.",
                "我早餐一般吃粥或者包子。　／　你早餐吃粥还是包子？"))

add("13-recall.html", "Y8 L11 · Checkpoint · 认字 recall", T, "Checkpoint",
    recall_slide(["面条", "炒面", "米饭", "炒菜", "包子", "或者"], 3))

add("14-extra.html", "Y8 L11 · Extra Words · 认一认 recognition only", T, "Extra Words · p.106",
    recall_slide(["春卷", "馄饨", "饺子", "小笼包", "生煎包", "豆浆"], 3,
                 "Extra Words · 认一认 — read once, name once, move on") + "\n" +
    callout("note", "认识就好 · Recognition only",
            "These are <b>not</b> for production and <b>not</b> in the Unit 4 test.",
            None, "小笼包 and 生煎包 both end in 包 — the same 包 as today's 包子."))

add("15-compare.html", "Y8 L11 · 句型 · 还是 vs 或者", T, "句型 · 还是 vs 或者",
    '  <p class="section-label">句型 · 两个「or」· Two words for “or”</p>\n'
    '  <div class="compare">\n'
    '    <div class="compare-col ask">\n'
    '      <p class="compare-head">还是</p>\n'
    '      <p class="compare-sub">háishi · 问 · asking — ends in <b>？</b></p>\n'
    '      <p class="compare-line">你午饭吃面条<b>还是</b>炒面？</p>\n'
    '      <p class="compare-line">你想吃苹果<b>还是</b>香蕉？</p>\n'
    '      <p class="compare-line">他晚上看书<b>还是</b>看电视？</p>\n    </div>\n'
    '    <div class="compare-col tell">\n'
    '      <p class="compare-head">或者</p>\n'
    '      <p class="compare-sub">huòzhě · 说 · telling — ends in <b>。</b></p>\n'
    '      <p class="compare-line">我午饭吃面条<b>或者</b>炒面。</p>\n'
    '      <p class="compare-line">苹果<b>或者</b>香蕉，都可以。</p>\n'
    '      <p class="compare-line">他晚上一般看书，<b>或者</b>看电视。</p>\n    </div>\n  </div>\n' +
    callout("warn", "怎么选 · How to choose",
            "句号用<b>或者</b>，问号用<b>还是</b>。 Look at the punctuation at the end of the sentence — it tells you which word you needed.",
            "你早餐一般吃粥还是包子？ — 粥或者包子，都可以。"))

add("16-summary.html", "Y8 L11 · 词汇总览 · summary board", "20–43 MIN · 练习", "词汇总览",
    summary_slide([("面条", "miantiao"), ("炒面", "chaomian"), ("米饭", "mifan"),
                   ("炒菜", "chaocai"), ("包子", "baozi"), ("或者", None)], 6,
                  "词汇总览 · Stays on screen for the whole task"))

add("17-task.html", "Y8 L11 · Activity 1 · 一天的菜单 (We Do)", "20–27 MIN · WE DO", "Activity 1 · 菜单",
    task_slide("Activity 1 · 一天的菜单 · A one-day menu", "PAIRS · 7 MIN",
               ["Three rows — 早餐 / 午饭 / 晚饭. <b>One sentence per row</b>, every sentence using 或者.",
                "Between the three rows you must use all five dishes <b>plus 粥</b> from last lesson. Nothing repeated.",
                "cn:早餐：我们一般吃粥或者包子。"],
               "Add a fourth row — 周末 — written as a contrast across two clauses. Then another pair asks you three 还是 questions about your menu, which you answer <b>without looking at the sheet</b>.",
               "周末我们一般不吃米饭，我们吃炒面或者面条，可是我妈妈一般吃粥。"))

add("18-act2.html", "Y8 L11 · Activity 2 · 还是 还是 或者？ (You Do)", "27–35 MIN · YOU DO", "Activity 2 · 练习册 Ex.15",
    '  <p class="section-label">Activity 2 · 还是 还是 或者？· 练习册 p.125 Ex.15</p>\n'
    '  <div class="badge badge-orange"><p>WHITEBOARDS · 8 MIN · 这是考试题型</p></div>\n'
    '  <div style="margin-top:14px">' +
    examples_block([("我们坐地铁 ______ 坐出租车去？", None, False),
                    ("晚饭我们吃炒饭 ______ 炒面。", None, False),
                    ("苹果 ______ 香蕉，都可以。", None, False),
                    ("你想去美国 ______ 英国上大学？", None, False),
                    ("今天来 ______ 明天来，都可以。", None, False),
                    ("他晚上一般看书，______ 看电视。", None, False)],
                   "还是 or 或者 — hold up per item, mark together") + "</div>\n"
    '  <div class="extension-box">\n    <p class="extension-label">Extension · 加油题</p>\n'
    '    <p class="extension-text">Write the <b>other</b> version of each — turn every statement into a question and every question into a statement, swapping the conjunction. Six rewrites.</p>\n'
    '    <p class="extension-cn">我们坐地铁或者坐出租车去，都可以。</p>\n  </div>')

def copy_slide(fname, ttl, sec, label, rows, note):
    return (fname, ttl, "35–39 MIN · 写一写", sec,
            f'  <p class="section-label">{label}</p>\n  <div class="stack gap-sm">\n' +
            "\n".join(f'    <div class="stroke-row"><p class="stroke-char">{h}</p><div class="stroke-meta">'
                      f'<p class="stroke-py">{p}</p><p class="stroke-en">{e}</p>'
                      f'<p class="stroke-count">{n} strokes</p></div></div>' for h, p, e, n in rows) +
            "\n  </div>\n" + note, "")

S.append(copy_slide("19-write-a.html", "Y8 L11 · 写一写 · 粥 或 者", "写一写 · 练习册 Ex.12 (1/2)",
    "写一写 · Copy the characters · 练习册 p.123 Ex.12",
    [("粥", "zhōu", "porridge; congee", 12), ("或", "huò", "or", 8), ("者", "zhě", "person or thing", 8)],
    callout("note", "安静写 · Quiet block",
            "Three copies each. 粥 is 弓 + 米 + 弓 — a rice between two bows, not one blob.",
            None, "Stroke order projected one character at a time. Teacher checks grip and direction, not speed.")))

S.append(copy_slide("20-write-b.html", "Y8 L11 · 写一写 · 面 条 炒", "写一写 · 练习册 Ex.12 (2/2)",
    "写一写 · Copy the characters · 练习册 p.124 Ex.12",
    [("面", "miàn", "flour; measure word", 9), ("条", "tiáo", "stripe; measure word", 7), ("炒", "chǎo", "stir-fry", 8)],
    callout("tip", "炒 = 火 + 少",
            "Fire on the left — that's the clue to what 炒面 and 炒菜 mean.",
            None, "全 般 店 once each if there's time. 店 comes back next lesson in 饭店、快餐店、水果店.")))

add("21-game.html", "Y8 L11 · Game · 接龙 Category Chain", "39–43 MIN · 游戏", "Game · 接龙",
    task_slide("Game · 接龙 · Category Chain", "WHOLE CLASS STANDING · 4 MIN",
               ["课本 p.109 Ex.16. Teacher names a category and one item — 中餐：炒面.",
                "Students around the room add one item each.",
                "Repeat an item, or fail to add one in three seconds — you sit down.",
                "Two rounds: 中餐 · 饮料."],
               "Your addition must be a <b>full sentence using 或者</b> that links your item to the previous student's. Fluent students start each round, so they set the bar.",
               "他说炒面，我早餐一般吃包子或者粥。"))

add("22-plenary.html", "Y8 L11 · Plenary · 改错 + exit ticket", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n  <div class="stack gap-md">\n' +
    callout("tip", "改错 · Fix the broken sentence",
            "Back to the corner of the board. The class calls the fix.",
            "我午饭一般吃快餐<b>或者</b>汉堡包。",
            "Name it: that's what you couldn't do at the start of the lesson.") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Write <b>two</b> sentences about the same two dishes — one statement with 或者, one question with 还是.",
            "我午饭一般吃面条或者炒面。　／　你午饭吃面条还是炒面？") + "\n" +
    callout("note", "下节课 · Next lesson",
            "去饭店吃饭 — eating out, and how to say something is <b>likely</b> to happen.") +
    "\n  </div>")

m, total = write_deck("l4-dishes-huozhe", S, "", "", "")
json.dump([{"file": f, "label": l} for f, l in m],
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "l4-manifest.json"), "w"),
          ensure_ascii=False, indent=1)
print(f"L4: {total} slides")
