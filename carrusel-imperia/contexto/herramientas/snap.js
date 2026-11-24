const { chromium } = require('playwright');
(async () => {
  const out = process.argv[2];
  const times = process.argv[3].split(',').map(Number);
  const only = process.argv[4] ? process.argv[4].split(',').map(Number) : [0,1,2,3,4,5,6,7,8];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: +(process.env.H || 1350) } });
  for (const i of only) {
    await p.goto(`file:///home/user/ebooks/carrusel-imperia/${process.env.PAGE || "index.html"}?render=${i}`);
    await p.evaluate(() => window.__ready); await p.evaluate(() => window.__seek(0.5)); await p.screenshot({ type: "jpeg" }); await p.waitForTimeout(150);
    for (const t of times) {
      await p.evaluate(t => new Promise(r => { window.__seek(t); requestAnimationFrame(() => requestAnimationFrame(() => { window.__seek(t); requestAnimationFrame(r); })); }), t);
      await p.screenshot({ path: `${out}/s${i}_${t}.jpg`, type: 'jpeg', quality: 80 });
    }
  }
  await b.close();
})();
