"""
Clase 14 - Asignar una matriz no la copia; copiar solo la lista de
filas tampoco.

copia = notas            -> alias: el mismo objeto.
copia = list(notas)      -> lista externa nueva, pero las FILAS son las
                            mismas (copia superficial).
Clonar con dos ciclos    -> filas nuevas: la original no cambia.
"""

notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0]]
N = 2
M = 3

alias = notas
alias[0][0] = 5.0
print("Con alias:", notas)            # notas cambio

notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0]]
superficial = list(notas)             # igual con notas[:]
superficial[0][0] = 5.0
print("Con list():", notas)           # notas TAMBIEN cambio

notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0]]
clon = [0.0] * N
for i in range(N):
    clon[i] = [0.0] * M
for i in range(N):
    for j in range(M):
        clon[i][j] = notas[i][j]
clon[0][0] = 5.0
print("Con clon:", notas)             # notas no cambio
print("El clon: ", clon)
