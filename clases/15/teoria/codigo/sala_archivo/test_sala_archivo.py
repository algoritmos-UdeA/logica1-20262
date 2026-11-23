"""
Clase 15 - Pruebas de guardar, cargar y cargar_sala.

La prueba principal es de IDA Y VUELTA: se guarda una sala, se carga en
otra y las dos deben quedar iguales. Las pruebas dejan el archivo
prueba_sala.txt en la carpeta.
"""

from sala import Sala, cargar_sala

PRUEBA = "prueba_sala.txt"

sala = Sala(3, 4, 5000)
sala.vender("A", 1)
sala.vender("C", 4)

# guardar: el archivo queda con el formato acordado
sala.guardar(PRUEBA)
archivo = open(PRUEBA, "r")
assert archivo.readline() == "3,4,5000\n"
assert archivo.readline() == "XOOO\n"
assert archivo.readline() == "OOOO\n"
assert archivo.readline() == "OOOX\n"
assert archivo.readline() == ""
archivo.close()

# cargar_sala: ida y vuelta
otra = cargar_sala(PRUEBA)
assert str(otra) == str(sala)
assert otra.get_recaudo() == 10000
assert otra.contar_libres() == 10
assert not otra.get_silla("C", 4).esta_libre()

# cargar sobre una sala con otras ventas: queda como dice el archivo
tercera = Sala(3, 4, 5000)
tercera.vender("B", 2)                # esta venta no esta en el archivo
tercera.cargar(PRUEBA)
assert tercera.get_silla("B", 2).esta_libre()
assert str(tercera) == str(sala)
assert tercera.get_recaudo() == 10000

# guardar no modifica la sala
assert sala.contar_libres() == 10

print("Pruebas de la sala con archivo: todas pasaron")
