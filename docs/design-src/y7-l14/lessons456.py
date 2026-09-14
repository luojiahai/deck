# -*- coding: utf-8 -*-
"""Lessons 3–6 of the Y7 L14 (Clothing 穿着) deck series."""

from builder import (ACT_CSS, RADICAL_CSS, TITLE_CSS, activity, board, li_sc, page,
                     pattern, plenary, preview_slide, qa, radicals, text_slide,
                     title_slide, vocab_a, vocab_b, vocab_c, write_deck)
from build import CFU_CSS, SW, cfu


# ══════════════════════════════════════════════════════════════════════════
# LESSON 3 — Text 2 · 你喜欢穿什么衣服？ · mixed
# ══════════════════════════════════════════════════════════════════════════
def lesson3():
    FL, P = "Lesson 3 of 6 · 课文二 · 你喜欢穿什么衣服？", "轻松学中文 Book 1 · Unit 5 · 课本 p.108"
    m = []

    m.append(("01-title.html", "Title · 你喜欢穿什么衣服？",
              page("L3-01 · Title", "", title_slide(
                  3, "你喜欢穿<br>什么衣服？", "Text 2 · 衣服 · 校服 · 毛衣 · 外套", "clothes",
                  ["Year 7 Chinese", "50 分钟", "Mixed", "课本 p.108"]),
                  FL, P, TITLE_CSS)))

    m.append(("02-review.html", "Review · 圈出衣服的词 (0–8 min)",
              page("L3-02 · Review", "Review · 练习册 p.152 第 11 题 · 0–8 min", activity(
                  "Review", "圈出衣服的词 · Circle the clothing words", "8 min",
                  [("练习册 p.152 第 11 题 — 十八个格子，圈出所有衣服的词。三分钟，自己做。",
                    "Workbook Ex.11 — eighteen cells, circle every clothing word. Three minutes, on your own."),
                   ("格子里混了很多以前学过的词：年级、出租车、睡觉、起床、上课、地铁、放学。",
                    "The grid mixes in words from earlier units — this is a recall test of the whole year."),
                   ("有两个词今天下课以前你才圈得出来 — 毛衣、外套。",
                    "Two of them you won't be able to circle until the end of today — 毛衣 and 外套.")],
                  target=["衬衫　汗衫　长衫　长裤　短裤　牛仔裤　校服",
                          "<span class='en'>今天学完再回来圈</span>毛衣　外套"],
                  extension="圈完以后，用其中四个词写一句话，中间用「、」和「和」。",
                  source="练习册 p.152"),
                  FL, "轻松学中文 Book 1 · 练习册 p.152 第 11 题", ACT_CSS, dense=True)))

    m.append(("03-li-sc.html", "Learning Intention & Success Criteria (8–10 min)",
              page("L3-03 · LI & SC", "目标 · Learning Intention & Success Criteria",
                   li_sc("我们学怎么问别人喜欢穿什么衣服，也学怎么一次说好几件。",
                         [("我会问「你喜欢穿什么衣服？」", "I can ask 你喜欢穿什么衣服？"),
                          ("我会一次说好几件衣服，中间用「、」，最后用「和」",
                           "I can answer with several garments — 、 between them, 和 before the last one"),
                          ("我会说 衣服、校服、毛衣、外套", "I can name 衣服, 校服, 毛衣 and 外套")]),
                   FL, P)))

    m.append(("04-vocab-a1.html", "I Do · 生词 1 · 衣服 · 校服",
              page("L3-04 · 生词 1", "I Do · 生词 · 第一组", vocab_a([
                  {"hanzi": "衣服", "pinyin": "yīfu", "en": "clothing", "art": "clothes"},
                  {"hanzi": "校服", "pinyin": "xiàofú", "en": "school uniform", "art": "uniform",
                   "clue": "<b>校</b> — 和「校车」「学校」一样"},
              ]), FL, P)))

    m.append(("05-vocab-b1.html", "I Do · 例句 1 · 衣服 · 校服",
              page("L3-05 · 例句 1", "I Do · 例句 · 衣服 · 校服", vocab_b([
                  ("nǐ xǐhuan chuān shénme yīfu", "你喜欢穿什么<b>衣服</b>？",
                   "What clothes do you like to wear?"),
                  ("wǒ shàngxué chuān xiàofú", "我上学穿<b>校服</b>。",
                   "I wear school uniform to school."),
                  ("wǒ bù xǐhuan xiàofú， wǒ xǐhuan chuān wǒ de yīfu",
                   "我不喜欢<b>校服</b>，我喜欢穿我的<b>衣服</b>。",
                   "I don't like the uniform, I like wearing my own clothes."),
              ], note=("你喜欢穿什么衣服？", "Ask three students. Full sentences, not one word.")),
                  FL, P)))

    m.append(("06-vocab-c1.html", "I Do · 写一句 1",
              page("L3-06 · 写一句 1", "I Do · 写一句 · 衣服 · 校服", vocab_c(
                  ["我喜欢穿<span class='blank'>　　　</span>衣服。"],
                  "写一句回答「你喜欢穿什么衣服？」",
                  "用两个分句，一个正的一个反的 — "
                  "<span class='cn'>我喜欢穿汗衫和牛仔裤，我不喜欢穿校服。</span>"),
                  FL, P)))

    m.append(("07-vocab-a2.html", "I Do · 生词 2 · 毛衣 · 外套",
              page("L3-07 · 生词 2", "I Do · 生词 · 第二组", vocab_a([
                  {"hanzi": "毛衣", "pinyin": "máoyī", "en": "sweater", "art": "sweater",
                   "clue": "<b>毛</b> máo = wool"},
                  {"hanzi": "外套", "pinyin": "wàitào", "en": "coat", "art": "coat",
                   "clue": "<b>外</b> wài = outer"},
              ]), FL, P)))

    m.append(("08-vocab-b2.html", "I Do · 例句 2 · 毛衣 · 外套",
              page("L3-08 · 例句 2", "I Do · 例句 · 毛衣 · 外套", vocab_b([
                  ("wǒ māma xǐhuan chuān hóngsè de máoyī", "我妈妈喜欢穿红色的<b>毛衣</b>。",
                   "My mum likes wearing a red sweater."),
                  ("wǒ bàba xǐhuan chuān hēisè de wàitào", "我爸爸喜欢穿黑色的<b>外套</b>。",
                   "My dad likes wearing a black coat."),
                  ("wǒ chuān máoyī hé wàitào", "我穿<b>毛衣</b>和<b>外套</b>。",
                   "I'm wearing a sweater and a coat."),
              ], note=("「外套」的「外」是什么？", "Which of the two goes on the outside? The character tells you.")),
                  FL, P)))

    m.append(("09-vocab-c2.html", "I Do · 写一句 2",
              page("L3-09 · 写一句 2", "I Do · 写一句 · 毛衣 · 外套", vocab_c(
                  ["我穿<span class='blank'>　　　</span>色的毛衣和<span class='blank'>　　　</span>色的外套。"],
                  "写一句。两件衣服，两个颜色。",
                  "写三件衣服，用「、」和「和」，再加一个分句写别人 — "
                  "<span class='cn'>我穿汗衫、毛衣和外套，我弟弟穿短裤。</span>"),
                  FL, P)))

    m.append(("10-board.html", "I Do · 十件衣服 · Summary Board",
              page("L3-10 · 词汇总览", "I Do · 到现在的十件衣服",
                   board([{"hanzi": "衬衫", "art": "shirt"}, {"hanzi": "汗衫", "art": "tee"},
                          {"hanzi": "毛衣", "art": "sweater"}, {"hanzi": "外套", "art": "coat"},
                          {"hanzi": "校服", "art": "uniform"},
                          {"hanzi": "牛仔裤", "art": "jeans"}, {"hanzi": "长裤", "art": "trousers"},
                          {"hanzi": "短裤", "art": "shorts"}, {"hanzi": "裙子", "art": "skirt"},
                          {"hanzi": "衣服", "art": "clothes"}],
                         cols=5, caption="只有汉字和图 — 这块板整节课都在屏幕上"),
                   FL, P)))

    m.append(("11-pattern.html", "I Do · 句型 · 一次说好几件",
              page("L3-11 · 句型", "I Do · 句型 · A、B、C 和 D", pattern(
                  "A <span class='op'>、</span> B <span class='op'>、</span> C <span class='op'>和</span> D",
                  [("nǐ xǐhuan chuān shénme yīfu", "你喜欢穿什么衣服？",
                    "What clothes do you like to wear?"),
                   ("wǒ xǐhuan chuān hànshān hé duǎnkù", "我喜欢穿汗衫和短裤。",
                    "I like wearing a T-shirt and shorts."),
                   ("wǒ chuān chènshān、 máoyī、 wàitào hé chángkù",
                    "我穿衬衫<b>、</b>毛衣<b>、</b>外套<b>和</b>长裤。",
                    "I wear a shirt, a sweater, a coat and trousers."),
                   ("wǒ xǐhuan chuān hànshān hé duǎnkù， wǒ bù xǐhuan chuān máoyī hé wàitào",
                    "我喜欢穿汗衫和短裤，我不喜欢穿毛衣和外套。",
                    "I like wearing a T-shirt and shorts; I don't like a sweater and a coat.")],
                  note=("info", "、", "说四件东西，只要一个「和」。",
                        "顿号 goes between the middle items; 和 only before the last one. "
                        "✗ 衬衫和毛衣和外套和长裤")),
                  FL, P, dense=True)))

    m.append(("12-cfu.html", "I Do · 检查 · CFU",
              page("L3-12 · CFU", "I Do · 检查一下 · Check for Understanding", cfu(
                  ["「<span class='cn'>衣服</span>」和「<span class='cn'>校服</span>」，哪一个是学校的？哪个字告诉你？",
                   "我说四样东西，要用几个「和」？",
                   "这句对不对？ <span class='cn'>我穿衬衫和毛衣和外套和长裤。</span>"],
                  pairs=[("我穿衬衫和毛衣和外套和长裤。", "我穿衬衫、毛衣、外套和长裤。")]),
                  FL, P, CFU_CSS)))

    m.append(("13-text2.html", "I Do · 课文二 · Text 2 (CD T67)",
              page("L3-13 · 课文二", "I Do · 课文二 · Text 2", text_slide(
                  [("A： nǐ xǐhuan chuān shénme yīfu？", "A：你喜欢穿什么衣服？"),
                   ("B： wǒ xǐhuan chuān hànshān hé duǎnkù。", "B：我喜欢穿汗衫和短裤。"),
                   ("A： nǐ shàngxué chuān xiàofú ma？", "A：你上学穿校服吗？"),
                   ("B： chuān。 wǒ chuān chènshān、 máoyī、 wàitào hé chángkù。",
                    "B：穿。我穿衬衫、毛衣、外套和长裤。")],
                  questions=["女孩喜欢穿什么？", "他的校服有哪四件衣服？"],
                  track="T67")
                  + '''
  <div class="tip-box" style="margin-top:14px;">
    <span class="tip-icon">穿</span>
    <span><span class="tip-text">注意最后的回答：「穿。」不是「是。」</span>
    <span class="tip-sub">Flag it now — the whole of next lesson is about this one answer.</span></span>
  </div>''',
                  FL, P, dense=True)))

    m.append(("14-act1-wardrobe.html", "We Do · 活动一 · 我的衣柜 (7 min)",
              page("L3-14 · 活动一", "Flexible Practice · We Do · 20–27 min", activity(
                  "We Do", "我的衣柜 · What's in your wardrobe", "7 min",
                  [("写<b>一句话</b>，至少四件衣服，每件都有颜色。",
                    "Write ONE sentence listing at least four garments, each with a colour."),
                   ("中间用「、」，最后一件前面用「和」— 数一数，只能有一个「和」。",
                    "顿号 between, 和 before the last — count them, there must be exactly one 和."),
                   ("四分钟。写完三个人读给全班听。", "Four minutes. Three students read theirs aloud.")],
                  target=["我有白色的衬衫、蓝色的牛仔裤、灰色的毛衣和黑色的外套。"
                          "<span class='py'>wǒ yǒu báisè de chènshān、 lánsè de niúzǎikù、 huīsè de máoyī hé hēisè de wàitào</span>"],
                  extension="写<b>别人</b>的衣柜，写完变成猜谜 — 说四件这个房间里某个人有的衣服，"
                            "最后问 <span class='cn'>他是谁？</span>"
                            "<span class='sub'>No summary board — turn away from the screen.</span>"),
                  FL, P, ACT_CSS)))

    m.append(("14b-radicals.html", "I Do · 部首 · 第二组 (冫 户 忄)",
              page("L3-14b · 部首", "I Do · 部首 · 课本 p.107 练习 4 · 第二组", radicals([
                  ("冫", "冰", "ice", "冷", "lěng"),
                  ("户", "门户", "household", "房", "fáng"),
                  ("忄", "心情", "feeling", "忙", "máng"),
              ], note=("六个部首到齐了：冂 牛 贝 冫 户 忄。",
                       "All six are now taught. Both Unit Test radical questions (Parts 2 and 3) "
                       "draw from this set plus Lesson 13's 疒 火 爫 弓 力 礻.")),
                  FL, "轻松学中文 Book 1 · 课本 p.107 练习 4", RADICAL_CSS)))

    m.append(("15-act2-dialogue.html", "You Do · 活动二 · 对话 + 笔顺 (9 min)",
              page("L3-15 · 活动二", "Flexible Practice · You Do · 27–36 min", activity(
                  "You Do", "课文二对话 · 然后写字", "9 min",
                  [("两人一组，照着课本演课文二。再演一次，这次合上书，只看总览板。",
                    "Pairs: perform Text 2 from the book, then again with the book closed."),
                   ("练习册 p.151–152 第 9 题 — 按笔顺抄写 衣 服 毛 外 套。",
                    "Workbook Ex.9 — copy 衣 服 毛 外 套 with stroke order."),
                   ("练习册 p.149 第 5 题 — 部首配汉字。「衤」那一格里有 衬 和 衫。",
                    "Workbook Ex.5 — match radicals to characters. 衬 and 衫 both sit under 衤."),
                   ("课本 p.107 第二组部首：冫 (冷)、户 (房)、忄 (忙)，抄到练习册 p.146。",
                    "Second radical set from p.107 — 冫 ice, 户 household, 忄 feeling. All six are on the Unit Test.")],
                  target=["<span class='en'>课本 p.107 第二组部首</span>冫 冷　户 房　忄 忙"],
                  extension="第 13 题写成一个<b>问句</b>，不是陈述句 — "
                            "<span class='cn'>你喜欢穿外套吗？</span> 再写答案："
                            "<span class='cn'>穿。／不穿。</span>"
                            "<span class='sub'>A head start on next lesson's verb-repeat answer.</span>",
                  source="练习册 p.149 · p.151–152 · 课本 p.107"),
                  FL, "轻松学中文 Book 1 · 练习册 p.149, p.151–152 · 课本 p.107", ACT_CSS, dense=True)))

    m.append(("16-game-jumble.html", "Game · 排句子 Sentence Jumble (7 min)",
              page("L3-16 · Game", "Game · 排句子 Sentence Jumble · 36–43 min", activity(
                  "Game", "排句子 · Sentence Jumble", "7 min",
                  [("每组一个信封，里面是课文二四句话，剪成一个一个的词，全打乱了。",
                    "One envelope per pair: the four sentences of Text 2, cut into single words and shuffled."),
                   ("比谁先把四句话都排好。「、」和「和」是单独的卡片 — 标点也要排对。",
                    "Race to rebuild all four. The 、 and 和 are separate cards, so punctuation counts too."),
                   ("最快的三组各读一句检查。", "The first three pairs each read one sentence aloud to check.")],
                  target=["你喜欢穿什么衣服？　我喜欢穿汗衫和短裤。",
                          "你上学穿校服吗？　穿。我穿衬衫、毛衣、外套和长裤。"],
                  extension="有一个信封里多了一句课文里没有的话 — "
                            "<span class='cn'>我不喜欢穿校服，我喜欢穿牛仔裤。</span>"
                            "<span class='sub'>Build all five, then work out which one is the intruder.</span>"),
                  FL, P, ACT_CSS)))

    m.append(("17-plenary.html", "Plenary · 出门条 (43–50 min)",
              page("L3-17 · Plenary", "Plenary · 回顾 · 自评 · 出门条", plenary(
                  ["我会问「你喜欢穿什么衣服？」",
                   "我会用「、」和「和」一次说好几件",
                   "我会说 衣服、校服、毛衣、外套"],
                  "你喜欢穿什么衣服？",
                  "用中文回答。至少两件衣服，一个「和」。<br>"
                  "<span class='caption'>Answer in Chinese — at least two garments and one 和.</span>"),
                  FL, P)))

    m.append(("18-preview.html", "Preview · 下一课",
              page("L3-18 · Preview", "Preview · 下一课", preview_slide(
                  "下一课 — 校服。还有中文里最奇怪的回答：<br>"
                  "别人问你「你穿校服吗？」，你不说「是」，你说「穿」。",
                  "Next lesson: school uniform — and the strangest answer in Chinese. "
                  "Asked 你穿校服吗？ you don't say 是, you say 穿。",
                  "uniform"), FL, P)))

    return write_deck("l3-text2-yifu", m, "L3 · 课文二 · 你喜欢穿什么衣服？")


# ══════════════════════════════════════════════════════════════════════════
# LESSON 4 — 校服 · 你上学穿校服吗？→ 穿。 · speaking / role-play
# ══════════════════════════════════════════════════════════════════════════
def lesson4():
    FL, P = "Lesson 4 of 6 · 校服 · 穿……吗？→ 穿。", "轻松学中文 Book 1 · Unit 5 · 课本 p.108–110"
    m = []

    m.append(("01-title.html", "Title · 你上学穿校服吗？",
              page("L4-01 · Title", "", title_slide(
                  4, "你上学<br>穿校服吗？", "School Uniform · 穿。not 是。", "uniform",
                  ["Year 7 Chinese", "50 分钟", "Speaking · Role-play", "课本 p.108–110"]),
                  FL, P, TITLE_CSS)))

    m.append(("02-review.html", "Review · 你喜欢穿什么衣服？(0–8 min)",
              page("L4-02 · Review", "Review · 复习 · 0–8 min", activity(
                  "Review", "两人对话 · 然后小白板", "8 min",
                  [("两人一组，背着课本做对话。A 问，B 至少说两件衣服，每件有颜色。换过来。",
                    "Pairs from memory: A asks 你喜欢穿什么衣服？ B answers with two garments and a colour each."),
                   ("小白板四题：写 a grey coat / a red sweater / school uniform，"
                    "再翻译 <span class='cn'>我穿衬衫、毛衣和长裤。</span>",
                    "Four whiteboard items — three to write, one to translate."),
                   ("练习册 p.149 第 6 题 — 口头快速过一遍，不用写。",
                    "Workbook Ex.6 — find the missing word. Quick oral run-through, not written.")],
                  target=["灰色的外套　红色的毛衣　校服",
                          "我穿衬衫、毛衣和长裤。"],
                  extension="B 回答完，再主动问 A 一个问题，然后把 A 的答案报给全班。",
                  source="练习册 p.149"),
                  FL, "轻松学中文 Book 1 · 练习册 p.149 第 6 题", ACT_CSS, dense=True)))

    m.append(("03-li-sc.html", "Learning Intention & Success Criteria (8–10 min)",
              page("L4-03 · LI & SC", "目标 · Learning Intention & Success Criteria",
                   li_sc("我们学怎么问和回答校服的问题。",
                         [("别人问「……吗？」，我会用动词回答 — 穿。／不穿。",
                           "I can answer a 穿……吗？ question by repeating the verb — not with 是"),
                          ("我会问也会答「你穿什么校服？」「你喜欢你的校服吗？」",
                           "I can ask and answer 你穿什么校服？ and 你喜欢你的校服吗？"),
                          ("我会说 帽子、手套、围巾、袜子", "I can name 帽子, 手套, 围巾 and 袜子")]),
                   FL, P)))

    m.append(("04-vocab-a1.html", "I Do · 生词 1 · 帽子 · 手套",
              page("L4-04 · 生词 1", "I Do · 生词 · 第一组 · 课本 p.110 Extra Words", vocab_a([
                  {"hanzi": "帽子", "pinyin": "màozi", "en": "hat", "art": "hat"},
                  {"hanzi": "手套", "pinyin": "shǒutào", "en": "gloves", "art": "gloves",
                   "clue": "<b>套</b> — 和「外套」一样的字"},
              ]) + '''
  <div class="note-box" style="margin-top:34px;">
    <span class="note-icon">有</span>
    <span><span class="note-text">帽子和手套用「有」，不用「穿」。</span>
    <span class="note-sub">说 我有帽子，不说 我穿帽子。Chinese uses a different verb for things you put on your head and hands, and Book 1 hasn't taught it yet.</span></span>
  </div>''', FL, "轻松学中文 Book 1 · 课本 p.110 Extra Words", dense=True)))

    m.append(("05-vocab-b1.html", "I Do · 例句 1 · 帽子 · 手套",
              page("L4-05 · 例句 1", "I Do · 例句 · 帽子 · 手套", vocab_b([
                  ("wǒ jiějie xǐhuan hēisè de màozi", "我姐姐喜欢黑色的<b>帽子</b>。",
                   "My sister likes black hats."),
                  ("wǒ māma yǒu fěnhóngsè de shǒutào", "我妈妈有粉红色的<b>手套</b>。",
                   "My mum has pink gloves."),
                  ("wǒ yǒu màozi hé shǒutào， shì lánsè de", "我有<b>帽子</b>和<b>手套</b>，是蓝色的。",
                   "I have a hat and gloves — they're blue."),
              ], note=("你有帽子吗？什么颜色的？", "Two answers: 有／没有, then the colour.")),
                  FL, P)))

    m.append(("06-vocab-c1.html", "I Do · 写一句 1",
              page("L4-06 · 写一句 1", "I Do · 写一句 · 帽子 · 手套", vocab_c(
                  ["我有<span class='blank'>　　　</span>色的<span class='blank'>　　　</span>。"],
                  "写一句。用「有」，不用「穿」。",
                  "两个分句，一句写自己，一句写家人，用「也」连起来 — "
                  "<span class='cn'>我有黑色的帽子，我妹妹也有，她的是粉红色的。</span>"),
                  FL, P)))

    m.append(("07-vocab-a2.html", "I Do · 生词 2 · 围巾 · 袜子",
              page("L4-07 · 生词 2", "I Do · 生词 · 第二组", vocab_a([
                  {"hanzi": "围巾", "pinyin": "wéijīn", "en": "scarf", "art": "scarf"},
                  {"hanzi": "袜子", "pinyin": "wàzi", "en": "socks", "art": "socks",
                   "clue": "袜子可以用「<b>穿</b>」"},
              ]), FL, P)))

    m.append(("08-vocab-b2.html", "I Do · 例句 2 · 围巾 · 袜子",
              page("L4-08 · 例句 2", "I Do · 例句 · 围巾 · 袜子", vocab_b([
                  ("wǒ yǒu lǜsè de wéijīn", "我有绿色的<b>围巾</b>。", "I have a green scarf."),
                  ("wǒ dìdi xǐhuan huángsè de wàzi", "我弟弟喜欢黄色的<b>袜子</b>。",
                   "My little brother likes yellow socks."),
                  ("wǒ de wéijīn hé wàzi shì báisè de", "我的<b>围巾</b>和<b>袜子</b>是白色的。",
                   "My scarf and socks are white."),
              ], note=("哪一个可以用「穿」？", "Only one of these two takes 穿. Which?")),
                  FL, P)))

    m.append(("09-vocab-c2.html", "I Do · 写一句 2",
              page("L4-09 · 写一句 2", "I Do · 写一句 · 围巾 · 袜子", vocab_c(
                  ["我的<span class='blank'>　　　</span>是<span class='blank'>　　　</span>色的。"],
                  "写一句。用今天的一个新词。",
                  "一句话写四样东西，四个不同的颜色，用「、」和「和」。"),
                  FL, P)))

    m.append(("10-pattern.html", "I Do · 句型 · 穿。不是「是」。",
              page("L4-10 · 句型", "I Do · 句型 · 用动词回答", '''
  <div style="display:flex;flex-direction:column;gap:34px;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:36px;">
      <div class="card" style="border:3px solid var(--accent-madder);background:var(--accent-madder-dim);">
        <div class="badge badge-madder" style="margin-bottom:18px;">✗ 不对</div>
        <div class="qa-body">
          <span class="qa-hanzi">你上学穿校服吗？</span>
          <span class="qa-hanzi" style="color:var(--accent-madder);text-decoration:line-through;">是。</span>
        </div>
      </div>
      <div class="card" style="border:3px solid var(--accent-teal);background:var(--accent-teal-dim);">
        <div class="badge badge-teal" style="margin-bottom:18px;">✓ 对</div>
        <div class="qa-body">
          <span class="qa-hanzi">你上学穿校服吗？</span>
          <span class="qa-hanzi" style="color:var(--accent-teal);">穿。／不穿。</span>
        </div>
      </div>
    </div>
    <div class="info-box">
      <span class="info-icon">动</span>
      <span><span class="info-text">问句里是什么动词，答案就重复那个动词。</span>
      <span class="info-sub">你喜欢吗？→ 喜欢。　你有吗？→ 有。　你穿吗？→ 穿。 This is on the Unit Test, Part 9.</span></span>
    </div>
  </div>''', FL, P)))

    m.append(("11-qa-uniform.html", "I Do · 三个校服问题 · Revision p.171",
              page("L4-11 · 校服问答", "I Do · 三个问题 · 复习 p.171 要考的", qa([
                  ("q", "nǐ shàngxué chuān xiàofú ma", "你上学穿校服吗？", "Do you wear uniform to school?"),
                  ("a", "chuān", "穿。", "Yes (I do)."),
                  ("q", "nǐ chuān shénme xiàofú", "你穿什么校服？", "What uniform do you wear?"),
                  ("a", "báisè de chènshān hé lánsè de chángkù", "白色的衬衫和蓝色的长裤。",
                   "A white shirt and blue trousers."),
                  ("q", "nǐ xǐhuan nǐ de xiàofú ma", "你喜欢你的校服吗？", "Do you like your uniform?"),
                  ("a", "bù xǐhuan", "不喜欢。", "No (I don't)."),
              ]) + '''
  <div class="warning-box" style="margin-top:24px;">
    <span class="warn-icon">考</span>
    <span><span class="warn-text">中间那两个问题，课本里一次都没出现过。</span>
    <span class="warn-sub">你穿什么校服？and 你喜欢你的校服吗？are on the Revision list (练习册 p.171) but nowhere in the textbook lesson — which is why they are taught here.</span></span>
  </div>''',
                  FL, "轻松学中文 Book 1 · 练习册 p.171 复习 第 7 题", dense=True)))

    m.append(("12-cfu.html", "I Do · 检查 · CFU",
              page("L4-12 · CFU", "I Do · 检查一下 · Check for Understanding", cfu(
                  ["「<span class='cn'>你喜欢穿裙子吗？</span>」— 连着问五个同学，只听答案对不对。",
                   "老师故意说错，你们喊出正确的说法。",
                   "写下我们学校的答案：<span class='cn'>你穿什么校服？</span>"],
                  pairs=[("你上学穿校服吗？— 是。", "你上学穿校服吗？— 穿。"),
                         ("你喜欢你的校服吗？— 对。", "你喜欢你的校服吗？— 喜欢。")]),
                  FL, P, CFU_CSS)))

    m.append(("13-act1-survey.html", "We Do · 活动一 · 全班调查 (6 min)",
              page("L4-13 · 活动一", "Flexible Practice · We Do · 20–26 min", activity(
                  "We Do", "全班调查 · Class uniform survey", "6 min",
                  [("站起来，走动，问每个同学一个问题，用「正」字记数。",
                    "Stand up, move round the room, ask everyone and tally with 正."),
                   ("问题：<span class='cn'>你喜欢你的校服吗？</span>　喜欢 ／ 不喜欢",
                    "The question — tally 喜欢 against 不喜欢."),
                   ("回来报告，用第十三课的句型。", "Report back in the frame you learned in Lesson 13.")],
                  target=["十五个人不喜欢校服。<span class='py'>shíwǔ ge rén bù xǐhuan xiàofú</span>",
                          "<span class='en'>第十三课 p.101 的报告句型</span>五个人喜欢黑色。"],
                  extension="记完数以后再追问一句 <span class='cn'>你喜欢穿什么衣服？</span>，"
                            "报告的时候一句话说<b>两</b>件事 — "
                            "<span class='cn'>十五个人不喜欢校服，他们喜欢穿汗衫和牛仔裤。</span>",
                  source="课本 p.101 格式"),
                  FL, P, ACT_CSS)))

    m.append(("14-act2-roleplay.html", "You Do · 活动二 · 校服角色卡 (9 min)",
              page("L4-14 · 活动二", "Flexible Practice · You Do · 26–35 min", activity(
                  "You Do", "校服角色卡 · Uniform role-play", "9 min",
                  [("两人一组，每组两张卡片。卡片上是一所学校的校服。",
                    "Pairs, two printed cards each. Every card describes one school's uniform."),
                   ("A 拿着卡片当那所学校的学生，B 问三个问题。",
                    "A holds the card and is a student at that school. B asks the three questions."),
                   ("换卡片，换角色，再做一次。每个人都要做两遍。",
                    "Swap cards and roles, then run it again — everyone does it twice.")],
                  target=["<span class='en'>卡片</span>红星中学：白色的衬衫、灰色的裙子、黑色的袜子",
                          "B：你上学穿校服吗？　A：穿。",
                          "B：你穿什么校服？　A：我穿白色的衬衫、灰色的裙子和黑色的袜子。",
                          "B：你喜欢你的校服吗？　A：不喜欢。"],
                  extension="问的人<b>不看卡片</b>，要自己想追问的问题 — "
                            "<span class='cn'>你喜欢什么颜色？你今天穿什么衣服？</span>"
                            "最后凭记忆把对方学校的校服报给全班："
                            "<span class='cn'>他穿白色的衬衫和灰色的裙子，他不喜欢他的校服。</span>"
                            "<span class='sub'>Pair a fluent student with a less confident one and give them the interviewer's role.</span>"),
                  FL, P, ACT_CSS, dense=True)))

    m.append(("15-act3-listening.html", "You Do · 活动三 · 听一听，选颜色 T68 (4 min)",
              page("L4-15 · 活动三", "Flexible Practice · You Do · 35–39 min", activity(
                  "You Do", "听一听，选颜色 · Listen and choose", "4 min",
                  [("课本 p.109 第 7 题。听两遍，把字母写在小白板上，每题举一次。",
                    "Textbook Ex.7. Play twice; write the letter on a whiteboard and hold it up after each item."),
                   ("六题里三题是衣服，三题是车 — 单元测验也是这样混着考的。",
                    "Three garments and three vehicles, deliberately mixed — the Unit Test does the same.")],
                  target=["衬衫　牛仔裤　裙子",
                          "出租车　校车　电车"],
                  extension="不要只写字母，把<b>整句话</b>写下来 — "
                            "<span class='cn'>爸爸穿白色的衬衫。</span>",
                  source="课本 p.109 练习 7 · CD T68"),
                  FL, "轻松学中文 Book 1 · 课本 p.109 练习 7 · CD T68", ACT_CSS)))

    m.append(("16-game-slap.html", "Game · 抢词卡 · 配件版 (4 min)",
              page("L4-16 · Game", "Game · 抢词卡 · 39–43 min", activity(
                  "Game", "抢词卡 · 配件版", "4 min",
                  [("四个小组，黑板上十张卡片：今天的四个配件 + 六件学过的衣服。",
                    "Four teams. Ten cards: today's four accessories plus six known garments."),
                   ("老师说，第一个拍到的得分。", "Teacher calls; first hand scores.")],
                  target=["帽子　手套　围巾　袜子",
                          "衬衫　汗衫　毛衣　外套　校服　长裤"],
                  extension="老师改说<b>英文</b>，不说中文 — "
                            "<span class='sub'>no sound-matching shortcut; they have to know the word.</span>"),
                  FL, P, ACT_CSS)))

    m.append(("17-plenary.html", "Plenary · 出门条 (43–50 min)",
              page("L4-17 · Plenary", "Plenary · 回顾 · 自评 · 出门条", plenary(
                  ["我会用动词回答 — 穿。不是「是」。",
                   "我会问也会答「你穿什么校服？」",
                   "我会说 帽子、手套、围巾、袜子"],
                  "你上学穿校服吗？<br>你喜欢你的校服吗？",
                  "两个问题都用中文回答，写在小白板上。<br>"
                  "<span class='caption'>Answer both in Chinese.</span>"),
                  FL, P)))

    m.append(("18-preview.html", "Preview · 下一课",
              page("L4-18 · Preview", "Preview · 下一课", preview_slide(
                  "下一课 — 写。你要听录音写下六个人穿什么，还要把故意写错的字找出来。",
                  "Next lesson: writing. You'll describe six people from a recording, "
                  "and hunt for the deliberate character mistakes.",
                  "sneaker"), FL, P)))

    return write_deck("l4-school-uniform", m, "L4 · 校服 · 你上学穿校服吗？")


# ══════════════════════════════════════════════════════════════════════════
# LESSON 5 — describing outfits · writing-focused
# ══════════════════════════════════════════════════════════════════════════
def lesson5():
    FL, P = "Lesson 5 of 6 · 写：他穿什么？", "轻松学中文 Book 1 · Unit 5 · 课本 p.109–111"
    m = []

    m.append(("01-title.html", "Title · 他穿什么？",
              page("L5-01 · Title", "", title_slide(
                  5, "他穿什么？", "Writing What People Wear", "sneaker",
                  ["Year 7 Chinese", "50 分钟", "Writing-focused", "课本 p.109–111"]),
                  FL, P, TITLE_CSS)))

    m.append(("02-review.html", "Review · 图配词 (0–8 min)",
              page("L5-02 · Review", "Review · 练习册 p.153 第 12 题 · 0–8 min", activity(
                  "Review", "图配词 · Match the picture", "8 min",
                  [("练习册 p.153 第 12 题 — 九张图配九个词。四分钟，自己做，然后点名对答案。",
                    "Workbook Ex.12 — match nine garment pictures to nine words. Four minutes solo, then cold call."),
                   ("三分钟口头：老师连着问，不举手。",
                    "Three minutes oral — teacher fires questions, no hands up. Listening for the verb-repeat answer.")],
                  target=["校服　短裤　毛衣　衬衫　裙子　长裤　汗衫　外套　牛仔裤",
                          "你上学穿校服吗？　你喜欢穿裙子吗？　你喜欢穿短裤吗？"],
                  extension="配完以后，挑三个词各写一句，每句要有颜色。",
                  source="练习册 p.153"),
                  FL, "轻松学中文 Book 1 · 练习册 p.153 第 12 题", ACT_CSS, dense=True)))

    m.append(("03-li-sc.html", "Learning Intention & Success Criteria (8–10 min)",
              page("L5-03 · LI & SC", "目标 · Learning Intention & Success Criteria",
                   li_sc("我们学怎么写一个人穿什么。",
                         [("我会写「他／她穿 + 颜色的衣服 + 和 + 颜色的衣服」",
                           "I can write 他/她穿 + colour + 的 + garment 和 colour + 的 + garment"),
                          ("我找得出句子里写错的字，也改得对",
                           "I can find a wrong character in a clothing sentence and write the right one"),
                          ("我会说 皮鞋、运动鞋、西装、领带", "I can name 皮鞋, 运动鞋, 西装 and 领带")]),
                   FL, P)))

    m.append(("04-vocab-a1.html", "I Do · 生词 1 · 皮鞋 · 运动鞋",
              page("L5-04 · 生词 1", "I Do · 生词 · 第一组 · 课本 p.110 Extra Words", vocab_a([
                  {"hanzi": "皮鞋", "pinyin": "píxié", "en": "leather shoes", "art": "leathershoe"},
                  {"hanzi": "运动鞋", "pinyin": "yùndòngxié", "en": "sneakers", "art": "sneaker",
                   "clue": "<b>鞋</b> 的部首是「革」— 第十五课再学"},
              ]), FL, "轻松学中文 Book 1 · 课本 p.110 Extra Words")))

    m.append(("05-vocab-b1.html", "I Do · 例句 1 · 皮鞋 · 运动鞋",
              page("L5-05 · 例句 1", "I Do · 例句 · 皮鞋 · 运动鞋", vocab_b([
                  ("wǒ bàba chuān hēisè de píxié shàngbān", "我爸爸穿黑色的<b>皮鞋</b>上班。",
                   "My dad wears black leather shoes to work."),
                  ("wǒ měitiān chuān yùndòngxié shàngxué", "我每天穿<b>运动鞋</b>上学。",
                   "I wear sneakers to school every day."),
                  ("wǒ yǒu píxié hé yùndòngxié， wǒ xǐhuan chuān yùndòngxié",
                   "我有<b>皮鞋</b>和<b>运动鞋</b>，我喜欢穿<b>运动鞋</b>。",
                   "I have leather shoes and sneakers; I like wearing sneakers."),
              ], note=("你今天穿什么鞋？", "鞋 takes 穿 — unlike hats and gloves.")),
                  FL, P)))

    m.append(("06-vocab-c1.html", "I Do · 写一句 1",
              page("L5-06 · 写一句 1", "I Do · 写一句 · 皮鞋 · 运动鞋", vocab_c(
                  ["我每天穿<span class='blank'>　　　</span>色的<span class='blank'>　　　</span>上学。"],
                  "写一句。写在本子上，不是小白板。",
                  "写两个人，用第十二课的交通方式 — "
                  "<span class='cn'>我爸爸开车上班，他穿黑色的皮鞋；我坐校车上学，我穿白色的运动鞋。</span>"),
                  FL, P)))

    m.append(("07-vocab-a2.html", "I Do · 生词 2 · 西装 · 领带",
              page("L5-07 · 生词 2", "I Do · 生词 · 第二组", vocab_a([
                  {"hanzi": "西装", "pinyin": "xīzhuāng", "en": "suit", "art": "suit"},
                  {"hanzi": "领带", "pinyin": "lǐngdài", "en": "tie", "art": "tie",
                   "clue": "领带用「<b>有</b>」，不用「穿」"},
              ]), FL, P)))

    m.append(("08-vocab-b2.html", "I Do · 例句 2 · 西装 · 领带",
              page("L5-08 · 例句 2", "I Do · 例句 · 西装 · 领带", vocab_b([
                  ("wǒ bàba shàngbān chuān xīzhuāng", "我爸爸上班穿<b>西装</b>。",
                   "My dad wears a suit to work."),
                  ("tā de lǐngdài shì hóngsè de", "他的<b>领带</b>是红色的。", "His tie is red."),
                  ("wǒ gēge chuān hēisè de xīzhuāng hé lánsè de lǐngdài",
                   "我哥哥穿黑色的<b>西装</b>和蓝色的<b>领带</b>。",
                   "My older brother is wearing a black suit and a blue tie."),
              ], note=("谁上班穿西装？", "Answer with a full sentence.")),
                  FL, P)))

    m.append(("09-vocab-c2.html", "I Do · 写一句 2",
              page("L5-09 · 写一句 2", "I Do · 写一句 · 西装 · 领带", vocab_c(
                  ["<span class='blank'>　　　</span>穿<span class='blank'>　　　</span>色的西装。"],
                  "写一句。写在本子上。",
                  "给一个要上班的人配一整套衣服 — 西装、衬衫、领带、皮鞋，"
                  "四个颜色，一句话，「、」和「和」都要放对。"),
                  FL, P)))

    m.append(("10-board.html", "I Do · 十八件衣服 · Recall Board",
              page("L5-10 · 词汇总览", "I Do · 到现在学过的全部衣服 · 整节课都在屏幕上",
                   board([{"hanzi": "衬衫", "art": "shirt"}, {"hanzi": "汗衫", "art": "tee"},
                          {"hanzi": "毛衣", "art": "sweater"}, {"hanzi": "外套", "art": "coat"},
                          {"hanzi": "校服", "art": "uniform"}, {"hanzi": "衣服", "art": "clothes"},
                          {"hanzi": "牛仔裤", "art": "jeans"}, {"hanzi": "长裤", "art": "trousers"},
                          {"hanzi": "短裤", "art": "shorts"}, {"hanzi": "裙子", "art": "skirt"},
                          {"hanzi": "帽子", "art": "hat"}, {"hanzi": "手套", "art": "gloves"},
                          {"hanzi": "围巾", "art": "scarf"}, {"hanzi": "袜子", "art": "socks"},
                          {"hanzi": "皮鞋", "art": "leathershoe"}, {"hanzi": "运动鞋", "art": "sneaker"},
                          {"hanzi": "西装", "art": "suit"}, {"hanzi": "领带", "art": "tie"}],
                         cols=6),
                   FL, P)))

    m.append(("11-pattern.html", "I Do · 句型 · 他穿 A 和 B",
              page("L5-11 · 句型", "I Do · 句型 · 他穿……和……", pattern(
                  "他/她 穿 <span class='slot'>颜色的衣服</span> 和 <span class='slot'>颜色的衣服</span> 。",
                  [("tā chuān báisè de hànshān hé chéngsè de duǎnkù",
                    "他穿白色的汗衫和橙色的短裤。",
                    "He's wearing a white T-shirt and orange shorts."),
                   ("tā chuān fěnhóngsè de chènshān hé zǐsè de qúnzi",
                    "她穿粉红色的衬衫和紫色的裙子。",
                    "She's wearing a pink shirt and a purple skirt."),
                   ("jīngjing chuān lǜsè de wàitào hé hēisè de chángkù",
                    "京京穿绿色的外套和黑色的长裤。",
                    "Jingjing is wearing a green coat and black trousers."),
                   ("wáng xiǎomíng jīntiān chuān chéngsè de chènshān、 hēisè de chángkù hé "
                    "báisè de yùndòngxié， tā bù chuān xiàofú",
                    "王小明今天穿橙色的衬衫<b>、</b>黑色的长裤<b>和</b>白色的运动鞋，"
                    "<b>他不穿校服</b>。",
                    "Wang Xiaoming is wearing an orange shirt, black trousers and white sneakers "
                    "today — he isn't wearing uniform.")]),
                  FL, P, dense=True)))

    m.append(("12-cfu.html", "I Do · 检查 · CFU",
              page("L5-12 · CFU", "I Do · 检查一下 · Check for Understanding", cfu(
                  ["怎么写 <b>brown leather shoes</b>？",
                   "这句哪里不对？ <span class='cn'>他穿白色汗衫。</span>",
                   "这句哪里不对？ <span class='cn'>他穿午仔裤。</span>"],
                  pairs=[("他穿白色汗衫。", "他穿白色的汗衫。"),
                         ("午仔裤", "牛仔裤")]),
                  FL, P, CFU_CSS)))

    m.append(("13-act1-dictation.html", "We Do · 活动一 · 听写 + 对照 T69 (7 min)",
              page("L5-13 · 活动一", "Flexible Practice · We Do · 20–27 min", activity(
                  "We Do", "听写 + 对照 · Dictation and check", "7 min",
                  [("课本 p.111 第 9 题。每一句放两遍，把听到的<b>整句话</b>写在本子上。",
                    "Textbook Ex.9. Each line played twice — write the full sentence in your book, not just a tick."),
                   ("写完以后看图，自己给自己打勾或画叉。",
                    "Then look at the six pictures and tick or cross your own sentence against them."),
                   ("第一句录音说的是「白汗衫」，不是「白色的汗衫」。说话可以省，写字不省。",
                    "Item 1 says 白汗衫, not 白色的汗衫 — spoken Chinese drops it, written work here keeps it.")],
                  target=["大生穿白汗衫，蓝短裤。",
                          "小文穿粉红色的衬衫，紫色的裙子。",
                          "京京穿绿色的外套，黑色的长裤。"],
                  extension="写完六句以后，把<b>画叉的两句改对</b> — 改成和图一样的句子，"
                            "<span class='sub'>which means producing a corrected sentence, not just marking a cross.</span>",
                  source="课本 p.111 练习 9 · CD T69"),
                  FL, "轻松学中文 Book 1 · 课本 p.111 练习 9 · CD T69", ACT_CSS, dense=True)))

    m.append(("14-act2-writing.html", "You Do · 活动二 · 写描述 + 找错字 (10 min)",
              page("L5-14 · 活动二", "Flexible Practice · You Do · 27–37 min", activity(
                  "You Do", "写描述 · 找错字", "10 min",
                  [("A · 课本 p.109 第 6 题 — 四个人，每人写一整句。第一句一起写。",
                    "Part A (4 min) — write a full sentence for each of the four people. Model the first together."),
                   ("B · 课本 p.110 第 8 题 — 十五样东西，颜色 + 的 + 衣服，这次用写的。三分钟写多少算多少。",
                    "Part B (3 min) — fifteen items, written this time. Nobody is expected to finish fifteen."),
                   ("C · 练习册 p.156 第 19 题 — 五句话，找出错字写对。第一题已经做好了：午仔裤 → 牛。",
                    "Part C (3 min) — spot the mistake in five sentences. This is Unit Test Part 8 in miniature.")],
                  target=["他穿白色的汗衫和橙色的短裤。",
                          "<span class='en'>找错字</span>他喜欢穿衬衫和<b>午</b>仔裤。 → 牛"],
                  extension="A 部分每个人写<b>两</b>句 — 穿什么，还有一件<b>没</b>穿的："
                            "<span class='cn'>他穿白色的汗衫和橙色的短裤，他不穿外套。</span>"
                            "<span class='sub'>For Part C, then write a sentence of your own with a deliberate error, swap with a partner, and have them find it.</span>",
                  source="课本 p.109–110 · 练习册 p.156"),
                  FL, "轻松学中文 Book 1 · 课本 p.109 练习 6, p.110 练习 8 · 练习册 p.156 第 19 题", ACT_CSS, dense=True)))

    m.append(("15-game-wordsearch.html", "Game · 找词竞赛 (6 min)",
              page("L5-15 · Game", "Game · 找词竞赛 · 37–43 min", activity(
                  "Game", "找词竞赛 · Word-search race", "6 min",
                  [("练习册 p.156 第 18 题 — 六乘六的字格，横着竖着藏了十二个词。",
                    "Workbook Ex.18 — a 6×6 character grid with twelve phrases hidden across and down."),
                   ("三人一组，圈出来再写下来。先找齐十二个的那组赢。",
                    "Teams of three: circle them and write them out. First team with all twelve wins."),
                   ("没有组找齐的话，找得最多的那组得分。",
                    "If nobody finishes, most-correct takes the point.")],
                  target=["衬衫　汗衫　校服　长裙　短裤",
                          "地铁　走路　公共汽车　粉红色　上学　中午　独生子"],
                  extension="赢的那组要把十二个词一个一个念出来，还要说英文 — "
                            "<span class='sub'>no reading the English off the page.</span>",
                  source="练习册 p.156 第 18 题"),
                  FL, "轻松学中文 Book 1 · 练习册 p.156 第 18 题", ACT_CSS)))

    m.append(("16-plenary.html", "Plenary · 出门条 (43–50 min)",
              page("L5-16 · Plenary", "Plenary · 回顾 · 自评 · 出门条", plenary(
                  ["我会写「他穿……和……」",
                   "我找得出错字，也改得对",
                   "我会说 皮鞋、运动鞋、西装、领带"],
                  "看屏幕上的人。<br>写一句话，两件衣服，两个颜色。",
                  "<span class='caption'>Look at the person on the screen. "
                  "Write one sentence describing what they're wearing.</span>"),
                  FL, P)))

    m.append(("17-preview.html", "Preview · 下一课",
              page("L5-17 · Preview", "Preview · 下一课", preview_slide(
                  "下一课 — 最后一课。读黄铁牛的故事，互相采访，"
                  "再给聚会上的陌生人写一份介绍。",
                  "Next lesson, the last one: read about 黄铁牛, interview each other about "
                  "everything from this year, and write a profile of a stranger at a party.",
                  "gown"), FL, P)))

    return write_deck("l5-describing-outfits", m, "L5 · 写：他穿什么？")


# ══════════════════════════════════════════════════════════════════════════
# LESSON 6 — profiles · mixed
# ══════════════════════════════════════════════════════════════════════════
def lesson6():
    FL, P = "Lesson 6 of 6 · 介绍一个人", "轻松学中文 Book 1 · Unit 5 · 课本 p.112–113"
    m = []

    m.append(("01-title.html", "Title · 介绍一个人",
              page("L6-01 · Title", "", title_slide(
                  6, "介绍一个人", "Profiles — Describing a Whole Person", "gown",
                  ["Year 7 Chinese", "50 分钟", "Mixed", "课本 p.112–113"]),
                  FL, P, TITLE_CSS)))

    m.append(("02-review.html", "Review · 十八件衣服配对赛 (0–8 min)",
              page("L6-02 · Review", "Review · 看图写汉字 · 0–8 min",
                   board([{"hanzi": "衬衫", "art": "shirt"}, {"hanzi": "汗衫", "art": "tee"},
                          {"hanzi": "毛衣", "art": "sweater"}, {"hanzi": "外套", "art": "coat"},
                          {"hanzi": "校服", "art": "uniform"}, {"hanzi": "衣服", "art": "clothes"},
                          {"hanzi": "牛仔裤", "art": "jeans"}, {"hanzi": "长裤", "art": "trousers"},
                          {"hanzi": "短裤", "art": "shorts"}, {"hanzi": "裙子", "art": "skirt"},
                          {"hanzi": "帽子", "art": "hat"}, {"hanzi": "手套", "art": "gloves"},
                          {"hanzi": "围巾", "art": "scarf"}, {"hanzi": "袜子", "art": "socks"},
                          {"hanzi": "皮鞋", "art": "leathershoe"}, {"hanzi": "运动鞋", "art": "sneaker"},
                          {"hanzi": "西装", "art": "suit"}, {"hanzi": "领带", "art": "tie"}],
                         cols=6,
                         caption="三分钟，能写几个写几个 — 然后自己数一数，满分十八"),
                   FL, P)))

    m.append(("03-li-sc.html", "Learning Intention & Success Criteria (8–10 min)",
              page("L6-03 · LI & SC", "目标 · Learning Intention & Success Criteria",
                   li_sc("我们学怎么写一个人的介绍，里面要有他穿什么。",
                         [("我会问也会答「你喜欢穿什么衣服？」「你今天穿什么衣服？」",
                           "I can ask and answer 你喜欢穿什么衣服？ and 你今天穿什么衣服？"),
                          ("我看得懂一段介绍，答得出关于衣服的问题",
                           "I can read a passage about someone and answer questions about their clothes"),
                          ("我会写一个人的介绍，用上今年学过的至少三样东西",
                           "I can write a short profile using at least three things I've learned this year")])
                   + '''
  <div class="info-box" style="margin-top:30px;">
    <span class="info-icon">今</span>
    <span><span class="info-text">今年学过的：名字 · 年龄 · 年级 · 国家 · 家人 · 时间 · 上学 · 颜色 · 衣服</span>
    <span class="info-sub">Nine topics from nine lessons — this list stays on the board as the scaffold for the writing task.</span></span>
  </div>''',
                   FL, P)))

    m.append(("04-vocab-a1.html", "I Do · 生词 1 · 长衫 · 大衣",
              page("L6-04 · 生词 1", "I Do · 生词 · 第一组 · 练习册 p.152 查字典", vocab_a([
                  {"hanzi": "长衫", "pinyin": "chángshān", "en": "long gown", "art": "gown",
                   "clue": "<b>长</b> + <b>衫</b> — 两个字都学过"},
                  {"hanzi": "大衣", "pinyin": "dàyī", "en": "overcoat", "art": "overcoat",
                   "clue": "<b>大</b> + <b>衣</b> — 两个字都学过"},
              ]) + '''
  <div class="note-box" style="margin-top:30px;">
    <span class="note-icon">读</span>
    <span><span class="note-text">这四个词，你差不多已经会读了。</span>
    <span class="note-sub">Every one is built from characters you already know. 长衫 even appeared back in Lesson 1 — you coloured a 棕色的长衫 without being told what it was.</span></span>
  </div>''',
                  FL, "轻松学中文 Book 1 · 练习册 p.152 第 10 题", dense=True)))

    m.append(("05-vocab-b1.html", "I Do · 例句 1 · 长衫 · 大衣",
              page("L6-05 · 例句 1", "I Do · 例句 · 长衫 · 大衣", vocab_b([
                  ("zhè shì zhōngguó de chángshān", "这是中国的<b>长衫</b>。",
                   "This is a Chinese long gown."),
                  ("wǒ māma xǐhuan hēisè de dàyī", "我妈妈喜欢黑色的<b>大衣</b>。",
                   "My mum likes black overcoats."),
                  ("wǒ māma xǐhuan chuān dàyī， wǒ bù xǐhuan， wǒ xǐhuan chángshān",
                   "我妈妈喜欢穿<b>大衣</b>，我不喜欢，我喜欢<b>长衫</b>。",
                   "My mum likes wearing an overcoat; I don't, I like a long gown."),
              ], note=("「长衫」的「长」念 cháng 还是 zhǎng？", "Same character, two readings — this one is cháng.")),
                  FL, P)))

    m.append(("06-vocab-c1.html", "I Do · 写一句 1",
              page("L6-06 · 写一句 1", "I Do · 写一句 · 长衫 · 大衣", vocab_c(
                  ["我<span class='blank'>　　　</span>喜欢穿<span class='blank'>　　　</span>。"],
                  "写一句。",
                  "光看汉字，猜猜 <span class='cn'>长裙</span> 和 <span class='cn'>短裙</span> 是什么意思，"
                  "再用其中一个写一句。"),
                  FL, P)))

    m.append(("07-vocab-a2.html", "I Do · 生词 2 · 风衣 · 连衣裙",
              page("L6-07 · 生词 2", "I Do · 生词 · 第二组", vocab_a([
                  {"hanzi": "风衣", "pinyin": "fēngyī", "en": "windbreaker", "art": "windbreaker"},
                  {"hanzi": "连衣裙", "pinyin": "liányīqún", "en": "dress", "art": "dress",
                   "clue": "<b>衣</b> + <b>裙</b> 连在一起"},
              ]), FL, P)))

    m.append(("08-vocab-b2.html", "I Do · 例句 2 · 风衣 · 连衣裙",
              page("L6-08 · 例句 2", "I Do · 例句 · 风衣 · 连衣裙", vocab_b([
                  ("wǒ jiějie yǒu fěnhóngsè de liányīqún", "我姐姐有粉红色的<b>连衣裙</b>。",
                   "My older sister has a pink dress."),
                  ("wǒ bàba xǐhuan chuān fēngyī", "我爸爸喜欢穿<b>风衣</b>。",
                   "My dad likes wearing a windbreaker."),
                  ("wǒ māma xǐhuan chuān liányīqún， wǒ bàba xǐhuan chuān fēngyī",
                   "我妈妈喜欢穿<b>连衣裙</b>，我爸爸喜欢穿<b>风衣</b>。",
                   "My mum likes wearing dresses, my dad likes a windbreaker."),
              ], note=("为什么叫「连衣裙」？", "Explain it in Chinese using only words you know.")),
                  FL, P)))

    m.append(("09-vocab-c2.html", "I Do · 写一句 2",
              page("L6-09 · 写一句 2", "I Do · 写一句 · 风衣 · 连衣裙", vocab_c(
                  ["<span class='blank'>　　　</span>有<span class='blank'>　　　</span>色的连衣裙。"],
                  "写一句。",
                  "用你会的词解释「连衣裙」为什么叫连衣裙 — "
                  "<span class='cn'>连衣裙是衣服和裙子。</span>"),
                  FL, P)))

    m.append(("10-pattern.html", "I Do · 句型 · 一份介绍",
              page("L6-10 · 句型", "I Do · 句型 · 一份介绍怎么写", pattern(
                  "这是 <span class='slot'>人</span> 。 他今年 <span class='slot'>几</span> 岁，"
                  "上 <span class='slot'>几</span> 年级。",
                  [("zhè shì wáng xiǎomíng", "这是王小明。", "This is Wang Xiaoming."),
                   ("tā jīnnián shí'èr suì， shàng qī niánjí", "他今年十二岁，上七年级。",
                    "He's twelve this year and in Year 7."),
                   ("tā měitiān zuò xiàochē shàngxué", "他每天坐校车上学。",
                    "He takes the school bus to school every day."),
                   ("tā shàngxué chuān xiàofú： báisè de chènshān hé lánsè de chángkù",
                    "他上学穿校服：白色的衬衫和蓝色的长裤。",
                    "He wears uniform to school: a white shirt and blue trousers.")]),
                  FL, P, dense=True)))

    m.append(("10b-model-profile.html", "  ↳ 范文 · The whole profile",
              page("L6-10b · 范文", "I Do · 句型 · 六句话，五个单元", '''
  <div class="model">
    <div class="m-line">这是王小明。</div>
    <div class="m-line">他今年十二岁，上七年级。</div>
    <div class="m-line">他每天坐校车上学。</div>
    <div class="m-line">他上学穿校服：白色的衬衫和蓝色的长裤。</div>
    <div class="m-line last">他不喜欢校服，他喜欢穿汗衫和牛仔裤。</div>
  </div>
  <div class="info-box" style="margin-top:30px;">
    <span class="info-icon">五</span>
    <span><span class="info-text">六句话，五个单元的内容。</span>
    <span class="info-sub">名字 · 年龄 · 年级 · 上学 · 衣服 — five topics from five different lessons, in one short paragraph. This is what you are writing in Activity 2.</span></span>
  </div>''',
                  FL, P, '''
  .model { background:var(--bg-tertiary); border-left:6px solid var(--accent-indigo);
           border-radius:0 var(--radius-lg) var(--radius-lg) 0; padding:32px 40px; }
  .m-line { font-family:var(--font-display); font-size:50px; font-weight:700;
            color:var(--text-primary); line-height:1.5; }
  .m-line.last { color:var(--accent-madder); }''')))

    m.append(("11-text-huangtieniu.html", "I Do · 阅读 · 黄铁牛 (练习册 p.157)",
              page("L6-11 · 黄铁牛", "I Do · 阅读理解 · 黄铁牛", text_slide(
                  [("wǒ jiào huáng tiěniú。 wǒ shì běijīng rén。 wǒ jīnnián shí'èr suì， "
                    "shàng qī niánjí。 wǒmen yì jiā rén xiànzài zhù zài xiānggǎng。",
                    "我叫黄铁牛。我是北京人。我今年十二岁，上七年级。我们一家人现在住在香港。"),
                   ("wǒ jiā yǒu sān kǒu rén： bàba、 māma hé wǒ。 wǒ bàba měitiān jiǔ diǎn "
                    "shàngbān。 tā zuò gōnggòng qìchē shàngbān。 tā xǐhuan chuān chènshān hé chángkù。",
                    "我家有三口人：爸爸、妈妈和我。我爸爸每天九点上班。他坐公共汽车上班。"
                    "他喜欢穿衬衫和长裤。"),
                   ("wǒ māma bù gōngzuò。 tā xǐhuan chuān qúnzi。",
                    "我妈妈不工作。她喜欢穿裙子。"),
                   ("wǒ měitiān bā diǎn shàngxué， xiàwǔ sì diǎn fàngxué。 "
                    "wǒ xǐhuan chuān hànshān hé niúzǎikù。",
                    "我每天八点上学，下午四点放学。我喜欢穿汗衫和牛仔裤。")],
                  ),
                  FL, "轻松学中文 Book 1 · 练习册 p.157 第 20 题", dense=True)))

    m.append(("11b-huangtieniu-questions.html", "  ↳ 黄铁牛 · 八个问题",
              page("L6-11b · 黄铁牛问题", "I Do · 阅读理解 · 八个问题", '''
  <div class="q-grid">
    <div class="q"><span class="q-n">1</span>黄铁牛今年上几年级？</div>
    <div class="q"><span class="q-n">2</span>他每天几点上学？</div>
    <div class="q"><span class="q-n">3</span>他爸爸工作吗？</div>
    <div class="q"><span class="q-n">4</span>他爸爸喜欢穿什么衣服？</div>
    <div class="q"><span class="q-n">5</span>他爸爸每天怎么上班？</div>
    <div class="q"><span class="q-n">6</span>他妈妈工作吗？</div>
    <div class="q"><span class="q-n">7</span>他妈妈喜欢穿什么衣服？</div>
    <div class="q"><span class="q-n">8</span>他喜欢穿什么衣服？</div>
  </div>
  <div class="tip-box" style="margin-top:30px;">
    <span class="tip-icon">范</span>
    <span><span class="tip-text">这段就是待会儿你要写的介绍的范文。</span>
    <span class="tip-sub">Keep the passage up beside these — it is the model for the writing task in Activity 2.</span></span>
  </div>''',
                  FL, "轻松学中文 Book 1 · 练习册 p.157 第 20 题", '''
  .q-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px 44px; }
  .q { display:flex; align-items:flex-start; gap:18px;
       font-family:var(--font-display); font-size:42px; font-weight:700;
       color:var(--text-primary); line-height:1.35; }
  .q-n { font-family:var(--font-body); font-size:26px; font-weight:700;
         color:var(--accent-madder); opacity:0.55; min-width:32px; padding-top:10px; }''')))

    m.append(("12-act1-interview.html", "We Do · 活动一 · 采访 (6 min)",
              page("L6-12 · 活动一", "Flexible Practice · We Do · 20–26 min", activity(
                  "We Do", "采访两个同学 · Interview", "6 min",
                  [("课本 p.112 第 11 题，十四个问题里挑七个 — 待会儿写介绍要用的那七个。",
                    "Textbook Ex.11, seven of the fourteen questions — the ones that feed the profile."),
                   ("采访<b>两</b>个同学，把答案记在 Notes 那一栏。",
                    "Interview TWO partners and note the answers in the Notes column."),
                   ("两个人报告，用课本的句型：他叫……",
                    "Two students report back in the textbook's frame: 他叫……")],
                  target=["你叫什么名字？　你今年多大了？　你上几年级？",
                          "你每天怎么上学？　你喜欢什么颜色？",
                          "你喜欢穿什么衣服？　你今天穿什么衣服？"],
                  extension="不看问题表，用中文采访，还要自己加一个问题。"
                            "报告的时候说成<b>一段话</b>，不是一条一条 — "
                            "<span class='cn'>他叫大生，今年十二岁，上七年级。他每天走路上学，"
                            "他喜欢蓝色，今天穿蓝色的汗衫和黑色的短裤。</span>",
                  source="课本 p.112 练习 11"),
                  FL, "轻松学中文 Book 1 · 课本 p.112 练习 11", ACT_CSS, dense=True)))

    m.append(("13-act2-profile.html", "You Do · 活动二 · 写介绍 (10 min)",
              page("L6-13 · 活动二", "Flexible Practice · You Do · 26–36 min", activity(
                  "You Do", "写介绍 · Write the profile", "10 min",
                  [("A · 写你采访的一个同学。至少四句，其中两句写衣服。黄铁牛那段留在屏幕上当范文。",
                    "Part A (5 min) — profile one of the people you interviewed. Minimum four sentences, "
                    "at least two about clothes."),
                   ("B · 课本 p.113 第 12 题 — 聚会的图。挑两个人，给他们各写一份介绍。",
                    "Part B (5 min) — the party scene. Choose two people and write a profile for each."),
                   ("这两个是陌生人，所有内容都是你编的。开头用「这是……」或者「这个人是……」",
                    "These are strangers, so everything is invented. Start each with 这是…… or 这个人是……")],
                  target=["这是王小明。他今年十二岁，上七年级。",
                          "他每天坐校车上学。他上学穿校服：白色的衬衫和蓝色的长裤。"],
                  extension="写三份，不是两份。其中一份要让全班光凭<b>衣服</b>就认得出是图里哪个人 — "
                            "念出来，让大家指。"
                            "<span class='sub'>No word bank, no summary board — turn away from the screen.</span>",
                  source="课本 p.113 练习 12"),
                  FL, "轻松学中文 Book 1 · 课本 p.113 练习 12", ACT_CSS, dense=True)))

    m.append(("14-game-dictionary.html", "Game · 查字典接力 (7 min)",
              page("L6-14 · Game", "Game · 查字典接力 · 36–43 min", activity(
                  "Game", "查字典接力 · Dictionary relay", "7 min",
                  [("三人一组，一本字典或者一台平板。练习册 p.152 第 10 题，十个词。",
                    "Teams of three, one dictionary or device each. Workbook Ex.10 — ten words."),
                   ("十个里面有九个你今天以前就见过了，真正的新词只有「和服」一个。",
                    "Nine of the ten you already know — only 和服 is genuinely new."),
                   ("所以比的不是认字，是<b>查得快不快</b>。全写对的第一组赢。",
                    "So this is a dictionary-skills race, not a vocabulary hunt. First team correct wins.")],
                  target=["和服　长衫　袜子　皮鞋　西装",
                          "手套　大衣　风衣　帽子　连衣裙"],
                  extension="用<b>部首</b>查，不用拼音查 — 和服查「禾」，袜子查「衤」。"
                            "<span class='sub'>And the team has to say which radical they used for each word.</span>",
                  source="练习册 p.152 第 10 题"),
                  FL, "轻松学中文 Book 1 · 练习册 p.152 第 10 题", ACT_CSS, dense=True)))

    m.append(("15-plenary.html", "Plenary · 回顾六节课 (43–50 min)",
              page("L6-15 · Plenary", "Plenary · 回顾整个单元 · 自评 · 出门条", plenary(
                  ["我会用「穿」说谁穿什么",
                   "我会用「的」把颜色放在衣服前面",
                   "我会用「、」和「和」一次说好几件",
                   "我会用动词回答 — 穿。不是「是」。",
                   "我会写一个人穿什么",
                   "我会写一个人的介绍"],
                  "我不喜欢穿校服。",
                  "翻译成中文。<br><span class='caption'>Translate: I do not like wearing school uniform. "
                  "(练习册 p.154 第 16 题 — and Unit Test Part 10.)</span>",
                  wide=True), FL, "轻松学中文 Book 1 · 练习册 p.154 第 16 题")))

    m.append(("16-arc.html", "Plenary · 六节课走过来 · The Sequence",
              page("L6-16 · Arc", "Plenary · 这六节课我们走过的路", '''
  <div class="arc-grid">
    <div class="arc"><span class="arc-n">1</span><span class="arc-cn">穿</span>
      <span class="arc-en">the verb, and three garments</span></div>
    <div class="arc"><span class="arc-n">2</span><span class="arc-cn">颜色的衣服</span>
      <span class="arc-en">colour + 的 + garment · 长 and 短</span></div>
    <div class="arc"><span class="arc-n">3</span><span class="arc-cn">你喜欢穿什么衣服？</span>
      <span class="arc-en">the question, and listing with 、和</span></div>
    <div class="arc"><span class="arc-n">4</span><span class="arc-cn">校服</span>
      <span class="arc-en">穿。 not 是。</span></div>
    <div class="arc"><span class="arc-n">5</span><span class="arc-cn">他穿什么？</span>
      <span class="arc-en">writing it down</span></div>
    <div class="arc last"><span class="arc-n">6</span><span class="arc-cn">介绍一个人</span>
      <span class="arc-en">the whole person</span></div>
  </div>''',
                  FL, P, '''
  .arc-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:28px; }
  .arc { background:var(--bg-secondary); border:2px solid var(--border-light);
         border-radius:var(--radius-lg); padding:28px 26px; display:flex;
         flex-direction:column; gap:10px; }
  .arc.last { border-color:var(--accent-madder); background:var(--accent-madder-dim); }
  .arc-n { font-family:var(--font-display); font-size:44px; font-weight:900;
           color:var(--accent-indigo); opacity:0.35; line-height:1; }
  .arc-cn { font-family:var(--font-display); font-size:48px; font-weight:700;
            color:var(--text-primary); line-height:1.25; }
  .arc-en { font-size:26px; color:var(--text-secondary); }''')))

    m.append(("17-preview.html", "Preview · 下一课 · 第十五课",
              page("L6-17 · Preview", "Preview · 下一课", preview_slide(
                  "下一课 — 第十五课：人体部位。<br>"
                  "还是这个「的」，只是后面换成了眼睛、鼻子和头发。",
                  "Next lesson — Lesson 15: Parts of the Body. The same 的 you've used all week, "
                  "but what comes after it is eyes, noses and hair."),
                  FL, "轻松学中文 Book 1 · 第十五课 人体部位 · 课本 p.114")))

    return write_deck("l6-profiles", m, "L6 · 介绍一个人 · Profiles")
