"""
Piedra, papel o tijera (versión estructurada): el programa principal.
Se ejecuta con: python main.py
"""
from reglas import (PIEDRA, PAPEL, TIJERA, GANA_USUARIO, GANA_MAQUINA,
                    es_jugada_valida, definir_ganador, jugar_maquina)
from juego import (sumar_si_gana, partida_terminada, nombre_ganador,
                   texto_ronda, texto_marcador)

RONDAS_PARA_GANAR = 3


def mostrar_menu():
    """Garantiza: imprime las jugadas posibles. No retorna nada."""
    print(PIEDRA, "Piedra")
    print(PAPEL, "Papel")
    print(TIJERA, "Tijera")


def leer_jugada():
    """Garantiza: pide una jugada hasta que sea válida y la retorna."""
    jugada = int(input("Su jugada: "))
    while not es_jugada_valida(jugada):
        print("Jugada no válida.")
        jugada = int(input("Su jugada: "))
    return jugada


def main():
    print("=== Piedra, papel o tijera ===")
    print("Gana la partida quien gane primero", RONDAS_PARA_GANAR, "rondas.")
    nombre_usuario = input("Su nombre: ")
    nombre_maquina = "Máquina"
    puntos_usuario = 0
    puntos_maquina = 0

    while not partida_terminada(puntos_usuario, puntos_maquina, RONDAS_PARA_GANAR):
        print()
        mostrar_menu()
        jugada_usuario = leer_jugada()
        jugada_maquina = jugar_maquina()
        resultado = definir_ganador(jugada_usuario, jugada_maquina)
        puntos_usuario = sumar_si_gana(puntos_usuario, resultado, GANA_USUARIO)
        puntos_maquina = sumar_si_gana(puntos_maquina, resultado, GANA_MAQUINA)
        print(texto_ronda(nombre_usuario, jugada_usuario,
                          nombre_maquina, jugada_maquina, resultado))
        print("Marcador:", texto_marcador(nombre_usuario, puntos_usuario,
                                          nombre_maquina, puntos_maquina))

    print()
    print("Ganador de la partida:", nombre_ganador(nombre_usuario, puntos_usuario,
                                                   nombre_maquina, puntos_maquina))


if __name__ == "__main__":
    main()
