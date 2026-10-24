# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:59:00 2026

@author: Soportedrai
"""

import funciones


#### Test
print(funciones.jugar_maquina())
print(funciones.jugar_maquina())
print(funciones.jugar_maquina())
print(funciones.jugar_maquina())

print(funciones.lanzar_dado())
print(funciones.lanzar_dado())
print(funciones.lanzar_dado())
print(funciones.lanzar_dado())

assert funciones.definir_ganador(1, 3) == 1, "ERROR: debe ganar tijeras"