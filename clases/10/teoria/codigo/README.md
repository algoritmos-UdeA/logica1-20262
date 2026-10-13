![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 10 — Código de ejemplo

Esta carpeta reúne los programas de la clase 10, agrupados por **problema**. Cada sección presenta el enunciado y, debajo, los archivos que lo resuelven, en el orden en que conviene leerlos. Varios archivos resuelven el mismo problema: son versiones sucesivas que muestran cómo mejora un programa al aplicar los temas de la clase.

| # | Problema | Archivos | Diapositivas |
|---|---|---|---|
| 1 | [Conversión de temperatura](#1-conversión-de-temperatura) | `temperaturas_v1.py` a `_v3.py`, `temperaturas_topdown_paso1.py` y `_paso2.py` | 11-38 |
| 2 | [Conversión de temperatura en varios archivos](#2-conversión-de-temperatura-en-varios-archivos) | Carpeta `temperaturas_modulos/` | 47-54 |
| 3 | [Seno por serie de Taylor](#3-seno-por-serie-de-taylor) | `seno.py`, `seno_vs_math.py` | 25-27 y 42 |
| 4 | [Adivina el número](#4-adivina-el-número) | Carpeta `adivina_numero/` | 46 |
| 5 | [Notas mayores que el promedio](#5-notas-mayores-que-el-promedio) | `notas_sin_arreglos.py` | 56 |

> [!TIP]
> Los programas que leen datos se ejecutan desde Spyder o VS Code, o desde la terminal con `python nombre_archivo.py`. Para probar a mano una función sin pasar por el menú, se usa `python -i nombre_archivo.py` y, al terminar el programa, se escribe la llamada en la consola (por ejemplo, `>>> celsius_a_kelvin(25)`).

---

## 1. Conversión de temperatura

### Enunciado

> Una estación meteorológica necesita un programa que convierta temperaturas medidas en grados Celsius (°C) a otras dos escalas: grados Fahrenheit (°F) y Kelvin (K). Al iniciar, el programa muestra un título y luego un menú con tres opciones:
>
> ```
> 1. °C a °F
> 2. °C a K
> 3. Salir
> ```
>
> El usuario elige una opción y el programa hace lo siguiente:
>
> - **Opción 1**: lee una temperatura en °C, la convierte a °F con la fórmula $F = \frac{9}{5}C + 32$ y muestra el resultado con dos decimales.
> - **Opción 2**: lee una temperatura en °C, la convierte a Kelvin con la fórmula $K = C + 273.15$ y muestra el resultado con dos decimales.
> - **Opción 3**: muestra un mensaje de despedida y termina el programa.
> - **Cualquier otro número**: muestra el mensaje `ERROR: Opcion no valida` y vuelve a mostrar el menú.
>
> Después de cada conversión, o de un error, el menú se muestra otra vez. El programa se repite hasta que el usuario elige la opción 3.
>
> **Requisito**: el programa debe estar organizado con funciones:
>
> - Una función que muestre el menú.
> - Una función por cada conversión, que reciba la temperatura en °C como parámetro y **devuelva** el valor convertido.
> - Las funciones de conversión no leen ni imprimen nada: eso lo hace el programa principal.
> - Pruebe cada función de conversión por separado antes de integrarla al programa principal.

*(Diapositivas 11 y 12).*

### Casos de prueba

| Opción | Entrada (°C) | Salida esperada | Tipo |
|---|---|---|---|
| 1 | 100 | `100.0°C = 212.00°F` | Típico (punto de ebullición) |
| 1 | 0 | `0.0°C = 32.00°F` | Típico (punto de congelación) |
| 1 | 37 | `37.0°C = 98.60°F` | Típico (temperatura corporal) |
| 1 | -40 | `-40.0°C = -40.00°F` | Especial (las dos escalas coinciden) |
| 2 | 25 | `25.0°C = 298.15°K` | Típico |
| 2 | -273.15 | `-273.15°C = 0.00°K` | Límite (cero absoluto) |
| 7 | — | `ERROR: Opcion no valida` | Especial (opción inexistente) |
| 3 | — | `Gracias por usarnos` | Salida del programa |

### Archivos

**Versiones del programa** (buenas prácticas y especificación):

| Archivo | Qué muestra |
|---|---|
| [temperaturas_v1.py](temperaturas_v1.py) | La versión hecha en clase. Ya usa funciones, pero con nombres poco claros (`menu`, `c_to_f`, `Tc`) y con las pruebas hechas con `print`, comentadas. |
| [temperaturas_v2.py](temperaturas_v2.py) | La misma lógica con **buenas prácticas**: nombres que dicen qué hace cada función (`mostrar_menu`, `celsius_a_fahrenheit`, `celsius_a_kelvin`), variables en *snake_case* (`temp_c`) y pruebas con `assert`. Diapositivas 15-16. |
| [temperaturas_v3.py](temperaturas_v3.py) | La versión 2 con la **especificación** de cada función: un docstring con *Supone / Garantiza*, que se consulta con `help(celsius_a_kelvin)`. Diapositivas 19-20. |

**Construcción top-down con stubs** (diapositivas 34-38):

| Archivo | Qué muestra |
|---|---|
| [temperaturas_topdown_paso1.py](temperaturas_topdown_paso1.py) | Paso 1: el programa principal está completo y las dos conversiones son **stubs** que retornan `0.0`. El programa corre, pero el resultado está mal: `100.0°C = 0.00°F`. |
| [temperaturas_topdown_paso2.py](temperaturas_topdown_paso2.py) | Paso 2: `celsius_a_fahrenheit` ya está implementada y probada; `celsius_a_kelvin` sigue siendo un stub. La prueba de Kelvin está **comentada** (línea 26), así que el programa corre: `100.0°C = 212.00°F` ya es correcto, pero `25.0°C = 0.00°K` todavía no (diapositiva 36). Si se quita el `#` de la línea 26, el programa se detiene con `AssertionError` en esa línea: las pruebas dicen qué falta por hacer (diapositiva 37). |
| [temperaturas_v2.py](temperaturas_v2.py) | Paso 3: el programa terminado, sin stubs y con todas las pruebas pasando. |

> [!NOTE]
> En los programas, el símbolo de Kelvin aparece como `°K`, aunque el Sistema Internacional lo escribe `K`, sin el símbolo de grado. Los resultados numéricos no cambian.

---

## 2. Conversión de temperatura en varios archivos

### Enunciado

El mismo programa de la [sección 1](#1-conversión-de-temperatura), organizado en **varios archivos**: un módulo `conversiones.py` con las funciones de conversión y un programa principal `main.py` que lo importa con `import conversiones`. *(Diapositivas 47-54).*

### Archivos

Cada carpeta es un programa completo. Sus archivos se ejecutan **desde su propia carpeta**, porque `main.py` solo encuentra a `conversiones.py` si los dos están en la misma carpeta.

| Carpeta | Qué muestra | Cómo se ejecuta |
|---|---|---|
| [temperaturas_modulos/0_name/](temperaturas_modulos/0_name/) | La variable `__name__`. `saludo.py` imprime `__main__` cuando se ejecuta solo, y `saludo` cuando lo importa `principal.py`. | `python saludo.py` y `python principal.py` |
| [temperaturas_modulos/1_sin_guarda/](temperaturas_modulos/1_sin_guarda/) | Las pruebas al final de `conversiones.py`, **sin guarda**. Como `import` ejecuta todo el módulo, al abrir el menú aparece `Pruebas de conversiones: todas pasaron`. Es un efecto secundario intencional, para mostrar el problema. | `python main.py` |
| [temperaturas_modulos/2_con_guarda/](temperaturas_modulos/2_con_guarda/) | **Opción 1**: las pruebas dentro de `if __name__ == "__main__":`, que solo se ejecutan al correr `conversiones.py` directamente. `main.py` agrupa el programa en `def main()` con su propia guarda. | `python conversiones.py` (pruebas) y `python main.py` (menú) |
| [temperaturas_modulos/3_archivo_pruebas/](temperaturas_modulos/3_archivo_pruebas/) | **Opción 2**: `conversiones.py` solo tiene funciones, y las pruebas están en `test_conversiones.py`. Es la organización que se usa desde el [laboratorio 4](../../../../laboratorios/4/). | `python test_conversiones.py` (pruebas) y `python main.py` (menú) |

---

## 3. Seno por serie de Taylor

### Enunciado

> Escriba una función `seno(x, n)` que aproxime el seno de un ángulo `x`, en radianes, sumando los primeros `n` términos de la serie de Taylor:
>
> $$
> \mathrm{sen}(x) = \sum_{k=0}^{n-1} (-1)^k \frac{x^{2k+1}}{(2k+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots
> $$
>
> El factorial se calcula con una función aparte, `factorial(n)`. Si no se indica `n`, se usan 10 términos. Compare el resultado con la función `math.sin` de la librería `math`.

*(Enunciado redactado a partir del código y de las diapositivas 25-27 y 42).*

### Archivos

| Archivo | Qué muestra |
|---|---|
| [seno.py](seno.py) | Una **función que llama a otra** (`seno` usa `factorial`) y un **parámetro con valor por defecto** (`n=10`). Imprime `seno(1.0)` con 10 términos (`0.8414709848078965`, que coincide con el valor real) y con 3 (`0.8416666666666667`), y una llamada con **argumentos por nombre**: `seno(n=3, x=1.0)`. |
| [seno_vs_math.py](seno_vs_math.py) | Una **función propia frente a una de librería**: `seno(1.0)` y `math.sin(1.0)` dan el mismo resultado. Muestra también el error que no produce mensaje: `math.sin(30)` interpreta 30 en radianes y da `-0.988`, mientras que `math.sin(math.radians(30))` da 0.5, el seno de 30°. |

---

## 4. Adivina el número

### Enunciado

> El programa elige un número entero al azar entre 1 y 100, y el usuario intenta adivinarlo con las pistas *mayor* o *menor*. Aplique el procedimiento completo: entender, diseñar (top-down), especificar, implementar con stubs y probar con `random.seed()`.

*(Diapositiva 46).*

### Archivos

| Carpeta | Qué contiene |
|---|---|
| [adivina_numero/](adivina_numero/) | Ejercicio guiado de repaso, con su propia guía ([README](adivina_numero/README.md)): diagrama top-down, especificación, archivo de partida con stubs (`adivina_numero_actividad.py`), solución de referencia (`adivina_numero.py`) y, en la sección 7, el programa dividido en módulos (`modulos_actividad/`). |

> [!WARNING]
> No nombre ningún archivo `random.py`: `import random` cargaría ese archivo en lugar del módulo de Python, y aparecería el error `AttributeError: module 'random' has no attribute 'randint'`.

---

## 5. Notas mayores que el promedio

### Enunciado

> Leer las notas de los estudiantes de un curso y mostrar **cuántas notas son mayores que el promedio**.

*(Diapositiva 56).*

### Archivos

| Archivo | Qué muestra |
|---|---|
| [notas_sin_arreglos.py](notas_sin_arreglos.py) | Un problema que **todavía no se puede resolver bien**. El programa lee las notas y calcula el promedio, pero el promedio solo se conoce después de leer todas las notas, y para entonces la variable `nota` solo conserva la última. Con 4 estudiantes (3.0, 4.5, 2.0, 4.0) muestra `Promedio del curso: 3.38` y `Nota guardada en la variable nota: 4.0`. |

**Pregunta para pensar:** ¿cómo se compara cada nota con el promedio, si las anteriores ya se perdieron? ¿Qué pasaría si el curso tuviera 40 estudiantes y se usaran 40 variables? La respuesta es el tema de la próxima clase: los **arreglos**.

---

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
