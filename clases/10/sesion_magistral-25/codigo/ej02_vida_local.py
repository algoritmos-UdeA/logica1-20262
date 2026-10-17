# Ambito: una variable local se crea de nuevo en cada llamada

def agregar_al_total(precio, cantidad):
    total = 0                           # local: empieza en 0 en cada llamada
    total = total + precio * cantidad
    return total

agregar_al_total(2000, 1)               # un chocolate
agregar_al_total(1500, 2)               # dos gaseosas
total = agregar_al_total(800, 3)        # tres chicles
print("Total a pagar:", total)
