"""
Clase 15 - Escribir un archivo CSV.

Primero el encabezado; despues una linea por fila de la matriz, con los
valores separados por comas y un "\n" al final.
"""

nombres = ["Ana", "Beto", "Carla", "Dario"]
notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]

archivo = open("notas_copia.csv", "w")
archivo.write("nombre,parcial1,parcial2,parcial3\n")
for i in range(len(nombres)):
    archivo.write(f"{nombres[i]},{notas[i][0]},{notas[i][1]},{notas[i][2]}\n")
archivo.close()

archivo = open("notas_copia.csv", "r")
print(archivo.read(), end="")
archivo.close()
