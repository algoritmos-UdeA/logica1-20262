"""Contenido de funciones.ipynb (formato común en formato.py).

Los ejemplos originales del notebook se toman, por posición, de la versión con
la que se agregó la carpeta al repositorio (commit 2df6db3), mediante O(i).
Decisión del docente (2026-10-19): en este notebook prima el contenido de
Python sobre lo visto en clase; *args, **kwargs, funciones anidadas, de orden
superior, decoradores y lambda van en el cuerpo, marcados con 🐍 y explicados
completos (autocontenido).

Uso, desde la raíz del repositorio:
    python laboratorios/resumen-python/herramientas/construir_funciones.py
"""
import json
import pathlib
import subprocess
import sys

sys.dont_write_bytecode = True  # no crear __pycache__ en el repositorio
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from formato import Notebook  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[3]
RUTA = "laboratorios/resumen-python/estructurada_python/funciones.ipynb"
orig = json.loads(subprocess.run(["git", "show", f"2df6db3:{RUTA}"], cwd=RAIZ, capture_output=True,
                                 check=True).stdout.decode("utf-8"))


def O(i):
    """Fuente de la celda i del notebook original."""
    return "".join(orig["cells"][i]["source"])


# Algunas celdas originales se corrigen al copiarlas (ver comentarios).
SUPERFICIE = O(45).replace("3.14259265", "3.14159265")  # errata en el valor de pi del original
SUPERFICIE_CON_CTX = SUPERFICIE

nb = Notebook("funciones.ipynb")
nb.insignias()
nb.encabezado(
    titulo="Funciones",
    intro=("Este notebook es un **refuerzo de Python** sobre las funciones: cómo se definen, cómo se "
           "invocan y cómo se comportan sus variables y sus argumentos. Además recorre herramientas de "
           "Python que van más allá de lo que se usa en los ejercicios del curso (`*args`, `**kwargs`, "
           "funciones anidadas, funciones de orden superior, decoradores y `lambda`): esas partes están "
           "marcadas con 🐍 y se explican completas aquí."),
    antes_de_empezar=("Este notebook supone que ya sabe usar variables, `print`, f-strings, condicionales y "
                      "ciclos en Python. Si necesita repasarlos, están en los notebooks *Repaso básico de "
                      "Python* y *Control de flujo* de esta misma carpeta. Lo demás que se usa aquí, incluidas "
                      "las partes marcadas con 🐍, se explica aquí. Si es la primera vez que estudia "
                      "funciones, avance primero hasta la sección *Parámetros con valores por defecto* y "
                      "después continúe con las partes marcadas con 🐍."),
    objetivos=[
        "Definir funciones con `def`, documentarlas con un *docstring* e invocarlas, distinguiendo entre devolver un valor con `return` y mostrarlo con `print`.",
        "Probar una función con `assert`.",
        "Explicar el ámbito de las variables (locales y globales, ocultamiento, `global`) y reconocer `NameError` y `UnboundLocalError`.",
        "Pasar argumentos por posición y por nombre, y definir parámetros con valores por defecto.",
        "Escribir funciones que reciben un número variable de argumentos con `*args` y `**kwargs`.",
        "Usar funciones como valores: funciones anidadas, funciones de orden superior y decoradores.",
        "Escribir funciones cortas con `lambda` y usarlas como argumento de otra función.",
        "Reconocer los errores frecuentes al definir, invocar y probar funciones.",
    ],
)

# ---------------------------------------------------------------- definición
nb.md("""
## Definición e invocación de una función

Una **función** es un bloque de código con nombre que se escribe una vez y se puede usar muchas veces. Usarla se llama **invocarla** (o llamarla). Las funciones reciben datos a través de sus **parámetros** y pueden devolver un resultado.

### Definición

```
def nombre_funcion(parametro1, parametro2, ...):
    # código de la función (sangrado)
```

La línea de `def` termina en dos puntos y el cuerpo va sangrado, igual que en un `if` o un `for`.

### Invocación

```
nombre_funcion(argumento1, argumento2, ...)
```

Los valores que se escriben entre paréntesis al invocar se llaman **argumentos**: cada uno se asigna al parámetro que está en su misma posición.
""")
nb.convencion("Los nombres de funciones se escriben en **snake_case**, como las variables, y deberían ser un verbo que diga qué hace la función: `calcular_promedio`, `mostrar_menu`.")
nb.md("""
### Definición mínima de una función

Una función sin código da error. En aquellos casos en los que, por lo menos inicialmente, no se necesita código, se emplea la instrucción **`pass`** para evitar este problema. La instrucción `pass` no realiza ninguna acción, pero permite que el bloque no quede vacío.
""")
nb.error("Si el cuerpo de la función queda vacío, Python da error. En un notebook el mensaje es `SyntaxError: incomplete input` (entrada incompleta); en un archivo `.py` sería `IndentationError: expected an indented block`.")
nb.code('''
def funcion():
''')
nb.code(O(5))
nb.code(O(6), contexto=O(5))
nb.md("""
Invocar `funcion()` no muestra nada, porque `pass` no hace nada. Pero toda función de Python **devuelve** algo: si no tiene `return`, devuelve el valor especial **`None`** (que representa "ningún valor"). Por eso, al imprimir lo que devuelve, aparece `None`:
""")
nb.code(O(7), contexto=O(5))
nb.md("""
Observe la siguiente celda: no tiene `print`, y aun así muestra un resultado. Es una particularidad de los notebooks: **si la última línea de una celda es una expresión, Jupyter muestra su valor**. En un programa `.py`, o en Python Tutor, esa línea no mostraría nada; allí hay que usar `print`. Varios ejemplos de este notebook aprovechan esa particularidad.

El resultado, `function`, indica que `funcion` es un valor de tipo función, igual que `7` es un valor de tipo `int`. Esto tiene consecuencias interesantes que se ven en la sección de funciones de orden superior.
""")
nb.code(O(8), contexto=O(5))
nb.md("""
**Ejemplo**: hacer y documentar una función que imprime **Welcome to Tijuana**. La documentación, llamada *docstring*, es un texto entre comillas triples escrito en la primera línea del cuerpo, justo después de la cabecera. No cambia lo que hace la función, pero queda guardada con ella: la función `help()` la muestra.
""")
nb.code(O(10))
nb.code(O(11), contexto=O(10))
nb.code(O(12).replace("Invocano", "Invocando"), contexto=O(10))
nb.md("""
### Cómo funciona en Python: `return` frente a `print`

* **`return valor`** termina la función y **devuelve** el valor a quien la invocó, que puede guardarlo en una variable, operarlo o pasarlo a otra función.
* **`print(valor)`** solo **muestra** el valor en pantalla. Después de mostrarlo, ese valor no se puede usar para nada más.

Una función que calcula algo casi siempre debe usar `return`: así el resultado se puede reutilizar.
""")
nb.prediga("¿Qué imprime cada `print`? Fíjese en qué función usa `return` y cuál usa `print`.")
nb.code('''
def area_rectangulo(base, altura):
    return base * altura

def mostrar_area(base, altura):
    print(base * altura)

a = area_rectangulo(3, 4)
print(a + 1)
b = mostrar_area(3, 4)
print(b)
''')
nb.error("Una función sin `return` devuelve `None`. Si se intenta operar con ese resultado, Python lanza `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`. Cuando vea `NoneType` en un error, revise si a la función le falta el `return`.")
nb.code('''
def mostrar_area(base, altura):
    print(base * altura)

total = mostrar_area(3, 4) + 1
''')
nb.md("""
### Probar una función con `assert`

La instrucción `assert condición` comprueba que algo sea cierto. Si la condición es verdadera, **no pasa nada** y el programa sigue; si es falsa, Python se detiene con `AssertionError`. Por eso sirve para escribir **pruebas**: cada `assert` compara lo que devuelve la función con el resultado que se sabe correcto.

`assert` sirve para **probar** el programa mientras se desarrolla, no para validar los datos que escribe el usuario: si Python se ejecuta en modo optimizado (`python -O programa.py`), omite todos los `assert`. Para validar datos se usa un `if`.
""")
nb.code('''
def area_rectangulo(base, altura):
    """Calcula el area de un rectangulo.

    Supone: base y altura son numeros mayores o iguales que 0.
    Garantiza: devuelve base * altura.
    """
    return base * altura

assert area_rectangulo(3, 4) == 12
assert area_rectangulo(0, 5) == 0
assert area_rectangulo(2.5, 2) == 5.0
print("Todas las pruebas pasaron")
''')
nb.convencion("En el curso, cada función se documenta con un docstring que dice qué **Supone** (lo que debe cumplirse al invocarla) y qué **Garantiza** (lo que devuelve), y se prueba con `assert` antes de usarla en el programa principal. Las funciones que calculan no usan `input()` ni `print()`: reciben los datos por parámetros y devuelven el resultado con `return`.")
nb.error("Una prueba que pasa no demuestra que la función esté bien. En esta versión, la función **suma** en vez de multiplicar; la primera prueba pasa por casualidad (2 + 2 = 2 × 2), y la segunda descubre el error con `AssertionError`. Por eso conviene probar varios casos distintos.")
nb.code('''
def area_rectangulo(base, altura):
    return base + altura      # error: suma en vez de multiplicar

assert area_rectangulo(2, 2) == 4     # pasa por casualidad
assert area_rectangulo(4, 3) == 12    # falla
''')

# ---------------------------------------------------------------- ámbito
nb.md("""
## Ámbito (scope) de las variables

El **ámbito** de una variable es la parte del programa donde ese nombre existe y se puede usar.

* Una variable creada **dentro** de una función (incluidos sus parámetros) es **local**: su nombre solo existe dentro de la función y no se puede usar desde afuera. El **valor** sí puede seguir existiendo después de que la función termina, si la función lo devuelve con `return`.
* Una variable creada **fuera** de toda función es **global**: se puede leer desde cualquier parte, también desde dentro de las funciones.

Cuando Python encuentra un nombre, lo busca en este orden, conocido como la [**regla LEGB**](https://www.datacamp.com/tutorial/scope-of-variables-python): primero en la función actual (**L**ocal); luego en las funciones que la contienen, si está definida dentro de otra (**E**nclosing, se ve en *Funciones anidadas*); después en el programa (**G**lobal); y por último entre los nombres propios de Python, como `print` o `len` (**B**uilt-in).
""")
nb.error("Una variable local no existe fuera de su función. Aunque la función ya se ejecutó, al pedir `total` desde afuera Python lanza `NameError`. Para usar el resultado afuera, la función debe devolverlo con `return` y quien la invoca debe guardarlo.")
nb.code('''
def calcular():
    total = 5
    return total

calcular()
print(total)
''')
nb.md("""
### Ocultamiento de variables (*shadowing*)

Cuando se crea una variable dentro de una función con el mismo nombre que una variable global, la variable local tiene prioridad dentro de esa función: la global queda **oculta** allí, pero no cambia. Este fenómeno se conoce como *ocultamiento* o *shadowing*.
""")
nb.prediga("¿Qué imprime cada uno de los tres `print`?")
nb.code(O(15))
nb.md("""
### Modificar una variable global con la palabra clave `global`

Si se necesita que una función modifique una variable global en lugar de crear una local, hay que declararlo explícitamente con la palabra clave `global`:

```
global nombre_variable
nombre_variable = valor
```

**Advertencia**: modificar variables globales desde una función hace que el código sea más difícil de entender y de depurar, porque el resultado ya no depende solo de los argumentos. Es una práctica que generalmente se debe evitar, en favor de pasar los datos como parámetros y devolver el resultado.
""")
nb.code(O(17))
nb.convencion("En el curso no se usa `global`. Las únicas variables globales aceptadas son las **constantes** (en MAYÚSCULAS, como `NOTA_MAXIMA = 5.0`), que las funciones solo leen.")
nb.error("Si una función **asigna** un valor a una variable, Python la considera local en **toda** la función, aunque exista una global con el mismo nombre. Si además la lee antes de asignarla (como en `contador = contador + 1`), Python lanza `UnboundLocalError: cannot access local variable 'contador' where it is not associated with a value` (no se puede usar la variable local porque todavía no tiene valor).")
nb.code('''
contador = 0

def incrementar():
    contador = contador + 1

incrementar()
''')
nb.md("La forma recomendada de resolverlo es pasar el valor como parámetro y devolver el nuevo valor:")
nb.code('''
def incrementar(contador):
    return contador + 1

contador = 0
contador = incrementar(contador)
print(contador)
''')

# ---------------------------------------------------------------- argumentos
nb.md("""
## Invocación de funciones: argumentos posicionales y por palabra clave

En Python hay dos formas de pasar los argumentos al invocar una función:

1. **Argumentos posicionales**: se asignan a los parámetros **en orden**: el primer argumento al primer parámetro, el segundo al segundo, y así sucesivamente.
2. **Argumentos por palabra clave** (o por nombre): se indica explícitamente a qué parámetro va cada valor, con la forma `parametro=valor`. Así el orden deja de importar y la invocación se lee mejor.

Los ejemplos siguientes muestran además que, como en Python el tipo lo tienen los valores y no las variables, una misma función puede trabajar con datos de distintos tipos: `suma` suma números y une textos, porque `+` hace ambas cosas.

**Definición**
""")
nb.code(O(20))
nb.md("**Diferentes invocaciones**")
nb.code(O(22), contexto=O(20))
nb.code(O(23), contexto=O(20))
nb.code(O(24), contexto=O(20))
nb.error("Si se pasan **más** argumentos que parámetros, Python lanza `TypeError: suma() takes 2 positional arguments but 3 were given` (recibe 2 y se le dieron 3).")
nb.code(O(25), contexto=O(20))
nb.error("Si se pasan **menos**, el mensaje es `TypeError: suma() missing 1 required positional argument: 'p2'` (falta un argumento obligatorio).")
nb.code('''
r = suma(2)
''', contexto=O(20))

# ---------------------------------------------------------------- por defecto
nb.md("""
## Parámetros con valores por defecto

Python permite asignar un **valor por defecto** a un parámetro: si al invocar la función no se pasa ese argumento, el parámetro toma el valor por defecto. Así, una misma función se puede invocar con más o con menos argumentos.

La sintaxis es simple: se utiliza el operador de asignación (`=`) en la definición de la función.

### Reglas clave para recordar

1. **Orden de los parámetros**: los parámetros con valores por defecto **deben ir siempre después** de los parámetros que no los tienen. Si se define un parámetro sin valor por defecto después de uno que sí lo tiene, Python da `SyntaxError`.
2. **Flexibilidad en la invocación**: al invocar la función, se pueden omitir los argumentos que tienen valor por defecto. También se pueden combinar con argumentos por palabra clave.
3. **Cuidado con los valores que se pueden modificar**: un valor por defecto se crea **una sola vez**, cuando se define la función, no cada vez que se invoca. Si es una lista que la función modifica, el cambio se acumula entre invocaciones. Se muestra al final de esta sección.

A continuación, se redefine la función `suma` con valores por defecto y se muestran las distintas formas de invocarla.
""")
nb.code(O(27))
nb.md("**Diferentes invocaciones**")
nb.code(O(29), contexto=O(27))
nb.code(O(30), contexto=O(27))
nb.code(O(31), contexto=O(27))
nb.code(O(32), contexto=O(27))
nb.prediga("Los argumentos van por nombre y en orden contrario al de la definición. ¿Qué devuelve?")
nb.code(O(33), contexto=O(27))
nb.code(O(34), contexto=O(27))
nb.code(O(35), contexto=O(27))
nb.error("Un parámetro sin valor por defecto no puede ir después de uno con valor por defecto: Python lanza `SyntaxError: non-default argument follows default argument`.")
nb.code('''
def suma(p1=0, p2):
    return p1 + p2
''')
nb.python("""Este ejemplo usa una **lista** (un grupo de valores entre corchetes, como `[1, 2]`; `[]` es una lista vacía) y el **método** `.append()`, que agrega un valor al final de la lista. Un *método* es una operación que pertenece a un tipo de dato y se escribe con un punto después del valor: `lista.append(valor)`. Los métodos se estudian a fondo en Programación Orientada a Objetos.""")
nb.convencion("En los ejercicios del curso, las listas se usan como **arreglos**: de tamaño fijo, creadas con `[0.0] * N`, sin `.append()` ni otros métodos.")
nb.md("""
Este es el problema de la regla 3: la lista vacía `[]` del valor por defecto se crea una sola vez, así que la segunda invocación encuentra la misma lista, que ya tiene el 1 de la primera.
""")
nb.prediga("¿Qué imprime la segunda invocación?")
nb.code('''
def agregar(elemento, lista=[]):
    lista.append(elemento)
    return lista

print(agregar(1))
print(agregar(2))     # se esperaba [2]
''')
nb.md("""
La práctica recomendada es usar `None` como valor por defecto y crear la lista **dentro** de la función, donde se crea de nuevo en cada invocación. `lista is None` pregunta si `lista` es exactamente el valor `None`; es la forma habitual de comprobarlo.
""")
nb.code('''
def agregar(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

print(agregar(1))
print(agregar(2))
''')

# ---------------------------------------------------------------- *args
nb.md("""
## Número variable de argumentos posicionales (`*args`)

Python permite crear funciones que acepten **cualquier cantidad** de argumentos posicionales. Para eso se antepone un asterisco (`*`) al nombre del parámetro. Por convención se usa el nombre `args` (abreviatura de *arguments*), pero puede ser cualquier nombre válido; en el ejemplo se llama `muestras`.

### ¿Cómo funciona?

Al invocar la función, todos los argumentos posicionales que sobran se **empaquetan** en una **tupla**: un grupo de valores entre paréntesis, como `(1, 3, 5)`. Una tupla se puede recorrer con `for`, su tamaño se obtiene con `len()` y la función `sum()` suma todos sus valores.

### Reglas y buenas prácticas

1. **Posición**: el parámetro `*args` debe ir **después** de todos los parámetros posicionales normales.
2. **Claridad**: es ideal para funciones que aplican la misma operación a todos los argumentos, como calcular un promedio, una suma o un máximo.
""")
nb.python("Python permite **anotar el tipo** esperado de un parámetro, por ejemplo `*muestras: float`. Las anotaciones no cambian lo que hace el programa (Python no las verifica); sirven como documentación. El curso no las usa: los tipos esperados se describen en el *Supone* del docstring.")
nb.md("""
La función `promedio` usa además el formato con `%`: `%d` se reemplaza por un entero y `%.3f` por un real con 3 decimales, en el orden de los valores que van después del `%`. Con una f-string sería `f"El promedio de la muestra de {len(muestras)} elementos es {promedio:.3f}."`.
""")
nb.convencion("Los ejemplos originales de este notebook usan los formatos con `%` y con `.format()`, que se explican donde aparecen. En código nuevo, use f-strings.")
nb.code(O(37))
nb.code(O(38), contexto=O(37))
nb.code(O(39), contexto=O(37))
nb.convencion("Dentro de esta función original, la variable que guarda el resultado también se llama `promedio`, como la función. Funciona (dentro de la función, el nombre local oculta a la función), pero confunde; un nombre como `resultado` sería mejor.")
nb.md("Dentro de la función, el parámetro con `*` es siempre una tupla, aunque se pase un solo argumento o ninguno:")
nb.code('''
def mostrar(*valores):
    print(valores)
    print(type(valores))

mostrar(4, 5, 6)
mostrar()
''')
nb.error("Si `promedio` se invoca sin argumentos, la tupla queda vacía, `len(muestras)` vale 0 y Python lanza `ZeroDivisionError`. Una función con `*args` debe considerar el caso en que no recibe nada. Esta función **supone** que recibe al menos un valor; con las convenciones del curso, esa condición se escribiría en el *Supone* de su docstring.")
nb.code('''
promedio()
''', contexto=O(37))
nb.md("""
Cuando la función tiene varios parámetros, el parámetro que recibe la cantidad variable de argumentos debe ir **después** de los parámetros normales. Después de él solo pueden ir `**kwargs` (se ve en la sección siguiente) y parámetros que se pasan obligatoriamente por nombre:
""")
nb.code(O(41))
nb.code(O(42), contexto=O(41))
nb.prediga("Esta invocación olvidó el título. ¿Qué toma la función como título y de cuántos elementos calcula el promedio?")
nb.code(O(43), contexto=O(41))
nb.md("""
No hay error, pero el resultado es incorrecto: el primer argumento, `1`, se asignó al parámetro `titulo`, y el promedio se calculó solo con los 7 números restantes. Python no puede saber que el título faltaba.
""")

# ---------------------------------------------------------------- **kwargs
nb.md("""
## Número variable de argumentos por palabra clave (`**kwargs`)

Así como `*args` recibe una cantidad variable de argumentos posicionales, con un doble asterisco (`**`) se recibe una cantidad variable de **argumentos por palabra clave** (de la forma `nombre=valor`). Por convención se usa el nombre `kwargs` (*keyword arguments*); en el ejemplo se llama `dato`.

### ¿Cómo funciona?

Los argumentos `nombre=valor` que no corresponden a ningún otro parámetro se empaquetan en un **diccionario**: una colección de pares **clave: valor** entre llaves, como `{'base': 22, 'tipo': 'Rectángulo'}`. Cada clave es el nombre del argumento (como texto) y se usa para obtener su valor: `dato["base"]` vale `22`.

### Reglas y buenas prácticas

1. **Posición**: el parámetro `**kwargs` debe ser **el último** de la definición. El orden es: parámetros normales, `*args`, `**kwargs`.
2. **Acceso seguro**: pedir una clave que no se pasó, como `dato["clave_inexistente"]`, produce `KeyError`. Para evitarlo se puede usar `.get()`, que se muestra más abajo.
3. **Casos de uso**: `**kwargs` es útil para recibir opciones de configuración que no siempre se pasan todas.

En el ejemplo, `dato["tipo"].lower()` usa el método `.lower()`, que devuelve el texto en minúsculas, para escribir "rectángulo" en medio de la frase.
""")
nb.code(SUPERFICIE)
nb.md("> 💡 En el notebook original, el valor de π de esta función tenía una errata (`3.14259265`); aquí está corregido a `3.14159265`.")
nb.convencion("Como en `promedio`, dentro de esta función original la variable del resultado se llama igual que la función (`superficie`). Funciona, pero confunde; un nombre como `resultado` sería mejor.")
nb.code(O(46), contexto=SUPERFICIE_CON_CTX)
nb.code(O(47), contexto=SUPERFICIE_CON_CTX)
nb.code(O(48), contexto=SUPERFICIE_CON_CTX)
nb.md("Si se pasan argumentos que la función no usa, como `radio` para un rectángulo, quedan en el diccionario pero no producen error:")
nb.code(O(49), contexto=SUPERFICIE_CON_CTX)
nb.error("Si falta un argumento que la función necesita, al pedir esa clave al diccionario Python lanza `KeyError`, con el nombre de la clave que faltó (aquí, `'altura'`).")
nb.code('''
superficie(tipo="Rectángulo", base=3)
''', contexto=SUPERFICIE_CON_CTX)
nb.python("El método `.get(clave)` de los diccionarios devuelve el valor de la clave o, si la clave no existe, `None` en vez de dar error. Con un segundo argumento, `.get(clave, valor)`, devuelve ese valor cuando la clave no existe.")
nb.code('''
datos = {"tipo": "Círculo", "radio": 2}
print(datos.get("radio"))
print(datos.get("base"))
print(datos.get("base", 0))
''')
nb.md("Una función puede combinar los tres tipos de parámetros, siempre en este orden:")
nb.code('''
def mostrar_todo(titulo, *valores, **opciones):
    print(titulo)
    print(valores)
    print(opciones)

mostrar_todo("Datos", 1, 2, 3, color="rojo", ancho=10)
''')

# ---------------------------------------------------------------- anidadas
nb.md("""
## Funciones anidadas

En Python se puede definir una función dentro de otra. A estas se les conoce como **funciones anidadas**.

Una función anidada puede **leer las variables de la función que la contiene**: es el nivel *Enclosing* de la regla LEGB. Cuando la función anidada **conserva** ese acceso incluso después de que la función externa terminó (porque la función externa la devolvió), se habla de un **cierre** o *closure*. Se ve en la sección siguiente, con la fábrica de funciones `html`.

### ¿Por qué usar funciones anidadas?

1. **Encapsular**: son útiles para funciones auxiliares que solo tienen sentido dentro de la función principal. Desde afuera no se ven, así que no se pueden usar por error en otra parte del programa.
2. **Fabricar funciones**: como se verá en *Funciones de orden superior*, una función puede crear otra función anidada y devolverla ya configurada.

El siguiente ejemplo, `lista_primos`, usa una función anidada `esprimo` para revisar si un número es primo. Observe que `esprimo` usa la variable `lista`, que pertenece a la función externa `lista_primos`. Dentro de `esprimo`, el `return False` termina la función en cuanto encuentra un divisor, aunque el `for` no haya terminado.

La lista empieza con un solo valor, `[2]`, y crece con `lista.append(numero)`, que agrega cada primo nuevo al final.
""")
nb.convencion("Este ejemplo usa `.append()` para que la lista crezca. En los ejercicios del curso, las listas se usan como arreglos de tamaño fijo, sin `.append()`.")
nb.code(O(51))
nb.code(O(52), contexto=O(51))
nb.prediga("La documentación promete los primos \"comprendidos entre el 2 y el valor de limite\". ¿Qué **debería** devolver `lista_primos(1)`? ¿Qué devuelve?")
nb.code('''
lista_primos(1)
''', contexto=O(51))
nb.md("""
Con un límite menor que 2 no hay ningún primo en el rango, pero la función devuelve `[2]`, porque la lista empieza con el 2 sin revisar el límite. Es un error de **caso límite**: la función sirve para los valores "normales" y falla en el borde. Por eso las pruebas deben incluir los bordes (aquí, 0, 1 y 2). La siguiente versión corrige el caso con un `if` al inicio, documenta lo que supone y garantiza, y lo prueba con `assert`:
""")
nb.code('''
def lista_primos(limite=100):
    """Genera una lista de los numeros primos entre 2 y limite.

    Supone: limite es un entero.
    Garantiza: devuelve los primos menores o iguales que limite;
               si limite < 2, devuelve una lista vacia.
    """
    if limite < 2:
        return []
    lista = [2]

    def esprimo(numero):
        for primo in lista:
            if numero % primo == 0:
                return False
        return True

    for numero in range(3, limite + 1):
        if esprimo(numero):
            lista.append(numero)
    return lista

assert lista_primos(0) == []
assert lista_primos(1) == []
assert lista_primos(2) == [2]
assert lista_primos(10) == [2, 3, 5, 7]
print("Todas las pruebas pasaron")
''')
nb.error("La función anidada solo existe dentro de la función que la contiene. Invocarla desde afuera da `NameError`.")
nb.code('''
esprimo(7)
''', contexto=O(51))

# ---------------------------------------------------------------- orden superior
nb.md("""
## Funciones de orden superior

En Python, las funciones son **valores**, como los números o los textos. Por eso una función:

* puede asignarse a una variable;
* puede pasarse como argumento a otra función;
* puede ser devuelta por otra función.

Una **función de orden superior** es una función que recibe otra función como argumento, o que devuelve una función como resultado.

### Cómo funciona en Python: la función como valor

La clave está en los paréntesis. `doble(5)` **invoca** la función y da su resultado; `doble`, sin paréntesis, es **la función misma**, que se puede guardar o pasar a otra función sin ejecutarla.
""")
nb.code('''
def doble(n):
    return 2 * n

otra = doble          # sin parentesis: no se invoca, se guarda la funcion
print(otra(5))        # otra se invoca igual que doble
print(otra is doble)  # True: los dos nombres son la misma funcion
print(type(doble))    # la funcion misma, no un resultado
''')
nb.md("Como la función es un valor, se puede pasar como argumento. Aquí, `aplicar` no sabe qué operación hará: la recibe en el parámetro `funcion`.")
CTX_APLICAR = '''
def doble(n):
    return 2 * n

def triple(n):
    return 3 * n

def aplicar(funcion, valor):
    return funcion(valor)
'''
nb.code(CTX_APLICAR + '''
print(aplicar(doble, 10))
print(aplicar(triple, 10))
''')
nb.error("Para pasar la función como argumento se escribe **sin paréntesis**. Con paréntesis, `doble()` intenta invocarla en ese momento, sin el argumento que necesita, y Python lanza `TypeError: doble() missing 1 required positional argument: 'n'`.")
nb.code('''
print(aplicar(doble(), 10))
''', contexto=CTX_APLICAR)
nb.md("""
### Patrón de fábrica de funciones

El ejemplo a continuación muestra un patrón común llamado **fábrica de funciones** (*factory*). La función `html` no hace el trabajo directamente: recibe una función (`funcion`) y **fabrica y devuelve** una función nueva (`empaqueta`), que al invocarse aplica `funcion` y encierra su resultado entre las etiquetas de una página HTML.

`empaqueta` es un **cierre**: cuando se invoca, `html` ya terminó, pero `empaqueta` sigue teniendo acceso a las variables `funcion` y `etiquetas`, que pertenecían a `html`.

En el texto de `etiquetas`, `\\n` es un salto de línea, y las llaves `{}` se reemplazan por un valor con el método `.format()`: `"<p>{}</p>".format("Hola")` produce `"<p>Hola</p>"`.
""")
nb.code(O(54))
nb.code(O(55), contexto=O(54))
nb.code(O(56))
nb.code(O(57), contexto=O(56))
nb.code(O(58), contexto=O(56))
nb.md("Al invocar `html(parrafo)` no se obtiene un texto sino **una función**: la función `empaqueta` que `html` fabricó.")
CTX_HTML = O(54) + "\n\n" + O(56)
nb.code(O(59), contexto=CTX_HTML)
nb.md("""
Esa función se puede invocar de inmediato, con un segundo par de paréntesis. Como la celda no usa `print`, Jupyter muestra el texto entre comillas y con los saltos de línea escritos como `\\n`; con `print`, en la celda siguiente, se ve como página.
""")
nb.code(O(60), contexto=CTX_HTML)
nb.code(O(61), contexto=CTX_HTML)
nb.code(O(62), contexto=CTX_HTML)

# ---------------------------------------------------------------- decoradores
nb.md("""
## Decoradores

Un **decorador** es una forma abreviada de aplicar una función de orden superior como `html` a otra función, para extender lo que hace sin cambiar su código.

En la sección anterior, la función decorada se obtenía así:

```python
def parrafo(texto):
    return '<p>' + str(texto) + '</p>'

parrafo = html(parrafo)   # ahora parrafo es la funcion empaqueta
print(parrafo("Hola, Mundo."))
```

Escribir `@html` justo encima de `def parrafo` hace **exactamente lo mismo** que la línea `parrafo = html(parrafo)`: define `parrafo` y en seguida la reemplaza por la función que devuelve `html`. A esta forma abreviada se le llama *azúcar sintáctico*.
""")
nb.code(O(64))
nb.code(O(65), contexto=O(64))
CTX_DECORADO = O(64) + "\n\n" + O(65)
nb.md("Ahora el nombre `parrafo` corresponde a la función `empaqueta`:")
nb.code(O(66), contexto=CTX_DECORADO)
nb.code(O(67), contexto=CTX_DECORADO)
nb.md("""
Por la misma razón, `help(parrafo)` muestra la documentación de `empaqueta` y no la de `parrafo`: la función original quedó "envuelta". Python tiene una forma de conservar su nombre y su documentación (`functools.wraps`), que requiere importar un módulo y no se usa aquí.
""")
nb.code(O(68), contexto=CTX_DECORADO)

# ---------------------------------------------------------------- lambda
nb.md("""
## Funciones con `lambda`

Python ofrece una forma concisa de crear funciones simples con la palabra clave `lambda`. A estas se les conoce como **funciones anónimas**, porque no necesitan un nombre como las que se definen con `def`.

Una función `lambda` es como un **atajo**: hace una sola cosa y se escribe justo donde se necesita.

**Sintaxis**

La estructura de una función `lambda` es siempre:

```
lambda parámetros: expresión
```

Donde:
* **`lambda`**: la palabra clave que inicia la función anónima.
* **parámetros**: los argumentos que recibe la función, separados por comas (igual que en una función con `def`).
* **dos puntos `:`**: separan los parámetros de la operación.
* **expresión**: una única expresión, cuyo resultado se devuelve automáticamente. No se escribe `return`.

### Ejemplo: `def` frente a `lambda`

Estas dos funciones hacen exactamente lo mismo:

* **Función tradicional con `def`**:

  ```python
  def sumar(a, b):
      return a + b

  print(sumar(5, 3))
  # Salida: 8
  ```

* **Función con `lambda`**:

  ```python
  sumar_lambda = lambda a, b: a + b

  # La invocacion es igual
  print(sumar_lambda(5, 3))
  # Salida: 8
  ```

Para reutilizar una función `lambda` se le puede dar un nombre con `=`, como en el ejemplo. Sin embargo, su principal uso es **sin nombre**, como argumento de otra función.
""")
nb.python("La guía de estilo PEP 8 recomienda usar `def`, y no `lambda`, cuando la función va a tener nombre. Los ejemplos originales de esta sección le dan nombre a sus `lambda` para poder mostrarlas; el uso típico se ve en el ejemplo de `sorted()`, más abajo.")
nb.md("""
El siguiente ejemplo tiene parámetros con valores por defecto. Usa dos métodos de los textos: `.format()`, que reemplaza las llaves `{}` por un valor, y `.center(ancho)`, que centra el texto en un espacio de `ancho` caracteres rellenando con espacios a ambos lados.
""")
nb.code(O(70))
nb.code(O(71), contexto=O(70))
nb.code(O(72), contexto=O(70))
nb.code(O(73), contexto=O(70))
nb.md("""
### ¿Cuándo usar `lambda`?

Las funciones `lambda` son ideales cuando se necesita una función sencilla por un momento, especialmente como argumento de funciones de orden superior de Python como `sorted()`, `map()` y `filter()`.

**Ejemplo con `sorted()`**: `sorted(valores)` devuelve una lista nueva con los valores ordenados de menor a mayor. Con el argumento `key=`, se le pasa una función que se aplica a cada elemento para decidir el orden.

En el ejemplo, cada elemento es una tupla `(x, y)`, y `punto[1]` es su segundo valor (las posiciones empiezan en 0). La `lambda` le dice a `sorted()` que ordene por ese segundo valor.
""")
nb.code(O(75))
nb.md("""
Como se muestra en el ejemplo anterior, usar una `lambda` aquí es mucho más directo que definir con `def` una función completa solo para esta línea.

### Funciones `lambda` con `if - else`

Dentro de una `lambda` no se puede escribir un bloque `if`, pero sí una **expresión condicional**, que elige entre dos valores en una sola línea:

```
lambda <parámetros>: <expresión_1> if <condición> else <expresión_2>
```

Si la condición es verdadera, el resultado es `<expresión_1>`; si no, `<expresión_2>`.

**Ejemplo**: `es_par` es una función que valida si un número entero es par.
""")
nb.code(O(78))
nb.code(O(79), contexto=O(78))
nb.code(O(80), contexto=O(78))
nb.md("> 💡 Como `numero % 2 == 0` ya es `True` o `False`, la misma función se puede escribir más corta: `es_par = lambda numero: numero % 2 == 0`.")
nb.md("""
**Ejemplo**: una función `factorial` que calcula el factorial de un número mediante **recursividad**.

Una función es **recursiva** cuando se invoca a sí misma. Aquí, el factorial de `numero` se calcula como `numero * factorial(numero - 1)`, y la condición `if numero > 1 else 1` es la que detiene las invocaciones: cuando el número llega a 1, devuelve 1 sin volver a invocarse. Por ejemplo, `factorial(3)` es `3 * factorial(2)`, que es `3 * 2 * factorial(1)`, que es `3 * 2 * 1`.
""")
nb.code(O(82))
nb.code(O(83), contexto=O(82))
nb.md("""
Dos precisiones sobre este ejemplo, que busca mostrar la recursividad con `lambda` y no ser una función de factorial completa:

* **Dominio**: la función **supone** que `numero` es un entero mayor o igual que 0 (recuerde que 0! = 1), pero no lo valida. Con otros valores no da error, sino resultados sin sentido matemático: `factorial(-3)` devuelve `1` y `factorial(2.5)` devuelve `3.75`.
* **Dependencia del nombre**: la `lambda` funciona porque, cada vez que se invoca, busca el nombre global `factorial`. Si ese nombre se reasignara a otra cosa, la recursión dejaría de funcionar. Por eso, para funciones recursivas se recomienda usar `def`.
""")

# ---------------------------------------------------------------- errores
nb.resumen_errores([
    ("`SyntaxError`", "El código no está bien escrito; Python ni siquiera empieza a ejecutarlo",
     "Una función sin cuerpo (en un notebook: `incomplete input`); un parámetro sin valor por defecto después de uno con valor por defecto",
     "Agregar el cuerpo (o `pass`); poner los parámetros con valor por defecto al final"),
    ("`TypeError`", "La invocación o la operación no es válida",
     "Más o menos argumentos que parámetros; operar con el `None` que devuelve una función sin `return`; pasar `doble()` en vez de `doble`",
     "Revisar cuántos parámetros tiene la función; agregar el `return`; pasar la función sin paréntesis"),
    ("`NameError`", "Se usa un nombre que no existe en ese lugar",
     "Usar fuera de una función una variable local, o una función anidada",
     "Devolver el valor con `return` y guardarlo al invocar"),
    ("`UnboundLocalError`", "Se lee una variable local antes de darle valor",
     "`contador = contador + 1` dentro de una función, con `contador` global",
     "Pasar el valor como parámetro y devolver el nuevo valor"),
    ("`AssertionError`", "Una prueba con `assert` no se cumplió",
     "`assert area_rectangulo(4, 3) == 12` cuando la función suma en vez de multiplicar",
     "Corregir la función (o la prueba, si el valor esperado estaba mal)"),
    ("`KeyError`", "Se pidió a un diccionario una clave que no tiene",
     "Pedir en `**kwargs` un argumento que no se pasó",
     "Pasar el argumento, o usar `.get(clave, valor)`"),
    ("`ZeroDivisionError`", "División por cero",
     "Promediar con `*args` cuando no se pasó ningún valor",
     "Comprobar que `len(args)` no sea 0 antes de dividir"),
])

# ---------------------------------------------------------------- ejercicios
nb.ejercicios([
    '''
def doble(x):
    return 2 * x

print(doble(3) + doble(4))
''',
    '''
def saludar(nombre):
    print("Hola", nombre)

r = saludar("Ana")
print(r)
''',
    '''
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3), potencia(2, 3), potencia(exponente=0, base=7))
''',
    '''
x = 10

def cambiar():
    x = 5
    return x

print(cambiar(), x)
''',
    '''
def contar(*valores):
    return len(valores)

print(contar(), contar(4, 5, 6))
''',
    '''
def aplicar(f, valor):
    return f(f(valor))

def sumar_tres(n):
    return n + 3

print(aplicar(sumar_tres, 1))
''',
    '''
cuadrado = lambda n: n * n
print(cuadrado(4) - cuadrado(2))
''',
    '''
def info(**datos):
    return len(datos)

print(info(a=1, b=2), info())
''',
])

# ---------------------------------------------------------------- recursos
nb.recursos("""
### Herramientas

* [Python Tutor](https://pythontutor.com/): visualiza la ejecución de un programa paso a paso. Muestra cómo se crea un espacio aparte para las variables de cada invocación, lo que ayuda mucho a entender el ámbito.
* [PEP 8](https://peps.python.org/pep-0008/): guía oficial de estilo de Python (nombres de funciones, `lambda`, espacios).

### Referencias

* CS50's Introduction to Programming with Python, [Lecture 0: Functions, Variables](https://cs50.harvard.edu/python/notes/0/) y [Lecture 5: Unit Tests](https://cs50.harvard.edu/python/notes/5/) (pruebas con `assert`).
* El Libro de Python: [funciones](https://ellibrodepython.com/funciones-en-python), [`*args` y `**kwargs`](https://ellibrodepython.com/args-kwargs-python), [decoradores](https://ellibrodepython.com/decoradores-python), [`lambda`](https://ellibrodepython.com/lambda-python) y [recursividad](https://ellibrodepython.com/recursividad).
* Tutorial oficial de Python (en español): [definir funciones](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions).
* DataCamp: [el ámbito de las variables en Python](https://www.datacamp.com/tutorial/scope-of-variables-python) (en inglés).
""")

nb.escribir(RAIZ / RUTA)
