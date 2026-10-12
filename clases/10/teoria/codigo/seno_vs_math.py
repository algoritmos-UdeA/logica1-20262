# -*- coding: utf-8 -*-
"""
Funcion seno propia frente a la funcion sin de la libreria math.

Muestra como importar un modulo de la biblioteca estandar y usar
sus funciones y constantes.

Autor(es): Nombre Apellido
Fecha: dd/mm/aaaa
Version: 1
"""
import math


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def seno(x, n=10):
    suma = 0
    for k in range(n):
        suma = suma + (-1)**k * x**(2*k + 1) / factorial(2*k + 1)
    return suma


############ Pruebas ##############
assert math.isclose(seno(1.0), math.sin(1.0))
assert factorial(5) == math.factorial(5)

############ Programa principal #########
x = 1.0
print("Funcion propia:  seno(1.0)     =", seno(x))
print("Libreria math:   math.sin(1.0) =", math.sin(x))

# math.sin trabaja en radianes
print("math.sin(30)               =", math.sin(30))
print("math.sin(math.radians(30)) =", math.sin(math.radians(30)))
print("math.pi                    =", math.pi)
