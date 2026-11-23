#!/usr/bin/env python3
"""Draw entry.png: a one-page newspaper front page summing up world news
of Monday 23 November 2026. Pure Pillow vector drawing + text, so every
word stays crisp and legible. Run: python3 draw.py -> writes entry.png
(1024x1024, well under 1 MiB).

Stories verified by web search on 23 Nov 2026 (BBC / Reuters / AP /
AFP / Al Jazeera / TBS News): COP31 collapses in Antalya; two more
tankers hit mines near Hormuz; three Russian Kh-101 missiles fell in
Poland; Russian strike on a Kyiv apartment block; Friday market plunge
and Taiwan's 17.5% weekly fall; plus BepiColombo, FIFA/UK 2035,
Democrats' House majority, and the Russian ship hit off Libya.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
NAVY2 = (28, 48, 88)
RED = (178, 34, 34)
AMBER = (232, 163, 23)
TEAL = (18, 122, 110)
GREY = (90, 88, 82)
LINE = (200, 192, 175)

B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, text, f, x, y, max_w, fill=INK, leading=None):
    lh = leading or int(f.size * 1.28)
    for ln in wrap(d, text, f, max_w):
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 154], fill=AMBER)
d.text((36, 26), "THE WORLD IN ONE DAY", font=font(B, 46), fill=(255, 255, 255))
d.text((36, 96), "MONDAY  ·  23 NOVEMBER 2026", font=font(B, 30), fill=AMBER)
d.text((W - 36, 34), "ONE DAY.", font=font(B, 20), fill=(255, 255, 255), anchor="ra")
d.text((W - 36, 64), "ONE PAGE.", font=font(B, 20), fill=(255, 255, 255), anchor="ra")
d.text((W - 36, 94), "ONE IMAGE.", font=font(B, 20), fill=AMBER, anchor="ra")

# ---------- lead story: COP31 collapse ----------
LX, LY, LW, LH = 36, 164, 952, 260
d.rectangle([LX, LY, LX + LW, LY + LH], fill=(255, 255, 255), outline=LINE, width=2)
d.rectangle([LX, LY, LX + LW, LY + 8], fill=RED)
d.text((LX + 24, LY + 22), "LEAD  ·  CLIMATE  ·  ANTALYA", font=font(B, 22), fill=RED)
d.text((LX + 24, LY + 52), "COP31 collapses —", font=font(SB, 40), fill=INK)
d.text((LX + 24, LY + 98), "no deal on climate", font=font(SB, 40), fill=INK)
para(d, "After a record two days of overtime, the UN climate summit ends "
        "with no agreement. The EU rejects a pact that never mentions "
        "fossil fuels; the chair calls it \u201cvery disappointing\u201d. "
        "The 1.5\u00b0C goal now looks out of reach.",
     font(R, 22), LX + 24, LY + 152, 620, fill=(60, 60, 60), leading=27)

# globe icon, right side of lead panel
cx, cy, r = LX + 800, LY + 128, 68
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TEAL)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY2, width=3)
d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=(255, 255, 255), width=3)
d.line([(cx - r, cy), (cx + r, cy)], fill=(255, 255, 255), width=3)
d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360, fill=(255, 255, 255), width=3)
d.text((cx, cy + r + 8), "NO DEAL", font=font(B, 22), fill=RED, anchor="ma")

# ---------- 2x2 grid ----------
panels = [
    ("HORMUZ  ·  OIL", RED, "Two more tankers hit mines",
     "near the Strait of Hormuz",
     "Iran's navy says two supertankers caught fire after striking mines "
     "east of the strait. Two more were hit by projectiles on Saturday. "
     "Brent holds near $93."),
    ("POLAND  ·  NATO", NAVY2, "Three Russian missiles",
     "fell in Poland",
     "Polish prosecutors say all three objects that crashed on Friday "
     "were Russian Kh-101 cruise missiles. NATO's council meets in "
     "Brussels on Monday."),
    ("UKRAINE", TEAL, "Russian strike hits",
     "Kyiv apartment block",
     "A drone hits a five-storey block in Dymer, north of Kyiv: 2 killed, "
     "11 missing, among them two children. A boy, 7, is pulled alive "
     "from the rubble."),
    ("MARKETS", (110, 90, 20), "Stocks plunge as",
     "Asia braces for Monday",
     "US shares fall sharply on Friday. Taiwan's market is down 17.5% in "
     "a week; its regulator bans short selling."),
]
PX, PY = 36, 440
PW, PH, GAP = 466, 206, 20
for i, (kicker, col, h1, h2, body) in enumerate(panels):
    x = PX + (i % 2) * (PW + GAP)
    y = PY + (i // 2) * (PH + GAP)
    d.rectangle([x, y, x + PW, y + PH], fill=(255, 255, 255), outline=LINE, width=2)
    d.rectangle([x, y, x + 8, y + PH], fill=col)
    d.text((x + 26, y + 16), kicker, font=font(B, 20), fill=col)
    d.text((x + 26, y + 44), h1, font=font(SB, 28), fill=INK)
    d.text((x + 26, y + 80), h2, font=font(SB, 28), fill=INK)
    para(d, body, font(R, 18), x + 26, y + 118, PW - 52, fill=(60, 60, 60), leading=22)

# ---------- bottom strip ----------
BY = 884
d.rectangle([36, BY, 988, 988], fill=NAVY)
d.text((56, BY + 12), "ALSO ON 23 NOVEMBER", font=font(B, 20), fill=AMBER)
strip_left = [
    "Mercury: BepiColombo enters orbit — 2nd mission ever.",
    "Democrats take largest House majority since 1992.",
]
strip_right = [
    "FIFA to name UK host of 2035 Women's World Cup.",
    "Russian ship hit by suspected drones off Libya.",
]
for j, item in enumerate(strip_left):
    d.text((56, BY + 44 + j * 26), "\u2022  " + item, font=font(R, 16),
           fill=(255, 255, 255))
for j, item in enumerate(strip_right):
    d.text((540, BY + 44 + j * 26), "\u2022  " + item, font=font(R, 16),
           fill=(255, 255, 255))

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
