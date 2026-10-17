# Una funcion puede LEER una constante global

IVA = 0.19    # constante global: en MAYUSCULA, su valor nunca cambia

def calcular_precio_con_iva(precio):
    precio_con_iva = precio + precio * IVA
    return precio_con_iva

precio = calcular_precio_con_iva(5000)
print(f"Precio con IVA: {precio:.2f}")
