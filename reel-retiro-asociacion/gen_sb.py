import sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R
meta = {}
for ln in open(os.path.join(R.BASE, "meta.txt")):
    d, cid, wh, du = ln.split()
    meta[cid] = d
def fmt(t): return f"{int(t//60)}:{t%60:04.1f}"
def label(cid):
    d = meta.get(cid, "NONE")
    return "sin fecha" if d == "NONE" else d[11:19]
segs = [("Apertura", "RETIRO DE ASOCIACIÓN · <em>Regnum Christi</em> · 21.11.2026", "00_apertura", [0], "Foto de grupo en el jardín. Título en Tenor Sans espaciada, filete dorado que se abre, «Regnum Christi» en EB Garamond itálica, fecha en dorado.")]
desc = {
 "01": "Bendición con alba y charla de apertura en el salón.",
 "02": "La charla continúa; el grupo se pone de pie a orar.",
 "03": "Testimonio con micrófono y los rostros que escuchan.",
 "04": "Jardín y carteles: «Con tu ayuda, el Reino florece…» y «Como piedras vivas…».",
 "05": "Recorrido guiado por el padre por la casa.",
 "06": "Saludos desde la escalera y el padre hablando en el patio.",
 "07": "La Virgen y la capilla: palabra y oración ante el altar.",
 "08": "Último momento en capilla, salida por el portón y el carro.",
}
for a, b, lab, words in R.MOMENTS:
    txt = " ".join(f"<em>{html.escape(w)}</em>" if acc else html.escape(w) for w, acc in words)
    segs.append((f"Momento {lab}", txt, f"{lab}_momento", list(range(a, b+1)), desc[lab]))
segs.append(("Cierre", "«En la comunidad encontramos el espejo donde vemos a Cristo en el otro» <span class='by'>— San Agustín</span>", "99_cierre", [len(R.SHOTS)-1],
             "Cielo y estatua desde la terraza en cámara lenta con zoom suave; velo vinotinto, cita línea a línea, escudo y @rcsenoritasbqto."))
cards, bar = [], []
for name, txt, img, shots, d in segs:
    s = R.starts[shots[0]]; e = R.shot_bounds(shots[-1])[1]
    bar.append(f'<a class="seg{" ends" if name in ("Apertura","Cierre") else ""}" href="#{img}" style="flex:{e-s:.2f}" title="{name}"><span>{name.replace("Momento ","")}</span></a>')
    sh = "".join(
        f'<figure><img src="img/shot{i:02d}.jpg" alt="Plano {i+1}" loading="lazy"><figcaption><b>{R.SHOTS[i][0]}</b><span>{R.SHOTS[i][2]:.1f} s · {label(R.SHOTS[i][0])}</span></figcaption></figure>'
        for i in shots)
    cards.append(f'''<article class="card" id="{img}">
  <img class="key" src="img/{img}.jpg" alt="Fotograma clave: {name}">
  <div class="info">
    <p class="when"><span>{name}</span><span>{fmt(s)} – {fmt(e)} · {e-s:.1f} s</span></p>
    <h2>{txt}</h2>
    <p class="desc">{d}</p>
    <div class="shots">{sh}</div>
  </div>
</article>''')
tpl = open(os.path.join(R.BASE, "work/sb_template.html")).read()
out = tpl.replace("{{BAR}}", "\n".join(bar)).replace("{{CARDS}}", "\n".join(cards)).replace("{{TOTAL}}", f"{R.TOTAL:.1f}").replace("{{NSHOTS}}", str(len(R.SHOTS)))
open(os.path.join(R.BASE, "storyboard/index.html"), "w").write(out)
print("ok", R.TOTAL)
