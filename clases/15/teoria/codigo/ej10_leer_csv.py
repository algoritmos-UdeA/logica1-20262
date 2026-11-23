"""
Clase 15 - Leer un archivo CSV a listas.

notas.csv tiene un encabezado y una linea por estudiante. Como no se sabe
de antemano cuantas lineas hay, las listas empiezan vacias y crecen con
append(): un metodo de la lista, que agrega un elemento al final.
"""

nombres = []
notas = []                  # una fila por estudiante

archivo = open("notas.csv", "r")
archivo.readline()          # se salta el encabezado
for linea in archivo:
    partes = linea.strip().split(",")
    nombres.append(partes[0])
    fila = []
    for j in range(1, len(partes)):
        fila.append(float(partes[j]))
    notas.append(fila)
archivo.close()

print(nombres)
print(notas)
print(len(notas), "estudiantes,", len(notas[0]), "parciales")
