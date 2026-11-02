"""Pruebas de ordenamientos.py. Se ejecutan con: python test_ordenamientos.py"""
from ordenamientos import (intercambiar, posicion_menor, ordenar_seleccion,
                           ordenar_burbuja, ordenar_insercion)

# intercambiar (caso 3: se llama y después se revisa la lista)
X = [29, 10, 14, 37, 13]
intercambiar(X, 0, 1)
assert X == [10, 29, 14, 37, 13]        # típico: vecinos
X = [29, 10, 14, 37, 13]
intercambiar(X, 0, 4)
assert X == [13, 10, 14, 37, 29]        # límite: primero y último
X = [29, 10, 14, 37, 13]
intercambiar(X, 2, 2)
assert X == [29, 10, 14, 37, 13]        # especial: la misma posición

# posicion_menor (caso 1: retorna y no modifica)
X = [29, 10, 14, 37, 13]
assert posicion_menor(X, 0) == 1        # típico: toda la lista
assert posicion_menor(X, 2) == 4        # típico: desde el medio
assert posicion_menor(X, 4) == 4        # límite: desde el último
assert posicion_menor([5, 3, 3], 0) == 1   # especial: menor repetido
assert posicion_menor([7], 0) == 0      # especial: un solo elemento
assert X == [29, 10, 14, 37, 13]        # no modifica la lista

# Los tres métodos: los mismos cinco casos
for ordenar in (ordenar_seleccion, ordenar_burbuja, ordenar_insercion):
    X = [29, 10, 14, 37, 13]
    ordenar(X)
    assert X == [10, 13, 14, 29, 37]    # ejemplo de la clase
    X = [1, 2, 3, 4]
    ordenar(X)
    assert X == [1, 2, 3, 4]            # ya ordenada
    X = [5, 4, 3, 2, 1]
    ordenar(X)
    assert X == [1, 2, 3, 4, 5]         # al revés
    X = [3.0, 1.5, 3.0, 1.5]
    ordenar(X)
    assert X == [1.5, 1.5, 3.0, 3.0]    # con repetidos
    X = [7]
    ordenar(X)
    assert X == [7]                     # un solo elemento

# Así NO (descomentar en clase): la función retorna None
# X = [29, 10, 14, 37, 13]
# assert ordenar_seleccion(X) == [10, 13, 14, 29, 37]

print("Pruebas de ordenamientos: todas pasaron")
