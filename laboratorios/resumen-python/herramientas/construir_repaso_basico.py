"""Contenido de repaso_basico.ipynb (formato común en formato.py).

Los ejemplos originales del notebook se toman, por posición, de la versión con
la que se agregó la carpeta al repositorio (commit 2df6db3), mediante O(i).

Uso, desde la raíz del repositorio:
    python laboratorios/resumen-python/herramientas/construir_repaso_basico.py
"""
import json
import pathlib
import subprocess
import sys

sys.dont_write_bytecode = True  # no crear __pycache__ en el repositorio
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from formato import Notebook  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[3]
RUTA = "laboratorios/resumen-python/estructurada_python/repaso_basico.ipynb"
orig = json.loads(subprocess.run(["git", "show", f"2df6db3:{RUTA}"], cwd=RAIZ, capture_output=True,
                                 check=True).stdout.decode("utf-8"))


def O(i):
    """Fuente de la celda i del notebook original."""
    return "".join(orig["cells"][i]["source"])


nb = Notebook("repaso_basico.ipynb")
nb.insignias()
nb.encabezado(
    titulo="Repaso básico de Python",
    intro=("Este notebook es un **refuerzo de Python** para quien ya entendió en clase cómo resolver "
           "un problema. Aquí no se repite la teoría: el foco está en **cómo se escribe y cómo se "
           "comporta** cada cosa en Python, con ejemplos que puede ejecutar y modificar."),
    objetivos=[
        "Reconocer los tipos básicos de Python (`int`, `float`, `bool`, `str`, `None`) y explicar por qué `7`, `7.0` y `\"7\"` son datos distintos.",
        "Nombrar variables respetando las reglas del lenguaje y la convención del curso (*snake_case*).",
        "Acceder a los caracteres de un string con índices y *slicing*, y saber cuándo eso produce un error.",
        "Mostrar resultados con `print` y **f-strings**, controlando decimales, ancho y alineación.",
        "Leer datos con `input()` y convertirlos al tipo adecuado con `int()`, `float()` y `str()`.",
        "Predecir el resultado de expresiones aritméticas, relacionales y lógicas aplicando la prioridad de operadores de Python.",
        "Leer un mensaje de error de Python (`SyntaxError`, `TypeError`, `ValueError`, `IndexError`, `ZeroDivisionError`...) e identificar cómo corregirlo.",
    ],
)

# ---------------------------------------------------------------- variables
nb.md("""
## Variables

### Asignación

Una variable se crea **asignándole un valor** con el signo `=`:

```python
nota = 4.5
```

Se lee de derecha a izquierda: Python calcula primero lo que está a la derecha del `=` y guarda el resultado con el nombre de la izquierda. Si la variable ya existía, su valor anterior se reemplaza. Por eso `contador = contador + 1` tiene sentido: toma el valor actual de `contador`, le suma 1 y guarda el resultado en la misma variable.

Ojo: en Python `=` **no** significa "es igual a"; para comparar se usa `==` (se ve en la sección de operadores relacionales).
""")
nb.code('''
contador = 0
contador = contador + 1
print(contador)
''')
nb.error("Una variable debe tener un valor **antes** de usarse en una expresión. Si no, Python lanza `NameError: name '...' is not defined`. Pasa lo mismo si el nombre está mal escrito (`Contador` en vez de `contador`). En la siguiente celda, `puntaje` nunca recibió un valor.")
nb.code('''
puntaje = puntaje + 1
print(puntaje)
''')
nb.md("""
### Tipos de datos escalares

En Python existen tres tipos de datos escalares (un solo valor) y un valor especial:
* **int**: números enteros (ej.: 7)
* **float**: números reales (ej.: 8.295)
* **bool**: valores booleanos: verdadero (`True`) o falso (`False`)
* **None**: no es un tipo sino un **valor especial** que representa la ausencia de datos; su tipo se llama `NoneType`, como se ve en el último ejemplo.

Los textos son de tipo **str** (strings); tienen su propia sección más abajo.

Para saber el tipo de dato al que pertenece una variable se suele emplear la función **type()**. A continuación se muestran algunos ejemplos:
""")
nb.code(O(4))
nb.code(O(5))
nb.code(O(6).replace("booleam", "boolean"))
nb.code(O(7))
nb.md("""
### Cómo funciona en Python: el tipo lo tiene el valor

En Python no se declara el tipo de una variable: una variable es un **nombre** que apunta a un valor, y el tipo lo tiene **el valor**. Por eso la misma variable puede apuntar primero a un entero y después a un texto (esto se llama *tipado dinámico*). Es cómodo, pero obliga a estar atento: `7`, `7.0` y `"7"` se ven parecidos y son tres cosas distintas.

Observe también que un número escrito con punto (`3.`) ya es `float`, aunque no tenga decimales.
""")
nb.prediga("¿Qué tipo imprime cada línea? ¿Cuál de las dos comparaciones da `True`?")
nb.code('''
dato = 7
print(dato, type(dato))
dato = 7.0
print(dato, type(dato))
dato = "7"
print(dato, type(dato))

print(7 == 7.0)    # mismo valor numérico, aunque los tipos sean distintos
print(7 == "7")    # un número nunca es igual a un texto
''')
nb.md("""
### Nombres de variables

Reglas **del lenguaje** (si no se cumplen, Python da error):

* El nombre empieza con una letra o un guion bajo (`_`), y después puede tener letras, dígitos y `_`. No puede tener espacios ni signos como `-`, `.` o `%`.
* Se distinguen mayúsculas de minúsculas: `nota`, `Nota` y `NOTA` son tres variables distintas.
* No se pueden usar **palabras reservadas** de Python como nombre: `if`, `else`, `elif`, `while`, `for`, `in`, `def`, `return`, `and`, `or`, `not`, `True`, `False`, `None`, `import`, `break`, `continue`, entre otras.

Hay dos estilos de nombrado muy usados en programación:
1. **camelCase**: `notaFinal` (común en Java o JavaScript).
2. **snake_case**: `nota_final` (el estilo recomendado en Python por la guía [PEP 8](https://peps.python.org/pep-0008/)).
""")
nb.convencion("Use **snake_case** y nombres que digan qué guardan (`total_notas` y no `tn` o `x2`). Las constantes van en MAYÚSCULAS (`NOTA_MAXIMA = 5.0`). Más adelante en este notebook aparecen nombres como `firstName`: funcionan, pero no siguen esta convención.")
nb.code('''
nota = 4.5
Nota = 2.0
NOTA_MAXIMA = 5.0
print(nota, Nota, NOTA_MAXIMA)    # tres variables distintas
''')
nb.error("Un nombre que empieza con un dígito no es válido. Python ni siquiera empieza a ejecutar la celda: lanza `SyntaxError` (error de sintaxis) y señala con `^` dónde está el problema.")
nb.code('''
2nota = 3.5
print(2nota)
''')
nb.error("Las instrucciones de este notebook empiezan **pegadas al margen izquierdo**. Los espacios al inicio de una línea (la *sangría*) tienen significado en Python: indican que la línea pertenece a un bloque, algo que se verá con las estructuras de control. Una línea con espacios de más, sin pertenecer a un bloque, da `IndentationError: unexpected indent`.")
nb.code('''
x = 1
    y = 2
print(x)
''')

# ---------------------------------------------------------------- strings
nb.md("""
## Strings: cadenas de caracteres

Los strings son secuencias de caracteres (símbolos). Son muy utilizados debido a que la mayoría de los programas necesitan en algún momento almacenar y procesar textos.
""")
nb.code(O(10))
nb.md('''
### Cómo funciona en Python: comillas y caracteres especiales

* Las comillas **simples** (`'...'`) y **dobles** (`"..."`) son equivalentes. Se elige una u otra según el texto: si el texto lleva comillas dobles, se encierra en simples, y al revés.
* Dentro de un string, la barra invertida `\\` introduce caracteres especiales: `\\n` es un salto de línea y `\\t` una tabulación.
* En varias celdas de este notebook aparece una línea como `""" strings """` al inicio. Es un string que no se asigna a ninguna variable: Python lo evalúa y lo descarta, así que funciona como un rótulo. Para comentar, lo habitual es usar `#`.
''')
nb.code('''
print('Ella dijo: "hola"')
print("It's ok")
print("Linea 1\\nLinea 2")
print("Nombre:\\tAna")
''')
nb.md("""
### Operadores básicos de los string

* **Concatenación**: emplea el signo más (`+`) para unir dos string.

```python
string1 + string2
```

* **Repetición**: emplea el signo por (`*`), el cual, cuando se usa multiplicando un entero **n** por un string, hace que este se repita **n** veces.

```python
num*string
```

* **Longitud**: función que permite obtener la longitud de un string.

```python
len(string)
```
""")
nb.prediga("¿Qué imprimen `0*s4` y `-3*s4`? ¿Dan error?")
nb.code(O(12).replace("Operacioes basicas", "Operaciones basicas"))
nb.md("""
### Acceso a los elementos de un string

La operación fundamental cuando se trabaja con secuencias es la **indexación**. Para indexar los caracteres en un string se usan los corchetes `[]` colocando el subíndice o la secuencia de indexado específica.

Los diferentes tipos de indexación son:
1. **Acceso a un único elemento**: sea un string **S** de **N** elementos, el acceso a uno de los elementos se hace mediante un subíndice **i** entre **0** y **N - 1**. Python también soporta indexado negativo, siendo **-1** el último del string y **-N** el primer elemento.
""")
nb.code(O(14).replace(
    "# Indexado con subindices positivos para obtener la U, r, A, i (ultima), a (ultima)\nprint(universidad[-24])",
    "# Indexado con subindices negativos para obtener la U, r, A, i (ultima), a (ultima)\nprint(universidad[-24])"))
nb.error("Un subíndice **mayor o igual** que `len(...)` no existe: Python lanza `IndexError: string index out of range`. Aquí el string tiene 24 caracteres, así que el último índice válido es 23.")
nb.code('''
universidad = "Universidad de Antioquia"
print(universidad[24])
''')
nb.convencion("Puede usar índices negativos cuando le resulten más claros (por ejemplo `texto[-1]` para el último carácter). Tenga presente que un índice negativo **no da error**: si por una cuenta mal hecha termina usando `-1` donde esperaba `0`, Python devuelve silenciosamente el último elemento y el error queda escondido. En cambio, un índice demasiado grande sí avisa con `IndexError`.")
nb.md("""
2. **Slicing**: operación empleada para acceder a un segmento de un string. Tenemos para tal fin varias formas:
   * Usando la sintaxis **[start:stop]**, en donde se extraen los caracteres entre las posiciones **start** y **stop - 1**.
   * Usando la sintaxis **[start:stop:step]**. Aquí se define el tamaño del paso (**step**), cuyo valor por defecto es **1**.
""")
nb.code(O(16))
nb.md("""
Cuando se omite en el intervalo el **start** o el **stop**, se toma por defecto el principio y el final del string, respectivamente. Por otro lado, cuando se omite el **step**, el valor que este toma por defecto es 1. Con un **step** negativo el recorrido va de derecha a izquierda.
""")
nb.prediga("¿Qué imprime `universidad[::4]`? ¿Y `universidad[-1::-3]`?")
nb.code(O(18))
nb.md("""
> 💡 A diferencia del acceso a un único elemento, el *slicing* **no da error** si los límites se salen del string: simplemente recorta hasta donde hay caracteres.
""")
nb.code('''
universidad = "Universidad de Antioquia"
print(universidad[20:100])
print(universidad[30:40])    # string vacio: no hay caracteres en ese rango
print(len(universidad[30:40]))
''')
nb.md("""
### Cómo funciona en Python: los strings no se pueden modificar

Un string es **inmutable**: se puede leer `texto[0]`, pero no cambiar `texto[0] = ...`. Para "cambiar" un texto se construye uno nuevo y se asigna a la variable.
""")
nb.code('''
universidad = "Universidad de Antioquia"
universidad[0] = "u"
''')
nb.code('''
universidad = "Universidad de Antioquia"
universidad = "u" + universidad[1:]    # "u" + todo desde la posicion 1: un string nuevo
print(universidad)
''')

# ---------------------------------------------------------------- print
nb.md("""
## Print

`print` permite poner en pantalla información literal así como valores de variables. Existen varias maneras de hacer esto. A continuación se muestra cómo:
1. **Imprimir concatenando strings con el signo +**:
""")
nb.code(O(20).replace("Contatenación", "Concatenación"))
nb.md("""
2. **Imprimir varios valores: separados por coma o strings escritos juntos**:
""")
nb.code(O(22))
nb.md("""
Observe las tres líneas: dos strings escritos uno al lado del otro se pegan sin espacio (Python los une en uno solo); separados por coma, `print` recibe **varios valores** y los muestra separados por un espacio, lo cual no es lo mismo que concatenar con `+`: con la coma se pueden mezclar textos y números sin convertirlos (`print("Edad:", 18)`); y entre paréntesis forman una *tupla*, que es un grupo de valores entre paréntesis (no hace falta para este notebook), por eso se imprimen con paréntesis y comillas.

### Cómo funciona en Python: `sep` y `end`

Cuando `print` recibe varios valores separados por coma, los separa con un espacio y al final pone un salto de línea. Ambas cosas se pueden cambiar con los parámetros `sep` (separador) y `end` (final).
""")
nb.code('''
print("A", "B", "C")
print("A", "B", "C", sep="-")
print("A", "B", "C", sep="")
print("Sin salto", end=" ")
print("de linea")
''')
nb.md("""
### f-strings (cadenas con formato)

Es la forma recomendada de mostrar resultados. Se escribe una `f` antes de las comillas y, dentro del texto, las variables o expresiones entre llaves `{}`. Python reemplaza cada `{...}` por su valor. Después de `:` se puede indicar el formato; por ejemplo, `:.2f` muestra un `float` con 2 decimales.
""")
nb.convencion("Para mostrar resultados use **f-strings**, y para los decimales `:.2f` (o los que pida el problema, como `:.6f`). Es la forma que usa el código de las clases.")
nb.code('''
x = 3
y = 3.
suma = x + y
print(f"La suma de {x} y {y} es {suma}")
print(f"La suma de {x} y {y:.2f} es {suma:.2f}")

promedio = 10 / 3
print(f"Promedio: {promedio:.2f}")
print(f"Promedio: {promedio:.6f}")
''')
nb.md("""
#### Qué puede ir dentro de las llaves

Dentro de `{}` puede ir cualquier **expresión** de Python: una variable, una operación, una comparación o una llamada a una función como `len()` o `int()`. Python la calcula y pone el resultado en el texto.

Si dentro de las llaves necesita escribir un texto, use comillas **distintas** a las de la f-string: `f"{'hola'}"`, no `f"{"hola"}"` (esto último solo funciona desde Python 3.12).
""")
nb.code('''
nombre = "Ana"
nota1 = 4.0
nota2 = 3.5
print(f"Estudiante: {nombre}")
print(f"El nombre tiene {len(nombre)} letras")
print(f"Promedio: {(nota1 + nota2) / 2}")
print(f"Aprobo: {(nota1 + nota2) / 2 >= 3.0}")
print(f"{nota1} + {nota2} = {nota1 + nota2}")
''')
nb.md("""
#### El especificador de formato

Lo que va después de `:` dentro de las llaves dice **cómo mostrar** el valor:

| Especificador | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `.2f` | `float` con 2 decimales (redondea solo al mostrar) | `f"{3.14159:.2f}"` | `3.14` |
| `.0f` | Sin decimales | `f"{2.71828:.0f}"` | `3` |
| `d` | Entero (solo para `int`) | `f"{42:d}"` | `42` |
| `,` | Separador de miles | `f"{1234567:,}"` | `1,234,567` |
| `,.2f` | Separador de miles y 2 decimales | `f"{1234567.891:,.2f}"` | `1,234,567.89` |
| `.1%` | Porcentaje: multiplica por 100 y agrega `%` | `f"{0.256:.1%}"` | `25.6%` |
| `+d` | Muestra siempre el signo | `f"{5:+d}"` | `+5` |
| `>5`, `<5`, `^6` | Ancho mínimo, alineado a la derecha, izquierda o centro | `f"[{'ab':>5}]"` | `[   ab]` |
| `8.2f` | Ancho 8 **y** 2 decimales | `f"[{3.5:8.2f}]"` | `[    3.50]` |
| `05d` | Ancho 5, rellenando con ceros | `f"{7:05d}"` | `00007` |
| `*^10` | Ancho 10, centrado, rellenando con `*` | `f"{'hola':*^10}"` | `***hola***` |

El orden es siempre el mismo: **relleno, alineación, signo, ancho, separador, decimales y tipo**; cada parte es opcional. Observe que `,` usa la convención en inglés (coma para miles y punto para decimales).
""")
nb.prediga("Use la tabla para escribir qué imprime cada línea.")
nb.code('''
total = 1234567.891
tasa = 0.075
print(f"Total: {total:,.2f}")
print(f"Tasa: {tasa:.1%}")
print(f"Codigo: {7:05d}")
print(f"Diferencia: {-3:+d} y {3:+d}")
print(f"[{'izq':<8}]")
print(f"[{'der':>8}]")
print(f"[{'centro':^10}]")
''')
nb.md("""
#### Alinear columnas

El ancho y la alineación sirven para imprimir datos en forma de tabla: cada columna ocupa siempre el mismo número de caracteres, sin importar cuánto mida el dato. Lo usual es alinear el texto a la izquierda y los números a la derecha.
""")
nb.code('''
print(f"{'Producto':<10}{'Cant':>6}{'Precio':>12}")
print(f"{'Donas':<10}{12:>6}{1500:>12,.2f}")
print(f"{'Duff':<10}{6:>6}{4200.5:>12,.2f}")
print(f"{'Squishee':<10}{3:>6}{18000:>12,.2f}")
''')
nb.md("""
#### `{variable=}` para depurar

Si después del nombre se escribe `=`, la f-string imprime **el texto de la expresión y su valor**. Es muy útil para los `print()` de depuración: se ve qué variable es cada número sin tener que escribir la etiqueta a mano.
""")
nb.code('''
x = 7
y = 2
print(f"{x=}, {y=}")
print(f"{x // y=}, {x % y=}")
print(f"{x / y=:.2f}")
''')
nb.md("""
#### Llaves literales

Como `{` y `}` tienen un significado especial, para que aparezcan tal cual en el texto se escriben dobles: `{{` y `}}`.
""")
nb.code('''
x = 7
print(f"{{x}} vale {x}")
''')
nb.error("Si se olvida la `f` antes de las comillas **no hay error**: Python imprime las llaves y el nombre tal cual. Es fácil de pasar por alto porque el programa \"funciona\".")
nb.code('''
nota = 4.5
print("Nota final: {nota}")     # falta la f
print(f"Nota final: {nota}")
''')
nb.error("El formato `.2f` solo sirve para números. Si el dato viene de `input()` y no se convirtió, es un `str` y Python lanza `ValueError: Unknown format code 'f' for object of type 'str'`. Pasa algo parecido al usar `d` con un `float`: el mensaje termina en `... for object of type 'float'`. La solución es convertir el dato con `float()` o `int()` antes de mostrarlo.")
nb.code('''
precio = "1500"      # asi llega lo que se lee con input()
print(f"Precio: {precio:.2f}")
''')
nb.md("""
#### `:.2f` frente a `round()`

`:.2f` solo cambia cómo **se muestra** el número; el valor guardado en la variable no cambia. La función `round(valor, 2)`, en cambio, **calcula** un número nuevo redondeado, y al imprimirlo no muestra ceros a la derecha. Para mostrar resultados, use `:.2f`.
""")
nb.code('''
promedio = 3.0
print(f"{promedio:.2f}")      # formato: siempre 2 decimales
print(round(promedio, 2))     # numero redondeado: 3.0
print(round(10 / 3, 2))
''')
nb.md("""
### Otras formas de dar formato: `%` y `format`

Hay otras dos formas de dar formato que encontrará en códigos más antiguos o de otros autores. Funcionan, pero en este curso se prefieren las f-strings.

* **Empleando el operador `%`**: el texto lleva marcas que se reemplazan, en orden, por los valores escritos después del `%`. Las marcas más comunes son `%d` (entero), `%f` (real, con 6 decimales) y `%.3f` (real con 3 decimales). Si hay varios valores, van entre paréntesis y separados por coma.

En el ejemplo, la variable se llama `sum_` (con guion bajo al final) porque `sum` ya es el nombre de una función de Python; agregar `_` es una forma habitual de no taparla.
""")
nb.code(O(24))
nb.md("""
> 💡 Fíjese en la segunda línea: `%d` muestra un entero, así que `1.5` se imprime como `1` (se trunca). Lo mismo pasa con `sum_` en la última línea.

* **Usando `format`**: se escribe el texto con llaves `{}` y después `.format(...)` con los valores; cada `{}` se reemplaza, en orden, por un valor. Dentro de las llaves se puede indicar el formato igual que en las f-strings (`{:.2f}`), o un nombre (`{verbo}`) que se asigna dentro de `format`.
""")
nb.code(O(26))

# ---------------------------------------------------------------- input
nb.md("""
## input

Tiene como objetivo principal recibir datos, a la vez que permite anteceder la recepción de los mismos con algún mensaje que le indique al usuario qué es lo que el programa espera recibir.

### Cómo funciona en Python: `input()`

* `input(mensaje)` muestra el mensaje, **detiene el programa** hasta que el usuario escribe algo y presiona `Enter`, y devuelve lo escrito.
* Lo que devuelve **siempre es un `str`**, aunque el usuario escriba un número.
* El mensaje se imprime tal cual, sin espacio al final: por eso conviene terminarlo en `": "`.
""")
nb.convencion("Los nombres `firstName` y `lastName` de la siguiente celda funcionan, pero en snake_case serían `nombre` y `apellido`.")
nb.code(O(28).replace("Digite al apellido", "Digite el apellido"), entradas=["Ana", "Pérez"])
nb.md("""
Para ver qué significa que `input()` devuelva un `str`, la siguiente celda usa directamente el texto `"18"`, que es exactamente lo que llegaría si el usuario escribe 18:
""")
nb.prediga("¿Qué imprime `edad * 2`? ¿Y `int(edad) * 2`? (La función `int()` convierte el texto en un número entero; se explica en detalle en [Sobre la conversión de datos](#sobre-la-conversion-de-datos)).")
nb.code('''
edad = "18"          # asi llega lo que se lee con input()
print(type(edad))
print(edad * 2)      # repite el texto
print(int(edad) * 2) # convierte a entero y multiplica
''')

# ---------------------------------------------------------------- cast
nb.md("""
### Sobre la conversión de datos

Como sucede en los lenguajes de programación en general, en Python es necesario que los operandos sean del tipo adecuado para poder llevar a cabo la operación; si no, habrá un error tal y como se muestra a continuación:
""")
nb.code(O(30))
nb.md("""
#### Conversión de datos - Cast

Ya que las variables en Python son dinámicamente creadas, es necesario tener en cuenta los tipos de datos manejados en el momento en que se llevan a cabo operaciones. Cuando dos variables comparten el mismo tipo no hay problema. El problema viene cuando las variables que operan son incompatibles para la operación que se está ejecutando. El cast en Python se hace de la siguiente forma:

```
tipoDato(variable)
```
Veamos diferentes escenarios de aplicación:
""")
nb.md("* **Caso 1**: no hay problema en la lógica del programa, por lo tanto no es necesario convertir.")
nb.code(O(33), entradas=["Keanu Reeves", "Neo"])
nb.md("* **Caso 2**: no hay error, pero la lógica del problema falla.")
nb.code(O(35), entradas=["3", "4"])
nb.md("""
* **Caso 3**: hay error en la operación, por lo que es necesario convertir. Es el ejemplo del inicio de esta sección (`s1 + 3`); la solución se muestra a continuación. Nótese la parte donde se llevó a cabo el **cast**:
""")
nb.code(O(39).replace("# Esto es un error", "# Corregido: str(3) convierte el entero en texto"))
nb.md("**Usando cast para corregir los bugs del programa de la suma**")
nb.code(O(41), entradas=["3", "4"])
nb.md("**Print y el cast**: cuando se concatenan diferentes tipos de datos en un string con el signo más (`+`), no olvide convertirlos todos a string. Aquí se muestra el caso en que el string a imprimir se concatena con `+` antes de imprimir.")
nb.code(O(43), entradas=["Ana", "18"])
nb.md("""
> 💡 Con una f-string no hace falta convertir a `str`: `print(f"{nombre} usted tiene {edad_dias} dias")` produce lo mismo.

### Cómo funciona en Python: qué hace cada conversión
""")
nb.prediga("¿Qué imprimen `int(3.99)` e `int(-3.99)`? ¿Redondean?")
nb.code('''
print(int("42"))
print(float("3.5"))
print(float(7))
print(int(3.99))      # int() trunca: descarta los decimales, no redondea
print(int(-3.99))
print(str(4.5) + "!")
print(int(" 7 "))     # los espacios al inicio y al final se ignoran
''')
nb.md("> 💡 No confunda convertir con dar formato: `int(3.99)` produce el **número** `3` (trunca), mientras que `f\"{3.99:.1f}\"` produce el **texto** `4.0` (redondea solo para mostrarlo) y no cambia el valor de la variable.")
nb.error("`int()` solo acepta textos que representen un **entero**. Si el usuario escribe `3.5` y el programa hace `int(input(...))`, Python lanza `ValueError: invalid literal for int() with base 10`. Si el dato puede tener decimales, lea con `float(input(...))`.")
nb.code('''
print(int(float("3.5")))   # primero a float y luego a int: funciona
print(int("3.5"))          # error
''')

# ---------------------------------------------------------------- operadores
nb.md("## Operadores")
nb.md("""
### Aritméticos

| Signo | Operador | Ejemplo | Resultado  |
| ------|----------| ------- | ---------- |
|+|Suma|3 + 4.5| 7.5 |
|-|Resta|5 - 4.5| 0.5 |
| * | Multiplicación | 5*4 | 20 |
| / | División | 9/2 | 4.5 |
| // | División entera | 9//2 | 4 |
| % | Módulo | 9%2 | 1 |
| ** | Potenciación | 9**2 | 81 |

A continuación se muestran diferentes ejemplos:
""")
nb.code(O(46))
nb.md("""
### Cómo funciona en Python: tipos del resultado

* `/` **siempre** devuelve `float`, aunque la división sea exacta: `4 / 2` da `2.0`.
* `//` y `%` con enteros devuelven enteros; si algún operando es `float`, el resultado es `float`.
* `//` redondea **hacia abajo** (hacia menos infinito), no hacia cero: `-7 // 2` da `-4`. Y `%` cumple siempre que `a == (a // b) * b + a % b`.
* `**` acepta exponentes negativos y fraccionarios: `9 ** 0.5` es la raíz cuadrada de 9.
* Si se mezclan `int` y `float`, el resultado es `float`.
""")
nb.prediga("Escriba el resultado de cada línea, incluyendo si lleva `.0` o no.")
nb.code('''
print(4 / 2)
print(7 // 2, 7 % 2)
print(-7 // 2, -7 % 2)
print(7.0 // 2)
print(2 ** 10)
print(2 ** -1)
print(9 ** 0.5)
print(2 + 3.0)
''')
nb.error("Dividir por cero, con `/`, `//` o `%`, lanza `ZeroDivisionError`. Antes de dividir por un dato que puede valer 0 (por ejemplo, una cantidad de notas leídas), hay que comprobarlo.")
nb.code('''
total = 10
cantidad = 0
print(total / cantidad)
''')
nb.md("""
### Prioridad de los operadores

Cuando una expresión tiene varios operadores, Python los evalúa en este orden (de mayor a menor prioridad):

| Prioridad | Operadores | Comentario |
|---|---|---|
| 1 | `( )` | Los paréntesis siempre se evalúan primero |
| 2 | `**` | Se agrupa de **derecha a izquierda**: `2 ** 3 ** 2` es `2 ** 9` |
| 3 | `-x` (signo negativo) | El signo a la **izquierda** de `**` va después: `-2 ** 2` es `-(2 ** 2)`. El signo a la **derecha** se aplica primero: `2 ** -2` es `2 ** (-2)` |
| 4 | `*`, `/`, `//`, `%` | De izquierda a derecha |
| 5 | `+`, `-` | De izquierda a derecha |
| 6 | `<`, `<=`, `>`, `>=`, `==`, `!=` | |
| 7 | `not` | |
| 8 | `and` | |
| 9 | `or` | |

Ante la duda, use paréntesis: no cambian el resultado si ya era correcto y hacen la expresión más fácil de leer.
""")
nb.prediga("Calcule cada línea a mano siguiendo la tabla.")
nb.code('''
print(2 + 3 * 4)
print((2 + 3) * 4)
print(-2 ** 2)
print((-2) ** 2)
print(2 ** -2)
print(2 ** 3 ** 2)
print(10 - 4 - 3)
print(10 / 2 * 5)
''')
nb.md("""
### Relacionales

| Signo | Operador | Ejemplo | Resultado  |
| ------|----------| ------- | ---------- |
| > | Mayor a | 4 > 3| True |
| < | Menor a | 4 < 3| False |
| >= | Mayor o igual a | -20 >= -10  | False |
| <= | Menor o igual a | -20 <= -10 | True |
| != | Diferente a | 2 != 3| True |
| == | Igual a | 2 == 2 | True |

A continuación se muestran diferentes ejemplos:
""")
nb.code(O(48))
nb.md("""
### Cómo funciona en Python: comparaciones

* `=` **asigna** y `==` **compara**. Confundirlos es uno de los errores más comunes.
* Python permite **encadenar** comparaciones: `0 <= nota <= 5` equivale a `0 <= nota and nota <= 5`.
* Los strings se comparan **carácter por carácter** (orden alfabético según el código de cada carácter): por eso `"10" < "9"` es `True`, porque compara `"1"` con `"9"`. Compare números como números, no como texto.
* Los `float` se guardan de forma aproximada: `0.1 + 0.2` no es exactamente `0.3`. Para comparar reales, se mira si la diferencia es muy pequeña: `abs(x)` devuelve el valor absoluto de `x`, y `1e-9` es notación científica para 1 × 10⁻⁹, es decir, `0.000000001`.
""")
nb.prediga("¿Cuáles de estas líneas imprimen `True`?")
nb.code('''
nota = 3.5
print(0 <= nota <= 5)
print(nota >= 0 and nota <= 5)
print("10" < "9")
print(10 < 9)
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(abs((0.1 + 0.2) - 0.3) < 1e-9)
''')
nb.md("""
### Lógicos

#### and

| op1 | op2 | op1 and op2 |
| ------|----------| ------- |
| False | False | False |
| False | True | False |
| True | False | False  |
| True | True | True |

#### or

| op1 | op2 | op1 or op2 |
| ------|----------| ------- |
| False | False | False |
| False | True | True |
| True | False | True  |
| True | True | True |

#### not

| op | not(op) |
| ------|----------|
| False | True |
| True | False |

**Ejemplos**:
""")
nb.code(O(50))
nb.md("""
### Cómo funciona en Python: operadores lógicos

* En Python los operadores lógicos son **palabras**: `and`, `or`, `not`. Los símbolos `&&`, `||` y `!` de otros lenguajes (C, Java) no existen en Python.
* `not` no necesita paréntesis: `not y` y `not(y)` son lo mismo.
* **Evaluación en cortocircuito**: si con el primer operando ya se sabe el resultado, Python **no evalúa** el segundo. En `False and ...` el resultado es `False` sin mirar el resto; en `True or ...`, es `True`. Esto permite proteger una división, como en la celda siguiente.
""")
nb.prediga("`divisor` vale 0. ¿Alguna de las dos líneas lanza `ZeroDivisionError`?")
nb.code('''
divisor = 0
print(divisor != 0 and 10 / divisor > 1)
print(divisor == 0 or 10 / divisor > 1)
''')
nb.md("""
### Abreviaciones de operaciones matemáticas

Hay casos en los que la variable resultado es usada también como operando. Por ejemplo:

```python
a = a + 1
```

En estos casos, es posible omitir la variable resultado en la parte en la que esta funciona como operando, empleando un abreviado de la operación tal y como se muestra a continuación:

```python
a += 1
```

Este tipo de abreviaciones funciona con todos los operadores aritméticos: `+=`, `-=`, `*=`, `/=`, `//=`, `%=` y `**=`. Veamos un ejemplo:
""")
nb.code(O(52))
nb.prediga("Siga el valor de `a` línea por línea. ¿En qué momento deja de ser entero?")
nb.code('''
a = 10
a += 5
print(a)
a -= 3
print(a)
a *= 2
print(a)
a /= 4
print(a)
a //= 2
print(a)
a **= 2
print(a)
a %= 5
print(a)
''')
nb.error("En Python **no existen** `a++` ni `a--` (sí existen en C o Java). Escribir `a++` da `SyntaxError`; use `a += 1`.")
nb.code('''
a = 1
a++
''')

# ---------------------------------------------------------------- errores
nb.md("""
## Resumen: errores frecuentes

Cómo leer un mensaje de error:

1. Lea la **última línea**: dice qué tipo de error ocurrió y, casi siempre, por qué.
2. Busque la **línea del código** que señala el mensaje (las líneas de arriba lo indican, a veces con una flecha `---->` o con `^`).
3. Revise qué operación hacía esa línea y con qué valores y tipos. Por ejemplo, ante un `TypeError`, compruebe si está sumando un texto y un número.

No cambie cosas al azar: use el mensaje para formular una hipótesis sobre la causa y corrija eso.

En un notebook, el error puede mencionar un archivo con un nombre extraño, como `915546707.py`: es un nombre interno que el notebook le da a la celda, no un archivo suyo. Lo que importa es el **número de línea** dentro de la celda.

| Error | Qué significa | Ejemplo típico | Cómo se corrige |
|---|---|---|---|
| `SyntaxError` | El código no está bien escrito; Python ni siquiera empieza a ejecutarlo | `2nota = 3`, `a++`, un paréntesis o una comilla sin cerrar | Revisar la línea señalada con `^` (o la anterior) |
| `IndentationError` | La sangría (espacios al inicio de la línea) no es la esperada | Una línea con espacios de más al inicio, sin pertenecer a un bloque | Quitar los espacios: en este notebook todas las instrucciones empiezan en el margen izquierdo |
| `NameError` | Se usa un nombre que no existe | Un nombre mal escrito (`Nota` en vez de `nota`) o una variable usada antes de asignarla | Revisar mayúsculas y que la variable se haya creado antes |
| `TypeError` | La operación no es válida para esos tipos, o el dato no se puede modificar | `"Test" + 3`, `texto[0] = "x"` | Convertir con `str()`, `int()` o `float()`, o construir un dato nuevo |
| `ValueError` | El tipo es correcto pero el valor no sirve | `int("3.5")`, `int("tres")` | Leer con el tipo adecuado o validar el dato |
| `IndexError` | La posición no existe | `texto[len(texto)]` | Recordar que el último índice es `len(texto) - 1` |
| `ZeroDivisionError` | División por cero | `total / 0` | Comprobar el divisor antes de dividir |
""")

# ---------------------------------------------------------------- ejercicios
EJERCICIOS = [
    '''
x = 7
y = 2
print(x / y, x // y, x % y)
''',
    '''
s = "Antioquia"
print(s[0] + s[-1], len(s), s[2:5])
''',
    '''
a = "5"
b = 2
print(a * b)
print(int(a) * b)
''',
    '''
print(2 + 3 * 2 ** 2)
print(-3 ** 2)
''',
    '''
n = 17
print(n % 2 == 1 and n > 10)
print(not n > 10 or n < 0)
''',
    '''
p = 2 / 3
print(f"{p:.2f}")
print(int(p * 10))
''',
    '''
total = 1234.5
print(f"Total: ${total:,.2f}")
print(f"[{'si':^6}]")
print(f"{0.075:.1%}")
''',
    '''
a = 5
b = 3
print(f"{a} / {b} = {a / b:.3f}")
print(f"{a=}, {a % b=}")
print("{a} + {b}")
''',
]
nb.ejercicios(EJERCICIOS)

# ---------------------------------------------------------------- recursos
nb.md("## Recursos adicionales")
nb.md("""
### Herramientas

* [Python Tutor](https://pythontutor.com/): visualiza la ejecución de un programa paso a paso.
* [PEP 8](https://peps.python.org/pep-0008/): guía oficial de estilo de Python (nombres, espacios, longitud de línea).

### Referencias principales

* https://cs50.harvard.edu/summer/2025/
* https://cs50.harvard.edu/summer/2024/
* https://github.com/microsoft/python-course
* https://developers.google.com/edu/python?hl=es-419
* https://github.com/iot-udea/repaso-python
* https://github.com/diplomado-bigdata-machinelearning-udea/Curso1/blob/master/s01/s01.ipynb
* https://github.com/microsoft/c9-python-getting-started
* https://github.com/ndleah/python-mini-project/tree/main
* https://realpython.com/github-copilot-python/
""")
nb.md("""
### Enlaces adicionales

* https://github.com/PythonistaMX/py101
* https://github.com/masterdatascience-UIMP-UC/introduccion-a-python
* https://github.com/joanby/python-ml-course/tree/master/notebooks
* https://github.com/iot-udea/repaso-python
* https://github.com/diplomado-bigdata-machinelearning-udea/Curso1/blob/master/s01/s01.ipynb
* https://mybinder.org/v2/gh/sisaza/informatica.git/master
""")

nb.escribir(RAIZ / RUTA)
