![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sala de cine: una matriz de objetos

## Qué hace

> Una sala de cine tiene filas identificadas con letras (A, B, C, …) y sillas numeradas desde 1. La boleta vale $5000. Se necesita ver el mapa de la sala (X ocupada, O libre), vender una boleta para una silla, liberar una silla, contar las sillas libres de cada fila y de toda la sala, y saber cuánto se ha recaudado.

Es el ejemplo 2 del bloque 2 de la [clase 14](../../../README.md) (diapositivas 57 a 61), adaptado de un ejercicio de Mera Banguero. La sala guarda sus sillas en una **matriz de objetos `Silla`**, que crea en su constructor (**composición**). El público cuenta con letras y desde 1, y la matriz desde 0: la conversión se hace en un solo lugar, `get_silla`.

Para verla construida paso a paso: notebook [Sala de cine: una matriz de objetos, paso a paso](../../notebooks/sala_cine_paso_a_paso.ipynb). Es el mismo camino del [laboratorio 5](../../../../../laboratorios/5/README.md) (el parqueadero), con otro problema.

## Los archivos

```
📁 sala_cine/
   📄 silla.py — la clase Silla
   📄 sala.py — la clase Sala (importa silla.py)
   📄 test_silla.py — las pruebas de Silla
   📄 test_sala.py — las pruebas de Sala
   📄 main.py — el programa con menú
```

| Archivo | Contenido |
|---|---|
| [silla.py](silla.py) | `Silla(fila, numero)`: sabe si está libre, se ocupa y se libera (los dos retornan `bool`); `__str__` da `X` u `O` |
| [sala.py](sala.py) | `Sala(filas, sillas_por_fila, precio)`, con la constante `LETRAS`, `indice_fila`, `es_silla_valida`, `get_silla`, `vender`, `liberar`, `contar_libres_fila`, `contar_libres`, `get_recaudo` y `__str__` (el mapa) |
| [test_silla.py](test_silla.py), [test_sala.py](test_sala.py) | Pruebas de cada clase, incluidas las dos formas de contar y una silla que no existe |
| [main.py](main.py) | Una sala de 5 filas (A a E) de 6 sillas, con el menú: ver el mapa, vender, liberar, resumen y salir |

## Cómo ejecutarlo

Primero las pruebas, en este orden (`Sala` usa `Silla`):

```
cd clases/14/teoria/codigo/sala_cine
python test_silla.py
python test_sala.py
python main.py
```

## Salida esperada

Las pruebas:

```
Pruebas de Silla: todas pasaron
Pruebas de Sala: todas pasaron
```

Una sesión con el menú: se vende C4, se intenta venderla otra vez, se intenta una silla que no existe (D9), se ve el mapa y el resumen, y se escribe una opción inválida. Para abreviar, el menú se muestra completo solo la primera vez:

```
=== Sala de cine ===
1. Ver el mapa
2. Vender una boleta
3. Liberar una silla
4. Resumen
0. Salir
Opcion: 2
Fila (letra): C
Numero de silla: 4
Listo
...
Opcion: 2
Fila (letra): C
Numero de silla: 4
No se pudo: la silla no existe o no esta en ese estado
...
Opcion: 2
Fila (letra): D
Numero de silla: 9
No se pudo: la silla no existe o no esta en ese estado
...
Opcion: 1
   1 2 3 4 5 6
A  O O O O O O
B  O O O O O O
C  O O O X O O
D  O O O O O O
E  O O O O O O
O: libre   X: ocupada
...
Opcion: 4
Fila A: 6 libres
Fila B: 6 libres
Fila C: 5 libres
Fila D: 6 libres
Fila E: 6 libres
Libres en total: 29
Recaudo: $ 5000
...
Opcion: 7
Opcion no valida
...
Opcion: 0
```

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'silla'` (o `'sala'`) | Se ejecutó desde otra carpeta | Entrar a la carpeta `sala_cine` antes de ejecutar |
| "No se pudo" al vender una silla que se ve libre | La fila se escribió en minúscula (`c` en vez de `C`) | Las filas son letras **mayúsculas** |
| `ValueError` al escribir el número de silla | Se escribió algo que no es un número entero | Escribir solo el número: `4` |
| Al cerrar el programa, las ventas se pierden | La sala vive en la memoria | Es el problema que resuelve la [clase 15](../../../../15/README.md) con archivos (`sala_archivo/`) |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
