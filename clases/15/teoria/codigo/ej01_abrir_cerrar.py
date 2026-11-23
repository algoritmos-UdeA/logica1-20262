"""
Clase 15 - Abrir y cerrar un archivo.

open(nombre, modo) abre el archivo y retorna un OBJETO archivo. Como todo
objeto, tiene atributos (name, mode, closed) y metodos (read, write,
close...). Al terminar, el archivo se cierra con close().
Ejecute este script desde la carpeta codigo/, donde esta trabalenguas.txt.
"""

archivo = open("trabalenguas.txt", "r")
print("Nombre del archivo:", archivo.name)
print("Modo de apertura:  ", archivo.mode)
print("Cerrado?           ", archivo.closed)
archivo.close()
print("Cerrado?           ", archivo.closed)
