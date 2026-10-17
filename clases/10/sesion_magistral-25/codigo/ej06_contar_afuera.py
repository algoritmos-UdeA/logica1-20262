# Recomendado: la funcion solo calcula; el programa principal cuenta

IVA = 0.19

def calcular_precio_con_iva(precio):
    precio_con_iva = precio + precio * IVA
    return precio_con_iva

# Pruebas
assert round(calcular_precio_con_iva(10000), 2) == 11900.00
assert round(calcular_precio_con_iva(0), 2) == 0.00

# Programa principal: Apu hace UNA venta
ventas = 0
precio = calcular_precio_con_iva(5000)
ventas = ventas + 1
print(f"Precio con IVA: {precio:.2f}")
print("Ventas registradas:", ventas)
