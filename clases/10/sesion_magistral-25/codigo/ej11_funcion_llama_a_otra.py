# Una funcion que llama a otra: cada llamada tiene sus propias variables

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def combinaciones(n, k):
    formas = factorial(n) // (factorial(k) * factorial(n - k))
    return formas

resultado = combinaciones(5, 3)
print("Formas de elegir 3 dulces entre 5:", resultado)
