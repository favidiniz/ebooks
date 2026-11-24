import re
base=open('nav-valeria.html').read()
base=base.replace("      if(i!==0) s.prepend(h);\n","")
base=base.replace("      s.insertAdjacentHTML('beforeend', svg);\n","")
P='assets/fiestas/fixed/'
STORE='<path d="M3.5 9.5L5 4h14l1.5 5.5"/><path d="M3.5 9.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5c0 1.4 1.1 2.5 2.4 2.5s2.4-1.1 2.4-2.5"/><path d="M5 12v8h14v-8M10 20v-5h4v5"/>'
CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def storeline(cls=''): return f'<span class="sl {cls}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round">{STORE}</svg><span><b>¡Llegamos a donde estés!</b> En tiendas aliadas a nivel nacional.</span></span>'
def L(t,d,cls='a-rise'): return f'<span class="line-mask"><span class="{cls}" style="--d:{d}s">{t}</span></span>'
css=r'''
/* ===== FIESTAS · FOTOS DE USUARIO ===== */
.slide.fx{background:#F6F1E8;color:var(--ink)}
.ph{position:absolute;inset:0;overflow:hidden}
.ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;transform-origin:50% 100%}
.on .ph img{animation:kb 7s cubic-bezier(.2,.6,.3,1) both}
@keyframes kb{from{transform:scale(1.045)}to{transform:scale(1)}}
.lg{position:absolute;z-index:30;filter:drop-shadow(0 2px 6px rgba(255,250,240,.55))}
.lg img{width:100%;display:block}
.kk{font:700 19px Montserrat;letter-spacing:.3em;text-transform:uppercase;color:var(--gold-lo)}
.ink{color:var(--ink)}
.gt{position:absolute;left:0;right:0;top:0;pointer-events:none}
.sl{display:inline-flex;align-items:center;gap:12px;font:600 21px/1.3 Montserrat}
.sl svg{width:30px;height:30px;flex:none;color:var(--gold-lo)}
.sl b{color:var(--gold-lo)}
.sparkle{position:absolute;inset:0;pointer-events:none;z-index:6}

/* --- VALERIA · editorial journal --- */
.cv-val .lg{left:58px;top:52px;width:220px}
.cv-val .ph img{filter:saturate(1.03) contrast(1.02)}
.cv-val .gt{height:560px;background:linear-gradient(180deg,rgba(248,243,234,.96) 0%,rgba(248,243,234,.82) 38%,rgba(248,243,234,0) 100%)}
.cv-val .tt{position:absolute;left:60px;right:60px;top:168px;z-index:10}
.cv-val h2{font-family:"Cormorant Garamond",serif;font-weight:500;font-size:96px;line-height:.95;margin:14px 0 0;color:var(--ink)}
.cv-val h2 em{font-style:italic;color:var(--gold-lo)}
.cv-val .rule{display:block;width:90px;height:2px;background:var(--gold);margin:20px 0 16px;transform-origin:left}
.cv-val .sub{font:500 25px/1.45 Montserrat;color:#3A342B;max-width:640px}
.cv-val .sub b{color:var(--ink)}
.plan{position:absolute;z-index:12;background:#FFFCF6;border-radius:18px;padding:24px 26px 22px;box-shadow:0 30px 60px -30px rgba(40,30,15,.55);border:1px solid rgba(143,112,48,.2)}
.plan::before{content:"";position:absolute;left:50%;top:-14px;width:120px;height:28px;margin-left:-60px;background:linear-gradient(90deg,rgba(215,188,114,.85),rgba(235,215,160,.85));transform:rotate(-3deg);border-radius:3px}
.plan h5{margin:0 0 14px;font:800 16px Montserrat;letter-spacing:.3em;color:var(--gold-lo)}
.plan .it2{display:flex;align-items:center;gap:14px;font:600 22px Montserrat;color:var(--ink);padding:9px 0;border-top:1px dashed rgba(143,112,48,.3)}
.plan .it2 i{width:30px;height:30px;border-radius:8px;border:2px solid var(--gold);display:grid;place-items:center;color:#fff;position:relative;flex:none}
.plan .it2 i::before{content:"";position:absolute;inset:-2px;border-radius:8px;background:var(--gold);transform:scale(0)}
.on .plan .it2 i::before{animation:pop .45s var(--ease-out) var(--c) both}
.plan .it2 i svg{width:20px;height:20px;position:relative;opacity:0}
.on .plan .it2 i svg{animation:fade .2s ease var(--c) both}
.plan .it2.hl{color:var(--gold-lo)}
.cv-val .qcard{position:absolute;z-index:12;background:rgba(255,252,246,.94);border-radius:22px;padding:26px 28px;box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
.cv-val .qcard p{margin:0;font:italic 500 36px/1.15 "Cormorant Garamond",serif;color:var(--ink)}
.cv-val .qcard small{display:block;margin-top:10px;font:700 15px Montserrat;letter-spacing:.24em;color:var(--gold-lo)}
.cv-val .swipe{position:absolute;right:60px;bottom:64px;z-index:12;font:700 19px Montserrat;letter-spacing:.24em;color:#F3E7C6;text-shadow:0 2px 8px rgba(0,0,0,.6)}
.on .cv-val .swipe b,.on.cv-val .swipe b{display:inline-block;animation:nudge 1.4s ease-in-out 3s infinite}
.cv-val.gr{background:#F6F1E8}
.cv-val.gr .silk{position:absolute;inset:0;background:url(assets/silk.webp) center/cover;opacity:.55}
.ring3{position:absolute}
.ring3 .trk{fill:none;stroke:rgba(168,134,55,.2);stroke-width:12}
.ring3 .arc{fill:none;stroke:var(--gold);stroke-width:12;stroke-linecap:round;stroke-dasharray:.3333 1;stroke-dashoffset:.3333}
.on .ring3 .arc{animation:arc 2.2s var(--ease) 1s both}
.ring3 .lbl{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ring3 .lbl b{font:500 150px/.9 "Cormorant Garamond",serif;color:var(--gold-lo)}
.ring3 .lbl span{font:700 22px Montserrat;letter-spacing:.3em;color:var(--ink)}
.moonz{position:absolute;font:italic 500 46px "Cormorant Garamond",serif;color:var(--gold)}
.on .moonz{animation:zz 3s ease-in-out var(--d) infinite}
@keyframes zz{0%{opacity:0;transform:translate(0,10px)}30%{opacity:1}100%{opacity:0;transform:translate(30px,-60px)}}
.tip3{display:flex;gap:16px;align-items:flex-start;font:500 24px/1.4 Montserrat;color:#3A342B}
.tip3 i{flex:none;width:40px;height:40px;border-radius:50%;background:var(--gold);color:#fff;display:grid;place-items:center;font:800 18px Montserrat;font-style:normal}

/* --- CAMILA · gift stickers --- */
.cv-cam .lg{right:54px;top:50px;width:210px}
.cv-cam .ph img{filter:saturate(1.08) brightness(1.03)}
.stk{position:absolute;z-index:12;display:inline-block;background:#FFFFFF;color:var(--ink);font:800 38px/1.1 Montserrat;padding:16px 24px;border-radius:16px;box-shadow:0 16px 34px -14px rgba(0,0,0,.45);transform:rotate(var(--r,0deg))}
.stk.g{background:linear-gradient(135deg,#E2C97F,#C9AA5C 55%,#B08D42);color:#1A1712}
.stk.k{background:#14120E;color:#F3E7C6}
.stk em{font:italic 500 1.15em "Cormorant Garamond",serif}
.on .stk{animation:stkIn .6s cubic-bezier(.3,1.6,.5,1) var(--d) both}
@keyframes stkIn{from{opacity:0;transform:rotate(var(--r,0deg)) scale(.3)}to{opacity:1;transform:rotate(var(--r,0deg)) scale(1)}}
.ribbon{position:absolute;left:-200px;right:-200px;top:50%;height:150px;margin-top:-75px;z-index:40;background:linear-gradient(180deg,#B08D42,#EBD7A0 45%,#C9AA5C 55%,#9C7A33);box-shadow:0 10px 30px rgba(0,0,0,.35);transform:rotate(-24deg) translateX(-130%)}
.on .ribbon{animation:rib 1.1s cubic-bezier(.6,0,.3,1) .05s both}
@keyframes rib{0%{transform:rotate(-24deg) translateX(-130%)}100%{transform:rotate(-24deg) translateX(130%)}}
.gtag{position:absolute;z-index:12;background:#FFFCF6;padding:18px 26px 18px 52px;border-radius:10px 40px 40px 10px;font:italic 500 34px "Cormorant Garamond",serif;color:var(--ink);box-shadow:0 14px 30px -14px rgba(0,0,0,.5);transform:rotate(var(--r,0deg));transform-origin:12px 50%}
.gtag::before{content:"";position:absolute;left:18px;top:50%;width:14px;height:14px;margin-top:-7px;border-radius:50%;border:2.5px solid var(--gold)}
.on .gtag{animation:swing 2.4s ease-in-out var(--d) both}
@keyframes swing{0%{opacity:0;transform:rotate(-30deg)}20%{opacity:1;transform:rotate(14deg)}40%{transform:rotate(-8deg)}60%{transform:rotate(4deg)}80%,100%{opacity:1;transform:rotate(var(--r,0deg))}}
.cnt2{position:absolute;z-index:12;border-radius:50%;background:linear-gradient(135deg,#E2C97F,#C9AA5C 55%,#A8873C);box-shadow:0 20px 40px -18px rgba(0,0,0,.5);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#1A1712}
.cnt2 b{font:600 130px/.9 "Cormorant Garamond",serif;counter-reset:n var(--n)}
.cnt2 b::after{content:counter(n)}
.on .cnt2 b{animation:cnt 2.4s cubic-bezier(.2,.7,.2,1) 1s both}
.cnt2 span{font:800 18px Montserrat;letter-spacing:.24em}
.cv-cam.gr{background:#FBF7EF}
.cv-cam.gr .silk{position:absolute;inset:0;background:url(assets/silk.webp) center/cover;opacity:.5}
.prow{display:grid;grid-template-columns:1fr 230px;align-items:center;gap:16px;background:#fff;border-radius:20px;padding:16px 20px 16px 26px;box-shadow:0 14px 30px -20px rgba(0,0,0,.4);transform:rotate(var(--r,0deg))}
.prow .w{font:800 16px Montserrat;letter-spacing:.2em;color:var(--gold-lo);text-transform:uppercase}
.prow .p{font:800 29px Montserrat;margin-top:4px;color:var(--ink)}
.prow .p small{display:block;font:500 19px Montserrat;color:#6E675B;margin-top:3px}
.prow img{width:100%;height:96px;object-fit:contain}
.on .prow{animation:stkIn .6s cubic-bezier(.3,1.5,.5,1) var(--d) both}

/* --- HUESPEDES · hotel stationery --- */
.cv-hue .lg{left:62px;top:58px;width:210px}
.cv-hue .ph img{filter:saturate(.96) brightness(1.03) contrast(1.01)}
.cv-hue .frame2{position:absolute;inset:26px;border:2px solid rgba(201,170,92,.9);z-index:20;pointer-events:none;box-shadow:inset 0 0 0 6px rgba(255,255,255,.25)}
.cv-hue .frame2::before,.cv-hue .frame2::after{content:"";position:absolute;width:22px;height:22px;border:2px solid var(--gold);transform:rotate(45deg);background:#F6F1E8}
.cv-hue .frame2::before{left:50%;top:-13px;margin-left:-11px}
.cv-hue .frame2::after{left:50%;bottom:-13px;margin-left:-11px}
.cv-hue .gt{height:520px;background:linear-gradient(180deg,rgba(246,241,232,.94) 0%,rgba(246,241,232,.7) 42%,rgba(246,241,232,0) 100%)}
.doors{position:absolute;inset:0;z-index:35;display:flex;pointer-events:none}
.doors i{flex:1;background:#F3EDE2;border:1px solid rgba(201,170,92,.4);box-shadow:inset 0 0 0 30px #F3EDE2,inset 0 0 0 32px rgba(201,170,92,.6)}
.on .doors i:first-child{animation:dl 1.3s cubic-bezier(.7,0,.2,1) .25s both}
.on .doors i:last-child{animation:dr 1.3s cubic-bezier(.7,0,.2,1) .25s both}
@keyframes dl{to{transform:translateX(-102%)}}
@keyframes dr{to{transform:translateX(102%)}}
.card3{position:absolute;z-index:14;background:#FFFCF6;border-radius:6px;padding:34px 36px;box-shadow:0 30px 60px -30px rgba(30,22,10,.6);outline:1px solid rgba(201,170,92,.8);outline-offset:-12px}
.card3 .kk{display:block;text-align:center;margin-bottom:10px}
.card3 h3{margin:0;text-align:center;font:500 62px/1 "Cormorant Garamond",serif;color:var(--ink)}
.card3 h3 em{font-style:italic;color:var(--gold-lo)}
.card3 p{margin:16px 0 0;text-align:center;font:500 22px/1.45 Montserrat;color:#3A342B}
.cv-hue .tt{position:absolute;z-index:14;left:64px;right:64px;top:150px}
.cv-hue h2{margin:12px 0 0;font:500 88px/.96 "Cormorant Garamond",serif;color:var(--ink)}
.cv-hue h2 em{font-style:italic;color:var(--gold-lo)}
.cv-hue .sub{margin-top:14px;font:600 25px/1.4 Montserrat;color:#3A342B}
.hanger{position:absolute;z-index:14;background:#FFFCF6;border-radius:28px 28px 10px 10px;padding:120px 30px 30px;box-shadow:0 30px 60px -28px rgba(30,22,10,.65);transform-origin:50% 0}
.hanger::before{content:"";position:absolute;left:50%;top:26px;width:74px;height:74px;margin-left:-37px;border-radius:50%;background:transparent;box-shadow:0 0 0 2px rgba(201,170,92,.8),0 0 0 999px transparent;}
.hanger::after{content:"";position:absolute;left:50%;top:30px;width:66px;height:66px;margin-left:-33px;border-radius:50%;background:#7d6a50;opacity:.0}
.on .hanger{animation:hsw 2.6s ease-in-out .3s both}
@keyframes hsw{0%{opacity:0;transform:rotate(-14deg)}15%{opacity:1}35%{transform:rotate(8deg)}55%{transform:rotate(-4deg)}75%{transform:rotate(2deg)}100%{opacity:1;transform:rotate(0)}}
.hanger h3{margin:0 0 6px;text-align:center;font:500 48px/1 "Cormorant Garamond",serif;color:var(--ink)}
.hanger h3 em{font-style:italic;color:var(--gold-lo)}
.hanger .kk{display:block;text-align:center;font-size:15px}
.hanger .row3{display:flex;align-items:center;gap:14px;padding:13px 0;border-top:1px solid rgba(201,170,92,.35);font:600 21px/1.25 Montserrat;color:var(--ink)}
.hanger .row3 i{flex:none;width:32px;height:32px;border-radius:50%;border:2px solid var(--gold);display:grid;place-items:center;color:#fff;position:relative}
.hanger .row3 i::before{content:"";position:absolute;inset:-2px;border-radius:50%;background:var(--gold);transform:scale(0)}
.on .hanger .row3 i::before{animation:pop .45s var(--ease-out) var(--c) both}
.hanger .row3 i svg{width:20px;height:20px;position:relative;opacity:0}
.on .hanger .row3 i svg{animation:fade .2s ease var(--c) both}
.hanger .row3.hl{color:var(--gold-lo);font-weight:800}
.chip3{display:inline-block;border-radius:999px;padding:10px 20px;font:700 19px Montserrat;letter-spacing:.06em;background:rgba(20,18,14,.86);color:#F3E7C6;border:1.5px solid var(--gold)}

/* --- VACACIONES · family album --- */
.cv-vac{background:#EFE6D6}
.cv-vac .paper{position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 40%,#F7F0E3 0%,#EADFCB 100%)}
.cv-vac .paper::after{content:"";position:absolute;inset:0;opacity:.18;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.75' numOctaves='3'/></filter><rect width='220' height='220' filter='url(%23n)'/></svg>")}
.dots{position:absolute;inset:0;pointer-events:none}
.dots i{position:absolute;width:var(--s);height:var(--s);border-radius:50%;background:var(--gold);opacity:.55}
.cv-vac .head{position:absolute;left:70px;right:70px;top:46px;z-index:10}
.cv-vac .head h2{margin:8px 0 0;font:500 66px/1 "Cormorant Garamond",serif;color:var(--ink)}
.cv-vac .head h2 em{font-style:italic;color:var(--gold-lo)}
.pola{position:absolute;left:110px;top:190px;width:860px;padding:20px 20px 0;background:#FFFEFB;box-shadow:0 30px 60px -26px rgba(50,35,15,.55),0 2px 4px rgba(0,0,0,.08);transform:rotate(var(--r,-1.4deg));z-index:5}
.on .pola{animation:drop2 1.1s cubic-bezier(.2,.9,.3,1.1) .1s both}
@keyframes drop2{from{opacity:0;transform:translateY(-60px) rotate(-7deg)}to{opacity:1;transform:rotate(var(--r,-1.4deg))}}
.pola .pic{position:relative;width:820px;height:948px;overflow:hidden;background:#ddd}
.pola .pic img{width:100%;height:100%;object-fit:cover;object-position:50% 99%;display:block;filter:sepia(.08) saturate(1.06)}
.on .pola .pic img{animation:dev 2.6s ease-out .4s both}
@keyframes dev{from{filter:sepia(.4) saturate(.2) brightness(1.7) contrast(.7)}to{filter:sepia(.08) saturate(1.06) brightness(1) contrast(1)}}
.pola .leak{position:absolute;inset:0;background:linear-gradient(110deg,transparent 30%,rgba(255,170,80,.45) 50%,transparent 70%);mix-blend-mode:screen;transform:translateX(-100%)}
.on .pola .leak{animation:leak 2.4s ease-in-out 1.6s both}
@keyframes leak{to{transform:translateX(100%)}}
.pola .stamp{position:absolute;right:22px;bottom:18px;font:700 30px "Courier New",monospace;letter-spacing:.08em;color:#FF8A3D;text-shadow:0 0 6px rgba(255,120,40,.7);opacity:0}
.on .pola .stamp{animation:fade .5s ease 2.2s both}
.pola .cap{height:152px;display:flex;align-items:center;justify-content:space-between;gap:20px;padding:0 6px}
.pola .cap p{margin:0;font:italic 500 40px/1.12 "Cormorant Garamond",serif;color:#2A251E;max-width:560px}
.pola .cap p small{display:block;font:600 17px/1.4 Montserrat;font-style:normal;color:#6E675B;margin-top:6px}
.cv-vac .lg{position:absolute;right:26px;bottom:52px;width:200px;filter:none}
.tape{position:absolute;width:170px;height:46px;background:linear-gradient(90deg,rgba(215,188,114,.8),rgba(240,222,170,.85));z-index:7;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.chip4{display:inline-block;border-radius:999px;padding:8px 18px;font:700 17px Montserrat;background:var(--gold);color:#1A1712;margin-right:8px}
'''
cal_val=f'''<div class="plan a-up" style="--d:1.2s;left:48px;top:470px;width:370px"><h5>DICIEMBRE</h5>
  <div class="it2" style="--c:2s"><i>{CHECK}</i>Cena de fin de año</div>
  <div class="it2" style="--c:2.5s"><i>{CHECK}</i>Compras de regalos</div>
  <div class="it2" style="--c:3s"><i>{CHECK}</i>Reunión con amigas</div>
  <div class="it2 hl" style="--c:3.6s"><i>{CHECK}</i>8 horas de sueño</div></div>'''
LOGO='<div class="lg a-fade" style="--d:.1s"><img src="assets/logo-dark.png" alt="Colchones Imperia"></div>'
def ph(f,extra=''): return f'<div class="ph"><img src="{P}{f}.png" alt="" style="{extra}"></div>'
CAR={}
CAR['valeria']=dict(title='Diciembre Valeria',head='Diciembre también se <em>descansa</em>.',desc='Con Valeria. Estilo editorial de revista: titulares serif sobre degradado crema, agenda que se marca y luz dorada.',
caption='Diciembre llega con todo: cenas, compras, reuniones… y menos horas de sueño 🌙 Este mes, tu descanso también va en la agenda. Guárdalo ✨',
guion=['<b>Portada</b> <span>Valeria sobre el Premium, titular editorial, destellos dorados</span>','<b>Agenda llena, sueño completo</b> <span>tarjeta de agenda que se va marcando; el último punto son 8 horas de sueño</span>','<b>Siesta de 20 minutos</b> <span>gráfico: anillo que se llena y “zZ” flotando (no había foto para esta escena)</span>','<b>Regálate buenas noches</b> <span>Valeria con su regalo dorado, cita y tiendas aliadas</span>'],
slides=f'''
<section class="slide fx cv-val">{ph('val-portada')}<div class="gt"></div><div class="bokeh"></div>{LOGO}
  <div class="tt"><div class="kk a-fade" style="--d:.3s">Temporada de fiestas</div>
  <h2>{L('Diciembre también',.35)}{L('se <em>descansa.</em>',.5)}</h2><i class="rule a-grow" style="--d:1s"></i>
  <div class="sub a-up" style="--d:1.2s">La temporada más intensa del año merece <b>buenas noches.</b></div></div>
  <div class="swipe a-up" style="--d:2.4s">DESLIZA <b>→</b></div>
</section>
<section class="slide fx cv-val">{ph('val-s2')}<div class="gt" style="height:480px"></div>{LOGO}
  <div class="tt" style="top:150px"><h2 style="font-size:84px">{L('Agenda llena,',.2)}{L('<em>sueño completo.</em>',.35)}</h2>
  <div class="sub a-up" style="--d:.9s;margin-top:16px;max-width:560px">Agenda también tus horas de sueño.</div></div>
  {cal_val}
</section>
<section class="slide fx cv-val gr"><div class="silk"></div>{LOGO}
  <div class="tt" style="top:168px"><div class="kk a-fade" style="--d:.2s">Si la noche se alargó</div>
  <h2>{L('Una siesta de',.3)}{L('<em>20 minutos.</em>',.45)}</h2><i class="rule a-grow" style="--d:1s"></i></div>
  <div class="ring3 a-fade" style="--d:.6s;left:300px;top:540px;width:480px;height:480px"><svg viewBox="0 0 480 480" style="position:absolute;inset:0"><circle class="trk" cx="240" cy="240" r="215"/><circle class="arc" cx="240" cy="240" r="215" pathLength="1" transform="rotate(-90 240 240)"/></svg><div class="lbl"><b>20</b><span>MINUTOS</span></div></div>
  <div class="moonz" style="--d:1.4s;left:760px;top:560px">z</div><div class="moonz" style="--d:2s;left:800px;top:520px;font-size:60px">Z</div>
  <div class="abs" style="left:80px;right:80px;top:1080px;display:flex;flex-direction:column;gap:16px">
    <div class="tip3 a-up" style="--d:1.8s"><i>1</i><span>Te recarga <b>sin quitarte el sueño</b> de la noche.</span></div>
    <div class="tip3 a-up" style="--d:2.1s"><i>2</i><span>Mejor antes de las 3 de la tarde.</span></div></div>
</section>
<section class="slide fx cv-val">{ph('val-s4')}<div class="gt" style="height:430px;background:linear-gradient(90deg,rgba(248,243,234,.95),rgba(248,243,234,.55) 45%,rgba(248,243,234,0) 70%)"></div><div class="bokeh"></div>{LOGO}
  <div class="tt" style="top:160px;right:auto;width:440px"><h2 style="font-size:84px">{L('Regálate',.2)}{L('<em>buenas</em>',.35)}{L('<em>noches.</em>',.5)}</h2></div>
  <div class="qcard a-up" style="--d:1.4s;left:40px;top:860px;width:400px"><p>“Mi plan para diciembre: dormir como realeza.”</p><small>VALERIA</small>
  <div style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(143,112,48,.3)">{storeline()}</div></div>
</section>''')

CAR['camila']=dict(title='Regalo Camila',head='El regalo que se usa <em>365 noches</em>.',desc='Con Camila. Estilo stickers de regalo: cinta dorada que barre la pantalla, etiquetas que se balancean y stickers que aparecen.',
caption='Mi regalo favorito de este año no cabe debajo del árbol 🎁 Se usa todas las noches y se agradece cada mañana. Te cuento cómo elegirlo según para quién es ✨',
guion=['<b>Portada</b> <span>una cinta dorada barre la pantalla y revela a Camila con su colchón con lazo</span>','<b>365 noches</b> <span>contador dorado tipo sticker que sube a 365</span>','<b>Un Imperia para cada quien</b> <span>gráfico con fotos reales de cada colchón (no había foto para esta escena)</span>','<b>Regala descanso</b> <span>selfie de Camila, cita y tiendas aliadas</span>'],
slides=f'''
<section class="slide fx cv-cam">{ph('cam-portada')}<div class="gt" style="height:420px;background:linear-gradient(180deg,rgba(250,246,238,.8),rgba(250,246,238,0))"></div>{LOGO}
  <div class="stk" style="--d:1.1s;--r:-3deg;left:56px;top:150px">Mi regalo favorito</div>
  <div class="stk g" style="--d:1.4s;--r:2deg;left:96px;top:236px"><em>no cabe debajo del árbol.</em></div>
  <div class="gtag" style="--d:1.9s;--r:4deg;left:690px;top:380px">Con cariño, Camila</div>
  <div class="stk k" style="--d:2.6s;--r:0deg;right:56px;bottom:70px;font-size:20px;letter-spacing:.2em;padding:12px 20px">TE CUENTO CUÁL →</div>
  <div class="ribbon"></div>
</section>
<section class="slide fx cv-cam">{ph('cam-s2','object-position:50% 100%')}{LOGO}
  <div class="stk" style="--d:.5s;--r:-2deg;left:50px;top:110px">Un regalo que se usa…</div>
  <div class="cnt2 a-pop" style="--d:.8s;right:60px;top:170px;width:290px;height:290px"><b></b><span>NOCHES AL AÑO</span></div>
  <div class="stk k" style="--d:3.2s;--r:2deg;right:70px;top:490px;font-size:22px;letter-spacing:.06em">≈ 2.920 horas de descanso</div>
  <div class="stk" style="--d:3.8s;--r:-1deg;left:50px;top:820px;font-size:26px;font-weight:600;max-width:520px;line-height:1.35">Pocos regalos se usan tanto como <b style="color:var(--gold-lo)">el lugar donde duermes.</b></div>
</section>
<section class="slide fx cv-cam gr"><div class="silk"></div>{LOGO}
  <div class="stk" style="--d:.3s;--r:-2deg;left:60px;top:150px">Un Imperia</div>
  <div class="stk g" style="--d:.55s;--r:2deg;left:110px;top:232px"><em>para cada quien.</em></div>
  <div class="abs" style="left:60px;right:60px;top:380px;display:flex;flex-direction:column;gap:18px">
    <div class="prow" style="--d:.9s;--r:-.6deg"><div><div class="w">Para mamá y papá</div><div class="p">Premium Pillow top<small>Hasta queen y king</small></div></div><img src="assets/m7163.webp" alt=""></div>
    <div class="prow" style="--d:1.15s;--r:.5deg"><div><div class="w">Para quien cuida su espalda</div><div class="p">Therapy Pillow<small>Núcleo firme, capa envolvente</small></div></div><img src="assets/m7257.webp" alt="" style="filter:brightness(1.25)"></div>
    <div class="prow" style="--d:1.4s;--r:-.4deg"><div><div class="w">Para los jóvenes de la casa</div><div class="p">San Remo<small>Individual o matrimonial</small></div></div><img src="assets/m7213.webp" alt=""></div>
    <div class="prow" style="--d:1.65s;--r:.6deg"><div><div class="w">Para ti, por todo este año</div><div class="p">Premium Doble Pillow top<small>Suavidad por ambos lados</small></div></div><img src="assets/m7166.webp" alt=""></div>
  </div>
</section>
<section class="slide fx cv-cam">{ph('cam-s4')}{LOGO}
  <div class="stk" style="--d:.6s;--r:3deg;right:56px;top:170px;font-size:32px;max-width:440px;font-weight:600;line-height:1.25"><em style="font-size:1.25em">“Créeme: es el regalo que más se agradece.”</em></div>
  <div class="stk g" style="--d:1.3s;--r:-2deg;right:70px;top:400px;font-size:44px">Este año,<br><em>regala descanso.</em></div>
  <div class="stk" style="--d:2s;--r:0deg;left:40px;bottom:60px;padding:14px 20px">{storeline()}</div>
</section>''')

CAR['huespedes']=dict(title='Huéspedes Herrera',head='Este diciembre, la casa <em>se llena</em>.',desc='Con la familia Herrera. Estilo papelería de hotel: marco dorado, puertas que se abren, colgador de puerta y tarjeta de bienvenida.',
caption='Diciembre es de casa llena 🏡 Abuelos, tíos, primos… ¿ya está lista la habitación de huéspedes? Esta es la lista de Mariana ✨',
guion=['<b>Portada</b> <span>dos puertas se abren y revelan a la familia preparando el cuarto</span>','<b>La lista de Mariana</b> <span>colgador de puerta que se balancea con 4 puntos que se marcan</span>','<b>Que duerman como en casa</b> <span>Sofía y Andrés en el San Remo negro + versiones</span>','<b>La mejor bienvenida</b> <span>tarjeta de bienvenida tipo hotel + tiendas aliadas</span>'],
slides=f'''
<section class="slide fx cv-hue">{ph('hue-portada')}<div class="gt"></div><div class="frame2"></div>{LOGO}
  <div class="tt"><div class="kk a-fade" style="--d:1.2s">Temporada de visitas</div>
  <h2>{L('Este diciembre,',1.3)}{L('<em>la casa se llena.</em>',1.45)}</h2>
  <div class="sub a-up" style="--d:1.9s">¿Ya está lista la habitación de huéspedes?</div></div>
  <div class="doors"><i></i><i></i></div>
</section>
<section class="slide fx cv-hue">{ph('hue-s2')}<div class="frame2"></div>{LOGO}
  <div class="hanger" style="left:640px;top:96px;width:390px"><span class="kk">Antes de que lleguen</span><h3>La lista de <em>Mariana</em></h3>
    <div class="row3" style="--c:1.8s"><i>{CHECK}</i>Sábanas limpias y una manta extra</div>
    <div class="row3" style="--c:2.3s"><i>{CHECK}</i>Almohadas de repuesto</div>
    <div class="row3" style="--c:2.8s"><i>{CHECK}</i>Una lámpara junto a la cama</div>
    <div class="row3 hl" style="--c:3.4s"><i>{CHECK}</i>Un colchón cómodo de verdad</div></div>
</section>
<section class="slide fx cv-hue">{ph('hue-s3')}<div class="gt" style="height:460px"></div><div class="frame2"></div>{LOGO}
  <div class="tt" style="top:150px;right:auto;width:620px"><div class="kk a-fade" style="--d:.2s">Para la habitación de huéspedes</div>
  <h2 style="font-size:80px">{L('Que duerman',.3)}{L('<em>como en casa.</em>',.45)}</h2></div>
  <div class="abs" style="left:60px;top:1000px;display:flex;flex-direction:column;gap:10px;z-index:14">
    <span class="chip3 a-pop" style="--d:1.3s">San Remo</span><span class="chip3 a-pop" style="--d:1.5s">Individual y matrimonial</span></div>
</section>
<section class="slide fx cv-hue">{ph('hue-s4')}<div class="frame2"></div>{LOGO}
  <div class="card3 a-up" style="--d:.7s;right:60px;top:110px;width:430px"><span class="kk">Bienvenidos</span><h3>La mejor bienvenida <em>es una buena noche.</em></h3>
  <p>— Mariana y Andrés</p><div style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(201,170,92,.5);text-align:center">{storeline()}</div></div>
</section>''')

def pola(f,cap,stamp,rot,extra=''):
    return f'''<div class="pola" style="--r:{rot}"><div class="pic"><img src="{P}{f}.png" alt="" style="{extra}"><div class="leak"></div><span class="stamp">{stamp}</span></div><div class="cap"><p>{cap}</p></div></div>
  <div class="tape" style="left:90px;top:170px;transform:rotate(-32deg)"></div><div class="tape" style="right:90px;top:170px;transform:rotate(28deg)"></div>'''
LOGOV='<div class="lg a-fade" style="--d:1.2s"><img src="assets/logo-dark.png" alt="Colchones Imperia"></div>'
def vhead(k,t,d=.2): return f'<div class="head"><div class="kk a-fade" style="--d:{d}s">{k}</div><h2>{L(t,d+.1)}</h2></div>'
CAR['vacaciones']=dict(title='Vacaciones Herrera',head='Vacaciones en la <em>cama grande</em>.',desc='Con la familia Herrera. Estilo álbum familiar: polaroids que caen y se revelan, cinta adhesiva dorada, fecha en naranja retro.',
caption='Llegaron las vacaciones… y todos terminan en la cama grande 💛 Mañanas lentas, desayunos y cero alarmas. ¿En tu casa también pasa? ✨',
guion=['<b>Portada</b> <span>polaroid que cae y se revela: Sofía saltando en el Premium</span>','<b>Mañanas lentas</b> <span>desayuno en la cama, con destello de luz de película</span>','<b>Para que quepan todos</b> <span>los cuatro acostados, vistos desde arriba + Queen y King</span>','<b>Cierre</b> <span>la familia sobre el Premium + tiendas aliadas</span>'],
slides=f'''
<section class="slide fx cv-vac"><div class="paper"></div><div class="dots"></div>
  {vhead('Vacaciones de fin de año','Todos a la <em>cama grande.</em>')}
  {pola('vac-portada','Llegaron las vacaciones… y todos terminan aquí.','DIC 26','-1.4deg')}
  {LOGOV}
</section>
<section class="slide fx cv-vac"><div class="paper"></div><div class="dots"></div>
  {vhead('Diciembre en casa','Mañanas <em>lentas.</em>')}
  {pola('vac-s2','Cero alarmas. Desayuno en la cama.','DIC 27','1.2deg')}
  {LOGOV}
</section>
<section class="slide fx cv-vac"><div class="paper"></div><div class="dots"></div>
  {vhead('Premium Doble Pillow top','Para que <em>quepan todos.</em>')}
  {pola('vac-s3','Suavidad por ambos lados.<small><span class="chip4">QUEEN</span><span class="chip4">KING</span></small>','DIC 28','-1deg','object-position:50% 50%')}
  {LOGOV}
</section>
<section class="slide fx cv-vac"><div class="paper"></div><div class="dots"></div>
  {vhead('Para recordar','Que se queden <em>en la memoria.</em>')}
  {pola('vac-s4','Estas vacaciones… y la cama grande.<small>¡Llegamos a donde estés! En tiendas aliadas a nivel nacional.</small>','DIC 30','1.4deg')}
  {LOGOV}
</section>''')

for key,c in CAR.items():
    s=base
    s=s.replace('/* ============ PREVIEW PAGE ============ */', css+'\n/* ============ PREVIEW PAGE ============ */')
    s=re.sub(r'<template id="slides">.*?</template>',lambda m:'<template id="slides">'+c['slides']+'</template>',s,flags=re.S)
    s=re.sub(r'<title>.*?</title>',f'<title>{c["title"]}</title>',s)
    s=s.replace("fetch('export-nav-valeria/'+f)",f"fetch('export-fx-{key}/'+f)").replace("'imperia-valeria-'+f",f"'imperia-{key}-'+f")
    s=re.sub(r'<header>.*?</header>',lambda m:f'<header>\n    <h1>{c["head"]}</h1>\n    <p>Fiestas · {c["desc"]} 4 slides 1080×1350 (4:5).</p>\n  </header>',s,flags=re.S)
    s=re.sub(r'<div class="capt">.*?</div>',lambda m:f'<div class="capt"><b>colchonesimperia</b> {c["caption"]}</div>',s,flags=re.S)
    notes='\n'.join(f'          <li>{g}</li>' for g in c['guion'])
    s=re.sub(r'<h3>Guion de slides</h3>\s*<ol>.*?</ol>',lambda m:f'<h3>Guion de slides</h3>\n        <ol>\n{notes}\n        </ol>',s,flags=re.S)
    s=s.replace("      // stars\n","""      s.querySelectorAll('.dots').forEach(box=>{ const r=rng(77+i*13); for(let k=0;k<22;k++){ const d=document.createElement('i'); const x=r()*1080, y=r()*1350; if(y>150&&y<1320&&x>80&&x<1000) continue; d.style.left=x+'px'; d.style.top=y+'px'; d.style.setProperty('--s',(4+r()*9).toFixed(0)+'px'); box.appendChild(d);} });
      // stars\n""",1)
    assert s.count('<section class="slide')==4, key
    open(f'fx-{key}.html','w').write(s)
print('ok')
