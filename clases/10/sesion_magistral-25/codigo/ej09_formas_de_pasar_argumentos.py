# Formas de pasar argumentos: por posicion y por nombre

def calcular_precio_final(precio, descuento, iva):
    precio_con_descuento = precio - precio * descuento
    precio_final = precio_con_descuento + precio_con_descuento * iva
    return precio_final

a = calcular_precio_final(10000, 0.10, 0.19)                       # por posicion
b = calcular_precio_final(precio=10000, descuento=0.10, iva=0.19)  # por nombre
c = calcular_precio_final(iva=0.19, precio=10000, descuento=0.10)  # por nombre, otro orden
d = calcular_precio_final(10000, descuento=0.10, iva=0.19)         # mezclados
e = calcular_precio_final(10000, 0.19, 0.10)                       # por posicion, EN DESORDEN
# f = calcular_precio_final(precio=10000, 0.10, 0.19)              # SyntaxError

print(f"a = {a:.2f}")
print(f"b = {b:.2f}")
print(f"c = {c:.2f}")
print(f"d = {d:.2f}")
print(f"e = {e:.2f}")
