# -*- coding: utf-8 -*-
"""
Conversión de temperatura con menú.

Lee una temperatura en grados Celsius y la convierte a grados
Fahrenheit o a Kelvin, según la opción que elija el usuario.

Autor(es): Nombre Apellido, Nombre Apellido
Fecha: dd/mm/aaaa
Versión: 3 (agrega la especificación de cada función)
"""

############ Funciones ############
# Despliegue
def mostrar_menu():
    """
    Muestra en pantalla el menú de opciones del programa.

    Supone:
        Nada (no recibe datos).
    Garantiza:
        Imprime las tres opciones del menú. No retorna ningún valor.
    """
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a K")
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
