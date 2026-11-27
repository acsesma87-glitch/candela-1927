# Candela 1927: dos versiones separadas

Se publica con GitHub Pages desde la rama `main`, carpeta raíz.

## Versión de Candela (NO TOCAR)
- Archivos de la raíz: `index.html`, `viaje.html`, `herramientas.html`, `altamar.html`, `sw.js`, `manifest.webmanifest` e iconos.
- Enlace: https://acsesma87-glitch.github.io/candela-1927/
- Es el enlace que tiene Candela en su móvil (ella usa las postales del viaje, hasta el 30 de noviembre).
- No se modifica NUNCA. Todo el trabajo se hace en `prueba/`; el usuario dirá cuándo hay que subirlo.

## Versión de trabajo (aquí se hacen todos los cambios)
- Carpeta `prueba/` (copia completa de la web).
- Enlace: https://acsesma87-glitch.github.io/candela-1927/prueba/
- Para ver todos los días abiertos: https://acsesma87-glitch.github.io/candela-1927/prueba/altamar.html?prueba#todo

## Pasar cambios a Candela
Solo cuando el usuario lo pida: copiar los archivos de `prueba/` a la raíz y subirlos.

## Cómo se genera Altamar (importante)
- `altamar.html` NO se edita a mano: se genera desde `fuente/` con `python3 fuente/build.py`, que escribe `prueba/altamar.html`.
- `fuente/engine.html`: motor (pantallas, herramientas, perras, libreta, diálogos, puzles, sonido).
- `fuente/dayN.js`: el guion de cada día. `fuente/scenes.py`: los dibujos (SVG) de las escenas y personajes.
- Si se edita `prueba/altamar.html` directamente, el siguiente `build.py` borra esos cambios. Hay que cambiar `fuente/` y volver a generar.
- Al cambiar algo en `prueba/`, subir el número de «versión de prueba N» en `fuente/engine.html` y el nombre de caché en `prueba/sw.js`.

## Lupa y linterna: BLINDADAS
- El manejo de la lupa y la linterna (cómo se mueven con el dedo, el tamaño, lo que se ve dentro del cristal, que vuelvan al centro al cambiar de herramienta, cómo detectan las pistas) funciona bien y NO se toca.
- Para cambiar cualquier cosa de su manejo hay que preguntárselo expresamente al usuario antes.
