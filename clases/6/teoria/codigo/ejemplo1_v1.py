# Constantes: evitan numeros magicos sueltos (Numeros por que si) en el codigo
PRECIO_HOMBRE = 10000
PRECIO_MUJER = PRECIO_HOMBRE / 2   # la mitad del precio de los hombres

# Inicialización de variables
entrada = PRECIO_HOMBRE

# --- Inputs ---
sex = input('Digite el sexo (F/M): ')

# --- Process ---
if sex == 'F' or sex == 'f':
    entrada = PRECIO_MUJER
else:
    entrada = PRECIO_HOMBRE
    
# --- Outputs ---
print(f'Valor de la entrada: ${entrada}')
