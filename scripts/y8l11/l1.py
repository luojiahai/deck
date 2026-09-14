# -*- coding: utf-8 -*-
"""Lesson 1 of 5 — 中餐还是西餐？ Food types + 还是."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, title, tag, section, body, cls=""):
    S.append((f, title, tag, section, body, cls))

add("01-title.html", "Y8 L11 · Title · 中餐还是西餐？", "Lesson 1 of 5", "Y8 · Lesson 11",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 11", "中餐还是西餐？", "Chinese Food or Western Food?",
                "Lesson 1 of 5 · 50 minutes · 课本 p.100–102",
                ["zhongcan", "xican", "kuaican", "regou", "hanbaobao", "bisabing"]))

add("02-review.html", "Y8 L11 · Review · Lesson 10", "0–8 MIN · 复习", "Review · Lesson 10",
    recall_slide(["蔬菜", "生菜", "黄瓜", "土豆", "西红柿", "苹果", "香蕉", "西瓜"], 4,
                 "认一认 · Read these back — pinyin and English, chorally") +
    "\n" + callout("note", "Whiteboards · 写一写",
                   "What would your mother say to you about vegetables?",
                   "妈妈说我应该每天吃蔬菜。",
                   "Then one more, using 可是 — 我不太喜欢吃蔬菜，可是……"))

add("03-li-sc.html", "Y8 L11 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to name types of food and ask someone to choose, using 还是.",
             [("I can say and read six food words in Chinese", "中餐、西餐、快餐、热狗、汉堡包、比萨饼"),
              ("I can ask a choice question with 还是", "你喜欢吃中餐还是西餐？"),
              ("I can answer without repeating 还是", "我喜欢吃中餐。／我两种都喜欢吃。")]))

# ── Cycle 1 ──
add("04-c1-words.html", "Y8 L11 · Cycle 1 · A — 中餐 / 西餐", T, "生词 · Cycle 1 of 3",
    words_slide(("中餐", "zhōngcān", "Chinese food", "zhongcan"),
                ("西餐", "xīcān", "western food", "xican")))
add("05-c1-examples.html", "Y8 L11 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 3",
    sentences_slide([
        ("Wǒ xǐhuan chī zhōngcān.", "我喜欢吃<b>中餐</b>。", "I like eating Chinese food.", False),
        ("Wǒ bú tài xǐhuan chī xīcān.", "我不太喜欢吃<b>西餐</b>。", "I don't much like eating western food.", False),
        ("Zhōngcān, xīcān, wǒ dōu xǐhuan chī.", "<b>中餐</b>、<b>西餐</b>，我都喜欢吃。", "Chinese food, western food — I like eating both.", True)]))
add("06-c1-write.html", "Y8 L11 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 3",
    write_slide(["我 ______ 喜欢吃中餐，______ 喜欢吃西餐。"],
                "60 seconds. Mini whiteboards. One sentence.",
                "Two clauses with 可是, about <b>someone else</b> — then say it aloud without reading it.",
                "我很喜欢吃西餐，可是我妈妈说我应该多吃中餐。"))

# ── Cycle 2 ──
add("07-c2-words.html", "Y8 L11 · Cycle 2 · A — 快餐 / 热狗", T, "生词 · Cycle 2 of 3",
    words_slide(("快餐", "kuàicān", "fast food", "kuaican"),
                ("热狗", "règǒu", "hot dog", "regou")))
add("08-c2-examples.html", "Y8 L11 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 3",
    sentences_slide([
        ("Wǒ hěn xǐhuan chī kuàicān.", "我很喜欢吃<b>快餐</b>。", "I really like eating fast food.", False),
        ("Wǒ bù xǐhuan chī règǒu.", "我不喜欢吃<b>热狗</b>。", "I don't like eating hot dogs.", False),
        ("Wǒ xǐhuan chī kuàicān, kěshì wǒ bù xǐhuan chī règǒu.", "我喜欢吃<b>快餐</b>，可是我不喜欢吃<b>热狗</b>。", "I like fast food, but I don't like hot dogs.", True)]))
add("09-c2-write.html", "Y8 L11 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 3",
    write_slide(["我 ______ 喜欢吃快餐。", "我 ______ 喜欢吃热狗。"],
                "60 seconds. Two sentences this time.",
                "Write what <b>your own mother</b> would say, using 说……应该 — and name two things you should eat instead.",
                "妈妈说我应该多吃蔬菜和水果，不应该每天吃热狗。"))

# ── Cycle 3 ──
add("10-c3-words.html", "Y8 L11 · Cycle 3 · A — 汉堡包 / 比萨饼", T, "生词 · Cycle 3 of 3",
    words_slide(("汉堡包", "hànbǎobāo", "hamburger", "hanbaobao"),
                ("比萨饼", "bǐsàbǐng", "pizza", "bisabing", "比萨（薩）饼（餅）")))
add("11-c3-examples.html", "Y8 L11 · Cycle 3 · B — 例句", T, "生词 · Cycle 3 of 3",
    sentences_slide([
        ("Wǒ xǐhuan chī hànbǎobāo.", "我喜欢吃<b>汉堡包</b>。", "I like eating hamburgers.", False),
        ("Bǐsàbǐng shì xīcān.", "<b>比萨饼</b>是西餐。", "Pizza is western food.", False),
        ("Hànbǎobāo hé bǐsàbǐng dōu shì kuàicān.", "<b>汉堡包</b>和<b>比萨饼</b>都是快餐。", "Hamburgers and pizza are both fast food.", True)]))
add("12-c3-write.html", "Y8 L11 · Cycle 3 · C — 写一句", T, "生词 · Cycle 3 of 3",
    write_slide(["______ 和 ______ 都是快餐。"],
                "60 seconds. Use two of today's words.",
                "Use 除了……以外, then add a 可是 clause naming something you <b>don't</b> like, so it runs as one turn.",
                "除了汉堡包以外，我还喜欢吃比萨饼和热狗。"))

add("13-recall.html", "Y8 L11 · Checkpoint · 认字 recall", T, "Checkpoint",
    recall_slide(["中餐", "西餐", "快餐", "热狗", "汉堡包", "比萨饼"], 3))

add("14-pattern.html", "Y8 L11 · I Do · 句型 A 还是 B？", T, "句型 · Sentence pattern",
    '  <div class="pattern-box"><p class="pattern-text">A <b>还是</b> B？</p>'
    '<p class="pattern-note">háishi · "or" — in a <b>question</b> only. The answer never contains 还是.</p></div>\n'
    '  <div style="margin-top:22px">' +
    examples_block([
        ("你喜欢吃中餐<b>还是</b>西餐？ — 我喜欢吃中餐。", None, False),
        ("你想吃热狗<b>还是</b>汉堡包？ — 我想吃汉堡包。", None, False),
        ("我们去打球<b>还是</b>看电影？ — 我们去看电影。", None, False),
        ("你想跟爸爸去吃快餐<b>还是</b>跟妈妈去吃中餐？", "Two full clauses, one either side.", True)]) +
    "</div>")

add("15-text1a.html", "Y8 L11 · 课文一 Text 1 (first half)", T, "课文一 · p.100 · CD 51",
    '  <p class="section-label">课文一 · Text 1 · 跟我读 · CD track 51</p>\n' +
    dialogue_block([
        ("A", "Nǐ xǐhuan chī zhōngcān háishi xīcān?", "你喜欢吃<b>中餐</b>还是<b>西餐</b>？"),
        ("B", "Wǒ liǎng zhǒng dōu xǐhuan chī.", "我两种都喜欢吃。"),
        ("A", "Nǐ xǐhuan chī kuàicān ma?", "你喜欢吃<b>快餐</b>吗？"),
        ("B", "Yě xǐhuan. Wǒ xǐhuan chī règǒu, hànbǎobāo hé bǐsàbǐng.", "也喜欢。我喜欢吃<b>热狗</b>、<b>汉堡包</b>和<b>比萨饼</b>。")]) +
    "\n" + callout("tip", "注意 · Notice",
                   "两种 — 种 is last lesson's measure word, doing new work here.",
                   None, "B 喜欢吃中餐还是西餐？ · B 喜欢吃什么快餐？"))

add("16-summary.html", "Y8 L11 · 词汇总览 · summary board", "20–43 MIN · 练习", "词汇总览",
    summary_slide([("中餐", "zhongcan"), ("西餐", "xican"), ("快餐", "kuaican"),
                   ("热狗", "regou"), ("汉堡包", "hanbaobao"), ("比萨饼", "bisabing")], 6,
                  "词汇总览 · Stays on screen for the whole task"))

add("17-task.html", "Y8 L11 · Activity 1 · 三个问题 (We Do)", "20–28 MIN · WE DO", "Activity 1 · 三个问题",
    task_slide("Activity 1 · 三个问题 · Three questions", "PAIRS · 8 MIN",
               ["Write <b>three</b> 还是 questions that between them use <b>all six</b> words.",
                "cn:你喜欢吃中餐还是西餐？",
                "cn:你想吃热狗还是汉堡包？",
                "cn:你喜欢吃快餐还是比萨饼？"],
               "Each question uses a different verb (吃／想吃／喜欢吃). Report back in the <b>third person</b> with a 可是 clause — and no notes.",
               "小明喜欢吃汉堡包，可是他妈妈说他不应该每天吃快餐。",
               steps=["Write your three questions.",
                      "Stand up. Ask three different classmates.",
                      "Report two answers back to the class."]))

add("18-act2.html", "Y8 L11 · Activity 2 · 我们应该……还是……？ (You Do)", "28–36 MIN · YOU DO", "Activity 2 · 练习册 Ex.9",
    '  <p class="section-label">Activity 2 · 我们应该……还是……？ · 练习册 p.121 Ex.9</p>\n'
    '  <div class="badge badge-orange"><p>WHITEBOARDS · 8 MIN</p></div>\n'
    '  <div style="margin-top:16px">' +
    examples_block([("我们应该坐电车<b>还是</b>坐地铁？", None, False),
                    ("我们应该吃中餐<b>还是</b>吃西餐？", None, False),
                    ("我们应该学法语<b>还是</b>学西班牙语？", None, False),
                    ("我们应该穿裤子<b>还是</b>穿裙子？", None, False)],
                   "Build all four. Hold them up. Then ask a partner and get a real answer.") + "</div>\n"
    '  <div class="extension-box">\n    <p class="extension-label">Extension · 加油题</p>\n'
    '    <p class="extension-text">Write two more of your own, then answer each in a full sentence that <b>explains</b> the choice.</p>\n'
    '    <p class="extension-cn">我想学西班牙语，可是我姐姐说我应该学法语。</p>\n  </div>')

add("19-game.html", "Y8 L11 · Game · 拍字 Slap the Character", "36–43 MIN · 游戏", "Game · 拍字",
    task_slide("Game · 拍字 · Slap the Character", "TWO TEAMS · 7 MIN",
               ["Two students at the board. Six A3 cards spread out.",
                "Teacher says a word in Chinese — first to slap it scores.",
                "Rotate every three calls."],
               "The teacher gives a <b>clue sentence</b> instead of the word, and students slap what it describes. Fluent students take the caller's chair and invent the clue themselves, in Chinese.",
               "这是西餐，是圆的。／ 妈妈说我不应该每天吃这个。"))

add("20-plenary.html", "Y8 L11 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n'
    '  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            "Thumbs on each success criterion — 👍 / 😐 / 👎", None,
            "Read the three criteria back off the screen first.") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Write <b>one</b> 还是 question about food — and your own answer to it.",
            "你喜欢吃汉堡包还是比萨饼？ — 我喜欢吃比萨饼。",
            "On a half-slip. Collected at the door.") + "\n" +
    callout("note", "下节课 · Next lesson",
            "What you <b>drink</b> — 你喜欢喝什么饮料？ And you'll design your own fast-food restaurant.") +
    "\n  </div>")

m, total = write_deck("l1-food-types-haishi", S, "", "", "")
json.dump([{"file": f, "label": l} for f, l in m], open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "l1-manifest.json"), "w"),
    ensure_ascii=False, indent=1)
print(f"L1: {total} slides written")
