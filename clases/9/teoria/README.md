![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 9 — Funciones: introducción (Teoría)

Diapositivas base del tema 9. Empiezan con un repaso rápido de todo lo visto hasta ahora (método de Polya, entrada/procesamiento/salida, las tres alternativas condicionales, los ciclos `Mientras` y `Para`, y los tipos de variables usados en los ciclos). Luego se introduce la idea de **modularizar**, es decir, dividir un programa en partes más pequeñas llamadas módulos o **funciones**, y se explica por qué conviene hacerlo. Después se presenta cómo se **definen** e **invocan** las funciones en Python, los cuatro tipos de funciones según si reciben datos y si devuelven un valor, y cómo **probar** una función por separado con `assert` antes de integrarla al programa. El tema se desarrolla con tres ejemplos: la conversión de temperatura (grados Celsius a Fahrenheit) y las calificaciones de un curso (el mismo Ejemplo 5 de la [clase 8](../../8/teoria/README.md)), cada uno resuelto sin funciones y con funciones, y el cálculo de áreas de figuras con un menú, desarrollado paso a paso (análisis, diseño, codificación, pruebas e integración). 62 diapositivas.

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
- **Definición de funciones en Python**: una función se define con la palabra clave `def`, seguida del nombre, los parámetros entre paréntesis y dos puntos: `def nombre_funcion(param1, param2, ..., paramN):`. El **cuerpo** va indentado. **Definir una función no la ejecuta**: solo se ejecuta cuando se la llama. Se introduce el **diagrama de caja negra**, que muestra solo las entradas y salidas de la función, sin sus detalles internos.
- **Tipos de funciones según entradas y salidas**: se ilustran con las funciones del ejemplo de áreas.
  - Caso 1, no recibe datos ni devuelve un valor: `mostrar_menu()`.
  - Caso 2, no recibe datos pero devuelve un valor con `return`: `leer_opcion()`.
  - Caso 3, recibe datos y devuelve un valor: `calcular_area_circulo(radio)`.
  - Caso 4, recibe datos pero no devuelve un valor: `mostrar_area(figura, area)`.

  Una diapositiva de resumen los organiza en una tabla de 2 × 2 (sin/con parámetros, no devuelve/devuelve un valor).
- **Invocación de funciones**: se llama a una función escribiendo su nombre con los **argumentos** entre paréntesis: `[variable =] nombre_funcion(arg1, ..., argN)`. Los argumentos se asocian a los parámetros **por posición** y pueden ser números, variables o expresiones. Si la función devuelve un valor, se guarda en una variable o se usa directamente; si no devuelve nada, se la llama sola.
- **Trabajando con funciones**: un ejemplo en dos partes. La primera define seis funciones (conversiones de temperatura en los dos sentidos, áreas del círculo y del rectángulo, `mostrar_menu()` y `mostrar_area()`), cada una con su diagrama de caja negra. La segunda muestra siete formas de invocarlas: sin argumentos, guardando el retorno, usándolo directamente en `print`, con una variable como argumento, con uno y con dos argumentos, y con una llamada dentro de otra (`mostrar_area("rectángulo", calcular_area_rectangulo(4, 3))`). Incluye la salida en pantalla y el valor final de cada variable.
- **Probar una función**: una **prueba unitaria** verifica una función de forma aislada con varios casos; la **integración** es combinar las funciones ya probadas en el programa completo. Conviene probar antes de integrar: si una función falla sola, el error está en ella; si falla dentro del programa completo, puede estar en la función, en la lectura de datos o en el menú. Los casos de prueba se clasifican en **típicos** (uso habitual), **límite** (valores extremos del rango válido) y **especiales** (valores atípicos o inválidos, por ejemplo `calcular_area_rectangulo(-4, 3)`, que devuelve `-12` porque la función no los rechaza).
- **Pruebas con `assert`**: la sintaxis es `assert condición [, "mensaje"]`. Si la condición es verdadera, el programa sigue sin mostrar nada; si es falsa, Python lanza `AssertionError` con la línea que falló o con el mensaje. Tips:
  - Una sola condición por `assert`: si se unen varias con `and`, al fallar no se sabe cuál causó el error.
  - Escribir siempre primero el valor obtenido y después el esperado: `llamada == esperado`.
  - No comparar decimales con `==` (`0.1 + 0.2 == 0.3` da `False`); usar `round(resultado, 2) == esperado`.
  - No escribir el `assert` entre paréntesis con coma: `assert (condición, "mensaje")` nunca falla, porque Python lo lee como una tupla no vacía (y avisa con un `SyntaxWarning`).
  - Solo se prueban con `assert` las funciones que devuelven un valor: `assert` no puede revisar lo que una función imprime en pantalla.
  - `assert` sirve para probar el programa, no para validar lo que escribe el usuario: si Python se ejecuta con la opción `-O`, los `assert` se ignoran. Los datos de entrada se validan con condicionales.
- **¿Está bien esta función?**: un ejercicio con una versión de `calcular_area_rectangulo()` que **suma** la base y la altura en vez de multiplicarlas. La prueba `assert calcular_area_rectangulo(2, 2) == 4` pasa (porque `2 + 2` y `2 * 2` dan lo mismo), y solo un segundo caso (`4, 3` → `12`) revela el error. Moraleja: un solo caso puede dar falsa confianza; varios casos, de distintos tipos, permiten descubrir el error.
- **Función llamadora y función llamada**: la función **llamadora** es la que usa a otra; la función **llamada** es la que es usada. Al llamar a una función, la ejecución pasa a ella; cuando la función termina (`return`), la ejecución vuelve al punto de la llamadora donde se hizo la llamada. Se ilustra con `celcius_to_fahrenheit(c)`, que recibe los grados Celsius como **parámetro** y devuelve los grados Fahrenheit con `return`, junto con los diagramas de flujo de la función llamada y del programa principal que la llama.
- **Cohesión funcional (una función, una tarea)**: la cohesión funcional es el grado en que todas las instrucciones de una función contribuyen a una misma tarea. Regla práctica: si para describir lo que hace una función hay que usar la palabra "y", probablemente son varias funciones. Se compara una función de **baja cohesión** (`promedio_de_notas()`, que lee dos notas, calcula el promedio **y** lo muestra) con dos de **alta cohesión** (`leer_nota(mensaje)` y `calcular_promedio(a, b)`, cada una con una sola tarea).
- **Comparación sin funciones vs. con funciones** (conversión de temperatura): el mismo programa escrito como un solo bloque y con la función `celsius_a_fahrenheit(c)`. Los dos producen el mismo resultado; con la función, el cálculo queda con un nombre que dice qué hace y se puede reutilizar.
- **Ejemplo área de figuras**: un programa con menú que calcula el área de un círculo, un rectángulo o un triángulo, y se repite hasta que el usuario elige la opción 4 (Salir). Se desarrolla en cinco etapas, señaladas en cada diapositiva con la barra *Análisis ▸ Diseño ▸ Codificación ▸ Pruebas ▸ Integración*:
  - **Análisis**: entradas, proceso y salidas, y una tabla de resultados esperados para datos conocidos (por ejemplo, círculo de radio 5 → 78.54; opción 7 → "Opción no válida"), con el tipo de cada caso (típico, límite o especial). Esa tabla se convierte después en los `assert`.
  - **Diseño**: una tabla que pasa de las tareas a las funciones, con los parámetros, el retorno y el tipo (caso 1 a 4) de cada una. El criterio es *una función, una tarea*.
  - **Codificación**: el código de las seis funciones y, como paso 1, su reunión en un solo archivo `areas.py`, con la constante `PI = 3.1416`.
  - **Pruebas** (paso 2): se agregan a `areas.py` los `assert` de las tres funciones de cálculo (dos casos por función, uno típico y uno límite).
  - **Integración** (paso 3): se agrega el programa principal, un ciclo `while opcion != "4"` que muestra el menú, lee la opción y llama a las funciones con una alternativa múltiple.
- **Ejemplo calificaciones (sin funciones)**: retoma el enunciado del Ejemplo 5 de la clase 8 (leer las notas de `N` estudiantes y calcular porcentajes de aprobados/reprobados y promedios). Incluye una tabla de resultados esperados para 5 estudiantes con notas `4.0, 2.5, 3.0, 1.5, 4.8` (60 % aprobaron, 40 % reprobaron, promedio de aprobadas 3.93, de reprobadas 2.0, general 3.16) y un resultado de ejecución que los confirma. La diapositiva deja un ejercicio: hacer la prueba de escritorio y encontrar un **bug grave** en el código tal como está planteado. El script de `codigo/` ya tiene la versión corregida, así que conviene intentar encontrar el bug antes de abrirlo.
- **Ejemplo calificaciones (con funciones)**: el mismo problema dividido en un programa principal y tres funciones, cada una con su propio diagrama de flujo (con parámetros y salidas):
  - `es_nota_aprobatoria(nota, nota_minima)`: devuelve `True` si la nota es aprobatoria y `False` si no.
  - `calcular_promedio(suma, cantidad)`: divide la suma por la cantidad, pero devuelve `0` si la cantidad es `0`. Así la protección contra la división por cero se escribe **una sola vez** y sirve para los tres promedios, en vez de repetirse en una alternativa múltiple como en la versión sin funciones.
  - `imprimir_reporte(est_aprob, est_reprob, suma_aprob, suma_reprob)`: calcula los tres promedios llamando a `calcular_promedio()` y muestra el reporte con dos decimales (`:.2f`). Es un ejemplo de una función que llama a otra función.

  El programa principal solo lee los datos, usa `es_nota_aprobatoria()` dentro del ciclo para decidir qué contador y acumulador actualizar, y al final llama a `imprimir_reporte()`.
- Referencias externas: las mismas de la clase 8 (ellibrodepython, w3resource, Real Python, curriculumresources.edu.gh, python-course.eu y los cursos de MakeCode Micro:bit), más cuatro nuevas sobre funciones y ciclos: Real Python — [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/), [Python's Built-in Functions](https://realpython.com/python-built-in-functions/) y [Best practices: functions](https://realpython.com/ref/best-practices/functions/), y Nick Parlante — [Python guide](https://cs.stanford.edu/people/nick/py/) (Stanford).

> [!NOTE]
> Los scripts de `codigo/` no son copias exactas de las diapositivas. Tienen los mismos cálculos, pero cambian algunos mensajes y formatos de salida. Por ejemplo, `ejemplo_calificaciones_modular.py` muestra también los porcentajes de aprobados y reprobados (`Aprobaron: 3 (60.0 %)`), que la versión de la diapositiva no muestra.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-09.pdf](clase-09.pdf) | Diapositivas completas del tema 9, en PDF (62 páginas). |
| [clase-09.pptx](clase-09.pptx) | Diapositivas completas del tema 9, editable (PowerPoint). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas de flujo (ver la tabla siguiente). |
| [images/](images/) | Exportación en `.png` de los diagramas de `diagramas/`, más las imágenes de apoyo de las diapositivas de ventajas de la modularización. Los diagramas de caja negra están en la subcarpeta `images/funciones_solas/`. |
| [notebooks/funciones.ipynb](notebooks/funciones.ipynb) | Notebook guiado para convertir en funciones cinco ejercicios de la clase 8: factorial, cantidad de divisores, número primo, Fibonacci y $e^x$ por serie. Propone una receta de cinco pasos (entradas → parámetros, salida → `return`, proceso sin `input()`/`print()`, pruebas con `assert` y programa principal). El factorial está resuelto completo como modelo; en los demás ejercicios el estudiante completa la función y el programa principal, con indicaciones y pistas que van disminuyendo y pruebas con `assert` ya escritas. Algunas funciones reutilizan otras: `es_primo()` usa `contar_divisores()` y `aproximar_exp()` usa `factorial()`. |

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

Los diagramas de **caja negra** del ejemplo "Trabajando con funciones" muestran solo las entradas y salidas de cada función. Sus imágenes están en `images/funciones_solas/`:

| Fuente (`diagramas/`) | Imagen (`images/funciones_solas/`) | Función |
|---|---|---|
| [celsius_to_fahrenheit.drawio](diagramas/celsius_to_fahrenheit.drawio) | [celsius_to_fahrenheit.png](images/funciones_solas/celsius_to_fahrenheit.png) | `celsius_to_fahrenheit(c)` |
| [fahrenheit_to_celsius.drawio](diagramas/fahrenheit_to_celsius.drawio) | [fahrenheit_to_celsius.png](images/funciones_solas/fahrenheit_to_celsius.png) | `fahrenheit_to_celsius(f)` |
| [calcular_area_circulo.drawio](diagramas/calcular_area_circulo.drawio) | [calcular_area_circulo.png](images/funciones_solas/calcular_area_circulo.png) | `calcular_area_circulo(radio)` |
| [calcular_area_rectangulo.drawio](diagramas/calcular_area_rectangulo.drawio) | [calcular_area_rectangulo.png](images/funciones_solas/calcular_area_rectangulo.png) | `calcular_area_rectangulo(base, altura)` |
| [mostrar_menu.drawio](diagramas/mostrar_menu.drawio) | [mostrar_menu.png](images/funciones_solas/mostrar_menu.png) | `mostrar_menu()` |
| [mostrar_area.drawio](diagramas/mostrar_area.drawio) | [mostrar_area.png](images/funciones_solas/mostrar_area.png) | `mostrar_area(figura, area)` |
| [invocacion_funciones.drawio](diagramas/invocacion_funciones.drawio) | — | Borrador con varias funciones juntas; no tiene imagen exportada. |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/ejemplo_temperatura_no_modular.py](codigo/ejemplo_temperatura_no_modular.py) | Conversión de grados Celsius a Fahrenheit en tres líneas, sin funciones. |
| [codigo/ejemplo_temperatura_modular.py](codigo/ejemplo_temperatura_modular.py) | La misma conversión, con la función `celsius_a_fahrenheit(c)` y un programa principal que la llama. Con `100` °C, las dos versiones muestran `100.0 °C = 212.0 °F`. |
| [codigo/ejemplo_calificaciones_no_modular.py](codigo/ejemplo_calificaciones_no_modular.py) | Ejemplo calificaciones sin funciones: porcentajes y promedios de aprobados/reprobados, con la alternativa múltiple que evita dividir por cero. Ya incluye la corrección del bug que la diapositiva deja como ejercicio. |
| [codigo/ejemplo_calificaciones_modular.py](codigo/ejemplo_calificaciones_modular.py) | Ejemplo calificaciones con las funciones `es_nota_aprobatoria()`, `calcular_promedio()` e `imprimir_reporte()`. Con las notas de la diapositiva (`4.0, 2.5, 3.0, 1.5, 4.8`) muestra 60 %/40 % y los promedios 3.93, 2.00 y 3.16. |
| [codigo/ejemplo_trabajo_funciones.py](codigo/ejemplo_trabajo_funciones.py) | Ejemplo "Trabajando con funciones": define las seis funciones y las invoca de siete formas distintas, cada una explicada con un comentario. |
| [codigo/areas.py](codigo/areas.py) | Ejemplo área de figuras completo en un solo archivo: constante, funciones, pruebas con `assert` y programa principal, en ese orden. Como las pruebas están antes del programa principal, si alguna falla el programa se detiene antes de mostrar el menú. |
| [codigo/areas_app/](codigo/areas_app/) | El mismo ejemplo dividido en tres archivos (no aparece en las diapositivas): `funciones.py` (constante y funciones), `test_funciones.py` (los `assert`) y `main.py` (programa principal). Los dos últimos traen las funciones con `import`. Se ejecutan desde esa carpeta: `python test_funciones.py` no muestra nada si todas las pruebas pasan, y `python main.py` abre el menú. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
