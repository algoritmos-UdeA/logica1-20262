![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Taller 4 — Arreglos

Este taller sirve de repaso del tema de **arreglos unidimensionales**: crear, llenar y recorrer un arreglo, alias y clones, funciones con listas en sus tres casos (clase 11) y arreglos parcialmente llenos (clase 12).

> [!NOTE]
> **La lista usada como arreglo.** En este curso, la lista de Python se usa con las reglas del arreglo:
>
> * **Tamaño fijo:** se crea con `[0.0] * N` (o con sus valores, `[3.0, 4.5, 2.0, 4.0]`) y no crece ni se encoge.
> * **Un solo tipo de dato:** todos reales, todos enteros, todos textos o todos lógicos.
> * **Acceso por posición**, de `0` a `N - 1`.
> * **Sin métodos de listas** (`append`, `remove`, `sort`, `reverse`, `index`, `count`…): son operaciones de objetos y se ven en Programación Orientada a Objetos. Todo lo que se pide en este taller se resuelve con recorridos.

## Cómo trabajar cada problema

1. **Entender:** identifique entradas, salidas y proceso. Pregúntese si los datos se van a usar **después** de leerlos: si es así, hay que guardarlos en un arreglo.
2. **Diseñar:** en los problemas de la sección 2, escriba el pseudocódigo con la notación de la clase 11 (`numeros = Arreglo(N)`, `Para (i = 0, N - 1, 1) Haga`). En la sección 3, divida el problema en funciones: escriba la cabecera, el *Supone* y el *Garantiza* de cada una, y diga de qué **caso** es (ver el [anexo A.4](#a4-funciones-con-listas)). Si la función modifica la lista que recibe, el *Garantiza* debe decirlo.
3. **Probar antes de integrar:** convierta los casos de prueba en `assert`. Pruebe casos **típicos**, **límite** (el primero, el último, un solo elemento) y **especiales** (lista vacía, valores repetidos, el valor no está).
4. **Implementar y verificar:** escriba las funciones hasta que pasen todas las pruebas y después el programa principal. Si lo resuelve en el computador, organícelo en tres archivos, como en el [laboratorio 4](../../laboratorios/4/README.md): un módulo con las funciones, `test_<módulo>.py` y `main.py` con la guarda `if __name__ == "__main__":`.

En los programas principales, los datos se leen **uno por línea**: primero la cantidad `N` y luego los `N` valores, como en `leer_notas(n)` de la clase 11.

---

## 1. Prueba de escritorio y predicción

Resuelva cada ejercicio **a mano, sin la ayuda del computador**. En la prueba de escritorio de un arreglo, dibuje sus casillas con su índice debajo y actualícelas a medida que cambian. Al terminar, compruebe su respuesta ejecutando el código o simulándolo en [Python Tutor](https://pythontutor.com/), que dibuja cada lista como una fila de casillas y muestra con flechas qué variables apuntan a ella.

### 1.1 Recorridos con `range`

**1.1.1** Suponga que `N = 4`. Escriba los valores que toma `i` en `for i in range(...)` con cada una de las siguientes expresiones. Si no toma ninguno, escriba "ninguno"; si produce un error, escriba "error".

| Expresión | Valores de `i` |
|---|---|
| `range(3)` | |
| `range(3, 10)` | |
| `range(3, 10, 3)` | |
| `range(3, 10.5, 0.5)` | |
| `range(10, 3)` | |
| `range(10, 3, -1)` | |
| `range(N)` | |
| `range(N - 1, -1, -1)` | |
| `range(N - 1, 0, -1)` | |
| `range(1, N, 2)` | |

> **Pregunta para pensar:** ¿cuál de las dos últimas expresiones con paso `-1` sirve para recorrer un arreglo de `N` elementos al revés? ¿Qué posición se salta la otra, y por qué ese error es peligroso aunque Python no lo señale?

**1.1.2** (Respuesta múltiple) ¿Con cuáles de las siguientes expresiones el código muestra `3`, `11` y `19`, uno por línea?

```python
for num in __________________:
    print(num)
```

* a. `range(3, 8, 20)`
* b. `range(3, 23, 8)`
* c. `range(3, 19, 8)`
* d. `range(3, 20, 8)`

**1.1.3** (Respuesta múltiple) ¿Cuáles de los siguientes códigos dejan `valores` con el contenido `[3, 6, 9]`? Para los que no, diga qué contenido queda o qué error se produce.

```python
valores = [0] * 3
```

* a.
  ```python
  for i in range(3):
      valores[i] = 3 * i
  ```
* b.
  ```python
  for i in range(3):
      valores[i] = 3 * (i + 1)
  ```
* c.
  ```python
  for i in range(1, 4):
      valores[i] = 3 * i
  ```
* d.
  ```python
  for i in range(1, 4):
      valores[i - 1] = 3 * i
  ```

### 1.2 Alias y clones

**Código 1.** ¿Qué muestra este código?

```python
lista1 = [1, 3, 5, 7, 9]
lista2 = lista1
lista1[0] = 111
print(lista1)
print(lista2)
```

**Código 2.** ¿Qué muestra este código? Compárelo con el código 1.

```python
N = 2
lista1 = [1, 43]
lista2 = [0] * N
for i in range(N):
    lista2[i] = lista1[i]
lista1[0] = 22
print(lista1)
print(lista2)
```

> **Pregunta para pensar:** después de `lista2 = lista1`, ¿cuántas listas hay en la memoria? ¿Y después del ciclo del código 2? Dibuje las flechas como lo hace Python Tutor.

**1.2.1** (Respuesta múltiple) Considere el siguiente código:

```python
a = [1, 2, 3]
b = a
# FALTA CÓDIGO AQUÍ
print(a, b)
```

La salida es `[1, 9, 3] [1, 9, 3]`. ¿Cuáles de los siguientes fragmentos pueden ir en el lugar de `# FALTA CÓDIGO AQUÍ`?

* a. `a[1] = 9`
* b. `a = [1, 9, 3]` y en la línea siguiente `b = [1, 9, 3]`
* c. `b[-2] = 9`
* d. `b[1] = 90` y en la línea siguiente `a[1] = b[1] // 10`

**1.2.2** (Respuesta múltiple) Repita el ejercicio anterior, pero ahora con dos listas distintas:

```python
a = [1, 2, 3]
b = [1, 2, 3]
# FALTA CÓDIGO AQUÍ
print(a, b)
```

> **Pregunta para pensar:** ¿por qué cambia tanto la respuesta entre 1.2.1 y 1.2.2, si la única diferencia es la segunda línea? En la opción c se usa el índice negativo `-2`: ¿a qué posición equivale en una lista de 3 elementos?

### 1.3 Funciones con listas

**1.3.1** (Respuesta única) ¿Qué muestra el siguiente código?

```python
def incrementar(lista, incremento):
    i = 0
    while i < len(lista):
        lista[i] = lista[i] + incremento
        i = i + 1

valores = [1, 2, 3]
print(incrementar(valores, 2))
print(valores)
```

* a. `[3, 4, 5]` y luego `[1, 2, 3]`
* b. `[3, 4, 5]` y luego `None`
* c. `None` y luego `[1, 2, 3]`
* d. `None` y luego `[3, 4, 5]`

> **Pregunta para pensar:** ¿de qué caso es `incrementar`? ¿Qué debería decir su *Garantiza*?

**1.3.2** La función `invertir` deja una lista al revés. Usa una función auxiliar, `intercambiar`, que cambia de lugar dos elementos de la lista.

```python
def intercambiar(lista, i, j):
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp

def invertir(lista):
    n = len(lista)
    for i in range(n // 2):
        intercambiar(lista, i, n - 1 - i)
```

¿Qué muestra cada uno de los siguientes fragmentos?

* a.
  ```python
  numeros = [1, 4, 3]
  invertir(numeros)
  print(numeros)
  ```
* b.
  ```python
  numeros = [1, 4, 3]
  numeros = invertir(numeros)
  print(numeros)
  ```

> **Pregunta para pensar:** ¿por qué el ciclo de `invertir` va solo hasta `n // 2`? Haga la prueba de escritorio con `[1, 4, 3, 5]` y con `[7]`. ¿Qué pasaría si fuera hasta `n`?

**1.3.3** (Respuesta única) La siguiente función suma los números de una lista **hasta encontrar el primer número par**, sin incluirlo:

```python
def sumar_hasta_par(lista):
    i = 0
    total = 0
    while i < len(lista) and lista[i] % 2 != 0:
        total = total + lista[i]
        i = i + 1
    return total
```

Por ejemplo, `sumar_hasta_par([1, 3, 4, 5, 7])` retorna `4`. Las cuatro versiones siguientes intentan hacer lo mismo con un `for`, que recorre **todas** las posiciones. ¿Cuál de ellas retorna siempre lo mismo que `sumar_hasta_par`?

* a.
  ```python
  def sumar_hasta_par(lista):
      encontro_par = False
      total = 0
      for i in range(len(lista)):
          if lista[i] % 2 != 0:
              total = total + lista[i]
              encontro_par = True
      return total
  ```
* b.
  ```python
  def sumar_hasta_par(lista):
      encontro_par = False
      total = 0
      for i in range(len(lista)):
          if lista[i] % 2 != 0:
              total = total + lista[i]
          encontro_par = True
      return total
  ```
* c.
  ```python
  def sumar_hasta_par(lista):
      encontro_par = False
      total = 0
      for i in range(len(lista)):
          if lista[i] % 2 != 0 and not encontro_par:
              total = total + lista[i]
          else:
              encontro_par = True
      return total
  ```
* d.
  ```python
  def sumar_hasta_par(lista):
      encontro_par = False
      total = 0
      for i in range(len(lista)):
          if lista[i] % 2 != 0:
              total = total + lista[i]
          elif not encontro_par:
              encontro_par = True
      return total
  ```

> [!Tip]
> **Pista:** pruebe cada versión con `[1, 3, 4, 5, 7]` y con `[2, 1, 3]`. ¿Qué papel cumple `encontro_par`? (Repase el rol de **bandera** en el [anexo del Taller 2](../condicionales-ciclos/README.md#a6-roles-de-las-variables-en-un-ciclo)).

> **Pregunta para pensar:** en la versión con `while`, ¿qué pasaría si se escribiera la condición al revés, `lista[i] % 2 != 0 and i < len(lista)`, y la lista solo tuviera impares?

**1.3.4** (Respuesta única) Considere la siguiente función:

```python
def misterio(lista):
    i = 0
    total = 0
    while i < len(lista):
        total = total + lista[i]
        i = i + 3
    return total
```

¿Cuál es la mejor descripción para el *Garantiza* de `misterio`?

* a. Retorna la suma de los elementos de las posiciones 0, 3, 6, … de la lista.
* b. Retorna 0.
* c. Retorna la suma de los números 0, 3, 6, … (las posiciones, no los elementos).
* d. Retorna la suma de todos los elementos, excepto uno de cada tres.

**1.3.5** (Respuesta única) A la siguiente función le falta una línea:

```python
def sumar_parejas(lista):
    """
    Suma los elementos de la lista por parejas: el 0 con el 1,
    el 2 con el 3, y así sucesivamente.

    Supone:
        lista tiene una cantidad par de elementos.
    Garantiza:
        Retorna una lista nueva, de la mitad del tamaño, con las sumas.
        Por ejemplo, sumar_parejas([1, 2, 3, 4, 5, 6]) retorna [3, 7, 11].
        No modifica lista.
    """
    resultado = [0] * (len(lista) // 2)
    i = 0
    while i < len(lista):
        resultado[i // 2] = lista[i] + lista[i + 1]
        # FALTA CÓDIGO AQUÍ
    return resultado
```

¿Cuál de las siguientes líneas completa la función? Para las demás, diga qué ocurre.

* a. `i = i * 2`
* b. `i = i + i`
* c. `i = i + 2`
* d. `i = i + 1`

---

## 2. Problemas con arreglos

**2.1 Tabla de cuadrados.** Elabore un algoritmo que calcule el cuadrado de los 100 primeros números enteros positivos, los guarde en un arreglo y a continuación muestre una tabla con cada número y su cuadrado.

| Posición | Número | Cuadrado |
|---|---|---|
| 0 | 1 | 1 |
| 9 | 10 | 100 |
| 99 | 100 | 10000 |

> **Pregunta para pensar:** ¿qué relación hay entre la posición de una casilla y el número cuyo cuadrado guarda? Este problema se puede resolver sin arreglo, con un solo ciclo. ¿Cuándo sí se necesitaría guardar los cuadrados?

**2.2 Números al revés.** Elabore un algoritmo que permita a un usuario introducir 15 números y que luego los muestre en el orden inverso al de entrada.

| Números leídos (con `N = 5` para probar) | Salida |
|---|---|
| 3, 8, 1, 9, 4 | 4, 9, 1, 8, 3 |

> [!Tip]
> **Pista:** use una constante `CANTIDAD = 15` y, mientras prueba, cámbiela por un valor pequeño. Para el recorrido inverso, vea la tabla de recorridos en el [anexo A.2](#a2-recorridos).

**2.3 Diferencia con el promedio.** Elabore un algoritmo que permita al usuario introducir 15 números, y luego muestre cada número y su diferencia con el promedio de los números introducidos.

| Números leídos (con `N = 5` para probar) | Promedio | Diferencias |
|---|---|---|
| 2.5, 4.0, 3.5, 1.0, 5.0 | 3.20 | -0.70, 0.80, 0.30, -2.20, 1.80 |

> **Pregunta para pensar:** ¿por qué este problema no se puede resolver sin un arreglo? Compárelo con el problema que motivó los arreglos en la [clase 11](../../clases/11/teoria/README.md).

**2.4 Calificación según el mejor puntaje.** Escriba un programa que lea los puntajes (de 0 a 100) de `N` estudiantes y luego le asigne a cada uno una letra según el **mejor** puntaje del grupo:

* La letra es `A` si el puntaje es mayor o igual que el mejor − 10.
* La letra es `B` si el puntaje es mayor o igual que el mejor − 20.
* La letra es `C` si el puntaje es mayor o igual que el mejor − 30.
* La letra es `D` si el puntaje es mayor o igual que el mejor − 40.
* En otro caso, la letra es `F`.

Escriba dos funciones: `buscar_mayor(puntajes)`, que retorna el mejor puntaje, y `asignar_letra(puntaje, mejor)`, que retorna la letra de un puntaje.

```text
Estudiante 0: puntaje 40, letra C
Estudiante 1: puntaje 55, letra B
Estudiante 2: puntaje 70, letra A
Estudiante 3: puntaje 58, letra B
```

| Puntajes | Mejor | Letras |
|---|---|---|
| 40, 55, 70, 58 | 70 | C, B, A, B |
| 90, 81, 75, 62, 50, 49 | 90 | A, A, B, C, D, F |

> **Pregunta para pensar:** ¿cuál de las dos funciones recibe la lista? ¿Por qué `asignar_letra` no la necesita?

**2.5 Elementos en las posiciones pares.** Escriba una función que reciba una lista y retorne una lista **nueva** con los elementos que están en las posiciones pares (0, 2, 4, …) de la lista recibida:

```python
def elementos_posiciones_pares(lista):
```

| `lista` | Resultado |
|---|---|
| `[]` | `[]` |
| `[16]` | `[16]` |
| `[7, 8, 15, 14, 3, 11]` | `[7, 15, 3]` |
| `[18, 15, 7, 1, 3, 19, 18, 14]` | `[18, 7, 3, 18]` |
| `[17, 1, 20, 18, 1, 19, 9, 17, 17, 19]` | `[17, 20, 1, 9, 17]` |

> [!Tip]
> **Pista:** antes de llenar la lista nueva hay que crearla con su tamaño exacto. ¿Cuántas posiciones pares tiene una lista de 5 elementos? ¿Y una de 6? Busque una expresión con `//` que sirva para los dos casos. Para llenarla se necesitan **dos** índices: uno que recorre la lista recibida y otro (`k`) que indica la siguiente casilla libre de la nueva, como en `posiciones_mayores_que` de la clase 11.

**2.6 Cuatro iguales seguidos.** Escriba una función que retorne `True` si la lista tiene cuatro números **consecutivos** con el mismo valor, y `False` si no:

```python
def hay_cuatro_iguales_seguidos(valores):
```

Escriba un programa principal que lea una serie de enteros e informe si tiene cuatro números consecutivos iguales.

| `valores` | Resultado |
|---|---|
| `[3, 4, 5, 5, 5, 5, 4, 5]` | `True` |
| `[3, 4, 5, 5, 6, 5, 5, 4, 5]` | `False` |
| `[2, 2, 2, 2]` | `True` |
| `[2, 2, 2, 3, 2]` | `False` |
| `[1, 1, 1]` | `False` |

> [!Tip]
> **Pista:** es una variante de **comparar vecinos**, pero con tres vecinos a la derecha: `valores[i + 1]`, `valores[i + 2]` y `valores[i + 3]`. ¿Hasta qué posición puede llegar `i` sin salirse del arreglo?

**2.7 Contar ocurrencias.** Escriba un programa que lea `N` enteros entre 1 y 100 y cuente cuántas veces aparece cada uno. Muestre solo los números que aparecen al menos una vez, en orden creciente, y use "vez" o "veces" según corresponda.

```text
Cantidad de números: 9
(se leen: 2, 5, 6, 5, 4, 3, 23, 43, 2)
2 aparece 2 veces
3 aparece 1 vez
4 aparece 1 vez
5 aparece 2 veces
6 aparece 1 vez
23 aparece 1 vez
43 aparece 1 vez
```

Escriba una función `contar_ocurrencias(numeros)` que retorne un arreglo de **contadores**, en el que la casilla `v` guarda cuántas veces aparece el número `v`. Por ejemplo, para la lista del ejemplo, la casilla 2 vale `2`, la casilla 5 vale `2` y la casilla 7 vale `0`.

> [!Tip]
> **Pista:** cree el arreglo de contadores con `[0] * 101`, para que el número `v` caiga en la casilla `v` (la casilla 0 no se usa). Cada número leído se usa **como índice**: `contadores[numeros[i]] = contadores[numeros[i]] + 1`. Es el mismo ejercicio de la clase 11 en el que el índice es el valor de otro arreglo.

**2.8 Eliminar repetidos.** Escriba una función que retorne una lista **nueva** con los valores de la lista recibida, pero sin repetidos: cada valor aparece una sola vez, en el orden de su primera aparición.

```python
def eliminar_repetidos(lista):
```

Escriba un programa principal que lea 10 números y muestre los distintos:

```text
(se leen: 1, 2, 3, 2, 1, 6, 3, 4, 5, 2)
Los números distintos son: 1 2 3 6 4 5
```

| `lista` | Resultado |
|---|---|
| `[1, 2, 3, 2, 1, 6, 3, 4, 5, 2]` | `[1, 2, 3, 6, 4, 5]` |
| `[7, 7, 7]` | `[7]` |
| `[4, 1, 9]` | `[4, 1, 9]` |
| `[]` | `[]` |

> [!Tip]
> **Pista:** sin `append`, la lista nueva se crea con su tamaño exacto, como en `posiciones_mayores_que` de la clase 11: primero se cuenta, luego se crea y por último se llena. Una función auxiliar ayuda: `es_primera_aparicion(lista, i)`, que retorna `True` si `lista[i]` no aparece en ninguna posición anterior a `i`. ¿Cuántas veces se usa esa función?

**2.9 Los casilleros.** Un colegio tiene 100 casilleros y 100 estudiantes. El primer día de clases todos los casilleros están cerrados. A medida que llegan los estudiantes, el primero, E1, abre todos los casilleros. Luego el segundo, E2, empieza en el casillero C2 y cierra uno de cada dos. El estudiante E3 empieza en el casillero C3 y cambia uno de cada tres (lo cierra si estaba abierto y lo abre si estaba cerrado). E4 empieza en C4 y cambia uno de cada cuatro, y así sucesivamente, hasta que E100 cambia C100.

Después de que todos los estudiantes pasaron, ¿cuáles casilleros quedaron abiertos? Escriba un programa que encuentre la respuesta. Use una función `simular_casilleros(n)` que retorne un arreglo de `n` valores lógicos (`True` = abierto).

| `n` | Casilleros abiertos |
|---|---|
| 4 | 1, 4 (el arreglo retornado es `[True, False, False, True]`) |
| 10 | 1, 4, 9 |

> [!Tip]
> **Pista:** el casillero C1 está en la posición 0. El estudiante `e` cambia las posiciones `e - 1`, `e - 1 + e`, `e - 1 + 2e`, … ¿Qué `range` genera esas posiciones? Para cambiar el estado de un casillero, use `not`.

> **Pregunta para pensar:** observe los números de los casilleros que quedan abiertos. ¿Qué tienen en común? ¿Por qué? (Pista: ¿cuántas veces se cambia cada casillero?)

### Para explorar por su cuenta

Los empleados del registro en una conferencia para autores de libros infantiles recopilaron datos sobre los participantes: cada uno ha escrito de 1 a 40 libros. Diseñe un programa que acepte en forma continua el número de libros escritos por cada participante, hasta que se introduzca un valor centinela, y luego muestre cuántos participantes han escrito cada número de libros (de 1 a 40). Rechace los valores fuera del rango. ¿En qué se parece al problema 2.7?

---

## 3. Arreglos parcialmente llenos

Cuando no se sabe cuántos datos habrá, el arreglo se crea con un **cupo** máximo y una variable `cantidad` dice cuántas casillas están ocupadas (de `0` a `cantidad - 1`). Las funciones reciben `cantidad` y recorren hasta ahí, no hasta `len()`. Una función que cambia `cantidad` la retorna: `cantidad = leer_numeros(numeros, CUPO)` (ver el [anexo A.5](#a5-patrones-frecuentes)).

**3.1 Números al revés, hasta un centinela.** Modifique el programa del problema 2.2 de modo que el usuario pueda introducir **cualquier cantidad** de números enteros positivos, hasta 15, terminando con el centinela `0`. Si el usuario introduce 15 números, el programa deja de pedirlos sin esperar el centinela.

| Números leídos | Salida |
|---|---|
| 4, 7, 2, 0 | 2, 7, 4 |
| 0 | Un mensaje que indica que no se introdujo ningún número |
| 15 números | Los 15 al revés, sin pedir el centinela |

> [!Tip]
> **Pista:** escriba una función `leer_numeros(numeros, cupo)` que llene el arreglo y **retorne** la cantidad de números leídos. El ciclo de lectura tiene **dos** razones para terminar: el centinela o el cupo lleno. Otra función, `mostrar_al_reves(numeros, cantidad)`, recorre desde `cantidad - 1` hasta 0.

**3.2 Diferencia con el promedio, hasta un centinela.** Modifique el programa del problema 2.3 de la misma forma: el usuario introduce números positivos, hasta 15, terminando con `0`.

| Números leídos | Promedio | Diferencias |
|---|---|---|
| 3, 5, 1, 0 | 3.00 | 0.00, 2.00, -2.00 |
| 0 | — | Un mensaje que indica que no se introdujo ningún número |

> **Pregunta para pensar:** si `calcular_promedio(numeros)` de la clase 11 se invoca con el arreglo parcialmente lleno, ¿qué resultado da con los datos `3, 5, 1, 0`? ¿Por qué? ¿Qué parámetro le falta?

---

## Anexo: Referencia rápida de arreglos

### A.1 Operaciones básicas

| Operación | Pseudocódigo | Python |
|---|---|---|
| Crear | `notas = Arreglo(N)` | `notas = [0.0] * N` |
| Crear con valores | `notas = [3.0, 4.5, 2.0, 4.0]` | `notas = [3.0, 4.5, 2.0, 4.0]` |
| Guardar un valor | `notas[2] = 5.0` | `notas[2] = 5.0` |
| Leer un valor del teclado | `Leer(notas[i])` | `notas[i] = float(input("Nota: "))` |
| Llenar | `Para (i = 0, N - 1, 1) Haga`<br>&nbsp;&nbsp;`Leer(notas[i])`<br>`Fin_Para` | `for i in range(N):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`notas[i] = float(input("Nota: "))` |
| Mostrar | `Para (i = 0, N - 1, 1) Haga`<br>&nbsp;&nbsp;`Escribir(notas[i])`<br>`Fin_Para` | `for i in range(N):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(notas[i])` |
| Acumular | `suma = 0`<br>`Para (i = 0, N - 1, 1) Haga`<br>&nbsp;&nbsp;`suma = suma + notas[i]`<br>`Fin_Para` | `suma = 0`<br>`for i in range(N):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`suma = suma + notas[i]` |
| Último elemento | `notas[N - 1]` | `notas[N - 1]` (o `notas[-1]`) |

> Un índice demasiado grande produce `IndexError: list index out of range`. Un índice negativo **no** produce error en Python: `notas[i - 1]` con `i = 0` toma, sin avisar, el **último** elemento. En pseudocódigo (y en lenguajes como C) los índices negativos no existen.

### A.2 Recorridos

| Recorrido | Pseudocódigo | Python | Posiciones (N = 6) |
|---|---|---|---|
| Completo | `Para (i = 0, N - 1, 1)` | `range(N)` | 0, 1, 2, 3, 4, 5 |
| Inverso | `Para (i = N - 1, 0, -1)` | `range(N - 1, -1, -1)` | 5, 4, 3, 2, 1, 0 |
| Desde la segunda | `Para (i = 1, N - 1, 1)` | `range(1, N)` | 1, 2, 3, 4, 5 |
| Hasta la penúltima | `Para (i = 0, N - 2, 1)` | `range(N - 1)` | 0, 1, 2, 3, 4 |
| Posiciones pares | `Para (i = 0, N - 1, 2)` | `range(0, N, 2)` | 0, 2, 4 |

Para cualquier recorrido hay que responder tres preguntas: **desde dónde**, **hasta dónde** y **de a cuánto**. Python también permite recorrer por elemento (`for nota in notas`), pero así no se conoce la posición y no se puede modificar el arreglo; el pseudocódigo no tiene esa forma.

### A.3 Alias y clones

| Instrucción | Qué hace |
|---|---|
| `copia = notas` | **No copia**: `copia` es otro nombre (un alias) de la misma lista. Cambiar `copia[0]` cambia `notas[0]` |
| `copia = [0.0] * N` y un recorrido que copia casilla por casilla | Crea una lista nueva (un clon) |
| `copia = notas[:]` o `copia = list(notas)` | En Python, también crean un clon |

### A.4 Funciones con listas

| | Caso 1 | Caso 2 | Caso 3 |
|---|---|---|---|
| Ejemplo | `calcular_promedio(notas)` | `leer_notas(n)` | `aplicar_bonificacion(notas, puntos)` |
| Entra | una lista | un valor | una lista (y un valor) |
| Sale (`return`) | un valor | una lista nueva | nada |
| ¿Modifica la lista? | No | — (la crea) | Sí |
| El *Garantiza* dice | "No modifica notas" | "Retorna una lista nueva" | "MODIFICA notas" |
| Se invoca | `prom = calcular_promedio(notas)` | `notas = leer_notas(4)` | `aplicar_bonificacion(notas, 0.5)` |
| Se prueba | `assert` sobre el valor retornado | Ejecutando el programa (usa `input`) | Se llama y **después** se revisa la lista |

* Dentro de la función, el número de elementos se obtiene con `len(lista)`, porque la función no recibe `N`.
* El parámetro es un **alias** de la lista que se pasa: si la función cambia una casilla, la lista cambia afuera. Si no se quiere modificar la original, se pasa un clon: `aplicar_bonificacion(notas[:], 0.5)`.
* Una función del caso 3 retorna `None`: `notas = aplicar_bonificacion(notas, 0.5)` deja `notas` en `None`, y `assert aplicar_bonificacion(X, 0.5) == [...]` siempre falla.

### A.5 Patrones frecuentes

**Crear una lista nueva de tamaño exacto (sin `append`):** primero se cuenta, luego se crea y por último se llena con un segundo índice `k`.

```python
cantidad = contar_mayores_que(notas, valor)
posiciones = [0] * cantidad
k = 0
for i in range(len(notas)):
    if notas[i] > valor:
        posiciones[k] = i
        k = k + 1
```

**Arreglo de contadores:** el valor leído se usa como índice.

```python
contadores = [0] * 101
for i in range(N):
    contadores[numeros[i]] = contadores[numeros[i]] + 1
```

**Comparar vecinos:** se recorre hasta la penúltima posición.

```python
for i in range(N - 1):
    if notas[i + 1] > notas[i]:
        print("Subió en la posición", i + 1)
```

**Arreglo parcialmente lleno:** un cupo fijo y la cantidad de casillas ocupadas. Las funciones reciben `cantidad`, y las que la cambian, la retornan.

```python
CUPO = 15
numeros = [0] * CUPO
cantidad = leer_numeros(numeros, CUPO)        # MODIFICA numeros y retorna la cantidad
for i in range(cantidad - 1, -1, -1):         # se recorre hasta cantidad, no hasta len()
    print(numeros[i])
```

---

> [!Important]
> Se usó IA generativa para seleccionar, adaptar y organizar los ejercicios de este taller a partir de talleres de repaso anteriores y de las indicaciones del docente. Las salidas y los casos de prueba se verificaron ejecutando el código. El docente revisó y validó la versión final.
