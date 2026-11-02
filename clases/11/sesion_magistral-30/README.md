![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 30

* **Tipo**: Presencial
* **Fecha**: 03/11/2026
* **Parte**: Primer bloque de clase (14-16)

## Resumen

Esta sesión completa la [teoría de la clase 11](../teoria/README.md) desde la diapositiva 25, donde quedó la [sesión 28](../sesion_magistral-28/README.md): el segundo bloque de ese día fue el [Parcial 2](../sesion_magistral-29/README.md). El tema central es la **implementación de funciones con arreglos**, y se trabaja en tres partes:

| Parte | Tema | Diapositivas |
|---|---|---|
| 1 | Comparar vecinos, asignar una lista no la copia (alias) y clonar una lista | 25-29 |
| 2 | Funciones con listas: la función recibe una lista y devuelve un valor, devuelve una lista nueva, o modifica la lista que recibe | 30-39 |
| 3 | El problema pendiente de la clase 10 (cuántas notas son mayores que el promedio y en qué posiciones), resuelto con diseño top-down, especificación, *stubs* y pruebas, en tres archivos | 40-47 |

## Código

La carpeta [`codigo/`](codigo/) tiene el material de las tres partes, con un README que explica qué se espera entender de cada una y cómo usarla:

* [`1_vecinos_alias_clonar.ipynb`](codigo/1_vecinos_alias_clonar.ipynb) y [`2_funciones_con_listas.ipynb`](codigo/2_funciones_con_listas.ipynb): notebooks sin salidas, para ejecutar celda por celda. Cada celda de código tiene un enlace a Python Tutor, donde se ve cuándo dos nombres apuntan a la misma lista.
* [`3_notas_mayores_que_promedio/`](codigo/3_notas_mayores_que_promedio/): el programa en dos pasos, `paso1_stubs/` (las funciones nuevas especificadas pero sin implementar, y las pruebas que señalan qué falta) y `paso2_completo/` (el programa terminado). Cada carpeta tiene su README, con la salida esperada.

Las diapositivas 48-51 (resumen, el problema de los arreglos paralelos que motiva la clase 12, referencias y cierre) completan la presentación.

> [!Important]
> Se usó IA generativa para preparar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
