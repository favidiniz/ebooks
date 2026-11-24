# LC&A · Producción diciembre 2026

Piezas finales en `out/`. **Para publicar, usar los videos animados de `out/video/`** (cada slide es un MP4). Los PNG quedan como respaldo estático.

| Archivo | Formato |
|---|---|
| `C1_economia_2027_1-4.png` | Carrusel 1080×1440 |
| `C2_los_que_vuelven_1-4.png` | Carrusel 1080×1440 |
| `C3_diciembre_en_la_via_1-4.png` | Carrusel 1080×1440 |
| `C4_poliza_con_hallacas_1-4.png` | Carrusel 1080×1440 |
| `C5_tu_resumen_2026_1-4.png` | Carrusel 1080×1440 |
| `Reel_12_uvas_12_planes.mp4` | Reel 1080×1920, 30 fps, 25 s, **sin audio**: agregar la música en IG o CapCut (instrumental venezolano suave, con toque de gaita) |
| `video/C*_N.mp4` | **Cada slide animada**: 1080×1440, 30 fps, 6 s. La **slide 1 (portada) está completa desde el primer cuadro** (es la miniatura del feed) y solo tiene movimiento ambiental. Las slides 2-4 entran por partes: los números cuentan y las barras crecen. |
| `_vista_general_carruseles.jpg` | Vista de todas las slides juntas |

Todas las slides llevan el RIF **J-30215603-3** y la fuente del dato en el pie. En el reel, el RIF va fijo durante todo el video y la fuente aparece mientras se muestra el dato.

## Notas de producción
- **Tipografía:** Jost (Google Fonts), la alternativa libre más cercana a Futura. Si se rehacen en Canva o Illustrator con Futura LT Pro (Book y Heavy), la jerarquía se mantiene igual.
- **Ilustraciones:** vectoriales, hechas a medida (no son stock), con la paleta de la marca.
- **Logo:** la reconstrucción vectorial de `../../logo/`.

## Editar y volver a exportar
Las piezas son HTML en `src/`. Para cambiar un texto, edita el `.html` y luego:

```bash
cd src
node render.js c1_economia.html c2_vuelven.html c3_via.html c4_hallacas.html c5_resumen.html
node render_anim.js c1_economia.html c2_vuelven.html c3_via.html c4_hallacas.html c5_resumen.html   # slides animadas (≈1 min por slide)
node render_anim.js c1_economia.html --stills   # capturas en t=0 / 0,6 / 1,5 / 6 s para revisar
node render_reel.js            # reel completo (≈2 min)
node render_reel.js --stills 2,8,18   # capturas sueltas para revisar
```

Requiere Node con Playwright y ffmpeg.
