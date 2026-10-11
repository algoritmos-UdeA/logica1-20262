# -*- coding: utf-8 -*-
"""
Conversion de temperatura con menu (diseno top-down, paso 2).

celsius_a_fahrenheit ya esta implementada y probada.
celsius_a_kelvin sigue siendo provisional (stub).
"""

############ Funciones ############
def mostrar_menu():
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a °K")
    print("3. Salir")

def celsius_a_fahrenheit(temp_c):
    temp_f = (9/5)*temp_c + 32
    return temp_f

def celsius_a_kelvin(temp_c):
    return 0.0  # PENDIENTE: implementar

############ Pruebas ##############
assert round(celsius_a_fahrenheit(100), 2) == 212.0
assert round(celsius_a_fahrenheit(0), 2) == 32.0
# assert round(celsius_a_kelvin(25), 2) == 298.15   # falla mientras sea stub

############ Programa principal #########
print("Programa de conversion de °C a °F y K")
while True:
    mostrar_menu()
    opcion = int(input("\nElija una opcion: "))
    if opcion == 1:
        temp_c = float(input("Digite la temperatura en °C: "))
        temp_f = celsius_a_fahrenheit(temp_c)
        print(f"{temp_c}°C = {temp_f:.2f}°F\n")
    elif opcion == 2:
        temp_c = float(input("Digite la temperatura en °C: "))
        temp_k = celsius_a_kelvin(temp_c)
        print(f"{temp_c}°C = {temp_k:.2f}°K\n")
    elif opcion == 3:
        print("Gracias por usarnos\n")
        break
    else:
        print("ERROR: Opcion no valida\n")
