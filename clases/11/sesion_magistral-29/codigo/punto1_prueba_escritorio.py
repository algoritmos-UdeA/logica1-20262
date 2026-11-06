i = 10
a = True
j = 100
s = 0
# Prueba de escritorio
cnt_line5 = 0
cnt_line13 = 0
while(i >= 0):                         # Linea 5
    cnt_line5 += 1                     # Conteo de las veces que se mete al ciclo
    if(i >= 4 and a):
        i -= 2
        for j in range(i,0,-2):
            print(f"{j}", end = " ")
        print()
        a = (j == 0)
    elif(i >= 3):
        i -= 1                         # Linea 13
        cnt_line13 += 1                # Conteo de la linea 13 
        continue
        i -= 2
        print(i)
    elif(i >= 1):
        print(i)
        a = True
        i -= 2
    else:
        i += 12
        print("+++++")
        break
        print("-----")
    print("-----")
    s = s + (i + j)
print("Nunca llega")
print(i,j,a,s)

print("*************************************************")
print("Resultados prueba de escritorio")
print(f"Veces que se ejecuta la linea 5: {cnt_line5}")
print(f"Veces que se ejecuta la linea 13: {cnt_line13}")
print("*************************************************")
