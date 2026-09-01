# Inicializacion

flag_negativo = False # Bandera (False = positivo, True = negativo)

# Entrada de datos
n = int(input('Ingrese un número entero positivo: '))
num = n   # Iniciacion de la variable de control num (contador)

# Proceso y salida (Impresion de la secuencia de números enteros positivos y negativos)
while num > 0:
    # Condicional para alternar el signo
    if flag_negativo == True:        
        print(-num, end = ' ')  # Se imprime el numero negativo
    else:        
        print(num, end = ' ')   # Se imprime el numero positivo

    flag_negativo = not(flag_negativo)  # Alternar el valor de la bandera
    num = num - 1                       # Actualizacion de la variable de control
