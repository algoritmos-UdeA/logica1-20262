"""
Clase 14 - Recorrer y mostrar una matriz.

Por filas: el ciclo externo recorre las filas (i) y el interno las
columnas (j). Por columnas: se invierte el orden de los ciclos.
"""

notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
N = 4
M = 3

print("Por filas (como tabla):")
for i in range(N):
    for j in range(M):
        print(notas[i][j], end="  ")
    print()                         # salto de linea al terminar la fila

print("Por columnas (un parcial a la vez):")
for j in range(M):
    print(f"Parcial {j + 1}:", end=" ")
    for i in range(N):
        print(notas[i][j], end="  ")
    print()

print("Por elemento:")
for fila in notas:
    for nota in fila:
        print(nota, end="  ")
    print()
