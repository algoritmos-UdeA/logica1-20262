"""
Clase 14 - Notas de un curso con una matriz: programa principal.

Lee los nombres y las notas de los parciales, calcula la nota final de
cada estudiante con los pesos de los parciales y muestra quienes
obtuvieron la nota final mas alta y la mas baja.
"""

import notas

PESOS = [0.3, 0.3, 0.4]      # un peso por parcial; suman 1.0


def main():
    print("Notas finales del curso")
    n = int(input("Cantidad de estudiantes: "))
    while n <= 0:
        print("ERROR: la cantidad debe ser mayor que 0")
        n = int(input("Cantidad de estudiantes: "))

    nombres = notas.leer_nombres(n)
    matriz = notas.leer_notas(n, len(PESOS))
    finales = notas.calcular_notas_finales(matriz, PESOS)

    for i in range(n):
        print(f"{nombres[i]}: {finales[i]:.2f}")
    notas.mostrar_estudiantes("Nota final mas alta", nombres, finales,
                              notas.buscar_mayor(finales))
    notas.mostrar_estudiantes("Nota final mas baja", nombres, finales,
                              notas.buscar_menor(finales))


if __name__ == "__main__":
    main()
