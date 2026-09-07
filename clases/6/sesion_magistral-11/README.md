![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesión magistral 11

* **Tipo**: Presencial
* **Fecha**: 01/09/2026
* **Parte**: Primer bloque de clase (14-16)

## Resumen

Se continúa repasando, en el tablero y por partes, un ejemplo de implementación de condicionales múltiples visto en las presentaciones de clase. El ejercicio combina dos fuentes de complejidad —una estructura condicional simple para el cálculo de horas extra y una estructura condicional anidada para el cálculo de impuestos por tramos— y se resuelve dividiéndolo en dos etapas independientes, verificando cada una con datos de prueba antes de integrarlas. Esta forma de avanzar no es solo una conveniencia de tablero: es el mismo hábito que conviene tener al programar cualquier problema con varias reglas de negocio — resolver y probar una parte a la vez, en vez de escribir todo de un tirón y depurar al final.

## Ejemplos

### Ejemplo 1

Se desea obtener la nómina semanal (salario neto) de los empleados de una empresa cuyo trabajo se paga por horas, del siguiente modo:

* Las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa que se debe introducir por teclado, igual que el número de horas y el nombre del trabajador.
* Las horas superiores a 35 se pagarán como extra, a un precio de 1.5 veces la hora normal.
* Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
  * Si sueldo <= 300000, libre de impuestos.
  * Los siguientes 150000 al 20%.
  * El resto al 30%.

#### Solución

El enunciado tiene dos reglas de negocio bien diferenciadas —el pago de horas (incluyendo el recargo por horas extra) y la deducción de impuestos por tramos— así que conviene resolverlas por separado: primero se plantea y se prueba únicamente el cálculo del salario base, y solo una vez confirmado que esa parte funciona correctamente se añade la lógica de impuestos sobre el resultado ya validado. Esto evita mezclar dos posibles fuentes de error en un solo intento y hace más fácil ubicar cualquier falla durante las pruebas.

La siguiente tabla resume las variables que va a necesitar la solución completa (algunas, como `imp`, `sal_neto` y `resto`, solo entran en juego en la segunda parte, pero se listan aquí desde el inicio para tener panorama completo del problema):

|#|Tipo|Nombre|Descripción|
|---|---|---|---|
|1|Constante (Entera)|`HORA_BASE = 35`|Cantidad mínima de horas normales|
|2|Constante (Real)|`EXTRA = 1.5`|Factor de cobro para la hora extra|
|3|Entrada (Texto)|`nom`|Nombre del empleado|
|4|Entrada (Entera)|`hr`|Cantidad total de horas trabajadas|
|5|Entrada (Entera)|`valor_hr`|Valor de la hora|
|6|Auxiliar (Entera)|`hr_extra`|Cantidad de horas extra|
|7|Salida (Real)|`sal_base`|Salario base (sin descontar impuestos)|
|8|Salida (Real)|`imp`|Impuestos|
|9|Salida (Real)|`sal_neto`|Salario a pagar (base - impuestos)|

Para verificar que el cálculo del salario base está bien planteado, antes de tocar el tema de impuestos, se usan estos dos casos:

|#|Valor hora|Horas trabajadas|Salario base esperado|
|----|----|----|----|
|1|10000|30|300000|
|2|10000|45|500000|

##### Parte 1 — Cálculo del salario base

El siguiente pseudocódigo cubre únicamente esta primera parte del problema:

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

**Pruebas de escritorio**

**Prueba 1**

|`hr`|`valor_hr`|`hr_extra`|`sal_base`|
|----|----|----|----|
|~~~?~~~|~~~?~~~|~~~?~~~|~~~?~~~|
|↘ 30|↘ 10000 |~~~0~~~|~~~0~~~|
|    |         | 0 |300000 ↗|

**Prueba 2**

|`hr`|`valor_hr`|`hr_extra`|`sal_base`|
|----|----|----|----|
|~~~?~~~|~~~?~~~|~~~?~~~|~~~?~~~|
|↘ 45|↘ 10000 |~~~0~~~|~~~0~~~|
|    |         | 10 | 500000 ↗|

Con estos dos casos se cubre tanto la rama de horas normales (Prueba 1) como la rama de horas extra (Prueba 2), que es justo la que conviene comprobar con más cuidado por ser la más propensa a errores de planteamiento.

El código Python correspondiente a esta primera parte queda así:

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
```

##### Parte 2 — Cálculo de impuestos

Con el salario base ya validado, se aborda la segunda regla de negocio. Para esto se necesita una variable auxiliar adicional:

|#|Tipo|Nombre|Descripción|
|---|---|---|---|
|10|Auxiliar (Real)|`resto`|Parte del salario por encima del mínimo del tramo, sobre la que se aplica cada tarifa|

El pseudocódigo de esta parte traduce directamente los tres tramos del enunciado: sin impuesto hasta 300000, 20% sobre los siguientes 150000, y 30% sobre lo que exceda 450000 (nótese que en el tramo más alto el segundo tramo se cobra completo, `0.2*150000`, y el 30% aplica solo sobre el excedente):

```
Si sal_base <= 300000 Entonces
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

Se retoman los salarios base ya confirmados en la parte anterior para probar este bloque:

|#|Valor hora|Horas trabajadas|Salario base|Impuesto esperado|Salario neto esperado|
|----|----|----|----|----|----|
|1|10000|30|300000|0|300000|
|2|10000|45|500000|45000|455000|

**Pruebas de escritorio**

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

##### Solución completa

Con las dos partes ya verificadas por separado, se integran en un solo algoritmo:

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

  Si sal_base <= 300000 Entonces
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

Y el código Python completo, ya con la salida en forma de recibo de pago:

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
# print(sal_base) # Se comento porque ya se verifico previamente que el calculo del salario base es correcto

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

## Buenas prácticas

Con lo visto hasta ahora (instrucciones secuenciales y estructuras condicionales, simples y anidadas), conviene ir adquiriendo estos hábitos. Algunos puntos se complementan con las notas de CS50 sobre [fundamentos de Python](https://cs50.harvard.edu/python/notes/1/) y [condicionales](https://cs50.harvard.edu/x/notes/1/#conditionals), referenciadas al final.

**Sobre variables y datos**

* **Declarar antes de usar, e inicializar siempre.** Toda variable de salida o auxiliar (`sal_base`, `imp`, `hr_extra`, `resto`) se inicializa antes del `Leer`, aunque el valor final se calcule más adelante. Esto evita depender de un valor "basura" si alguna rama del condicional no llega a asignarla.
* **Usar CONSTANTES para los valores fijos del enunciado.** `HORA_BASE` y `EXTRA` no cambian entre ejecuciones; escribirlas como constantes con nombre (en mayúsculas) en vez de repetir `35` o `1.5` sueltos en el código hace que, si el enunciado cambia esos valores, solo haya que modificarlos en un lugar.
* **Nombrar las variables por lo que representan**, no por su tipo o posición (`sal_base`, `sal_neto`, `hr_extra` se entienden solos; `x1`, `aux2` no).
* **No asumir que el dato de entrada es válido.** CS50 lo resume como "nunca asumas que la entrada del usuario es correcta": aquí `hr` y `valor_hr` se leen directamente sin comprobar, por ejemplo, que no sean negativos. No hace falta resolverlo todavía, pero es un hábito a tener presente a medida que los programas crecen.

**Sobre las condiciones**

* **Verificar que la condición compare la variable correcta.** Es el error más fácil de cometer y más difícil de detectar a simple vista: escribir `Si (sal_base <= HORA_BASE)` en vez de `Si (hr <= HORA_BASE)` compila y "corre" igual, pero calcula mal. Antes de dar por buena una condición, preguntarse: ¿esta variable ya tiene, en este punto del algoritmo, el valor que necesito comparar?
* **No confundir comparar con asignar.** En Python, `=` asigna un valor (`sal_base = valor_hr*hr`) y `==` compara si dos valores son iguales. Es una de las confusiones más comunes al empezar (CS50 la señala explícitamente): una condición como `if sal_base = 300000` no compara nada, es un error de sintaxis en Python — la forma correcta es `if sal_base == 300000`.
* **Probar cada rama del condicional, no solo el caso "feliz".** Un solo caso de prueba con horas normales no habría revelado el error anterior; hizo falta un caso con horas extra para forzar la otra rama. Como regla práctica: si una estructura `Si/Sino` tiene dos caminos, se necesitan casos de prueba que recorran los dos.
* **Encadenar condiciones mutuamente excluyentes en vez de anidar sin necesidad.** El bloque de impuestos ya hace esto: una vez se sabe que `sal_base > 300000`, no hace falta volver a preguntar por ese caso, solo por los que quedan. En Python esto se escribe de forma más plana con `elif` en lugar de un `else` que contiene otro `if` adentro:

  ```py
  if sal_base <= 300000:
      imp = 0
  elif sal_base <= 450000:
      resto = sal_base - 300000
      imp = 0.2*resto
  else:
      resto = sal_base - 450000
      imp = 0.2*150000 + 0.3*resto
  ```

  Es equivalente a la versión con `if` anidado dentro del `else` que ya usamos, pero con un nivel menos de sangría — vale la pena tenerlo presente para cuando el número de tramos o condiciones crezca.

**Sobre la relación pseudocódigo–código**

* **Mantener pseudocódigo y código fuente sincronizados.** Si se corrige un error en uno, debe reflejarse en el otro; de lo contrario quedan como dos versiones distintas del algoritmo y el pseudocódigo deja de servir como referencia confiable.
* **Usar impresiones temporales para verificar por partes, y luego comentarlas (no borrarlas).** El `print(sal_base)` intermedio de este ejemplo es un buen hábito de depuración incremental: se deja comentado una vez confirmado, como rastro de que esa parte ya se validó.

**Para profundizar**

* CS50P — [Conditionals and functions](https://cs50.harvard.edu/python/notes/1/)
* CS50x — [Conditionals](https://cs50.harvard.edu/x/notes/1/#conditionals)

### Referencia

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.