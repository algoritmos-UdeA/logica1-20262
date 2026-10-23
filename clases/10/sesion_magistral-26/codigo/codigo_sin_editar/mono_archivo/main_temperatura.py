# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:55:28 2026

@author: Soportedrai
"""
######

ZERO_ABSOLUTO = -273.15 # °C

############ Funciones ############
# Despliegue
def mostrar_menu():
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a °K")
    print("3. Salir")

# Conversion de temperatura
def celsius_a_fahrenheit(c):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Supone:
        temp_c es un número (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en grados Fahrenheit (float).
    """

    f = (9/5)*c + 32
    return f

def celsius_a_kelvin(c):
    """
    Convierte una temperatura de grados Celsius a Kelvin.

    Supone:
        temp_c es un número (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en Kelvin (float),
        mayor o igual a 0.
    """
    k = c + 273.15
    return k


############ Test ################

# assert condición [, "Mensaje opcional"]

# celsius_a_fahrenheit
assert celsius_a_fahrenheit(5) == 41
assert round(celsius_a_fahrenheit(1),1) == 33.8 ,"El resultado es 33.8"
assert round(celsius_a_fahrenheit(1.5),1) == 34.7 ,"El resultado es 34.7"
assert round(celsius_a_fahrenheit(100),2) == 212.00
assert round(celsius_a_fahrenheit(0),2) == 32.00
assert round(celsius_a_fahrenheit(37),2) == 98.60
assert round(celsius_a_fahrenheit(-40),2) == -40.00

# celsius_a_kelvin
assert round(celsius_a_kelvin(10),2) == 283.15 ,"El resultado es 283.15"
assert round(celsius_a_kelvin(-20),2) == 253.15 ,"El resultado es 253.15"


############ Programa principal #########
print("Programa de conversion de °C a °F y °K")
while True:
    # Menu
    mostrar_menu()
    # Entrada de datos
    opc = int(input("\nElija una opcion: "))
    # Seleccion
    if opc == 1:
        # C --> F
        temp_c = float(input("Digite la temperatura en °C: "))
        if temp_c < ZERO_ABSOLUTO:
            print("ERROR: Temperatura invalida")
            continue
        temp_f = celsius_a_fahrenheit(temp_c)

        print(f"{temp_c}°C = {temp_f:.2f}°F\n")
    elif opc == 2:
        # C --> K
        temp_c = float(input("Digite la temperatura en °C: "))
        if temp_c < ZERO_ABSOLUTO:
            print("ERROR: Temperatura invalida")
            continue
        temp_k = celsius_a_kelvin(temp_c)
        print(f"{temp_c}°C = {temp_k:.2f}°K\n")
    elif opc == 3:
        print("Gracias por usarnos\n")
        break
    else:
        print("ERROR: Opcion no valida\n")