# -*- coding: utf-8 -*-
"""
Clase 11 - Operaciones basicas: llenar, recorrer y acumular.

Traduccion a Python del pseudocodigo de las diapositivas 14 a 16:
    notas = Arreglo(N)          ->  notas = [0.0] * N
    Para (i = 0, N - 1, 1) Haga ->  for i in range(N):
"""

N = 4


def main():
    # Crear el arreglo con N casillas
    notas = [0.0] * N

    # Llenar: un ciclo visita las posiciones 0, 1, ..., N - 1
    for i in range(N):
        notas[i] = float(input(f"Nota del estudiante {i + 1}: "))

    # Recorrer y mostrar
    for i in range(N):
        print(f"Posicion {i}: {notas[i]}")

    # Recorrer y acumular
    suma = 0
    for i in range(N):
        suma = suma + notas[i]
    promedio = suma / N
    print(f"Promedio: {promedio:.2f}")


if __name__ == "__main__":
    main()
