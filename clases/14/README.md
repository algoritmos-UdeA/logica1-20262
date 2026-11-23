![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 14 — Arreglos bidimensionales (matrices)

Continuación de las clases [11](../11/README.md) (arreglos), [12](../12/README.md) (ordenamiento y búsqueda) y [13](../13/README.md) (programación orientada a objetos). La clase 12 dejó una pregunta abierta: en un curso real cada estudiante tiene **varias notas**, una por parcial, y guardarlas en un arreglo por parcial vuelve a producir arreglos paralelos. La respuesta es la **matriz**: una tabla de valores del mismo tipo, organizada en filas y columnas, bajo un solo nombre, a la que se llega con dos índices, `notas[i][j]`.

La clase recorre el mismo camino de los arreglos, con una dimensión más:

1. **La matriz y sus operaciones:** qué es, sus partes y la lista de listas usada como matriz. Después, en pseudocódigo y en Python, cómo crearla en dos pasos (y el error de `[[0.0] * M] * N`), guardar y leer, llenarla, recorrerla por filas y por columnas, acumular por fila y por columna, salirse de la matriz, las diagonales y triangulares, el mayor con su posición, la búsqueda, la transpuesta y la suma, y la copia (`list()` no alcanza).
2. **Funciones con matrices:** los tres casos de las funciones con listas, ahora con matrices.
3. **El problema pendiente resuelto:** notas de un curso con tres parciales que valen 30 %, 30 % y 40 %. Se calcula la nota final de cada estudiante y se muestra a quienes tienen la más alta y la más baja (con empates), en tres archivos.
4. **Matrices y objetos:** una clase `Matriz` que encapsula la lista de listas, y una matriz de objetos, una sala de cine con objetos `Silla`. Es el camino del [laboratorio 5](../../laboratorios/5/README.md), el parqueadero.

La clase cierra con un problema que todavía no se puede resolver bien: al cerrar el programa, los datos se pierden. Eso abre el tema de archivos.

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema completo, con la descripción de cada diagrama y de cada script.
- [`teoria/clase-14.pdf`](teoria/clase-14.pdf) / [`teoria/clase-14.pptx`](teoria/clase-14.pptx) — diapositivas completas (68 diapositivas).
- [`teoria/codigo/README.md`](teoria/codigo/README.md) — **índice del código**: el enunciado de cada problema y los archivos que lo resuelven.
- [`teoria/codigo/`](teoria/codigo/) — los scripts de los ejemplos:
  - `ej00_sin_matriz.py` … `ej11_alias_copia.py`: un script por cada operación de las diapositivas.
  - `funciones_matrices.py` y `test_funciones_matrices.py`: los tres casos de funciones con matrices.
  - `notas_matriz/`: el problema de las notas finales en tres archivos.
  - `matriz_poo/`: la clase `Matriz`, sus pruebas y un programa que la usa.
  - `sala_cine/`: la sala de cine, una matriz de objetos `Silla`, con menú.

## Notebooks

En [`teoria/notebooks/`](teoria/notebooks/). Se abren en Google Colab con el botón de cada uno, o en Jupyter.

| Notebook | Para qué |
|---|---|
| [Arreglos bidimensionales (matrices)](teoria/notebooks/matrices.ipynb) | Acompaña las diapositivas: los mismos ejemplos, listos para ejecutar, con un enlace a Python Tutor en cada celda y los errores típicos en vivo (`[[0.0] * M] * N`, el acumulador que no se reinicia, la copia que comparte las filas) |
| [Notas finales de un curso con una matriz, paso a paso](teoria/notebooks/notas_finales_paso_a_paso.ipynb) | Construye el problema integrador función por función, cada una con sus pruebas |
| [La clase `Matriz`, paso a paso](teoria/notebooks/clase_matriz_paso_a_paso.ipynb) | La clase crece en cuatro pasos, del constructor a `transpuesta` y `sumar` |
| [Sala de cine: una matriz de objetos, paso a paso](teoria/notebooks/sala_cine_paso_a_paso.ipynb) | `Silla`, después `Sala` en tres pasos y una sesión de taquilla. Es el camino del laboratorio 5 con otro problema |

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| Por definir | — | — | — | — |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisa y valida la versión final.
