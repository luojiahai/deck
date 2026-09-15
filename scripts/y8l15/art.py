# -*- coding: utf-8 -*-
"""SVG drawings for the Y8 L15 社区 (Neighbourhood) decks.

Flat two-tone line art on a 200x200 viewBox, in the Unit 5 palette shared
with y8-l13 and y8-l14: graphite ink, slate blue, terracotta, brass.
Objects and diagrams only — no faces, no figures.

Never emoji: Chromium ships no colour emoji font and both the PPTX and the
PDF export run through Chromium, so an emoji renders as an empty box.

Never text either. These files are rasterised to PNG by export.sh, and the
rasteriser has no CJK font — a 汉字 inside an SVG would survive the browser
and vanish from the PowerPoint. That rules out the obvious drawing for a
shop, which is its sign, so every shop here is told apart by what is in its
window: flowers, a pencil and ruler, a sofa, books, a barber's pole, a
burger. The awning colour is a second signal, not the only one.

This lesson's abstract words are spatial rather than unpicturable, so they
get DIAGRAMS in the drafting-vellum idiom the unit already uses:

  离  an architect's dimension line — ticks at both ends, arrows inward.
      That is what 离 is: the span between two places, not a verb.
  远  the same two buildings pushed to the edges with a long dashed run
      between them, so 离 and 远 read as a pair rather than as synonyms.
  对面 a road seen from above with one arrow crossing it.
  然后 two arrows end to end through three nodes, the second one terracotta.
  大约 a span bracket with a wave over it — a range, not a point.

挺 has nothing to draw and gets no entry; it renders as a textonly card.

Run:  python3 scripts/y8l15/art.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y8-l15", "img")

# fill="none" on the group is load-bearing: a <path> with only a stroke
# inherits the SVG default fill of black, which turns every awning strut and
# roof line into a solid black wedge. Shapes that want a fill declare one.
W = 'fill="none" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
W3 = 'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'
W2 = 'stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"'

INK = "#39414A"          # graphite, the drawing hand
SLATE = "#3D5A73"        # drafting ink blue
SLATE_D = "#263C4E"
TERRA = "#B05B3B"        # awnings, markers, the moving arrow
TERRA_D = "#7E3C24"
BRASS = "#A8801E"        # handles, dials, route pips
MOSS = "#4F7355"
PAPER = "#FDFDF8"        # white fill
COOL = "#DCE3E8"         # cool pale fill
WARM = "#EFE7DA"         # warm pale fill

ART = {}


def shop(awning, window_inner, door=WARM):
    """A shopfront, drawn the same way every time so the only thing that
    differs between the eight shops in this series is the window and the
    awning colour. Consistency is the point: students learn to read the
    window, not to decode a new building each slide."""
    return f'''<g {W}>
<path d="M26 66h148v104H26z" fill="{PAPER}" stroke="{INK}"/>
<path d="M20 48h160v24H20z" fill="{awning}" stroke="{INK}" {W3}/>
<path d="M60 48v24M100 48v24M140 48v24" stroke="{PAPER}" {W2}/>
<path d="M38 92h78v56H38z" fill="{COOL}" stroke="{SLATE}" {W3}/>
{window_inner}
<path d="M130 100h32v70h-32z" fill="{door}" stroke="{INK}" {W3}/>
<circle cx="136" cy="136" r="3.5" fill="{BRASS}" stroke="none"/>
<path d="M14 170h172" stroke="{INK}" {W3}/>
</g>'''


# ── Lesson 1 · the shops next door ─────────────────────────────────
ART["fujin"] = f'''<g {W}>
<circle cx="100" cy="100" r="80" fill="none" stroke="{SLATE}" stroke-width="3" stroke-dasharray="8 8"/>
<path d="M76 98h48v46H76z" fill="{PAPER}" stroke="{INK}"/>
<path d="M68 98 100 68l32 30" stroke="{INK}"/>
<path d="M92 118h16v26H92z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
<path d="M40 44h30v24H40z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M36 38h38v8H36z" fill="{TERRA}" stroke="none"/>
<path d="M136 52h30v24h-30z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M132 46h38v8h-38z" fill="{MOSS}" stroke="none"/>
<path d="M54 140h30v24H54z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M50 134h38v8H50z" fill="{SLATE}" stroke="none"/>
</g>'''

ART["huadian"] = shop(TERRA, f'''<path d="M58 148v-26M77 148v-34M96 148v-28" stroke="{MOSS}" {W2}/>
<circle cx="58" cy="115" r="9" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<circle cx="77" cy="107" r="9" fill="{BRASS}" stroke="{TERRA_D}" {W2}/>
<circle cx="96" cy="113" r="9" fill="{PAPER}" stroke="{TERRA_D}" {W2}/>
<path d="M44 148h66" stroke="{SLATE}" {W2}/>''')

ART["wenjudian"] = shop(SLATE, f'''<path d="M48 142 84 106" stroke="{BRASS}" stroke-width="7" stroke-linecap="butt"/>
<path d="M84 106l10-10 6 6-10 10z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M46 140l4 8 8-4z" fill="{INK}" stroke="none"/>
<path d="M92 118h20v30H92z" fill="{PAPER}" stroke="{INK}" {W2}/>
<path d="M92 126h20M92 134h20M92 142h20" stroke="{SLATE}" stroke-width="1.6"/>''')

ART["jiajudian"] = shop(MOSS, f'''<path d="M46 122h40v12H46z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M42 126h8v20h-8zM82 126h8v20h-8z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M46 134h40v12H46z" fill="{COOL}" stroke="{INK}" {W2}/>
<path d="M96 104h18v44H96z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M105 104v44" stroke="{INK}" stroke-width="1.6"/>
<circle cx="102" cy="126" r="2.5" fill="{BRASS}" stroke="none"/>''')

# ── Lesson 2 · distance ────────────────────────────────────────────
ART["chaoshi"] = f'''<g {W}>
<path d="M18 74h164v92H18z" fill="{PAPER}" stroke="{INK}"/>
<path d="M18 74 36 46h128l18 28z" fill="{SLATE}" stroke="{SLATE_D}"/>
<path d="M32 96h58v46H32z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M104 96h64v70h-64z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M136 96v70" stroke="{INK}" {W3}/>
<path d="M128 126h6M138 126h6" stroke="{BRASS}" stroke-width="5"/>
<path d="M40 150h42v16H40z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M44 150 40 128h-8" stroke="{TERRA}" {W3}/>
<circle cx="48" cy="174" r="5" fill="{PAPER}" stroke="{TERRA_D}" {W2}/>
<circle cx="76" cy="174" r="5" fill="{PAPER}" stroke="{TERRA_D}" {W2}/>
<path d="M10 166h180" stroke="{INK}" {W3}/>
</g>'''

# 远 — the same two buildings as 离 below, pushed to the edges. The pair is
# the teaching point: 离 names the span, 远 says the span is long.
ART["yuan"] = f'''<g {W}>
<path d="M14 104h32v52H14z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M8 104 30 82l22 22" stroke="{INK}" {W3}/>
<path d="M24 128h12v28H24z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M154 104h32v52h-32z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M148 104 170 82l22 22" stroke="{INK}" {W3}/>
<path d="M164 128h12v28h-12z" fill="{SLATE}" stroke="{SLATE_D}" {W2}/>
<path d="M50 130h100" stroke="{SLATE}" stroke-width="3.5" stroke-dasharray="9 9"/>
<path d="M50 130l12-7v14zM150 130l-12-7v14z" fill="{SLATE}" stroke="none"/>
<path d="M14 168h172" stroke="{INK}" {W3}/>
</g>'''

# 离 — an architect's dimension line, which is what the character does:
# it names the span between two places. It is not a verb, so the drawing
# gives it nothing to do except measure.
ART["li"] = f'''<g {W}>
<path d="M28 82h34v62H28z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M22 82 45 60l23 22" stroke="{INK}" {W3}/>
<path d="M40 110h12v34H40z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M138 82h34v62h-34z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M132 82 155 60l23 22" stroke="{INK}" {W3}/>
<path d="M150 110h12v34h-12z" fill="{SLATE}" stroke="{SLATE_D}" {W2}/>
<path d="M45 150v26M155 150v26" stroke="{BRASS}" {W2}/>
<path d="M45 166h110" stroke="{TERRA}" stroke-width="3.5"/>
<path d="M45 166l14-7v14zM155 166l-14-7v14z" fill="{TERRA}" stroke="none"/>
</g>'''

# ── Lesson 3 · the road, and what is across it ─────────────────────
ART["malu"] = f'''<g {W}>
<path d="M10 78h180v44H10z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M24 100h20M60 100h20M96 100h20M132 100h20M168 100h14" stroke="{PAPER}" stroke-width="5"/>
<path d="M32 26h50v40H32z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M28 20h58v8H28z" fill="{TERRA}" stroke="none"/>
<path d="M50 44h14v22H50z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M118 134h50v40h-50z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M114 128h58v8h-58z" fill="{MOSS}" stroke="none"/>
<path d="M136 152h14v22h-14z" fill="{WARM}" stroke="{INK}" {W2}/>
</g>'''

ART["duimian"] = f'''<g {W}>
<path d="M10 82h180v40H10z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M24 102h18M58 102h18M124 102h18M158 102h18" stroke="{PAPER}" stroke-width="5"/>
<path d="M28 30h52v42H28z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M24 24h60v8H24z" fill="{SLATE}" stroke="none"/>
<path d="M120 132h52v42h-52z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M116 126h60v8h-60z" fill="{TERRA}" stroke="none"/>
<path d="M100 152 100 56" stroke="{TERRA}" stroke-width="5" stroke-dasharray="0"/>
<path d="M100 48l-11 16h22z" fill="{TERRA}" stroke="none"/>
<circle cx="100" cy="158" r="6" fill="{TERRA}" stroke="none"/>
</g>'''

ART["huochezhan"] = f'''<g {W}>
<path d="M16 70h74v84H16z" fill="{PAPER}" stroke="{INK}"/>
<path d="M10 70 53 44l43 26z" fill="{SLATE}" stroke="{SLATE_D}"/>
<path d="M28 94h20v22H28z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M58 94h20v22H58z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M42 126h22v28H42z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M104 86h80v56h-80z" fill="{WARM}" stroke="{INK}"/>
<path d="M114 98h24v22h-24zM148 98h24v22h-24z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<circle cx="124" cy="150" r="9" fill="{PAPER}" stroke="{INK}" {W2}/>
<circle cx="164" cy="150" r="9" fill="{PAPER}" stroke="{INK}" {W2}/>
<path d="M96 166h94" stroke="{INK}" {W3}/>
<path d="M96 174h94" stroke="{BRASS}" {W2}/>
</g>'''

# 路 as a bus route: the destination board stays blank, because a number
# painted here would be rasterised by a font-less pipeline. The route is
# carried by the brass pips on the badge instead.
ART["lu"] = f'''<g {W}>
<path d="M44 44h112v126H44z" fill="{PAPER}" stroke="{INK}"/>
<path d="M56 56h88v20H56z" fill="{SLATE}" stroke="{SLATE_D}" {W3}/>
<path d="M56 88h88v44H56z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M100 88v44" stroke="{INK}" {W2}/>
<circle cx="66" cy="150" r="8" fill="{BRASS}" stroke="{INK}" {W2}/>
<circle cx="134" cy="150" r="8" fill="{BRASS}" stroke="{INK}" {W2}/>
<circle cx="100" cy="150" r="14" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<circle cx="94" cy="150" r="2.6" fill="{PAPER}" stroke="none"/>
<circle cx="100" cy="150" r="2.6" fill="{PAPER}" stroke="none"/>
<circle cx="106" cy="150" r="2.6" fill="{PAPER}" stroke="none"/>
<path d="M34 170h132" stroke="{INK}" {W3}/>
</g>'''

# ── Lesson 4 · the journey ─────────────────────────────────────────
ART["dianyingyuan"] = f'''<g {W}>
<path d="M28 62h144v108H28z" fill="{PAPER}" stroke="{INK}"/>
<path d="M18 62h164v28H18z" fill="{TERRA}" stroke="{TERRA_D}"/>
<circle cx="38" cy="98" r="4" fill="{BRASS}" stroke="none"/>
<circle cx="70" cy="98" r="4" fill="{BRASS}" stroke="none"/>
<circle cx="102" cy="98" r="4" fill="{BRASS}" stroke="none"/>
<circle cx="134" cy="98" r="4" fill="{BRASS}" stroke="none"/>
<circle cx="164" cy="98" r="4" fill="{BRASS}" stroke="none"/>
<path d="M40 112h40v26H40z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M46 120h28M46 130h20" stroke="{SLATE}" stroke-width="1.8"/>
<path d="M100 112h62v58h-62z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M131 112v58" stroke="{INK}" {W3}/>
<circle cx="126" cy="142" r="3" fill="{BRASS}" stroke="none"/>
<circle cx="136" cy="142" r="3" fill="{BRASS}" stroke="none"/>
<path d="M14 170h172" stroke="{INK}" {W3}/>
</g>'''

ART["chuan"] = f'''<g {W}>
<path d="M22 118h156l-22 40H44z" fill="{PAPER}" stroke="{INK}"/>
<path d="M56 78h92v40H56z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M68 90h16v14H68zM94 90h16v14H94zM120 90h16v14h-16z" fill="{PAPER}" stroke="{SLATE}" {W2}/>
<path d="M92 50h22v28H92z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
<path d="M92 60h22" stroke="{PAPER}" {W2}/>
<circle cx="48" cy="136" r="7" fill="{COOL}" stroke="{SLATE}" {W2}/>
<circle cx="152" cy="136" r="7" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M14 172q14-9 28 0t28 0 28 0 28 0 28 0 28 0" stroke="{SLATE}" {W3}/>
<path d="M14 186q14-9 28 0t28 0 28 0 28 0 28 0 28 0" stroke="{SLATE}" {W2}/>
</g>'''

ART["ranhou"] = f'''<g {W}>
<circle cx="26" cy="100" r="12" fill="{PAPER}" stroke="{INK}"/>
<circle cx="100" cy="100" r="12" fill="{PAPER}" stroke="{INK}"/>
<circle cx="174" cy="100" r="12" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M44 100h34" stroke="{SLATE}" stroke-width="5"/>
<path d="M86 100l-14-8v16z" fill="{SLATE}" stroke="none"/>
<path d="M118 100h34" stroke="{TERRA}" stroke-width="5"/>
<path d="M160 100l-14-8v16z" fill="{TERRA}" stroke="none"/>
<path d="M56 68v-14M138 68v-14" stroke="{BRASS}" {W2}/>
<path d="M46 54h22M128 54h22" stroke="{BRASS}" stroke-width="5"/>
</g>'''

# ── Lesson 5 · how long, and how far ───────────────────────────────
ART["shijian"] = f'''<g {W}>
<circle cx="100" cy="100" r="66" fill="{PAPER}" stroke="{INK}"/>
<path d="M100 40v12M160 100h-12M100 160v-12M40 100h12" stroke="{INK}" {W3}/>
<path d="M142 58l-8 8M142 142l-8-8M58 142l8-8M58 58l8 8" stroke="{SLATE}" {W2}/>
<path d="M100 100V62" stroke="{INK}" stroke-width="5"/>
<path d="M100 100l30 22" stroke="{INK}" stroke-width="5"/>
<circle cx="100" cy="100" r="5" fill="{INK}" stroke="none"/>
<path d="M100 22a78 78 0 0 1 68 40" stroke="{TERRA}" stroke-width="5" fill="none"/>
<path d="M168 62l-18-2 8 16z" fill="{TERRA}" stroke="none"/>
</g>'''

ART["dayue"] = f'''<g {W}>
<path d="M28 74q14-12 28 0t28 0 28 0 28 0 28 0" stroke="{TERRA}" stroke-width="5"/>
<path d="M28 98q14-12 28 0t28 0 28 0 28 0 28 0" stroke="{TERRA}" stroke-width="5"/>
<path d="M34 132v-14M166 132v-14" stroke="{SLATE}" {W3}/>
<path d="M34 132h132" stroke="{SLATE}" stroke-width="3.5"/>
<path d="M34 132l14-7v14zM166 132l-14-7v14z" fill="{SLATE}" stroke="none"/>
<circle cx="76" cy="158" r="5" fill="{BRASS}" stroke="none"/>
<circle cx="100" cy="158" r="5" fill="{BRASS}" stroke="none"/>
<circle cx="124" cy="158" r="5" fill="{BRASS}" stroke="none"/>
</g>'''

ART["feiji"] = f'''<g {W}>
<path d="M22 104q26-18 68-18h58l30 18-30 18H90q-42 0-68-18z" fill="{PAPER}" stroke="{INK}"/>
<path d="M112 86 92 44h16l32 42z" fill="{SLATE}" stroke="{SLATE_D}" {W3}/>
<path d="M74 104 48 138h18l34-34z" fill="{COOL}" stroke="{INK}" {W3}/>
<circle cx="70" cy="100" r="4" fill="{SLATE}" stroke="none"/>
<circle cx="88" cy="99" r="4" fill="{SLATE}" stroke="none"/>
<circle cx="106" cy="99" r="4" fill="{SLATE}" stroke="none"/>
<circle cx="124" cy="99" r="4" fill="{SLATE}" stroke="none"/>
<path d="M150 104h22" stroke="{TERRA}" {W3}/>
<path d="M30 160h140" stroke="{BRASS}" stroke-width="3" stroke-dasharray="12 10"/>
</g>'''

ART["jichang"] = f'''<g {W}>
<path d="M14 118h124v48H14z" fill="{PAPER}" stroke="{INK}"/>
<path d="M14 118q62-30 124 0" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M28 132h22v22H28zM62 132h22v22H62zM96 132h22v22H96z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M152 166V72" stroke="{INK}" {W3}/>
<path d="M176 166V72" stroke="{INK}" {W3}/>
<path d="M144 48h40v26h-40z" fill="{SLATE}" stroke="{SLATE_D}" {W3}/>
<path d="M150 56h28v12h-28z" fill="{COOL}" stroke="none"/>
<path d="M24 56q14-8 32-8h22l12 8-12 8H56q-18 0-32-8z" fill="{PAPER}" stroke="{TERRA}" {W3}/>
<path d="M62 48 52 28h8l15 20z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M44 64 34 82h7l13-18z" fill="{COOL}" stroke="{TERRA}" {W2}/>
<path d="M10 176h180" stroke="{BRASS}" stroke-width="3" stroke-dasharray="14 12"/>
</g>'''

# ── Lesson 6 · four more shops ─────────────────────────────────────
ART["shuiguodian"] = shop(MOSS, f'''<path d="M42 118h32v30H42z" fill="{WARM}" stroke="{INK}" {W2}/>
<circle cx="50" cy="112" r="8" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<circle cx="66" cy="112" r="8" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M82 118h30v30H82z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M84 112q14-14 26-2" stroke="{BRASS}" stroke-width="6"/>
<path d="M88 104q12-12 22-2" stroke="{BRASS}" stroke-width="6"/>''')

ART["shudian"] = shop(SLATE, f'''<path d="M44 100h66v22H44z" fill="{PAPER}" stroke="{INK}" {W2}/>
<path d="M56 100v22M68 100v22M80 100v22M94 100v22" stroke="{TERRA}" {W2}/>
<path d="M44 126h66v22H44z" fill="{PAPER}" stroke="{INK}" {W2}/>
<path d="M58 126v22M72 126v22M88 126v22M100 126v22" stroke="{MOSS}" {W2}/>''')

ART["lifadian"] = shop(TERRA, f'''<path d="M52 118h34v30H52z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M52 112h34v8H52z" fill="{COOL}" stroke="{INK}" {W2}/>
<path d="M60 148v10M78 148v10" stroke="{INK}" {W2}/>
<path d="M98 104h14v42H98z" fill="{PAPER}" stroke="{INK}" {W2}/>
<path d="M98 112l14-8M98 124l14-8M98 136l14-8M98 146l14-8" stroke="{TERRA}" {W2}/>''')

ART["kuaicandian"] = shop(BRASS, f'''<path d="M46 122q16-16 32 0z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M44 124h36v7H44z" fill="{MOSS}" stroke="{INK}" stroke-width="1.6"/>
<path d="M44 131h36v8H44z" fill="{TERRA}" stroke="{TERRA_D}" stroke-width="1.6"/>
<path d="M44 139h36v8H44z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M92 116h24l-4 32h-16z" fill="{PAPER}" stroke="{INK}" {W2}/>
<path d="M92 124h24" stroke="{SLATE}" {W2}/>
<path d="M112 116l6-16" stroke="{SLATE}" {W3}/>''')

# ── Activity scenes ────────────────────────────────────────────────
ART["jiedao"] = f'''<g {W}>
<path d="M12 72h44v92H12zM56 72h44v92H56zM100 72h44v92h-44zM144 72h44v92h-44z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M12 58h44v18H12z" fill="{TERRA}" stroke="{INK}" {W2}/>
<path d="M56 58h44v18H56z" fill="{SLATE}" stroke="{INK}" {W2}/>
<path d="M100 58h44v18h-44z" fill="{MOSS}" stroke="{INK}" {W2}/>
<path d="M144 58h44v18h-44z" fill="{BRASS}" stroke="{INK}" {W2}/>
<path d="M20 92h28v26H20zM64 92h28v26H64zM108 92h28v26h-28zM152 92h28v26h-28z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M26 130h16v34H26zM70 130h16v34H70zM114 130h16v34h-16zM158 130h16v34h-16z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M6 164h188" stroke="{INK}" {W3}/>
<path d="M6 176h188" stroke="{BRASS}" stroke-width="3" stroke-dasharray="12 10"/>
</g>'''

ART["ditu"] = f'''<g {W}>
<path d="M10 10h180v180H10z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M10 82h180v36H10z" fill="{COOL}" stroke="{INK}" {W2}/>
<path d="M82 10h36v180H82z" fill="{COOL}" stroke="{INK}" {W2}/>
<path d="M22 100h18M52 100h18M130 100h18M160 100h18" stroke="{PAPER}" stroke-width="4"/>
<path d="M100 22v16M100 52v16M100 132v16M100 162v16" stroke="{PAPER}" stroke-width="4"/>
<path d="M26 28h40v40H26z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M26 22h40v8H26z" fill="{TERRA}" stroke="none"/>
<path d="M134 28h40v40h-40z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M134 22h40v8h-40z" fill="{MOSS}" stroke="none"/>
<path d="M26 132h40v40H26z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M26 126h40v8H26z" fill="{SLATE}" stroke="none"/>
<path d="M134 132h40v40h-40z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M134 126h40v8h-40z" fill="{BRASS}" stroke="none"/>
</g>'''

ART["tijie"] = f'''<g {W}>
<path d="M100 20v160" stroke="{INK}" {W3}/>
<path d="M100 20l-10 16h20z" fill="{SLATE}" stroke="none"/>
<path d="M100 180l-10-16h20z" fill="{TERRA}" stroke="none"/>
<path d="M44 48h112M44 74h112M44 100h112M44 126h112M44 152h112" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 6"/>
<circle cx="100" cy="48" r="7" fill="{SLATE}" stroke="{SLATE_D}" {W2}/>
<circle cx="100" cy="74" r="7" fill="{PAPER}" stroke="{INK}" {W2}/>
<circle cx="100" cy="100" r="7" fill="{PAPER}" stroke="{INK}" {W2}/>
<circle cx="100" cy="126" r="7" fill="{PAPER}" stroke="{INK}" {W2}/>
<circle cx="100" cy="152" r="7" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
</g>'''

ART["tubiao"] = f'''<g {W}>
<path d="M14 34h172v132H14z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M14 34h172v26H14z" fill="{SLATE}" stroke="{SLATE_D}" {W2}/>
<path d="M57 34v132M100 34v132M143 34v132" stroke="{INK}" {W2}/>
<path d="M14 86h172M14 112h172M14 138h172" stroke="{INK}" stroke-width="2" stroke-dasharray="5 5"/>
<path d="M24 74h24M67 74h24M110 74h24M153 74h24" stroke="{PAPER}" stroke-width="4"/>
<path d="M24 100h22M67 100h18M110 100h24M153 100h14" stroke="{TERRA}" {W2}/>
<path d="M24 126h22M67 126h22M110 126h16M153 126h18" stroke="{INK}" {W2}/>
<path d="M24 152h22M67 152h16M110 152h22M153 152h12" stroke="{INK}" {W2}/>
</g>'''

ART["zhilu"] = f'''<g {W}>
<path d="M96 40v146" stroke="{INK}" stroke-width="7"/>
<path d="M96 52h74l18 17-18 17H96z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
<path d="M96 92H30l-18 17 18 17h66z" fill="{SLATE}" stroke="{SLATE_D}" {W3}/>
<path d="M96 132h58l18 17-18 17H96z" fill="{MOSS}" stroke="{INK}" {W3}/>
<path d="M118 69h34M48 109h34M118 149h24" stroke="{PAPER}" stroke-width="4"/>
<path d="M76 186h40" stroke="{INK}" {W3}/>
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
