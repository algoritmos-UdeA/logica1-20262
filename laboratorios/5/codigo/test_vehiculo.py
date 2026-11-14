"""
Punto de chequeo 1: pruebas de la clase Vehiculo.
Se ejecutan con: python test_vehiculo.py

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.
"""
from vehiculo import Vehiculo

# Las constantes de la clase
assert Vehiculo.CARRO == "carro"
assert Vehiculo.MOTO == "moto"

# Un carro
carro = Vehiculo("ABC123", Vehiculo.CARRO)
assert carro.get_placa() == "ABC123"
assert carro.get_tipo() == "carro"
assert str(carro) == "ABC123 (carro)"

# Una moto
moto = Vehiculo("XYZ78A", Vehiculo.MOTO)
assert moto.get_placa() == "XYZ78A"
assert moto.get_tipo() == Vehiculo.MOTO
assert str(moto) == "XYZ78A (moto)"

# Dos vehículos son dos objetos distintos: cada uno tiene sus datos
assert carro.get_placa() == "ABC123"
assert carro is not moto

print("Punto de chequeo 1 superado: la clase Vehiculo pasa todas sus pruebas")
