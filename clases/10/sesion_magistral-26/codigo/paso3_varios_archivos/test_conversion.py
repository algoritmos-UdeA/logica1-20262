# -*- coding: utf-8 -*-
"""
Sesion 26 - Paso 3: pruebas del modulo conversion.

Ejecute este archivo para revisar las funciones de conversion.py.
"""
from conversion import celsius_a_fahrenheit, celsius_a_kelvin, kelvin_a_celsius

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

# kelvin_a_celsius
assert round(kelvin_a_celsius(500), 2) == 226.85                              # tipico
assert round(kelvin_a_celsius(3.15), 2) == -270.00                            # tipico (dato decimal)
assert round(kelvin_a_celsius(0), 2) == -273.15, "El resultado es -273.15"    # limite (cero absoluto)

print("Pruebas de conversion: todas pasaron")
