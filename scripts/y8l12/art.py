# -*- coding: utf-8 -*-
"""SVG drawings for the Y8 L12 外出就餐 deck series.

Flat line drawings, 200x200 viewBox, in the same hand as the y8-l10 and
y8-l11 sets next door: chunky strokes, the unit's muted palette, no faces,
no gradients, no emoji. Emoji render as empty boxes through the Chromium
export path, which is why every visual in this series is a real SVG.

Only the money and market vocabulary is drawn here. Anything already drawn
for Lesson 10 or Lesson 11 (fruit, dishes, the restaurant, the rating hands)
is copied across by build.py rather than redrawn — one apple in the unit.

Run:  python3 scripts/y8l12/art.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y8-l12", "img")

# Unit 4 palette, shared with y8-l10 / y8-l11
INK   = "#33531C"   # dark green outline
GREEN = "#4C7A2C"
LEAF  = "#5C8A3A"
ORNG  = "#B96A12"
TOM   = "#B93F2C"
GOLD  = "#D8A93C"
PAPER = "#F2EFDE"
NOTE  = "#C9D8C0"   # banknote green
NOTE2 = "#E3CBD8"   # banknote pink (the 100)
COIN  = "#D9C48A"
COIN2 = "#C0C4C8"   # silver
BROWN = "#7E5A2E"
SLATE = "#4E5A42"


def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" '
            'width="200" height="200">' + body + '</svg>')


def note(x, y, w, h, fill, label, lx=None, ly=None, fs=30):
    """A banknote: rounded rect, an inner rule, and the denomination."""
    lx = x + w / 2 if lx is None else lx
    ly = y + h / 2 + fs * 0.35 if ly is None else ly
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" '
            f'stroke="{INK}" stroke-width="5"/>'
            f'<rect x="{x+7}" y="{y+7}" width="{w-14}" height="{h-14}" rx="3" fill="none" '
            f'stroke="{INK}" stroke-width="2.5" opacity=".45"/>'
            f'<text x="{lx}" y="{ly}" font-family="Georgia,serif" font-size="{fs}" '
            f'font-weight="700" fill="{INK}" text-anchor="middle">{label}</text>')


def coin(cx, cy, r, fill, label, fs=30):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r-8}" fill="none" stroke="{INK}" '
            f'stroke-width="2.5" opacity=".45"/>'
            f'<text x="{cx}" y="{cy + fs*0.35}" font-family="Georgia,serif" font-size="{fs}" '
            f'font-weight="700" fill="{INK}" text-anchor="middle">{label}</text>')


ART = {}

# ── Lesson 1 · the money words ──────────────────────────────────────
# 钱 — money in general: a couple of notes with coins in front.
ART["qian"] = svg(
    note(24, 54, 116, 62, NOTE, "¥") +
    note(44, 78, 116, 62, NOTE2, "¥") +
    coin(52, 152, 26, COIN, "") +
    coin(104, 158, 22, COIN2, ""))

# 块 — the spoken yuan: the ¥1 note.
ART["kuai"] = svg(note(16, 62, 168, 82, NOTE, "1", fs=46))

# 元 — the written yuan: the same note, showing 壹圆.
ART["yuan"] = svg(
    note(16, 62, 168, 82, NOTE, "1", lx=70, ly=118, fs=46) +
    f'<text x="140" y="112" font-family="Georgia,serif" font-size="26" font-weight="700" '
    f'fill="{INK}" text-anchor="middle" opacity=".8">壹圆</text>')

# 毛 — 1/10 yuan, spoken: the 5 jiao coin.
ART["mao"] = svg(coin(100, 100, 66, COIN, "5", fs=52))

# 角 — 1/10 yuan, written: the 1 jiao note showing 壹角.
ART["jiao"] = svg(
    note(24, 70, 152, 68, NOTE, "1", lx=70, ly=112, fs=40) +
    f'<text x="140" y="108" font-family="Georgia,serif" font-size="22" font-weight="700" '
    f'fill="{INK}" text-anchor="middle" opacity=".8">壹角</text>')

# 分 — 1/100 yuan: the smallest coin, drawn small against a faint outline
# of the 1 yuan coin so the size difference reads.
ART["fen"] = svg(
    f'<circle cx="100" cy="100" r="64" fill="none" stroke="{INK}" stroke-width="3" '
    f'stroke-dasharray="7 7" opacity=".4"/>' +
    coin(100, 100, 34, COIN2, "1", fs=28))

# ── Lesson 2 · buying and selling ───────────────────────────────────
# 买 — buy: a shopping basket with produce, a note dropping in.
# Drawn as a basket rather than a hand: hands at this size read as
# squiggles, and nothing else in the unit's art has one.
ART["mai-buy"] = svg(
    note(52, 16, 108, 50, NOTE, "\u00a5", fs=28) +
    f'<path d="M26 92h148l-16 84c-1 8-8 14-16 14H58c-8 0-15-6-16-14z" fill="{PAPER}" '
    f'stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    f'<path d="M18 92h164" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M70 92V74c0-16 13-29 30-29s30 13 30 29v18" fill="none" stroke="{INK}" '
    f'stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M64 112l8 66M100 112v66M136 112l-8 66" stroke="{INK}" stroke-width="3.5" opacity=".45"/>')

# 卖 — sell: a stall awning over a counter with produce on it.
ART["mai-sell"] = svg(
    f'<path d="M20 34h160l14 40H6z" fill="{TOM}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M6 74h188" stroke="{INK}" stroke-width="5"/>'
    f'<path d="M48 34v40M100 34v40M152 34v40" stroke="{INK}" stroke-width="3.5" opacity=".5"/>'
    f'<rect x="26" y="128" width="148" height="46" rx="6" fill="{BROWN}" stroke="{INK}" stroke-width="5"/>'
    f'<circle cx="62" cy="112" r="20" fill="{TOM}" stroke="{INK}" stroke-width="5"/>'
    f'<circle cx="104" cy="112" r="20" fill="{LEAF}" stroke="{INK}" stroke-width="5"/>'
    f'<circle cx="146" cy="112" r="20" fill="{ORNG}" stroke="{INK}" stroke-width="5"/>')

# 斤 — half a kilo: a pan balance, vegetables in the left bowl.
ART["jin"] = svg(
    f'<path d="M100 26v122" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M62 168h76" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M100 148c-14 0-22 8-24 20M100 148c14 0 22 8 24 20" fill="none" stroke="{INK}" stroke-width="6"/>'
    f'<path d="M34 50h132" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
    f'<circle cx="100" cy="50" r="9" fill="{GOLD}" stroke="{INK}" stroke-width="5"/>'
    f'<path d="M40 50v22M160 50v22" stroke="{INK}" stroke-width="4"/>'
    f'<path d="M12 72h56c0 22-13 34-28 34S12 94 12 72z" fill="{PAPER}" stroke="{INK}" '
    f'stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M132 72h56c0 22-13 34-28 34s-28-12-28-34z" fill="{PAPER}" stroke="{INK}" '
    f'stroke-width="5" stroke-linejoin="round"/>'
    f'<circle cx="30" cy="64" r="12" fill="{LEAF}" stroke="{INK}" stroke-width="4"/>'
    f'<circle cx="52" cy="64" r="12" fill="{TOM}" stroke="{INK}" stroke-width="4"/>')

# 一共 — altogether: three items braced into one total.
ART["yigong"] = svg(
    f'<circle cx="46" cy="42" r="22" fill="{TOM}" stroke="{INK}" stroke-width="5"/>'
    f'<circle cx="46" cy="98" r="22" fill="{LEAF}" stroke="{INK}" stroke-width="5"/>'
    f'<circle cx="46" cy="154" r="22" fill="{ORNG}" stroke="{INK}" stroke-width="5"/>'
    f'<path d="M84 22c10 0 12 6 12 16v48c0 8 4 12 12 12-8 0-12 4-12 12v48c0 10-2 16-12 16" '
    f'fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<text x="154" y="116" font-family="Georgia,serif" font-size="58" font-weight="700" '
    f'fill="{GREEN}" text-anchor="middle">¥</text>')

# ── Lesson 3 · using and permission ─────────────────────────────────
# 用 — use: a hand holding a pen over a line.
ART["yong"] = svg(
    f'<path d="M150 22l26 26-92 92-34 8 8-34z" fill="{GOLD}" stroke="{INK}" stroke-width="5" '
    f'stroke-linejoin="round"/>'
    f'<path d="M136 36l26 26" stroke="{INK}" stroke-width="5"/>'
    f'<path d="M50 114l-8 34 34-8z" fill="{SLATE}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M28 174h144" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')

# 可以 — may: a tick.
ART["keyi"] = svg(
    f'<circle cx="100" cy="100" r="76" fill="{GREEN}" opacity=".14"/>'
    f'<circle cx="100" cy="100" r="76" fill="none" stroke="{GREEN}" stroke-width="7"/>'
    f'<path d="M62 102l26 28 52-60" fill="none" stroke="{GREEN}" stroke-width="16" '
    f'stroke-linecap="round" stroke-linejoin="round"/>')

# 币 — currency: a coin, seen edge-on behind a face-on one.
ART["bi"] = svg(
    f'<ellipse cx="158" cy="112" rx="18" ry="50" fill="{COIN2}" stroke="{INK}" stroke-width="5"/>' +
    coin(78, 106, 58, COIN, "¥", fs=44))

# 人民币 — RMB: the ¥100 note.
ART["renminbi"] = svg(note(10, 58, 180, 88, NOTE2, "100", fs=48))

# ── Lesson 4 · how good it is ───────────────────────────────────────
# 好吃 — delicious: a bowl with steam.
ART["haochi"] = svg(
    f'<path d="M30 104h140c0 38-32 62-70 62s-70-24-70-62z" fill="{PAPER}" stroke="{INK}" '
    f'stroke-width="6" stroke-linejoin="round"/>'
    f'<path d="M22 104h156" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M44 130h112" stroke="{INK}" stroke-width="4" opacity=".4"/>'
    f'<path d="M72 88c0-14 12-14 12-28s-12-14-12-28" fill="none" stroke="{GREEN}" '
    f'stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M106 92c0-14 12-14 12-28s-12-14-12-28" fill="none" stroke="{GREEN}" '
    f'stroke-width="7" stroke-linecap="round"/>')

# 特别 — especially: a star. Abstract, but the star is the degree marker
# used on the 好吃 ladder, so it earns its place next to 好吃.
ART["tebie"] = svg(
    f'<path d="M100 20l24 50 55 8-40 38 10 54-49-26-49 26 10-54-40-38 55-8z" fill="{GOLD}" '
    f'stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>')

# ── Lesson 5 · how often, roughly how much ──────────────────────────
# 次 — times: three tally marks with the fourth struck through.
ART["ci"] = svg(
    f'<path d="M44 48v104M78 48v104M112 48v104M146 48v104" stroke="{INK}" stroke-width="10" '
    f'stroke-linecap="round"/>'
    f'<path d="M30 156L162 44" stroke="{TOM}" stroke-width="10" stroke-linecap="round"/>')

# 一次 — once: a single tally mark.
ART["yici"] = svg(
    f'<path d="M100 44v112" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>')

# 大概 — roughly: a price tag under an approximately sign.
ART["dagai"] = svg(
    f'<path d="M26 70c-6-14 6-30 22-30h-6l106 0c12 0 22 10 22 22v56c0 12-10 22-22 22H48c-16 0-28-16-22-30z" '
    f'fill="none" stroke="none"/>'
    f'<path d="M110 36l64 64-58 58c-6 6-16 6-22 0L36 100V44c0-4 4-8 8-8z" fill="{PAPER}" '
    f'stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    f'<circle cx="68" cy="72" r="12" fill="none" stroke="{INK}" stroke-width="6"/>'
    f'<path d="M96 128c8-12 18-12 26 0s18 12 26 0" fill="none" stroke="{TOM}" stroke-width="8" '
    f'stroke-linecap="round"/>'
    f'<path d="M96 152c8-12 18-12 26 0s18 12 26 0" fill="none" stroke="{TOM}" stroke-width="8" '
    f'stroke-linecap="round"/>')

# ── Lesson 6 · spending, and whether it was worth it ────────────────
# 花 — spend: a till with a total showing.
ART["hua"] = svg(
    f'<rect x="20" y="86" width="160" height="82" rx="10" fill="{SLATE}" stroke="{INK}" stroke-width="6"/>'
    f'<rect x="38" y="30" width="124" height="52" rx="8" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>'
    f'<text x="100" y="68" font-family="Georgia,serif" font-size="32" font-weight="700" '
    f'fill="{INK}" text-anchor="middle">¥216</text>'
    f'<rect x="38" y="104" width="28" height="18" rx="4" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    f'<rect x="80" y="104" width="28" height="18" rx="4" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    f'<rect x="122" y="104" width="28" height="18" rx="4" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
    f'<rect x="38" y="134" width="112" height="18" rx="4" fill="{GOLD}" stroke="{INK}" stroke-width="4"/>')

# 百 — hundred: a fan of ¥100 notes.
ART["bai"] = svg(
    note(14, 66, 132, 62, NOTE2, "100", fs=30) +
    note(38, 84, 132, 62, NOTE2, "100", fs=30) +
    note(62, 102, 132, 62, NOTE2, "100", fs=30))

# 算 — regard as / count as: an abacus row, beads counted to one side.
ART["suan"] = svg(
    f'<rect x="20" y="30" width="160" height="140" rx="10" fill="none" stroke="{INK}" stroke-width="6"/>'
    f'<path d="M20 100h160" stroke="{INK}" stroke-width="6"/>'
    f'<path d="M60 30v140M100 30v140M140 30v140" stroke="{INK}" stroke-width="3.5" opacity=".5"/>'
    f'<ellipse cx="60" cy="52" rx="17" ry="11" fill="{BROWN}" stroke="{INK}" stroke-width="4"/>'
    f'<ellipse cx="100" cy="52" rx="17" ry="11" fill="{BROWN}" stroke="{INK}" stroke-width="4"/>'
    f'<ellipse cx="140" cy="76" rx="17" ry="11" fill="{BROWN}" stroke="{INK}" stroke-width="4"/>'
    f'<ellipse cx="60" cy="148" rx="17" ry="11" fill="{GOLD}" stroke="{INK}" stroke-width="4"/>'
    f'<ellipse cx="100" cy="124" rx="17" ry="11" fill="{GOLD}" stroke="{INK}" stroke-width="4"/>'
    f'<ellipse cx="140" cy="148" rx="17" ry="11" fill="{GOLD}" stroke="{INK}" stroke-width="4"/>')

# 贵 — expensive: a price tag with the arrow going up.
ART["gui"] = svg(
    f'<path d="M104 46l56 56-52 52c-6 6-16 6-22 0L32 100V52c0-3 3-6 6-6z" fill="{PAPER}" '
    f'stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    f'<circle cx="62" cy="76" r="11" fill="none" stroke="{INK}" stroke-width="6"/>'
    f'<path d="M150 170V58" stroke="{TOM}" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M124 84l26-30 26 30" fill="none" stroke="{TOM}" stroke-width="12" '
    f'stroke-linecap="round" stroke-linejoin="round"/>')


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, body in ART.items():
        open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(body)
    print(f"art: {len(ART)} svg written to index/designs/y8-l12/img/")


if __name__ == "__main__":
    main()
