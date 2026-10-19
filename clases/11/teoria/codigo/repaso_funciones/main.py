# -*- coding: utf-8 -*-
"""
Programa principal: convierte una temperatura de °C a °F.

Ejecutar con: python main.py
"""

import conversiones


def main():
    temp_c = float(input("Ingrese los °C: "))
    temp_f = conversiones.celsius_a_fahrenheit(temp_c)
    print(f"{temp_c} °C = {temp_f:.2f} °F")


if __name__ == "__main__":
    main()
