# -*- coding: utf-8 -*-
"""
Sesion 26 - Parentesis (ejecutar o importar): programa principal que importa saludos.py.
"""
from saludos import hola

print("En principal.py, __name__ vale:", __name__)

if __name__ == "__main__":
    # Solo se ejecuta si se corre principal.py directamente.
    hola()
    hola()
    hola()
