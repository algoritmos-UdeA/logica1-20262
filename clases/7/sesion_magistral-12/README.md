![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 12

* **Tipo**: Presencial
* **Fecha**: 01/09/2026
* **Parte**: Segundo bloque de clase (16-18)

## Resumen

Continuando la introducción a ciclos de las diapositivas de la clase [(teoría)](../teoria/), esta sesión practica en vivo la estructura `Mientras`/`while`. Se empieza con un ejemplo mínimo (`hola_ciclos`) que no resuelve ningún problema en particular, sino que sirve para observar con cuidado, iteración por iteración, cómo evoluciona la variable de control — y para descubrir, con una prueba de escritorio completa, un error de conteo ("off-by-one") fácil de pasar por alto cuando la actualización de la variable ocurre antes de usarla. Con esa base ya asentada, se resuelve el problema de generar la serie de números pares hasta `N` de dos formas equivalentes, comparando sus pruebas de escritorio para confirmar que ambas producen la misma salida, pero con una cantidad distinta de trabajo por iteración.

## Ejemplos

### Ejemplo 1 — `hola_ciclos`

Antes de resolver un problema concreto, se ejecuta un ciclo mínimo cuyo único propósito es observar su comportamiento: contar cuántas veces se repite el cuerpo e imprimir el valor final de la variable de control al salir.

|#|Tipo|Nombre|Descripción|
|---|---|---|---|
|1|Constante (Entera)|`N = 10`|Límite usado en la condición de control (no es, como se verá, la cantidad de veces que se repite el ciclo)|
|2|Variable de control (Entera)|`i`|Cuenta las iteraciones ya realizadas|

#### Pseudocódigo

```
Inicio
  N = 10
  i = 0
  Mientras (i <= N) Haga
    i = i + 1
    Escribir('Hola')
  Fin_Mientras
  Escribir('Valor de i al salir:', i)
Fin
```

#### Prueba de escritorio

Se traza el valor de `i` en cada evaluación de la condición `i <= N` (todas verdaderas, hasta que `i` llega a 11):

|`N`|`i`|
|----|----|
|~~10~~|~~0~~|
| |~~1~~|
| |~~2~~|
| |~~3~~|
| |~~4~~|
| |~~5~~|
| |~~6~~|
| |~~7~~|
| |~~8~~|
| |~~9~~|
| |~~10~~|
| |**11**|

**Salida esperada**: `Hola` se imprime 11 veces, y el último mensaje es `Valor de i al salir: 11`.

> **Para reflexionar:** aunque `N = 10`, la prueba de escritorio muestra que `i` toma 11 valores distintos (0 a 10) mientras la condición es verdadera, y termina en 11, no en 10. La razón está en el orden de las instrucciones dentro del cuerpo: como `i = i + 1` ocurre *antes* del `Escribir('Hola')`, la condición `i <= N` todavía se evalúa como verdadera cuando `i` vale 10, así que el cuerpo se ejecuta una vez más de lo que parece a primera vista. Es el mismo tipo de error de conteo ("off-by-one") que se puede cometer al no fijarse en el orden exacto de las instrucciones dentro del cuerpo del ciclo.

#### Código Python

**Código**: [hola_ciclos.py](hola_ciclos.py)

```py
N = 10
i = 0
while i<= N:      
    i = i + 1
    print("Hola")
print("Valor de i al salir:", i)
```

### Ejemplo 2 — Serie de números pares hasta N

Imprimir los números pares entre 0 y `N`, partiendo siempre de un contador (`num`) inicializado en 0. Se resuelve de dos formas equivalentes, para comparar cuánto trabajo hace cada una por iteración.

|#|Tipo|Nombre|Descripción|
|---|---|---|---|
|1|Entrada (Entera)|`N`|Límite superior del rango en el que se buscan los números pares|
|2|Variable de control (Entera)|`num`|Recorre los valores desde 0 hasta `N`|

Para ambas formas se usa el mismo caso de prueba: `N = 10`.

#### Forma 1 — filtrando con módulo

Se avanza de 1 en 1 y se filtra con el operador módulo (`%`) cuáles valores son pares.

##### Pseudocódigo

```
Inicio
  Leer(N)
  num = 0
  Mientras (num <= N) Haga
    Si (num % 2 == 0) Entonces
      Escribir(num)
    Fin_Si
    num = num + 1
  Fin_Mientras
Fin
```

##### Prueba de escritorio

|`N`|`num`|`num % 2 == 0`|`Escribir(num)`|
|----|----|----|----|
|~~10~~|~~0~~|~~Sí~~|~~0~~|
| |~~1~~|~~No~~| |
| |~~2~~|~~Sí~~|~~2~~|
| |~~3~~|~~No~~| |
| |~~4~~|~~Sí~~|~~4~~|
| |~~5~~|~~No~~| |
| |~~6~~|~~Sí~~|~~6~~|
| |~~7~~|~~No~~| |
| |~~8~~|~~Sí~~|~~8~~|
| |~~9~~|~~No~~| |
| |**10**|**Sí**|**10**|

**Salida esperada**: `0, 2, 4, 6, 8, 10` (11 evaluaciones de la condición del ciclo, una por cada valor de `num` entre 0 y 10).

##### Código Python

**Código**: [serie_pares1.py](serie_pares1.py)

```py
N = int(input("Digite el numero: "))
num = 0
i = 0
while num <= N:
    if num%2 == 0:
        print(num)
    num += 1
```

#### Forma 2 — avanzando de 2 en 2

Como se parte de `num = 0` (ya par), avanzar directamente de 2 en 2 genera solo números pares, sin necesidad de la condición con módulo.

##### Pseudocódigo

```
Inicio
  Leer(N)
  num = 0
  Mientras (num <= N) Haga
    Escribir(num)
    num = num + 2
  Fin_Mientras
Fin
```

##### Prueba de escritorio

|`N`|`num`|`Escribir(num)`|
|----|----|----|
|~~10~~|~~0~~|~~0~~|
| |~~2~~|~~2~~|
| |~~4~~|~~4~~|
| |~~6~~|~~6~~|
| |~~8~~|~~8~~|
| |**10**|**10**|

**Salida esperada**: `0, 2, 4, 6, 8, 10` — la misma salida que la Forma 1, pero en solo 6 evaluaciones de la condición del ciclo en vez de 11.

##### Código Python

**Código**: [serie_pares2.py](serie_pares2.py)

```py
N = int(input("Digite el numero: "))
num = 0
i = 0
while num <= N:
    print(num)
    num += 2
```

> **Para reflexionar:** ambas pruebas de escritorio llegan al mismo resultado (`0, 2, 4, 6, 8, 10`), pero la Forma 1 evalúa la condición del ciclo 11 veces (una por cada entero entre 0 y 10, descartando los impares con el `Si`) mientras que la Forma 2 solo la evalúa 6 veces, al saltar directamente de par en par. Ninguna de las dos es "incorrecta" — la diferencia importa cuando `N` es grande, o cuando el criterio para filtrar (en vez de `num % 2 == 0`) es más costoso de evaluar que simplemente ajustar el incremento del ciclo.
>
> *Nota: ambos scripts dejan declarada una variable auxiliar `i` (con algunas líneas comentadas que la incrementaban e imprimían) que ya no se usa en la versión final — un rastro de una versión anterior del ejemplo.*

## Para explorar por su cuenta

*Ideas complementarias basadas en CS50P (Python) y CS50x (C). No fueron parte del contenido dictado en esta sesión — se incluyen como material opcional para quien quiera profundizar.*

### `hola_ciclos` es, en esencia, el ejemplo `meow` de CS50

La Lecture 2 de CS50P introduce el `while` con un ejemplo casi idéntico a `hola_ciclos`:

```py
i = 0
while i < 3:
    print("meow")
    i += 1
```

Las notas describen el `while` como "casi universal en todos los lenguajes de programación" — la misma estructura (inicializar la variable de control, repetir mientras se cumpla una condición, actualizarla dentro del cuerpo) es la que se trazó en la prueba de escritorio de `hola_ciclos`. La diferencia entre `i < 3` (CS50P) y `i <= N` con `N = 10` (esta sesión) es justo el tipo de detalle — un operador de comparación distinto — que puede correr el conteo en una unidad, como se vio en la reflexión sobre el resultado final `i = 11`.

### Ciclos infinitos: la otra cara de la moneda del off-by-one

CS50x también muestra un ciclo que nunca termina:

```c
while (true)
{
    printf("meow\n");
}
```

y advierte que la única forma de detenerlo es interrumpirlo manualmente (`control-C`). Vale la pena conectarlo con la reflexión sobre `hola_ciclos`: ahí la condición sí terminaba, aunque con un valor final distinto al esperado (11 en vez de 10); pero un error en la actualización de la variable de control — o su ausencia — puede hacer que la condición nunca se vuelva falsa. Los **ciclos infinitos** y su **ruptura controlada** (`break`) son, de hecho, el primer tema anunciado para la próxima clase magistral (ver [teoría](../teoria/#contenido-cubierto)).

### Referencia

- Malan, D. (Harvard). *CS50's Introduction to Programming with Python* — [Lecture 2: Loops](https://cs50.harvard.edu/python/notes/2/).
- Malan, D. (Harvard). *CS50 Introduction to Computer Science* — [Lecture 1: C — Loops and `meow.c`](https://cs50.harvard.edu/x/notes/1/#loops-and-meowc).

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
