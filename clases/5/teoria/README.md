![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 5 — Condicionales (Teoría)

Diapositivas base del tema 5: tras un repaso del método de Polya, el modelo entrada-procesamiento-salida y los operadores vistos en la clase 4, se introduce la estructura condicional (`if`/`else`) — su representación en diagrama de flujo, pseudocódigo y Python — y los dos casos principales de alternativa (simple y doble), desarrollados con varios ejemplos guiados de principio a fin. 54 diapositivas.

## Contenido cubierto

- **Repaso**: método de Polya (resumen de sus 4 pasos), tipos de datos (numéricas, lógicas, alfanuméricas), modelo entrada/procesamiento/salida, tabla resumen diagrama de bloques–pseudocódigo–Python, ciclo de desarrollo de un programa, y un ejemplo ya codificado (área de un círculo).
- **Repaso de operadores** (de la clase 4): aritméticos, relacionales, lógicos (`not`, `and`, `or`) y su tabla de prioridad y asociatividad.
- **Prueba de escritorio** con dos ejemplos guiados de seguimiento de variables paso a paso a partir de un diagrama de flujo: uno puramente secuencial (`x`, `y`, `z`) y otro que ya incorpora una decisión dentro de un ciclo (`i`, `a`, `b`), usado para anticipar el bloque de decisión antes de explicarlo formalmente.
- **Nuevo bloque — Condición**: el símbolo de decisión (rombo) en el diagrama de flujo, con dos salidas posibles (sí/no).
- **Condicionales**: definición como expresión lógica (verdadera o falsa) construida con operadores relacionales y lógicos; condición simple vs. compuesta; sintaxis en pseudocódigo (`Si...Entonces...Sino...Fin_Si`) y en Python (`if`/`else`); comparaciones encadenadas de Python (`20 <= distancia <= 35`) como forma compacta de una condición compuesta con `and`.
- **4 ejemplos guiados** de traducción de un enunciado a condicional (diagrama de flujo + pseudocódigo + Python, con link de ejecución): ángulo recto, punto de ebullición del agua, condición compuesta con `and`, y rango de distancia (con dos formas equivalentes en Python).
- **Casos en problemas de decisión lógica**: alternativa simple, alternativa doble y alternativa múltiple (esta última solo mencionada; se desarrolla en una clase posterior).
- **Alternativa simple** (`if` sin `else`, la rama falsa no tiene instrucciones): desarrollo completo — datos de entrada/salida, definición de variables, diagrama de flujo, pseudocódigo, Python y prueba de escritorio — de dos ejemplos recurrentes en el curso: precio de entrada al bar de Moe según el sexo, y salario neto con subsidio de transporte.
- **Alternativa doble** (`if`/`else`, ambas ramas tienen instrucciones): los mismos dos ejemplos (bar de Moe, salario neto) resueltos ahora con `if`/`else`, con una comparación lado a lado de ambos diagramas de flujo (simple vs. doble) para resaltar la diferencia.
- **Ejemplos de repaso** adicionales resueltos con alternativa doble: mayoría de edad, y si un número es divisor de otro (con el operador módulo `%`).
- **Ejercicios de repaso propuestos** (sin resolver en la diapositiva): mayor entre dos números, raíz cuadrada con validación de negativos, función definida por partes (`f(x)`), intercambio condicional de dos números, y precio de un tiquete aéreo con descuento condicional.
- 8 referencias externas: ellibrodepython, w3resource, Real Python (incluye cheatsheets y guías específicas de condicionales), curriculumresources.edu.gh y python-course.eu.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-05.pdf](clase-05.pdf) | Diapositivas completas del tema 5, en PDF (54 páginas). |
| [clase-05.pptx](clase-05.pptx) | Diapositivas completas del tema 5, editable (PowerPoint). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas de flujo usados en las diapositivas (condicional simple/doble y selección simple/doble). |
| [images/](images/) | Exportación en `.png` de cada diagrama de `diagramas/`, con el mismo nombre de archivo. |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/ejemplo1.py](codigo/ejemplo1.py) | Verifica si una edad es mayor o menor que la mayoría de edad (18 años) con `if`/`else`. |
| [codigo/ejemplo2.py](codigo/ejemplo2.py) | Determina si el segundo número digitado es divisor del primero, comprobando que el residuo (`%`) sea cero. |
| [codigo/condicional_simple1.py](codigo/condicional_simple1.py) | Alternativa simple (`if` sin `else`): calcula el precio de entrada al bar de Moe, sobrescribiendo el precio de hombre solo si el sexo digitado es `'F'`. |
| [codigo/condicional_simple2.py](codigo/condicional_simple2.py) | Alternativa simple: calcula el subsidio de transporte (30% del salario base) solo si el salario base es menor al salario mínimo; en caso contrario el subsidio queda en su valor inicial de 0. |
| [codigo/condicional_doble1.py](codigo/condicional_doble1.py) | Alternativa doble (`if`/`else`): mismo ejemplo del bar de Moe que `condicional_simple1.py`, pero fijando explícitamente el precio en ambas ramas en vez de dejar un valor por defecto. |
| [codigo/condicional_doble2.py](codigo/condicional_doble2.py) | Alternativa doble: mismo cálculo de subsidio de transporte que `condicional_simple2.py`, pero asignando el subsidio (`0.3*sal_base` o `0`) explícitamente en cada rama del `if`/`else`. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
