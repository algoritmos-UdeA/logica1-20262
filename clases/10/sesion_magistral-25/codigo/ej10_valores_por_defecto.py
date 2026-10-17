# Parametros con valor por defecto

def calcular_precio_final(precio, descuento=0.0, iva=0.19):
    precio_con_descuento = precio - precio * descuento
    precio_final = precio_con_descuento + precio_con_descuento * iva
    return precio_final

a = calcular_precio_final(10000)               # sin descuento, IVA general
b = calcular_precio_final(10000, 0.10)         # 10 % de descuento, IVA general
c = calcular_precio_final(10000, iva=0.05)     # sin descuento, IVA del 5 %
d = calcular_precio_final(10000, 0.10, 0.0)    # 10 % de descuento, sin IVA

print(f"a = {a:.2f}")
print(f"b = {b:.2f}")
print(f"c = {c:.2f}")
print(f"d = {d:.2f}")
