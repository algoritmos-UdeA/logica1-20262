![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 11 — Arreglos unidimensionales y listas

Continuación de la [clase 10](../10/README.md), que cerró con un problema pendiente: leer las notas de un curso y decir **cuántas notas son mayores que el promedio**. Con una sola variable no se puede, porque el promedio solo se conoce después de leer todas las notas y, para entonces, las anteriores ya se perdieron. Para resolverlo se presenta el **arreglo**: una variable que guarda muchos valores del mismo tipo bajo un solo nombre, a los que se llega por su **índice**, de 0 a N - 1. En Python el arreglo se escribe con una **lista usada como arreglo**, con reglas: tamaño fijo (`[0.0] * N`), un solo tipo de dato y acceso por posición. Cada operación básica (crear, guardar, leer, llenar, recorrer, acumular, comparar vecinos y clonar) se muestra en pseudocódigo y en Python, y se advierte que con listas `=` no copia: crea un **alias**. Luego se estudian las **funciones con listas** en tres casos: la función recibe una lista y devuelve un valor, devuelve una lista nueva, o modifica la lista que recibe (y entonces su *Garantiza* debe decirlo). La clase termina resolviendo el problema de la clase 10 con diseño top-down y un programa en tres archivos, y deja planteado un problema con **arreglos paralelos** para la clase siguiente.

## Teoría

- [`teoria/clase-11.pdf`](teoria/clase-11.pdf) / [`teoria/clase-11.pptx`](teoria/clase-11.pptx) — diapositivas completas (51 diapositivas).
- [`teoria/codigo/`](teoria/codigo/) — los scripts de los ejemplos:
  - `notas_sin_arreglos.py`: el problema que quedó pendiente en la clase 10.
  - `recorrido_suma.py`: crear, llenar, recorrer y acumular un arreglo.
  - `indices_python.py`: índices y las dos formas de recorrer una lista.
  - `funciones_listas.py`: los tres casos de funciones con listas, con sus pruebas.
  - `notas_con_arreglos/`: el problema de la clase 10 resuelto en tres archivos (`notas.py`, `test_notas.py` y `main.py`).
  - `repaso_funciones/`: repaso de la organización en archivos de la clase 10.

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| 27 | Mar 20 oct (bloque 2, 16-18) — tentativa | 🏫 Presencial | Pendiente por dictar | — |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
