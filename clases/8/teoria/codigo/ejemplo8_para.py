n0 = 0
n1 = 1

N = int(input("Ingrese la cantidad de terminos (debe ser positivo): "))

if N < 0:
    print("El número de términos debe ser positivo")
elif N == 1:
    print(n0)
elif N >= 2:
    print(n0)
    print(n1)
    for i in range(2, N):        
        n2 = n0 + n1
        print(n2)
        n0 = n1
        n1 = n2
