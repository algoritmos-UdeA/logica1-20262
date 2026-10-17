# Error: modificar una global dentro de una funcion, sin global

ventas = 0

def registrar_venta():
    ventas = ventas + 1
    return ventas

registrar_venta()
