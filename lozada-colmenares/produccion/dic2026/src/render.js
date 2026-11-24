// Uso: node render.js c1.html [c2.html ...]  → exporta cada .slide a ../out/<nombre>_<n>.png (1080x1440)
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport: {width: 1200, height: 1600}, deviceScaleFactor: 1});
  for (const f of process.argv.slice(2)) {
    await page.goto('file://' + path.resolve(__dirname, f));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const slides = await page.$$('.slide');
    for (let i = 0; i < slides.length; i++) {
      const name = slides[i];
      const id = await name.getAttribute('data-name');
      const out = path.resolve(__dirname, '../out', `${id}.png`);
      await name.screenshot({path: out});
      console.log('ok', out);
    }
  }
  await browser.close();
})();
