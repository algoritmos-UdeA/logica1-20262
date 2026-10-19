# -*- coding: utf-8 -*-
"""
Modulo conversiones: funciones para convertir temperaturas.
"""


def celsius_a_fahrenheit(temp_c):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Supone:
        temp_c es un numero (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en grados Fahrenheit (float).
    """
    temp_f = (9 / 5) * temp_c + 32
    return temp_f
