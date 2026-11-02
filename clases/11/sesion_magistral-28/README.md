![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algoritmos-UdeA/logica1-20262/blob/main/clases/11/sesion_magistral-28/codigo/arreglos.ipynb)

# Sesion magistral 28

* **Tipo**: Presencial
* **Fecha**: 27/10/2026
* **Parte**: Primer bloque de clase (14-16)

## Resumen

Primera sesión de la clase 11, sobre **arreglos unidimensionales**. Se recorrió la [teoría](../teoria/README.md) hasta la diapositiva 24, con una parte en un notebook de Jupyter y otra en el tablero:

| Parte | Tema | Diapositivas |
|---|---|---|
| 1 | ¿Por qué hace falta un arreglo? Una variable por nota no sirve para muchos estudiantes | 8-10 |
| 2 | La lista usada como arreglo: tipo `list`, acceso por posición, índices negativos | 11-14 |
| 3 | Crear un arreglo con `[0.0] * N`, guardar y leer valores | 15-16 |
| 4 | El índice puede ser una expresión (ejercicio con dos arreglos) | 17 |
| 5 | El índice es una variable: llenar un arreglo por teclado o con una expresión | 18-19 |
| 6 | Recorrer y mostrar, por índice y por elemento | 20 |
| 7 | Recorrer y acumular: la suma y el promedio | 21 |
| 8 | La solución del problema pendiente de la clase 10 (cuántas notas son mayores que el promedio), con `for` y con `while` | — |
| 9 | Cuidado con salirse del arreglo: `IndexError` | 22 |
| 10 | Otros recorridos: el inverso, de tres formas, y sus variantes | 23-24 |

El segundo bloque del día fue el [Parcial 2](../sesion_magistral-29/README.md), así que las diapositivas 25 en adelante (comparar vecinos, alias y copia, funciones con listas y la solución con funciones del problema pendiente) quedan para la próxima sesión.

## Notebook

[`codigo/arreglos.ipynb`](codigo/arreglos.ipynb) reúne lo que se hizo en el notebook y en el tablero, en el orden de la clase, con la explicación de cada paso, para que pueda estudiarlo aunque no haya asistido. Las celdas escritas en clase están tal como quedaron, salvo la condición de la Parte 8, que se escribió `>=` y se corrigió a `>`, porque el enunciado pide las notas **mayores** que el promedio. Se marcan con **📝 En el tablero** las celdas que se trabajaron en el tablero, con el código de las diapositivas, y con **🔍 Para entender** las que se agregaron después de la clase:

* un índice negativo no da error y puede esconder un dato equivocado;
* el promedio dividiendo entre `N` en lugar de un 4 escrito a mano, con su prueba de escritorio;
* un caso donde `>` y `>=` dan resultados distintos;
* un recorrido inverso con el límite equivocado, que se salta la posición 0 sin dar error;
* la comprobación de la tabla de variantes de recorrido.

Algunas celdas de clase usan cosas que en el curso no se usan con los arreglos (`append`, las rebanadas como `notas[:2]`, `len` antes de funciones, un entero en una lista de reales). El notebook las deja y explica, en cada caso, cómo se trabaja en el curso. Termina con un resumen y cinco ejercicios para practicar, sin solución.

Se puede abrir en Google Colab, sin instalar nada, con el botón **Open in Colab** de arriba, o en Jupyter, siguiendo las instrucciones de la [sesión 19](../../8/sesion_magistral-19/README.md) (Anaconda Navigator o la extensión de Jupyter de VS Code). Debajo de cada celda de código hay un enlace para ver ese código paso a paso en [Python Tutor](https://pythontutor.com/).

La carpeta [`codigo/codigo_sin_editar/`](codigo/codigo_sin_editar/) conserva el notebook tal como quedó al final de la clase.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del código escrito en clase. El docente revisó y validó la versión final.
