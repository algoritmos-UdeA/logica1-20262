"""Pruebas de la clase Conductor. Se ejecuta con: python test_conductor.py"""
from conductor import Conductor

# Un conductor nuevo está disponible y en (0.0, 0.0)
cj = Conductor("2002", "CJ", "GRV992")
assert cj.get_cedula() == "2002"
assert cj.get_nombre() == "CJ"
assert cj.get_placa() == "GRV992"
assert cj.esta_disponible() == True
assert str(cj) == "2002 CJ (GRV992) en (0.0, 0.0) disponible"

# Cambiar de posición
cj.set_posicion(1.0, 1.0)
assert cj.get_posicion().get_x() == 1.0
assert cj.get_posicion().get_y() == 1.0

# Ocupar y liberar
cj.ocupar()
assert cj.esta_disponible() == False
assert str(cj) == "2002 CJ (GRV992) en (1.0, 1.0) ocupado"
cj.liberar()
assert cj.esta_disponible() == True

# Ocupar a un conductor no ocupa a otro
tommy = Conductor("2001", "Tommy", "VCT986")
cj.ocupar()
assert tommy.esta_disponible() == True

print("Pruebas de conductor: todas pasaron")
