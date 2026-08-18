# 1.5 semana = 10 dias. 
# 365 / 10 = 36,5 veces al año.
PROMEDIO_AÑO = 36.5
GRAMO = 0.5
edad = int(input("Ingrese su edad : "))
uñas = (edad * PROMEDIO_AÑO)
kilos = uñas * GRAMO / 1000
print(f"""Usted ha cortado sus uñas en promedio {uñas} veces en su vida 
y ha generado el equivalente a {kilos} kilogramos de material de uñas.""")