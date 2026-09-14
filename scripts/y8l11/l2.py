# -*- coding: utf-8 -*-
"""Lesson 2 of 5 — 你喜欢喝什么饮料？ Drinks + Text 1."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import *

T = "10–20 MIN · I DO"
S = []
def add(f, t, tag, sec, body, cls=""): S.append((f, t, tag, sec, body, cls))

def chars_slide(label, rows, note=None):
    trs = "\n".join(
        f'      <tr><td class="hanzi-cell">{h}</td><td class="pinyin-cell">{p}</td>'
        f'<td class="english-cell">{e}</td><td class="english-cell">{s}</td></tr>'
        for h, p, e, s in rows)
    n = ("\n" + note) if note else ""
    return (f'  <p class="section-label">{label}</p>\n  <table class="pair-table">\n'
            f'    <tr><th>汉字</th><th>拼音</th><th>English</th><th>Strokes</th></tr>\n'
            f'{trs}\n  </table>{n}')

add("01-title.html", "Y8 L11 · Title · 饮料 Drinks", "Lesson 2 of 5", "Y8 · Lesson 11",
    title_slide("轻松学中文 2 · Unit 4 · Lesson 11", "你喜欢喝什么饮料？", "Drinks",
                "Lesson 2 of 5 · 50 minutes · 课本 p.100–104",
                ["he", "yinliao", "kele", "qishui", "kuaican"]))

add("02-review.html", "Y8 L11 · Review · Lesson 1", "0–8 MIN · 复习", "Review · Lesson 1",
    recall_slide(["中餐", "西餐", "快餐", "热狗", "汉堡包", "比萨饼"], 3,
                 "认一认 · Characters only — pinyin and English, chorally") +
    "\n" + callout("note", "Cold call · 还是",
                   "Four students, one 还是 question each. Answer <b>without</b> 还是.",
                   "你喜欢吃中餐还是西餐？ — 我喜欢吃中餐。"))

add("03-pinyin.html", "Y8 L11 · 拼音 ie / üe · CD 52", "0–8 MIN · 复习", "拼音 · p.102 Ex.3 · CD 52",
    '  <p class="section-label">听一听，写声调 · Listen and add the vowels with tone marks</p>\n'
    '  <div class="opt-grid">\n' +
    "\n".join(f'    <div class="opt-cell"><p class="opt-key">{i}</p><p class="opt-cn">{w}</p></div>'
              for i, w in enumerate(["jièyuè", "quèyuè", "xièjué", "quēlüè", "quèqiè", "jiéyuē"], 1)) +
    "\n  </div>\n" +
    callout("tip", "Focus · ie / üe",
            "Play twice. Students write on whiteboards, then answers up on screen.",
            None, "üe keeps its two dots after j / q / x — but loses them in writing: lüè not lüè."))

add("04-li-sc.html", "Y8 L11 · Learning Intention & Success Criteria", "8–10 MIN", "学习目标",
    sc_slide("We are learning to say what we drink, and sort food and drink into four categories.",
             [("I can say and read four drink words", "喝、饮料、可乐、汽水"),
              ("I can ask and answer about drinks", "你喜欢喝什么饮料？"),
              ("I can sort a food into a category and say why", "比萨饼是快餐。")]))

add("05-c1-words.html", "Y8 L11 · Cycle 1 · A — 喝 / 饮料", T, "生词 · Cycle 1 of 2",
    words_slide(("喝", "hē", "to drink", "he"),
                ("饮料", "yǐnliào", "drink; beverage", "yinliao", "飲料")))
add("06-c1-examples.html", "Y8 L11 · Cycle 1 · B — 例句", T, "生词 · Cycle 1 of 2",
    sentences_slide([
        ("Wǒ xǐhuan hē shuǐ.", "我喜欢<b>喝</b>水。", "I like drinking water.", False),
        ("Wǒ bù xǐhuan hē zhèxiē yǐnliào.", "我不喜欢<b>喝</b>这些<b>饮料</b>。", "I don't like drinking these beverages.", False),
        ("Nǐ xǐhuan hē shénme yǐnliào?", "你喜欢<b>喝</b>什么<b>饮料</b>？", "What drinks do you like? — today's question.", True)]))
add("07-c1-write.html", "Y8 L11 · Cycle 1 · C — 写一句", T, "生词 · Cycle 1 of 2",
    write_slide(["我喜欢喝 ______ 。", "我不太喜欢喝 ______ 。"],
                "60 seconds. Mini whiteboards.",
                "Write it, then add a 可是 clause of your own so it runs as two joined sentences.",
                "妈妈说我应该多喝水，不应该喝太多饮料。") +
    "\n" + callout("tip", "部首 · Radical clue",
                   "喝 has 口 (mouth) on the left — drinking happens at the mouth. 汽水 has 氵 (water) twice."))

add("08-c2-words.html", "Y8 L11 · Cycle 2 · A — 可乐 / 汽水", T, "生词 · Cycle 2 of 2",
    words_slide(("可乐", "kělè", "coke", "kele", "可樂"),
                ("汽水", "qìshuǐ", "soda water", "qishui")))
add("09-c2-examples.html", "Y8 L11 · Cycle 2 · B — 例句", T, "生词 · Cycle 2 of 2",
    sentences_slide([
        ("Wǒ xǐhuan hē kělè.", "我喜欢喝<b>可乐</b>。", "I like drinking coke.", False),
        ("Wǒ bú tài xǐhuan hē qìshuǐ.", "我不太喜欢喝<b>汽水</b>。", "I don't much like soda water.", False),
        ("Nǐ xiǎng hē kělè háishi qìshuǐ?", "你想喝<b>可乐</b>还是<b>汽水</b>？", "Coke or soda water? — last lesson's 还是, today's words.", True)]))
add("10-c2-write.html", "Y8 L11 · Cycle 2 · C — 写一句", T, "生词 · Cycle 2 of 2",
    write_slide(["你想喝 ______ 还是 ______ ？"],
                "60 seconds. Then ask the person next to you.",
                "Ask <b>three</b> classmates, then report the count in Chinese — standing, no notes.",
                "我问了三个同学。两个同学喜欢喝可乐，一个同学喜欢喝汽水。"))

add("11-recall.html", "Y8 L11 · Checkpoint · 认字 recall", T, "Checkpoint",
    recall_slide(["喝", "饮料", "可乐", "汽水"], 4))

add("12-pattern.html", "Y8 L11 · I Do · 句型 你喜欢喝什么饮料？", T, "句型 · Sentence pattern",
    '  <div class="pattern-box"><p class="pattern-text">你喜欢<b>喝</b>什么<b>饮料</b>？</p>'
    '<p class="pattern-note">→ 我喜欢喝……。</p></div>\n  <div style="margin-top:22px">' +
    examples_block([("你喜欢喝什么饮料？ — 我喜欢喝可乐。", None, False),
                    ("你喜欢喝什么饮料？ — 可乐和汽水，我都喜欢喝。", None, False),
                    ("你喜欢喝什么饮料？ — 我不喜欢喝饮料，我喜欢喝水。", None, False),
                    ("你喜欢吃什么快餐？喜欢喝什么饮料？ — 我喜欢吃汉堡包，喝可乐。", "Both halves in one turn.", True)]) + "</div>")

add("13-text1.html", "Y8 L11 · 课文一 Text 1 (full)", T, "课文一 · p.100 · CD 51",
    '  <p class="section-label">课文一 · Text 1 · 全文 · CD track 51</p>\n' +
    dialogue_block([
        ("A", "Nǐ xǐhuan chī zhōngcān háishi xīcān?", "你喜欢吃中餐还是西餐？"),
        ("B", "Wǒ liǎng zhǒng dōu xǐhuan chī.", "我两种都喜欢吃。"),
        ("A", "Nǐ xǐhuan chī kuàicān ma?", "你喜欢吃快餐吗？"),
        ("B", "Yě xǐhuan. Wǒ xǐhuan chī règǒu, hànbǎobāo hé bǐsàbǐng.", "也喜欢。我喜欢吃热狗、汉堡包和比萨饼。"),
        ("A", "Nǐ xǐhuan hē shénme yǐnliào?", "你喜欢<b>喝</b>什么<b>饮料</b>？"),
        ("B", "Wǒ xǐhuan hē kělè hé qìshuǐ.", "我喜欢喝<b>可乐</b>和<b>汽水</b>。")]))

add("14-chars.html", "Y8 L11 · 简单字 虫 贝 刀 叉", T, "简单字 · p.104 Ex.9",
    chars_slide("简单字 · Learn the simple characters",
                [("虫", "chóng", "insect", "6"), ("贝", "bèi", "shell", "4"),
                 ("刀", "dāo", "knife", "2"), ("叉", "chā", "fork", "3")],
                callout("tip", "注意 · Notice",
                        "刀 and 叉 are what you eat <b>西餐</b> with — the pair names today's contrast.",
                        None, "Stroke order modelled once each on the board before the relay.")))

add("15-summary.html", "Y8 L11 · 词汇总览 · summary board", "20–43 MIN · 练习", "词汇总览",
    summary_slide([("中餐", "zhongcan"), ("西餐", "xican"), ("快餐", "kuaican"), ("热狗", "regou"), ("汉堡包", "hanbaobao"),
                   ("比萨饼", "bisabing"), ("喝", "he"), ("饮料", "yinliao"), ("可乐", "kele"), ("汽水", "qishui")], 5,
                  "词汇总览 · All ten words — stays on screen for the whole task"))

add("16-act1.html", "Y8 L11 · Activity 1 · 听一听 + 分类 (We Do)", "20–28 MIN · WE DO", "Activity 1 · 分类",
    task_slide("Activity 1 · 听一听，然后分类 · Listen, then sort", "PAIRS · 8 MIN",
               ["<b>First 4 min —</b> 课本 p.104 Ex.7, CD track 53. Listen and tick, six items. Play twice.",
                "<b>Then 4 min —</b> four items in <b>every</b> column of the printed grid.",
                "cn:中餐　·　西餐　·　快餐　·　饮料",
                "Six words come from Lesson 1, four from today. The rest you supply."],
               "Every placement justified in a full sentence, at least two of them contrasted. Then add a fifth row: one item that could go in <b>two</b> columns — and argue for both.",
               "热狗和汉堡包都是快餐，可是比萨饼也是西餐。"))

add("17-act2.html", "Y8 L11 · Activity 2 · 设计一家快餐店 (You Do)", "28–35 MIN · YOU DO", "Activity 2 · 菜单",
    task_slide("Activity 2 · 设计一家快餐店 · Design a fast-food restaurant", "PAIRS · 7 MIN",
               ["课本 p.104 Ex.8 · 练习册 p.127 Ex.20. Your menu must carry:",
                "cn:店名　·　四种吃的　·　三种喝的　·　价钱　·　地址、电话",
                "Model — 乐乐快餐店：鱼肉汉堡包 ¥9.80 · 热狗 ¥6.50 · 沙拉 ¥8.60 · 可乐 ¥5.00 · 橙汁 ¥4.50",
                "Extra Words if you want them: 薯条 · 苹果派 · 沙拉 · 咖啡"],
               "Add a one-line 广告 using 还是 to address the customer. Then <b>sell</b> it to another pair aloud — buyers ask two 还是 questions before choosing, and sellers answer without reading their own menu.",
               "你想吃汉堡包还是比萨饼？我们店都有！"))

add("18-write.html", "Y8 L11 · 写一写 · Character copying", "35–39 MIN · 写一写", "写一写 · 练习册 Ex.1",
    '  <p class="section-label">写一写 · Copy the characters · 练习册 p.118 Ex.1</p>\n'
    '  <div class="stack gap-sm">\n' +
    "\n".join(f'    <div class="stroke-row"><p class="stroke-char">{h}</p><div class="stroke-meta">'
              f'<p class="stroke-py">{p}</p><p class="stroke-en">{e}</p>'
              f'<p class="stroke-count">{n} strokes</p></div></div>'
              for h, p, e, n in [("餐", "cān", "food; meal", 16), ("喝", "hē", "drink", 12),
                                 ("饮", "yǐn", "drink", 7), ("料", "liào", "material", 10)]) +
    "\n  </div>\n" +
    callout("note", "安静写 · Quiet block",
            "Three copies each. 餐 is the hard one — watch the top-left 卜 shape and the 夕 beside it.",
            None, "快 狗 饼 are simpler and already carry radicals you know — 忄 犭 饣. The relay does the rest."))

add("19-game.html", "Y8 L11 · Game · 写字接力 Writing Relay", "39–43 MIN · 游戏", "Game · 写字接力",
    task_slide("Game · 写字接力 · Writing Relay", "TEAMS OF FOUR · 4 MIN",
               ["Teacher calls a character — 虫 / 贝 / 刀 / 叉.",
                "Student 1 runs up, writes it with correct stroke order, passes the marker.",
                "Wrong stroke order? The next student fixes it before adding theirs.",
                "Most correct characters in four rounds wins."],
               "The teacher calls the <b>English meaning</b> instead of the sound, and the runner writes the character <b>and</b> its pinyin with the tone mark.",
               "insect → 虫 chóng"))

add("20-plenary.html", "Y8 L11 · Plenary · exit ticket & preview", "43–50 MIN · 小结", "Plenary",
    '  <p class="section-label">小结 · Plenary</p>\n  <div class="stack gap-md">\n' +
    callout("tip", "Self-assessment · 自评",
            f"Traffic light on whiteboards for each criterion — {RATE}", None,
            "Written and held up together, so you see the whole room at once.") + "\n" +
    callout("warn", "Exit ticket · 出门条",
            "Translate into Chinese — <i>“I like eating fast food and drinking coke.”</i>",
            "我喜欢吃快餐，喝可乐。") + "\n" +
    callout("note", "下节课 · Next lesson",
            "一日三餐 — breakfast, lunch and dinner, and how to say what you <b>normally</b> eat.") +
    "\n  </div>")

m, total = write_deck("l2-drinks-text1", S, "", "", "")
json.dump([{"file": f, "label": l} for f, l in m],
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "l2-manifest.json"), "w"),
          ensure_ascii=False, indent=1)
print(f"L2: {total} slides")
