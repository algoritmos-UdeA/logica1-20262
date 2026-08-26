# Sesion magistral 9

## 1. Prueba de escritorio

Dado el diagrama de flujo de la figura, hacer la prueba de escritorio y a partir de esta determinar los valores finales de las variables y la salida en pantalla.

### Diagrama de flujo

![prueba_escritorio](ejemplo_prueba-escritorio.png)

### Código Python

**Achivo**: [prueba_escritorio.py](prueba_escritorio.py)

```py
a = 10
b = -3
i = 0

while i <= 5:
    if not(i%2 == 0):
        # yes
        a = a - 2
    else:
        # No
        b = b + 1
    b = (-2)*a
    i = i + 1
# Fin ciclo
print(a,b,i)
```

## Ejemplo 1

Moe con el fin de incentivar su negocio organizo una noche de solos y solas. Los precios que fijo fueron de $10000 para los hombres y de la mitad de este valor para las mujeres. Hacer un programa que de acuerdo al sexo de la persona que asista muestre el precio de la entrada al bar de Moe.

### Solución 1

Bug, no funciona miento con letras minusculas asociadas al sexo.

#### Pseudocodigo

```
Inicio
  PRECIO_HOMBRE = 10000
  PRECIO_MUJER = PRECIO_HOMBRE/2
  Leer(sexo)
  Si (sexo == 'M') Entonces    
    precio = PRECIO_HOMBRE
  Sino
    precio = PRECIO_MUJER
  Fin_Si
  Escribir(precio)
Fin
```

####  Código python

**Solución**: [ejemplo1_bar_moe_bug.py](ejemplo1_bar_moe_bug.py)

```py
# Constantea
PRECIO_HOMBRES = 10000
PRECIO_MUJERES = PRECIO_HOMBRES/2

# Entradas
sexo = input("Digite el sexo (M: Hombre / F: Mujer): ")

# Proceso
if sexo == 'M':
    precio = PRECIO_HOMBRES
else:
    precio = PRECIO_MUJERES

# Salidas
print(f"Valor: {precio}")
```

### Solución 2

#### Pseudocodigo

Mejora el problema de la anterior 

```
Inicio
  PRECIO_HOMBRE = 10000
  PRECIO_MUJER = PRECIO_HOMBRE/2
  Leer(sexo)
  Si ((sexo == 'M') or (sexo == 'm')) Entonces    
    precio = PRECIO_HOMBRE
  Sino
    precio = PRECIO_MUJER
  Fin_Si
  Escribir(precio)
Fin
```

**Código**: [ejemplo1_bar_moe_if_else.py](ejemplo1_bar_moe_if_else.py)

```py
# Constantea
PRECIO_HOMBRES = 10000
PRECIO_MUJERES = PRECIO_HOMBRES//2

# Entradas
sexo = input("Digite el sexo (M: Hombre / F: Mujer): ")

# Proceso
if (sexo == 'M') or (sexo == 'm'):
    precio = PRECIO_HOMBRES
else:
    precio = PRECIO_MUJERES

# Salidas
print(f"Valor: {precio}")
```

