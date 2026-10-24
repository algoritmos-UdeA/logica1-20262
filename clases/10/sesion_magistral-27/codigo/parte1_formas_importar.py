# -*- coding: utf-8 -*-
"""
Sesion 27 - Parte 1: formas de importar una funcion de un modulo.

Las tres formas usan la misma funcion, math.sqrt; cambia como se escribe
la llamada. La forma "from math import *" no se recomienda y no se usa aqui.
"""

# Forma 1 (recomendada): se importa el modulo y se usa el prefijo math.
import math
print(math.sqrt(16))

# Forma 2: se importan solo las funciones que se van a usar, sin prefijo
from math import sqrt, pi
print(sqrt(16), pi)

# Forma 3: el modulo con un nombre mas corto
import math as m
print(m.sqrt(16))
