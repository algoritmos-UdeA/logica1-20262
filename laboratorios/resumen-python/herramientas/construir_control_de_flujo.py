"""Contenido de control_de_flujo.ipynb (formato común en formato.py).

Los ejemplos originales del notebook se toman, por posición, de la versión con
la que se agregó la carpeta al repositorio (commit 2df6db3), mediante O(i).
Decisiones del docente (2026-10-19): los ejemplos de `for` sobre listas y
diccionarios van en "Para explorar" (con una explicación mínima; los métodos se
ven en POO), y `actor.lower()` se conserva explicando qué hace.

Uso, desde la raíz del repositorio:
    python laboratorios/resumen-python/herramientas/construir_control_de_flujo.py
"""
import json
import pathlib
import subprocess
import sys

sys.dont_write_bytecode = True  # no crear __pycache__ en el repositorio
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from formato import Notebook  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[3]
RUTA = "laboratorios/resumen-python/estructurada_python/control_de_flujo.ipynb"
orig = json.loads(subprocess.run(["git", "show", f"2df6db3:{RUTA}"], cwd=RAIZ, capture_output=True,
                                 check=True).stdout.decode("utf-8"))


def O(i):
    """Fuente de la celda i del notebook original."""
    return "".join(orig["cells"][i]["source"])


nb = Notebook("control_de_flujo.ipynb")
nb.insignias()
nb.encabezado(
    titulo="Control de flujo",
    intro=("Este notebook es un **refuerzo de Python** sobre las estructuras que permiten a un programa "
           "**tomar decisiones** (`if`, `elif`, `else`) y **repetir instrucciones** (`while`, `for`, con "
           "`break` y `continue`). Aquí no se repite la teoría: el foco está en **cómo se escriben y cómo "
           "se comportan** en Python, con ejemplos que puede ejecutar y modificar."),
    antes_de_empezar=("Este notebook supone que ya sabe usar variables, `print`, `input`, f-strings y los "
                      "operadores relacionales (`<`, `==`, ...) y lógicos (`and`, `or`, `not`) de Python. Si "
                      "necesita repasarlos, están en el notebook *Repaso básico de Python* de esta misma "
                      "carpeta. Lo demás que se usa aquí se explica aquí."),
    objetivos=[
        "Escribir bloques `if`, `if-else` e `if-elif-else` con la sintaxis de Python (dos puntos y sangría) y predecir cuál de ellos se ejecuta.",
        "Repetir instrucciones con `while`, cuidando la inicialización, la condición y la actualización para no crear un ciclo infinito.",
        "Interrumpir un ciclo con `break` o saltar una vuelta con `continue`, y explicar en qué se diferencian.",
        "Recorrer un texto con `for` y generar sucesiones de números con `range()`, sabiendo que el límite final no se incluye.",
        "Escribir ciclos anidados y predecir cuántas veces se ejecuta cada instrucción.",
        "Asignar varios valores a la vez con desempaquetado.",
        "Reconocer los errores frecuentes de estas estructuras (`SyntaxError`, `IndentationError`, `NameError`, `TypeError`, `ValueError`) y el ciclo infinito.",
    ],
)

# ---------------------------------------------------------------- bloques
nb.md("""
## Bloques y sangría

En Python, las instrucciones que dependen de un `if`, un `while` o un `for` forman un **bloque**. La sintaxis tiene dos reglas:

1. La línea que abre el bloque (`if ...`, `while ...`, `for ...`, `else`) termina en **dos puntos** (`:`).
2. Las instrucciones del bloque van **sangradas**: corridas hacia la derecha con espacios. El bloque termina en la primera línea que vuelve al margen anterior.

No hay llaves `{ }` ni palabras como `Fin_Si`: **la sangría es la que dice dónde empieza y dónde termina cada bloque**. Colab y Jupyter sangran solos la línea siguiente cuando usted escribe `:` y presiona `Enter`.
""")
nb.code('''
nota = 4.2
if nota >= 3.0:
    print("Aprobo")            # dentro del if
    print("Felicitaciones")    # dentro del if
print("Fin")                   # fuera del if: se ejecuta siempre
''')
nb.convencion("Use **4 espacios** por nivel de sangría (es lo que recomienda la guía de estilo PEP 8 y lo que ponen Colab y Jupyter). No mezcle espacios y tabulaciones.")
nb.prediga("`nota` vale 2.5. ¿Qué líneas se imprimen?")
nb.code('''
nota = 2.5
if nota >= 3.0:
    print("A")
    print("B")
print("C")
''')
nb.error("Si la línea que debía ir dentro del bloque queda pegada al margen, Python lanza `IndentationError: expected an indented block` (se esperaba un bloque sangrado).")
nb.code('''
nota = 4.2
if nota >= 3.0:
print("Aprobo")
''')
nb.error("Olvidar los dos puntos al final del `if`, `elif`, `else`, `while` o `for` da `SyntaxError: expected ':'`.")
nb.code('''
nota = 4.2
if nota >= 3.0
    print("Aprobo")
''')

# ---------------------------------------------------------------- condicionales
nb.md("""
## Condicionales: `if`, `elif`, `else`

### Estructura `if` simple

Se evalúa una condición y, si es verdadera, se ejecuta un bloque de código. Ejemplo:
""")
nb.code(O(6), entradas=["Ramon Valdez"])
nb.md("""
`actor.lower()` devuelve una copia del texto en **minúsculas**. Se usa porque la comparación con `==` distingue mayúsculas de minúsculas: así el programa reconoce el nombre aunque el usuario escriba `Ramon Valdez`, `RAMON VALDEZ` o `ramon valdez`. La notación `texto.operación()` se llama *método* y se explica en Programación Orientada a Objetos; por ahora basta con saber qué hace `.lower()`.
""")
nb.code('''
print("Ramon" == "ramon")
print("RAMON VALDEZ".lower())
print("RAMON VALDEZ".lower() == "ramon valdez")
''')
nb.md("""
### Estructura `if - else`

Se evalúa una condición. Si es verdadera, se ejecuta un bloque de código; si es falsa, se ejecuta el bloque del `else`. Ejemplo:
""")
nb.code(O(8), entradas=["15"])
nb.md("""
### Estructura `if - elif - else`

Se evalúan varias condiciones en secuencia. Si una es verdadera, se ejecuta su bloque. Si ninguna es verdadera, se ejecuta el bloque `else` (si existe). Ejemplo:
""")
nb.code(O(10), entradas=["4.3"])
nb.md("""
### Cómo funciona en Python: el orden de las condiciones

* Python revisa las condiciones **de arriba hacia abajo** y ejecuta **solo el primer bloque** cuya condición sea verdadera; los demás se saltan, aunque también sean verdaderos.
* El `else` no lleva condición: es lo que queda cuando todas las anteriores fueron falsas.
* Por eso el **orden** importa. En el ejemplo anterior, una nota de 4.3 cumple `nota >= 4` y también `nota >= 3`, pero solo se imprime `Excelente`, porque esa condición está primero.
""")
nb.prediga("Es el mismo ejemplo, con las dos condiciones en el orden contrario. ¿Qué imprime con `nota = 4.5`?")
nb.code('''
nota = 4.5
if nota >= 3:
    print("Bueno")
elif nota >= 4:
    print("Excelente")
else:
    print("Insuficiente")
''')
nb.md("""
El programa no da ningún error, pero la respuesta está mal: con este orden, el bloque `Excelente` **nunca** se puede ejecutar, porque toda nota mayor o igual que 4 ya cumplió la primera condición.

Tampoco es lo mismo escribir varios `if` seguidos que una cadena `if-elif`: los `if` separados se revisan **todos**, uno por uno.
""")
nb.prediga("¿Cuántas líneas se imprimen?")
nb.code('''
nota = 4.5
if nota >= 4:
    print("Excelente")
if nota >= 3:
    print("Bueno")
''')
nb.md("""
### Cómo funciona en Python: condiciones compuestas

En el ejemplo de la nota, la primera condición es `((nota > 5.0) or (nota < 0.0))`. Los paréntesis alrededor de cada comparación no son obligatorios, porque las comparaciones se evalúan antes que `and`, `or` y `not`. Python permite además **encadenar** comparaciones, así que la misma idea ("la nota está fuera del rango de 0 a 5") se puede escribir de tres formas:
""")
nb.code('''
nota = 7.0
print((nota > 5.0) or (nota < 0.0))
print(nota > 5.0 or nota < 0.0)      # sin parentesis: mismo resultado
print(not 0.0 <= nota <= 5.0)        # comparacion encadenada, negada
''')
nb.error("Dentro de una condición se compara con `==`. Si se escribe un solo `=`, que es la asignación, Python lanza `SyntaxError` y sugiere usar `==`.")
nb.code('''
nota = 5.0
if nota = 5.0:
    print("Nota maxima")
''')

# ---------------------------------------------------------------- while
nb.md("""
## Iteraciones y ciclos lógicos

### `while`

Se ejecuta un bloque de código repetidamente mientras una condición sea verdadera. Ejemplo:
""")
nb.code(O(13))
nb.convencion("Este ejemplo original usa una variable llamada `sum`. Funciona, pero `sum` ya es el nombre de una función de Python, y al usarlo como variable esa función queda tapada. Prefiera nombres como `suma` o `total`.")
nb.md("""
### Cómo funciona en Python: las tres partes de un `while`

* **Antes** del ciclo se le da valor inicial a la variable que controla la condición (`i = 0`) y a las que acumulan resultados (`sum = 0`).
* La **condición** se evalúa **antes de cada vuelta**. Si es falsa desde el principio, el bloque no se ejecuta ni una vez.
* **Dentro** del bloque algo debe cambiar la condición (`i += 1`). Si nada la cambia, el ciclo no termina nunca.
""")
nb.prediga("¿Cuántas veces se imprime `vuelta` y cuánto vale `i` al final?")
nb.code('''
i = 1
while i <= 3:
    print("vuelta", i)
    i += 1
print("al salir, i =", i)
''')
nb.prediga("Ahora `i` empieza en 10. ¿Cuántas vueltas da el ciclo?")
nb.code('''
i = 10
while i <= 3:
    print("vuelta", i)
    i += 1
print("fin del programa")
''')
nb.md("""
> ⚠️ **Error frecuente: el ciclo infinito.** Si dentro del `while` nada cambia la condición (por ejemplo, se olvida el `i += 1`), el ciclo nunca termina y la celda se queda ejecutándose indefinidamente. **No es un error de Python**: el programa hace exactamente lo que dice. Para detenerlo, en Colab pulse el botón ■ que aparece a la izquierda de la celda; en Jupyter, use el botón ■ de la barra o **Kernel → Interrupt**. Python mostrará `KeyboardInterrupt`. Luego revise qué debía cambiar la condición.
>
> ```python
> i = 1
> while i <= 3:
>     print("vuelta", i)
>     # falta i += 1: la condicion siempre es verdadera
> ```
""")
nb.error("Una variable que acumula dentro del ciclo debe tener un valor **antes** del ciclo. Si no, en la primera vuelta Python no sabe a qué sumarle y lanza `NameError`.")
nb.code('''
i = 1
while i <= 3:
    total += i
    i += 1
print(total)
''')
nb.md("""
### Leer datos hasta un valor de parada

Un uso típico de `while` en Python es leer datos con `input()` hasta que el usuario escriba un valor especial (un *centinela*) que indica que ya no hay más datos. Observe que hay **dos** `input()`: uno antes del ciclo, para tener el primer dato, y otro al final del bloque, para leer el siguiente antes de volver a evaluar la condición.
""")
nb.code('''
total = 0
numero = int(input("Numero (-1 para terminar): "))
while numero != -1:
    total += numero
    numero = int(input("Numero (-1 para terminar): "))
print(f"Total: {total}")
''', entradas=["4", "5", "3", "-1"])

# ---------------------------------------------------------------- break / continue
nb.md("""
### Interrupciones de ejecución de un bloque

En ciertas circunstancias es necesario interrumpir el flujo normal de un ciclo. Python cuenta con dos instrucciones para hacerlo:
* **`continue`**: interrumpe la vuelta actual del ciclo y pasa a la siguiente (vuelve a evaluar la condición).
* **`break`**: interrumpe el ciclo por completo y sale de él; el programa sigue con la primera instrucción después del ciclo.

#### Ejemplo `break`

Un ciclo que está programado para iterar desde 0 hasta 10, pero que, cuando el valor de la variable de control llega a 4, se rompe y sale del ciclo.
""")
nb.code(O(16))
nb.md("""
> 💡 Observe con cuidado: el último valor impreso es `i = 3`, pero cuando se ejecuta el `break`, `i` ya vale **4**, porque la línea `i += 1` está entre el `print` y el `if`. Compruébelo con el enlace a Python Tutor, siguiendo el valor de `i` instrucción por instrucción.
""")
nb.md("""
#### Ejemplo `continue`

El mismo ciclo, pero cuando el valor de la variable de control llega a 4 se ejecuta `continue`.
""")
nb.code(O(18).replace(
    "    # Despues de que se llama el continue esta instruccion nunca se ejecuta",
    "    # En las vueltas en que se ejecuta el continue, esta instruccion se salta"))
nb.md("""
### Cómo funciona en Python: `break` frente a `continue`

Observe que en el ejemplo de `continue` el ciclo sí llega hasta `i = 10`: `continue` no termina el ciclo, solo se salta lo que falta **de esa vuelta** (aquí, la línea de guiones).
""")
nb.prediga("Los dos ciclos son iguales salvo por una palabra. ¿Qué imprime cada uno?")
nb.code('''
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)
print("---")
n = 0
while n < 5:
    n += 1
    if n == 3:
        break
    print(n)
''')
nb.md("""
> ⚠️ **Error frecuente.** En un `while`, si el `continue` se ejecuta **antes** de actualizar la variable de control, la actualización se salta y el ciclo puede volverse infinito. En este fragmento, cuando `i` llega a 3, el `continue` evita el `i += 1` y `i` se queda en 3 para siempre:
>
> ```python
> i = 0
> while i < 5:
>     if i == 3:
>         continue      # i nunca pasa de 3: ciclo infinito
>     i += 1
> ```
""")
nb.md("""
### `while True` con `break`

En Python es común escribir `while True:` (un ciclo cuya condición siempre es verdadera) y salir con `break` cuando se cumple lo que se busca. Se usa mucho para **validar datos**: se pide el dato hasta que sea correcto.
""")
nb.code('''
while True:
    nota = float(input("Nota (0 a 5): "))
    if 0 <= nota <= 5:
        break
    print("Nota fuera de rango, intente de nuevo")
print(f"Nota valida: {nota}")
''', entradas=["7", "-2", "4"])

# ---------------------------------------------------------------- for
nb.md("""
### `for`

El `for` de Python **recorre los elementos de una secuencia**, uno por uno: en cada vuelta, la variable del `for` toma el siguiente elemento. No hace falta inicializar ni actualizar una variable de control: el `for` lo hace solo y termina cuando se acaban los elementos.

Las secuencias que se usan en este notebook son los **textos** (`str`), que se recorren letra por letra, y los **rangos de números** que produce `range()`. Al final, en *Para explorar*, se recorren también listas y diccionarios.

* **Iterando sobre un string**
""")
nb.code(O(21))
nb.md("""
Un recorrido con `for` se combina con un `if` para contar o acumular. En el siguiente ejemplo, `letra in "aeiouAEIOU"` es `True` cuando la letra aparece en ese texto (el operador `in` pregunta si algo está contenido en una secuencia):
""")
nb.code('''
palabra = "Antioquia"
vocales = 0
for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales += 1
print(f"{palabra} tiene {vocales} vocales")
''')
nb.md("""
* **Iteraciones con la función `range`**

  Esta función produce una sucesión de números enteros en un rango definido.

  ```python
  range(inicio, fin, paso)
  ```

  **Donde**:

  * **`inicio`**: es el primer número del rango. Si se omite, vale 0.
  * **`fin`**: es el valor límite del rango, que **nunca se incluye**. Con paso positivo, la sucesión avanza mientras los valores sean **menores** que `fin`; con paso negativo, mientras sean **mayores**. El último valor depende del inicio, del límite y del paso: `range(3, 11, 2)` produce 3, 5, 7, 9 y `range(26, 10, -4)` produce 26, 22, 18, 14.
  * **`paso`**: es la magnitud de los incrementos o decrementos del rango. Puede ser positivo o negativo, pero no 0. Si se omite, vale 1.
""")
nb.code(O(30))
nb.code(O(31))
nb.code(O(32).replace("antess", "antes"))
nb.code(O(33))
nb.md("""
### Cómo funciona en Python: `range`

* `range(N)` produce `0, 1, ..., N - 1`: son **N** números, pero el último es `N - 1`. Para contar de 1 a N se escribe `range(1, N + 1)`.
* Con paso negativo el límite tampoco se incluye: `range(10, 0, -1)` llega hasta 1. Para incluir el 0 se escribe `range(10, -1, -1)`.
* Si el rango no tiene números (por ejemplo, `range(5, 2)`, que va hacia arriba pero termina antes de empezar), **no hay error**: el `for` simplemente no da ninguna vuelta.
* En los ejemplos siguientes, `print(..., end=" ")` imprime sin saltar de línea (deja un espacio en su lugar), y el `print()` vacío hace el salto al final.
""")
nb.prediga("Escriba los números que imprime cada `for`.")
nb.code('''
for i in range(1, 4):
    print(i, end=" ")
print()
for i in range(3, 0, -1):
    print(i, end=" ")
print()
for i in range(5, 2):
    print(i, end=" ")
print("<- range(5, 2) no produjo ningun numero")
''')
nb.error("`range()` solo acepta **enteros**. Un error típico es calcular el límite con `/`, que siempre da `float`: Python lanza `TypeError: 'float' object cannot be interpreted as an integer`. Use `//` (división entera) o conviértalo con `int()`.")
nb.code('''
N = 7
for i in range(N / 2):
    print(i)
''')
nb.error("El paso de `range()` no puede ser 0 (el rango nunca avanzaría): Python lanza `ValueError: range() arg 3 must not be zero`.")
nb.code('''
for i in range(1, 10, 0):
    print(i)
''')
nb.md("""
### Cómo funciona en Python: la variable del `for`

* En cada vuelta, el `for` le **asigna** a la variable el siguiente elemento. Si dentro del bloque se le cambia el valor, eso **no altera** las vueltas que faltan: en la vuelta siguiente vuelve a recibir el elemento que le toca.
* Al terminar el ciclo, la variable conserva el valor que tenía al final de la última vuelta: normalmente, el último elemento recorrido (o el valor que se le haya asignado dentro de esa vuelta). Si el `for` no dio ninguna vuelta, la variable no recibe ningún valor, y usarla después puede dar `NameError`. Compare con el `while` de más arriba, donde `i` terminaba en 4 (un valor más que el último usado), porque la condición tuvo que fallar para salir.
""")
nb.prediga("¿Cuántas vueltas da este `for`? ¿Qué imprime en cada una?")
nb.code('''
for i in range(3):
    print("antes:", i)
    i = 100
    print("despues:", i)
''')
nb.code('''
total = 0
for i in range(1, 6):
    total += i
print(f"total = {total}, i al final = {i}")
''')
nb.md("""
> 💡 **¿`for` o `while`?** Si se sabe de antemano cuántas vueltas hay que dar (recorrer un texto, contar de 1 a N), el `for` es más corto y no hay riesgo de olvidar la actualización. Si el número de vueltas depende de lo que pase durante el ciclo (leer hasta un centinela, repetir hasta que un dato sea válido), se usa `while`.
""")

# ---------------------------------------------------------------- anidados
nb.md("""
### Ciclos anidados

Es posible anidar ciclos dentro de otros ciclos: por **cada** vuelta del ciclo de afuera, el ciclo de adentro da **todas** sus vueltas. Ejemplo:
""")
nb.code(O(35))
nb.md("""
Este ejemplo original usa el formato con `%d`, que reemplaza cada `%d` por un entero, en orden. Con una f-string se escribiría `print(f"i: {i} j: {j}")`. Como el ciclo de afuera da 2 vueltas y el de adentro 5, el `print` se ejecuta 2 × 5 = 10 veces.

El siguiente ejemplo imprime una tabla de multiplicar. `{fila * col:4d}` muestra el producto como entero ocupando 4 espacios, para que las columnas queden alineadas, y `end=""` hace que todos los productos de una fila queden en la misma línea. El `print()` que está **después** del ciclo de adentro (pero dentro del de afuera) es el que cambia de fila.
""")
nb.prediga("¿Cuántas filas y cuántas columnas tiene la tabla?")
nb.code('''
for fila in range(1, 4):
    for col in range(1, 5):
        print(f"{fila * col:4d}", end="")
    print()
''')
nb.md("""
### Cómo funciona en Python: `break` en ciclos anidados

Un `break` solo sale del ciclo **en el que está escrito** (el más interno). El ciclo de afuera continúa con su siguiente vuelta.
""")
nb.prediga("¿Qué pares `i j` se imprimen?")
nb.code('''
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
''')

# ---------------------------------------------------------------- desempaquetado
nb.md("""
## Desempaquetado

El desempaquetado es una característica de Python que permite asignar los elementos de una colección a varias variables en una sola línea de código. En los ejemplos se usa una **lista**: un grupo de valores separados por comas y encerrados entre corchetes, como `['Pepe', 'Pérez', 4.5]`. La sintaxis básica es la siguiente (es un esquema, no código que se pueda ejecutar):

```
<nombre 1>, <nombre 2>, ..., <nombre n> = <colección de tamaño n>
```

En caso de que el número de nombres y el tamaño de la colección no coincidan, se produce un error de tipo `ValueError`.
""")
nb.md("""
### Cómo funciona en Python: asignar varios valores a la vez

La forma más simple no necesita corchetes: `x, y = 3, 4` asigna 3 a `x` y 4 a `y`. Python calcula **primero** todos los valores de la derecha y **después** los asigna, así que `x, y = y, x` intercambia los valores de dos variables sin necesitar una variable temporal.
""")
nb.prediga("¿Qué imprime cada `print`?")
nb.code('''
x, y = 3, 4
print(x, y)
x, y = y, x
print(x, y)
''')
nb.md("Lo mismo funciona cuando los valores vienen agrupados en una lista, como en el ejemplo original:")
nb.code(O(37))
nb.error("Si hay **más** valores que variables, Python lanza `ValueError: too many values to unpack` (demasiados valores para desempaquetar); si hay **menos**, `ValueError: not enough values to unpack`.")
nb.code(O(38))
nb.code('''
nombre, apellido, calificacion = ['Pepe', 'Perez']    # error: faltan valores
''')
# ---------------------------------------------------------------- para explorar
nb.md("""
## Para explorar: listas y diccionarios en un `for`

Esta sección es opcional. El `for` de Python recorre cualquier colección de datos, no solo textos y rangos. Aquí se muestran dos colecciones que se estudian más adelante:

* Una **lista** es un grupo de valores en un orden, entre corchetes: `[-1, 2.15, 'casa']`. El `for` la recorre valor por valor.
* Un **diccionario** guarda pares **clave: valor** entre llaves: `{'001': 'Bart'}` asocia la clave `'001'` con el valor `'Bart'`. El `for` recorre las **claves**, y `diccionario[clave]` da el valor asociado.
""")
nb.convencion("En el curso, las listas se usan como **arreglos**: de tamaño fijo, con un solo tipo de dato y accediendo por posición, sin métodos como `.append()`. Los ejemplos de esta sección usan `.values()` e `.items()`, que son *métodos* de los diccionarios (la notación `objeto.operación()`); los métodos se explican en Programación Orientada a Objetos.")
nb.md("* **Iterando sobre una lista**")
nb.code(O(23))
nb.md("* **Iterando sobre un diccionario**: el `for` recorre las claves, y con cada clave se obtiene su valor.")
nb.code(O(25))
nb.md("Con `.values()` se recorren directamente los valores:")
nb.code(O(26))
nb.convencion("El siguiente ejemplo original usa `id` como nombre de variable. Funciona, pero `id` ya es una función de Python y queda tapada; un nombre como `codigo` sería mejor.")
nb.code(O(27))
nb.md("Con `.items()` se recorren los pares completos; cada uno se imprime entre paréntesis porque es una *tupla* (un grupo de valores entre paréntesis):")
nb.code(O(28))

# ---------------------------------------------------------------- errores
nb.resumen_errores([
    ("`SyntaxError`", "El código no está bien escrito; Python ni siquiera empieza a ejecutarlo",
     "Falta `:` al final de `if`, `elif`, `else`, `while` o `for`; `=` en vez de `==` en una condición",
     "Revisar la línea señalada con `^`"),
    ("`IndentationError`", "La sangría (espacios al inicio de la línea) no es la esperada",
     "La línea que debía ir dentro de un bloque quedó pegada al margen (`expected an indented block`)",
     "Sangrar las instrucciones del bloque con 4 espacios"),
    ("`NameError`", "Se usa un nombre que no existe",
     "Un acumulador usado en el ciclo sin valor inicial (`total += i` sin `total = 0` antes)",
     "Inicializar la variable antes del ciclo"),
    ("`TypeError`", "La operación no es válida para esos tipos",
     "`range(N / 2)`: `range()` solo acepta enteros",
     "Usar `//` o convertir con `int()`"),
    ("`ValueError`", "El tipo es correcto pero el valor no sirve",
     "`range(1, 10, 0)`; desempaquetar con más o menos valores que variables",
     "Usar un paso distinto de 0; poner tantas variables como valores"),
    ("Ciclo infinito (no es un error de Python)", "El ciclo nunca termina y la celda no deja de ejecutarse",
     "Olvidar actualizar la variable de control, o un `continue` antes de actualizarla",
     "Detener la celda (■) y revisar qué debe cambiar la condición"),
])

# ---------------------------------------------------------------- ejercicios
nb.ejercicios([
    '''
x = 7
if x > 5:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")
print("D")
''',
    '''
n = 0
while n < 10:
    n += 3
print(n)
''',
    '''
for i in range(2, 11, 3):
    print(i, end=" ")
''',
    '''
total = 0
for i in range(1, 5):
    if i % 2 == 0:
        continue
    total += i
print(total)
''',
    '''
for i in range(4):
    for j in range(i):
        print("*", end="")
    print(i)
''',
    '''
i = 5
while i > 0:
    i -= 2
    if i == 1:
        break
print(i)
''',
    '''
a, b = 1, 2
a, b = b, a + b
print(a, b)
''',
    '''
cuenta = 0
for letra in "programa":
    if letra == "a":
        cuenta += 1
print(cuenta)
''',
])

# ---------------------------------------------------------------- recursos
nb.recursos("""
### Herramientas

* [Python Tutor](https://pythontutor.com/): visualiza la ejecución de un programa paso a paso. Es especialmente útil para seguir las vueltas de un ciclo.
* [PEP 8](https://peps.python.org/pep-0008/): guía oficial de estilo de Python (sangría, nombres, espacios).

### Referencias

* CS50's Introduction to Programming with Python, [Lecture 1: Conditionals](https://cs50.harvard.edu/python/notes/1/) y [Lecture 2: Loops](https://cs50.harvard.edu/python/notes/2/).
* El Libro de Python: [`if`](https://ellibrodepython.com/if-python), [`while`](https://ellibrodepython.com/while-python), [`for`](https://ellibrodepython.com/for-python), [`break`](https://ellibrodepython.com/break-python) y [`continue`](https://ellibrodepython.com/continue-python).
* Tutorial oficial de Python (en español): [Más herramientas para control de flujo](https://docs.python.org/es/3/tutorial/controlflow.html) y [el tipo `range`](https://docs.python.org/es/3/library/stdtypes.html#range).
""")

nb.escribir(RAIZ / RUTA)
