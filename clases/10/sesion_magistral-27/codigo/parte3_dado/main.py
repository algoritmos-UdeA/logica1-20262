# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 3: programa principal del dado.

Lanza el dado las veces que el usuario indique, muestra cada resultado
y cuenta cuantas veces salio el 6.
"""
from dados import lanzar_dado


def main():
    print("Simulador de un dado")
    n = int(input("¿Cuántas veces quiere lanzar el dado? "))
    if n <= 0:
        print("ERROR: el número de lanzamientos debe ser positivo")
    else:
        cantidad_seis = 0
        for i in range(1, n + 1):
            cara = lanzar_dado()
            print(f"Lanzamiento {i}: {cara}")
            if cara == 6:
                cantidad_seis = cantidad_seis + 1
        print(f"El 6 salió {cantidad_seis} de {n} veces")


if __name__ == "__main__":
    main()
