"""
Clase 15 - with: el archivo se cierra solo.

Todo lo que va indentado dentro del with trabaja con el archivo abierto.
Al salir del bloque, Python lo cierra, aunque se olvide escribir close().
"""

with open("trabalenguas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
    print("Dentro del with, cerrado?", archivo.closed)

print("Fuera del with, cerrado?", archivo.closed)
