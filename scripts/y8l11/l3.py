# -*- coding: utf-8 -*-
"""Lesson 3 of 5 — 一日三餐 Three meals + 一般."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, t, tag, sec, body, cls=""): S.append((f, t, tag, sec, body, cls))

add("01-title.html", "Y8 L11 · Title · 一日三餐", "Lesson 3 of 5", "Y8 · Lesson 11",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 11", "一日三餐", "Three Meals a Day",
                "Lesson 3 of 5 · 50 minutes · 课本 p.101, p.105, p.107",
                ["zaocan", "wufan", "wanfan", "zhou", "quanjiaren"]))

add("02-review.html", "Y8 L11 · Review · Bingo", "0–8 MIN · 复习", "Review · Lessons 1–2",
    task_slide("复习 · Bingo", "WHOLE CLASS · 6 MIN",
               ["Draw a 3×3 grid. Fill it with any <b>nine</b> of these ten words — in characters.",
                "cn:中餐 · 西餐 · 快餐 · 热狗 · 汉堡包 · 比萨饼 · 喝 · 饮料 · 可乐 · 汽水",
                "Teacher calls each word in <b>Chinese only</b> — no English, no pinyin.",
                "First to a line calls 我赢了！ Play on to two winners."],
               "Then one whiteboard question — everyone writes their own answer and holds it up.",
               "你喜欢吃中餐还是西餐？"))

add("03-li-sc.html", "Y8 L11 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to name the three meals and say what we normally eat at each one.",
             [("I can say and read the three meals and 一般", "早餐、午饭、晚饭、一般"),
              ("I can say what I normally eat", "我早餐一般吃粥。"),
              ("I can talk about my whole family", "我们全家人都喜欢吃中餐。")]))

add("04-c1-words.html", "Y8 L11 · Cycle 1 · A — 早餐 / 午饭", T, "生词 · Cycle 1 of 3",
    words_slide(("早餐", "zǎocān", "breakfast", "zaocan"),
                ("午饭", "wǔfàn", "lunch", "wufan", "午飯")))
add("05-c1-examples.html", "Y8 L11 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 3",
    sentences_slide([
        ("Wǒ zǎocān chī shuǐguǒ.", "我<b>早餐</b>吃水果。", "I eat fruit for breakfast.", False),
        ("Wǒ wǔfàn chī kuàicān.", "我<b>午饭</b>吃快餐。", "I eat fast food for lunch.", False),
        ("Wǒ zǎocān chī shuǐguǒ, wǔfàn chī kuàicān.", "我<b>早餐</b>吃水果，<b>午饭</b>吃快餐。", "Fruit for breakfast, fast food for lunch.", True)]) +
    "\n" + callout("tip", "两个说法 · Two words, one meal",
                   "The book writes <b>早餐</b> in Text 2 and <b>早饭</b> in the workbook. Same meal.",
                   None, "餐 and 饭 swap freely here — which is why 午饭 and 晚饭 take 饭."))
add("06-c1-write.html", "Y8 L11 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 3",
    write_slide(["我早餐吃 ______ ，午饭吃 ______ 。"],
                "60 seconds. Real food — what you actually ate.",
                "Write about a <b>family member</b>, three clauses, ending with a contrast.",
                "我爸爸早餐吃中餐，午饭吃西餐，可是他不喜欢吃快餐。"))

add("07-c2-words.html", "Y8 L11 · Cycle 2 · A — 晚饭 / 一般", T, "生词 · Cycle 2 of 3",
    words_slide(("晚饭", "wǎnfàn", "dinner", "wanfan", "晚飯"),
                ("一般", "yìbān", "normally", None)))
add("08-c2-examples.html", "Y8 L11 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 3",
    sentences_slide([
        ("Wǒ wǎnfàn chī zhōngcān.", "我<b>晚饭</b>吃中餐。", "I eat Chinese food for dinner.", False),
        ("Wǒ yìbān hē shuǐ.", "我<b>一般</b>喝水。", "I normally drink water.", False),
        ("Wǒ wǎnfàn yìbān chī zhōngcān.", "我<b>晚饭一般</b>吃中餐。", "I normally eat Chinese food for dinner — today's pattern.", True)]))
add("09-c2-write.html", "Y8 L11 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 3",
    write_slide(["我晚饭一般吃 ______ 。"],
                "60 seconds. 一般 goes before the verb.",
                "Two clauses contrasting weekdays and the weekend — then one more sentence saying which you prefer.",
                "我晚饭一般吃中餐，可是周末我们一般吃西餐。"))

add("10-c3-words.html", "Y8 L11 · Cycle 3 · A — 全 / 粥", T, "生词 · Cycle 3 of 3",
    words_slide(("全", "quán", "whole", "quanjiaren"),
                ("粥", "zhōu", "porridge; congee", "zhou")))
add("11-c3-examples.html", "Y8 L11 · Cycle 3 · B — 例句", T, "生词 · Cycle 3 of 3",
    sentences_slide([
        ("Wǒmen quán jiā rén dōu xǐhuan chī zhōngcān.", "我们<b>全</b>家人都喜欢吃中餐。", "My whole family likes eating Chinese food. — straight from Text 2.", False),
        ("Wǒ zǎocān yìbān chī zhōu.", "我早餐一般吃<b>粥</b>。", "I normally eat congee for breakfast.", False),
        ("Wǒmen quán jiā rén zǎocān yìbān dōu chī zhōu.", "我们<b>全</b>家人早餐一般都吃<b>粥</b>。", "My whole family normally eats congee for breakfast.", True)]))
add("12-c3-write.html", "Y8 L11 · Cycle 3 · C — 写一句", T, "生词 · Cycle 3 of 3",
    write_slide(["我们全家人 ______ 喜欢吃 ______ 。"],
                "60 seconds. Then two of you read yours aloud.",
                "Three clauses, ending on yourself as the exception — then deliver it to the class <b>without looking at your board</b>.",
                "我们全家人早餐一般吃粥，可是我不太喜欢吃粥，我一般吃水果。"))

add("13-recall.html", "Y8 L11 · Checkpoint · 认字 recall", T, "Checkpoint",
    recall_slide(["早餐", "午饭", "晚饭", "一般", "全", "粥"], 3))

add("14-pattern.html", "Y8 L11 · I Do · 句型 一般", T, "句型 · Sentence pattern",
    '  <div class="pattern-box"><p class="pattern-text">我 + 时间 + <b>一般</b> + 吃／喝 + X</p>'
    '<p class="pattern-note">时间先，<b>一般</b>第二，动词第三 — 我 / 早餐 / 一般 / 吃 / 粥。</p></div>\n'
    '  <div style="margin-top:22px">' +
    examples_block([("我早餐<b>一般</b>吃粥。", None, False),
                    ("我午饭<b>一般</b>吃快餐，喝可乐。", None, False),
                    ("我们全家人晚饭<b>一般</b>吃中餐。", None, False),
                    ("我早餐<b>一般</b>吃水果，可是周末我<b>一般</b>吃汉堡包。", "The pattern twice, joined by 可是.", True)]) + "</div>\n" +
    callout("warn", "常见错误 · Watch out",
            "一般 goes <b>before</b> the verb, never after it.",
            "✗ 我吃一般早餐粥。　✓ 我早餐一般吃粥。"))

add("15-summary.html", "Y8 L11 · 词汇总览 · summary board", "20–43 MIN · 练习", "词汇总览",
    summary_slide([("早餐", "zaocan"), ("午饭", "wufan"), ("晚饭", "wanfan"),
                   ("一般", None), ("全", "quanjiaren"), ("粥", "zhou")], 6,
                  "词汇总览 · Stays on screen for the whole task"))

add("16-task.html", "Y8 L11 · Activity 1 · 一日三餐表 (We Do)", "20–27 MIN · WE DO", "Activity 1 · 三餐表",
    task_slide("Activity 1 · 一日三餐表 · Your own meal grid", "SOLO → PAIRS · 7 MIN",
               ["课本 p.101 Ex.2. Fill the grid with <b>your own real food</b> — Chinese only.",
                "cn:　　　　　吃　　　　　喝",
                "cn:早餐　　___　　　___",
                "cn:午餐　　___　　　___",
                "cn:晚餐　　___　　　___",
                "Then report to your partner: 我早饭一般吃……，喝……。"],
               "Every row uses a frequency word instead of plain 一般 — 有时候 / 经常 / 常常 / 差不多每天都. Then fill a <b>second</b> grid for a family member and present that one, in the third person.",
               "我妈妈早饭差不多每天都喝咖啡，很少吃东西。"))

add("17-act2.html", "Y8 L11 · Activity 2 · 一起去吃午饭 (You Do)", "27–36 MIN · YOU DO", "Activity 2 · 对话",
    '  <p class="section-label">Activity 2 · 我们一起去吃午饭吧！· 课本 p.103 Ex.5 · PAIRS · 5 MIN</p>\n'
    '  <div style="margin-top:6px">' +
    dialogue_block([("A", "Wǒmen yìqǐ qù chī wǔfàn ba!", "我们一起去吃<b>午饭</b>吧！"),
                    ("B", "Hǎo a. Nǐ xiǎng chī xīcān háishi zhōngcān?", "好啊。你想吃西餐还是中餐？"),
                    ("A", "Wǒ xiǎng chī zhōngcān.", "我想吃中餐。"),
                    ("B", "Nǐ xiǎng hē shénme yǐnliào?", "你想喝什么饮料？"),
                    ("A", "Wǒ xiǎng hē kělè.", "我想喝可乐。")]) + "</div>\n" +
    callout("note", "演两遍 · Run it twice", "Swap roles the second time. Then keep your partner — the next slide uses them."))

add("18-interview.html", "Y8 L11 · Activity 2b · 采访 interview", "27–36 MIN · YOU DO", "Activity 2 · 采访",
    task_slide("采访 · Interview your partner", "PAIRS · 4 MIN",
               ["Ask about all three meals. Note the answers.",
                "cn:你早饭一般吃什么？　午饭呢？　晚饭呢？",
                "Then report <b>two</b> of them back to the class — in the third person."],
               "A three-turn version where you <b>disagree</b>, resolved in Chinese without switching to English. Use 可是 to object and 应该 to argue, then report the outcome in the third person.",
               "可是我们昨天吃了西餐，今天应该吃中餐。"))

add("18-game.html", "Y8 L11 · Game · 猜一猜 20 Questions", "36–43 MIN · 游戏", "Game · 猜一猜",
    task_slide("Game · 猜一猜 · 20 Questions", "WHOLE CLASS · 7 MIN",
               ["One student holds a food or drink card from Lessons 1–3.",
                "The class asks yes/no or 还是 questions — <b>Chinese only</b>.",
                "cn:是饮料吗？　是中餐还是西餐？　早餐吃吗？",
                "Up to twenty questions, then guess. Beanbag passes to whoever asks next."],
               "The holder may only answer in <b>full sentences</b> — never a bare 是 or 不是. Fluent students take the card first, so they carry the answering load.",
               "这不是饮料，这是快餐。"))

add("19-plenary.html", "Y8 L11 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Thumbs on each criterion — {RATE}", None,
            "Then 30 seconds on 早饭 / 午饭 / 晚饭 / 米饭 — class gives the English. The fourth is new: it arrives next lesson.") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Write one sentence using <b>一般</b>, about any meal.",
            "我晚饭一般吃米饭。",
            "Whiteboards, held up together. Teacher scans for 一般 sitting after the verb.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "The dishes themselves — 面条、炒面、米饭、炒菜、包子 — and the second word for “or”.") +
    "\n  </div>")

m, total = write_deck("l3-three-meals-yiban", S, "", "", "")
json.dump([{"file": f, "label": l} for f, l in m],
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "l3-manifest.json"), "w"),
          ensure_ascii=False, indent=1)
print(f"L3: {total} slides")
