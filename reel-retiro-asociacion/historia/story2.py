#!/usr/bin/env python3
"""Historia 1080x1920 v2 — estilo statement: Montserrat protagonista + Caveat a mano."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
from PIL import Image, ImageDraw

W, H = 1080, 1920
P1, P2, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
M = lambda s, w: R.F("Montserrat.ttf", s, w)
X0 = 84  # margen izquierdo

cv = R.end_bg(0)
d = ImageDraw.Draw(cv, "RGBA")

# ---- cabecera: escudo + REGNUM CHRISTI (como en el feed)
esc = R.asset("escudo").copy(); esc.thumbnail((96, 96), Image.LANCZOS)
wm = R.asset("logo").copy(); wm.thumbnail((400, 78), Image.LANCZOS)   # letras originales del logo
R._paste(cv, esc, X0, 226)
R._paste(cv, wm, X0 + esc.width + 22, int(226 + esc.height / 2 - wm.height / 2))

# ---- statement
bs = 112
while M(bs, 900).getlength("NOS PREPARAMOS") > W - 2 * X0: bs -= 2
big = M(bs, 900)
R.atext(d, (X0, 470), "NOS PREPARAMOS", font=big, fill=R.WHITE + (255,), anchor="ls")
R.atext(d, (X0, 590), "PARA DECIR", font=big, fill=R.WHITE + (255,), anchor="ls")
huge = M(300, 900)
R.atext(d, (X0 - 6, 885), "SÍ", font=huge, fill=R.GOLD + (255,), anchor="ls")
sw = huge.getlength("SÍ")
R.scribble(d, X0, X0 + sw, 925, 1.0, R.WHITE + (255,), 9, seed=3)
# nota a mano junto al SÍ
xn = X0 + sw + 40
R.atext(d, (xn, 760), "retiro de", font=R.HAND(84), fill=R.WHITE + (255,), anchor="ls")
R.atext(d, (xn, 840), "asociación", font=R.HAND(84), fill=R.WHITE + (255,), anchor="ls")
R.atext(d, (xn, 910), "21.11.2026", font=R.HAND(60), fill=R.GOLD + (255,), anchor="ls")

# ---- polaroids
def polaroid(path, width, caption, cy_frac=0.5):
    ph = Image.open(path).convert("RGB")
    pw = width - 36; phh = pw
    r = max(pw / ph.width, phh / ph.height)
    ph = ph.resize((int(ph.width * r), int(ph.height * r)), Image.LANCZOS)
    top = int(max(0, min(ph.height - phh, (ph.height - phh) * cy_frac)))
    left = (ph.width - pw) // 2
    ph = ph.crop((left, top, left + pw, top + phh))
    card = Image.new("RGBA", (width, phh + 18 + 92), R.PAPER + (255,))
    card.paste(ph, (18, 18))
    R.atext(ImageDraw.Draw(card), (width / 2, phh + 18 + 48), caption, font=R.HAND(60), fill=R.VINO + (255,), anchor="mm")
    return card

R.place(cv, polaroid(P1, 480, "¡todas juntas!", 0.66), 330, 1230, 1.0, 5)
R.place(cv, polaroid(P2, 480, "con nuestra Madre", 0.5), 760, 1330, 1.0, -4)
for (x, y, r) in [(980, 1040, 26), (1012, 1092, 13), (96, 1500, 18)]:
    R.star(d, x, y, r, R.GOLD + (240,))

# ---- firma abajo a la derecha (como en el feed)
xr = W - X0
R.atext(d, (xr, 1700), "Sección de", font=M(34, 500), fill=R.WHITE + (255,), anchor="rs")
R.atext(d, (xr, 1748), "Jóvenes Femenina", font=M(40, 700), fill=R.WHITE + (255,), anchor="rs")
R.atext(d, (xr, 1786), "@rcsenoritasbqto", font=M(26, 500), fill=R.GOLD + (255,), anchor="rs")

cv.convert("RGB").save(OUT, quality=95)
print("ok", OUT)
