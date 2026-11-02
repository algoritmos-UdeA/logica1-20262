![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 31

* **Tipo**: Presencial
* **Fecha**: 03/11/2026
* **Parte**: Segundo bloque de clase (16-18)

## Resumen

Esta sesión cubre el tema completo de la [clase 12](../README.md), **ordenamiento y búsqueda**, que responde las preguntas del problema de los arreglos paralelos que quedó al final de la clase 11: ¿cómo se muestra el listado de mayor a menor nota?, ¿cuál es la nota de Carla? y, si se ordenan las notas, ¿cómo sigue cada nombre unido a su nota?

| Parte | Tema |
|---|---|
| 1 | Búsqueda lineal: buscar en desorden, y contar sus comparaciones |
| 2 | Intercambiar dos posiciones con una variable temporal: la pieza que se reutiliza |
| 3-5 | Los métodos de ordenamiento por selección, burbuja e inserción |
| 6 | Comparación de los tres métodos: iguales por fuera, distintos por dentro, y cuánto trabaja cada uno |
| 7 | Búsqueda binaria: buscar en una lista ordenada, descartando la mitad en cada paso |
| 8 | Integrador: administración de notas de un curso, con arreglos paralelos parcialmente llenos, ordenados por nota y por nombre |
| 9-10 | Lo incómodo de esa solución, que motiva la Programación Orientada a Objetos y las matrices, y lo que Python ya trae (`sorted()` y `.sort()`) |

## Notebook

[`notebooks/ordenamiento_busqueda.ipynb`](notebooks/ordenamiento_busqueda.ipynb) complementa las diapositivas: reúne el código de la clase y la teoría más importante, para que el tema se pueda estudiar completo sin ellas. Se puede abrir en Google Colab con el botón **Open in Colab** que tiene al comienzo, o en Jupyter.

Cada algoritmo sigue el mismo camino que en las diapositivas:

1. **la idea**, con una analogía (la guía telefónica, el mazo de cartas, las cartas en la mano) y un diagrama;
2. **el algoritmo** funcionando, con un `print` por pasada para ver cómo cambia la lista;
3. **la función**, con su especificación (*Supone / Garantiza*), que reutiliza `intercambiar` y `posicion_menor`;
4. **las pruebas** con `assert`, con su tabla de casos típicos, límite y especiales.

Además:

* **Contar pasos**, como en el libro *Grokking Algorithms* de Aditya Bhargava: cuántas comparaciones hace cada búsqueda y cada método de ordenamiento, en el mejor y en el peor caso, y cómo crece ese número cuando crecen los datos (tiempo lineal, cuadrático y logarítmico).
* **Videos** de AlgoRythmics, donde cada método de ordenamiento se baila con una danza folclórica: selección, burbuja e inserción, y como material para explorar Shell sort, quick sort y merge sort, que no son parte del curso.
* **Errores frecuentes** que fallan a propósito: intercambiar sin variable temporal, probar un ordenamiento comparando lo que retorna (`None`), y usar la búsqueda binaria en una lista que no está ordenada.
* Un enlace a **Python Tutor** debajo de cada celda de código.

El programa integrador completo, con su menú, está en [`teoria/codigo/curso/`](../teoria/codigo/curso/), y el índice del código de la clase en [`teoria/codigo/README.md`](../teoria/codigo/README.md).

> [!Important]
> Se usó IA generativa para preparar este contenido a partir de las diapositivas y el código de la clase. El docente revisó y validó la versión final.
