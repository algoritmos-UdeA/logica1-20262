cant_pares = 0
cant_impares = 0
sum_pares = 0
sum_impares = 0
i = 0 
N = int(input("Digite la cantidad de numeros a ingresar: "))
while i < N:
    # print(i)
    num = int(input(f"Ingrese el numero {i + 1}: "))
    if num%2 == 0:
        cant_pares += 1  # cant_pares = cant_pares + 1
        sum_pares += num # sum_paresd = sum_pares + num
    else:
        cant_impares += 1
        sum_impares += num
    i = i + 1
"""
print(cant_pares)
print(cant_impares)
print(sum_pares)
print(sum_impares)
"""
if cant_impares == 0:
    print("No se ingresaron pares")
if cant_pares == 0:
    print("No se ingresaron impares")
if ((cant_impares != 0) or (cant_pares != 0)):
    prom_pares = sum_pares/cant_pares
    prom_impares = sum_impares/cant_impares
    print(cant_pares, cant_impares)
    print(prom_pares, prom_impares)

