#!/usr/bin/env python3
"""Historia 1080x1920 v3 — solo Montserrat + logo; vinotinto y blanco; retícula limpia."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
from PIL import Image, ImageDraw

W, H = 1080, 1920
P1, P2, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
M = lambda s, w: R.F("Montserrat.ttf", s, w)
X0 = 84; CW = W - 2 * X0
WHITE, VINO = R.WHITE, R.VINO
SOFT = (255, 255, 255, 170)

cv = R.end_bg(0)
d = ImageDraw.Draw(cv, "RGBA")

# ---- cabecera: escudo + letras originales del logo
# logo oficial completo, tal cual (sin separar ni recomponer)
logo = R.asset("logo_completo").copy()
logo = logo.crop(logo.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())
logo.thumbnail((400, 170), Image.LANCZOS)
R._paste(cv, logo, X0, 236)

# ---- titular
bs = 120
while M(bs, 900).getlength("NOS PREPARAMOS") > CW: bs -= 2
big = M(bs, 900)
y1 = 560
R.atext(d, (X0, y1), "NOS PREPARAMOS", font=big, fill=WHITE + (255,), anchor="ls")
y2 = y1 + int(bs * 1.28)
R.atext(d, (X0, y2), "PARA DECIR", font=big, fill=WHITE + (255,), anchor="ls")
# "SÍ" resaltado en recuadro blanco, como los titulares del feed
xs = X0 + big.getlength("PARA DECIR ") + 6
l, t, r, b = big.getbbox("SÍ", anchor="ls")
pad = 18
d.rectangle([xs - pad, y2 - int(bs * 1.0) - pad, xs + r + pad, y2 + 22], fill=WHITE + (255,))
R.atext(d, (xs, y2), "SÍ", font=big, fill=VINO + (255,), anchor="ls")
# bajada
R.tracked(d, (X0, y2 + 92), "RETIRO DE ASOCIACIÓN  ·  21.11.2026", M(32, 600), SOFT, 4, anchor_mid=False)

# ---- dos fotos alineadas a la retícula
gap = 24
pw = (CW - gap) // 2; ph = int(pw * 1.62)
py = y2 + 150
def photo(path, cy_frac):
    im = Image.open(path).convert("RGB")
    r = max(pw / im.width, ph / im.height)
    im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    top = int(max(0, min(im.height - ph, (im.height - ph) * cy_frac)))
    left = (im.width - pw) // 2
    im = im.crop((left, top, left + pw, top + ph)).convert("RGBA")
    mask = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, pw - 1, ph - 1], radius=28, fill=255)
    im.putalpha(mask)
    return im
for k, (path, fr) in enumerate([(P1, 0.62), (P2, 0.5)]):
    im = photo(path, fr)
    x = X0 + k * (pw + gap)
    sh, (ox, oy) = R.shadow_of(im, blur=20, alpha=0.35, off=(0, 16))
    R._paste(cv, sh, x + ox, py + oy)
    R._paste(cv, im, x, py)

# ---- firma
fy = py + ph + 110
d.line([(X0, fy - 54), (W - X0, fy - 54)], fill=(255, 255, 255, 70), width=2)
R.atext(d, (X0, fy), "Sección de Jóvenes Femenina", font=M(34, 700), fill=WHITE + (255,), anchor="ls")
R.atext(d, (W - X0, fy), "@rcsenoritasbqto", font=M(30, 500), fill=SOFT, anchor="rs")

cv.convert("RGB").save(OUT, quality=95)
print("ok", OUT, "fy", fy)
