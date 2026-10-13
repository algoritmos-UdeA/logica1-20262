![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Taller 2 — Estructuras condicionales y ciclos

> [!important]
> **Autoría y fuentes:** este taller es una recopilación. Su base es un taller de ciclos que el docente del curso preparó en 2022, y la mayoría de sus enunciados vienen de los libros de **Efraín Alberto Oviedo**, *Lógica de Programación*, y de **Joyce Farrell**, *Introducción a la programación lógica y diseño* (7a ed., Cengage Learning, 2013). Los enunciados pertenecen a sus autores; aquí solo se transcribieron, se precisaron algunos datos que faltaban para poder resolverlos y se agregaron casos de prueba, pistas y preguntas de reflexión de acuerdo con la notación vista en clase. La tabla [Fuentes de los ejercicios](#fuentes-de-los-ejercicios) indica el origen de cada uno.

Este taller sirve de repaso para el parcial de **estructuras de control**: condicionales (clases 5 y 6) y ciclos `Mientras`/`while` y `Para`/`for` (clases 7 y 8).

## Cómo trabajar cada problema

En los problemas de las secciones 2 a 5, siga el ciclo usado en los laboratorios:

1. **Entender:** identifique entradas, salidas y proceso.
2. **Diseñar a mano:** escriba el pseudocódigo o diagrama de flujo y haga la **prueba de escritorio** con al menos uno de los casos de prueba.
3. **Implementar y verificar:** codifique en Python y compare la salida con los casos de prueba. Si no coincide, decida primero si el error está en el algoritmo, en la predicción o en el código.

Los casos de prueba **no son los únicos posibles**: agregue los suyos, sobre todo los casos límite (el valor exacto donde cambia una condición, `N = 0`, ningún dato antes del centinela, etc.).

---

## 1. Prueba de escritorio

Realice la prueba de escritorio de cada código **a mano, sin la ayuda del computador**. Haga una tabla con una columna por variable (en el orden en que aparecen) y anote la salida. Al terminar, puede comprobar su resultado ejecutando el código o simulándolo en [Python Tutor](https://pythontutor.com/).

### 1.1 Condicionales

**Código 1.** Haga la prueba de escritorio para cada uno de estos pares de valores: `(x, y) = (7, 3)`, `(7, 8)`, `(2, 3)` y `(5, 6)`.

```python
x = 7
y = 3
if x > 5 and y > 5:
    z = x + y
elif x > 5 or y > 5:
    z = x - y
else:
    z = x * y
print(z)
```

**Código 2.** Haga la prueba de escritorio para `n = 9`, `n = 10`, `n = 15` y `n = 7`.

```python
n = 9
mensaje = ""
if n % 3 == 0:
    mensaje = mensaje + "Fizz"
if n % 5 == 0:
    mensaje = mensaje + "Buzz"
if mensaje == "":
    print(n)
else:
    print(mensaje)
```

**Código 3.** Es el mismo código 2, pero con `elif` en la segunda condición. Repita la prueba con los mismos cuatro valores de `n`.

```python
n = 9
mensaje = ""
if n % 3 == 0:
    mensaje = mensaje + "Fizz"
elif n % 5 == 0:
    mensaje = mensaje + "Buzz"
if mensaje == "":
    print(n)
else:
    print(mensaje)
```

> **Pregunta para pensar:** ¿para cuál valor de `n` los códigos 2 y 3 dan resultados distintos? ¿Por qué? ¿Cuándo dos `if` seguidos **no** son equivalentes a un `if`-`elif`?

### 1.2 Ciclo `while`

**Código 4.** Variables: `a`, `b`, `c`.

```python
a = 1
b = 2
c = 5
while a < c:
    a = a + 1
    b = b + c
print(a, b, c)
```

**Código 5.** Variables: `d`, `e`, `f`.

```python
d = 4
e = 6
f = 7
while d > f:
    d = d + 1
    e = e - 1
print(d, e, f)
```

**Código 6.** Variables: `g`, `h`.

```python
g = 4
h = 6
while g < h:
    g = g + 1
print(g, h)
```

**Código 7.** Variables: `j`, `k`, `m`, `n`.

```python
j = 2
k = 5
n = 9
while j < k:
    m = 6
    while m < n:
        print("Adiós")
        m = m + 1
    j = j + 1
```

**Código 8.** Variables: `j`, `k`, `m`, `n`.

```python
j = 2
k = 5
m = 6
n = 9
while j < k:
    while m < n:
        print("Hola")
        m = m + 1
    j = j + 1
```

> **Pregunta para pensar:** los códigos 7 y 8 solo se diferencian en **dónde** está la instrucción `m = 6`. ¿Cuántas veces imprime cada uno? ¿Por qué? (Compare con el consejo 4 de la [sesión 21](../../clases/8/sesion_magistral-21/README.md#consejos-para-usar-contadores-banderas-y-acumuladores-en-ciclos-anidados)).

**Código 9.** Variables: `p`, `q`, `r`.

```python
p = 2
q = 4
while p < q:
    print("Adiós")
    r = 1
    while r < q:
        print("Adiós")
        r = r + 1
    p = p + 1
```

### 1.3 Ciclo `for` y ruptura de ciclos

**Código 10.** Variables: `i`, `s`.

```python
s = 0
for i in range(10, 0, -3):
    s = s + i
    print(i, s)
print("Final:", s)
```

**Código 11.** Variables: `i`, `j`. Recuerde que `print(..., end=" ")` no salta de línea y que `print()` solo salta de línea.

```python
for i in range(1, 4):
    for j in range(i, 4):
        print(i * j, end=" ")
    print()
```

**Código 12.** Haga la prueba de escritorio para `n = 12`, `n = 35` y `n = 13`. Variables: `n`, `d`.

```python
n = 12
d = 2
while d < n:
    if n % d == 0:
        break
    d = d + 1
print(d)
```

> **Pregunta para pensar:** ¿qué representa el valor que imprime el código 12? ¿Qué pasa cuando `n` es primo?

---

## 2. Estructuras condicionales

**2.1** Un almacén de escritorios hace los siguientes descuentos: si el cliente compra menos de 5 unidades se le da un descuento del 10% sobre la compra; si el número de unidades es mayor o igual a 5 pero menor que 10, se le otorga un 20%, y si son 10 o más se le da un 40%. Haga un algoritmo que determine cuánto debe pagar un cliente si el valor de cada escritorio es de $800.000.

| Unidades | Total a pagar |
|---|---|
| 3 | $2.160.000 |
| 5 | $3.200.000 |
| 9 | $5.760.000 |
| 10 | $4.800.000 |

> **Pregunta para pensar:** según la tabla, comprar 10 escritorios sale más barato que comprar 9. ¿Es un error del algoritmo o de la política de descuentos?

**2.2** Una frutería ofrece las manzanas con descuento según la siguiente tabla:

| N.º de manzanas compradas | Descuento |
|---|---|
| 0 – 2 | 0% |
| 3 – 5 | 10% |
| 6 – 10 | 15% |
| 11 en adelante | 20% |

Determine cuánto pagará una persona que compre manzanas en esa frutería. El precio de cada manzana es un dato de entrada.

| Manzanas | Precio por manzana | Total a pagar |
|---|---|---|
| 2 | $1.000 | $2.000 |
| 3 | $1.000 | $2.700 |
| 6 | $1.000 | $5.100 |
| 10 | $1.000 | $8.500 |
| 11 | $1.000 | $8.800 |

**2.3** Haga un algoritmo que determine cuál es el mayor en un grupo de cuatro datos diferentes.

> [!Tip]
> **Pista:** en el laboratorio 2 se resolvió el mayor de **tres** números. Compare dos estrategias: anidar las comparaciones, o guardar en una variable `mayor` el mejor valor visto hasta el momento y compararlo con cada dato siguiente. ¿Cuál crece mejor si fueran 10 datos?

**2.4** Haga un algoritmo que determine la suma del valor menor y el valor mayor en un grupo de 4 datos.

| Datos | Mayor | Menor | Suma |
|---|---|---|---|
| 7, 2, 9, 4 | 9 | 2 | 11 |
| -3, 5, 0, 1 | 5 | -3 | 2 |
| 6, 6, 6, 6 | 6 | 6 | 12 |

**2.5** Haga un algoritmo que lea la abscisa (`X`) y la ordenada (`Y`) de un punto del plano cartesiano y determine si pertenece o no a la recta `Y = 3X + 5`. Suponga que las coordenadas son números enteros.

| X | Y | ¿Pertenece? |
|---|---|---|
| 1 | 8 | Sí |
| -2 | -1 | Sí |
| 0 | 4 | No |

> **Pregunta para pensar:** ¿por qué se pide que las coordenadas sean enteras? Pruebe en Python `0.1 + 0.2 == 0.3`.

**2.6** Elabore un algoritmo que lea un punto `(x, y)` y diga si está o no en el área determinada por la parábola `Y = 4 - X²` y la recta `Y = X - 3`. Considere que los puntos del borde están dentro del área.

> [!Tip]
> **Pista:** haga primero un dibujo. Entre los dos puntos de corte, la parábola queda por encima de la recta, así que un punto está en el área si su `y` está **entre** las dos curvas evaluadas en su `x`.

| Punto | ¿Está en el área? |
|---|---|
| (0, 0) | Sí |
| (0, 5) | No |
| (3, -5) | No |
| (2, -0.5) | Sí |
| (-3, -6) | Sí (está en el borde) |

**2.7** Elabore un algoritmo que lea el par ordenado `(A, B)` y determine si está o no en el área comprendida entre las rectas `Y = 2X - 2`, `Y = X + 1` y `X = 20`. Considere que los puntos del borde están dentro del área.

| Punto (A, B) | ¿Está en el área? |
|---|---|
| (10, 15) | Sí |
| (10, 20) | No |
| (25, 30) | No |
| (2, 3) | No |
| (3, 4) | Sí (es el vértice donde se cortan las dos rectas) |

**2.8** Un proveedor de computadores ofrece un descuento del 10% si el computador cuesta $1.000.000 o más. Además, independientemente, ofrece un 5% de descuento si la marca es ABACO. Determine cuánto pagará un cliente por la compra de un computador, con IVA incluido. Suponga que ambos descuentos se calculan sobre el precio original y que el IVA (19%) se aplica después de los descuentos.

| Precio | Marca | Total a pagar |
|---|---|---|
| $2.000.000 | ABACO | $2.023.000 |
| $800.000 | ABACO | $904.400 |
| $1.000.000 | Otra | $1.071.000 |
| $500.000 | Otra | $595.000 |

> **Pregunta para pensar:** la palabra "independientemente" indica que los dos descuentos pueden aplicarse a la vez. ¿Qué pasaría con el primer caso de prueba si usara `if`-`elif` en lugar de dos `if` separados? (Compare con los códigos 2 y 3 de la sección 1).

**2.9** Determine el precio de un pasaje de ida y vuelta en avión, conociendo la distancia del viaje (solo ida) y el número de días de estancia. Si la distancia es superior a 1.000 km **y** el número de días de estancia es superior a 7, la aerolínea hace un descuento del 30%. El precio por kilómetro es de $89,50.

| Distancia (km) | Días | Precio |
|---|---|---|
| 1200 | 10 | $150.360 |
| 1200 | 7 | $214.800 |
| 800 | 10 | $143.200 |
| 1000 | 15 | $179.000 |

**2.10** En un juego de preguntas que se responden "SI" o "NO", gana quien responda correctamente las tres preguntas. Si se responde mal cualquiera de ellas, ya no se hace la siguiente y el juego termina. Las preguntas son:

1. ¿En Python, `range(1, 5)` incluye el número 5? (respuesta correcta: NO)
2. ¿El ciclo `Mientras` puede ejecutarse cero veces? (respuesta correcta: SI)
3. ¿En Python, `7 // 2` da como resultado `3`? (respuesta correcta: SI)

El programa debe indicar si el jugador ganó o en qué pregunta perdió.

> [!Tip]
> **Pista:** "ya no se hace la siguiente" significa que la segunda pregunta solo se lee **dentro** del camino donde la primera fue correcta. Es un caso de anidamiento real, no de condiciones independientes.

**2.11** Cierta universidad tiene un programa para estimular a los estudiantes con buen rendimiento académico:

| Nivel | Promedio | Créditos | Descuento |
|---|---|---|---|
| Pregrado | 4,5 o más | 28 | 25% |
| Pregrado | mayor o igual a 4,0 y menor que 4,5 | 25 | 10% |
| Pregrado | mayor que 3,5 y menor que 4,0 | 20 | 0% |
| Pregrado | mayor o igual a 2,5 y menor que 3,5 | 15 | 0% |
| Pregrado | menor que 2,5 | no puede matricularse | — |
| Posgrado | 4,5 o más | 20 | 20% |
| Posgrado | menor que 4,5 | 10 | 0% |

Haga un algoritmo que determine cuánto debe pagar un estudiante y cuántos créditos registra, si el valor de cada crédito es de $50.000 para pregrado y $300.000 para posgrado.

| Nivel | Promedio | Créditos | Total a pagar |
|---|---|---|---|
| Pregrado | 4,7 | 28 | $1.050.000 |
| Pregrado | 4,2 | 25 | $1.125.000 |
| Pregrado | 3,7 | 20 | $1.000.000 |
| Pregrado | 3,0 | 15 | $750.000 |
| Pregrado | 2,0 | — | No puede matricularse |
| Posgrado | 4,6 | 20 | $4.800.000 |
| Posgrado | 4,0 | 10 | $3.000.000 |

> **Pregunta para pensar:** ¿qué debería pasar con un estudiante de pregrado con promedio exactamente **3,5**? Revise la tabla con cuidado. ¿Qué hace su programa en ese caso? ¿Cómo corregiría el enunciado?

### Para explorar por su cuenta

Se tienen cuatro esferas (A, B, C, D), de las cuales se sabe que tres son de igual peso y una es diferente. Elabore un algoritmo que determine cuál es la esfera diferente y si es de mayor o menor peso. Este acertijo aparece **resuelto** en el capítulo 4 del libro de Oviedo (ejercicio resuelto N.º 15): inténtelo primero y luego compare su solución con la del libro.

---

## 3. Ciclos con contadores y acumuladores

**3.1** Un vendedor desea calcular la comisión total sobre la venta de varios artículos. Al vendedor le corresponde el 10% de comisión sobre los artículos cuyo precio es menor o igual a $1.000 y el 7% sobre aquellos cuyo precio es mayor de $1.000. Elabore un algoritmo para obtener la comisión total, si se sabe que el vendedor hizo `N` ventas.

| N | Precios | Comisión total |
|---|---|---|
| 3 | 500, 1000, 2000 | $290 |
| 0 | — | $0 |

**3.2** En un curso se practican 4 evaluaciones con los siguientes porcentajes: 25%, 20%, 25% y 30%, respectivamente. Para cada uno de los `N` estudiantes se informa el código y las cuatro notas. Haga un algoritmo que calcule la nota definitiva de cada estudiante, el promedio de notas definitivas del curso y el porcentaje de estudiantes que perdieron (definitiva menor que 3,0).

| Código | Notas | Definitiva |
|---|---|---|
| 101 | 4.0, 3.5, 3.0, 4.5 | 3.80 |
| 102 | 2.0, 3.0, 2.0, 3.0 | 2.50 |
| 103 | 5.0, 4.0, 3.0, 1.0 | 3.10 |

Resultado del curso: promedio `3.13`, porcentaje de perdedores `33.33%`.

**3.3** Se tiene la siguiente información de cada uno de los `N` estudiantes de una universidad:

* Edad.
* Género (1: hombre; 2: mujer).
* Carrera (1: ingeniería; 2: otra carrera).

Haga un algoritmo que obtenga:

* El promedio de edad de los estudiantes de ingeniería.
* El porcentaje de hombres en la universidad.
* El porcentaje de mujeres que estudian ingeniería (respecto al total de mujeres).

| Edad | Género | Carrera |
|---|---|---|
| 18 | 1 | 1 |
| 20 | 2 | 1 |
| 22 | 2 | 2 |
| 19 | 1 | 2 |
| 25 | 2 | 1 |

Resultado esperado: promedio de edad en ingeniería `21.00`, porcentaje de hombres `40.00%`, porcentaje de mujeres en ingeniería `66.67%`.

> [!Tip]
> **Pista:** cada porcentaje y cada promedio es una división. ¿Qué pasa si no hay estudiantes de ingeniería, o si no hay mujeres? Proteja cada división como en la [sesión 13](../../clases/7/sesion_magistral-13/README.md).

**3.4** Cada uno de cuatro atletas desea saber si ha bajado o subido de peso desde la última vez que se pesó. Para esto, cada uno se pesa cinco veces, calcula el promedio de su peso actual y lo compara con el peso anterior. Haga un algoritmo que determine para cada atleta si bajó de peso, subió de peso o está estable, y cuánto es el cambio de peso en caso de que exista diferencia respecto al peso anterior.

| Peso anterior | Cinco pesadas | Promedio actual | Resultado |
|---|---|---|---|
| 70 | 70, 71, 69, 70, 70 | 70.00 | Estable |
| 80 | 78, 79, 78.5, 79.5, 78 | 78.60 | Bajó 1.40 |
| 60 | 61, 62, 61.5, 60.5, 62 | 61.40 | Subió 1.40 |

> [!Tip]
> **Pista:** este es un problema de **ciclos anidados**: un ciclo externo para los atletas y uno interno para las pesadas. ¿En cuál de los dos se debe poner en cero el acumulador de pesos? Muestre los decimales con `:.2f`: al restar números con decimales, Python puede mostrar resultados como `-1.4000000000000057`.

**3.5** Se tienen `N` registros de vehículos, cada uno con:

* Tipo (1: carro; 2: moto; 3: bus).
* Combustible (1: gasolina; 2: diésel; 3: eléctrico).
* Antigüedad (en años).

Haga un algoritmo que obtenga:

* El número de carros eléctricos.
* El total de vehículos a gasolina.
* El número de motos diésel con menos de 5 años de antigüedad.
* El número de buses eléctricos.
* El total de vehículos diésel.
* El número de motos a gasolina con menos de 10 años de antigüedad.

| Tipo | Combustible | Antigüedad |
|---|---|---|
| 1 | 3 | 2 |
| 3 | 3 | 8 |
| 2 | 2 | 3 |
| 2 | 1 | 12 |
| 1 | 1 | 1 |
| 3 | 2 | 6 |
| 2 | 1 | 7 |

Resultado esperado, en el orden de la lista: `1`, `3`, `1`, `1`, `2`, `1`.

---

## 4. Centinela, validación y búsqueda de extremos

**4.1** Yabe Online Auctions requiere que sus vendedores publiquen los artículos para la venta por un periodo de seis semanas, durante el cual el precio de cualquier artículo no vendido baja 12% cada semana. Por ejemplo, uno que cuesta 10 dólares durante la primera semana cuesta 12% menos, u 8.80 dólares, durante la segunda semana. Durante la tercera, el mismo artículo cuesta 12% menos que 8.80, o 7.74 dólares. Diseñe una aplicación que permita a un usuario introducir precios hasta que se introduzca un valor centinela apropiado. La salida del programa es el precio de cada artículo durante cada semana, de la uno a la seis.

| Precio inicial | Semanas 1 a 6 |
|---|---|
| 10 | 10.00, 8.80, 7.74, 6.81, 6.00, 5.28 |
| 25 | 25.00, 22.00, 19.36, 17.04, 14.99, 13.19 |

> **Pregunta para pensar:** ¿qué valor centinela es "apropiado" para un precio? ¿Por qué `0` o un número negativo sirven y `10` no?

**4.2** Diseñe un programa para la Hollywood Movie Rating Guide, que pueda instalarse en un quiosco en los cines. Cada cliente del cine introduce un valor de 0 a 4 indicando el número de estrellas con las que califica la película de la semana. Si un usuario introduce un valor que no está en el rango correcto, se le vuelve a pedir, cuantas veces sea necesario, hasta que introduzca un valor correcto. El programa se ejecuta en forma continua hasta que el gerente del cine introduce un número negativo para salir. Al final, despliegue la calificación promedio de la película.

| Valores introducidos (en orden) | Salida esperada |
|---|---|
| 4, 3, 7, 2, -1 | El 7 se rechaza y se vuelve a pedir; promedio `3.00` |
| -1 | Un mensaje indicando que no hubo calificaciones |

> [!Tip]
> **Pista:** hay **dos** ciclos: uno externo controlado por el centinela (número negativo) y uno interno de validación (valores mayores que 4). ¿Cuál condición se revisa primero?

**4.3** Un restaurante paga a sus meseros dos clases de comisiones:

* Una comisión del 7% sobre toda venta.
* Otra comisión que depende del tipo de venta: 15% si la venta es de contado, 10% si se hizo en cheque y 5% si se hizo con tarjeta de crédito.

El restaurante tiene, por cada venta:

* Identificación del mesero (1, 2, 3).
* Tipo de venta (1: contado; 2: cheque; 3: tarjeta).
* Cuantía de la venta.

Elabore un algoritmo que obtenga el total a pagar a cada uno de los tres meseros. Las ventas se leen hasta que se introduzca `0` como identificación del mesero.

| Mesero | Tipo | Cuantía |
|---|---|---|
| 1 | 1 | 100000 |
| 2 | 3 | 200000 |
| 1 | 2 | 50000 |
| 3 | 1 | 80000 |
| 0 | — | — |

Resultado esperado: mesero 1 `$30.500`, mesero 2 `$24.000`, mesero 3 `$17.600`.

**4.4** Una empresa tiene un número variable de empleados y de cada uno de ellos tiene la siguiente información:

* Código.
* Nombre.
* Número de hijos.
* Salario por hora.
* Número de horas trabajadas en el mes.

El devengado es el salario por hora multiplicado por las horas trabajadas. La retención se determina así:

* Si el empleado tiene más de 6 hijos, no hay retención.
* Si el devengado es menor de $300.000 (y tiene 6 hijos o menos), se le retiene un porcentaje igual a `(6 - hijos) / 2`.
* Si el devengado es igual o mayor a $300.000 (y tiene 6 hijos o menos): si tiene menos de 3 hijos, se le retiene un 3%; si tiene 3 hijos o más, se le retiene un porcentaje igual a `10 / hijos`.

El subsidio por cada hijo es de $1.200. Elabore un algoritmo que muestre, para cada empleado: código, nombre, devengado, retención, subsidio y total a pagar (devengado − retención + subsidio). Los datos se leen hasta que se introduzca `0` como código.

| Código | Nombre | Hijos | Salario/hora | Horas | Devengado | Retención | Subsidio | Total |
|---|---|---|---|---|---|---|---|---|
| 1 | Ana | 2 | 2000 | 100 | 200000 | 4000 (2%) | 2400 | 198400 |
| 2 | Luis | 4 | 5000 | 160 | 800000 | 20000 (2.5%) | 4800 | 784800 |
| 3 | Marta | 0 | 4000 | 100 | 400000 | 12000 (3%) | 0 | 388000 |
| 4 | Pedro | 7 | 1500 | 100 | 150000 | 0 (0%) | 8400 | 158400 |

> **Pregunta para pensar:** en la versión original del enunciado, la regla decía "un porcentaje igual a 6 menos el número de hijos dividido por 2". ¿De qué dos formas se puede leer esa frase? ¿Qué porcentaje le retendrían a Ana con cada lectura? ¿Por qué se escribió aquí con paréntesis?

**4.5** Varias ambulancias recorren la ciudad. Cuando la CENTRAL recibe una llamada, se informa la ubicación de la emergencia mediante coordenadas, lo mismo que la ubicación de todas las ambulancias. La CENTRAL es el punto `(0, 0)`, u origen de coordenadas, y se sabe que hay `N` ambulancias en servicio. Elabore un algoritmo que, dada la información necesaria, informe las coordenadas de la ambulancia más cercana al punto de emergencia.

> [!Tip]
> **Pista:** use la fórmula de la distancia entre dos puntos, $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$. La raíz cuadrada se puede calcular con `** 0.5` o con `math.sqrt` (visto en la clase 10). Pregunta extra: ¿hace falta calcular la raíz para saber cuál ambulancia está más cerca?

| Emergencia | Ambulancias | Más cercana |
|---|---|---|
| (3, 4) | (0, 0), (5, 5), (2, 3), (10, 1) | (2, 3), a una distancia de 1.41 |

**4.6** Se tienen `N` registros, cada uno con 4 valores que corresponden a las longitudes de las patas de una mesa. Elabore un algoritmo que chequee si con los cuatro valores de cada registro se puede fabricar una mesa no coja de cuatro patas (las cuatro patas iguales) o, si no se puede, una mesa no coja de tres patas (al menos tres patas iguales). El algoritmo debe mostrar el número de mesas de cuatro y de tres patas que se pueden formar, y la cantidad total de patas sobrantes.

| Registro | Resultado | Patas sobrantes |
|---|---|---|
| 70, 70, 70, 70 | Mesa de 4 patas | 0 |
| 70, 70, 70, 68 | Mesa de 3 patas | 1 |
| 70, 68, 66, 70 | Ninguna mesa | 4 |
| 65, 70, 65, 65 | Mesa de 3 patas | 1 |

Resultado esperado: `1` mesa de cuatro patas, `2` mesas de tres patas y `6` patas sobrantes.

> [!Tip]
> **Pista:** con cuatro patas `a`, `b`, `c`, `d`, hay solo cuatro formas de escoger tres: `abc`, `abd`, `acd` y `bcd`.

**4.7** Para cada uno de `N` estudiantes se tiene la nota obtenida en una materia. Haga un algoritmo que obtenga la nota máxima, la nota mínima, cuántos ganaron y cuántos perdieron la materia (se gana con 3,0 o más).

| Notas | Máxima | Mínima | Ganaron | Perdieron |
|---|---|---|---|---|
| 3.5, 4.8, 2.0, 3.0 | 4.8 | 2.0 | 3 | 1 |

> [!NOTE]
> Este problema es el Ejemplo 9 de la clase 8, resuelto en la [sesión 20](../../clases/8/sesion_magistral-20/README.md). Intente resolverlo sin mirar y luego compare cómo inicializó la máxima y la mínima con las dos formas de esa sesión.

### Para explorar por su cuenta

Modifique el programa del ejercicio 4.2 para que un usuario tenga **tres intentos** para introducir una calificación válida. Después de tres entradas incorrectas, el programa emite un mensaje apropiado y continúa con un usuario nuevo (Farrell, cap. 5, ejercicio 13b).

---

## 5. Series y sucesiones

**5.1** Escriba un algoritmo que lea un número entero `N` y calcule el resultado de la serie:

$$1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots \pm \frac{1}{N}$$

| N | Resultado |
|---|---|
| 1 | 1.000000 |
| 2 | 0.500000 |
| 4 | 0.583333 |
| 5 | 0.783333 |

**5.2** Elabore un algoritmo que imprima los términos de la siguiente serie y obtenga su suma:

$$2,\ 5,\ 7,\ 10,\ 12,\ 15,\ 17,\ \ldots,\ 1800$$

Resultado esperado: la serie tiene `720` términos y su suma es `648720`.

> [!Tip]
> **Pista:** observe cuánto se suma para pasar de un término al siguiente. ¿Siempre es lo mismo? Una bandera que cambie con `not` (como en la sesión 17) puede ayudar.

**5.3** Cierta sucesión parte de los números 0, 1, 1; de ahí en adelante, cada término nuevo se forma sumando los tres términos inmediatamente anteriores:

$$0,\ 1,\ 1,\ 2,\ 4,\ 7,\ 13,\ 24,\ \ldots$$

Haga un algoritmo que genere y muestre los primeros `N` términos de la sucesión.

| N | Salida |
|---|---|
| 1 | 0 |
| 3 | 0 1 1 |
| 10 | 0 1 1 2 4 7 13 24 44 81 |

> [!Tip]
> **Pista:** es una extensión de la serie de Fibonacci de la [sesión 20](../../clases/8/sesion_magistral-20/README.md), pero con **tres** variables temporales en lugar de dos. El orden del corrimiento sigue importando.

**5.4** Elabore un algoritmo que, dado un valor de `x`, determine la suma de los `N` primeros términos de la serie:

$$f(x) = \frac{x}{2!} + \frac{2x^2}{4!} + \frac{3x^3}{6!} + \frac{4x^4}{8!} + \frac{5x^5}{10!} + \cdots$$

| x | N | Resultado |
|---|---|---|
| 1 | 1 | 0.500000 |
| 1 | 3 | 0.587500 |
| 2 | 4 | 1.368254 |

> [!Tip]
> **Pista:** escriba primero el término general (el término número `n`), como en la [sesión 19](../../clases/8/sesion_magistral-19/README.md). ¿Qué factorial lleva el término `n`?

**5.5** El seno de un ángulo `x` (en radianes) puede calcularse de forma aproximada sumando los `N` primeros términos de la serie infinita:

$$\operatorname{sen}(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

| x | N | Resultado |
|---|---|---|
| 0.5236 (≈ π/6) | 3 | 0.500003 |
| 1 | 4 | 0.841468 |
| 3 | 3 | 0.525000 |
| 3 | 8 | 0.141120 |

> **Pregunta para pensar:** el seno de 3 radianes es aproximadamente `0.141120`. ¿Por qué con `x = 3` y `N = 3` el resultado está tan lejos, y con `x = 1` y `N = 4` está tan cerca? Cuando termine, compare su programa con [`seno.py`](../../clases/10/teoria/codigo/seno.py) de la clase 10.

---

## Fuentes de los ejercicios

| Ejercicio(s) | Fuente |
|---|---|
| 1.1 y 1.3 (códigos 1-3 y 10-12) | Agregados para este taller |
| 1.2 (códigos 4-9) | Taller de ciclos del docente del curso (2022) |
| 2.1 – 2.9, 2.11 | Oviedo, cap. 4, ejercicios propuestos 32, 34, 25, 26, 29, 30, 31, 36, 37 y 35. En 2.2 se agregó el precio de la manzana como dato de entrada; en 2.8 se fijó el IVA en 19%; en 2.9 se precisó que la distancia es solo de ida |
| 2.10 | Oviedo, cap. 4, ejercicio propuesto 33, con las preguntas cambiadas por preguntas del curso |
| 2 — Para explorar | Oviedo, cap. 4, ejercicio resuelto N.º 15 |
| 3.1 | Oviedo, cap. 5, ejercicio propuesto 61 |
| 3.2 | Oviedo, cap. 5, ejercicio propuesto 69 |
| 3.3 | Oviedo, cap. 5, ejercicio propuesto 79 |
| 3.4 | Oviedo, cap. 5, ejercicio resuelto N.º 26 |
| 3.5 | Adaptado de Oviedo, cap. 6, ejercicio propuesto 103 (se conservó la estructura del problema y se cambió el contexto) |
| 4.1 | Farrell, cap. 5 "Creación de ciclos", ejercicio 9 |
| 4.2 y 4 — Para explorar | Farrell, cap. 5 "Creación de ciclos", ejercicio 13 (a y b) |
| 4.3 | Oviedo, cap. 5, ejercicio propuesto 78 (se agregó el centinela) |
| 4.4 | Oviedo, cap. 5, ejercicio propuesto 60, en la versión del taller de 2022 (que agrega la regla de más de 6 hijos para todos los salarios), con el límite "igual o mayor a $300.000" del libro; se agregó el centinela y la fórmula con paréntesis |
| 4.5 | Oviedo, cap. 5, ejercicio propuesto 47 |
| 4.6 | Oviedo, cap. 5, ejercicio propuesto 59 (se precisó qué es una mesa "no coja") |
| 4.7, 5.1, 5.2 | Taller de ciclos del docente del curso (2022) |
| 5.3 | Oviedo, cap. 5, ejercicio propuesto 74 |
| 5.4 | Oviedo, cap. 5, ejercicio propuesto 56 (el último denominador aparece en el libro como 16!; se corrigió a 10!, como en el taller de 2022) |
| 5.5 | Oviedo, cap. 6, ejercicio propuesto 110 |

**Referencias**

* Oviedo, E. A. *Lógica de Programación*. Disponible en [`material/libros/`](../../material/libros/Logica-de-Programacion-Efrain-Oviedo.pdf).
* Farrell, J. (2013). *Introducción a la programación lógica y diseño* (7a ed.). Cengage Learning. Disponible en [`material/libros/`](../../material/libros/Joyce-Farrell_Introduccion-a-la-programacion.pdf).

---

## Anexo: Referencia rápida (pseudocódigo y Python)

En el parcial, las soluciones se escriben **a mano y en Python**, y se puede consultar la hoja de referencia [`python-cheatsheet.pdf`](./python-cheatsheet.pdf) (*Real Python Pocket Reference*), que está en esta carpeta. Este anexo complementa esa hoja: muestra cada estructura en **pseudocódigo**, con la notación de las clases 5 a 8, junto a su **equivalente en Python**. Así, el diseño que se piensa en pseudocódigo se puede escribir directamente en Python.

### A.1 Instrucciones básicas

| Instrucción | Pseudocódigo | Python |
|---|---|---|
| Inicio y fin del algoritmo | `Inicio` ... `Fin` | No se escriben: el programa empieza en la primera línea y termina en la última |
| Entrada (entero) | `Leer(N)` | `N = int(input("Mensaje: "))` |
| Entrada (real) | `Leer(nota)` | `nota = float(input("Mensaje: "))` |
| Salida | `Escribir("Suma: ", suma)` | `print("Suma: ", suma)` |
| Asignación | `suma = 0` | `suma = 0` |
| Constante | `NOTA_MINIMA = 3.0` | `NOTA_MINIMA = 3.0` |
| Valores lógicos | `Verdadero`, `Falso` | `True`, `False` |
| Actualizar un contador | `i = i + 1` | `i = i + 1` o `i += 1` |
| Actualizar un acumulador | `suma = suma + nota` | `suma = suma + nota` o `suma += nota` |

> En Python, `input()` siempre devuelve texto (`str`). Si el valor se va a usar en una operación numérica, debe convertirse con `int()` o `float()`.

### A.2 Operadores

| Tipo | Pseudocódigo | Python |
|---|---|---|
| Aritméticos | `+`, `-`, `*`, `/`, `//`, `%` | `+`, `-`, `*`, `/`, `//`, `%` |
| Potencia | `^` | `**` |
| Relacionales | `>`, `>=`, `<`, `<=`, `==`, `!=` | `>`, `>=`, `<`, `<=`, `==`, `!=` |
| Lógicos | `and`, `or`, `not` | `and`, `or`, `not` |

**Prioridad en Python**, de mayor a menor: paréntesis `()` → potencia `**` → `*`, `/`, `//`, `%` → `+`, `-` → relacionales → `not` → `and` → `or`. Ante la duda, use paréntesis.

> `/` siempre da un resultado real (`7 / 2` → `3.5`); `//` da la división entera (`7 // 2` → `3`) y `%` el residuo (`7 % 2` → `1`). Un número `n` es par si `n % 2 == 0`.

### A.3 Estructuras condicionales

| Estructura | Pseudocódigo | Python |
|---|---|---|
| Alternativa simple | `Si (nota >= 3.0) Entonces`<br>&nbsp;&nbsp;`Escribir("Aprobó")`<br>`Fin_Si` | `if nota >= 3.0:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Aprobó")` |
| Alternativa doble | `Si (nota >= 3.0) Entonces`<br>&nbsp;&nbsp;`Escribir("Aprobó")`<br>`Sino`<br>&nbsp;&nbsp;`Escribir("Reprobó")`<br>`Fin_Si` | `if nota >= 3.0:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Aprobó")`<br>`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Reprobó")` |
| Alternativa múltiple | `Si (nota >= 4.0) Entonces`<br>&nbsp;&nbsp;`Escribir("Excelente")`<br>`Sino`<br>&nbsp;&nbsp;`Si (nota >= 3.0) Entonces`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Escribir("Aprobó")`<br>&nbsp;&nbsp;`Sino`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Escribir("Reprobó")`<br>&nbsp;&nbsp;`Fin_Si`<br>`Fin_Si` | `if nota >= 4.0:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Excelente")`<br>`elif nota >= 3.0:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Aprobó")`<br>`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Reprobó")` |
| Condición compuesta | `Si (nota >= 0) and (nota <= 5) Entonces` | `if nota >= 0 and nota <= 5:` |

> El pseudocódigo no tiene un equivalente de `elif`: la alternativa múltiple siempre se escribe con bloques `Si ... Sino` anidados. En Python, ese mismo algoritmo se puede escribir con `if` anidados o con `if`/`elif`/`else`. Las dos formas son correctas, pero la segunda suele ser más fácil de leer.
>
> En pseudocódigo, el final de cada bloque se marca con `Fin_Si`, `Fin_Mientras` o `Fin_Para`. En Python no existen esas palabras: el bloque lo delimita la **sangría** (indentación) y cada encabezado termina en **dos puntos** (`:`). Al escribir a mano, deje clara la sangría de cada línea.

### A.4 Estructuras repetitivas

| Estructura | Pseudocódigo | Python |
|---|---|---|
| Ciclo `Mientras` | `i = 1`<br>`Mientras (i <= N) Haga`<br>&nbsp;&nbsp;`Escribir(i)`<br>&nbsp;&nbsp;`i = i + 1`<br>`Fin_Mientras` | `i = 1`<br>`while i <= N:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(i)`<br>&nbsp;&nbsp;&nbsp;&nbsp;`i = i + 1` |
| Ciclo `Para` (paso positivo) | `Para (i = 1, N, 1) Haga`<br>&nbsp;&nbsp;`Escribir(i)`<br>`Fin_Para` | `for i in range(1, N + 1, 1):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(i)` |
| Ciclo `Para` desde 0 | `Para (i = 0, N - 1, 1) Haga`<br>&nbsp;&nbsp;`Leer(nota)`<br>`Fin_Para` | `for i in range(N):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`nota = float(input("Nota: "))` |
| Ciclo `Para` (paso negativo) | `Para (num = N, 1, -1) Haga`<br>&nbsp;&nbsp;`Escribir(num)`<br>`Fin_Para` | `for num in range(N, 0, -1):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(num)` |
| Ciclo que se repite hasta un `Romper` | `Mientras (Verdadero) Haga`<br>&nbsp;&nbsp;`...`<br>`Fin_Mientras` | `while True:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`...` |
| Terminar el ciclo | `Romper` | `break` |
| Saltar a la siguiente iteración | `Continuar` | `continue` |

> **Cuidado con `range()`:** en `range(inicio, parada, paso)` el valor de parada **no se incluye**. Por eso el `fin` del pseudocódigo se traduce como `fin + 1` cuando el paso es positivo, y como `fin - 1` cuando el paso es negativo: `Para (num = N, 1, -1)` se escribe `range(N, 0, -1)`.
>
> `Romper` (`break`) termina el ciclo por completo; `Continuar` (`continue`) solo salta el resto del cuerpo en la iteración actual y sigue con la siguiente. Si hay ciclos anidados, los dos afectan solo al ciclo **más interno** que los contiene.

### A.5 Patrones frecuentes en los ciclos

Estos son los esquemas que más se repiten en los ejercicios de las secciones 3 a 5. Los `...` indican la parte que cambia en cada problema.

| Patrón | Pseudocódigo | Python |
|---|---|---|
| **Contador y acumulador** con `N` datos | `cnt = 0`<br>`suma = 0`<br>`Para (i = 1, N, 1) Haga`<br>&nbsp;&nbsp;`Leer(nota)`<br>&nbsp;&nbsp;`suma = suma + nota`<br>&nbsp;&nbsp;`Si (nota >= 3.0) Entonces`<br>&nbsp;&nbsp;&nbsp;&nbsp;`cnt = cnt + 1`<br>&nbsp;&nbsp;`Fin_Si`<br>`Fin_Para` | `cnt = 0`<br>`suma = 0`<br>`for i in range(1, N + 1):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`nota = float(input("Nota: "))`<br>&nbsp;&nbsp;&nbsp;&nbsp;`suma = suma + nota`<br>&nbsp;&nbsp;&nbsp;&nbsp;`if nota >= 3.0:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cnt = cnt + 1` |
| **Centinela** (no se sabe cuántos datos hay) | `Leer(nota)`<br>`Mientras (nota != -1) Haga`<br>&nbsp;&nbsp;`...`<br>&nbsp;&nbsp;`Leer(nota)`<br>`Fin_Mientras` | `nota = float(input("Nota (-1 para terminar): "))`<br>`while nota != -1:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`...`<br>&nbsp;&nbsp;&nbsp;&nbsp;`nota = float(input("Nota (-1 para terminar): "))` |
| **Validación** (repetir la lectura hasta que el dato sea válido) | `Leer(nota)`<br>`Mientras (nota < 0 or nota > 5) Haga`<br>&nbsp;&nbsp;`Escribir("Nota inválida")`<br>&nbsp;&nbsp;`Leer(nota)`<br>`Fin_Mientras` | `nota = float(input("Nota: "))`<br>`while nota < 0 or nota > 5:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print("Nota inválida")`<br>&nbsp;&nbsp;&nbsp;&nbsp;`nota = float(input("Nota: "))` |
| **Bandera** (detenerse cuando algo ocurre) | `encontrado = Falso`<br>`i = 0`<br>`Mientras ((i < N) and (encontrado == Falso)) Haga`<br>&nbsp;&nbsp;`Leer(num)`<br>&nbsp;&nbsp;`Si (num == 0) Entonces`<br>&nbsp;&nbsp;&nbsp;&nbsp;`encontrado = Verdadero`<br>&nbsp;&nbsp;`Fin_Si`<br>&nbsp;&nbsp;`i = i + 1`<br>`Fin_Mientras` | `encontrado = False`<br>`i = 0`<br>`while i < N and encontrado == False:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`num = int(input("Numero: "))`<br>&nbsp;&nbsp;&nbsp;&nbsp;`if num == 0:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`encontrado = True`<br>&nbsp;&nbsp;&nbsp;&nbsp;`i = i + 1` |
| **Ruptura** (el mismo problema con `Romper`) | `encontrado = Falso`<br>`Para (i = 1, N, 1) Haga`<br>&nbsp;&nbsp;`Leer(num)`<br>&nbsp;&nbsp;`Si (num == 0) Entonces`<br>&nbsp;&nbsp;&nbsp;&nbsp;`encontrado = Verdadero`<br>&nbsp;&nbsp;&nbsp;&nbsp;`Romper`<br>&nbsp;&nbsp;`Fin_Si`<br>`Fin_Para` | `encontrado = False`<br>`for i in range(1, N + 1):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`num = int(input("Numero: "))`<br>&nbsp;&nbsp;&nbsp;&nbsp;`if num == 0:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`encontrado = True`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`break` |
| **Búsqueda de extremos** (mayor y menor; se inicializan con el primer dato) | `Leer(nota)`<br>`mayor = nota`<br>`menor = nota`<br>`Para (i = 2, N, 1) Haga`<br>&nbsp;&nbsp;`Leer(nota)`<br>&nbsp;&nbsp;`Si (nota > mayor) Entonces`<br>&nbsp;&nbsp;&nbsp;&nbsp;`mayor = nota`<br>&nbsp;&nbsp;`Fin_Si`<br>&nbsp;&nbsp;`Si (nota < menor) Entonces`<br>&nbsp;&nbsp;&nbsp;&nbsp;`menor = nota`<br>&nbsp;&nbsp;`Fin_Si`<br>`Fin_Para` | `nota = float(input("Nota: "))`<br>`mayor = nota`<br>`menor = nota`<br>`for i in range(2, N + 1):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`nota = float(input("Nota: "))`<br>&nbsp;&nbsp;&nbsp;&nbsp;`if nota > mayor:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`mayor = nota`<br>&nbsp;&nbsp;&nbsp;&nbsp;`if nota < menor:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`menor = nota` |

> En el patrón **centinela**, el dato se lee **dos veces**: una antes del ciclo (para la primera comparación) y otra al **final** del cuerpo (para la siguiente vuelta). Si se olvida la segunda lectura, el ciclo nunca termina.
>
> En la **búsqueda de extremos** se usan dos `Si` **separados**, no un `Si ... Sino`: un mismo dato puede ser a la vez el mayor y el menor (por ejemplo, el primero). También se pueden inicializar con valores "al revés" del rango válido, como `mayor = 0.0` y `menor = 5.0` para notas de 0 a 5.
>
> En Python, `encontrado == False` también se puede escribir `not encontrado`.

### A.6 Roles de las variables en un ciclo

| Rol | Para qué sirve | Pseudocódigo | Python |
|---|---|---|---|
| Variable de control | Decide si el ciclo sigue | `Mientras (i <= N) Haga` | `while i <= N:` |
| Contador | Cuenta sucesos; aumenta en un valor constante | `cnt = cnt + 1` | `cnt = cnt + 1` |
| Acumulador | Totaliza valores que cambian | `suma = suma + nota` | `suma = suma + nota` |
| Bandera | Recuerda si algo ocurrió (verdadero o falso) | `encontrado = Verdadero` | `encontrado = True` |
| Centinela | Valor especial de entrada que indica que no hay más datos | `Mientras (nota != -1) Haga` | `while nota != -1:` |

Los roles no son excluyentes: una misma variable puede ser contador y variable de control a la vez.

### A.7 ¿Qué estrategia de ciclo usar?

| Situación | Estrategia | Condición típica en pseudocódigo | Condición típica en Python |
|---|---|---|---|
| Se sabe cuántas veces repetir (`N` datos) | Contador | `Para (i = 1, N, 1)` o `Mientras (i <= N)` | `for i in range(1, N + 1):` o `while i <= N:` |
| No se sabe cuántos datos hay | Centinela | `Mientras (dato != -1)` | `while dato != -1:` |
| Se repite hasta que ocurra algo | Bandera o `Romper` | `Mientras (encontrado == Falso)` | `while encontrado == False:` |
| Se pide un dato hasta que sea válido | Ciclo de validación | `Mientras (nota < 0 or nota > 5)` | `while nota < 0 or nota > 5:` |

### A.8 Más referencia

* Hoja de referencia de Python: [`python-cheatsheet.pdf`](./python-cheatsheet.pdf) (*Real Python Pocket Reference*).
* Operadores y su prioridad, método de Polya y formato de la prueba de escritorio: [Anexo del Taller 1](../algoritmos-secuenciales/README.md#anexo-tablas-de-referencia-rápida).
* Consejos para contadores, banderas y acumuladores en ciclos anidados: [sesión 21](../../clases/8/sesion_magistral-21/README.md#consejos-para-usar-contadores-banderas-y-acumuladores-en-ciclos-anidados).
