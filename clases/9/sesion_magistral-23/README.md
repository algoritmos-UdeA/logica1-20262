![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 23

* **Tipo**: Presencial
* **Fecha**: 06/10/2026
* **Parte**: Segundo bloque de clase (16-18)

## Resumen

Primera sesión de la [clase 9](../README.md). Se introducen la **definición** y la **invocación** de funciones respondiendo a la pregunta *¿para qué sirve una función?* Cada ejemplo se resuelve dos veces, primero **sin función** y después **con función**. Al comparar las dos versiones se ve por qué conviene escribir un bloque de código una sola vez y **reutilizarlo** con datos distintos.

| Parte | Ejemplos | Qué enseña |
|---|---|---|
| 1 | Conversión de temperatura: `c_to_f(c)`, `c_to_k(c)` y un programa con menú que las integra | Funciones que **reciben** un dato y **devuelven** un resultado con `return`, invocadas con un número, con una variable o con una expresión |
| 2 | El rectángulo de caritas, la serie `1 2 2 3 3 3 ...`, el triángulo y la escalera de Mario | Los ciclos anidados de la [sesión 22](../../8/sesion_magistral-22/README.md) convertidos en funciones que **reciben** datos e **imprimen**, sin devolver nada |
| 3 | La misma función, hecha de dos formas | Quien usa una función no necesita saber cómo está hecha por dentro (la **caja negra**) |

En clase se convirtieron en funciones la temperatura y el rectángulo (`imprimir_caritas`). La serie, el triángulo y la escalera se completaron después, con el mismo procedimiento, para que el patrón quede completo.

## Archivos

| Archivo | Descripción |
|---|---|
| [`funciones.ipynb`](funciones.ipynb) | Notebook con los ejemplos resueltos y explicados paso a paso, para estudiarlos aunque no haya asistido. Cada ejemplo sigue los mismos pasos: sin función → definición → invocación → ¿por qué conviene la función? Incluye celdas marcadas con **🔍 Para entender**, agregadas después de la clase (por ejemplo, qué devuelve una función sin `return`), un resumen que clasifica las funciones según los cuatro tipos de la teoría, y cuatro ejercicios para practicar, sin solución. |
| [`temperaturas.py`](temperaturas.py) | El programa de temperaturas con menú, tal como se escribió en clase en Spyder. Es el mismo de la última celda de la Parte 1 del notebook. |
| [`codigo_sin_editar/`](codigo_sin_editar/) | El notebook y el script tal como quedaron al final de la clase. |

Para abrir el notebook, siga las instrucciones de la [sesión 19](../../8/sesion_magistral-19/README.md) (Anaconda Navigator o la extensión de Jupyter de VS Code).

> [!NOTE]
> El notebook corrige tres detalles del código escrito en clase, y cada corrección está señalada con una nota: un comentario que decía `# c = 5` cuando `c` valía 1, una etiqueta `T1` que debía ser `T2`, y los resultados en Kelvin que se mostraban con la unidad `°F`. Además, el símbolo `°` aparecía dañado en el notebook original. `temperaturas.py` se conserva sin cambios.

## Lo que viene en la clase 10

`temperaturas.py` funciona, pero es el punto de partida de la [clase 10](../../10/README.md), donde se mejora con **buenas prácticas**:

* **Nombres que digan qué hace cada cosa**: `menu` pasa a ser `mostrar_menu`; `c_to_f`, `celsius_a_fahrenheit`; y `Tc`, `temp_c`.
* **Pruebas que se revisen solas**: las pruebas con `print`, que quedaron comentadas dentro de `"""`, se reemplazan por pruebas con `assert`.
* **La especificación de cada función**: un texto (*docstring*) que explica qué supone y qué garantiza.
* **Las etiquetas de las pruebas**: las de Kelvin todavía dicen `°F`.
* **El encabezado del archivo**: todavía dice `Editor de Spyder. Este es un archivo temporal.`

En la clase 10, este mismo programa aparece como [`temperaturas_v1.py`](../../10/teoria/codigo/temperaturas_v1.py) ("hecho en clase"), y su versión mejorada es [`temperaturas_v2.py`](../../10/teoria/codigo/temperaturas_v2.py).

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del código escrito en clase. El docente revisó y validó la versión final.
