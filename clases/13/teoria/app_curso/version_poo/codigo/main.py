"""
Administración de notas de un curso (versión POO): el menú.
Se ejecuta con: python main.py
"""
from estudiante import Estudiante
from curso import Curso

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
    curso = Curso(N)

    # Estudiantes ya inscritos
    curso.agregar_estudiante(Estudiante("000", "Ana", 3.0))
    curso.agregar_estudiante(Estudiante("123", "Beto", 4.5))
    curso.agregar_estudiante(Estudiante("987", "Carla", 2.0))
    curso.agregar_estudiante(Estudiante("007", "Dario", 4.0))

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            id_nuevo = input("Id: ")
            nombre = input("Nombre: ")
            nota = float(input("Nota: "))
            if curso.agregar_estudiante(Estudiante(id_nuevo, nombre, nota)):
                print("Estudiante agregado.")
            else:
                print("No se pudo agregar: el curso está lleno o el Id ya existe.")

        elif opcion == "2":
            id_buscado = input("Id a eliminar: ")
            if curso.eliminar_estudiante(id_buscado):
                print("Estudiante eliminado.")
            else:
                print("No existe un estudiante con ese Id.")

        elif opcion == "3":
            id_buscado = input("Id: ")
            nota = float(input("Nueva nota: "))
            if curso.actualizar_nota(id_buscado, nota):
                print("Nota actualizada.")
            else:
                print("No se pudo actualizar: el Id no existe o la nota no está entre 0.0 y 5.0.")

        elif opcion == "4":
            id_buscado = input("Id a buscar: ")
            pos = curso.buscar_id(id_buscado)
            if pos == -1:
                print("No existe un estudiante con ese Id.")
            else:
                print(curso.get_estudiante(pos))

        elif opcion == "5":
            curso.mostrar_listado()

        elif opcion == "6":
            curso.ordenar_por_nota()
            curso.mostrar_listado()

        elif opcion == "7":
            curso.ordenar_por_nombre()
            curso.mostrar_listado()

        elif opcion != "0":
            print("Opción no válida.")

    print("Hasta luego.")


if __name__ == "__main__":
    main()
