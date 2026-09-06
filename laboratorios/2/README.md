# Laboratorio 2 — Estructuras condicionales

## Antes de empezar

Antes de la sesión de laboratorio, vea estos dos videos cortos de Code.org (están en inglés; active los subtítulos en español si los necesita):

* [Conditionals: If and If/Else Statements](https://www.youtube.com/watch?v=sO4UYCbTxxo): una introducción breve a qué significa que un programa tome una decisión.
* [Conditionals: 3 Types](https://www.youtube.com/watch?v=ZgB0Wp-fShk): presenta las tres variantes que vamos a practicar en este laboratorio — condicional simple, doble y de varias alternativas — como un adelanto de la estructura completa que sigue este documento.

## Objetivos

Al finalizar este laboratorio, el estudiante estará en capacidad de:

* Reconocer, dentro de un problema, en qué punto el algoritmo debe **tomar una decisión** (bifurcar su flujo) en lugar de ejecutar pasos en secuencia.
* Diseñar algoritmos que utilicen estructuras condicionales **simples** (`if`), **dobles** (`if`-`else`), de **selección múltiple** (`elif`) y **anidadas**, usando diagramas de flujo o pseudocódigo.
* Traducir enunciados en lenguaje natural a **expresiones lógicas correctas**, combinando operadores relacionales (`>`, `>=`, `<`, `<=`, `==`, `!=`) y lógicos (`and`, `or`, `not`) cuando el problema lo requiera.
* Reconocer cuándo varias condiciones son **mutuamente excluyentes** (se resuelven con `elif`) y cuándo son **independientes entre sí** (se resuelven con varios `if` separados, porque más de una puede cumplirse a la vez).
* Verificar manualmente un algoritmo mediante **pruebas de escritorio que cubran tanto el camino verdadero como el falso** de cada condición, no solo un caso feliz.
* Implementar en Python estructuras condicionales simples, dobles, de selección múltiple y anidadas.
* Ejecutar y depurar programas con decisiones, identificando errores comunes como condiciones invertidas, límites mal definidos (`>` en vez de `>=`), vacíos entre rangos, o ramas que nunca se alcanzan.

## Herramientas necesarias

Para el desarrollo de esta práctica necesita, como mínimo, lo siguiente:

* **Anaconda**: distribución de Python que incluye el intérprete, el gestor de paquetes y Jupyter Notebook.
* **Visual Studio Code**: editor de código ligero, con la extensión de Python instalada, para escribir y ejecutar sus programas.
* **draw.io**: herramienta para diseñar diagramas de flujo (opcional para bocetar antes de pasarlos a papel; la versión final de cada diagrama debe entregarse a mano, según se indica en la metodología).
* **PyCharm** (opcional): alternativa de IDE más completa a Visual Studio Code.

Si no desea instalar nada, también puede trabajar con las siguientes plataformas en línea, sin necesidad de instalación:

* **Python Tutor** (pythontutor.com): visualización paso a paso de la ejecución de un programa, útil para observar el momento exacto en que una condición se evalúa como verdadera o falsa. La usaremos también al final del laboratorio, en la sección [Visualización de la ejecución](#visualización-de-la-ejecución).
* **CodeSkulptor** (py3.codeskulptor.org): entorno de Python en el navegador, orientado a principiantes.

Adicionalmente, cada pareja debe traer hojas, lápiz/lapicero y, si lo desea, la plantilla de solución de problemas impresa (ver [Recursos](#recursos)) para desarrollar el método de Polya a mano.

## Metodología de trabajo

Seguimos utilizando la versión simplificada del método de **George Pólya** presentada en el laboratorio anterior, aplicada **a mano** antes de escribir cualquier línea de código. Para cada problema, siga los siguientes pasos:

### 1. Entender el problema

Identifique:

* ¿Qué información recibe el problema? (datos de entrada)
* ¿Qué resultado debe producir? (datos de salida)
* **¿En qué punto del algoritmo se debe tomar una decisión?** Formule explícitamente la condición (o condiciones) que se deben evaluar, y qué debe ocurrir en cada caso.
* ¿La decisión tiene dos caminos posibles (`if`-`else`), varias alternativas sobre una misma variable (`elif`), o solo importa un caso y el resto del algoritmo sigue igual (`if` simple)?
* ¿Hay casos límite en los que no es evidente qué camino debe tomar la condición? (por ejemplo, ¿un valor igual al límite cuenta como "mayor" o no? ¿quedan valores sin cubrir entre dos rangos consecutivos?)

### 2. Diseñar un plan

Diseñe una solución mediante un **diagrama de flujo o pseudocódigo**. En esta etapa **todavía no escriba código Python**. Escriba explícitamente cada condición como una expresión lógica (por ejemplo `edad >= 62`, no solo "si es mayor").

### 3. Revisar el plan (prueba de escritorio + predicción)

Realice una **prueba de escritorio** usando los casos de prueba proporcionados en cada problema. A diferencia del laboratorio anterior, aquí es indispensable probar **más de un camino**: para cada condición del algoritmo, su prueba de escritorio debe incluir al menos un caso donde la condición sea verdadera y otro donde sea falsa. Antes de implementar cualquier programa, debe poder responder:

> **¿Qué resultado espero obtener en cada caso de prueba, y por qué esa condición tomó ese camino?**

### 4. Implementar el plan

Solo después de completar los pasos anteriores, codifique el algoritmo en Python y ejecútelo con los mismos casos de prueba, comparando la salida real contra su predicción (ver la sección [Verificación](#verificación)).

La idea central del laboratorio sigue siendo:

> **Entender → Diseñar → Predecir → Implementar → Verificar**

Se proporciona una plantilla de solución de problemas (ver [Recursos](#recursos)) como guía opcional para organizar estos pasos. Su uso no es obligatorio: cada pareja es libre de aplicar el método de Polya en el formato que prefiera (a mano en hojas propias, en la plantilla, etc.), siempre que el análisis, el diagrama de flujo o pseudocódigo y la prueba de escritorio de cada problema queden documentados en papel. **Estos documentos deben traerse a la sesión de laboratorio**, ya que son la base para la codificación y para la sustentación del ejercicio ante el docente.

## Trabajo en parejas

El laboratorio se realiza mediante la misma dinámica inspirada en *pair programming* (ver [Recursos](#recursos)) del laboratorio anterior. Cada pareja trabaja con dos roles:

**Analista / Navegante**

* Lidera el análisis inicial del problema (pasos 1 a 3 del método de Polya), incluyendo la identificación explícita de cada condición.
* Revisa permanentemente la solución mientras su compañero programa.
* Identifica posibles errores y casos límite (por ejemplo, condiciones con `>` que debieron ser `>=`).
* Piensa en el siguiente paso mientras se implementa la solución.

**Conductor / Programador**

* Implementa el algoritmo en Python (paso 4).
* Explica en voz alta lo que está escribiendo.
* Contrasta el código con el algoritmo diseñado por su compañero.
* Ejecuta y verifica los casos de prueba, incluyendo los que evalúan cada condición como verdadera y como falsa.

> **Importante:** ambos integrantes son responsables de comprender tanto el algoritmo como el código, y deben poder sustentar cualquier parte del trabajo ante el docente. Los roles deben **alternarse entre los problemas**, de manera que ambos tengan la oportunidad de ejercer los dos roles durante la sesión.

## Fechas importantes

* **Asignación:** 5 de septiembre de 2026.
* **Sesiones de laboratorio disponibles para trabajar en él:** 5, 12 y 19 de septiembre de 2026.
* **Entrega y sustentación:** 19 de septiembre de 2026, durante la sesión de laboratorio. Traiga completos los documentos en papel (ver [Entregables](#entregables)) y esté en capacidad de sustentar cualquiera de los 14 problemas ante el docente.

## Entregables

Al finalizar el laboratorio, cada pareja debe entregar:

* **En papel:** el planteamiento del algoritmo (diagrama de flujo o pseudocódigo) de cada uno de los problemas, junto con la prueba de escritorio de **solo 2** de los casos de prueba de cada problema — no es necesario hacer a mano la prueba de escritorio de la tabla completa. Elija los 2 casos de forma que cubran caminos distintos del algoritmo (por ejemplo, uno donde una condición clave sea verdadera y otro donde sea falsa), no dos casos que tomen el mismo camino.
* **En Python:** un script `.py` por cada problema, que implemente el algoritmo diseñado y permita verificar todos los casos de la tabla de pruebas correspondiente (estos sí se ejecutan todos, aunque en papel solo se documenten 2).

---

# Problemas

Los problemas están organizados de menor a mayor complejidad en el tipo de estructura condicional requerida: primero `if` simple, luego `if`-`else`, y finalmente varias alternativas (selección múltiple y anidamiento).

## Nivel 1 — Condicional simple (`if`)

En estos problemas, el algoritmo siempre produce cierta salida base; la condición solo determina si se agrega **una acción adicional**. Note que **no se necesita `else`**: si la condición es falsa, el algoritmo simplemente continúa sin ejecutar ese paso adicional.

### 1. Alerta de aforo en un evento

Un centro de eventos necesita controlar el aforo de sus salones. Escriba un programa que le pida al usuario la capacidad máxima del salón y el número de asistentes registrados. El programa debe mostrar siempre el número de asistentes registrados; además, **únicamente si el número de asistentes supera la capacidad máxima**, debe mostrar un mensaje de alerta indicando por cuántas personas se excedió el aforo.

**Restricción:** resuelva este problema utilizando una única instrucción `if` (sin `else`).

**Ejemplo de ejecución del programa (caso con exceso de aforo):**

```
Capacidad máxima: 300
Asistentes registrados: 350

Asistentes registrados: 350
Alerta: se excedió el aforo en 50 personas
```

**Casos de prueba:**

| Caso | Capacidad máxima | Asistentes | ¿Hay alerta? | Mensaje de alerta |
|---|---|---|---|---|
| 1 | 300 | 350 | Sí | Excede en 50 personas |
| 2 | 300 | 280 | No | (no se muestra) |

### 2. Recargo por pago tardío de una factura

Una empresa cobra un recargo por mora en el pago de sus facturas: si una factura se paga con **más de 5 días** de retraso, se aplica un recargo del 3% sobre el valor original. Escriba un programa que le pida al usuario el valor de la factura y el número de días de retraso en el pago, y que calcule y muestre el valor del recargo (0 si no aplica) y el valor total a pagar.

> [!Tip]
> **Pista**: inicialice una variable `recargo` en 0 antes de evaluar la condición. Solo si el retraso es mayor a 5 días, reasigne `recargo` con el 3% del valor de la factura. El total a pagar (`valor_factura + recargo`) se calcula siempre, después del `if`, sin necesidad de un `else`.

**Casos de prueba:**

| Caso | Valor factura | Días de retraso | Recargo | Total a pagar |
|---|---|---|---|---|
| 1 | $500.000 | 10 | $15.000 | $515.000 |
| 2 | $500.000 | 3 | $0 | $500.000 |
| 3 | $500.000 | 5 | $0 | $500.000 |

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> En el caso 3, el retraso es exactamente 5 días y no hay recargo. ¿Qué habría pasado si la condición se hubiera escrito como `dias_retraso >= 5` en lugar de `dias_retraso > 5`? ¿Por qué es importante leer con cuidado si un enunciado dice "más de", "al menos" o "mínimo"?

### 3. Turno preferencial en una fila de atención

Una entidad bancaria asigna turnos de atención general a todos sus clientes, pero da prioridad adicional a las personas mayores. Escriba un programa que le pida al usuario su edad y siempre muestre el mensaje `Turno asignado: General`; **únicamente si la persona tiene 62 años o más**, el programa debe mostrar además el mensaje `Aplica para turno preferencial`.

**Restricción:** resuelva este problema utilizando una única instrucción `if` (sin `else`).

**Casos de prueba:**

| Caso | Edad | ¿Aplica turno preferencial? |
|---|---|---|
| 1 | 70 | Sí |
| 2 | 40 | No |
| 3 | 62 | Sí |

## Nivel 2 — Selección entre dos alternativas (`if`-`else`)

En estos problemas, la condición **siempre** determina cuál de dos caminos mutuamente excluyentes debe tomar el algoritmo: en cualquier ejecución, se ejecuta exactamente una de las dos ramas.

### 4. Aprobación de una materia

Escriba un programa que le pida al usuario el nombre del estudiante y su nota final en una materia (valor entre 0.0 y 5.0). Si la nota final es mayor o igual a 3.0, el programa debe mostrar el mensaje `Aprobado`; en caso contrario, debe mostrar el mensaje `Reprobado`.

**Casos de prueba:**

| Caso | Nota final | Resultado |
|---|---|---|
| 1 | 3.5 | Aprobado |
| 2 | 2.8 | Reprobado |
| 3 | 3.0 | Aprobado |

**Pregunta para pensar:**

> El caso 3 usa exactamente el valor límite (3.0). ¿Por qué es importante incluir siempre, en sus casos de prueba, un caso que use el valor exacto de la condición y no solo valores claramente arriba o abajo del límite?

### 5. Tarifa de un parqueadero

Un parqueadero cobra tarifas diferentes según la hora de ingreso del vehículo: si el vehículo ingresa entre las 6:00 y las 17:59 (es decir, `hora_ingreso >= 6` y `hora_ingreso < 18`), aplica la **tarifa diurna** de $2.000 por hora; en cualquier otro horario, aplica la **tarifa nocturna** de $3.000 por hora. Escriba un programa que le pida al usuario la hora de ingreso (formato militar, 0 a 23) y el número de horas que el vehículo permanecerá estacionado, y que calcule y muestre cuál tarifa se aplicó y el valor total a pagar.

> [!Tip]
> **Pista**: la condición completa de la tarifa diurna combina dos comparaciones con `and`: `hora_ingreso >= 6 and hora_ingreso < 18`.

**Casos de prueba:**

| Caso | Hora de ingreso | Horas estacionado | Tarifa aplicada | Total a pagar |
|---|---|---|---|---|
| 1 | 6 | 1 | Diurna | $2.000 |
| 2 | 10 | 3 | Diurna | $6.000 |
| 3 | 18 | 2 | Nocturna | $6.000 |
| 4 | 22 | 3 | Nocturna | $9.000 |

### 6. Multa por exceso de velocidad

En una vía urbana el límite de velocidad es de 60 km/h. Por cada km/h que un vehículo supere el límite, se cobra una multa de $20.000. Escriba un programa que le pida al usuario la velocidad registrada del vehículo (en km/h) y que muestre el valor de la multa; si el vehículo no superó el límite, el programa debe mostrar un mensaje indicando que no hay multa (no debe mostrar $0 como si fuera una multa real).

**Casos de prueba:**

| Caso | Velocidad (km/h) | Resultado |
|---|---|---|
| 1 | 85 | Multa de $500.000 |
| 2 | 55 | Sin multa |
| 3 | 60 | Sin multa |
| 4 | 61 | Multa de $20.000 |

## Nivel 3 — Varias alternativas

En estos problemas una sola comparación no alcanza: unas veces porque hay más de dos alternativas posibles sobre una misma variable (`elif`, o varios `if` independientes cuando las alternativas no se excluyen entre sí), y otras porque una condición solo tiene sentido evaluarla si otra condición anterior ya se cumplió (anidamiento verdadero). Los problemas están ordenados para que primero practique la selección entre varias opciones, y luego combine eso con la dependencia entre condiciones — que es, en últimas, la misma progresión que sigue cualquier programa real: primero decides entre varias alternativas, y esas alternativas a veces viven dentro de otra decisión más grande. **En los problemas con anidamiento real, no empiece escribiendo código:** primero dibuje o escriba en papel el árbol de decisiones completo.

### 7. Precio en la máquina dispensadora — Minimercado de Apu

En el minimercado de Apu hay una máquina dispensadora que tiene 4 productos etiquetados con los números 1, 2, 3 y 4, cada uno con un valor de $500, $800, $300 y $900, respectivamente. Diseñe un algoritmo que lea el número de producto que ingresa el usuario y le muestre su precio. Si el usuario ingresa un código que no corresponde a ninguno de los cuatro productos, el programa debe mostrar un mensaje indicando que el producto no es válido, en lugar de un precio.

**Este problema tiene dos partes:**

1. Resuélvalo primero usando **anidamiento puro**: cada `else` contiene, dentro de sí, el siguiente `if` que compara con el código restante (sin usar la palabra clave `elif`).
2. Reescriba **la misma lógica** usando una cadena `if` / `elif` / `elif` / `elif` / `else`.

Compare las dos versiones línea por línea antes de continuar.

<details>
<summary>Pista adicional</summary>

`elif` no es una estructura nueva: es una forma abreviada de escribir `else:` seguido, en la línea de abajo, de un nuevo `if`. Al usar `elif` evita que cada nueva comparación quede "empujada" más a la derecha (una sangría más), lo cual hace que el código sea más fácil de leer cuando hay varias alternativas mutuamente excluyentes sobre una misma variable, como el código del producto en este problema.

</details>

**Casos de prueba:**

| Caso | Código ingresado | Resultado esperado |
|---|---|---|
| 1 | 1 | $500 |
| 2 | 2 | $800 |
| 3 | 3 | $300 |
| 4 | 4 | $900 |
| 5 | 5 | Producto no válido |
| 6 | 0 | Producto no válido |

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> Al comparar sus dos versiones, ¿qué le pasó a la sangría (indentación) del código a medida que agregaba productos en la versión anidada pura? Si la máquina de Apu tuviera 20 productos en lugar de 4, ¿cuál de las dos versiones seguiría siendo legible y cuál no?

### 8. Factura de The Barking Lot

The Barking Lot es una guardería para perros que lo ha contratado a usted para desarrollar un programa que calcule la factura semanal de sus clientes. El programa debe leer el ID del propietario del perro, y el nombre, raza, edad y peso (en kilogramos) del perro, y mostrar una factura con todos esos datos junto con la tarifa semanal correspondiente, calculada así según el peso del perro:

* Menos de 7 kg: $55.000
* De 7 a 14 kg (inclusive): $75.000
* Más de 14 y hasta 37 kg (inclusive): $105.000
* Más de 37 kg: $125.000

**Ejemplo de ejecución del programa:**

```
ID del propietario: 1017654321
Nombre del perro: Rocky
Raza: Labrador
Edad: 3
Peso (kg): 9.5

Factura - The Barking Lot
--------------------------
ID propietario: 1017654321
Nombre del perro: Rocky
Raza: Labrador
Edad: 3 años
Peso: 9.5 kg

Tarifa semanal: $75.000
```

<details>
<summary>Pista adicional</summary>

Cuando los rangos son consecutivos y no se solapan (como aquí), no es necesario escribir cada condición con dos comparaciones (por ejemplo `peso >= 7 and peso <= 14`). Si ordena su cadena `if`/`elif` de menor a mayor peso, cada rama solo necesita comparar contra el **límite superior** de su rango, porque si el programa llegó hasta ahí es porque ya descartó (en las condiciones anteriores) todos los pesos menores:

```
si peso < 7:
    tarifa = 55000
si no, si peso <= 14:
    tarifa = 75000
si no, si peso <= 37:
    tarifa = 105000
si no:
    tarifa = 125000
```

Esta forma es más corta y, como verá en la pregunta de reflexión, evita por construcción el tipo de vacío que puede aparecer si cada rango se escribe de forma independiente.

</details>

**Casos de prueba:**

| Caso | Peso (kg) | Tarifa esperada |
|---|---|---|
| 1 | 5 | $55.000 |
| 2 | 6.99 | $55.000 |
| 3 | 7 | $75.000 |
| 4 | 14 | $75.000 |
| 5 | 14.5 | $105.000 |
| 6 | 37 | $105.000 |
| 7 | 37.1 | $125.000 |

Los casos 2-3, 4-5 y 6-7 prueban los límites exactos entre tarifas consecutivas.

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> Una versión anterior de este enunciado decía "de 7 a 14 kg inclusive" para la segunda tarifa y "de 14.1 a 37 kg inclusive" para la tercera, en vez de "más de 14 y hasta 37 kg". Pruebe mentalmente qué haría un algoritmo escrito exactamente así con un perro de 14.05 kg. ¿En qué tarifa cae? Ahora revise la pista adicional: ¿por qué la forma de escribir la cadena `elif` que se sugiere ahí (comparando solo contra el límite superior de cada rango) hace que este tipo de vacío sea imposible, sin importar qué tan finos sean los decimales del peso?

### 9. Letreros personalizados — Mark Daniels

Mark Daniels es un carpintero que crea letreros personalizados para casas. Necesita una aplicación que calcule el precio de cualquier letrero que pida un cliente, con base en los siguientes factores:

* El cargo mínimo para todos los letreros es $30.000.
* Si el letrero se hace de roble, se agregan $15.000. No se agrega ningún cargo por pino.
* Los primeros seis caracteres (letras o números) están incluidos en el cargo mínimo; hay un cargo adicional de $3.000 por cada carácter extra.
* Los caracteres en blanco o negro están incluidos en el cargo mínimo; hay un cargo adicional de $12.000 si son laminados en oro.

Diseñe un programa que calcule el precio del letrero y que acepte como datos el número de pedido, el nombre del cliente, el tipo de madera, el número de caracteres y el color de los caracteres, y que despliegue todos los datos ingresados junto con el precio final del letrero.

**Ejemplo de ejecución del programa:**

```
Número de pedido: 4521
Cliente: Laura Gómez
Tipo de madera: Roble
Número de caracteres: 12
Color de caracteres: Dorado

Pedido - Letreros Mark Daniels
-------------------------------
Número de pedido: 4521
Cliente: Laura Gómez
Madera: Roble
Caracteres: 12
Color: Dorado

Precio final: $75.000
```

> [!Tip]
> **`if` independientes, no `elif`**: en los problemas anteriores (la máquina de Apu, las tarifas de The Barking Lot) usamos `elif` porque las condiciones eran mutuamente excluyentes — solo una podía cumplirse a la vez. Aquí es distinto: la madera, la cantidad de caracteres y el color son factores independientes que pueden combinarse de cualquier manera (un letrero puede ser de roble, con muchos caracteres extra, y en dorado, todo al mismo tiempo). Por eso este problema se resuelve con **varias instrucciones `if` separadas**, cada una sumando su propio cargo — no con una cadena `elif` donde solo se ejecutaría una rama.

**Casos de prueba** (aíslan cada factor por separado y luego los combinan):

| Caso | Madera | Caracteres | Color | Precio esperado |
|---|---|---|---|---|
| 1 | Pino | 6 | Blanco | $30.000 |
| 2 | Roble | 6 | Blanco | $45.000 |
| 3 | Pino | 6 | Dorado | $42.000 |
| 4 | Pino | 7 | Blanco | $33.000 |
| 5 | Pino | 12 | Blanco | $48.000 |
| 6 | Roble | 12 | Dorado | $75.000 |

Los casos 1-2 aíslan el cargo por madera, el caso 3 aísla el cargo por color, los casos 4-5 aíslan el cargo por caracteres extra (incluyendo el límite exacto de 6), y el caso 6 combina los tres cargos a la vez.

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> Si hubiera escrito la condición de la madera y la del color como parte de la misma cadena `elif` (por ejemplo: `if madera == "roble": ... elif color == "dorado": ...`), ¿qué le habría pasado a un letrero de roble Y dorado al mismo tiempo? Pruébelo mentalmente con el caso 6 y explique por qué el resultado sería incorrecto.

### 10. Clasificación de un triángulo por sus lados

Dados los tres lados de un triángulo (`a`, `b`, `c`), escriba un programa que primero determine si esos tres lados **realmente forman un triángulo válido**, y si es así, lo clasifique según sus lados.

Para que tres longitudes formen un triángulo válido, la suma de cualquier par de lados debe ser mayor que el lado restante (desigualdad triangular): `a + b > c` **y** `a + c > b` **y** `b + c > a`.

Si el triángulo es válido, clasifíquelo así:

* **Equilátero**: los tres lados son iguales.
* **Isósceles**: exactamente dos lados son iguales (o los tres, pero ese caso ya se cubrió como equilátero).
* **Escaleno**: los tres lados son diferentes.

Si los lados no forman un triángulo válido, el programa debe indicarlo con un mensaje y no debe intentar clasificarlo.

**Casos de prueba:**

| Caso | a | b | c | Resultado |
|---|---|---|---|---|
| 1 | 5 | 5 | 5 | Equilátero |
| 2 | 5 | 5 | 8 | Isósceles |
| 3 | 4 | 5 | 6 | Escaleno |
| 4 | 1 | 2 | 10 | No es un triángulo válido |

**Antes de ejecutar:** complete su prueba de escritorio para los cuatro casos y escriba el resultado que espera obtener en cada uno, antes de correr el programa.

### 11. El mayor de tres números

Diseñe un algoritmo que lea tres números `A`, `B` y `C`, y muestre en pantalla cuál es el valor más grande de los tres.

**Restricción:** resuelva este problema utilizando condicionales anidados (`if` dentro de `if`); no utilice funciones predefinidas como `max()`.

<details>
<summary>Pista adicional</summary>

No es necesario comparar los tres pares de valores por separado. Compare primero `A` y `B`; dentro de cada una de esas dos ramas, compare el "ganador" contra `C`. Con solo dos niveles de anidamiento (dos comparaciones en el peor caso) es suficiente para resolver el problema, sin importar cuántos de los tres valores estén repetidos.

</details>

> [!Tip]
> **Sobre los casos de prueba**: no es necesario ni práctico probar todas las combinaciones posibles de valores para confiar en que un algoritmo funciona. Lo que realmente importa es que, entre todos sus casos de prueba, se recorra **cada camino distinto** que el algoritmo puede tomar: en este problema, que en algún caso gane A, en otro gane B, en otro gane C, y que se ponga a prueba qué pasa cuando hay valores repetidos. Unos pocos casos bien elegidos que cubran esos caminos dan la misma confianza que probar decenas de combinaciones sueltas — y son mucho más fáciles de verificar a mano.

**Casos de prueba:**

| Caso | A | B | C | Mayor esperado |
|---|---|---|---|---|
| 1 | 9 | 5 | 3 | A |
| 2 | 5 | 9 | 3 | B |
| 3 | 5 | 3 | 9 | C |
| 4 | 5 | 5 | 5 | 5 (cualquiera) |
| 5 | 7 | 7 | 3 | 7 (A o B) |
| 6 | 7 | 3 | 3 | A |

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> En el caso 5 hay un empate entre A y B, y ambos son el valor más grande. ¿Cuál de las dos variables reporta su algoritmo como "el mayor"? ¿Depende del orden en que escribió las comparaciones? ¿Por qué eso no es un error, sino una decisión de diseño válida?

### 12. Elegibilidad para un crédito educativo

Un fondo universitario ficticio otorga créditos educativos condonables siguiendo estas reglas, que deben evaluarse **en este orden**:

1. El solicitante debe tener entre 16 y 28 años (ambos incluidos). Si no cumple esta condición, el proceso termina de inmediato con el mensaje `No cumple el requisito de edad`.
2. Solo si cumple el requisito de edad, se evalúa su promedio académico: debe ser mayor o igual a 3.5. Si no lo cumple, el proceso termina con el mensaje `No cumple el promedio académico mínimo`.
3. Solo si cumple edad y promedio, se evalúa el estrato socioeconómico del solicitante: si es 1, 2 o 3, el mensaje final es `Aprobado: crédito 100% condonable`; si es 4, 5 o 6, el mensaje final es `Aprobado: crédito 50% condonable`.

Escriba un programa que le pida al usuario su edad, su promedio académico y su estrato, y que muestre **únicamente el mensaje correspondiente al primer criterio que no cumpla**, o el mensaje de aprobación correspondiente si cumple con todos.

**Casos de prueba:**

| Caso | Edad | Promedio | Estrato | Resultado |
|---|---|---|---|---|
| 1 | 20 | 4.2 | 2 | Aprobado: crédito 100% condonable |
| 2 | 20 | 4.2 | 5 | Aprobado: crédito 50% condonable |
| 3 | 20 | 3.0 | 2 | No cumple el promedio académico mínimo |
| 4 | 32 | 4.5 | 2 | No cumple el requisito de edad |

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> Si hubiera evaluado las tres condiciones (edad, promedio, estrato) con estructuras `if` independientes en lugar de anidadas, ¿habría sido posible que el programa mostrara más de un mensaje a la vez, o el mensaje incorrecto? Explique con un caso concreto.

### 13. Incentivo por producción

Una empresa tiene cuatro categorías salariales numeradas del 1 al 4. Además, tiene un programa de incentivos: si un empleado produjo **más de 50 unidades**, recibe un incremento sobre su salario mensual según su categoría — 5% para la categoría 1, 7% para la categoría 2, 10% para la categoría 3 y 15% para la categoría 4. Si no superó las 50 unidades, no recibe ningún incremento, sin importar su categoría.

Diseñe un algoritmo que lea el nombre, el salario mensual, la categoría y el número de unidades producidas de un empleado, y que muestre el valor del incentivo (si aplica) y el salario final que recibirá. Si la categoría ingresada no es 1, 2, 3 ni 4, el programa debe indicar que la categoría no es válida.

**Ejemplo de ejecución del programa (con incentivo):**

```
Nombre: Ana Pérez
Salario mensual: $1.000.000
Categoría: 2
Unidades producidas: 80

Incentivo por producción: $70.000
Salario final: $1.070.000
```

**Ejemplo de ejecución del programa (sin incentivo):**

```
Nombre: Carlos Ruiz
Salario mensual: $1.000.000
Categoría: 3
Unidades producidas: 30

No aplica incentivo (unidades producidas ≤ 50)
Salario final: $1.000.000
```

**Casos de prueba** (todos con salario mensual de $1.000.000):

| Caso | Categoría | Unidades | Incentivo | Salario final |
|---|---|---|---|---|
| 1 | 1 | 60 | $50.000 | $1.050.000 |
| 2 | 2 | 80 | $70.000 | $1.070.000 |
| 3 | 3 | 100 | $100.000 | $1.100.000 |
| 4 | 4 | 200 | $150.000 | $1.150.000 |
| 5 | 2 | 50 | No aplica (unidades no supera 50) | $1.000.000 |
| 6 | 3 | 30 | No aplica | $1.000.000 |
| 7 | 5 | 70 | — | Categoría no válida |

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> Con el diseño que usamos (primero se revisan las unidades, y solo dentro de esa rama se revisa la categoría), ¿qué pasaría con un empleado que tiene categoría 9 (inválida) pero solo produjo 30 unidades? ¿Su algoritmo reportaría el error de categoría inválida, o simplemente diría que no aplica incentivo, sin mencionar el problema con la categoría? ¿Le parece correcto ese comportamiento, o cree que la categoría debería validarse sin importar las unidades producidas?

### 14. Factura de Dash Cell Phone Company

Dash Cell Phone Company cobra a sus clientes una tarifa básica de $15.000 mensuales por el servicio de mensajes de texto, con las siguientes condiciones adicionales:

* Los primeros 60 mensajes del mes, sin importar su longitud, están incluidos en la tarifa básica.
* Se cobran $150 adicionales por cada mensaje enviado después del mensaje 60, hasta el mensaje 180.
* Se cobran $300 adicionales por cada mensaje enviado después del mensaje 180.
* Sobre el valor total de la factura (tarifa básica + cargos adicionales) se aplican impuestos por un 12%.

Diseñe un programa que lea los siguientes datos de un cliente:

* Código de área (3 dígitos).
* Número de teléfono (7 dígitos).
* Número de mensajes de texto enviados en el mes.

El programa debe mostrar todos los datos leídos, junto con el valor de la factura **antes** de impuestos y el valor **después** de aplicar el 12% de impuestos.

**Ejemplo de ejecución del programa:**

```
Código de área: 300
Número de teléfono: 4521987
Mensajes enviados: 210

Factura antes de impuestos: $54.000
Factura con impuestos (12%): $60.480
```

<details>
<summary>Pista adicional</summary>

El error más común en este tipo de problema es, para un cliente que envió más de 180 mensajes, cobrar *todos* sus mensajes por encima del 60 a $300 cada uno. Eso no es correcto: los mensajes entre el 61 y el 180 (120 mensajes) siempre se cobran a $150, sin importar cuántos mensajes más se hayan enviado después; solo los que exceden el mensaje 180 se cobran a $300. Es decir, cuando un cliente supera los 180 mensajes, su rama del algoritmo debe sumar **dos** cargos adicionales (el bloque completo de $150 × 120, más el excedente a $300), no reemplazar uno por el otro.

</details>

**Casos de prueba:**

| Caso | Mensajes enviados | Factura antes de impuestos | Factura con impuestos (12%) |
|---|---|---|---|
| 1 | 30 | $15.000 | $16.800 |
| 2 | 60 | $15.000 | $16.800 |
| 3 | 61 | $15.150 | $16.968 |
| 4 | 180 | $33.000 | $36.960 |
| 5 | 181 | $33.300 | $37.296 |
| 6 | 250 | $54.000 | $60.480 |

Los casos 2-3 y 4-5 están diseñados a propósito alrededor de los límites exactos (60/61 y 180/181): si su algoritmo usa `>` donde debía usar `>=` (o viceversa), estos casos lo revelarán.

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> Los casos 1 y 2 dan exactamente el mismo resultado (30 mensajes y 60 mensajes cuestan lo mismo). ¿Por qué tiene sentido que sea así, según la regla del enunciado? ¿Qué le indica esto sobre qué condición exacta debe usar para decidir si un mensaje adicional se cobra o no?

---

## Visualización de la ejecución

Seleccione una de las soluciones desarrolladas con anidamiento real — por ejemplo, **Clasificación de un triángulo**, **El mayor de tres números**, **Elegibilidad para un crédito educativo** o **Incentivo por producción** — y ejecútela utilizando **Python Tutor** (ver [Herramientas necesarias](#herramientas-necesarias)). Compare, para al menos dos de sus casos de prueba con resultados distintos:

1. Su prueba de escritorio
2. Su predicción
3. La ejecución mostrada por Python Tutor, prestando especial atención a **qué condiciones se evaluaron y en qué orden**, y cuáles ramas del `if` anidado nunca llegaron a ejecutarse.

Observe especialmente el momento exacto en que cada condición se evalúa como verdadera o falsa, y pregúntese: **¿la ejecución real del programa coincide con el árbol de decisiones que dibujé en mi diseño?**

## Verificación

Para cada problema:

1. Diseñe el algoritmo, identificando explícitamente cada condición.
2. Realice una prueba de escritorio que cubra **tanto el camino verdadero como el falso** de cada condición (y, en los problemas anidados, combinaciones que lleguen a cada rama posible), y escriba el resultado esperado en cada caso.
3. Implemente el programa.
4. Ejecute todos los casos de prueba proporcionados, incluyendo los casos límite.
5. Compare el resultado obtenido con el esperado.

Si los resultados son diferentes, **no modifique inmediatamente el código**. Primero intente identificar: **¿mi error está en la condición (operador o límite incorrecto), en el orden de las condiciones anidadas, en mi predicción, o en la implementación?**

## Reflexión final

Antes de finalizar el laboratorio, responda brevemente:

> ¿En cuál problema fue más difícil definir correctamente el límite de una condición (por ejemplo, decidir entre `>` y `>=`)? ¿Cómo se dio cuenta de que su primera versión estaba mal?

> En los problemas de condicionales anidados, ¿hubo algún caso de prueba que reveló que una condición interna se estaba evaluando aunque no debía (porque la condición externa ya era falsa)? ¿Qué aprendió al corregirlo?

El objetivo de esta reflexión no es evaluar si cometió errores, sino reconocer cómo cambió su forma de razonar sobre un algoritmo cuando este ya no es puramente secuencial, sino que puede tomar caminos distintos según los datos de entrada.

**Idea central del laboratorio:** un algoritmo con decisiones no tiene un único camino de ejecución. Diseñar bien una estructura condicional significa identificar con precisión cada condición, definir correctamente sus límites, y anticipar todos los caminos posibles antes de escribir código — no solo el camino más obvio.

## Recursos

* [Programación en pareja (pair programming) — Wikipedia](https://es.wikipedia.org/wiki/Programaci%C3%B3n_en_pareja): explicación del concepto, roles típicos (conductor y navegante) y beneficios de la técnica.
* [¿Qué es Pair Programming? — video de referencia](https://www.youtube.com/watch?v=q7d_JtyCq1A): ejemplo visual de cómo se aplica la técnica en la práctica.
* [Plantilla de solución de problemas (método de Polya)](./plantilla_metodo_polya_UdeA.docx): formato opcional para documentar los cuatro pasos del método de Polya en cada problema.

> [!important]
> ### Nota de transparencia sobre uso de IA
> Se usó IA generativa para la redacción y organización del contenido de este laboratorio (enunciados, pistas y casos de prueba), tomando como referencia el formato del laboratorio anterior del curso. El docente revisó y validó el material final antes de su publicación; aun así, es posible que se haya pasado por alto algún error. Si encuentra alguna inconsistencia, se agradece informarla al docente para corregirla.