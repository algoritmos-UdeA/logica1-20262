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
    area = base * altura / 2
    return area


def mostrar_area(figura, area):
    print(f"Área del {figura}: {area:.2f}")
