![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Parte 1 — Programación estructurada en Python

Estos notebooks son un **refuerzo de Python** para quien ya entendió en clase cómo resolver un problema. No repiten la teoría (algoritmos, pseudocódigo, método de Polya): se concentran en **cómo se escribe y cómo se comporta** cada cosa en Python, con ejemplos que se pueden ejecutar y modificar.

Cada notebook es **autocontenido**: todo lo que usa se explica en el mismo notebook. Algunos temas van más allá de lo que se usa en los ejercicios del curso; esas partes están marcadas con 🐍 y también se explican completas.

## Notebooks

Se recomienda estudiarlos en este orden, porque cada uno supone lo visto en los anteriores.

| # | Notebook | Qué repasa | Clases relacionadas | Abrir en Colab |
|---|---|---|---|---|
| 1 | [Repaso básico de Python](repaso_basico.ipynb) | Tipos de datos, nombres de variables, strings (índices y *slicing*), `print` y f-strings, `input` y conversión de tipos, operadores y su prioridad | [Clase 3](../../../clases/3/README.md), [Clase 4](../../../clases/4/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algoritmos-UdeA/logica1-20262/blob/main/laboratorios/resumen-python/estructurada_python/repaso_basico.ipynb) |
| 2 | [Control de flujo](control_de_flujo.ipynb) | Bloques y sangría, `if`/`elif`/`else`, `while`, `break` y `continue`, `for` y `range`, ciclos anidados, desempaquetado | [Clases 5 a 8](../../../clases/5/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algoritmos-UdeA/logica1-20262/blob/main/laboratorios/resumen-python/estructurada_python/control_de_flujo.ipynb) |
| 3 | [Funciones](funciones.ipynb) | `def`, `return` frente a `print`, pruebas con `assert`, ámbito de las variables, argumentos y valores por defecto; 🐍 `*args`, `**kwargs`, funciones anidadas, de orden superior, decoradores y `lambda` | [Clase 9](../../../clases/9/README.md), [Clase 10](../../../clases/10/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algoritmos-UdeA/logica1-20262/blob/main/laboratorios/resumen-python/estructurada_python/funciones.ipynb) |
| 4 | [Tipos de datos estructurados](variables_estructuradas.ipynb) | Strings y sus métodos, listas (alias y copia), tuplas y diccionarios; 🐍 métodos de listas y diccionarios | [Clase 11](../../../clases/11/README.md) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/algoritmos-UdeA/logica1-20262/blob/main/laboratorios/resumen-python/estructurada_python/variables_estructuradas.ipynb) |

## Cómo estudiar con estos notebooks

1. Ábralo con el botón **Open in Colab** (no necesita instalar nada) o descárguelo y ábralo en Jupyter.
2. Ejecute las celdas **una por una y en orden** (`Shift + Enter`). No use *ejecutar todo*: algunas celdas fallan a propósito para mostrar un error, y otras piden datos con `input()`.
3. Antes de ejecutar las celdas marcadas con 🔮, **escriba en papel lo que cree que van a imprimir**. Después compruébelo.
4. Si un resultado no le queda claro, abra el enlace 🔎 que hay debajo de cada celda: muestra la ejecución paso a paso en [Python Tutor](https://pythontutor.com/).
5. Al final de cada notebook hay una tabla de **errores frecuentes** y ejercicios de **prediga la salida** con su solución.

## Marcas que encontrará

| Marca | Qué significa |
|---|---|
| 🔮 **Prediga antes de ejecutar** | Escriba qué cree que imprime la celda y solo después ejecútela. |
| ⚠️ **Error frecuente** | Un error típico: el mensaje que da Python y cómo corregirlo. Suele ir antes de una celda que falla a propósito. |
| 📏 **Convención del curso** | Una forma de escribir el código que se acordó en el curso (por ejemplo, *snake_case* o la lista usada como arreglo). |
| 🐍 **Propio de Python** | Algo que Python permite pero que el curso no usa en sus ejercicios, o que se ve más adelante. Se explica completo. |
| 🔎 **Ver paso a paso en Python Tutor** | Abre la celda en Python Tutor para seguir su ejecución instrucción por instrucción. |

---

> Los notebooks se generan con los scripts de [`../herramientas/`](../herramientas/README.md), que son para quien los mantiene, no para estudiarlos.
