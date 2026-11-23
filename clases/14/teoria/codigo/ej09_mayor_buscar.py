"""
Clase 14 - El mayor y su posicion; buscar un valor.

Para el mayor se guardan tres cosas: el valor y su posicion (fila y
columna). La posicion dice de quien es la nota y en que parcial.
Para buscar, la fila y la columna empiezan en -1: si siguen en -1 al
final, el valor no esta.
"""

nombres = ["Ana", "Beto", "Carla", "Dario"]
notas = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]
N = 4
M = 3

# El mayor: se empieza con la primera casilla
mayor = notas[0][0]
fila_mayor = 0
columna_mayor = 0
for i in range(N):
    for j in range(M):
        if notas[i][j] > mayor:
            mayor = notas[i][j]
            fila_mayor = i
            columna_mayor = j
print(f"Mejor nota: {mayor}, de {nombres[fila_mayor]}, "
      f"en el parcial {columna_mayor + 1}")

# Buscar un valor: la primera vez que aparece, recorriendo por filas
buscado = 2.0
fila = -1
columna = -1
for i in range(N):
    for j in range(M):
        if notas[i][j] == buscado and fila == -1:
            fila = i
            columna = j
if fila == -1:
    print(buscado, "no esta")
else:
    print(f"{buscado} esta en la fila {fila}, columna {columna}")
