![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 8 — Ciclo Para (Teoría)

Diapositivas base del tema 8: tras un repaso rápido del método de Polya, entrada/procesamiento/salida, las tres alternativas condicionales y el ciclo `Mientras`/`while` (cerrado con el problema repaso del cine del señor Burns, retomado de la clase 7 y resuelto aquí — ver [`codigo/cine_sr_burns/`](codigo/cine_sr_burns/)), se introduce la estructura **Para**/`for` — su equivalencia con `Mientras`, la noción de secuencia en Python y nueve ejemplos guiados que van del recorrido simple de números a la búsqueda de extremos y la instrucción `continue`. Cierra con ciclos anidados y cinco ejercicios de repaso sin resolver. 69 diapositivas.

## Contenido cubierto

- **Repaso**: método de Polya (entender, diseñar, implementar, revisar), entrada/procesamiento/salida, la tabla resumen de bloques (entrada, salida, proceso) en diagrama de flujo/pseudocódigo/Python, y las tres alternativas condicionales (simple, doble, múltiple con mismo criterio y con criterio diferente) — todo como puente hacia el tema nuevo.
- **Repaso de ciclos (`Mientras`)**: recuerda brevemente el diagrama de flujo, pseudocódigo (`Mientras (condición) Haga`) y Python (`while (condición):`) del ciclo visto en la clase 7, junto con los tipos de variables de apoyo (variable de control, contador, acumulador, bandera, centinela) y la clasificación de iteraciones conocidas vs. desconocidas.
- **Problema repaso (cine del señor Burns)**: retoma el enunciado planteado sin resolver en la teoría de la clase 7 (venta de boletas VIP/normales hasta agotar cupo o hasta que el cajero cierre la venta) como ejercicio de repaso de iteraciones desconocidas antes de pasar al ciclo `Para`; su solución completa está en [`codigo/cine_sr_burns/README.md`](codigo/cine_sr_burns/README.md).
- **Ciclo Para**: representación equivalente en diagrama de flujo, pseudocódigo (`Para (vc = inicio, fin, actualizacion) Haga ... Fin_Para`) y Python (`for vc in range(inicio, fin + 1, actualizacion):`). A diferencia del `Mientras`, la inicialización, la condición de control y la actualización de la variable de control se definen juntas en la cabecera del ciclo, lo que lo hace automático y apropiado para ciclos de número de iteraciones **conocido**.
- **Ejemplo 1**: imprimir los primeros `N` números, retomando el mismo problema de motivación de la clase 7 pero con `Para` en vez de `Mientras`.
- **Ejemplo 2**: suma de los primeros `N` números enteros positivos, con prueba de escritorio.
- **Ejemplo 3**: factorial de un número entero no negativo `n`, con prueba de escritorio.
- **Ejemplo 4**: imprimir los números de `n` a 1 alternando el signo (p. ej. 6, -5, 4, -3, 2, -1), usando un `range` descendente. Deja una nota importante sobre el límite excluido de `range()`: con paso positivo el límite de parada es `fin + 1` (porque `range()` excluye ese valor), pero con paso **negativo** es `fin - 1` — por eso `range(N, 0, -1)` y no `range(N, 2, -1)`.
- **Sobre el ciclo Para en Python / ¿Qué es una secuencia?**: a diferencia de otros lenguajes (C, Java), el `for` de Python no cuenta posiciones — recorre, elemento por elemento, una **secuencia** (colección ordenada indexada desde 0). Cadenas, listas y `range` son las tres secuencias usadas en el curso, y las tres comparten exactamente la misma sintaxis `for iterating_var in sequence:`.
- **Ejemplo 5 (notas de un curso, número de estudiantes conocido)**: lee `N` notas y calcula porcentajes y promedios de aprobados/reprobados con un acumulador condicional (contar y sumar por separado según la nota sea aprobada o reprobada). Se deja deliberadamente con un bug: no valida que las notas ingresadas estén dentro del rango permitido (0.0–5.0) — el punto de partida de los ejemplos 9 y de `continue` más adelante.
- **Ejemplo 6**: cuenta y lista los divisores de un número positivo.
- **Ejemplo 7 (primalidad)**: resuelto en dos formas equivalentes — contando todos los divisores hasta `num // 2` y comparando contra 2 (`ejemplo7_para.py`), y con una bandera `es_primo` que se pone en `False` y corta el ciclo con `break` apenas aparece el primer divisor, sin seguir contando los demás (`ejemplo7_para_bandera.py`, "Otra forma" — más eficiente).
- **Ejemplo 8 (Fibonacci)**: imprime los primeros `n` términos de la sucesión, manejando dos variables de estado (`n0`, `n1`) que se van rotando en cada iteración con ayuda de una variable temporal (`n2`).
- **"Ciclos: algunos patrones analizados"**: una síntesis de mitad de clase que nombra los patrones ya cubiertos — acumulador de suma (ejemplo 2), acumulador condicional (ejemplo 5), conteo condicional (ejemplos 6 y 7), bandera + ruptura (ejemplo 7, otra forma) y variables de estado múltiples (Fibonacci) — antes de introducir el patrón de búsqueda de extremos.
- **Búsqueda de extremos**: patrón general para encontrar el máximo/mínimo de una secuencia manteniendo una variable con el "mejor" valor visto hasta el momento, actualizada por comparación en cada iteración (a diferencia de un acumulador, aquí no se combina la información de todos los datos: solo se retiene uno). Se comparan dos formas de inicializar esa variable antes de la primera comparación:
  - **Opción 1 — valores fijos**: aprovechar que el dominio de los datos es conocido (notas entre 0.0 y 5.0) e inicializar `maximo`/`minimo` en los extremos opuestos del dominio. Es la opción más simple, pero solo funciona si el rango de los datos se conoce con certeza.
  - **Opción 2 — el primer dato leído**: inicializar `maximo`/`minimo` con el primer elemento de la secuencia, distinguiendo la primera iteración de las demás. Es más general: no asume nada sobre el rango de los datos.
- **Ejemplo 9 (extiende el ejemplo 5)**: agrega al enunciado la nota máxima y mínima del curso. `ejemplo9_opcion1.py` resuelve con la inicialización de valores fijos (Opción 1); `ejemplo9_opcion2.py` combina la inicialización con el primer dato (Opción 2) con la validación de rango por `continue` (ver el siguiente punto).
- **`continue`**: se motiva retomando el bug dejado pendiente en el ejemplo 5 — ¿qué pasa si el usuario ingresa una nota fuera de rango? A diferencia de `Romper`/`break` (termina el ciclo por completo), `continue` solo salta el resto del cuerpo en la iteración actual y sigue con la siguiente, sin salir del ciclo. `ejemplo9_opcion2.py` usa `continue` para descartar una nota fuera de 0.0–5.0 antes de contarla en ningún cálculo, incluida la búsqueda de extremos (por eso lleva su propio contador `notas_validas`, usado para distinguir la primera nota *válida* de las siguientes).
- **Ciclos anidados**: forma general con `Para` anidado (`i`/`j` como variables de control independientes; si el externo se repite F veces y el interno C veces, el cuerpo más interno se ejecuta F×C veces) y cuatro casos de uso típicos: programas con menú (ciclo externo del menú + ciclo interno de una tarea repetitiva), cálculo de series matemáticas (ciclo externo de los términos + ciclo interno del factorial de cada término), validación de datos con reintentos, y recorrido de tablas o matrices.
- **5 ejercicios de repaso sin resolver** (ciclos anidados): cuadro de asteriscos NxN, el mismo cuadro pero hueco por dentro, triángulo rectángulo de asteriscos, los primeros N números primos, y aproximación de $e^x$ mediante su serie de Taylor.
- 12 referencias externas: ellibrodepython, w3resource, Real Python (sitio general, cheatsheet, condicionales y `while`), curriculumresources.edu.gh, python-course.eu, y los dos cursos de MakeCode Micro:bit (`csintro` y el listado general) — las mismas ya usadas en la clase 7.

> [!NOTE]
> A la fecha de esta página, `codigo/ejemplo9_continue.py` sigue vacío (un stub pendiente de completar) y `diagramas/`/`images/` solo cubren los ejemplos 1 a 8 — la búsqueda de extremos y `continue` (ejemplo 9) todavía no tienen su propio diagrama de flujo exportado.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-08.pdf](clase-08.pdf) | Diapositivas completas del tema 8, en PDF (69 páginas). |
| [clase-08.pptx](clase-08.pptx) | Diapositivas completas del tema 8, editable (PowerPoint). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas de flujo de los ejemplos 1 a 8. |
| [images/](images/) | Exportación en `.png` de cada diagrama de `diagramas/`, con el mismo nombre de archivo. |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/ejemplo1_para.py](codigo/ejemplo1_para.py) | Ejemplo 1: imprime los números de 1 a `N` con `for`. |
| [codigo/ejemplo2_para.py](codigo/ejemplo2_para.py) | Ejemplo 2: suma de los primeros `N` números enteros positivos, con un acumulador (`suma`). |
| [codigo/ejemplo3_para.py](codigo/ejemplo3_para.py) | Ejemplo 3: factorial de `n`, con un acumulador de producto (`fact`). |
| [codigo/ejemplo4_para.py](codigo/ejemplo4_para.py) | Ejemplo 4: secuencia alternante de signos de `n` a 1, usando `range` descendente y la fórmula `(-1)**i`. |
| [codigo/ejemplo5_para.py](codigo/ejemplo5_para.py) | Ejemplo 5: porcentajes y promedios de notas aprobadas/reprobadas de `N` estudiantes; deja pendiente la validación del rango de la nota (0.0–5.0). |
| [codigo/ejemplo6_para.py](codigo/ejemplo6_para.py) | Ejemplo 6: lista y cuenta los divisores de un número positivo. |
| [codigo/ejemplo7_para.py](codigo/ejemplo7_para.py) | Ejemplo 7: determina si un número es primo contando todos sus divisores hasta `num // 2`. |
| [codigo/ejemplo7_para_bandera.py](codigo/ejemplo7_para_bandera.py) | Ejemplo 7, otra forma: misma primalidad, con la bandera `es_primo` y `break` al encontrar el primer divisor. |
| [codigo/ejemplo8_para.py](codigo/ejemplo8_para.py) | Ejemplo 8: imprime los primeros `n` términos de la sucesión de Fibonacci. |
| [codigo/ejemplo9_opcion1.py](codigo/ejemplo9_opcion1.py) | Ejemplo 9, Opción 1: extiende el ejemplo 5 con la nota máxima/mínima del curso, inicializadas con los extremos fijos del dominio (0.0–5.0). |
| [codigo/ejemplo9_opcion2.py](codigo/ejemplo9_opcion2.py) | Ejemplo 9, Opción 2: misma búsqueda de extremos, pero inicializada con la primera nota *válida* leída, y con `continue` para descartar notas fuera de rango antes de contarlas. |
| [codigo/ejemplo9_continue.py](codigo/ejemplo9_continue.py) | Vacío — stub pendiente para el ejemplo aislado de `break` vs. `continue` de la sección "Contextualización". |
| [codigo/cine_sr_burns/](codigo/cine_sr_burns/) | Solución completa del problema repaso del cine del señor Burns (planteado en la teoría de la clase 7): enunciado, pseudocódigo, diagrama de flujo, código Python y verificación en su propio [README.md](codigo/cine_sr_burns/README.md). |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
