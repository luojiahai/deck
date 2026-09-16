# -*- coding: utf-8 -*-
"""SVG drawings for the Y9 L15 邻居 (Neighbours) decks.

Flat two-tone line art, 200x200 viewBox, same convention and same Unit 5
palette as scripts/y9l13/art.py and scripts/y9l14/art.py — so an L13, an
L14 and an L15 deck read as one visual family on a projector.

Objects and diagrams only: no faces, no figures. 哭 is three falling tears
rather than a crying child, and 吵 is two speech bubbles colliding rather
than two people arguing — an AI-drawn human reads as wrong before it reads
as anything.

哭 was first drawn as a cot with a burst of sound over it, which is the
scene Text 1 describes (半夜听见孩子哭). On the projector it read as a
bench. Tears carry no scene, but they are unmistakable, and a drawing
nobody can identify teaches less than no drawing at all.

Words with no entry here render as textonly cards:

  最近  a time word
  烦人  a quality, not a thing
  把    a function word — there is nothing to draw
  注意  abstract
  办法  abstract
  声    deliberately textonly even though "sound" is picturable: the only
        honest drawing is radiating arcs, and this deck already spends
        them on 听见 (arcs arriving at an ear) and 响 (arcs leaving a
        television). A third arc diagram in the same lesson teaches the
        class that arcs mean nothing in particular.

Never emoji: Chromium ships no colour emoji font and any PDF/PPTX export
runs through Chromium, so an emoji renders as an empty box on the slide.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y9-l15", "img")

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

# ══ Lesson 1 · moving in ═══════════════════════════════════════════

ART["banjia"] = f'''<g {W}>
<path d="M12 160h176" stroke="{INK}" stroke-width="5"/>
<rect x="18" y="104" width="46" height="44" fill="{WARM}" stroke="{INK}"/>
<path d="M18 122h46M41 104v44" stroke="{INK2}" stroke-width="3"/>
<rect x="26" y="74" width="32" height="30" fill="{PAPER}" stroke="{INK}"/>
<path d="M42 74v30M26 88h32" stroke="{INK2}" stroke-width="3"/>
<rect x="74" y="86" width="64" height="52" fill="{PAPER}" stroke="{INK}"/>
<path d="M138 86h20l18 26v26h-38z" fill="{WARM}" stroke="{INK}"/>
<path d="M142 96h14l10 16h-24z" fill="{BLUE_F}" stroke="{INK}" stroke-width="3"/>
<path d="M82 100h48M82 114h48" stroke="{RED}" stroke-width="4"/>
<circle cx="96" cy="146" r="13" fill="{PAPER}" stroke="{INK}"/>
<circle cx="152" cy="146" r="13" fill="{PAPER}" stroke="{INK}"/>
</g>'''

ART["linju"] = f'''<g {W}>
<path d="M8 148h184" stroke="{INK}" stroke-width="5"/>
<path d="M10 92 54 56l44 36z" fill="{WARM}" stroke="{INK}"/>
<rect x="20" y="92" width="68" height="56" fill="{PAPER}" stroke="{INK}"/>
<rect x="30" y="104" width="22" height="20" fill="{BLUE_F}" stroke="{INK}" stroke-width="3"/>
<rect x="62" y="112" width="18" height="36" fill="{RED_F}" stroke="{INK}" stroke-width="3"/>
<path d="M102 92 146 56l44 36z" fill="{WARM}" stroke="{INK}"/>
<rect x="112" y="92" width="68" height="56" fill="{PAPER}" stroke="{INK}"/>
<rect x="148" y="104" width="22" height="20" fill="{BLUE_F}" stroke="{INK}" stroke-width="3"/>
<rect x="120" y="112" width="18" height="36" fill="{RED_F}" stroke="{INK}" stroke-width="3"/>
<path d="M94 110v38M100 110v38M106 110v38" stroke="{GREEN}" stroke-width="4"/>
<path d="M90 120h20M90 134h20" stroke="{GREEN}" stroke-width="4"/>
</g>'''

# ══ Lesson 2 · what you can hear ═══════════════════════════════════

ART["tingjian"] = f'''<g {W}>
<path d="M108 48C72 48 54 74 54 106c0 28 12 46 30 46 11 0 14-11 14-20
         0-11 8-16 16-16" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>
<path d="M104 76c-18 0-26 14-26 30" stroke="{INK2}" stroke-width="4"/>
<path d="M134 74a44 44 0 0 1 0 60" stroke="{RED}" stroke-width="5"/>
<path d="M150 62a62 62 0 0 1 0 84" stroke="{RED}" stroke-width="5"/>
<path d="M166 50a80 80 0 0 1 0 108" stroke="{RED_F}" stroke-width="5"/>
</g>'''

ART["xiang"] = f'''<g {W}>
<rect x="20" y="58" width="112" height="78" rx="8" fill="{PAPER}" stroke="{INK}"/>
<rect x="31" y="69" width="90" height="56" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<path d="M44 90h64M44 104h44" stroke="{INK2}" stroke-width="3"/>
<path d="M58 136l-8 18h56l-8-18" fill="{WARM}" stroke="{INK}"/>
<path d="M142 78a40 40 0 0 1 0 48" stroke="{RED}" stroke-width="5"/>
<path d="M158 66a58 58 0 0 1 0 72" stroke="{RED}" stroke-width="5"/>
<path d="M174 54a76 76 0 0 1 0 96" stroke="{RED_F}" stroke-width="5"/>
</g>'''

ART["banye"] = f'''<g {W}>
<circle cx="78" cy="106" r="48" fill="{PAPER}" stroke="{INK}"/>
<path d="M78 62v8M78 142v8M34 106h8M114 106h8" stroke="{INK2}" stroke-width="4"/>
<path d="M78 106V72" stroke="{INK}" stroke-width="6"/>
<path d="M78 106V62" stroke="{RED}" stroke-width="4"/>
<circle cx="78" cy="106" r="5" fill="{INK}" stroke="none"/>
<path d="M156 40a28 28 0 1 0 24 36 22 22 0 1 1-24-36z" fill="{AMBER_F}" stroke="{INK}"/>
<path d="M136 96l4 10 10 4-10 4-4 10-4-10-10-4 10-4z" fill="{AMBER}" stroke="none"/>
<path d="M172 116l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="{AMBER}" stroke="none"/>
</g>'''

ART["ku"] = f'''<g {W}>
<path d="M100 44c0 0 34 52 34 74a34 34 0 0 1-68 0c0-22 34-74 34-74z"
      fill="{BLUE_F}" stroke="{INK}" stroke-width="5"/>
<path d="M88 112c0 10 6 18 14 20" stroke="{PAPER}" stroke-width="5"/>
<path d="M42 92c0 0 22 34 22 48a22 22 0 0 1-44 0c0-14 22-48 22-48z"
      fill="{BLUE_F}" stroke="{INK}" stroke-width="4"/>
<path d="M158 92c0 0 22 34 22 48a22 22 0 0 1-44 0c0-14 22-48 22-48z"
      fill="{BLUE_F}" stroke="{INK}" stroke-width="4"/>
<path d="M76 168h48M52 178h96" stroke="{INK2}" stroke-width="4"/>
<path d="M100 32V18M66 44 56 30M134 44l10-14" stroke="{RED}" stroke-width="5"/>
</g>'''

# ══ Lesson 3 · the 把 sentence ═════════════════════════════════════

ART["chao"] = f'''<g {W}>
<rect x="14" y="54" width="74" height="52" rx="12" fill="{WARM}" stroke="{INK}"/>
<path d="M38 106l-8 20 26-20" fill="{WARM}" stroke="{INK}"/>
<path d="M28 74h46M28 88h30" stroke="{INK2}" stroke-width="4"/>
<rect x="112" y="78" width="74" height="52" rx="12" fill="{PAPER}" stroke="{INK}"/>
<path d="M162 130l8 20-26-20" fill="{PAPER}" stroke="{INK}"/>
<path d="M126 98h46M126 112h30" stroke="{INK2}" stroke-width="4"/>
<path d="M98 58l10 14-12 14 10 14-10 14" stroke="{RED}" stroke-width="6"/>
</g>'''

ART["xing"] = f'''<g {W}>
<path d="M20 74v66" stroke="{INK}" stroke-width="8"/>
<rect x="20" y="118" width="104" height="22" fill="{PAPER}" stroke="{INK}"/>
<rect x="32" y="102" width="88" height="16" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<rect x="36" y="86" width="32" height="16" rx="7" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>
<path d="M26 140v14M116 140v14" stroke="{INK}" stroke-width="5"/>
<circle cx="156" cy="112" r="24" fill="{PAPER}" stroke="{INK}"/>
<circle cx="139" cy="93" r="9" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<circle cx="173" cy="93" r="9" fill="{WARM}" stroke="{INK}" stroke-width="3"/>
<path d="M145 133l-7 12M167 133l7 12" stroke="{INK}" stroke-width="4"/>
<path d="M156 112V99M156 112l11 6" stroke="{INK}" stroke-width="4"/>
<path d="M124 100l-10-6M124 124l-10 6M188 100l9-6M188 124l9 6" stroke="{RED}" stroke-width="5"/>
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
