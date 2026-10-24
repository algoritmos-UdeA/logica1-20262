# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 3: pruebas del modulo dados.

Un resultado al azar no se puede comparar con un valor fijo.
Se prueba lo que la especificacion garantiza, de dos formas:
- el resultado siempre esta entre 1 y 6;
- con la misma semilla (random.seed), la secuencia se repite.
"""
import random
from dados import lanzar_dado

############ Test ################

# El resultado siempre esta en el rango 1..6 (se prueba muchas veces)
for i in range(1000):
    cara = lanzar_dado()
    assert 1 <= cara <= 6, "El dado debe dar un valor entre 1 y 6"

# Con la misma semilla se obtiene el mismo resultado
random.seed(10)
primer_lanzamiento = lanzar_dado()
random.seed(10)
assert lanzar_dado() == primer_lanzamiento, "La misma semilla debe repetir el resultado"

print("Pruebas de dados: todas pasaron")
