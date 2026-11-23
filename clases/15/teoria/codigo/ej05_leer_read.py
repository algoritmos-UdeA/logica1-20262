"""
Clase 15 - Leer con read().

read() retorna TODO el contenido como un solo texto (str).
read(n) retorna los n caracteres siguientes: el archivo recuerda hasta
donde se ha leido.
"""

archivo = open("trabalenguas.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
print(type(contenido))

archivo = open("trabalenguas.txt", "r")
print(archivo.read(5))        # Pedro
print(archivo.read(7))        # " Pablo " (sigue donde quedo)
archivo.close()
