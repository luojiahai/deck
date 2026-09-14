# -*- coding: utf-8 -*-
"""SVG drawings for the Y9 L11 零食 decks.

Flat two-tone line art, 200x200 viewBox, same convention as y8-l11/img.
Objects only - no faces, no figures. A word with no picturable referent
(各种各样, 比如, 从小, 总是, 加, 有时, 完) gets no entry here and renders
as a textonly card instead.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "index", "designs", "y9-l11", "img")

W = 'stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'

ART = {}

# ── Lesson 1 · snacks ──────────────────────────────────────────────
ART["lingshi"] = f'''<g {W}>
<path d="M54 58h92v112H54z" fill="#D8A254" stroke="#7A4426"/>
<path d="M48 38h104v22H48z" fill="#E8C88C" stroke="#7A4426"/>
<path d="M56 38v22M72 38v22M88 38v22M104 38v22M120 38v22M136 38v22" stroke="#7A4426" stroke-width="3"/>
<rect x="54" y="92" width="92" height="44" fill="#B0472F" stroke="#7A2418" stroke-width="3"/>
<path d="M66 106h68M66 122h44" stroke="#F2E0C0" stroke-width="6"/>
<circle cx="76" cy="76" r="9" fill="#F0DCA8" stroke="#7A4426" stroke-width="3"/>
<circle cx="124" cy="152" r="10" fill="#F0DCA8" stroke="#7A4426" stroke-width="3"/>
<circle cx="74" cy="154" r="8" fill="#6B3A1E" stroke="#3A1E0E" stroke-width="3"/>
</g>'''

ART["qiaokeli"] = f'''<g {W}>
<path d="M42 58h116v104H42z" fill="#6B3A1E" stroke="#3A1E0E"/>
<path d="M42 58 60 40h116l-18 18z" fill="#8A5230" stroke="#3A1E0E"/>
<path d="M158 58l18-18v104l-18 18z" fill="#4E2814" stroke="#3A1E0E"/>
<path d="M81 58v104M119 58v104M42 93h116M42 128h116" stroke="#3A1E0E" stroke-width="3"/>
</g>'''

ART["dangao"] = f'''<g {W}>
<path d="M40 96h120v58c0 6-4 10-10 10H50c-6 0-10-4-10-10z" fill="#E8C88C" stroke="#7A4426"/>
<path d="M40 96c0-14 27-24 60-24s60 10 60 24c0 8-27 14-60 14s-60-6-60-14z" fill="#F2E0C0" stroke="#7A4426"/>
<path d="M40 124h120" stroke="#7A4426" stroke-width="3"/>
<path d="M56 82c8 10 16 2 22 10M96 76c8 10 16 2 22 10M136 84c-6 8-12 2-16 8" stroke="#B0472F" stroke-width="5"/>
<circle cx="100" cy="58" r="13" fill="#B0472F" stroke="#7A2418"/>
<path d="M100 45V32" stroke="#2F6B44" stroke-width="5"/>
</g>'''

ART["bingqilin"] = f'''<g {W}>
<path d="M66 104h68l-34 74z" fill="#D8A254" stroke="#7A4426"/>
<path d="M78 122l14 30M110 112l-16 34M122 122l-12 26" stroke="#7A4426" stroke-width="3"/>
<circle cx="80" cy="88" r="24" fill="#F0DCA8" stroke="#7A4426"/>
<circle cx="122" cy="88" r="24" fill="#C8607A" stroke="#7A2C42"/>
<circle cx="101" cy="58" r="23" fill="#8A5230" stroke="#3A1E0E"/>
</g>'''

ART["binggan"] = f'''<g {W}>
<circle cx="70" cy="82" r="38" fill="#E8C88C" stroke="#7A4426"/>
<g fill="#6B3A1E" stroke="none">
<circle cx="58" cy="70" r="6"/><circle cx="84" cy="76" r="6"/>
<circle cx="64" cy="96" r="6"/><circle cx="88" cy="100" r="5"/>
</g>
<rect x="106" y="106" width="70" height="70" rx="8" fill="#F2E0C0" stroke="#7A4426"/>
<g fill="#7A4426" stroke="none">
<circle cx="124" cy="124" r="4"/><circle cx="146" cy="124" r="4"/><circle cx="162" cy="124" r="4"/>
<circle cx="124" cy="146" r="4"/><circle cx="146" cy="146" r="4"/><circle cx="162" cy="146" r="4"/>
<circle cx="124" cy="164" r="4"/><circle cx="146" cy="164" r="4"/><circle cx="162" cy="164" r="4"/>
</g>
</g>'''

# ── Lesson 2 · teeth, a proper meal ────────────────────────────────
ART["yachi"] = f'''<g {W}>
<path d="M100 32c34 0 52 20 52 48 0 24-10 34-14 58-3 18-8 30-16 30s-10-14-12-30c-2-14-4-20-10-20s-8 6-10 20c-2 16-4 30-12 30s-13-12-16-30c-4-24-14-34-14-58 0-28 18-48 52-48z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M74 62c6-8 16-12 26-12" stroke="#A8700F" stroke-width="5"/>
<path d="M160 44l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="#A8700F" stroke="none"/>
</g>'''

ART["zhengcan"] = f'''<g {W}>
<ellipse cx="98" cy="128" rx="74" ry="30" fill="#F2E0C0" stroke="#7A4426"/>
<ellipse cx="98" cy="122" rx="62" ry="24" fill="#FDFBF3" stroke="#7A4426" stroke-width="3"/>
<path d="M56 122c0-14 10-22 22-22s22 8 22 22z" fill="#FDFBF3" stroke="#5C4A37" stroke-width="3"/>
<path d="M104 112h34c4 0 6 4 4 8l-4 10h-34z" fill="#B0472F" stroke="#7A2418" stroke-width="3"/>
<path d="M112 100c8-12 22-12 28 0" fill="#2F6B44" stroke="#1E4A2D" stroke-width="3"/>
<path d="M150 58l-4 44M164 58l-2 44" stroke="#7A4426" stroke-width="5"/>
</g>'''

# ── Lesson 3 · breakfast ───────────────────────────────────────────
ART["gulei"] = f'''<g {W}>
<path d="M34 96h132c0 40-30 70-66 70s-66-30-66-70z" fill="#FDFBF3" stroke="#7A4426"/>
<path d="M34 96h132" stroke="#7A4426"/>
<g fill="#D8A254" stroke="#7A4426" stroke-width="3">
<circle cx="66" cy="86" r="11"/><circle cx="100" cy="80" r="11"/><circle cx="134" cy="86" r="11"/>
<circle cx="83" cy="102" r="10"/><circle cx="117" cy="102" r="10"/>
</g>
<path d="M60 140c14 10 66 10 80 0" stroke="#A8C8E0" stroke-width="5"/>
</g>'''

ART["niunai"] = f'''<g {W}>
<path d="M34 78h56v92H34z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M34 78 62 42l28 36z" fill="#EDF3F8" stroke="#5C4A37"/>
<path d="M44 112h36M44 132h26" stroke="#3F6B8A" stroke-width="5"/>
<path d="M112 84h54l-8 86h-38z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M114 108h50l-6 62h-38z" fill="#F2F6FA" stroke="none"/>
</g>'''

ART["mianbao"] = f'''<g {W}>
<path d="M34 104c0-30 22-48 50-48s50 18 50 48v56c0 6-4 10-10 10H44c-6 0-10-4-10-10z" fill="#D8A254" stroke="#7A4426"/>
<path d="M34 118h100" stroke="#7A4426" stroke-width="3"/>
<path d="M54 82c6-10 16-14 26-14M96 70c10 2 18 8 22 16" stroke="#7A4426" stroke-width="3"/>
<path d="M134 118c0-22 14-34 30-34s30 12 30 34v42c0 6-4 10-10 10h-40c-6 0-10-4-10-10z" fill="#F2E0C0" stroke="#7A4426"/>
<path d="M148 128h34" stroke="#7A4426" stroke-width="3"/>
</g>'''

ART["jiandan"] = f'''<g {W}>
<path d="M52 108c-18-6-22-30-6-44 8-8 10-24 28-28 16-4 24 8 38 6 20-2 34 10 32 28-2 16 12 22 8 38-4 18-26 20-38 28-14 10-32 8-42-4-8-10-4-18-20-24z" fill="#FDFBF3" stroke="#5C4A37"/>
<circle cx="100" cy="102" r="30" fill="#E8A93A" stroke="#A8700F"/>
<circle cx="90" cy="92" r="8" fill="#F2C766" stroke="none"/>
</g>'''

ART["xiangchang"] = f'''<g {W}>
<path d="M52 62c26-12 50 4 56 30 6 26-6 48-28 54" fill="none" stroke="#7A2418" stroke-width="34" stroke-linecap="round"/>
<path d="M52 62c26-12 50 4 56 30 6 26-6 48-28 54" fill="none" stroke="#B0472F" stroke-width="24" stroke-linecap="round"/>
<path d="M104 92c26-12 50 4 56 30 6 26-6 44-28 50" fill="none" stroke="#7A2418" stroke-width="34" stroke-linecap="round"/>
<path d="M104 92c26-12 50 4 56 30 6 26-6 44-28 50" fill="none" stroke="#B0472F" stroke-width="24" stroke-linecap="round"/>
<path d="M66 74l10 6M92 118l12 2M118 104l10 6M144 148l12 2" stroke="#7A2418" stroke-width="4"/>
</g>'''

# ── Lesson 4 · lunch & dinner ──────────────────────────────────────
ART["shala"] = f'''<g {W}>
<path d="M30 104h140c0 38-30 66-70 66s-70-28-70-66z" fill="#FDFBF3" stroke="#7A4426"/>
<path d="M30 104h140" stroke="#7A4426"/>
<path d="M46 102c-4-18 10-32 26-26 4-16 24-20 34-8 12-10 30-2 30 12 16 0 22 14 18 22z" fill="#5E8F35" stroke="#33531C"/>
<circle cx="76" cy="86" r="12" fill="#B0472F" stroke="#7A2418" stroke-width="3"/>
<circle cx="126" cy="92" r="11" fill="#7FA84A" stroke="#33531C" stroke-width="3"/>
</g>'''

ART["suannai"] = f'''<g {W}>
<path d="M56 84h84l-10 84H66z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M52 74h92v14H52z" fill="#C8607A" stroke="#7A2C42"/>
<path d="M144 76c18-14 30-10 34 0-14 6-22 12-34 8z" fill="#EDD0DA" stroke="#7A2C42"/>
<path d="M72 110h52M74 132h36" stroke="#C8607A" stroke-width="4"/>
</g>'''

ART["zacaitang"] = f'''<g {W}>
<path d="M28 106h144c0 40-32 68-72 68s-72-28-72-68z" fill="#FDFBF3" stroke="#7A4426"/>
<path d="M40 106h120c0 14-4 22-8 26H48c-4-4-8-12-8-26z" fill="#D8A254" stroke="none"/>
<path d="M28 106h144" stroke="#7A4426"/>
<circle cx="70" cy="116" r="9" fill="#B0472F" stroke="#7A2418" stroke-width="3"/>
<circle cx="100" cy="122" r="9" fill="#5E8F35" stroke="#33531C" stroke-width="3"/>
<circle cx="130" cy="116" r="9" fill="#E8A93A" stroke="#A8700F" stroke-width="3"/>
<path d="M74 74c-8-10 8-18 0-28M100 68c-8-10 8-18 0-28M126 74c-8-10 8-18 0-28" stroke="#A8B5BE" stroke-width="5"/>
</g>'''

ART["wan"] = f'''<g {W}>
<path d="M28 82h144c0 46-32 78-72 78s-72-32-72-78z" fill="#FDFBF3" stroke="#5C4A37"/>
<path d="M28 82h144" stroke="#5C4A37"/>
<ellipse cx="100" cy="82" rx="72" ry="14" fill="#EDF3F8" stroke="#5C4A37"/>
<path d="M76 168h48c0 6-10 10-24 10s-24-4-24-10z" fill="#E4D5BC" stroke="#5C4A37"/>
<path d="M46 104c4 22 18 38 36 44" stroke="#A8B5BE" stroke-width="5"/>
</g>'''

# ── Lesson 5 · helping ─────────────────────────────────────────────
ART["bangmang"] = f'''<g {W}>
<path d="M26 106h148l-12 60c-1 6-6 10-12 10H50c-6 0-11-4-12-10z" fill="#EDF3F8" stroke="#5C4A37"/>
<path d="M26 106h148" stroke="#5C4A37"/>
<g fill="#FDFBF3" stroke="#A8B5BE" stroke-width="3">
<circle cx="54" cy="88" r="14"/><circle cx="82" cy="72" r="11"/>
<circle cx="112" cy="80" r="13"/><circle cx="140" cy="66" r="10"/>
<circle cx="160" cy="88" r="12"/>
</g>
<path d="M52 148h56c0 12-13 20-28 20s-28-8-28-20z" fill="#FDFBF3" stroke="#5C4A37" stroke-width="3"/>
<path d="M60 134h40c0 10-9 16-20 16s-20-6-20-16z" fill="#FDFBF3" stroke="#5C4A37" stroke-width="3"/>
<rect x="122" y="132" width="44" height="26" rx="9" fill="#E8A93A" stroke="#A8700F" stroke-width="3"/>
<path d="M134 140v10M146 140v10M158 140v10" stroke="#A8700F" stroke-width="3"/>
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
