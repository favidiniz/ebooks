# Kit de contexto · Colchones Imperia

> Para quien retome este trabajo (persona o IA): este documento reúne **todo** lo aprendido y acordado con la clienta en el chat anterior. Léelo completo antes de proponer o diseñar nada. Si algo aquí contradice tu criterio, gana este documento.
>
> Repositorio: `favidiniz/ebooks`, rama `claude/charming-keller-6fcx4e`, carpeta `carrusel-imperia/`.
> Idioma de trabajo: **español (Venezuela), tuteo**. Respuestas cortas, claras y en tono cercano.

---

## 1. La marca

- **Nombre:** Colchones Imperia.
- **RIF:** **J-50441309-6** (va en la portada de TODOS los posts).
- **Instagram:** @colchonesimperia · ubicación que usan: “Zona Industrial 3”.
- **País:** Venezuela (las etiquetas dicen “Elaborado en la República Bolivariana de Venezuela”).
- **Cómo se vende:** **NO hay entrega a domicilio.** Imperia **distribuye a tiendas aliadas a nivel nacional**. La gente compra en esas tiendas.
  - Frase de cierre oficial: **“¡Llegamos a donde estés! En tiendas aliadas a nivel nacional.”** con ícono de tienda (nunca camión).
- **Su post con más interacción** fue uno sobre su distribución/“llegamos a donde estés”.
- **Sus posts anteriores** (referencia de tono): carruseles con imágenes generadas por IA, frases repartidas en varios slides (“Cuando la vida te da señales claras… solo queda… prestarles atención”), datos de sueño, logo dorado en todos los slides, descripciones cortas con emoji.

### Fuentes de material
- Drive con fotos profesionales y videos: https://drive.google.com/drive/folders/1LxSZLIgcep41kZcXAKtC9huX_3nIDcGd
  - `Fotos/`: 24 fotos de estudio PNG con fondo transparente (DSC_7163 … DSC_7276).
  - `Videos/`: “Colchones Negros.mp4”, “Premium.mp4”.
- Drive con referencias/catálogos: https://drive.google.com/drive/folders/1navkPF90-gZTNFxKOnhDkhD3cC55vBkr (Catálogo IMPERIA 2026). Copia en `contexto/referencias/Catalogo-Imperia-2026.pdf`.
- Los Drive son públicos: se descargan con `https://drive.usercontent.google.com/download?id=ID&export=download&confirm=t` y se listan con `https://drive.google.com/embeddedfolderview?id=ID`.

---

## 2. Productos (según catálogo 2026)

| Línea | Modelo | Descripción oficial (resumen) | Medidas |
|---|---|---|---|
| San Remo | **San Remo** | Superficie acolchada y soporte firme para un sueño reparador. *Confort.* | Individual, matrimonial |
| San Remo | **San Remo Pillow top** | Equilibrio perfecto entre suavidad y firmeza; capa superior acolchada envolvente. *Suavidad y soporte extra.* | Individual, matrimonial |
| San Remo | **San Remo Doble Pillow top** | Capas acolchadas en ambos lados. *Lujo en cada lado.* | Individual, matrimonial |
| Rebond | **Therapy Pillow** (ortopédico) | Beneficios terapéuticos; capa tipo pillow envolvente y núcleo firme que favorece la alineación de la columna. *Bienestar y confort en un solo colchón.* | Individual, matrimonial |
| Premium | **Premium** | Para los gustos más exigentes; acabados artesanales e ingeniería de soporte superior. *El estándar de confort que tu estilo de vida merece.* | Individual, matrimonial |
| Premium | **Premium Pillow top** | Cubierta superior de alta gama, acogida envolvente, sensación de ingravidez. *Suite de cinco estrellas.* | Individual, matrimonial, queen, king |
| Premium | **Premium Doble Pillow top** | Doble capa de acolchado premium en ambas caras, “sensación de nube bidireccional”, maximiza la vida útil. *Una experiencia de lujo total y descanso sin fronteras.* | Individual, matrimonial, queen, king |

Todos son **ortopédicos**. El catálogo no trae medidas en cm (dice “0 x 0 cm”): **no inventes centímetros ni precios**.

**Garantía:** la clienta confirmó **10 años de garantía** (línea Premium; su etiqueta dice “Años de garantía”). La etiqueta real del **San Remo** dice **6 años**. Si un post habla de garantía sin aclarar la línea, confirmar con la clienta.

### Fotos de estudio → modelo (identificación por forma/color; confirmar con la clienta si hay duda)
- **DSC_7166**: Premium Doble Pillow top (gris, grueso, pillow top doble).
- **DSC_7163**: Premium Pillow top (gris, más delgado). **DSC_7168**: primer plano Premium con etiqueta.
- **DSC_7213** (blanco grueso) y **DSC_7276 / DSC_7188** (negro grueso): San Remo Doble Pillow top.
- **DSC_7201 / DSC_7215** (blancos) y **DSC_7266** (negro): San Remo Pillow top.
- **DSC_7234** (negro plano) y **DSC_7183**: San Remo clásico.
- **DSC_7257**: Therapy Pillow (negro, etiqueta azulada).
- Versiones web ya recortadas (sin fondo, sin hilos de estudio): `carrusel-imperia/assets/mXXXX.webp`.

### Etiquetas reales (la IA SIEMPRE las inventa; hay que reemplazarlas)
- **Premium:** etiqueta negra, “IMPERIA” en dorado, “Premium” en cursiva, corona y “Años de garantía” (**10 años**). Tela lateral gris con malla blanca en rombos y costura en hexágonos, ribete negro.
- **San Remo:** etiqueta plateada/blanca, logo con corona “COLCHONES IMPERIA”, franja dorada “SAN REMO”, “6 años de garantía · Ortopédico · Resortes / Pillow”.
- Recortes reales listos: `contexto/referencias/etiquetas-reales/premium.png` y `san-remo.png`.

---

## 3. Identidad visual

### Colores (ÚNICOS permitidos en lo que diseñamos)
| Token | Hex | Uso |
|---|---|---|
| Negro | `#0C0B09` (y `#14120D`, `#1A160F`) | Fondos oscuros |
| Dorado | `#C9AA5C` | Acento principal, marcos, íconos |
| Dorado claro | `#EBD7A0` | Brillos, cursivas sobre negro |
| Dorado oscuro | `#8F7030` | Cursivas y etiquetas sobre crema |
| Marfil / crema | `#F5F2EB`, `#FBF8F1`, `#FFFCF6` | Fondos claros, tarjetas |
| Texto oscuro | `#1A1712`, `#3A342B` | Texto sobre crema |

**PROHIBIDO:** rojo, verde navideño, azul marino (aunque sea Navidad). Los únicos rojos aceptables son los que ya vienen dentro de una foto (pijamas, lazos).

### Tipografía
- **Títulos:** Cormorant Garamond (500), con la palabra clave en **cursiva dorada**.
- **Texto, etiquetas, botones:** Montserrat (500–800); etiquetas pequeñas en mayúsculas con letter-spacing amplio.
- El catálogo original usa Neue Montreal, Montserrat y Glacial Indifference; nosotros mantenemos Cormorant + Montserrat.

### Logo
- Corona + “COLCHONES IMPERIA”. Archivos: `assets/logo.png` (dorado, para fondos oscuros) y `assets/logo-dark.png` (dorado oscuro, para fondos claros). Sobre fotos con fondo variado va dentro de una **pastilla crema** con sombra.
- Fondo de seda blanca del catálogo: `assets/silk.webp`.

---

## 4. Reglas y preferencias de la clienta (TODAS obligatorias)

### Proceso
1. **Proponer temas primero** y esperar su visto bueno antes de diseñar (salvo que ella diga “hazlos de los temas que consideres”).
2. Si falta una foto, **intercalar un gráfico** en su lugar (no le pidas que genere más).
3. Entregar siempre un **ZIP** listo para descargar (MP4 + PNG por slide, ordenado por carpetas).
4. Ella **no quiere pagar** APIs de imágenes. Las fotos las genera ella en la **app de Gemini** (gratis) con los prompts que le damos.

### Formato
- **Carruseles:** máximo **4 slides**, 1080×1350 (4:5), cada slide en **MP4 animado de 7 s a 30 fps** + PNG.
- **Story sets:** 4 historias 1080×1920 (9:16); dejar libres los ~250 px de arriba y de abajo; dejar espacio vacío donde irá el sticker (encuesta, pregunta, cuestionario, deslizador, cuenta regresiva) y decirle en cuál historia va cada sticker.
- **Sin números de slide.**
- **Sin llamados a la acción con palabra clave** (nada de “escríbenos TRONO por DM”). Cierres de marca: “Descansa como realeza.”, “Tu trono te espera.”, etc.
- **Logo en TODOS los slides**, siempre en la **misma posición dentro de un mismo carrusel/set** (puede cambiar entre carruseles).
- **RIF en la portada** de cada carrusel/set, pegado al logo, letra pequeña.
- **El primer fotograma de la portada debe estar completo** (foto + título + logo + RIF): es lo que queda en el feed. Nunca un fondo blanco/vacío que luego se anima. (Técnica: renderizar la portada con un desfase, `OFF=4.2`.)
- Portadas **no demasiado oscuras** cuando se pide contraste con posts oscuros anteriores.

### Estilo
- **Cada carrusel con su propio estilo** (no repetitivo), pero **sin perder la línea gráfica de Imperia**. Ejemplos usados: revista editorial, stickers de regalo, papelería de hotel, álbum de polaroids, tarjeta con marco dorado, lista en cuaderno, cine (tira de película + marquesina), cuento nocturno.
- **Nada infantil:** sin dibujos (bastones de caramelo, esferas dibujadas, luces de colores, estrellas fugaces). Decoración permitida: nieve/destellos dorados y blancos, marcos dorados finos, cintas doradas, tipografía.
- **Protagonismo de los colchones.** Solo colchones **Imperia reales**; **nunca genéricos**. En fotos con personas, el colchón debe verse con su etiqueta.
- **En story sets: un solo colchón/línea por set** (no mezclar San Remo con Premium en el mismo set).
- **NUNCA tapar las caras de los modelos** con textos, recuadros o degradados. Revisar cada slide.
- **Ninguna foto debe perder calidad** (no recortar caras, no agrandar de más; usar fotos en su resolución original).
- Fotos de personas = **estilo foto de usuario** (UGC, tomada con celular, natural, gente USANDO el colchón: acostada, sentada, tendiendo la cama), a pantalla completa o en tarjeta.
- **Habitaciones distintas en cada carrusel**; dentro de un carrusel, mismo cuarto, colchón y outfit; entre carruseles, todo cambia.

### Temporadas
- **15 nov – 15 dic:** ambiente de fiestas, **sin decir “Feliz Navidad”** ni nombrar fechas.
- **15 – 31 dic:** **bien navideño** con decoración (pero en la paleta Imperia), **sin “Feliz Navidad” ni “Feliz año nuevo”**. Los días especiales los hará ella aparte.

### Correcciones de imagen (siempre)
- Reemplazar la **etiqueta inventada** por la real (perspectiva, luz y color igualados).
- Corregir la **textura del lateral** cuando la IA la cambia (Premium: malla en rombos + hexágonos).
- Herramientas en `contexto/herramientas/` (ver sección 8).

---

## 5. Modelos oficiales de la marca (personajes ficticios)

Son **personajes ficticios** creados para Imperia (no personas reales). Rasgos fijos; **la ropa sí puede cambiar** por campaña. Hojas de casting en `carrusel-imperia/assets/casting/` y en la página de casting: https://claude.ai/artifact/4Zdkkd2AKkMrT5KD7XLAac

| Personaje | Rasgos fijos | Uso |
|---|---|---|
| **Valeria**, 27 | Latina, piel trigueña clara, ojos marrón oscuro, pecas suaves, cabello castaño oscuro largo y liso con raya al medio, collar dorado fino, look natural | Descanso, bienestar, rutinas |
| **Camila**, 32 | Latina, piel bronceada, ojos miel, sonrisa amplia, cabello ondulado a media espalda con reflejos miel, argollas doradas | Recomendaciones tipo amiga, testimonios, selfies |
| **Familia Herrera** | **Mariana** (34, piel clara, moño bajo), **Andrés** (36, piel trigueña, cabello oscuro ondulado, barba corta, reloj plateado), **Sofía** (6, cabello castaño liso con flequillo), **Lucía** (bebé, lazo blanco) | Familia, Premium/Doble Pillow top, visitas, vacaciones |

Archivos: `valeria-pola.jpg`, `camila-pola.jpg`, `herrera-pola.jpg` (hojas completas) + recortes (`valeria-frente.jpg`, `mariana.jpg`, `andres.jpg`, `sofia.jpg`, `lucia.jpg`, etc.).

La clienta también aceptaría fotos suyas o de una amiga **con consentimiento por escrito**. Nunca usar caras de personas reales sin permiso.

---

## 6. Cómo se generan las fotos (flujo que funciona)

- Yo (la IA) **no puedo generar imágenes** en esta sesión: el conector de Higgsfield solo lee (plan gratis, 10 créditos) y la API de Gemini requiere facturación (la clienta **no quiere pagar**). Se borró/no se usa.
- **Flujo:** preparar un **kit ZIP** con una carpeta por foto: `imagen-1-casting-….jpg` (cara) + `imagen-2-colchon-….jpg` (foto real del colchón) + `prompt.txt`. Ella lo pasa a Gemini.
  - Forma más cómoda: **un chat de Gemini por carrusel**: primer mensaje largo con habitación + colchón + outfit + estilo + FOTO 1; luego mensajes cortos “Misma habitación, colchón y outfit. FOTO 2: …”.
- Estructura de cada prompt: caras exactas de la imagen 1 + colchón exacto de la imagen 2 · ESCENA · HABITACIÓN (detallada) · COLCHÓN (modelo y descripción) · OUTFIT · estilo “foto de usuario realista tomada con celular, luz cálida… etiqueta del lateral visible de frente y sin nada que la tape, sin textos agregados, vertical 4:5 con espacio arriba para un título”.
- Gemini entrega 1122×1402 aprox.; a veces 928×1152 (más pequeñas, avisar).

---

## 7. Lo que ya está hecho (no repetir temas)

**Carruseles gráficos (4 slides):** “Tu cama es tu trono” (también versión 9 slides), “Cuidados del colchón / ¿Y tú, lo cuidas a él?”, “Tu próximo colchón está a 3 pasos”, “El descanso empieza antes de cerrar los ojos”, y 4 de fiestas v1 (gráficos con polas).
**Carruseles con fotos (antes del 15 dic):** Valeria “Diciembre también se descansa”, Camila “El regalo que se usa 365 noches”, Herrera “La casa se llena”, Herrera “Vacaciones en la cama grande”.
**Carruseles navideños (15–31 dic):** Valeria “La noche antes de las visitas” (San Remo negro), Camila “Mi lista de diciembre” (Premium Pillow top), Herrera “Función navideña en la cama grande” (Premium Doble Pillow top king), Herrera “Esperando a Santa” (San Remo blanco).
**Story sets (15 nov–15 dic), uno por colchón:** Therapy Pillow, San Remo Pillow top, San Remo, Valeria + Premium Pillow top, Camila + Premium Doble Pillow top, Herrera + San Remo Doble Pillow top.

Todo exportado en `carrusel-imperia/export-*/` y ZIPs en `carrusel-imperia/descargas/` (los ZIP no se suben a git).

### Descripciones (captions)
Cortas, cálidas, con 1–3 emojis, sin palabra clave; cierre con tiendas aliadas. Ej.: “Tu colchón te cuida todas las noches… ¿y tú a él? 🛏️✨ … Encuéntralo en tiendas aliadas de todo el país 📍”.

---

## 8. Cómo se construye técnicamente

- Cada carrusel es un HTML en `carrusel-imperia/` (`xm-*.html`, `fx-*.html`, `st-*.html`…) con slides de 1080×1350 (o 1920 para stories) y animaciones CSS.
- **Render a video:** `contexto/herramientas/render.js` (Playwright, ya instalado en el entorno) toma cada fotograma y `ffmpeg` arma el MP4:
  ```
  PAGE=xm-camila.html H=1350 OFF=0 node render.js <indiceSlide> <carpetaFrames>
  ffmpeg -framerate 30 -i carpeta/f%04d.jpg -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -movflags +faststart slide-01.mp4
  ```
  Para la portada usar `OFF=4.2` (primer fotograma completo). `H=1920` para stories. `snap.js` saca capturas sueltas para revisar.
- **Generadores:** `mk7.py` (navideños), `mk8.py`/`mk9.py` (stories), `mk6.py` (fiestas con fotos). Ojo: las rutas absolutas apuntan a `/home/user/ebooks/carrusel-imperia/` y a una carpeta temporal; ajustarlas.
- **Etiquetas:** `detect2.py` (ubicar etiqueta falsa) + `composite2.py` (pegar la real con perspectiva y color). Si la detección falla, marcar esquinas a mano con `grid2.py`.
- **Textura Premium:** `texture.py` (transfiere la tela real de DSC_7166 al lateral).
- **Kit de prompts:** `kit2.py`.
- Las páginas se publican como Artifacts privados (claude.ai) con botones de descarga.

### Publicar en Instagram
Se recomendó conectar **Buffer** (conector de claude.ai) con @colchonesimperia como cuenta profesional; **aún no está configurado**. No publicar nada sin su aprobación.

---

## 9. Checklist antes de entregar cualquier pieza

- [ ] ¿Máx. 4 slides / 4 historias? ¿Sin números de slide?
- [ ] ¿Logo en todos, misma posición? ¿RIF en la portada?
- [ ] ¿Primer fotograma de la portada completo?
- [ ] ¿Solo negro/dorado/crema/blanco? ¿Nada de rojo, verde ni azul marino? ¿Sin dibujos infantiles?
- [ ] ¿Ninguna cara tapada?
- [ ] ¿Solo colchones Imperia, con etiqueta real y textura correcta?
- [ ] ¿Un solo colchón por story set?
- [ ] ¿Sin palabra clave por DM? ¿Cierre con “En tiendas aliadas a nivel nacional”? ¿Nada de entrega a domicilio?
- [ ] ¿Sin “Feliz Navidad / Año nuevo”? ¿Tono de temporada correcto según fecha?
- [ ] ¿Fotos sin pérdida de calidad?
- [ ] ¿ZIP entregado con MP4 + PNG ordenados?
