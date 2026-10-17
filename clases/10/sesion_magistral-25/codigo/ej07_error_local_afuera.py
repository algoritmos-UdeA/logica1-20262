# Error: usar afuera una variable local

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

calcular_subtotal(1500, 2)      # el resultado no se guarda
print(subtotal)
