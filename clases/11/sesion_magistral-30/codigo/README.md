![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesión magistral 30 — Código

Material para la parte de la [teoría de la clase 11](../../teoria/README.md) que quedó pendiente después de la [sesión 28](../../sesion_magistral-28/README.md): las diapositivas 25-47. Todo usa las notas de la clase, `[3.0, 4.5, 2.0, 4.0]`, y se recomienda recorrerlo en este orden:

| Parte | Archivo o carpeta | Diapositivas | Qué se espera que el lector entienda |
|---|---|---|---|
| 1 | [`1_vecinos_alias_clonar.ipynb`](1_vecinos_alias_clonar.ipynb) | 25-29 | Que un recorrido que usa `notas[i + 1]` debe llegar solo hasta la penúltima posición (`range(N - 1)`), o se sale del arreglo. Que con listas, `copia = notas` **no copia**: crea un **alias**, otro nombre para la misma lista, y lo que se cambie con uno se ve con el otro. Y que para tener una lista independiente hay que **clonarla**: con un recorrido, con `notas[:]` o con `list(notas)` |
| 2 | [`2_funciones_con_listas.ipynb`](2_funciones_con_listas.ipynb) | 30-39 | Los tres casos de funciones con listas: recibe una lista y devuelve un valor (`calcular_promedio`), devuelve una lista nueva (`leer_notas`), o **modifica** la lista que recibe (`aplicar_bonificacion`). Que dentro de la función el parámetro es un alias de la lista que se pasó: por eso el Caso 3 cambia la lista de afuera sin `return`, y su *Garantiza* debe decirlo. Y cómo se prueba cada caso |
| 3 | [`3_notas_mayores_que_promedio/`](3_notas_mayores_que_promedio/) | 40-47 | Cómo se resuelve un problema completo con lo anterior: diseño top-down, funciones reutilizadas y nuevas, especificación antes del código, *stubs* y pruebas, en tres archivos. Es el problema que quedó pendiente en la clase 10. Tiene su propio README, y uno más en cada uno de sus dos pasos |

## Cómo usar los notebooks

* Se abren en Jupyter (Anaconda Navigator o la extensión de Jupyter de VS Code, como se explicó en la [sesión 19](../../../8/sesion_magistral-19/README.md)) o en Google Colab, con el botón **Open in Colab** que tiene cada notebook al comienzo.
* Están **sin salidas**: las celdas se ejecutan en orden, una por una, prediciendo antes qué van a imprimir.
* Debajo de cada celda de código hay un enlace **🔎 Ver paso a paso en Python Tutor**. Allí cada lista se dibuja como una caja y cada nombre como una flecha, así que se ve cuándo dos nombres apuntan a **la misma** lista.
* Las celdas marcadas con ⚠️ fallan **a propósito**: `IndexError` al comparar vecinos hasta la última posición, y `TypeError` al guardar el resultado de una función del Caso 3, que retorna `None`.
* Una celda del notebook 2 pide cuatro notas con `input()`.

## Cómo usar la parte 3

Los archivos `.py` se ejecutan desde la terminal, **desde la carpeta de cada paso**:

```
cd 3_notas_mayores_que_promedio/paso1_stubs
python test_notas.py
python main.py
```

El README de [`3_notas_mayores_que_promedio/`](3_notas_mayores_que_promedio/) explica qué muestra cada paso, y el de cada paso trae la salida esperada.

> [!Important]
> Se usó IA generativa para preparar este material a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
