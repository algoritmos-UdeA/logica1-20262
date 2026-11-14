"""
Punto de chequeo 2: pruebas de la clase Puesto.
Se ejecutan con: python test_puesto.py

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.
"""
from vehiculo import Vehiculo
from puesto import Puesto

# Un puesto nuevo está libre
puesto = Puesto(1, 3)
assert puesto.get_piso() == 1
assert puesto.get_numero() == 3
assert puesto.esta_libre() == True
assert puesto.get_vehiculo() == None
assert str(puesto) == "Piso 1, puesto 3: libre"

# Ocupar un puesto libre
carro = Vehiculo("ABC123", Vehiculo.CARRO)
assert puesto.ocupar(carro) == True
assert puesto.esta_libre() == False
assert puesto.get_vehiculo() is carro           # el mismo objeto, no una copia
assert str(puesto) == "Piso 1, puesto 3: ABC123 (carro)"

# Un puesto ocupado no se puede ocupar otra vez: el primer vehículo se queda
moto = Vehiculo("XYZ78A", Vehiculo.MOTO)
assert puesto.ocupar(moto) == False
assert puesto.get_vehiculo() is carro

# Liberar: el puesto queda libre y entrega el vehículo que tenía
assert puesto.liberar() is carro
assert puesto.esta_libre() == True
assert puesto.get_vehiculo() == None

# Liberar un puesto que ya estaba libre entrega None
assert puesto.liberar() == None
assert puesto.esta_libre() == True

# Un puesto liberado se puede volver a ocupar
assert puesto.ocupar(moto) == True
assert str(puesto) == "Piso 1, puesto 3: XYZ78A (moto)"

# Dos puestos son dos objetos distintos: ocupar uno no ocupa el otro
otro = Puesto(2, 1)
assert otro.esta_libre() == True

print("Punto de chequeo 2 superado: la clase Puesto pasa todas sus pruebas")
