"""
Clase 14 - Pruebas de notas.py.

leer_nombres, leer_notas y mostrar_estudiantes usan input() o print():
se prueban ejecutando el programa.
"""

import notas

NOTAS = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
PESOS = [0.3, 0.3, 0.4]

# calcular_notas_finales
finales = notas.calcular_notas_finales(NOTAS, PESOS)
assert len(finales) == 4
assert round(finales[0], 2) == 2.95                                    # tipico
assert round(finales[1], 2) == 4.55
assert round(finales[2], 2) == 2.9
assert round(finales[3], 2) == 3.75
assert notas.calcular_notas_finales([[4.0, 2.0]], [0.5, 0.5]) == [3.0]  # limite: 1 fila
assert notas.calcular_notas_finales([[3.0, 5.0]], [1.0, 0.0]) == [3.0]  # especial: peso 0
assert NOTAS[0] == [3.0, 3.5, 2.5]                                      # no modifica

# buscar_mayor y buscar_menor
assert notas.buscar_mayor([2.95, 4.55, 2.9, 3.75]) == 4.55
assert notas.buscar_menor([2.95, 4.55, 2.9, 3.75]) == 2.9
assert notas.buscar_mayor([3.5]) == 3.5                                 # limite

# contar_iguales y posiciones_iguales
assert notas.contar_iguales([4.0, 3.0, 4.0], 4.0) == 2
assert notas.posiciones_iguales([4.0, 3.0, 4.0], 4.0) == [0, 2]         # empate
assert notas.posiciones_iguales([4.0, 3.0], 5.0) == []                  # no esta
assert notas.posiciones_iguales([], 4.0) == []                          # lista vacia

# Empate en la nota final: dos estudiantes con las mismas notas
empate = notas.calcular_notas_finales([[4.0, 4.0, 4.0],
                                       [3.0, 3.0, 3.0],
                                       [4.0, 4.0, 4.0]], PESOS)
mayor = notas.buscar_mayor(empate)
assert notas.posiciones_iguales(empate, mayor) == [0, 2]

print("Pruebas de notas: todas pasaron")
