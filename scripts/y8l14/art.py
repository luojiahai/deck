# -*- coding: utf-8 -*-
"""SVG drawings for the Y8 L14 家具 (Furniture) decks.

Flat two-tone line art on a 200x200 viewBox, in the Unit 5 palette shared
with y8-l13: graphite ink, slate blue, terracotta, brass. Objects and
diagrams only — no faces, no figures.

Never emoji: Chromium ships no colour emoji font and both the PPTX and the
PDF export run through Chromium, so an emoji renders as an empty box.

Never text either. These files are rasterised to PNG by export.sh, and the
rasteriser has no CJK font — a 汉字 inside an SVG would survive the browser
and vanish from the PowerPoint. So a measure word is shown by COUNTING: 张
is one sofa, then two, then three; 把 is the same with chairs. The first
version put brass tally strokes beside each row, which ran out of horizontal
room on the third row and silently drew one stroke next to three objects —
the diagram contradicted itself. The objects are the tally.

A word with no picturable referent gets no entry here and renders as a
textonly card instead. This lesson is almost entirely concrete — it is a
unit about furniture — so the only judgement calls are the two measure
words and 里面. All three get DIAGRAMS rather than scenes: 张 and 把 repeat
one object against a rising tally, and 里面 is one volume with a single
terracotta marker inside it. The marker is the only thing that carries
meaning, which is the teaching point.

Run:  python3 scripts/y8l14/art.py
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y8-l14", "img")

# fill="none" on the group is load-bearing: a <path> with only a stroke
# inherits the SVG default fill of black, which turns every leg, handle and
# vent into a solid black wedge. Shapes that want a fill declare one.
W = 'fill="none" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
W3 = 'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'
W2 = 'stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"'

INK = "#39414A"          # graphite, the drawing hand
SLATE = "#3D5A73"        # drafting ink blue
SLATE_D = "#263C4E"
TERRA = "#B05B3B"        # upholstery / marker
TERRA_D = "#7E3C24"
BRASS = "#A8801E"        # tallies, handles, dials
MOSS = "#4F7355"
PAPER = "#FDFDF8"        # white fill
COOL = "#DCE3E8"         # cool pale fill
WARM = "#EFE7DA"         # warm pale fill

ART = {}

# ── Lesson 1 · the living room ─────────────────────────────────────
ART["shafa"] = f'''<g {W}>
<path d="M30 78h140v46H30z" fill="{WARM}" stroke="{INK}"/>
<path d="M76 78v46M124 78v46" stroke="{INK}" {W3}/>
<path d="M18 92h26v56H18z" rx="6" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M156 92h26v56h-26z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M30 118h140v34H30z" fill="{COOL}" stroke="{INK}"/>
<path d="M36 152v18M164 152v18" stroke="{INK}" {W3}/>
<path d="M76 118v34M124 118v34" stroke="{SLATE}" {W2}/>
</g>'''

ART["chaji"] = f'''<g {W}>
<path d="M22 104h156v16H22z" fill="{WARM}" stroke="{INK}"/>
<path d="M40 120v50M160 120v50" stroke="{INK}"/>
<path d="M46 150h108v11H46z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M86 66h30v26H86z" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M116 72h12a8 8 0 0 1 0 16h-12" stroke="{SLATE}" {W3}/>
<path d="M88 78h26" stroke="{TERRA}" {W3}/>
<path d="M78 104h46" stroke="{BRASS}" stroke-width="2"/>
</g>'''

ART["dianshigui"] = f'''<g {W}>
<path d="M44 34h112v62H44z" fill="{SLATE}" stroke="{SLATE_D}"/>
<path d="M56 46h88v38H56z" fill="{COOL}" stroke="none"/>
<path d="M94 96h12v14H94z" fill="{INK}" stroke="none"/>
<path d="M26 110h148v50H26z" fill="{PAPER}" stroke="{INK}"/>
<path d="M100 110v50" stroke="{INK}" {W3}/>
<path d="M78 134h14M108 134h14" stroke="{BRASS}" stroke-width="5"/>
<path d="M38 160v12M162 160v12" stroke="{INK}" {W3}/>
</g>'''


# 张 — the measure word for flat things, counted by repeating this lesson's
# own 沙发. An abstract plank was tried first and read as a bookshelf board,
# which is the one object in this deck that 张 does not count.
ART["zhang"] = f'''<g {W}>
<g transform="translate(72,14)"><path d="M8 0h40v13H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M2 6h8v20H2zM46 6h8v20h-8z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M8 13h40v13H8z" fill="{COOL}" stroke="{INK}" {W3}/></g>
<g transform="translate(43,82)"><path d="M8 0h40v13H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M2 6h8v20H2zM46 6h8v20h-8z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M8 13h40v13H8z" fill="{COOL}" stroke="{INK}" {W3}/></g><g transform="translate(101,82)"><path d="M8 0h40v13H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M2 6h8v20H2zM46 6h8v20h-8z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M8 13h40v13H8z" fill="{COOL}" stroke="{INK}" {W3}/></g>
<g transform="translate(14,150)"><path d="M8 0h40v13H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M2 6h8v20H2zM46 6h8v20h-8z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M8 13h40v13H8z" fill="{COOL}" stroke="{INK}" {W3}/></g><g transform="translate(72,150)"><path d="M8 0h40v13H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M2 6h8v20H2zM46 6h8v20h-8z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M8 13h40v13H8z" fill="{COOL}" stroke="{INK}" {W3}/></g><g transform="translate(130,150)"><path d="M8 0h40v13H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M2 6h8v20H2zM46 6h8v20h-8z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M8 13h40v13H8z" fill="{COOL}" stroke="{INK}" {W3}/></g>
</g>'''

# ── Lesson 2 · appliances, and what is inside ──────────────────────
ART["kongtiao"] = f'''<g {W}>
<path d="M26 40h148v44a6 6 0 0 1-6 6H32a6 6 0 0 1-6-6z" fill="{PAPER}" stroke="{INK}"/>
<path d="M26 74h148" stroke="{INK}" {W3}/>
<path d="M40 82h120" stroke="{SLATE}" stroke-width="6"/>
<circle cx="152" cy="58" r="5" fill="{BRASS}" stroke="none"/>
<path d="M62 106c0 14-10 18-10 32s10 18 10 32" stroke="{SLATE}" {W3}/>
<path d="M100 106c0 14-10 18-10 32s10 18 10 32" stroke="{SLATE}" {W3}/>
<path d="M138 106c0 14-10 18-10 32s10 18 10 32" stroke="{SLATE}" {W3}/>
</g>'''

ART["xiyiji"] = f'''<g {W}>
<path d="M34 28h132v148H34z" fill="{PAPER}" stroke="{INK}"/>
<path d="M34 66h132" stroke="{INK}" {W3}/>
<circle cx="44" cy="47" r="6" fill="{BRASS}" stroke="none"/>
<circle cx="66" cy="47" r="6" fill="none" stroke="{SLATE}" {W2}/>
<path d="M120 42h36v10h-36z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<circle cx="100" cy="122" r="42" fill="{COOL}" stroke="{INK}"/>
<circle cx="100" cy="122" r="28" fill="{PAPER}" stroke="{SLATE}" {W3}/>
<path d="M78 122a22 22 0 0 0 44 0" stroke="{TERRA}" {W3}/>
<path d="M52 176v10M148 176v10" stroke="{INK}" {W3}/>
</g>'''

# 里面 — one volume, one marker, and the marker is inside it. The pale
# second marker outside is the contrast that makes "inside" mean anything.
ART["limian"] = f'''<g {W}>
<path d="M44 76 78 48h88v88l-34 28H44z" fill="{COOL}" stroke="{INK}"/>
<path d="M44 76h88v88M132 76l34-28" stroke="{INK}" {W3}/>
<circle cx="88" cy="120" r="15" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
<circle cx="182" cy="170" r="10" fill="none" stroke="{INK}" stroke-opacity="0.3" {W2}/>
</g>'''

# ── Lesson 3 · the kitchen ─────────────────────────────────────────
ART["bingxiang"] = f'''<g {W}>
<path d="M50 20h100v160H50z" fill="{PAPER}" stroke="{INK}"/>
<path d="M50 74h100" stroke="{INK}" {W3}/>
<path d="M136 34v28M136 88v34" stroke="{BRASS}" stroke-width="6"/>
<path d="M64 90h36v24H64z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M64 128h56" stroke="{SLATE}" {W2}/>
<path d="M64 148h56" stroke="{SLATE}" {W2}/>
<path d="M64 38h34v20H64z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M62 180v8M138 180v8" stroke="{INK}" {W3}/>
</g>'''

ART["kaoxiang"] = f'''<g {W}>
<path d="M26 44h148v112H26z" fill="{PAPER}" stroke="{INK}"/>
<path d="M26 78h148" stroke="{INK}" {W3}/>
<circle cx="48" cy="61" r="7" fill="none" stroke="{BRASS}" {W3}/>
<circle cx="76" cy="61" r="7" fill="none" stroke="{BRASS}" {W3}/>
<path d="M112 56h44v10h-44z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M44 96h112v48H44z" fill="{SLATE}" stroke="{SLATE_D}" {W3}/>
<path d="M58 112h84M58 128h84" stroke="{TERRA}" {W3}/>
<path d="M44 88h112" stroke="{BRASS}" stroke-width="6"/>
<path d="M40 156v10M160 156v10" stroke="{INK}" {W3}/>
</g>'''

ART["dianlu"] = f'''<g {W}>
<path d="M24 34h152v112H24z" fill="{COOL}" stroke="{INK}"/>
<circle cx="66" cy="68" r="20" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="134" cy="68" r="20" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="66" cy="118" r="20" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="134" cy="118" r="20" fill="{PAPER}" stroke="{TERRA}" {W3}/>
<circle cx="134" cy="118" r="11" fill="none" stroke="{TERRA}" {W2}/>
<path d="M44 68h-9M88 68h9" stroke="{SLATE_D}" {W3}/>
<circle cx="66" cy="68" r="17" fill="{SLATE}" stroke="{SLATE_D}" {W3}/>
<circle cx="66" cy="68" r="4.5" fill="{BRASS}" stroke="none"/>
<path d="M24 146h152v22H24z" fill="{PAPER}" stroke="{INK}" {W3}/>
<circle cx="66" cy="157" r="7" fill="none" stroke="{BRASS}" {W2}/>
<circle cx="100" cy="157" r="7" fill="none" stroke="{BRASS}" {W2}/>
<circle cx="134" cy="157" r="7" fill="none" stroke="{BRASS}" {W2}/>
</g>'''

# ── Lesson 4 · your own room ───────────────────────────────────────
ART["yizi"] = f'''<g {W}>
<path d="M62 24h58v84H62z" fill="{WARM}" stroke="{INK}"/>
<path d="M62 48h58M62 76h58" stroke="{INK}" {W3}/>
<path d="M44 106h92v16H44z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M52 122v56M128 122v56M62 122v56M138 122v56" stroke="{INK}" {W3}/>
<path d="M52 158h86" stroke="{INK}" {W2}/>
</g>'''

# 把 — the measure word for chairs. Same construction as 张: one object,
# three times, tally rising.
# 把 — the same construction with 椅子, so the two measure-word diagrams are
# a matched pair and the only difference a student sees is the object.
ART["ba"] = f'''<g {W}>
<g transform="translate(79,8)"><path d="M8 0h26v34H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M8 14h26" stroke="{INK}" {W2}/><path d="M0 34h42v9H0z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M5 43v13M37 43v13" stroke="{INK}" {W3}/></g>
<g transform="translate(50,72)"><path d="M8 0h26v34H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M8 14h26" stroke="{INK}" {W2}/><path d="M0 34h42v9H0z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M5 43v13M37 43v13" stroke="{INK}" {W3}/></g><g transform="translate(108,72)"><path d="M8 0h26v34H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M8 14h26" stroke="{INK}" {W2}/><path d="M0 34h42v9H0z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M5 43v13M37 43v13" stroke="{INK}" {W3}/></g>
<g transform="translate(21,136)"><path d="M8 0h26v34H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M8 14h26" stroke="{INK}" {W2}/><path d="M0 34h42v9H0z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M5 43v13M37 43v13" stroke="{INK}" {W3}/></g><g transform="translate(79,136)"><path d="M8 0h26v34H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M8 14h26" stroke="{INK}" {W2}/><path d="M0 34h42v9H0z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M5 43v13M37 43v13" stroke="{INK}" {W3}/></g><g transform="translate(137,136)"><path d="M8 0h26v34H8z" fill="{WARM}" stroke="{INK}" {W3}/><path d="M8 14h26" stroke="{INK}" {W2}/><path d="M0 34h42v9H0z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/><path d="M5 43v13M37 43v13" stroke="{INK}" {W3}/></g>
</g>'''

ART["shuzhuo"] = f'''<g {W}>
<path d="M18 96h164v16H18z" fill="{WARM}" stroke="{INK}"/>
<path d="M28 112h64v34H28z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M48 129h24" stroke="{BRASS}" stroke-width="5"/>
<path d="M32 146v34M170 112v68" stroke="{INK}"/>
<path d="M124 56h40v40h-40z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M144 96v-8" stroke="{SLATE}" {W3}/>
<path d="M56 62 76 42l14 24z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
<path d="M73 66v30" stroke="{INK}" {W3}/>
<path d="M62 96h22" stroke="{INK}" {W3}/>
</g>'''

# ── Lesson 5 · storage ─────────────────────────────────────────────
ART["yigui"] = f'''<g {W}>
<path d="M42 20h116v160H42z" fill="{PAPER}" stroke="{INK}"/>
<path d="M100 20v160" stroke="{INK}" {W3}/>
<path d="M88 92v20M112 92v20" stroke="{BRASS}" stroke-width="6"/>
<path d="M58 40h28v16H58z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M114 40h28v16h-28z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M52 180v10M148 180v10" stroke="{INK}" {W3}/>
<path d="M58 140h28M114 140h28" stroke="{SLATE}" stroke-opacity="0.5" {W2}/>
</g>'''

ART["shujia"] = f'''<g {W}>
<path d="M28 26h144v152H28z" fill="{PAPER}" stroke="{INK}"/>
<path d="M28 74h144M28 122h144" stroke="{INK}" {W3}/>
<path d="M44 38h12v36H44z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M60 38h10v36H60z" fill="{SLATE}" stroke="{SLATE_D}" {W2}/>
<path d="M74 42h12v32H74z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M90 40 106 44l-8 30-16-4z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M44 86h11v36H44z" fill="{SLATE}" stroke="{SLATE_D}" {W2}/>
<path d="M59 90h12v32H59z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M75 86h10v36H75z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M44 134h12v36H44z" fill="{WARM}" stroke="{INK}" {W2}/>
<path d="M60 138h11v32H60z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M75 134h10v36H75z" fill="{SLATE}" stroke="{SLATE_D}" {W2}/>
</g>'''

# ── Lesson 6 · the store, and the rooms being furnished ────────────
ART["jiajudian"] = f'''<g {W}>
<path d="M100 14 24 54h152z" fill="{TERRA}" stroke="{TERRA_D}"/>
<path d="M36 54h128v132H36z" fill="{PAPER}" stroke="{INK}"/>
<path d="M36 88h128M36 122h128M36 156h128" stroke="{INK}" {W3}/>
<path d="M52 64h30v16H52z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M52 98h30v16H52z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M52 132h30v16H52z" fill="{COOL}" stroke="{SLATE}" {W2}/>
<path d="M96 162h34v24H96z" fill="{WARM}" stroke="{INK}" {W3}/>
<circle cx="103" cy="175" r="3" fill="{BRASS}" stroke="none"/>
<path d="M176 54v34M176 88v34M176 122v34M176 156v30" stroke="{BRASS}" {W3}/>
<path d="M171 54h10M171 88h10M171 122h10M171 156h10M171 186h10" stroke="{BRASS}" stroke-width="2.5"/>
</g>'''

ART["keting"] = f'''<g {W}>
<path d="M20 40h160v130H20z" fill="{PAPER}" stroke="{INK}"/>
<path d="M112 62h56v40h-56z" fill="{SLATE}" stroke="{SLATE_D}" {W3}/>
<path d="M120 70h40v24h-40z" fill="{COOL}" stroke="none"/>
<path d="M112 110h56v24h-56z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M132 120h16" stroke="{BRASS}" {W3}/>
<path d="M34 104h56v18H34z" fill="{WARM}" stroke="{INK}" {W3}/>
<path d="M28 112h10v34H28z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M86 112h10v34H86z" fill="{TERRA}" stroke="{TERRA_D}" {W2}/>
<path d="M34 122h56v24H34z" fill="{COOL}" stroke="{INK}" {W3}/>
</g>'''

ART["chufang"] = f'''<g {W}>
<path d="M20 40h160v130H20z" fill="{PAPER}" stroke="{INK}"/>
<path d="M32 58h44v96H32z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M32 96h44" stroke="{INK}" {W3}/>
<path d="M66 70v16M66 106v18" stroke="{BRASS}" {W3}/>
<path d="M96 104h72v50H96z" fill="{WARM}" stroke="{INK}" {W3}/>
<circle cx="116" cy="122" r="10" fill="{PAPER}" stroke="{INK}" {W2}/>
<circle cx="148" cy="122" r="10" fill="{PAPER}" stroke="{TERRA}" {W2}/>
<path d="M104 138h56" stroke="{SLATE}" {W2}/>
<path d="M96 58h72v34H96z" fill="{COOL}" stroke="{SLATE}" {W3}/>
<path d="M126 68h12v14h-12z" fill="{PAPER}" stroke="{SLATE}" {W2}/>
</g>'''

ART["chuang"] = f'''<g {W}>
<path d="M16 40h24v100H16z" fill="{WARM}" stroke="{INK}"/>
<path d="M22 52h12v52H22z" fill="{COOL}" stroke="{INK}" {W2}/>
<path d="M40 92h146v30H40z" fill="{PAPER}" stroke="{INK}"/>
<path d="M40 122h146v13H40z" fill="{COOL}" stroke="{INK}" {W3}/>
<path d="M50 68h54v26H50z" fill="{PAPER}" stroke="{INK}" {W3}/>
<path d="M112 86h74v36h-74z" fill="{TERRA}" stroke="{TERRA_D}" {W3}/>
<path d="M112 100h74" stroke="{TERRA_D}" {W2}/>
<path d="M48 135v22M178 135v22" stroke="{INK}" {W3}/>
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
