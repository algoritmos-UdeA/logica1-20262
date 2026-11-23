![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 15 — Código de ejemplo (índice por problema)

Todos los programas usan solo Python (3.11), sin bibliotecas externas.

> [!IMPORTANT]
> Los programas buscan sus archivos de datos **en la carpeta desde la que se ejecutan**. Antes de ejecutar, entre a la carpeta del ejemplo: `cd codigo` para los scripts sueltos, `cd codigo/notas_archivo` o `cd codigo/sala_archivo` para los otros. Si aparece `FileNotFoundError`, revise la carpeta.

Las dos carpetas ([`notas_archivo/`](notas_archivo/README.md) y [`sala_archivo/`](sala_archivo/README.md)) tienen su propio README: qué hace, sus archivos, cómo ejecutarla, la salida esperada y qué hacer si algo falla.

Varios ejemplos **crean archivos** al ejecutarse (`saludo.txt`, `nombres.txt`, `notas_copia.csv`, `notas_finales.csv`, `prueba_*.csv`…). Esos archivos no se suben al repositorio; el [`.gitignore`](.gitignore) de esta carpeta los excluye.

## Archivos de datos

| Archivo | Contenido |
|---|---|
| [trabalenguas.txt](trabalenguas.txt) | Tres líneas de texto, para los ejemplos de lectura |
| [notas.csv](notas.csv) | Encabezado y una línea por estudiante: `nombre,parcial1,parcial2,parcial3` (Ana, Beto, Carla y Dario) |

## 1. Las operaciones con archivos

Un script por cada operación de las diapositivas 13-31.

| Archivo | Qué muestra | Salida (resumida) |
|---|---|---|
| [ej01_abrir_cerrar.py](ej01_abrir_cerrar.py) | `open`, `close` y los atributos `name`, `mode` y `closed` | `Cerrado? False` … `Cerrado? True` |
| [ej02_escribir.py](ej02_escribir.py) | `write` y el `"\n"` | crea `saludo.txt`: `Hola, Ana` / `Hasta pronto` |
| [ej03_escribir_ciclo.py](ej03_escribir_ciclo.py) | Escribir una lista, una línea por elemento; números con f-string | crea `nombres.txt` y `notas.txt` |
| [ej04_w_vs_a.py](ej04_w_vs_a.py) | `"w"` frente a `"a"` | `Juan, Ana` → `Juan, Ana, Clara, Julia` → `Pedro` |
| [ej05_leer_read.py](ej05_leer_read.py) | `read()` y `read(n)` | el trabalenguas, `<class 'str'>`, `Pedro`, ` Pablo ` |
| [ej06_leer_for.py](ej06_leer_for.py) | `for linea in archivo`, con y sin `strip()` | primero con líneas en blanco, después sin ellas |
| [ej07_readline.py](ej07_readline.py) | `readline()` para el encabezado y `while linea != ""` | `Encabezado: nombre,…` y `Dato: Ana,3.0,3.5,2.5` … |
| [ej08_readlines.py](ej08_readlines.py) | `readlines()` | la lista de líneas con sus `"\n"`, `3 lineas` |
| [ej09_split.py](ej09_split.py) | `strip`, `split(",")` y `float` (no usa archivos) | `['Beto', '4.5', '4.0', '5.0']`, `4.54.0`, `8.5` |
| [ej10_leer_csv.py](ej10_leer_csv.py) | Leer `notas.csv` a una lista y una matriz con `append` | `4 estudiantes, 3 parciales` |
| [ej11_escribir_csv.py](ej11_escribir_csv.py) | Escribir un CSV | crea `notas_copia.csv`, igual a `notas.csv` |
| [ej12_with.py](ej12_with.py) | `with`: se cierra solo | `Dentro del with, cerrado? False` / `Fuera del with, cerrado? True` |
| [ej13_no_existe.py](ej13_no_existe.py) | ⚠️ Un nombre mal escrito (`notas.cvs`) | `FileNotFoundError` (a propósito) |
| [ej14_try_except.py](ej14_try_except.py) | Un vistazo a `try`/`except` (no es tema del curso) | `No se encontro el archivo notas.cvs` |

## 2. Funciones con archivos

| Archivo | Contenido |
|---|---|
| [funciones_archivos.py](funciones_archivos.py) | `leer_nombres(nombre_archivo)`, `leer_notas(nombre_archivo)` y `guardar_curso(nombre_archivo, nombres, notas)` |
| [test_funciones_archivos.py](test_funciones_archivos.py) | La prueba escribe su propio `prueba_curso.csv`. Prueba un caso típico, un archivo con solo el encabezado, la ida y vuelta, y que `guardar_curso` reemplaza → `Pruebas de funciones_archivos: todas pasaron` |

## 3. Notas finales desde un archivo — [`notas_archivo/`](notas_archivo/)

> **Enunciado** (diapositiva 37): Leer los nombres y las notas de los tres parciales desde `notas.csv`, calcular la nota final de cada estudiante (30 %, 30 % y 40 %), mostrarla junto con la más alta y la más baja, y guardar el resultado en `notas_finales.csv`.

| Archivo | Contenido |
|---|---|
| [notas.csv](notas_archivo/notas.csv) | Los datos del curso |
| [notas.py](notas_archivo/notas.py) | `leer_nombres` y `leer_notas`; `calcular_notas_finales`, `buscar_mayor` y `buscar_menor`, las mismas de la clase 14; y `guardar_finales` |
| [test_notas.py](notas_archivo/test_notas.py) | Pruebas con sus propios archivos; revisa `prueba_finales.csv` línea por línea → `Pruebas de notas: todas pasaron` |
| [main.py](notas_archivo/main.py) | Lee, calcula, muestra y guarda |

`python main.py` muestra:

```
Notas leidas de notas.csv: 4 estudiantes
Ana: 2.95
Beto: 4.55
Carla: 2.90
Dario: 3.75
Nota final mas alta: 4.55
Nota final mas baja: 2.90
Resultado guardado en notas_finales.csv
```

Y crea `notas_finales.csv`:

```
nombre,final
Ana,2.95
Beto,4.55
Carla,2.90
Dario,3.75
```

## 4. La sala de cine que se guarda — [`sala_archivo/`](sala_archivo/)

> **Enunciado** (diapositiva 42): La sala de cine de la clase 14 pierde sus ventas al cerrar el programa. Agréguele a la clase `Sala` un método `guardar(nombre_archivo)` y un método `cargar(nombre_archivo)`, y escriba una función `cargar_sala(nombre_archivo)` que cree una sala a partir de un archivo. El programa carga la sala al empezar y la guarda al salir.

Formato de `sala.txt`: la primera línea tiene el tamaño y el precio (`5,6,5000`); después va una línea por fila de la sala, con `X` (ocupada) u `O` (libre) por silla.

| Archivo | Contenido |
|---|---|
| [sala.txt](sala_archivo/sala.txt) | El estado inicial: 4 sillas vendidas (A1, B5, B6, C4) |
| [silla.py](sala_archivo/silla.py) | La clase `Silla`, igual a la de la clase 14 |
| [sala.py](sala_archivo/sala.py) | La clase `Sala` de la clase 14, con `guardar` y `cargar`, y la función `cargar_sala` |
| [test_silla.py](sala_archivo/test_silla.py), [test_sala.py](sala_archivo/test_sala.py) | Las pruebas de la clase 14, que siguen pasando |
| [test_sala_archivo.py](sala_archivo/test_sala_archivo.py) | El formato del archivo línea por línea, la ida y vuelta, y cargar sobre una sala con otras ventas → `Pruebas de la sala con archivo: todas pasaron` |
| [main.py](sala_archivo/main.py) | El menú de la clase 14; carga `sala.txt` al empezar y lo guarda con la opción 0 |

| Prueba del programa | Resultado |
|---|---|
| Primera ejecución: vender D3 y salir con 0 | `sala.txt` queda con `OOXOOO` en la fila D |
| Segunda ejecución: ver el mapa | D3 aparece ocupada: la venta no se perdió |

> [!TIP]
> `main.py` modifica `sala.txt`. Para volver al estado inicial, recupérelo del repositorio (`git checkout -- sala.txt`) o vuelva a escribir su contenido.

> [!Important]
> Se usó IA generativa para escribir este código y esta guía a partir de las indicaciones del docente. El docente revisa y valida la versión final.
