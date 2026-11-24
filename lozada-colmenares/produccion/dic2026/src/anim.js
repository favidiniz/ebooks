// Animación de slides de carrusel (sin dependencias).
// - Slide 1 de cada carrusel = PORTADA: todo visible desde el cuadro 0 (es la miniatura del feed),
//   solo movimiento ambiental (flotar, girar, pulsar).
// - Slides 2-4: entrada escalonada (subir + aparecer), barras que crecen, números que cuentan,
//   y luego movimiento ambiental.
// - RIF, fuente, logo y contador siempre visibles.
(function(){
  const FIXED = '.foot,.logo,.count,.tag';
  const ROWS = '.row,.rowr,.track,.chk,.brow,.cnt,.chip';
  const NUM = /^([+≈]?)(\d{1,3}(?:[.,]\d+)?)(\s?(?:%|M|mil)?)$/;
  const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)), lin=(t,a,b)=>cl((t-a)/(b-a)), eo=x=>1-Math.pow(1-x,3);
  const eob=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
  const state=new Map();

  function setup(slide, isCover){
    const units=[], nums=[], bars=[], floats=[];
    const top=el=>el.getBoundingClientRect().top;
    const kids=[...slide.children].filter(e=>!e.matches(FIXED) && e.tagName!=='SCRIPT');
    kids.sort((a,b)=>top(a)-top(b));
    kids.forEach(k=>{
      const sub=[...k.querySelectorAll(ROWS)];
      units.push({el:k, kind: k.matches('svg,.blob,.bokeh')||k.querySelector('svg')&&!k.textContent.trim()?'pop':'up'});
      sub.forEach(s=>units.push({el:s, kind:'left', parent:k}));
    });
    // números que cuentan
    slide.querySelectorAll('*').forEach(e=>{
      if(e.closest(FIXED)) return;
      if([...e.childNodes].some(n=>n.nodeType===1)) return;
      const tx=e.textContent.trim(); const m=tx.match(NUM);
      if(m && e.closest('.datum')==null){ nums.push({el:e,pre:m[1],val:parseFloat(m[2].replace('.','').replace(',','.')),dec:(m[2].split(/[.,]/)[1]||'').length,sep:m[2].includes(',')?',':'.',suf:m[3],orig:tx, thousands:/^\d{1,3}\.\d{3}$/.test(m[2])}); }
    });
    slide.querySelectorAll('.bar,.brow .b').forEach(b=>bars.push(b));
    slide.querySelectorAll(':scope > svg, :scope > .blob, :scope > .bokeh').forEach((f,i)=>floats.push({el:f,ph:i*1.7}));
    // orden de aparición
    let d=.15; const delay=new Map();
    units.forEach(u=>{ if(u.parent){ const pd=delay.get(u.parent)||d; const n=(u.parent._n=(u.parent._n||0)+1); delay.set(u.el,pd+.25+n*.18);} else { delay.set(u.el,d); d+=.22; } });
    units.forEach(u=>{u.d=delay.get(u.el); u.base=parseFloat(getComputedStyle(u.el).opacity)||1;});
    nums.forEach(n=>{ let p=n.el; let dd=0; while(p&&p!==slide){ if(delay.has(p)){dd=Math.max(dd,delay.get(p));} p=p.parentElement||p.parentNode; } n.d=dd; });
    bars.forEach(b=>{ let p=b; let dd=.3; while(p&&p!==slide){ if(delay.has(p)){dd=Math.max(dd,delay.get(p));} p=p.parentElement; } b._d=dd+.15; b.style.transformOrigin='left center'; });
    state.set(slide,{units,nums,bars,floats,isCover});
  }

  function fmt(n,v){
    let s = n.dec? v.toFixed(n.dec) : String(Math.round(v));
    if(n.dec) s=s.replace('.',n.sep);
    if(n.thousands){ s=Math.round(v).toLocaleString('es-ES'); }
    return n.pre+s+n.suf;
  }

  window.animSlide=function(slide,t){
    const isCover = slide.dataset.name.endsWith('_1');
    if(!state.has(slide)) setup(slide,isCover);
    const S=state.get(slide);
    // ambiente: todo flota suavemente
    S.floats.forEach(f=>{ const y=Math.sin(t*Math.PI*2/4.5+f.ph)*9, r=Math.sin(t*Math.PI*2/6+f.ph)*1.2;
      f.el.style.translate=`0 ${y.toFixed(2)}px`; f.el.style.rotate=`${r.toFixed(2)}deg`; });
    if(S.isCover){ // portada: completa desde el cuadro 0
      S.units.forEach(u=>{ if(!S.floats.find(f=>f.el===u.el)){u.el.style.opacity=u.base;} });
      // movimiento ambiental de portada (parte de su estado final, nunca de vacío)
      slide.querySelectorAll(':scope > *').forEach((e,i)=>{
        if(e.matches(FIXED)||S.floats.find(f=>f.el===e)) return;
        const fs=parseFloat(getComputedStyle(e).fontSize);
        if(fs>=150){ const s=1+.025*Math.sin(t*Math.PI*2/3); e.style.transformOrigin='left center'; e.style.scale=s.toFixed(4); }
        else if(e.matches('.hand')){ e.style.rotate=`${(Math.sin(t*Math.PI*2/2.5)*1.5).toFixed(2)}deg`; }
        else if(e.matches('.pill,.datum')){ e.style.scale=(1+.02*Math.sin(t*Math.PI*2/2)).toFixed(4); }
      });
      S.floats.forEach(f=>{ const y=Math.sin(t*Math.PI*2/3+f.ph)*16, r=Math.sin(t*Math.PI*2/4+f.ph)*2.5;
        f.el.style.translate=`0 ${y.toFixed(2)}px`; f.el.style.rotate=`${r.toFixed(2)}deg`; });
      return;
    }
    S.units.forEach(u=>{
      const p=eo(lin(t,u.d,u.d+.7));
      u.el.style.opacity=(u.base*p).toFixed(3);
      const fl=S.floats.find(f=>f.el===u.el);
      if(u.kind==='up'){ u.el.style.translate=`0 ${(1-p)*46}px`; }
      else if(u.kind==='left'){ u.el.style.translate=`${(1-p)*-40}px 0`; }
      else { const q=eob(lin(t,u.d,u.d+.8)); u.el.style.scale=`${(.6+.4*q).toFixed(3)}`; if(fl){ const y=Math.sin(t*Math.PI*2/4.5+fl.ph)*9; u.el.style.translate=`0 ${y.toFixed(2)}px`; } }
    });
    S.bars.forEach(b=>{ const p=eo(lin(t,b._d,b._d+1.0)); b.style.scale=`${p.toFixed(3)} 1`; });
    S.nums.forEach(n=>{ const p=eo(lin(t,n.d+.05,n.d+1.3)); n.el.textContent = p>=1? n.orig : fmt(n,n.val*p); });
  };
})();
