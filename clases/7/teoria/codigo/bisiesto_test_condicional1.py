

year = 1900

# Proceso
if(year%400 == 0):
    print("Si es bisiesto")
else:
    if(year%100 == 0):
        print("No es bisiesto")
    else:
        if(year%4 == 0):
            print("Si es bisiesto")
        else:
            print("No es bisiesto")
            