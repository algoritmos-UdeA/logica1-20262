# -*- coding: utf-8 -*-
"""
Pruebas del modulo notas.

Ejecutar con: python test_notas.py
"""

import notas

# calcular_promedio
assert round(notas.calcular_promedio([3.0, 4.5, 2.0, 4.0]), 3) == 3.375  # tipico
assert notas.calcular_promedio([3.5]) == 3.5                              # limite: un estudiante
assert notas.calcular_promedio([4.0, 4.0, 4.0]) == 4.0                    # especial: todas iguales

# contar_mayores_que
assert notas.contar_mayores_que([3.0, 4.5, 2.0, 4.0], 3.375) == 2         # tipico
assert notas.contar_mayores_que([4.0, 4.0, 4.0], 4.0) == 0                # especial: iguales no cuentan
assert notas.contar_mayores_que([3.5], 3.5) == 0                          # limite: un estudiante
assert notas.contar_mayores_que([], 3.0) == 0                             # limite: lista vacia

# posiciones_mayores_que
assert notas.posiciones_mayores_que([3.0, 4.5, 2.0, 4.0], 3.375) == [1, 3]   # tipico
assert notas.posiciones_mayores_que([4.0, 4.0, 4.0], 4.0) == []              # especial
assert notas.posiciones_mayores_que([5.0, 1.0, 5.0], 3.0) == [0, 2]          # primera y ultima

# Las funciones no modifican la lista que reciben
datos = [3.0, 4.5, 2.0, 4.0]
notas.posiciones_mayores_que(datos, 3.375)
assert datos == [3.0, 4.5, 2.0, 4.0]

print("Pruebas de notas: todas pasaron")
