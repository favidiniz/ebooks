import re
base=open('nav-valeria.html').read()
base=base.replace("      if(i!==0) s.prepend(h);\n","").replace("      s.insertAdjacentHTML('beforeend', svg);\n","")
base=base.replace('.slide{position:relative;width:1080px;height:1350px','.slide{position:relative;width:1080px;height:1920px')
base=base.replace('aspect-ratio:4/5;overflow:hidden;background:#000','aspect-ratio:9/16;overflow:hidden;background:#000')
FX='assets/fiestas/fixed/'
STORE='<path d="M3.5 9.5L5 4h14l1.5 5.5"/><path d="M3.5 9.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5"/><path d="M5 12v8h14v-8M10 20v-5h4v5"/>'
CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def SL(): return f'<span class="sl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round">{STORE}</svg><span><b>¡Llegamos a donde estés!</b> En tiendas aliadas a nivel nacional.</span></span>'
def L(t,d): return f'<span class="line-mask"><span class="a-rise" style="--d:{d}s">{t}</span></span>'
def H(lines,d0=.2,cls='hd',st=''): return f'<h2 class="{cls}" style="{st}">'+''.join(L(t,d0+i*.14) for i,t in enumerate(lines))+'</h2>'
GOLD='<div class="lg a-fade" style="--d:.05s"><img src="assets/logo.png" alt="Colchones Imperia"></div>'
DARK='<div class="lg a-fade" style="--d:.05s"><img src="assets/logo-dark.png" alt="Colchones Imperia"></div>'
RIF='<div class="rif">RIF J-50441309-6</div>'
GLIT='<div class="glit"></div>'
def mat(src,x,y,w,d=.5,float_=True,extra=''):
    inner=f'<img class="mat" style="position:relative;width:100%;{extra}" src="{src}" alt="">'
    if float_: inner=f'<div class="float">{inner}</div>'
    return f'<div class="shadow a-fade" style="--d:{d+.4}s;left:{x+w*.1:.0f}px;width:{w*.8:.0f}px;top:{y+w*.48:.0f}px"></div><div class="abs mrise" style="--d:{d}s;left:{x}px;top:{y}px;width:{w}px">{inner}</div>'
def card(f,x=60,y=430,w=960,h=1200,pos='50% 50%',d=.2):
    return f'<div class="bgb" style="background-image:url({FX}{f}.png)"></div><div class="pc" style="--d:{d}s;left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="{FX}{f}.png" alt="" style="object-position:{pos}"></div>'
css=r'''
/* ===== STORIES 9:16 ===== */
.st{font-family:Montserrat,sans-serif}
.st .lg{position:absolute;z-index:40}.st .lg img{width:100%;display:block}
.st .rif{position:absolute;z-index:40;font:700 15px Montserrat;letter-spacing:.2em;white-space:nowrap}
.st .hd{font-family:"Cormorant Garamond",serif;font-weight:500;line-height:1;margin:0}
.st .hd em{font-style:italic;color:var(--gold)}
.st .kk{font:800 20px Montserrat;letter-spacing:.32em;color:var(--gold);text-transform:uppercase}
.st .sub{font:500 30px/1.45 Montserrat}
.st .sl{display:inline-flex;align-items:center;gap:14px;font:600 26px/1.3 Montserrat}
.st .sl svg{width:38px;height:38px;flex:none;color:var(--gold)}
.st .sl b{color:var(--gold)}
.st .abs{position:absolute}
.st .shadow{position:absolute;height:70px}
.on .mrise{animation:up 1.2s var(--ease-out) var(--d) both}
.on .float{animation:float 5s ease-in-out 1.6s infinite}
.glit{position:absolute;inset:0;pointer-events:none;z-index:30;overflow:hidden}
.glit i{position:absolute;width:var(--s);height:var(--s);background:var(--c);clip-path:polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%);opacity:0}
.on .glit i{animation:gl var(--t) ease-in-out var(--d) infinite}
@keyframes gl{0%,100%{opacity:0;transform:scale(.4) rotate(0)}50%{opacity:var(--o);transform:scale(1) rotate(45deg)}}
.bgb{position:absolute;inset:-60px;background-size:cover;background-position:center;filter:blur(38px) saturate(.9);transform:scale(1.15)}
.pc{position:absolute;z-index:10;border-radius:30px;overflow:hidden;border:2px solid rgba(233,206,140,.95);box-shadow:0 50px 90px -40px rgba(0,0,0,.7)}
.pc img{width:100%;height:100%;object-fit:cover;display:block}
.on .pc{animation:pcIn 1.1s var(--ease-out) var(--d) both}
@keyframes pcIn{from{opacity:0;transform:translateY(60px) scale(.97)}to{opacity:1;transform:none}}
.on .pc img{animation:zoom 7s var(--ease) both}
.chipg{display:inline-block;border:1.5px solid var(--gold);border-radius:999px;padding:12px 26px;font:700 24px Montserrat;letter-spacing:.05em}
.opt{display:flex;align-items:center;gap:22px;padding:28px 32px;border-radius:26px;font:600 34px Montserrat}
.opt i{flex:none;width:58px;height:58px;border-radius:50%;display:grid;place-items:center;font:600 34px "Cormorant Garamond",serif;font-style:normal}
.res{display:grid;grid-template-columns:300px 1fr;align-items:center;gap:22px;padding:22px 26px;border-radius:26px}
.res img{width:100%;height:150px;object-fit:contain}
.res .w{font:800 18px Montserrat;letter-spacing:.24em;text-transform:uppercase}
.res .p{font:500 46px/1.05 "Cormorant Garamond",serif;margin-top:6px}
.res .p small{display:block;font:500 22px Montserrat;margin-top:6px}
.sign{display:flex;align-items:center;gap:26px;padding:30px 34px;border-radius:26px;border:1.5px solid rgba(201,170,92,.5);font:600 36px Montserrat}
.sign i{flex:none;width:64px;height:64px;border-radius:50%;border:2.5px solid var(--gold);display:grid;place-items:center;position:relative;color:var(--ink)}
.sign i::before{content:"";position:absolute;inset:-2px;border-radius:50%;background:var(--gold);transform:scale(0)}
.on .sign i::before{animation:pop .5s var(--ease-out) var(--c) both}
.sign i svg{width:36px;height:36px;position:relative;opacity:0}
.on .sign i svg{animation:fade .3s ease var(--c) both}
.rib{position:absolute;left:-200px;right:-200px;height:120px;z-index:45;background:linear-gradient(180deg,#9C7A33,#EBD7A0 45%,#C9AA5C 55%,#8F7030);box-shadow:0 10px 30px rgba(0,0,0,.35);transform:rotate(-20deg) translateX(-130%)}
.on .rib{animation:rib2 1.2s cubic-bezier(.6,0,.3,1) .1s both}
@keyframes rib2{to{transform:rotate(-20deg) translateX(130%)}}
.callnum{position:absolute;z-index:12;width:54px;height:54px;margin:-27px 0 0 -27px;border-radius:50%;background:var(--gold);color:var(--ink);display:grid;place-items:center;font:700 30px "Cormorant Garamond",serif;box-shadow:0 0 0 12px rgba(201,170,92,.25)}
.on .callnum{animation:pop .6s var(--ease-out) var(--d) both}
.legend{display:flex;flex-direction:column;gap:18px}
.legend div{display:flex;gap:20px;align-items:flex-start}
.legend b{flex:none;width:44px;height:44px;border-radius:50%;background:var(--gold);color:var(--ink);display:grid;place-items:center;font:700 26px "Cormorant Garamond",serif}
.legend p{margin:0;font:500 28px/1.35 Montserrat;color:#CFC6B4}
.legend p strong{color:var(--ivory);font-weight:700}
/* set looks */
.sA{background:radial-gradient(100% 60% at 50% 45%,#2B251A 0%,#14120D 55%,#0A0907 100%);color:var(--ivory)}
.sA .lg{left:50%;top:150px;width:300px;margin-left:-150px}.sA .rif{left:0;right:0;top:250px;text-align:center;color:#CFC6B4}
.sB{background:#F5F2EB;color:var(--ink)}
.sB .silkb{position:absolute;inset:0;background:url(assets/silk.webp) center/cover;opacity:.75}
.sB .lg{left:70px;top:150px;width:260px}.sB .rif{left:350px;top:200px;color:#3A342B}
.sB .hd em{color:var(--gold-lo)}.sB .kk{color:var(--gold-lo)}
.sB .opt{background:rgba(255,255,255,.85);border:1px solid rgba(143,112,48,.25);box-shadow:0 20px 40px -26px rgba(60,45,20,.5)}
.sB .opt i{background:var(--gold);color:var(--ink)}
.sB .res{background:rgba(255,255,255,.88);border:1px solid rgba(143,112,48,.22)}
.sB .res .w{color:var(--gold-lo)}
.sB .sl{color:var(--ink)}.sB .sl b{color:var(--gold-lo)}.sB .sl svg{color:var(--gold-lo)}
.sC{background:linear-gradient(180deg,#0C0B09 0%,#1A160F 55%,#0C0B09 100%);color:var(--ivory)}
.sC .frm{position:absolute;inset:34px;border:1.5px solid rgba(201,170,92,.7);z-index:35;pointer-events:none}
.sC .lg{right:80px;top:150px;width:250px}.sC .rif{right:84px;top:240px;color:#CFC6B4}
.sP .lg{left:84px;top:150px;width:250px;z-index:40}
.sP .rif{left:350px;top:196px}
.sP .band{position:absolute;left:0;right:0;z-index:20}
.sV{background:#F5F2EB;color:var(--ink)}.sV .bgb{opacity:.55}
.sV .veil{position:absolute;inset:0;background:rgba(245,242,235,.55)}
.sV .hd em{color:var(--gold-lo)}.sV .kk{color:var(--gold-lo)}.sV .rif{color:#3A342B}
.sV .sl{color:var(--ink)}.sV .sl b{color:var(--gold-lo)}.sV .sl svg{color:var(--gold-lo)}
.sK{background:#0C0B09;color:var(--ivory)}.sK .bgb{opacity:.6}
.sK .veil{position:absolute;inset:0;background:rgba(12,11,9,.55)}.sK .rif{color:#CFC6B4}
.sK .tagg{position:absolute;z-index:22;background:#FBF8F1;color:var(--ink);padding:16px 26px 16px 50px;border-radius:10px 40px 40px 10px;font:italic 500 36px "Cormorant Garamond",serif;box-shadow:0 14px 30px -14px rgba(0,0,0,.6)}
.sK .tagg::before{content:"";position:absolute;left:18px;top:50%;width:14px;height:14px;margin-top:-7px;border-radius:50%;border:2.5px solid var(--gold)}
.sH{background:#EFE6D6;color:var(--ink)}.sH .bgb{opacity:.5}
.sH .veil{position:absolute;inset:0;background:rgba(239,230,214,.6)}
.sH .hd em{color:var(--gold-lo)}.sH .kk{color:var(--gold-lo)}.sH .rif{color:#3A342B}
.sH .pc{border-radius:6px;border:18px solid #FFFEFB;border-bottom-width:18px;box-shadow:0 40px 70px -30px rgba(50,35,15,.6)}
.sP .sl{padding:16px 26px;border-radius:999px;box-shadow:0 14px 30px -16px rgba(0,0,0,.5);font-size:23px}.sV .sl,.sH .sl{background:#FBF8F1}.sK .sl{background:rgba(12,11,9,.85);border:1px solid rgba(201,170,92,.5)}
.sH .sl{color:var(--ink)}.sH .sl b{color:var(--gold-lo)}.sH .sl svg{color:var(--gold-lo)}
'''
S={}
# ===== A · PREMIUM AL DETALLE (dark luxe) =====
S['premium']=dict(title='Story Premium',cls='sA',head='Premium <em>al detalle</em>.',desc='Gráfico, sin personas. Negro y dorado, logo arriba al centro.',
notes=['<b>1 · Gancho</b> <span>el Premium sube y flota entre destellos</span>','<b>2 · Anatomía</b> <span>primer plano con 3 puntos numerados</span>','<b>3 · Lado A / Lado B</b> <span>el colchón gira · deja espacio abajo para una <b>encuesta</b> (“¿Firme o suave?”)</span>','<b>4 · Medidas + tiendas</b>'],
slides=f'''
<section class="slide st sA">{GLIT}{GOLD}{RIF}
  <div class="abs" style="left:80px;right:80px;top:420px;text-align:center"><div class="kk a-fade" style="--d:.2s">Línea Premium</div>{H(['Hay colchones…','<em>y hay un Premium.</em>'],.3,'hd','font-size:104px;margin-top:20px')}</div>
  <div class="glow abs" style="left:50%;top:880px;width:1100px;height:700px;margin-left:-550px"></div>
  {mat('assets/m7166.webp',90,950,900,.6)}
  <div class="abs a-up" style="--d:1.6s;left:0;right:0;top:1500px;text-align:center;font:600 26px Montserrat;letter-spacing:.2em;color:var(--gold-hi)">DOBLE PILLOW TOP · ORTOPÉDICO</div>
</section>
<section class="slide st sA">{GLIT}{GOLD}
  <div class="abs" style="left:80px;right:80px;top:330px">{H(['Lo que no se ve,','<em>se siente.</em>'],.2,'hd','font-size:92px')}</div>
  <div class="abs a-fade" style="--d:.3s;left:300px;top:520px;width:700px"><img src="assets/m7168.webp" alt="" style="width:100%;display:block"></div>
  <div class="callnum" style="--d:1.2s;left:733px;top:594px">1</div><div class="callnum" style="--d:1.5s;left:457px;top:668px">2</div><div class="callnum" style="--d:1.8s;left:770px;top:944px">3</div>
  <div class="legend abs" style="left:90px;right:90px;top:1340px">
    <div class="a-up" style="--d:1.3s"><b>1</b><p><strong>Doble pillow top</strong>: acogida envolvente por ambas caras.</p></div>
    <div class="a-up" style="--d:1.6s"><b>2</b><p><strong>Acolchado premium</strong>: sensación de nube que se mantiene.</p></div>
    <div class="a-up" style="--d:1.9s"><b>3</b><p><strong>Soporte ortopédico</strong>: firmeza toda la noche.</p></div></div>
</section>
<section class="slide st sA">{GLIT}{GOLD}
  <div class="abs" style="left:80px;right:80px;top:330px;text-align:center">{H(['Suavidad','<em>por ambos lados.</em>'],.2,'hd','font-size:96px')}</div>
  <div class="s7" style="position:absolute;inset:0;background:none">
    <div class="stage a-up" style="--d:.5s;left:90px;top:640px;width:900px;height:490px"><div class="card"><div class="face a"><img src="assets/m7166.webp" alt=""><span class="side">LADO A</span></div><div class="face b"><img src="assets/m7166.webp" alt=""><span class="side">LADO B</span></div></div></div></div>
  <div class="abs a-up" style="--d:1.2s;left:120px;right:120px;top:1180px;text-align:center;font:500 28px/1.45 Montserrat;color:#CFC6B4">Doble capa de acolchado premium que <b style="color:var(--ivory)">alarga la vida útil</b> del colchón.</div>
</section>
<section class="slide st sA">{GLIT}{GOLD}
  <div class="abs" style="left:80px;right:80px;top:330px;text-align:center">{H(['Para cada','<em>tamaño de reino.</em>'],.2,'hd','font-size:96px')}</div>
  <div class="glow abs" style="left:50%;top:560px;width:1100px;height:600px;margin-left:-550px"></div>
  {mat('assets/m7163.webp',110,640,860,.4)}
  <div class="abs" style="left:80px;right:80px;top:1130px;display:flex;justify-content:center;gap:14px;flex-wrap:wrap"><span class="chipg a-pop" style="--d:1.2s">Individual</span><span class="chipg a-pop" style="--d:1.35s">Matrimonial</span><span class="chipg a-pop" style="--d:1.5s">Queen</span><span class="chipg a-pop" style="--d:1.65s">King</span></div>
  <div class="abs a-up" style="--d:2s;left:0;right:0;top:1300px;text-align:center"><div class="hd" style="font:italic 500 54px 'Cormorant Garamond',serif;color:var(--gold-hi)">Descanso de realeza.</div><div style="margin-top:24px;color:var(--ivory)">{SL()}</div></div>
</section>''')
# ===== B · CUAL ES TU IMPERIA (cream quiz) =====
S['quiz']=dict(title='Story Quiz',cls='sB',head='¿Cuál es <em>tu Imperia</em>?',desc='Gráfico, sin personas. Crema con seda, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>tres colchones entran en fila</span>','<b>2 · Pregunta</b> <span>tres opciones · espacio abajo para un <b>sticker de cuestionario</b> con A, B y C</span>','<b>3 · Resultados</b> <span>cada opción con su colchón real</span>','<b>4 · Cierre</b> <span>tiendas aliadas</span>'],
slides=f'''
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}{RIF}
  <div class="abs" style="left:80px;right:80px;top:400px">{H(['¿Cuál es','<em>tu Imperia?</em>'],.2,'hd','font-size:120px')}<div class="sub a-up" style="--d:.8s;margin-top:24px;color:#3A342B">Responde y descúbrelo en 3 historias.</div></div>
  {mat('assets/m7213.webp',170,760,740,.6,False)}
  {mat('assets/m7257.webp',50,1150,480,.9,False,'filter:brightness(1.15)')}
  {mat('assets/m7163.webp',550,1170,480,1.2,False)}
</section>
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}
  <div class="abs" style="left:80px;right:80px;top:330px">{H(['¿Cómo te gusta','<em>dormir?</em>'],.2,'hd','font-size:100px')}</div>
  <div class="abs" style="left:80px;right:80px;top:640px;display:flex;flex-direction:column;gap:22px">
    <div class="opt a-up" style="--d:.8s"><i>A</i>Firme y clásico</div>
    <div class="opt a-up" style="--d:1.05s"><i>B</i>Que cuide mi espalda</div>
    <div class="opt a-up" style="--d:1.3s"><i>C</i>Como en un hotel 5★</div></div>
</section>
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}
  <div class="abs" style="left:80px;right:80px;top:330px">{H(['Tu respuesta,','<em>tu Imperia.</em>'],.2,'hd','font-size:96px')}</div>
  <div class="abs" style="left:60px;right:60px;top:620px;display:flex;flex-direction:column;gap:22px">
    <div class="res a-up" style="--d:.7s"><img src="assets/m7213.webp" alt=""><div><div class="w">Si elegiste A</div><div class="p">San Remo<small>Soporte firme, sueño reparador.</small></div></div></div>
    <div class="res a-up" style="--d:1s"><img src="assets/m7257.webp" alt="" style="filter:brightness(1.15)"><div><div class="w">Si elegiste B</div><div class="p">Therapy Pillow<small>Alineación de la columna.</small></div></div></div>
    <div class="res a-up" style="--d:1.3s"><img src="assets/m7163.webp" alt=""><div><div class="w">Si elegiste C</div><div class="p">Premium Pillow top<small>Una suite de cinco estrellas.</small></div></div></div></div>
</section>
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}
  <div class="abs" style="left:80px;right:80px;top:380px;text-align:center">{H(['Tu trono','<em>te espera.</em>'],.2,'hd','font-size:120px')}</div>
  <div class="glow abs" style="left:50%;top:700px;width:1000px;height:600px;margin-left:-500px"></div>
  {mat('assets/m7213.webp',100,780,880,.5)}
  <div class="abs a-up" style="--d:1.6s;left:0;right:0;top:1340px;text-align:center">{SL()}</div>
</section>''')
# ===== C · CUARTO LISTO PARA DICIEMBRE (black frame) =====
S['renueva']=dict(title='Story Renueva',cls='sC',head='Tu cuarto, <em>listo para diciembre</em>.',desc='Gráfico, sin personas. Negro con marco dorado, logo arriba a la derecha.',
notes=['<b>1 · Gancho</b> <span>una cinta dorada barre la pantalla y aparece el San Remo negro</span>','<b>2 · 3 señales</b> <span>se marcan una a una</span>','<b>3 · Elige tu medida</b> <span>espacio abajo para una <b>cuenta regresiva</b> o una encuesta</span>','<b>4 · Cierre</b> <span>tiendas aliadas</span>'],
slides=f'''
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}{RIF}
  <div class="abs" style="left:90px;right:90px;top:420px"><div class="kk a-fade" style="--d:.9s">Antes de las fiestas</div>{H(['Tu cuarto,','<em>listo para diciembre.</em>'],1,'hd','font-size:100px;margin-top:20px')}</div>
  <div class="glow abs" style="left:50%;top:860px;width:1100px;height:700px;margin-left:-550px"></div>
  {mat('assets/m7276.webp',90,960,900,1.2,True,'filter:brightness(1.2)')}
  <div class="rib" style="top:900px"></div>
</section>
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}
  <div class="abs" style="left:90px;right:90px;top:330px">{H(['3 señales de que','<em>pide cambio.</em>'],.2,'hd','font-size:96px')}</div>
  <div class="abs" style="left:90px;right:90px;top:700px;display:flex;flex-direction:column;gap:24px">
    <div class="sign a-up" style="--d:.7s;--c:1.3s"><i>{CHECK}</i>Se hunde en el centro</div>
    <div class="sign a-up" style="--d:.9s;--c:1.8s"><i>{CHECK}</i>Suena al moverte</div>
    <div class="sign a-up" style="--d:1.1s;--c:2.3s"><i>{CHECK}</i>Despiertas más cansado</div></div>
  <div class="abs a-up" style="--d:2.8s;left:90px;right:90px;top:1300px;font:italic 500 50px 'Cormorant Garamond',serif;color:var(--gold-hi)">Si marcaste una, es momento.</div>
</section>
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}
  <div class="abs" style="left:90px;right:90px;top:330px">{H(['Elige tu','<em>nuevo trono.</em>'],.2,'hd','font-size:100px')}</div>
  {mat('assets/m7213.webp',110,600,860,.4)}
  <div class="abs" style="left:90px;right:90px;top:1080px;display:flex;gap:14px;flex-wrap:wrap"><span class="chipg a-pop" style="--d:1.2s">San Remo</span><span class="chipg a-pop" style="--d:1.35s">Therapy Pillow</span><span class="chipg a-pop" style="--d:1.5s">Premium</span></div>
</section>
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}
  <div class="abs" style="left:90px;right:90px;top:380px;text-align:center">{H(['Recibe diciembre','<em>descansando.</em>'],.2,'hd','font-size:100px')}</div>
  <div class="glow abs" style="left:50%;top:640px;width:1100px;height:640px;margin-left:-550px"></div>
  {mat('assets/m7166.webp',90,720,900,.4)}
  <div class="abs a-up" style="--d:1.6s;left:0;right:0;top:1300px;text-align:center">{SL()}</div>
</section>''')
# ===== D · VALERIA (cream, card) =====
def band(top,html,cls='',st=''): return f'<div class="band {cls}" style="top:{top}px;padding:0 84px;{st}">{html}</div>'
S['valeria']=dict(title='Story Valeria',cls='sP sV',head='Tu descanso <em>en la agenda</em>.',desc='Con Valeria. Foto en tarjeta sobre fondo crema desenfocado, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>Valeria sobre el Premium</span>','<b>2 · Agenda</b> <span>espacio abajo para un <b>deslizador</b> (“¿Cuánto duermes en diciembre?”)</span>','<b>3 · Su colchón</b> <span>Premium en foto de estudio</span>','<b>4 · Cierre</b> <span>Valeria con su regalo + tiendas aliadas</span>'],
slides=f'''
<section class="slide st sP sV">{card('val-portada',100,470,880,1100,'50% 70%')}<div class="veil" style="z-index:1;background:none"></div>{GLIT}{DARK}{RIF}
  {band(280,H(['Diciembre se pone','<em>intenso…</em>'],.3,'hd','font-size:84px'))}
</section>
<section class="slide st sP sV">{card('val-s2',190,470,700,875,'50% 60%')}{GLIT}{DARK}
  {band(280,H(['8 horas de sueño:','<em>también van en la agenda.</em>'],.3,'hd','font-size:72px'))}
</section>
<section class="slide st sP sV"><div class="bgb" style="background-image:url(assets/silk.webp);filter:none;opacity:.8;transform:none;inset:0"></div>{GLIT}{DARK}
  {band(300,'<div class="kk a-fade" style="--d:.2s">El favorito de Valeria</div>'+H(['Premium','<em>Pillow top.</em>'],.3,'hd','font-size:110px;margin-top:16px'))}
  <div class="glow abs" style="left:50%;top:700px;width:1000px;height:600px;margin-left:-500px"></div>
  {mat('assets/m7163.webp',100,780,880,.5)}
  {band(1300,'<div class="sub a-up" style="--d:1.4s;color:#3A342B">Una cubierta superior de alta gama con <b>sensación de ingravidez</b>. Hasta queen y king.</div>')}
</section>
<section class="slide st sP sV">{card('val-s4',100,470,880,1100,'50% 60%')}{GLIT}{DARK}
  {band(280,H(['Regálate','<em>buenas noches.</em>'],.3,'hd','font-size:90px'))}
  <div class="abs a-up" style="--d:1.4s;left:60px;right:60px;top:1600px;text-align:center;z-index:25">{SL()}</div>
</section>''')
# ===== E · CAMILA (dark, gift tag) =====
S['camila']=dict(title='Story Camila',cls='sP sK',head='El regalo de <em>365 noches</em>.',desc='Con Camila. Foto en tarjeta sobre fondo oscuro desenfocado, etiqueta de regalo, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>una cinta dorada barre la pantalla y revela a Camila con el colchón con lazo</span>','<b>2 · 365 noches</b> <span>espacio abajo para un <b>sticker de pregunta</b> (“¿A quién le regalarías un Imperia?”)</span>','<b>3 · Guía de regalo</b> <span>tres colchones según la persona</span>','<b>4 · Cierre</b> <span>selfie de Camila + tiendas aliadas</span>'],
slides=f'''
<section class="slide st sP sK">{card('cam-portada',100,470,880,1100,'50% 60%')}<div class="veil"></div>{GLIT}{GOLD}{RIF}
  {band(280,H(['Mi regalo favorito','<em>no cabe debajo del árbol.</em>'],.5,'hd','font-size:70px'))}
  <div class="tagg a-pop" style="--d:1.5s;right:120px;top:1520px">Con cariño, Camila</div>
  <div class="rib" style="top:900px"></div>
</section>
<section class="slide st sP sK">{card('cam-s2',190,470,700,875,'50% 90%')}<div class="veil"></div>{GLIT}{GOLD}
  {band(280,H(['Un regalo que se usa','<em>365 noches al año.</em>'],.3,'hd','font-size:74px'))}
</section>
<section class="slide st sP sK"><div class="veil" style="background:radial-gradient(100% 60% at 50% 45%,#2B251A,#0C0B09)"></div>{GLIT}{GOLD}
  {band(300,H(['¿Para','<em>quién es?</em>'],.2,'hd','font-size:110px'))}
  <div class="abs" style="left:60px;right:60px;top:620px;display:flex;flex-direction:column;gap:22px;z-index:20">
    <div class="res a-up" style="--d:.6s;background:rgba(255,255,255,.06);border:1px solid rgba(201,170,92,.35)"><img src="assets/m7163.webp" alt=""><div><div class="w" style="color:var(--gold)">Para mamá y papá</div><div class="p">Premium Pillow top</div></div></div>
    <div class="res a-up" style="--d:.9s;background:rgba(255,255,255,.06);border:1px solid rgba(201,170,92,.35)"><img src="assets/m7257.webp" alt="" style="filter:brightness(1.3)"><div><div class="w" style="color:var(--gold)">Para quien cuida su espalda</div><div class="p">Therapy Pillow</div></div></div>
    <div class="res a-up" style="--d:1.2s;background:rgba(255,255,255,.06);border:1px solid rgba(201,170,92,.35)"><img src="assets/m7213.webp" alt=""><div><div class="w" style="color:var(--gold)">Para los jóvenes de la casa</div><div class="p">San Remo</div></div></div></div>
</section>
<section class="slide st sP sK">{card('cam-s4',100,470,880,1100,'50% 50%')}<div class="veil"></div>{GLIT}{GOLD}
  {band(280,H(['Créeme:','<em>se agradece cada mañana.</em>'],.3,'hd','font-size:76px'))}
  <div class="abs a-up" style="--d:1.4s;left:60px;right:60px;top:1600px;text-align:center;z-index:25;color:var(--ivory)">{SL()}</div>
</section>''')
# ===== F · HERRERA (album paper) =====
S['herrera']=dict(title='Story Herrera',cls='sP sH',head='Llegan <em>las visitas</em>.',desc='Con la familia Herrera. Estilo álbum: foto con borde blanco de polaroid sobre papel, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>la familia preparando el cuarto de huéspedes</span>','<b>2 · San Remo</b> <span>Sofía en el San Remo negro · espacio abajo para una <b>encuesta</b> (“¿Te visitan en diciembre?”)</span>','<b>3 · La cama grande</b> <span>todos en el Premium Doble Pillow top</span>','<b>4 · Cierre</b> <span>la pareja + tiendas aliadas</span>'],
slides=f'''
<section class="slide st sP sH">{card('hue-portada',100,470,880,1100,'50% 55%')}<div class="veil"></div>{GLIT}{DARK}{RIF}
  {band(280,H(['Diciembre:','<em>llegan las visitas.</em>'],.3,'hd','font-size:86px'))}
</section>
<section class="slide st sP sH">{card('hue-s3',190,470,700,875,'50% 60%')}<div class="veil"></div>{GLIT}{DARK}
  {band(280,H(['Que duerman','<em>como en casa.</em>'],.3,'hd','font-size:88px'))}
</section>
<section class="slide st sP sH">{card('vac-portada',100,470,880,1100,'50% 75%')}<div class="veil"></div>{GLIT}{DARK}
  {band(280,H(['Y en la cama grande,','<em>espacio para todos.</em>'],.3,'hd','font-size:76px'))}
  <div class="abs a-up" style="--d:1.4s;left:0;right:0;top:1600px;text-align:center;font:700 24px Montserrat;letter-spacing:.14em;color:var(--gold-lo);z-index:25">PREMIUM DOBLE PILLOW TOP · QUEEN Y KING</div>
</section>
<section class="slide st sP sH">{card('hue-s4',100,470,880,1100,'50% 50%')}<div class="veil"></div>{GLIT}{DARK}
  {band(280,H(['La mejor bienvenida','<em>es una buena noche.</em>'],.3,'hd','font-size:76px'))}
  <div class="abs a-up" style="--d:1.4s;left:60px;right:60px;top:1600px;text-align:center;z-index:25">{SL()}</div>
</section>''')
for key,c in S.items():
    s=base.replace('/* ============ PREVIEW PAGE ============ */', css+'\n/* ============ PREVIEW PAGE ============ */')
    s=re.sub(r'<template id="slides">.*?</template>',lambda m:'<template id="slides">'+c['slides']+'</template>',s,flags=re.S)
    s=re.sub(r'<title>.*?</title>',f'<title>{c["title"]}</title>',s)
    s=re.sub(r"fetch\('export-nav-valeria/'\+f\)",f"fetch('export-st-{key}/'+f)",s).replace("'imperia-valeria-'+f",f"'imperia-story-{key}-'+f")
    s=re.sub(r'<header>.*?</header>',lambda m:f'<header>\n    <h1>{c["head"]}</h1>\n    <p>Story set · 4 historias 1080×1920 (9:16) · 15 nov – 15 dic. {c["desc"]}</p>\n  </header>',s,flags=re.S)
    s=re.sub(r'<div class="capt">.*?</div>',lambda m:'<div class="capt"><b>Story set</b> Las zonas de arriba y abajo quedan libres para la barra y la respuesta de Instagram.</div>',s,flags=re.S)
    notes='\n'.join(f'          <li>{g}</li>' for g in c['notes'])
    s=re.sub(r'<h3>Guion de slides</h3>\s*<ol>.*?</ol>',lambda m:f'<h3>Guion de historias</h3>\n        <ol>\n{notes}\n        </ol>',s,flags=re.S)
    s=s.replace("      // stars\n","""      s.querySelectorAll('.glit').forEach(box=>{ const r=rng(71+i*11); for(let k=0;k<22;k++){ const d=document.createElement('i'); d.style.left=(r()*1080)+'px'; d.style.top=(r()*1920)+'px'; d.style.setProperty('--s',(10+r()*18).toFixed(0)+'px'); d.style.setProperty('--o',(.4+r()*.5).toFixed(2)); d.style.setProperty('--t',(2.4+r()*3).toFixed(1)+'s'); d.style.setProperty('--d',(-r()*5).toFixed(1)+'s'); d.style.setProperty('--c',k%3?'#EBD7A0':'#fff'); box.appendChild(d);} });
      // stars\n""",1)
    assert s.count('<section class="slide')==4,key
    open(f'st-{key}.html','w').write(s)
print('ok')
