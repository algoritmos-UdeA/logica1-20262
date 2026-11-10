"""
Piedra, papel o tijera (versión POO): el programa principal.
Se ejecuta con: python main.py
"""
from reglas import PIEDRA, PAPEL, TIJERA, es_jugada_valida, jugar_maquina
from jugador import Jugador
from partida import Partida

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
    usuario = Jugador(input("Su nombre: "))
    maquina = Jugador("Máquina")
    partida = Partida(usuario, maquina, RONDAS_PARA_GANAR)

    while not partida.terminada():
        print()
        mostrar_menu()
        jugada_usuario = leer_jugada()
        partida.jugar_ronda(jugada_usuario, jugar_maquina())
        print(partida.get_ultima_ronda())
        print("Marcador:", partida)

    print()
    print("Ganador de la partida:", partida.get_ganador().get_nombre())


if __name__ == "__main__":
    main()
