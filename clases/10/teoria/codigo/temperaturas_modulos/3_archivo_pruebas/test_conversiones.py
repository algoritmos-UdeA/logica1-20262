"""
Pruebas del modulo conversiones.
"""
import conversiones

assert round(conversiones.celsius_a_fahrenheit(100), 2) == 212.0
assert round(conversiones.celsius_a_fahrenheit(0), 2) == 32.0
assert round(conversiones.celsius_a_kelvin(25), 2) == 298.15
assert round(conversiones.celsius_a_kelvin(-273.15), 2) == 0.0
print("Pruebas de conversiones: todas pasaron")
