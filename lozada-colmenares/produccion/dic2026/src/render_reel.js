// Uso: node render_reel.js [--stills t1,t2,...]  → ../out/reel_frames/*.jpg y ../out/Reel_12_uvas_12_planes.mp4 (1080x1920, 30 fps)
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');const {execSync}=require('child_process');
(async()=>{
  const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(__dirname,'reel_12uvas.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
  const v=await p.$('#v');
  const si=process.argv.indexOf('--stills');
  if(si>0){for(const t of process.argv[si+1].split(',')){await p.evaluate(t=>render(+t),t);await v.screenshot({path:path.resolve(__dirname,`../out/_still_${t}.jpg`),type:'jpeg',quality:85});}await b.close();return;}
  const dir=path.resolve(__dirname,'../out/reel_frames');fs.rmSync(dir,{recursive:true,force:true});fs.mkdirSync(dir,{recursive:true});
  const FPS=30,DUR=25;
  for(let f=0;f<FPS*DUR;f++){await p.evaluate(t=>render(t),f/FPS);await v.screenshot({path:`${dir}/${String(f).padStart(4,'0')}.jpg`,type:'jpeg',quality:93});}
  await b.close();
  execSync(`ffmpeg -y -loglevel error -framerate ${FPS} -i "${dir}/%04d.jpg" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart "${path.resolve(__dirname,'../out/Reel_12_uvas_12_planes.mp4')}"`);
  fs.rmSync(dir,{recursive:true,force:true});console.log('mp4 ok');
})();
