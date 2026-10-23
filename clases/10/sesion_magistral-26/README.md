![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 26

* **Tipo**: Presencial
* **Fecha**: 20/10/2026
* **Parte**: Primer bloque de clase (14-16)

## Resumen

Tercera sesión de la [clase 10](../README.md). Retoma lo que quedó pendiente en la [sesión 24](../sesion_magistral-24/README.md#lo-que-quedó-pendiente-de-un-archivo-a-varios): llevar el programa de conversión de temperaturas de **un solo archivo** a **varios archivos**. Se usa otra vez el mismo programa, ya conocido, para que la atención quede en la organización del código y no en un problema nuevo.

El programa se construye primero con funciones provisionales (*stubs*) y pruebas escritas de antemano. Luego se completa hasta que todas las pruebas pasan, y finalmente se reparte en módulos que se importan entre sí. Un paréntesis con un ejemplo pequeño explica la **guarda** `if __name__ == "__main__":`, y el último paso, que no se hizo en clase, la aplica al programa de temperaturas.

| Paso | Archivo de esta página | Qué enseña |
|---|---|---|
| 1 | [`paso1_stubs.py`](codigo/paso1_stubs.py) | Armar el programa completo con *stubs* y escribir las pruebas antes que las funciones |
| 2 | [`paso2_un_archivo.py`](codigo/paso2_un_archivo.py) | Completar las funciones hasta que pasen las pruebas, y por qué no conviene dejarlo todo en un archivo |
| 3 | [`paso3_varios_archivos/`](codigo/paso3_varios_archivos/) | Repartir el programa en módulos y usarlos con `import` |
| Paréntesis | [`parentesis_guarda/`](codigo/parentesis_guarda/) | La variable `__name__` y la guarda: ejecutar un archivo no es lo mismo que importarlo |
| 4 | [`paso4_main_y_guarda/`](codigo/paso4_main_y_guarda/) | `def main()` y la guarda en el programa de temperaturas, más una opción nueva en el menú (**no se hizo en clase**) |

> [!TIP]
> **Si no asistió a clase**, siga esta ruta:
> 1. Si no vio la sesión 24, lea su [paso 3](../sesion_magistral-24/README.md#paso-3--buenas-prácticas-y-especificación): ahí se explican la especificación (*Supone / Garantiza*) y la validación con `continue`, que esta sesión da por conocidas.
> 2. Recorra los pasos en orden. En cada uno: lea la sección, ejecute los archivos de ese paso y compárelos con los del paso anterior. La lista **Qué cambia** al inicio de cada paso le dice qué buscar.
> 3. Desde el paso 3, un programa ya no es un archivo sino una **carpeta**. Al descargar los archivos, conserve la estructura de carpetas que muestra el diagrama de cada paso.
> 4. Resuelva los [ejercicios de práctica](#ejercicios-de-práctica) antes de ver las soluciones.

**Contenido de esta página:**

* [Paso 1 — Empezar con stubs](#paso-1--empezar-con-stubs)
* [Paso 2 — Completar las funciones hasta que pasen las pruebas](#paso-2--completar-las-funciones-hasta-que-pasen-las-pruebas)
* [Paso 3 — De un archivo a varios](#paso-3--de-un-archivo-a-varios)
* [Paréntesis: ejecutar o importar](#paréntesis-ejecutar-o-importar)
* [Paso 4 — `main()` y la guarda en el programa de temperaturas](#paso-4--main-y-la-guarda-en-el-programa-de-temperaturas)
* [Ejercicios de práctica](#ejercicios-de-práctica)
* [Recomendaciones de otros cursos](#recomendaciones-de-otros-cursos)
* [Para explorar por su cuenta](#para-explorar-por-su-cuenta)
* [Archivos](#archivos)

## Paso 1 — Empezar con stubs

En la [sesión 24](../sesion_magistral-24/README.md) primero se escribieron las funciones de conversión y después sus pruebas. Esta vez se empieza al revés: el programa se arma completo desde el principio, con funciones **provisionales**, y el cálculo se completa después.

Un **stub** es una función provisional. Ya tiene su nombre, sus parámetros y su especificación definitivos, pero su cuerpo todavía no hace el cálculo: devuelve un valor fijo.

```python
def celsius_a_fahrenheit(temp_c):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Supone:
        temp_c es un número (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en grados Fahrenheit (float).
    """
    # PENDIENTE: implementar
    return 0.0
```

¿Para qué sirve una función que da un resultado incorrecto? Para que el resto del programa ya se pueda escribir. El programa principal solo necesita saber **qué** hace cada función (su especificación), no **cómo** lo hace. Con los stubs, el menú, la lectura de datos y la salida quedan escritos desde el inicio.

> [!NOTE]
> Esta forma de trabajar se llama **diseño top-down** (de arriba hacia abajo): primero se escribe el programa principal y después las funciones que necesita. Se explica completa, con el diagrama del problema dividido en partes, en la [teoría de la clase 10](../teoria/README.md#contenido-cubierto).

### Primero el plan, después el código

En [`paso1_stubs.py`](codigo/paso1_stubs.py) también están escritas, desde el principio, las pruebas con `assert`. Antes de escribir una sola prueba se decide **qué debe pasar**: para cada caso, qué recibe la función, qué debe devolver y de qué tipo es el caso. Las pruebas no se inventan al final: son la traducción a Python de este plan.

| Función | Entrada | Resultado esperado | Tipo | Prueba en Python |
|---|---|---|---|---|
| `celsius_a_fahrenheit` | `5` | `41` | Típico | `assert celsius_a_fahrenheit(5) == 41` |
| | `1` | `33.8` | Típico | `assert round(celsius_a_fahrenheit(1), 1) == 33.8` |
| | `1.5` | `34.7` | Típico (dato decimal) | `assert round(celsius_a_fahrenheit(1.5), 1) == 34.7` |
| | `100` | `212.00` | Típico (ebullición) | `assert round(celsius_a_fahrenheit(100), 2) == 212.00` |
| | `0` | `32.00` | Típico (congelación) | `assert round(celsius_a_fahrenheit(0), 2) == 32.00` |
| | `37` | `98.60` | Típico (temperatura corporal) | `assert round(celsius_a_fahrenheit(37), 2) == 98.60` |
| | `-40` | `-40.00` | Especial (las escalas coinciden) | `assert round(celsius_a_fahrenheit(-40), 2) == -40.00` |
| `celsius_a_kelvin` | `10` | `283.15` | Típico | `assert round(celsius_a_kelvin(10), 2) == 283.15` |
| | `-20` | `253.15` | Típico (temperatura negativa) | `assert round(celsius_a_kelvin(-20), 2) == 253.15` |
| | `-273.15` | `0.00` | Límite (cero absoluto) | `assert round(celsius_a_kelvin(-273.15), 2) == 0.00` |

Cada fila de la tabla es una línea de pruebas en el archivo. Se usa `round()` porque los números reales no siempre son exactos: `celsius_a_fahrenheit(37)` devuelve `98.60000000000001` (vea la [sesión 24](../sesion_magistral-24/README.md#casos-de-prueba-1)). En la tabla se omiten los mensajes opcionales que llevan algunos `assert` en el archivo.

Esas pruebas son la **meta**: el programa está terminado cuando todas pasan. Por ahora, con los stubs, el programa ni siquiera llega al menú:

```text
Traceback (most recent call last):
  File "paso1_stubs.py", line 57, in <module>
    assert celsius_a_fahrenheit(5) == 41                                          # tipico
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

El error no es una mala noticia: es información. **Las pruebas dicen qué falta por hacer.**

## Paso 2 — Completar las funciones hasta que pasen las pruebas

**Qué cambia respecto al paso 1:**

* Los stubs se reemplazan, uno a la vez, por el cálculo real.
* Las pruebas y el programa principal **no cambian**.

Cada vez que se ejecuta el archivo, la primera prueba que falla dice qué sigue:

| Estado del archivo | Qué muestra Python | Qué indica |
|---|---|---|
| Las dos funciones son stubs | `AssertionError` en la línea 57: `assert celsius_a_fahrenheit(5) == 41` | Falta implementar `celsius_a_fahrenheit` |
| `celsius_a_fahrenheit` implementada; `celsius_a_kelvin` todavía es stub | `AssertionError: El resultado es 283.15` en la línea 66 | Fahrenheit ya pasa sus siete pruebas; falta Kelvin |
| Las dos implementadas ([`paso2_un_archivo.py`](codigo/paso2_un_archivo.py)) | `Todas las pruebas pasaron` y enseguida el menú | El programa está listo |

Las pruebas no solo avisan lo que **falta**, también lo que está **mal**: si al implementar `celsius_a_fahrenheit` se olvida el `+ 32`, Python muestra el mismo `AssertionError` de la línea 57 que con el stub.

Con todas las pruebas superadas, el programa funciona:

```text
Todas las pruebas pasaron
Programa de conversion de °C a °F y °K
--------------------------------
1. °C a °F
2. °C a °K
3. Salir

Elija una opcion: 1
Digite la temperatura en °C: 100
100.0°C = 212.00°F

--------------------------------
1. °C a °F
2. °C a °K
3. Salir

Elija una opcion: 3
Gracias por usarnos
```

### ¿Todo en un solo archivo?

El programa funciona, pero tiene un inconveniente: **cada vez que se ejecuta para usarlo, primero corren todas las pruebas**. A quien quiere convertir una temperatura no le interesan las pruebas, y si una fallara, el programa ni siquiera arrancaría. Las pruebas son para quien **escribe** las funciones; el menú es para quien **usa** el programa.

El archivo ya está dividido en cuatro zonas, marcadas con comentarios: constantes, funciones, pruebas y programa principal. Esas zonas son los cortes del paso siguiente.

## Paso 3 — De un archivo a varios

**Qué cambia respecto al paso 2:**

* Las zonas del archivo se reparten en cuatro archivos, todos en la **misma carpeta**.
* `main.py` importa las funciones que usa.
* Se agrega una función nueva, `kelvin_a_celsius`, con sus pruebas.
* Las demás funciones, sus pruebas y el programa principal **no cambian**.

Hasta el paso 2, el programa era un solo archivo:

```text
📄 paso2_un_archivo.py — constantes, funciones, pruebas y programa principal
```

Desde este paso, el programa es una **carpeta** con varios archivos que trabajan juntos:

```text
📁 paso3_varios_archivos/
├── 📄 conversion.py — módulo: funciones de cálculo
├── 📄 pantalla.py — módulo: funciones que muestran información
├── 📄 test_conversion.py — se ejecuta para PROBAR
└── 📄 main.py — se ejecuta para USAR el programa
```

| Archivo | Zona del paso 2 que recibe | Para qué se ejecuta |
|---|---|---|
| [`conversion.py`](codigo/paso3_varios_archivos/conversion.py) | Funciones de conversión | No se ejecuta: otros archivos lo importan |
| [`pantalla.py`](codigo/paso3_varios_archivos/pantalla.py) | `mostrar_menu()` | No se ejecuta: otros archivos lo importan |
| [`test_conversion.py`](codigo/paso3_varios_archivos/test_conversion.py) | Pruebas | Para **probar** las funciones |
| [`main.py`](codigo/paso3_varios_archivos/main.py) | Constantes y programa principal | Para **usar** el programa |

Un archivo `.py` cuyas funciones se usan desde otro archivo se llama **módulo**. Repartir las funciones en módulos organiza el código: cada módulo agrupa funciones **relacionadas entre sí**. `conversion.py` reúne las que calculan conversiones, y `pantalla.py` las que muestran algo al usuario. Así, para cambiar cómo se ve el menú se abre `pantalla.py`, y para corregir un cálculo se abre `conversion.py`.

Ahora quien usa el programa ejecuta `main.py` y ve el menú de inmediato, sin pruebas. Quien escribe las funciones ejecuta `test_conversion.py`:

```text
Pruebas de conversion: todas pasaron
```

En el módulo quedó también una función nueva, `kelvin_a_celsius`. Agregarla solo tocó dos archivos: la función fue a `conversion.py` y sus pruebas a `test_conversion.py`. `main.py` no cambió. Sus casos de prueba siguen el mismo plan del paso 1:

| Función | Entrada | Resultado esperado | Tipo | Prueba en Python |
|---|---|---|---|---|
| `kelvin_a_celsius` | `500` | `226.85` | Típico | `assert round(kelvin_a_celsius(500), 2) == 226.85` |
| | `3.15` | `-270.00` | Típico (dato decimal) | `assert round(kelvin_a_celsius(3.15), 2) == -270.00` |
| | `0` | `-273.15` | Límite (cero absoluto) | `assert round(kelvin_a_celsius(0), 2) == -273.15` |

### ¿Cómo usa `main.py` las funciones de otro archivo? `import`

Para usar las funciones de un módulo hay que **importarlas**, con el nombre del archivo sin `.py`. Hay varias formas:

| Forma | Cómo se llama la función | Comentario |
|---|---|---|
| `import conversion` | `conversion.celsius_a_fahrenheit(temp_c)` | El prefijo dice de dónde viene la función, como en `math.sqrt()` |
| `from conversion import celsius_a_fahrenheit, celsius_a_kelvin` | `celsius_a_fahrenheit(temp_c)` | **La que quedó en clase**: se nombra cada función que se va a usar |
| `from conversion import *` | `celsius_a_fahrenheit(temp_c)` | No se recomienda: trae todo sin decir qué, y puede reemplazar sin aviso una función con el mismo nombre |

Con la forma que quedó, el programa principal es **idéntico** al del paso 2: solo se agregan dos líneas al inicio de `main.py`.

```python
from conversion import celsius_a_fahrenheit, celsius_a_kelvin
from pantalla import mostrar_menu
```

Observe que `main.py` no importa `kelvin_a_celsius`: solo se importa lo que se va a usar.

> [!WARNING]
> Los archivos deben estar en la misma carpeta. Si no, `main.py` falla con `ModuleNotFoundError: No module named 'conversion'`.

Después de ejecutar `main.py` o `test_conversion.py`, en la carpeta aparece algo que nadie escribió:

```text
📁 paso3_varios_archivos/
├── 📁 __pycache__/ — la crea Python al importar: no se edita ni se entrega
│   ├── conversion.cpython-311.pyc
│   └── pantalla.cpython-311.pyc
├── 📄 conversion.py
├── 📄 pantalla.py
├── 📄 test_conversion.py
└── 📄 main.py
```

Python guarda en `__pycache__/` una versión traducida de cada módulo **importado**, para cargarlo más rápido la próxima vez. Por eso aparecen `conversion` y `pantalla`, pero no `main` ni `test_conversion`, que se ejecutaron sin que nadie los importara. El número del nombre (`311`) es la versión de Python, así que puede ser distinto en su computador. La carpeta se puede borrar sin problema: Python la vuelve a crear.

## Paréntesis: ejecutar o importar

Antes de terminar el programa de temperaturas, un paréntesis con un ejemplo más pequeño, para ver qué ocurre cuando un archivo se **ejecuta** y cuando se **importa**.

En el paso 3, cada archivo tiene un papel fijo: `conversion.py` y `pantalla.py` solo se importan, y `main.py` y `test_conversion.py` solo se ejecutan. Pero un mismo archivo puede necesitar las dos cosas. Por ejemplo, un módulo con sus pruebas al final: las pruebas deberían correr al ejecutarlo, pero no al importarlo, porque `import` ejecuta **todo** el archivo, de arriba hacia abajo.

Para distinguir los dos casos, Python le da a cada archivo una variable especial, `__name__`:

| Cómo se usa el archivo | Valor de `__name__` |
|---|---|
| Se ejecuta directamente (▶ en Spyder, o `python saludos.py`) | `"__main__"` |
| Otro archivo lo importa | El nombre del módulo, sin `.py`: `"saludos"` |

El ejemplo es una carpeta aparte, con dos archivos:

```text
📁 parentesis_guarda/
├── 📄 saludos.py — módulo: define hola()
└── 📄 principal.py — importa saludos y llama a hola()
```

Al ejecutar [`saludos.py`](codigo/parentesis_guarda/saludos.py) directamente:

```text
En saludos.py, __name__ vale: __main__
Pruebas de saludos
```

Y al ejecutar [`principal.py`](codigo/parentesis_guarda/principal.py), que importa `saludos`:

```text
En saludos.py, __name__ vale: saludos
En principal.py, __name__ vale: __main__
hola que mas!!!
hola que mas!!!
hola que mas!!!
```

La línea `Pruebas de saludos` ya no aparece. Está dentro de la **guarda**, un `if` que pregunta si el archivo se está ejecutando directamente:

```python
if __name__ == "__main__":
    # Solo se ejecuta si se corre saludos.py directamente,
    # no cuando otro archivo lo importa. Aqui van las pruebas del modulo.
    print("Pruebas de saludos")
```

Cada archivo tiene su propia guarda, y cada una protege algo distinto:

| Archivo | Qué protege su guarda | Efecto |
|---|---|---|
| `saludos.py` (módulo) | Sus pruebas | Corren al ejecutarlo, no al importarlo |
| `principal.py` (programa principal) | Las llamadas a `hola()` | El programa solo arranca si se ejecuta directamente |

Los `print` de `__name__` están **fuera** de la guarda a propósito, para ver su valor en los dos casos. En un programa real no se escriben.

Volvamos al programa de temperaturas: en el paso 4 se le pone la guarda a `main.py`.

## Paso 4 — `main()` y la guarda en el programa de temperaturas

> [!NOTE]
> Este paso **no se hizo en clase**. Completa la idea de la sesión: aplica al programa de temperaturas lo visto en el paréntesis.

**Qué cambia respecto al paso 3** ([`paso4_main_y_guarda/`](codigo/paso4_main_y_guarda/)):

* El programa principal de `main.py` se agrupa en una función `main()`, que se llama dentro de la guarda.
* El menú tiene una opción nueva, **°K a °C**, que usa `kelvin_a_celsius`. La función ya estaba escrita y probada en el paso 3, pero `main.py` no la usaba.
* `conversion.py` y `test_conversion.py` no cambian.

```text
📁 paso4_main_y_guarda/
├── 📄 conversion.py — sin cambios
├── 📄 pantalla.py — ✏️ opción 3. °K a °C
├── 📄 test_conversion.py — sin cambios
└── 📄 main.py — ✏️ def main(), guarda y opción 3
```

```python
from conversion import celsius_a_fahrenheit, celsius_a_kelvin, kelvin_a_celsius
from pantalla import mostrar_menu

############ Constantes ############
CERO_ABSOLUTO = -273.15  # °C
CERO_ABSOLUTO_K = 0.0    # °K


############ Programa principal #########
def main():
    print("Programa de conversion de temperaturas")
    while True:
        ...
        elif opc == 3:
            # K --> C
            temp_k = float(input("Digite la temperatura en °K: "))
            if temp_k < CERO_ABSOLUTO_K:
                print("ERROR: Temperatura invalida")
                continue
            temp_c = kelvin_a_celsius(temp_k)
            print(f"{temp_k}°K = {temp_c:.2f}°C\n")
        ...


if __name__ == "__main__":
    main()
```

Para agregar la opción se tocaron tres partes del programa, y cada cambio fue al módulo que le corresponde:

| Cambio | Dónde |
|---|---|
| Mostrar la opción `3. °K a °C` (Salir pasa a ser la 4) | `pantalla.py` |
| Importar `kelvin_a_celsius` y atender la opción 3 | `main.py` |
| Validar el dato antes de llamar a la función, con la constante `CERO_ABSOLUTO_K` | `main.py` |

Como en la sesión 24, el programa principal valida la temperatura **antes** de invocar la función, para cumplir lo que `kelvin_a_celsius` **supone**: un valor mayor o igual a 0.

```text
Elija una opcion: 3
Digite la temperatura en °K: -5
ERROR: Temperatura invalida
--------------------------------
1. °C a °F
2. °C a °K
3. °K a °C
4. Salir

Elija una opcion: 3
Digite la temperatura en °K: 300
300.0°K = 26.85°C
```

### Casos de prueba del programa principal

Estos casos **no** se pueden escribir con `assert`, porque dependen de lo que el usuario escribe y de lo que el programa muestra en pantalla. Se revisan ejecutando `main.py`:

| Opción | Entrada | Salida esperada | Tipo |
|---|---|---|---|
| 1 | `100` | `100.0°C = 212.00°F` | Típico |
| 1 | `-40` | `-40.0°C = -40.00°F` | Especial (las escalas coinciden) |
| 2 | `25` | `25.0°C = 298.15°K` | Típico |
| 2 | `-273.15` | `-273.15°C = 0.00°K` | Límite (cero absoluto) |
| 2 | `-300` | `ERROR: Temperatura invalida` y vuelve el menú | Especial (no cumple el contrato) |
| 3 | `300` | `300.0°K = 26.85°C` | Típico (opción nueva) |
| 3 | `0` | `0.0°K = -273.15°C` | Límite (cero absoluto) |
| 3 | `-5` | `ERROR: Temperatura invalida` y vuelve el menú | Especial (no cumple el contrato) |
| 9 | — | `ERROR: Opcion no valida` | Especial (opción inexistente) |
| 4 | — | `Gracias por usarnos` | Salida del programa |

### La estructura final

Con la guarda, si otro archivo importa `main.py`, el menú no arranca. El programa queda así:

| Archivo | Contenido | Se ejecuta para… |
|---|---|---|
| `conversion.py` | Solo funciones de cálculo, con su especificación | — (se importa) |
| `pantalla.py` | Solo funciones que muestran información | — (se importa) |
| `test_conversion.py` | Pruebas con `assert` de `conversion.py` | Probar |
| `main.py` | `import` → constantes → `def main()` → guarda | Usar el programa |

Es la forma recomendada de organizar un programa de aquí en adelante, y la que se usa en el [laboratorio 4](../../../laboratorios/4/README.md): un módulo con funciones, un `test_<modulo>.py` y un `main.py`.

> [!NOTE]
> El programa escribe `°K`, como se hizo en clase, pero la forma correcta es `K`, sin el símbolo de grado: el Kelvin es una escala absoluta y no se escribe con `°`, a diferencia de `°C` y `°F`.

## Ejercicios de práctica

Intente cada ejercicio antes de abrir la solución. Trabaje sobre una **copia** de la carpeta [`paso4_main_y_guarda/`](codigo/paso4_main_y_guarda/).

### Ejercicio 1: una conversión nueva, de punta a punta

Agregue al programa la opción **°F a °C**. Use la función `fahrenheit_a_celsius(temp_f)` del [ejercicio 2 de la sesión 24](../sesion_magistral-24/README.md#ejercicio-2-una-función-nueva-con-su-contrato), o escríbala usted, con su especificación. Antes de programar, responda: ¿qué archivos hay que modificar, y qué va en cada uno? ¿Cuál es el menor valor válido en grados Fahrenheit?

<details>
<summary>Solución</summary>

Se modifican los cuatro archivos, y cada cambio va al que le corresponde. El menor valor válido es el cero absoluto en grados Fahrenheit: $-273.15 \cdot \frac{9}{5} + 32 = -459.67$.

**`conversion.py`**: la función, con su especificación.

```python
def fahrenheit_a_celsius(temp_f):
    """
    Convierte una temperatura de grados Fahrenheit a grados Celsius.

    Supone:
        temp_f es un número (int o float) mayor o igual a -459.67
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en grados Celsius (float),
        mayor o igual a -273.15.
    """
    temp_c = (temp_f - 32) * 5/9
    return temp_c
```

**`test_conversion.py`**: se agrega la función al `from ... import` y sus pruebas, antes del mensaje final.

```python
from conversion import celsius_a_fahrenheit, celsius_a_kelvin, kelvin_a_celsius, fahrenheit_a_celsius
...
# fahrenheit_a_celsius
assert round(fahrenheit_a_celsius(212), 2) == 100.00                          # tipico (ebullicion)
assert round(fahrenheit_a_celsius(98.6), 2) == 37.00                          # tipico (temperatura corporal)
assert round(fahrenheit_a_celsius(-459.67), 2) == -273.15                     # limite (cero absoluto)
assert round(fahrenheit_a_celsius(-40), 2) == -40.00                          # especial (las escalas coinciden)
```

**`pantalla.py`**: la opción nueva en el menú; Salir pasa a ser la 5.

```python
    print("3. °K a °C")
    print("4. °F a °C")
    print("5. Salir")
```

**`main.py`**: el `import`, una constante para validar y la opción 4. La opción de salida pasa a ser `opc == 5`.

```python
from conversion import celsius_a_fahrenheit, celsius_a_kelvin, kelvin_a_celsius, fahrenheit_a_celsius
...
CERO_ABSOLUTO_F = -459.67  # °F
...
        elif opc == 4:
            # F --> C
            temp_f = float(input("Digite la temperatura en °F: "))
            if temp_f < CERO_ABSOLUTO_F:
                print("ERROR: Temperatura invalida")
                continue
            temp_c = fahrenheit_a_celsius(temp_f)
            print(f"{temp_f}°F = {temp_c:.2f}°C\n")
        elif opc == 5:
            print("Gracias por usarnos\n")
            break
```

Con la opción 4: `212` → `212.0°F = 100.00°C`, `-459.67` → `-459.67°F = -273.15°C`, y `-500` → `ERROR: Temperatura invalida`.

</details>

### Ejercicio 2: el módulo que no aparece

En su copia, cree dentro de la carpeta una subcarpeta llamada `otra` y mueva allí `pantalla.py`, para que quede así:

```text
📁 paso4_main_y_guarda/
├── 📁 otra/
│   └── 📄 pantalla.py
├── 📄 conversion.py
├── 📄 test_conversion.py
└── 📄 main.py
```

Antes de ejecutar `main.py`, prediga: ¿el programa arranca? ¿Qué mensaje muestra Python, y en qué línea? ¿Y si ejecuta `test_conversion.py`?

<details>
<summary>Solución</summary>

`main.py` no arranca. Python busca `pantalla.py` en la carpeta de `main.py`, no lo encuentra y se detiene en la línea del `import`:

```text
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    from pantalla import mostrar_menu
ModuleNotFoundError: No module named 'pantalla'
```

`test_conversion.py`, en cambio, funciona: solo importa `conversion`, que sigue en su lugar. Para corregir el error, devuelva `pantalla.py` a la misma carpeta de `main.py`.

</details>

## Recomendaciones de otros cursos

Estas recomendaciones vienen de cursos y documentación en los que se apoya este curso. Cada una explica por qué esta sesión hizo las cosas como las hizo. Las citas son traducciones libres.

| Recomendación | Dónde aparece en esta sesión | Fuente |
|---|---|---|
| **Una función que retorna su resultado se puede probar; una que lo imprime, no.** CS50P cambia una función `hello` que imprimía un saludo para que lo **retorne**, y así poder probarla. | `conversion.py` retorna y no imprime, por eso tiene pruebas. `pantalla.py` imprime, por eso no las tiene. | CS50P, Lecture 5, [*Testing Strings*](https://cs50.harvard.edu/python/notes/5/#testing-strings) |
| **Las pruebas van en un archivo aparte, cuyo nombre empieza por `test_`.** Así lo hace CS50P con `test_calculator.py`. Es la convención que reconoce `pytest`, la herramienta de pruebas que se usa en la industria. | `test_conversion.py` (paso 3) | CS50P, Lecture 5, [*pytest*](https://cs50.harvard.edu/python/notes/5/#pytest) |
| **Un módulo propio es una librería más.** CS50P crea `sayings.py`, un archivo con funciones que "por sí solo no hace nada por el usuario": sirve para que otro programa lo importe. | `conversion.py` y `pantalla.py` (paso 3) | CS50P, Lecture 4, [*Making Your Own Libraries*](https://cs50.harvard.edu/python/notes/4/#making-your-own-libraries) |
| **`from` permite importar solo lo que se necesita.** "`from` nos permite ser muy específicos sobre lo que queremos importar". | `from conversion import celsius_a_fahrenheit, celsius_a_kelvin` (paso 3) | CS50P, Lecture 4, [*Random*](https://cs50.harvard.edu/python/notes/4/#random) |
| **Evite `from modulo import *`.** "Las importaciones con comodín deben evitarse, porque no dejan claro qué nombres están presentes". | La forma no recomendada de la tabla del paso 3 | PEP 8, guía de estilo de Python, [*Imports*](https://peps.python.org/pep-0008/#imports) |
| **Los nombres de los módulos son cortos y en minúscula**; se puede usar guion bajo si mejora la lectura. No use espacios ni guiones (`-`): un archivo `mi-modulo.py` no se puede importar. | `conversion`, `pantalla`, `test_conversion` | PEP 8, [*Package and Module Names*](https://peps.python.org/pep-0008/#package-and-module-names) |
| **Dentro de la guarda van las menos instrucciones posible: normalmente, solo la llamada a `main()`.** Si el programa se escribe directamente dentro de la guarda, sus variables quedan **globales** para todo el archivo, y una función podría usar una de ellas por error en lugar de una variable local. | `main()` dentro de la guarda (paso 4). El riesgo es el de las variables globales que se vio en la [sesión 25](../sesion_magistral-25/README.md) | Documentación de Python, [`__main__`: *Idiomatic Usage*](https://docs.python.org/3/library/__main__.html#idiomatic-usage) |
| **`__pycache__/` se mantiene sola.** Python compara la fecha de modificación de cada módulo con su versión guardada y la vuelve a generar si cambió. Solo hace que el módulo **cargue** más rápido; el programa no se ejecuta más rápido. | La carpeta `__pycache__/` del paso 3 | Tutorial de Python, [*"Compiled" Python files*](https://docs.python.org/3/tutorial/modules.html#compiled-python-files) |

## Para explorar por su cuenta

Esta sección no se vio en clase.

* **Las pruebas dentro del módulo, con guarda.** En este programa las pruebas están en un archivo aparte. La otra opción es dejarlas al final de `conversion.py`, dentro de `if __name__ == "__main__":`, como en el paréntesis. Compare las dos formas en las carpetas [`2_con_guarda`](../teoria/codigo/temperaturas_modulos/2_con_guarda/) y [`3_archivo_pruebas`](../teoria/codigo/temperaturas_modulos/3_archivo_pruebas/) de la teoría; la tabla que las compara está en la [teoría de la clase 10](../teoria/README.md#contenido-cubierto) (sección "¿Dónde se ubican las pruebas?").
* **Consultar la especificación de una función importada.** Desde la consola de Spyder, ubicada en la carpeta del programa:

  ```text
  >>> from conversion import kelvin_a_celsius
  >>> help(kelvin_a_celsius)
  Help on function kelvin_a_celsius in module conversion:

  kelvin_a_celsius(temp_k)
      Convierte una temperatura de Kelvin a grados Celsius.
      ...
  ```

  Observe que `help()` dice de qué módulo viene la función. Así se usa una función que otra persona escribió: leyendo su especificación, sin abrir su código.
* **Otro programa completo en varios archivos.** El ejercicio guiado [adivina el número](../teoria/codigo/adivina_numero/README.md#7-organizar-el-programa-en-varios-archivos) recorre el mismo camino, de un archivo a varios, con un problema nuevo.

## Archivos

```text
📁 sesion_magistral-26/
├── 📁 codigo/ — versiones revisadas, las que se usan en esta página
│   ├── 📄 paso1_stubs.py
│   ├── 📄 paso2_un_archivo.py
│   ├── 📁 paso3_varios_archivos/
│   │   ├── 📄 conversion.py
│   │   ├── 📄 pantalla.py
│   │   ├── 📄 test_conversion.py
│   │   └── 📄 main.py
│   ├── 📁 parentesis_guarda/
│   │   ├── 📄 saludos.py
│   │   └── 📄 principal.py
│   └── 📁 paso4_main_y_guarda/ — no se hizo en clase
│       ├── 📄 conversion.py
│       ├── 📄 pantalla.py
│       ├── 📄 test_conversion.py
│       └── 📄 main.py
└── 📁 ejemplos_sin_editar/ — los archivos tal como se escribieron en clase
```

| Archivo | Descripción |
|---|---|
| [`codigo/paso1_stubs.py`](codigo/paso1_stubs.py) | Paso 1: el programa completo con las conversiones como stubs; se detiene en la primera prueba |
| [`codigo/paso2_un_archivo.py`](codigo/paso2_un_archivo.py) | Paso 2: el programa terminado en un solo archivo; todas las pruebas pasan |
| [`codigo/paso3_varios_archivos/`](codigo/paso3_varios_archivos/) | Paso 3: `conversion.py`, `pantalla.py`, `test_conversion.py` y `main.py` |
| [`codigo/parentesis_guarda/`](codigo/parentesis_guarda/) | Paréntesis: `saludos.py` y `principal.py`, para ver el valor de `__name__` y el efecto de la guarda |
| [`codigo/paso4_main_y_guarda/`](codigo/paso4_main_y_guarda/) | Paso 4 (no se hizo en clase): el paso 3 con `def main()`, la guarda y la opción °K a °C |
| [`ejemplos_sin_editar/`](ejemplos_sin_editar/) | Los archivos tal como se escribieron en clase: `conversion.py` (stubs, paso 1), `mono_archivo/` (paso 2), `multi_archivo/` (paso 3) y `ejemplo/` (paréntesis) |

> [!NOTE]
> Los archivos de `codigo/` son versiones revisadas de los escritos en clase. Se quitaron los encabezados automáticos de Spyder y se agregó un comentario inicial que describe el paso. Además:
> * La constante se llama `CERO_ABSOLUTO` (en clase, `ZERO_ABSOLUTO`) y el parámetro de las funciones de un solo archivo se llama `temp_c` (en clase, `c`, aunque la especificación ya hablaba de `temp_c`).
> * Se alinearon los comentarios de las pruebas, indicando el tipo de cada caso, y se agregó la prueba del cero absoluto de `celsius_a_kelvin`.
> * `kelvin_a_celsius` tiene su especificación completa (en clase quedó en blanco), y `test_conversion.py` muestra un solo mensaje al final (en clase, dos).
> * En el paréntesis, los `print` que muestran `__name__` están activos (en clase quedaron comentados), y la guarda de `saludos.py` imprime `Pruebas de saludos` (en clase, `TESTS`).
>
> Los archivos de `ejemplos_sin_editar/` se conservan como referencia.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del código escrito en clase y de las diapositivas de la clase 10. El docente revisó y validó la versión final.
