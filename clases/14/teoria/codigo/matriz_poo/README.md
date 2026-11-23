![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# La clase `Matriz`

## Qué hace

> Diseñe una clase llamada **Matriz** para representar una tabla de números. La clase contiene tres atributos privados (`filas`, `columnas` y `datos`), un constructor que crea la matriz con todas las casillas en un valor dado (`0.0` si no se da), `get_filas()` y `get_columnas()`, `es_posicion_valida(i, j)`, `get(i, j)` y `set(i, j, valor)` (que solo cambia la casilla si la posición es válida y retorna `True` o `False`), `sumar_fila(i)`, `sumar_columna(j)`, `es_cuadrada()`, `transpuesta()` y `sumar(otra)` (que retornan una `Matriz` nueva) y `__str__`, que la muestra como tabla.

Es el ejemplo 1 del bloque 2 de la [clase 14](../../../README.md) (diapositivas 51 a 56). La clase **encapsula** la lista de listas: quien la usa no toca los datos directamente, sino a través de métodos.

Para verla construida método por método: notebook [La clase `Matriz`, paso a paso](../../notebooks/clase_matriz_paso_a_paso.ipynb).

## Los archivos

```
📁 matriz_poo/
   📄 matriz.py — la clase Matriz
   📄 test_matriz.py — las pruebas con assert
   📄 main.py — un programa que usa la clase con las notas del curso
```

| Archivo | Contenido |
|---|---|
| [matriz.py](matriz.py) | La clase `Matriz`, con la especificación de cada método |
| [test_matriz.py](test_matriz.py) | Pruebas del constructor, de `set` con posiciones inválidas (fila que no existe y columna negativa), de las sumas, de `transpuesta` y `sumar` (que no modifican el original) y de `__str__` |
| [main.py](main.py) | Guarda las notas de 4 estudiantes en 3 parciales en una `Matriz` y muestra la tabla, el promedio de cada estudiante, el de cada parcial y la transpuesta. No pide datos |

`test_matriz.py` y `main.py` hacen `from matriz import Matriz`: los tres archivos deben estar en la misma carpeta.

## Cómo ejecutarlo

```
cd clases/14/teoria/codigo/matriz_poo
python test_matriz.py
python main.py
```

En Spyder: abra cada archivo y ejecútelo con **F5**.

## Salida esperada

Las pruebas:

```
Pruebas de Matriz: todas pasaron
```

El programa:

```
Notas:
   3.0   3.5   2.5
   4.5   4.0   5.0
   2.0   3.0   3.5
   4.0   4.5   3.0
Ana: 3.00
Beto: 4.50
Carla: 2.83
Dario: 3.83
Parcial 1: 3.38
Parcial 2: 3.75
Parcial 3: 3.50
Transpuesta (una fila por parcial):
   3.0   4.5   2.0   4.0
   3.5   4.0   3.0   4.5
   2.5   5.0   3.5   3.0
```

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'matriz'` | Se ejecutó desde otra carpeta | Entrar a la carpeta `matriz_poo` antes de ejecutar |
| `AttributeError: 'Matriz' object has no attribute '__datos'` | Se intentó usar `m.__datos` desde afuera de la clase | Los datos son privados: usar `m.get(i, j)` y `m.set(i, j, valor)` |
| Un valor "no se guarda" y no hay mensaje | `set` recibió una posición inválida y retornó `False` | Revisar lo que retorna `set`: `if not m.set(i, j, v): ...` |
| `IndexError` en `sumar` | Las dos matrices no tienen el mismo tamaño | Es lo que exige el *Supone* de `sumar` |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
