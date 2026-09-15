# -*- coding: utf-8 -*-
"""SVG drawings for the Y8 L13 房子 (House) decks.

Flat two-tone line art on a 200x200 viewBox, same convention as the
y9-l11 / y9-l12 img folders but in this unit's own palette: graphite ink,
slate blue, terracotta, brass. Objects and diagrams only - no faces, no
figures.

Never emoji: Chromium ships no colour emoji font and both the PPTX and the
PDF export run through Chromium, so an emoji renders as an empty box.

A word with no picturable referent gets no entry here and renders as a
textonly card instead. In this lesson almost everything is picturable - it
is a unit about rooms - so the only judgement calls are the six position
words, which get diagrams rather than scenes: one grey volume, one
terracotta marker, and the marker is the only thing that moves between
them. That consistency is the teaching point.

Run:  python3 scripts/y8l13/art.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y8-l13", "img")

# fill="none" on the group is load-bearing: a <path> with only a stroke
# inherits the SVG default fill of black, which turned every tap, pipe and
# shower arm into a solid black wedge. Shapes that want a fill declare one.
W = 'fill="none" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
W3 = 'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'

INK = "#39414A"          # graphite, the drawing hand
SLATE = "#3D5A73"        # drafting ink blue
SLATE_D = "#263C4E"
TERRA = "#B05B3B"        # roof tile / brick
TERRA_D = "#7E3C24"
BRASS = "#A8801E"
MOSS = "#4F7355"
PAPER = "#FDFDF8"        # white fill
COOL = "#DCE3E8"         # cool pale fill
WARM = "#EFE7DA"         # warm pale fill

ART = {}

# ── Lesson 1 · the house, its storeys, up and down ─────────────────
ART["fangzi"] = f'''<g {W}>
<path d="M100 28 14 88h172z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M30 88h140v96H30z" fill="{PAPER}" stroke="{INK}"/>
<path d="M30 136h140" stroke="{INK}" {W3}/>
<rect x="48" y="102" width="30" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="122" y="102" width="30" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="48" y="150" width="30" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M112 184v-34h32v34z" fill="{WARM}" stroke="{INK}" {W3}/>
<circle cx="118" cy="168" r="3" fill="{BRASS}" stroke="none"/>
<path d="M100 28v-14" stroke="{TERRA_D}" {W3}/>
</g>'''

ART["fangjian"] = f'''<g {W}>
<path d="M26 60h148v112H26z" fill="{PAPER}" stroke="{INK}"/>
<path d="M26 60 62 92v80H26zM174 60l-36 32v80h36z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M62 92h76v80H62z" fill="{PAPER}" stroke="{INK}" {W3}/>
<rect x="80" y="108" width="40" height="30" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M100 108v30M80 123h40" stroke="{SLATE}" stroke-width="2"/>
<path d="M138 120v52h26v-52z" fill="{WARM}" stroke="{INK}" {W3}/>
<circle cx="145" cy="148" r="3" fill="{BRASS}" stroke="none"/>
</g>'''

ART["ceng"] = f'''<g {W}>
<path d="M100 22 18 72h164z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M32 72h136v52H32z" fill="{COOL}" stroke="{INK}"/>
<path d="M32 124h136v52H32z" fill="{PAPER}" stroke="{INK}"/>
<path d="M32 124h136" stroke="{SLATE}" stroke-width="5"/>
<rect x="52" y="86" width="26" height="24" rx="2" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<rect x="122" y="86" width="26" height="24" rx="2" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<rect x="52" y="140" width="26" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="122" y="140" width="26" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M182 72v52M182 124v52" stroke="{BRASS}" {W3}/>
<path d="M177 72h10M177 124h10M177 176h10" stroke="{BRASS}" stroke-width="2.5"/>
</g>'''

ART["lou"] = f'''<g {W}>
<path d="M44 26h112v156H44z" fill="{PAPER}" stroke="{INK}"/>
<path d="M44 64h112M44 102h112M44 140h112" stroke="{INK}" {W3}/>
<rect x="60" y="38" width="24" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<rect x="116" y="38" width="24" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<rect x="60" y="76" width="24" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<rect x="116" y="76" width="24" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<rect x="60" y="114" width="24" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<rect x="116" y="114" width="24" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<path d="M88 182v-30h24v30z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M44 26h112l-8-12H52z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
</g>'''

ART["loushang"] = f'''<g {W}>
<path d="M40 40h120v142H40z" fill="{PAPER}" stroke="{INK}"/>
<path d="M40 110h120" stroke="{INK}"/>
<path d="M40 40h120v70H40z" fill="{TERRA}" fill-opacity="0.22" stroke="{INK}"/>
<rect x="58" y="60" width="26" height="22" rx="2" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<rect x="116" y="60" width="26" height="22" rx="2" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<rect x="58" y="130" width="26" height="22" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="116" y="130" width="26" height="22" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M178 96V56M178 56l-9 12M178 56l9 12" stroke="{TERRA}" stroke-width="6"/>
<path d="M40 40h120l-8-14H48z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
</g>'''

ART["louxia"] = f'''<g {W}>
<path d="M40 40h120v142H40z" fill="{PAPER}" stroke="{INK}"/>
<path d="M40 110h120" stroke="{INK}"/>
<path d="M40 110h120v72H40z" fill="{TERRA}" fill-opacity="0.22" stroke="{INK}"/>
<rect x="58" y="60" width="26" height="22" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="116" y="60" width="26" height="22" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="58" y="130" width="26" height="22" rx="2" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<rect x="116" y="130" width="26" height="22" rx="2" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M178 122v40M178 162l-9-12M178 162l9-12" stroke="{TERRA}" stroke-width="6"/>
<path d="M40 40h120l-8-14H48z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
</g>'''

# ── Lesson 2 · rooms upstairs ──────────────────────────────────────
ART["woshi"] = f'''<g {W}>
<path d="M22 150h156v14H22z" fill="{INK}" fill-opacity="0.12" stroke="{INK}"/>
<path d="M30 150v-46c0-8 6-14 14-14h92c8 0 14 6 14 14v46z" fill="{PAPER}" stroke="{INK}"/>
<path d="M30 118h120v32H30z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M42 116V96c0-5 4-8 9-8h34c5 0 9 3 9 8v20z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M30 164v12M150 164v12" stroke="{INK}" {W3}/>
<path d="M160 150v-40" stroke="{INK}" {W3}/>
<path d="M146 110h28l-6-22h-16z" fill="{BRASS}" fill-opacity="0.5" stroke="{BRASS}" {W3}/>
<rect x="60" y="34" width="52" height="34" rx="3" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M86 34v34M60 51h52" stroke="{SLATE}" stroke-width="2"/>
</g>'''

ART["shufang"] = f'''<g {W}>
<path d="M18 122h104v10H18z" fill="{WARM}" stroke="{INK}"/>
<path d="M26 132v48M114 132v48" stroke="{INK}" {W3}/>
<path d="M44 122V96h44v26z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M44 96h44" stroke="{SLATE}" {W3}/>
<path d="M56 122v-16h20v16z" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<path d="M132 42h52v140h-52z" fill="{PAPER}" stroke="{INK}"/>
<path d="M132 82h52M132 122h52M132 158h52" stroke="{INK}" {W3}/>
<path d="M140 78V52h8v26zM152 78V56h7v22zM164 78V50h8v28z" fill="{TERRA}" stroke="{TERRA_D}" stroke-width="2.5"/>
<path d="M140 118V92h9v26zM154 118V96h8v22z" fill="{MOSS}" stroke="{INK}" stroke-width="2.5"/>
<path d="M140 154v-22h30v22z" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
</g>'''

ART["yushi"] = f'''<g {W}>
<path d="M24 112h136v34c0 14-10 24-24 24H48c-14 0-24-10-24-24z" fill="{PAPER}" stroke="{INK}"/>
<path d="M24 112h136" stroke="{SLATE}" stroke-width="5"/>
<path d="M36 128h112v18c0 8-5 12-13 12H49c-8 0-13-4-13-12z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M44 170v12M140 170v12" stroke="{INK}" {W3}/>
<path d="M150 112V62h20" stroke="{SLATE}" stroke-width="5"/>
<path d="M156 56h28l6 14h-40z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M162 76v12M172 76v14M182 76v10" stroke="{SLATE}" stroke-width="2.5"/>
<circle cx="60" cy="96" r="6" fill="none" stroke="{BRASS}" {W3}/>
<circle cx="84" cy="96" r="6" fill="none" stroke="{BRASS}" {W3}/>
</g>'''

ART["xizao"] = f'''<g {W}>
<path d="M62 44h30l8 16H54z" fill="{COOL}" stroke="{SLATE}"/>
<path d="M77 44V22h68v18" stroke="{SLATE}" stroke-width="5"/>
<path d="M60 74c4 10 4 16 0 26M77 76c4 10 4 18 0 28M94 74c4 10 4 16 0 26" stroke="{SLATE}" {W3}/>
<path d="M52 116c4 10 4 16 0 26M69 118c4 10 4 18 0 28M86 116c4 10 4 16 0 26M101 120c4 8 4 14 0 22" stroke="{SLATE}" {W3}/>
<path d="M28 152h144v12c0 12-8 20-20 20H48c-12 0-20-8-20-20z" fill="{PAPER}" stroke="{INK}"/>
<path d="M28 152h144" stroke="{SLATE}" stroke-width="5"/>
<path d="M136 88h36v58h-36z" fill="{WARM}" stroke="{BRASS}" {W3}/>
<path d="M146 88v58M158 88v58" stroke="{BRASS}" stroke-width="2"/>
<path d="M132 84h44" stroke="{INK}" {W3}/>
</g>'''

# ── Lesson 3 · rooms downstairs ────────────────────────────────────
ART["keting"] = f'''<g {W}>
<path d="M18 116h96c8 0 12 5 12 12v34H18z" fill="{PAPER}" stroke="{INK}"/>
<path d="M18 116V96c0-8 5-12 12-12h72c8 0 12 4 12 12v20" fill="{COOL}" stroke="{INK}"/>
<path d="M40 116V94h28v22zM76 116V94h28v22z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M26 162v14M118 162v14" stroke="{INK}" {W3}/>
<path d="M136 70h50v40h-50z" fill="{INK}" fill-opacity="0.82" stroke="{INK}"/>
<path d="M144 78h34v24h-34z" fill="{COOL}" stroke="none"/>
<path d="M161 110v16M146 126h30" stroke="{INK}" {W3}/>
<path d="M136 162h50v-26h-50z" fill="{WARM}" stroke="{INK}" {W3}/>
</g>'''

ART["canting"] = f'''<g {W}>
<path d="M30 54h28v44H30zM142 54h28v44h-28z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M34 98v34M54 98v34M146 98v34M166 98v34" stroke="{INK}" stroke-width="2.5"/>
<ellipse cx="100" cy="112" rx="76" ry="26" fill="{PAPER}" stroke="{INK}"/>
<path d="M100 138v34M74 172h52" stroke="{INK}"/>
<ellipse cx="68" cy="108" rx="16" ry="6" fill="{COOL}" stroke="{SLATE}" {W3}/>
<ellipse cx="132" cy="108" rx="16" ry="6" fill="{COOL}" stroke="{SLATE}" {W3}/>
<ellipse cx="100" cy="98" rx="14" ry="6" fill="{TERRA}" fill-opacity="0.4" stroke="{TERRA_D}" {W3}/>
<path d="M84 74h32v18H84z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M76 36h18v38H76z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M106 36h18v38h-18z" fill="{WARM}" stroke="{INK}" {W3}/>
</g>'''

ART["chufang"] = f'''<g {W}>
<path d="M30 76h140v20H30z" fill="{COOL}" stroke="{INK}"/>
<path d="M34 96h132v84H34z" fill="{PAPER}" stroke="{INK}"/>
<path d="M52 112h96v52H52z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M52 126h96" stroke="{SLATE}" stroke-width="2.5"/>
<circle cx="100" cy="146" r="12" fill="{TERRA}" fill-opacity="0.35" stroke="{TERRA_D}" {W3}/>
<circle cx="56" cy="86" r="9" fill="none" stroke="{INK}" {W3}/>
<circle cx="86" cy="86" r="9" fill="{TERRA}" fill-opacity="0.6" stroke="{TERRA_D}" {W3}/>
<circle cx="116" cy="86" r="9" fill="none" stroke="{INK}" {W3}/>
<circle cx="146" cy="86" r="9" fill="none" stroke="{INK}" {W3}/>
<path d="M62 74h48v-18H62z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M110 62h12" stroke="{SLATE}" {W3}/>
<path d="M74 44c5-9-4-13 0-22M96 40c5-9-4-13 0-20" stroke="{BRASS}" {W3}/>
</g>'''

ART["xishoujian"] = f'''<g {W}>
<path d="M56 96h58v34c0 16-12 28-28 28h-4c-16 0-26-12-26-28z" fill="{PAPER}" stroke="{INK}"/>
<path d="M56 96h58" stroke="{SLATE}" stroke-width="5"/>
<path d="M70 158h32v20H70z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M62 178h48" stroke="{INK}" {W3}/>
<path d="M58 92V44h48v48z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M106 58h12v8h-12z" fill="{BRASS}" stroke="{BRASS}" stroke-width="2"/>
<path d="M134 122h46v10h-46z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M140 132c0 14 4 20 10 24h20c6-4 10-10 10-24z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M157 122V96h16" stroke="{SLATE}" {W3}/>
<circle cx="157" cy="140" r="4" fill="{SLATE}" stroke="none"/>
</g>'''

# ── Lesson 4 · six position words, one diagram family ──────────────
# Two sub-families, deliberately. 上/下/左/右 are a bare volume with the
# marker on that side - a direction. 里/外 add a dashed boundary, because
# the word is about being in or out of something, not about which side.
# Without that boundary 外面 and 右面 render as the same picture, which is
# how the word gets learnt wrong.
def _cube(marker, extra=""):
    return f'''<g {W}>
<path d="M56 86h88v74H56z" fill="{COOL}" stroke="{INK}"/>
<path d="M56 86 78 64h88l-22 22M144 160l22-22V64" fill="{COOL}" fill-opacity="0.55" stroke="{INK}" {W3}/>
{extra}
{marker}
</g>'''


def _bounded(marker, extra=""):
    return f'''<g {W}>
<path d="M20 44h160v134H20z" fill="none" stroke="{TERRA_D}" stroke-width="3" stroke-dasharray="8 7" rx="8"/>
<path d="M62 92h68v62H62z" fill="{COOL}" stroke="{INK}"/>
<path d="M62 92 80 74h68l-18 18M130 154l18-18V74" fill="{COOL}" fill-opacity="0.55" stroke="{INK}" {W3}/>
{extra}
{marker}
</g>'''


_DOT = f'<circle cx="%d" cy="%d" r="13" fill="{TERRA}" stroke="{TERRA_D}"/>'
_ARR = f'<path d="%s" stroke="{TERRA_D}" stroke-width="4" fill="none"/>'

ART["shangmian"] = _cube(_DOT % (100, 26), _ARR % "M100 43v22M100 65l-7-9M100 65l7-9")
ART["xiamian"] = _cube(_DOT % (100, 184), _ARR % "M100 167v-22M100 145l-7 9M100 145l7-9")
ART["zuomian"] = _cube(_DOT % (22, 123), _ARR % "M39 123h20M59 123l-9-6M59 123l-9 6")
ART["youmian"] = _cube(_DOT % (178, 123), _ARR % "M161 123h-20M141 123l9-6M141 123l9 6")
ART["limian"] = _bounded(_DOT % (96, 123))
ART["waimian"] = _bounded(_DOT % (190, 111), _ARR % "M177 111h-8")

# ── Lesson 5 · outside the house ───────────────────────────────────
ART["yangfang"] = f'''<g {W}>
<path d="M100 20 20 74h160z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M34 74h132v88H34z" fill="{PAPER}" stroke="{INK}"/>
<path d="M88 162v-42h24v42z" fill="{WARM}" stroke="{INK}" {W3}/>
<circle cx="94" cy="142" r="3" fill="{BRASS}" stroke="none"/>
<rect x="48" y="92" width="28" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="124" y="92" width="28" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="48" y="128" width="28" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<rect x="124" y="128" width="28" height="24" rx="2" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M84 162v20h32v-20" fill="none" stroke="{INK}" {W3}/>
<path d="M76 182h48M70 190h60" stroke="{INK}" {W3}/>
<path d="M12 162c10-4 14-12 14-22M188 162c-10-4-14-12-14-22" stroke="{MOSS}" {W3}/>
</g>'''

ART["huayuan"] = f'''<g {W}>
<path d="M14 150h172" stroke="{MOSS}" stroke-width="5"/>
<path d="M22 150v-30M48 150v-30M74 150v-30M126 150v-30M152 150v-30M178 150v-30" stroke="{INK}" {W3}/>
<path d="M14 128h172" stroke="{INK}" {W3}/>
<path d="M100 150V86" stroke="{MOSS}" {W3}/>
<circle cx="100" cy="66" r="24" fill="{MOSS}" fill-opacity="0.45" stroke="{MOSS}"/>
<path d="M88 110c-8-6-8-16 0-20 8 4 8 14 0 20zM112 110c8-6 8-16 0-20-8 4-8 14 0 20z" fill="{MOSS}" fill-opacity="0.4" stroke="{MOSS}" {W3}/>
<circle cx="42" cy="104" r="11" fill="{TERRA}" fill-opacity="0.55" stroke="{TERRA_D}" {W3}/>
<path d="M42 115v13" stroke="{MOSS}" {W3}/>
<circle cx="158" cy="110" r="11" fill="{BRASS}" fill-opacity="0.5" stroke="{BRASS}" {W3}/>
<path d="M158 121v7" stroke="{MOSS}" {W3}/>
<path d="M14 168h172" stroke="{MOSS}" stroke-width="2.5"/>
</g>'''

ART["fangqian"] = f'''<g {W}>
<path d="M100 34 42 74h116z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M52 74h96v60H52z" fill="{PAPER}" stroke="{INK}"/>
<path d="M90 134v-28h20v28z" fill="{WARM}" stroke="{INK}" {W3}/>
<rect x="64" y="90" width="20" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<rect x="116" y="90" width="20" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<path d="M28 134h144v42H28z" fill="{TERRA}" fill-opacity="0.2" stroke="{TERRA_D}" stroke-dasharray="7 6"/>
<path d="M100 176V134" stroke="{TERRA_D}" stroke-width="3" stroke-dasharray="6 5"/>
<path d="M100 150v18M100 168l-8-9M100 168l8-9" stroke="{TERRA_D}" stroke-width="4"/>
</g>'''

ART["fanghou"] = f'''<g {W}>
<path d="M28 26h144v42H28z" fill="{TERRA}" fill-opacity="0.2" stroke="{TERRA_D}" stroke-dasharray="7 6"/>
<path d="M100 34v18M100 34l-8 9M100 34l8 9" stroke="{TERRA_D}" stroke-width="4"/>
<path d="M100 70 42 110h116z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M52 110h96v60H52z" fill="{PAPER}" stroke="{INK}"/>
<path d="M90 170v-28h20v28z" fill="{WARM}" stroke="{INK}" {W3}/>
<rect x="64" y="126" width="20" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
<rect x="116" y="126" width="20" height="18" rx="2" fill="{COOL}" stroke="{SLATE}" stroke-width="2.5"/>
</g>'''

ART["cheku"] = f'''<g {W}>
<path d="M20 74h160v18H20z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M28 92h144v84H28z" fill="{PAPER}" stroke="{INK}"/>
<path d="M28 92v84M172 92v84" stroke="{INK}"/>
<path d="M28 92h144v16H28z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M54 158c0-8 6-14 12-20l10-14h48l10 14c6 6 12 12 12 20v10H54z" fill="{COOL}" stroke="{SLATE}"/>
<path d="M78 130h44l7 14H71z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<circle cx="72" cy="168" r="9" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="128" cy="168" r="9" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M20 176h160" stroke="{INK}" {W3}/>
</g>'''

# ── Lesson 6 · parked, and the measure word ────────────────────────
ART["ting"] = f'''<g {W}>
<path d="M22 40v128M178 40v128" stroke="{BRASS}" stroke-width="5" stroke-dasharray="14 10"/>
<path d="M22 168h156" stroke="{BRASS}" stroke-width="5"/>
<path d="M40 134c0-10 8-18 16-26l12-20h64l12 20c8 8 16 16 16 26v12H40z" fill="{COOL}" stroke="{SLATE}"/>
<path d="M70 88h60l9 18H61z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M100 88v18" stroke="{SLATE}" stroke-width="2.5"/>
<circle cx="62" cy="146" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="138" cy="146" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M46 118h14M140 118h14" stroke="{BRASS}" stroke-width="4"/>
</g>'''

ART["liang"] = f'''<g {W}>
<g transform="translate(0,-46) scale(0.46) translate(10,20)">
<path d="M34 138c0-10 8-18 16-26l12-20h76l12 20c8 8 16 16 16 26v14H34z" fill="{TERRA}" fill-opacity="0.4" stroke="{TERRA_D}"/>
<path d="M66 92h68l9 18H57z" fill="{PAPER}" stroke="{TERRA_D}" {W3}/>
<circle cx="58" cy="152" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="142" cy="152" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
</g>
<g transform="translate(0,20) scale(0.46) translate(10,20)">
<path d="M34 138c0-10 8-18 16-26l12-20h76l12 20c8 8 16 16 16 26v14H34z" fill="{COOL}" stroke="{SLATE}"/>
<path d="M66 92h68l9 18H57z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<circle cx="58" cy="152" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="142" cy="152" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
</g>
<g transform="translate(0,86) scale(0.46) translate(10,20)">
<path d="M34 138c0-10 8-18 16-26l12-20h76l12 20c8 8 16 16 16 26v14H34z" fill="{MOSS}" fill-opacity="0.35" stroke="{MOSS}"/>
<path d="M66 92h68l9 18H57z" fill="{PAPER}" stroke="{MOSS}" {W3}/>
<circle cx="58" cy="152" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="142" cy="152" r="12" fill="{PAPER}" stroke="{INK}" {W3}/>
</g>
<path d="M172 32v12M172 98v12M172 164v12" stroke="{BRASS}" stroke-width="5"/>
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
