"""Pruebas de ronda.py. Se ejecutan con: python test_ronda.py"""
from reglas import PIEDRA, PAPEL, TIJERA, EMPATE, GANA_USUARIO, GANA_MAQUINA
from jugador import Jugador
from ronda import Ronda

ana = Jugador("Ana")
maquina = Jugador("Máquina")

# Resultado: uno por cada caso (los 9 casos se prueban en test_reglas.py)
r = Ronda(ana, PIEDRA, maquina, TIJERA)
assert r.get_jugada_usuario() == PIEDRA
assert r.get_jugada_maquina() == TIJERA
assert r.get_resultado() == GANA_USUARIO
assert str(r) == "Ana: piedra | Máquina: tijera | gana Ana"

r = Ronda(ana, PIEDRA, maquina, PAPEL)
assert r.get_resultado() == GANA_MAQUINA
assert str(r) == "Ana: piedra | Máquina: papel | gana Máquina"

r = Ronda(ana, TIJERA, maquina, TIJERA)
assert r.get_resultado() == EMPATE
assert str(r) == "Ana: tijera | Máquina: tijera | empate"

# Crear una ronda no le suma puntos a nadie: eso lo hace la Partida
assert ana.get_puntos() == 0 and maquina.get_puntos() == 0

print("Pruebas de ronda: todas pasaron")
