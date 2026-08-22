# Constantes: evitan numeros magicos sueltos (Numeros por que si) en el codigo
PRECIO_HOMBRE = 10000
PRECIO_MUJER = PRECIO_HOMBRE / 2   # la mitad del precio de los hombres

# Inicialización de variables
entrada = PRECIO_HOMBRE

# --- Inputs ---
sex = input('Digite el sexo (F/M): ')

# --- Process ---
if sex == 'F':
    valor_entrada = PRECIO_MUJER

# --- Outputs ---
print(f'Valor de la entrada: ${valor_entrada}')

"""
print('Valor de la entrada: $', valor_entrada, sep = '')
print('Valor de la entrada: $' + str(valor_entrada))
"""
