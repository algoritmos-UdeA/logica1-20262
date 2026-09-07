![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 7 — Ciclos (Teoría)

Diapositivas base del tema 7: tras un breve repaso de condicionales (el ejemplo del año bisiesto), se motiva la necesidad de las estructuras repetitivas con el problema de imprimir cada vez más números en pantalla, y se desarrolla la estructura **Mientras**/`while` — sus componentes (inicialización, condición de control, cuerpo, actualización), los tipos de variables de apoyo (variable de control, contador, acumulador, bandera, centinela) y siete ejemplos guiados que cubren tanto ciclos con número de iteraciones conocido como desconocido. 77 diapositivas.

## Contenido cubierto

- **Repaso (año bisiesto)**: se retoma el ejemplo de repaso de la clase de condicionales múltiples en sus dos formas — condicionales anidados con la bandera `flag_bisiesto`, y una única condición combinada con `and`/`or` — como puente hacia el tema de ciclos.
- **Motivación de los ciclos**: los problemas de imprimir los primeros 10, 100 y 1000 números en pantalla muestran que, sin una estructura repetitiva, el código crece linealmente con la cantidad de salidas — de ahí la necesidad del **ciclo** (bucle o iteración): una estructura que repite un conjunto de instrucciones mientras se cumpla una condición.
- **Componentes de un ciclo**: inicialización (previa al ciclo, no parte de él), condición de control o parada, y cuerpo (instrucciones que se repiten, incluida la actualización obligatoria de la variable de control para garantizar que el ciclo pueda terminar).
- **Estructura Mientras/`while`**: representación equivalente en diagrama de flujo, pseudocódigo (`Mientras (condicion) Entonces ... Fin_Mientras`) y Python (`while (condicion): ...`).
- **Tipos de variables útiles en ciclos**: variable de control, contador (se actualiza en una cantidad constante, `contador = contador + CONSTANTE`), acumulador (se actualiza en una cantidad variable), bandera y centinela — con ejemplos de cada rol.
- **Tipos de problemas con ciclos**: con número de iteraciones **conocido** de antemano (p. ej. promedio de notas de un curso) vs. **desconocido** (p. ej. asistentes a una función de cine) — estos últimos requieren bandera o centinela en vez de un contador acotado.
- **Ejemplo 1**: imprimir los primeros N=10 números, retomando el problema de motivación para mostrar cómo el ciclo generaliza la solución con solo cambiar `N`.
- **Ejemplo 2**: suma de los primeros `N` números enteros positivos, con prueba de escritorio.
- **Ejemplo 3**: factorial de un número entero no negativo `n`, con prueba de escritorio.
- **Ejemplo 4**: imprimir los números de `n` a 1 alternando el signo (p. ej. 6, -5, 4, -3, 2, -1), resuelto en 4 formas equivalentes: bandera numérica con una asignación de `num` por rama, bandera numérica con impresión inline, bandera booleana alternada con `not()`, y una fórmula cerrada con `(-1)**i` (sin bandera).
- **Ejemplo 5 (cine del señor Burns)**: enunciado de un problema con número de iteraciones **desconocido** (venta de boletas VIP/normales hasta agotar cupo o hasta que el cajero digite -1) — se plantea pero su solución queda para la siguiente clase.
- **Ejemplo 6 (notas de un curso, iteraciones desconocidas)**: leer una cantidad desconocida de notas y calcular porcentajes y promedios de aprobados/reprobados, resuelto de dos formas — con **bandera** (`hay_estudiante` s/n, preguntada antes de cada iteración) y con **centinela** (nota = -1, un valor fuera del rango válido 0.0–5.0, comparado directamente en la condición del ciclo). Ambas versiones se dejan deliberadamente con un bug para que el estudiante lo encuentre y corrija (el caso más probable: si todos los estudiantes aprueban o todos reprueban, el cálculo del promedio del grupo vacío divide entre cero).
- **Ejemplo 7**: el mismo problema de las notas, pero con el número de estudiantes conocido de antemano (`N`), resuelto con un contador — mismo bug intencional que el ejemplo 6, retomado explícitamente como primer ejercicio de repaso.
- **Bandera vs. centinela**: comparación directa de las dos formas de manejar un número desconocido de iteraciones — la bandera necesita una variable adicional preguntada antes de cada iteración, el centinela se compara directamente contra el mismo dato de entrada sin variable extra.
- **12 ejercicios de repaso** (corregir el bug del ejemplo 7, promedio crédito, cuenta de supermercado, clasificación por rangos, pares, cuenta regresiva, cuadrados, múltiplos, acumulado parcial, numeración de entradas) y **próxima clase**: serie de Fibonacci, ciclos infinitos, ruptura de ciclos (`break`), solución completa del ejemplo 5, valores extremos en ciclos, y la estructura `Haga` (do-while).
- 12 referencias externas: ellibrodepython, w3resource, Real Python (sitio general, cheatsheet, condicionales y `while`), curriculumresources.edu.gh, python-course.eu, y los dos cursos de MakeCode Micro:bit (`csintro` y el listado general) — ya usadas en la clase 6.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-07.pdf](clase-07.pdf) | Diapositivas completas del tema 7, en PDF (77 páginas). |
| [clase-07.pptx](clase-07.pptx) | Diapositivas completas del tema 7, editable (PowerPoint). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas de flujo de cada ejemplo. |
| [images/](images/) | Exportación en `.png` de cada diagrama de `diagramas/`, con el mismo nombre de archivo. |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/ejemplo1_bisiesto_forma1.py](codigo/ejemplo1_bisiesto_forma1.py) | Repaso — año bisiesto, forma 1: condicionales anidados con la bandera `flag_bisiesto`. |
| [codigo/ejemplo2_bisiesto_forma2.py](codigo/ejemplo2_bisiesto_forma2.py) | Repaso — año bisiesto, forma 2: una única condición combinada con `and`/`or`, sin bandera. |
| [codigo/bisiesto_test_condicional1.py](codigo/bisiesto_test_condicional1.py) | Prueba puntual de la forma 1 (condicionales anidados, sin `Leer` ni bandera) con el caso límite `year = 1900`. |
| [codigo/bisiesto_test_condicional2.py](codigo/bisiesto_test_condicional2.py) | Prueba puntual de la forma 2 (condición combinada) con el mismo caso límite `year = 1900`, para verificar que ambas formas coinciden. |
| [codigo/ciclos_ejemplo1.py](codigo/ciclos_ejemplo1.py) | Ejemplo 1: imprime los números de 1 a `N` (N=10) con `while`, en vez de un único `Escribir` con todos los valores listados. |
| [codigo/ciclos_ejemplo2.py](codigo/ciclos_ejemplo2.py) | Ejemplo 2: suma de los primeros `N` números enteros positivos, usando un contador (`num`) y un acumulador (`suma`). |
| [codigo/ciclos_ejemplo3.py](codigo/ciclos_ejemplo3.py) | Ejemplo 3: factorial de `n`, usando un contador (`i`) y un acumulador de producto (`fact`). |
| [codigo/ciclos_ejemplo4a.py](codigo/ciclos_ejemplo4a.py) | Ejemplo 4, forma 1: secuencia alternante de signos con una bandera numérica (`flag_negativo`) y una asignación de `num` por rama. |
| [codigo/ciclos_ejemplo4b.py](codigo/ciclos_ejemplo4b.py) | Ejemplo 4, forma 2: misma bandera numérica, pero imprimiendo directamente `-num`/`num` en cada rama en vez de asignar `num` primero. |
| [codigo/ciclos_ejemplo4c.py](codigo/ciclos_ejemplo4c.py) | Ejemplo 4, forma 3: bandera booleana (`True`/`False`) que se alterna con `not()` en vez de asignarse explícitamente en cada rama. |
| [codigo/ciclos_ejemplo4d.py](codigo/ciclos_ejemplo4d.py) | Ejemplo 4, forma 4: sin bandera — el signo se obtiene con la fórmula cerrada `(-1)**i`, usando `i` como contador/exponente. |
| [codigo/ciclos_ejemplo6a.py](codigo/ciclos_ejemplo6a.py) | Ejemplo 6, forma bandera: lee notas mientras el usuario responda `'s'` a `¿Hay estudiante?`; incluye un bug intencional a corregir. |
| [codigo/ciclos_ejemplo6b.py](codigo/ciclos_ejemplo6b.py) | Ejemplo 6, forma centinela: lee notas hasta que se ingresa `-1` (fuera del rango válido 0.0–5.0); mismo bug intencional que la forma bandera. |
| [codigo/ciclos_ejemplo7.py](codigo/ciclos_ejemplo7.py) | Ejemplo 7: mismo problema de las notas, pero con el número de estudiantes `N` conocido de antemano y un contador (`i < N`); mismo bug intencional, retomado como primer ejercicio de repaso. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
