"""Pruebas de partida.py. Se ejecutan con: python test_partida.py"""
from reglas import PIEDRA, PAPEL, TIJERA, EMPATE, GANA_USUARIO, GANA_MAQUINA
from jugador import Jugador
from partida import Partida

# Partida nueva
ana = Jugador("Ana")
maquina = Jugador("Máquina")
partida = Partida(ana, maquina, 3)
assert partida.terminada() == False
assert partida.get_cantidad_rondas() == 0
assert partida.get_ultima_ronda() == None
assert str(partida) == "Ana 0 - 0 Máquina"

# Gana el usuario: suma él
assert partida.jugar_ronda(PIEDRA, TIJERA) == GANA_USUARIO
assert ana.get_puntos() == 1 and maquina.get_puntos() == 0
assert str(partida.get_ultima_ronda()) == "Ana: piedra | Máquina: tijera | gana Ana"

# Empate: no suma nadie, pero la ronda cuenta
assert partida.jugar_ronda(PAPEL, PAPEL) == EMPATE
assert ana.get_puntos() == 1 and maquina.get_puntos() == 0
assert partida.get_cantidad_rondas() == 2

# Gana la máquina: suma ella
assert partida.jugar_ronda(TIJERA, PIEDRA) == GANA_MAQUINA
assert str(partida) == "Ana 1 - 1 Máquina"
assert partida.terminada() == False

# Ana gana dos rondas más y llega a 3: termina la partida
partida.jugar_ronda(PAPEL, PIEDRA)
assert partida.terminada() == False          # 2 - 1: todavía no
partida.jugar_ronda(TIJERA, PAPEL)
assert partida.terminada() == True           # 3 - 1
assert partida.get_ganador() is ana          # el mismo objeto, no una copia
assert partida.get_cantidad_rondas() == 5
assert str(partida) == "Ana 3 - 1 Máquina"

# Partida que gana la máquina, a 1 ronda (límite)
beto = Jugador("Beto")
otra_maquina = Jugador("Máquina")
corta = Partida(beto, otra_maquina, 1)
corta.jugar_ronda(PIEDRA, PAPEL)
assert corta.terminada() == True
assert corta.get_ganador() is otra_maquina

print("Pruebas de partida: todas pasaron")
