#!/usr/bin/env python3
"""Historia 1080x1920 v4 — foto a sangre, titular sobre el cielo, pie vinotinto. Solo Montserrat + logo oficial."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 1080, 1920
PHOTO, OUT = sys.argv[1], sys.argv[2]
M = lambda s, w: R.F("Montserrat.ttf", s, w)
X0 = 84; CW = W - 2 * X0
WHITE, VINO, VINO_D = R.WHITE, R.VINO, R.VINO_D

# ---- foto a sangre
im = Image.open(PHOTO).convert("RGB")
r = max(W / im.width, H / im.height)
im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
cv = im.convert("RGBA")

def grad(y0, y1, a0, a1, col):
    ys = np.arange(H, dtype=np.float32)
    t = np.clip((ys - y0) / (y1 - y0), 0, 1); t = t * t * (3 - 2 * t)
    a = (a0 + (a1 - a0) * t)[:, None].repeat(W, 1)
    arr = np.zeros((H, W, 4), np.uint8); arr[..., :3] = col; arr[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")
cv.alpha_composite(grad(0, 900, 0.55, 0.0, VINO_D))      # velo superior suave para el titular
cv.alpha_composite(grad(1380, 1700, 0.0, 0.96, VINO))     # pie vinotinto

layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(layer, "RGBA")

# ---- logo oficial completo, tal cual
logo = R.asset("logo_completo").copy()
logo = logo.crop(logo.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())
logo.thumbnail((400, 176), Image.LANCZOS)
R._paste(layer, logo, X0, 220)

# ---- titular
bs = 120
while M(bs, 900).getlength("NOS PREPARAMOS") > CW: bs -= 2
big = M(bs, 900)
y1 = 540; y2 = y1 + int(bs * 1.28)
R.atext(d, (X0, y1), "NOS PREPARAMOS", font=big, fill=WHITE + (255,), anchor="ls")
R.atext(d, (X0, y2), "PARA DECIR", font=big, fill=WHITE + (255,), anchor="ls")
xs = X0 + big.getlength("PARA DECIR ") + 6
l, t, rr, b = big.getbbox("SÍ", anchor="ls")
pad = 18
d.rectangle([xs - pad, y2 - int(bs * 1.0) - pad, xs + rr + pad, y2 + 22], fill=WHITE + (255,))
R.atext(d, (xs, y2), "SÍ", font=big, fill=VINO + (255,), anchor="ls")

# sombra suave solo para el texto superior
sh = Image.new("RGBA", (W, H), VINO_D + (0,))
sh.putalpha(layer.getchannel("A").point(lambda v: int(v * 0.35)).filter(ImageFilter.GaussianBlur(14)))
cv.alpha_composite(sh); cv.alpha_composite(layer)

# ---- pie
d2 = ImageDraw.Draw(cv, "RGBA")
fy = 1712
R.tracked(d2, (X0, fy - 70), "RETIRO DE ASOCIACIÓN", M(34, 800), WHITE + (255,), 4, anchor_mid=False)
R.atext(d2, (X0, fy), "21 · 11 · 2026", font=M(30, 500), fill=(255, 255, 255, 190), anchor="ls")
R.atext(d2, (W - X0, fy - 70), "Sección de", font=M(28, 500), fill=WHITE + (255,), anchor="rs")
R.atext(d2, (W - X0, fy - 34), "Jóvenes Femenina", font=M(34, 700), fill=WHITE + (255,), anchor="rs")
R.atext(d2, (W - X0, fy), "@rcsenoritasbqto", font=M(26, 500), fill=(255, 255, 255, 190), anchor="rs")

cv.convert("RGB").save(OUT, quality=95)
print("ok", OUT)
