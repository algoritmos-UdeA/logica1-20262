"""
Clase 14 - Sala de cine: programa principal con menu.

La sala tiene 5 filas (A a E) de 6 sillas y la boleta vale $5000.
"""

from sala import Sala


def main():
    sala = Sala(5, 6, 5000)
    opcion = -1
    while opcion != 0:
        print()
        print("=== Sala de cine ===")
        print("1. Ver el mapa")
        print("2. Vender una boleta")
        print("3. Liberar una silla")
        print("4. Resumen")
        print("0. Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            print(sala)
            print("O: libre   X: ocupada")
        elif opcion == 2 or opcion == 3:
            letra = input("Fila (letra): ")
            numero = int(input("Numero de silla: "))
            if opcion == 2:
                hecho = sala.vender(letra, numero)
            else:
                hecho = sala.liberar(letra, numero)
            if hecho:
                print("Listo")
            else:
                print("No se pudo: la silla no existe o no esta en ese estado")
        elif opcion == 4:
            for i in range(sala.get_filas()):
                letra = Sala.LETRAS[i]
                print(f"Fila {letra}: {sala.contar_libres_fila(letra)} libres")
            print("Libres en total:", sala.contar_libres())
            print("Recaudo: $", sala.get_recaudo())
        elif opcion != 0:
            print("Opcion no valida")


if __name__ == "__main__":
    main()
