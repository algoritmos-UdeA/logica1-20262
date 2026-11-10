![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 12 — Ordenamiento y búsqueda

Continuación de la [clase 11](../11/README.md), que cerró con un problema pendiente: los nombres y las notas de un curso guardados en dos **arreglos paralelos**, con preguntas que todavía no se podían responder bien: ¿cómo se muestra el listado de mayor a menor nota?, ¿cuál es la nota de Carla? y, si se ordenan las notas, ¿cómo sigue cada nombre unido a su nota? Para responderlas se estudian dos tareas básicas sobre arreglos. La primera es **buscar**: la **búsqueda lineal** revisa los elementos uno por uno y sirve con cualquier lista, mientras que la **búsqueda binaria** descarta la mitad en cada paso, pero exige que la lista esté ordenada. La segunda es **ordenar**: a partir de una pieza reutilizable, la función `intercambiar` (con una variable temporal), se construyen tres métodos, **selección**, **burbuja** e **inserción**. Por fuera los tres son la misma caja negra (modifican la lista que reciben y no retornan nada), pero por dentro trabajan distinto. Cada algoritmo sigue el mismo camino: la idea con un diagrama, el algoritmo con una traza en consola, la función con su especificación (*Supone / Garantiza*) y las pruebas con `assert`. La clase termina con un programa integrador, la **administración de notas de un curso**, que guarda a los estudiantes en tres arreglos paralelos parcialmente llenos (cupo `N` y `cantidad`) y los ordena por nota o por nombre sin separar a cada estudiante de sus datos. Las incomodidades de esa solución motivan los temas siguientes: la programación orientada a objetos y las matrices.

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema completo: búsqueda lineal, intercambio, los tres métodos de ordenamiento y su comparación, búsqueda binaria, el integrador con arreglos paralelos parcialmente llenos, lo incómodo de esa solución y `sorted()`/`.sort()`, con la descripción de cada diagrama y de cada script.
- [`teoria/clase-12.pdf`](teoria/clase-12.pdf) / [`teoria/clase-12.pptx`](teoria/clase-12.pptx) — diapositivas completas (63 diapositivas).
- [`teoria/codigo/README.md`](teoria/codigo/README.md) — **índice del código**: el enunciado de cada problema y los enlaces a los archivos que lo resuelven.
- [`teoria/codigo/`](teoria/codigo/) — los scripts de los ejemplos:
  - `busquedas.py` y `test_busquedas.py`: búsqueda lineal y búsqueda binaria, con sus pruebas.
  - `ordenamientos.py` y `test_ordenamientos.py`: `intercambiar`, `posicion_menor` y los tres métodos de ordenamiento, con sus pruebas.
  - `curso/`: el programa integrador en tres archivos (`curso.py`, `test_curso.py` y `main.py`).

> [!TIP]
> Este mismo programa se resuelve con objetos en la clase 13. La página [app_curso](../13/teoria/app_curso/README.md) pone las dos versiones lado a lado: arreglos paralelos frente a las clases `Estudiante` y `Curso`.

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| 31 | Mar 3 nov (bloque 2, 16-18) | 🏫 Presencial | El tema completo: búsqueda lineal, intercambio con variable temporal, ordenamiento por selección, burbuja e inserción, su comparación contando pasos, búsqueda binaria, y el integrador de notas de un curso con arreglos paralelos parcialmente llenos. Con un notebook complementario a las diapositivas | [sesion_magistral-31](sesion_magistral-31/README.md) |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
