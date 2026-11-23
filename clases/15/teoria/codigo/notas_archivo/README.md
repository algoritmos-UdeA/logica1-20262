![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Notas finales desde un archivo

## Qué hace

> Leer los nombres y las notas de los tres parciales desde `notas.csv`, calcular la nota final de cada estudiante (30 %, 30 % y 40 %), mostrarla junto con la más alta y la más baja, y guardar el resultado en `notas_finales.csv`.

Es el problema integrador de la [clase 15](../../../README.md) (diapositivas 37 a 41). El cálculo es el mismo de la clase 14 ([`notas_matriz/`](../../../../14/teoria/codigo/notas_matriz/)). Lo nuevo es de dónde vienen los datos y a dónde van: **ya no hay que escribir las notas cada vez**, porque están en el archivo.

Para verlo construido función por función: notebook [Notas finales desde un archivo, paso a paso](../../notebooks/notas_archivo_paso_a_paso.ipynb).

## Los archivos

```
📁 notas_archivo/
   📄 notas.csv — los datos del curso (entrada)
   📄 notas.py — las funciones
   📄 test_notas.py — las pruebas con assert
   📄 main.py — el programa principal
```

Al ejecutar aparecen archivos nuevos en la carpeta: `notas_finales.csv` (lo escribe `main.py`) y `prueba_notas.csv` y `prueba_finales.csv` (los escriben las pruebas). No se suben al repositorio.

| Archivo | Contenido |
|---|---|
| [notas.csv](notas.csv) | Encabezado `nombre,parcial1,parcial2,parcial3` y una línea por estudiante |
| [notas.py](notas.py) | `leer_nombres` y `leer_notas` (leen el CSV), `calcular_notas_finales`, `buscar_mayor` y `buscar_menor` (las mismas de la clase 14) y `guardar_finales` (escribe el CSV de salida) |
| [test_notas.py](test_notas.py) | Las pruebas escriben su propio archivo con datos conocidos y revisan, línea por línea, el archivo que escribe `guardar_finales` |
| [main.py](main.py) | Lee `notas.csv`, calcula, muestra y guarda `notas_finales.csv`. No pide nada por teclado |

## Cómo ejecutarlo

**Desde esta carpeta**, donde está `notas.csv`:

```
cd clases/15/teoria/codigo/notas_archivo
python test_notas.py
python main.py
```

## Salida esperada

Las pruebas:

```
Pruebas de notas: todas pasaron
```

El programa:

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

Y el archivo que crea, `notas_finales.csv`:

```
nombre,final
Ana,2.95
Beto,4.55
Carla,2.90
Dario,3.75
```

Para otro curso no hay que cambiar el programa: basta con cambiar `notas.csv`.

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `FileNotFoundError: [Errno 2] No such file or directory: 'notas.csv'` | Se ejecutó desde una carpeta donde no hay `notas.csv` (por ejemplo, `python codigo/notas_archivo/main.py` desde `teoria/`) | Entrar a la carpeta `notas_archivo` antes de ejecutar |
| El programa funciona, pero `notas_finales.csv` aparece en otra carpeta | Se ejecutó desde `codigo/`, que tiene **otro** `notas.csv` de ejemplo: el programa leyó ese y escribió ahí | Igual: ejecutar desde `notas_archivo` |
| `ValueError: could not convert string to float: '0;3'` | El archivo se guardó con Excel en español, que separa con `;` y usa coma decimal (`Ana;3,0;3,5;2,5`) | Revisar el archivo en el bloc de notas: comas entre los datos y punto decimal (`Ana,3.0,3.5,2.5`) |
| `IndexError: list index out of range` en `calcular_notas_finales` | `notas.csv` tiene una línea en blanco: se leyó como un estudiante sin notas | Borrar las líneas en blanco del archivo |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
