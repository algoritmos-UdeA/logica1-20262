![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Laboratorio 1 — Introducción a la resolución de problemas y programación

## Objetivos

Al finalizar este laboratorio, el estudiante estará en capacidad de:

* Identificar las **entradas, procesos y salidas** de un problema computacional sencillo.
* Diseñar algoritmos secuenciales utilizando **diagramas de flujo o pseudocódigo**.
* Aplicar una estrategia sistemática de resolución de problemas antes de comenzar a programar.
* Verificar manualmente un algoritmo mediante **pruebas de escritorio y casos de prueba**, prediciendo el resultado antes de ejecutar el programa.
* Implementar algoritmos secuenciales básicos utilizando Python.
* Ejecutar y depurar programas sencillos utilizando un entorno de desarrollo.

## Herramientas necesarias

Para el desarrollo de esta práctica necesita, como mínimo, lo siguiente:

* **Anaconda**: distribución de Python que incluye el intérprete, el gestor de paquetes y Jupyter Notebook.
* **Visual Studio Code**: editor de código ligero, con la extensión de Python instalada, para escribir y ejecutar sus programas.
* **draw.io**: herramienta para diseñar diagramas de flujo (opcional para bocetar antes de pasarlos a papel; la versión final de cada diagrama debe entregarse a mano, según se indica en la metodología).
* **PyCharm** (opcional): alternativa de IDE más completa a Visual Studio Code.

Si no desea instalar nada, también puede trabajar con las siguientes plataformas en línea, sin necesidad de instalación:

* **Python Tutor** (pythontutor.com): visualización paso a paso de la ejecución de un programa. La usaremos también al final del laboratorio, en la sección [Visualización de la ejecución](#visualización-de-la-ejecución).
* **CodeSkulptor** (py3.codeskulptor.org): entorno de Python en el navegador, orientado a principiantes.

Adicionalmente, cada pareja debe traer hojas, lápiz/lapicero y, si lo desea, la plantilla de solución de problemas impresa (ver [Recursos](#recursos)) para desarrollar el método de Polya a mano.

## Metodología de trabajo

En este laboratorio utilizamos una versión simplificada del método de **George Pólya** para resolver problemas, aplicada **a mano** antes de escribir cualquier línea de código. Para cada problema, siga los siguientes pasos:

### 1. Entender el problema

Identifique:

* ¿Qué información recibe el problema? (datos de entrada)
* ¿Qué resultado debe producir? (datos de salida)
* ¿Qué variables o constantes auxiliares necesita?
* ¿Hay casos especiales que deban considerarse?

### 2. Diseñar un plan

Diseñe una solución mediante un **diagrama de flujo o pseudocódigo**. En esta etapa **todavía no escriba código Python**. Puede usar directamente los operadores de división entera (`//`) y módulo (`%`) donde el problema lo requiera; no es necesario descomponerlos en otras operaciones.

### 3. Revisar el plan (prueba de escritorio + predicción)

Realice una **prueba de escritorio** usando los casos de prueba proporcionados en cada problema. Antes de implementar cualquier programa, debe poder responder:

> **¿Qué resultado espero obtener, y por qué?**

### 4. Implementar el plan

Solo después de completar los pasos anteriores, codifique el algoritmo en Python y ejecútelo con los mismos casos de prueba, comparando la salida real contra su predicción (ver la sección [Verificación](#verificación)).

La idea central del laboratorio es:

> **Entender → Diseñar → Predecir → Implementar → Verificar**

Se proporciona una plantilla de solución de problemas (ver [Recursos](#recursos)) como guía opcional para organizar estos pasos. Su uso no es obligatorio: cada pareja es libre de aplicar el método de Polya en el formato que prefiera (a mano en hojas propias, en la plantilla, etc.), siempre que el análisis, el diagrama de flujo o pseudocódigo y la prueba de escritorio de cada problema queden documentados en papel. **Estos documentos deben traerse a la sesión de laboratorio**, ya que son la base para la codificación y para la sustentación del ejercicio ante el docente.

## Trabajo en parejas

El laboratorio se realiza mediante una dinámica inspirada en *pair programming* (ver [Recursos](#recursos)). Cada pareja trabaja con dos roles:

**Analista / Navegante**

* Lidera el análisis inicial del problema (pasos 1 a 3 del método de Polya).
* Revisa permanentemente la solución mientras su compañero programa.
* Identifica posibles errores y casos especiales.
* Piensa en el siguiente paso mientras se implementa la solución.

**Conductor / Programador**

* Implementa el algoritmo en Python (paso 4).
* Explica en voz alta lo que está escribiendo.
* Contrasta el código con el algoritmo diseñado por su compañero.
* Ejecuta y verifica los casos de prueba.

> **Importante:** ambos integrantes son responsables de comprender tanto el algoritmo como el código, y deben poder sustentar cualquier parte del trabajo ante el docente. Los roles deben **alternarse entre los problemas**, de manera que ambos tengan la oportunidad de ejercer los dos roles durante la sesión.

---

# Problemas

Los problemas están organizados aproximadamente de menor a mayor dificultad.

## Nivel 1 — Entrada, proceso y salida

En estos primeros problemas concéntrese en identificar claramente **entrada → proceso → salida**; no se requieren transformaciones complejas de los datos.

### 1. Nota definitiva del curso

Escriba un programa que calcule la nota definitiva de un estudiante en un curso que se evalúa con cuatro notas, cada una con un porcentaje distinto sobre la nota final: la primera nota vale el 10%, la segunda el 20%, la tercera el 30% y la cuarta el 40%.

El programa debe solicitar al usuario el nombre del estudiante, su número de identificación y las cuatro notas del curso (valores entre 0.0 y 5.0). Con esta información, el programa debe generar un informe que muestre cada nota junto con su porcentaje correspondiente, y finalmente la nota definitiva del curso.

**Ejemplo de ejecución del programa:**

```
Nombre del estudiante: María Gómez
Identificación: 1017654321

Informe de notas
-----------------
Nota 1 (10%): 4.0
Nota 2 (20%): 3.5
Nota 3 (30%): 4.5
Nota 4 (40%): 3.0

Nota definitiva: 3.65
```

> [!Tip]
> **Pista**: la nota definitiva se obtiene multiplicando cada nota por su respectivo porcentaje (expresado como valor decimal, no como número entero) y sumando los resultados. Por ejemplo, con el caso 1: 4.0 × 0.10 + 3.5 × 0.20 + 4.5 × 0.30 + 3.0 × 0.40 = 3.65.

**Casos de prueba:**

| Caso | Nota 1 (10%) | Nota 2 (20%) | Nota 3 (30%) | Nota 4 (40%) | Nota definitiva |
|---|---|---|---|---|---|
| 1 | 4.0 | 3.5 | 4.5 | 3.0 | 3.65 |
| 2 | 3.0 | 4.0 | 2.5 | 5.0 | 3.85 |

### 2. Porcentaje de hombres y mujeres

Escriba un programa que le pregunte al usuario el número de hombres y el número de mujeres matriculados en una clase. El programa debe mostrar el porcentaje de hombres y de mujeres en la clase.

Antes de programar, determine:

* ¿Cuál es el total de estudiantes?
* ¿Cómo se calcula un porcentaje?
* ¿Qué valor deberían sumar ambos porcentajes?

> [!Tip]
> **Pista**: el porcentaje de hombres se calcula dividiendo el número de hombres entre el total de estudiantes y multiplicando por 100. El mismo procedimiento aplica para el porcentaje de mujeres.

**Casos de prueba:**

| Caso | Hombres | Mujeres | Total estudiantes | % Hombres | % Mujeres |
|---|---|---|---|---|---|
| 1 | 8 | 12 | 20 | 40% | 60% |
| 2 | 15 | 10 | 25 | 60% | 40% |

### 3. Financiación de vehículos — Agencia XGW

Dada la estabilidad económica que existe actualmente en Colombia, las agencias automotrices comienzan a ofrecer distintos planes de financiamiento para la comercialización de sus vehículos. La empresa XGW ofrece el siguiente plan de financiación: dado el monto total del vehículo (en pesos colombianos), el cliente debe pagar el 35% de enganche (cuota inicial) y el resto en 18 mensualidades sin interés.

Realice un algoritmo que permita obtener cuál es el valor de la cuota inicial y el valor de las mensualidades que debe pagar el cliente. Identifique cuidadosamente los datos de entrada, las operaciones necesarias y los resultados esperados.

**Casos de prueba:**

| Caso | Monto del vehículo | Cuota inicial (35%) | Mensualidad (18 cuotas) |
|---|---|---|---|
| 1 | $60.000.000 | $21.000.000 | $2.166.666,67 |
| 2 | $85.000.000 | $29.750.000 | $3.069.444,44 |

### 4. Cuenta de un restaurante

Un grupo de amigos cena en un restaurante y quiere dividir la cuenta en partes iguales. Escriba un programa que le pida al usuario el valor total del consumo (sin propina), el porcentaje de propina que desean dejar y el número de personas que van a pagar. El programa debe calcular y mostrar:

* El valor de la propina.
* El valor total a pagar (consumo + propina).
* El valor que le corresponde pagar a cada persona.

Antes de implementar, escriba explícitamente la fórmula que utilizará para cada resultado.

**Ejemplo de ejecución del programa:**

```
Valor del consumo: 120000
Porcentaje de propina (%): 10
Número de personas: 4

Propina: 12000.0
Total a pagar: 132000.0
Valor por persona: 33000.0
```

> [!Tip]
> **Pista**: recuerde convertir el porcentaje de propina ingresado (por ejemplo, 10) a su forma decimal (0.10) antes de multiplicarlo por el consumo.

**Casos de prueba:**

| Caso | Consumo | Propina (%) | Personas | Propina ($) | Total ($) | Por persona ($) |
|---|---|---|---|---|---|---|
| 1 | $120.000 | 10 | 4 | $12.000 | $132.000 | $33.000 |
| 2 | $85.000 | 15 | 3 | $12.750 | $97.750 | $32.583,33 |

## Nivel 2 — Fórmulas y transformaciones

En los siguientes problemas no basta con identificar entradas y salidas: debe analizar cuidadosamente cómo transformar los datos de entrada para obtener el resultado.

### 5. Interés compuesto

Cuando una cuenta bancaria paga interés compuesto, no solo paga intereses sobre el monto principal que fue depositado en la cuenta, sino también sobre los intereses que se han acumulado con el tiempo. Suponga que desea depositar cierta cantidad de dinero en una cuenta de ahorros y dejar que la cuenta gane interés compuesto durante un número determinado de años. La fórmula para calcular el saldo de la cuenta después de un número específico de años es:

$$
A = P\left(1 + \frac{r}{n}\right)^{nt}
$$

Los términos de la fórmula son:

* **A** es la cantidad de dinero en la cuenta después del número de años especificado.
* **P** es el monto principal que originalmente fue depositado en la cuenta.
* **r** es la tasa de interés anual.
* **n** es el número de veces por año que el interés se compone (capitaliza).
* **t** es el número de años especificado.

Escriba un programa que realice el cálculo. El programa debe pedirle al usuario que ingrese lo siguiente:

* El monto principal originalmente depositado en la cuenta.
* La tasa de interés anual pagada por la cuenta.
* El número de veces por año que el interés se compone (por ejemplo, si el interés se compone mensualmente, se debe ingresar 12; si se compone trimestralmente, se debe ingresar 4).
* El número de años que la cuenta permanecerá generando intereses.

Una vez ingresados los datos, el programa debe calcular y mostrar la cantidad de dinero que habrá en la cuenta después del número de años especificado.

> [!Tip]
> **Pista**: la tasa de interés anual (r) debe ingresarse como un valor decimal, no como porcentaje. Por ejemplo, una tasa del 5% se debe ingresar como 0.05.

**Casos de prueba:**

| Caso | Principal (P) | Tasa anual (r) | Veces/año (n) | Años (t) | Monto final (A) |
|---|---|---|---|---|---|
| 1 | $1.000.000 | 0.05 | 12 | 3 | $1.161.330,30 |
| 2 | $2.000.000 | 0.08 | 4 | 5 | $2.971.894,79 |

### 6. Plantación de vides

Una viticultora está plantando varias filas nuevas de vides (cultivo de uva) y necesita saber cuántas vides plantar en cada fila. Ella ha determinado que, después de medir la longitud de una futura fila, puede usar la siguiente fórmula para calcular el número de vides que caben en la fila, junto con los ensambles de poste extremo (estructuras de soporte tipo espaldera, o "trellis") que deben construirse en cada extremo de la fila:

$$
V = \frac{R - 2E}{S}
$$

Los términos de la fórmula son:

* **V** es el número de vides que caben en la fila.
* **R** es la longitud de la fila, en pies.
* **E** es el espacio, en pies, usado por un ensamble de poste extremo.
* **S** es el espacio entre vides, en pies.

Como la viticultora toma sus medidas en metros, el programa debe pedirle al usuario que ingrese los siguientes datos en metros:

* La longitud de la fila, en metros.
* El espacio usado por un ensamble de poste extremo, en metros.
* El espacio entre las vides, en metros.

Una vez ingresados los datos, el programa debe calcular y mostrar el número de vides que caben en la fila.

> [!Tip]
> **Pista**: la fórmula trabaja con medidas en pies, por lo que el programa debe convertir los datos de metros a pies antes de aplicarla (1 metro equivale aproximadamente a 3.28084 pies). Además, tenga en cuenta que el número de vides debe ser un valor entero (no tiene sentido hablar de una fracción de vid), por lo que el resultado debe truncarse a la parte entera, descartando los decimales.

**Casos de prueba:**

| Caso | Longitud de fila (m) | Espacio poste extremo (m) | Espacio entre vides (m) | Vides (V) |
|---|---|---|---|---|
| 1 | 30 | 1 | 2 | 14 |
| 2 | 45 | 1.5 | 2.5 | 16 |

**Pregunta para pensar** (respóndala después de resolver el problema, no antes):

> Si R, E y S están expresadas inicialmente en la misma unidad (metros), ¿es realmente necesario convertirlas a pies antes de aplicar la fórmula? Justifique su respuesta matemáticamente, comparando el resultado de aplicar la fórmula directamente en metros contra el de convertir primero a pies.

## Nivel 3 — Pensamiento algorítmico

Los siguientes problemas requieren descubrir una estrategia de solución antes de traducirla a código. **No empiece escribiendo código.**

### 7. Número invertido

Dado un número de dos dígitos, escriba un programa que obtenga el número invertido.

**Casos de prueba:**

| Caso | Número | Número invertido |
|---|---|---|
| 1 | 23 | 32 |
| 2 | 48 | 84 |

**Pista 1:** piense primero: ¿cómo podría separar matemáticamente las dos cifras de un número? Intente resolverlo en papel antes de consultar la pista adicional.

<details>
<summary>Pista adicional</summary>

Puede obtener la cifra de las decenas y la cifra de las unidades usando división entera (`//`) y módulo (`%`). Por ejemplo, para el número 23: la decena se obtiene como 23 // 10 (= 2) y la unidad como 23 % 10 (= 3). Con estas dos cifras puede construir el número invertido como unidad × 10 + decena (= 32). Puede usar estos mismos operadores directamente en su diagrama de flujo o pseudocódigo. Tenga en cuenta que el programa asume que el usuario siempre ingresa un número de dos dígitos (entre 10 y 99); no es necesario validar este rango.

</details>

**Antes de ejecutar:** complete su prueba de escritorio y escriba el resultado que espera obtener, antes de correr el programa.

### 8. Un minuto después

Escriba un programa que le pida al usuario una hora en formato militar (24 horas), indicando por separado la hora (0 a 23) y los minutos (0 a 59). El programa debe calcular y mostrar cuál será la hora exactamente un minuto después.

**Restricción:** intente resolver el problema **sin utilizar estructuras condicionales**.

**Casos de prueba:**

| Caso | Hora | Minutos | Hora un minuto después |
|---|---|---|---|
| 1 | 10 | 23 | 10:24 |
| 2 | 14 | 59 | 15:00 |
| 3 | 23 | 59 | 0:00 |

Antes de programar, analice especialmente:

* ¿Qué ocurre cuando los minutos llegan a 60?
* ¿Qué ocurre después de las 23:59?
* ¿Existe alguna operación matemática que permita representar comportamientos cíclicos?

<details>
<summary>Pista adicional</summary>

No es necesario usar condicionales para resolver el acarreo de minutos a horas ni el de horas a un nuevo día. Puede lograrlo combinando los operadores de división entera (`//`) y módulo (`%`). Piense primero cómo obtener el nuevo valor de los minutos usando `%`, y luego cómo saber si ese incremento de un minuto "se pasó" de 59 a 0 usando `//`, para sumar ese resultado a la hora. Finalmente, aplique `%` sobre la hora para que, si se llega a 24, vuelva a 0. Puede usar estos mismos operadores directamente en su diagrama de flujo o pseudocódigo.

</details>

---

## Visualización de la ejecución

Seleccione una de las soluciones desarrolladas, preferiblemente **Número invertido** o **Un minuto después**, y ejecútela utilizando **Python Tutor** (ver [Herramientas necesarias](#herramientas-necesarias)). Compare:

1. Su prueba de escritorio.
2. Su predicción.
3. La ejecución mostrada por Python Tutor.

Observe especialmente cómo cambian los valores almacenados en las variables durante la ejecución, y pregúntese: **¿la ejecución real del programa coincide con el modelo que tenía en mente?**

## Verificación

Para cada problema:

1. Diseñe el algoritmo.
2. Realice una prueba de escritorio y escriba el resultado esperado.
3. Implemente el programa.
4. Ejecute los casos de prueba proporcionados.
5. Compare el resultado obtenido con el esperado.

Si los resultados son diferentes, **no modifique inmediatamente el código**. Primero intente identificar: **¿mi error está en el algoritmo, en mi predicción o en la implementación?**

## Reflexión final

Antes de finalizar el laboratorio, responda brevemente:

> ¿En cuál problema fue más importante pensar en el algoritmo antes de comenzar a escribir código? ¿Por qué?

> ¿Hubo algún caso en el que su predicción fuera diferente del resultado producido por el programa? ¿Qué aprendió al identificar la causa?

El objetivo de esta reflexión no es evaluar si cometió errores, sino reconocer cómo cambió su forma de resolver el problema.

**Idea central del laboratorio:** programar no consiste en comenzar a escribir código. Primero entendemos el problema, diseñamos una solución y razonamos sobre su comportamiento. El programa es la implementación de esa solución.

## Recursos

* [Programación en pareja (pair programming) — Wikipedia](https://es.wikipedia.org/wiki/Programaci%C3%B3n_en_pareja): explicación del concepto, roles típicos (conductor y navegante) y beneficios de la técnica.
* [¿Qué es Pair Programming? — video de referencia](https://www.youtube.com/watch?v=q7d_JtyCq1A): ejemplo visual de cómo se aplica la técnica en la práctica.
* [Plantilla de solución de problemas (método de Polya)](./plantilla_metodo_polya_UdeA.docx): formato opcional para documentar los cuatro pasos del método de Polya en cada problema.

> [!important]
> ### Nota de transparencia sobre uso de IA
> Se usó IA generativa para la redacción y organización del contenido de este laboratorio (enunciados, pistas y casos de prueba). El docente revisó y validó el material final antes de su publicación; aun así, es posible que se haya pasado por alto algún error. Si encuentra alguna inconsistencia, se agradece informarla al docente para corregirla.