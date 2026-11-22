#!/usr/bin/env python3
"""Historias recap — diseño desde cero.
Fotos intactas a su resolución nativa (1440x2560, ya es 9:16): sin recorte, sin reescalado, sin color.
Texto en etiquetas sólidas vinotinto (sin fundidos), logo horizontal, sans regular+bold, texto vertical fino."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PHOTO, OUT, VAR = sys.argv[1], sys.argv[2], sys.argv[3]
LIB = "/usr/share/fonts/truetype/liberation/"
def SF(size, bold=False): return ImageFont.truetype(LIB + ("LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"), int(size))

photo = Image.open(PHOTO).convert("RGB")
W, H = photo.size
assert (W, H) == (1440, 2560), photo.size
k = W / 1080                                  # escala respecto a 1080
WHITE, VINO = (255, 255, 255), R.VINO

CFG = {
    "grupo":  dict(tags=[("Así vivimos", False), ("nuestro Retiro", True), ("de Asociación", True)],
                   n="01", top_ink=WHITE, side_ink=WHITE, tag_y=1440),
    "virgen": dict(tags=[("De la mano de María,", False), ("preparando", True), ("nuestro sí", True)],
                   n="02", top_ink=VINO, side_ink=VINO, tag_y=1470),
}[VAR]

cv = photo.convert("RGBA")
L = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L, "RGBA")
X0 = int(72 * k)

# ---- logo horizontal (tamaño nativo del archivo, sin ampliar)
logo = R.asset("logo_horizontal").copy()
if CFG["top_ink"] != WHITE:
    t = Image.new("RGBA", logo.size, CFG["top_ink"] + (0,)); t.putalpha(logo.getchannel("A")); logo = t
R._paste(L, logo, (W - logo.width) // 2, int(226 * k))

# ---- etiquetas apiladas (titular)
fs = 66 * k
padx, pady, gap = int(26 * k), int(18 * k), int(10 * k)
y = int(CFG["tag_y"] * k)
for txt, bold in CFG["tags"]:
    f = SF(fs, bold)
    l, t_, r, b = f.getbbox(txt, anchor="ls")
    asc = int(fs * 0.74); desc = int(fs * 0.22)
    box = [X0, y, X0 + int(r) + 2 * padx, y + asc + desc + 2 * pady]
    d.rectangle(box, fill=VINO + (255,))
    R.atext(d, (X0 + padx, y + pady + asc), txt, font=f, fill=WHITE + (255,), anchor="ls")
    y = box[3] + gap

# ---- sello: fecha + @ en etiqueta blanca
sf = SF(30 * k, True)
stamp = "21.11.2026  ·  @rcsenoritasbqto"
sw = sf.getlength(stamp)
y += int(8 * k)
d.rectangle([X0, y, X0 + sw + 2 * int(20 * k), y + int(58 * k)], fill=WHITE + (255,))
R.atext(d, (X0 + int(20 * k), y + int(40 * k)), stamp, font=sf, fill=VINO + (255,), anchor="ls")

# ---- pestaña vertical vinotinto pegada al borde derecho
vt = f"{CFG['n']} / 02    —    RETIRO DE ASOCIACIÓN    —    SECCIÓN DE JÓVENES FEMENINA"
vf = SF(22 * k, True)
trk = 5 * k
tw = int(sum(vf.getlength(c) for c in vt) + trk * (len(vt) - 1))
th = int(64 * k); padv = int(40 * k)
strip = Image.new("RGBA", (tw + 2 * padv, th), VINO + (255,))
R.tracked(ImageDraw.Draw(strip, "RGBA"), (padv, int(th / 2 + 8 * k)), vt, vf, WHITE + (255,), trk, anchor_mid=False)
strip = strip.rotate(90, expand=True)
R._paste(L, strip, W - strip.width, int(430 * k))

# sombra muy leve solo para lo blanco que cae sobre la foto (no toca la foto)
sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
a = L.getchannel("A")
sh.putalpha(a.point(lambda v: int(v * 0.22)).filter(ImageFilter.GaussianBlur(6 * k)))
cv.alpha_composite(sh, (0, int(3 * k)))
cv.alpha_composite(L)
cv.convert("RGB").save(OUT, quality=100, subsampling=0)
print("ok", OUT, cv.size)
