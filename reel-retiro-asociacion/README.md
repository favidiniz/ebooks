# Reel · Retiro de Asociación · Regnum Christi (21.11.2026)

- `reel_retiro_asociacion_RC_v2.mp4`: 1080×1920, 30 fps, 58,9 s, H.264, sin audio. Tarjetas animadas, notas a mano con flechas, polaroids, cortinillas vinotinto/dorado y cierre con escudo + logo animados.
- `render2.py`: script de la v2 (usa `assets/escudo.png` y `assets/logo.png`). `render.py` es la v1.
- `render.py`: lista de planos (SHOTS), textos (MOMENTS) y animaciones; vuelve a exportar con
  `python3 render.py video salida.mp4` (espera los clips en `../dl/clips`, las fuentes en `../fonts`).
- Escudo: coloca `assets/escudo.png` (PNG transparente) junto a la carpeta base y vuelve a renderizar; aparece en el cierre.
- Fuentes: Tenor Sans, EB Garamond, Montserrat y Caveat (notas a mano) (Google Fonts, licencia OFL).
