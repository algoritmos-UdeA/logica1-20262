# -*- coding: utf-8 -*-
"""
Conversion de temperatura con menu (diseno top-down, paso 1).

El programa principal ya esta completo. Las funciones de conversion
son provisionales (stubs): devuelven 0.0 hasta que se implementen.
"""

############ Funciones ############
def mostrar_menu():
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a K")
    print("3. Salir")

def celsius_a_fahrenheit(temp_c):
    return 0.0  # PENDIENTE: implementar

def celsius_a_kelvin(temp_c):
    return 0.0  # PENDIENTE: implementar

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
        print(f"{temp_c}°C = {temp_k:.2f}K\n")
    elif opcion == 3:
        print("Gracias por usarnos\n")
        break
    else:
        print("ERROR: Opcion no valida\n")
