![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# La sala de cine que se guarda

## Qué hace

> La sala de cine de la clase 14 pierde sus ventas al cerrar el programa. Agréguele a la clase `Sala` un método `guardar(nombre_archivo)` y un método `cargar(nombre_archivo)`, y escriba una función `cargar_sala(nombre_archivo)` que cree una sala a partir de un archivo. El programa carga la sala al empezar y la guarda al salir.

Es el bloque 2 de la [clase 15](../../../README.md) (diapositivas 42 a 48). Parte de la sala de la clase 14 ([`sala_cine/`](../../../../14/teoria/codigo/sala_cine/)): las ventas ahora **sobreviven** al programa.

Para verla construida paso a paso, con dos ejecuciones simuladas: notebook [La sala de cine que se guarda, paso a paso](../../notebooks/sala_archivo_paso_a_paso.ipynb).

### El formato de `sala.txt`

```
5,6,5000
XOOOOO
OOOOXX
OOOXOO
OOOOOO
OOOOOO
```

La primera línea tiene el tamaño y el precio: filas, sillas por fila y precio de la boleta. Después va una línea por fila de la sala (A, B, C…), con `X` para una silla ocupada y `O` para una libre. El archivo inicial tiene vendidas A1, B5, B6 y C4.

## Los archivos

```
📁 sala_archivo/
   📄 sala.txt — el estado de la sala (lo lee y lo reescribe main.py)
   📄 silla.py — la clase Silla, igual a la de la clase 14
   📄 sala.py — la clase Sala de la clase 14 + guardar, cargar y cargar_sala
   📄 test_silla.py — las pruebas de Silla (de la clase 14)
   📄 test_sala.py — las pruebas de Sala (de la clase 14)
   📄 test_sala_archivo.py — las pruebas de guardar, cargar y cargar_sala
   📄 main.py — el programa con menú
```

| Archivo | Contenido |
|---|---|
| [sala.py](sala.py) | Además de lo de la clase 14: `guardar` recorre la matriz de objetos escribiendo `str(silla)`, `cargar` deja cada silla como dice el archivo (MODIFICA la sala), y `cargar_sala` lee la primera línea, crea la sala con ese tamaño y la carga |
| [test_sala_archivo.py](test_sala_archivo.py) | Revisa el archivo línea por línea, la **ida y vuelta** (guardar y cargar da la misma sala) y cargar sobre una sala con otras ventas. Deja `prueba_sala.txt` en la carpeta (no se sube al repositorio) |
| [main.py](main.py) | El menú de la clase 14: carga `sala.txt` al empezar y lo guarda con la opción **0. Guardar y salir** |

## Cómo ejecutarlo

**Desde esta carpeta**, donde está `sala.txt`. Primero las pruebas, en este orden:

```
cd clases/15/teoria/codigo/sala_archivo
python test_silla.py
python test_sala.py
python test_sala_archivo.py
python main.py
```

## Salida esperada

Las pruebas:

```
Pruebas de Silla: todas pasaron
Pruebas de Sala: todas pasaron
Pruebas de la sala con archivo: todas pasaron
```

**Primera ejecución:** se ve el mapa cargado del archivo, se vende D3 y se sale con 0. Para abreviar, el menú se muestra completo solo la primera vez:

```
Sala cargada de sala.txt

=== Sala de cine ===
1. Ver el mapa
2. Vender una boleta
3. Liberar una silla
4. Resumen
0. Guardar y salir
Opcion: 1
   1 2 3 4 5 6
A  X O O O O O
B  O O O O X X
C  O O O X O O
D  O O O O O O
E  O O O O O O
O: libre   X: ocupada
...
Opcion: 2
Fila (letra): D
Numero de silla: 3
Listo
...
Opcion: 0
Sala guardada en sala.txt
```

`sala.txt` queda con `OOXOOO` en la fila D.

**Segunda ejecución:** la venta de D3 sigue ahí.

```
Sala cargada de sala.txt
...
Opcion: 1
   1 2 3 4 5 6
A  X O O O O O
B  O O O O X X
C  O O O X O O
D  O O X O O O
E  O O O O O O
O: libre   X: ocupada
...
Opcion: 4
Fila A: 5 libres
Fila B: 4 libres
Fila C: 5 libres
Fila D: 5 libres
Fila E: 6 libres
Libres en total: 25
Recaudo: $ 25000
...
Opcion: 0
Sala guardada en sala.txt
```

> [!TIP]
> `main.py` **modifica** `sala.txt`. Para volver al estado inicial, recupérelo del repositorio (`git checkout -- sala.txt`) o copie otra vez el contenido de la sección [El formato de `sala.txt`](#el-formato-de-salatxt).

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `FileNotFoundError: [Errno 2] No such file or directory: 'sala.txt'` | Se ejecutó desde otra carpeta | Entrar a la carpeta `sala_archivo` antes de ejecutar |
| Las ventas no quedaron guardadas | Se cerró el programa sin la opción 0 (por ejemplo, con Ctrl+C o cerrando la ventana) | Salir siempre con **0. Guardar y salir** |
| `IndexError: string index out of range` al cargar | `sala.txt` tiene menos filas o sillas de las que dice su primera línea | Revisar el archivo: la primera línea debe coincidir con las filas que siguen |
| `ValueError` o `IndexError` al cargar | La primera línea de `sala.txt` tiene algo que no es un número (`ValueError`) o le faltan datos (`5,6`: `IndexError`) | Debe tener tres números enteros separados por comas, como `5,6,5000` |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
