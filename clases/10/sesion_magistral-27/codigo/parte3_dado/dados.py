# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 3: modulo dados.

Funciones para simular el lanzamiento de un dado. No lee ni imprime nada.
Lo importan main.py y test_dados.py.
"""
import random

CARAS = 6


def lanzar_dado():
    """
    Simula el lanzamiento de un dado de seis caras.

    Supone:
        Nada: no recibe datos.
    Garantiza:
        Retorna un entero al azar entre 1 y 6, incluidos los extremos.
    """
    return random.randint(1, CARAS)
