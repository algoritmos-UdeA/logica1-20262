"""Pruebas de jugador.py. Se ejecutan con: python test_jugador.py"""
from jugador import Jugador

j = Jugador("Ana")
assert j.get_nombre() == "Ana"
assert j.get_puntos() == 0                  # empieza en 0
assert str(j) == "Ana: 0"

j.sumar_punto()
j.sumar_punto()
assert j.get_puntos() == 2
assert str(j) == "Ana: 2"

# Dos jugadores son dos objetos distintos: sumarle a uno no cambia al otro
a = Jugador("Ana")
b = Jugador("Beto")
a.sumar_punto()
assert a.get_puntos() == 1 and b.get_puntos() == 0

print("Pruebas de jugador: todas pasaron")
