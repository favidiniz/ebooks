import re
base=open('nav-valeria.html').read()
base=base.replace("      if(i!==0) s.prepend(h);\n","").replace("      s.insertAdjacentHTML('beforeend', svg);\n","")
P='assets/navidad/fixed/'
STORE='<path d="M3.5 9.5L5 4h14l1.5 5.5"/><path d="M3.5 9.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5"/><path d="M5 12v8h14v-8M10 20v-5h4v5"/>'
CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def SL(): return f'<span class="sl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round">{STORE}</svg><span><b>¡Llegamos a donde estés!</b> En tiendas aliadas a nivel nacional.</span></span>'
def L(t,d): return f'<span class="line-mask"><span class="a-rise" style="--d:{d}s">{t}</span></span>'
def ph(f,pos='50% 50%'): return f'<div class="ph"><img src="{P}{f}.png" alt="" style="object-position:{pos}"></div>'
RIF='<div class="rif">RIF J-50441309-6</div>'
ORN=lambda c1,c2: f'<svg viewBox="0 0 60 84"><defs><radialGradient id="g{c1[1:]}" cx="35%" cy="35%"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset=".25" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient></defs><line x1="30" y1="0" x2="30" y2="20" stroke="#C9AA5C" stroke-width="1.5"/><rect x="23" y="18" width="14" height="9" rx="2" fill="#C9AA5C"/><circle cx="30" cy="54" r="28" fill="url(#g{c1[1:]})"/></svg>'
BOW='<svg viewBox="0 0 200 120"><path d="M100 60 C70 10 20 10 22 45 C24 80 70 75 100 60Z M100 60 C130 10 180 10 178 45 C176 80 130 75 100 60Z" fill="#8F7030" stroke="#7E151B" stroke-width="2"/><path d="M92 62 L70 115 L88 108 L96 120 L104 64Z M108 62 L130 115 L112 108 L104 120 L96 64Z" fill="#8F7030" stroke="#7E151B" stroke-width="2"/><circle cx="100" cy="60" r="13" fill="#C9333B" stroke="#7E151B" stroke-width="2"/></svg>'
CANE='<svg viewBox="0 0 60 140"><defs><clipPath id="cc"><path d="M14 140 V40 a16 16 0 0 1 32 0 v8 h-12 v-8 a4 4 0 0 0 -8 0 V140Z"/></clipPath></defs><g clip-path="url(#cc)"><rect width="60" height="140" fill="#fff"/>'+''.join(f'<rect x="-40" y="{y}" width="140" height="9" fill="#8F7030" transform="rotate(-35 30 {y})"/>' for y in range(-20,170,18))+'</g><path d="M14 140 V40 a16 16 0 0 1 32 0 v8 h-12 v-8 a4 4 0 0 0 -8 0 V140Z" fill="none" stroke="#9c1a22" stroke-width="1.5"/></svg>'
TREE='<svg viewBox="0 0 40 48"><path d="M20 2 L32 20 H26 L36 34 H4 L14 20 H8Z" fill="#1F5A3A"/><rect x="17" y="34" width="6" height="8" fill="#7A4E2A"/><circle cx="20" cy="2" r="3" fill="#E9C66B"/></svg>'
css=r'''
/* ===== NAVIDAD ===== */
.slide.xm{background:#141210;color:var(--ink)}
.ph{position:absolute;inset:0;overflow:hidden}
.ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;transform-origin:50% 60%}
.on .ph img{animation:kb 7s cubic-bezier(.2,.6,.3,1) both}
@keyframes kb{from{transform:scale(1.05)}to{transform:scale(1)}}
.lg{position:absolute;z-index:40}.lg img{width:100%;display:block}
.rif{position:absolute;z-index:40;font:700 14px Montserrat;letter-spacing:.2em;white-space:nowrap}
.sl{display:inline-flex;align-items:center;gap:12px;font:600 21px/1.3 Montserrat}
.sl svg{width:30px;height:30px;flex:none}
.snow{position:absolute;inset:0;pointer-events:none;z-index:30;overflow:hidden}
.snow i{position:absolute;top:-20px;width:var(--s);height:var(--s);border-radius:50%;background:var(--c,#fff);opacity:var(--o);filter:blur(var(--b))}
.on .snow i{animation:fall var(--t) linear var(--d) infinite}
@keyframes fall{from{transform:translate(0,-30px)}to{transform:translate(var(--dx),1420px)}}
.bulbs{position:absolute;left:0;right:0;top:0;height:200px;z-index:35;pointer-events:none}
.bulbs .w{fill:none;stroke:#2B4A2F;stroke-width:3}
.bulbs circle{fill:var(--c);filter:drop-shadow(0 0 10px var(--c))}
.on .bulbs circle{animation:tw2 1.6s ease-in-out var(--d) infinite}
@keyframes tw2{0%,100%{opacity:1}50%{opacity:.35}}
.orn{position:absolute;z-index:34;width:var(--w,60px);transform-origin:50% 0}
.on .orn{animation:swing2 3.2s ease-in-out var(--d) infinite alternate}
@keyframes swing2{from{transform:rotate(-7deg)}to{transform:rotate(7deg)}}
.hd{font-family:"Cormorant Garamond",serif;font-weight:500;line-height:.98;margin:0}
.hd em{font-style:italic}
/* -- 1 VALERIA · tarjeta con luces -- */
.x-val .card{position:absolute;inset:28px;border:2px solid rgba(233,206,140,.95);z-index:33;pointer-events:none;box-shadow:inset 0 0 0 7px rgba(255,255,255,.18)}
.x-val .lg{left:56px;top:70px;width:230px;background:#FFFCF6;padding:12px 16px;border-radius:12px;box-shadow:0 12px 26px -14px rgba(0,0,0,.5)}.x-val .rif{left:300px;top:102px;color:#3A342B}.x-val .cov .hd{font-size:70px}
.x-val .scrim{position:absolute;left:0;right:0;z-index:12}
.x-val .tt{position:absolute;left:66px;right:66px;z-index:20}
.x-val .hd{font-size:88px;color:#1A1712}.x-val .hd em{color:#8F7030}
.x-val .sub{margin-top:14px;font:500 24px/1.45 Montserrat;color:#3A342B;max-width:640px}
.x-val .tg2{display:block;margin-bottom:16px;font:800 17px Montserrat;letter-spacing:.3em;color:#8F7030}
.x-val .note{position:absolute;z-index:20;background:#FFFCF6;border-radius:18px;padding:24px 28px;box-shadow:0 26px 50px -24px rgba(0,0,0,.6);border-top:6px solid #8F7030}
.x-val .note .hd{font-size:58px}
.x-val .note .sub{font-size:21px;margin-top:10px}
/* -- 2 CAMILA · lista de papel -- */
.x-cam .lg{right:50px;top:46px;width:230px;background:#FFFDF7;padding:12px 16px;border-radius:12px;box-shadow:0 12px 26px -14px rgba(0,0,0,.55)}.x-cam .rif{right:66px;top:120px;color:#3A342B;font-size:12px}
.paper{position:absolute;z-index:20;background:#FFFDF7;border-radius:6px;box-shadow:0 30px 60px -28px rgba(0,0,0,.6);padding:34px 34px 30px 74px;background-image:linear-gradient(90deg,transparent 52px,rgba(201,170,92,.6) 52px,rgba(201,170,92,.6) 54px,transparent 54px),repeating-linear-gradient(180deg,transparent 0 45px,rgba(201,170,92,.16) 45px 46px);transform:rotate(var(--r,0deg))}
.on .paper{animation:pIn .8s cubic-bezier(.3,1.4,.5,1) var(--d) both}
@keyframes pIn{from{opacity:0;transform:rotate(var(--r,0deg)) translateY(60px) scale(.9)}to{opacity:1;transform:rotate(var(--r,0deg))}}
.paper .hd{font-size:62px;color:#1A1712}.paper .hd em{color:#8F7030}
.paper .k{font:800 16px Montserrat;letter-spacing:.3em;color:#8F7030;margin-bottom:8px}
.it3{display:flex;align-items:center;gap:16px;font:italic 500 34px/46px "Cormorant Garamond",serif;color:#1A1712}
.it3 i{flex:none;width:30px;height:30px;border:2.5px solid #1A1712;border-radius:5px;display:grid;place-items:center;color:#8F7030;position:relative}
.it3 i svg{width:28px;height:28px;opacity:0;transform:scale(.3)}
.on .it3 i svg{animation:tick .4s cubic-bezier(.3,1.8,.5,1) var(--c) both}
@keyframes tick{to{opacity:1;transform:scale(1.25)}}
.it3 s{text-decoration:none;background:linear-gradient(#8F7030,#8F7030) 0 55%/0 2.5px no-repeat}
.on .it3 s{animation:strike .5s ease var(--c) both}
@keyframes strike{to{background-size:100% 2.5px}}
.it3.big{font-size:42px}
.washi{position:absolute;z-index:22;width:150px;height:40px;background:linear-gradient(90deg,rgba(215,188,114,.75),rgba(240,222,170,.85));opacity:.9;transform:rotate(var(--r))}
.cane{position:absolute;z-index:23;width:62px}
.on .cane{animation:stkIn2 .6s cubic-bezier(.3,1.6,.5,1) var(--d) both}
@keyframes stkIn2{from{opacity:0;transform:rotate(var(--r)) scale(.2)}to{opacity:1;transform:rotate(var(--r)) scale(1)}}
.x-cam .foot{position:absolute;z-index:20;background:#FFFDF7;border-radius:14px;padding:14px 20px;box-shadow:0 16px 34px -16px rgba(0,0,0,.5);color:#1A1712}
.x-cam .foot b{color:#8F7030}.x-cam .foot svg{color:#8F7030}
/* -- 3 PELICULAS · cine -- */
.film{position:absolute;top:0;bottom:0;width:62px;z-index:33;background:#0C0B09;overflow:hidden}
.film.l{left:0}.film.r{right:0}
.film i{position:absolute;left:16px;width:30px;height:2200px;top:-800px;background:repeating-linear-gradient(180deg,#F3E7C6 0 22px,transparent 22px 52px);border-radius:4px;opacity:.85}
.on .film i{animation:roll 4s linear infinite}
@keyframes roll{to{transform:translateY(520px)}}
.x-mov .lg{left:88px;bottom:44px;width:190px}.x-mov .rif{left:296px;bottom:66px;color:#F3E7C6}
.x-mov .lgbg{position:absolute;left:62px;right:62px;bottom:0;height:150px;z-index:32;background:linear-gradient(0deg,rgba(12,11,9,.88),rgba(12,11,9,0))}
.marq{position:absolute;z-index:20;left:110px;right:110px;background:rgba(12,11,9,.9);border:3px solid #C9AA5C;border-radius:22px;padding:30px 36px;text-align:center;box-shadow:0 30px 70px -30px rgba(0,0,0,.8)}
.marq .bul{position:absolute;inset:-14px;pointer-events:none}
.marq .bul i{position:absolute;width:12px;height:12px;border-radius:50%;background:#FFE9A8;box-shadow:0 0 10px #FFD36B}
.on .marq .bul i{animation:tw2 .9s steps(2) var(--d) infinite}
.marq .k{font:800 18px Montserrat;letter-spacing:.34em;color:#E7C36A}
.marq .hd{font-size:78px;color:#FFF6E2;margin-top:6px}.marq .hd em{color:#E7C36A}
.marq .sub{font:500 22px Montserrat;color:#E8DCC2;margin-top:10px}
.ticket{position:absolute;z-index:20;display:flex;background:#FBF6EA;color:#1A1712;border-radius:12px;box-shadow:0 20px 40px -18px rgba(0,0,0,.7);transform:rotate(var(--r))}
.on .ticket{animation:stkIn2 .7s cubic-bezier(.3,1.5,.5,1) var(--d) both}
.ticket .a{padding:18px 24px;border-right:3px dashed #8F7030}
.ticket .a small{display:block;font:800 14px Montserrat;letter-spacing:.3em;color:#8F7030}
.ticket .a b{display:block;font:italic 600 44px/1.05 "Cormorant Garamond",serif}
.ticket .b{padding:18px 20px;display:flex;align-items:center;font:800 26px Montserrat;color:#8F7030;writing-mode:vertical-rl;transform:rotate(180deg)}
.x-mov .cap{position:absolute;z-index:20;left:110px;right:110px;font:500 25px/1.45 Montserrat;color:#F3E7C6;text-shadow:0 2px 10px rgba(0,0,0,.8)}
.x-mov .cap b{color:#FFE29A}
/* -- 4 SANTA · cuento nocturno -- */
.x-san .lg{left:50%;top:40px;width:210px;margin-left:-105px}.x-san .rif{left:0;right:0;top:110px;text-align:center;color:#F3E7C6}
.x-san .topv{position:absolute;left:0;right:0;top:0;height:300px;z-index:12;background:linear-gradient(180deg,rgba(12,11,9,.72),rgba(12,11,9,0))}
.x-san .botv{position:absolute;left:0;right:0;bottom:0;z-index:12;background:linear-gradient(0deg,rgba(12,11,9,.9) 0%,rgba(12,11,9,.6) 45%,rgba(12,11,9,0) 100%)}
.x-san .tt{position:absolute;left:70px;right:70px;z-index:20;text-align:center}
.x-san .hd{font-size:80px;color:#FFF8EA}.x-san .hd em{color:#F0CF7A}
.x-san .sub{margin-top:14px;font:500 24px/1.45 Montserrat;color:#E6DEC8}
.x-san .sub b{color:#F0CF7A}
.x-san .sky i{position:absolute;width:var(--s);height:var(--s);background:#FFF3C8;clip-path:polygon(50% 0,61% 39%,100% 50%,61% 61%,50% 100%,39% 61%,0 50%,39% 39%);opacity:.3}
.on .x-san .sky i,.on.x-san .sky i{animation:tw3 var(--t) ease-in-out var(--d) infinite}
@keyframes tw3{0%,100%{opacity:.2;transform:scale(.7)}50%{opacity:1;transform:scale(1.1)}}
.shoot{position:absolute;z-index:25;left:-300px;top:var(--y);width:260px;height:4px;border-radius:4px;background:linear-gradient(90deg,rgba(240,207,122,0),#FFE9A8);transform:rotate(-14deg)}
.shoot::after{content:"";position:absolute;right:-8px;top:-8px;width:20px;height:20px;background:#FFF3C8;clip-path:polygon(50% 0,61% 39%,100% 50%,61% 61%,50% 100%,39% 61%,0 50%,39% 39%)}
.on .shoot{animation:shoot 2.6s cubic-bezier(.4,0,.2,1) var(--d) infinite}
@keyframes shoot{0%{transform:translate(0,0) rotate(-14deg);opacity:0}10%{opacity:1}70%{opacity:1}100%{transform:translate(1700px,-420px) rotate(-14deg);opacity:0}}
.x-san .badge{display:inline-flex;align-items:center;gap:10px;margin-top:18px;background:rgba(240,207,122,.14);border:1.5px solid #F0CF7A;border-radius:999px;padding:10px 20px;font:700 19px Montserrat;letter-spacing:.08em;color:#F0CF7A}
.x-san .sl{color:#F3E7C6}.x-san .sl b{color:#F0CF7A}.x-san .sl svg{color:#F0CF7A}
'''
def bulbs(n=13,top=40,sag=70):
    pts=[];out=''
    for k in range(n):
        x=40+k*(1000/(n-1)); y=top+sag*4*(k/(n-1))*(1-k/(n-1))
        col=['#FF5A4E','#FFD36B','#7BE0A3','#FFD36B','#FFF1C9'][k%5]
        out+=f'<circle cx="{x:.0f}" cy="{y+12:.0f}" r="9" style="--c:{col};--d:{(k%3)*.5:.1f}s"/>'
    return f'<svg class="bulbs" viewBox="0 0 1080 200"><path class="w" d="M0 {top} Q540 {top+2*sag} 1080 {top}"/>{out}</svg>'
LOGO_D='<div class="lg a-fade" style="--d:.1s"><img src="assets/logo-dark.png" alt="Colchones Imperia"></div>'
LOGO_G='<div class="lg a-fade" style="--d:.1s"><img src="assets/logo.png" alt="Colchones Imperia"></div>'
SNOW='<div class="snow"></div>'
CAR={}
# ---------- 1 VALERIA ----------
def vh(lines,d0=.2): return '<h2 class="hd">'+''.join(L(t,d0+i*.15) for i,t in enumerate(lines))+'</h2>'
CAR['valeria']=dict(title='Visitas Valeria',key='x-val',head='La noche antes de <em>las visitas</em>.',
desc='Con Valeria. Estilo tarjeta navideña: marco dorado, guirnalda de luces de colores que titilan, esferas que se balancean y nieve.',
caption='La casa se llena estos días… pero antes, una noche solo para mí 🎄✨ Luces, chocolate y un buen colchón. ¿Tú también tienes tu ritual?',
guion=['<b>Portada</b> <span>Valeria abrazando su cojín con lazo, luces de colores y esferas</span>','<b>Primero, el cuarto</b> <span>vista desde arriba colgando la guirnalda</span>','<b>Un momento para mí</b> <span>chocolate caliente frente al ventanal</span>','<b>Dormir de verdad</b> <span>Valeria dormida + San Remo negro + tiendas aliadas</span>'],
slides=f'''
<section class="slide xm x-val">{ph('v-p','50% 70%')}<div class="scrim" style="top:0;height:520px;background:linear-gradient(180deg,rgba(250,246,240,.97) 0%,rgba(250,246,240,.9) 60%,rgba(250,246,240,0))"></div>
  
  <div class="card"></div>{LOGO_D}{RIF}{SNOW}
  <div class="tt cov" style="top:180px"><span class="tg2">ESTOS DÍAS</span>{vh(['Antes de que lleguen todos…','<em>me toca a mí.</em>'])}
  <div class="sub">La casa se llena en diciembre. <b>Tu descanso también cuenta.</b></div></div>
</section>
<section class="slide xm x-val">{ph('v-s2','50% 30%')}<div class="scrim" style="top:0;height:330px;background:linear-gradient(180deg,rgba(250,246,240,.9),rgba(250,246,240,0))"></div>
  <div class="card"></div>{LOGO_D}{SNOW}
  <div class="note a-up" style="--d:.6s;left:70px;bottom:90px;width:560px"><span class="tg2">PASO 1</span>{vh(['Primero, el cuarto.','<em>Luces, pino y lazos.</em>'],.8)}<div class="sub">Que se sienta diciembre desde que abres la puerta.</div></div>
</section>
<section class="slide xm x-val">{ph('v-s3','50% 60%')}
  <div class="card"></div>{LOGO_D}{SNOW}
  <div class="note a-up" style="--d:.6s;left:60px;top:190px;width:440px"><span class="tg2">PASO 2</span>{vh(['Después,','<em>un rato para mí.</em>'],.8)}<div class="sub">Chocolate caliente, manta y la ciudad encendida.</div></div>
</section>
<section class="slide xm x-val">{ph('v-s4','50% 40%')}<div class="scrim" style="bottom:0;height:560px;background:linear-gradient(0deg,rgba(250,246,240,.96) 0%,rgba(250,246,240,.85) 50%,rgba(250,246,240,0))"></div>
  <div class="card"></div>{LOGO_D}{SNOW}
  <div class="tt" style="bottom:90px"><span class="tg2">Y AL FINAL</span>{vh(['Dormir de verdad,','<em>como realeza.</em>'],.5)}
  <div class="sub" style="margin-top:12px">San Remo negro: superficie acolchada y soporte firme.</div><div style="margin-top:16px;color:#3A342B">{SL()}</div></div>
</section>''')
# ---------- 2 CAMILA ----------
CAR['camila']=dict(title='Lista Camila',key='x-cam',head='Mi lista de <em>diciembre</em>.',
desc='Con Camila. Estilo lista en papel: hoja de cuaderno, casillas que se marcan, tachones rojos, bastones de caramelo y cinta adhesiva.',
caption='Mi lista de diciembre ✍️🎄 Pijamas a juego ✔️ Regalos envueltos ✔️ Y lo más importante… dormir rico ✔️ ¿Qué no puede faltar en la tuya?',
guion=['<b>Portada</b> <span>Camila escribiendo su lista; la hoja de papel entra con bastones de caramelo</span>','<b>Pijamas a juego</b> <span>la casilla se marca y el ítem se tacha</span>','<b>Regalos envueltos</b> <span>segunda casilla marcada</span>','<b>Lista completa</b> <span>el último ítem: un colchón que valga la pena + tiendas aliadas</span>'],
slides=f'''
<section class="slide xm x-cam">{ph('c-p','50% 70%')}{LOGO_D}{RIF}{SNOW}
  <div class="paper" style="--d:.2s;--r:-2deg;left:50px;top:46px;width:520px;padding-top:24px;padding-bottom:22px"><div class="k">LO QUE NO PUEDE FALTAR</div><h2 class="hd">Mi lista de <em>diciembre</em></h2></div>
  <div class="washi" style="--r:-14deg;left:30px;top:34px"></div>
</section>
<section class="slide xm x-cam">{ph('c-s2','50% 40%')}{LOGO_D}{SNOW}
  <div class="paper" style="--d:.3s;--r:1.5deg;left:60px;bottom:110px;width:520px"><div class="it3 big" style="--c:1.4s"><i>{CHECK}</i><s>Pijamas a juego</s></div><div style="font:500 21px/1.4 Montserrat;color:#3A342B;margin-top:10px">Cuadros para toda la noche.</div></div>
  <div class="washi" style="--r:10deg;left:420px;bottom:330px"></div>
</section>
<section class="slide xm x-cam">{ph('c-s3','50% 40%')}{LOGO_D}{SNOW}
  <div class="paper" style="--d:.3s;--r:-1.5deg;right:40px;top:560px;width:450px"><div class="it3" style="--c:.9s;opacity:.55"><i>{CHECK}</i><s>Pijamas a juego</s></div><div class="it3 big" style="--c:1.6s"><i>{CHECK}</i><s>Regalos envueltos</s></div><div style="font:500 21px/1.4 Montserrat;color:#3A342B;margin-top:10px">Papel kraft, cinta y chocolate al lado.</div></div>
  <div class="washi" style="--r:-12deg;right:340px;top:546px"></div>
</section>
<section class="slide xm x-cam">{ph('c-s4','50% 40%')}{LOGO_D}{SNOW}
  <div class="paper" style="--d:.3s;--r:1deg;left:60px;bottom:330px;width:620px"><div class="it3" style="--c:.9s;opacity:.55"><i>{CHECK}</i><s>Pijamas a juego</s></div><div class="it3" style="--c:1.2s;opacity:.55"><i>{CHECK}</i><s>Regalos envueltos</s></div><div class="it3 big" style="--c:1.9s"><i>{CHECK}</i><s>Un colchón que valga la pena</s></div><div style="font:500 21px/1.4 Montserrat;color:#3A342B;margin-top:12px">Premium Pillow top: acabados artesanales y soporte superior.</div></div>
  <div class="foot a-up" style="--d:2.6s;left:60px;bottom:110px">{SL()}</div>
</section>''')
# ---------- 3 PELICULAS ----------
def marq(n=22):
    out=''
    for k in range(n):
        t=k/n; 
        if t<.25: x,y=t/.25*100,0
        elif t<.5: x,y=100,(t-.25)/.25*100
        elif t<.75: x,y=100-(t-.5)/.25*100,100
        else: x,y=0,100-(t-.75)/.25*100
        out+=f'<i style="left:calc({x:.1f}% - 6px);top:calc({y:.1f}% - 6px);--d:{(k%2)*.45}s"></i>'
    return f'<div class="bul">{out}</div>'
FILM='<div class="film l"><i></i></div><div class="film r"><i></i></div>'
CAR['peliculas']=dict(title='Películas Herrera',key='x-mov',head='Función navideña en la <em>cama grande</em>.',
desc='Con la familia Herrera. Estilo cine: tira de película que corre a los lados, marquesina con bombillos y boletos.',
caption='Función de esta noche: películas navideñas en la cama grande 🍿🎄 Mantas, palomitas y toda la familia. ¿Quién se duerme primero en tu casa?',
guion=['<b>Portada</b> <span>marquesina con bombillos: “Función navideña”</span>','<b>Llegan las palomitas</b> <span>boleto “Función 1”, Sofía saltando</span>','<b>Las risas</b> <span>boleto “Función 2”</span>','<b>Final</b> <span>las niñas dormidas + Premium Doble Pillow top + tiendas aliadas</span>'],
slides=f'''
<section class="slide xm x-mov">{ph('m-s4','50% 60%')}{FILM}<div class="lgbg"></div>{LOGO_G}{RIF}{SNOW}
  <div class="marq a-up" style="--d:.2s;top:120px">{marq()}<div class="k">ESTA NOCHE EN CASA</div><h2 class="hd">Función navideña<br><em>en la cama grande</em></h2><div class="sub">Mantas, palomitas y toda la familia.</div></div>
</section>
<section class="slide xm x-mov">{ph('m-s2','50% 50%')}{FILM}<div class="lgbg"></div>{LOGO_G}{SNOW}
  <div class="ticket" style="--d:.4s;--r:-4deg;left:110px;top:110px"><div class="a"><small>FUNCIÓN 1</small><b>Llegan las<br>palomitas</b></div><div class="b">ADMITE 4</div></div>
</section>
<section class="slide xm x-mov">{ph('m-p','50% 55%')}{FILM}<div class="lgbg"></div>{LOGO_G}{SNOW}
  <div class="ticket" style="--d:.4s;--r:3deg;right:110px;top:110px"><div class="a"><small>FUNCIÓN 2</small><b>Y las risas<br>de todos</b></div><div class="b">ADMITE 4</div></div>
</section>
<section class="slide xm x-mov">{ph('m-s3','50% 45%')}<div style="position:absolute;left:0;right:0;top:0;height:470px;z-index:12;background:linear-gradient(180deg,rgba(12,11,9,.85),rgba(12,11,9,0))"></div>{FILM}<div class="lgbg"></div>{LOGO_G}{SNOW}
  <div class="marq a-up" style="--d:.3s;top:60px;padding:20px 30px;left:170px;right:170px">{marq(18)}<div class="k">FIN DE LA FUNCIÓN</div><h2 class="hd" style="font-size:50px">Como siempre, <em>no llegan al final.</em></h2></div>
  <div class="cap a-up" style="--d:1.2s;top:auto;bottom:170px;left:auto;right:90px;width:470px;background:rgba(12,11,9,.82);border:1.5px solid #C9AA5C;border-radius:16px;padding:18px 22px;font-size:21px">Premium Doble Pillow top, <b>en queen y king</b>: espacio para todos.<div style="margin-top:12px">{SL()}</div></div>
</section>''')
# ---------- 4 SANTA ----------
SKY='<div class="sky" style="position:absolute;inset:0;z-index:14;pointer-events:none"></div>'
SH='<i class="shoot" style="--y:360px;--d:.6s"></i>'
CAR['santa']=dict(title='Santa Herrera',key='x-san',head='La noche de <em>esperar a Santa</em>.',
desc='Con la familia Herrera. Estilo cuento nocturno: cielo azul con estrellas que titilan, estrella fugaz dorada y textos centrados.',
caption='Esta noche alguien no quiere dormir… pero tiene que hacerlo 🌙✨ Galletas listas, leche servida y la carta bien a la vista. ¿Así es en tu casa?',
guion=['<b>Portada</b> <span>Sofía mirando la luna; estrellas y estrella fugaz</span>','<b>Todo listo</b> <span>papá la arropa: galletas y leche</span>','<b>La carta</b> <span>la carta sobre el San Remo blanco</span>','<b>Dulces sueños</b> <span>las niñas dormidas + San Remo + tiendas aliadas</span>'],
slides=f'''
<section class="slide xm x-san">{ph('s-p','50% 60%')}<div class="topv" style="height:520px;background:linear-gradient(180deg,rgba(12,11,9,.82) 0%,rgba(12,11,9,.5) 55%,rgba(12,11,9,0))"></div>{SKY}{SH}{LOGO_G}{RIF}{SNOW}
  <div class="tt" style="top:170px"><h2 class="hd">{L('Esta noche alguien',.2)}{L('no quiere dormir…',.35)}</h2><div class="sub a-up" style="--d:.9s"><b>pero tiene que hacerlo.</b></div></div>
</section>
<section class="slide xm x-san">{ph('s-s2','50% 60%')}<div class="topv"></div><div class="botv" style="height:520px"></div>{SKY}{LOGO_G}{SNOW}
  <div class="tt" style="bottom:100px"><h2 class="hd" style="font-size:68px">{L('Galletas listas,',.3)}{L('<em>leche servida.</em>',.45)}</h2><div class="sub a-up" style="--d:1s">Papá revisa que no falte nada antes de apagar la luz.</div></div>
</section>
<section class="slide xm x-san">{ph('s-s3','50% 50%')}<div class="topv" style="height:520px"></div>{SKY}{LOGO_G}{SNOW}
  <div class="tt" style="top:160px"><h2 class="hd" style="font-size:72px">{L('Y la carta,',.3)}{L('<em>bien a la vista.</em>',.45)}</h2></div>
</section>
<section class="slide xm x-san">{ph('s-s4','50% 35%')}<div class="topv"></div><div class="botv" style="height:470px"></div>{SKY}{LOGO_G}{SNOW}
  <div class="tt" style="bottom:90px"><h2 class="hd" style="font-size:74px">{L('Dulces sueños.',.3)}{L('<em>Mañana hay sorpresas.</em>',.45)}</h2>
  <div class="badge a-up" style="--d:1.1s">SAN REMO · soporte firme y superficie acolchada</div><div class="a-up" style="--d:1.4s;margin-top:18px">{SL()}</div></div>
</section>''')
for key,c in CAR.items():
    s=base.replace('/* ============ PREVIEW PAGE ============ */', css+'\n/* ============ PREVIEW PAGE ============ */')
    s=re.sub(r'<template id="slides">.*?</template>',lambda m:'<template id="slides">'+c['slides']+'</template>',s,flags=re.S)
    s=re.sub(r'<title>.*?</title>',f'<title>{c["title"]}</title>',s)
    s=re.sub(r"fetch\('export-nav-valeria/'\+f\)",f"fetch('export-xm-{key}/'+f)",s).replace("'imperia-valeria-'+f",f"'imperia-{key}-'+f")
    s=re.sub(r'<header>.*?</header>',lambda m:f'<header>\n    <h1>{c["head"]}</h1>\n    <p>Navidad (15 al 31 de diciembre) · {c["desc"]} 4 slides 1080×1350.</p>\n  </header>',s,flags=re.S)
    s=re.sub(r'<div class="capt">.*?</div>',lambda m:f'<div class="capt"><b>colchonesimperia</b> {c["caption"]}</div>',s,flags=re.S)
    notes='\n'.join(f'          <li>{g}</li>' for g in c['guion'])
    s=re.sub(r'<h3>Guion de slides</h3>\s*<ol>.*?</ol>',lambda m:f'<h3>Guion de slides</h3>\n        <ol>\n{notes}\n        </ol>',s,flags=re.S)
    s=s.replace("      // stars\n","""      s.querySelectorAll('.snow').forEach(box=>{ const r=rng(51+i*7); const cs=['#fff','#F3E1A6','#E7C36A']; for(let k=0;k<40;k++){ const d=document.createElement('i'); d.style.left=(r()*1080)+'px'; d.style.setProperty('--s',(3+r()*7).toFixed(1)+'px'); d.style.setProperty('--o',(.35+r()*.55).toFixed(2)); d.style.setProperty('--b',(r()*1.5).toFixed(1)+'px'); d.style.setProperty('--t',(6+r()*7).toFixed(1)+'s'); d.style.setProperty('--d',(-r()*13).toFixed(1)+'s'); d.style.setProperty('--dx',((r()-.5)*160).toFixed(0)+'px'); d.style.setProperty('--c',cs[k%3]); box.appendChild(d);} });
      s.querySelectorAll('.sky').forEach(box=>{ const r=rng(13+i*5); for(let k=0;k<26;k++){ const d=document.createElement('i'); d.style.left=(r()*1080)+'px'; d.style.top=(r()*420)+'px'; d.style.setProperty('--s',(8+r()*16).toFixed(0)+'px'); d.style.setProperty('--t',(1.8+r()*2.5).toFixed(1)+'s'); d.style.setProperty('--d',(-r()*3).toFixed(1)+'s'); box.appendChild(d);} });
      // stars\n""",1)
    assert s.count('<section class="slide')==4,key
    open(f'xm-{key}.html','w').write(s)
print('ok')
