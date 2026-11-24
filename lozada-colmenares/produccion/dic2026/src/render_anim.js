// Uso: node render_anim.js c1_economia.html [...]  [--stills]
// Exporta cada .slide como MP4 animado 1080x1440, 30 fps, 6 s → ../out/video/<nombre>.mp4
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');const {execSync}=require('child_process');
const FPS=30, DUR=6;
(async()=>{
  const args=process.argv.slice(2), stills=args.includes('--stills');
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:1600},deviceScaleFactor:1});
  const outDir=path.resolve(__dirname,'../out/video');fs.mkdirSync(outDir,{recursive:true});
  for(const f of args.filter(a=>!a.startsWith('--'))){
    await p.goto('file://'+path.resolve(__dirname,f));
    await p.addScriptTag({path:path.resolve(__dirname,'anim.js')});
    await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
    const slides=await p.$$('.slide');
    for(let i=0;i<slides.length;i++){
      const s=slides[i]; const name=await s.getAttribute('data-name');
      await s.scrollIntoViewIfNeeded();
      if(stills){ for(const t of [0,0.6,1.5,6]){ await p.evaluate(([i,t])=>animSlide(document.querySelectorAll('.slide')[i],t),[i,t]);
        await s.screenshot({path:path.join(outDir,`_still_${name}_${t}.jpg`),type:'jpeg',quality:80}); } continue; }
      const dir=path.join(outDir,'_frames_'+name);fs.rmSync(dir,{recursive:true,force:true});fs.mkdirSync(dir);
      for(let fr=0;fr<FPS*DUR;fr++){ await p.evaluate(([i,t])=>animSlide(document.querySelectorAll('.slide')[i],t),[i,fr/FPS]);
        await s.screenshot({path:`${dir}/${String(fr).padStart(4,'0')}.jpg`,type:'jpeg',quality:93}); }
      execSync(`ffmpeg -y -loglevel error -framerate ${FPS} -i "${dir}/%04d.jpg" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart "${path.join(outDir,name+'.mp4')}"`);
      fs.rmSync(dir,{recursive:true,force:true}); console.log('ok',name);
    }
  }
  await b.close();
})();
