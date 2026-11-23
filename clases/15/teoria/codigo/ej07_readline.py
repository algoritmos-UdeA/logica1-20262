"""
Clase 15 - Leer con readline().

readline() lee UNA linea. Al llegar al final del archivo retorna "" (texto
vacio): esa es la condicion para terminar el while. Sirve cuando se quiere
tratar distinto una parte del archivo, por ejemplo el encabezado.
"""

archivo = open("notas.csv", "r")
encabezado = archivo.readline()       # la primera linea
print("Encabezado:", encabezado.strip())

linea = archivo.readline()
while linea != "":
    print("Dato:", linea.strip())
    linea = archivo.readline()
archivo.close()
