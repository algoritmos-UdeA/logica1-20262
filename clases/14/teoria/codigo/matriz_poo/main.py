"""
Clase 14 - Programa que usa la clase Matriz.

Guarda las notas del curso en una Matriz, muestra la tabla, el promedio
de cada estudiante y de cada parcial, y la transpuesta.
"""

from matriz import Matriz

NOMBRES = ["Ana", "Beto", "Carla", "Dario"]
DATOS = [[3.0, 3.5, 2.5],
         [4.5, 4.0, 5.0],
         [2.0, 3.0, 3.5],
         [4.0, 4.5, 3.0]]


def main():
    n = len(DATOS)
    m = len(DATOS[0])
    notas = Matriz(n, m)
    for i in range(n):
        for j in range(m):
            notas.set(i, j, DATOS[i][j])

    print("Notas:")
    print(notas)
    for i in range(notas.get_filas()):
        promedio = notas.sumar_fila(i) / notas.get_columnas()
        print(f"{NOMBRES[i]}: {promedio:.2f}")
    for j in range(notas.get_columnas()):
        promedio = notas.sumar_columna(j) / notas.get_filas()
        print(f"Parcial {j + 1}: {promedio:.2f}")

    print("Transpuesta (una fila por parcial):")
    print(notas.transpuesta())


if __name__ == "__main__":
    main()
