![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 12 — Ordenamiento y búsqueda (Teoría)

Diapositivas base del tema 12, que continúa la [clase 11](../../11/teoria/README.md). Empiezan con un repaso de la lista usada como arreglo, de los tres casos de funciones con listas y de la diferencia entre alias y copia. Luego retoman el problema que quedó pendiente: los nombres y las notas de un curso guardados en dos **arreglos paralelos**. Para resolverlo se estudian dos tareas básicas: **buscar** (búsqueda lineal y búsqueda binaria) y **ordenar** (selección, burbuja e inserción, construidos sobre la función `intercambiar`). Cada algoritmo sigue el mismo camino: la idea con un diagrama, el algoritmo con una traza en consola, la función con su especificación (*Supone / Garantiza*) y las pruebas con `assert`. La clase termina con un programa integrador, la administración de notas de un curso, cuyas incomodidades motivan los temas siguientes: la programación orientada a objetos y las matrices. 63 diapositivas.

## Contenido cubierto

- **Apertura y repaso** (diapositivas 1-6): método de Polya, entrada → proceso → salida, y tres repasos de la clase 11:
  - la lista usada como arreglo, recorrida con el índice como variable;
  - los tres casos de funciones con listas (retorna un valor, retorna una lista nueva, o modifica la lista que recibe). Los métodos de ordenamiento de esta clase son del **caso 3**;
  - alias y copia: `B = A` no copia; `B = list(A)` o `B = A[:]` sí. Ordenar en el lugar modifica la lista original, así que para conservarla primero se hace una copia.
- **El problema pendiente** (diapositivas 7-10): nombres y notas en dos arreglos paralelos, donde la misma posición corresponde al mismo estudiante. Quedan tres preguntas: ¿cómo se muestra el listado de mayor a menor nota?, ¿cuál es la nota de Carla? y, si se ordena `notas`, ¿cómo se mantiene cada nombre unido a su nota? La primera y la tercera piden ordenar; la segunda pide buscar.
  - **Ordenar** es reorganizar los datos según un criterio, llamado **clave**, en orden ascendente o descendente: canciones por título, correos por fecha (el más reciente primero), productos por precio, archivos por nombre, y en este curso, estudiantes por nota.
  - **¿Buscar en desorden o en orden?**: en una guía telefónica de 1000 páginas, ordenada por apellido, se puede buscar página por página (búsqueda lineal, hasta 1000 pasos) o abrir por la mitad y descartar la otra mitad (búsqueda binaria, unos 10 pasos, pero solo si está ordenada). Idea tomada de CS50x, Lecture 3.
  - **Plan de la clase**: buscar en desorden, ordenar, buscar en orden, y resolver el problema pendiente. Todo con funciones: caja negra, *Supone / Garantiza* y pruebas con `assert`.
- **Búsqueda lineal** (diapositivas 11-16): se recorre el arreglo desde la posición 0 y se compara cada elemento con el valor buscado; al encontrarlo, se guarda su posición y se detiene el recorrido con `break`. Si no está, la posición queda en `-1`, que sirve porque ninguna posición válida es negativa. Funciona aunque el arreglo no esté ordenado.
  - Se presenta en pseudocódigo y en Python, y después como la función `buscar_lineal(lista, valor)`, que usa `len(lista)` porque no recibe `N`. Es del caso 1: retorna una posición y no modifica la lista.
  - **Pruebas**: típico (en el medio), límite (el primero y el último) y especiales (no está, está repetido → la primera aparición, lista vacía).
  - **¿Cuál es la nota de Carla?**: se busca `"Carla"` en `nombres` y la posición encontrada se usa en `notas`. Si el nombre no está, `pos` vale `-1` y no se debe usar `notas[pos]`: Python devolvería la última nota sin dar error.
  - **¿Cuántas comparaciones hace?**: en el mejor caso, 1 (el valor está en la primera posición); en el peor, `N` (está en la última o no está). Si `N` se duplica, el peor caso también.
- **Intercambio** (diapositivas 17-22): los tres métodos de ordenamiento se basan en intercambiar dos elementos. Si se escribe `X[i] = X[j]` y luego `X[j] = X[i]`, el valor de `X[i]` se pierde; por eso se usa una variable temporal `temp` que lo guarda antes de sobrescribirlo.
  - **Propio de Python**: `X[i], X[j] = X[j], X[i]` intercambia en una sola línea, porque Python evalúa primero todo el lado derecho y después asigna. C, Java y el pseudocódigo no lo permiten; por eso los algoritmos de la clase se escriben con `temp`.
  - **`intercambiar(lista, i, j)`**: el intercambio como función del caso 3 (MODIFICA la lista, sin `return`). Para probarla, se llama y después se revisa la lista, creando `X` otra vez antes de cada prueba.
  - **`posicion_menor(lista, inicio)`**: retorna la posición del menor desde `inicio` hasta el final (caso 1). Además de los casos típico, límite y especial, se prueba que la lista no cambió.
- **Ordenamiento por selección** (diapositivas 23-26): en cada pasada se busca el menor de la parte sin ordenar y se intercambia con la primera posición de esa parte, como quien escoge de un mazo la carta más baja y la pone a la izquierda. Con `N` elementos se hacen `N - 1` pasadas. El algoritmo se muestra con un `print` por pasada; al convertirlo en función, cada comentario se vuelve una llamada (`posicion_menor` e `intercambiar`): el nombre de la función reemplaza al comentario.
  - **Pruebas**: el ejemplo de la clase, una lista ya ordenada, una al revés, una con repetidos y una de un solo elemento. Como la función no retorna nada, se llama y después se revisa la lista. **Error frecuente**: `assert ordenar_seleccion(X) == [...]` falla siempre, porque la función retorna `None`.
- **Ordenamiento por burbuja** (diapositivas 27-29): se recorre la lista comparando vecinos y se intercambian si están en desorden. En cada pasada el mayor "sube" hasta el final, así que cada pasada revisa un elemento menos (`N - 1 - i`). Si una pasada no hizo intercambios (`hubo_intercambio` en `False`), la lista ya está ordenada y se sale con `break`. Como función, el `temp` se reemplaza por `intercambiar(lista, j, j + 1)`, la misma de la selección.
- **Ordenamiento por inserción** (diapositivas 30-33): como al ordenar cartas en la mano, se toma la siguiente y se mete en su lugar entre las que ya están ordenadas. Un `while` desplaza una casilla a la derecha los elementos mayores que el actual, y al final el actual se coloca en el hueco. Durante el desplazamiento un número aparece repetido por un momento (por ejemplo, `[10, 14, 29, 37, 37]`): no es un error, es el hueco que se va corriendo. Inserción **no intercambia, desplaza**: es el único de los tres métodos que no usa `intercambiar`.
- **Comparación** (diapositivas 34-35): por fuera los tres métodos son iguales (reciben una lista, la dejan ordenada y no retornan nada); por dentro trabajan distinto. Número de comparaciones de cada uno:

  | Método | Ya ordenado (mejor caso) | Ejemplo `[29, 10, 14, 37, 13]` | Al revés (peor caso) | 1000 al azar |
  |---|---|---|---|---|
  | Selección | 10 | 10 | 10 | 499 500 |
  | Burbuja | 4 | 10 | 10 | 498 554 |
  | Inserción | 4 | 8 | 10 | 246 325 |

  Selección siempre busca el menor completo, aunque ya esté en su lugar; con 1000 elementos al azar, inserción hace cerca de la mitad de comparaciones que los otros dos. Los tres ordenan bien: la diferencia es cuánto trabajan.
- **Búsqueda binaria** (diapositivas 36-43): si la lista está ordenada, se abre en la mitad, se ve si el buscado está antes o después y se descarta la otra mitad. Tres variables marcan la parte que todavía se revisa: `inicio`, `fin` y `medio = (inicio + fin) // 2`. Si `X[medio]` es menor que el buscado, `inicio = medio + 1`; si es mayor, `fin = medio - 1`; si `inicio` pasa a `fin`, no está.
  - Se usa `while` y no `for`, porque no se sabe de antemano cuántos pasos habrá, con el mismo patrón de la búsqueda lineal: `pos = -1` al inicio y `break` al encontrarlo.
  - **El *Supone* es nuevo y obligatorio**: la lista debe estar ordenada de menor a mayor. La función no lo revisa; es responsabilidad de quien la llama. Las pruebas usan la lista de la búsqueda lineal ordenada, `[2.87, 3.5, 4.0, 5.0]`, e incluyen buscar un valor menor que todos, mayor que todos y en un hueco. La lista original, de mayor a menor, queda como "Así NO".
  - **Lineal frente a binaria**: en el peor caso, la lineal revisa todo y la binaria descarta la mitad en cada paso. Si se duplica `N`, la lineal hace el doble de comparaciones y la binaria solo una más (con un millón de elementos: 1 000 000 frente a 20). La lineal sirve si la lista no está ordenada o se busca una sola vez; la binaria, si ya está ordenada o se va a buscar muchas veces.
- **Integrador: administración de notas de un curso** (diapositivas 44-56): un curso admite máximo `N = 10` estudiantes; de cada uno se guarda su id (texto), su nombre y su nota. Hay 4 inscritos, y el programa permite agregar, eliminar, actualizar, buscar, listar y ordenar con un menú. En la clase se implementan en detalle las opciones 6 y 7 (ordenar); el resto usa lo visto en clases anteriores y está en el repositorio.
  - **El arreglo parcialmente lleno**: se crean tres vectores de tamaño `N` y una variable `cantidad`, que dice cuántas casillas están ocupadas (de 0 a `cantidad - 1`) y cuál es la próxima libre. Por eso las funciones reciben `cantidad` y recorren hasta ahí, no hasta `len()`.
  - **Primer intento**, `ordenar_seleccion(notas)` tal como está: todos quedan con 0.0, porque la función recorre las 10 casillas y los seis 0.0 de las libres son los menores.
  - **Segundo intento**, hasta `cantidad` y de mayor a menor con `posicion_mayor_nota`, pero moviendo solo `notas`: las notas quedan bien ordenadas, pero los nombres no se movieron, y ahora Ana "tiene" el 4.5 de Beto.
  - **La solución**: `intercambiar_estudiantes` llama tres veces a `intercambiar`, una por vector y con las mismas posiciones. `ordenar_por_nota` es la selección con tres cambios: `posicion_mayor_nota` en vez de `posicion_menor`, `cantidad` en vez de `len()` e `intercambiar_estudiantes` en vez de `intercambiar`. `ordenar_por_nombre` es la misma función, comparando nombres con `<` (Python compara textos letra por letra, como en el diccionario).
  - **Pruebas**: además de los casos típicos, hay algo nuevo que probar: cada estudiante conserva su Id, nombre y nota, y las casillas libres no se tocan. Casos especiales: notas repetidas, un solo estudiante y el curso vacío.
  - **Diseño y archivos**: `main` muestra el menú y llama una función por opción. Son los mismos tres archivos de siempre (`curso.py`, `test_curso.py` y `main.py`), y `curso.py` importa `intercambiar` de `ordenamientos.py`.
- **¿Qué fue incómodo?** (diapositivas 57-59): un estudiante no existe como tal (son tres vectores que comparten una posición); cada intercambio son tres; `cantidad` va a todas partes y las funciones que la cambian tienen que retornarla; y hay una función de ordenar por cada criterio, casi idénticas. ¿Qué pasa si mañana se agrega el correo? Un vector más y cambios en varias funciones.
  - **La próxima clase (POO)**: un `Estudiante` guarda juntos su Id, su nombre y su nota, y un `Curso` tiene a sus estudiantes. El menú es el mismo. Se resuelven las tres primeras incomodidades; la de una función por criterio sigue igual.
  - **Otra pregunta**: ¿y si hay varias notas por estudiante? Un vector por parcial serían más vectores paralelos; mejor una tabla donde la fila `i` es un estudiante y la columna `j` una evaluación: una **matriz**, `notas[i][j]`.
- **Lo que Python ya trae** (diapositiva 60): `sorted(lista)` retorna una lista nueva ordenada y no cambia la original; `lista.sort()` modifica la lista y no retorna nada (caso 3, como `ordenar_seleccion`); con `reverse=True` ordenan de mayor a menor.
- **Resumen** (diapositiva 61) y **referencias** (diapositiva 62): material de Mera Banguero, la [guía de ordenamiento de Python](https://docs.python.org/3/howto/sorting.html), el material de Algoritmos y Programación del [Politécnico Colombiano JIC](https://github.com/algoritmos-poli/sesiones_presenciales), [CS50x 2026, Lecture 3](https://cs50.harvard.edu/x/2026/notes/3/), Lambert, *Fundamentals of Python: Data Structures*, cap. 3 (la función *swap* como pieza reutilizable), [CS Comics](https://www.cs-comics.com/how-an-array-of-integers-gets-stored-in-memory/) y [Python Tutor](https://pythontutor.com), donde se pueden ejecutar los enlaces de simulación de las diapositivas.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-12.pdf](clase-12.pdf) | Diapositivas completas del tema 12, en PDF. |
| [clase-12.pptx](clase-12.pptx) | Diapositivas completas del tema 12, editable (PowerPoint, 63 diapositivas). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas (ver la tabla siguiente). |
| [images/](images/) | Exportación en `.png` de los diagramas de `diagramas/`. |
| [codigo/](codigo/) | Scripts de los ejemplos (ver [Código de ejemplo](#código-de-ejemplo)). Su [README](codigo/README.md) reúne el **enunciado** de cada problema con los archivos que lo resuelven. |

### Diagramas

Cada fuente de `diagramas/` tiene su imagen, con el mismo nombre, en `images/`.

| Fuente (`diagramas/`) | Imagen | Contenido |
|---|---|---|
| [plan_clase12.drawio](diagramas/plan_clase12.drawio) | [plan_clase12.png](images/plan_clase12.png) | El plan de la clase: buscar en desorden, ordenar, buscar en orden y el problema pendiente. |
| [alias_lista_c12.drawio](diagramas/alias_lista_c12.drawio) | [alias_lista_c12.png](images/alias_lista_c12.png) | Repaso: `alias = notas`, dos nombres para una sola lista. |
| [copia_lista_c12.drawio](diagramas/copia_lista_c12.drawio) | [copia_lista_c12.png](images/copia_lista_c12.png) | Repaso: `copia = notas[:]` o `list(notas)`, dos listas distintas. |
| [conservar_original.drawio](diagramas/conservar_original.drawio) | [conservar_original.png](images/conservar_original.png) | Para conservar el original, primero se copia y después se ordena la copia. No se usa en las diapositivas. |
| [busqueda_guia.drawio](diagramas/busqueda_guia.drawio) | [busqueda_guia.png](images/busqueda_guia.png) | La guía telefónica de 1000 páginas: página por página (hasta 1000 pasos) frente a abrir por la mitad (unos 10 pasos). |
| [busqueda_lineal_traza.drawio](diagramas/busqueda_lineal_traza.drawio) | [busqueda_lineal_traza.png](images/busqueda_lineal_traza.png) | Traza de la búsqueda lineal de 3.5 en `[5.0, 4.0, 3.5, 2.87]`: se detiene con `break` en la posición 2. |
| [caja_negra_buscar_lineal.drawio](diagramas/caja_negra_buscar_lineal.drawio) | [caja_negra_buscar_lineal.png](images/caja_negra_buscar_lineal.png) | `buscar_lineal` como caja negra: entran la lista y el valor, sale la posición. |
| [busqueda_paralelos.drawio](diagramas/busqueda_paralelos.drawio) | [busqueda_paralelos.png](images/busqueda_paralelos.png) | ¿Cuál es la nota de Carla?: se busca en `nombres` y la posición encontrada se usa en `notas`. |
| [intercambio_temporal.drawio](diagramas/intercambio_temporal.drawio) | [intercambio_temporal.png](images/intercambio_temporal.png) | El intercambio con `temp`, paso a paso. |
| [intercambio_python.drawio](diagramas/intercambio_python.drawio) | [intercambio_python.png](images/intercambio_python.png) | `X[i], X[j] = X[j], X[i]`: Python evalúa el lado derecho y después asigna. |
| [caja_negra_intercambiar.drawio](diagramas/caja_negra_intercambiar.drawio) | [caja_negra_intercambiar.png](images/caja_negra_intercambiar.png) | `intercambiar` como caja negra: sale la misma lista, modificada, sin `return`. |
| [caja_negra_posicion_menor.drawio](diagramas/caja_negra_posicion_menor.drawio) | [caja_negra_posicion_menor.png](images/caja_negra_posicion_menor.png) | `posicion_menor` como caja negra: `posicion_menor([29, 10, 14, 37, 13], 2)` devuelve 4. |
| [seleccion_pasadas.drawio](diagramas/seleccion_pasadas.drawio) | [seleccion_pasadas.png](images/seleccion_pasadas.png) | Las 4 pasadas de la selección sobre `[29, 10, 14, 37, 13]`. |
| [caja_negra_ordenar_seleccion.drawio](diagramas/caja_negra_ordenar_seleccion.drawio) | [caja_negra_ordenar_seleccion.png](images/caja_negra_ordenar_seleccion.png) | `ordenar_seleccion` como caja negra (caso 3). |
| [burbuja_pasadas.drawio](diagramas/burbuja_pasadas.drawio) | [burbuja_pasadas.png](images/burbuja_pasadas.png) | Las pasadas de la burbuja, comparación por comparación; en la pasada 4 no hay intercambios y se detiene. |
| [caja_negra_ordenar_burbuja.drawio](diagramas/caja_negra_ordenar_burbuja.drawio) | [caja_negra_ordenar_burbuja.png](images/caja_negra_ordenar_burbuja.png) | `ordenar_burbuja` como caja negra (caso 3). |
| [insercion_pasadas.drawio](diagramas/insercion_pasadas.drawio) | [insercion_pasadas.png](images/insercion_pasadas.png) | Las 4 pasadas de la inserción: la parte ordenada (verde), el actual (amarillo) y la parte sin revisar. |
| [insercion_desplazamiento.drawio](diagramas/insercion_desplazamiento.drawio) | [insercion_desplazamiento.png](images/insercion_desplazamiento.png) | La última pasada de la inserción (`actual = 13`): los mayores se desplazan y 13 se inserta en la posición 1. |
| [caja_negra_ordenar_insercion.drawio](diagramas/caja_negra_ordenar_insercion.drawio) | [caja_negra_ordenar_insercion.png](images/caja_negra_ordenar_insercion.png) | `ordenar_insercion` como caja negra (caso 3). |
| [arbol_ordenamientos.drawio](diagramas/arbol_ordenamientos.drawio) | [arbol_ordenamientos.png](images/arbol_ordenamientos.png) | Qué funciones de apoyo usa cada método: selección usa `posicion_menor` e `intercambiar`, burbuja usa `intercambiar`, inserción ninguna. |
| [comparacion_metodos.drawio](diagramas/comparacion_metodos.drawio) | [comparacion_metodos.png](images/comparacion_metodos.png) | Número de comparaciones de los tres métodos en cuatro situaciones. |
| [busqueda_binaria_traza.drawio](diagramas/busqueda_binaria_traza.drawio) | [busqueda_binaria_traza.png](images/busqueda_binaria_traza.png) | Traza de la búsqueda binaria de 15 en `[2, 5, 10, 12, 15, 17, 20]`: 3 pasos. |
| [caja_negra_buscar_binaria.drawio](diagramas/caja_negra_buscar_binaria.drawio) | [caja_negra_buscar_binaria.png](images/caja_negra_buscar_binaria.png) | `buscar_binaria` como caja negra: la lista debe entrar ordenada. |
| [lineal_vs_binaria.drawio](diagramas/lineal_vs_binaria.drawio) | [lineal_vs_binaria.png](images/lineal_vs_binaria.png) | Comparaciones en el peor caso para `N` de 10 a 1000 millones: la binaria necesita a lo sumo 30. |
| [arreglo_parcial.drawio](diagramas/arreglo_parcial.drawio) | [arreglo_parcial.png](images/arreglo_parcial.png) | Los tres vectores de tamaño 10 con 4 casillas ocupadas: `cantidad = 4` es también la próxima casilla libre. |
| [intercambio_paralelo.drawio](diagramas/intercambio_paralelo.drawio) | [intercambio_paralelo.png](images/intercambio_paralelo.png) | `intercambiar_estudiantes(…, 0, 1)`: el estudiante se mueve en los tres vectores, con las tres llamadas a `intercambiar`. |
| [intercambio_paralelo_sin_codigo.drawio](diagramas/intercambio_paralelo_sin_codigo.drawio) | [intercambio_paralelo_sin_codigo.png](images/intercambio_paralelo_sin_codigo.png) | El mismo diagrama, sin las líneas de código. |
| [paralelos_ordenados.drawio](diagramas/paralelos_ordenados.drawio) | [paralelos_ordenados.png](images/paralelos_ordenados.png) | El curso antes y después de `ordenar_por_nota`: cada Id y nombre sigue unido a su nota. |
| [arbol_curso.drawio](diagramas/arbol_curso.drawio) | [arbol_curso.png](images/arbol_curso.png) | Diagrama top-down del integrador: en verde, la parte de ordenar; en azul, el resto del menú; en gris, `intercambiar`, reutilizada. |
| [modulos_curso.drawio](diagramas/modulos_curso.drawio) | [modulos_curso.png](images/modulos_curso.png) | Los archivos del integrador (`main.py`, `test_curso.py`, `curso.py` y `ordenamientos.py`) y sus `import`. |
| [uml_curso.drawio](diagramas/uml_curso.drawio) | [uml_curso.png](images/uml_curso.png) | Adelanto de POO: las clases `Curso` y `Estudiante` en UML. |
| [matriz_notas.drawio](diagramas/matriz_notas.drawio) | [matriz_notas.png](images/matriz_notas.png) | Adelanto de matrices: una tabla de notas con un estudiante por fila y una evaluación por columna; `notas[2][1]` es 3.0. |

> [!NOTE]
> La imagen `arbol_ordenamientos.png` todavía dice "funciones de apoyo (bloque 3)" en la leyenda, que viene de una versión anterior de la presentación. La fuente `.drawio` ya tiene la leyenda actualizada; falta volver a exportar la imagen.

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/busquedas.py](codigo/busquedas.py) | `buscar_lineal` y `buscar_binaria`. Al ejecutarlo imprime `2` (3.5 en `[5.0, 4.0, 3.5, 2.87]`) y `4` (15 en `[2, 5, 10, 12, 15, 17, 20]`). |
| [codigo/test_busquedas.py](codigo/test_busquedas.py) | Pruebas de las dos búsquedas → `Pruebas de busquedas: todas pasaron`. Tiene comentada la prueba "Así NO" con la lista de mayor a menor. |
| [codigo/ordenamientos.py](codigo/ordenamientos.py) | `intercambiar`, `posicion_menor` y los tres métodos. Al ejecutarlo, los tres ordenan `[29, 10, 14, 37, 13]` y dan `[10, 13, 14, 29, 37]`. |
| [codigo/test_ordenamientos.py](codigo/test_ordenamientos.py) | Pruebas de las funciones de apoyo y de los tres métodos con los mismos cinco casos → `Pruebas de ordenamientos: todas pasaron`. Tiene comentada la prueba "Así NO", que falla porque los métodos retornan `None`. |
| [codigo/curso/](codigo/curso/) | El integrador en tres archivos (`curso.py`, `test_curso.py` y `main.py`), más una copia de `ordenamientos.py` de la que `curso.py` importa `intercambiar`. Se ejecuta desde su propia carpeta: `python test_curso.py` → `Pruebas de curso: todas pasaron`, y después `python main.py`. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
