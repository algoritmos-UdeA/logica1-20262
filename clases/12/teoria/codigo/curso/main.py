"""
Clase 12 - Integrador: menú de administración de notas de un curso.
Se ejecuta con: python main.py
"""
from curso import (buscar_id, agregar_estudiante, eliminar_estudiante,
                   actualizar_nota, mostrar_listado, ordenar_por_nota,
                   ordenar_por_nombre)

N = 10      # cupo máximo del curso


def mostrar_menu():
    """Garantiza: imprime las opciones del menú. No retorna nada."""
    print()
    print("=== Administración del curso ===")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Actualizar nota")
    print("4. Buscar estudiante")
    print("5. Listar curso")
    print("6. Ordenar por nota")
    print("7. Ordenar por nombre")
    print("0. Salir")


def main():
    ids = [""] * N
    nombres = [""] * N
    notas = [0.0] * N
    cantidad = 0

    # Estudiantes ya inscritos
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "000", "Ana", 3.0)
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "123", "Beto", 4.5)
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "987", "Carla", 2.0)
    cantidad = agregar_estudiante(ids, nombres, notas, cantidad, "007", "Dario", 4.0)

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            id_nuevo = input("Id: ")
            nombre = input("Nombre: ")
            nota = float(input("Nota: "))
            antes = cantidad
            cantidad = agregar_estudiante(ids, nombres, notas, cantidad, id_nuevo, nombre, nota)
            if cantidad == antes:
                print("No se pudo agregar: el curso está lleno o el Id ya existe.")
            else:
                print("Estudiante agregado.")

        elif opcion == "2":
            id_buscado = input("Id a eliminar: ")
            antes = cantidad
            cantidad = eliminar_estudiante(ids, nombres, notas, cantidad, id_buscado)
            if cantidad == antes:
                print("No existe un estudiante con ese Id.")
            else:
                print("Estudiante eliminado.")

        elif opcion == "3":
            id_buscado = input("Id: ")
            nota = float(input("Nueva nota: "))
            if actualizar_nota(ids, notas, cantidad, id_buscado, nota):
                print("Nota actualizada.")
            else:
                print("No existe un estudiante con ese Id.")

        elif opcion == "4":
            id_buscado = input("Id a buscar: ")
            pos = buscar_id(ids, cantidad, id_buscado)
            if pos == -1:
                print("No existe un estudiante con ese Id.")
            else:
                print(ids[pos], nombres[pos], notas[pos])

        elif opcion == "5":
            mostrar_listado(ids, nombres, notas, cantidad)

        elif opcion == "6":
            ordenar_por_nota(ids, nombres, notas, cantidad)
            mostrar_listado(ids, nombres, notas, cantidad)

        elif opcion == "7":
            ordenar_por_nombre(ids, nombres, notas, cantidad)
            mostrar_listado(ids, nombres, notas, cantidad)

        elif opcion != "0":
            print("Opción no válida.")

    print("Hasta luego.")


if __name__ == "__main__":
    main()
