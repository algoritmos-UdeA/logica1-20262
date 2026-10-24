# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:09:36 2026

@author: Soportedrai
"""

from funciones import mostrar_menu, jugar_maquina, mostrar_jugada


def main():
    print("Piedra - Papel - Tijera")
    mostrar_menu()
    jug_usuario = int(input("Elija una opcion: "))
    jug_maquina = jugar_maquina()
    print(jug_usuario,jug_maquina)
    print(f"Usuario: {mostrar_jugada(jug_usuario)}")
    print(f"Maquina: {mostrar_jugada(jug_maquina)}")
    
    
    
if __name__ == "__main__":
    main()
    