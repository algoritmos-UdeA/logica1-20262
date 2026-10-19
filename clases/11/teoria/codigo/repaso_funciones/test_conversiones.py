# -*- coding: utf-8 -*-
"""
Pruebas del modulo conversiones.

Ejecutar con: python test_conversiones.py
"""

import conversiones

assert round(conversiones.celsius_a_fahrenheit(100), 2) == 212.0   # tipico: ebullicion
assert round(conversiones.celsius_a_fahrenheit(0), 2) == 32.0      # tipico: congelacion
assert round(conversiones.celsius_a_fahrenheit(-40), 2) == -40.0   # especial: las escalas coinciden

print("Pruebas de conversiones: todas pasaron")
