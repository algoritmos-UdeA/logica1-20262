# NO recomendado: una funcion que MODIFICA una variable global

IVA = 0.19
ventas = 0

def calcular_precio_con_iva(precio):
    global ventas
    ventas = ventas + 1
    precio_con_iva = precio + precio * IVA
    return precio_con_iva

# Pruebas
assert round(calcular_precio_con_iva(10000), 2) == 11900.00
assert round(calcular_precio_con_iva(0), 2) == 0.00

# Programa principal: Apu hace UNA venta
precio = calcular_precio_con_iva(5000)
print(f"Precio con IVA: {precio:.2f}")
print("Ventas registradas:", ventas)
