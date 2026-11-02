![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Paso 2 — El programa completo

> Leer las notas de los estudiantes de un curso y mostrar el promedio, cuántas notas son mayores que el promedio y en qué posiciones están.

## Qué se pretende mostrar

1. **La implementación cumple el contrato.** Las dos funciones que en el [paso 1](../paso1_stubs/) eran stubs ya están implementadas (diapositivas 44-45). `test_notas.py` y `main.py` son **los mismos** del paso 1: lo único que cambió es `notas.py`.
   * `contar_mayores_que(notas, valor)` es el patrón **contar** de la sesión 28, ahora dentro de una función: recorre con `range(len(notas))` y suma 1 cada vez que `notas[i] > valor`.
   * `posiciones_mayores_que(notas, valor)` devuelve una **lista nueva** sin usar `append`. Primero **cuenta** cuántas posiciones habrá, llamando a `contar_mayores_que`. Después **crea** la lista del tamaño justo, `[0] * cantidad`. Al final la **llena** con dos índices: `i` recorre `notas`, y `k` marca la siguiente casilla libre de `posiciones`.
2. **Una función puede usar a otra.** `posiciones_mayores_que` reutiliza `contar_mayores_que` en lugar de repetir el conteo.
3. **El programa principal se lee como el árbol top-down** (diapositiva 47): leer → calcular → buscar → mostrar. Es el problema de la clase 10, que ahora sí se puede resolver porque las notas quedan guardadas en un arreglo y se recorren dos veces.

| Archivo | Contenido |
|---|---|
| [`notas.py`](notas.py) | Las cinco funciones, todas implementadas |
| [`test_notas.py`](test_notas.py) | Las pruebas con `assert`, iguales a las del paso 1 |
| [`main.py`](main.py) | El programa principal, igual al del paso 1 |

Estos tres archivos son copias idénticas de los de [`teoria/codigo/notas_con_arreglos/`](../../../../teoria/codigo/notas_con_arreglos/).

## Cómo ejecutarlo

Desde esta carpeta (`paso2_completo/`):

```
python test_notas.py
python main.py
```

Para probar una función a mano, sin pasar por el programa principal:

```
python -i notas.py
>>> posiciones_mayores_que([3.0, 4.5, 2.0, 4.0], 3.375)
[1, 3]
```

## Salida esperada

### Las pruebas

```
Pruebas de notas: todas pasaron
```

Si una prueba fallara, el programa se detendría con `AssertionError` en esa línea, como en el paso 1.

### El programa principal: el ejemplo de la clase

Con 4 estudiantes y las notas 3.0, 4.5, 2.0 y 4.0:

```
Notas mayores que el promedio
Cantidad de estudiantes: 4
Nota del estudiante 1: 3.0
Nota del estudiante 2: 4.5
Nota del estudiante 3: 2.0
Nota del estudiante 4: 4.0
Promedio del curso: 3.38
Notas mayores que el promedio: 2
Posiciones: [1, 3]
```

El promedio es 13.5 / 4 = 3.375. Las notas mayores son 4.5 (posición 1) y 4.0 (posición 3). La prueba de escritorio de `posiciones_mayores_que` con estos datos:

| `i` | `notas[i]` | ¿`> 3.375`? | `k` | `posiciones` |
|---|---|---|---|---|
| — | — | — | 0 | `[0, 0]` |
| 0 | 3.0 | no | 0 | `[0, 0]` |
| 1 | 4.5 | sí | 1 | `[1, 0]` |
| 2 | 2.0 | no | 1 | `[1, 0]` |
| 3 | 4.0 | sí | 2 | `[1, 3]` |

La lista empieza como `[0, 0]` porque `contar_mayores_que` dijo que habría 2 posiciones.

### El programa principal: una cantidad inválida y una nota igual al promedio

Si primero se escribe `0` y después 3 estudiantes con notas 5.0, 1.0 y 3.0:

```
Notas mayores que el promedio
Cantidad de estudiantes: 0
ERROR: la cantidad debe ser mayor que 0
Cantidad de estudiantes: 3
Nota del estudiante 1: 5.0
Nota del estudiante 2: 1.0
Nota del estudiante 3: 3.0
Promedio del curso: 3.00
Notas mayores que el promedio: 1
Posiciones: [0]
```

* El `while` de `main.py` no deja pasar el `0`: `leer_notas` y `calcular_promedio` **suponen** que hay al menos una nota, y quien las llama debe garantizarlo.
* El promedio es 3.0 y la nota 3.0 es **igual** al promedio, no mayor: por eso solo cuenta el 5.0, en la posición 0. Es el mismo caso límite de `>` frente a `>=` de la [sesión 28](../../../../sesion_magistral-28/README.md).

> [!Important]
> Se usó IA generativa para preparar este material a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
