# Inicializacion


# Entradas
num_sup = int(input("Indique el limite superior de los numeros a visualizar: "))

# Salidas
for i in range(1, num_sup+1):
    # print(i)
    cnt_div = 2  # Contador de divisores
    for j in range(2,i//2 + 1):
        if (i % j == 0):
            cnt_div += 1
            break
    # Salidas
    if (cnt_div <= 2):
        print(f"{i} ")
