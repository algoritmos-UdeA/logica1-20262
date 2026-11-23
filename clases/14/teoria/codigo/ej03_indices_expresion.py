"""
Clase 14 - El indice puede ser una expresion.

Ejercicio: como queda la matriz B despues de estas instrucciones?
Primero resuelvalo a mano; despues ejecute el programa para comprobar.
"""

A = [[2, 5, -1],
     [0, 7, 1],
     [3, -2, 4]]
B = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]

B[0][0] = A[1][1] * 2
B[1][2] = B[1][2] + A[2][0]
B[A[1][2]][A[0][2] + 1] = A[0][1] - B[2][2]
B[2][A[2][0] - 1] = B[A[1][0]][A[1][0]] + A[2][1]

for i in range(3):
    print(B[i])
