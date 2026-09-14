"""
Resumen:
Este ejemplo permite encontrar el cero de una lista de numeros. Emplea un ciclo controlado por un contador y una bandera. 
Cuando se ingresa el valor buscado, la bandera se activa y el ciclo se rompe. Al final se despliega la posición en la que 
se encontró el valor buscado.
"""

# Constantes
VALOR_BUSCADO = 0

# Inicializacion de variables
encontrado = False
i = 0

# Solicitud la cantidad de numeros a ingresar
N = int(input('Ingrese el número de números: '))
while ((i < N) and (not(encontrado))):
    i += 1   # i = i + 1
    num = int(input(f'Ingrese el número {i}: '))
    # Validación si es el value buscado
    if num == VALOR_BUSCADO:
        encontrado = True        
   
# Despliegue de resultados
if encontrado:
    # Valor encontrado
    print(str(VALOR_BUSCADO) + " encontrado en la posición " + str(i))
else:
    # Valor no encontrado
    print(str(VALOR_BUSCADO) + " no encontrado")
