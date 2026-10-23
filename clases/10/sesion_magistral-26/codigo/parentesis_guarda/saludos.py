# -*- coding: utf-8 -*-
"""
Sesion 26 - Parentesis (ejecutar o importar): modulo saludos.

Ejecute este archivo directamente y luego ejecute principal.py.
Compare lo que aparece en pantalla en cada caso.
"""

def hola():
    print("hola que mas!!!")


print("En saludos.py, __name__ vale:", __name__)

if __name__ == "__main__":
    # Solo se ejecuta si se corre saludos.py directamente,
    # no cuando otro archivo lo importa. Aqui van las pruebas del modulo.
    print("Pruebas de saludos")
