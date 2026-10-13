![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 22

* **Tipo**: Presencial
* **Fecha**: 06/10/2026
* **Parte**: Primer bloque de clase (14-16)

## Resumen

Esta sesión trabaja los **ciclos anidados**, el último tema de la [teoría de la clase 8](../teoria/README.md) (diapositivas 65-67), con tres ejemplos que surgieron en clase y se resolvieron en un notebook de Jupyter. Cada ejemplo da un paso más en la relación entre el ciclo externo y el interno:

| # | Ejemplo | Qué enseña |
|---|---|---|
| 1 | La serie `1 2 2 3 3 3 ...` y su mejora en forma de triángulo | El ciclo interno se repite una cantidad de veces que **depende** de la variable del externo. Se escribe de tres formas equivalentes, y la posición del `print()` decide la forma de la salida |
| 2 | Un rectángulo de `N × M` caritas `^_^` | El ciclo interno se repite siempre la **misma** cantidad de veces (regla `F × C`). La misma solución con `for` y con `while`, donde hay que reiniciar `j` en cada fila |
| 3 | La escalera de Mario | **Dos** ciclos internos seguidos (espacios y `#`) y variables que se actualizan al final de cada fila |

## Notebook

[`ciclos_anidados.ipynb`](ciclos_anidados.ipynb) reconstruye los tres ejemplos en el orden de la clase, con la explicación de cada paso, para que pueda estudiarlos aunque no haya asistido. Incluye el análisis y el pseudocódigo de cada ejemplo, pruebas de escritorio, y celdas marcadas con **🔍 Para entender** que se agregaron después de la clase para mostrar errores frecuentes: el `print()` en el lugar equivocado y el `while` interno sin reiniciar `j`. Termina con un resumen y cuatro ejercicios para practicar, sin solución.

Para abrirlo, siga las instrucciones de la [sesión 19](../sesion_magistral-19/README.md) (Anaconda Navigator o la extensión de Jupyter de VS Code).

La carpeta [`codigo_sin_editar/`](codigo_sin_editar/) conserva el notebook tal como quedó al final de la clase.

## Relación con otras sesiones

* La [sesión 21](../sesion_magistral-21/README.md) resuelve los seis ejercicios de ciclos anidados de la diapositiva 67 y reúne consejos para usar contadores, banderas y acumuladores dentro de ciclos anidados.
* El triángulo del ejemplo 1 es el ejercicio del triángulo rectángulo de la diapositiva 67, con números en lugar de asteriscos. El rectángulo del ejemplo 2 se convierte en el cuadrado de asteriscos cuando `N = M`.
* La escalera de Mario es el problema *Mario* de CS50x ([versión fácil](https://cs50.harvard.edu/x/psets/1/mario/less/)), que la sesión 21 había dejado como reto.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del código escrito en clase. El docente revisó y validó la versión final.
