# -*- coding: utf-8 -*-
"""
Sesion 26 - Paso 4 (no se hizo en clase): programa principal.

El programa del paso 3 con dos mejoras:
- Organizado como se recomienda de aqui en adelante:
  imports -> constantes -> def main() -> guarda.
  El programa solo arranca si este archivo se ejecuta directamente.
- El menu tiene una opcion nueva, °K a °C, que usa kelvin_a_celsius.
"""
from conversion import celsius_a_fahrenheit, celsius_a_kelvin, kelvin_a_celsius
from pantalla import mostrar_menu

############ Constantes ############
CERO_ABSOLUTO = -273.15  # °C
CERO_ABSOLUTO_K = 0.0    # °K


############ Programa principal #########
def main():
    print("Programa de conversion de temperaturas")
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
            # K --> C
            temp_k = float(input("Digite la temperatura en °K: "))
            if temp_k < CERO_ABSOLUTO_K:
                print("ERROR: Temperatura invalida")
                continue
            temp_c = kelvin_a_celsius(temp_k)
            print(f"{temp_k}°K = {temp_c:.2f}°C\n")
        elif opc == 4:
            print("Gracias por usarnos\n")
            break
        else:
            print("ERROR: Opcion no valida\n")


if __name__ == "__main__":
    main()
