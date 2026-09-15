# -*- coding: utf-8 -*-
"""SVG drawings for the Y9 L13 社区 (Neighbourhood) decks.

Flat two-tone line art, 200x200 viewBox, same convention as y9-l11 and
y9-l12. Objects and diagrams only - no faces, no figures.

Unit 5 palette (see shared/tokens.css): map paper and ink, with a signal
red, a route green and a slate blue. The direction words get *diagrams*
rather than pictures - an arrow bending right IS what 往右拐 means, and a
diagram teaches it faster than any photograph could.

A word with no picturable referent (生活, 方便, 看到, 向) has no entry here
and renders as a textonly card instead.

Never emoji: Chromium ships no colour emoji font and the PPTX/PDF export
runs through Chromium, so an emoji renders as an empty box on the slide.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y9-l13", "img")

# fill:none is the group default. A stroke-only <path> inherits fill:black
# otherwise, which silently floods every arrow and diagram solid - that is
# exactly how the first draft of this file lost all nine direction arrows.
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

# ══ Lesson 1 · where I live ════════════════════════════════════════

ART["shizhongxin"] = f'''<g {W}>
<ellipse cx="100" cy="164" rx="86" ry="20" fill="none" stroke="{INK2}" stroke-dasharray="9 8" stroke-width="3"/>
<rect x="46" y="72" width="30" height="82" fill="{WARM}" stroke="{INK}"/>
<rect x="82" y="40" width="36" height="114" fill="{PAPER}" stroke="{INK}"/>
<rect x="124" y="64" width="30" height="90" fill="{WARM}" stroke="{INK}"/>
<rect x="24" y="104" width="22" height="50" fill="{PAPER}" stroke="{INK}"/>
<rect x="154" y="96" width="22" height="58" fill="{PAPER}" stroke="{INK}"/>
<path d="M54 86h14M54 100h14M54 114h14M54 128h14" stroke="{BLUE}" stroke-width="5"/>
<path d="M90 56h20M90 72h20M90 88h20M90 104h20M90 120h20M90 136h20" stroke="{BLUE}" stroke-width="5"/>
<path d="M132 78h14M132 92h14M132 106h14M132 120h14" stroke="{BLUE}" stroke-width="5"/>
<path d="M100 40V22" stroke="{RED}" stroke-width="4"/>
<circle cx="100" cy="18" r="6" fill="{RED}" stroke="none"/>
</g>'''

ART["youju"] = f'''<g {W}>
<path d="M34 78 100 44l66 34z" fill="{WARM}" stroke="{INK}"/>
<rect x="44" y="78" width="112" height="76" fill="{PAPER}" stroke="{INK}"/>
<rect x="58" y="96" width="84" height="44" rx="3" fill="{WARM}" stroke="{INK}"/>
<path d="M58 96l42 26 42-26" fill="none" stroke="{RED}" stroke-width="4"/>
<path d="M34 154h132" stroke="{INK}"/>
<rect x="164" y="104" width="24" height="50" rx="10" fill="{RED_F}" stroke="{RED}"/>
<path d="M168 116h16" stroke="{RED}" stroke-width="4"/>
</g>'''

# ══ Lesson 2 · the facilities ══════════════════════════════════════

ART["zhensuo"] = f'''<g {W}>
<path d="M38 82 100 48l62 34z" fill="{WARM}" stroke="{INK}"/>
<rect x="48" y="82" width="104" height="72" fill="{PAPER}" stroke="{INK}"/>
<path d="M38 154h124" stroke="{INK}"/>
<path d="M92 96h16v14h14v16h-14v14H92v-14H78v-16h14z" fill="{RED_F}" stroke="{RED}"/>
<path d="M22 132c0-16 12-22 12-34" fill="none" stroke="{INK2}" stroke-width="4"/>
<circle cx="22" cy="140" r="9" fill="none" stroke="{INK2}" stroke-width="4"/>
<circle cx="34" cy="94" r="5" fill="{INK2}" stroke="none"/>
</g>'''

ART["yinhang"] = f'''<g {W}>
<path d="M28 74 100 40l72 34z" fill="{WARM}" stroke="{INK}"/>
<rect x="36" y="74" width="128" height="10" fill="{PAPER}" stroke="{INK}"/>
<path d="M54 84v56M82 84v56M118 84v56M146 84v56" stroke="{INK}" stroke-width="7"/>
<rect x="32" y="140" width="136" height="12" fill="{PAPER}" stroke="{INK}"/>
<path d="M24 152h152" stroke="{INK}"/>
<ellipse cx="100" cy="170" rx="24" ry="7" fill="{AMBER_F}" stroke="{AMBER}" stroke-width="3"/>
<ellipse cx="100" cy="182" rx="24" ry="7" fill="{AMBER_F}" stroke="{AMBER}" stroke-width="3"/>
<path d="M76 170v12M124 170v12" stroke="{AMBER}" stroke-width="3"/>
</g>'''

ART["baihuo"] = f'''<g {W}>
<rect x="38" y="34" width="124" height="120" fill="{PAPER}" stroke="{INK}"/>
<path d="M38 60h124M38 90h124" stroke="{INK}" stroke-width="3"/>
<rect x="52" y="40" width="26" height="14" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="88" y="40" width="26" height="14" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="124" y="40" width="26" height="14" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="52" y="68" width="26" height="14" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="88" y="68" width="26" height="14" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="124" y="68" width="26" height="14" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="50" y="100" width="46" height="42" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<path d="M62 138v-20c0-6 4-10 11-10s11 4 11 10v20" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="3"/>
<rect x="110" y="100" width="42" height="42" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<rect x="120" y="116" width="24" height="18" rx="3" fill="{RED_F}" stroke="{RED}" stroke-width="3"/>
<path d="M126 116v-6c0-4 3-6 6-6s6 2 6 6v6" fill="none" stroke="{RED}" stroke-width="3"/>
<path d="M28 154h144" stroke="{INK}"/>
</g>'''

ART["shizheng"] = f'''<g {W}>
<path d="M100 14v22" stroke="{INK2}" stroke-width="3"/>
<path d="M100 16h26l-8 9 8 9h-26z" fill="{RED_F}" stroke="{RED}" stroke-width="3"/>
<path d="M22 72 100 36l78 36z" fill="{WARM}" stroke="{INK}"/>
<rect x="30" y="72" width="140" height="10" fill="{PAPER}" stroke="{INK}"/>
<path d="M46 82v52M74 82v52M100 82v52M126 82v52M154 82v52" stroke="{INK}" stroke-width="7"/>
<rect x="26" y="134" width="148" height="10" fill="{PAPER}" stroke="{INK}"/>
<path d="M18 156h164M26 144h148l6 12H20z" fill="{WARM}" stroke="{INK}"/>
<circle cx="100" cy="58" r="10" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>
<path d="M100 52v6l4 4" stroke="{INK}" stroke-width="3"/>
</g>'''

# ══ Lesson 3 · church, park, front, back ═══════════════════════════

ART["jiaotang"] = f'''<g {W}>
<path d="M100 16v24M90 24h20" stroke="{RED}" stroke-width="5"/>
<path d="M100 40 62 88h76z" fill="{WARM}" stroke="{INK}"/>
<rect x="62" y="88" width="76" height="66" fill="{PAPER}" stroke="{INK}"/>
<path d="M86 154v-38c0-8 6-14 14-14s14 6 14 14v38z" fill="{WARM}" stroke="{INK}"/>
<circle cx="100" cy="72" r="9" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="3"/>
<rect x="34" y="106" width="28" height="48" fill="{PAPER}" stroke="{INK}"/>
<rect x="138" y="106" width="28" height="48" fill="{PAPER}" stroke="{INK}"/>
<rect x="42" y="118" width="12" height="18" rx="6" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="3"/>
<rect x="146" y="118" width="12" height="18" rx="6" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="3"/>
<path d="M26 154h148" stroke="{INK}"/>
</g>'''

ART["gongyuan"] = f'''<g {W}>
<path d="M14 158h172" stroke="{INK}"/>
<path d="M22 158c22-26 60-30 78-30s56 4 78 30z" fill="{GREEN_F}" stroke="{GREEN}" stroke-width="3"/>
<circle cx="50" cy="78" r="28" fill="{GREEN_F}" stroke="{GREEN}"/>
<path d="M50 106v32" stroke="{INK2}" stroke-width="5"/>
<circle cx="152" cy="90" r="22" fill="{GREEN_F}" stroke="{GREEN}"/>
<path d="M152 112v26" stroke="{INK2}" stroke-width="5"/>
<path d="M100 96c14 0 20 10 20 18h-40c0-8 6-18 20-18z" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="3"/>
<path d="M100 96V76" stroke="{BLUE}" stroke-width="3"/>
<path d="M100 76c-6-8-2-16 0-18 2 2 6 10 0 18z" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="3"/>
<ellipse cx="100" cy="122" rx="30" ry="8" fill="{BLUE_F}" stroke="{BLUE}" stroke-width="3"/>
<path d="M36 140h40M40 140v10M72 140v10" stroke="{AMBER}" stroke-width="4"/>
</g>'''

ART["qianmian"] = f'''<g {W}>
<path d="M14 156h172" stroke="{INK2}" stroke-width="3"/>
<rect x="104" y="58" width="60" height="62" fill="{PAPER}" stroke="{INK2}" stroke-width="3" opacity="0.5"/>
<rect x="38" y="82" width="74" height="74" fill="{RED_F}" stroke="{RED}"/>
<path d="M50 100h50M50 118h50M50 136h30" stroke="{RED}" stroke-width="4"/>
<path d="M100 36h-62" stroke="{RED}" stroke-width="5"/>
<path d="M50 26 38 36l12 10" fill="none" stroke="{RED}" stroke-width="5"/>
</g>'''

ART["houmian"] = f'''<g {W}>
<path d="M14 156h172" stroke="{INK2}" stroke-width="3"/>
<rect x="38" y="82" width="74" height="74" fill="{PAPER}" stroke="{INK2}" stroke-width="3" opacity="0.5"/>
<rect x="104" y="58" width="60" height="62" fill="{GREEN_F}" stroke="{GREEN}"/>
<path d="M116 76h36M116 92h36M116 108h22" stroke="{GREEN}" stroke-width="4"/>
<path d="M100 36h62" stroke="{GREEN}" stroke-width="5"/>
<path d="M150 26l12 10-12 10" fill="none" stroke="{GREEN}" stroke-width="5"/>
</g>'''

# ══ Lesson 4 · the street furniture of directions ══════════════════

ART["kafeiguan"] = f'''<g {W}>
<rect x="34" y="72" width="132" height="82" fill="{PAPER}" stroke="{INK}"/>
<path d="M28 72h144l-8-22H36z" fill="{WARM}" stroke="{INK}"/>
<path d="M50 50v22M72 50v22M94 50v22M116 50v22M138 50v22" stroke="{RED}" stroke-width="4"/>
<rect x="56" y="96" width="60" height="46" rx="4" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<path d="M68 112h30v16c0 5-4 8-9 8h-12c-5 0-9-3-9-8z" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>
<path d="M98 116h8c5 0 8 3 8 7s-3 7-8 7h-4" fill="none" stroke="{INK}" stroke-width="3"/>
<path d="M76 106c-3-5 1-8 0-12M88 106c-3-5 1-8 0-12" stroke="{INK2}" stroke-width="3"/>
<rect x="128" y="100" width="28" height="42" rx="3" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<path d="M28 154h144" stroke="{INK}"/>
<path d="M156 34h30v20h-30z" fill="{RED_F}" stroke="{RED}" stroke-width="3"/>
<path d="M171 54v18" stroke="{RED}" stroke-width="3"/>
</g>'''

ART["guomalu"] = f'''<g {W}>
<rect x="16" y="60" width="168" height="90" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<path d="M32 60v90M58 60v90M84 60v90M110 60v90M136 60v90M162 60v90" stroke="{PAPER}" stroke-width="14"/>
<path d="M32 60v90M58 60v90M84 60v90M110 60v90M136 60v90M162 60v90" stroke="{INK2}" stroke-width="2"/>
<path d="M26 34h136" stroke="{RED}" stroke-width="7"/>
<path d="M150 20l18 14-18 14" fill="none" stroke="{RED}" stroke-width="7"/>
<path d="M16 170h168" stroke="{INK}" stroke-width="3"/>
</g>'''

ART["yizhi"] = f'''<g {W}>
<path d="M44 20v160M156 20v160" stroke="{INK2}" stroke-width="4"/>
<path d="M100 178V46" stroke="{BLUE}" stroke-width="9"/>
<path d="M78 66 100 38l22 28" fill="none" stroke="{BLUE}" stroke-width="9"/>
<path d="M100 170v-12M100 146v-12M100 122v-12" stroke="{PAPER}" stroke-width="5"/>
</g>'''

ART["wangqian"] = f'''<g {W}>
<path d="M40 24v152M160 24v152" stroke="{INK2}" stroke-width="4"/>
<circle cx="100" cy="158" r="13" fill="{WARM}" stroke="{INK}"/>
<path d="M100 140V56" stroke="{GREEN}" stroke-width="9"/>
<path d="M76 78 100 48l24 30" fill="none" stroke="{GREEN}" stroke-width="9"/>
</g>'''

ART["honglvdeng"] = f'''<g {W}>
<rect x="66" y="16" width="68" height="132" rx="12" fill="{WARM}" stroke="{INK}"/>
<circle cx="100" cy="50" r="19" fill="{RED_F}" stroke="{RED}"/>
<circle cx="100" cy="94" r="19" fill="{AMBER_F}" stroke="{AMBER}"/>
<circle cx="100" cy="138" r="19" fill="{PAPER}" stroke="{INK2}"/>
<path d="M100 148v40" stroke="{INK2}" stroke-width="7"/>
<path d="M76 188h48" stroke="{INK}" stroke-width="6"/>
</g>'''

# ══ Lesson 5 · turning and counting ════════════════════════════════

ART["guai"] = f'''<g {W}>
<path d="M56 24v152M144 92v84" stroke="{INK2}" stroke-width="4" opacity="0.55"/>
<path d="M14 92h172" stroke="{INK2}" stroke-width="4" opacity="0.55"/>
<path d="M100 176v-62h56" fill="none" stroke="{RED}" stroke-width="9"/>
<path d="M132 92l28 22-28 22" fill="none" stroke="{RED}" stroke-width="9"/>
</g>'''

ART["zhuan"] = f'''<g {W}>
<path d="M144 24v152M56 92v84" stroke="{INK2}" stroke-width="4" opacity="0.55"/>
<path d="M14 92h172" stroke="{INK2}" stroke-width="4" opacity="0.55"/>
<path d="M100 176v-62H44" fill="none" stroke="{GREEN}" stroke-width="9"/>
<path d="M68 92 40 114l28 22" fill="none" stroke="{GREEN}" stroke-width="9"/>
</g>'''

ART["lukou"] = f'''<g {W}>
<rect x="10" y="76" width="180" height="48" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="76" y="10" width="48" height="180" fill="{WARM}" stroke="{INK2}" stroke-width="3"/>
<rect x="76" y="76" width="48" height="48" fill="{WARM}" stroke="none"/>
<path d="M10 100h56M134 100h56M100 10v56M100 134v56" stroke="{PAPER}" stroke-width="5" stroke-dasharray="14 12"/>
<circle cx="100" cy="100" r="40" fill="none" stroke="{RED}" stroke-width="6" stroke-dasharray="11 9"/>
</g>'''

ART["di"] = f'''<g {W}>
<path d="M14 116h172" stroke="{INK2}" stroke-width="5"/>
<path d="M56 60v112M110 60v112M164 60v112" stroke="{INK2}" stroke-width="5" opacity="0.5"/>
<circle cx="56" cy="116" r="17" fill="{RED_F}" stroke="{RED}" stroke-width="4"/>
<circle cx="110" cy="116" r="17" fill="{PAPER}" stroke="{INK2}" stroke-width="4"/>
<circle cx="164" cy="116" r="17" fill="{PAPER}" stroke="{INK2}" stroke-width="4"/>
<path d="M52 110v12M48 110h8" stroke="{RED}" stroke-width="4"/>
<path d="M105 110h10M115 110l-10 12h10" fill="none" stroke="{INK2}" stroke-width="4"/>
<path d="M159 110h10M169 110l-10 6h8M167 116l-8 6h10" fill="none" stroke="{INK2}" stroke-width="4"/>
<path d="M14 40h30" stroke="{RED}" stroke-width="6"/>
<path d="M36 30l12 10-12 10" fill="none" stroke="{RED}" stroke-width="6"/>
</g>'''

# ══ Lesson 6 · landing the route ═══════════════════════════════════

ART["youshou"] = f'''<g {W}>
<path d="M62 176v-52l-14-16c-5-6-4-13 2-17 5-4 12-3 16 2l12 14V44c0-7 5-12 12-12s12 5 12 12v44V38c0-7 5-12 12-12s12 5 12 12v50V52c0-7 5-12 12-12s12 5 12 12v44" fill="{WARM}" stroke="{INK}"/>
<path d="M62 176h86v-30c0-8-4-14-12-14h-6" fill="{WARM}" stroke="{INK}"/>
<path d="M148 96v40" stroke="{INK}"/>
<path d="M156 24h30" stroke="{RED}" stroke-width="6"/>
<path d="M178 14l12 10-12 10" fill="none" stroke="{RED}" stroke-width="6"/>
</g>'''

ART["zhong"] = f'''<g {W}>
<circle cx="100" cy="100" r="76" fill="{PAPER}" stroke="{INK}"/>
<circle cx="100" cy="100" r="64" fill="none" stroke="{INK2}" stroke-width="3"/>
<path d="M100 42v12M158 100h-12M100 158v-12M42 100h12" stroke="{INK}" stroke-width="5"/>
<path d="M129 58l-6 10M142 129l-10-6M71 142l6-10M58 71l10 6" stroke="{INK2}" stroke-width="3"/>
<path d="M100 100V58" stroke="{INK}" stroke-width="6"/>
<path d="M100 100l30 16" stroke="{RED}" stroke-width="6"/>
<circle cx="100" cy="100" r="7" fill="{RED}" stroke="none"/>
</g>'''


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
