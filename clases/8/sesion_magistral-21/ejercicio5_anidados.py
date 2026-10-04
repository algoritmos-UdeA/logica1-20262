num_primo_count = 0  # Contador de primos
num = 1              # Numero a evaluar

# Entradas
N = int(input("Indique el limite superior de los numeros a visualizar: "))

# Salidas
while num_primo_count < N:     
    cnt_div = 2  # Contador de divisores
    for j in range(2,num//2 + 1):
        if (num % j == 0):
            cnt_div += 1
            break
    # Impresion del numero primo y actualizacion del contador de primos
    if (cnt_div <= 2):
        print(f"{num} ")
        num_primo_count += 1  # Actualizacion 
    num += 1 # Actualizacion del numero a evaluar  
