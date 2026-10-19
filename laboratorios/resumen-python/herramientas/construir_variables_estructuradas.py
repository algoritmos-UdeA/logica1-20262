"""Contenido de variables_estructuradas.ipynb (formato común en formato.py).

Los ejemplos originales del notebook se toman, por posición, de la versión con
la que se agregó la carpeta al repositorio (commit 2df6db3), mediante O(i).
Decisión del docente (2026-10-19): en este notebook prima el contenido de
Python sobre lo visto en clase; métodos, tuplas y diccionarios van en el
cuerpo, marcados con 🐍 y explicados completos (autocontenido). Las tablas
de operadores y métodos del original tenían resultados incorrectos; aquí se
reescriben con los valores verificados en Python 3.11.

Uso, desde la raíz del repositorio:
    python laboratorios/resumen-python/herramientas/construir_variables_estructuradas.py
"""
import json
import pathlib
import subprocess
import sys

sys.dont_write_bytecode = True  # no crear __pycache__ en el repositorio
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from formato import Notebook  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[3]
RUTA = "laboratorios/resumen-python/estructurada_python/variables_estructuradas.ipynb"
orig = json.loads(subprocess.run(["git", "show", f"2df6db3:{RUTA}"], cwd=RAIZ, capture_output=True,
                                 check=True).stdout.decode("utf-8"))


def O(i):
    """Fuente de la celda i del notebook original."""
    return "".join(orig["cells"][i]["source"])


class Cadena:
    """Celdas originales que se ejecutan en secuencia y modifican los mismos datos.

    Cada celda recibe como contexto (para Python Tutor) el código de las celdas
    anteriores de la misma cadena.
    """

    def __init__(self):
        self.previas = []

    def code(self, fuente, acumular=True):
        nb.code(fuente, contexto="\n\n".join(self.previas) if self.previas else None)
        if acumular:
            self.previas.append(fuente.strip("\n"))


nb = Notebook("variables_estructuradas.ipynb")
nb.insignias()
nb.encabezado(
    titulo="Tipos de datos estructurados",
    intro=("Este notebook es un **refuerzo de Python** sobre los tipos que guardan **varios datos** en una "
           "sola variable: los textos (`str`), las **listas**, las **tuplas** y los **diccionarios**. Muestra "
           "sus operadores y sus métodos tal como los ofrece Python. Varias de estas herramientas no se usan "
           "en los ejercicios del curso, o se ven más adelante; esas partes están marcadas con 🐍 y se "
           "explican completas aquí."),
    antes_de_empezar=("Este notebook supone que ya sabe usar variables, `print`, f-strings, condicionales, "
                      "ciclos y funciones en Python. Si necesita repasarlos, están en los notebooks *Repaso "
                      "básico de Python*, *Control de flujo* y *Funciones* de esta misma carpeta. Lo demás que "
                      "se usa aquí, incluidas las partes marcadas con 🐍, se explica aquí."),
    objetivos=[
        "Usar los operadores de los textos (índices, *slicing*, `len`, `+`, `*`, `in`, `min`, `max`, `for`) y sus métodos más comunes, sabiendo que un método de texto devuelve un texto nuevo.",
        "Crear listas, acceder a sus elementos, modificarlos y operarlas con `+`, `*`, `in`, `len`, `min`, `max` y `sum`.",
        "Modificar listas con sus métodos y distinguir los métodos que cambian la lista (y devuelven `None`) de los que devuelven un valor.",
        "Explicar por qué `=` no copia una lista y cómo hacer una copia.",
        "Usar tuplas y explicar qué significa que sean inmutables.",
        "Usar diccionarios: crearlos, consultar, agregar y eliminar pares clave-valor, recorrerlos y usar sus métodos.",
        "Reconocer los errores frecuentes con estos tipos (`IndexError`, `KeyError`, `ValueError`, `TypeError`, `AttributeError`).",
    ],
)

# ---------------------------------------------------------------- métodos (concepto)
nb.md("""
## Antes de seguir: qué es un método

Los tipos de esta sección traen **operaciones propias** que se escriben con un punto después del valor: `texto.upper()`, `lista.append(5)`, `diccionario.keys()`. Esas operaciones se llaman **métodos**. Un método es como una función, pero pertenece a un tipo de dato y se aplica sobre el valor que está antes del punto.

Hay dos clases de métodos, y conviene distinguirlas desde el principio:

* Los que **devuelven un valor nuevo** sin cambiar el original, como todos los métodos de los textos: `nombre.upper()` devuelve el texto en mayúsculas, pero `nombre` sigue igual.
* Los que **modifican** el valor sobre el que se aplican, como `lista.append(5)`: cambian la lista y devuelven `None`.
""")
nb.python("Los métodos son parte de la **Programación Orientada a Objetos**, que el curso estudia más adelante. Aquí solo se necesita saber usarlos: `valor.metodo(argumentos)`.")

# ---------------------------------------------------------------- strings
nb.md("""
## Strings

Un string es una **secuencia de caracteres**: letras, dígitos, espacios o símbolos. Se usa para guardar un mensaje, una palabra, un nombre, etc. Los strings se escriben encerrando la secuencia de caracteres entre comillas dobles (`"`) o sencillas (`'`).

### Operadores

| Operador | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `s[i]` | Devuelve el carácter de la posición **i** del string **s** | `C = 'Hello world'` | `C[0]` → `'H'`<br>`C[-11]` → `'H'`<br>`C[-3]` → `'r'`<br>`C[8]` → `'r'` |
| `len(s)` | Devuelve la longitud del string **s** | `A = 'Hello world'` | `len(A)` → `11` |
| `s1 + s2` | Devuelve la concatenación de **s1** y **s2** | `B1 = 'Hello'`<br>`B2 = 'nena'` | `B1 + B2` → `'Hellonena'`<br>`B1 + ' ' + B2` → `'Hello nena'` |
| `n * s` | Repite **n** veces el string **s** | `D = "ja"` | `3 * D` → `'jajaja'` |
| `s[inicio:fin]` | Devuelve el segmento de **s** entre las posiciones **inicio** y **fin - 1** | `C = 'Hello world'` | `C[2:7]` → `'llo w'`<br>`C[:5]` → `'Hello'`<br>`C[6:]` → `'world'`<br>`C[-5:-1]` → `'worl'` |
| `e in s` | `True` si **e** aparece en **s** | `frase = 'centella'` | `'a' in frase` → `True`<br>`'va' in 'vaca'` → `True`<br>`'ba' in 'vaca'` → `False` |
| `e not in s` | `True` si **e** no aparece en **s** | `voc = 'aeiou'` | `'i' not in voc` → `False`<br>`'z' not in voc` → `True` |
| `min(s)` | Devuelve el carácter menor de **s** | `frase = 'centella'` | `min(frase)` → `'a'` |
| `max(s)` | Devuelve el carácter mayor de **s** | `frase = 'centella'` | `max(frase)` → `'t'` |
| `for e in s` | Recorre los caracteres de **s**, uno por uno | `for l in 'Antioquia':`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(l)` | `A`, `n`, `t`, `i`, `o`, `q`, `u`, `i`, `a` (uno por línea) |

`min` y `max` comparan los caracteres por su código: para letras minúsculas sin tilde, es el orden alfabético. Las mayúsculas van antes que las minúsculas (`'Z' < 'a'` es `True`).
""")
nb.prediga("Use la tabla para escribir qué imprime cada línea.")
nb.code('''
C = 'Hello world'
print(C[0], C[-11], C[-3], C[8])
print(len(C))
print('Hello' + ' ' + 'nena')
print(3 * "ja")
print(C[2:7], C[:5], C[6:], C[-5:-1])
print('va' in 'vaca', 'ba' in 'vaca', 'z' not in 'aeiou')
print(min('centella'), max('centella'))
''')
nb.md("""
### Métodos

Los métodos de los strings **nunca cambian el string original** (los strings son inmutables): siempre devuelven un valor nuevo. Para conservar el resultado hay que guardarlo, por ejemplo `nombre = nombre.upper()`.

#### Métodos que verifican el contenido de un string

| Método | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `s.isalpha()` | `True` si **s** contiene solo letras | `'Hello'`<br>`'Hello!'` | `'Hello'.isalpha()` → `True`<br>`'Hello!'.isalpha()` → `False` |
| `s.isdigit()` | `True` si **s** contiene solo dígitos | `'124'`<br>`'124A'` | `'124'.isdigit()` → `True`<br>`'124A'.isdigit()` → `False` |
| `s.islower()`<br>`s.isupper()` | `True` si las letras de **s** están todas en minúscula (o todas en mayúscula) | `'hello'`<br>`'Hello'` | `'hello'.islower()` → `True`<br>`'Hello'.isupper()` → `False` |
""")
nb.code('''
print('Hello'.isalpha(), 'Hello!'.isalpha())
print('124'.isdigit(), '124A'.isdigit())
print('hello'.islower(), 'Hello'.isupper())
''')
nb.md("""
> 💡 `isdigit()` sirve para revisar un dato leído con `input()` **antes** de convertirlo con `int()`, y así evitar el `ValueError`. Ojo: `'-5'.isdigit()` y `'3.5'.isdigit()` son `False`, porque el signo y el punto no son dígitos.

#### Métodos que buscan y reemplazan

| Método | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `s.find(w)` | Devuelve la posición de la primera aparición de **w** en **s**, o `-1` si no aparece | `'Hello'`<br>`'Bye!'` | `'Hello'.find('o')` → `4`<br>`'Bye!'.find('o')` → `-1` |
| `s.replace(w, t)` | Devuelve una copia de **s** con todas las apariciones de **w** reemplazadas por **t** | `'Hello'` | `'Hello'.replace('H', 'J')` → `'Jello'`<br>`'Hello'.replace('ll', 'r')` → `'Hero'` |
| `s.lower()`<br>`s.upper()` | Devuelve una copia de **s** en minúsculas (o en mayúsculas) | `'Hello!'` | `'Hello!'.lower()` → `'hello!'`<br>`'Hello!'.upper()` → `'HELLO!'` |
""")
nb.prediga("Después de aplicar los métodos, ¿cuánto vale `s` en la última línea?")
nb.code('''
s = 'Hello'
print(s.find('o'), 'Bye!'.find('o'))
print(s.replace('H', 'J'), s.replace('ll', 'r'))
print(s.lower(), s.upper())
print(s)     # s no cambio: los metodos devolvieron strings nuevos
''')
nb.md("""
#### Métodos que quitan caracteres de los extremos

| Método | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `s.strip(w)` | Devuelve una copia de **s** sin los caracteres de **w** que haya al **inicio y al final**. Sin argumento, quita los espacios y saltos de línea | `'Hello!'`<br>`'Hello\\n'`<br>`'ababcdeababfghba'` | `'Hello!'.strip(' !')` → `'Hello'`<br>`'Hello\\n'.strip('\\n')` → `'Hello'`<br>`'ababcdeababfghba'.strip('ba')` → `'cdeababfgh'` |
| `s.lstrip(w)` | Igual, pero solo al **inicio** (izquierda) | `'Hello! '`<br>`'ababcdeababfghba'` | `'Hello! '.lstrip(' !')` → `'Hello! '`<br>`'ababcdeababfghba'.lstrip('ba')` → `'cdeababfghba'` |
| `s.rstrip(w)` | Igual, pero solo al **final** (derecha) | `'Hello! '`<br>`'ababcdeababfghba'` | `'Hello! '.rstrip(' !')` → `'Hello'`<br>`'ababcdeababfghba'.rstrip('ba')` → `'ababcdeababfgh'` |

Observe que `w` no se trata como una palabra sino como un **conjunto de caracteres**: `strip('ba')` quita todas las `a` y `b` de los extremos, en cualquier orden, hasta encontrar un carácter que no esté en el conjunto. Por eso las `ab` del medio no se tocan.
""")
nb.code('''
print(f"[{'  Hola  '.strip()}]")      # los corchetes muestran que no quedan espacios
print('Hello!'.strip(' !'))
print('ababcdeababfghba'.strip('ba'))
print('ababcdeababfghba'.lstrip('ba'))
print('ababcdeababfghba'.rstrip('ba'))
''')
nb.md("""
#### Métodos para dividir un string

| Método | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `s.split(w)` | Devuelve una **lista** con los pedazos de **s** separados por **w**. Sin argumento, separa por espacios | `'gallo,gato'` | `'gallo,gato'.split(',')` → `['gallo', 'gato']` |

`split` devuelve una lista (se ve en la sección siguiente). Es muy útil para separar varios datos escritos en una sola línea, por ejemplo números separados por comas; cada pedazo sigue siendo un texto y hay que convertirlo para operar.
""")
nb.code('''
print('gallo,gato'.split(','))
print('uno dos   tres'.split())
partes = '3.5,4.0,2.8'.split(',')
print(partes)
print(float(partes[0]) + float(partes[1]))
''')

# ---------------------------------------------------------------- listas
nb.md("""
## Listas

Una lista es una **secuencia ordenada** de elementos, que pueden ser de cualquier tipo. Se escribe con los valores separados por comas y encerrados entre corchetes (`[]`). A diferencia de los strings, las listas **sí se pueden modificar**: se puede cambiar un elemento, agregar o quitar.
""")
nb.convencion("""En los ejercicios del curso, la lista se usa como **arreglo**: de tamaño fijo, creada con `[0.0] * N`, con un solo tipo de dato, recorrida por posición con `range(N)` y sin métodos como `.append()`. Por ejemplo:

```python
N = 4
notas = [0.0] * N
for i in range(N):
    notas[i] = i * 0.5
print(notas)    # [0.0, 0.5, 1.0, 1.5]
```

Este notebook muestra además todo lo que Python permite hacer con las listas.""")
nb.md("""
### Operadores

| Operador | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `L[i]` | Devuelve el elemento de la posición **i** de la lista **L** | `A = [1, 2, 3, 4, -3]` | `A[0]` → `1`<br>`A[-2]` → `4`<br>`A[5]` → `IndexError` |
| `L[i] = v` | Cambia el elemento de la posición **i** por **v** | `A = [1, 2, 3]` | después de `A[0] = 9`, `A` es `[9, 2, 3]` |
| `len(L)` | Devuelve la longitud de **L** | `A = [1, 2, 3, 4, -3]` | `len(A)` → `5` |
| `L1 + L2` | Devuelve una lista nueva con los elementos de **L1** seguidos de los de **L2** | `x = ['a', 'b']`<br>`y = [1, 2, 3]` | `x + y` → `['a', 'b', 1, 2, 3]` |
| `n * L` | Repite **n** veces la lista **L** | `z = [-1, -2, 0]` | `2 * z` → `[-1, -2, 0, -1, -2, 0]` |
| `L[inicio:fin]` | Devuelve una lista nueva con los elementos entre **inicio** y **fin - 1** | `A = [1, 2, 5, 4, -3]` | `A[1:3]` → `[2, 5]`<br>`A[:4]` → `[1, 2, 5, 4]`<br>`A[3:]` → `[4, -3]`<br>`A[:]` → `[1, 2, 5, 4, -3]` |
| `e in L` | `True` si **e** es un elemento de **L** | `A = ['a', 'bc']` | `'bc' in A` → `True`<br>`'b' in A` → `False` |
| `e not in L` | `True` si **e** no es un elemento de **L** | `A = ['a', 'bc']` | `'bc' not in A` → `False`<br>`'b' not in A` → `True` |
| `min(L)`, `max(L)` | Devuelven el menor y el mayor elemento de **L** | `t = [-10, 4, -2, 0]` | `min(t)` → `-10`<br>`max(t)` → `4` |
| `sum(L)` | Devuelve la suma de los elementos (deben ser números) | `t = [-10, 4, -2, 0]` | `sum(t)` → `-8` |
| `for e in L` | Recorre los elementos de **L**, uno por uno | `for num in [1, 2, 3]:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(num)` | `1`, `2`, `3` (uno por línea) |

Observe que `'b' in ['a', 'bc']` es `False`: `in` pregunta si `'b'` es **un elemento** de la lista, no si aparece dentro de algún texto de la lista.
""")
nb.md("""
#### Ejemplos

1. Defina una lista con los siguientes elementos: 20, True, "good", "good".
2. Defina las siguientes listas:
    * `cienciasExatas`: Calculo, Matematicas, Fisica, Estadistica.
    * `cienciasHumanas`: Filosofia, Literatura, Historia, Sociales.
3. Cree una lista `ciencias` con los elementos de `cienciasExatas` y `cienciasHumanas`.
4. Imprima los elementos y segmentos mostrados a continuación:
    * `ciencias[1]`
    * `ciencias[-3]`
    * `ciencias[:8]`
    * `ciencias[1::5]`
    * `ciencias[-1:-7:-1]`
5. Muestre si Matematicas está en `cienciasHumanas`.
6. Muestre si Matematicas no está en `cienciasHumanas`.
7. Dadas las siguientes notas: 2.3, 4.5, 5.0, 1.4, 4.1, 2.2
    * Encuentre la nota más alta.
    * Encuentre la nota más baja.
    * Encuentre la suma y el promedio de las notas.

**Solución**

Como en los otros notebooks de esta carpeta, cuando la última línea de una celda es una expresión (por ejemplo, solo el nombre de una lista), Jupyter muestra su valor sin necesidad de `print`. En Python Tutor o en un archivo `.py`, esa línea no muestra nada.
""")
nb.convencion("La primera lista del ejemplo mezcla tipos (un entero, un booleano y textos): Python lo permite, pero en el curso cada arreglo tiene un solo tipo de dato. Los nombres `cienciasExatas` y `cienciasHumanas` del ejemplo original están en camelCase; en el curso serían `ciencias_exactas` y `ciencias_humanas`.")
nb.code(O(9))
c = Cadena()
c.code(O(10))
c.code(O(11))
nb.prediga("`ciencias` tiene 8 elementos. ¿Qué imprime `ciencias[1::5]`? ¿Y `ciencias[-1:-7:-1]`?")
c.code(O(12))
c.code(O(13))
c.code(O(14))
nb.code(O(15))
nb.error("Una posición mayor o igual que `len(L)` no existe: Python lanza `IndexError: list index out of range`. La lista `A` tiene 5 elementos, así que su última posición es 4.")
nb.code('''
A = [1, 2, 3, 4, -3]
print(A[5])
''')
nb.md("""
### Cómo funciona en Python: modificar una lista y `=` que no copia

A diferencia de un string, a una lista se le puede cambiar un elemento con una asignación por posición.
""")
nb.code('''
notas = [3.0, 4.5, 2.0]
notas[1] = 5.0
print(notas)
''')
nb.md("""
Una variable no "contiene" la lista: **apunta** a ella. Por eso `B = A` no crea una lista nueva, sino un segundo nombre para **la misma** lista (se dice que `B` es un *alias* de `A`). Cualquier cambio hecho a través de `B` se ve también en `A`. Para obtener una **copia** independiente se usa `A[:]` o `list(A)`.
""")
nb.prediga("¿Qué imprime `print(A)` en cada caso?")
nb.code('''
A = [1, 2, 3]
B = A          # B es otro nombre para la misma lista
B[0] = 99
print(A)

A = [1, 2, 3]
C = A[:]       # C es una copia
C[0] = 99
print(A, C)
''')
nb.md("> 💡 Python Tutor es ideal para ver esto: dibuja una flecha desde cada variable hacia la lista, y con `B = A` las dos flechas apuntan a la misma.")

# ---------------------------------------------------------------- métodos de listas
nb.md("""
### Métodos

La tabla muestra, para cada método, lo que **devuelve** y cómo **queda** la lista después de aplicarlo. Los métodos que modifican la lista (`append`, `insert`, `extend`, `remove`, `sort`, `reverse`) devuelven `None`.

| Método | Acción | Ejemplo | Devuelve | La lista queda |
|:--|:--|:--|:--|:--|
| `L.append(e)` | Agrega **e** al final | `L = [1, 2, 3]`<br>`L.append(-5)` | `None` | `[1, 2, 3, -5]` |
| `L.insert(i, e)` | Inserta **e** en la posición **i** | `L = ['a', 'b', 'c']`<br>`L.insert(1, 'x')` | `None` | `['a', 'x', 'b', 'c']` |
| `L.extend(L2)` | Agrega al final **cada uno** de los elementos de **L2** | `M = ['a', 'b']`<br>`M.extend([2, 3])` | `None` | `['a', 'b', 2, 3]` |
| `L.remove(e)` | Borra la primera aparición de **e** (`ValueError` si no está) | `M = ['a', 'b', 'c', 'b']`<br>`M.remove('b')` | `None` | `['a', 'c', 'b']` |
| `L.pop(i)` | Borra el elemento de la posición **i** (sin **i**, el último) | `L = ['a', 'b', 'c']`<br>`L.pop(1)` | `'b'` | `['a', 'c']` |
| `L.count(e)` | Cuenta cuántas veces aparece **e** | `M = ['a', 'b', 'c', 'b']`<br>`M.count('b')` | `2` | sin cambios |
| `L.index(e)` | Devuelve la posición de la primera aparición de **e** (`ValueError` si no está) | `L = ['a', 'b', 'c']`<br>`L.index('b')` | `1` | sin cambios |
| `L.sort()` | Ordena la lista de menor a mayor | `L = [2, 1, 3, 2]`<br>`L.sort()` | `None` | `[1, 2, 2, 3]` |
| `L.reverse()` | Invierte el orden de la lista | `L = [1, 2, 3]`<br>`L.reverse()` | `None` | `[3, 2, 1]` |
""")
nb.python("Los métodos de las listas no se usan en los ejercicios del curso, donde la lista es un arreglo de tamaño fijo (ver el cuadro 📏 del inicio de la sección *Listas*).")
nb.error("Como los métodos que modifican la lista devuelven `None`, escribir `L = L.append(4)` es un error de lógica: la lista sí recibe el 4, pero luego `L` pasa a valer `None` y la lista se pierde. Al intentar usar `L` como lista, Python lanza `AttributeError: 'NoneType' object has no attribute 'append'` (el valor `None` no tiene el método `append`).")
nb.code('''
L = [1, 2, 3]
L = L.append(4)     # error de logica: append devuelve None
print(L)
L.append(5)
''')
nb.md("""
#### Ejemplos

1. Cree una lista `L1` con los elementos: 1, 2, 5, "xxx", 7, 3, -25.
2. Usando `append`, agregue -2.3 al final de la lista.
3. Agregue la lista `['xxx', 'yyy']` al final de la lista.
4. Cuente el número de unos (1) que hay en la lista.
5. Inserte en la posición 1 la lista `[4, 3, 2, 1]`.
6. Sea `L2` otra lista con `["pepe", "pepa", "pipx"]`. Extienda `L1` con `L2`. ¿En qué se diferencia `append` (punto 3) de `extend`?
7. Borre el elemento `['xxx', 'yyy']` de la lista.
8. Averigüe la posición de `"xxx"` y de `[4, 3, 2, 1]`.
9. Borre los dos elementos del punto anterior.
10. Ordene la lista. Si hay un error, interprételo y corríjalo.
11. Invierta el orden de la lista.

#### Solución

Las celdas siguientes modifican la **misma** lista `L1`, una después de otra: ejecútelas en orden.
""")
c = Cadena()
c.code(O(19))
c.code(O(20))
c.code(O(21))
c.code(O(22))
c.code(O(23))
c.code(O(24))
nb.md("""
Compare los puntos 3 y 6: `append(['xxx', 'yyy'])` agregó **un solo elemento**, que es una lista completa (por eso aparece `['xxx', 'yyy']` entre corchetes dentro de `L1`), mientras que `extend(L2)` agregó **cada uno** de los elementos de `L2` por separado.
""")
c.code(O(25))
c.code(O(26))
nb.md("""
En el punto 9 el orden importa: `L1.pop(p1)` borra primero la posición 4 y después `L1.pop(p2)` borra la posición 1. Como la posición 1 está **antes** que la 4, no se corrió al borrar la primera. Si se borrara primero la posición menor, todos los elementos siguientes se correrían una posición hacia la izquierda y `p1` ya no señalaría a `"xxx"`.
""")
c.code(O(27))
nb.error("`sort()` necesita comparar los elementos entre sí, y Python no sabe si un texto es menor o mayor que un número: lanza `TypeError: '<' not supported between instances of 'str' and 'int'` (el operador `<` no funciona entre un `str` y un `int`).")
c.code(O(28), acumular=False)
nb.md("""
La corrección del ejemplo original quita los tres textos antes de ordenar. Observe que la lista que se imprime **ya aparece ordenada**, antes de llamar de nuevo a `sort()`: cuando `sort()` falla en la celda anterior, puede dejar la lista **parcialmente reordenada** (aquí alcanzó a ordenar los números antes de encontrar el primer texto). En Python Tutor, que no ejecuta la celda que falla, esa línea se imprime en el orden original.
""")
c.code(O(29))
c.code(O(30))
nb.md("""
Para consultar más métodos se pueden usar estos comandos:

| Comando | Acción |
|:--|:--|
| `dir(list)` | Lista los nombres de los atributos y métodos de las listas. Los que empiezan y terminan con `__` son de uso interno de Python |
| `help(list)` | Muestra toda la documentación de las listas |
| `help(list.metodo)` | Muestra la documentación de un método, por ejemplo `help(list.extend)` |
""")
nb.code(O(31))
nb.code(O(32))
nb.md("A continuación se muestra la documentación del método **extend**:")
nb.code(O(33))

# ---------------------------------------------------------------- tuplas
nb.md("""
## Tuplas

Las tuplas son como las listas, excepto que **no se pueden modificar** una vez creadas: son **inmutables**. Se escriben encerrando sus elementos entre paréntesis, separados por comas. Como en las listas, los elementos no tienen que ser del mismo tipo.
""")
nb.python("El curso no usa tuplas en sus ejercicios. Aparecen en Python más de lo que parece: por ejemplo, `x, y = 3, 4` y el `*args` de una función usan tuplas.")
nb.md("""
### Operadores

Son los mismos de las listas, salvo los que modifican:

| Operador | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `T[i]` | Devuelve el elemento de la posición **i** de la tupla **T** | `T = (1, 2, 3, 4, -3)` | `T[0]` → `1`<br>`T[-3]` → `3`<br>`T[-2]` → `4` |
| `len(T)` | Devuelve la longitud de **T** | `A = (1, 2, 3, 'oso')`<br>`B = ([1, 2], 3)`<br>`C = ()` | `len(A)` → `4`<br>`len(B)` → `2`<br>`len(C)` → `0` |
| `T1 + T2` | Devuelve una tupla nueva con los elementos de **T1** seguidos de los de **T2** | `x = ('a', 'b')`<br>`y = (1, 2, 3)` | `x + y` → `('a', 'b', 1, 2, 3)` |
| `n * T` | Repite **n** veces la tupla **T** | `z = (-1, -2, 0)` | `2 * z` → `(-1, -2, 0, -1, -2, 0)` |
| `T[inicio:fin]` | Devuelve una tupla nueva con los elementos entre **inicio** y **fin - 1** | `A = (1, 2, 5, 4, -3)` | `A[1:3]` → `(2, 5)`<br>`A[:4]` → `(1, 2, 5, 4)`<br>`A[3:]` → `(4, -3)` |
| `e in T`<br>`e not in T` | `True` si **e** es (o no es) un elemento de **T** | `A = ('a', 'bc')` | `'bc' in A` → `True`<br>`'b' not in A` → `True` |
| `min(T)`, `max(T)` | Devuelven el menor y el mayor elemento de **T** | `t = (-10, 4, -2, 0)` | `min(t)` → `-10`<br>`max(t)` → `4` |
| `for e in T` | Recorre los elementos de **T** | `for num in (1, 2, 3):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(num)` | `1`, `2`, `3` (uno por línea) |

#### Ejemplos

1. Declare una tupla `T1` con 2, 3, 4 y 5 como elementos.
2. Determine el tamaño de la tupla anterior.
3. Cree una tupla `T2` con `'a'` y `'b'` como elementos.
4. Repita la tupla anterior 3 veces y guarde el resultado en otra tupla `T3`.
5. Cree otra tupla `T4` a partir de todas las tuplas creadas antes.
6. Mire si 4 está en la tupla `T4`.
7. Mire si 4 no está en la tupla `T4`.
8. ¿Cuál es el elemento mínimo de `T1`? ¿Por qué no se puede sacar el elemento mínimo de `T4`?
9. Declare una tupla `T5` que tenga como elementos: morfeo, neo, trinity.
10. ¿Cuál es el elemento máximo de la tupla anterior?
11. Recorra con un ciclo la tupla `T5`.

**Solución**:
""")
c = Cadena()
for i in range(38, 46):
    c.code(O(i))
nb.error("Para responder la segunda pregunta del punto 8: `T4` mezcla números y textos, y para hallar el mínimo hay que compararlos entre sí. Igual que con `sort()`, Python lanza `TypeError`.")
c.code('''
min(T4)
''', acumular=False)
c.code(O(46))
c.code(O(47).replace("Cual es elemento minimo", "Cual es elemento maximo"))
c.code(O(48))
nb.md("""
### Cómo funciona en Python: qué significa que una tupla sea inmutable

Una tupla no permite cambiar, agregar ni quitar elementos.
""")
nb.error("Asignar a una posición de una tupla da `TypeError: 'tuple' object does not support item assignment` (la tupla no admite asignar elementos).")
nb.code('''
T = (2, 3, 4, 5)
T[0] = 10
''')
nb.error("Las tuplas no tienen métodos para agregar ni quitar: `T.append(6)` da `AttributeError: 'tuple' object has no attribute 'append'`.")
nb.code('''
T = (2, 3, 4, 5)
T.append(6)
''')
nb.md("""
Dos detalles de la sintaxis de las tuplas:

* Lo que crea la tupla es la **coma**, no los paréntesis: `t = 1, 2, 3` también es una tupla. Por eso una tupla de **un solo elemento** necesita una coma: `(5,)` es una tupla, pero `(5)` es solo el número 5 entre paréntesis.
* Si una tupla contiene una lista, la tupla no puede cambiar **cuál** lista contiene, pero esa lista sí se puede modificar por dentro.
""")
nb.prediga("¿Qué tipo tiene cada valor? ¿Cómo queda `T` al final?")
nb.code('''
print(type((5,)), type((5)))
t = 1, 2, 3
print(t)

T = (1, 2, [3, 4], 6)
T[2][0] = 30       # se modifica la lista que esta dentro de la tupla
print(T)
''')
nb.md("""
### Métodos

| Método | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `T.count(e)` | Cuenta cuántas veces aparece **e** en la tupla | `M = ('a', 'b', 'c', 'b')` | `M.count('b')` → `2` |
| `T.index(e)` | Devuelve la posición de la primera aparición de **e** (`ValueError` si no está) | `L = ('a', 'b', 'c', 'd')` | `L.index('b')` → `1` |

#### Ejemplos

1. Declare la tupla `T = (1, 2, [3, 4], 6)`.
2. Encuentre el índice de 4.
3. Encuentre el índice de `[3, 4]`.
4. Cuente el número de veces que aparece el -1 en la tupla.

**Solución**:
""")
c = Cadena()
c.code(O(52))
nb.error("El 4 no es un elemento de `T`: está **dentro** de la lista `[3, 4]`, que es el elemento de la posición 2. Por eso `T.index(4)` no lo encuentra y Python lanza `ValueError: tuple.index(x): x not in tuple`.")
c.code(O(53), acumular=False)
c.code(O(54))
c.code(O(55).replace("en la lista", "en la tupla"))

# ---------------------------------------------------------------- diccionarios
nb.md("""
## Diccionarios

Un diccionario guarda **pares clave: valor**. En lugar de buscar un elemento por su posición, como en las listas, se busca por su **clave** (en inglés, *key*), que suele ser un texto o un número. Al dato asociado a cada clave se le llama **valor** (*value*).

La sintaxis es `{clave1: valor1, clave2: valor2, ..., claveN: valorN}`, y `{}` es un diccionario vacío.

* Las claves no se repiten: asignar a una clave que ya existe reemplaza su valor.
* Las claves deben ser valores que no cambian, como textos, números o tuplas; una lista no puede ser clave.
* Los pares se guardan en el **orden en que se agregaron**.
""")
nb.python("El curso no usa diccionarios en sus ejercicios. Son una de las estructuras más usadas en Python, por ejemplo para representar un registro con varios campos.")
nb.md("""
### Operadores

| Operador | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `len(d)` | Devuelve el número de pares de **d** | `A = {'a': 1, 'b': 2, 'c': 3}`<br>`B = {'ab': 1, 'b': [2, 3]}`<br>`C = {}` | `len(A)` → `3`<br>`len(B)` → `2`<br>`len(C)` → `0` |
| `k in d`<br>`k not in d` | `True` si **k** es (o no es) una **clave** de **d** | `A = {'a': 1, 'b': 2, 'c': 3}` | `'a' in A` → `True`<br>`'d' not in A` → `True`<br>`1 in A` → `False` (1 es un valor, no una clave) |
| `d1 == d2`<br>`d1 != d2` | Compara si los dos diccionarios tienen los mismos pares (el orden no importa) | `d1 = {"red": 41, "blue": 3}`<br>`d2 = {"blue": 3, "red": 41}` | `d1 == d2` → `True`<br>`d1 != d2` → `False` |
| `d[k]` | Devuelve el valor asociado a la clave **k** (`KeyError` si no existe) | `d1 = {"red": 41, "blue": 3}` | `d1["red"]` → `41`<br>`d1["r"]` → `KeyError` |
| `d[k] = v` | Asocia la clave **k** con el valor **v**: si **k** ya existe, reemplaza su valor; si no, agrega el par | `d1 = {"A": 1, "B": 2}` | después de `d1["A"] = -1`: `{'A': -1, 'B': 2}`<br>después de `d1["C"] = 5`: `{'A': -1, 'B': 2, 'C': 5}` |
| `del d[k]` | Elimina el par con clave **k** | `vocales = {1: 'a', 2: 'e', 3: 'z'}`<br>`del vocales[3]` | `vocales` queda `{1: 'a', 2: 'e'}` |
| `for k in d` | Recorre las **claves** de **d** | `meses = {'enero': 31, 'febrero': 28}`<br>`for m in meses:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(m, meses[m])` | `enero 31`<br>`febrero 28` |

#### Ejemplo

1. Cree un diccionario llamado `cursos` a partir de la siguiente tabla:

| Código | Materia |
|------|-------|
| '001' | 'Matematicas' |
| '002' | 'Español' |
| '003' | 'Filosofia' |
| '004' | 'Quimica' |
| '005' | 'Fisica' |
| '006' | 'Sociales' |

2. Determine si el curso de **Etica y valores**, cuyo código es **007**, está en el diccionario anterior.
3. Determine si el curso de Matematicas (código **001**) se encuentra en el diccionario.
4. Devuelva la materia cuyo código es **005**.
5. Agregue la materia **Etica y valores** a los cursos.
6. Recorriendo el diccionario, imprima los códigos y las materias asociadas a ellos.
""")
c = Cadena()
c.code(O(59))
c.code(O(60))
c.code(O(61))
c.code(O(62).replace("duyo", "cuyo"))
nb.error("Pedir una clave que no existe da `KeyError`, con la clave que faltó. Antes de pedirla, se puede preguntar con `in` si existe (como en los puntos 2 y 3).")
c.code('''
cursos['008']
''', acumular=False)
c.code("# Punto 5: Agregar la materia Etica y valores a los cursos.\n" + O(63))
c.code("# Punto 6: Recorrer el diccionario e imprimir codigos y materias.\n" + O(64))
nb.md("""
### Métodos

| Método | Acción | Ejemplo | Resultado |
|:--|:--|:--|:--|
| `d.keys()` | Devuelve las claves de **d** | `A = {'a': 1, 'b': 2, 'c': 3}` | `A.keys()` → `dict_keys(['a', 'b', 'c'])` |
| `d.values()` | Devuelve los valores de **d** | `A = {'a': 1, 'b': 2, 'c': 3}` | `A.values()` → `dict_values([1, 2, 3])` |
| `d.items()` | Devuelve los pares, cada uno como una tupla `(clave, valor)` | `A = {'a': 1, 'b': 2, 'c': 3}` | `A.items()` → `dict_items([('a', 1), ('b', 2), ('c', 3)])` |
| `d.get(k, e)` | Devuelve `d[k]` si **k** es clave de **d**; si no, devuelve **e** (si no se pasa **e**, devuelve `None`). Nunca da `KeyError` | `A = {'a': 1, 'b': 2, 'c': 3}` | `A.get('c', 4)` → `3`<br>`A.get('f', 4)` → `4`<br>`A.get('d')` → `None` |
| `d.pop(k)` | Elimina el par con clave **k** y devuelve su valor | `A = {'a': 1, 'b': 2, 'c': 3}`<br>`A.pop('b')` | devuelve `2`; `A` queda `{'a': 1, 'c': 3}` |
| `d.popitem()` | Elimina el **último** par agregado y lo devuelve como tupla | `A = {'a': 1, 'b': 2, 'c': 3}`<br>`A.popitem()` | devuelve `('c', 3)`; `A` queda `{'a': 1, 'b': 2}` |
| `d.clear()` | Borra todos los pares; **d** queda vacío. Devuelve `None` | `A = {'a': 1, 'b': 2}`<br>`A.clear()` | `A` queda `{}` |
| `d.update(d2)` | Agrega a **d** los pares de **d2** (si una clave ya existe, reemplaza su valor). Devuelve `None` | `A = {'a': 1, 'b': 2}`<br>`B = {'xyz': 1, 'm': [2, 3]}`<br>`A.update(B)` | `A` queda `{'a': 1, 'b': 2, 'xyz': 1, 'm': [2, 3]}`; `B` no cambia |

`keys()`, `values()` e `items()` devuelven unas *vistas* del diccionario: se pueden recorrer con `for` y preguntar con `in`, pero no se puede acceder a ellas por posición. Si se necesita una lista, se convierten con `list()`, por ejemplo `list(A.keys())`.

#### Ejemplo

1. Cree el diccionario `cursos` a partir de la tabla del ejemplo anterior.
2. Obtenga los códigos de los cursos registrados.
3. Obtenga los nombres de las materias registradas.
4. Obtenga cada uno de los pares (código, materia) registrados.
5. Determine el curso (**Etica y valores**) cuyo código es **007**.
6. Elimine el curso de **Sociales**.
7. Elimine el último curso agregado al diccionario.
8. Borre todas las materias de `cursos`.
9. Agregue a lo que quedó el curso de **Etica y valores**.
""")
c = Cadena()
c.code(O(67))
c.code(O(68))
c.code(O(69))
c.code(O(70))
c.code(O(71).replace("# Punto 5: Determinar el curso (Etica y valores) cuyo codigo es 007.",
                     "# Punto 5: Determinar el curso (Etica y valores) cuyo codigo es 007.\n"
                     "# get devuelve None porque la clave '007' no existe"))
c.code("# Punto 6: Eliminar el curso de Sociales.\n" + O(72))
c.code("# Punto 7: Eliminar el ultimo curso agregado.\n" + O(73))
c.code("# Punto 8: Borrar todas las materias.\n" + O(74))
c.code("# Punto 9: Agregar el curso de Etica y valores.\n" + O(75))

# ---------------------------------------------------------------- errores
nb.resumen_errores([
    ("`IndexError`", "La posición no existe en la lista o el texto",
     "`A[5]` cuando `A` tiene 5 elementos (posiciones 0 a 4)",
     "Recordar que la última posición es `len(A) - 1`"),
    ("`KeyError`", "La clave no existe en el diccionario",
     "`cursos['008']` cuando no hay curso con ese código",
     "Preguntar antes con `in`, o usar `.get(clave)`"),
    ("`ValueError`", "El valor no está en la lista o la tupla",
     "`T.index(4)` cuando el 4 está dentro de otra lista; `L.remove(e)` con un `e` que no está",
     "Preguntar antes con `in`"),
    ("`TypeError`", "La operación no es válida para esos tipos",
     "`sort()` o `min()` con números y textos mezclados; asignar a una posición de una tupla",
     "Usar elementos de un solo tipo; usar una lista si hay que modificar"),
    ("`AttributeError`", "El valor no tiene ese método",
     "`L = L.append(4)` y después `L.append(5)` (`L` quedó en `None`); `T.append(6)` con una tupla",
     "No asignar el resultado de un método que modifica; usar una lista si hay que agregar"),
])

# ---------------------------------------------------------------- ejercicios
nb.ejercicios([
    '''
s = "Medellin"
print(s[0], s[-1], len(s), s[2:5])
''',
    '''
palabra = "hola"
print(palabra.upper())
print(palabra)
''',
    '''
L = [3, 1, 2]
L.append(5)
print(L, len(L))
''',
    '''
A = [1, 2, 3]
B = A
B[0] = 10
print(A)
''',
    '''
A = [1, 2, 3]
B = A[:]
B[0] = 10
print(A, B)
''',
    '''
t = (4, 5, 6)
print(t[1] + t[-1], 5 in t)
''',
    '''
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 0
print(d, len(d))
''',
    '''
L = [5, 2, 8]
r = L.sort()
print(r, L)
''',
])

# ---------------------------------------------------------------- recursos
nb.recursos("""
### Herramientas

* [Python Tutor](https://pythontutor.com/): visualiza la ejecución paso a paso. Dibuja cada lista, tupla y diccionario con flechas desde las variables, lo que ayuda mucho a entender los alias (`B = A`).
* [PEP 8](https://peps.python.org/pep-0008/): guía oficial de estilo de Python.

### Referencias

* CS50's Introduction to Programming with Python, [Lecture 2: Loops](https://cs50.harvard.edu/python/notes/2/) (listas y diccionarios).
* El Libro de Python: [cadenas](https://ellibrodepython.com/cadenas-python), [listas](https://ellibrodepython.com/listas-en-python), [tuplas](https://ellibrodepython.com/tuplas-python) y [diccionarios](https://ellibrodepython.com/diccionarios-en-python).
* Tutorial oficial de Python (en español): [estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html) y [métodos de los strings](https://docs.python.org/es/3/library/stdtypes.html#string-methods).
""")

nb.escribir(RAIZ / RUTA)
