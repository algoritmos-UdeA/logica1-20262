"""
Clase 15 - Escribir en un archivo.

El modo "w" crea el archivo (si ya existia, lo deja vacio). write(texto)
escribe el texto tal cual: NO agrega el salto de linea; hay que escribir
"\n" para pasar a la linea siguiente.
"""

archivo = open("saludo.txt", "w")
archivo.write("Hola, Ana")
archivo.write("\n")
archivo.write("Hasta pronto\n")
archivo.close()

# Para comprobar, se abre otra vez, ahora para leer
archivo = open("saludo.txt", "r")
print(archivo.read())
archivo.close()
