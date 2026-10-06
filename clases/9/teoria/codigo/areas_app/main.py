from funciones import *

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

