

year = 1900

# Proceso y salida
if((year%4 == 0) and (year%100 != 0) or (year%400 == 0)):
    print("Si es bisiesto")
else:
    print("No es bisiesto")
