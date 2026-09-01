# Inicializacion
flag_bisiesto = 0

# Entradas
year = int(input("Digite el año: "))

# Proceso
if(year%400 == 0):
    flag_bisiesto = 1
else:
    if(year%100 != 0):
        if(year%4 == 0):
            flag_bisiesto = 1
        
# Salida
if (flag_bisiesto == 1):
    print(year, "es bisiesto")
else:
    print(year, "no es bisiesto")