![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 11 — Arreglos unidimensionales y listas (Teoría)

Diapositivas base del tema 11, que continúa la [clase 10](../../10/teoria/README.md). Empiezan con un repaso de funciones y de la organización de un programa en tres archivos. Luego retoman el problema que quedó pendiente en la clase 10, contar cuántas notas son mayores que el promedio, que no se puede resolver con una sola variable. Para resolverlo se presenta el **arreglo**: una variable que guarda muchos valores del mismo tipo bajo un solo nombre, a los que se llega por su **índice**. En Python el arreglo se escribe con una **lista usada como arreglo**, con reglas. Cada operación básica se muestra en pseudocódigo y en Python, lado a lado: crear, guardar y leer, llenar, recorrer, acumular, comparar vecinos y clonar. Después se estudian las **funciones con listas** en tres casos, y la clase termina resolviendo el problema de la clase 10 con diseño top-down y un programa en tres archivos. 51 diapositivas.

## Contenido cubierto

- **Repaso** (diapositivas 2-7): método de Polya, entrada → proceso → salida, la imagen de *CS Comics* sobre cómo se guarda un arreglo en memoria, y lo que ya se sabe de funciones: `def`, `return`, nombre con verbo, especificación (*Supone / Garantiza*), la invocación (definir una función no la ejecuta), y la convención de los tres archivos: funciones (`conversiones.py`), pruebas con `assert` (`test_conversiones.py`) y programa principal (`main.py`) con `def main()` y la guarda `if __name__ == "__main__":`.
- **Motivación** (diapositivas 8-10):
  - **El problema pendiente**: leer las notas de un curso y mostrar cuántas son mayores que el promedio. El promedio solo se conoce después de leer todas las notas, y para entonces la variable `nota` solo conserva la última. Con 3.0, 4.5, 2.0 y 4.0, el programa calcula el promedio 3.38, pero en `nota` solo queda 4.0.
  - **Una variable por nota**: con 4 estudiantes funciona (`nota1` a `nota4`, cuatro `if`), pero con 40 serían 40 variables, 40 lecturas y 40 `if`. Y no se puede usar un ciclo, porque cada variable tiene un nombre distinto. Observación: si los datos se van a usar después de leerlos, hay que guardarlos todos.
  - **Los empleados del señor Burns**: registrar la identificación de cada empleado de la planta nuclear obliga a crear una variable nueva por empleado (`id_lenny`, `id_carl`…). ¿Existe una forma de guardar muchos valores bajo un solo nombre?
- **¿Qué es un arreglo?** (diapositivas 11-13): una variable que guarda muchos valores bajo un solo nombre. Todos los valores son del mismo tipo, se guardan en casillas contiguas de la memoria, el tamaño se decide al crearlo y no cambia, y a cada valor se llega por su posición. Vocabulario: **identificador** (`notas`), **elemento** (por ejemplo, `4.5`), **índice** o posición (en `notas[1]`, el índice es 1) y **tamaño** (4). Las posiciones empiezan en 0: si el arreglo tiene `N` elementos, la última posición es `N - 1`.

  | Ventajas | Limitaciones |
  |---|---|
  | Muchos datos bajo un solo nombre | El tamaño es fijo: no crece ni se encoge |
  | Se recorren con un ciclo, sin importar cuántos datos sean | Todos los elementos deben ser del mismo tipo |
  | Se llega a cualquier elemento directamente por su posición | Un arreglo muy grande ocupa mucha memoria, aunque no se use completo |

- **La lista usada como arreglo** (diapositiva 14): una lista de Python puede hacer más cosas que un arreglo, pero en este curso se usa con las reglas del arreglo. Idea clave: "en Python el arreglo se escribe con una lista, pero la disciplina del arreglo la pone el programador".

  | La lista en Python permite… | Usada como arreglo, en este curso… |
  |---|---|
  | Crecer y encogerse: `append()`, `remove()` | Tamaño fijo: se crea con `[0.0] * N` y no cambia |
  | Mezclar tipos: `[1, "oso", 2.5, True]` | Un solo tipo: todos reales, todos enteros, etc. |
  | Índices negativos: `notas[-1]` | Acceso por posición de 0 a `N - 1` |

  Las operaciones propias de las listas, como `notas.append(5.0)`, son operaciones de objetos y se verán en Programación Orientada a Objetos.
- **Crear un arreglo** (diapositiva 15): en pseudocódigo, `notas = Arreglo(N)`; en Python, `notas = [0.0] * N`, porque cada casilla necesita un valor inicial y el operador `*` repite el valor `N` veces. Si ya se conocen los valores, se crea e inicializa a la vez: `notas = [3.0, 4.5, 2.0, 4.0]`, igual en los dos.
- **Guardar y leer valores** (diapositiva 16): cada casilla se usa como una variable normal. Solo cambian `Leer`/`Escribir` por `input()`/`print()`; el acceso con corchetes, `notas[i]`, es igual en los dos.
- **El índice puede ser una expresión** (diapositiva 17): `notas[i]`, `notas[i + 1]`, `notas[N - 1]`, e incluso el valor de otro arreglo. Se propone un ejercicio con dos arreglos `A` y `B`, que se puede copiar tal cual en Python para comprobar la respuesta.

  <details>
  <summary>Respuesta del ejercicio</summary>

  `B` queda así: `[10, 1, 6, -1, 5, 7, -2, -21]`. Por ejemplo, en la última instrucción, `A[6] % A[5]` es `17 % 10 = 7`, y `A[A[7] + A[5]]` es `A[-3 + 10] = A[7] = -3`; entonces `B[7] = -3 + 6 * -3 = -21`.

  </details>

- **La clave: el índice es una variable** (diapositiva 18): con índices fijos se escribe una línea por casilla; con el índice como variable dentro de un ciclo, una sola línea sirve para cualquier `N`. Con ese patrón se llena (`Leer(notas[i])`), se muestra (`Escribir(notas[i])`), se acumula (`suma = suma + notas[i]`) y se cuenta (`Si notas[i] > x Entonces cont = cont + 1`). Cita de Farrell, cap. 6: "El verdadero beneficio de utilizar un arreglo está en su capacidad para usar una variable como un subíndice".
- **Llenar un arreglo** (diapositiva 19): con valores leídos por teclado, o calculados con una expresión. Por ejemplo, `aprobo[i] = notas[i] >= 3.0` llena un arreglo de valores lógicos.
- **Recorrer y mostrar** (diapositiva 20): por índice (`for i in range(N)`), que da la posición y sirve para leer y modificar, o por elemento (`for nota in notas`), que es más corto pero no da la posición y solo sirve para leer. El recorrido por elemento existe en Python y en otros lenguajes, pero no en el pseudocódigo.
- **Recorrer y acumular** (diapositiva 21): la suma de las notas con su prueba de escritorio (3.0 → 7.5 → 9.5 → 13.5) y el promedio, 3.38. Como las notas quedan en el arreglo, después de calcular el promedio se pueden volver a recorrer: eso era lo que faltaba para resolver el problema de la clase 10.
- **Cuidado con salirse del arreglo** (diapositiva 22): con `range(N + 1)` (o `Para (i = 0, N, 1)`), las cuatro notas se muestran bien, pero en la última vuelta `i` vale 4 y el programa se detiene con `IndexError: list index out of range`. Un recorrido completo va de 0 a `N - 1`.
- **Otros recorridos** (diapositivas 23-24): el recorrido inverso es `range(N - 1, -1, -1)`, con límite `-1` porque `range` no incluye el final. Con `range(N - 1, 0, -1)` el ciclo se salta la posición 0 **sin dar error**. Para cualquier recorrido hay que responder tres preguntas: desde dónde, hasta dónde y de a cuánto.

  | Recorrido | Pseudocódigo | Python | Posiciones (N = 6) |
  |---|---|---|---|
  | Completo | `Para (i = 0, N - 1, 1)` | `range(N)` | 0, 1, 2, 3, 4, 5 |
  | Inverso | `Para (i = N - 1, 0, -1)` | `range(N - 1, -1, -1)` | 5, 4, 3, 2, 1, 0 |
  | Desde la segunda | `Para (i = 1, N - 1, 1)` | `range(1, N)` | 1, 2, 3, 4, 5 |
  | Hasta la penúltima | `Para (i = 0, N - 2, 1)` | `range(N - 1)` | 0, 1, 2, 3, 4 |
  | Posiciones pares | `Para (i = 0, N - 1, 2)` | `range(0, N, 2)` | 0, 2, 4 |
  | Posiciones impares | `Para (i = 1, N - 1, 2)` | `range(1, N, 2)` | 1, 3, 5 |
  | Primera mitad | `Para (i = 0, N // 2 - 1, 1)` | `range(N // 2)` | 0, 1, 2 |
  | Segunda mitad | `Para (i = N // 2, N - 1, 1)` | `range(N // 2, N)` | 3, 4, 5 |

- **Comparar vecinos** (diapositiva 25): ¿la nota de un estudiante subió de una evaluación a la siguiente? Se compara `notas[i + 1]` con `notas[i]`, recorriendo hasta la penúltima posición (`range(N - 1)`): con 4 notas hay 3 comparaciones, y si `i` llegara a 3 se compararía con `notas[4]`, que no existe.
- **Asignar una lista no la copia** (diapositiva 26): con variables, `b = a` y luego `b = 5.0` no cambia `a`. Con listas, `copia = notas` le pone otro nombre (un **alias**) a la misma lista: después de `copia[0] = 5.0`, `notas` también cambió.
- **Clonar una lista** (diapositivas 27-28): crear una lista nueva y copiarle los valores casilla por casilla con un recorrido, o en Python con `notas[:]` (rebanada completa) o `list(notas)`. En los tres casos, cambiar `copia` ya no cambia `notas`.
- **Resumen de operaciones** (diapositiva 29): una tabla pseudocódigo | Python con todas las operaciones anteriores, más el último elemento (`A[N - 1]`, y en Python también `A[-1]`). Observación: toda operación sobre un arreglo completo es un recorrido.
- **Funciones con listas** (diapositivas 30-39): una lista puede entrar a una función, salir de ella, o entrar y salir modificada. Lo que distingue cada caso es qué entra, qué sale y si la lista cambia. Cada caso se presenta con su definición, su invocación (con diagrama de caja negra) y sus pruebas.

  | | Caso 1 | Caso 2 | Caso 3 |
  |---|---|---|---|
  | Ejemplo | `calcular_promedio(notas)` | `leer_notas(n)` | `aplicar_bonificacion(notas, puntos)` |
  | Entra | una lista | un valor | una lista (y un valor) |
  | Sale (`return`) | un valor | una lista nueva | nada |
  | ¿Modifica la lista? | No | — (la crea) | Sí |
  | *Garantiza* dice | "No modifica notas" | "Retorna una lista nueva" | "MODIFICA la lista" |
  | Se invoca | `prom = calcular_promedio(lista_notas)` | `lista_notas = leer_notas(4)` | `aplicar_bonificacion(lista_notas, 0.5)` |
  | Se prueba | `assert` sobre el valor que devuelve | Ejecutando el programa (usa `input`) | Llamar y después revisar la lista |

  - **Caso 1**: la función no recibe `N`; con `len(notas)` sabe cuántos elementos tiene, así sirve para listas de cualquier tamaño. Al invocarla, el parámetro `notas` es un alias de la lista que se pasó. Además de los casos típico, límite y especial, se prueba el contrato: la lista sigue igual después de la llamada.
  - **Caso 2**: aquí sí se usa `n` en el `range`, porque la lista todavía no existe. La lista se crea dentro de la función, pero no se pierde: `return` la entrega afuera.
  - **Caso 3**: `aplicar_bonificacion` suma `puntos` a cada nota sin pasar de `NOTA_MAXIMA = 5.0`. La lista cambia afuera porque el parámetro es un alias: `[3.0, 4.5, 2.0, 4.0]` con 0.5 queda `[3.5, 5.0, 2.5, 4.5]`. Si no se quiere modificar la original, se pasa un clon: `aplicar_bonificacion(lista_notas[:], 0.5)`.
- **Volviendo al problema** (diapositivas 40-47): el enunciado se amplía a "mostrar el promedio, cuántas notas son mayores que el promedio y en qué posiciones están". Ejemplo: 3.0, 4.5, 2.0, 4.0 → promedio 3.38, 2 notas mayores, en las posiciones `[1, 3]`.
  - **Diseño top-down**: entrada → proceso → salida. Dos funciones ya existen y solo se reutilizan (`leer_notas` y `calcular_promedio`); faltan dos, `contar_mayores_que` y `posiciones_mayores_que`, y la segunda usa a la primera.
  - **Especificación**: las dos reciben la lista y un `valor` (no el promedio, para que sirvan con cualquier número) y no modifican la lista. `posiciones_mayores_que` combina dos casos: recibe una lista (caso 1) y devuelve una lista nueva (caso 2).
  - **Implementación**: `contar_mayores_que` es el patrón contar dentro de una función. `posiciones_mayores_que`, sin `append`, primero cuenta cuántas posiciones habrá, crea `[0] * cantidad` del tamaño justo, y la llena con un segundo índice `k` que marca la siguiente casilla libre. Las dos tienen su prueba de escritorio con `valor = 3.375`.
  - **Tres archivos**: `notas.py` (las cinco funciones: dos reutilizadas, dos nuevas y `mostrar_resultados`), `test_notas.py` y `main.py`, que valida con un `while` que `n > 0` (el *Supone* de las funciones) antes de llamarlas. `main()` se lee como el árbol: leer → calcular → buscar → mostrar.
- **Resumen de la clase** (diapositiva 48): cuando los datos se usan después de leerlos, hay que guardarlos todos; la clave es usar el índice como variable dentro de un ciclo; con listas, `=` crea un alias y para copiar se clona; si una función modifica la lista que recibe, su *Garantiza* debe decirlo.
- **Un problema que todavía no se puede resolver bien** (diapositiva 49): además de las notas, se tienen los nombres de los estudiantes. Mostrar quién sacó la mejor nota y el listado ordenado de la nota mayor a la menor. ¿Cómo se sabe a quién pertenece cada nota? ¿Cómo se encuentra la mayor nota y dónde está? Si se ordenan las notas, ¿cómo se mantiene cada nombre unido a su nota? Es el punto de partida de la [clase 12](../../12/README.md).
- Referencias (diapositiva 50): Mera Banguero, *Guía teórica 05: Arreglos unidimensionales*; [CS50x, Lecture 2: Arrays](https://cs50.harvard.edu/x/notes/2/); [CS50P, Lecture 2: Loops](https://cs50.harvard.edu/python/notes/2/) (listas); [MIT 6.100L, Lecture 11: Aliasing and Cloning](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_lec11.pdf); Farrell, *Introducción a la programación: lógica y diseño*, cap. 6; [CS Comics](https://www.cs-comics.com/how-an-array-of-integers-gets-stored-in-memory/); y [Python Tutor](https://pythontutor.com), donde se pueden ejecutar los enlaces de simulación de las diapositivas.

> [!NOTE]
> Los docstrings de `recorrido_suma.py`, `indices_python.py` y `funciones_listas.py` citan los números de diapositiva de una versión anterior de la presentación. En la versión actual, ese material corresponde a las diapositivas 15-21, 14, 20 y 22, y 30-39, respectivamente.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-11.pdf](clase-11.pdf) | Diapositivas completas del tema 11, en PDF. |
| [clase-11.pptx](clase-11.pptx) | Diapositivas completas del tema 11, editable (PowerPoint, 51 diapositivas). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas (ver la tabla siguiente). |
| [images/](images/) | Exportación en `.png` de los diagramas de `diagramas/`. |
| [codigo/](codigo/) | Scripts de los ejemplos (ver [Código de ejemplo](#código-de-ejemplo)). |

### Diagramas

Cada fuente de `diagramas/` tiene su imagen, con el mismo nombre, en `images/`.

| Fuente (`diagramas/`) | Imagen | Contenido |
|---|---|---|
| [repaso_caja_negra.drawio](diagramas/repaso_caja_negra.drawio) | [repaso_caja_negra.png](images/repaso_caja_negra.png) | Repaso: la función `celsius_a_fahrenheit` como caja negra. |
| [repaso_flujo_main.drawio](diagramas/repaso_flujo_main.drawio) | [repaso_flujo_main.png](images/repaso_flujo_main.png) | Repaso: quién llama a la función y qué recibe de vuelta. |
| [repaso_modulos.drawio](diagramas/repaso_modulos.drawio) | [repaso_modulos.png](images/repaso_modulos.png) | Repaso: un programa en tres archivos (funciones, pruebas y programa principal). |
| [arreglo_ids_empleados.drawio](diagramas/arreglo_ids_empleados.drawio) | [arreglo_ids_empleados.png](images/arreglo_ids_empleados.png) | Los empleados del señor Burns: una variable por empleado (`id_lenny`, `id_carl`…) frente a un solo arreglo `ids`, donde `ids[2]` → `"003"`. |
| [arreglo_notas.drawio](diagramas/arreglo_notas.drawio) | [arreglo_notas.png](images/arreglo_notas.png) | "Hasta hoy" (una variable `nota`, donde solo queda 4.0) frente a "desde hoy" (el arreglo `notas`): promedio 3.38 y 2 notas mayores, en las posiciones 1 y 3. |
| [arreglo_notas_azul.drawio](diagramas/arreglo_notas_azul.drawio) | [arreglo_notas_azul.png](images/arreglo_notas_azul.png) | El arreglo `notas` con sus posiciones, de 0 a 3. |
| [arreglo_notas_definicion.drawio](diagramas/arreglo_notas_definicion.drawio) | [arreglo_notas_definicion.png](images/arreglo_notas_definicion.png) | Una variable por nota (`nota1` a `nota4`, que no se pueden recorrer con un ciclo) frente a un arreglo: un nombre, muchos valores, `notas[1]` → 4.5. |
| [partes_arreglo.drawio](diagramas/partes_arreglo.drawio) | [partes_arreglo.png](images/partes_arreglo.png) | Partes de un arreglo: identificador, elemento, índice y tamaño; la última posición es `N - 1`. |
| [leer_escribir_arreglo.drawio](diagramas/leer_escribir_arreglo.drawio) | [leer_escribir_arreglo.png](images/leer_escribir_arreglo.png) | `Leer(notas[1])` guarda en la casilla 1 lo que se digita; `Escribir(notas[0])` muestra en pantalla la casilla 0. |
| [ejercicio_indices_inicial.drawio](diagramas/ejercicio_indices_inicial.drawio) | [ejercicio_indices_inicial.png](images/ejercicio_indices_inicial.png) | Ejercicio de índices: los arreglos `A` y `B` antes de las instrucciones. |
| [ejercicio_indices_final.drawio](diagramas/ejercicio_indices_final.drawio) | [ejercicio_indices_final.png](images/ejercicio_indices_final.png) | Ejercicio de índices: el arreglo `B` después de las instrucciones, con las casillas que cambiaron (0, 2, 3 y 7) en verde. Es la respuesta del ejercicio. |
| [alias_lista.drawio](diagramas/alias_lista.drawio) | [alias_lista.png](images/alias_lista.png) | `copia = notas`: dos nombres para la misma lista. |
| [clonar_lista_corta.drawio](diagramas/clonar_lista_corta.drawio) | [clonar_lista_corta.png](images/clonar_lista_corta.png) | Clonar con `notas[:]` o `list(notas)`: dos listas distintas. |
| [clonar_lista_recorrido.drawio](diagramas/clonar_lista_recorrido.drawio) | [clonar_lista_recorrido.png](images/clonar_lista_recorrido.png) | Clonar con un recorrido, casilla por casilla. |
| [tres_casos_funciones.drawio](diagramas/tres_casos_funciones.drawio) | [tres_casos_funciones.png](images/tres_casos_funciones.png) | Los tres casos de funciones con listas. |
| [caja_negra_lista.drawio](diagramas/caja_negra_lista.drawio) | [caja_negra_lista.png](images/caja_negra_lista.png) | Caso 1: `calcular_promedio` como caja negra. |
| [caja_negra_lista_invocacion.drawio](diagramas/caja_negra_lista_invocacion.drawio) | [caja_negra_lista_invocacion.png](images/caja_negra_lista_invocacion.png) | Caso 1: la invocación, con el parámetro como alias de la lista. |
| [caja_negra_caso2.drawio](diagramas/caja_negra_caso2.drawio) | [caja_negra_caso2.png](images/caja_negra_caso2.png) | Caso 2: `leer_notas` como caja negra. |
| [caja_negra_caso2_invocacion.drawio](diagramas/caja_negra_caso2_invocacion.drawio) | [caja_negra_caso2_invocacion.png](images/caja_negra_caso2_invocacion.png) | Caso 2: la invocación; la lista creada adentro sale con `return`. |
| [caja_negra_caso3.drawio](diagramas/caja_negra_caso3.drawio) | [caja_negra_caso3.png](images/caja_negra_caso3.png) | Caso 3: `aplicar_bonificacion` como caja negra. |
| [caja_negra_caso3_invocacion.drawio](diagramas/caja_negra_caso3_invocacion.drawio) | [caja_negra_caso3_invocacion.png](images/caja_negra_caso3_invocacion.png) | Caso 3: la invocación; lo que la función cambia se ve afuera. |
| [arbol_notas.drawio](diagramas/arbol_notas.drawio) | [arbol_notas.png](images/arbol_notas.png) | Diagrama top-down del problema de las notas mayores que el promedio. |
| [cajas_funciones_nuevas.drawio](diagramas/cajas_funciones_nuevas.drawio) | [cajas_funciones_nuevas.png](images/cajas_funciones_nuevas.png) | Las dos funciones nuevas como cajas negras: `contar_mayores_que(notas, 3.375)` devuelve 2 y `posiciones_mayores_que(notas, 3.375)` devuelve `[1, 3]`. |
| [modulos_notas.drawio](diagramas/modulos_notas.drawio) | [modulos_notas.png](images/modulos_notas.png) | El programa en tres archivos: `notas.py`, `test_notas.py` y `main.py`. |
| [arreglos_paralelos.drawio](diagramas/arreglos_paralelos.drawio) | [arreglos_paralelos.png](images/arreglos_paralelos.png) | Nombres y notas en dos arreglos paralelos: la misma posición habla del mismo estudiante. Si se ordena `notas`, ¿cómo se mantiene cada nombre unido a su nota? (el problema que queda para la clase 12). |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/notas_sin_arreglos.py](codigo/notas_sin_arreglos.py) | El problema pendiente de la clase 10 (copia idéntica del de esa clase). Con 3.0, 4.5, 2.0 y 4.0 muestra `Promedio del curso: 3.38` y `Nota guardada en la variable nota: 4.0`. |
| [codigo/recorrido_suma.py](codigo/recorrido_suma.py) | Crear (`[0.0] * N`), llenar por teclado, recorrer y mostrar, y recorrer y acumular. Con 3.0, 4.5, 2.0 y 4.0 muestra cada posición y `Promedio: 3.38`. |
| [codigo/indices_python.py](codigo/indices_python.py) | Índices positivos y negativos (`notas[-1]` es el último), las dos formas de recorrer (por posición y por elemento), y una línea comentada con `notas[4]`: al quitar el `#`, el programa se detiene con `IndexError`. |
| [codigo/funciones_listas.py](codigo/funciones_listas.py) | Los tres casos de funciones con listas (`calcular_promedio`, `leer_notas` y `aplicar_bonificacion`), con sus pruebas con `assert` y un `main()` que muestra la lista antes y después de la bonificación: `[3.0, 4.5, 2.0, 4.0]` → `[3.5, 5.0, 2.5, 4.5]`. |
| [codigo/notas_con_arreglos/](codigo/notas_con_arreglos/) | El problema de la clase 10 resuelto en tres archivos: `notas.py` (las cinco funciones), `test_notas.py` (`python test_notas.py` → `Pruebas de notas: todas pasaron`) y `main.py`. Con 4 estudiantes y las notas del ejemplo muestra `Promedio del curso: 3.38`, `Notas mayores que el promedio: 2` y `Posiciones: [1, 3]`. Se ejecuta desde su propia carpeta. |
| [codigo/repaso_funciones/](codigo/repaso_funciones/) | Repaso de la organización en tres archivos de la clase 10, con una sola función: `conversiones.py` (`celsius_a_fahrenheit`), `test_conversiones.py` y `main.py`. Con 100 °C muestra `100.0 °C = 212.00 °F`. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
