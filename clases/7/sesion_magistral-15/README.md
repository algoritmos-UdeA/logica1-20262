![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 15

* **Tipo**: Presencial
* **Fecha**: 15/09/2026
* **Parte**: Primer bloque de clase (14-16)

## Repaso Condicionales multiples

Se retomo el problema de los numeros.

## Parte 1

### Repaso rápido: alternativas en pseudocódigo y Python

Antes de retomar el ejercicio, conviene refrescar cómo se corresponden las estructuras de decisión que se van a usar (revisadas con más detalle en la [teoría de clase 6](../../6/teoria/README.md)):

| Estructura | Pseudocódigo | Python |
|---|---|---|
| Alternativa simple | `Si (condición) Entonces` ... `Fin_Si` | `if condición:` ... |
| Alternativa doble | `Si (condición) Entonces` ... `Sino` ... `Fin_Si` | `if condición:` ... `else:` ... |
| Alternativa múltiple | bloques `Si...Sino` anidados uno dentro de otro (el pseudocódigo del curso no tiene otra forma de expresarlo) | `if`/`else` anidados, o `elif` — dos formas distintas de escribir en Python el mismo anidamiento del pseudocódigo |

**Enunciado**

Realizar un programa que permita ingresar `N` números enteros (positivos, negativos o cero) por teclado. El programa debe permitir desplegar la siguiente información:

* Cantidad de pares e impares ingresados.
* Promedio de números pares e impares.

El planteamiento en pseudocodigo fue el siguiente:

```
Inicio
  cant_pares = 0
  cant_impares = 0
  sum_pares = 0
  sum_impares = 0
  i = 0
  Leer(N)
  Mientras i < N Haga
    Leer(num)
    Si (num % 2 == 0) Entonces
      cant_pares = cant_pares + 1
      sum_pares = sum_pares + num
    Sino
      cant_impares = cant_impares + 1
      sum_impares = sum_impares + num
    Fin_Si
    i = i + 1
  Fin_Mientras
  Si cant_impares == 0 Entonces
    Si cant_pares == 0 Entonces
       Escribir("No se ingresaron numeros")
    Sino
       Escribir("No se ingresaron numeros impares")
       prom_pares = sum_pares/cant_pares       
       Escribir(cant_pares, prom_pares)
    Fin_Si       
  Sino  
    Si cant_pares == 0 Entonces
       Escribir("No se ingresaron pares")
       prom_impares = sum_impares/cant_impares       
       Escribir(cant_impares, prom_impares)
    Sino
       prom_pares = sum_pares/cant_pares       
       Escribir(cant_pares, prom_pares)
       prom_impares = sum_impares/cant_impares       
       Escribir(cant_impares, prom_impares)
    Fin_Si       
  Fin_Si
Fin
```

El bloque final de condicionales anidados, el que se retoma en esta sesión, se puede visualizar así:

```mermaid
flowchart TD
    Start([Inicio]) --> C1
    C1{"cant_impares == 0?"} -- "Verdadero" --> C2
    C1 -- "Falso" --> C3
    C2{"cant_pares == 0?"} -- "Verdadero" --> A["Escribir('No se ingresaron numeros')"]
    C2 -- "Falso" --> B["Escribir('No se ingresaron numeros impares')<br/>prom_pares = sum_pares / cant_pares<br/>Escribir(cant_pares, prom_pares)"]
    C3{"cant_pares == 0?"} -- "Verdadero" --> C["Escribir('No se ingresaron pares')<br/>prom_impares = sum_impares / cant_impares<br/>Escribir(cant_impares, prom_impares)"]
    C3 -- "Falso" --> D["prom_pares = sum_pares / cant_pares<br/>Escribir(cant_pares, prom_pares)<br/>prom_impares = sum_impares / cant_impares<br/>Escribir(cant_impares, prom_impares)"]
    A --> End([Fin])
    B --> End
    C --> End
    D --> End

    classDef cond fill:#fef9c3,stroke:#a16207,color:#713f12;
    classDef action fill:#dcfce7,stroke:#15803d,color:#14532d;
    class C1,C2,C3 cond
    class A,B,C,D action
```

Se analizo sobre todo la parte final donde se comparo la implementacion de python con condicionales anididados en el codigo [impares_v1.py](codigo/impares_v1.py). El fragmento de codigo en python quedo asi:

```py
if (cant_impares == 0) and (cant_pares == 0):
    # No se ingresaron numeros
    print("No se ingresaron numeros")
else:
    if cant_pares == 0:
        # Todos los numeros ingresados fueron impares
        print("No se ingresaron pares")
        prom_impares = sum_impares/cant_impares
        print(f"El promedio de los {cant_impares} ingresados fue {prom_impares:.2f}")
    else:
        if cant_impares == 0:
            # Todos los numeros ingresados fueron pares
            print("No se ingresaron impares")
            prom_pares = sum_pares/cant_pares
            print(f"El promedio de los {cant_pares} ingresados fue {prom_pares:.2f}")
        else:
            # Se ingresaron tanto numeros pares como impares
            prom_pares = sum_pares/cant_pares
            prom_impares = sum_impares/cant_impares
            print(f"El promedio de los {cant_pares} ingresados fue {prom_pares:.2f}")
            print(f"El promedio de los {cant_impares} ingresados fue {prom_impares:.2f}")
```

Notese que del fragmento anterior se pueden identificar 4 posibilidades:

| Caso | `cant_pares` | `cant_impares` | Resultado |
|---|---|---|---|
| 1 | 0 | 0 | "No se ingresaron numeros" |
| 2 | 0 | > 0 | "No se ingresaron pares" + promedio de impares |
| 3 | > 0 | 0 | "No se ingresaron impares" + promedio de pares |
| 4 | > 0 | > 0 | promedio de pares + promedio de impares |

Se realizo la prueba de escritorio con 4 casos donde se pudiera ver cada uno de los analisis por cada rama:

| Caso | `N` | Números | `cant_impares` | `cant_pares` | `sum_impares` | `sum_pares` |
|---|---|---|---|---|---|---|
| 1 | 0 | (ninguno) | 0 | 0 | 0 | 0 |
| 2 | 3 | 1, 3, 5 | 3 | 0 | 9 | 0 |
| 3 | 3 | 2, 4, 6 | 0 | 3 | 0 | 12 |
| 4 | 5 | 3, 4, 7, 8, 10 | 2 | 3 | 10 | 22 |

Retomando estos 4 casos, se traza el bloque de anidados tomando `cant_impares`, `sum_impares`, `cant_pares` y `sum_pares` como entradas ya conocidas (las mismas de la tabla anterior), y se deduce de ahí por cuál rama se entra y qué promedios se calculan (`—` donde no se calcula, precisamente para evitar la división por cero):

| Caso | `cant_impares` | `sum_impares` | `cant_pares` | `sum_pares` | `prom_impares` | `prom_pares` |
|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | — | — |
| 2 | 3 | 9 | 0 | 0 | 3.00 | — |
| 3 | 0 | 0 | 3 | 12 | — | 4.00 |
| 4 | 2 | 10 | 3 | 22 | 5.00 | 7.33 |

El pseudocódigo del curso no cuenta con una estructura equivalente a `elif`: solo permite anidar bloques `Si...Entonces...Sino...Fin_Si`, uno dentro de otro. Por esta razón, el pseudocódigo presentado anteriormente sigue siendo válido para describir la lógica de `v2` — las cuatro preguntas de la Tabla 1 se evalúan en el mismo orden en ambas versiones. Lo que cambia entre `v1` y `v2` no es la lógica, sino la forma en que Python organiza esas preguntas en el código.

> [!TIP]
> ### Por qué demasiado anidamiento dificulta la lectura
>
> Cada nivel de anidamiento obliga a recordar, mientras se lee el código, a qué condición pertenece cada `Sino` — entre más profundo el anidamiento, más difícil es rastrear esa relación sin perder el hilo, sobre todo porque en Python no existe un `Fin_Si` explícito: es solo la indentación la que marca dónde empieza y termina cada bloque. En `v1`, la cuarta pregunta ("¿hay de ambos?") queda a tres niveles de indentación de distancia de la primera; en `v2`, las cuatro preguntas quedan al mismo nivel, una después de otra, como una lista de casos que se revisan en orden. El resultado es idéntico en ambas versiones — lo que cambia es cuánta memoria exige seguir el rastro de los `Sino` anidados para llegar a ese resultado.

| Pregunta (Tabla 1) | Ubicación en v1 | Ubicación en v2 |
|---|---|---|
| ¿No hay pares ni impares? | primer `if` | primer `if` |
| ¿No hay pares? | `if` dentro del primer `else` | `elif` |
| ¿No hay impares? | `if` dentro del segundo `else` anidado | `elif` |
| ¿Hay de ambos? | `else` más profundo | `else` |

El fragmento correspondiente en Python ([impares_v2.py](codigo/impares_v2.py)) queda así:

```py
if (cant_impares == 0) and (cant_pares == 0):
    # No se ingresaron numeros
    print("No se ingresaron numeros")
elif cant_pares == 0:
    # Todos los numeros ingresados fueron impares
    print("No se ingresaron pares")
    prom_impares = sum_impares/cant_impares
    print(f"El promedio de los {cant_impares} ingresados fue {prom_impares:.2f}")
elif cant_impares == 0:
    # Todos los numeros ingresados fueron pares
    print("No se ingresaron impares")
    prom_pares = sum_pares/cant_pares
    print(f"El promedio de los {cant_pares} ingresados fue {prom_pares:.2f}")
else:
    # Se ingresaron tanto numeros pares como impares
    prom_pares = sum_pares/cant_pares
    prom_impares = sum_impares/cant_impares
    print(f"El promedio de los {cant_pares} ingresados fue {prom_pares:.2f}")
    print(f"El promedio de los {cant_impares} ingresados fue {prom_impares:.2f}")
```

Por eso los resultados de la Tabla 3 no cambian entre versiones: `v1` y `v2` responden las mismas preguntas, en el mismo orden — solo cambia cuánto anidamiento hace falta para expresarlas.

### Conclusiones

El ejercicio confirma que las 4 ramas identificadas cubren todos los casos posibles sin caer en división por cero — condición necesaria antes de calcular cualquier promedio. El anidamiento (v1) hace explícita la jerarquía de decisiones ("primero pregunto si no hay nada; si hay algo, pregunto qué falta"), lo cual ayuda a razonar el problema paso a paso, pero a costa de una indentación creciente. Reconocer ese patrón es justamente lo que permite aplanarlo con `elif` (v2) sin perder ningún caso.

## Parte 2

*Pendiente — próxima entrega: tipos de problema con ciclos según iteraciones conocidas y desconocidas.*
