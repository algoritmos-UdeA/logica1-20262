![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 10 — Funciones: diseño, librerías y módulos (Teoría)

Diapositivas base del tema 10, que continúa la [clase 9](../../9/teoria/README.md). Empiezan con un repaso breve de la definición, la invocación y las pruebas de funciones con `assert`. Luego retoman el programa de conversión de temperaturas: la versión hecha en clase (`temperaturas_v1.py`) se mejora paso a paso aplicando **buenas prácticas**. Sobre ese mismo programa se introducen la **especificación** de una función (*Supone / Garantiza*), el **ámbito** de las variables, las formas de pasar argumentos, los **parámetros con valor por defecto** y las funciones que llaman a otras funciones. Después se presenta el **diseño top-down** para resolver problemas grandes, construyendo el programa con *stubs*, y el uso de **librerías**: las funciones integradas y los módulos `math` y `random`. La clase termina con la organización de un programa en **varios archivos** (módulos propios, `__name__`, la guarda `if __name__ == "__main__":` y `def main()`) y con un problema que motiva el tema siguiente, los arreglos. 60 diapositivas.

## Contenido cubierto

- **Repaso** (diapositivas 2-10): método de Polya, entrada → proceso → salida, qué es una función y qué es modularizar, la sintaxis de `def`, el diagrama de caja negra, la invocación con argumentos por posición, la prueba unitaria frente a la integración, los tipos de casos de prueba (típico, límite y especial) y la sintaxis de `assert`. Es el mismo contenido de la [clase 9](../../9/teoria/README.md), resumido.
- **Ejemplo conversión de temperatura**: una estación meteorológica necesita un programa con un menú de tres opciones: convertir de °C a °F, convertir de °C a Kelvin, o salir. Cualquier otro número muestra `ERROR: Opcion no valida`. El programa debe tener una función para el menú y una función por conversión, que **reciba** la temperatura y **retorne** el valor convertido, sin leer ni imprimir nada. Se presentan:
  - las **entradas** (la opción del menú, entera, y la temperatura en °C, real) y las **salidas** (la temperatura convertida con dos decimales, o un mensaje de error o de despedida);
  - una tabla de **casos de prueba**. Por ejemplo, 100 °C → 212.00 °F (típico, punto de ebullición), −40 °C → −40.00 °F (especial: las dos escalas coinciden), −273.15 °C → 0.00 K (límite: el cero absoluto) y la opción 7 → `ERROR: Opcion no valida` (especial);
  - el **diagrama de flujo** del programa, que corresponde a `temperaturas_v2.py`.
- **Buenas prácticas**: se comparan, lado a lado, la versión hecha en clase (`temperaturas_v1.py`) y la mejorada (`temperaturas_v2.py`). Las dos hacen exactamente lo mismo, pero la segunda se entiende sin necesidad de explicarla. Reglas:
  - El nombre de una función empieza con un verbo y dice qué hace: `mostrar_menu`, no `menu`.
  - Se usan nombres completos, no abreviaturas crípticas: `celsius_a_fahrenheit`, no `c_to_f`.
  - Las variables van en minúscula, con guion bajo (*snake_case*): `temp_c`, no `Tc`.
  - Las pruebas se escriben con `assert`, para que se revisen solas y no a ojo (en `v1` eran `print` comentados).
- **¿Cómo ejecutar un programa?**: con el botón del IDE (▶ en Spyder, *Run Python File* en VS Code), desde la terminal (`python nombre_archivo.py`), o con `python -i nombre_archivo.py`. Esta última forma deja abierta la consola después de ejecutar, para llamar a mano una función: `>>> celsius_a_kelvin(25)`. En los tres casos, Python lee el archivo de arriba hacia abajo y ejecuta cada instrucción.
- **Ejecutar no es lo mismo que probar**: *ejecutar* es correr el programa completo, como lo usaría el usuario; *probar* es verificar que cada función da el resultado esperado. Si el archivo tiene pruebas con `assert`, cada ejecución también las corre: si pasan, el programa arranca normalmente; si alguna falla, se detiene con `AssertionError` e indica la línea.
- **Especificación de una función**: responde a la pregunta "¿cómo sabe alguien usar una función que no escribió?". La especificación es un **contrato** entre dos personas:
  - **Supone** (compromiso de quien **usa** la función): entregar datos válidos.
  - **Garantiza** (compromiso de quien **escribe** la función): devolver el resultado correcto, si los datos son válidos.

  En Python se escribe como un **docstring**, un texto entre `"""` justo debajo del `def`, y se consulta con `help(nombre_funcion)`. Por ejemplo, `celsius_a_kelvin(temp_c)` supone que `temp_c` es un número mayor o igual a −273.15 y garantiza que retorna la temperatura en Kelvin, mayor o igual a 0. Si alguien la llama con −300, obtiene −26.85 K, un resultado sin sentido. ¿De quién es la culpa? De quien llamó a la función, porque no cumplió lo que ella supone: la función cumplió su parte. Con la especificación, varias personas pueden construir un mismo programa sin leer el código de las demás.
- **Ámbito de las variables**: el ámbito es la parte del programa donde una variable existe y se puede usar.
  - Una **variable local** se crea dentro de una función y solo existe mientras la función se ejecuta. Los parámetros también son locales.
  - Una **variable global** se crea fuera de las funciones, en el programa principal.

  Dos variables pueden tener el mismo nombre y ser distintas, si viven en ámbitos diferentes: cada llamada a una función crea su propio espacio de variables. En el ejemplo de la diapositiva 21, `f(x)` cambia su `x` local a 4, pero la `x` global sigue valiendo 3.
- **Variables globales: ¿sí o no?**: una función puede **leer** una variable global, pero no debería **modificarla**. Lo que necesita lo recibe por parámetros, y lo que produce lo entrega con `return`. Se permiten las **constantes globales**, escritas en MAYÚSCULA porque su valor nunca cambia (por ejemplo, `CERO_ABSOLUTO = -273.15`). No se recomienda modificar una global con la palabra `global`. En el ejemplo de la diapositiva 23, un contador global `conversiones` termina en 3 aunque el usuario hizo una sola conversión, porque las pruebas con `assert` también llamaron a la función.
- **Errores típicos de ámbito**:
  - Usar afuera una variable local: llamar `celsius_a_fahrenheit(23)` sin guardar el resultado y luego hacer `print(temp_f)` produce `NameError: name 'temp_f' is not defined`. Solución: guardar el resultado, `temp_f = celsius_a_fahrenheit(23)`.
  - Modificar una global sin `global`: `conversiones = conversiones + 1` dentro de la función produce `UnboundLocalError`. Recomendación: contar en el programa principal, no dentro de la función.
- **Formas de pasar argumentos**, con la función `seno(x, n)`, que aproxima el seno con `n` términos de la serie de Taylor y llama a `factorial`:
  - **Por posición**: `seno(1.0, 3)`. Los argumentos se asignan en el orden de los parámetros.
  - **Por nombre**: `seno(x=1.0, n=3)` o `seno(n=3, x=1.0)`. El orden no importa.
  - Se pueden **mezclar** (`seno(1.0, n=3)`), pero los argumentos por nombre van después de los posicionales. `seno(n=3, 1.0)` produce `SyntaxError` y Python no ejecuta ninguna línea.
- **Parámetros con valor por defecto**: si se omite `n`, `seno(1.0)` produce `TypeError: seno() missing 1 required positional argument: 'n'`. Con `def seno(x, n=10):`, el argumento puede omitirse y se usa `n = 10`. Con 10 términos, `seno(1.0)` da `0.8414709848078965`, que coincide con el valor real; con 3 términos da `0.8416666666666667`, con error en la cuarta cifra. Los parámetros con valor por defecto van al final: `def seno(n=10, x):` produce `SyntaxError`.
- **Una función que llama a otra**: `seno` usa `factorial`. Esto permite:
  - **Reutilización**: `factorial` se escribe y se prueba una vez, y se usa donde se necesite.
  - **Abstracción**: `seno` solo necesita saber **qué** hace `factorial`, no **cómo** lo hace.

  Al terminar `factorial`, la ejecución vuelve al punto exacto de la llamada. Cada llamada crea su propio marco en la **pila de llamadas**, con sus propias variables: por eso hay dos `n` distintas, la de `seno` y la de `factorial`.
- **Resolución de problemas complejos: diseño top-down**: *divide y vencerás* consiste en dividir un problema complejo en subproblemas más sencillos, y estos a su vez en otros más simples, hasta que cada uno sea fácil de resolver. En el diseño **top-down** (descendente) se parte del problema completo (arriba) y se baja, nivel por nivel, hasta las piezas más pequeñas. Idea clave: no se resuelve el problema grande, se resuelven muchos problemas pequeños.
  - **El primer nivel** casi siempre es el mismo: entrada → proceso → salida. El programa de temperaturas ya era top-down; ahora el método tiene nombre.
  - **¿Hasta dónde dividir?**: se divide hasta que cada pieza haga una sola cosa y su nombre lo diga. Se ilustra con un programa que muestra el calendario de un mes. Antes de ver la solución, la diapositiva pregunta: ¿en qué partes dividirían este problema? En el árbol, `es_bisiesto` es el ejemplo de la clase 7, y `obtener_dias_mes` aparece en dos ramas, lo que es **reutilización**. No todo subproblema necesita ser una función: si es una sola línea, puede quedarse dentro de otra.
- **Top-down y bottom-up**:

  | | Top-down | Bottom-up |
  |---|---|---|
  | Orden | De arriba hacia abajo: primero el programa principal | De abajo hacia arriba: primero las funciones más pequeñas |
  | Lo que falta se reemplaza por… | *Stubs*: versiones provisionales e incompletas de una función | *Drivers*: pequeños programas de prueba, como los `assert` |
  | Ventaja | El programa corre desde el primer momento | Cada pieza llega probada a la integración |

  Lo que tienen en común: "los dos construyen una función a la vez, ayudan a aislar los errores y facilitan la depuración" (Liang, §6.13). Nunca se escribe todo para probarlo al final.
- **Del planteamiento al código**: cada caja del árbol es un subproblema, y en el código se convierte en una función (`mostrar_menu()`, `celsius_a_fahrenheit(temp_c)`, `celsius_a_kelvin(temp_c)`). Leer la opción, leer la temperatura y mostrar el resultado son una línea cada una (`input` o `print`), dentro del programa principal. Si el árbol ya está listo, ¿por dónde se empieza a programar? Por arriba: el programa principal.
- **Construir de arriba hacia abajo**: un **stub** es una versión provisional de una función que permite ejecutar el programa antes de terminarlo. El programa de temperaturas se construye en tres pasos, y en cada uno se puede ejecutar:
  1. `temperaturas_topdown_paso1.py`: programa principal completo; las dos conversiones son stubs que retornan `0.0`. El resultado está mal (`100.0°C = 0.00°F`), pero el menú, las opciones y la salida ya se pueden probar.
  2. `temperaturas_topdown_paso2.py`: Fahrenheit implementada y probada con `assert`; Kelvin sigue como stub. El programa principal no cambió. Si se activa la prueba de Kelvin, falla con `AssertionError` y señala la línea: **las pruebas dicen qué falta por hacer**.
  3. `temperaturas_v2.py`: ningún stub, todas las pruebas pasan.
- **Funciones integradas**: `print()`, `input()`, `int()`, `float()` y `round()` no fueron escritas en el curso. Son funciones integradas (*built-in*): están disponibles en cualquier programa sin importarlas, y se comportan como cualquier función, porque reciben argumentos y retornan un valor. Se agregan `abs(x)`, `round(x, n)`, `max(a, b, ...)` y `min(a, b, ...)`, por ejemplo `max(3, 9, 4)` → 9.
- **Librerías**: otras funciones están agrupadas en **módulos** que se deben **importar**. Hay tres tipos: las funciones integradas (sin importación), la **biblioteca estándar** (`math`, `random`: se importan con `import` y vienen con Python) y los **paquetes externos** (`numpy`, `matplotlib`: además deben instalarse; Anaconda ya los incluye). A partir de esta clase se usa el módulo `math`: el cálculo de raíces con `** 0.5` puede reemplazarse por `math.sqrt()`.
- **Módulo `math`**: funciones y constantes matemáticas de uso frecuente, como `math.sqrt(16)` → 4.0, `math.pow(2, 10)` → 1024.0, `math.factorial(5)` → 120, `math.sin(x)` y `math.cos(x)` (con `x` en **radianes**), `math.radians(180)` → π, y las constantes `math.pi` y `math.e`. Antes de escribir una función matemática, conviene revisar si ya existe en `math`: si existe, ya está escrita y probada.
- **Función propia frente a función de librería**: la `seno(x, n=10)` del curso y `math.sin(x)` producen el mismo resultado para `x = 1.0` (`0.8414709848078965`). ¿Para qué se escribió entonces `seno`? Para comprender su funcionamiento interno. En un programa real se recomienda usar `math.sin`.
- **Formas de importar**: `import math` (**recomendada**: el prefijo `math.` indica de dónde proviene cada función), `from math import sqrt, pi` (útil cuando se usan pocas funciones con frecuencia), `import math as m` (útil para abreviar nombres largos) y `from math import *` (**no recomendada**: importa todo y puede reemplazar funciones sin advertencia; por ejemplo, después de ella `pow(2, 3)` da `8.0` en vez de `8`, porque ahora es `math.pow`).
- **¿Cómo consultar una librería?**: para usar una función de librería no hace falta leer su código, basta con su especificación. Se consulta con `help(math.sin)` (que ya advierte *measured in radians*), con `dir(math)` para ver qué contiene el módulo, o con la documentación oficial. Si `help()` se abre en una pantalla aparte en la terminal, se sale con la tecla `q`. Errores típicos:

  | Código | Error | Causa |
  |---|---|---|
  | `x = sqrt(25)` | `NameError: name 'sqrt' is not defined` | No se importó el módulo |
  | `import math` … `sqrt(25)` | `NameError: name 'sqrt' is not defined` | Falta el prefijo `math.` |
  | `import maths` | `ModuleNotFoundError: No module named 'maths'` | Nombre del módulo mal escrito |
  | `math.Sqrt(4)` | `AttributeError: module 'math' has no attribute 'Sqrt'` | Python distingue mayúsculas de minúsculas |
  | `math.sqrt(-4)` | `ValueError: math domain error` | Argumento fuera del dominio de la función |
  | `math.factorial(2.5)` | `TypeError: 'float' object cannot be interpreted as an integer` | Tipo de argumento incorrecto |

  El error más peligroso es el que no muestra mensaje: `math.sin(30)` no produce error, pero el resultado es incorrecto porque se esperaban radianes. Python solo detecta errores de **escritura**, no de **razonamiento**; para estos últimos sirven las pruebas con `assert`.
- **Ejercicio de repaso: adivina el número** (diapositiva 46): el programa elige un número entero al azar entre 1 y 100, y el usuario intenta adivinarlo con las pistas *mayor* o *menor*. Integra todo lo visto en la clase: entender, diseñar (top-down), especificar, implementar con stubs y probar con `random.seed()`. Tiene su propia guía autocontenida en [`codigo/adivina_numero/`](codigo/adivina_numero/). Precaución: no nombrar ningún archivo `random.py`.
- **Dividir un programa en varios archivos**: un **módulo** es un archivo `.py` cuyas funciones pueden usarse desde otro archivo. Se importa igual que `math` o `random`, con el nombre del archivo sin la extensión (`import conversiones`), y se llama con el prefijo del módulo (`conversiones.celsius_a_fahrenheit(temp_c)`). Ambos archivos deben estar en la misma carpeta.
- **¿Qué ocurre al importar un módulo?**: `import conversiones` ejecuta **todo** el archivo de arriba hacia abajo, no solo las definiciones `def`. Si las pruebas están al final del módulo, también se ejecutan al importarlo. Pregunta: ¿le interesa al usuario del menú ver el resultado de las pruebas? ¿Qué ocurriría si una de ellas fallara?
- **`__name__`**: Python le asigna a cada archivo la variable especial `__name__`. Vale `"__main__"` si el archivo se ejecutó directamente, y el nombre del módulo (sin `.py`) si fue importado. Por eso el mismo `saludo.py` imprime `__main__` cuando se ejecuta solo, y `saludo` cuando lo importa `principal.py`.
- **¿Dónde se ubican las pruebas?**: tres opciones, comparadas en la diapositiva 52.

  | | 1. Sin guarda | 2. Guarda en el módulo | 3. Archivo aparte |
  |---|---|---|---|
  | Ubicación de las pruebas | Final de `conversiones.py` | Final de `conversiones.py`, dentro de `if __name__ == "__main__":` | `test_conversiones.py` |
  | ¿Se ejecutan al importar? | Sí (problema) | No | No |
  | Cómo se ejecutan las pruebas | `python conversiones.py` | `python conversiones.py` | `python test_conversiones.py` |
  | Ventaja | Ninguna frente a las otras dos | Pruebas junto a las funciones que prueban | Módulo limpio: solo funciones |
  | Desventaja | Ensucia la salida del programa y puede detenerlo | El módulo crece | Un archivo más, y hay que escribir `conversiones.` antes de cada función |
  | Conveniente para | No se recomienda | Módulos pequeños | Módulos con muchas pruebas |

  **Recomendación para este curso**: se usa la guarda en el módulo mientras haya pocas pruebas; cuando las pruebas crecen, se trasladan a `test_<módulo>.py`. En ambos casos, el programa principal (`main.py`) nunca muestra las pruebas. En la industria, las pruebas se escriben dentro de funciones `def test_...():` y se ejecutan con la herramienta `pytest`, que reconoce los archivos llamados `test_<módulo>.py`.
- **`def main()` y la guarda en el programa principal**: el programa principal se agrupa en una función `main()`, y la llamada `main()` se coloca dentro de `if __name__ == "__main__":`. Así el programa solo arranca cuando el archivo se ejecuta directamente. Esta estructura (`import` → funciones → `def main()` → guarda) es la forma habitual de organizar un programa en Python, y **se recomienda usarla en todos los programas de aquí en adelante**.
- **Errores frecuentes al trabajar con varios archivos**:

  | Situación | Mensaje de Python |
  |---|---|
  | `main.py` y `conversiones.py` en carpetas distintas | `ModuleNotFoundError: No module named 'conversiones'` |
  | Escribir `import conversiones.py` | `ModuleNotFoundError: No module named 'conversiones.py'; 'conversiones' is not a package` |
  | Llamar `celsius_a_fahrenheit(10)` sin el prefijo `conversiones.` | `NameError: name 'celsius_a_fahrenheit' is not defined` |
  | Nombrar un archivo propio `random.py` | Python importa el archivo propio en lugar del módulo `random`, y la librería queda oculta |

  Al importar un módulo propio aparece la carpeta `__pycache__/`. Python la crea automáticamente para cargar el módulo más rápido; puede ignorarse y **no debe entregarse**.
- **Resumen de la clase**: una función bien diseñada tiene un nombre claro, una especificación, pruebas, y no depende de variables globales.
- **Un problema que todavía no se puede resolver bien** (diapositivas 56-57): leer las notas de un curso y mostrar **cuántas notas son mayores que el promedio**. El promedio solo se conoce después de leer todas las notas, pero para entonces la variable `nota` solo conserva la última. Con 4 estudiantes (3.0, 4.5, 2.0, 4.0), el programa calcula el promedio 3.38, pero en `nota` solo queda 4.0. ¿Y si el curso tuviera 40 estudiantes y se usaran 40 variables? La respuesta es el tema de la próxima clase: los **arreglos** (listas en Python), que guardan muchos valores en una sola variable, cada uno en una posición que empieza en 0.
- Referencias externas: sobre diseño top-down y descomposición, Aprender a Programar (CU00225A), Stanford CS106A (*Karel Reader*, cap. 8, *Stepwise Refinement*, y la lección 3, *Decomposition*), MIT 6.100L, lección 7 (*Decomposition, Abstraction, Functions*), CS50P, lección 0, y Liang, *Introduction to Programming Using Python*, §6.13. Además, las referencias generales del curso (ellibrodepython, Real Python, la documentación oficial de Python, python-course.eu y otras).

> [!NOTE]
> Los scripts de `codigo/` no siempre coinciden carácter por carácter con las diapositivas. Por ejemplo, el símbolo de Kelvin no es uniforme: el Sistema Internacional lo escribe `K`, sin el símbolo de grado. `temperaturas_v1.py` y `temperaturas_v2.py` muestran `°K`; `temperaturas_v3.py` y los pasos top-down usan `K` en el título, pero `°K` en el menú y en el resultado. Los resultados numéricos son los mismos en todas las versiones.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-10.pdf](clase-10.pdf) | Diapositivas completas del tema 10, en PDF. |
| [clase-10.pptx](clase-10.pptx) | Diapositivas completas del tema 10, editable (PowerPoint, 60 diapositivas). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas top-down y de módulos (ver la tabla siguiente). |
| [images/](images/) | Exportación en `.png` de los diagramas de `diagramas/`, más cinco capturas de pantalla usadas en las diapositivas. |
| [codigo/](codigo/) | Scripts de los ejemplos (ver [Código de ejemplo](#código-de-ejemplo)). Su [README](codigo/README.md) reúne el **enunciado** de cada problema con los archivos que lo resuelven. |
| [codigo/adivina_numero/](codigo/adivina_numero/) | Ejercicio guiado *Adivina el número*, con su propia guía (`README.md`): diseño top-down, especificación, stubs, pruebas con `random.seed()` y, al final, el programa dividido en módulos. |

### Diagramas

| Fuente (`diagramas/`) | Imagen | Contenido |
|---|---|---|
| [arbol_temperaturas.drawio](diagramas/arbol_temperaturas.drawio) | [arbol_temperaturas.png](images/arbol_temperaturas.png) | Diagrama top-down del programa de temperaturas, con el primer nivel entrada → proceso → salida. |
| [arbol_temperaturas_paso1.drawio](diagramas/arbol_temperaturas_paso1.drawio) | [arbol_temperaturas_paso1.png](images/arbol_temperaturas_paso1.png) | El mismo árbol en el paso 1 de la construcción top-down: las dos conversiones son stubs. |
| [arbol_temperaturas_paso2.drawio](diagramas/arbol_temperaturas_paso2.drawio) | [arbol_temperaturas_paso2.png](images/arbol_temperaturas_paso2.png) | Paso 2: Fahrenheit implementada; Kelvin sigue como stub. |
| [arbol_temperaturas_paso3.drawio](diagramas/arbol_temperaturas_paso3.drawio) | [arbol_temperaturas_paso3.png](images/arbol_temperaturas_paso3.png) | Paso 3: programa terminado, sin stubs. |
| [arbol_calendario.drawio](diagramas/arbol_calendario.drawio) | [arbol_calendario.png](images/arbol_calendario.png) | Diagrama top-down del calendario de un mes. `es_bisiesto` viene de la clase 7 y `obtener_dias_mes` es usada por dos funciones. |
| [temperaturas_principal.drawio](diagramas/temperaturas_principal.drawio) | [temperaturas_principal.png](images/temperaturas_principal.png) | Diagrama de flujo del programa principal de temperaturas (`temperaturas_v2.py`). |
| [temperaturas_todos.drawio](diagramas/temperaturas_todos.drawio) | — | Diagramas de flujo del programa de temperaturas en un solo archivo; no tiene imagen exportada. |
| [arbol_adivina_numero.drawio](diagramas/arbol_adivina_numero.drawio) | [arbol_adivina_numero.png](codigo/adivina_numero/arbol_adivina_numero.png) | Diagrama top-down del ejercicio *Adivina el número*. Su imagen está en la carpeta del ejercicio, no en `images/`. |
| [modulos_estructura.drawio](diagramas/modulos_estructura.drawio) | [modulos_estructura.png](images/modulos_estructura.png) | Un programa dividido en dos archivos: el módulo de funciones y el programa principal que lo importa. |
| [modulos_main.drawio](diagramas/modulos_main.drawio) | [modulos_main.png](images/modulos_main.png) | Estructura de `main.py` con `def main()` y la guarda: si se ejecuta directamente, arranca el menú; si se importa, no muestra nada. |
| [modulos_name.drawio](diagramas/modulos_name.drawio) | [modulos_name.png](images/modulos_name.png) | Valor de `__name__` cuando un archivo se ejecuta directamente y cuando se importa. |
| [modulos_sin_guarda.drawio](diagramas/modulos_sin_guarda.drawio) | [modulos_sin_guarda.png](images/modulos_sin_guarda.png) | Pruebas sin guarda: se ejecutan al importar el módulo. |
| [modulos_con_guarda.drawio](diagramas/modulos_con_guarda.drawio) | [modulos_con_guarda.png](images/modulos_con_guarda.png) | Opción 1: pruebas protegidas con la guarda. |
| [modulos_archivo_pruebas.drawio](diagramas/modulos_archivo_pruebas.drawio) | [modulos_archivo_pruebas.png](images/modulos_archivo_pruebas.png) | Opción 2: pruebas en un archivo `test_conversiones.py` aparte. |
| [modulos_error_carpetas.drawio](diagramas/modulos_error_carpetas.drawio) | [modulos_error_carpetas.png](images/modulos_error_carpetas.png) | Error frecuente: el módulo y el programa principal en carpetas distintas (`ModuleNotFoundError`), frente a la forma correcta, en la misma carpeta, donde aparece `__pycache__/`. |
| [arreglo_notas.drawio](diagramas/arreglo_notas.drawio) | [arreglo_notas.png](images/arreglo_notas.png) | Un arreglo de notas con sus posiciones, que empiezan en 0 (anuncio de la próxima clase). |

### Capturas de pantalla

| Imagen | Contenido |
|---|---|
| [run_ide.png](images/run_ide.png) | Botón ▷ (*Run Python File*) de VS Code para ejecutar `temperaturas_v2.py`. |
| [run_terminal.png](images/run_terminal.png) | Ejecución de `temperaturas_v2.py` con `python -i`: al salir del menú, la consola queda abierta y se llama a mano `celsius_a_kelvin(100)`, que retorna `373.15`. |
| [assertion_error.png](images/assertion_error.png) | Una prueba de `temperaturas_v2.py` con un valor esperado erróneo (`200.0` en vez de `212.0`): el programa se detiene con `AssertionError` y señala la línea 25. |
| [help_funcion.png](images/help_funcion.png) | Consulta de la especificación de una función propia con `help()`. |
| [falla_stub.png](images/falla_stub.png) | `temperaturas_topdown_paso2.py` detenido con `AssertionError` al activar la prueba de un stub (diapositiva 37). |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/temperaturas_v1.py](codigo/temperaturas_v1.py) | Versión del programa de temperaturas hecha en clase: ya tiene funciones, pero con nombres poco claros (`menu`, `c_to_f`) y pruebas con `print` comentadas. Es el punto de partida de las buenas prácticas. |
| [codigo/temperaturas_v2.py](codigo/temperaturas_v2.py) | Versión mejorada: nombres que dicen qué hace cada función (`mostrar_menu`, `celsius_a_fahrenheit`, `celsius_a_kelvin`), pruebas con `assert` y menú con `while True`. Con la opción 1 y 100 °C muestra `100.0°C = 212.00°F`. |
| [codigo/temperaturas_v3.py](codigo/temperaturas_v3.py) | La versión 2 con la **especificación** de cada función (docstring *Supone / Garantiza*), que se puede consultar con `help()`. |
| [codigo/temperaturas_topdown_paso1.py](codigo/temperaturas_topdown_paso1.py) | Paso 1 de la construcción top-down: programa principal completo y las dos conversiones como stubs que retornan `0.0`. El programa corre, pero muestra `100.0°C = 0.00°F`. |
| [codigo/temperaturas_topdown_paso2.py](codigo/temperaturas_topdown_paso2.py) | Paso 2: `celsius_a_fahrenheit` implementada y probada; `celsius_a_kelvin` sigue como stub. En el archivo, la prueba de Kelvin está **activa**, así que el script se detiene con `AssertionError` (como en la diapositiva 37). Para obtener la salida de la diapositiva 36, en la que el programa corre, se comenta esa línea. |
| [codigo/seno.py](codigo/seno.py) | `seno(x, n=10)` por serie de Taylor, que llama a `factorial(n)`: una función que llama a otra y un parámetro con valor por defecto. Imprime `seno(1.0)` con 10 términos (`0.8414709848078965`) y con 3 (`0.8416666666666667`). |
| [codigo/seno_vs_math.py](codigo/seno_vs_math.py) | Compara la `seno` propia con `math.sin`: dan el mismo resultado. Muestra también el error sin mensaje de `math.sin(30)` (que interpreta 30 en radianes) frente a `math.sin(math.radians(30))` → 0.5. |
| [codigo/temperaturas_modulos/](codigo/temperaturas_modulos/) | El programa de temperaturas dividido en módulos, en cuatro carpetas. Cada una se ejecuta desde su propia carpeta: |
| ↳ [0_name/](codigo/temperaturas_modulos/0_name/) | `saludo.py` y `principal.py` imprimen el valor de `__name__`: `__main__` al ejecutar `saludo.py` solo, y `saludo` cuando lo importa `principal.py`. |
| ↳ [1_sin_guarda/](codigo/temperaturas_modulos/1_sin_guarda/) | `conversiones.py` con las pruebas al final, sin guarda: al ejecutar `main.py` aparece `Pruebas de conversiones: todas pasaron` antes del menú. Es un efecto secundario **intencional**, para mostrar el problema. |
| ↳ [2_con_guarda/](codigo/temperaturas_modulos/2_con_guarda/) | Opción 1: las pruebas de `conversiones.py` dentro de la guarda, y `main.py` con `def main()` y su guarda. |
| ↳ [3_archivo_pruebas/](codigo/temperaturas_modulos/3_archivo_pruebas/) | Opción 2: `conversiones.py` solo con funciones, las pruebas en `test_conversiones.py` (`python test_conversiones.py`) y el mismo `main.py`. |
| [codigo/adivina_numero/](codigo/adivina_numero/) | Ejercicio guiado *Adivina el número* (ver [Recursos](#recursos)). |
| [codigo/notas_sin_arreglos.py](codigo/notas_sin_arreglos.py) | Problema que motiva la próxima clase: después de leer todas las notas, la variable `nota` solo conserva la última, así que no se puede saber cuántas notas son mayores que el promedio. Con 3.0, 4.5, 2.0 y 4.0 muestra `Promedio del curso: 3.38` y `Nota guardada en la variable nota: 4.0`. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
