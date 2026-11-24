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
def band(top,html,cls='',st=''): return f'<div class="band {cls}" style="top:{top}px;padding:0 84px;{st}">{html}</div>'
def sizes(lst,top,d=1.2,center=True):
    ch=''.join(f'<span class="chipg a-pop" style="--d:{d+i*.15:.2f}s">{x}</span>' for i,x in enumerate(lst))
    return f'<div class="abs" style="left:80px;right:80px;top:{top}px;display:flex;justify-content:{"center" if center else "flex-start"};gap:14px;flex-wrap:wrap;z-index:20">{ch}</div>'
AV=lambda img,pos: f'<div style="width:150px;height:150px;border-radius:50%;overflow:hidden;border:4px solid var(--gold);flex:none"><img src="{img}" alt="" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>'
# ===== 1 · THERAPY PILLOW (dark luxe) =====
S['therapy']=dict(title='Story Therapy',cls='sA',head='Therapy <em>Pillow</em>.',desc='Gráfico, sin personas. Solo Therapy Pillow. Negro y dorado, logo arriba al centro.',
notes=['<b>1 · Gancho</b> <span>el Therapy Pillow flota entre destellos</span>','<b>2 · Anatomía</b> <span>capa pillow + núcleo firme</span>','<b>3 · Pregunta</b> <span>espacio abajo para una <b>encuesta</b> (“¿Despiertas con dolor de espalda?”)</span>','<b>4 · Medidas + tiendas</b>'],
slides=f"""
<section class="slide st sA">{GLIT}{GOLD}{RIF}
  <div class="abs" style="left:80px;right:80px;top:420px;text-align:center"><div class="kk a-fade" style="--d:.2s">Therapy Pillow · Rebond</div>{H(['Tu espalda también','<em>merece descansar.</em>'],.3,'hd','font-size:96px;margin-top:20px')}</div>
  <div class="glow abs" style="left:50%;top:880px;width:1100px;height:700px;margin-left:-550px"></div>
  {mat('assets/m7257.webp',80,960,920,.6,True,'filter:brightness(1.25)')}
  <div class="abs a-up" style="--d:1.6s;left:0;right:0;top:1480px;text-align:center;font:600 26px Montserrat;letter-spacing:.2em;color:var(--gold-hi)">ORTOPÉDICO · INDIVIDUAL Y MATRIMONIAL</div>
</section>
<section class="slide st sA">{GLIT}{GOLD}
  <div class="abs" style="left:80px;right:80px;top:330px">{H(['Bienestar y confort','<em>en un solo colchón.</em>'],.2,'hd','font-size:86px')}</div>
  {mat('assets/m7257.webp',80,640,920,.3,False,'filter:brightness(1.25)')}
  <div class="callnum" style="--d:1.1s;left:560px;top:700px">1</div><div class="callnum" style="--d:1.4s;left:330px;top:960px">2</div>
  <div class="legend abs" style="left:90px;right:90px;top:1260px">
    <div class="a-up" style="--d:1.3s"><b>1</b><p><strong>Capa tipo pillow</strong>: una sensación envolvente y suave.</p></div>
    <div class="a-up" style="--d:1.6s"><b>2</b><p><strong>Núcleo firme</strong>: favorece la correcta alineación de la columna.</p></div></div>
</section>
<section class="slide st sA">{GLIT}{GOLD}
  <div class="abs" style="left:80px;right:80px;top:330px;text-align:center">{H(['¿Despiertas con','<em>la espalda cargada?</em>'],.2,'hd','font-size:90px')}</div>
  {mat('assets/m7257.webp',200,660,680,.5,True,'filter:brightness(1.25)')}
  <div class="abs a-up" style="--d:1.2s;left:120px;right:120px;top:1080px;text-align:center;font:500 28px/1.45 Montserrat;color:#CFC6B4">El Therapy Pillow cuida tu cuerpo <b style="color:var(--ivory)">mientras duermes.</b></div>
</section>
<section class="slide st sA">{GLIT}{GOLD}
  <div class="abs" style="left:80px;right:80px;top:330px;text-align:center">{H(['Despierta','<em>como nuevo.</em>'],.2,'hd','font-size:110px')}</div>
  <div class="glow abs" style="left:50%;top:560px;width:1100px;height:600px;margin-left:-550px"></div>
  {mat('assets/m7257.webp',80,640,920,.4,True,'filter:brightness(1.25)')}
  {sizes(['Individual','Matrimonial'],1150)}
  <div class="abs a-up" style="--d:2s;left:0;right:0;top:1300px;text-align:center"><div style="font:italic 500 54px 'Cormorant Garamond',serif;color:var(--gold-hi)">Therapy Pillow.</div><div style="margin-top:24px;color:var(--ivory)">{SL()}</div></div>
</section>""")
# ===== 2 · SAN REMO PILLOW TOP (cream) =====
S['sanremo-pt']=dict(title='Story San Remo Pillow',cls='sB',head='San Remo <em>Pillow top</em>.',desc='Gráfico, sin personas. Solo San Remo Pillow top, en blanco y negro. Crema con seda, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>el San Remo Pillow top blanco flota</span>','<b>2 · Pregunta</b> <span>A, B, C · espacio abajo para una <b>encuesta o cuestionario</b></span>','<b>3 · Respuesta</b> <span>las dos: equilibrio entre suavidad y firmeza, en blanco o negro</span>','<b>4 · Medidas + tiendas</b>'],
slides=f"""
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}{RIF}
  <div class="abs" style="left:80px;right:80px;top:400px"><div class="kk a-fade" style="--d:.2s">San Remo Pillow top</div>{H(['Ni muy firme,','<em>ni muy suave.</em>'],.3,'hd','font-size:112px;margin-top:18px')}</div>
  <div class="glow abs" style="left:50%;top:860px;width:1000px;height:640px;margin-left:-500px"></div>
  {mat('assets/m7201.webp',90,960,900,.6)}
</section>
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}
  <div class="abs" style="left:80px;right:80px;top:330px">{H(['¿Cómo te gusta','<em>tu colchón?</em>'],.2,'hd','font-size:100px')}</div>
  <div class="abs" style="left:80px;right:80px;top:640px;display:flex;flex-direction:column;gap:22px">
    <div class="opt a-up" style="--d:.8s"><i>A</i>Firme</div>
    <div class="opt a-up" style="--d:1.05s"><i>B</i>Suave</div>
    <div class="opt a-up" style="--d:1.3s"><i>C</i>Las dos cosas</div></div>
</section>
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}
  <div class="abs" style="left:80px;right:80px;top:330px">{H(['Si dijiste C,','<em>es tu San Remo Pillow top.</em>'],.2,'hd','font-size:80px')}</div>
  {mat('assets/m7215.webp',60,700,600,.5,False)}
  {mat('assets/m7266.webp',420,930,620,.8,False)}
  <div class="abs a-up" style="--d:1.4s;left:80px;right:80px;top:1320px;font:500 30px/1.45 Montserrat;color:#3A342B">El <b style="color:var(--ink)">equilibrio perfecto</b> entre suavidad y firmeza, con una capa superior acolchada que te envuelve. En blanco o en negro.</div>
</section>
<section class="slide st sB"><div class="silkb"></div>{GLIT}{DARK}
  <div class="abs" style="left:80px;right:80px;top:380px;text-align:center">{H(['Suavidad y','<em>soporte extra.</em>'],.2,'hd','font-size:112px')}</div>
  <div class="glow abs" style="left:50%;top:700px;width:1000px;height:600px;margin-left:-500px"></div>
  {mat('assets/m7201.webp',100,760,880,.5)}
  {sizes(['Individual','Matrimonial'],1230)}
  <div class="abs a-up" style="--d:1.8s;left:0;right:0;top:1380px;text-align:center">{SL()}</div>
</section>""")
# ===== 3 · SAN REMO clásico (black frame) =====
S['sanremo']=dict(title='Story San Remo',cls='sC',head='San Remo, <em>el clásico</em>.',desc='Gráfico, sin personas. Solo San Remo. Negro con marco dorado, logo arriba a la derecha.',
notes=['<b>1 · Gancho</b> <span>una cinta dorada barre la pantalla y aparece el San Remo</span>','<b>2 · 3 señales</b> <span>de que tu colchón pide cambio</span>','<b>3 · Por qué San Remo</b> <span>espacio abajo para una <b>cuenta regresiva</b> o una encuesta</span>','<b>4 · Cierre</b> <span>tiendas aliadas</span>'],
slides=f"""
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}{RIF}
  <div class="abs" style="left:90px;right:90px;top:420px"><div class="kk a-fade" style="--d:.9s">San Remo · Ortopédico</div>{H(['El clásico','<em>que no falla.</em>'],1,'hd','font-size:112px;margin-top:20px')}</div>
  <div class="glow abs" style="left:50%;top:860px;width:1100px;height:700px;margin-left:-550px"></div>
  {mat('assets/m7234.webp',80,1000,920,1.2,True,'filter:brightness(1.25)')}
  <div class="rib" style="top:900px"></div>
</section>
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}
  <div class="abs" style="left:90px;right:90px;top:330px">{H(['3 señales de que','<em>pide cambio.</em>'],.2,'hd','font-size:96px')}</div>
  <div class="abs" style="left:90px;right:90px;top:700px;display:flex;flex-direction:column;gap:24px">
    <div class="sign a-up" style="--d:.7s;--c:1.3s"><i>{CHECK}</i>Se hunde en el centro</div>
    <div class="sign a-up" style="--d:.9s;--c:1.8s"><i>{CHECK}</i>Suena al moverte</div>
    <div class="sign a-up" style="--d:1.1s;--c:2.3s"><i>{CHECK}</i>Despiertas más cansado</div></div>
  <div class="abs a-up" style="--d:2.8s;left:90px;right:90px;top:1300px;font:italic 500 50px 'Cormorant Garamond',serif;color:var(--gold-hi)">Si marcaste una, el San Remo te espera.</div>
</section>
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}
  <div class="abs" style="left:90px;right:90px;top:330px">{H(['Superficie acolchada,','<em>soporte firme.</em>'],.2,'hd','font-size:86px')}</div>
  {mat('assets/m7234.webp',110,600,860,.4,True,'filter:brightness(1.25)')}
  <div class="abs a-up" style="--d:1.2s;left:90px;right:90px;top:1060px;font:500 28px/1.45 Montserrat;color:#CFC6B4">Para un <b style="color:var(--ivory)">sueño reparador</b>, noche tras noche.</div>
</section>
<section class="slide st sC"><div class="frm"></div>{GLIT}{GOLD}
  <div class="abs" style="left:90px;right:90px;top:380px;text-align:center">{H(['Recibe diciembre','<em>descansando.</em>'],.2,'hd','font-size:100px')}</div>
  <div class="glow abs" style="left:50%;top:640px;width:1100px;height:640px;margin-left:-550px"></div>
  {mat('assets/m7234.webp',90,720,900,.4,True,'filter:brightness(1.25)')}
  {sizes(['Individual','Matrimonial'],1190)}
  <div class="abs a-up" style="--d:1.8s;left:0;right:0;top:1340px;text-align:center">{SL()}</div>
</section>""")
# ===== 4 · VALERIA · PREMIUM PILLOW TOP =====
S['valeria']=dict(title='Story Valeria',cls='sP sV',head='Valeria y su <em>Premium Pillow top</em>.',desc='Con Valeria. Solo Premium Pillow top. Foto en tarjeta sobre crema, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>Valeria en su Premium Pillow top</span>','<b>2 · Pregunta</b> <span>espacio abajo para un <b>deslizador</b> (“¿Cuánto duermes en diciembre?”)</span>','<b>3 · Por qué</b> <span>cubierta de alta gama, sensación de ingravidez</span>','<b>4 · Cierre</b> <span>cita de Valeria + medidas + tiendas aliadas</span>'],
slides=f"""
<section class="slide st sP sV">{card('val-s4',100,470,880,1100,'50% 60%')}{GLIT}{DARK}{RIF}
  {band(280,H(['Mi plan para diciembre:','<em>dormir como realeza.</em>'],.3,'hd','font-size:74px'))}
</section>
<section class="slide st sP sV"><div class="bgb" style="background-image:url(assets/silk.webp);filter:none;opacity:.8;transform:none;inset:0"></div>{GLIT}{DARK}
  {band(300,H(['Diciembre se pone','<em>intenso…</em>'],.3,'hd','font-size:100px'))}
  {mat('assets/m7163.webp',160,640,760,.5)}
  {band(1060,'<div class="sub a-up" style="--d:1.2s;color:#3A342B">Por eso el sueño también va <b>en la agenda.</b></div>')}
</section>
<section class="slide st sP sV"><div class="bgb" style="background-image:url(assets/silk.webp);filter:none;opacity:.8;transform:none;inset:0"></div>{GLIT}{DARK}
  {band(300,'<div class="kk a-fade" style="--d:.2s">Premium Pillow top</div>'+H(['Una suite de','<em>cinco estrellas.</em>'],.3,'hd','font-size:100px;margin-top:16px'))}
  <div class="glow abs" style="left:50%;top:700px;width:1000px;height:600px;margin-left:-500px"></div>
  {mat('assets/m7163.webp',100,760,880,.5)}
  {band(1260,'<div class="sub a-up" style="--d:1.4s;color:#3A342B">Una cubierta superior de alta gama con <b>sensación de ingravidez</b>.</div>')}
</section>
<section class="slide st sP sV"><div class="bgb" style="background-image:url(assets/silk.webp);filter:none;opacity:.8;transform:none;inset:0"></div>{GLIT}{DARK}
  {band(300,'<div class="a-up" style="--d:.2s;display:flex;align-items:center;gap:26px">'+AV(FX+'val-s4.png','52% 22%')+'<div><div style="font:italic 500 56px/1.1 Cormorant Garamond,serif;color:var(--ink)">“Dormir como realeza.”</div><div class="kk" style="margin-top:10px">Valeria</div></div></div>')}
  {mat('assets/m7163.webp',100,640,880,.5)}
  {sizes(['Individual','Matrimonial','Queen','King'],1120)}
  <div class="abs a-up" style="--d:1.8s;left:0;right:0;top:1300px;text-align:center;z-index:25">{SL()}</div>
</section>""")
# ===== 5 · CAMILA · PREMIUM DOBLE PILLOW TOP =====
S['camila']=dict(title='Story Camila',cls='sP sK',head='Camila y el <em>Premium Doble Pillow top</em>.',desc='Con Camila. Solo Premium Doble Pillow top. Foto en tarjeta sobre oscuro, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>cinta dorada que revela a Camila con su colchón con lazo</span>','<b>2 · 365 noches</b> <span>espacio abajo para un <b>sticker de pregunta</b> (“¿A quién le regalarías un Imperia?”)</span>','<b>3 · Por ambos lados</b> <span>el colchón gira: lado A, lado B</span>','<b>4 · Cierre</b> <span>selfie de Camila + tiendas aliadas</span>'],
slides=f"""
<section class="slide st sP sK">{card('cam-portada',100,470,880,1100,'50% 60%')}<div class="veil"></div>{GLIT}{GOLD}{RIF}
  {band(280,H(['Mi regalo favorito','<em>no cabe debajo del árbol.</em>'],.5,'hd','font-size:70px'))}
  <div class="tagg a-pop" style="--d:1.5s;right:120px;top:1520px">Con cariño, Camila</div>
  <div class="rib" style="top:900px"></div>
</section>
<section class="slide st sP sK"><div class="veil" style="background:radial-gradient(100% 60% at 50% 45%,#2B251A,#0C0B09)"></div>{GLIT}{GOLD}
  {band(300,H(['Un regalo que se usa','<em>365 noches al año.</em>'],.3,'hd','font-size:80px'))}
  {mat('assets/m7166.webp',140,620,800,.5)}
</section>
<section class="slide st sP sK"><div class="veil" style="background:radial-gradient(100% 60% at 50% 45%,#2B251A,#0C0B09)"></div>{GLIT}{GOLD}
  {band(300,'<div class="kk a-fade" style="--d:.2s">Premium Doble Pillow top</div>'+H(['Sensación de nube','<em>por ambos lados.</em>'],.3,'hd','font-size:86px;margin-top:16px'))}
  <div class="s7" style="position:absolute;inset:0;background:none"><div class="stage a-up" style="--d:.5s;left:90px;top:680px;width:900px;height:490px"><div class="card"><div class="face a"><img src="assets/m7166.webp" alt=""><span class="side">LADO A</span></div><div class="face b"><img src="assets/m7166.webp" alt=""><span class="side">LADO B</span></div></div></div></div>
  {band(1240,'<div class="sub a-up" style="--d:1.2s;color:#CFC6B4">Doble capa de acolchado premium que <b style="color:var(--ivory)">mantiene la suavidad por más tiempo.</b></div>')}
</section>
<section class="slide st sP sK">{card('cam-s4',100,470,880,1100,'50% 50%')}<div class="veil"></div>{GLIT}{GOLD}
  {band(280,H(['Créeme:','<em>se agradece cada mañana.</em>'],.3,'hd','font-size:76px'))}
  <div class="abs a-up" style="--d:1.4s;left:60px;right:60px;top:1600px;text-align:center;z-index:25;color:var(--ivory)">{SL()}</div>
</section>""")
# ===== 6 · HERRERA · SAN REMO DOBLE PILLOW TOP =====
S['herrera']=dict(title='Story Herrera',cls='sP sH',head='Los Herrera y el <em>San Remo Doble Pillow top</em>.',desc='Con la familia Herrera. Solo San Remo Doble Pillow top (blanco y negro). Estilo álbum, logo arriba a la izquierda.',
notes=['<b>1 · Gancho</b> <span>la familia preparando el cuarto de huéspedes</span>','<b>2 · Mariana lo prueba</b> <span>espacio abajo para una <b>encuesta</b> (“¿Te visitan en diciembre?”)</span>','<b>3 · También en negro</b> <span>Sofía en el San Remo Doble Pillow top negro</span>','<b>4 · Cierre</b> <span>la pareja + medidas + tiendas aliadas</span>'],
slides=f"""
<section class="slide st sP sH">{card('hue-portada',100,470,880,1100,'50% 55%')}<div class="veil"></div>{GLIT}{DARK}{RIF}
  {band(280,H(['Diciembre:','<em>llegan las visitas.</em>'],.3,'hd','font-size:86px'))}
</section>
<section class="slide st sP sH">{card('hue-s2',190,470,700,875,'50% 60%')}<div class="veil"></div>{GLIT}{DARK}
  {band(280,H(['Mariana ya','<em>lo probó.</em>'],.3,'hd','font-size:90px'))}
</section>
<section class="slide st sP sH">{card('hue-s3',100,470,880,1100,'50% 60%')}<div class="veil"></div>{GLIT}{DARK}
  {band(280,H(['Lujo en cada lado,','<em>también en negro.</em>'],.3,'hd','font-size:78px'))}
  <div class="abs a-up" style="--d:1.4s;left:0;right:0;top:1600px;text-align:center;font:700 24px Montserrat;letter-spacing:.14em;color:var(--gold-lo);z-index:25">SAN REMO DOBLE PILLOW TOP</div>
</section>
<section class="slide st sP sH">{card('hue-s4',100,470,880,1100,'50% 50%')}<div class="veil"></div>{GLIT}{DARK}
  {band(280,H(['La mejor bienvenida','<em>es una buena noche.</em>'],.3,'hd','font-size:76px'))}
  <div class="abs a-up" style="--d:1.4s;left:60px;right:60px;top:1600px;text-align:center;z-index:25">{SL()}</div>
</section>""")
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
