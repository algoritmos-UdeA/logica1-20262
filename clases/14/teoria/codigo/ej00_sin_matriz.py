"""
Clase 14 - Posible solucion sin matriz: un arreglo por parcial.

Funciona con 3 parciales, pero cada parcial es un arreglo con nombre
distinto: no se pueden recorrer los parciales con un ciclo. Con 10
parciales serian 10 arreglos y 10 terminos en cada suma.
"""

nombres = ["Ana", "Beto", "Carla", "Dario"]
notas1 = [3.0, 4.5, 2.0, 4.0]   # parcial 1
notas2 = [3.5, 4.0, 3.0, 4.5]   # parcial 2
notas3 = [2.5, 5.0, 3.5, 3.0]   # parcial 3
N = 4

for i in range(N):
    promedio = (notas1[i] + notas2[i] + notas3[i]) / 3
    print(f"{nombres[i]}: {promedio:.2f}")

# Y el promedio de cada parcial? Un ciclo por arreglo:
suma1 = 0.0
for i in range(N):
    suma1 = suma1 + notas1[i]
print(f"Parcial 1: {suma1 / N:.2f}")
# ... y lo mismo otra vez para notas2 y para notas3
