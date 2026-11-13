"""Pruebas de la clase Cliente. Se ejecuta con: python test_cliente.py"""
from cliente import Cliente

# Un cliente nuevo está en (0.0, 0.0)
lucia = Cliente("1001", "Lucia")
assert lucia.get_cedula() == "1001"
assert lucia.get_nombre() == "Lucia"
assert lucia.get_posicion().get_x() == 0.0
assert lucia.get_posicion().get_y() == 0.0
assert str(lucia) == "1001 Lucia en (0.0, 0.0)"

# Cambiar de posición
lucia.set_posicion(2.0, 3.0)
assert lucia.get_posicion().get_x() == 2.0
assert lucia.get_posicion().get_y() == 3.0
assert str(lucia) == "1001 Lucia en (2.0, 3.0)"

# Cada cliente tiene su propio punto: mover a uno no mueve al otro
michael = Cliente("1002", "Michael")
assert lucia.get_posicion() is not michael.get_posicion()
michael.set_posicion(5.0, 5.0)
assert str(lucia) == "1001 Lucia en (2.0, 3.0)"

# El cliente y su punto colaboran: distancia entre dos clientes
lucia.set_posicion(0.0, 0.0)
michael.set_posicion(3.0, 4.0)
assert lucia.get_posicion().calcular_distancia(michael.get_posicion()) == 5.0

print("Pruebas de cliente: todas pasaron")
