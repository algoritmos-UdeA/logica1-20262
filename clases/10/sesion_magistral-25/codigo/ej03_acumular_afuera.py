# Solucion: la funcion calcula y el programa principal acumula

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

total = 0
total = total + calcular_subtotal(2000, 1)    # un chocolate
total = total + calcular_subtotal(1500, 2)    # dos gaseosas
total = total + calcular_subtotal(800, 3)     # tres chicles
print("Total a pagar:", total)
