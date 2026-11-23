"""
Clase 15 - Pruebas de funciones_archivos.py.

Para probar una funcion que lee, la prueba ESCRIBE primero un archivo
pequeno con datos conocidos. Para probar una que escribe, se escribe y
despues se lee otra vez (prueba de ida y vuelta).
Las pruebas dejan el archivo prueba_curso.csv en la carpeta.
"""

import funciones_archivos as fa

PRUEBA = "prueba_curso.csv"

# 1. Leer: se prepara un archivo con datos conocidos
archivo = open(PRUEBA, "w")
archivo.write("nombre,parcial1,parcial2,parcial3\n")
archivo.write("Lisa,5.0,4.5,5.0\n")
archivo.write("Bart,2.0,3.0,1.5\n")
archivo.close()

assert fa.leer_nombres(PRUEBA) == ["Lisa", "Bart"]                      # tipico
assert fa.leer_notas(PRUEBA) == [[5.0, 4.5, 5.0], [2.0, 3.0, 1.5]]      # tipico

archivo = open(PRUEBA, "w")
archivo.write("nombre,parcial1,parcial2,parcial3\n")                     # solo el encabezado
archivo.close()
assert fa.leer_nombres(PRUEBA) == []                                    # limite: sin estudiantes
assert fa.leer_notas(PRUEBA) == []

# 2. Escribir y volver a leer (ida y vuelta)
nombres = ["Ana", "Beto"]
notas = [[3.0, 3.5, 2.5], [4.5, 4.0, 5.0]]
fa.guardar_curso(PRUEBA, nombres, notas)
assert fa.leer_nombres(PRUEBA) == nombres
assert fa.leer_notas(PRUEBA) == notas

archivo = open(PRUEBA, "r")
assert archivo.readline() == "nombre,parcial1,parcial2,parcial3\n"     # el formato exacto
assert archivo.readline() == "Ana,3.0,3.5,2.5\n"
archivo.close()

# 3. guardar_curso reemplaza: el archivo no acumula datos viejos
fa.guardar_curso(PRUEBA, ["Carla"], [[2.0, 3.0, 3.5]])
assert fa.leer_nombres(PRUEBA) == ["Carla"]

print("Pruebas de funciones_archivos: todas pasaron")
