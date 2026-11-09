![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 13 — Código de ejemplo

Esta carpeta reúne los programas de la clase 13, agrupados por **ejemplo**. Cada sección presenta el enunciado y, debajo, los archivos que lo resuelven con su salida. Cada archivo tiene la clase (o las clases), un ejemplo de uso y sus pruebas con `assert`; si todas pasan, se imprime un mensaje final, y si alguna falla, el programa se detiene con `AssertionError` en la línea de esa prueba.

| # | Ejemplo | Archivos | Diapositivas |
|---|---|---|---|
| 1 | [El rectángulo](#1-el-rectángulo) | `ej1_rectangulo.py`, `ej1_rectangulo_privado.py` | 26-34 |
| 2 | [El ventilador](#2-el-ventilador) | `ej2_ventilador.py` | 35-39 |
| 3 | [El celular](#3-el-celular) | `ej3_celular.py` | 40-41 |
| 4 | [La cuenta bancaria](#4-la-cuenta-bancaria) | `ej4_cuenta_titular.py` | 42-48 |
| 5 | [Un arreglo de cuentas](#5-un-arreglo-de-cuentas) | `ej5_arreglo_cuentas.py` | 49-51 |
| 6 | [El banco](#6-el-banco) | `ej6_banco.py` | 52-59 |

> [!TIP]
> Los scripts se ejecutan desde esta carpeta, con `python ej1_rectangulo.py`, etc. `ej5_arreglo_cuentas.py` importa las clases de `ej4_cuenta_titular.py`, así que los dos archivos tienen que estar juntos.

---

## 1. El rectángulo

### Enunciado

> Diseñe una clase llamada `Rectangulo` para representar un rectángulo. La clase contiene:
>
> - Dos atributos, `base` y `altura`.
> - Un constructor que crea un rectángulo con la base y la altura dadas.
> - Un método `calcular_area()` que retorna el área.
> - Un método `calcular_perimetro()` que retorna el perímetro.
>
> Dibuje el diagrama UML y luego impleméntela. Pruébela con dos rectángulos: de 3.0 × 4.0 y de 5.0 × 2.0.

*(Enunciado de la diapositiva 26).*

### Archivos

| Archivo | Qué muestra |
|---|---|
| [ej1_rectangulo.py](ej1_rectangulo.py) | La clase con atributos **públicos**. Prueba los dos rectángulos y muestra que `r1 is r3` da `False` aunque tengan los mismos valores: son dos objetos distintos. Al final, `r1.base = -5.0` se acepta sin ningún control. |
| [ej1_rectangulo_privado.py](ej1_rectangulo_privado.py) | La versión mejorada: atributos **privados** (`self.__base`), `get_base`/`get_altura` para consultar y `set_base`/`set_altura` para cambiar. Los *setters* solo aceptan valores mayores que 0 y devuelven `True` o `False`. Al final muestra que `r2.__base = -5.0`, escrito desde afuera, no da error pero crea otro atributo: la base verdadera, `r2._Rectangulo__base`, sigue en 3.0. |

### Salida

`ej1_rectangulo.py`:

```
False
Rectangulo: todas las pruebas pasaron
-20.0
-2.0
```

`ej1_rectangulo_privado.py`:

```
Rectangulo: todas las pruebas pasaron
3.0
12.0
-5.0
3.0
```

### Casos de prueba del rectángulo privado

| Caso | Tipo | Resultado esperado |
|---|---|---|
| `r1.set_base(5.0)` | Típico | `True`, y el área pasa a 20.0 |
| `r1.set_base(0.0)` | Límite | `False` |
| `r1.set_base(-5.0)` | Especial | `False` |
| `r1.get_base()` después de los rechazos | | `5.0`: el valor rechazado no entra |

---

## 2. El ventilador

### Enunciado

> Diseñe una clase llamada `Ventilador`. La clase contiene:
>
> - Tres constantes `LENTO`, `MEDIO` y `RAPIDO`, con los valores 1, 2 y 3, para indicar la velocidad.
> - Cuatro atributos privados, cada uno con su valor por defecto:
>
>   | Atributo | Tipo | Valor por defecto |
>   |---|---|---|
>   | `velocidad` | `int` | `LENTO` |
>   | `radio` | `float` | `5.0` |
>   | `color` | `str` | `"azul"` |
>   | `encendido` | `bool` | `False` |
>
> - Un constructor que crea un ventilador; si no se le dan valores, usa los valores por defecto.
> - Métodos para consultar cada atributo.
> - Un método para cambiar la velocidad, que solo acepta 1, 2 o 3, y otro para cambiar el color.
> - Métodos para encender y apagar el ventilador.
> - Un método que devuelve una descripción del ventilador en texto.
>
> Dibuje el diagrama UML, implemente la clase y escriba pruebas con dos ventiladores: uno rápido, de radio 10.0, color `"amarillo"` y encendido; otro con los valores por defecto.

*(Enunciado de la diapositiva 35).*

### Archivo

| Archivo | Qué muestra |
|---|---|
| [ej2_ventilador.py](ej2_ventilador.py) | Constantes de clase (`Ventilador.RAPIDO`), un constructor con valores por defecto, `set_velocidad` que valida y devuelve `bool`, métodos que cambian el estado y no devuelven nada (`encender`, `apagar`), y `__str__`, que da el texto de `print(v)` y de `str(v)`. |

### Salida

```
3 10.0 amarillo True
1 5.0 azul False
Ventilador azul, radio 5.0, velocidad 1, apagado
None
Ventilador azul, radio 5.0, velocidad 2, encendido
Ventilador: todas las pruebas pasaron
```

El `None` lo imprime `print(v3.encender())`: `encender` no devuelve nada; lo útil es que el ventilador queda encendido.

---

## 3. El celular

### Enunciado

> Implemente en Python la clase `Celular` a partir de su diagrama UML.
>
> Pruebas: cree un celular, cambie su precio y verifique los cambios con `assert`.
>
> Reto: haga que `set_precio` rechace los precios menores o iguales a 0 y devuelva `True` o `False`. ¿Qué cambia en el diagrama UML?

*(Enunciado de la diapositiva 40; el diagrama es [uml_celular.png](../images/uml_celular.png)).*

### Archivo

| Archivo | Qué muestra |
|---|---|
| [ej3_celular.py](ej3_celular.py) | La solución: atributos privados, *getters* y *setters* que no validan. La solución del reto está en un comentario, debajo del `set_precio`; para usarla, se reemplaza ese método por la versión comentada. En el UML, su línea pasa a ser `+ set_precio(precio: float) : bool`. |

### Salida

```
Celular: todas las pruebas pasaron
```

---

## 4. La cuenta bancaria

### Enunciado

> Diseñe dos clases:
>
> **Clase `Titular`**. La clase contiene:
> - Un atributo privado `nombre` (`str`).
> - Un atributo privado `cedula` (`str`).
> - Un constructor que crea un titular con su nombre y su cédula.
> - Métodos para consultar cada atributo.
>
> **Clase `CuentaBancaria`**. La clase contiene:
> - Un atributo privado `titular`, de tipo `Titular`.
> - Un atributo privado `saldo` (`float`), con valor por defecto 0.0.
> - Un constructor que crea una cuenta con su titular y su saldo inicial.
> - Métodos para consultar el titular y el saldo.
> - Un método `depositar` que suma un valor al saldo.
> - Un método `retirar` que resta un valor del saldo, solo si el saldo alcanza; devuelve `True` o `False`.
> - Un método `transferir` que pasa un valor de esta cuenta a otra cuenta, solo si el saldo alcanza; devuelve `True` o `False`.
> - Un método que devuelve una descripción de la cuenta en texto.
>
> Además: dibuje el diagrama UML de cada clase y el que las relaciona. Pruebe las clases: Homero abre su cuenta con 30000.0 y Marge con el saldo por defecto; Homero le transfiere 15000.0 a Marge, y después Marge intenta transferir más de lo que tiene.

*(Enunciado de la diapositiva 42).*

### Archivo

| Archivo | Qué muestra |
|---|---|
| [ej4_cuenta_titular.py](ej4_cuenta_titular.py) | Las dos clases. La cuenta guarda un objeto `Titular` como atributo, y `transferir` recibe otra cuenta como parámetro y usa sus propios métodos: `self.retirar(valor)` y luego `destino.depositar(valor)`. El uso y las pruebas están dentro de la guarda `if __name__ == "__main__":`, para que no se ejecuten cuando el Ejemplo 5 importa las clases. |

### Salida

```
Homero Simpson: $30000.0
Marge Simpson: $0.0
True
False
Homero Simpson: $15000.0
Marge Simpson: $15000.0
CuentaBancaria: todas las pruebas pasaron
```

### Casos de prueba

| Caso | Resultado esperado |
|---|---|
| Marge abre su cuenta con el saldo por defecto | Saldo 0.0 |
| Homero (30000.0) le transfiere 15000.0 a Marge | `True`; los dos quedan con 15000.0 |
| Marge (15000.0) intenta transferirle 99000.0 a Homero | `False`; los dos siguen con 15000.0 |

Una transferencia cambia dos cuentas, así que cada prueba revisa los dos saldos: si solo se revisara uno, un error en el otro pasaría sin que nadie lo notara.

---

## 5. Un arreglo de cuentas

### Enunciado

> Escriba un programa que guarde en un arreglo las cuentas de Homero (15000.0), Marge (15000.0) y el señor Burns (1000000.0), y que:
>
> - Encuentre la posición de la cuenta con el mayor saldo y muestre su descripción.
> - Le dé un bono de 10000.0 a cada cuenta y muestre todas las cuentas.

*(Enunciado de la diapositiva 49).*

### Archivo

| Archivo | Qué muestra |
|---|---|
| [ej5_arreglo_cuentas.py](ej5_arreglo_cuentas.py) | `cuentas = [None] * 3`, con una cuenta en cada casilla. La búsqueda de la posición del mayor compara `cuentas[i].get_saldo()`, no `cuentas[i]`. Para el bono no se reasigna la casilla: se le pide a cada cuenta que deposite, con `cuentas[i].depositar(10000.0)`. Importa `Titular` y `CuentaBancaria` de `ej4_cuenta_titular.py`. |

### Salida

```
2
Señor Burns: $1000000.0
Homero Simpson: $25000.0
Marge Simpson: $25000.0
Señor Burns: $1010000.0
```

---

## 6. El banco

### Enunciado

> Convertir el arreglo de cuentas del Ejemplo 5 en una clase `Banco`, con un nombre, un cupo y la cantidad de cuentas abiertas. El banco abre las cuentas (solo si hay cupo), encuentra la posición del mayor saldo, ordena las cuentas de mayor a menor saldo y le da un bono a cada cuenta. Pruebas: las mismas del Ejemplo 5, más ordenar y llenar el cupo de 5 cuentas.

*(Enunciado redactado a partir de las diapositivas 52-57).*

### Archivo

| Archivo | Qué muestra |
|---|---|
| [ej6_banco.py](ej6_banco.py) | La clase `Banco`, con el arreglo de cuentas como atributo privado (`self.__cuentas = [None] * cupo`) y `self.__cantidad`. Como el banco crea sus cuentas en `abrir_cuenta`, la relación es de composición. `posicion_mayor_saldo(inicio=0)` sirve para buscar el mayor de todo el banco y para ordenar; `ordenar_por_saldo` es la selección de mayor a menor, con un solo intercambio por paso porque se mueve la cuenta completa. Los recorridos van hasta `cantidad`, no hasta `len()`, porque las casillas libres siguen en `None`. Para que el archivo funcione solo, incluye `Titular`, `CuentaBancaria` y la función `intercambiar` de la clase 12. |

### Salida

```
2
Señor Burns: $1000000.0
Homero Simpson: $25000.0
Marge Simpson: $25000.0
Señor Burns: $1010000.0
Señor Burns: $1010000.0
Marge Simpson: $25000.0
Homero Simpson: $25000.0
Banco: todas las pruebas pasaron
```

Después de ordenar, Marge queda antes que Homero aunque tienen el mismo saldo: la selección no conserva el orden de los empates. No es un error.

### Casos de prueba

| # | Qué se hace | Resultado esperado | Por qué |
|---|---|---|---|
| 1 | Se abren las cuentas de Homero, Marge y el señor Burns | 3 cuentas abiertas | Los mismos datos del Ejemplo 5 |
| 2 | Se busca la posición del mayor saldo | 2 (el señor Burns) | Igual que en el Ejemplo 5 |
| 3 | Se da un bono de 10000.0 a cada cuenta | Homero queda con 25000.0 | Igual que en el Ejemplo 5 |
| 4 | Se ordenan las cuentas por saldo | El señor Burns queda en la posición 0 | Nuevo: ordenar |
| 5 | Se abren las cuentas de Lisa y Bart | `True` las dos: el banco queda lleno (5 de 5) | Caso límite: se llena el cupo |
| 6 | Se intenta abrir la cuenta de Maggie | `False`: no hay cupo | Caso especial: arreglo lleno |

*(Tabla de la diapositiva 57).*

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
