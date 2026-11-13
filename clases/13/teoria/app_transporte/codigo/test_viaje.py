"""Pruebas de la clase Viaje. Se ejecuta con: python test_viaje.py"""
from cliente import Cliente
from conductor import Conductor
from viaje import Viaje

lucia = Cliente("1001", "Lucia")
cj = Conductor("2002", "CJ", "GRV992")
cj.set_posicion(1.0, 1.0)

# Al crear el viaje: conoce a los dos y ocupa al conductor
viaje = Viaje(lucia, cj, 6.0, 8.0)
assert viaje.get_cliente() is lucia
assert viaje.get_conductor() is cj
assert cj.esta_disponible() == False
assert viaje.esta_finalizado() == False

# Origen (la posición del cliente al solicitarlo) y destino
assert str(viaje.get_origen()) == "(0.0, 0.0)"
assert str(viaje.get_destino()) == "(6.0, 8.0)"

# Distancia y valor: 4000 + 1500 * 10
assert viaje.calcular_distancia() == 10.0
assert viaje.calcular_valor() == 19000.0
assert str(viaje) == ("Lucia con CJ: (0.0, 0.0) -> (6.0, 8.0) | "
                      "10.00 km | $19000 | en curso")

# Al finalizar: los dos quedan en el destino y el conductor se libera
viaje.finalizar()
assert viaje.esta_finalizado() == True
assert str(lucia.get_posicion()) == "(6.0, 8.0)"
assert str(cj.get_posicion()) == "(6.0, 8.0)"
assert cj.esta_disponible() == True

# El origen es un punto propio del viaje: no se movió con el cliente
assert str(viaje.get_origen()) == "(0.0, 0.0)"
assert viaje.calcular_distancia() == 10.0

# Caso límite: un viaje al mismo lugar solo cobra la tarifa base
corto = Viaje(lucia, cj, 6.0, 8.0)
assert corto.calcular_distancia() == 0.0
assert corto.calcular_valor() == 4000.0

print("Pruebas de viaje: todas pasaron")
