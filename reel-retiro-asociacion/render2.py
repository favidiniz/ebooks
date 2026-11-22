#!/usr/bin/env python3
"""Reel Retiro de Asociación RC — v2 (tarjetas, notas a mano, flechas, cierre con escudo/logo).
Uso:  render2.py stills OUTDIR   |   render2.py video OUT.mp4   |   render2.py preview OUT.mp4 (540p)
Recursos opcionales: assets/escudo.png y assets/logo.png (PNG transparentes).
"""
import sys, os, glob, subprocess, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/..")
CLIPS, FONTS, ASSETS = BASE + "/dl/clips", BASE + "/fonts", BASE + "/assets"
W, H, FPS = 1080, 1920, 30

VINO = (110, 22, 38); VINO_D = (70, 10, 22); VINO_L = (142, 36, 56)
WHITE = (255, 255, 255); PAPER = (253, 250, 246)
GOLD = (222, 186, 110); GOLD_D = (168, 128, 52)

_fc = {}
def F(name, size, wght=None):
    k = (name, size, wght)
    if k not in _fc:
        f = ImageFont.truetype(f"{FONTS}/{name}", size)
        if wght:
            try: f.set_variation_by_axes([wght])
            except Exception: pass
        _fc[k] = f
    return _fc[k]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def ease_io(x): x = clamp(x); return x * x * (3 - 2 * x)
def back_out(x, s=1.9):
    x = clamp(x); x -= 1; return x * x * ((s + 1) * x + s) + 1

# ------------------------------------------------------------------ EDL
SHOTS = [
    ("dd5b9a05", 0.6, 3.6, 1.0),   # 0 apertura
    ("3c461547", 2.0, 2.0, 1.0),   # 1  M1
    ("f33d8239", 2.4, 2.0, 1.0),   # 2
    ("7f233f9c", 0.4, 2.0, 1.0),   # 3
    ("c76ca9ef", 4.6, 1.9, 1.0),   # 4  M2
    ("06e849d0", 0.0, 1.4, 1.0),   # 5
    ("aaceadd2", 0.6, 2.5, 1.0),   # 6
    ("11a86873", 0.5, 1.8, 1.0),   # 7  M3
    ("4b9f4e5d", 1.5, 2.2, 1.0),   # 8
    ("6c0fab77", 0.6, 1.8, 1.0),   # 9
    ("0a166d44", 1.4, 1.8, 1.0),   # 10 M4
    ("16a80705", 0.0, 1.7, 1.0),   # 11
    ("6f447e5e", 0.3, 2.2, 1.0),   # 12
    ("8838e0f4", 2.6, 2.0, 1.0),   # 13 M5
    ("994afafb", 1.6, 2.0, 1.0),   # 14
    ("74ae2ba7", 1.0, 2.0, 1.0),   # 15
    ("ebac2810", 0.5, 2.0, 1.0),   # 16 M6
    ("8ca61869", 1.6, 2.0, 1.0),   # 17
    ("b6c4ebad", 0.5, 2.0, 1.0),   # 18
    ("1676024b", 0.5, 2.0, 1.0),   # 19 M7
    ("699af540", 1.0, 2.0, 1.0),   # 20
    ("1413d3cc", 2.0, 2.0, 1.0),   # 21
    ("79df9735", 3.6, 1.8, 1.0),   # 22 M8
    ("7f1ee76f", 5.0, 1.9, 1.0),   # 23
    ("fb2ef70c", 6.0, 1.9, 1.0),   # 24
    ("c795e18c", 12.4, 4.6, 0.7),  # 25 cita (cielo + estatua)
    (None, 0, 3.8, 1.0),           # 26 tarjeta final vinotinto
]
starts, acc = [], 0.0
for s in SHOTS: starts.append(acc); acc += s[2]
TOTAL = acc
def sb(i): return starts[i], starts[i] + SHOTS[i][2]
QUOTE, END = 25, 26

MOMENTS = [
    (1, 3,  "01", [("Reconozco",0),("mi",0),("sed",1)]),
    (4, 6,  "02", [("Dejo",0),("que",0),("Él",1),("me",0),("encuentre",0)]),
    (7, 9,  "03", [("Soy",0),("amada,",1),("soy",0),("hija",1)]),
    (10,12, "04", [("Le",0),("dejo",0),("hablar",0),("a",0),("mi",0),("corazón",1)]),
    (13,15, "05", [("Comprendo",0),("mi",0),("vocación",1)]),
    (16,18, "06", [("Soy",0),("apóstol",0),("del",0),("agua",1),("viva",1)]),
    (19,21, "07", [("Reconozco",0),("el",0),("don",1)]),
    (22,24, "08", [("Soy",0),("enviada",1)]),
]
# Notas a mano: plano -> (texto, (x,y) texto, (x,y) punta de flecha, curvatura)
NOTES = {
    0:  ("¡todas juntas!", (330, 790), (470, 935), -0.35),
    1:  ("la Eucaristía", (740, 420), (520, 640), 0.35),
    8:  ("escuchando con el corazón", (420, 520), (760, 860), -0.3),
    13: ("recorriendo la casa", (380, 560), (640, 960), 0.3),
    16: ("¡hola!", (220, 560), (300, 860), -0.4),
    19: ("nuestra Madre", (290, 330), (560, 470), 0.35),
    24: ("¡nos vamos!", (300, 420), (520, 700), -0.35),
}
# Polaroids con las fotos de la carpeta: plano -> (archivo, centro, ancho, giro, pie)
POLAROIDS = {
    2:  ("0ffc2070", (790, 480), 380, 6, "la charla"),
    20: ("de430a7d", (300, 470), 400, -6, "María"),
}

# ------------------------------------------------------------------ utilidades de dibujo
def shadow_of(rgba, blur=18, alpha=0.38, off=(0, 14)):
    a = rgba.split()[3].point(lambda v: int(v * alpha))
    pad = blur * 3
    sh = Image.new("RGBA", (rgba.width + pad * 2, rgba.height + pad * 2), (20, 4, 8, 0))
    m = Image.new("L", sh.size, 0); m.paste(a, (pad, pad))
    sh.putalpha(m.filter(ImageFilter.GaussianBlur(blur)))
    return sh, (off[0] - pad, off[1] - pad)

def place(canvas, rgba, cx, cy, scale=1.0, rot=0.0, alpha=1.0, shadow=True):
    if alpha <= 0.01 or scale <= 0.02: return
    im = rgba
    if scale != 1.0:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
    if rot: im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    if alpha < 1: im.putalpha(im.split()[3].point(lambda v: int(v * alpha)))
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    if shadow:
        sh, (ox, oy) = shadow_of(im)
        _paste(canvas, sh, x + ox, y + oy)
    _paste(canvas, im, x, y)

def _paste(canvas, im, x, y):
    # alpha_composite con recorte a los bordes
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(canvas.width, x + im.width), min(canvas.height, y + im.height)
    if x1 <= x0 or y1 <= y0: return
    canvas.alpha_composite(im.crop((x0 - x, y0 - y, x1 - x, y1 - y)), (x0, y0))

def atext(d, xy, txt, font, fill, anchor="la"):
    """Texto con opacidad real: se dibuja opaco en una capa y se compone con alfa."""
    a = fill[3] if len(fill) == 4 else 255
    if a <= 0: return
    img = d._image
    l, t, r, b = font.getbbox(txt, anchor=anchor)
    pad = 4
    lay = Image.new("RGBA", (int(r - l) + pad * 2, int(b - t) + pad * 2), fill[:3] + (0,))
    ImageDraw.Draw(lay).text((pad - l, pad - t), txt, font=font, fill=fill[:3] + (255,), anchor=anchor)
    if a < 255: lay.putalpha(lay.split()[3].point(lambda v: v * a // 255))
    _paste(img, lay, int(round(xy[0] + l - pad)), int(round(xy[1] + t - pad)))

def tracked(d, xy, txt, font, fill, tracking, anchor_mid=True):
    widths = [font.getlength(c) for c in txt]
    total = sum(widths) + tracking * (len(txt) - 1)
    x = xy[0] - total / 2 if anchor_mid else xy[0]
    for c, w_ in zip(txt, widths):
        atext(d, (x, xy[1]), c, font=font, fill=fill, anchor="ls"); x += w_ + tracking
    return total

def scribble(d, x0, x1, y, p, col, width=6, seed=0):
    rnd = random.Random(seed)
    n = 24; pts = []
    for k in range(n + 1):
        t = k / n
        pts.append((x0 + (x1 - x0) * t, y + math.sin(t * math.pi * 1.0) * -6 + rnd.uniform(-1.5, 1.5)))
    m = max(2, int(len(pts) * clamp(p)))
    if p > 0.02: d.line(pts[:m], fill=col, width=width, joint="curve")

def star(d, cx, cy, r, col):
    pts = []
    for k in range(8):
        ang = k * math.pi / 4 - math.pi / 2
        rr = r if k % 2 == 0 else r * 0.28
        pts.append((cx + math.cos(ang) * rr, cy + math.sin(ang) * rr))
    d.polygon(pts, fill=col)

def bezier(p0, p1, p2, n=40):
    return [((1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0], (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1])
            for t in [k / n for k in range(n + 1)]]

# ------------------------------------------------------------------ tarjeta de momento
SANS = lambda: F("Montserrat.ttf", 82, 650)
SERIF = lambda: F("EBGaramond-Italic.ttf", 112, 500)
LABEL = lambda: F("TenorSans-Regular.ttf", 30)
HAND = lambda s=72: F("Caveat.ttf", s, 650)

def moment_card(words, label, t, style):
    """Devuelve RGBA de la tarjeta con las palabras reveladas según t."""
    bg, fg, acc, lab, under = ((PAPER, VINO, VINO, GOLD_D, GOLD) if style == 0
                               else (VINO, WHITE, GOLD, GOLD, GOLD))
    sans, serif = SANS(), SERIF()
    space = sans.getlength(" ")
    items = [(w, serif if a else sans, acc if a else fg, (serif if a else sans).getlength(w), a) for w, a in words]
    lines, cur, cw = [], [], 0
    for it in items:
        add = it[3] + (space if cur else 0)
        if cur and cw + add > 820: lines.append((cur, cw)); cur, cw = [], 0; add = it[3]
        cur.append(it); cw += add
    if cur: lines.append((cur, cw))
    padx, top, lh = 60, 34, 122
    cwid = int(max(lw for _, lw in lines) + padx * 2)
    cwid = max(cwid, 520)
    chei = int(top + lh * len(lines) + 44)
    card = Image.new("RGBA", (cwid, chei), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, cwid - 1, chei - 1], radius=34, fill=bg + (255,))
    if style == 1:
        d.rounded_rectangle([10, 10, cwid - 11, chei - 11], radius=26, outline=GOLD + (150,), width=2)
    k = 0; unders = []
    for li, (its, lw) in enumerate(lines):
        x = cwid / 2 - lw / 2; y = top + lh * (li + 1) - 26
        for (w, f, col, ww, a) in its:
            p = ease_out((t - (0.28 + k * 0.12)) / 0.3)
            if p > 0:
                atext(d, (x, y + (1 - p) * 26), w, font=f, fill=col + (int(255 * p),), anchor="ls")
            if a: unders.append((x, x + ww, y + 16, 0.28 + k * 0.12 + 0.25))
            x += ww + space; k += 1
    for j, (x0, x1, y, t0) in enumerate(unders):
        scribble(d, x0 - 4, x1 + 4, y, (t - t0) / 0.35, under + (255,), 6, seed=j + len(label))
    return card

def draw_moment(canvas, words, label, t, dur, idx):
    style = idx % 2
    card = moment_card(words, label, t, style)
    s = back_out(t / 0.42) if t < 0.42 else 1.0
    out = ease_io((t - (dur - 0.22)) / 0.22)
    s *= (1 - 0.15 * out)
    rot = (-2.2 if idx % 2 == 0 else 2.0) * (1 + (1 - clamp(t / 0.42)) * 2)
    cy = 1420 + (1 - ease_out(t / 0.42)) * 60
    place(canvas, card, W / 2, cy, s, rot, 1 - out)
    # destellos dorados
    if t > 0.6 and out < 1:
        d = ImageDraw.Draw(canvas, 'RGBA')
        hw = card.width / 2
        for j, (dx, dy, r0) in enumerate([(hw - 10, -card.height / 2 - 30, 26), (hw + 30, -card.height / 2 + 20, 14), (-hw - 10, card.height / 2 + 10, 18)]):
            ph = (t - 0.6 - j * 0.15) * 4.5
            if ph < 0: continue
            r = r0 * (0.55 + 0.45 * abs(math.sin(ph))) * (1 - out)
            star(d, W / 2 + dx, cy + dy, r, GOLD + (240,))

# ------------------------------------------------------------------ notas a mano y flechas
def draw_note(canvas, spec, lt, dur):
    txt, (tx, ty), (ax, ay), curv = spec
    if lt < 0.25: return
    fade = 1 - ease_io((lt - (dur - 0.15)) / 0.15)
    pt = ease_out((lt - 0.25) / 0.35) * fade
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    f = HAND(88)
    atext(d, (tx, ty + (1 - pt) * 18), txt, font=f, fill=WHITE + (int(255 * pt),), anchor="mm")
    # flecha curva desde debajo del texto hasta el punto
    bx, by = tx, ty + 46
    mx, my = (bx + ax) / 2, (by + ay) / 2
    nx, ny = -(ay - by), (ax - bx)
    nl = math.hypot(nx, ny) or 1
    ctrl = (mx + nx / nl * curv * 260, my + ny / nl * curv * 260)
    pts = bezier((bx, by), ctrl, (ax, ay))
    pa = ease_io((lt - 0.45) / 0.45)
    m = int(len(pts) * pa)
    a8 = int(255 * fade)
    if m >= 2:
        d.line(pts[:m], fill=WHITE + (a8,), width=8, joint="curve")
    if pa > 0.92:
        (x1, y1), (x2, y2) = pts[-6], pts[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        for da in (2.55, -2.55):
            d.line([(x2, y2), (x2 + math.cos(ang + da) * 38, y2 + math.sin(ang + da) * 38)], fill=WHITE + (a8,), width=7)
    sh = Image.new("RGBA", (W, H), (30, 6, 12, 0))
    sh.putalpha(layer.split()[3].point(lambda v: int(v * 0.5)).filter(ImageFilter.GaussianBlur(6)))
    canvas.alpha_composite(sh); canvas.alpha_composite(layer)

_pol = {}
def polaroid(fid, width, caption):
    k = (fid, width)
    if k not in _pol:
        ph = Image.open(glob.glob(f"{CLIPS}/{fid}*")[0]).convert("RGB")
        pw = width - 36; phh = int(pw * 1.18)
        r = max(pw / ph.width, phh / ph.height)
        ph = ph.resize((int(ph.width * r), int(ph.height * r)), Image.LANCZOS)
        ph = ph.crop(((ph.width - pw) // 2, (ph.height - phh) // 2, (ph.width - pw) // 2 + pw, (ph.height - phh) // 2 + phh))
        card = Image.new("RGBA", (width, phh + 18 + 86), PAPER + (255,))
        card.paste(ph, (18, 18))
        d = ImageDraw.Draw(card)
        atext(d, (width / 2, phh + 18 + 46), caption, font=HAND(56), fill=VINO + (255,), anchor="mm")
        _pol[k] = card
    return _pol[k]

def draw_polaroid(canvas, spec, lt, dur):
    fid, (cx, cy), width, rot, cap = spec
    if lt < 0.15: return
    s = back_out((lt - 0.15) / 0.45, 1.6)
    out = ease_io((lt - (dur - 0.18)) / 0.18)
    x = cx + (1 - ease_out((lt - 0.15) / 0.45)) * (300 if cx > W / 2 else -300)
    place(canvas, polaroid(fid, width, cap), x, cy, s * (1 - 0.2 * out), rot + (1 - clamp((lt - 0.15) / 0.45)) * rot * 2, 1 - out)

# ------------------------------------------------------------------ apertura, cita, final
def draw_open(canvas, t, dur):
    cw, chh = 940, 430
    card = Image.new("RGBA", (cw, chh), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, cw - 1, chh - 1], radius=36, fill=VINO + (255,))
    d.rounded_rectangle([12, 12, cw - 13, chh - 13], radius=28, outline=GOLD + (160,), width=2)
    a1 = ease_out((t - 0.35) / 0.4); a2 = ease_out((t - 0.6) / 0.5); a3 = ease_out((t - 0.95) / 0.4)
    tracked(d, (cw / 2, 108 + (1 - a1) * 16), "RETIRO DE ASOCIACIÓN", F("TenorSans-Regular.ttf", 46), WHITE + (int(255 * a1),), 8)
    rw = 130 * ease_out((t - 0.5) / 0.5)
    if rw > 1:
        d.line([(cw / 2 - rw, 148), (cw / 2 + rw, 148)], fill=GOLD + (255,), width=3)
        d.ellipse([cw / 2 - 6, 142, cw / 2 + 6, 154], fill=GOLD + (255,))
    atext(d, (cw / 2, 290 + (1 - a2) * 22), "Regnum Christi", font=F("EBGaramond-Italic.ttf", 126, 500), fill=WHITE + (int(255 * a2),), anchor="ms")
    tracked(d, (cw / 2, 372 + (1 - a3) * 14), "21 . 11 . 2026", F("Montserrat.ttf", 40, 600), GOLD + (int(255 * a3),), 10)
    s = back_out(t / 0.5) if t < 0.5 else 1.0
    out = ease_io((t - (dur - 0.2)) / 0.2)
    place(canvas, card, W / 2, 470 - (1 - ease_out(t / 0.5)) * 80, s * (1 - 0.1 * out), -2.0, 1 - out)
    if t > 1.2:
        d2 = ImageDraw.Draw(canvas, 'RGBA')
        for j, (x, y, r0) in enumerate([(W / 2 + 430, 250, 30), (W / 2 + 470, 310, 15), (W / 2 - 440, 690, 20)]):
            ph = (t - 1.2 - j * 0.2) * 4
            if ph > 0: star(d2, x, y, r0 * (0.55 + 0.45 * abs(math.sin(ph))) * (1 - out), GOLD + (240,))

def draw_quote(canvas, t, dur):
    lines = ["“En la comunidad", "encontramos el espejo", "donde vemos a Cristo", "en el otro”"]
    cw, chh = 900, 640
    card = Image.new("RGBA", (cw, chh), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, cw - 1, chh - 1], radius=36, fill=PAPER + (255,))
    fq = F("EBGaramond-Italic.ttf", 70, 500)
    for i, ln in enumerate(lines):
        a = ease_out((t - (0.45 + i * 0.3)) / 0.45)
        atext(d, (cw / 2, 150 + i * 92 + (1 - a) * 20), ln, font=fq, fill=VINO + (int(255 * a),), anchor="ms")
    aa = ease_out((t - 1.8) / 0.5)
    rw = 70 * aa
    if rw > 1: d.line([(cw / 2 - rw, 500), (cw / 2 + rw, 500)], fill=GOLD + (255,), width=3)
    tracked(d, (cw / 2, 566), "SAN AGUSTÍN", F("TenorSans-Regular.ttf", 38), GOLD_D + (int(255 * aa),), 8)
    s = back_out(t / 0.5) if t < 0.5 else 1.0
    out = ease_io((t - (dur - 0.2)) / 0.2)
    place(canvas, card, W / 2, 900 + (1 - ease_out(t / 0.5)) * 70, s, 1.5, 1 - out)

_res = {}
def asset(name):
    p = f"{ASSETS}/{name}.png"
    if name not in _res: _res[name] = Image.open(p).convert("RGBA") if os.path.exists(p) else None
    return _res[name]

def end_bg(t):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H * 0.42) / H) ** 2)
    k = np.clip(d / 0.7, 0, 1)[..., None]
    c0 = np.array(VINO_L, np.float32); c1 = np.array(VINO_D, np.float32)
    img = (c0 * (1 - k) + c1 * k).astype(np.uint8)
    return Image.fromarray(img, "RGB").convert("RGBA")
_ENDBG = None

def draw_end(t, dur):
    global _ENDBG
    if _ENDBG is None: _ENDBG = end_bg(0)
    cv = _ENDBG.copy(); d = ImageDraw.Draw(cv, 'RGBA')
    # polvo dorado
    rnd = random.Random(7)
    for k in range(0):
        x0, y0, sp, r = rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(18, 60), rnd.uniform(1.5, 4.5)
        y = (y0 - t * sp) % H; a = int(120 * (0.5 + 0.5 * math.sin(t * 3 + k)))
        d.ellipse([x0 - r, y - r, x0 + r, y + r], fill=GOLD + (a,))
    esc, logo = asset("escudo"), asset("logo")
    cy_e = 760
    if esc is not None:
        im = esc.copy(); im.thumbnail((420, 420), Image.LANCZOS)
        p = (t - 0.15) / 0.6
        s = back_out(p, 1.7); rot = (1 - ease_out(p)) * -14
        # anillo dorado que se dibuja
        pr = ease_io((t - 0.3) / 0.8)
        if False:
            R = 290
            d.arc([W / 2 - R, cy_e - R, W / 2 + R, cy_e + R], -90, -90 + 360 * pr, fill=GOLD + (230,), width=4)
        place(cv, im, W / 2, cy_e, s, rot, ease_out(p), shadow=True)
        # destello que cruza el escudo
        g = (t - 1.0) / 0.6
        if False:
            band = Image.new("L", im.size, 0); bd = ImageDraw.Draw(band)
            x = -im.width * 0.5 + g * im.width * 2
            bd.polygon([(x, 0), (x + 70, 0), (x - 60, im.height), (x - 130, im.height)], fill=200)
            band = band.filter(ImageFilter.GaussianBlur(14))
            mask = Image.fromarray((np.asarray(band, np.float32) * np.asarray(im.split()[3], np.float32) / 255).astype(np.uint8))
            glint = Image.new("RGBA", im.size, (255, 246, 220, 0)); glint.putalpha(mask)
            _paste(cv, glint, int(W / 2 - im.width / 2), int(cy_e - im.height / 2))
    if logo is not None:
        im = logo.copy(); im.thumbnail((860, 300), Image.LANCZOS)
        p = ease_io((t - 1.3) / 0.8)
        if p > 0:
            crop = im.crop((0, 0, max(1, int(im.width * p)), im.height))
            _paste(cv, crop, int(W / 2 - im.width / 2), int(1180 - im.height / 2 + (1 - p) * 10))
    else:
        if True:
            a = ease_out((t - (1.3 if esc is not None else 0.3)) / 0.6)
            yb = 1200 if esc is not None else 900
            dd = ImageDraw.Draw(cv, 'RGBA')
            col = WHITE + (int(255 * a),)
            atext(dd, (W / 2, yb + (1 - a) * 20), "Regnum Christi", font=F("EBGaramond-Italic.ttf", 150, 500), fill=col, anchor="ms")
            rw = 150 * a
            if rw > 1: dd.line([(W / 2 - rw, yb + 60), (W / 2 + rw, yb + 60)], fill=GOLD + (255,), width=3)
    ha = ease_out((t - 2.0) / 0.5)
    tracked(ImageDraw.Draw(cv, 'RGBA'), (W / 2, 1460 + (1 - ha) * 16), "@rcsenoritasbqto", F("Montserrat.ttf", 48, 600), GOLD + (int(255 * ha),), 3)
    return cv

# ------------------------------------------------------------------ cortinilla entre momentos
WIPES = [starts[m[0]] for m in MOMENTS] + [starts[QUOTE], starts[END]]
def draw_wipe(canvas, t):
    for tc in WIPES:
        if abs(t - tc) < 0.2:
            p = ease_io((t - tc + 0.2) / 0.4)
            skew, bw = 520, W + 520 + 260
            x = -bw + p * (W + skew + bw)
            d = ImageDraw.Draw(canvas, 'RGBA')
            d.polygon([(x, 0), (x + bw, 0), (x + bw - skew, H), (x - skew, H)], fill=VINO + (255,))
            for e in (x, x + bw):
                d.polygon([(e - 10, 0), (e + 10, 0), (e + 10 - skew, H), (e - 10 - skew, H)], fill=GOLD + (255,))

# ------------------------------------------------------------------ composición
def compose(frame, t, i, lt):
    if i == END:
        cv = draw_end(lt, SHOTS[i][2])
        draw_wipe(cv, t); return cv.convert("RGB")
    cv = frame.convert("RGBA")
    if i == 0: draw_open(cv, lt, SHOTS[0][2])
    if i == QUOTE: draw_quote(cv, lt, SHOTS[i][2])
    if i in POLAROIDS: draw_polaroid(cv, POLAROIDS[i], lt, SHOTS[i][2])
    if i in NOTES: draw_note(cv, NOTES[i], lt, SHOTS[i][2])
    for idx, (a, b, label, words) in enumerate(MOMENTS):
        s, e = starts[a], sb(b)[1]
        if s <= t < e: draw_moment(cv, words, label, t - s, e - s, idx)
    draw_wipe(cv, t)
    return cv.convert("RGB")

def clip_path(cid): return glob.glob(f"{CLIPS}/{cid}*")[0]
VF = ("scale=1188:2112:force_original_aspect_ratio=increase:flags=lanczos,crop=1188:2112,"
      "unsharp=5:5:0.6:5:5:0.0,eq=contrast=1.05:saturation=1.08")
SW, SH = 1188, 2112   # 10 % extra para zoom/paneo

def motion(img, i, lt, dur):
    z = 1.0 + 0.09 * (1 - ease_out(lt / 0.35)) + 0.05 * (lt / dur)   # zoom de impacto + empuje
    if i == QUOTE: z = 1.0 + 0.07 * (lt / dur)
    dx = (1 if i % 2 else -1) * 30 * (lt / dur - 0.5)
    cw, ch = W / z, H / z
    cx, cy = SW / 2 + dx, SH / 2
    return img.resize((W, H), Image.BICUBIC, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2))

def shot_frames(i):
    cid, src, dur, speed = SHOTS[i]
    n = int(round(dur * FPS))
    if cid is None:
        for k in range(n): yield None
        return
    vf = VF + (f",setpts=PTS/{speed}" if speed != 1 else "") + f",fps={FPS}"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(src), "-t", str(dur * speed + 0.3), "-i", clip_path(cid),
                          "-vf", vf, "-an", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    last = None
    for k in range(n):
        buf = p.stdout.read(SW * SH * 3)
        if len(buf) == SW * SH * 3: last = Image.frombytes("RGB", (SW, SH), buf)
        yield last
    p.stdout.close(); p.wait()

def still(t):
    i = max(k for k in range(len(SHOTS)) if starts[k] <= t)
    cid, src, dur, speed = SHOTS[i]; lt = t - starts[i]
    fr = None
    if cid:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(src + lt * speed), "-i", clip_path(cid), "-frames:v", "1",
                              "-vf", VF, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
        fr = motion(Image.frombytes("RGB", (SW, SH), raw[:SW * SH * 3]), i, lt, dur)
    return compose(fr, t, i, lt)

if __name__ == "__main__":
    mode, out = sys.argv[1], sys.argv[2]
    if mode == "stills":
        os.makedirs(out, exist_ok=True)
        ts = [float(x) for x in sys.argv[3:]] if len(sys.argv) > 3 else None
        if ts is None:
            ts = [2.6] + [sb(m[1])[1] - 0.6 for m in MOMENTS] + [starts[QUOTE] + 3.6, TOTAL - 0.3] + \
                 [starts[i] + 1.2 for i in list(NOTES) + list(POLAROIDS)]
        for t in ts:
            still(t).save(f"{out}/t{t:05.2f}.jpg", quality=86); print(round(t, 2))
        print("TOTAL", TOTAL)
    else:
        small = mode == "preview"
        args = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an"]
        args += (["-vf", "scale=540:960", "-c:v", "libx264", "-preset", "veryfast", "-crf", "26"] if small else
                 ["-c:v", "libx264", "-preset", "slow", "-crf", "17", "-profile:v", "high"])
        args += ["-pix_fmt", "yuv420p", "-movflags", "+faststart", out]
        enc = subprocess.Popen(args, stdin=subprocess.PIPE)
        fi = 0
        for i in range(len(SHOTS)):
            for k, fr in enumerate(shot_frames(i)):
                lt = k / FPS; t = starts[i] + lt
                if fr is not None: fr = motion(fr, i, lt, SHOTS[i][2])
                enc.stdin.write(compose(fr, t, i, lt).tobytes()); fi += 1
            print(f"plano {i+1}/{len(SHOTS)}", flush=True)
        enc.stdin.close(); enc.wait()
        print("frames", fi, "dur", fi / FPS)
