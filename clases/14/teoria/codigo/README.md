![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 14 — Código de ejemplo (índice por problema)

Todos los programas usan solo Python (3.11), sin bibliotecas externas. Los scripts sueltos se ejecutan desde esta carpeta (`python ej05_recorrer_mostrar.py`). Los de las carpetas se ejecutan **desde su propia carpeta**: primero las pruebas y después el programa.

Los datos son los mismos en toda la clase: 4 estudiantes (Ana, Beto, Carla, Dario) y 3 parciales.

```python
notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
```

## 1. Las operaciones básicas con matrices

Un script por cada operación de las diapositivas 9-34.

| Archivo | Qué muestra | Salida (resumida) |
|---|---|---|
| [ej00_sin_matriz.py](ej00_sin_matriz.py) | La solución sin matriz: un arreglo por parcial | `Ana: 3.00` … `Parcial 1: 3.38` |
| [ej01_crear_matriz.py](ej01_crear_matriz.py) | Crear en dos pasos, guardar, leer y crear con valores | `[[0.0, 0.0, 0.0], …]`, `5.0`, `Suma: 6.5` |
| [ej02_filas_alias.py](ej02_filas_alias.py) | ⚠️ `[[0.0] * M] * N` repite la misma fila | `[[5.0, 0.0, 0.0], [5.0, 0.0, 0.0], …]` |
| [ej03_indices_expresion.py](ej03_indices_expresion.py) | Ejercicio: el índice como expresión | `[14, 1, 2]`, `[-3, 4, 8]`, `[6, 7, 12]` |
| [ej04_llenar.py](ej04_llenar.py) | Llenar por teclado y por expresión (usa `input()`) | `[True, True, False]` … |
| [ej05_recorrer_mostrar.py](ej05_recorrer_mostrar.py) | Mostrar por filas como tabla, por columnas y por elemento | `Parcial 1: 3.0  4.5  2.0  4.0` … |
| [ej06_acumular.py](ej06_acumular.py) | Total, promedio por fila y por columna, contar | `Suma: 42.5`, `Estudiante 2: 2.83`, `Parcial 1: 3.38`, `Notas menores que 3.0: 2` |
| [ej07_salirse.py](ej07_salirse.py) | ⚠️ `N` y `M` intercambiados | `3.0`, `3.5`, `2.5` y `IndexError` (a propósito) |
| [ej08_cuadradas.py](ej08_cuadradas.py) | Diagonales y triangulares de una matriz de 4 × 4 | `34`, `34`, `70`, `100` |
| [ej09_mayor_buscar.py](ej09_mayor_buscar.py) | El mayor con su posición; buscar un valor | `Mejor nota: 5.0, de Beto, en el parcial 3` |
| [ej10_transpuesta_suma.py](ej10_transpuesta_suma.py) | Transpuesta y suma: matrices nuevas | `[[1, 4], [2, 5], [3, 6]]`, `[[11, 22, 33], [44, 55, 66]]` |
| [ej11_alias_copia.py](ej11_alias_copia.py) | Alias, copia con `list()` (comparte filas) y clon con dos ciclos | con `list()` la original **sí** cambia; con el clon, no |

## 2. Funciones con matrices: los tres casos

| Archivo | Contenido |
|---|---|
| [funciones_matrices.py](funciones_matrices.py) | `calcular_promedio_fila(notas, i)` (caso 1), `leer_notas(n, m)` (caso 2) y `aplicar_bonificacion(notas, j, puntos)` (caso 3), con su especificación |
| [test_funciones_matrices.py](test_funciones_matrices.py) | Pruebas con `assert` de los casos 1 y 3 → `Pruebas de funciones_matrices: todas pasaron` |

## 3. Notas finales de un curso — [`notas_matriz/`](notas_matriz/)

> **Enunciado** (diapositiva 42): Se tienen los nombres de los estudiantes de un curso y sus notas en tres parciales, que valen 30 %, 30 % y 40 %. Calcular la nota final de cada estudiante y mostrar quiénes obtuvieron la nota final más alta y quiénes la más baja.

Adaptado del ejercicio de las notas parciales de Mera Banguero, con pesos por parcial.

| Archivo | Contenido |
|---|---|
| [notas.py](notas_matriz/notas.py) | `leer_nombres`, `leer_notas`, `calcular_notas_finales`, `buscar_mayor`, `buscar_menor`, `contar_iguales`, `posiciones_iguales` y `mostrar_estudiantes` |
| [test_notas.py](notas_matriz/test_notas.py) | Pruebas, incluido un empate → `Pruebas de notas: todas pasaron` |
| [main.py](notas_matriz/main.py) | Programa principal, con `PESOS = [0.3, 0.3, 0.4]` |

Con los datos de la clase, `main.py` termina así:

```
Ana: 2.95
Beto: 4.55
Carla: 2.90
Dario: 3.75
Nota final mas alta: 4.55
  Beto
Nota final mas baja: 2.90
  Carla
```

## 4. La clase `Matriz` — [`matriz_poo/`](matriz_poo/)

> **Enunciado** (diapositiva 51): Diseñe una clase llamada `Matriz` para representar una tabla de números. La clase contiene tres atributos privados (`filas`, `columnas` y `datos`), un constructor que crea la matriz con todas las casillas en un valor dado (`0.0` si no se da), `get_filas()` y `get_columnas()`, `es_posicion_valida(i, j)`, `get(i, j)` y `set(i, j, valor)` (que solo cambia la casilla si la posición es válida y retorna `True` o `False`), `sumar_fila(i)`, `sumar_columna(j)`, `es_cuadrada()`, `transpuesta()` y `sumar(otra)` (que retornan una `Matriz` nueva) y `__str__`, que la muestra como tabla.

| Archivo | Contenido |
|---|---|
| [matriz.py](matriz_poo/matriz.py) | La clase `Matriz` |
| [test_matriz.py](matriz_poo/test_matriz.py) | Pruebas → `Pruebas de Matriz: todas pasaron` |
| [main.py](matriz_poo/main.py) | Guarda las notas del curso en una `Matriz`; muestra la tabla, los promedios y la transpuesta |

## 5. Sala de cine: una matriz de objetos — [`sala_cine/`](sala_cine/)

> **Enunciado** (diapositiva 57): Una sala de cine tiene filas identificadas con letras (A, B, C, …) y sillas numeradas desde 1. La boleta vale $5000. Se necesita ver el mapa de la sala (X ocupada, O libre), vender una boleta para una silla, liberar una silla, contar las sillas libres de cada fila y de toda la sala, y saber cuánto se ha recaudado.

Adaptado de un ejercicio de Mera Banguero (una sala de 12 filas, A a L, con 10 sillas cada una). `main.py` usa una sala de 5 filas y 6 sillas.

| Archivo | Contenido |
|---|---|
| [silla.py](sala_cine/silla.py) | La clase `Silla`: fila, número y si está ocupada |
| [sala.py](sala_cine/sala.py) | La clase `Sala`: crea sus sillas en una matriz de objetos (composición); `get_silla` convierte de la letra y el número del público a los índices de la matriz |
| [test_silla.py](sala_cine/test_silla.py), [test_sala.py](sala_cine/test_sala.py) | Pruebas → `Pruebas de Silla: todas pasaron` y `Pruebas de Sala: todas pasaron` |
| [main.py](sala_cine/main.py) | Menú: ver el mapa, vender, liberar, resumen, salir |

| Caso de prueba del menú | Resultado |
|---|---|
| Vender A1 y C4 | `Listo` en los dos |
| Vender otra vez C4 | `No se pudo: la silla no existe o no esta en ese estado` |
| Ver el mapa | A1 y C4 con `X`, las demás con `O` |
| Resumen | Fila A: 5 libres, fila C: 5 libres, 28 libres en total, recaudo $ 10000 |

> [!Important]
> Se usó IA generativa para escribir este código y esta guía a partir de las indicaciones del docente. El docente revisa y valida la versión final.
