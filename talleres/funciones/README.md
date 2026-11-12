![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Taller 3 — Funciones

Este taller sirve de repaso del tema de **funciones**: definición e invocación, los cuatro casos según parámetros y retorno, pruebas con `assert` (clase 9), especificación con *Supone*/*Garantiza*, ámbito de las variables, formas de pasar argumentos, funciones integradas, los módulos `math` y `random`, y programas en varios archivos (clase 10).

## Cómo trabajar cada problema

En los problemas de la sección 4, siga los pasos del ejemplo de áreas de la clase 9 y del laboratorio 4:

1. **Entender:** identifique entradas, salidas y proceso. Decida qué hace la **función** y qué hace el **programa principal**: la función calcula; el programa principal lee los datos, llama a la función y muestra el resultado.
2. **Especificar:** escriba la cabecera de la función y su *docstring* con **Supone** (qué debe cumplir lo que recibe) y **Garantiza** (qué devuelve o qué hace). Diga de qué **caso** es (ver el [anexo A.2](#a2-los-cuatro-casos)).
3. **Probar antes de integrar:** convierta la tabla de casos de prueba en instrucciones `assert`. Agregue casos propios: uno **típico**, uno **límite** y, si aplica, uno **especial**.
4. **Implementar y verificar:** escriba el cuerpo de la función hasta que pasen todas las pruebas, y solo entonces escriba el programa principal.

Si lo resuelve en el computador, organice cada problema en tres archivos, como en el [laboratorio 4](../../laboratorios/4/README.md): un módulo solo con funciones, un archivo `test_<módulo>.py` con los `assert` y un `main.py` con `def main()` y la guarda `if __name__ == "__main__":` (ver el [anexo A.9](#a9-un-programa-en-varios-archivos)).

---

## 1. Preguntas de repaso

Responda con sus palabras y, cuando pueda, con un ejemplo de código.

**1.1** ¿Cuáles son los beneficios de usar funciones?

**1.2** ¿Cómo se define una función? ¿Cómo se invoca? ¿Qué pasa si se define una función pero nunca se invoca?

**1.3** Defina los términos **cabecera**, **parámetro** y **argumento** de una función. Señálelos en este código:

```python
def calcular_area_rectangulo(base, altura):
    return base * altura

area = calcular_area_rectangulo(4, 3)
```

**1.4** ¿Una función puede invocar a otra? Dé un ejemplo de los vistos en clase.

**1.5** ¿Puede un argumento tener el mismo nombre que su parámetro? Si son iguales, ¿son la misma variable?

**1.6** ¿Qué diferencia hay entre una función que **retorna** un valor y una que lo **imprime**? ¿Cuál de las dos se puede probar con `assert`? ¿Por qué?

**1.7** ¿Para qué sirven el **Supone** y el **Garantiza** de la especificación? ¿Quién debe cumplir cada parte: quien escribe la función o quien la invoca?

---

## 2. Prueba de escritorio

Realice la prueba de escritorio de cada código **a mano, sin la ayuda del computador**. Además de la tabla de variables, señale **en qué función** vive cada variable: una variable de `main()` y un parámetro con el mismo nombre son variables distintas. Al terminar, puede comprobar su resultado ejecutando el código o simulándolo en [Python Tutor](https://pythontutor.com/), que muestra cada función en su propio cuadro.

### 2.1 Ámbito: variables locales y globales

**Código 1.** Variables: `x` y `y` del programa principal; `x` y `y` de `funcion`.

```python
def funcion(x):
    print(x)
    x = 4.5
    y = 3.4
    print(y)

x = 2
y = 4
funcion(x)
print(x)
print(y)
```

> **Pregunta para pensar:** dentro de `funcion` se asigna `x = 4.5` y `y = 3.4`. ¿Por qué los dos últimos `print` no muestran esos valores? (Compare con el ejemplo 1 de la [sesión 25](../../clases/10/sesion_magistral-25/README.md)).

**Código 2.** Variables: `mayor` de `main()`; `valor1`, `valor2` y `mayor` de `obtener_mayor`.

```python
def main():
    mayor = 0
    obtener_mayor(1, 2, mayor)
    print(mayor)

def obtener_mayor(valor1, valor2, mayor):
    if valor1 > valor2:
        mayor = valor1
    else:
        mayor = valor2

main()
```

> **Pregunta para pensar:** quien escribió este código quería que se imprimiera `2`. ¿Por qué no ocurre? Corríjalo **sin** usar variables globales: ¿qué le falta a `obtener_mayor` y qué debe cambiar en `main()`?

**Código 3.** Variables: `veces` de `main()`; `mensaje` y `n` de `imprimir_n_veces`.

```python
def main():
    veces = 3
    print("Antes de la llamada, veces vale", veces)
    imprimir_n_veces("¡Bienvenido!", veces)
    print("Después de la llamada, veces vale", veces)

def imprimir_n_veces(mensaje, n):
    while n > 0:
        print("n =", n)
        print(mensaje)
        n -= 1

main()
```

> **Pregunta para pensar:** el parámetro `n` llega a `0` dentro de la función. ¿Cuánto vale `veces` después de la llamada? ¿Por qué?

### 2.2 Funciones que retornan un valor

**Código 4.** Variables: `i` de `main()`; `i`, `num`, `linea` y `j` de `construir_linea`. Recuerde que `str(2)` convierte el número `2` en el texto `"2"`, y que `+` entre textos los une.

```python
def main():
    i = 1
    while i <= 6:
        print(construir_linea(i, 2))
        i += 1

def construir_linea(i, num):
    linea = ""
    for j in range(1, i):
        linea += str(num) + " "
        num *= 2
    return linea

main()
```

> **Pregunta para pensar:** ¿qué imprime la primera vuelta, cuando `i = 1`? ¿Cuántas veces se repite el `for` en esa llamada?

**Código 5.** `print` sin `return`. Variables: `n1`, `n2` y `menor` de `min`.

```python
def main():
    print(min(5, 6))

def min(n1, n2):
    menor = n1
    if n2 < menor:
        menor = n2

main()
```

> **Pregunta para pensar:** ¿qué le falta a la función para que el programa imprima `5`? Además, `min` ya es el nombre de una función integrada de Python (sesión 27). ¿Qué pasa con la `min` de Python cuando se define una función propia con ese nombre? Proponga un nombre mejor.

**Código 6.** Una función puede usar `return` sin ningún valor. ¿Tiene errores la función `sumar_e_imprimir`? Si los tiene, corríjalos. Luego haga la prueba de escritorio de todo el código.

```python
def sumar_e_imprimir(x, y):
    print(x + y)
    return

resultado = sumar_e_imprimir(2, 3)
print(resultado)
```

### 2.3 Formas de pasar argumentos

**Código 7.** Parámetros con valor por defecto. Para cada llamada, escriba qué valor recibe cada parámetro y si lo recibe por posición, por nombre o por defecto.

```python
def f(x, y=1, z=2):
    return x + y + z

print(f(1, 1, 1))
print(f(y=1, x=2, z=3))
print(f(1, z=3))
```

**Código 8.** Variables: `ancho` y `alto` de `mostrar`, en cada llamada.

```python
def mostrar(ancho=1, alto=2):
    print(ancho, alto)

mostrar()
mostrar(ancho=5)
mostrar(alto=24)
mostrar(4, 5)
```

> **Pregunta para pensar:** ¿cómo se invoca `mostrar` para cambiar solo el `alto` sin escribir su nombre? ¿Se puede?

---

## 3. Encontrar y corregir errores

**3.1** Identifique y corrija los errores del siguiente programa. Para cada error, diga si Python lo detecta **antes** de ejecutar (error de sintaxis o de sangría) o si es un error de **lógica** (el programa corre, pero no hace nada útil).

```python
def funcion1(n, m):
funcion2(3.4)

def funcion2(n):
    if n > 0:
        return 1
  elif n == 0:
        return 0
  elif n < 0:
        return -1

funcion1(2, 3)
```

> [!Tip]
> **Pista:** hay dos errores de sangría. Cuando los corrija, el programa corre sin errores... y no muestra nada. ¿Qué pasa con el valor que retorna `funcion2`? ¿Para qué recibe `funcion1` los parámetros `n` y `m`?

**3.2** Suponga que la cabecera de una función es:

```python
def f(p1, p2, p3, p4):
```

¿Cuáles de las siguientes llamadas son correctas? Para las correctas, diga qué valor recibe cada parámetro; para las incorrectas, explique por qué.

* a. `f(1, p2=3, p3=4, p4=4)`
* b. `f(1, p2=3, 4, p4=4)`
* c. `f(p1=1, p2=3, 4, p4=4)`
* d. `f(p1=1, p2=3, p3=4, p4=4)`
* e. `f(p4=1, p2=3, p3=4, p1=4)`

**3.3** Haga la prueba de escritorio del siguiente programa. Variables: `i` de `main()`; `i` y `linea` de `funcion1`.

```python
def main():
    i = 0
    while i <= 4:
        funcion1(i)
        i += 1
        print("i vale", i)

def funcion1(i):
    linea = " "
    while i >= 1:
        if i % 3 != 0:
            linea += str(i) + " "
            i -= 1
    print(linea)

main()
```

> **Pregunta para pensar:** ¿qué ocurre en la llamada `funcion1(3)`? ¿Cuál es la variable de control del ciclo de `funcion1` y en qué caso deja de actualizarse? Corrija el programa cambiando **una sola línea** de sitio, de modo que cada línea muestre los números de `i` a `1` que no son múltiplos de 3. (Compare con el caso 4 de la [sesión 13](../../clases/7/sesion_magistral-13/README.md)).

---

## 4. Problemas de programación

En cada problema, la tabla de casos de prueba se refiere a la **función**. El programa principal se prueba ejecutándolo.

**4.1 Números pentagonales.** Un número pentagonal se define como $\frac{n(3n - 1)}{2}$ para $n = 1, 2, 3, \ldots$ De manera que los primeros números pentagonales son 1, 5, 12, 22, ... Escriba una función con la siguiente cabecera, que **retorne** el número pentagonal `n`:

```python
def calcular_pentagonal(n):
```

Luego escriba un programa principal que use la función para mostrar los primeros 100 números pentagonales, **10 números por línea**.

| `n` | `calcular_pentagonal(n)` |
|---|---|
| 1 | 1 |
| 4 | 22 |
| 10 | 145 |
| 100 | 14950 |

> [!Tip]
> **Pista:** $n(3n - 1)$ siempre es par, así que se puede dividir con `//` y el resultado es un entero. Para mostrar varios números en la misma línea use `print(..., end=" ")`; para saltar de línea después de cada décimo número, piense en el residuo `%`.

**4.2 Suma de los dígitos.** Escriba una función que calcule la suma de los dígitos de un número entero, con la siguiente cabecera:

```python
def sumar_digitos(n):
```

Por ejemplo, `sumar_digitos(234)` retorna `9` (2 + 3 + 4). Escriba un programa principal que le pida al usuario un entero y muestre la suma de sus dígitos usando esta función.

| `n` | `sumar_digitos(n)` |
|---|---|
| 234 | 9 |
| 7 | 7 |
| 1000 | 1 |
| 9999 | 36 |
| 0 | 0 |

> [!Tip]
> **Pista:** use el operador `%` para extraer el último dígito y el operador `//` para quitarlo. Por ejemplo, para extraer el 4 de 234 se usa `234 % 10` (= 4), y para quitarlo, `234 // 10` (= 23). Repita con un ciclo hasta que no queden dígitos.

> **Pregunta para pensar:** ¿qué retorna su función con `n = -234`? ¿Qué debería decir el **Supone** de la especificación?

**4.3 Número al revés y palíndromos.** Este problema tiene dos partes, para comparar una función que **imprime** con una que **retorna**. Si resolvió el [problema 1 del laboratorio 3](../../laboratorios/3/README.md#1-número-invertido-con-ciclo), ya tiene el ciclo: ahora se trata de ponerlo dentro de una función.

**a.** Escriba una función que **muestre** un entero al revés:

```python
def mostrar_invertido(numero):
```

Por ejemplo, `mostrar_invertido(3456)` muestra `6543`. Escriba un programa principal que pida un entero y lo muestre al revés.

**b.** Escriba las siguientes dos funciones. Use `invertir` para implementar `es_palindromo`: un número es palíndromo si al revés es igual a sí mismo.

```python
def invertir(numero):
    """Retorna el número al revés; por ejemplo, invertir(456) retorna 654."""

def es_palindromo(numero):
    """Retorna True si el número es palíndromo y False si no lo es."""
```

Complete la especificación de cada una (Supone y Garantiza) y escriba un programa principal que pida un entero e informe si es palíndromo.

| `numero` | `invertir(numero)` | `es_palindromo(numero)` |
|---|---|---|
| 456 | 654 | `False` |
| 121 | 121 | `True` |
| 1221 | 1221 | `True` |
| 7 | 7 | `True` |
| 10 | 1 | `False` |

> **Pregunta para pensar:** ¿qué muestra `mostrar_invertido(1200)` y qué retorna `invertir(1200)`? ¿Por qué son distintos? ¿Cuál de las dos funciones de la parte a o b se puede probar con `assert`, y cuál se puede reutilizar dentro de otra función?

**4.4 Patrón de números.** Escriba una función que muestre un patrón como el siguiente, con los números alineados a la derecha:

```text
      1
    2 1
  3 2 1
4 3 2 1
```

La cabecera de la función es:

```python
def mostrar_patron(n):
```

El ejemplo es para `n = 4`: la última línea tiene los números de `n` a `1`. Escriba un programa principal que pida un número `n` y llame a `mostrar_patron(n)`. Suponga que `1 <= n <= 9`, para que cada número ocupe un solo carácter.

> [!Tip]
> **Pista:** es un problema de ciclos anidados, como la pirámide de la [sesión 21](../../clases/8/sesion_magistral-21/README.md). En la fila `i` hay que escribir primero los espacios y luego los números de `i` a `1`. ¿Cuántos espacios lleva la fila `i`? (Cada número ocupa dos caracteres: el dígito y un espacio).

> **Pregunta para pensar:** ¿de qué caso es esta función (ver el [anexo A.2](#a2-los-cuatro-casos))? ¿Cómo se prueba, si no se puede usar `assert`?

**4.5 Ordenar tres números.** Escriba una función que **muestre** tres números en orden creciente:

```python
def mostrar_ordenados(num1, num2, num3):
```

Escriba un programa principal que pida los tres números (uno por uno) y llame a la función.

| Números leídos | Salida |
|---|---|
| 3, 2.4, 5 | `Los números ordenados son 2.4 3.0 5.0` |
| 31, 12.4, 15 | `Los números ordenados son 12.4 15.0 31.0` |
| 2, 2, 1 | `Los números ordenados son 1.0 2.0 2.0` |

> [!Tip]
> **Pista:** se puede resolver con condicionales o con las funciones integradas `min()` y `max()` de la [sesión 27](../../clases/10/sesion_magistral-27/README.md). Si ya sabe cuál es el menor y cuál el mayor, ¿cómo se obtiene el del medio con una sola operación aritmética?

**4.6 Tablas de conversión de temperatura.** Escriba un módulo que contenga las dos funciones siguientes:

```python
def celsius_a_fahrenheit(temp_c):
    """Convierte de grados Celsius a grados Fahrenheit."""

def fahrenheit_a_celsius(temp_f):
    """Convierte de grados Fahrenheit a grados Celsius."""
```

Las fórmulas de conversión son:

$$
C = \frac{5}{9}(F - 32) \qquad F = \frac{9}{5}C + 32
$$

Escriba un programa principal que invoque estas funciones para mostrar las dos tablas siguientes, una al lado de la otra (no importa la alineación exacta de las columnas):

```text
Celsius   Fahrenheit   |   Fahrenheit   Celsius
40.0      104.0        |   120.0        48.89
39.0      102.2        |   110.0        43.33
...
32.0      89.6         |   40.0         4.44
31.0      87.8         |   30.0         -1.11
```

| Función | Argumento | Resultado (redondeado) |
|---|---|---|
| `celsius_a_fahrenheit` | 40 | 104.0 |
| `celsius_a_fahrenheit` | 37 | 98.6 |
| `fahrenheit_a_celsius` | 120 | 48.89 |
| `fahrenheit_a_celsius` | 30 | -1.11 |
| `fahrenheit_a_celsius` | 32 | 0.0 |

> [!Tip]
> **Pista:** `celsius_a_fahrenheit(37)` no da exactamente `98.6`. Compare los decimales con `round(resultado, 2) == esperado`, como en la clase 9. Es el mismo programa de temperaturas de las sesiones 24 a 26: puede partir del módulo `conversion.py` del [paso 4 de la sesión 26](../../clases/10/sesion_magistral-26/README.md) y agregarle la función que falta.

**4.7 Contar números primos.** Escriba una función `es_primo(num)` que retorne `True` si `num` es primo y `False` si no lo es. Luego úsela en un programa principal para encontrar **cuántos** números primos hay menores que 10 000.

| `num` | `es_primo(num)` |
|---|---|
| 2 | `True` |
| 9 | `False` |
| 13 | `True` |
| 1 | `False` |
| 0 | `False` |

Resultado esperado: hay `4` primos menores que 10, `25` menores que 100 y `1229` menores que 10 000.

> [!Tip]
> **Pista:** un número primo es un entero mayor que 1 que solo es divisible por 1 y por sí mismo; por eso 1 **no** es primo. La primalidad se trabajó en la [sesión 19](../../clases/8/sesion_magistral-19/README.md) (sin funciones) y en el ejercicio `es_primo` del [notebook de la clase 9](../../clases/9/teoria/notebooks/funciones.ipynb). ¿Conviene que el conteo esté dentro de `es_primo` o en el programa principal?

**4.8 Suma de una serie.** Escriba una función que retorne la suma de la siguiente serie para un valor de `i`:

$$
m(i) = \frac{1}{2} + \frac{2}{3} + \frac{3}{4} + \cdots + \frac{i}{i + 1}
$$

Escriba un programa principal que muestre una tabla con los valores de `i` de 1 a 20 y el valor de $m(i)$ con cuatro decimales:

```text
i     m(i)
1     0.5000
2     1.1667
...
19    16.4023
20    17.3546
```

| `i` | $m(i)$ (cuatro decimales) |
|---|---|
| 1 | 0.5000 |
| 2 | 1.1667 |
| 3 | 1.9167 |
| 20 | 17.3546 |

> **Pregunta para pensar:** el programa principal llama a la función 20 veces y cada llamada vuelve a sumar desde el primer término. ¿Se podría hacer la tabla sin la función, con un solo acumulador? ¿Qué se gana y qué se pierde?

**4.9 Cuadrícula de ceros y unos.** Escriba una función que muestre una cuadrícula de `n` filas por `n` columnas, en la que cada posición es un `0` o un `1` generado al azar:

```python
def mostrar_cuadricula(n):
```

Escriba un programa principal que pida `n` y muestre la cuadrícula. Una ejecución con `n = 3` podría verse así:

```text
Ingrese n: 3
011
001
110
```

> [!Tip]
> **Pista:** use `random.randint(0, 1)` (sesión 27) dentro de dos ciclos anidados. La función no necesita guardar los números: solo los muestra.

> **Pregunta para pensar:** cada ejecución muestra una cuadrícula distinta. ¿Cómo haría para que dos ejecuciones muestren **la misma** cuadrícula mientras busca un error? (Pista: la semilla). ¿Por qué esa instrucción no debe quedar en el programa final?

**4.10 Milisegundos a horas, minutos y segundos.** Escriba una función que convierta una cantidad de milisegundos a horas, minutos y segundos, y **retorne** el resultado como un texto con el formato `horas:minutos:segundos`:

```python
def convertir_milisegundos(milis):
```

Escriba un programa principal que pida los milisegundos y muestre el texto que retorna la función.

| `milis` | `convertir_milisegundos(milis)` |
|---|---|
| 5500 | `"0:0:5"` |
| 100000 | `"0:1:40"` |
| 3600000 | `"1:0:0"` |
| 555550000 | `"154:19:10"` |

> [!Tip]
> **Pista:** primero convierta a segundos con `//`; luego use `//` y `%` para separar horas, minutos y segundos, como en los ejercicios de conversión del [Taller 1](../algoritmos-secuenciales/README.md). Para armar el texto, convierta cada número con `str()` y únalos con `+`: `str(1) + ":" + str(0)` da `"1:0"`.

---

## Anexo: Referencia rápida de funciones en Python

Las funciones se escriben **solo en Python**: el pseudocódigo del curso no tiene una sintaxis para funciones.

### A.1 Definir e invocar

```python
def calcular_area_rectangulo(base, altura):   # cabecera: nombre y parámetros
    area = base * altura                       # cuerpo (con sangría)
    return area                                # valor que retorna

resultado = calcular_area_rectangulo(4, 3)     # invocación: 4 y 3 son los argumentos
print(resultado)                               # 12
```

* **Definir** una función no la ejecuta: solo se ejecuta cuando se **invoca**.
* Los argumentos pueden ser números, variables o expresiones: `calcular_area_rectangulo(b, 2 * h)`.
* Una función puede invocar a otra; la que invoca es la **llamadora** y la invocada, la **llamada**. Cuando la llamada termina, la ejecución vuelve al punto de la llamadora donde se hizo la llamada.
* Nombres: un verbo que diga qué hace la función, en `snake_case` (`calcular_salario_bruto`, no `cal_sal_br` ni `calcularSalarioBruto`). No use nombres de funciones integradas (`min`, `max`, `sum`) para funciones o variables propias.

### A.2 Los cuatro casos

| | **No retorna** un valor | **Retorna** un valor |
|---|---|---|
| **Sin parámetros** | Caso 1: `mostrar_menu()` | Caso 2: `opcion = leer_opcion()` |
| **Con parámetros** | Caso 4: `mostrar_area(figura, area)` | Caso 3: `area = calcular_area_circulo(radio)` |

### A.3 `return` frente a `print`

| La función... | Qué recibe quien la invoca | ¿Se puede probar con `assert`? | ¿Se puede usar dentro de otra cuenta? |
|---|---|---|---|
| **retorna** el resultado (`return area`) | El valor | Sí | Sí |
| **imprime** el resultado (`print(area)`) | `None` | No | No |

* Una función sin `return`, o con `return` solo, retorna `None`. Por eso `print(funcion_sin_return())` muestra `None`.
* `return` termina la función de inmediato: las instrucciones que estén después no se ejecutan.

### A.4 Especificación: *Supone* y *Garantiza*

```python
def calcular_promedio(suma, cantidad):
    """
    Calcula el promedio de varios datos a partir de su suma y su cantidad.

    Supone:
        suma es un número; cantidad es un entero mayor o igual a 0.
    Garantiza:
        Retorna suma / cantidad (float). Si cantidad es 0, retorna 0.
    """
```

La especificación es un **contrato**: quien **invoca** la función se compromete a cumplir el *Supone*; quien la **escribe** se compromete a cumplir el *Garantiza*. Con ella, cualquiera puede usar la función sin leer su cuerpo (la función como **caja negra**).

### A.5 Pruebas con `assert`

```python
assert calcular_area_rectangulo(4, 3) == 12                 # típico
assert calcular_area_rectangulo(0, 3) == 0                  # límite
assert round(fahrenheit_a_celsius(30), 2) == -1.11          # decimales: con round
print("Todas las pruebas pasaron")
```

* Si la condición es verdadera, no pasa nada; si es falsa, Python se detiene con `AssertionError` e indica la línea.
* Una condición por `assert`, con el valor obtenido primero y el esperado después.
* Decimales: nunca con `==` directo (`0.1 + 0.2 == 0.3` da `False`); use `round(..., 2)`.
* No escriba `assert (condición, "mensaje")` entre paréntesis: nunca falla.
* Solo se prueban con `assert` las funciones que **retornan** un valor (casos 2 y 3).
* Un solo caso puede dar falsa confianza: pruebe casos **típicos**, **límite** y **especiales**.

### A.6 Formas de pasar argumentos

| Forma | Ejemplo con `def f(x, y=1, z=2):` | Qué recibe cada parámetro |
|---|---|---|
| Por posición | `f(5, 6, 7)` | `x = 5`, `y = 6`, `z = 7` |
| Por nombre | `f(z=7, x=5)` | `x = 5`, `y = 1` (por defecto), `z = 7` |
| Mezcladas | `f(5, z=7)` | `x = 5`, `y = 1`, `z = 7` |
| Inválida | `f(x=5, 6)` | `SyntaxError`: un argumento por posición no puede ir después de uno por nombre |

* Los parámetros con valor por defecto van **al final** de la cabecera: `def f(x=1, y):` es un error.

### A.7 Ámbito de las variables

* Los parámetros y las variables que se crean dentro de una función son **locales**: solo existen mientras la función se ejecuta y no se ven desde afuera (`NameError`).
* Una variable local y una del programa principal con el mismo nombre son **variables distintas**.
* Al invocar una función con un número o un texto, el parámetro recibe el **valor**: si la función le asigna otro valor al parámetro, la variable del llamador **no cambia** (códigos 2 y 3 de este taller). Con las listas es distinto: se verá en la clase 11.
* Una función puede **leer** una constante global (`NOTA_MINIMA = 3.0`). Modificar una variable global con `global` no se recomienda: la función debe **retornar** el resultado y el programa principal lo guarda.

### A.8 Funciones integradas y módulos

| Función | Ejemplo | Resultado |
|---|---|---|
| `abs(x)` | `abs(-3.5)` | `3.5` |
| `round(x, n)` | `round(3.14159, 2)` | `3.14` |
| `max(...)`, `min(...)` | `max(3, 7, 5)` | `7` |
| `math.sqrt(x)` | `math.sqrt(16)` | `4.0` |
| `random.randint(a, b)` | `random.randint(1, 6)` | un entero al azar entre 1 y 6, **incluidos** los dos |
| `random.seed(s)` | `random.seed(10)` | fija la semilla: la misma secuencia "aleatoria" en cada ejecución (útil para probar) |

| Forma de importar | Cómo se invoca |
|---|---|
| `import math` | `math.sqrt(16)` |
| `from math import sqrt` | `sqrt(16)` |

Para saber qué recibe y qué retorna una función que ya existe, consulte su especificación con `help(math.sqrt)`.

### A.9 Un programa en varios archivos

```text
📁 problema/
📄 numeros.py       — solo funciones (con su especificación); no lee ni imprime resultados
📄 test_numeros.py  — import de las funciones + los assert + print("Pruebas: todas pasaron")
📄 main.py          — programa principal: lee, invoca y muestra
```

```python
# main.py
from numeros import sumar_digitos

def main():
    n = int(input("Ingrese un entero: "))
    print("La suma de sus dígitos es", sumar_digitos(n))

if __name__ == "__main__":
    main()
```

La guarda `if __name__ == "__main__":` hace que `main()` se ejecute solo cuando se corre ese archivo directamente, y no cuando otro archivo lo importa.

---

> [!Important]
> Se usó IA generativa para seleccionar, adaptar y organizar los ejercicios de este taller a partir de talleres de repaso anteriores y de las indicaciones del docente. Las salidas y los casos de prueba se verificaron ejecutando el código. El docente revisó y validó la versión final.
