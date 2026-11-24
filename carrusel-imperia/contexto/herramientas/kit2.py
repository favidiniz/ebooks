import os, shutil
S='/tmp/claude-0/-home-user-ebooks/578aafb8-e622-52a6-8fca-47556ff481b3/scratchpad'
K=S+'/kit2/Kit-Fotos-Imperia-Navidad'
shutil.rmtree(S+'/kit2',ignore_errors=True); os.makedirs(K+'/_referencias')
CAST='/home/user/ebooks/carrusel-imperia/assets/casting/'
cast={'valeria':CAST+'valeria-pola.jpg','camila':CAST+'camila-pola.jpg','herrera':CAST+'herrera-pola.jpg'}
mat={m:S+f'/drive/small/DSC_{m}.jpg' for m in ['7166','7163','7213','7276']}
mname={'7166':'Premium-Doble-Pillow-top-gris','7163':'Premium-Pillow-top-gris','7213':'San-Remo-blanco','7276':'San-Remo-negro'}
for k,v in cast.items(): shutil.copy(v,f'{K}/_referencias/casting-{k}.jpg')
for k,v in mat.items(): shutil.copy(v,f'{K}/_referencias/colchon-{mname[k]}-DSC_{k}.jpg')

COMMON=("Foto de usuario realista tomada con celular, momento natural y espontáneo, luz cálida, ambiente MUY navideño. "
 "La etiqueta del lateral del colchón debe verse de frente, nítida y sin nada que la tape. "
 "No agregues texto, letras ni marcas en la foto (salvo la etiqueta del colchón). Formato vertical 4:5, con espacio libre arriba para un título.")
CAR=[
('1-Valeria-La-noche-antes-de-las-visitas','valeria','7276',
 "HABITACIÓN: loft de apartamento estilo escandinavo; paredes gris perla claro, piso de madera clara, ventanal grande con marco negro que deja ver luces de la ciudad al atardecer; cama baja con cabecero de madera clara; un árbol de Navidad pequeño y frondoso en la esquina con esferas doradas y blancas; guirnalda de pino natural con lucecitas cálidas sobre el cabecero; cojines blancos con lazos rojos; manta tejida crema.",
 "COLCHÓN: el colchón exacto de la imagen 2 (San Remo negro: tapa negra acolchada, laterales negros con bordado, etiqueta plateada en el lateral), con sábana blanca ajustable que deja ver el lateral y la etiqueta.",
 "OUTFIT DE VALERIA (igual en todas las fotos de este carrusel): pijama de franela de cuadros escoceses rojo y crema (camisa de botones y pantalón), medias tejidas color crema y argollas doradas pequeñas.",
 [('01-Portada',"Valeria acostada de lado sobre el colchón abrazando un cojín con lazo rojo, sonriendo a la cámara, el árbol iluminado detrás desenfocado."),
  ('02-Slide-2',"Valeria de rodillas sobre el colchón colgando la guirnalda de luces en el cabecero, mirando hacia atrás a la cámara y riendo."),
  ('03-Slide-3',"Valeria sentada sobre el colchón envuelta en la manta crema, sosteniendo con las dos manos una taza de chocolate caliente con malvaviscos, mirando por el ventanal."),
  ('04-Slide-4',"Valeria durmiendo plácidamente de lado sobre el colchón, ojos cerrados, el árbol y las lucecitas encendidas en la penumbra cálida de la noche.")]),
('2-Camila-La-lista-de-diciembre','camila','7163',
 "HABITACIÓN: dormitorio bohemio y acogedor; pared de fondo verde salvia, cabecero tapizado en terciopelo verde esmeralda, mesas de noche de ratán, plantas en macetas de barro, ventana con cortinas de lino blanco y luz de mañana; árbol de Navidad mediano con esferas rojas y doradas, guirnalda de rodajas de naranja seca y canela colgada en la pared; regalos envueltos en papel kraft con cintas rojas en el piso.",
 "COLCHÓN: el colchón exacto de la imagen 2 (Premium Pillow top: tapa blanca con dibujo gris, laterales grises con rombos, ribete negro y etiqueta negra en el lateral), con sábana blanca ajustable que deja ver el lateral y la etiqueta.",
 "OUTFIT DE CAMILA (igual en todas las fotos de este carrusel): suéter oversize de punto trenzado verde esmeralda, pantalón ancho color crema, un lazo rojo de terciopelo en el cabello y sus argollas doradas.",
 [('01-Portada',"Camila sentada con las piernas cruzadas sobre el colchón escribiendo una lista larga en un papel tipo pergamino que cae hasta el colchón, mordiendo el lápiz y sonriendo a la cámara."),
  ('02-Slide-2',"Camila de pie junto a la cama (con el colchón en primer plano) mostrando a la cámara un set de pijamas a juego de cuadros rojos, riéndose emocionada."),
  ('03-Slide-3',"Camila sentada sobre el colchón envolviendo un regalo con papel kraft y cinta roja, rodeada de tijeras, rollos de cinta y una taza de chocolate caliente."),
  ('04-Slide-4',"Camila acostada boca arriba sobre el colchón, sosteniendo la lista con todo tachado y haciendo pulgar arriba a la cámara, muy feliz.")]),
('3-Herrera-Maraton-de-peliculas','herrera','7166',
 "HABITACIÓN: dormitorio principal amplio; paredes azul marino profundo, vigas de madera oscura en el techo, cama king con cabecero de cuero coñac; árbol de Navidad grande y elegante junto a la cama con luces blancas cálidas y esferas doradas; guirnalda de pino con lucecitas sobre el cabecero; una pantalla o proyector frente a la cama ilumina las caras con luz suave; mantas a cuadros rojos y verdes; tazón grande de palomitas y tazas de chocolate.",
 "COLCHÓN: el colchón exacto de la imagen 2 en tamaño king (Premium Doble Pillow top: tapa blanca acolchada, laterales grises con dibujo, ribete negro y etiqueta negra en el lateral), con sábana blanca ajustable que deja ver el lateral y la etiqueta.",
 "OUTFITS DE LA FAMILIA (iguales en todas las fotos de este carrusel): los cuatro con pijamas a juego de cuadros rojo y negro (buffalo check); Mariana con el cabello en moño bajo; la bebé Lucía con mameluco rojo del mismo estampado y su lazo blanco en la cabeza.",
 [('01-Portada',"La familia Herrera completa sobre el colchón bajo mantas a cuadros, con un tazón de palomitas en el centro, mirando la pantalla con caras de emoción iluminadas por la luz de la película."),
  ('02-Slide-2',"Andrés llegando a la cama con un tazón gigante de palomitas mientras Sofía salta sobre el colchón celebrando y Mariana carga a Lucía riéndose."),
  ('03-Slide-3',"Sofía y la bebé Lucía dormidas a mitad de la película recostadas sobre Mariana, Andrés las mira con ternura; luz tenue de la pantalla y del árbol."),
  ('04-Slide-4',"Plano abierto de los cuatro riéndose a carcajadas sobre el colchón con las mantas, el árbol iluminado al lado y la guirnalda sobre el cabecero.")]),
('4-Herrera-Esperando-a-Santa','herrera','7213',
 "HABITACIÓN: cuarto infantil de Sofía; paredes crema con estrellitas doradas pintadas, cama con estructura de madera en forma de casita adornada con lucecitas cálidas, ventana grande con cortinas blancas y una luna llena brillante en el cielo nocturno; árbol de Navidad pequeño con adornos hechos a mano; una media navideña roja con la letra S colgada en la cama; en la mesa de noche un plato con galletas de jengibre y un vaso de leche; alfombra de lana blanca.",
 "COLCHÓN: el colchón exacto de la imagen 2 (San Remo blanco: tapa blanca acolchada, laterales blancos con dibujo, ribete claro y etiqueta plateada en el lateral), con sábana blanca ajustable que deja ver el lateral y la etiqueta.",
 "OUTFITS (iguales en todas las fotos de este carrusel): Sofía con camisón blanco de algodón con detalles de lazos rojos; la bebé Lucía con mameluco de terciopelo rojo y lazo blanco; Mariana con bata larga color crema; Andrés con suéter de punto azul marino.",
 [('01-Portada',"Sofía arrodillada sobre el colchón mirando por la ventana hacia la luna con ojos ilusionados, abrazando un peluche, las lucecitas de la cama encendidas."),
  ('02-Slide-2',"Andrés arropando a Sofía en la cama mientras Mariana, con Lucía en brazos, sonríe a su lado; Sofía señala el plato de galletas."),
  ('03-Slide-3',"Primer plano de la mesa de noche con las galletas de jengibre y el vaso de leche junto a la cama, la mano de Sofía dejando una carta para Santa sobre el colchón."),
  ('04-Slide-4',"Sofía y Lucía dormidas juntas sobre el colchón bajo una manta blanca, Mariana y Andrés las miran abrazados desde el borde de la cama; luz de luna y lucecitas.")]),
]
for car,who,m,room,mt,outfit,shots in CAR:
    for name,scene in shots:
        d=f'{K}/{car}/{name}'; os.makedirs(d)
        shutil.copy(cast[who],f'{d}/imagen-1-casting-{who}.jpg')
        shutil.copy(mat[m],f'{d}/imagen-2-colchon-{mname[m]}.jpg')
        quien="Usa las caras, el cabello y los rasgos exactos de la imagen 1" + (" (familia Herrera: Mariana, Andrés, Sofía de 6 años y la bebé Lucía)" if who=='herrera' else "") + " y el colchón exacto de la imagen 2."
        txt=f"{quien}\n\nESCENA: {scene}\n\n{room}\n\n{mt}\n\n{outfit}\n\n{COMMON}\n"
        open(f'{d}/prompt.txt','w').write(txt)
open(f'{K}/LEEME.txt','w').write('''KIT DE FOTOS · COLCHONES IMPERIA · Navidad (15 al 31 de diciembre)

16 fotos de usuario para 4 carruseles. Cada carrusel tiene SU propia habitación,
SU propio colchón Imperia y SUS propios outfits (iguales dentro del carrusel,
distintos entre carruseles):

  1 Valeria   · loft escandinavo gris con ventanal de ciudad · San Remo NEGRO · pijama de cuadros rojo y crema
  2 Camila    · dormitorio bohemio verde salvia y ratán      · Premium Pillow top · suéter verde esmeralda + lazo rojo
  3 Herrera   · dormitorio azul marino con vigas y proyector  · Premium Doble Pillow top (king) · pijamas buffalo rojo y negro
  4 Herrera   · cuarto infantil con estrellas y cama casita   · San Remo BLANCO · camisón blanco, terciopelo rojo, bata crema

Cada carpeta = una foto, con:
  - imagen-1-casting-...  → cara oficial del personaje
  - imagen-2-colchon-...  → colchón Imperia que debe aparecer
  - prompt.txt            → texto para pegar

CÓMO GENERAR EN GEMINI
  1. Chat nuevo para cada foto.
  2. Adjunta las dos imágenes (primero la 1, luego la 2).
  3. Pega el texto de prompt.txt y envía.
  4. Descarga y nombra el archivo como la carpeta (ej: "3-Herrera - 01-Portada").

SI ALGO SALE MAL, ESCRÍBELE EN EL MISMO CHAT:
  - "El colchón debe ser idéntico al de la imagen 2."
  - "Mantén las caras exactamente como en la imagen 1."
  - "Que la etiqueta del lateral se vea de frente y sin nada que la tape."
  - "Hazla vertical 4:5."
  (No te preocupes si la etiqueta sale con texto inventado: se corrige después.)
''')
print('ok')
