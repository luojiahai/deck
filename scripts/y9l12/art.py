# -*- coding: utf-8 -*-
"""SVG drawings for the Y9 L12 外出就餐 decks.

Flat two-tone line art, 200x200 viewBox, same convention as y9-l11/img.
Objects only - no faces, no figures. A word with no picturable referent
(饱, 饿, 只) gets no entry here and renders as a textonly card instead.
Never emoji: Chromium ships no colour emoji font and the PPTX/PDF export
runs through Chromium, so an emoji renders as an empty box on the slide.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y9-l12", "img")

W = 'stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'

ART = {}

# ── Lesson 1 · the buffet table ────────────────────────────────────
ART["zizhucan"] = f'''<g {W}>
<path d="M18 120h164v14H18z" fill="#E4D5BC" stroke="#5C4A37"/>
<path d="M30 134v42M170 134v42" stroke="#5C4A37"/>
<ellipse cx="58" cy="110" rx="30" ry="11" fill="#FDFBF3" stroke="#5C4A37"/>
<ellipse cx="120" cy="110" rx="26" ry="10" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M40 104c6-12 32-12 38 0z" fill="#B0472F" stroke="#7A2418" stroke-width="3"/>
<path d="M100 104c6-10 28-10 34 0z" fill="#2F6B44" stroke="#1E4A2E" stroke-width="3"/>
<rect x="150" y="92" width="30" height="20" rx="3" fill="#F2E0C0" stroke="#7A4426" stroke-width="3"/>
<path d="M150 98h30M150 105h30" stroke="#7A4426" stroke-width="2"/>
<path d="M26 92v-30M26 62l-8-14M26 62l8-14" stroke="#A8700F" stroke-width="4"/>
<path d="M54 74c10-8 28-8 38 0" stroke="#A8700F" stroke-width="3"/>
</g>'''

ART["longxia"] = f'''<g {W}>
<path d="M88 62h24c9 0 14 6 14 15v46H74V77c0-9 5-15 14-15z" fill="#B0472F" stroke="#7A2418"/>
<path d="M74 92h52M74 108h52" stroke="#7A2418" stroke-width="3"/>
<path d="M76 123h48l-3 17H79zM79 140h42l-4 17H83zM83 157h34l-5 16H88z" fill="#C8604A" stroke="#7A2418" stroke-width="3"/>
<path d="M100 173l-22 16c-3-11 4-20 12-24zM100 173l22 16c3-11-4-20-12-24z" fill="#C8604A" stroke="#7A2418" stroke-width="3"/>
<path d="M74 84 44 66" stroke="#7A2418" stroke-width="5"/>
<path d="M126 84l30-18" stroke="#7A2418" stroke-width="5"/>
<path d="M44 66c-12-7-24-2-26 9-2 12 9 20 20 17 9-2 13-11 10-19z" fill="#C8604A" stroke="#7A2418"/>
<path d="M156 66c12-7 24-2 26 9 2 12-9 20-20 17-9-2-13-11-10-19z" fill="#C8604A" stroke="#7A2418"/>
<path d="M22 70 8 60M178 70l14-10" stroke="#7A2418" stroke-width="4"/>
<path d="M74 100 50 112M74 114 52 130M126 100l24 12M126 114l22 16" stroke="#7A2418" stroke-width="3"/>
<path d="M92 62 80 26M108 62l12-36" stroke="#7A2418" stroke-width="3"/>
<circle cx="91" cy="74" r="4" fill="#3A1E0E" stroke="none"/>
<circle cx="109" cy="74" r="4" fill="#3A1E0E" stroke="none"/>
</g>'''

ART["sanwenyu"] = f'''<g {W}>
<path d="M28 82c26-22 118-22 144 0 6 8 6 28 0 36-26 22-118 22-144 0-6-8-6-28 0-36z" fill="#E4907E" stroke="#8A4230"/>
<path d="M40 88c22 6 100 6 122 0M40 112c22-6 100-6 122 0" stroke="#F7DCD2" stroke-width="6"/>
<path d="M36 100c24 8 104 8 128 0" stroke="#F7DCD2" stroke-width="7"/>
<ellipse cx="100" cy="150" rx="66" ry="14" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M60 146c8-6 18-6 26 0M116 146c8-6 18-6 26 0" stroke="#A8B5BE" stroke-width="3"/>
</g>'''

ART["shousi"] = f'''<g {W}>
<path d="M22 118h156v10H22z" fill="#8A5230" stroke="#3A1E0E" stroke-width="3"/>
<rect x="30" y="86" width="42" height="32" rx="6" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M30 92c14-12 30-12 42 0v-2c0-4-4-6-8-6H38c-4 0-8 2-8 6z" fill="#E4907E" stroke="#8A4230" stroke-width="3"/>
<rect x="80" y="86" width="42" height="32" rx="6" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M80 92c14-12 30-12 42 0v-2c0-4-4-6-8-6H88c-4 0-8 2-8 6z" fill="#E8A93A" stroke="#A8700F" stroke-width="3"/>
<rect x="130" y="80" width="42" height="38" rx="6" fill="#2B2018" stroke="#14110D" stroke-width="3"/>
<circle cx="151" cy="99" r="12" fill="#FDFBF3" stroke="#5C4A37" stroke-width="3"/>
<circle cx="151" cy="99" r="5" fill="#E4907E" stroke="none"/>
</g>'''

# ── Lesson 2 · roast, steak, desserts ──────────────────────────────
ART["kao"] = f'''<g {W}>
<path d="M28 108h144" stroke="#5C4A37"/>
<path d="M44 108v-16M64 108v-16M84 108v-16M104 108v-16M124 108v-16M144 108v-16M160 108v-16" stroke="#5C4A37" stroke-width="3"/>
<path d="M28 108h144v8H28z" fill="#8A5230" stroke="#3A1E0E" stroke-width="3"/>
<path d="M40 176c-6-16 4-26 8-34 4 12 12 10 12 22 0 8-8 14-20 12z" fill="#E8A93A" stroke="#A8700F" stroke-width="3"/>
<path d="M88 178c-8-20 6-32 10-42 5 14 16 12 16 28 0 10-10 18-26 14z" fill="#E8A93A" stroke="#A8700F" stroke-width="3"/>
<path d="M142 176c-6-16 4-26 8-34 4 12 12 10 12 22 0 8-8 14-20 12z" fill="#E8A93A" stroke="#A8700F" stroke-width="3"/>
<ellipse cx="100" cy="88" rx="36" ry="14" fill="#8A5230" stroke="#3A1E0E"/>
</g>'''

ART["niupai"] = f'''<g {W}>
<ellipse cx="100" cy="112" rx="78" ry="56" fill="#FDFBF3" stroke="#5C4A37"/>
<ellipse cx="100" cy="112" rx="62" ry="43" fill="none" stroke="#E0CFB3" stroke-width="3"/>
<path d="M56 100c8-22 44-30 66-16 18 12 24 34 8 46-20 16-58 12-70-6-4-6-6-14-4-24z" fill="#8A4230" stroke="#4E1E14"/>
<path d="M68 96c14 10 34 12 52 4M64 112c16 10 40 12 58 2M74 128c14 6 30 6 42 0" stroke="#5C2418" stroke-width="4"/>
<path d="M138 146l22 20M160 166l-6 6" stroke="#A8B5BE" stroke-width="4"/>
<path d="M42 142v22M36 142v22M48 142v22" stroke="#A8B5BE" stroke-width="3"/>
</g>'''

ART["tianpin"] = f'''<g {W}>
<path d="M22 106h74l-14 62c-1 6-6 8-12 8H48c-6 0-11-2-12-8z" fill="#F2E0C0" stroke="#7A4426"/>
<path d="M22 106h74" stroke="#7A4426"/>
<path d="M32 90c8-16 32-16 40 0z" fill="#C8607A" stroke="#7A2C42" stroke-width="3"/>
<circle cx="52" cy="76" r="8" fill="#B0472F" stroke="#7A2418" stroke-width="3"/>
<path d="M112 168h72l-10-62h-52z" fill="#E8C88C" stroke="#7A4426"/>
<path d="M104 106h88l-8-24h-72z" fill="#F2E0C0" stroke="#7A4426"/>
<path d="M110 130h66M112 148h62" stroke="#B0472F" stroke-width="5"/>
<circle cx="148" cy="72" r="9" fill="#B0472F" stroke="#7A2418" stroke-width="3"/>
</g>'''

ART["nailao"] = f'''<g {W}>
<path d="M28 138V96l72-34 72 34v42z" fill="#E8C88C" stroke="#A8700F"/>
<path d="M28 138h144v22H28z" fill="#D8A254" stroke="#A8700F"/>
<path d="M28 96l72 22 72-22" stroke="#A8700F" stroke-width="3"/>
<circle cx="66" cy="120" r="10" fill="#FDFBF3" stroke="#A8700F" stroke-width="3"/>
<circle cx="112" cy="112" r="8" fill="#FDFBF3" stroke="#A8700F" stroke-width="3"/>
<circle cx="142" cy="126" r="9" fill="#FDFBF3" stroke="#A8700F" stroke-width="3"/>
<circle cx="88" cy="146" r="7" fill="#FDFBF3" stroke="#A8700F" stroke-width="3"/>
</g>'''

# ── Lesson 4 · the menu and the duck ───────────────────────────────
ART["caidan"] = f'''<g {W}>
<path d="M30 34h140v144H30z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M30 34h140v26H30z" fill="#B0472F" stroke="#7A2418"/>
<path d="M50 78h100M50 96h100M50 114h78M50 132h92M50 150h64" stroke="#C9B392" stroke-width="5"/>
<path d="M140 78h10M140 96h10M140 114h10M140 132h10" stroke="#A8700F" stroke-width="5"/>
<path d="M60 48h80" stroke="#F2E0C0" stroke-width="5"/>
</g>'''

ART["diancai"] = f'''<g {W}>
<path d="M22 46h118v122H22z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M22 46h118v22H22z" fill="#2F6B44" stroke="#1E4A2E"/>
<path d="M40 86h82M40 104h82M40 122h58" stroke="#C9B392" stroke-width="5"/>
<circle cx="64" cy="104" r="11" fill="none" stroke="#B0472F" stroke-width="4"/>
<path d="M150 178l14-52c2-8 10-12 16-8 6 4 6 12 0 18l-20 22" fill="#E8C88C" stroke="#7A4426" stroke-width="3"/>
<path d="M164 126l-10 30" stroke="#7A4426" stroke-width="3"/>
<path d="M132 116l24-10" stroke="#7A4426" stroke-width="4"/>
</g>'''

ART["kaoya"] = f'''<g {W}>
<ellipse cx="100" cy="140" rx="80" ry="22" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M44 130c0-30 26-52 58-52s54 20 54 48c0 10-24 18-56 18s-56-8-56-14z" fill="#B0703A" stroke="#6B3A1E"/>
<path d="M60 106c18 8 66 8 84-2M56 122c20 8 72 8 92-2" stroke="#8A5230" stroke-width="4"/>
<path d="M156 108c10-6 18-16 18-28 0-10-8-16-16-12-6 4-8 14-6 22" fill="#B0703A" stroke="#6B3A1E" stroke-width="3"/>
<path d="M174 78l14-6-14-8z" fill="#E8A93A" stroke="#A8700F" stroke-width="3"/>
<circle cx="166" cy="80" r="3.5" fill="#3A1E0E" stroke="none"/>
<path d="M36 140c6-6 16-6 22 0" stroke="#A8B5BE" stroke-width="3"/>
</g>'''

# ── Lesson 5 · cooking methods ─────────────────────────────────────
ART["hongshao"] = f'''<g {W}>
<path d="M26 96h148c0 44-32 74-74 74s-74-30-74-74z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M26 96h148" stroke="#5C4A37"/>
<path d="M44 106h112c0 30-24 50-56 50s-56-20-56-50z" fill="#8A4230" stroke="#4E1E14" stroke-width="3"/>
<rect x="62" y="110" width="26" height="22" rx="3" fill="#D8A254" stroke="#7A4426" stroke-width="3"/>
<rect x="96" y="116" width="26" height="22" rx="3" fill="#D8A254" stroke="#7A4426" stroke-width="3"/>
<rect x="76" y="136" width="26" height="18" rx="3" fill="#D8A254" stroke="#7A4426" stroke-width="3"/>
<path d="M126 128c8 4 14 2 18-4" stroke="#2F6B44" stroke-width="5"/>
<path d="M74 176h52c0 6-11 10-26 10s-26-4-26-10z" fill="#E4D5BC" stroke="#5C4A37" stroke-width="3"/>
</g>'''

ART["zheng"] = f'''<g {W}>
<path d="M30 120h140v46H30z" fill="#E8C88C" stroke="#7A4426"/>
<path d="M30 120h140" stroke="#7A4426"/>
<path d="M36 142h128" stroke="#A8700F" stroke-width="3"/>
<path d="M26 104h148v16H26z" fill="#D8A254" stroke="#7A4426"/>
<path d="M22 88h156v16H22z" fill="#E8C88C" stroke="#7A4426"/>
<path d="M60 74c-8-10 4-18-2-28M100 70c-8-12 4-20-2-30M140 74c-8-10 4-18-2-28" stroke="#A8B5BE" stroke-width="5"/>
<path d="M96 166v12M104 166v12" stroke="#7A4426" stroke-width="3"/>
</g>'''

ART["rousi"] = f'''<g {W}>
<ellipse cx="100" cy="128" rx="78" ry="40" fill="#FDFBF3" stroke="#5C4A37"/>
<ellipse cx="100" cy="124" rx="62" ry="29" fill="#F1E8D8" stroke="#E0CFB3" stroke-width="3"/>
<g stroke="#8A4230" stroke-width="7" stroke-linecap="round" fill="none">
<path d="M52 118c18-8 40-10 62-4"/>
<path d="M58 132c20-10 50-10 72 0"/>
<path d="M66 106c16-6 38-6 54 2"/>
<path d="M74 142c18-6 40-6 56 2"/>
</g>
<g stroke="#2F6B44" stroke-width="5" stroke-linecap="round" fill="none">
<path d="M84 112c14 6 30 4 44-2"/>
<path d="M96 136c12 4 24 2 34-4"/>
</g>
</g>'''

ART["qingcai"] = f'''<g {W}>
<path d="M100 178V96" stroke="#6B8A3A"/>
<path d="M100 104c-22-6-40-26-38-48 22-4 42 12 48 34" fill="#4E8A3A" stroke="#2F5A22"/>
<path d="M100 104c22-6 40-26 38-48-22-4-42 12-48 34" fill="#6BA84A" stroke="#2F5A22"/>
<path d="M100 140c-18-4-32-20-32-38 18-2 34 10 40 28" fill="#6BA84A" stroke="#2F5A22"/>
<path d="M100 140c18-4 32-20 32-38-18-2-34 10-40 28" fill="#4E8A3A" stroke="#2F5A22"/>
<path d="M86 178h28c0 6-6 8-14 8s-14-2-14-8z" fill="#E4D5BC" stroke="#5C4A37" stroke-width="3"/>
</g>'''

# ── Lesson 6 · drinks ──────────────────────────────────────────────
ART["bei"] = f'''<g {W}>
<path d="M50 74h84v58c0 20-18 34-42 34s-42-14-42-34z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M50 74h84" stroke="#5C4A37"/>
<path d="M58 96h68v34c0 14-14 24-34 24s-34-10-34-24z" fill="#E4D5BC" stroke="#C9B392" stroke-width="3"/>
<path d="M134 92c20-6 30 6 30 18s-12 22-30 18" fill="none" stroke="#5C4A37"/>
<ellipse cx="100" cy="176" rx="44" ry="10" fill="#F1E8D8" stroke="#5C4A37"/>
<path d="M84 56c-6-8 4-14-2-22M112 56c-6-8 4-14-2-22" stroke="#A8B5BE" stroke-width="4"/>
</g>'''

ART["lucha"] = f'''<g {W}>
<path d="M58 60h84l-10 108c-1 8-8 12-16 12H84c-8 0-15-4-16-12z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M62 96h76l-8 72c-1 6-6 8-12 8H82c-6 0-11-2-12-8z" fill="#9EC46A" stroke="#6B8A3A" stroke-width="3"/>
<path d="M58 60h84" stroke="#5C4A37"/>
<path d="M88 130c8-10 20-12 30-4-10 8-22 10-30 4z" fill="#4E8A3A" stroke="#2F5A22" stroke-width="3"/>
<path d="M84 46c-6-8 4-14-2-22M116 46c-6-8 4-14-2-22" stroke="#A8B5BE" stroke-width="4"/>
</g>'''

ART["ping"] = f'''<g {W}>
<path d="M84 44h32v26c0 8 18 16 18 34v72c0 8-6 12-14 12H80c-8 0-14-4-14-12V104c0-18 18-26 18-34z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M80 28h40v18H80z" fill="#B0472F" stroke="#7A2418"/>
<path d="M66 114h68v58c0 6-4 10-12 10H78c-8 0-12-4-12-10z" fill="#8A4230" stroke="#4E1E14" stroke-width="3"/>
<rect x="72" y="126" width="56" height="30" rx="4" fill="#F2E0C0" stroke="#7A4426" stroke-width="3"/>
<path d="M82 136h36M82 146h26" stroke="#B0472F" stroke-width="4"/>
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
