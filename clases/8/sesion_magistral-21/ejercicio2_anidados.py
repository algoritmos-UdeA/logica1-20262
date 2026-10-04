# Inicializacion

# Entradas
N = int(input("Ingrese el lado del cuadrado (numero positivo): "))

# Proceso y salidas
print()
for i in range(N):
    # Bordes inferior y superior
    if i == 0 or i == N-1:
        # Se imprimen todas las columnas
        for j in range(N):
            print("*", end="")
    else:
        # Bordes laterales
        print("*", end="") # Borde izquierdo
        for j in range(1, N-1):
            print(" ", end="")
        print("*", end="") # Borde derecho
    # Cambio de linea (proxima fila)
    print() 
