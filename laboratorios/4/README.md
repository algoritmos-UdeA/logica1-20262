![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Laboratorio 4 — Funciones: instrucción asistida por computador

## Antes de empezar

Antes de la sesión de laboratorio, repase el siguiente material:

* **Clase 9** — definición e invocación de funciones, tipos de funciones según sus entradas y salidas, y pruebas con `assert`.
* **Clase 10** — especificación de una función (*Supone / Garantiza*), ámbito de las variables, parámetros con valor por defecto, diseño **top-down** con *stubs*, y uso de librerías (`math`, `random`).
* **Clase 10, módulos propios** — `import`, `__name__`, `def main()` con la guarda, y la comparación de dónde ubicar las pruebas (carpeta [`temperaturas_modulos/`](../../clases/10/teoria/codigo/temperaturas_modulos/)).
* **Ejercicio guiado [Adivina el número](../../clases/10/teoria/codigo/adivina_numero/)** — muestra, paso a paso, el mismo procedimiento que se exige en este laboratorio: diseño top-down, especificación, implementación con stubs y pruebas con `random.seed()`. Su **sección 7** (opción 2: archivo de pruebas aparte) es la organización en archivos que se usa en este laboratorio y en los siguientes.

> [!NOTE]
> Los problemas de este laboratorio están **adaptados** de los ejercicios 5.49 a 5.53 (*Computer-Assisted Instruction*) del libro de P. Deitel y H. Deitel, *C How to Program*, 9.ª edición global, Pearson, 2023, págs. 293-294, disponible en [`material/libros/`](../../material/libros/). El original está planteado en C; aquí se resuelve en Python con las estructuras vistas en el curso.

## Objetivos

Al finalizar este laboratorio, el estudiante estará en capacidad de:

* Descomponer un problema en **funciones** mediante diseño **top-down**, y decidir qué subproblemas merecen una función propia.
* Escribir la **especificación** de cada función (*Supone / Garantiza*) antes de implementarla.
* Separar las funciones que **calculan** (reciben datos y retornan un valor, sin leer ni imprimir) de las que **interactúan** con el usuario, de modo que las primeras puedan probarse con `assert`.
* Utilizar el módulo **`random`** para generar datos al azar, y `random.seed()` para obtener resultados repetibles al probar.
* Utilizar **parámetros con valor por defecto** y **funciones que llaman a otras funciones**.
* Organizar un programa en **varios archivos**: un módulo con las funciones, un archivo de pruebas y un programa principal.
* Usar la **especificación** como contrato entre quien escribe una función y quien la usa.
* Construir un programa de forma **incremental**: cada nivel parte del programa del nivel anterior y le agrega una funcionalidad.

## Herramientas necesarias

* **Anaconda**: distribución de Python que incluye el intérprete y Spyder.
* **Visual Studio Code** (opcional): editor de código con la extensión de Python.
* **draw.io** (opcional): el diagrama top-down puede hacerse a mano; draw.io es una alternativa para dibujarlo en el computador.

## Descripción general

La **instrucción asistida por computador** (*CAI*, por sus siglas en inglés) consiste en usar programas para apoyar el aprendizaje. En este laboratorio se construye, en **cinco niveles**, un programa que ayuda a un estudiante de primaria a practicar operaciones aritméticas:

| Nivel | Funcionalidad que se agrega |
|---|---|
| **1** | Preguntas de multiplicación con números de un dígito; repetir la pregunta hasta acertar |
| **2** | Mensajes variados de acierto y de error, elegidos al azar |
| **3** | Seguimiento del desempeño: porcentaje de aciertos después de 10 respuestas |
| **4** | Niveles de dificultad (cantidad de dígitos de los operandos) |
| **5** | Tipo de operación: suma, resta, multiplicación o mezcla aleatoria |

Cada nivel **parte del programa del nivel anterior**. Por eso se recomienda terminar y probar un nivel completamente antes de pasar al siguiente.

## Organización en archivos

A partir de este laboratorio, los programas del curso se organizan en **tres archivos**, como en la opción 2 del ejercicio guiado [*Adivina el número*](../../clases/10/teoria/codigo/adivina_numero/) (sección 7.5). Cada nivel va en su **propia carpeta**:

```
laboratorio4/
├── nivel1/
│   ├── cai.py
│   ├── test_cai.py
│   └── main.py
├── nivel2/
│   ├── cai.py
│   ├── test_cai.py
│   └── main.py
...
└── nivel5/
```

| Archivo | Contenido | Se ejecuta con |
|---|---|---|
| `cai.py` | `import random` y **todas** las funciones del programa, cada una con su especificación. No tiene pruebas ni programa principal | *(no se ejecuta: se importa)* |
| `test_cai.py` | `import cai`, las pruebas con `assert` y, al final, `print("Pruebas de cai: todas pasaron")` | `python test_cai.py` |
| `main.py` | `import cai`, las constantes, el programa principal dentro de `def main():` y la guarda `if __name__ == "__main__":` | `python main.py` |

**Para comenzar un nivel nuevo**, copie la carpeta completa del nivel anterior, cámbiele el nombre (por ejemplo, `nivel1/` → `nivel2/`) y modifique **solo** lo que el nivel pide. La carpeta [`plantilla_nivel1/`](plantilla_nivel1/) tiene los tres archivos del nivel 1 con el encabezado y comentarios `# PISTA`. Su `main.py` ya trae escritos `def main():` y la guarda, que se mantienen igual en todos los niveles.

> [!IMPORTANT]
> * Las funciones que **imprimen** (como `mostrar_pregunta`) también van en `cai.py`, pero **no** se prueban con `assert`.
> * Desde `main.py` y `test_cai.py`, cada función se llama con el prefijo del módulo: `cai.generar_operando()`.
> * `test_cai.py` no lleva guarda: nadie lo importa, solo se ejecuta directamente.
> * Ningún archivo puede llamarse como un módulo de Python (`random.py`, `math.py`).

### Errores frecuentes al trabajar con varios archivos

| Síntoma | Causa | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'cai'` | `main.py` o `test_cai.py` no están en la misma carpeta que `cai.py` | Mantener los tres archivos de un nivel en la misma carpeta |
| `ModuleNotFoundError: No module named 'cai.py'; 'cai' is not a package` | Se escribió `import cai.py` | Importar sin la extensión: `import cai` |
| `NameError: name 'es_correcta' is not defined` | Se llamó a la función sin el prefijo del módulo | Escribir `cai.es_correcta(...)` |
| `AttributeError: module 'random' has no attribute 'randint'` | Un archivo propio se llama `random.py` | Renombrarlo y borrar la carpeta `__pycache__/` |
| El nivel 3 se comporta como el nivel 2 | Se editó el archivo de la carpeta equivocada al copiar el nivel | Revisar en el editor la ruta del archivo abierto |

> [!NOTE]
> Al importar `cai` aparece una carpeta `__pycache__/` junto a los archivos. Python la crea automáticamente; puede ignorarse y **no se entrega**.

## Metodología de trabajo

Para cada nivel se siguen cuatro pasos. Son los mismos del ejemplo de temperaturas de la clase 10 y del ejercicio guiado *Adivina el número*.

### 1. Entender y diseñar (a mano)

* Identificar las **entradas**, el **proceso** y las **salidas** del nivel.
* Actualizar el **diagrama top-down**: ¿qué subproblemas nuevos aparecen? ¿Cuáles se convierten en funciones?
* Actualizar la **tabla de variables** del programa principal, indicando su rol (contador, acumulador, variable de control, etc.) cuando aplique.

### 2. Especificar

* Escribir el **docstring** de cada función nueva **antes** de su código, con el formato visto en clase:

```python
def nombre_funcion(parametro):
    """
    Descripcion breve de lo que hace la funcion.

    Supone:
        Condiciones que deben cumplir los parametros.
    Garantiza:
        Lo que la funcion retorna (o lo que muestra en pantalla)
        si se cumplen las suposiciones.
    """
```

Las funciones que **imprimen** también se especifican: su *Garantiza* dice qué muestran en pantalla y que no retornan ningún valor, como `mostrar_menu` en `temperaturas_v3.py` de la clase 10:

```python
    Garantiza:
        Imprime las tres opciones del menú. No retorna ningún valor.
```

### 3. Implementar con stubs y probar

* Escribir en `cai.py` las funciones nuevas como **stubs** (versiones provisionales que retornan un valor fijo), y en `main.py` el **programa principal** que las usa.
* Escribir en `test_cai.py` las **pruebas con `assert`** de las funciones que calculan. Al ejecutar `python test_cai.py`, las pruebas deben fallar mientras las funciones sean stubs.
* Implementar **una función a la vez** en `cai.py`, ejecutando `python test_cai.py` después de cada una, hasta que todas las pruebas pasen. Luego ejecutar `python main.py`.

> [!IMPORTANT]
> En este curso, solo se prueban con `assert` las funciones que **retornan un valor y no leen ni imprimen nada**. Las funciones que usan `random` se prueban con `random.seed()` (ver el ejercicio guiado *Adivina el número*, sección 5). Como `test_cai.py` y `main.py` son archivos distintos, fijar la semilla en las pruebas **no** afecta al programa principal.

### 4. Verificar

* Ejecutar `python test_cai.py`: todas las pruebas deben pasar. Las pruebas con `assert` **automatizan** la verificación de las funciones de `cai.py`: cada vez que se ejecutan, comparan el resultado de cada función con el esperado.
* Ejecutar `python main.py` y comparar su comportamiento con los ejemplos de ejecución del enunciado. El programa principal **no tiene pruebas con `assert`**: para razonar sobre su flujo (ciclos, contadores, condiciones de salida) sigue siendo útil la prueba de escritorio. Por eso en el nivel 3, donde esa lógica se vuelve delicada, se pide una (ver los [Entregables](#entregables)).

## Trabajo en parejas

Este laboratorio se realiza **en parejas**. La organización en archivos permite que dos personas trabajen al mismo tiempo en el mismo programa, como se vio en la clase 9 (*trabajo simultáneo*), siempre que se pongan de acuerdo en la **especificación** de cada función. En la clase 10 la especificación se presentó como un **contrato**: quien usa la función se compromete a cumplir el *Supone*, y quien la escribe, a cumplir el *Garantiza*. En este laboratorio cada integrante ocupa uno de esos dos lados.

**Autor del módulo**

* Escribe en `cai.py` las funciones del nivel, con su especificación.
* Escribe en `test_cai.py` las pruebas de esas funciones.
* Garantiza que cada función cumple su especificación: `python test_cai.py` debe pasar.

**Usuario del módulo**

* Escribe `main.py` usando **solo** la especificación de las funciones, sin mirar cómo están implementadas.
* Diseña el programa principal: ciclos, contadores, lectura de datos y mensajes.
* Revisa que la especificación diga todo lo que necesita saber para usar cada función. Si no lo dice, la pareja la corrige.

**Antes de escribir código**, la pareja acuerda en papel el diagrama top-down y la especificación de cada función nueva: ese es el contrato. Al terminar, integran los tres archivos y ejecutan `python main.py`.

**Los roles se alternan en cada nivel**: quien fue autor del módulo en el nivel 1 es usuario en el nivel 2, y así sucesivamente. De esta manera cada integrante escribe funciones y programa principal varias veces.

> [!IMPORTANT]
> La **sustentación es individual**. Cada integrante debe poder explicar cualquier archivo de cualquier nivel, no solo los que escribió.

## Fechas importantes

* **Asignación:** *por definir*.
* **Entrega y sustentación:** *por definir*.

## Entregables

* **En papel (a mano, uno por pareja):**
  * El **diagrama top-down** del nivel 5 (el programa completo). Puede hacerse a mano o, si se prefiere, en draw.io e imprimirse.
  * La **especificación** (*Supone / Garantiza*) de cada función.
  * La **tabla de variables** del programa principal del nivel 5.
  * Una **prueba de escritorio** de las primeras respuestas del nivel 3 (ver la [Pregunta para pensar](#nivel-3--seguimiento-del-desempeño) de ese nivel).
* **En Python:** una carpeta por nivel (`nivel1/`, `nivel2/`, …, `nivel5/`), cada una con sus tres archivos `cai.py`, `test_cai.py` y `main.py` (ver [Organización en archivos](#organización-en-archivos)), **sin** la carpeta `__pycache__/`. Cada archivo debe tener su encabezado (título, resumen, autores, fecha y versión), y en cada nivel `python test_cai.py` debe pasar todas las pruebas.

---

# Problemas

## Nivel 1 — Preguntas de multiplicación

> [!TIP]
> Comience copiando la carpeta [`plantilla_nivel1/`](plantilla_nivel1/) y renómbrela `nivel1/`. Sus comentarios `# PISTA` indican qué va en cada archivo.

Escriba un programa que ayude a un estudiante de primaria a aprender a multiplicar. El programa debe generar **dos enteros positivos de un dígito** (del 1 al 9) al azar y mostrar una pregunta como:

```
¿Cuánto es 6 por 7?
```

El estudiante ingresa su respuesta y el programa la verifica:

* Si es **correcta**, muestra `¡Muy bien!` y genera una **nueva** pregunta.
* Si es **incorrecta**, muestra `No. Intente de nuevo.` y repite **la misma** pregunta hasta que el estudiante acierte.

Para terminar el programa, el estudiante ingresa `0` como respuesta.

**Funciones requeridas:**

| Función | Descripción | Tipo |
|---|---|---|
| `generar_operando()` | Retorna un entero al azar entre 1 y 9 | Retorna un valor (usa `random`) |
| `mostrar_pregunta(a, b)` | Imprime `¿Cuánto es a por b?` | No retorna valor (imprime) |
| `es_correcta(resultado, respuesta)` | Retorna `True` si la respuesta coincide con el resultado correcto, y `False` en caso contrario | Retorna un valor |

**Casos de prueba de `es_correcta`:**

| `resultado` | `respuesta` | Resultado esperado |
|---|---|---|
| 42 | 42 | `True` |
| 42 | 41 | `False` |
| 9 | 9 | `True` |

**Ejemplo de ejecución** (ilustrativo: los números cambian en cada ejecución):

```
¿Cuánto es 6 por 7?
Respuesta: 48
No. Intente de nuevo.
¿Cuánto es 6 por 7?
Respuesta: 42
¡Muy bien!
¿Cuánto es 3 por 9?
Respuesta: 0
Fin de la práctica.
```

<details>
<summary>Pista adicional</summary>

El programa necesita dos ciclos: uno **externo** que genera preguntas nuevas, y uno **interno** que repite la misma pregunta mientras la respuesta sea incorrecta. Piense en qué condición debe terminar cada uno, y en dónde debe revisarse si el estudiante ingresó `0`.

Para probar `generar_operando`, escriba en `test_cai.py` un ciclo que genere 1000 valores y verifique con `assert` que todos estén entre 1 y 9. Use `random.seed()` con un número fijo para que la prueba sea repetible.

</details>

> **Pregunta para pensar:** el enunciado original de Deitel pide que una función aparte genere cada pregunta. ¿Por qué se separó aquí en `generar_operando` (que retorna un número) y `mostrar_pregunta` (que imprime)? ¿Cuál de las dos se puede probar con `assert`, y por qué?

---

## Nivel 2 — Mensajes variados

Un problema de los programas de práctica es que el estudiante se aburre con mensajes repetitivos. Modifique el programa del nivel 1 para que muestre **mensajes variados**, elegidos al azar:

| Número | Mensaje de acierto | Mensaje de error |
|---|---|---|
| 1 | `¡Muy bien!` | `No. Intente de nuevo.` |
| 2 | `¡Excelente!` | `Incorrecto. Intente una vez más.` |
| 3 | `¡Buen trabajo!` | `¡No se rinda!` |
| 4 | `¡Siga así!` | `No. Siga intentando.` |

Use `random.randint(1, 4)` en el programa principal para elegir el número del mensaje.

**Funciones nuevas:**

| Función | Descripción | Tipo |
|---|---|---|
| `mensaje_acierto(numero)` | Retorna el mensaje de acierto correspondiente a `numero` (de 1 a 4) | Retorna un valor |
| `mensaje_error(numero)` | Retorna el mensaje de error correspondiente a `numero` (de 1 a 4) | Retorna un valor |

**Casos de prueba:**

| Llamada | Resultado esperado |
|---|---|
| `mensaje_acierto(1)` | `"¡Muy bien!"` |
| `mensaje_acierto(4)` | `"¡Siga así!"` |
| `mensaje_error(2)` | `"Incorrecto. Intente una vez más."` |
| `mensaje_error(3)` | `"¡No se rinda!"` |

<details>
<summary>Pista adicional</summary>

Use una **alternativa múltiple** (`if` / `elif` / `else`). Observe que las funciones **reciben** el número como parámetro en lugar de generarlo internamente con `random`: así su resultado no depende del azar y pueden probarse con `assert`.

</details>

> **Pregunta para pensar:** ¿qué ventaja tiene que `random.randint(1, 4)` se llame en el programa principal y no dentro de `mensaje_acierto`? Piense en cómo escribiría las pruebas en cada caso.

---

## Nivel 3 — Seguimiento del desempeño

Modifique el programa del nivel 2 para que cuente las respuestas **correctas** e **incorrectas** del estudiante. Después de **10 respuestas** (contando también los reintentos), el programa calcula el **porcentaje de respuestas correctas** y muestra:

* Si el porcentaje es **menor que 75 %**: `Por favor, pida ayuda adicional a su profesor.`
* Si el porcentaje es **75 % o más**: `¡Felicitaciones, está listo para pasar al siguiente nivel!`

En este nivel ya no se usa `0` para terminar: el programa termina después de las 10 respuestas, **aunque la pregunta en curso no se haya acertado**. Si el estudiante ingresa `0`, se cuenta como una respuesta incorrecta más.

**Funciones nuevas:**

| Función | Descripción | Tipo |
|---|---|---|
| `calcular_porcentaje(aciertos, total)` | Retorna el porcentaje de aciertos sobre el total. Si `total` es 0, retorna 0.0 | Retorna un valor |
| `mensaje_desempeno(porcentaje)` | Retorna el mensaje de felicitación o de ayuda según el porcentaje | Retorna un valor |

**Casos de prueba:**

| Llamada | Resultado esperado | Tipo |
|---|---|---|
| `calcular_porcentaje(8, 10)` | `80.0` | Típico |
| `calcular_porcentaje(7, 10)` | `70.0` | Típico |
| `calcular_porcentaje(0, 0)` | `0.0` | Especial (sin respuestas) |
| `mensaje_desempeno(75.0)` | `"¡Felicitaciones, está listo para pasar al siguiente nivel!"` | Límite |
| `mensaje_desempeno(74.9)` | `"Por favor, pida ayuda adicional a su profesor."` | Límite |

**Ejemplo de ejecución** (abreviado):

```
¿Cuánto es 4 por 8?
Respuesta: 32
¡Excelente!
...
(10 respuestas en total)
...
Respuestas correctas: 8 de 10 (80.0 %)
¡Felicitaciones, está listo para pasar al siguiente nivel!
```

<details>
<summary>Pista adicional</summary>

Use dos **contadores** (`aciertos` y `errores`) y un ciclo que termine cuando la suma de ambos llegue a 10. Note que el ciclo interno del nivel 1 (repetir hasta acertar) ahora también debe detenerse si se completan las 10 respuestas.

</details>

> **Pregunta para pensar:** si el estudiante responde mal 10 veces seguidas la primera pregunta, ¿cuántas preguntas distintas vio? ¿Cuál es su porcentaje? Realice la **prueba de escritorio** de las primeras 5 respuestas de una ronda en la que el estudiante acierta las preguntas 1 y 2, falla una vez la pregunta 3 antes de acertarla, y acierta la pregunta 4. Registre en cada fila los valores de `aciertos`, `errores` y el total de respuestas (incluya esta prueba en los entregables).

> **Pregunta para pensar:** con exactamente 10 respuestas, ¿qué porcentajes son posibles? ¿Cuántas respuestas correctas se necesitan, como mínimo, para recibir el mensaje de felicitación? Si `74.9` nunca aparece en una ronda de 10 respuestas, ¿por qué tiene sentido probar `mensaje_desempeno(74.9)`?

---

## Nivel 4 — Niveles de dificultad

Modifique el programa del nivel 3 para que, al iniciar, el usuario elija un **nivel de dificultad**:

* **Nivel 1:** operandos de un dígito (del 1 al 9).
* **Nivel 2:** operandos de hasta dos dígitos (del 1 al 99).
* **Nivel 3:** operandos de hasta tres dígitos (del 1 al 999), y así sucesivamente.

**Funciones nuevas o modificadas:**

| Función | Descripción | Tipo |
|---|---|---|
| `maximo_operando(nivel)` | Retorna el mayor operando posible para el nivel dado | Retorna un valor |
| `generar_operando(nivel=1)` | **Modificada:** retorna un entero al azar entre 1 y `maximo_operando(nivel)`. Si no se indica el nivel, usa el nivel 1 | Retorna un valor (usa `random`) |

**Casos de prueba de `maximo_operando`:**

| Llamada | Resultado esperado |
|---|---|
| `maximo_operando(1)` | `9` |
| `maximo_operando(2)` | `99` |
| `maximo_operando(3)` | `999` |

<details>
<summary>Pista adicional</summary>

Observe el patrón: 9 = 10¹ − 1, 99 = 10² − 1, 999 = 10³ − 1. En Python, la potencia se escribe con `**`.

Con el valor por defecto `nivel=1`, la llamada `generar_operando()` del nivel 1 sigue funcionando sin cambios. Esto permite modificar una función **sin romper** el código que ya la usaba.

Al escribir la especificación, piense: ¿qué debe **suponer** `maximo_operando` sobre `nivel`? ¿Qué retornaría con `nivel = 0`?

</details>

> **Pregunta para pensar:** `generar_operando` ahora **llama** a `maximo_operando`, y las dos están en `cai.py`. ¿Necesita `main.py` saber que existe `maximo_operando`? ¿Qué archivos de la carpeta `nivel4/` tuvo que modificar respecto a `nivel3/`, y cuáles quedaron iguales?

---

## Nivel 5 — Tipos de operación

Modifique el programa del nivel 4 para que, además del nivel de dificultad, el usuario elija el **tipo de operación** que desea practicar:

| Opción | Tipo |
|---|---|
| 1 | Solo sumas |
| 2 | Solo restas |
| 3 | Solo multiplicaciones |
| 4 | Mezcla aleatoria de las tres |

La pregunta debe adaptarse a la operación: `¿Cuánto es 6 más 7?`, `¿Cuánto es 9 menos 4?`, `¿Cuánto es 6 por 7?`.

Como el programa está dirigido a estudiantes de primaria, **las restas no deben tener resultado negativo**: el primer operando debe ser siempre el mayor. Ordenar los operandos es responsabilidad del **programa principal** (`main.py`), antes de mostrar la pregunta; por eso `calcular_resultado` puede **suponer** que, en una resta, `a >= b`.

**Funciones nuevas o modificadas:**

| Función | Descripción | Tipo |
|---|---|---|
| `calcular_resultado(a, b, operacion)` | Retorna el resultado de aplicar la operación (1: suma, 2: resta, 3: multiplicación) a `a` y `b`. Supone que `a >= b` cuando la operación es una resta | Retorna un valor |
| `nombre_operacion(operacion)` | Retorna `"más"`, `"menos"` o `"por"` según la operación | Retorna un valor |
| `elegir_operacion(tipo)` | Si `tipo` es 1, 2 o 3, lo retorna; si es 4, retorna una operación al azar entre 1 y 3. Se llama una vez por cada **pregunta nueva**, no en cada intento: mientras el estudiante reintenta, la operación no cambia | Retorna un valor (usa `random` en la opción 4) |
| `mostrar_pregunta(a, b, operacion)` | **Modificada:** imprime la pregunta con el nombre de la operación | No retorna valor (imprime) |

**Casos de prueba:**

| Llamada | Resultado esperado |
|---|---|
| `calcular_resultado(3, 5, 1)` | `8` |
| `calcular_resultado(9, 4, 2)` | `5` |
| `calcular_resultado(6, 7, 3)` | `42` |
| `nombre_operacion(3)` | `"por"` |
| `elegir_operacion(2)` | `2` |
| `elegir_operacion(4)` | Un valor entre 1 y 3 (pruébelo con `random.seed()` y un ciclo) |

<details>
<summary>Pista adicional</summary>

Para que la resta nunca sea negativa, use en `main.py` las funciones integradas `max()` y `min()` (clase 10): el primer operando es el mayor de los dos números generados y el segundo, el menor.

`calcular_resultado` debe usarse tanto para calcular la respuesta correcta como para verificarla con `es_correcta`, sin importar el tipo de operación. Así, `es_correcta` no necesita cambiar.

</details>

> **Pregunta para pensar:** compare el programa del nivel 5 con el del nivel 1. ¿Qué funciones no cambiaron nunca? ¿Cuáles se modificaron, y cuántas de esas modificaciones obligaron a cambiar `main.py`? ¿En qué niveles el usuario del módulo tuvo que esperar a que el autor terminara, y en cuáles le bastó con la especificación? ¿Qué le dice esto sobre la ventaja de dividir un programa en funciones y en archivos?

---

## Retos opcionales

1. **Varios estudiantes:** al terminar las 10 respuestas del nivel 3 (o posteriores), pregunte `¿Otro estudiante? (s/n)` y reinicie los contadores si la respuesta es `s`.
2. **División:** agregue la división como opción 5. Para que el resultado sea siempre entero, genere primero el divisor y el cociente, y calcule el dividendo como su producto.

## Reflexión final

> ¿En qué nivel le resultó más útil tener las pruebas con `assert` ya escritas? ¿Hubo algún cambio en una función que una prueba detectó antes de que usted lo notara al ejecutar el programa?

> ¿Qué función le costó más especificar (escribir su *Supone / Garantiza*) antes de implementarla? ¿Cambió su especificación después de implementarla?

**Idea central del laboratorio:** un programa dividido en funciones bien especificadas y probadas puede **crecer** nivel a nivel sin volver a escribirse desde cero. Cada nivel agrega o modifica unas pocas funciones, y las pruebas confirman que lo que ya funcionaba sigue funcionando.

## Recursos

* [Documentación oficial del módulo `random` (en español)](https://docs.python.org/es/3/library/random.html)
* [Ejercicio guiado *Adivina el número*](../../clases/10/teoria/codigo/adivina_numero/), sección 7: el modelo de organización en archivos de este laboratorio.
* Deitel, P. y Deitel, H. *C How to Program*, 9.ª edición global, Pearson, 2023, ejercicios 5.49-5.53 (págs. 293-294).

> [!important]
> ### Nota de transparencia sobre uso de IA
> Se usó IA generativa para la redacción y organización del contenido de este laboratorio (enunciados, pistas y casos de prueba), adaptando problemas de distintas fuentes (algunas en inglés) al contexto del curso, y tomando como referencia el formato del laboratorio anterior. El docente revisó y validó el material final antes de su publicación; aun así, es posible que se haya pasado por alto algún error. Si encuentra alguna inconsistencia, se agradece informarla al docente para corregirla.