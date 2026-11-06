
# Entrada de datos
N = int(input("Ingrese el numero de filas: "))
print()  # Cambio de linea

########## Inicializacion de variables ##########
# Contadores
num_espacios1 = N - 1 # Espacios externos
num_espacios2 = 0     # Espacios internos 

######### Ciclo para la impresion de las filas #########
for i in range(N):
    # Impresion de los espacios externos
    for j in range(num_espacios1):
        print(" ", end="")
    # Impresion de la parte central de la fila
    if i == 0:
        # Primera fila
        print("*", end="") # Un asterisco
    elif i < N - 1:
        # Filas intermedias 
        print("*", end="") # Primer asterisco
        # Espacios internos
        for j in range(num_espacios2):
            print(" ", end="")
        print("*", end="") # Segundo asterisco
        num_espacios2 += 1 # Actualizacion del numero de espacios internos
    else:
        # Ultima fila con N asteriscos
        for j in range(N):
            print("*", end="")
    print()  # Cambio de linea
    num_espacios1 -= 1 # Disminucion del numero de espacios externos 

