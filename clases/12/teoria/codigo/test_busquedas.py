"""Pruebas de busquedas.py. Se ejecutan con: python test_busquedas.py"""
from busquedas import buscar_lineal, buscar_binaria

# buscar_lineal (no necesita lista ordenada)
X = [5.0, 4.0, 3.5, 2.87]
assert buscar_lineal(X, 3.5) == 2          # típico: está en el medio
assert buscar_lineal(X, 5.0) == 0          # límite: el primero
assert buscar_lineal(X, 2.87) == 3         # límite: el último
assert buscar_lineal(X, 7.0) == -1         # especial: no está
assert buscar_lineal([1, 2, 1], 1) == 0    # especial: repetido -> la primera
assert buscar_lineal([], 3.5) == -1        # especial: lista vacía

# buscar_binaria (Supone: lista ordenada de menor a mayor)
X = [2.87, 3.5, 4.0, 5.0]
assert buscar_binaria(X, 3.5) == 1          # típico: está en el medio
assert buscar_binaria(X, 2.87) == 0         # límite: el primero
assert buscar_binaria(X, 5.0) == 3          # límite: el último
assert buscar_binaria(X, 1.0) == -1         # especial: menor que todos
assert buscar_binaria(X, 7.0) == -1         # especial: mayor que todos
assert buscar_binaria(X, 3.7) == -1         # especial: en un hueco
assert buscar_binaria([1, 2, 2, 2, 3], 2) == 2   # especial: repetido -> una de ellas
assert buscar_binaria([], 3.5) == -1        # especial: lista vacía
# Así NO (descomentar en clase): lista de mayor a menor, no cumple el Supone
# assert buscar_binaria([5.0, 4.0, 3.5, 2.87], 3.5) == 2

print("Pruebas de busquedas: todas pasaron")
