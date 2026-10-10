# -*- coding: utf-8 -*-
"""
Conversion de temperatura con menu: °C a °F y °C a K.
"""

############ Funciones ############
# Despliegue
def mostrar_menu():
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a K")
    print("3. Salir")

# Conversion de temperatura
def celsius_a_fahrenheit(temp_c):
    temp_f = (9/5)*temp_c + 32
    return temp_f

def celsius_a_kelvin(temp_c):
    temp_k = temp_c + 273.15
    return temp_k

############ Pruebas ##############
# celsius_a_fahrenheit
assert round(celsius_a_fahrenheit(100), 2) == 212.0    # tipico: ebullicion
assert round(celsius_a_fahrenheit(0), 2) == 32.0       # tipico: congelacion
assert round(celsius_a_fahrenheit(37), 2) == 98.6      # tipico: temperatura corporal
assert round(celsius_a_fahrenheit(-40), 2) == -40.0    # especial: las escalas coinciden
# celsius_a_kelvin
assert round(celsius_a_kelvin(25), 2) == 298.15        # tipico
assert round(celsius_a_kelvin(-273.15), 2) == 0.0      # limite: cero absoluto

############ Programa principal #########
print("Programa de conversion de °C a °F y K")
while True:
    # Menu
    mostrar_menu()
    # Entrada de datos
    opcion = int(input("\nElija una opcion: "))
    # Seleccion
    if opcion == 1:
        # C --> F
        temp_c = float(input("Digite la temperatura en °C: "))
        temp_f = celsius_a_fahrenheit(temp_c)
        print(f"{temp_c}°C = {temp_f:.2f}°F\n")
    elif opcion == 2:
        # C --> K
        temp_c = float(input("Digite la temperatura en °C: "))
        temp_k = celsius_a_kelvin(temp_c)
        print(f"{temp_c}°C = {temp_k:.2f}K\n")
    elif opcion == 3:
        print("Gracias por usarnos\n")
        break
    else:
        print("ERROR: Opcion no valida\n")
