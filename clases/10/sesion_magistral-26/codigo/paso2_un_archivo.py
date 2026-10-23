# -*- coding: utf-8 -*-
"""
Sesion 26 - Paso 2: el programa completo en un solo archivo.

Conversion de temperatura con menu: °C a °F y °C a °K.
- Los stubs del paso 1 se reemplazan por el calculo real, y todas
  las pruebas pasan.
- El archivo tiene cuatro zonas: constantes, funciones, pruebas y
  programa principal. En el paso 3, cada zona se lleva a otro archivo.
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
    return temp_c + 273.15


############ Test ################

# assert condición [, "Mensaje opcional"]

# celsius_a_fahrenheit
assert celsius_a_fahrenheit(5) == 41                                          # tipico
assert round(celsius_a_fahrenheit(1), 1) == 33.8, "El resultado es 33.8"      # tipico
assert round(celsius_a_fahrenheit(1.5), 1) == 34.7, "El resultado es 34.7"    # tipico (dato decimal)
assert round(celsius_a_fahrenheit(100), 2) == 212.00                          # tipico (ebullicion)
assert round(celsius_a_fahrenheit(0), 2) == 32.00                             # tipico (congelacion)
assert round(celsius_a_fahrenheit(37), 2) == 98.60                            # tipico (temperatura corporal)
assert round(celsius_a_fahrenheit(-40), 2) == -40.00                          # especial (las escalas coinciden)

# celsius_a_kelvin
assert round(celsius_a_kelvin(10), 2) == 283.15, "El resultado es 283.15"     # tipico
assert round(celsius_a_kelvin(-20), 2) == 253.15, "El resultado es 253.15"    # tipico (negativa)
assert round(celsius_a_kelvin(-273.15), 2) == 0.00                            # limite (cero absoluto)

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
