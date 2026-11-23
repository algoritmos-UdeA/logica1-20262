![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 14 — Arreglos bidimensionales (matrices) (Teoría)

Diapositivas base del tema 14. Siguen el mismo camino de la [clase 11](../../11/teoria/README.md) (arreglos), con una dimensión más. La clase empieza con un repaso: la lista usada como arreglo, los tres casos de funciones con listas y el arreglo de objetos de la clase 13. Después retoma el problema que dejó la clase 12: **varias notas por estudiante**. Define la matriz y la lista de listas usada como matriz, y presenta cada operación en pseudocódigo y en Python. Sigue con las funciones con matrices y la solución del problema pendiente en tres archivos. Termina con dos ejemplos de matrices y objetos: una clase `Matriz` y una sala de cine que guarda objetos `Silla`. 68 diapositivas.

## Contenido cubierto

- **Apertura y repaso** (diapositivas 1-7):
  - Método de Polya y entrada → proceso → salida.
  - Una imagen es una matriz de píxeles: cada píxel está en una fila y una columna. CS50x trabaja así las imágenes en el problema *Filter*.
  - Repaso de la lista usada como arreglo, de los tres casos de funciones con listas (con alias y copia) y del arreglo de objetos (`Banco` de la clase 13).
- **El problema pendiente** (diapositivas 8-10):
  - Enunciado: nombres de los estudiantes y sus notas en tres parciales que valen 30 %, 30 % y 40 %. Se pide la nota final de cada uno y quiénes tienen la más alta y la más baja.
  - Solución ingenua: un arreglo por parcial (`notas1`, `notas2`, `notas3`). Son arreglos paralelos otra vez, y los parciales no se pueden recorrer con un ciclo.
  - Otro caso: las ventas de tres sucursales en seis meses. La pregunta es cómo guardar una tabla completa bajo un solo nombre.
- **Definición** (diapositivas 11-14):
  - Qué es una matriz: un solo tipo, filas y columnas, tamaño fijo `N × M`, dos índices.
  - Sus partes: identificador, elemento, fila `i`, columna `j`, tamaño. En `notas[i][j]` siempre va primero la fila.
  - Arreglo frente a matriz: una fila de la matriz es un arreglo; la matriz es un arreglo de arreglos.
  - La **lista de listas usada como matriz**, con las reglas del curso: todas las filas con `M` casillas, un solo tipo, tamaño fijo.
- **Operaciones, en pseudocódigo y Python** (diapositivas 15-34):
  - **Crear** con `notas = Matriz(N, M)`, que en Python se hace en dos pasos: `[0.0] * N` y después una fila nueva por vuelta. ⚠️ `[[0.0] * M] * N` repite la **misma fila** N veces sin dar error.
  - **Guardar y leer**; el índice como expresión, con un ejercicio cuya respuesta está en la diapositiva.
  - **La clave:** dos índices, dos ciclos.
  - **Llenar** por teclado y por expresión (`aprobo[i][j] = notas[i][j] >= 3.0`).
  - **Recorrer:** mostrar como tabla con `end="  "` y `print()`, recorrer por elemento (`for fila in notas`) y recorrer por columnas intercambiando los ciclos.
  - **Acumular:** el total con prueba de escritorio; por fila (el promedio de cada estudiante, con el acumulador que se reinicia en cada fila); por columna (el promedio de cada parcial; la columna 0 es el arreglo de la clase 11).
  - **Salirse de la matriz:** `N` y `M` intercambiados dan `IndexError`, o un recorrido incompleto que no avisa. Un índice negativo tampoco da error.
  - **Otros recorridos** en una tabla (una fila, una columna, diagonales, triangulares). En las **matrices cuadradas**, las diagonales y las triangulares toman ejemplos de Mera Banguero.
  - **Mayor y su posición** (quién y en qué parcial), y **buscar** con `fila = -1`, sin `break`, porque `break` solo sale del ciclo interno.
  - **Transpuesta y suma:** crean una matriz nueva.
  - **Copiar:** `alias = notas` no copia nada, y `list(notas)` o `notas[:]` copian solo la lista de filas, así que las filas se comparten. Se **clona con dos ciclos**.
  - Resumen en tabla.
- **Funciones con matrices** (diapositivas 35-41): los tres casos, cada uno con definición, invocación y pruebas. Las funciones usan `len(m)` para las filas y `len(m[0])` para las columnas.
  - **Caso 1:** `calcular_promedio_fila(notas, i)` recibe la matriz y devuelve un valor. Pruebas: típico, 1 × 1, solo la fila pedida, no modifica.
  - **Caso 2:** `leer_notas(n, m)` devuelve una matriz nueva. Usa `input()`, así que se prueba ejecutando.
  - **Caso 3:** `aplicar_bonificacion(notas, j, puntos)` modifica la columna `j`, con tope de 5.0.
  - Tabla resumen de los tres casos.
- **El problema resuelto** (diapositivas 42-49):
  - Entender (Polya) y calcular a mano: Beto tiene la nota más alta (4.55) y Carla la más baja (2.90). `nombres` es paralelo a las filas y `pesos`, a las columnas.
  - Árbol top-down.
  - `calcular_notas_finales` con su prueba de escritorio. Las cuentas tienen errores de redondeo (`0.3 * 3.0` da `0.8999999999999999` y la nota de Carla, `2.9000000000000004`), por eso se usa `round` y `:.2f`.
  - Los empates con `posiciones_iguales`: el patrón de `posiciones_mayores_que` de la clase 11 (contar, crear del tamaño justo, llenar), sin `append`.
  - Los tres archivos y `main.py` con su salida.
  - ¿Qué fue incómodo? Datos sueltos, índices sin protección, crear y copiar a mano, operaciones aparte. Eso lleva al bloque 2.
- **Bloque 2: matrices y objetos** (diapositivas 50-61):
  - **Ejemplo 1 – clase `Matriz`:**
    - Enunciado al estilo Liang y UML (`datos : float[*][*]`).
    - Constructor que crea la lista de listas por dentro; `get`; `set` que valida con `es_posicion_valida` y retorna `bool`.
    - `sumar_fila`, `sumar_columna` y `es_cuadrada`; `transpuesta()` y `sumar(otra)`, que **crean otro objeto `Matriz`** sin modificar el original.
    - Pruebas, uso y comparación entre funciones sobre listas y la clase.
  - **Ejemplo 2 – sala de cine**, adaptado de Mera Banguero:
    - `Silla` (fila, número, ocupada) y `Sala`, que **crea** sus sillas en una matriz de objetos (composición).
    - Dos formas de contar: el público dice **C4** y la matriz guarda `sillas[2][3]`. La conversión se hace en un solo lugar, `get_silla`.
    - Vender, contar libres y el mapa X/O.
- **Cierre** (diapositivas 62-68):
  - Errores típicos, con los silenciosos en rojo: filas alias, copia superficial, acumulador fuera del ciclo.
  - Resumen de la clase.
  - Un problema que todavía no se puede resolver bien: al cerrar el programa, los datos se pierden. Abre el tema de archivos.
  - Para explorar: comprensiones de listas, NumPy, multiplicación de matrices como reto e imágenes y juegos de tablero.
  - Referencias y cierre.

> [!NOTE]
> Convenciones de esta clase, las mismas de los arreglos:
>
> - La matriz se crea **sin `append`**, en dos pasos.
> - Las operaciones básicas usan `N` y `M`; `len()` aparece cuando la matriz entra a una función.
> - El pseudocódigo escribe `Matriz(N, M)` y `notas[i][j]`, sin tipos. Las funciones se muestran solo en Python.
> - Una posición se retorna como una lista de dos enteros, `[fila, columna]`, porque las tuplas no se han visto.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-14.pdf](clase-14.pdf) | Diapositivas completas del tema 14, en PDF. |
| [clase-14.pptx](clase-14.pptx) | Diapositivas completas del tema 14, editable (PowerPoint, 68 diapositivas). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas (ver la tabla siguiente). |
| [images/](images/) | Exportación en `.png` de los diagramas de `diagramas/`. |
| [codigo/](codigo/) | Scripts de los ejemplos. Su [README](codigo/README.md) reúne el **enunciado** de cada problema con los archivos que lo resuelven. |
| [notebooks/](notebooks/) | Cuatro notebooks: uno que acompaña las diapositivas ([matrices.ipynb](notebooks/matrices.ipynb)) y tres que construyen paso a paso las notas finales, la clase `Matriz` y la sala de cine. Ver el [README de la clase](../README.md#notebooks). |

### Diagramas

| Diagrama | Contenido |
|---|---|
| [matriz_pixeles](images/matriz_pixeles.png) | Una imagen de 8 × 8 como matriz de ceros y unos, y cómo se ve. |
| [arreglo_notas](images/arreglo_notas.png), [tres_casos_funciones](images/tres_casos_funciones.png), [arreglo_cuentas](images/arreglo_cuentas.png) | Copias de las clases 11 y 13 para el repaso. |
| [matriz_notas](images/matriz_notas.png) | Copia de la clase 12: las notas de 4 estudiantes en 3 parciales, `notas[2][1] = 3.0`. |
| [vectores_por_parcial](images/vectores_por_parcial.png) | La solución ingenua: tres arreglos con tres nombres distintos. |
| [ventas_sucursal_mes](images/ventas_sucursal_mes.png) | Ventas de tres sucursales en seis meses. |
| [matriz_definicion](images/matriz_definicion.png) | Un arreglo por parcial (tres nombres) frente a una matriz (un nombre). |
| [partes_matriz](images/partes_matriz.png) | Identificador, fila 2, columna 1, elemento `notas[2][1]` y tamaño. |
| [arreglo_vs_matriz](images/arreglo_vs_matriz.png) | Un índice frente a dos índices. |
| [lista_de_listas](images/lista_de_listas.png) | La matriz en memoria: una lista de filas, cada una una lista. |
| [filas_alias](images/filas_alias.png) | `[[0.0] * M] * N`: las 4 casillas apuntan a una sola fila; la forma correcta, una fila por vuelta. |
| [ejercicio_indices_matriz_inicial](images/ejercicio_indices_matriz_inicial.png), [ejercicio_indices_matriz_final](images/ejercicio_indices_matriz_final.png) | Las matrices A y B antes y después del ejercicio del índice como expresión. |
| [recorrido_filas](images/recorrido_filas.png), [recorrido_columnas](images/recorrido_columnas.png) | El orden en que se visita cada casilla. |
| [suma_por_fila](images/suma_por_fila.png), [suma_por_columna](images/suma_por_columna.png) | Un resultado por fila (promedio de cada estudiante) y por columna (promedio de cada parcial). |
| [diagonales](images/diagonales.png), [triangulares](images/triangulares.png) | Diagonal principal y secundaria; triangular superior e inferior, en una matriz de 4 × 4. |
| [transpuesta](images/transpuesta.png), [suma_matrices](images/suma_matrices.png) | La transpuesta de 2 × 3 a 3 × 2 y la suma casilla por casilla. |
| [alias_matriz](images/alias_matriz.png), [copia_superficial](images/copia_superficial.png), [clonar_matriz](images/clonar_matriz.png) | Alias, copia con `list()` (filas compartidas) y clon con dos ciclos. |
| [tres_casos_matriz](images/tres_casos_matriz.png), [caja_caso1](images/caja_caso1.png), [caja_caso2](images/caja_caso2.png), [caja_caso3](images/caja_caso3.png) | Las cajas negras de las tres funciones con matrices. |
| [arbol_notas_matriz](images/arbol_notas_matriz.png) | Árbol top-down del problema de las notas finales (gris: ya vista; verde: nueva). |
| [modulos_notas_matriz](images/modulos_notas_matriz.png) | Los tres archivos de `notas_matriz/`, sus `import` y las salidas. |
| [uml_matriz](images/uml_matriz.png), [objetos_matriz](images/objetos_matriz.png) | El UML de `Matriz` y los dos objetos que deja `t = notas.transpuesta()`. |
| [uml_sala_cine](images/uml_sala_cine.png) | `Sala` ◆── `Silla` (composición). |
| [sala_mapa](images/sala_mapa.png), [sala_memoria](images/sala_memoria.png), [sala_dos_numeraciones](images/sala_dos_numeraciones.png) | El mapa de la sala, la matriz de objetos `Silla` en memoria y la conversión de C4 a `sillas[2][3]`. |

Cada imagen tiene su fuente con el mismo nombre en [diagramas/](diagramas/).

## Código de ejemplo

Ver [codigo/README.md](codigo/README.md): allí está cada problema con su enunciado, los archivos y la salida real. Todo se ejecuta con Python 3.11, sin bibliotecas externas.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisa y valida la versión final.
