"""
Clase 15 - El archivo no existe (error a proposito).

En modo "r", si el archivo no esta en la carpeta desde la que se ejecuta
el programa, Python se detiene con FileNotFoundError. Revise el nombre
(con su extension) y la carpeta de trabajo.
"""

archivo = open("notas.cvs", "r")      # ERROR: la extension es .csv, no .cvs
print(archivo.read())
archivo.close()
