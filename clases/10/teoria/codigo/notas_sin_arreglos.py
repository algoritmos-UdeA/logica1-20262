"""
Problema motivador para la clase de arreglos.

Se leen las notas de un curso y se calcula el promedio.
Pregunta: ¿cuántas notas son mayores que el promedio?
"""


def main():
    cantidad = int(input("Cantidad de estudiantes: "))
    suma = 0.0
    for i in range(cantidad):
        nota = float(input(f"Nota del estudiante {i + 1}: "))
        suma += nota
    promedio = suma / cantidad
    print(f"Promedio del curso: {promedio:.2f}")
    # ¿Cuántas notas son mayores que el promedio?
    # Problema: la variable nota solo conserva la última nota leída.
    print(f"Nota guardada en la variable nota: {nota}")


if __name__ == "__main__":
    main()
