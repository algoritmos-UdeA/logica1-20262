"""Pruebas de la clase Plataforma. Se ejecuta con: python test_plataforma.py"""
from punto import Punto
from cliente import Cliente
from conductor import Conductor
from plataforma import Plataforma

plataforma = Plataforma()

# Sin conductores no hay a quién asignar
assert plataforma.conductor_mas_cercano(Punto(0.0, 0.0)) == None

# Registrar y buscar
lucia = Cliente("1001", "Lucia")
kendl = Cliente("1003", "Kendl")
kendl.set_posicion(10.0, 10.0)
plataforma.registrar_cliente(lucia)
plataforma.registrar_cliente(kendl)

tommy = Conductor("2001", "Tommy", "VCT986")
tommy.set_posicion(3.0, 4.0)
cj = Conductor("2002", "CJ", "GRV992")
cj.set_posicion(1.0, 1.0)
plataforma.registrar_conductor(tommy)
plataforma.registrar_conductor(cj)

assert plataforma.buscar_cliente("1001") is lucia
assert plataforma.buscar_cliente("9999") == None
assert plataforma.buscar_conductor("2002") is cj
assert plataforma.buscar_conductor("9999") == None

# El conductor más cercano a (0, 0) es CJ (1.41 km); Tommy está a 5 km
assert plataforma.conductor_mas_cercano(Punto(0.0, 0.0)) is cj
# El más cercano a (3, 3) es Tommy (1 km)
assert plataforma.conductor_mas_cercano(Punto(3.0, 3.0)) is tommy

# Solicitar un viaje: Lucia va a (6, 8) con CJ
viaje = plataforma.solicitar_viaje("1001", 6.0, 8.0)
assert viaje != None
assert viaje.get_conductor() is cj
assert viaje.calcular_valor() == 19000.0
assert cj.esta_disponible() == False
assert plataforma.buscar_viaje_activo("1001") is viaje

# Un cliente con un viaje sin finalizar no puede solicitar otro
assert plataforma.solicitar_viaje("1001", 1.0, 1.0) == None

# Un cliente que no está registrado no puede solicitar
assert plataforma.solicitar_viaje("9999", 1.0, 1.0) == None

# CJ está ocupado: a Kendl le asignan a Tommy, el único disponible
viaje_kendl = plataforma.solicitar_viaje("1003", 13.0, 14.0)
assert viaje_kendl.get_conductor() is tommy
assert viaje_kendl.calcular_distancia() == 5.0

# Finalizar el viaje de Lucia
assert plataforma.finalizar_viaje("1001") == True
assert viaje.esta_finalizado() == True
assert cj.esta_disponible() == True
assert str(lucia.get_posicion()) == "(6.0, 8.0)"
assert plataforma.buscar_viaje_activo("1001") == None

# No se puede finalizar dos veces, ni el viaje de quien no tiene
assert plataforma.finalizar_viaje("1001") == False
assert plataforma.finalizar_viaje("9999") == False

# Sin conductores disponibles no hay viaje
cj.ocupar()
assert plataforma.solicitar_viaje("1001", 0.0, 0.0) == None

print("Pruebas de plataforma: todas pasaron")
