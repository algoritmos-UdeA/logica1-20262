"""Pruebas de estudiante.py. Se ejecutan con: python test_estudiante.py"""
from estudiante import Estudiante

# Constructor y get_
e = Estudiante("000", "Ana", 3.0)
assert e.get_id() == "000"
assert e.get_nombre() == "Ana"
assert e.get_nota() == 3.0

# set_nota: típico, límites y fuera de rango
assert e.set_nota(4.2) == True and e.get_nota() == 4.2      # típico
assert e.set_nota(0.0) == True and e.get_nota() == 0.0      # límite inferior
assert e.set_nota(5.0) == True and e.get_nota() == 5.0      # límite superior
assert e.set_nota(5.1) == False and e.get_nota() == 5.0     # fuera: no cambia
assert e.set_nota(-1.0) == False and e.get_nota() == 5.0    # fuera: no cambia

# __str__: una línea del listado
assert str(Estudiante("007", "Dario", 4.0)) == "007 \t Dario \t 4.0"

# El Id "007" es texto: no se convierte en 7
assert Estudiante("007", "Dario", 4.0).get_id() != 7

print("Pruebas de estudiante: todas pasaron")
