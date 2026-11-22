#!/usr/bin/env python3
"""Historia recap 1080x1920 — la foto manda; texto breve en pasado tipo pie de foto.
Línea gráfica de los posts: logo horizontal + sans regular/bold, vinotinto y blanco."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
PHOTO, OUT, VAR = sys.argv[1], sys.argv[2], sys.argv[3]
LIB = "/usr/share/fonts/truetype/liberation/"
def SF(size, bold=False): return ImageFont.truetype(LIB + ("LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"), size)
WHITE, VINO = R.WHITE, R.VINO
CFG = {
    "grupo":  dict(l1="Así vivimos nuestro", l2="Retiro de Asociación", logo=WHITE, ink=WHITE, n="01", x=262),
    "virgen": dict(l1="De la mano de María,", l2="preparando nuestro sí", logo=VINO, ink=VINO, n="02", x=72),
}[VAR]
X0 = CFG["x"]

# ---- foto a sangre, sin retoques
im = Image.open(PHOTO).convert("RGB")
r = max(W / im.width, H / im.height)
im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
cv = im.convert("RGBA")

# ---- logo discreto arriba
logo = R.asset("logo_horizontal").copy(); logo.thumbnail((300, 80), Image.LANCZOS)
if CFG["logo"] != WHITE:
    tint = Image.new("RGBA", logo.size, CFG["logo"] + (0,)); tint.putalpha(logo.getchannel("A")); logo = tint
R._paste(cv, logo, X0 - 4, 232)

# ---- pie de foto arriba, en la zona limpia de la foto (cielo / techo)
L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L, "RGBA")
INK = CFG["ink"]; SOFTA = 210
d.rectangle([X0, 352, X0 + 64, 358], fill=INK + (255,))                    # filete corto
R.atext(d, (W - X0, 362), CFG["n"] + " / 02", font=SF(28, True), fill=INK + (SOFTA,), anchor="rs")
R.atext(d, (X0, 440), CFG["l1"], font=SF(58), fill=INK + (255,), anchor="ls")
R.atext(d, (X0, 510), CFG["l2"], font=SF(62, True), fill=INK + (255,), anchor="ls")
R.atext(d, (X0, 566), "21.11.2026  ·  @rcsenoritasbqto", font=SF(30), fill=INK + (SOFTA,), anchor="ls")
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sh.putalpha(L.getchannel("A").point(lambda v: int(v * (0.4 if INK == WHITE else 0))).filter(ImageFilter.GaussianBlur(6)))
cv.alpha_composite(sh, (0, 2)); cv.alpha_composite(L)
cv.convert("RGB").save(OUT, quality=100, subsampling=0)
print("ok", OUT)
