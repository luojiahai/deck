# -*- coding: utf-8 -*-
"""SVG drawings for the Y9 L14 问路 (Asking the Way) decks.

Flat two-tone line art, 200x200 viewBox, same convention and same Unit 5
palette as scripts/y9l13/art.py — so an L13 deck and an L14 deck read as
one visual family on a projector.

Objects and diagrams only: no faces, no figures. 警察 is a police cap and
badge rather than an officer, and 偷 is a diagram of a wallet leaving a bag
rather than a hand — an AI-drawn human reads as wrong before it reads as
anything.

Verbs and function words have no entry here and render as textonly cards:
骑, 路 (route), 座, 被, 留. A forced drawing for an abstract word is
decoration, and decoration on a teaching slide is noise.

Never emoji: Chromium ships no colour emoji font and any PDF/PPTX export
runs through Chromium, so an emoji renders as an empty box on the slide.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y9-l14", "img")

# fill:none is the group default. A stroke-only <path> inherits fill:black
# otherwise, which silently floods every diagram solid.
W = 'fill="none" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'

INK = "#2A3440"
INK2 = "#4A5763"
PAPER = "#FDFCF8"
WARM = "#E8E2D5"
RED = "#B3321E"
RED_F = "#DE9184"
GREEN = "#2D6A4F"
GREEN_F = "#93C2A7"
BLUE = "#2F5A7A"
BLUE_F = "#A3C3D6"
AMBER = "#C9922B"
AMBER_F = "#F0D194"

ART = {}

# ══ Lesson 1 · getting around ══════════════════════════════════════

ART["zixingche"] = f'''<g {W}>
<circle cx="52" cy="134" r="34" fill="{PAPER}" stroke="{INK}"/>
<circle cx="148" cy="134" r="34" fill="{PAPER}" stroke="{INK}"/>
<circle cx="52" cy="134" r="5" fill="{INK}" stroke="none"/>
<circle cx="148" cy="134" r="5" fill="{INK}" stroke="none"/>
<path d="M52 134 92 76h40l16 58" stroke="{BLUE}" stroke-width="5"/>
<path d="M92 76 78 134h70" stroke="{BLUE}" stroke-width="5"/>
<path d="M78 134h70" stroke="{BLUE}" stroke-width="5"/>
<circle cx="96" cy="134" r="11" fill="none" stroke="{RED}" stroke-width="4"/>
<path d="M76 70h30" stroke="{INK}" stroke-width="6"/>
<path d="M132 76 126 62h-20" stroke="{INK}" stroke-width="5"/>
<path d="M106 62h22" stroke="{INK}" stroke-width="6"/>
</g>'''

ART["gouwu"] = f'''<g {W}>
<path d="M40 82h60l10 86H30z" fill="{WARM}" stroke="{INK}"/>
<path d="M56 82V66a14 14 0 0 1 28 0v16" stroke="{INK}" stroke-width="4"/>
<path d="M104 96h56l8 72h-72z" fill="{PAPER}" stroke="{INK}"/>
<path d="M118 96V84a14 14 0 0 1 28 0v12" stroke="{INK}" stroke-width="4"/>
<path d="M48 118h24M48 134h24" stroke="{RED}" stroke-width="5"/>
<path d="M120 126h28M120 142h28" stroke="{BLUE}" stroke-width="5"/>
</g>'''

ART["guangchang"] = f'''<g {W}>
<path d="M16 150h168" stroke="{INK}" stroke-width="5"/>
<path d="M30 150 58 92h84l28 58z" fill="{WARM}" stroke="{INK}"/>
<path d="M58 92h84M46 116h108M38 134h124" stroke="{INK2}" stroke-width="3"/>
<circle cx="100" cy="118" r="22" fill="{BLUE_F}" stroke="{INK}"/>
<path d="M100 118V92" stroke="{BLUE}" stroke-width="5"/>
<path d="M100 92c-10 0-16 8-16 8M100 92c10 0 16 8 16 8" stroke="{BLUE}" stroke-width="4"/>
<rect x="24" y="60" width="12" height="44" fill="{PAPER}" stroke="{INK}"/>
<rect x="164" y="60" width="12" height="44" fill="{PAPER}" stroke="{INK}"/>
<path d="M30 60v-8M170 60v-8" stroke="{RED}" stroke-width="4"/>
</g>'''

ART["chezhan"] = f'''<g {W}>
<path d="M100 172V64" stroke="{INK}" stroke-width="6"/>
<rect x="56" y="30" width="88" height="46" rx="6" fill="{PAPER}" stroke="{INK}"/>
<circle cx="80" cy="53" r="12" fill="none" stroke="{RED}" stroke-width="5"/>
<path d="M104 44h30M104 56h22" stroke="{INK2}" stroke-width="4"/>
<path d="M40 172v-26h68v26" fill="{WARM}" stroke="{INK}"/>
<path d="M40 146h68" stroke="{INK}" stroke-width="5"/>
<path d="M52 146v26M96 146v26" stroke="{INK2}" stroke-width="3"/>
<path d="M124 172h56" stroke="{INK2}" stroke-width="4" stroke-dasharray="10 8"/>
</g>'''

# ══ Lesson 2 · the bus route ═══════════════════════════════════════

ART["miao"] = f'''<g {W}>
<path d="M22 66 100 34l78 32z" fill="{RED_F}" stroke="{INK}"/>
<path d="M22 66c14 8 26 10 26 10M178 66c-14 8-26 10-26 10" stroke="{INK}" stroke-width="4"/>
<rect x="44" y="76" width="112" height="14" fill="{WARM}" stroke="{INK}"/>
<path d="M56 90v70M144 90v70" stroke="{INK}" stroke-width="6"/>
<path d="M78 160V104h44v56z" fill="{PAPER}" stroke="{INK}"/>
<path d="M100 104v56" stroke="{INK2}" stroke-width="3"/>
<path d="M30 160h140" stroke="{INK}" stroke-width="5"/>
<path d="M40 172h120" stroke="{INK2}" stroke-width="4"/>
<path d="M100 34V22" stroke="{RED}" stroke-width="4"/>
</g>'''

ART["he"] = f'''<g {W}>
<path d="M18 40c34 20 20 44 42 62s60 14 60 40-26 24-40 42"
      stroke="{BLUE}" stroke-width="26" stroke-linecap="butt" opacity="0.35"/>
<path d="M18 40c34 20 20 44 42 62s60 14 60 40-26 24-40 42" stroke="{BLUE}" stroke-width="5"/>
<path d="M46 26c34 20 20 44 42 62s60 14 60 40-26 24-40 46" stroke="{BLUE}" stroke-width="5"/>
<path d="M66 82c10 4 18 4 26 0M92 122c10 4 18 4 26 0" stroke="{BLUE_F}" stroke-width="4"/>
<path d="M156 58c0 10-6 14-6 14M170 58c0 10-6 14-6 14" stroke="{GREEN}" stroke-width="4"/>
<path d="M150 72h26" stroke="{GREEN}" stroke-width="4"/>
</g>'''

ART["qiao"] = f'''<g {W}>
<path d="M10 150h180" stroke="{BLUE}" stroke-width="16" opacity="0.35" stroke-linecap="butt"/>
<path d="M10 150h180" stroke="{BLUE}" stroke-width="4"/>
<path d="M20 112c34-40 126-40 160 0" fill="none" stroke="{INK}" stroke-width="6"/>
<path d="M20 112v22M180 112v22" stroke="{INK}" stroke-width="6"/>
<path d="M56 122c18-22 70-22 88 0" fill="{PAPER}" stroke="{INK}"/>
<path d="M20 96c34-40 126-40 160 0" fill="none" stroke="{INK2}" stroke-width="3"/>
<path d="M62 84v14M100 76v12M138 84v14" stroke="{INK2}" stroke-width="4"/>
<path d="M14 96h172" stroke="{RED}" stroke-width="4" stroke-dasharray="12 8"/>
</g>'''

# ══ Lesson 4 · what's in the bag ═══════════════════════════════════

ART["shoutibao"] = f'''<g {W}>
<path d="M40 82h120l10 90H30z" fill="{WARM}" stroke="{INK}"/>
<path d="M68 82V62a32 32 0 0 1 64 0v20" stroke="{INK}" stroke-width="5"/>
<rect x="86" y="70" width="28" height="22" rx="4" fill="{PAPER}" stroke="{INK}"/>
<path d="M100 78v8" stroke="{RED}" stroke-width="5"/>
<path d="M36 116h128" stroke="{INK2}" stroke-width="3"/>
</g>'''

ART["qianbao"] = f'''<g {W}>
<path d="M28 68h130a10 10 0 0 1 10 10v82a10 10 0 0 1-10 10H28z" fill="{WARM}" stroke="{INK}"/>
<path d="M28 68v102" stroke="{INK}" stroke-width="6"/>
<rect x="44" y="46" width="90" height="28" rx="4" fill="{PAPER}" stroke="{INK}"/>
<path d="M58 60h56" stroke="{GREEN}" stroke-width="5"/>
<rect x="112" y="102" width="58" height="26" rx="6" fill="{PAPER}" stroke="{INK}"/>
<circle cx="141" cy="115" r="8" fill="none" stroke="{RED}" stroke-width="4"/>
</g>'''

ART["yaoshi"] = f'''<g {W}>
<circle cx="146" cy="52" r="24" fill="none" stroke="{INK2}" stroke-width="5"/>
<circle cx="66" cy="70" r="26" fill="{PAPER}" stroke="{INK}"/>
<circle cx="66" cy="70" r="10" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M82 88 132 148" stroke="{INK}" stroke-width="9"/>
<path d="M112 124l-16 14M126 140l-14 12" stroke="{INK}" stroke-width="7"/>
<circle cx="126" cy="86" r="20" fill="{AMBER_F}" stroke="{INK}"/>
<circle cx="126" cy="86" r="7" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M138 98l30 36" stroke="{AMBER}" stroke-width="8"/>
<path d="M156 118l-12 10" stroke="{AMBER}" stroke-width="6"/>
</g>'''

ART["shouji"] = f'''<g {W}>
<rect x="58" y="20" width="84" height="160" rx="14" fill="{PAPER}" stroke="{INK}"/>
<rect x="70" y="42" width="60" height="110" rx="4" fill="{BLUE_F}" stroke="{INK}"/>
<path d="M88 32h24" stroke="{INK2}" stroke-width="5"/>
<circle cx="100" cy="166" r="8" fill="none" stroke="{INK}" stroke-width="4"/>
<path d="M82 62h36M82 80h36M82 98h22" stroke="{PAPER}" stroke-width="5"/>
<path d="M82 124h36" stroke="{RED}" stroke-width="5"/>
</g>'''

ART["xianjin"] = f'''<g {W}>
<rect x="24" y="52" width="130" height="66" rx="6" fill="{GREEN_F}" stroke="{INK}"/>
<rect x="40" y="70" width="130" height="66" rx="6" fill="{PAPER}" stroke="{INK}"/>
<circle cx="105" cy="103" r="20" fill="none" stroke="{GREEN}" stroke-width="5"/>
<path d="M97 95h16M97 111h16M105 91v24" stroke="{GREEN}" stroke-width="4"/>
<path d="M56 86h14M140 120h14" stroke="{INK2}" stroke-width="4"/>
<circle cx="52" cy="158" r="18" fill="{AMBER_F}" stroke="{INK}"/>
<circle cx="88" cy="164" r="14" fill="{AMBER_F}" stroke="{INK}"/>
<path d="M46 158h12M52 152v12" stroke="{AMBER}" stroke-width="4"/>
</g>'''

# First draft set the shirt body 24 units wide and the trousers 48: at
# projector distance the shirt read as an arrow and the trousers as a cup.
# Both are now near twice as wide, with a visible collar and a leg split.
ART["fuzhuang"] = f'''<g {W}>
<path d="M20 36h72" stroke="{INK2}" stroke-width="3"/>
<path d="M56 36V26a6 6 0 0 1 8-4" stroke="{INK2}" stroke-width="3"/>
<path d="M56 52 18 68v20h16v58h44V88h16V68z" fill="{BLUE_F}" stroke="{INK}"/>
<path d="M44 56 56 70 68 56" stroke="{INK}" stroke-width="4"/>
<path d="M34 88h44" stroke="{BLUE}" stroke-width="3"/>
<path d="M112 36h72" stroke="{INK2}" stroke-width="3"/>
<path d="M148 36V26a6 6 0 0 1 8-4" stroke="{INK2}" stroke-width="3"/>
<path d="M116 66h64v16l-6 64h-22l-4-50-4 50h-22l-6-64z" fill="{WARM}" stroke="{INK}"/>
<path d="M116 82h64" stroke="{INK}" stroke-width="4"/>
<path d="M148 96v50" stroke="{INK2}" stroke-width="3"/>
</g>'''

# ══ Lesson 5 · reporting a theft ═══════════════════════════════════

# 偷 as a diagram, not a hand: a wallet leaving an open bag along a dashed
# arc. An AI-drawn hand reads as wrong before it reads as "steal".
ART["tou"] = f'''<g {W}>
<path d="M30 96h96l8 76H22z" fill="{WARM}" stroke="{INK}"/>
<path d="M52 96V80a26 26 0 0 1 52 0v16" stroke="{INK}" stroke-width="5"/>
<path d="M30 96c24 12 72 12 96 0" stroke="{INK}" stroke-width="4"/>
<path d="M100 70C120 34 158 30 172 40" stroke="{RED}" stroke-width="4" stroke-dasharray="10 8"/>
<path d="M164 30l12 10-12 12" stroke="{RED}" stroke-width="4"/>
<rect x="130" y="52" width="52" height="34" rx="5" fill="{PAPER}" stroke="{INK}"/>
<path d="M130 64h52" stroke="{INK2}" stroke-width="3"/>
<circle cx="168" cy="76" r="5" fill="{RED}" stroke="none"/>
</g>'''

# 警察 as cap and badge — objects, not a person.
ART["jingcha"] = f'''<g {W}>
<path d="M34 118c0-40 30-64 66-64s66 24 66 64z" fill="{BLUE_F}" stroke="{INK}"/>
<path d="M22 118h156a8 8 0 0 1 8 8v10H14v-10a8 8 0 0 1 8-8z" fill="{INK2}" stroke="{INK}"/>
<path d="M34 118h132" stroke="{INK}" stroke-width="4"/>
<path d="M100 54v-8" stroke="{RED}" stroke-width="4"/>
<path d="M100 70 86 80v14c0 10 6 16 14 20 8-4 14-10 14-20V80z" fill="{AMBER_F}" stroke="{INK}"/>
<path d="M100 82v18" stroke="{AMBER}" stroke-width="4"/>
<path d="M40 156h120" stroke="{INK2}" stroke-width="4" stroke-dasharray="10 8"/>
</g>'''

ART["xingming"] = f'''<g {W}>
<rect x="34" y="24" width="132" height="152" rx="8" fill="{PAPER}" stroke="{INK}"/>
<path d="M52 56h60" stroke="{INK}" stroke-width="6"/>
<path d="M52 84h96" stroke="{RED}" stroke-width="4"/>
<path d="M52 92h96" stroke="{INK2}" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M52 118h96M52 140h96" stroke="{INK2}" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M62 78c10-10 18-2 26-10s16 4 24-4" stroke="{BLUE}" stroke-width="4"/>
<circle cx="150" cy="56" r="10" fill="none" stroke="{INK2}" stroke-width="3"/>
</g>'''

# ══ Lesson 6 · the three cards ═════════════════════════════════════

def _card(fill, mark):
    return f'''<g {W}>
<rect x="18" y="46" width="164" height="108" rx="10" fill="{fill}" stroke="{INK}"/>
<rect x="34" y="64" width="48" height="60" rx="4" fill="{PAPER}" stroke="{INK}"/>
<path d="M98 74h68M98 96h68M98 118h44" stroke="{INK2}" stroke-width="4"/>
{mark}
</g>'''

ART["shenfenzheng"] = _card(WARM, f'''
<circle cx="58" cy="86" r="13" fill="none" stroke="{INK2}" stroke-width="3"/>
<path d="M40 118c4-14 32-14 36 0" stroke="{INK2}" stroke-width="3"/>
<path d="M34 140h148" stroke="{RED}" stroke-width="5"/>''')

ART["xueshengzheng"] = _card(BLUE_F, f'''
<circle cx="58" cy="86" r="13" fill="none" stroke="{INK2}" stroke-width="3"/>
<path d="M40 118c4-14 32-14 36 0" stroke="{INK2}" stroke-width="3"/>
<path d="M150 52 168 60l-18 8-18-8z" fill="{PAPER}" stroke="{INK}"/>
<path d="M34 140h148" stroke="{BLUE}" stroke-width="5"/>''')

ART["jieshuzheng"] = _card(GREEN_F, f'''
<rect x="38" y="70" width="40" height="10" fill="{PAPER}" stroke="{INK}"/>
<rect x="38" y="86" width="40" height="10" fill="{PAPER}" stroke="{INK}"/>
<rect x="38" y="102" width="40" height="10" fill="{PAPER}" stroke="{INK}"/>
<path d="M34 140h148" stroke="{GREEN}" stroke-width="5"/>''')


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, body in ART.items():
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" '
               'width="200" height="200">' + body.replace("\n", "") + '</svg>')
        with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(svg)
    print("wrote %d drawings to %s" % (len(ART), os.path.normpath(OUT)))


if __name__ == "__main__":
    main()
