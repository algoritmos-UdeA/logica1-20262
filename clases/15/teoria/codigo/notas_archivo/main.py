"""
Clase 15 - Notas finales de un curso, leidas de un archivo: programa
principal.

Lee notas.csv, calcula la nota final de cada estudiante con los pesos de
los parciales, muestra el resultado y lo guarda en notas_finales.csv.
Ya no hay que escribir las notas cada vez: estan en el archivo.
"""

import notas

ENTRADA = "notas.csv"
SALIDA = "notas_finales.csv"
PESOS = [0.3, 0.3, 0.4]      # un peso por parcial; suman 1.0


def main():
    nombres = notas.leer_nombres(ENTRADA)
    matriz = notas.leer_notas(ENTRADA)
    finales = notas.calcular_notas_finales(matriz, PESOS)

    print(f"Notas leidas de {ENTRADA}: {len(nombres)} estudiantes")
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {finales[i]:.2f}")
    print(f"Nota final mas alta: {notas.buscar_mayor(finales):.2f}")
    print(f"Nota final mas baja: {notas.buscar_menor(finales):.2f}")

    notas.guardar_finales(SALIDA, nombres, finales)
    print(f"Resultado guardado en {SALIDA}")


if __name__ == "__main__":
    main()
