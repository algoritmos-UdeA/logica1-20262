"""
Punto de chequeo 4: pruebas de la primera parte de la clase Parqueadero
(la matriz de puestos y las consultas).
Se ejecutan con: python test_parqueadero_matriz.py

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.

Prueba: __init__, get_pisos, get_puestos_por_piso, get_recaudo,
get_puesto y contar_libres.
"""
from vehiculo import Vehiculo
from parqueadero import Parqueadero

# Un parqueadero de 2 pisos y 5 puestos por piso
parqueadero = Parqueadero(2, 5)
assert parqueadero.get_pisos() == 2
assert parqueadero.get_puestos_por_piso() == 5
assert parqueadero.get_recaudo() == 0
assert parqueadero.contar_libres() == 10

# get_puesto usa los números del usuario, que empiezan en 1.
# Cada puesto sabe en qué piso está y qué número tiene.
primero = parqueadero.get_puesto(1, 1)
assert primero.get_piso() == 1 and primero.get_numero() == 1
ultimo = parqueadero.get_puesto(2, 5)
assert ultimo.get_piso() == 2 and ultimo.get_numero() == 5
medio = parqueadero.get_puesto(1, 4)
assert medio.get_piso() == 1 and medio.get_numero() == 4

# Todos los puestos empiezan libres, y son 10 objetos distintos
for piso in range(1, 3):
    for numero in range(1, 6):
        puesto = parqueadero.get_puesto(piso, numero)
        assert puesto.esta_libre() == True
        assert puesto.get_piso() == piso
        assert puesto.get_numero() == numero
assert parqueadero.get_puesto(1, 1) is not parqueadero.get_puesto(1, 2)
assert parqueadero.get_puesto(1, 1) is not parqueadero.get_puesto(2, 1)

# get_puesto entrega siempre el mismo objeto, no una copia
assert parqueadero.get_puesto(1, 1) is primero

# contar_libres cambia cuando se ocupa o se libera un puesto
primero.ocupar(Vehiculo("ABC123", Vehiculo.CARRO))
assert parqueadero.contar_libres() == 9
ultimo.ocupar(Vehiculo("XYZ78A", Vehiculo.MOTO))
assert parqueadero.contar_libres() == 8
primero.liberar()
assert parqueadero.contar_libres() == 9

# Caso límite: un parqueadero de un solo puesto
pequeno = Parqueadero(1, 1)
assert pequeno.contar_libres() == 1
assert pequeno.get_puesto(1, 1).get_numero() == 1

# Caso especial: más pisos que puestos por piso (para no confundir filas y columnas)
torre = Parqueadero(4, 2)
assert torre.contar_libres() == 8
assert torre.get_puesto(4, 2).get_piso() == 4
assert torre.get_puesto(4, 2).get_numero() == 2

print("Punto de chequeo 4 superado: la matriz y las consultas de Parqueadero pasan sus pruebas")
print("Ahora ejecute: python test_pantalla.py")
