#!/usr/bin/env python3
"""
Modify l8-review-test-prep.pptx to:
1. Clone each exercise slide as an answer-reveal slide (showing all answers)
2. On the original exercise slides, hide answer text by clearing it
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
import copy
from lxml import etree
import re

PP = '/Users/luojiahai/Code/deck/index/designs/y7-l10/l8-review-test-prep/l8-review-test-prep.pptx'


def duplicate_slide(prs, slide_idx):
    """Duplicate slide at slide_idx, insert right after it."""
    slide = prs.slides[slide_idx]
    slide_layout = slide.slide_layout

    # Add new slide with same layout
    new_slide = prs.slides.add_slide(slide_layout)

    # Clear all default shapes from new slide's spTree
    spTree = new_slide.shapes._spTree
    to_remove = []
    for child in spTree:
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if tag in ('sp', 'pic', 'grpSp', 'cxnSp', 'graphicFrame'):
            to_remove.append(child)
    for child in to_remove:
        spTree.remove(child)

    # Copy shapes from original to new
    orig_spTree = slide.shapes._spTree
    for child in list(orig_spTree):
        tag = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if tag in ('sp', 'pic', 'grpSp', 'cxnSp', 'graphicFrame'):
            new_child = copy.deepcopy(child)
            spTree.append(new_child)

    # Move the new slide to right after the original
    ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}
    sldIdLst = prs._element.find('p:sldIdLst', ns)
    sldIds = list(sldIdLst)
    new_sldId = sldIds[-1]
    sldIdLst.remove(new_sldId)
    sldIdLst.insert(slide_idx + 1, new_sldId)

    return new_slide


def clear_text_shape(shape):
    """Clear all text from a shape."""
    txBody = shape._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}txBody')
    if txBody is not None:
        for p in list(txBody):
            tag = p.tag.split('}')[-1] if '}' in p.tag else p.tag
            if tag == 'p':
                txBody.remove(p)
        empty_p = etree.SubElement(txBody, '{http://schemas.openxmlformats.org/drawingml/2006/main}p')
        empty_r = etree.SubElement(empty_p, '{http://schemas.openxmlformats.org/drawingml/2006/main}r')
        empty_t = etree.SubElement(empty_r, '{http://schemas.openxmlformats.org/drawingml/2006/main}t')
        empty_t.text = ''


def get_shape_text(shape):
    """Get the full text content of a shape."""
    if not shape.has_text_frame:
        return ''
    return shape.text_frame.text


# ─── Warm-Up ─────────────────────────────────────────────

def hide_warmup_answers(slide):
    """Hide shapes with text starting with 'Answer:'."""
    for shape in slide.shapes:
        text = get_shape_text(shape).strip()
        if text.startswith('Answer:'):
            clear_text_shape(shape)
            print(f"    Hiding: '{text[:50]}'")


# ─── Round 1: Vocabulary Lightning ───────────────────────

# Pinyin pattern: letters with optional tone marks, space-separated
PINYIN_RE = re.compile(
    r'^[a-zA-ZāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜÜü]+(?:\s+[a-zA-ZāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜÜü]+)*$'
)

# Single digit or two digits (q-num badges)
QNUM_RE = re.compile(r'^\d{1,2}$')

# English text (no CJK, no digits-only, not labels)
def is_english_label(text):
    """Check if text is an English label (translation)."""
    if not text:
        return False
    # Skip single/double digits (q-num)
    if QNUM_RE.match(text):
        return False
    # Must be ASCII-only
    if not all(ord(c) < 128 for c in text):
        return False
    # Skip known non-answer labels
    skip_prefixes = (
        'Items', 'of ', 'pts', 'L8', 'Y7', 'Round', 'Format',
        '0–', '1–', '2–', '3–', '4–', '5–', '6–', '7–', '8–', '9–',
        '8–', 'EN ', '中文', 'Y7 Chinese', 'Vocabulary', 'Beat',
        'Game', 'Learning', 'We are', 'I can', 'I feel',
        'On your', 'Your', 'Final', 'Congratulations',
        'REVISIT', 'Error Bounty',
    )
    for pfx in skip_prefixes:
        if text.startswith(pfx):
            return False
    return True


def hide_r1_answers(slide):
    """Hide ↓ arrows, pinyin, and English translations.
    Keep: q-num (single digit), cn (Chinese character).
    Hide: ↓ arrows, py (pinyin with diacritics), en (English translations).
    """
    for shape in slide.shapes:
        text = get_shape_text(shape).strip()
        if not text:
            continue

        # Hide ↓ arrows
        if text == '↓':
            clear_text_shape(shape)
            print(f"    Hiding arrow: '{shape.name}'")
            continue

        # Keep q-num (1-2 digit numbers)
        if QNUM_RE.match(text):
            continue

        # Keep Chinese characters
        if re.search(r'[一-鿿]', text):
            continue

        # Hide pinyin (letters with tone marks, no digits)
        if PINYIN_RE.match(text):
            clear_text_shape(shape)
            print(f"    Hiding pinyin: '{text}'")
            continue

        # Hide English labels (translations)
        if is_english_label(text):
            clear_text_shape(shape)
            print(f"    Hiding English: '{text[:50]}'")


# ─── Round 2: Translation Showdown ─────────────────────

def hide_r2_answers(slide):
    """Hide ↓ arrows and answer text.
    Pattern: q-num (keep) → q-text (keep) → ↓ (hide) → a-text (hide) → pts-tag (keep)
    The answer text is the shape immediately after a ↓ arrow (and is not 'EN → 中文' or '中文 → EN').
    """
    # First pass: collect shape list and their text
    shape_data = [(s, get_shape_text(s).strip()) for s in slide.shapes]

    for i, (shape, text) in enumerate(shape_data):
        if text == '↓':
            # Hide the arrow
            clear_text_shape(shape)
            print(f"    Hiding arrow: '{shape.name}'")
            # The immediate next shape with text (that's not a pts-tag) is the answer
            for j in range(i + 1, min(i + 4, len(shape_data))):
                next_shape, next_text = shape_data[j]
                if next_text and next_text not in ('EN → 中文', '中文 → EN', '↓', ''):
                    clear_text_shape(next_shape)
                    print(f"    Hiding answer: '{next_text[:50]}'")
                    break


# ─── Round 3: Error Bounty ────────────────────────────

# Known "given" expressions that MUST be kept visible
GIVEN_TEXTS = {
    '二点十分', '四点三十分', '三点五分', '七差十分点',
    '六点十五分', '差十分二点', '九点三刻', '十二点六十',
}

# Known reason/correction patterns to hide
REASON_PATTERNS = {
    '二 → 两 before 点', 'No error', 'Need 零 for single-digit',
    'Word order: 差 X 分 Y 点', '60分 = 1 hour',
    'Need 零 for single-digit min', '60分 = 1 hour, rolls over',
}

# Labels/section text that should be preserved
KEEP_TEXTS = {
    'L8 · BEAT THE TEST', 'Round 3 · Error Bounty',
    'Y7 Chinese · Unit 4.1 Telling Time',
    '30–38 min · Round 3 · 20 pts each',
    'Error Bounty · 错误悬赏',
    'Spot the mistake & write the correct form — some are already right!',
    '8 items · 3 correct · 5 wrong',
}


def hide_r3_answers(slide):
    """Hide verdict badges, correction text, and reason text.
    Keep: q-num, given text, labels, footer.
    """
    for shape in slide.shapes:
        text = get_shape_text(shape).strip()
        if not text:
            continue

        # Hide verdict badges
        if 'WRONG' in text or 'CORRECT' in text:
            clear_text_shape(shape)
            print(f"    Hiding verdict: '{text[:50]}'")
            continue

        # Hide reason explanations
        if text in REASON_PATTERNS:
            clear_text_shape(shape)
            print(f"    Hiding reason: '{text[:50]}'")
            continue

        # Keep known labels
        if text in KEEP_TEXTS:
            continue

        # Keep q-num (single digits)
        if QNUM_RE.match(text):
            continue

        # Keep given texts (the original expressions students need to correct)
        if text in GIVEN_TEXTS:
            continue

        # Everything else with Chinese time vocabulary is likely a correction
        if re.search(r'[一-鿿]', text) and ('点' in text or '/' in text):
            clear_text_shape(shape)
            print(f"    Hiding correction: '{text[:50]}'")


# ─── Main ─────────────────────────────────────────────

def main():
    print("Opening PPTX...")
    prs = Presentation(PP)

    # Exercise slides to process (0-indexed, original 14-slide deck)
    # Process in REVERSE order so indices don't shift
    # Format: (index, label, hide_function)
    exercises = [
        (10, 'r3-items', hide_r3_answers),          # Slide 11
        (8,  'r2-items-b', hide_r2_answers),         # Slide 9
        (7,  'r2-items-a', hide_r2_answers),         # Slide 8
        (5,  'r1-items-b', hide_r1_answers),         # Slide 6
        (4,  'r1-items-a', hide_r1_answers),         # Slide 5
        (1,  'warm-up', hide_warmup_answers),        # Slide 2
    ]

    for orig_idx, label, hide_fn in exercises:
        print(f"\n--- Processing slide {orig_idx + 1} ({label}) ---")
        print(f"  Cloning slide {orig_idx + 1}...")
        duplicate_slide(prs, orig_idx)
        print(f"  Hiding answers on original...")
        hide_fn(prs.slides[orig_idx])

    print(f"\nTotal slides: {len(prs.slides)} (expecting 20)")
    print(f"Saving...")
    prs.save(PP)
    print(f"Done! Saved to {PP}")


if __name__ == '__main__':
    main()
