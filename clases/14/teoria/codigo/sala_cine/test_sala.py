"""
Clase 14 - Pruebas de la clase Sala.
"""

from sala import Sala

sala = Sala(3, 4, 5000)               # filas A, B, C con sillas 1 a 4
assert sala.contar_libres() == 12

# Las dos formas de contar: letra y numero desde 1 -> indices desde 0
assert sala.indice_fila("A") == 0
assert sala.indice_fila("C") == 2
assert sala.indice_fila("D") == -1    # la sala no tiene fila D
assert sala.get_silla("C", 4).get_fila() == "C"
assert sala.get_silla("C", 4).get_numero() == 4

# Silla valida
assert sala.es_silla_valida("A", 1)
assert not sala.es_silla_valida("A", 0)
assert not sala.es_silla_valida("A", 5)
assert not sala.es_silla_valida("Z", 1)

# Vender
assert sala.vender("B", 2)
assert not sala.vender("B", 2)        # ya vendida
assert not sala.vender("D", 1)        # no existe
assert sala.contar_libres_fila("B") == 3
assert sala.contar_libres() == 11
assert sala.get_recaudo() == 5000

# Liberar
assert sala.liberar("B", 2)
assert not sala.liberar("B", 2)       # ya estaba libre
assert sala.get_recaudo() == 0

# Mapa
sala.vender("A", 1)
sala.vender("C", 4)
assert str(sala) == "   1 2 3 4\nA  X O O O\nB  O O O O\nC  O O O X"

print("Pruebas de Sala: todas pasaron")
