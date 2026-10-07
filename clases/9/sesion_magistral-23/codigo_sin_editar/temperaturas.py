# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

############ Funciones ############
# Despliegue
def menu():
    print("--------------------------------")
    print("1. °C a °F")
    print("2. °C a °K")
    print("3. Salir")

# Conversion de temperatura
def c_to_f(c):
    f = (9/5)*c + 32
    return f

def c_to_k(c):
    k = c + 273.15
    return k

############ Test ################

"""
# Test de c_to_f
T1 = c_to_f(5) # c = 5
T1c = 1
T2 = c_to_f(T1c) # c = 5
print(f"T1 = 5°C = {T1}°F")
print(f"T2 = {T1c}°C = {T2}°F")

# Test de c_to_k
T1k = c_to_k(10)
# 2. T2c = -20
T2c = -20 # -10 - 10
T2k = c_to_k(T2c)
# Despliegue de rtesultados
print(f"T1c = 10°C = {T1k}°F")
print(f"T2c = {T2c}°C = {T2k:.2f}°F")
"""

############ Programa principal #########
print("Programa de conversion de °C a °F y °K")
while True:
    # Menu
    menu()
    # Entrada de datos
    opc = int(input("\nElija una opcion: "))
    # Seleccion
    if opc == 1:
        # C --> F
        Tc = float(input("Digite la temperatura en °C: "))
        Tf = c_to_f(Tc)
        print(f"{Tc}°C = {Tf:.2f}°F\n")
    elif opc == 2:
        # C --> K
        Tc = float(input("Digite la temperatura en °C: "))
        Tk = c_to_k(Tc)
        print(f"{Tc}°C = {Tk:.2f}°K\n")
    elif opc == 3:
        print("Gracias por usarnos\n")
        break
    else:
        print("ERROR: Opcion no valida\n")
    
    



