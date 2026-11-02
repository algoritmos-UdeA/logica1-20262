# -*- coding: utf-8 -*-
"""
Programa principal: notas mayores que el promedio.

Ejecutar con: python main.py
"""

import notas


def main():
    print("Notas mayores que el promedio")
    n = int(input("Cantidad de estudiantes: "))
    # leer_notas y calcular_promedio suponen n > 0: se valida antes de llamarlas
    while n <= 0:
        print("ERROR: la cantidad debe ser mayor que 0")
        n = int(input("Cantidad de estudiantes: "))

    lista_notas = notas.leer_notas(n)
    promedio = notas.calcular_promedio(lista_notas)
    posiciones = notas.posiciones_mayores_que(lista_notas, promedio)
    notas.mostrar_resultados(promedio, posiciones)


if __name__ == "__main__":
    main()
