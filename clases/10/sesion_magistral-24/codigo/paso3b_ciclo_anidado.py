# -*- coding: utf-8 -*-
"""
Sesion 24 - Paso 3b (complemento, NO se hizo en clase).

Igual al paso 3, pero si la temperatura no cumple el contrato se vuelve a
pedir SOLO la temperatura, con un ciclo anidado, en lugar de usar continue
(que regresa al menu y obliga a elegir la opcion otra vez).
"""

############ Constantes ############
CERO_ABSOLUTO = -273.15  # °C

############ Funciones ############
# Despliegue
def mostrar_menu():
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a °K")
    print("3. Salir")

# Conversion de temperatura
def celsius_a_fahrenheit(temp_c):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Supone:
        temp_c es un número (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en grados Fahrenheit (float).
    """
    temp_f = (9/5)*temp_c + 32
    return temp_f

def celsius_a_kelvin(temp_c):
    """
    Convierte una temperatura de grados Celsius a Kelvin.

    Supone:
        temp_c es un número (int o float) mayor o igual a -273.15
        (el cero absoluto).
    Garantiza:
        Retorna la temperatura equivalente en Kelvin (float),
        mayor o igual a 0.
    """
    temp_k = temp_c + 273.15
    return temp_k


############ Test ################

# assert condición [, "Mensaje opcional"]

# celsius_a_fahrenheit
assert celsius_a_fahrenheit(5) == 41
assert round(celsius_a_fahrenheit(1), 1) == 33.8, "El resultado es 33.8"
assert round(celsius_a_fahrenheit(1.5), 1) == 34.7, "El resultado es 34.7"
assert round(celsius_a_fahrenheit(100), 2) == 212.00
assert round(celsius_a_fahrenheit(0), 2) == 32.00
assert round(celsius_a_fahrenheit(37), 2) == 98.60
assert round(celsius_a_fahrenheit(-40), 2) == -40.00

# celsius_a_kelvin
assert round(celsius_a_kelvin(10), 2) == 283.15, "El resultado es 283.15"
assert round(celsius_a_kelvin(-20), 2) == 253.15, "El resultado es 253.15"
assert round(celsius_a_kelvin(-273.15), 2) == 0.00   # limite: cero absoluto

print("Todas las pruebas pasaron")


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
        # Ciclo anidado: se repite la lectura hasta que cumpla el contrato
        while temp_c < CERO_ABSOLUTO:
            print("ERROR: Temperatura invalida")
            temp_c = float(input("Digite la temperatura en °C: "))
        temp_f = celsius_a_fahrenheit(temp_c)
        print(f"{temp_c}°C = {temp_f:.2f}°F\n")
    elif opc == 2:
        # C --> K
        temp_c = float(input("Digite la temperatura en °C: "))
        # Ciclo anidado: se repite la lectura hasta que cumpla el contrato
        while temp_c < CERO_ABSOLUTO:
            print("ERROR: Temperatura invalida")
            temp_c = float(input("Digite la temperatura en °C: "))
        temp_k = celsius_a_kelvin(temp_c)
        print(f"{temp_c}°C = {temp_k:.2f}°K\n")
    elif opc == 3:
        print("Gracias por usarnos\n")
        break
    else:
        print("ERROR: Opcion no valida\n")
