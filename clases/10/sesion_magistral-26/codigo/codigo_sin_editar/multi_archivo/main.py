# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:12:21 2026

@author: Soportedrai
"""
# from conversion import *
from conversion import celsius_a_fahrenheit, celsius_a_kelvin
# from pantalla import *
from pantalla import mostrar_menu

ZERO_ABSOLUTO = -273.15 # °C

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