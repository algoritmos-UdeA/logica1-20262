# -*- coding: utf-8 -*-
"""
Sesion 26 - Paso 3: programa principal.

Ejecute este archivo para usar el programa. Importa las funciones
de conversion.py y de pantalla.py, que deben estar en la misma carpeta.
"""
from conversion import celsius_a_fahrenheit, celsius_a_kelvin
from pantalla import mostrar_menu

############ Constantes ############
CERO_ABSOLUTO = -273.15  # °C

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
        if temp_c < CERO_ABSOLUTO:
            print("ERROR: Temperatura invalida")
            continue
        temp_f = celsius_a_fahrenheit(temp_c)
        print(f"{temp_c}°C = {temp_f:.2f}°F\n")
    elif opc == 2:
        # C --> K
        temp_c = float(input("Digite la temperatura en °C: "))
        if temp_c < CERO_ABSOLUTO:
            print("ERROR: Temperatura invalida")
            continue
        temp_k = celsius_a_kelvin(temp_c)
        print(f"{temp_c}°C = {temp_k:.2f}°K\n")
    elif opc == 3:
        print("Gracias por usarnos\n")
        break
    else:
        print("ERROR: Opcion no valida\n")
