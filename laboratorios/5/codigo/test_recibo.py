"""
Punto de chequeo 3: pruebas de la clase Recibo.
Se ejecutan con: python test_recibo.py

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.
"""
from vehiculo import Vehiculo
from recibo import Recibo

carro = Vehiculo("ABC123", Vehiculo.CARRO)
moto = Vehiculo("XYZ78A", Vehiculo.MOTO)

# Las tarifas por hora
assert Recibo.TARIFA_CARRO == 3000
assert Recibo.TARIFA_MOTO == 1000

# El caso calculado a mano: un carro que estuvo 130 minutos
recibo = Recibo(carro, 130)
assert recibo.get_vehiculo() is carro
assert recibo.get_minutos() == 130
assert recibo.calcular_horas() == 3             # 2 horas completas y una fracción
assert recibo.calcular_valor() == 9000          # 3 horas a $3000
assert str(recibo) == "ABC123 (carro) | 130 min | 3 h | $9000"

# Una moto que estuvo 45 minutos paga 1 hora
recibo = Recibo(moto, 45)
assert recibo.calcular_horas() == 1
assert recibo.calcular_valor() == 1000
assert str(recibo) == "XYZ78A (moto) | 45 min | 1 h | $1000"

# calcular_horas: los límites entre una hora y la siguiente
assert Recibo(carro, 59).calcular_horas() == 1
assert Recibo(carro, 60).calcular_horas() == 1      # hora exacta: no hay fracción
assert Recibo(carro, 61).calcular_horas() == 2      # un minuto más ya es otra hora
assert Recibo(carro, 120).calcular_horas() == 2
assert Recibo(carro, 121).calcular_horas() == 3

# calcular_horas: casos especiales. Como mínimo se cobra 1 hora
assert Recibo(carro, 0).calcular_horas() == 1
assert Recibo(carro, 1).calcular_horas() == 1

# calcular_valor: el mismo tiempo vale distinto según el tipo
assert Recibo(carro, 120).calcular_valor() == 6000
assert Recibo(moto, 120).calcular_valor() == 2000
assert Recibo(moto, 0).calcular_valor() == 1000

print("Punto de chequeo 3 superado: la clase Recibo pasa todas sus pruebas")
