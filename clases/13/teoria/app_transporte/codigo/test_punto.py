"""Pruebas de la clase Punto. Se ejecuta con: python test_punto.py"""
from punto import Punto

# Constructor y métodos de consulta
origen = Punto()
assert origen.get_x() == 0.0
assert origen.get_y() == 0.0
a = Punto(3.0, 4.0)
assert a.get_x() == 3.0
assert a.get_y() == 4.0
assert str(a) == "(3.0, 4.0)"

# Métodos de modificación
a.set_x(6.0)
a.set_y(8.0)
assert str(a) == "(6.0, 8.0)"

# Distancia: caso típico (triángulo 6-8-10), en los dos sentidos
assert origen.calcular_distancia(a) == 10.0
assert a.calcular_distancia(origen) == 10.0

# Distancia: caso límite (de un punto a sí mismo)
assert a.calcular_distancia(a) == 0.0

# Distancia: casos especiales (coordenadas negativas, resultado con decimales)
b = Punto(1.0, 1.0)
c = Punto(-4.0, -3.0)
assert round(origen.calcular_distancia(b), 2) == 1.41
assert round(b.calcular_distancia(c), 2) == 6.40

# calcular_distancia no modifica los puntos
assert str(b) == "(1.0, 1.0)"
assert str(c) == "(-4.0, -3.0)"

print("Pruebas de punto: todas pasaron")
