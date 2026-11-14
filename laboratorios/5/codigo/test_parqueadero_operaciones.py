"""
Punto de chequeo 5: pruebas de la segunda parte de la clase Parqueadero
(buscar, ingresar y retirar).
Se ejecutan con: python test_parqueadero_operaciones.py

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.

Prueba: buscar_puesto_libre, buscar_vehiculo, ingresar_vehiculo y
retirar_vehiculo.
"""
from vehiculo import Vehiculo
from parqueadero import Parqueadero

parqueadero = Parqueadero(2, 3)
carro = Vehiculo("ABC123", Vehiculo.CARRO)
moto = Vehiculo("XYZ78A", Vehiculo.MOTO)

# buscar_puesto_libre: en un parqueadero vacío es el piso 1, puesto 1
assert parqueadero.buscar_puesto_libre() is parqueadero.get_puesto(1, 1)

# buscar_vehiculo: en un parqueadero vacío no hay nadie
assert parqueadero.buscar_vehiculo("ABC123") == None

# ingresar_vehiculo: el caso calculado a mano. El carro queda en piso 1, puesto 1
puesto = parqueadero.ingresar_vehiculo(carro)
assert puesto is parqueadero.get_puesto(1, 1)
assert puesto.get_vehiculo() is carro
assert parqueadero.contar_libres() == 5

# El siguiente vehículo queda en el siguiente puesto libre: piso 1, puesto 2
puesto = parqueadero.ingresar_vehiculo(moto)
assert puesto is parqueadero.get_puesto(1, 2)
assert parqueadero.buscar_puesto_libre() is parqueadero.get_puesto(1, 3)

# buscar_vehiculo: retorna el puesto donde está, o None
assert parqueadero.buscar_vehiculo("ABC123") is parqueadero.get_puesto(1, 1)
assert parqueadero.buscar_vehiculo("XYZ78A") is parqueadero.get_puesto(1, 2)
assert parqueadero.buscar_vehiculo("NOESTA") == None

# No pueden entrar dos vehículos con la misma placa
repetido = Vehiculo("ABC123", Vehiculo.MOTO)
assert parqueadero.ingresar_vehiculo(repetido) == None
assert parqueadero.contar_libres() == 4

# Cuando se llena el piso 1, se sigue con el piso 2
parqueadero.ingresar_vehiculo(Vehiculo("DEF456", Vehiculo.CARRO))      # piso 1, puesto 3
puesto = parqueadero.ingresar_vehiculo(Vehiculo("GHI789", Vehiculo.CARRO))
assert puesto is parqueadero.get_puesto(2, 1)

# retirar_vehiculo: el caso calculado a mano. 130 minutos de carro son $9000
recibo = parqueadero.retirar_vehiculo("ABC123", 130)
assert recibo != None
assert recibo.get_vehiculo() is carro
assert recibo.get_minutos() == 130
assert recibo.calcular_valor() == 9000
assert parqueadero.get_recaudo() == 9000
assert parqueadero.get_puesto(1, 1).esta_libre() == True
assert parqueadero.buscar_vehiculo("ABC123") == None

# El puesto que quedó libre es otra vez el primero libre, aunque haya otros después
assert parqueadero.buscar_puesto_libre() is parqueadero.get_puesto(1, 1)
puesto = parqueadero.ingresar_vehiculo(Vehiculo("JKL012", Vehiculo.MOTO))
assert puesto is parqueadero.get_puesto(1, 1)

# Retirar una placa que no está: no cambia nada
libres = parqueadero.contar_libres()
assert parqueadero.retirar_vehiculo("NOESTA", 60) == None
assert parqueadero.get_recaudo() == 9000
assert parqueadero.contar_libres() == libres

# El recaudo se acumula: la moto estuvo 45 minutos y paga $1000
recibo = parqueadero.retirar_vehiculo("XYZ78A", 45)
assert recibo.calcular_valor() == 1000
assert parqueadero.get_recaudo() == 10000

# Un vehículo que ya salió puede volver a entrar
assert parqueadero.ingresar_vehiculo(carro) is parqueadero.get_puesto(1, 2)

# Parqueadero lleno: no hay puesto libre y no se puede ingresar
lleno = Parqueadero(1, 2)
lleno.ingresar_vehiculo(Vehiculo("AAA111", Vehiculo.CARRO))
lleno.ingresar_vehiculo(Vehiculo("BBB222", Vehiculo.CARRO))
assert lleno.contar_libres() == 0
assert lleno.buscar_puesto_libre() == None
assert lleno.ingresar_vehiculo(Vehiculo("CCC333", Vehiculo.CARRO)) == None
assert lleno.buscar_vehiculo("CCC333") == None

print("Punto de chequeo 5 superado: la clase Parqueadero está completa")
print("Ahora ejecute: python main.py")
