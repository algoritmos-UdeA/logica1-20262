"""
Resumen:
Este ejemplo usa un ciclo controlado por un contador. El ciclo se ejecuta un número determinado de veces, que es 
el número de estudiantes al que se le ingresará la nota.
"""
# Constantes
NOTA_MINIMA = 3.0
MINIMO_VALIDO = 0.0
MAXIMO_VALIDO = 5.0

# Inicializacion
notas_reprobadas = 0
notas_aprobadas = 0
suma_reprobadas = 0
suma_aprobadas = 0
notas_validas = 0


# Solicitud de la nota del estudiante
N = int(input('Ingrese el número de estudiantes: '))
for i in range(N):
    # Solicitud de la nota del estudiante
    nota = float(input(f'Ingrese la nota del estudiante {i+1}: '))

    # Validacion del rango de la nota
    if nota < MINIMO_VALIDO or nota > MAXIMO_VALIDO:
        print(f"ERROR: la nota {nota} esta fuera de rango, se descarta")
        continue

    # Actualizacion de las notas minima y maxima    
    if notas_validas == 0:
        nota_maxima = nota
        nota_minima = nota
    else:
        if nota > nota_maxima:
            nota_maxima = nota
        if nota < nota_minima:
            nota_minima = nota
    notas_validas += 1

    # Validadación si gano o perdio
    if nota >= NOTA_MINIMA:
        # Gano
        notas_aprobadas += 1    
        suma_aprobadas += nota  
    else:
        # Perdio
        notas_reprobadas += 1
        suma_reprobadas += nota

    
# Calculo de los totales 
suma_notas = suma_reprobadas + suma_aprobadas
total_notas = notas_reprobadas + notas_aprobadas


if total_notas == 0:
    # Caso en el que no hay estudiantes
    print("No hay estudiantes")
else:
    # Caso en el que hay estudiantes

    # Calculo de los porcentajes y promedios
    p_aprobaron = (notas_aprobadas/total_notas)*100
    p_reprobaron = (notas_reprobadas/total_notas)*100

    if notas_aprobadas == 0:
        # Caso en el que nungun estudiante gano
        prom_nota_reprobada = suma_reprobadas/notas_reprobadas
        prom_nota_aprobada = 0
    elif notas_reprobadas == 0:
        # Caso en el que nungun estudiante perdio
        prom_nota_reprobada = 0
        prom_nota_aprobada = suma_aprobadas/notas_aprobadas
    else:
        # Caso en el que hay estudiantes que ganaron y perdieron
        prom_nota_reprobada = suma_reprobadas/notas_reprobadas
        prom_nota_aprobada = suma_aprobadas/notas_aprobadas
    prom = suma_notas/total_notas
    # Salida de datos (Despliegue de los resultados)
    print(f"Porcentaje de estudiantes que aprobaron: {p_aprobaron}%")
    print(f"Porcentaje de estudiantes que reprobaron: {p_reprobaron}%")
    print(f"Promedio de notas reprobadas: {prom_nota_reprobada}")
    print(f"Promedio de notas aprobadas: {prom_nota_aprobada}")
    print(f"Promedio general de notas: {prom}")
    print(f"Nota minima: {nota_minima}")
    print(f"Nota maxima: {nota_maxima}")