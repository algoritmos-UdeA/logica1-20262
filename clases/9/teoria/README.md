![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 9 — Funciones: introducción (Teoría)

Diapositivas base del tema 9. Empiezan con un repaso rápido de todo lo visto hasta ahora (método de Polya, entrada/procesamiento/salida, las tres alternativas condicionales, los ciclos `Mientras` y `Para`, y los tipos de variables usados en los ciclos). Luego se introduce la idea de **modularizar**, es decir, dividir un programa en partes más pequeñas llamadas módulos o **funciones**, y se explica por qué conviene hacerlo. El tema se desarrolla con dos ejemplos resueltos de dos formas cada uno, sin funciones y con funciones: la conversión de temperatura (grados Celsius a Fahrenheit) y las calificaciones de un curso (el mismo Ejemplo 5 de la [clase 8](../../8/teoria/README.md)). 40 diapositivas.

## Contenido cubierto

- **Repaso**: método de Polya, entrada/procesamiento/salida, tabla resumen de bloques (entrada, salida, proceso, decisión) en diagrama de flujo/pseudocódigo/Python, las tres alternativas condicionales (simple, doble, múltiple con mismo criterio y con criterio diferente), los ciclos `Mientras` y `Para`, los tipos de variables usados en los ciclos (variable de control, contador, acumulador, bandera, centinela) y la clasificación de iteraciones conocidas vs. desconocidas. Sirve de puente: todo lo anterior se sigue usando **dentro** de las funciones.
- **Módulo y modularizar**: un **módulo** es una porción de código que realiza una tarea específica. También se le llama subrutina, procedimiento, función o método, según el lenguaje. **Modularizar** es dividir un programa grande en módulos. Se ilustra con el programa de conversión de temperatura (`f = (9.0/5)*c + 32`) escrito primero como un solo bloque de instrucciones.
- **Ventajas de la modularización**, cada una con su propia diapositiva:
  - **Abstracción**: permite concentrarse en lo importante e ignorar los detalles. Se explica con una lista de tareas pendientes: "Lavar la ropa" (con abstracción) frente a la lista de todos los pasos necesarios para lavarla (sin abstracción). Adaptado de Farrell, *Programming Logic and Design*.
  - **Trabajo simultáneo**: los módulos de un proyecto grande pueden ser escritos por programadores distintos al mismo tiempo, lo que reduce el tiempo de desarrollo.
  - **Reutilización y confiabilidad**: un módulo ya escrito se puede usar en otros programas (reutilización), y si ya fue probado se puede confiar en que funciona correctamente (confiabilidad).
  - **Facilidad para identificar estructuras**: agrupar tareas en módulos ayuda a los programadores principiantes a identificar las estructuras de un programa.
- **Programa principal**: la mayoría de los programas tienen un módulo principal que contiene la lógica general y llama a los demás módulos.
- **Cómo nombrar funciones**: el nombre debe ser una sola palabra (sin espacios), significativo, y va seguido de un par de paréntesis. Una tabla compara nombres para una función que calcula el salario bruto de un empleado: `calcular_salario_bruto()` (bueno), `cal_sal_br()` (válido pero críptico), `calcular_salario_bruto_para_un_empleado()` (válido pero demasiado largo), `calcular bruto()` (no válido: tiene un espacio) y `calcularsalariobruto()` (válido pero difícil de leer sin separadores).
- **Función llamadora y función llamada**: la función **llamadora** es la que usa a otra; la función **llamada** es la que es usada. Al llamar a una función, la ejecución pasa a ella; cuando la función termina (`return`), la ejecución vuelve al punto de la llamadora donde se hizo la llamada. Se ilustra con `celcius_to_fahrenheit(c)`, que recibe los grados Celsius como **parámetro** y devuelve los grados Fahrenheit con `return`, junto con los diagramas de flujo de la función llamada y del programa principal que la llama.
- **Cohesión funcional (una función, una tarea)**: la cohesión funcional es el grado en que todas las instrucciones de una función contribuyen a una misma tarea. Regla práctica: si para describir lo que hace una función hay que usar la palabra "y", probablemente son varias funciones. Se compara una función de **baja cohesión** (`promedio_de_notas()`, que lee dos notas, calcula el promedio **y** lo muestra) con dos de **alta cohesión** (`leer_nota(mensaje)` y `calcular_promedio(a, b)`, cada una con una sola tarea).
- **Comparación sin funciones vs. con funciones** (conversión de temperatura): el mismo programa escrito como un solo bloque y con la función `celsius_a_fahrenheit(c)`. Los dos producen el mismo resultado; con la función, el cálculo queda con un nombre que dice qué hace y se puede reutilizar.
- **Ejemplo calificaciones (sin funciones)**: retoma el enunciado del Ejemplo 5 de la clase 8 (leer las notas de `N` estudiantes y calcular porcentajes de aprobados/reprobados y promedios). Incluye una tabla de resultados esperados para 5 estudiantes con notas `4.0, 2.5, 3.0, 1.5, 4.8` (60 % aprobaron, 40 % reprobaron, promedio de aprobadas 3.93, de reprobadas 2.0, general 3.16) y un resultado de ejecución que los confirma. La diapositiva deja un ejercicio: hacer la prueba de escritorio y encontrar un **bug grave** en el código tal como está planteado. El script de `codigo/` ya tiene la versión corregida, así que conviene intentar encontrar el bug antes de abrirlo.
- **Ejemplo calificaciones (con funciones)**: el mismo problema dividido en un programa principal y tres funciones, cada una con su propio diagrama de flujo (con parámetros y salidas):
  - `es_nota_aprobatoria(nota, nota_minima)`: devuelve `True` si la nota es aprobatoria y `False` si no.
  - `calcular_promedio(suma, cantidad)`: divide la suma por la cantidad, pero devuelve `0` si la cantidad es `0`. Así la protección contra la división por cero se escribe **una sola vez** y sirve para los tres promedios, en vez de repetirse en una alternativa múltiple como en la versión sin funciones.
  - `imprimir_reporte(est_aprob, est_reprob, suma_aprob, suma_reprob)`: calcula los tres promedios llamando a `calcular_promedio()` y muestra el reporte con dos decimales (`:.2f`). Es un ejemplo de una función que llama a otra función.

  El programa principal solo lee los datos, usa `es_nota_aprobatoria()` dentro del ciclo para decidir qué contador y acumulador actualizar, y al final llama a `imprimir_reporte()`.
- 14 referencias externas: las mismas de la clase 8 (ellibrodepython, w3resource, Real Python, curriculumresources.edu.gh, python-course.eu y los cursos de MakeCode Micro:bit), más cuatro nuevas sobre funciones y ciclos: Real Python — [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/), [Python's Built-in Functions](https://realpython.com/python-built-in-functions/) y [Best practices: functions](https://realpython.com/ref/best-practices/functions/), y Nick Parlante — [Python guide](https://cs.stanford.edu/people/nick/py/) (Stanford).

> [!NOTE]
> Los scripts de `codigo/` no son copias exactas de las diapositivas. Tienen los mismos cálculos, pero cambian algunos mensajes y formatos de salida. Por ejemplo, `ejemplo_calificaciones_modular.py` muestra también los porcentajes de aprobados y reprobados (`Aprobaron: 3 (60.0 %)`), que la versión de la diapositiva no muestra.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-09.pdf](clase-09.pdf) | Diapositivas completas del tema 9, en PDF (40 páginas). |
| [clase-09.pptx](clase-09.pptx) | Diapositivas completas del tema 9, editable (PowerPoint). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas de flujo (ver la tabla siguiente). |
| [images/](images/) | Exportación en `.png` de los diagramas de `diagramas/`, más las imágenes de apoyo de las diapositivas de ventajas de la modularización. |

### Diagramas de flujo

La mayoría de los diagramas tienen el mismo nombre en `diagramas/` y en `images/`. Las dos excepciones son los diagramas de función llamada/llamadora, que tienen nombres distintos en cada carpeta.

| Fuente (`diagramas/`) | Imagen (`images/`) | Contenido |
|---|---|---|
| [no_modular.drawio](diagramas/no_modular.drawio) | [no_modular.png](images/no_modular.png) | Conversión de temperatura como un solo bloque de instrucciones. |
| [modular.drawio](diagramas/modular.drawio) | [modular.png](images/modular.png) | La misma conversión, dividida en programa principal y función. |
| [funciones1.drawio](diagramas/funciones1.drawio) | [funcion_llamada.png](images/funcion_llamada.png) | Función llamada `celcius_to_farenheit()`, con su parámetro (`c`) y su salida (`f`). |
| [funciones2.drawio](diagramas/funciones2.drawio) | [funcion_llamadora.png](images/funcion_llamadora.png) | Programa principal (función llamadora) que lee `temp_c`, llama a la función y escribe `temp_f`. |
| [ejemplo_no_modular.drawio](diagramas/ejemplo_no_modular.drawio) | [ejemplo_no_modular.png](images/ejemplo_no_modular.png) | Ejemplo calificaciones sin funciones. |
| [ejemplo_modular.drawio](diagramas/ejemplo_modular.drawio) | [ejemplo_modular.png](images/ejemplo_modular.png) | Programa principal del ejemplo calificaciones con funciones. |
| [funcion_nota.drawio](diagramas/funcion_nota.drawio) | [funcion_nota.png](images/funcion_nota.png) | Función `es_nota_aprobatoria()`. |
| [funcion_calcular_promedio.drawio](diagramas/funcion_calcular_promedio.drawio) | [funcion_calcular_promedio.png](images/funcion_calcular_promedio.png) | Función `calcular_promedio()`. |
| [funcion_imprimir_reporte.drawio](diagramas/funcion_imprimir_reporte.drawio) | [funcion_imprimir_reporte.png](images/funcion_imprimir_reporte.png) | Función `imprimir_reporte()`. |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/ejemplo_temperatura_no_modular.py](codigo/ejemplo_temperatura_no_modular.py) | Conversión de grados Celsius a Fahrenheit en tres líneas, sin funciones. |
| [codigo/ejemplo_temperatura_modular.py](codigo/ejemplo_temperatura_modular.py) | La misma conversión, con la función `celsius_a_fahrenheit(c)` y un programa principal que la llama. Con `100` °C, las dos versiones muestran `100.0 °C = 212.0 °F`. |
| [codigo/ejemplo_calificaciones_no_modular.py](codigo/ejemplo_calificaciones_no_modular.py) | Ejemplo calificaciones sin funciones: porcentajes y promedios de aprobados/reprobados, con la alternativa múltiple que evita dividir por cero. Ya incluye la corrección del bug que la diapositiva deja como ejercicio. |
| [codigo/ejemplo_calificaciones_modular.py](codigo/ejemplo_calificaciones_modular.py) | Ejemplo calificaciones con las funciones `es_nota_aprobatoria()`, `calcular_promedio()` e `imprimir_reporte()`. Con las notas de la diapositiva (`4.0, 2.5, 3.0, 1.5, 4.8`) muestra 60 %/40 % y los promedios 3.93, 2.00 y 3.16. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
