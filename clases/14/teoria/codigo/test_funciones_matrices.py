"""
Clase 14 - Pruebas de funciones_matrices.py.

leer_notas usa input(): no se prueba con assert, se prueba ejecutando.
"""

import funciones_matrices as fm

# Caso 1: calcular_promedio_fila
notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
assert fm.calcular_promedio_fila(notas, 1) == 4.5                     # tipico
assert fm.calcular_promedio_fila([[3.5]], 0) == 3.5                   # limite: 1 x 1
assert fm.calcular_promedio_fila([[4.0, 4.0], [1.0, 2.0]], 0) == 4.0  # especial
assert notas == [[3.0, 3.5, 2.5], [4.5, 4.0, 5.0],
                 [2.0, 3.0, 3.5], [4.0, 4.5, 3.0]]                    # no modifica

# Caso 3: aplicar_bonificacion
datos = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0]]
fm.aplicar_bonificacion(datos, 2, 0.5)
assert datos == [[3.0, 3.5, 3.0], [4.5, 4.0, 5.0]]   # tipico; 5.0 se queda en 5.0
datos = [[4.8, 1.0]]
fm.aplicar_bonificacion(datos, 0, 0.5)
assert datos == [[5.0, 1.0]]                         # especial: 5.3 se recorta
datos = [[3.0, 4.5]]
fm.aplicar_bonificacion(datos, 1, 0)
assert datos == [[3.0, 4.5]]                         # sin bonificacion no cambia

print("Pruebas de funciones_matrices: todas pasaron")
