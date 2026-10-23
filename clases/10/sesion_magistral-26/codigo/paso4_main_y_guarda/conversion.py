# -*- coding: utf-8 -*-
"""
Sesion 26 - Paso 4 (no se hizo en clase): modulo conversion.

Solo funciones de conversion de temperatura: no lee, no imprime
y no tiene pruebas. Lo importan main.py y test_conversion.py.
"""

def celsius_a_fahrenheit(temp_c):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Supone:
        temp_c es un número (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en grados Fahrenheit (float).
    """
    temp_f = (9/5)*temp_c + 32
    return temp_f


def celsius_a_kelvin(temp_c):
    """
    Convierte una temperatura de grados Celsius a Kelvin.

    Supone:
        temp_c es un número (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en Kelvin (float),
        mayor o igual a 0.
    """
    temp_k = temp_c + 273.15
    return temp_k


def kelvin_a_celsius(temp_k):
    """
    Convierte una temperatura de Kelvin a grados Celsius.

    Supone:
        temp_k es un número (int o float) mayor o igual a 0
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en grados Celsius (float),
        mayor o igual a -273.15.
    """
    temp_c = temp_k - 273.15
    return temp_c
