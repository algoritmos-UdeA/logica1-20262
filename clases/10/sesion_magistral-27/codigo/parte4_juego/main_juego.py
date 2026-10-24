# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 4: programa principal del juego piedra, papel o tijera.

Muestra la jugada del usuario y la de la maquina.
Todavia no dice quien gano: eso necesita definir_ganador (actividad).
"""
from funciones import mostrar_menu, jugar_maquina, obtener_nombre_jugada


def main():
    print("Piedra - Papel - Tijera")
    mostrar_menu()
    jugada_usuario = int(input("Elija una opcion: "))
    jugada_maquina = jugar_maquina()
    print(f"Usuario: {obtener_nombre_jugada(jugada_usuario)}")
    print(f"Maquina: {obtener_nombre_jugada(jugada_maquina)}")


if __name__ == "__main__":
    main()
