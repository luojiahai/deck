# -*- coding: utf-8 -*-
"""
Inline SVG garment drawings for the Y7 L14 (Clothing 穿着) decks.

Why SVG and not emoji: 👕👖 look fine in a browser and export as EMPTY BOXES
to PPTX and PDF, because the export path runs through Chromium, which ships
no colour emoji font. Some of the older decks in this repo have that bug.

Every drawing is a flat line figure on a 220×210 canvas, stroked in a single
token colour passed in as {C}. They are deliberately schematic — the job is
to be unmistakable from the back of a classroom, not to be illustrative.
The distinctions that actually carry meaning are drawn hard:

    长裤 vs 短裤   leg length
    衬衫 vs 汗衫   collar + placket + buttons vs round neck, no buttons
    毛衣 vs 外套   closed ribbed body vs open front with lapels
    裙子 vs 连衣裙  skirt alone vs bodice + skirt
    皮鞋 vs 运动鞋  smooth lace-up vs chunky striped sole
"""

_OPEN = ('<svg viewBox="0 0 220 210" xmlns="http://www.w3.org/2000/svg" '
         'fill="none" stroke-width="4.5" stroke-linecap="round" '
         'stroke-linejoin="round">')

SVGS = {

    # ── 穿 · the verb. A headless-featured pictogram figure with a garment
    #    going on, plus a motion arc. A circle for a head is a pictogram;
    #    a drawn face would be slop.
    "chuan": '''
      <circle cx="110" cy="32" r="21" stroke="#56514A"/>
      <path d="M74 90 L74 184 L146 184 L146 90" stroke="{C}"/>
      <path d="M74 90 L40 108 L52 144 L74 134" stroke="{C}"/>
      <path d="M146 90 L180 108 L168 144 L146 134" stroke="{C}"/>
      <path d="M74 90 L96 82 L110 102 L124 82 L146 90" stroke="{C}"/>
      <path d="M110 102 L110 184" stroke="{C}"/>
      <path d="M150 48 C 178 48, 186 66, 178 82" stroke="#2C4C7C" stroke-dasharray="7 8"/>
      <path d="M171 72 L178 85 L189 77" stroke="#2C4C7C"/>''',

    # ── 衬衫 · shirt: collar notch, placket, three buttons
    "shirt": '''
      <path d="M70 56 L70 188 L150 188 L150 56" stroke="{C}"/>
      <path d="M70 56 L34 76 L48 118 L70 106" stroke="{C}"/>
      <path d="M150 56 L186 76 L172 118 L150 106" stroke="{C}"/>
      <path d="M70 56 L92 48 L110 72 L128 48 L150 56" stroke="{C}"/>
      <path d="M110 72 L110 188" stroke="{C}"/>
      <circle cx="110" cy="98" r="4" fill="{C}" stroke="none"/>
      <circle cx="110" cy="128" r="4" fill="{C}" stroke="none"/>
      <circle cx="110" cy="158" r="4" fill="{C}" stroke="none"/>''',

    # ── 汗衫 · T-shirt: round neck, short sleeves, no buttons
    "tee": '''
      <path d="M74 64 L74 184 L146 184 L146 64" stroke="{C}"/>
      <path d="M74 64 L40 84 L52 122 L74 110" stroke="{C}"/>
      <path d="M146 64 L180 84 L168 122 L146 110" stroke="{C}"/>
      <path d="M74 64 C 88 54, 132 54, 146 64" stroke="{C}"/>
      <path d="M88 60 C 98 78, 122 78, 132 60" stroke="{C}"/>''',

    # ── 牛仔裤 · jeans: waistband, fly, pockets, belt loops
    "jeans": '''
      <path d="M68 44 L152 44 L147 190 L117 190 L110 112 L103 190 L73 190 Z" stroke="{C}"/>
      <path d="M69 66 L151 66" stroke="{C}"/>
      <path d="M110 66 L110 92" stroke="{C}"/>
      <path d="M78 74 L98 74 L94 94" stroke="{C}"/>
      <path d="M142 74 L122 74 L126 94" stroke="{C}"/>
      <path d="M84 44 L84 66 M136 44 L136 66" stroke="{C}"/>''',

    # ── 长裤 · trousers: same silhouette, no denim detailing, with a crease
    "trousers": '''
      <path d="M68 44 L152 44 L147 190 L117 190 L110 112 L103 190 L73 190 Z" stroke="{C}"/>
      <path d="M69 64 L151 64" stroke="{C}"/>
      <path d="M88 78 L88 186" stroke="{C}" stroke-dasharray="6 9"/>
      <path d="M132 78 L132 186" stroke="{C}" stroke-dasharray="6 9"/>''',

    # ── 短裤 · shorts: identical top, legs cut at the knee
    "shorts": '''
      <path d="M68 52 L152 52 L148 146 L118 146 L110 104 L102 146 L72 146 Z" stroke="{C}"/>
      <path d="M69 72 L151 72" stroke="{C}"/>
      <path d="M110 72 L110 96" stroke="{C}"/>''',

    # ── 裙子 · skirt: A-line with waistband and pleats
    "skirt": '''
      <path d="M80 54 L140 54 L170 178 L50 178 Z" stroke="{C}"/>
      <path d="M79 74 L141 74" stroke="{C}"/>
      <path d="M100 74 L92 176 M110 74 L110 176 M120 74 L128 176" stroke="{C}" stroke-dasharray="6 10"/>''',

    # ── 毛衣 · sweater: round neck, long sleeves, ribbed cuffs and hem
    "sweater": '''
      <path d="M72 62 L72 170 L148 170 L148 62" stroke="{C}"/>
      <path d="M72 62 L36 82 L48 150 L72 142" stroke="{C}"/>
      <path d="M148 62 L184 82 L172 150 L148 142" stroke="{C}"/>
      <path d="M72 62 C 88 52, 132 52, 148 62" stroke="{C}"/>
      <path d="M86 58 C 96 76, 124 76, 134 58" stroke="{C}"/>
      <path d="M72 170 L148 170 L148 188 L72 188 Z" stroke="{C}"/>
      <path d="M48 150 L72 142 L76 160 L52 168 Z" stroke="{C}"/>
      <path d="M172 150 L148 142 L144 160 L168 168 Z" stroke="{C}"/>''',

    # ── 外套 · coat: open front, lapels, buttons on one side
    "coat": '''
      <path d="M72 58 L72 190 L106 190 L106 74" stroke="{C}"/>
      <path d="M148 58 L148 190 L114 190 L114 74" stroke="{C}"/>
      <path d="M72 58 L36 78 L48 152 L70 144" stroke="{C}"/>
      <path d="M148 58 L184 78 L172 152 L150 144" stroke="{C}"/>
      <path d="M72 58 L96 50 L106 74 L92 94 Z" stroke="{C}"/>
      <path d="M148 58 L124 50 L114 74 L128 94 Z" stroke="{C}"/>
      <circle cx="122" cy="112" r="4" fill="{C}" stroke="none"/>
      <circle cx="122" cy="142" r="4" fill="{C}" stroke="none"/>
      <circle cx="122" cy="172" r="4" fill="{C}" stroke="none"/>''',

    # ── 衣服 · clothing in general: a rail with three garments on hangers
    "clothes": '''
      <path d="M24 44 L196 44" stroke="{C}"/>
      <path d="M62 44 L62 62 M110 44 L110 62 M158 44 L158 62" stroke="{C}"/>
      <path d="M44 76 L62 62 L80 76" stroke="{C}"/>
      <path d="M92 76 L110 62 L128 76" stroke="{C}"/>
      <path d="M140 76 L158 62 L176 76" stroke="{C}"/>
      <path d="M46 76 L42 150 L82 150 L78 76" stroke="{C}"/>
      <path d="M94 76 L92 170 L128 170 L126 76" stroke="{C}"/>
      <path d="M142 76 L138 146 L178 146 L174 76" stroke="{C}"/>''',

    # ── 校服 · school uniform: shirt with a tie
    "uniform": '''
      <path d="M70 58 L70 190 L150 190 L150 58" stroke="{C}"/>
      <path d="M70 58 L36 78 L50 118 L70 106" stroke="{C}"/>
      <path d="M150 58 L184 78 L170 118 L150 106" stroke="{C}"/>
      <path d="M70 58 L92 50 L110 76 L128 50 L150 58" stroke="{C}"/>
      <path d="M100 66 L110 78 L120 66" stroke="#B03C2C"/>
      <path d="M110 78 L100 96 L110 150 L120 96 Z" stroke="#B03C2C"/>
      <circle cx="132" cy="120" r="4" fill="{C}" stroke="none"/>
      <circle cx="132" cy="150" r="4" fill="{C}" stroke="none"/>''',

    # ── 帽子 · hat: cap with a brim
    "hat": '''
      <path d="M56 132 C 56 76, 164 76, 164 132" stroke="{C}"/>
      <path d="M40 132 C 40 150, 180 150, 180 132 Z" stroke="{C}"/>
      <path d="M40 132 L180 132" stroke="{C}"/>
      <path d="M56 116 C 90 106, 130 106, 164 116" stroke="{C}"/>''',

    # ── 手套 · gloves: a pair of mittens
    "gloves": '''
      <path d="M64 142 L64 92 C 64 70, 110 70, 110 92 L110 116" stroke="{C}"/>
      <path d="M110 116 C 130 110, 134 142, 112 146" stroke="{C}"/>
      <path d="M64 142 L112 146 L110 172 L62 168 Z" stroke="{C}"/>
      <path d="M76 146 L74 170 M90 148 L88 171" stroke="{C}"/>
      <path d="M132 138 L132 88 C 132 68, 172 68, 172 88 L172 138 L170 164 L130 164 Z"
            stroke="{C}" opacity="0.4"/>
      <path d="M132 88 C 118 84, 114 112, 130 116" stroke="{C}" opacity="0.4"/>''',

    # ── 围巾 · scarf: a looped scarf
    "scarf": '''
      <path d="M68 60 C 68 36, 152 36, 152 60 C 152 84, 68 84, 68 60 Z" stroke="{C}"/>
      <path d="M84 80 L78 160 L110 164 L110 82" stroke="{C}"/>
      <path d="M118 82 L126 148 L156 144 L146 78" stroke="{C}"/>
      <path d="M80 162 L78 180 M90 163 L88 181 M100 164 L98 182 M108 164 L107 182" stroke="{C}"/>
      <path d="M129 147 L133 164 M141 146 L145 163 M153 145 L157 162" stroke="{C}"/>''',

    # ── 袜子 · socks: a pair
    "socks": '''
      <path d="M56 48 L56 128 C 56 158, 90 170, 118 162 L146 152
               C 158 148, 158 130, 146 126 L100 114 L100 48 Z" stroke="{C}"/>
      <path d="M56 70 L100 70" stroke="{C}"/>
      <path d="M100 114 C 88 130, 92 148, 112 158" stroke="{C}" stroke-dasharray="6 8"/>
      <path d="M116 44 L116 120 L160 132 C 172 136, 172 152, 160 156 L140 162"
            stroke="{C}" opacity="0.4"/>
      <path d="M116 66 L160 66 L160 132" stroke="{C}" opacity="0.4"/>''',

    # ── 皮鞋 · leather shoes: smooth lace-up, side profile
    "leathershoe": '''
      <path d="M40 148 L40 120 C 40 100, 74 96, 86 112 C 102 134, 140 130, 170 134
               C 186 136, 188 148, 186 156 L40 156 Z" stroke="{C}"/>
      <path d="M40 156 L186 156" stroke="{C}"/>
      <path d="M56 116 L82 116 M52 128 L88 126" stroke="{C}"/>
      <path d="M120 134 C 136 122, 158 124, 170 134" stroke="{C}"/>''',

    # ── 运动鞋 · sneakers: chunky striped sole, laces
    "sneaker": '''
      <path d="M38 142 L38 116 C 38 96, 72 92, 84 108 C 100 130, 140 126, 168 130
               C 184 132, 188 140, 186 148 L38 148 Z" stroke="{C}"/>
      <path d="M34 148 L190 148 L190 166 L34 166 Z" stroke="{C}"/>
      <path d="M50 108 L80 116 M48 120 L84 126 M48 132 L88 136" stroke="{C}"/>
      <path d="M110 130 L118 148 M132 132 L140 148 M154 130 L160 148" stroke="{C}"/>''',

    # ── 西装 · suit: jacket with lapels over trousers
    "suit": '''
      <path d="M74 50 L74 132 L110 132 L110 64" stroke="{C}"/>
      <path d="M146 50 L146 132 L110 132" stroke="{C}"/>
      <path d="M74 50 L44 68 L56 112 L74 104" stroke="{C}"/>
      <path d="M146 50 L176 68 L164 112 L146 104" stroke="{C}"/>
      <path d="M74 50 L96 42 L110 64 L94 86 Z" stroke="{C}"/>
      <path d="M146 50 L124 42 L110 64 L126 86 Z" stroke="{C}"/>
      <circle cx="120" cy="104" r="4" fill="{C}" stroke="none"/>
      <path d="M80 132 L140 132 L136 196 L116 196 L110 156 L104 196 L84 196 Z" stroke="{C}"/>''',

    # ── 领带 · tie: knot and blade
    "tie": '''
      <path d="M88 46 L110 38 L132 46 L124 74 L96 74 Z" stroke="{C}"/>
      <path d="M96 74 L124 74 L136 88 L120 106 L100 106 L84 88 Z" stroke="{C}"/>
      <path d="M100 106 L120 106 L132 170 L110 192 L88 170 Z" stroke="{C}"/>''',

    # ── 长衫 · long gown: straight body, mandarin collar, side slit
    "gown": '''
      <path d="M82 60 L76 196 L144 196 L138 60" stroke="{C}"/>
      <path d="M82 60 L46 78 L58 140 L80 132" stroke="{C}"/>
      <path d="M138 60 L174 78 L162 140 L140 132" stroke="{C}"/>
      <path d="M98 54 L98 66 L122 66 L122 54" stroke="{C}"/>
      <path d="M98 54 C 106 46, 114 46, 122 54" stroke="{C}"/>
      <path d="M110 66 C 128 76, 134 88, 134 102 L134 196" stroke="{C}"/>
      <circle cx="126" cy="86" r="3.4" fill="{C}" stroke="none"/>
      <circle cx="134" cy="118" r="3.4" fill="{C}" stroke="none"/>
      <path d="M78 154 L78 196 M142 154 L142 196" stroke="{C}" stroke-dasharray="6 9"/>''',

    # ── 大衣 · overcoat: long, double-breasted, lapels
    "overcoat": '''
      <path d="M76 56 L68 194 L110 194 L110 72" stroke="{C}"/>
      <path d="M144 56 L152 194 L110 194" stroke="{C}"/>
      <path d="M76 56 L42 76 L54 142 L74 134" stroke="{C}"/>
      <path d="M144 56 L178 76 L166 142 L146 134" stroke="{C}"/>
      <path d="M76 56 L98 48 L110 72 L94 92 Z" stroke="{C}"/>
      <path d="M144 56 L122 48 L110 72 L126 92 Z" stroke="{C}"/>
      <circle cx="94" cy="112" r="4" fill="{C}" stroke="none"/>
      <circle cx="126" cy="112" r="4" fill="{C}" stroke="none"/>
      <circle cx="94" cy="144" r="4" fill="{C}" stroke="none"/>
      <circle cx="126" cy="144" r="4" fill="{C}" stroke="none"/>''',

    # ── 风衣 · windbreaker: trench with a tied belt
    "windbreaker": '''
      <path d="M76 56 L70 188 L110 188 L110 72" stroke="{C}"/>
      <path d="M144 56 L150 188 L110 188" stroke="{C}"/>
      <path d="M76 56 L42 76 L54 138 L74 130" stroke="{C}"/>
      <path d="M144 56 L178 76 L166 138 L146 130" stroke="{C}"/>
      <path d="M76 56 L98 48 L110 72 L94 90 Z" stroke="{C}"/>
      <path d="M144 56 L122 48 L110 72 L126 90 Z" stroke="{C}"/>
      <path d="M70 124 L150 124" stroke="{C}"/>
      <path d="M100 114 L120 114 L120 134 L100 134 Z" stroke="{C}"/>
      <path d="M120 124 L142 136" stroke="{C}"/>''',

    # ── 连衣裙 · dress: fitted bodice flaring into a skirt
    "dress": '''
      <path d="M80 58 L86 108 L54 186 L166 186 L134 108 L140 58" stroke="{C}"/>
      <path d="M80 58 L52 74 L62 104 L84 96" stroke="{C}"/>
      <path d="M140 58 L168 74 L158 104 L136 96" stroke="{C}"/>
      <path d="M80 58 C 94 48, 126 48, 140 58" stroke="{C}"/>
      <path d="M92 56 C 100 72, 120 72, 128 56" stroke="{C}"/>
      <path d="M86 108 L134 108" stroke="{C}"/>''',
}


def svg(name, colour="#2C4C7C"):
    """Return a complete <svg> element for a garment, stroked in `colour`."""
    if name not in SVGS:
        raise KeyError(f"no drawing for {name!r} — add it rather than "
                       f"falling back to an emoji")
    return _OPEN + SVGS[name].replace("{C}", colour) + "</svg>"


def swatch_svg(fill, ring="#221F1A"):
    """A plain colour disc, for colour words that have no object to draw."""
    return (f'<svg viewBox="0 0 220 210" xmlns="http://www.w3.org/2000/svg">'
            f'<circle cx="110" cy="110" r="74" fill="{fill}" '
            f'stroke="{ring}" stroke-opacity="0.2" stroke-width="4"/></svg>')
