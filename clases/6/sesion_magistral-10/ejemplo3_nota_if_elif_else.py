
# Constantes
NOTA_INVALIDA = 'X'

# Inicialializacion
nota_letra = NOTA_INVALIDA # Nota desconocia

# Entradas
nota_num = int(input("Digite una nota en el rango [0,100]: "))

# Proceso

if (nota_num < 0) or (nota_num > 100):
    print("ERROR: Nota fuera de rango")
    # rango [0,100]
elif (nota_num >= 90):
    # rango [90,100]
    nota_letra = 'A'
elif (nota_num >= 80):
    # rango [80,90]
    nota_letra = 'B'
elif (nota_num >= 70):
    # rango [70,80]
    nota_letra = 'C'
elif (nota_num >= 60):
    # rango [60,70]
    nota_letra = 'D'
else:
    # rango [0,60)
    nota_letra = 'E'

if nota_letra != NOTA_INVALIDA:
    print(f"{nota_num} = {nota_letra}")
    