"""
Clase 15 - Pruebas (las mismas de la clase 14) de la clase Silla.
"""

from silla import Silla

s = Silla("B", 3)
assert s.get_fila() == "B" and s.get_numero() == 3
assert s.esta_libre()                 # empieza libre
assert str(s) == "O"

assert s.ocupar()                     # libre -> se ocupa
assert not s.esta_libre()
assert str(s) == "X"
assert not s.ocupar()                 # ya estaba ocupada

assert s.liberar()                    # ocupada -> se libera
assert s.esta_libre()
assert not s.liberar()                # ya estaba libre

print("Pruebas de Silla: todas pasaron")
