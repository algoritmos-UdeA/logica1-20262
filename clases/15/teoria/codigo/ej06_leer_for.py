"""
Clase 15 - Leer linea por linea con for.

for linea in archivo: recorre el archivo de a una linea. Cada linea
termina con "\n", y print agrega otro: por eso aparecen lineas en blanco.
strip() quita los espacios y el "\n" de los extremos.
"""

archivo = open("trabalenguas.txt", "r")
for linea in archivo:
    print(linea)               # deja una linea en blanco entre cada una
archivo.close()

print("-----")
archivo = open("trabalenguas.txt", "r")
for linea in archivo:
    print(linea.strip())       # sin el "\n" del final
archivo.close()
