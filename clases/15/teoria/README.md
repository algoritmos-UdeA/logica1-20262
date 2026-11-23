![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 15 — Archivos (Teoría)

Diapositivas base del tema 15. Retoman el problema que dejó la [clase 14](../../14/teoria/README.md): al cerrar el programa, los datos se pierden. Presentan los archivos de texto y CSV, las funciones que leen y escriben archivos y cómo probarlas, la solución del problema de las notas finales con archivos, y una sala de cine que se guarda y se carga. Cierran con lo que ya se puede construir con todo el curso. 54 diapositivas.

## Contenido cubierto

- **Apertura y repaso** (diapositivas 1-10):
  - Método de Polya y entrada → proceso → salida.
  - La memoria es volátil y el disco es persistente.
  - Repaso de la matriz de notas de la clase 14 y de "todo dato es un objeto". Desde esta clase se usa `append`, porque al leer un archivo no se sabe cuántos datos hay.
  - El problema pendiente: el programa pide 12 notas cada vez. Una solución ingenua (escribir los datos en el código) y por qué no sirve.
  - Otros casos cotidianos y el plan de la clase.
- **Archivos de texto** (diapositivas 11-32):
  - Qué es un archivo (nombre, extensión, carpeta, texto o binario) y el ciclo **abrir → procesar → cerrar**.
  - `open(nombre_archivo, modo)` con la tabla de los modos `"r"`, `"w"` y `"a"`; el objeto archivo y sus atributos `name`, `mode` y `closed`.
  - **Escribir:** `write` no agrega `"\n"`; varias líneas con un ciclo; `write` solo recibe texto. ⚠️ `"w"` borra lo que había.
  - **Leer:** `read()` y `read(n)`, `for linea in archivo` (y la línea en blanco que deja el `"\n"`), `readline()` con `while linea != ""` y `readlines()`. Una tabla compara cuándo usar cada forma, basada en *Practical Programming* y en el material de Informática 2.
  - **Del texto al dato:** `strip`, `split(",")` y `float`, y cómo armar listas con `append`.
  - **CSV:** el mismo archivo en el bloc de notas y en una hoja de cálculo. Advertencia: Excel en español usa `;` y coma decimal. Cómo leer y escribir un CSV.
  - **`with`**, la carpeta de trabajo y el `FileNotFoundError`, el *buffer* (por qué hay que cerrar), los errores típicos (en rojo los silenciosos), un vistazo a `try`/`except` y una tabla resumen.
- **Funciones con archivos** (diapositivas 33-36):
  - `leer_nombres`, `leer_notas` y `guardar_curso` reciben el nombre del archivo. Hay dos funciones de lectura porque una función retorna una sola cosa. El *Garantiza* de `guardar_curso` dice CREA o REEMPLAZA.
  - Para probarlas, la prueba escribe su propio archivo, y una prueba de **ida y vuelta** guarda y vuelve a leer.
- **El problema resuelto** (diapositivas 37-41):
  - Leer `notas.csv`, calcular las notas finales (reutilizando la clase 14) y guardar `notas_finales.csv`.
  - Árbol top-down, `main.py` con su salida y el archivo generado.
  - Pruebas que revisan el archivo línea por línea.
  - ¿Qué fue incómodo?: el archivo se lee dos veces, los datos van sueltos y el formato está repetido. Eso lleva a los objetos.
- **Bloque 2: archivos y objetos** (diapositivas 42-48):
  - La sala de cine de la clase 14 pierde sus ventas al cerrar.
  - El formato de `sala.txt` (tamaño y precio en la primera línea, una línea `X`/`O` por fila) y el UML con los métodos nuevos.
  - `guardar` recorre la matriz de objetos escribiendo `str(silla)`. `cargar` modifica la sala según el archivo. La función `cargar_sala` crea la sala a partir del archivo, y `main` carga al empezar y guarda al salir.
  - Pruebas de ida y vuelta.
- **Cierre** (diapositivas 49-54):
  - Resumen y "Lo que ya se puede construir": todos los temas del curso y para qué sirven en un programa.
  - Para explorar: el módulo `csv` con `DictReader`, `os.path.exists`, JSON y archivos binarios.
  - Referencias y cierre.

> [!NOTE]
> Python Tutor no permite abrir archivos. Por eso solo tienen enlace de simulación las diapositivas 5, 6 y 22, que no usan archivos. En las demás, el contenido de cada archivo se muestra en una caja tipo bloc de notas.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-15.pdf](clase-15.pdf) | Diapositivas completas del tema 15, en PDF. |
| [clase-15.pptx](clase-15.pptx) | Diapositivas completas del tema 15, editable (PowerPoint, 54 diapositivas). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas. |
| [images/](images/) | Exportación en `.png` de los diagramas. |
| [codigo/](codigo/) | Scripts de los ejemplos. Su [README](codigo/README.md) explica cada problema y cómo ejecutarlo. |
| [notebooks/](notebooks/) | Tres notebooks: uno que acompaña las diapositivas ([archivos.ipynb](notebooks/archivos.ipynb)) y dos que construyen paso a paso las notas finales desde un archivo y la sala que se guarda. Ver el [README de la clase](../README.md#notebooks). |

### Diagramas

| Diagrama | Contenido |
|---|---|
| [memoria_disco](images/memoria_disco.png) | La memoria (volátil) y el disco (persistente); escribir y leer entre los dos. |
| [matriz_notas](images/matriz_notas.png) | Copia de la clase 12/14: las notas de 4 estudiantes en 3 parciales. |
| [ciclo_archivo](images/ciclo_archivo.png) | Abrir → procesar → cerrar. |
| [w_vs_a](images/w_vs_a.png) | `lista.txt` después de `"w"`, de `"a"` y otra vez de `"w"`. |
| [lectura_lineas](images/lectura_lineas.png) | Cada línea termina con `"\n"`; `for linea in archivo` da una por vuelta. |
| [split_linea](images/split_linea.png) | `"Beto,4.5,4.0,5.0\n"` → `strip` → `split(",")` → `float`. |
| [csv_hoja](images/csv_hoja.png) | El mismo CSV en el bloc de notas y en una hoja de cálculo. |
| [csv_a_listas](images/csv_a_listas.png) | De `notas.csv` a la lista `nombres` y la matriz `notas`. |
| [carpeta_trabajo](images/carpeta_trabajo.png) | El archivo se busca en la carpeta desde la que se ejecuta el programa. |
| [buffer](images/buffer.png) | `write` → buffer → disco; `close()` vacía el buffer. |
| [funciones_archivos](images/funciones_archivos.png) | Las cajas negras de `leer_nombres`, `leer_notas` y `guardar_curso`. |
| [ida_y_vuelta](images/ida_y_vuelta.png) | La prueba de ida y vuelta: guardar, leer y comparar. |
| [flujo_notas_archivo](images/flujo_notas_archivo.png) | `notas.csv` → `main.py` → `notas_finales.csv`. |
| [arbol_notas_archivo](images/arbol_notas_archivo.png) | Árbol top-down del problema (gris: de la clase 14; verde: nuevo). |
| [sala_ejecuciones](images/sala_ejecuciones.png) | Dos ejecuciones de la sala: lo vendido en la primera sigue en la segunda. |
| [sala_archivo_formato](images/sala_archivo_formato.png) | La sala en memoria y `sala.txt` en el disco, con `guardar` y `cargar`. |
| [uml_sala_archivo](images/uml_sala_archivo.png) | `Sala` con `guardar` y `cargar`, la `Silla` y la función `cargar_sala`. |

Cada imagen tiene su fuente con el mismo nombre en [diagramas/](diagramas/).

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisa y valida la versión final.
