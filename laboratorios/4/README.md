# Laboratorio 4 — Funciones: instrucción asistida por computador

## Antes de empezar

Antes de la sesión de laboratorio, repase el siguiente material:

* **Clase 9** — definición e invocación de funciones, tipos de funciones según sus entradas y salidas, y pruebas con `assert`.
* **Clase 10** — especificación de una función (*Supone / Garantiza*), ámbito de las variables, parámetros con valor por defecto, diseño **top-down** con *stubs*, y uso de librerías (`math`, `random`).
* **Ejercicio guiado [Adivina el número](../../clases/10/teoria/codigo/adivina_numero/)** — muestra, paso a paso, el mismo procedimiento que se exige en este laboratorio: diseño top-down, especificación, implementación con stubs y pruebas con `random.seed()`.

> [!NOTE]
> Los problemas de este laboratorio están **adaptados** de los ejercicios 5.49 a 5.53 (*Computer-Assisted Instruction*) del libro de P. Deitel y H. Deitel, *C How to Program*, 9.ª edición global, Pearson, 2023, págs. 293-294, disponible en [`material/libros/`](../../material/libros/). El original está planteado en C; aquí se resuelve en Python con las estructuras vistas en el curso.

## Objetivos

Al finalizar este laboratorio, el estudiante estará en capacidad de:

* Descomponer un problema en **funciones** mediante diseño **top-down**, y decidir qué subproblemas merecen una función propia.
* Escribir la **especificación** de cada función (*Supone / Garantiza*) antes de implementarla.
* Separar las funciones que **calculan** (reciben datos y retornan un valor, sin leer ni imprimir) de las que **interactúan** con el usuario, de modo que las primeras puedan probarse con `assert`.
* Utilizar el módulo **`random`** para generar datos al azar, y `random.seed()` para obtener resultados repetibles al probar.
* Utilizar **parámetros con valor por defecto** y **funciones que llaman a otras funciones**.
* Construir un programa de forma **incremental**: cada nivel parte del programa del nivel anterior y le agrega una funcionalidad.

## Herramientas necesarias

* **Anaconda**: distribución de Python que incluye el intérprete y Spyder.
* **Visual Studio Code** (opcional): editor de código con la extensión de Python.
* **draw.io**: para el diagrama top-down.
* **Python Tutor** ([pythontutor.com](https://pythontutor.com/)): para visualizar la pila de llamadas entre funciones.

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
        Lo que la funcion retorna si se cumplen las suposiciones.
    """
```

### 3. Implementar con stubs y probar

* Escribir primero el **programa principal** y las funciones como **stubs** (versiones provisionales que retornan un valor fijo).
* Escribir las **pruebas con `assert`** de las funciones que calculan. Las pruebas deben fallar mientras las funciones sean stubs.
* Implementar **una función a la vez**, ejecutando el programa después de cada una, hasta que todas las pruebas pasen.

> [!IMPORTANT]
> Solo se prueban con `assert` las funciones que **retornan un valor y no leen ni imprimen nada**. Las funciones que usan `random` se prueban con `random.seed()` (ver el ejercicio guiado *Adivina el número*, sección 5).

### 4. Verificar

* Ejecutar el programa completo y comparar su comportamiento con los ejemplos de ejecución del enunciado.
* Realizar una **prueba de escritorio** de al menos una ronda de preguntas.

## Trabajo individual

Este laboratorio se realiza de manera **individual**. Cada estudiante es responsable de aplicar la metodología en cada nivel y de estar en capacidad de sustentar cualquier parte de su solución.

## Fechas importantes

* **Asignación:** *por definir*.
* **Entrega y sustentación:** *por definir*.

## Entregables

* **En papel (a mano):**
  * El **diagrama top-down** del nivel 5 (el programa completo).
  * La **especificación** (*Supone / Garantiza*) de cada función.
  * La **tabla de variables** del programa principal del nivel 5.
  * Una **prueba de escritorio** de las primeras respuestas del nivel 3 (ver la [Pregunta para pensar](#nivel-3--seguimiento-del-desempeño) de ese nivel).
* **En Python:** un script por nivel (`nivel1.py`, `nivel2.py`, …, `nivel5.py`). Cada script debe incluir, en este orden: encabezado (título, resumen, autor, fecha y versión), funciones con su especificación, sección de **pruebas con `assert`** y programa principal.

---

# Problemas

## Nivel 1 — Preguntas de multiplicación

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

Para probar `generar_operando`, use `random.seed()` y verifique que los valores generados estén siempre entre 1 y 9 (por ejemplo, generando 1000 valores en un ciclo).

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

En este nivel ya no se usa `0` para terminar: el programa termina después de las 10 respuestas.

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

</details>

> **Pregunta para pensar:** `generar_operando` ahora **llama** a `maximo_operando`. Ejecute su programa en **Python Tutor** y observe la pila de llamadas en el momento en que `maximo_operando` retorna. ¿Cuántos marcos (*frames*) hay abiertos? ¿Qué variables tiene cada uno?

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

Como el programa está dirigido a estudiantes de primaria, **las restas no deben tener resultado negativo**: el primer operando debe ser siempre el mayor.

**Funciones nuevas o modificadas:**

| Función | Descripción | Tipo |
|---|---|---|
| `calcular_resultado(a, b, operacion)` | Retorna el resultado de aplicar la operación (1: suma, 2: resta, 3: multiplicación) a `a` y `b` | Retorna un valor |
| `nombre_operacion(operacion)` | Retorna `"más"`, `"menos"` o `"por"` según la operación | Retorna un valor |
| `elegir_operacion(tipo)` | Si `tipo` es 1, 2 o 3, lo retorna; si es 4, retorna una operación al azar entre 1 y 3 | Retorna un valor (usa `random` en la opción 4) |
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

Para que la resta nunca sea negativa, use las funciones integradas `max()` y `min()` (clase 10): el primer operando es el mayor de los dos números generados y el segundo, el menor.

`calcular_resultado` debe usarse tanto para calcular la respuesta correcta como para verificarla con `es_correcta`, sin importar el tipo de operación. Así, `es_correcta` no necesita cambiar.

</details>

> **Pregunta para pensar:** compare el programa del nivel 5 con el del nivel 1. ¿Qué funciones no cambiaron nunca? ¿Cuáles se modificaron, y cuántas de esas modificaciones obligaron a cambiar el programa principal? ¿Qué le dice esto sobre la ventaja de dividir un programa en funciones?

---

## Retos opcionales

1. **Varios estudiantes:** al terminar las 10 respuestas del nivel 3 (o posteriores), pregunte `¿Otro estudiante? (s/n)` y reinicie los contadores si la respuesta es `s`.
2. **División:** agregue la división como opción 5. Para que el resultado sea siempre entero, genere primero el divisor y el cociente, y calcule el dividendo como su producto.
3. **Separación en archivos:** mueva las funciones a un archivo `funciones_cai.py` e impórtelas desde `nivel5.py` (se verá en el siguiente tema de la clase 10).

## Reflexión final

> ¿En qué nivel le resultó más útil tener las pruebas con `assert` ya escritas? ¿Hubo algún cambio en una función que una prueba detectó antes de que usted lo notara al ejecutar el programa?

> ¿Qué función le costó más especificar (escribir su *Supone / Garantiza*) antes de implementarla? ¿Cambió su especificación después de implementarla?

**Idea central del laboratorio:** un programa dividido en funciones bien especificadas y probadas puede **crecer** nivel a nivel sin volver a escribirse desde cero. Cada nivel agrega o modifica unas pocas funciones, y las pruebas confirman que lo que ya funcionaba sigue funcionando.

## Recursos

* [Documentación oficial del módulo `random` (en español)](https://docs.python.org/es/3/library/random.html)
* [Python Tutor](https://pythontutor.com/): visualización de la pila de llamadas entre funciones.
* Deitel, P. y Deitel, H. *C How to Program*, 9.ª edición global, Pearson, 2023, ejercicios 5.49-5.53 (págs. 293-294).

> [!important]
> ### Nota de transparencia sobre uso de IA
> Se usó IA generativa para la redacción y organización del contenido de este laboratorio (enunciados, pistas y casos de prueba), adaptando problemas de distintas fuentes (algunas en inglés) al contexto del curso, y tomando como referencia el formato del laboratorio anterior. El docente revisó y validó el material final antes de su publicación; aun así, es posible que se haya pasado por alto algún error. Si encuentra alguna inconsistencia, se agradece informarla al docente para corregirla.