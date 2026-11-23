"""
Clase 15 - Leer con readlines().

readlines() retorna una LISTA con todas las lineas, cada una con su "\n".
"""

archivo = open("trabalenguas.txt", "r")
lineas = archivo.readlines()
archivo.close()

print(lineas)
print(len(lineas), "lineas")
print(lineas[1].strip())
