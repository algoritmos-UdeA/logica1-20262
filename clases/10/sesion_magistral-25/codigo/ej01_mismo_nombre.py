# Ambito: dos variables con el mismo nombre en ambitos distintos

def aplicar_descuento(precio):
    descuento = 0.10
    precio = precio - precio * descuento
    print("Dentro de la funcion: precio =", precio, "y descuento =", descuento)
    return precio

precio = 5000
descuento = 0.50
precio_final = aplicar_descuento(precio)
print("precio_final =", precio_final)
print("precio =", precio)
print("descuento =", descuento)
