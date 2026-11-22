#!/usr/bin/env python3
"""Historia 1080x1920 — Retiro de Asociación RC, misma línea gráfica del reel."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
from PIL import Image, ImageDraw, ImageFilter

W, H = 1080, 1920
P1, P2, OUT = sys.argv[1], sys.argv[2], sys.argv[3]

cv = R.end_bg(0)
d = ImageDraw.Draw(cv, "RGBA")

def polaroid(path, width, caption, cy_frac=0.5):
    ph = Image.open(path).convert("RGB")
    pw = width - 40; phh = int(pw * 1.0)
    r = max(pw / ph.width, phh / ph.height)
    ph = ph.resize((int(ph.width * r), int(ph.height * r)), Image.LANCZOS)
    top = int(clampi((ph.height - phh) * cy_frac, 0, ph.height - phh))
    left = (ph.width - pw) // 2
    ph = ph.crop((left, top, left + pw, top + phh))
    card = Image.new("RGBA", (width, phh + 20 + 100), R.PAPER + (255,))
    card.paste(ph, (20, 20))
    R.atext(ImageDraw.Draw(card), (width / 2, phh + 20 + 52), caption, font=R.HAND(64), fill=R.VINO + (255,), anchor="mm")
    return card

def clampi(v, a, b): return max(a, min(b, v))

# ---- encabezado
R.tracked(d, (W / 2, 300), "RETIRO DE ASOCIACIÓN", R.F("TenorSans-Regular.ttf", 40), R.GOLD + (255,), 8)
d.line([(W / 2 - 110, 330), (W / 2 + 110, 330)], fill=R.GOLD + (255,), width=3)
d.ellipse([W / 2 - 6, 324, W / 2 + 6, 336], fill=R.GOLD + (255,))
R.atext(d, (W / 2, 440), "Lo que vivimos hoy", font=R.F("EBGaramond-Italic.ttf", 118, 500), fill=R.WHITE + (255,), anchor="ms")

# ---- polaroids
p1 = polaroid(P1, 500, "¡todas juntas!", 0.66)
p2 = polaroid(P2, 500, "con nuestra Madre", 0.5)
R.place(cv, p1, 310, 800, 1.0, 5)
R.place(cv, p2, 770, 975, 1.0, -4)

# ---- tarjeta resumen
lines = [[("Un", 0), ("día", 0), ("para", 0), ("prepararnos", 0)],
         [("a", 0), ("dar", 0), ("nuestro", 0), ("sí", 1)],
         [("y", 0), ("asociarnos", 0), ("al", 0)],
         [("Regnum", 1), ("Christi", 1)]]
sans, serif = R.F("Montserrat.ttf", 54, 650), R.F("EBGaramond-Italic.ttf", 74, 500)
space = sans.getlength(" ")
lw = [sum((serif if a else sans).getlength(w) for w, a in ln) + space * (len(ln) - 1) for ln in lines]
cw, lh, top = int(max(lw) + 120), 80, 36
ch = top + lh * len(lines) + 46
card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
cd.rounded_rectangle([0, 0, cw - 1, ch - 1], radius=32, fill=R.PAPER + (255,))
for i, ln in enumerate(lines):
    x = cw / 2 - lw[i] / 2; y = top + lh * (i + 1) - 14
    for w, a in ln:
        f = serif if a else sans
        R.atext(cd, (x, y), w, font=f, fill=R.VINO + (255,), anchor="ls")
        if a: R.scribble(cd, x - 4, x + f.getlength(w.rstrip(",")) + 4, y + 14, 1.0, R.GOLD + (255,), 6, seed=i)
        x += f.getlength(w) + space
cy_card = 1475
R.place(cv, card, W / 2, cy_card, 1.0, -1.5)
for j, (dx, dy, r0) in enumerate([(-cw / 2 + 4, -ch / 2 - 24, 24), (-cw / 2 - 28, -ch / 2 + 14, 13), (cw / 2 + 6, ch / 2 + 4, 18)]):
    R.star(d, W / 2 + dx, cy_card + dy, r0, R.GOLD + (240,))

# ---- nota a mano con flecha hacia la foto de grupo
R.draw_note(cv, ("¡qué regalo!", (800, 560), (720, 700), 0.4), 2.0, 99)

# ---- firma: escudo + @
esc = R.asset("escudo").copy(); esc.thumbnail((92, 92), Image.LANCZOS)
handle = "@rcsenoritasbqto"
fh = R.F("Montserrat.ttf", 40, 600)
tw = fh.getlength(handle) + 2 * (len(handle) - 1)
gx = W / 2 - (esc.width + 22 + tw) / 2
R._paste(cv, esc, int(gx), int(1735 - esc.height / 2))
R.tracked(d, (gx + esc.width + 22, 1749), handle, fh, R.GOLD + (255,), 2, anchor_mid=False)

cv.convert("RGB").save(OUT, quality=95)
print("ok", OUT)
