![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 15 — Archivos

Continuación de la [clase 14](../14/README.md), que terminó con un problema: el programa de las notas finales pide los nombres y las 12 notas **cada vez** que se ejecuta, y al cerrarlo todo se pierde. Los datos de un programa viven en la **memoria**, que se borra al cerrar; para que sobrevivan hay que guardarlos en el **disco**, en un **archivo**.

La clase recorre el mismo camino de las anteriores:

1. **Archivos de texto:** qué es un archivo y el ciclo **abrir → procesar → cerrar**. Los modos `"r"`, `"w"` (que vacía el archivo) y `"a"`. Escribir con `write`. Leer con `read`, `for linea in archivo`, `readline` y `readlines`. Del texto al dato con `strip`, `split` y `float`, armando listas con `append`. Archivos **CSV**, `with`, la carpeta de trabajo, el *buffer* (por qué hay que cerrar), los errores típicos y un vistazo a `try`/`except`.
2. **Funciones con archivos:** reciben el nombre del archivo, y se prueban con un archivo de prueba y con pruebas de **ida y vuelta** (guardar y volver a leer).
3. **El problema pendiente resuelto:** las notas finales se leen de `notas.csv` y el resultado se guarda en `notas_finales.csv`, reutilizando el cálculo de la clase 14.
4. **Archivos y objetos:** la sala de cine de la clase 14 aprende a **guardarse** y **cargarse**. Al salir se guarda en `sala.txt` y al empezar se carga: las ventas no se pierden.

Según el cronograma, archivos es el último tema del curso. La clase cierra con "Lo que ya se puede construir", que junta todo lo visto como puente al proyecto de aula.

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema completo, con la descripción de cada diagrama.
- [`teoria/clase-15.pdf`](teoria/clase-15.pdf) / [`teoria/clase-15.pptx`](teoria/clase-15.pptx) — diapositivas completas (54 diapositivas).
- [`teoria/codigo/README.md`](teoria/codigo/README.md) — **índice del código**: el enunciado de cada problema, los archivos que lo resuelven y cómo ejecutarlos.
- [`teoria/codigo/`](teoria/codigo/) — los scripts de los ejemplos:
  - `ej01_abrir_cerrar.py` … `ej14_try_except.py`: un script por cada operación de las diapositivas, con sus archivos de datos (`trabalenguas.txt`, `notas.csv`).
  - `funciones_archivos.py` y `test_funciones_archivos.py`: funciones que leen y escriben un CSV, y cómo probarlas.
  - `notas_archivo/`: el problema de las notas finales, leído de un archivo.
  - `sala_archivo/`: la sala de cine que se guarda y se carga.

## Notebooks

En [`teoria/notebooks/`](teoria/notebooks/). Se abren en Google Colab con el botón de cada uno, o en Jupyter. Cada uno **crea sus propios archivos de datos** en la carpeta de trabajo (en Colab, en el almacenamiento temporal de la sesión), así que funciona sin descargar nada más. Python Tutor no permite abrir archivos, y por eso estos notebooks muestran el contenido de cada archivo después de escribirlo.

| Notebook | Para qué |
|---|---|
| [Archivos](teoria/notebooks/archivos.ipynb) | Acompaña las diapositivas: escribir, `"w"` frente a `"a"`, las cuatro formas de leer, `strip`/`split`/`float`, CSV, `with` y los errores típicos en vivo |
| [Notas finales desde un archivo, paso a paso](teoria/notebooks/notas_archivo_paso_a_paso.ipynb) | Las funciones de lectura y escritura, una a la vez, cada una probada con su propio archivo de prueba, y el integrador |
| [La sala de cine que se guarda, paso a paso](teoria/notebooks/sala_archivo_paso_a_paso.ipynb) | La `Sala` de la clase 14 gana `guardar` y `cargar`; se simulan dos ejecuciones para ver que las ventas no se pierden |

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| Por definir | — | — | — | — |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisa y valida la versión final.
