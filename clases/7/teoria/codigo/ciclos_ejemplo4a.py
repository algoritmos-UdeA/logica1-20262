# Inicializacion

flag_negativo = 0 # Bandera (0 = positivo, 1 = negativo)

# Entrada de datos
n = int(input('Ingrese un número entero positivo: '))
i = n   # Iniciacion de la variable de control i (contador)

# Proceso y salida (Impresion de la secuencia de números enteros positivos y negativos)
while i > 0:
    # Condicional para alternar el signo
    if flag_negativo == 1:
        # Numero negativo
        num = -i
        flag_negativo = 0
    else:
        # Numero positivo
        num = i
        flag_negativo = 1
    print(num, end = ' ') # Se imprime el numero
    i = i - 1  # Actualizacion de la variable de control
