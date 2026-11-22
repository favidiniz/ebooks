#!/usr/bin/env python3
"""Reel Retiro de Asociación RC — render 1080x1920 @30fps, sin audio.
Uso:  render.py stills OUTDIR      -> fotogramas clave para storyboard
      render.py video OUT.mp4      -> exporta el reel completo
"""
import sys, os, glob, subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__)) + "/.."
CLIPS = BASE + "/dl/clips"
FONTS = BASE + "/fonts"
ESCUDO = BASE + "/assets/escudo.png"   # si existe se usa; si no, marcador
W, H, FPS = 1080, 1920, 30

# Paleta Regnum Christi
VINO = (110, 22, 38)
VINO_D = (72, 12, 24)
WHITE = (255, 255, 255)
GOLD = (222, 186, 110)

def F(name, size, wght=None):
    f = ImageFont.truetype(f"{FONTS}/{name}", size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f

# ---------------------------------------------------------------- EDL
# (clip, inicio en origen, duración en salida, velocidad)
SHOTS = [
    ("dd5b9a05", 0.6, 3.6, 1.0),   # apertura: foto de grupo
    ("3c461547", 2.0, 2.0, 1.0),   # 1 Reconozco mi sed
    ("f33d8239", 2.4, 2.0, 1.0),
    ("7f233f9c", 0.4, 2.0, 1.0),
    ("c76ca9ef", 4.6, 1.9, 1.0),   # 2 Dejo que Él me encuentre
    ("06e849d0", 0.0, 1.4, 1.0),
    ("aaceadd2", 0.6, 2.5, 1.0),
    ("11a86873", 0.5, 1.8, 1.0),   # 3 Soy amada, soy hija
    ("4b9f4e5d", 1.5, 2.2, 1.0),
    ("6c0fab77", 0.6, 1.8, 1.0),
    ("0a166d44", 1.4, 1.8, 1.0),   # 4 Le dejo hablar a mi corazón
    ("16a80705", 0.0, 1.7, 1.0),
    ("6f447e5e", 0.3, 2.2, 1.0),
    ("8838e0f4", 2.6, 2.0, 1.0),   # 5 Comprendo mi vocación
    ("994afafb", 1.6, 2.0, 1.0),
    ("74ae2ba7", 1.0, 2.0, 1.0),
    ("ebac2810", 0.5, 2.0, 1.0),   # 6 Soy apóstol del agua viva
    ("8ca61869", 1.6, 2.0, 1.0),
    ("b6c4ebad", 0.5, 2.0, 1.0),
    ("1676024b", 0.5, 2.0, 1.0),   # 7 Reconozco el don
    ("699af540", 1.0, 2.0, 1.0),
    ("1413d3cc", 2.0, 2.0, 1.0),
    ("79df9735", 3.6, 1.8, 1.0),   # 8 Soy enviada
    ("7f1ee76f", 5.0, 1.9, 1.0),
    ("fb2ef70c", 6.0, 1.9, 1.0),
    ("c795e18c", 11.8, 6.4, 0.625), # cierre: cielo + estatua (cámara lenta)
]
starts, acc = [], 0.0
for s in SHOTS:
    starts.append(acc); acc += s[2]
TOTAL = acc

def shot_bounds(i): return starts[i], starts[i] + SHOTS[i][2]

# Momentos: (primer plano, último plano, número, [(palabra, acento)])
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

# ---------------------------------------------------------------- easing
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def ease_io(x): x = clamp(x); return x * x * (3 - 2 * x)

# ---------------------------------------------------------------- capas
def vgrad(top_a, bot_a, y0, y1, color):
    a = np.zeros((H, W), np.float32)
    ys = np.arange(H, dtype=np.float32)
    t = np.clip((ys - y0) / max(1, (y1 - y0)), 0, 1)
    a[:] = (top_a + (bot_a - top_a) * (t * t * (3 - 2 * t)))[:, None]
    img = np.zeros((H, W, 4), np.uint8)
    img[..., :3] = color
    img[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(img, "RGBA")

GRAD_LOW = vgrad(0.0, 0.88, 900, 1700, VINO_D)       # legibilidad textos
GRAD_TOP = vgrad(0.28, 0.0, 0, 380, VINO_D)           # cierre superior suave
def vignette():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((xx - W/2) / (W*0.75))**2 + ((yy - H/2) / (H*0.75))**2)
    a = np.clip((d - 0.55) / 0.6, 0, 1) * 0.45
    img = np.zeros((H, W, 4), np.uint8); img[..., :3] = VINO_D
    img[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(img, "RGBA")
VIGN = vignette()

def text_rgba(draw_fn):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_fn(layer)
    return layer

def put_text(layer, xy, txt, font, fill, alpha, tracking=0, anchor="ls"):
    if alpha <= 0: return
    a = int(255 * clamp(alpha))
    d = ImageDraw.Draw(layer)
    if tracking == 0:
        d.text(xy, txt, font=font, fill=fill + (a,), anchor=anchor)
        return
    # tracking manual (centrado)
    widths = [font.getlength(c) for c in txt]
    total = sum(widths) + tracking * (len(txt) - 1)
    x = xy[0] - total / 2 if anchor[0] == "m" else xy[0]
    for c, w_ in zip(txt, widths):
        d.text((x, xy[1]), c, font=font, fill=fill + (a,), anchor="l" + anchor[1])
        x += w_ + tracking

def shadowed(layer_fn):
    """Dibuja texto con sombra suave vinotinto para legibilidad."""
    from PIL import ImageFilter
    txt = text_rgba(layer_fn)
    sh = Image.new("RGBA", (W, H), VINO_D + (0,))
    sh.putalpha(txt.split()[3].point(lambda v: int(v * 0.55)))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out.alpha_composite(sh); out.alpha_composite(txt)
    return out

# ---- animación de palabras (estilo kit: aparición palabra a palabra con subida)
SANS = F("Montserrat.ttf", 88, 600)
SERIF_I = F("EBGaramond-Italic.ttf", 128, 500)
LABEL = F("TenorSans-Regular.ttf", 40)
MAXW = 900

def layout_words(words):
    items = []
    for w, acc in words:
        f = SERIF_I if acc else SANS
        items.append((w, f, GOLD if acc else WHITE, f.getlength(w)))
    space = SANS.getlength(" ")
    lines, cur, cw = [], [], 0
    for it in items:
        add = it[3] + (space if cur else 0)
        if cur and cw + add > MAXW:
            lines.append((cur, cw)); cur, cw = [], 0; add = it[3]
        cur.append(it); cw += add
    if cur: lines.append((cur, cw))
    return lines, space

def draw_moment(layer, words, label, t, dur):
    lines, space = layout_words(words)
    line_h = 124
    base_y = 1440 - (len(lines) - 1) * line_h / 2
    out_a = 1 - ease_io((t - (dur - 0.28)) / 0.28)
    # etiqueta + filete dorado
    la = ease_out(t / 0.35) * out_a
    rule_w = 90 * ease_out((t - 0.05) / 0.45)
    ly = base_y - 130
    d = ImageDraw.Draw(layer)
    if rule_w > 1:
        d.line([(W/2 - rule_w, ly - 12), (W/2 + rule_w, ly - 12)], fill=GOLD + (int(255*la),), width=2)
    put_text(layer, (W/2, ly + 34), f"{label}  ·  08", LABEL, GOLD, la, tracking=6, anchor="ms")
    k = 0
    for li, (items, lw) in enumerate(lines):
        x = W/2 - lw/2
        y = base_y + li * line_h
        for (w, f, col, ww) in items:
            t0 = 0.18 + k * 0.13
            p = ease_out((t - t0) / 0.38)
            if p > 0:
                dy = (1 - p) * 34
                put_text(layer, (x, y + dy), w, f, col, p * out_a, anchor="ls")
            x += ww + space; k += 1

def draw_open(layer, t, dur):
    out_a = 1 - ease_io((t - (dur - 0.3)) / 0.3)
    f1 = F("TenorSans-Regular.ttf", 50)
    f2 = F("EBGaramond-Italic.ttf", 150, 500)
    f3 = F("Montserrat.ttf", 44, 500)
    a1 = ease_out((t - 0.15) / 0.5) * out_a
    a2 = ease_out((t - 0.55) / 0.6) * out_a
    a3 = ease_out((t - 1.05) / 0.5) * out_a
    y0 = 1250
    put_text(layer, (W/2, y0 + (1-a1)*24), "RETIRO DE ASOCIACIÓN", f1, WHITE, a1, tracking=9, anchor="ms")
    rw = 150 * ease_out((t - 0.35) / 0.7)
    d = ImageDraw.Draw(layer)
    if rw > 1:
        d.line([(W/2 - rw, y0 + 42), (W/2 + rw, y0 + 42)], fill=GOLD + (int(255*out_a),), width=3)
        d.ellipse([W/2-6, y0+36, W/2+6, y0+48], fill=GOLD + (int(255*out_a),))
    put_text(layer, (W/2, y0 + 200 + (1-a2)*30), "Regnum Christi", f2, WHITE, a2, anchor="ms")
    put_text(layer, (W/2, y0 + 300 + (1-a3)*20), "21 . 11 . 2026", f3, GOLD, a3, tracking=10, anchor="ms")

_escudo = None
def escudo_img(size):
    global _escudo
    if os.path.exists(ESCUDO):
        if _escudo is None: _escudo = Image.open(ESCUDO).convert("RGBA")
        im = _escudo.copy(); im.thumbnail((size, size), Image.LANCZOS); return im
    # marcador de posición: contorno de escudo dorado
    im = Image.new("RGBA", (size, size), (0,0,0,0)); d = ImageDraw.Draw(im)
    s = size
    pts = [(s*0.12,s*0.08),(s*0.88,s*0.08),(s*0.88,s*0.5),(s*0.5,s*0.95),(s*0.12,s*0.5)]
    d.line(pts + [pts[0]], fill=GOLD + (255,), width=4, joint="curve")
    d.text((s/2, s*0.45), "ESCUDO", font=F("Montserrat.ttf", int(s*0.13), 600), fill=GOLD+(255,), anchor="mm")
    return im

def draw_close(layer, t, dur):
    f_q = F("EBGaramond-Italic.ttf", 72, 450)
    f_a = F("TenorSans-Regular.ttf", 40)
    f_h = F("Montserrat.ttf", 42, 600)
    quote = ["“En la comunidad", "encontramos el espejo", "donde vemos a Cristo", "en el otro”"]
    y0 = 560
    for i, ln in enumerate(quote):
        a = ease_out((t - (0.45 + i * 0.32)) / 0.6)
        put_text(layer, (W/2, y0 + i * 96 + (1-a)*26), ln, f_q, WHITE, a, anchor="ms")
    aa = ease_out((t - 1.9) / 0.6)
    d = ImageDraw.Draw(layer)
    yq = y0 + len(quote) * 96 + 30
    rw = 70 * aa
    if rw > 1: d.line([(W/2 - rw, yq), (W/2 + rw, yq)], fill=GOLD + (int(255*aa),), width=2)
    put_text(layer, (W/2, yq + 70), "SAN AGUSTÍN", f_a, GOLD, aa, tracking=8, anchor="ms")
    ea = ease_out((t - 2.6) / 0.7)
    if ea > 0 and os.path.exists(ESCUDO):
        em = escudo_img(260)
        em.putalpha(em.split()[3].point(lambda v: int(v * ea)))
        layer.alpha_composite(em, (int(W/2 - em.width/2), int(1210 + (1-ea)*20)))
    ha = ease_out((t - 3.1) / 0.6)
    put_text(layer, (W/2, 1560 if os.path.exists(ESCUDO) else 1300), "@rcsenoritasbqto", f_h, WHITE, ha, tracking=2, anchor="ms")

# ---------------------------------------------------------------- composición
def compose(frame_rgb, t):
    """frame_rgb: PIL RGB 1080x1920; t: tiempo global"""
    img = frame_rgb.convert("RGBA")
    img.alpha_composite(VIGN)
    # qué segmento
    if t < shot_bounds(0)[1]:
        img.alpha_composite(GRAD_LOW); img.alpha_composite(GRAD_TOP)
        s, e = shot_bounds(0)
        img.alpha_composite(shadowed(lambda L: draw_open(L, t - s, e - s)))
        return img.convert("RGB")
    last = len(SHOTS) - 1
    if t >= starts[last]:
        s, e = shot_bounds(last)
        lt = t - s
        k = ease_io(lt / 0.7) * 0.78
        ov = Image.new("RGBA", (W, H), VINO_D + (int(255 * k),))
        img.alpha_composite(ov)
        img.alpha_composite(shadowed(lambda L: draw_close(L, lt, e - s)))
        return img.convert("RGB")
    for a, b, label, words in MOMENTS:
        s = starts[a]; e = shot_bounds(b)[1]
        if s <= t < e:
            img.alpha_composite(GRAD_LOW)
            img.alpha_composite(shadowed(lambda L: draw_moment(L, words, label, t - s, e - s)))
            break
    return img.convert("RGB")

def clip_path(cid): return glob.glob(f"{CLIPS}/{cid}*")[0]

VF = ("scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,"
      "unsharp=5:5:0.6:5:5:0.0,eq=contrast=1.04:saturation=1.06,"
      "colorbalance=rs=0.02:gs=0.0:bs=-0.03:rh=0.02:bh=-0.02")

def zoom(img, lt, dur, amount):
    z = 1 + amount * (lt / dur)
    cw, ch = W / z, H / z
    return img.resize((W, H), Image.BICUBIC, box=((W-cw)/2, (H-ch)/2, (W+cw)/2, (H+ch)/2))

def shot_frames(i):
    cid, src, dur, speed = SHOTS[i]
    n = int(round(dur * FPS))
    srcdur = dur * speed + 0.2
    vf = VF + (f",setpts=PTS/{speed}" if speed != 1 else "") + f",fps={FPS}"
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(src), "-t", str(srcdur / 1),
                          "-i", clip_path(cid), "-vf", vf, "-an", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         stdout=subprocess.PIPE)
    last = None
    for k in range(n):
        buf = p.stdout.read(W * H * 3)
        if len(buf) == W * H * 3:
            last = Image.frombytes("RGB", (W, H), buf)
        yield last
    p.stdout.close(); p.wait()

def still(t):
    for i in range(len(SHOTS)):
        s, e = shot_bounds(i)
        if s <= t < e: break
    cid, src, dur, speed = SHOTS[i]
    ts = src + (t - s) * speed
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ts), "-i", clip_path(cid), "-frames:v", "1",
                          "-vf", VF, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    img = Image.frombytes("RGB", (W, H), raw[:W*H*3])
    if i == len(SHOTS) - 1: img = zoom(img, t - s, dur, 0.06)
    return compose(img, t)

if __name__ == "__main__":
    mode, out = sys.argv[1], sys.argv[2]
    if mode == "stills":
        os.makedirs(out, exist_ok=True)
        times = [(f"00_apertura", 2.8)]
        for a, b, label, words in MOMENTS:
            times.append((f"{label}_momento", shot_bounds(b)[1] - 0.45))
        times.append(("99_cierre", TOTAL - 0.4))
        times += [(f"shot{i:02d}", starts[i] + SHOTS[i][2] / 2) for i in range(len(SHOTS))]
        for name, t in times:
            still(t).save(f"{out}/{name}.jpg", quality=88)
            print(name, round(t, 2))
        print("TOTAL", TOTAL)
    else:
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an",
                                "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
                                "-profile:v", "high", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        fi = 0
        for i in range(len(SHOTS)):
            s, e = shot_bounds(i)
            for k, fr in enumerate(shot_frames(i)):
                t = fi / FPS
                if i == len(SHOTS) - 1: fr = zoom(fr, k / FPS, SHOTS[i][2], 0.06)
                enc.stdin.write(compose(fr, t).tobytes()); fi += 1
            print(f"plano {i+1}/{len(SHOTS)} ok", flush=True)
        enc.stdin.close(); enc.wait()
        print("frames", fi, "dur", fi / FPS)
