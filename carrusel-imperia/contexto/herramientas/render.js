// usage: node render.js <slideIndex> <framesDir> [seconds] [fps]
const { chromium } = require('playwright');
(async () => {
  const i = +process.argv[2], out = process.argv[3];
  const secs = +(process.argv[4] || 7), fps = +(process.argv[5] || 30);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: +(process.env.H || 1350) } });
  await p.goto(`file:///home/user/ebooks/carrusel-imperia/${process.env.PAGE || "index.html"}?render=${i}`);
  await p.evaluate(() => window.__ready); await p.evaluate(() => window.__seek(0.5)); await p.screenshot({ type: "jpeg" }); await p.waitForTimeout(150);
  const seek = t => p.evaluate(t => new Promise(r => { window.__seek(t); requestAnimationFrame(() => requestAnimationFrame(() => { window.__seek(t); requestAnimationFrame(r); })); }), t);
  const n = Math.round(secs * fps);
  for (let f = 0; f < n; f++) {
    await seek(f / fps + (+(process.env.OFF || 0)));
    await p.screenshot({ path: `${out}/f${String(f).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 98 });
  }
  await seek(6.8);
  await p.screenshot({ path: `${out}/still.png`, type: 'png' });
  await b.close();
})();
