"""
Clase 14 - Pruebas de la clase Matriz.
"""

from matriz import Matriz

# Constructor y consultas
m = Matriz(2, 3)
assert m.get_filas() == 2 and m.get_columnas() == 3
assert m.get(1, 2) == 0.0                 # todas las casillas empiezan en 0.0
assert Matriz(2, 2, 1.5).get(0, 1) == 1.5 # valor inicial dado
assert not m.es_cuadrada()
assert Matriz(3, 3).es_cuadrada()

# set valida la posicion
assert m.set(0, 0, 4.0)                   # posicion valida
assert m.get(0, 0) == 4.0
assert not m.set(2, 0, 9.0)               # fila 2 no existe
assert not m.set(0, -1, 9.0)              # no se aceptan negativos
assert m.get(0, 0) == 4.0                 # no cambio nada

# sumar_fila y sumar_columna
m.set(0, 1, 2.0)
m.set(1, 1, 3.0)
assert m.sumar_fila(0) == 6.0
assert m.sumar_columna(1) == 5.0

# transpuesta: una Matriz nueva, la original no cambia
t = m.transpuesta()
assert t.get_filas() == 3 and t.get_columnas() == 2
assert t.get(1, 0) == 2.0 and t.get(1, 1) == 3.0
assert m.get_filas() == 2

# sumar: una Matriz nueva
s = m.sumar(Matriz(2, 3, 1.0))
assert s.get(0, 0) == 5.0 and s.get(1, 2) == 1.0
assert m.get(0, 0) == 4.0                 # m no cambio

# __str__
assert str(Matriz(1, 2, 3.0)) == "   3.0   3.0"

print("Pruebas de Matriz: todas pasaron")
