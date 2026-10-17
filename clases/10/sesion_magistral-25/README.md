![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 25

* **Tipo**: Presencial
* **Fecha**: 13/10/2026
* **Parte**: Segundo bloque de clase (16-18)

## Resumen

Segunda sesión de la [clase 10](../README.md), continuación de la [sesión 24](../sesion_magistral-24/README.md). Se estudian dos temas:

* **El ámbito de las variables**: dónde existe cada variable, qué diferencia hay entre una variable **local** y una **global**, por qué una función no debería modificar una variable global, y qué errores aparecen cuando no se respeta el ámbito.
* **Las formas de pasar argumentos** a una función: por posición, por nombre y con valores por defecto. También se ve qué pasa cuando una función llama a otra.

El diseño top-down, el tema siguiente de la clase, quedó pendiente para la próxima sesión.

> [!NOTE]
> En clase, estas ideas se explicaron con el programa de temperaturas y con la función [`seno`](../teoria/codigo/seno.py). Esta página usa **ejemplos nuevos**, ambientados en el Kwik-E-Mart, la tienda de Apu en Springfield, para practicar las mismas ideas con otros datos. Todos los ejemplos están en la carpeta [`codigo/`](codigo/), y las salidas que se muestran son las que produce cada archivo al ejecutarlo.

> [!TIP]
> **Si no asistió a clase**, siga esta ruta:
> 1. Lea [cómo usar los enlaces de Python Tutor](#cómo-usar-los-enlaces-de-python-tutor). El ámbito se entiende mucho mejor **viendo** cómo se crean y desaparecen las variables que leyendo sobre ello.
> 2. En cada ejemplo, **antes de mirar la salida**, intente predecir qué va a imprimir el programa. Luego compruébelo con la salida y con el enlace de Python Tutor.
> 3. Resuelva los [ejercicios de práctica](#ejercicios-de-práctica-prediga-la-salida) antes de abrir las soluciones.

**Contenido de esta página:**

* [Cómo usar los enlaces de Python Tutor](#cómo-usar-los-enlaces-de-python-tutor)
* [Parte 1 — Ámbito: variables locales y globales](#parte-1--ámbito-variables-locales-y-globales)
* [Parte 2 — Variables globales: ¿sí o no?](#parte-2--variables-globales-sí-o-no)
* [Parte 3 — Formas de pasar argumentos](#parte-3--formas-de-pasar-argumentos)
* [Parte 4 — Una función que llama a otra](#parte-4--una-función-que-llama-a-otra)
* [Resumen de reglas](#resumen-de-reglas)
* [Ejercicios de práctica: prediga la salida](#ejercicios-de-práctica-prediga-la-salida)
* [Para explorar por su cuenta](#para-explorar-por-su-cuenta)
* [Lo que quedó pendiente](#lo-que-quedó-pendiente)
* [Archivos](#archivos)

## Cómo usar los enlaces de Python Tutor

[Python Tutor](https://pythontutor.com) ejecuta un programa **línea por línea** y dibuja las variables que existen en cada momento. Cada ejemplo de esta página tiene un enlace que abre su código ya cargado. La página está en inglés; esto es lo que hay que mirar:

| En la pantalla | Qué significa |
|---|---|
| Botones **Next >** y **< Prev** | Avanzan o retroceden una línea |
| Flecha **roja** | La siguiente línea que se va a ejecutar |
| Flecha **verde clara** | La línea que se acaba de ejecutar |
| **Print output** | Lo que el programa ha mostrado en pantalla hasta ese momento |
| **Global frame** | Las variables **globales**, las del programa principal |
| Un recuadro con el nombre de una función (por ejemplo, `aplicar_descuento`) | Las variables **locales** de esa llamada. Aparece cuando se llama a la función y desaparece cuando termina |
| **Return value** | El valor que la función está a punto de devolver con `return` |

La idea más importante del ámbito se ve directamente en el dibujo: **cada llamada a una función tiene su propio recuadro**, y las variables de ese recuadro no son las del *Global frame*, aunque tengan el mismo nombre.

## Parte 1 — Ámbito: variables locales y globales

El **ámbito** de una variable es la parte del programa donde esa variable existe y se puede usar.

| | Dónde se crea | Cuánto tiempo existe |
|---|---|---|
| **Variable local** | Dentro de una función. Los **parámetros** también son locales | Solo mientras la función se ejecuta |
| **Variable global** | Fuera de las funciones, en el programa principal | Hasta que termina el programa |

### Ejemplo 1: el mismo nombre, dos variables distintas

En el Kwik-E-Mart, una función aplica un descuento del 10 % a un precio. Observe que hay **dos** variables llamadas `precio` y **dos** llamadas `descuento`: unas en el programa principal y otras dentro de la función.

```python
# Ambito: dos variables con el mismo nombre en ambitos distintos

def aplicar_descuento(precio):
    descuento = 0.10
    precio = precio - precio * descuento
    print("Dentro de la funcion: precio =", precio, "y descuento =", descuento)
    return precio

precio = 5000
descuento = 0.50
precio_final = aplicar_descuento(precio)
print("precio_final =", precio_final)
print("precio =", precio)
print("descuento =", descuento)
```

Antes de ver la salida: ¿cuánto valdrán `precio` y `descuento` al final del programa?

```text
Dentro de la funcion: precio = 4500.0 y descuento = 0.1
precio_final = 4500.0
precio = 5000
descuento = 0.5
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Ambito%3A%20dos%20variables%20con%20el%20mismo%20nombre%20en%20ambitos%20distintos%0A%0Adef%20aplicar_descuento%28precio%29%3A%0A%20%20%20%20descuento%20%3D%200.10%0A%20%20%20%20precio%20%3D%20precio%20-%20precio%20%2A%20descuento%0A%20%20%20%20print%28%22Dentro%20de%20la%20funcion%3A%20precio%20%3D%22%2C%20precio%2C%20%22y%20descuento%20%3D%22%2C%20descuento%29%0A%20%20%20%20return%20precio%0A%0Aprecio%20%3D%205000%0Adescuento%20%3D%200.50%0Aprecio_final%20%3D%20aplicar_descuento%28precio%29%0Aprint%28%22precio_final%20%3D%22%2C%20precio_final%29%0Aprint%28%22precio%20%3D%22%2C%20precio%29%0Aprint%28%22descuento%20%3D%22%2C%20descuento%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

La función cambió **su** `precio` a `4500.0` y usó **su** `descuento` de `0.1`. El `precio` y el `descuento` globales no cambiaron. Esta prueba de escritorio separa las variables por ámbito:

| Línea | Qué pasa | Variables globales | Variables locales de `aplicar_descuento` |
|---|---|---|---|
| 9 | Se crea `precio` global | `precio = 5000` | (la función no se ha llamado) |
| 10 | Se crea `descuento` global | `precio = 5000`, `descuento = 0.5` | |
| 11 | Se llama `aplicar_descuento(precio)`: el **valor** `5000` se copia en el parámetro | sin cambios | `precio = 5000` |
| 4 | Se crea `descuento` local | sin cambios | `precio = 5000`, `descuento = 0.1` |
| 5 | Se cambia el `precio` **local** | sin cambios | `precio = 4500.0`, `descuento = 0.1` |
| 7 | `return precio` devuelve `4500.0`; las variables locales **desaparecen** | sin cambios | (ya no existen) |
| 11 | El valor devuelto se guarda | `precio = 5000`, `descuento = 0.5`, `precio_final = 4500.0` | |

**Idea clave:** al llamar a una función, el parámetro recibe una **copia del valor** del argumento. Lo que la función haga con su parámetro no cambia la variable del programa principal. La única forma de sacar un resultado de la función es con `return`, y guardándolo en una variable.

### Ejemplo 2: una variable local no recuerda nada

Apu quiere sumar lo que compra un cliente: un chocolate de \$2000, dos gaseosas de \$1500 y tres chicles de \$800. Alguien escribe esta función, con la idea de que `total` vaya acumulando cada compra:

```python
# Ambito: una variable local se crea de nuevo en cada llamada

def agregar_al_total(precio, cantidad):
    total = 0                           # local: empieza en 0 en cada llamada
    total = total + precio * cantidad
    return total

agregar_al_total(2000, 1)               # un chocolate
agregar_al_total(1500, 2)               # dos gaseosas
total = agregar_al_total(800, 3)        # tres chicles
print("Total a pagar:", total)
```

La cuenta correcta es $2000 + 3000 + 2400 = 7400$. ¿Qué imprime el programa?

```text
Total a pagar: 2400
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Ambito%3A%20una%20variable%20local%20se%20crea%20de%20nuevo%20en%20cada%20llamada%0A%0Adef%20agregar_al_total%28precio%2C%20cantidad%29%3A%0A%20%20%20%20total%20%3D%200%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20local%3A%20empieza%20en%200%20en%20cada%20llamada%0A%20%20%20%20total%20%3D%20total%20%2B%20precio%20%2A%20cantidad%0A%20%20%20%20return%20total%0A%0Aagregar_al_total%282000%2C%201%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20un%20chocolate%0Aagregar_al_total%281500%2C%202%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20dos%20gaseosas%0Atotal%20%3D%20agregar_al_total%28800%2C%203%29%20%20%20%20%20%20%20%20%23%20tres%20chicles%0Aprint%28%22Total%20a%20pagar%3A%22%2C%20total%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

`total` es una variable **local**: se crea en cada llamada, empieza en `0` y desaparece cuando la función termina. La función no tiene memoria entre una llamada y otra, así que la tercera llamada solo devuelve el valor de los chicles, `2400`. Además, los resultados de las dos primeras llamadas se perdieron, porque no se guardaron en ninguna variable.

En Python Tutor se ve claramente: el recuadro de `agregar_al_total` aparece **tres veces**, y cada vez empieza con `total = 0`.

### Ejemplo 3: la función calcula, el programa principal acumula

La solución es repartir el trabajo. La función calcula **un** subtotal, y el **acumulador** queda en el programa principal, como en los ciclos de las clases 7 y 8:

```python
# Solucion: la funcion calcula y el programa principal acumula

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

total = 0
total = total + calcular_subtotal(2000, 1)    # un chocolate
total = total + calcular_subtotal(1500, 2)    # dos gaseosas
total = total + calcular_subtotal(800, 3)     # tres chicles
print("Total a pagar:", total)
```

```text
Total a pagar: 7400
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Solucion%3A%20la%20funcion%20calcula%20y%20el%20programa%20principal%20acumula%0A%0Adef%20calcular_subtotal%28precio%2C%20cantidad%29%3A%0A%20%20%20%20subtotal%20%3D%20precio%20%2A%20cantidad%0A%20%20%20%20return%20subtotal%0A%0Atotal%20%3D%200%0Atotal%20%3D%20total%20%2B%20calcular_subtotal%282000%2C%201%29%20%20%20%20%23%20un%20chocolate%0Atotal%20%3D%20total%20%2B%20calcular_subtotal%281500%2C%202%29%20%20%20%20%23%20dos%20gaseosas%0Atotal%20%3D%20total%20%2B%20calcular_subtotal%28800%2C%203%29%20%20%20%20%20%23%20tres%20chicles%0Aprint%28%22Total%20a%20pagar%3A%22%2C%20total%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

## Parte 2 — Variables globales: ¿sí o no?

Una función **puede leer** una variable global, pero **no debería modificarla**. Lo que una función necesita lo recibe por **parámetros**, y lo que produce lo entrega con **`return`**.

### Ejemplo 4: sí, leer una constante global

Las **constantes globales** sí se permiten: se escriben en MAYÚSCULA para indicar que su valor nunca cambia. En Colombia, el IVA general es del 19 %:

```python
# Una funcion puede LEER una constante global

IVA = 0.19    # constante global: en MAYUSCULA, su valor nunca cambia

def calcular_precio_con_iva(precio):
    precio_con_iva = precio + precio * IVA
    return precio_con_iva

precio = calcular_precio_con_iva(5000)
print(f"Precio con IVA: {precio:.2f}")
```

```text
Precio con IVA: 5950.00
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Una%20funcion%20puede%20LEER%20una%20constante%20global%0A%0AIVA%20%3D%200.19%20%20%20%20%23%20constante%20global%3A%20en%20MAYUSCULA%2C%20su%20valor%20nunca%20cambia%0A%0Adef%20calcular_precio_con_iva%28precio%29%3A%0A%20%20%20%20precio_con_iva%20%3D%20precio%20%2B%20precio%20%2A%20IVA%0A%20%20%20%20return%20precio_con_iva%0A%0Aprecio%20%3D%20calcular_precio_con_iva%285000%29%0Aprint%28f%22Precio%20con%20IVA%3A%20%7Bprecio%3A.2f%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

La función no tiene ninguna variable local llamada `IVA`, así que Python la busca en el ámbito global y la encuentra. Leerla no causa ningún problema, porque nadie la modifica. Es lo mismo que se hizo con `CERO_ABSOLUTO` en la [sesión 24](../sesion_magistral-24/README.md#validar-el-dato-antes-de-llamar-a-la-función).

### Ejemplo 5: no, modificar una variable global con `global`

Ahora Apu quiere contar cuántas ventas hizo. Alguien agrega un contador global y lo modifica dentro de la función con la palabra `global`, que le dice a Python: "dentro de esta función, `ventas` es la variable global". El programa principal hace **una sola venta**:

```python
# NO recomendado: una funcion que MODIFICA una variable global

IVA = 0.19
ventas = 0

def calcular_precio_con_iva(precio):
    global ventas
    ventas = ventas + 1
    precio_con_iva = precio + precio * IVA
    return precio_con_iva

# Pruebas
assert round(calcular_precio_con_iva(10000), 2) == 11900.00
assert round(calcular_precio_con_iva(0), 2) == 0.00

# Programa principal: Apu hace UNA venta
precio = calcular_precio_con_iva(5000)
print(f"Precio con IVA: {precio:.2f}")
print("Ventas registradas:", ventas)
```

```text
Precio con IVA: 5950.00
Ventas registradas: 3
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20NO%20recomendado%3A%20una%20funcion%20que%20MODIFICA%20una%20variable%20global%0A%0AIVA%20%3D%200.19%0Aventas%20%3D%200%0A%0Adef%20calcular_precio_con_iva%28precio%29%3A%0A%20%20%20%20global%20ventas%0A%20%20%20%20ventas%20%3D%20ventas%20%2B%201%0A%20%20%20%20precio_con_iva%20%3D%20precio%20%2B%20precio%20%2A%20IVA%0A%20%20%20%20return%20precio_con_iva%0A%0A%23%20Pruebas%0Aassert%20round%28calcular_precio_con_iva%2810000%29%2C%202%29%20%3D%3D%2011900.00%0Aassert%20round%28calcular_precio_con_iva%280%29%2C%202%29%20%3D%3D%200.00%0A%0A%23%20Programa%20principal%3A%20Apu%20hace%20UNA%20venta%0Aprecio%20%3D%20calcular_precio_con_iva%285000%29%0Aprint%28f%22Precio%20con%20IVA%3A%20%7Bprecio%3A.2f%7D%22%29%0Aprint%28%22Ventas%20registradas%3A%22%2C%20ventas%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

¡Tres ventas! Las dos pruebas con `assert` también llamaron a la función, y cada llamada sumó una venta. Leyendo solo el programa principal no hay forma de saberlo: hay que revisar **todas** las llamadas a la función en todo el archivo. Por eso las variables globales que se modifican hacen que un programa sea difícil de entender y de depurar.

### Ejemplo 6: contar en el programa principal

La función vuelve a hacer **una sola cosa**, calcular el precio, y la venta se cuenta donde ocurre, en el programa principal:

```python
# Recomendado: la funcion solo calcula; el programa principal cuenta

IVA = 0.19

def calcular_precio_con_iva(precio):
    precio_con_iva = precio + precio * IVA
    return precio_con_iva

# Pruebas
assert round(calcular_precio_con_iva(10000), 2) == 11900.00
assert round(calcular_precio_con_iva(0), 2) == 0.00

# Programa principal: Apu hace UNA venta
ventas = 0
precio = calcular_precio_con_iva(5000)
ventas = ventas + 1
print(f"Precio con IVA: {precio:.2f}")
print("Ventas registradas:", ventas)
```

```text
Precio con IVA: 5950.00
Ventas registradas: 1
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Recomendado%3A%20la%20funcion%20solo%20calcula%3B%20el%20programa%20principal%20cuenta%0A%0AIVA%20%3D%200.19%0A%0Adef%20calcular_precio_con_iva%28precio%29%3A%0A%20%20%20%20precio_con_iva%20%3D%20precio%20%2B%20precio%20%2A%20IVA%0A%20%20%20%20return%20precio_con_iva%0A%0A%23%20Pruebas%0Aassert%20round%28calcular_precio_con_iva%2810000%29%2C%202%29%20%3D%3D%2011900.00%0Aassert%20round%28calcular_precio_con_iva%280%29%2C%202%29%20%3D%3D%200.00%0A%0A%23%20Programa%20principal%3A%20Apu%20hace%20UNA%20venta%0Aventas%20%3D%200%0Aprecio%20%3D%20calcular_precio_con_iva%285000%29%0Aventas%20%3D%20ventas%20%2B%201%0Aprint%28f%22Precio%20con%20IVA%3A%20%7Bprecio%3A.2f%7D%22%29%0Aprint%28%22Ventas%20registradas%3A%22%2C%20ventas%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

### Errores típicos de ámbito

Si no se respeta el ámbito, Python lo avisa con un error.

**Error 1: usar afuera una variable local.**

```python
# Error: usar afuera una variable local

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

calcular_subtotal(1500, 2)      # el resultado no se guarda
print(subtotal)
```

```text
Traceback (most recent call last):
  File "ej07_error_local_afuera.py", line 8, in <module>
    print(subtotal)
          ^^^^^^^^
NameError: name 'subtotal' is not defined
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Error%3A%20usar%20afuera%20una%20variable%20local%0A%0Adef%20calcular_subtotal%28precio%2C%20cantidad%29%3A%0A%20%20%20%20subtotal%20%3D%20precio%20%2A%20cantidad%0A%20%20%20%20return%20subtotal%0A%0Acalcular_subtotal%281500%2C%202%29%20%20%20%20%20%20%23%20el%20resultado%20no%20se%20guarda%0Aprint%28subtotal%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

`subtotal` solo existió dentro de la función, y desapareció cuando terminó. **Solución:** guardar el resultado, `subtotal = calcular_subtotal(1500, 2)`.

**Error 2: modificar una variable global sin `global`.**

```python
# Error: modificar una global dentro de una funcion, sin global

ventas = 0

def registrar_venta():
    ventas = ventas + 1
    return ventas

registrar_venta()
```

```text
Traceback (most recent call last):
  File "ej08_error_global_sin_global.py", line 9, in <module>
    registrar_venta()
  File "ej08_error_global_sin_global.py", line 6, in registrar_venta
    ventas = ventas + 1
             ^^^^^^
UnboundLocalError: cannot access local variable 'ventas' where it is not associated with a value
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Error%3A%20modificar%20una%20global%20dentro%20de%20una%20funcion%2C%20sin%20global%0A%0Aventas%20%3D%200%0A%0Adef%20registrar_venta%28%29%3A%0A%20%20%20%20ventas%20%3D%20ventas%20%2B%201%0A%20%20%20%20return%20ventas%0A%0Aregistrar_venta%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

Como la función **asigna** un valor a `ventas`, Python decide que `ventas` es una variable **local** de esa función. Entonces, para calcular `ventas + 1`, busca la `ventas` local, que todavía no tiene valor, y falla. Leer una global funciona (ejemplo 4); asignarle un valor dentro de una función, no. **Recomendación:** no usar `global`; contar en el programa principal, como en el ejemplo 6.

| Error | Causa | Solución |
|---|---|---|
| `NameError: name 'subtotal' is not defined` | Se usó fuera de la función una variable local | Guardar el valor devuelto: `subtotal = calcular_subtotal(...)` |
| `UnboundLocalError: cannot access local variable 'ventas' ...` | Se asignó un valor a una global dentro de una función | Recibir el dato por parámetro, devolver el resultado con `return` y hacer la cuenta en el programa principal |

## Parte 3 — Formas de pasar argumentos

Python permite dos formas de pasar argumentos a una función:

* **Por posición**: los argumentos se asignan en el mismo orden de los parámetros.
* **Por nombre**: se escribe `parametro=valor`, y el orden no importa.

### Ejemplo 9: por posición y por nombre

Esta función calcula el precio final de un producto: primero aplica el descuento y después el IVA. Tiene tres parámetros, y los tres son números:

```python
# Formas de pasar argumentos: por posicion y por nombre

def calcular_precio_final(precio, descuento, iva):
    precio_con_descuento = precio - precio * descuento
    precio_final = precio_con_descuento + precio_con_descuento * iva
    return precio_final

a = calcular_precio_final(10000, 0.10, 0.19)                       # por posicion
b = calcular_precio_final(precio=10000, descuento=0.10, iva=0.19)  # por nombre
c = calcular_precio_final(iva=0.19, precio=10000, descuento=0.10)  # por nombre, otro orden
d = calcular_precio_final(10000, descuento=0.10, iva=0.19)         # mezclados
e = calcular_precio_final(10000, 0.19, 0.10)                       # por posicion, EN DESORDEN
# f = calcular_precio_final(precio=10000, 0.10, 0.19)              # SyntaxError

print(f"a = {a:.2f}")
print(f"b = {b:.2f}")
print(f"c = {c:.2f}")
print(f"d = {d:.2f}")
print(f"e = {e:.2f}")
```

```text
a = 10710.00
b = 10710.00
c = 10710.00
d = 10710.00
e = 8910.00
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Formas%20de%20pasar%20argumentos%3A%20por%20posicion%20y%20por%20nombre%0A%0Adef%20calcular_precio_final%28precio%2C%20descuento%2C%20iva%29%3A%0A%20%20%20%20precio_con_descuento%20%3D%20precio%20-%20precio%20%2A%20descuento%0A%20%20%20%20precio_final%20%3D%20precio_con_descuento%20%2B%20precio_con_descuento%20%2A%20iva%0A%20%20%20%20return%20precio_final%0A%0Aa%20%3D%20calcular_precio_final%2810000%2C%200.10%2C%200.19%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20por%20posicion%0Ab%20%3D%20calcular_precio_final%28precio%3D10000%2C%20descuento%3D0.10%2C%20iva%3D0.19%29%20%20%23%20por%20nombre%0Ac%20%3D%20calcular_precio_final%28iva%3D0.19%2C%20precio%3D10000%2C%20descuento%3D0.10%29%20%20%23%20por%20nombre%2C%20otro%20orden%0Ad%20%3D%20calcular_precio_final%2810000%2C%20descuento%3D0.10%2C%20iva%3D0.19%29%20%20%20%20%20%20%20%20%20%23%20mezclados%0Ae%20%3D%20calcular_precio_final%2810000%2C%200.19%2C%200.10%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20por%20posicion%2C%20EN%20DESORDEN%0A%23%20f%20%3D%20calcular_precio_final%28precio%3D10000%2C%200.10%2C%200.19%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20SyntaxError%0A%0Aprint%28f%22a%20%3D%20%7Ba%3A.2f%7D%22%29%0Aprint%28f%22b%20%3D%20%7Bb%3A.2f%7D%22%29%0Aprint%28f%22c%20%3D%20%7Bc%3A.2f%7D%22%29%0Aprint%28f%22d%20%3D%20%7Bd%3A.2f%7D%22%29%0Aprint%28f%22e%20%3D%20%7Be%3A.2f%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

Las cuatro primeras llamadas son equivalentes. La quinta, `e`, pasa el IVA y el descuento **en desorden**: la función aplicó un descuento del 19 % y un IVA del 10 %. Python **no avisa**, porque los dos valores son números válidos; simplemente el resultado está mal. Cuando una función tiene varios parámetros del mismo tipo, pasar los argumentos **por nombre** evita este error.

Hay dos reglas al mezclar las dos formas:

| Llamada | Error | Regla |
|---|---|---|
| `calcular_precio_final(precio=10000, 0.10, 0.19)` | `SyntaxError: positional argument follows keyword argument` | Los argumentos por nombre van **después** de los posicionales. Como es un error de sintaxis, Python no ejecuta **ninguna** línea del archivo |
| `calcular_precio_final(10000, 0.10, 0.19, precio=5)` | `TypeError: calcular_precio_final() got multiple values for argument 'precio'` | Cada parámetro recibe **un solo** valor: aquí `precio` ya lo recibió por posición |

### Ejemplo 10: parámetros con valor por defecto

En la mayoría de las ventas no hay descuento y el IVA es el general. Un **valor por defecto** le da a un parámetro el valor que tendrá si se omite su argumento:

```python
# Parametros con valor por defecto

def calcular_precio_final(precio, descuento=0.0, iva=0.19):
    precio_con_descuento = precio - precio * descuento
    precio_final = precio_con_descuento + precio_con_descuento * iva
    return precio_final

a = calcular_precio_final(10000)               # sin descuento, IVA general
b = calcular_precio_final(10000, 0.10)         # 10 % de descuento, IVA general
c = calcular_precio_final(10000, iva=0.05)     # sin descuento, IVA del 5 %
d = calcular_precio_final(10000, 0.10, 0.0)    # 10 % de descuento, sin IVA

print(f"a = {a:.2f}")
print(f"b = {b:.2f}")
print(f"c = {c:.2f}")
print(f"d = {d:.2f}")
```

```text
a = 11900.00
b = 10710.00
c = 10500.00
d = 9000.00
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Parametros%20con%20valor%20por%20defecto%0A%0Adef%20calcular_precio_final%28precio%2C%20descuento%3D0.0%2C%20iva%3D0.19%29%3A%0A%20%20%20%20precio_con_descuento%20%3D%20precio%20-%20precio%20%2A%20descuento%0A%20%20%20%20precio_final%20%3D%20precio_con_descuento%20%2B%20precio_con_descuento%20%2A%20iva%0A%20%20%20%20return%20precio_final%0A%0Aa%20%3D%20calcular_precio_final%2810000%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20sin%20descuento%2C%20IVA%20general%0Ab%20%3D%20calcular_precio_final%2810000%2C%200.10%29%20%20%20%20%20%20%20%20%20%23%2010%20%25%20de%20descuento%2C%20IVA%20general%0Ac%20%3D%20calcular_precio_final%2810000%2C%20iva%3D0.05%29%20%20%20%20%20%23%20sin%20descuento%2C%20IVA%20del%205%20%25%0Ad%20%3D%20calcular_precio_final%2810000%2C%200.10%2C%200.0%29%20%20%20%20%23%2010%20%25%20de%20descuento%2C%20sin%20IVA%0A%0Aprint%28f%22a%20%3D%20%7Ba%3A.2f%7D%22%29%0Aprint%28f%22b%20%3D%20%7Bb%3A.2f%7D%22%29%0Aprint%28f%22c%20%3D%20%7Bc%3A.2f%7D%22%29%0Aprint%28f%22d%20%3D%20%7Bd%3A.2f%7D%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

| Llamada | `precio` | `descuento` | `iva` | Resultado |
|---|---|---|---|---|
| `calcular_precio_final(10000)` | `10000` | `0.0` (por defecto) | `0.19` (por defecto) | `11900.00` |
| `calcular_precio_final(10000, 0.10)` | `10000` | `0.10` | `0.19` (por defecto) | `10710.00` |
| `calcular_precio_final(10000, iva=0.05)` | `10000` | `0.0` (por defecto) | `0.05` | `10500.00` |
| `calcular_precio_final(10000, 0.10, 0.0)` | `10000` | `0.10` | `0.0` | `9000.00` |

Observe la llamada `c`: para cambiar el IVA **sin** dar un descuento, el único camino es pasar `iva` **por nombre**. Por posición, el segundo valor siempre llega a `descuento`.

`precio` no tiene valor por defecto, así que siempre hay que darlo:

| Código | Error | Regla |
|---|---|---|
| `calcular_precio_final()` | `TypeError: calcular_precio_final() missing 1 required positional argument: 'precio'` | Los parámetros sin valor por defecto son **obligatorios** |
| `def calcular_precio_final(descuento=0.0, precio, iva=0.19):` | `SyntaxError: non-default argument follows default argument` (en Python 3.12 o superior: `parameter without a default follows parameter with a default`) | Los parámetros con valor por defecto van **al final** |

## Parte 4 — Una función que llama a otra

Una función puede usar otras funciones. Apu quiere saber de cuántas formas puede armar un combo con 3 dulces distintos, si tiene 5 tipos de dulce. Eso son las **combinaciones** de 5 elementos tomados de 3 en 3:

$$
C(n, k) = \frac{n!}{k! \cdot (n - k)!}
$$

```python
# Una funcion que llama a otra: cada llamada tiene sus propias variables

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def combinaciones(n, k):
    formas = factorial(n) // (factorial(k) * factorial(n - k))
    return formas

resultado = combinaciones(5, 3)
print("Formas de elegir 3 dulces entre 5:", resultado)
```

```text
Formas de elegir 3 dulces entre 5: 10
```

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=%23%20Una%20funcion%20que%20llama%20a%20otra%3A%20cada%20llamada%20tiene%20sus%20propias%20variables%0A%0Adef%20factorial%28n%29%3A%0A%20%20%20%20fact%20%3D%201%0A%20%20%20%20for%20i%20in%20range%281%2C%20n%20%2B%201%29%3A%0A%20%20%20%20%20%20%20%20fact%20%3D%20fact%20%2A%20i%0A%20%20%20%20return%20fact%0A%0Adef%20combinaciones%28n%2C%20k%29%3A%0A%20%20%20%20formas%20%3D%20factorial%28n%29%20%2F%2F%20%28factorial%28k%29%20%2A%20factorial%28n%20-%20k%29%29%0A%20%20%20%20return%20formas%0A%0Aresultado%20%3D%20combinaciones%285%2C%203%29%0Aprint%28%22Formas%20de%20elegir%203%20dulces%20entre%205%3A%22%2C%20resultado%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

`combinaciones` llama **tres veces** a `factorial`. Cada llamada crea su propio recuadro con sus propias variables, que se apilan uno encima de otro: es la **pila de llamadas**. Cuando `factorial` termina, su recuadro desaparece y la ejecución vuelve al punto exacto de la línea 10 donde se hizo la llamada.

| Momento | Pila de llamadas (la última es la que se está ejecutando) | Devuelve |
|---|---|---|
| Se llama `combinaciones(5, 3)` | Global → `combinaciones` (`n = 5`, `k = 3`) | |
| Se calcula `factorial(n)` | Global → `combinaciones` (`n = 5`, `k = 3`) → `factorial` (`n = 5`) | `120` |
| Se calcula `factorial(k)` | Global → `combinaciones` (`n = 5`, `k = 3`) → `factorial` (`n = 3`) | `6` |
| Se calcula `factorial(n - k)` | Global → `combinaciones` (`n = 5`, `k = 3`) → `factorial` (`n = 2`) | `2` |
| `formas = 120 // (6 * 2)` | Global → `combinaciones` (`n = 5`, `k = 3`, `formas = 10`) | `10` |

Hay **cuatro** variables `n` distintas en esta ejecución: la de `combinaciones` y una por cada llamada a `factorial`. Ninguna interfiere con las otras, porque cada una vive en su propio recuadro.

Esto permite:

* **Reutilización**: `factorial` se escribe y se prueba una vez, y se usa donde se necesite.
* **Abstracción**: `combinaciones` solo necesita saber **qué** hace `factorial`, no **cómo** lo hace.

## Resumen de reglas

| Regla | Ejemplo |
|---|---|
| Cada llamada a una función tiene sus propias variables locales, que desaparecen al terminar | 1, 2, parte 4 |
| El parámetro recibe una copia del valor: cambiarlo no cambia la variable del programa principal | 1 |
| El resultado de una función sale con `return` y se guarda en una variable | 1, 3, error 1 |
| Una función puede leer una constante global (en MAYÚSCULA) | 4 |
| Una función no debería modificar una variable global: se cuenta y se acumula en el programa principal | 3, 5, 6, error 2 |
| Por posición importa el orden; por nombre, no | 9 |
| Los argumentos por nombre van después de los posicionales | 9 |
| Los parámetros con valor por defecto van al final, y su argumento se puede omitir | 10 |

## Ejercicios de práctica: prediga la salida

Para cada programa, escriba en papel lo que cree que muestra en pantalla. Después abra la solución y compruébelo en Python Tutor.

### Ejercicio 1

```python
def duplicar(x):
    x = x * 2
    return x

x = 7
duplicar(x)
print(x)
```

<details>
<summary>Solución</summary>

```text
7
```

`duplicar` cambia su `x` **local** a `14` y la devuelve, pero el valor devuelto no se guarda en ninguna variable. La `x` global sigue valiendo `7`. Para que cambie habría que escribir `x = duplicar(x)`.

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=def%20duplicar%28x%29%3A%0A%20%20%20%20x%20%3D%20x%20%2A%202%0A%20%20%20%20return%20x%0A%0Ax%20%3D%207%0Aduplicar%28x%29%0Aprint%28x%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

</details>

### Ejercicio 2

```python
total = 100

def gastar(valor):
    total = 50
    return total - valor

print(gastar(20))
print(total)
```

<details>
<summary>Solución</summary>

```text
30
100
```

Dentro de `gastar`, la asignación `total = 50` crea una variable **local** `total`; la global no se toca. La función devuelve `50 - 20 = 30`, y la `total` global sigue en `100`.

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=total%20%3D%20100%0A%0Adef%20gastar%28valor%29%3A%0A%20%20%20%20total%20%3D%2050%0A%20%20%20%20return%20total%20-%20valor%0A%0Aprint%28gastar%2820%29%29%0Aprint%28total%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

</details>

### Ejercicio 3

```python
def calcular_cambio(pago, precio=1000):
    return pago - precio

print(calcular_cambio(5000))
print(calcular_cambio(5000, 3500))
print(calcular_cambio(precio=200, pago=1000))
```

<details>
<summary>Solución</summary>

```text
4000
1500
800
```

* `calcular_cambio(5000)`: `precio` toma su valor por defecto, `1000`.
* `calcular_cambio(5000, 3500)`: `precio` recibe `3500` por posición.
* `calcular_cambio(precio=200, pago=1000)`: por nombre, el orden no importa; es `1000 - 200`.

[▶ Ver paso a paso en Python Tutor](https://pythontutor.com/visualize.html#code=def%20calcular_cambio%28pago%2C%20precio%3D1000%29%3A%0A%20%20%20%20return%20pago%20-%20precio%0A%0Aprint%28calcular_cambio%285000%29%29%0Aprint%28calcular_cambio%285000%2C%203500%29%29%0Aprint%28calcular_cambio%28precio%3D200%2C%20pago%3D1000%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

</details>

### Ejercicio 4

Estos dos programas se parecen mucho. ¿Cuál funciona y cuál produce un error? ¿Por qué?

**Programa A:**

```python
saldo = 500

def mostrar_saldo():
    print("Saldo:", saldo)

mostrar_saldo()
```

**Programa B:**

```python
saldo = 500

def retirar(valor):
    saldo = saldo - valor
    return saldo

retirar(100)
```

<details>
<summary>Solución</summary>

El programa A funciona:

```text
Saldo: 500
```

El programa B produce un error:

```text
Traceback (most recent call last):
  File "p4b.py", line 7, in <module>
    retirar(100)
  File "p4b.py", line 4, in retirar
    saldo = saldo - valor
            ^^^^^
UnboundLocalError: cannot access local variable 'saldo' where it is not associated with a value
```

`mostrar_saldo` solo **lee** la global `saldo`, y eso está permitido. `retirar` **asigna** un valor a `saldo`, así que Python la trata como local, y al calcular `saldo - valor` la `saldo` local todavía no tiene valor. Es el error 2 de la parte 2. La forma correcta es recibir el saldo por parámetro y devolver el nuevo saldo:

```python
def retirar(saldo, valor):
    nuevo_saldo = saldo - valor
    return nuevo_saldo

saldo = 500
saldo = retirar(saldo, 100)
print("Saldo:", saldo)       # Saldo: 400
```

[▶ Programa A en Python Tutor](https://pythontutor.com/visualize.html#code=saldo%20%3D%20500%0A%0Adef%20mostrar_saldo%28%29%3A%0A%20%20%20%20print%28%22Saldo%3A%22%2C%20saldo%29%0A%0Amostrar_saldo%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) · [▶ Programa B en Python Tutor](https://pythontutor.com/visualize.html#code=saldo%20%3D%20500%0A%0Adef%20retirar%28valor%29%3A%0A%20%20%20%20saldo%20%3D%20saldo%20-%20valor%0A%20%20%20%20return%20saldo%0A%0Aretirar%28100%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

</details>

## Para explorar por su cuenta

Esta sección no se vio en clase.

* **Visualice sus propios programas.** En [pythontutor.com](https://pythontutor.com), elija *Python* y pegue cualquier programa del curso que tenga funciones. Si un programa usa `input()`, Python Tutor le pedirá los datos en un cuadro de texto. Es una buena forma de revisar la [nómina](../../6/sesion_magistral-11/README.md) o los ejercicios del [laboratorio 3](../../../laboratorios/3/README.md) ahora que sabe escribir funciones.
* **Lectura complementaria.** El Libro de Python explica, con otros ejemplos, los argumentos [por posición](https://ellibrodepython.com/funciones-en-python#argumentos-por-posición), [por nombre](https://ellibrodepython.com/funciones-en-python#argumentos-por-nombre) y [por defecto](https://ellibrodepython.com/funciones-en-python#argumentos-por-defecto). La misma página presenta argumentos de longitud variable (`*args`) y anotaciones de tipo, que **no** se usan en este curso.

## Lo que quedó pendiente

El diseño **top-down** no alcanzó a verse en esta sesión: dividir un problema grande en subproblemas, el árbol de funciones y la construcción del programa de arriba hacia abajo con *stubs*. Está resumido en la [teoría de la clase 10](../teoria/README.md), y los archivos que lo muestran paso a paso están en el [índice del código](../teoria/codigo/README.md): `temperaturas_topdown_paso1.py` y `temperaturas_topdown_paso2.py`. El ejercicio guiado [adivina el número](../teoria/codigo/adivina_numero/README.md) lo aplica de principio a fin.

## Archivos

| Archivo | Descripción |
|---|---|
| [`codigo/ej01_mismo_nombre.py`](codigo/ej01_mismo_nombre.py) | Ejemplo 1: el mismo nombre en dos ámbitos |
| [`codigo/ej02_vida_local.py`](codigo/ej02_vida_local.py) | Ejemplo 2: una variable local no recuerda entre llamadas |
| [`codigo/ej03_acumular_afuera.py`](codigo/ej03_acumular_afuera.py) | Ejemplo 3: acumular en el programa principal |
| [`codigo/ej04_constante_global.py`](codigo/ej04_constante_global.py) | Ejemplo 4: leer una constante global |
| [`codigo/ej05_global_modificada.py`](codigo/ej05_global_modificada.py) | Ejemplo 5: modificar una global con `global` (no recomendado) |
| [`codigo/ej06_contar_afuera.py`](codigo/ej06_contar_afuera.py) | Ejemplo 6: contar en el programa principal |
| [`codigo/ej07_error_local_afuera.py`](codigo/ej07_error_local_afuera.py) | Error 1: `NameError` |
| [`codigo/ej08_error_global_sin_global.py`](codigo/ej08_error_global_sin_global.py) | Error 2: `UnboundLocalError` |
| [`codigo/ej09_formas_de_pasar_argumentos.py`](codigo/ej09_formas_de_pasar_argumentos.py) | Ejemplo 9: argumentos por posición y por nombre |
| [`codigo/ej10_valores_por_defecto.py`](codigo/ej10_valores_por_defecto.py) | Ejemplo 10: parámetros con valor por defecto |
| [`codigo/ej11_funcion_llama_a_otra.py`](codigo/ej11_funcion_llama_a_otra.py) | Parte 4: una función que llama a otra y la pila de llamadas |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase 10 y de las indicaciones del docente sobre lo visto en clase. Los ejemplos son una variación de los de las diapositivas. El docente revisó y validó la versión final.
