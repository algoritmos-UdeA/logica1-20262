# -*- coding: utf-8 -*-
"""
Sesion 24 - Paso 1: pruebas con assert.

Conversion de temperatura con menu: °C a °F y °C a °K.
Las pruebas con print del paso 0 se reemplazan por pruebas con assert.
Los nombres todavia no siguen las buenas practicas (eso llega en el paso 3).
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

# assert condición [, "Mensaje opcional"]

# c_to_f
assert c_to_f(5) == 41                                          # tipico
assert round(c_to_f(1), 1) == 33.8, "El resultado es 33.8"      # tipico
assert round(c_to_f(1.5), 1) == 34.7, "El resultado es 34.7"    # tipico (dato decimal)
assert round(c_to_f(100), 2) == 212.00                          # tipico (ebullicion)
assert round(c_to_f(0), 2) == 32.00                             # tipico (congelacion)
assert round(c_to_f(37), 2) == 98.60                            # tipico (temperatura corporal)
assert round(c_to_f(-40), 2) == -40.00                          # especial (las escalas coinciden)

# c_to_k
assert round(c_to_k(10), 2) == 283.15, "El resultado es 283.15"   # tipico
assert round(c_to_k(-20), 2) == 253.15, "El resultado es 253.15"  # tipico (negativa)

print("Todas las pruebas pasaron")


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
