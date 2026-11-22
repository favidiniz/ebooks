#!/usr/bin/env python3
"""Historia 1080x1920 v5 — calcada del estilo de los posts de @rcsenoritasbqto:
logo horizontal arriba-izq, escudo marca de agua, títulos centrados regular+bold (sans tipo Helvetica),
imagen fundida con el rojo, datos abajo-izq y firma abajo-der."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render2 as R
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
PHOTO, OUT = sys.argv[1], sys.argv[2]
LIB = "/usr/share/fonts/truetype/liberation/"
def S(size, bold=False): return ImageFont.truetype(LIB + ("LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"), size)
X0 = 60
RED = np.array([118, 36, 31], np.float32)      # rojo de los posts
GLOW = np.array([176, 70, 48], np.float32)
WHITE = (255, 255, 255)

# ---- fondo rojo con resplandor cálido al centro
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
dd = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - 1080) / (H * 0.42)) ** 2)
k = np.clip(1 - dd, 0, 1)[..., None] ** 1.6
cv = Image.fromarray((RED * (1 - k) + GLOW * k).astype(np.uint8), "RGB").convert("RGBA")

# ---- escudo grande como marca de agua (arriba a la derecha, como en el post)
esc = R.asset("escudo").copy()
esc = esc.resize((1250, int(esc.height * 1250 / esc.width)), Image.LANCZOS)
esc.putalpha(esc.getchannel("A").point(lambda v: int(v * 0.07)))
R._paste(cv, esc, 290, -170)

# ---- foto fundida con el fondo
ph = Image.open(PHOTO).convert("RGB")
crop = ph.crop((0, int(ph.height * 0.40), ph.width, int(ph.height * 0.93)))
crop = crop.resize((W, int(crop.height * W / crop.width)), Image.LANCZOS)
pY = 720
mask = np.ones((crop.height, W), np.float32)
ys = np.arange(crop.height, dtype=np.float32)
top_f, bot_f = 230, 380
mask *= np.clip(ys / top_f, 0, 1)[:, None] ** 1.3
mask *= np.clip((crop.height - ys) / bot_f, 0, 1)[:, None] ** 1.2
xs = np.arange(W, dtype=np.float32)
side = np.clip(np.minimum(xs, W - xs) / 90, 0, 1)[None, :]
mask *= 0.55 + 0.45 * side
pc = crop.convert("RGBA"); pc.putalpha(Image.fromarray((mask * 255).astype(np.uint8)))
R._paste(cv, pc, 0, pY)

# ---- capa de texto (con sombra suave como en el post)
L = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(L, "RGBA")
logo = R.asset("logo_horizontal")
R._paste(L, logo, X0 - 6, 236)

def mixed(y, parts, size):
    """Línea centrada con tramos regular/bold."""
    fonts = [S(size, b) for _, b in parts]
    widths = [f.getlength(t) for (t, _), f in zip(parts, fonts)]
    x = W / 2 - sum(widths) / 2
    for (t, _), f, w_ in zip(parts, fonts, widths):
        R.atext(d, (x, y), t, font=f, fill=WHITE + (255,), anchor="ls"); x += w_

mixed(470, [("RETIRO", True), (" DE ASOCIACIÓN", False)], 40)
mixed(575, [("Nos preparamos para", False)], 80)
mixed(668, [("decir nuestro ", True), ("SÍ", True)], 84)

# abajo izquierda: fecha
R.atext(d, (X0, 1630), "Sábado", font=S(48), fill=WHITE + (255,), anchor="ls")
R.atext(d, (X0, 1686), "21 de Noviembre", font=S(50, True), fill=WHITE + (255,), anchor="ls")
# abajo derecha: firma
xr = W - X0
R.atext(d, (xr, 1612), "Sección de", font=S(36), fill=WHITE + (255,), anchor="rs")
R.atext(d, (xr, 1650), "Jóvenes Femenina", font=S(38, True), fill=WHITE + (255,), anchor="rs")
R.atext(d, (xr, 1686), "@rcsenoritasbqto", font=S(27), fill=WHITE + (255,), anchor="rs")

sh = Image.new("RGBA", (W, H), (40, 8, 6, 0))
sh.putalpha(L.getchannel("A").point(lambda v: int(v * 0.45)).filter(ImageFilter.GaussianBlur(8)))
cv.alpha_composite(sh, (0, 3)); cv.alpha_composite(L)
cv.convert("RGB").save(OUT, quality=95)
print("ok", OUT)
