"""
Punto de chequeo 4 (segunda parte): pruebas de pantalla.py.
Se ejecutan con: python test_pantalla.py

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.

pantalla.py ya viene hecho, pero usa las clases Vehiculo, Puesto, Recibo
y la primera parte de Parqueadero. Estas pruebas solo pasan cuando esas
clases están completas: confirman que el parqueadero ya se puede ver.
"""
from vehiculo import Vehiculo
from puesto import Puesto
from recibo import Recibo
from parqueadero import Parqueadero
from pantalla import (texto_puesto, texto_encabezado, texto_piso, texto_mapa,
                      texto_vehiculos, texto_recibo, mostrar_mapa,
                      mostrar_vehiculos, mostrar_recibo)

# texto_puesto: libre, con carro y con moto
puesto = Puesto(1, 1)
assert texto_puesto(puesto) == "[   ]"
puesto.ocupar(Vehiculo("ABC123", Vehiculo.CARRO))
assert texto_puesto(puesto) == "[ C ]"
puesto.liberar()
puesto.ocupar(Vehiculo("XYZ78A", Vehiculo.MOTO))
assert texto_puesto(puesto) == "[ M ]"

# texto_encabezado: los números quedan alineados con los corchetes
assert texto_encabezado(1) == "         1"
assert texto_encabezado(3) == "         1     2     3"

# Un parqueadero vacío de 2 pisos y 5 puestos por piso
parqueadero = Parqueadero(2, 5)
assert texto_piso(parqueadero, 1) == "Piso 1 [   ] [   ] [   ] [   ] [   ]"
assert texto_vehiculos(parqueadero) == "(no hay vehículos)"
assert texto_mapa(parqueadero) == (
    "         1     2     3     4     5\n"
    "Piso 2 [   ] [   ] [   ] [   ] [   ]\n"
    "Piso 1 [   ] [   ] [   ] [   ] [   ]\n"
    "\n"
    "C: carro   M: moto   [   ]: libre\n"
    "Libres: 10 de 10")

# El mismo parqueadero con cinco vehículos
parqueadero.get_puesto(1, 1).ocupar(Vehiculo("ABC123", Vehiculo.CARRO))
parqueadero.get_puesto(1, 2).ocupar(Vehiculo("DEF456", Vehiculo.CARRO))
parqueadero.get_puesto(1, 4).ocupar(Vehiculo("XYZ78A", Vehiculo.MOTO))
parqueadero.get_puesto(2, 2).ocupar(Vehiculo("QWE12B", Vehiculo.MOTO))
parqueadero.get_puesto(2, 5).ocupar(Vehiculo("GHI789", Vehiculo.CARRO))

assert texto_piso(parqueadero, 1) == "Piso 1 [ C ] [ C ] [   ] [ M ] [   ]"
assert texto_piso(parqueadero, 2) == "Piso 2 [   ] [ M ] [   ] [   ] [ C ]"
assert texto_mapa(parqueadero) == (
    "         1     2     3     4     5\n"
    "Piso 2 [   ] [ M ] [   ] [   ] [ C ]\n"
    "Piso 1 [ C ] [ C ] [   ] [ M ] [   ]\n"
    "\n"
    "C: carro   M: moto   [   ]: libre\n"
    "Libres: 5 de 10")
assert texto_vehiculos(parqueadero) == (
    "ABC123  carro  piso 1, puesto 1\n"
    "DEF456  carro  piso 1, puesto 2\n"
    "XYZ78A  moto  piso 1, puesto 4\n"
    "QWE12B  moto  piso 2, puesto 2\n"
    "GHI789  carro  piso 2, puesto 5")

# Al liberar un puesto, el mapa cambia
parqueadero.get_puesto(1, 2).liberar()
assert texto_piso(parqueadero, 1) == "Piso 1 [ C ] [   ] [   ] [ M ] [   ]"

# texto_recibo
recibo = Recibo(Vehiculo("ABC123", Vehiculo.CARRO), 130)
assert texto_recibo(recibo) == (
    "--- Recibo ---\n"
    "Vehículo: ABC123 (carro)\n"
    "Tiempo: 130 minutos\n"
    "Horas cobradas: 3\n"
    "Valor: $9000")

print("Punto de chequeo 4 superado: el parqueadero ya se puede ver en pantalla")
print()
mostrar_mapa(parqueadero)
print()
mostrar_vehiculos(parqueadero)
print()
mostrar_recibo(recibo)
