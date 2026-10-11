# -*- coding: utf-8 -*-
"""
Aproximacion del seno con la serie de Taylor.

Ejemplo de una funcion que llama a otra (seno -> factorial)
y de un parametro con valor por defecto (n=10).
"""

def factorial(n):
    """
    Calcula el factorial de n.

    Supone:
        n es un entero mayor o igual a 0.
    Garantiza:
        Retorna n! (int). factorial(0) es 1.
    """
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def seno(x, n=10):
    """
    Aproxima el seno de x sumando los primeros n terminos de la serie de Taylor.

    Supone:
        x es un angulo en radianes (int o float); n es un entero >= 1.
    Garantiza:
        Retorna la aproximacion de sen(x) (float).
    """
    suma = 0
    for k in range(n):
        suma = suma + (-1)**k * x**(2*k + 1) / factorial(2*k + 1)
    return suma

############ Pruebas ##############
assert factorial(0) == 1
assert factorial(5) == 120
assert round(seno(0), 6) == 0.0
assert round(seno(1.0), 6) == 0.841471
assert round(seno(1.0, 3), 6) == 0.841667

############ Programa principal #########
print(seno(1.0))          # n omitido: usa 10 terminos
print(seno(1.0, 3))       # solo 3 terminos
print(seno(n=3, x=1.0))   # argumentos por nombre
