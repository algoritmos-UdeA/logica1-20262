# -*- coding: utf-8 -*-
"""
Sesion 24 - Paso 2: las funciones y sus pruebas, sin el programa principal.

Este archivo solo tiene las funciones y sus pruebas con assert. No tiene
menu ni input(): la interaccion con el usuario queda para otro archivo.
Al ejecutarlo, las pruebas corren y el archivo termina de inmediato.
Si todas pasan, solo se muestra "Todas las pruebas pasaron".
"""

############ Funciones ############
# Despliegue
def menu():
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a °K")
    print("3. Salir")

# Conversion de temperatura
def c_to_f(c):
    f = (9/5)*c + 32
    return f

def c_to_k(c):
    k = c + 273.15
    return k

############ Test ################

# assert condición [, "Mensaje opcional"]

# c_to_f
assert c_to_f(5) == 41
assert round(c_to_f(1), 1) == 33.8, "El resultado es 33.8"
assert round(c_to_f(1.5), 1) == 34.7, "El resultado es 34.7"

# c_to_k
assert round(c_to_k(10), 2) == 283.15, "El resultado es 283.15"
assert round(c_to_k(-20), 2) == 253.15, "El resultado es 253.15"

print("Todas las pruebas pasaron")
