![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 11

* **Tipo**: Presencial
* **Fecha**: 01/09/2026
* **Parte**: Primer bloque de clase (14-16)

## Resumen

Se continua repasando un ejemplo de implementación de condicionales multiples de las presentaciones de clase. Este ejemplo se realiza en el tablero por partes.

## Ejemplos

### Ejemplo 1

Se desea obtener la nomina semanal (salario neto) – de los empleados de una empresa cuyo trabajo se paga por horas y del siguiente modo:
* Las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa que se debe introducir por teclado igual que el numero de horas y el nombre del trabajador.
* Las horas superiores a 35 se pagaran como extra a un precio de 1.5 horas normales. 
* Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
  * Si sueldo <= 300000, libre de impuestos.
  * Los siguientes 150000 al 20%.
  * El resto al 30%.

#### Solución

Este problema se abordo por partes (ha analizaba y se codificaba). Inicialmente solo se abordo la parte asociada al calculo del salario base segun las condiciones dadas en el enunciado y se probo. La siguiente tabla muestra la declaración de variables

|#|Tipo|Nombre|Descripción|
|---|---|---|---|
|1|Constante (Entera)|`HORA_BASE = 35`|Cantidad minima de horas normales|
|2|Constante (Real)|`EXTRA = 1.5`|Factor de cobro para la hora extra|
|3|Entrada (Texto)|`nom`|Nombre del empleado|
|4|Entrada (Entera)|`hr`|Cantida total de horas trabajadas|
|5|Entrada (Entera)|`valor_hr`|Valor de la hora|
|6|Auxiliar (Entera)|`hr_extra`|Cantidad de horas extras|
|7|Salida (Real)|`sal_base`|Salario base (sin descontar impuestos)|
|8|Salida (Real)|`imp`|Impuestos|
|9|Salida (Real)|`sal_neto`|Salario a pagar (base - impuestos)|


Los siguientes valores de prueba se van a emplear para verificar que el algoritmo de calculo de suelto esta bien planteado:

|#|Valor hora|Horas trabajadas|Salario base|
|----|----|----|----|
|1|10000|30|300000|
|2|10000|45|500000|

#### Pseudocodigo

```
Inicio
  HORA_BASE = 35
  EXTRA = 1.5
  sal_base = 0
  hr_extra = 0
  imp = 0
  sal_neto = 0

  Leer(nom, hr, valor_hr)
  Si (hr <= HORA_BASE) Entonces
    sal_base = valor_hr*hr
  Sino
    hr_extra = hr - HORA_BASE
    sal_base = valor_hr*HORA_BASE + EXTRA*valor_hr*hr_extra 
  Fin_Si
  Escribir(sal_base)
Fin
```

#### Pruebas de escritorio

**Prueba 1**

|`hr`|`valor_hr`|`hr_extra`|`sal_base`|
|----|----|----|----|
|~~~?~~~|~~~?~~~|~~~?~~~|~~~?~~~|
|↘ 30|↘ 10000 |~~~0~~~|~~~0~~~|
|    |         | 10 |300000 ↗|

**Prueba 2**

|`hr`|`valor_hr`|`hr_extra`|`sal_base`|
|----|----|----|----|
|~~~?~~~|~~~?~~~|~~~?~~~|~~~?~~~|
|↘ 40|↘ 10000 |~~~0~~~|~~~0~~~|
|    |         | 10 | 500000 ↗|


#### Codigo python

```py
# Constantes
HORA_BASE = 35
EXTRA = 1.5

# Inicializacion de variables
sal_base = 0
hr_extra = 0
imp = 0
sal_neto = 0


# Entrada de datos
nom = input("Nombre: ")
hr = int(input("Horas: "))
valor_hr = int(input("Valor hora: "))

# Calculo del salario base
if hr <= HORA_BASE:
    sal_base = valor_hr*hr
else:
    hr_extra = hr - HORA_BASE
    sal_base = valor_hr*HORA_BASE + EXTRA*valor_hr*hr_extra

print(sal_base)  # Se imprime para verificar el calculo del salario base

# Calculo de los impuestos
# To Do...
```

El problema aun esta incompleto. Inicialmente vamos a definir otras auxiliares mas para la implementación de esta parte:

|#|Tipo|Nombre|Descripción|
|---|---|---|---|
|10|Auxiliar (Real)|`resto`|Parte del salario por encima del minimo base sin impuestos|

A continuación, el siguiente pseudocogido implementa la parte donde se hacen las validaciones necesarias para obtener el impuesto:

```
SI sal_base <= 300000 Entonces
    imp = 0
Sino
    Si sal_base <= 450000 Entonces
        resto = sal_base - 300000
        imp = 0.2*resto
    Sino
        resto = sal_base - 450000
        imp = 0.2*150000 + 0.3*resto
    Fin_Si
Fin_Si
sal_neto = sal_base - imp
```

Vamos a realizar los siguientes casos de test para el pseucododigo anterior, continuando con los valores previos obtenidos para el salario neto.

|#|Valor hora|Horas trabajadas|Salario base|Impuesto|Salario neto|
|----|----|----|----|----|----|
|1|10000|30|300000|0|300000|
|2|10000|45|500000|45|455000|

A continuación se muestran las pruebas de escritorio para cada caso:

**Prueba 1**

|`sal_base`|`imp`|`resto`|`sal_neto`|
|----|----|----|----|
|~~~?~~~|~~~?~~~|~~~?~~~|~~~?~~~|
|300000|~~~0~~~|0|~~~0~~~|
|      |   0 ↗ | |300000 ↗|

**Prueba 2**

|`sal_base`|`imp`|`resto`|`sal_neto`|
|----|----|----|----|
|~~~?~~~|~~~?~~~|~~~?~~~|~~~?~~~|
|500000| ~~~0~~~ |~~~0~~~|~~~0~~~|
|      |    45000 ↗ | 50000 | 455000 ↗|


Finalmente, el pseudocodigo completo del problema se muestra a continuación:

```
Inicio
  HORA_BASE = 35
  EXTRA = 1.5
  sal_base = 0
  hr_extra = 0
  imp = 0
  sal_neto = 0
  resto = 0

  Leer(nom, hr, valor_hr)
  Si (hr <= HORA_BASE) Entonces
    sal_base = valor_hr*hr
  Sino
    hr_extra = hr - HORA_BASE
    sal_base = valor_hr*HORA_BASE + EXTRA*valor_hr*hr_extra 
  Fin_Si  

  SI sal_base <= 300000 Entonces
    imp = 0
  Sino
    Si sal_base <= 450000 Entonces
      resto = sal_base - 300000
      imp = 0.2*resto
    Sino
      resto = sal_base - 450000
      imp = 0.2*150000 + 0.3*resto
    Fin_Si
  Fin_Si

  sal_neto = sal_base - imp
  Escribir(sal_base,imp,sal_neto)
Fin
```

Finalmente, el código python asociado al pseudocodigo anterior se muestra a continuación:

```py
# Constantes
HORA_BASE = 35
EXTRA = 1.5

# Inicializacion de variables
sal_base = 0
hr_extra = 0
imp = 0
sal_neto = 0
resto = 0

nom = input("Nombre: ")
hr = int(input("Horas: "))
valor_hr = int(input("Valor hora: "))
# Calculo del salario base
if hr <= HORA_BASE:
    sal_base = valor_hr*hr
else:
    hr_extra = hr - HORA_BASE
    sal_base = valor_hr*HORA_BASE + EXTRA*valor_hr*hr_extra
# print(sal_base) # Se comento por que se verifico previamente que el calculo del salario base es correcto

# Calculo de los impuestos
if sal_base <= 300000:
    # Caso sin impuestos
    imp = 0
else:
    # Caso con impuestos
    if sal_base <= 450000:
        # Impuestos tipo 1
        resto = sal_base - 300000
        imp = 0.2*resto
    else:
        # Impuestos tipo 2
        resto = sal_base - 450000
        imp = 0.2*150000 + 0.3*resto

# Calculo del salario neto
sal_neto = sal_base - imp

# print(sal_base,imp,sal_neto) # Impresion rapida para verificar los calculos de salario base, impuestos y salario neto

# Salida de datos (Impresion del recibo de pago)
print("----------------------------------")
print("        RECIBO DE PAGO ")
print(f"Empleado: {nom}")
print(f"- Salario base: $ {sal_base}")
print(f"- impuestos: $ {imp}")
print(f"- Salario neto: $ {sal_neto}")
print("----------------------------------")
```


### Referencia


> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.