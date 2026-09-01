# Inicializacion

flag_negativo = 0 # Bandera (0 = positivo, 1 = negativo)

# Entrada de datos
n = int(input('Ingrese un número entero positivo: '))
num = n   # Iniciacion de la variable de control num (contador)

# Proceso y salida (Impresion de la secuencia de números enteros positivos y negativos)
while num > 0:
    # Condicional para alternar el signo
    if flag_negativo == 1:        
        print(-num, end = ' ')  # Se imprime el numero negativo
        flag_negativo = 0
    else:        
        print(num, end = ' ')   # Se imprime el numero positivo
        flag_negativo = 1      
    num = num - 1               # Actualizacion de la variable de control
