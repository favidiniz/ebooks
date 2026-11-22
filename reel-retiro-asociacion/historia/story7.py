#!/usr/bin/env python3
"""Historia 1080x1920 v7 — base v4 (foto a sangre, pie vinotinto) con la línea de los posts: logo horizontal y sans regular+bold."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 1080, 1920
PHOTO, OUT, VAR = sys.argv[1], sys.argv[2], sys.argv[3]
from PIL import ImageFont
LIB = "/usr/share/fonts/truetype/liberation/"
def SF(size, bold=False): return ImageFont.truetype(LIB + ("LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"), size)
CFG = {"grupo": dict(l1="Nos preparamos", l2="para decir", veil=(0.55, 900)),
       "virgen": dict(l1="De la mano de María", l2="camino al", veil=None, shift=200, ink=R.VINO)}[VAR]
INK = CFG.get("ink", R.WHITE)            # color del texto superior
BOX_TXT = R.WHITE if INK != R.WHITE else R.VINO
M = lambda s, w: R.F("Montserrat.ttf", s, w)
X0 = 84; CW = W - 2 * X0
WHITE, VINO, VINO_D = R.WHITE, R.VINO, R.VINO_D

# ---- foto a sangre
im = Image.open(PHOTO).convert("RGB")
r = max(W / im.width, H / im.height)
im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
if CFG.get("shift"):
    sft = CFG["shift"]
    # limpiar la esquina de la lámpara: techo liso, se rellena con el tono de cada fila (tomado de la derecha)
    arr = np.asarray(im, np.float32).copy()
    CY, CX = 230, 260
    rowcol = np.median(arr[:CY + 60, 400:, :], axis=1)            # (filas, 3)
    yy, xx = np.mgrid[0:CY + 60, 0:CX + 80].astype(np.float32)
    m = np.clip((CX + 80 - xx) / 80, 0, 1) * np.clip((CY + 60 - yy) / 60, 0, 1)
    arr[:CY + 60, :CX + 80] = arr[:CY + 60, :CX + 80] * (1 - m[..., None]) + rowcol[:, None, :] * m[..., None]
    im = Image.fromarray(arr.astype(np.uint8))
    col0 = np.median(np.asarray(im, np.float32)[0:6, 400:, :], axis=(0, 1))
    top = Image.new("RGB", (W, sft + 40), tuple(int(c) for c in col0))
    canvas = Image.new("RGB", (W, H)); canvas.paste(top, (0, 0)); canvas.paste(im.crop((0, 0, W, H - sft)), (0, sft))
    # costura suave
    seam = np.linspace(0, 1, 60, dtype=np.float32)[:, None, None]
    a = np.asarray(top.crop((0, sft - 30, W, sft + 30)), np.float32); b = np.asarray(im.crop((0, 0, W, 60)), np.float32)
    canvas.paste(Image.fromarray((a * (1 - seam) + b * seam).astype(np.uint8)), (0, sft - 30))
    im = canvas
cv = im.convert("RGBA")

def grad(y0, y1, a0, a1, col):
    ys = np.arange(H, dtype=np.float32)
    t = np.clip((ys - y0) / (y1 - y0), 0, 1); t = t * t * (3 - 2 * t)
    a = (a0 + (a1 - a0) * t)[:, None].repeat(W, 1)
    arr = np.zeros((H, W, 4), np.uint8); arr[..., :3] = col; arr[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")
if CFG["veil"]: cv.alpha_composite(grad(0, CFG["veil"][1], CFG["veil"][0], 0.0, VINO_D))      # velo superior suave para el titular
cv.alpha_composite(grad(1380, 1700, 0.0, 0.96, VINO))     # pie vinotinto

layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(layer, "RGBA")

# ---- logo horizontal (como en los posts)
logo = R.asset("logo_horizontal").copy()
if INK != R.WHITE:
    tint = Image.new("RGBA", logo.size, INK + (0,)); tint.putalpha(logo.getchannel("A")); logo = tint
R._paste(layer, logo, X0 - 6, 236)

# ---- etiqueta + titular (regular + bold, como la línea de los posts)
lab_b, lab_r = SF(38, True), SF(38)
R.atext(d, (X0, 470), "RETIRO", font=lab_b, fill=INK + (255,), anchor="ls")
R.atext(d, (X0 + lab_b.getlength("RETIRO "), 470), "DE ASOCIACIÓN", font=lab_r, fill=INK + (255,), anchor="ls")
bs = 112
def fits(s_):
    return (SF(s_).getlength(CFG["l1"]) <= CW and
            SF(s_, True).getlength(CFG["l2"] + " SÍ") + 40 <= CW)
while not fits(bs): bs -= 2
reg, bold = SF(bs), SF(bs, True)
y1 = 470 + int(bs * 1.25); y2 = y1 + int(bs * 1.2)
R.atext(d, (X0, y1), CFG["l1"], font=reg, fill=INK + (255,), anchor="ls")
R.atext(d, (X0, y2), CFG["l2"], font=bold, fill=INK + (255,), anchor="ls")
xs = X0 + bold.getlength(CFG["l2"] + " ") + 14
l, t, rr, b = bold.getbbox("SÍ", anchor="ls")
pad = 16
d.rectangle([xs - pad, y2 - int(bs * 0.98) - pad, xs + rr + pad, y2 + 20], fill=INK + (255,))
R.atext(d, (xs, y2), "SÍ", font=bold, fill=BOX_TXT + (255,), anchor="ls")

# sombra suave solo para el texto superior
sh = Image.new("RGBA", (W, H), VINO_D + (0,))
sh.putalpha(layer.getchannel("A").point(lambda v: int(v * (0.35 if INK == R.WHITE else 0.0))).filter(ImageFilter.GaussianBlur(14)))
cv.alpha_composite(sh); cv.alpha_composite(layer)

# ---- pie
d2 = ImageDraw.Draw(cv, "RGBA")
fy = 1712
R.atext(d2, (X0, fy - 46), "Sábado", font=SF(40), fill=WHITE + (255,), anchor="ls")
R.atext(d2, (X0, fy), "21 de Noviembre", font=SF(44, True), fill=WHITE + (255,), anchor="ls")
R.atext(d2, (W - X0, fy - 76), "Sección de", font=SF(32), fill=WHITE + (255,), anchor="rs")
R.atext(d2, (W - X0, fy - 38), "Jóvenes Femenina", font=SF(36, True), fill=WHITE + (255,), anchor="rs")
R.atext(d2, (W - X0, fy), "@rcsenoritasbqto", font=SF(27), fill=(255, 255, 255, 210), anchor="rs")

cv.convert("RGB").save(OUT, quality=100, subsampling=0)
print("ok", OUT)
