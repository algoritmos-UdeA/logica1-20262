"""
Clase 15 - Pruebas de notas.py.

Las pruebas escriben su propio archivo (prueba_notas.csv) con datos
conocidos, y comprueban el archivo que genera guardar_finales.
"""

import notas

PRUEBA = "prueba_notas.csv"
SALIDA = "prueba_finales.csv"

archivo = open(PRUEBA, "w")
archivo.write("nombre,parcial1,parcial2,parcial3\n")
archivo.write("Ana,3.0,3.5,2.5\n")
archivo.write("Beto,4.5,4.0,5.0\n")
archivo.close()

# Leer
assert notas.leer_nombres(PRUEBA) == ["Ana", "Beto"]
assert notas.leer_notas(PRUEBA) == [[3.0, 3.5, 2.5], [4.5, 4.0, 5.0]]

# Calcular (las mismas pruebas de la clase 14)
finales = notas.calcular_notas_finales(notas.leer_notas(PRUEBA), [0.3, 0.3, 0.4])
assert round(finales[0], 2) == 2.95
assert round(finales[1], 2) == 4.55
assert notas.buscar_mayor([2.95, 4.55]) == 4.55
assert notas.buscar_menor([2.95, 4.55]) == 2.95

# Guardar y revisar el archivo generado, linea por linea
notas.guardar_finales(SALIDA, ["Ana", "Beto"], finales)
archivo = open(SALIDA, "r")
assert archivo.readline() == "nombre,final\n"
assert archivo.readline() == "Ana,2.95\n"
assert archivo.readline() == "Beto,4.55\n"
assert archivo.readline() == ""          # no hay mas lineas
archivo.close()

print("Pruebas de notas: todas pasaron")
