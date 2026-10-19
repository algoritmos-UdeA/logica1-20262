# -*- coding: utf-8 -*-
"""
Clase 11 - Indices en Python (diapositivas 21 a 23).

Una lista se puede recorrer por posicion o por elemento. Python acepta
indices negativos, que cuentan desde el final. Usar una posicion que no
existe produce IndexError.
"""


def main():
    notas = [3.0, 4.5, 2.0, 4.0]

    # Indices positivos y negativos
    print("Tamano:", len(notas))
    print("notas[0]  =", notas[0])
    print("notas[3]  =", notas[3])
    print("notas[-1] =", notas[-1])     # el ultimo elemento
    print("notas[-4] =", notas[-4])     # el primero, contado desde el final

    # Forma 1: recorrer por posicion (se conoce i)
    for i in range(len(notas)):
        print(f"Posicion {i}: {notas[i]}")

    # Forma 2: recorrer por elemento (solo para leer los valores)
    for nota in notas:
        print("Nota:", nota)

    # El error mas comun: las posiciones validas son 0, 1, 2 y 3
    # Quite el # de la siguiente linea y ejecute el programa:
    # print(notas[4])                   # IndexError: list index out of range


if __name__ == "__main__":
    main()
