# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:53:02 2026

@author: Soportedrai
"""

import random

PIEDRA = 1
PAPEL = 2
TIJERA = 3

def mostrar_jugada(eleccion):
    if eleccion == 1:
        return "piedra"
    elif eleccion == 2:
        return "papel"
    elif eleccion == 3:
        return "tijera"
    else:
        return "Incorrecto"

def jugar_maquina():
    """
    Especificaion
    """
    return random.randint(1, 3)
    
def mostrar_menu():
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
   
def lanzar_dado():
    """
    Especificaion
    """
    return random.randint(1, 6)

    
def definir_ganador(jugada_usuario, jugada_maquina):
    """
    Entradas: 
        - jugada_usuario: (1,2,3)
        - jugada_maquina: (1,2,3)
    Salidas:
        int (entero): 0: Usuario (W)
                      1: Maquina (W)
                      2: Empate
    """
    # Codigo
    
    return 0