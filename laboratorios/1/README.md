# Laboratorio 1 - Introducción a la logica de programación

## Objetivos

* Plantear algoritmos básicos mediante el uso de diagramas de flujo.
* Comprender el concepto de programación secuencial.
* Aprender a usar un IDE python para codificar programas.


## Actividad

Para los siguientes problemas realizar un analisis del problema de manera que aplique los conceptos vistos en clase. Antes de codificar el algoritmo se pide que realice a mano los siguientes procedimientos:
1. Planteamiento de la solución identificando: Entradas, salidas y proceso.
2. Realizar el diagrama de flujo o pseudocódigo del algoritmo planteado.
3. Hacer una prueba de escritorio sencilla para verificar que el algoritmo planteado esta bien realizado.
4. Codificar el python el algoritmo ya verificado.

## Problemas

1. **Nota definitiva del curso**: Escriba un programa que calcule la nota definitiva de un estudiante en un curso que se evalúa con cuatro notas, cada una con un porcentaje distinto sobre la nota final: la primera nota vale el 10%, la segunda el 20%, la tercera el 30% y la cuarta el 40%.

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
   **Pista**: la nota definitiva se obtiene multiplicando cada nota por su respectivo porcentaje (expresado como valor decimal, no como número entero) y sumando los resultados. Por ejemplo, con las notas del ejemplo: 4.0 × 0.10 + 3.5 × 0.20 + 4.5 × 0.30 + 3.0 × 0.40 = 3.65.
   
2. **Financiación de vehículos — Agencia XGW**: Dada la estabilidad económica que existe actualmente en Colombia, las agencias automotrices comienzan a ofrecer distintos planes de financiamiento para la comercialización de sus vehículos. La empresa XGW ofrece el siguiente plan de financiación: dado el monto total del vehículo (en pesos colombianos), el cliente debe pagar el 35% de enganche (cuota inicial) y el resto en 18 mensualidades sin interés.
   
   Realice un algoritmo que permita obtener cuál es el valor de la cuota inicial y el valor de las mensualidades que debe pagar el cliente.

3. **Porcentaje de hombres y mujeres**: Escriba un programa que le pregunte al usuario el número de hombres y el número de mujeres matriculados en una clase. El programa debe mostrar el porcentaje de hombres y de mujeres en la clase.

   > [!Tip] 
   **Pista***: Suponga que hay 8 hombres y 12 mujeres en una clase. Hay 20 estudiantes en la clase. El porcentaje de hombres se puede calcular como 8 ÷ 20 = 0.4, o 40%. El porcentaje de mujeres se puede calcular como 12 ÷ 20 = 0.6, o 60%.

4. **Plantación de vides**: Una viticultora está plantando varias filas nuevas de vides (cultivo de uva) y necesita saber cuántas vides plantar en cada fila. Ella ha determinado que, después de medir la longitud de una futura fila, puede usar la siguiente fórmula para calcular el número de vides que caben en la fila, junto con los ensambles de poste extremo (estructuras de soporte tipo espaldera, o "trellis") que deben construirse en cada extremo de la fila:

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
   >
   > **Pista**: la fórmula trabaja con medidas en pies, por lo que el programa debe convertir los datos de metros a pies antes de aplicarla (1 metro equivale aproximadamente a 3.28084 pies). Además, tenga en cuenta que el número de vides debe ser un valor entero (no tiene sentido hablar de una fracción de vid), por lo que el resultado debe truncarse a la parte entera, descartando los decimales.

5. **Número invertido**: Dado un número de dos dígitos, escriba un programa que obtenga el número invertido. Por ejemplo, si se ingresa el número 23, el programa debe mostrar 32.

   > [!Tip]
   **Pista**: puede obtener la cifra de las decenas y la cifra de las unidades usando división entera (`//`) y módulo (`%`). 

6. **Interés compuesto**: Cuando una cuenta bancaria paga interés compuesto, no solo paga intereses sobre el monto principal que fue depositado en la cuenta, sino también sobre los intereses que se han acumulado con el tiempo. Suponga que desea depositar cierta cantidad de dinero en una cuenta de ahorros y dejar que la cuenta gane interés compuesto durante un número determinado de años. La fórmula para calcular el saldo de la cuenta después de un número específico de años es:

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
   **Pista**: la tasa de interés anual (r) debe ingresarse como un valor decimal, no como porcentaje. Por ejemplo, una tasa del 5% se debe ingresar como 0.05.

7. **Un minuto después**: Escriba un programa que le pida al usuario una hora en formato militar (24 horas), indicando por separado la hora (0 a 23) y los minutos (0 a 59). El programa debe calcular y mostrar cuál será la hora exactamente un minuto después.

   Por ejemplo, si el usuario ingresa la hora 14 y los minutos 59, el programa debe mostrar 15:00. Si el usuario ingresa la hora 23 y los minutos 59, el programa debe mostrar 0:00 (la medianoche del día siguiente).

   > [!Tip]
   **Pista**: no es necesario usar condicionales para resolver el acarreo de minutos a horas ni el de horas a un nuevo día. Puede lograrlo combinando los operadores de división entera (`//`) y módulo (`%`). Piense primero cómo obtener el nuevo valor de los minutos usando `%`, y luego cómo saber si ese incremento de un minuto "se pasó" de 59 a 0 usando `//`, para sumar ese resultado a la hora. Finalmente, aplique `%` sobre la hora para que, si se llega a 24, vuelva a 0.

