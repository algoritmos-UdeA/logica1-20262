
# Inicializacion
num_asteriscos = 1 # Contador de asteriscos por fila


# Entradas
N = int(input("Ingrese el numero de filas: "))
num_espacios = N - 1   # Contador de espacios por fila


# Proceso y salidas
for i in range(1, N+1):
    # Espacios por fila
    for j in range(num_espacios):
        print(" ", end="")
    num_espacios -= 1
    # Asteriscos por fila
    for j in range(num_asteriscos):
        print("*", end="")      
    num_asteriscos += 2
    print()  # Nueva línea después de cada fila

