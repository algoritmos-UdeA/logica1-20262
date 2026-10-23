# from conversion import *
from conversion import celsius_a_fahrenheit, celsius_a_kelvin, kelvin_a_celsius

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


# kelvin_a_celsius
assert round(kelvin_a_celsius(0),2) == -273.15 ,"Error"
assert round(kelvin_a_celsius(3.15),2) == -270
assert round(kelvin_a_celsius(500),2) == 226.85

print("En hora buena, todas las pruebas pasaron")



print("Todos los test pasaron")