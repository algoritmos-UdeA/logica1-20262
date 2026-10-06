# ---------- Constante ----------
PI = 3.1416


# ---------- Funciones ----------
def mostrar_menu():
    print("\n--- Áreas de figuras ---")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Salir")


def leer_opcion():
    opcion = input("Opción: ")
    return opcion


def calcular_area_circulo(radio):
    area = PI * radio ** 2
    return area


def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area


def calcular_area_triangulo(base, altura):
    area = base * altura / 2           # PRUEBA: Quitar el 2 de la division para ver qué pasa
    return area


def mostrar_area(figura, area):
    print(f"Área del {figura}: {area:.2f}")


# ---------- Pruebas ----------
assert calcular_area_rectangulo(4, 3) == 12
assert calcular_area_rectangulo(0, 5) == 0
assert calcular_area_triangulo(6, 2) == 6
assert calcular_area_triangulo(0, 5) == 0
assert round(calcular_area_circulo(5), 2) == 78.54
assert calcular_area_circulo(0) == 0


# ---------- Programa principal ----------
opcion = ""
while opcion != "4":
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == "1":
        radio = float(input("Radio: "))
        area = calcular_area_circulo(radio)
        mostrar_area("círculo", area)
    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        area = calcular_area_rectangulo(base, altura)
        mostrar_area("rectángulo", area)
    elif opcion == "3":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        area = calcular_area_triangulo(base, altura)
        mostrar_area("triángulo", area)
    elif opcion != "4":
        print("Opción no válida")